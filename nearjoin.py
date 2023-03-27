import numpy
import pandas as pd
import statistics
import self as self
import train as train

file = open(r'C:\Users\86178\Downloads\archive (4)\a.csv')
# 读取指定目录下的csv格式的文件
file_data=pd.read_csv(file, low_memory=False)
file_data

file_data=file_data.interpolate(kind='nearest')
for title in file_data.columns.values:
    if title=="Unnamed: 0":
        continue
    elif file_data[title].dtype == "int64" or file_data[title].dtype == "float64":
      print("ok")
