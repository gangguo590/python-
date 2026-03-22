import pandas as pd
import numpy as np
#pandas是基于numpy的，numpy是专门处理数值数据的，而pandas则是专门处理表格数据的

#对象的创建
#一维���象的创建
dict_v = {'a': 1, 'b': 2, 'c': 3}     #字典创建法
sr = pd.Series(dict_v)
print(sr)
#v = [6, 9, 5]     #列表创建法
v = np.array([6, 9, 5])     #numpy数组创建法
k = ['a', 'b', 'c']
sr = pd.Series(v, index=k)    #index省略时索引默认从0开始
print(sr)
#查看属性
print(sr.values)    #查看值
print(sr.index)     #查看索引
print("------------------------------")
#二维对象的创建
#字典创建法
dict_v = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
df = pd.DataFrame(dict_v, index=['A', 'B', 'C'])
print(df)
#数组创建法
v = np.array([["18岁", 4, 7], ["22岁", 5, 8], ["25岁", 6, 9]])
k = ['1号', '2号', '3号']
c = ['年龄', '身高', '体重']
df = pd.DataFrame(v, index = k, columns = c)
print(df)
#二维对象的属性
print(df.values)    #查看值
print(df.index)     #查看索引
print(df.columns)   #查看列名
print("------------------------------")

#一维对象的索引:显示索引和隐式索引
#显示索引
print(df.loc['1号'])  #通过显示索引访问行
#隐式索引
print(df.iloc[0])     #通过隐式索引访问行
print("------------------------------")
#访问切片
print(df.loc['1号':'2号'])   #通过显示索引访问行切片
print(df.iloc[0:2])    #通过隐式索引访问行切片，左闭右开
print("------------------------------")
#二维对象的索引
print(df.loc['1号', '年龄'])   #通过显示索引访问单个元素
print(df.iloc[0, 0])    #通过隐式索引访问单个元素
print(df.loc[['1号', '2号'], ['年龄', '身高']])   #通过显示索引访问多个元素
print(df.iloc[0, 0:2])   #通过隐式索引访问多个元素，左闭右开
print("------------------------------")
#访问切片
print(df.loc['1号':'2号', '年龄':'身高'])   #通过显示索引访问切片
print(df.iloc[0:2, 0:2])   #通过隐式索引访问切片，左闭右开
print("------------------------------")

#对象的变形：转置，翻转，
print(df.T)  #转置
print(df.iloc[::-1, : ])   #翻转，行翻转/上下翻转
print(df.iloc[:, ::-1])    #列翻转/左右翻转
#对象的重塑
print("------------------------------")
#对象的拼接
v1 = np.array([["男"], ["女"], ["男"]])
k1 = ['1号', '2号', '3号']
c1 = ['性别']
df1 = pd.DataFrame(v1, index = k1, columns = c1)
print(pd.concat([df, df1], axis=1))   #按列拼接
print("------------------------------")
#一维对象与三维对象的合并:看成插入操作
print(df)
print(df1)
df["性别"] = df1["性别"].values   #加上一列
print(df)
print("------------------------------")
df.loc["4号"] = ["28岁", 7, 10, "男"]   #加上一行
print(df)
print("------------------------------")
#二维对象的合并
df2 = pd.DataFrame(np.array([["是"], ["是"], ["是"], ["是"]]), index=['1号', '2号', '3号', '4号'], columns=['ikun'])
#print(pd.concat([df, df2], axis=1))   #按列拼接
df["ikun"] = df2["ikun"].values   #加上一列
print(df)
print("------------------------------")

#对象的运算

#布尔型数组
print(df["年龄"] > "20岁")   #比较运算，返回布尔型数组
#统计true数量
print(np.sum(df["年龄"] > "20岁"))   #统计true数量
#作为掩码
print(df[df["年龄"] > "20岁"])   #作为掩码，返回满足条件的行
print("------------------------------")

#对象的缺失值
df.loc["5号"] = [np.nan, np.nan, np.nan, np.nan, np.nan]   #添加一行缺失值
print(df)
print(df.isnull())   #判断缺失值，返回布尔型数组
#剔除缺失值
print(df.dropna())   #剔除缺失值，返回剔除后的对象
df.loc[["1号"],["年龄"]] = np.nan   #添加一个缺失值
print(df)
print(df.dropna())   #剔除缺失值，返回剔除后的对象，只要有一个缺失值就剔除整行
print(df.dropna(thresh=3))   #剔除缺失值，返回剔除后的对象，只有当非缺失值<3（即缺失值>=3）时才剔除该行
print("------------------------------")
#填充缺失值
#方法1：用年龄列的平均值填充（需要先提取数字）
age_values = df['年龄'].dropna().str.extract(r'(\d+)')[0].astype(int)   #提取数字并转换为整数
age_mean = age_values.mean()   #计算平均值
filled_df = df.fillna(age_mean)   #用平均值填充
print(filled_df)
print("------------------------------")
#方法2：更简洁的做法 - 用平均值和"岁"拼接
age_mean_str = str(int(age_mean)) + "岁"
filled_df2 = df.fillna(age_mean_str)   #用和格式匹配的值填充
print(filled_df2)
print("--------------------------------")

#导入excel文件 - 使用openpyxl库
try:
    df_excel = pd.read_excel("1号-5号数据表.xlsx", index_col=0)   #使用read_excel导入Excel文件，并把首列作为索引
    print(df_excel)
except FileNotFoundError:
    print("错误：找不到Excel文件，请检查文件路径")
except ImportError as e:
    print(f"错误：缺少必要的库，请运行: pip install openpyxl")
    print(f"详细信息: {e}")
except Exception as e:
    print(f"错误：{e}")
print("--------------------------------")

#数据分析
#聚合方法
print(df_excel.head())   #查看前几行数据，前5行内容
print("------------------------------")
print(df_excel.max())    #查看每列的最大值
print(df_excel.min())    #查看每列的最小值
print(df_excel.sum())    #查看每列的总和
print(df_excel.mean())   #查看每列的平均值
print("------------------------------")
#描述方法
print(df_excel.describe())   #查看每列的描述统计信息，包括计数、均值、标准差、最小值、四分位数和最大值
#数据透视
print(df_excel.pivot_table("S.1", index='S'))    #查看S对S.1的透视表，默认聚合函数为平均值，S.1是输出，S是输入
print("------------------------------")
print(df_excel.pivot_table("S.1", index='S', aggfunc='sum'))    #查看S对S.1的透视表，聚合函数为总和
print("------------------------------")
print(df_excel.pivot_table("S.1", index='S', columns='D'))    #查看S和D对S.1的透视表，默认聚合函数为平均值，S.1是输出，S和D是输入
print("------------------------------")
#多个输入时
#重置
df_excel['S分箱'] = pd.cut(df_excel['S'], bins=[0, 20, 100, 654], labels=['0-20', '20-100', '100-654'], include_lowest=True)   #对S列进行分箱，分为三个区间，并设置标签
print(df_excel[['S', 'S分箱']])
df_excel['J'] = pd.qcut(df_excel['J'], 2, labels=['低J', '高J'])   #对J列进行分箱，分为两个区间，并设置标签
print(df_excel.pivot_table("S.1", index=['S分箱', 'J', 'G'], columns='D'))    #查看S分箱、G和J对S.1的透视表，默认聚合函数为平均值，S.1是输出，S分箱、G和J是输入，D是列输入