import pandas as pd
import matplotlib.pyplot as plt


file = open(r'C:\Users\86178\Downloads\archive (4)\a.csv')
# 读取指定目录下的csv格式的文件
titanic=pd.read_csv(file, low_memory=False)
# 读取Titanic数据集

# 检查年龄是否有缺失
any(titanic.Data_Value.isnull())
# 不妨删除含有缺失年龄的观察
titanic.dropna(subset=['Data_Value'], inplace=True)

# 设置图片大小
plt.figure(figsize=(10,8))

# 设置图形的显示风格
plt.style.use('ggplot')

# 设置中文和负号正常显示
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘图：整体乘客的年龄箱线图
plt.boxplot(x = titanic.Data_Value, # 指定绘图数据
            patch_artist  = True, # 要求用自定义颜色填充盒形图，默认白色填充
            showmeans = True, # 以点的形式显示均值
            widths = 0.2,
            boxprops = {'color':'black','facecolor':'#9999ff'}, # 设置箱体属性，填充色和边框色
            flierprops = {'marker':'o','markerfacecolor':'red','color':'black'}, # 设置异常值属性，点的形状、填充色和边框色
            meanprops = {'marker':'D','markerfacecolor':'indianred'}, # 设置均值点的属性，点的形状、填充色
            medianprops = {'linestyle':'--','color':'orange'}) # 设置中位数线的属性，线的类型和颜色
# 设置y轴的范围
plt.ylim(0,85)

# 去除箱线图的上边框与右边框的刻度标签
plt.tick_params(top='off', right='off')

# 显示图形
plt.show()