#coding=utf-8
#author='Shichao-Dong'


import report
import xlsxwriter


def Report():
    workbook = xlsxwriter.Workbook('D:/file/android.xlsx')
    bo = report.GenerateReport(workbook)
    bo.writedata()
    bo.close()


if __name__ == "__main__":
    Report()