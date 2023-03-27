# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import numpy
import pandas as pd
import statistics
import self as self
import train as train

file = open(r'C:\Users\86178\Downloads\archive (4)\a.csv')
# 读取指定目录下的csv格式的文件
file_data=pd.read_csv(file, low_memory=False)
file_data
for title in file_data.columns.values:
    if title=="Unnamed: 0":
        continue
    if file_data[title].dtype == "int64" or file_data[title].dtype == "float64":
        a = max(file_data[title])
        b = min(file_data[title])
        c = sum(file_data[title]) / len(file_data[title])
        col_null = file_data[title].isnull().sum(axis=0)
        print("中位数是", statistics.median(file_data[title]))
        print('四分数是', numpy.percentile(file_data[title], (25)), numpy.percentile(file_data[title], (50)), numpy.percentile(file_data[title], (75)))
        print("最大值是", a, sep="")
        print("最小值是", b, sep="")
        print("平均值是", c, sep="")
        print("缺失值的总数", col_null)
    else:
        vc = file_data[title].value_counts()
        print(vc)

