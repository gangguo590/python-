from cProfile import label

import matplotlib.pyplot as plt  # 导入 Matplotlib 的绘图模块
import numpy as np  # 导入 NumPy 库

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']  # 设置中文字体优先级
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示成方块的问题

#使用matlab方式绘图                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
#fig1 = plt.figure()  # 创建一个新的图形对象
x = [1, 2, 3, 4, 5]  # 定义 x 轴数据
y = [1, 4, 9, 16, 25]  # 定义 y 轴数据
y1 = [10, 44, 19, 66, 35]  # 定义 y 轴数据
y2 = [23, 89, 56, 45, 26]
y3 = [12, 23, 8, 89, 25]
y4 = [34, 56, 78, 12, 45]
#plt.plot(x, y)
#fig1.savefig('python.svg')  # 保存为 SVG 格式
#plt.show()  # 再显示
#一幅图的在一个代码块中完成
fig2 = plt.figure()  # 创建一个新的图形对象
#x = [1, 2, 3, 4, 5]  # 定义 x 轴数据
#plt.plot(x, y, x, y1, x, y2)  # 绘制多线图
#plt.show()  # 显示图形

#绘制多子图
#plt.subplot(3, 1, 1), plt.plot(x, y)  # 绘制第一个子图,参数说明：3行2列的第1个子图
#plt.subplot(3, 1, 2), plt.plot(x, y1)  # 绘制第二个子图
#plt.subplot(3, 1, 3), plt.plot(x, y2)   # 绘制第三个子图
#plt.show()  # 显示图形

#图表类型
#二维图
plt.plot(x, y, color='#7DEEEE', linestyle='-', linewidth=2, marker='o')     #设置颜色
plt.plot(x, y1, color='#4EF69C', linestyle='--', linewidth=2.5, marker='s')   #设置线条样式
plt.plot(x, y2, color='#F6F64E', linestyle='-.', linewidth=1, marker='^')   #设置线条宽度
plt.plot(x, y3, color='#F6644E', linestyle=':', linewidth=1.5, marker='d')   #设置标记样式
plt.plot(x, y4, color='#F6644E', linestyle=' ', linewidth=1.5, marker='x')   #' '表示隐藏线条，可以用来绘制散点图
plt.show()  # 显示图形

#网格图
a = np.linspace(0, 10, 100)  # 生成从0到10的100个等间距的数
b = np.sin(a)*np.cos(a).reshape(-1, 1)  # 计算正弦和余弦的乘积，并调整形状以适应网格图
plt.figure()  # 创建一个新的图形对象
plt.imshow(b)   # 绘制网格图，默认使用颜色映射来表示数值大小
plt.colorbar()  # 显示颜色条，表示数值与颜色的对应关系
plt.show()  # 显示图形

#统计图
data = np.random.randn(10000)  # 生成10000个随机数，服从标准正态分布
data1 = np.random.normal(3, 1, 10000)  # 生成10000个随机数，服从均值为3，标准差为1的正态分布
data2 = np.random.normal(-3, 1, 10000)  # 生成10000个随机数，服从均值为-3，标准差为1的正态分布
plt.figure()  # 创建一个新的图形对象
plt.hist(data, bins=30, color='#7DEEEE', edgecolor='black', alpha=0.7)  # 绘制直方图，设置颜色和边框颜色
plt.hist(data1, bins=30, color='#4EF69C', edgecolor='black', alpha=0.7)  # 绘制第二个直方图
plt.hist(data2, bins=30, color='#F6F64E', edgecolor='black', alpha=0.7)  # 绘制第三个直方图
plt.show()  # 显示图形

#图窗属性
#坐标轴上下限
#lim发
plt.figure()  # 创建一个新的图形对象
plt.subplot(2, 1, 1), plt.plot(x, y)
plt.subplot(2, 1, 2), plt.plot(x, y), plt.xlim(0, 6), plt.ylim(0, 30)  # 设置坐标轴的上下限
#plt.plot(x, y)  # 绘制线图
#plt.xlim(0, 6)  # 设置 x 轴的范围
#plt.ylim(0, 30)  # 设置 y 轴的范围
#axis法
#plt.plot(x, y)  # 绘制线图
#plt.axis([0, 6, 0, 30])  # 设置坐标轴的范围，参数依次为 x 轴最小值、x 轴最大值、y 轴最小值、y 轴最大值
plt.show()  # 显示图形
#标题与轴名称
fig = plt.figure()  # 创建一个新的图形对象
plt.plot(x, y, label = '数据1')  # 绘制线图
plt.title('示例图表')  # 设置图表标题
plt.xlabel('X 轴')  # 设置 x 轴标签
plt.ylabel('Y 轴')  # 设置 y 轴标签
plt.legend(loc = 'upper right', frameon = False)  # 添加图例，参数为图例标签列表
plt.grid()  # 显示网格线
plt.show()  # 显示图形
#图例：一般出现在二维图与统计图中，网格图中则是颜色条
#plt.legend()

#网格
#plt.grid()  # 显示网格线