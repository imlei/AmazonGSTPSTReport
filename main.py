#对Amazon的GST和PST的信息进行汇总合并，并生成报表。
#自动读取目录的文件，并转换成Xlsx文件，此外输出最终的结果

import os
import csv
import numpy as np
import pandas as pd
import openpyxl

#filename = os.path.abspath('.')
#print(filename)
#print(os.path.abspath("__file__"))
#print(os.path.abspath(filename))
#参数设置
#设置转为为Excel的文件名
set_excel_file = "taxreport.xlsx"


#csv 转换成excel文件的模块
def csvtoxlsx(self):
    csv = pd.read_csv(self,encoding='utf-8')
    csv.to_excel(set_excel_file,sheet_name='Sheet1')

#设置当前目录
filePath = r"D:\test\taxfile"
os.chdir(filePath)
print("文件夹的地址")
print(filePath)
#遍历设置好的目录，并且找到CSV文件
print("开始遍历")
filecsv = []
for root, dirs, files in os.walk(filePath):
   print(root)
   print(dirs)
   print(files)
   #cvs to excel,取得文件名
   for file in files:
       if file.endswith(".csv"):
           filecsv.append(file)
   print(filecsv)
for csv_file in filecsv:
    
    print(csv_file)
    excelfile = csvtoxlsx(csv_file)

#读取和操作Excel的文件
df = pd.read_excel(set_excel_file)
taxreport = pd.pivot_table(df, values=["Tax_Amount","Taxable_Amount"], index="Tax_Type", aggfunc="sum", margins=True, margins_name="Total")
taxreport.to_excel("taxsum.xlsx")
