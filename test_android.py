#coding=utf-8
#author='Shichao-Dong'

import os,platform
import subprocess
import re

# subprocess.Popen("adb shell input keyevent  3")

# 获取devices
result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
# print len(result),result[1].split()[0]
dev = result[1].split()[0]
if len(result)-2 == 1:
    print dev
else:
    print 'No device found'



command = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe")
print command
cmd = "adb %s" %('get-state')
print cmd
print os.popen(cmd).read()

pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")
package = subprocess.Popen("adb shell dumpsys activity | findstr  mFocusedActivity", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
print package
packagename = pattern.findall(package)[0].split('/')[0]
print pattern.findall(package)[0].split('/')[0]
print pattern.findall(package)[0].split('/')[1]

#获取mem占用情况
men_list=[]
cmd = 'adb -s '+ dev + ' shell dumpsys meminfo ' + packagename
print cmd
men_s = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
for info in men_s:
    if len(info.split())>0 and info.split()[0].decode() == "TOTAL":
        men_list.append(int(info.split()[1].decode()))

print men_list

#获取cpu
cpu_list=[]
cmd = 'adb -s '+dev + ' shell top -n 1| findstr ' + packagename
print cmd
top_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
print top_info
if len(top_info)>=1:
    cpu_list.append(int(top_info[0].split()[2][0:-1]))

print cpu_list

#获取pid和uid
cmd = 'adb -s '+ dev +' shell ps |findstr ' + packagename
print cmd
pid_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
if len(pid_info)>=1:
    pid = pid_info[0].split()[1]
print 'pid为:' + pid

cmd ='adb -s '+ dev +' shell cat  /proc/'+ pid + '/status'
print cmd
uid_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
if len(uid_info)>= 1:
    uid = uid_info[6].split()[1]
print 'uid为:'+uid


#获取流量
receive = []
send = []
cmd = 'adb -s '+ dev +' shell cat /proc/net/xt_qtaguid/stats | findstr '+ uid
print cmd
flow_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
if len(flow_info)>= 1:
    for flow in flow_info:
        down = 0
        up = 0
        down =down + int(flow.split()[5])
        up = up+ int(flow.split()[7])
    receive.append(down)
    send.append(up)
print receive,send

#电量



# #获取fps
# fps = []
# cmd = 'adb shell dumpsys gfxinfo '+ packagename
# results = os.popen(cmd).read().strip()
# frames = [x for x in results.split('\n') if validator(x)]
# frame_count = len(frames)
# jank_count = 0
# vsync_overtime = 0
# render_time = 0
# for frame in frames:
#     time_block = re.split(r'\s+', frame.strip())
#     if len(time_block) == 3:
#         try:
#             render_time = float(time_block[0]) + float(time_block[1]) + float(time_block[2])
#         except Exception as e:
#             render_time = 0
#
#
#     if render_time > 16.67:
#         jank_count += 1
#         if render_time % 16.67 == 0:
#             vsync_overtime += int(render_time / 16.67) - 1
#         else:
#             vsync_overtime += int(render_time / 16.67)
#
# _fps = int(frame_count * 60 / (frame_count + vsync_overtime))
# fps.append(_fps)
# # return (frame_count, jank_count, fps)
#
# print(fps)

