#coding=utf-8
#author='Shichao-Dong'


import os,platform
import subprocess
import re
import exceptions


serialno_num=''

#判断系统类型，windows使用findstr，linux使用grep
system = platform.system()
if system is "Windows":
    find_util = "findstr"
else:
    find_util = "grep"

#判断是否设置环境变量ANDROID_HOME
if "ANDROID_HOME" in os.environ:
    if system == "Windows":
        command = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe")
    else:
        command = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb")
else:
    raise EnvironmentError(
        "Adb not found in $ANDROID_HOME path: %s." %os.environ["ANDROID_HOME"])

#获取手机
def get_devices():
    devices=[]
    result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    for line in result[1:]:
        if 'device' in line.strip():
            devices.append(line.split()[0])
        else:
            break
    return devices


#adb命令
def adb(args):
    # global serialno_num
    # if serialno_num == "":
    #     devices = get_devices()
    #     if len(devices) == 1:
    #         serialno_num = devices[0]
    #     else:
    #         raise EnvironmentError("more than 1 device")
    cmd = "adb %s" %(str(args))
    return os.popen(cmd)

#adb shell命令
def shell(args):
    # global serialno_num
    # if serialno_num == "":
    #     devices = get_devices()
    #     serialno_num = devices[0]

    cmd = "adb shell %s" %( str(args))
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def get_current_packagename():
    #正则匹配出package和activity
    pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")
    package = shell("dumpsys activity | findstr  mFocusedActivity").stdout.read()
    print pattern.findall(package)[0].split('/')[0]
    return pattern.findall(package)[0].split('/')[0]

def get_current_activity():
    #正则匹配出package和activity
    pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")
    package = shell("dumpsys activity | findstr  mFocusedActivity").stdout.read()
    print pattern.findall(package)[0].split('/')[-1]
    return pattern.findall(package)[0].split('/')[-1]



if __name__ == "__main__":
    get_current_activity()
    get_current_packagename()