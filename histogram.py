import numpy as np
from matplotlib import pyplot as plt
import numpy
import pandas as pd
import statistics
import self as self
import train as train
import matplotlib.pyplot as plt
def draw_histogram2(arr):
    nums, bins, patches = plt.hist(arr, bins=20, edgecolor='k', density=True)
    plt.xticks(bins, bins)
    for num, bin in zip(nums, bins):
        plt.annotate("%.4f" % num, xy=(bin, num), xytext=(bin + 0.2, num + 0.0005))
    plt.show()

def draw_histogram1(arr):
    nums, bins, patches = plt.hist(arr, bins="auto", edgecolor='k', density=True)
    plt.xticks(bins, bins)
    for num, bin in zip(nums, bins):
        plt.annotate("%.4f" % num, xy=(bin, num), xytext=(bin + 0.2, num + 0.0005))

def draw_histogram(arr):
    plt.hist(arr)
    plt.show()

file = open(r'C:\Users\86178\Downloads\archive (4)\a.csv')
# 读取指定目录下的csv格式的文件
file_data=pd.read_csv(file, low_memory=False)
file_data
for title in file_data.columns.values:
    if title=="Unnamed: 0":
        continue
    if file_data[title].dtype == "int64" or file_data[title].dtype == "float64":
        draw_histogram2(file_data[title])
    else:
        draw_histogram(file_data[title])