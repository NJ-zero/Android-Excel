#! python2
#coding=utf-8
#author='Shichao-Dong'

import sys,os
import xlsxwriter
reload(sys)
sys.path.append('D:\Ptest\AndroidScripts')
from public import publicfunction as util

PATH = lambda p: os.path.abspath(p)

#获取当前应用包名
package_name = util.get_current_packagename()
print u'本次测试APP为:'+ package_name

#定义top次数
times=20

#获取men cpu 占用情况
def top():
    cpu = []
    mem = []
    print 'Starting get mem cpu information...'
    top_info = util.shell("top -n %s | findstr %s$" %(str(times), package_name)).stdout.readlines()
    for info in top_info:
        temp_list = info.split()
        #print temp_list[2]
        cpu.append(int(temp_list[2][0:-1]))
        #print temp_list[6]
        mem.append(int(temp_list[6][0:-1]))
    print cpu,mem
    return (cpu,mem)


#获取devices用作表格sheet
def devices():
    devices=util.get_devices()
    print '设备号为:' + devices[0]
    return devices[0]


#获取pid
def get_pid():
    pid_info = util.shell("ps| findstr %s$" %package_name).stdout.readlines()
    pid = pid_info[0].split()[1]
    print 'pid为:' + pid
    return str(pid)

#获取uid
def get_uid():
    cmd = 'cat  /proc/'+ get_pid() + '/status'
    uid_info = util.shell(cmd).stdout.readlines()
    uid = uid_info[6].split()[1]
    print 'uid为:'+uid
    return str(uid)


#上传流量
def get_flow_send():
    cmd = '"cat proc/net/xt_qtaguid/stats|grep '+'%s"'%get_uid()
    print cmd
    flow = util.shell(cmd).stdout.readlines()
    print flow







if __name__ == "__main__":
    print "Starting get top information..."
    get_flow_send()