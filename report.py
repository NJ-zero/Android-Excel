#coding=utf-8
#author='Shichao-Dong'

import sys,os
import xlsxwriter
reload(sys)
sys.path.append('E:\TestAndroid')
from script import get_cpu_mem_info as info

class GenerateReport :
    def __init__(self, wd):
        self.wd = wd

    def writedata(self):
        format1 = self.wd.add_format({'bold':True,'align':'center','valign':'vcenter','border':1})
        sheet = str(info.devices())
        worksheet = self.wd.add_worksheet(sheet)
        worksheet.write('A1','cpu',format1)
        worksheet.write('B1','mem',format1)

        #写mem cpu信息到表格中
        mem,cpu=info.top()
        for i in range(len(mem)):
            worksheet.write(i+1,0,mem[i],format1)

        for i in range(len(mem)):
            worksheet.write(i+1,1,cpu[i],format1)

        self.chart(worksheet,sheet,'cpu',len(cpu))
        self.chart(worksheet,sheet,'mem',len(mem))


    def chart(self,worksheet,sheet,type,lenData):
        '''
        :param worksheet: 固定apiworksheet.insert_chart
        :param sheet: 插入表格用，取values
        :param type: 识别cpu还是mem后续可以继续加
        :param lenData: 数组长度
        :return:
        '''

        if type == 'cpu':
            values = "="+sheet+"!$A$2:$A$" + str(lenData + 1)
            row = 'D3'
            title = u'cpu使用率'
        elif type == 'mem':
            values = "="+sheet+"!$B$2:$B$" + str(lenData + 1)
            row = 'D20'
            title = u'mem占用率'

        chart1 = self.wd.add_chart({'type': 'line'})
        chart1.add_series({
            'values': values,
            'name':title,
        })
        chart1.set_title({'name': title})
        worksheet.insert_chart(row, chart1)

    def close(self):
        self.wd.close()
