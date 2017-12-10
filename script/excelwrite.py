#coding=utf-8
#author='Shichao-Dong'

import sys,os
import datetime
import xlsxwriter
reload(sys)
import get_cpu_mem_info as info



def chart_cpu(name,lenData):
    values= '=' + name + "!$A$1:$A$" + str(lenData + 1)
    row = 'A' + str(lenData)
    title = 'cpu占用率'



def workbook(filename,sheet):
    workbook = xlsxwriter.Workbook(filename)
    worksheet=workbook.add_worksheet(sheet)
    #定义格式
    format1=workbook.add_format({'bold':True,'align':'center','valign':'vcenter','border':1})

    worksheet.set_column("A:B",15)
    worksheet.write('A1','cpu(%)',format1)
    worksheet.write('B1','mem(k)',format1)
    #写mem cpu信息到表格中
    mem,cpu=info.top()
    for i in range(len(mem)):
        worksheet.write(i+1,0,mem[i],format1)

    for i in range(len(mem)):
        worksheet.write(i+1,1,cpu[i],format1)


    values = "="+sheet+"!$A$2:$A$" + str(len(mem) + 1)
    print values
    row = 'D3'
    title = u'cpu使用率'

    chart1 = workbook.add_chart({'type': 'line'})
    chart1.add_series({
            'values': values,
            'name':title,
        })
    chart1.set_title({'name': title})
    worksheet.insert_chart(row, chart1)

    values = "="+sheet+"!$B$2:$B$" + str(len(mem) + 1)
    print values
    row = 'D20'
    title = u'mem占用'

    chart1 = workbook.add_chart({'type': 'line'})
    chart1.add_series({
            'values': values,
            'name':title,
        })
    chart1.set_title({'name': title})
    worksheet.insert_chart(row, chart1)



    return workbook




if __name__ == "__main__":
    workbook('D:/file/android.xlsx',sheet = str(info.devices()))