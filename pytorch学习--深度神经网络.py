from hmac import new

from matplotlib import axis
from matplotlib.figure import figaspect
from numpy.random import f
from scipy import optimize
from torch.utils.data import DataLoader, Dataset, random_split
import test
import torch
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
ts1 = torch.randn(3, 5)   #3行5列的标准正态分布随机数
print(ts1)
#搬到gpu上
#ts2 = ts1.to('cuda:0')
#print(ts2)

#DNN
import torch.nn as nn
#生成数据集
x1 = torch.rand(10000, 1)   # 生成10000个随机数，作为输入数据
x2 = torch.rand(10000, 1)   # 生成10000个随机数，作为输入数据
x3 = torch.rand(10000, 1)   # 生成10000个随机数，作为输入数据
y1 = ((x1 + x2 + x3) < 1).float()   # 生成标签数据，满足条件的标签为1，不满足的标签为0
y2 = ((1 < (x1 + x2 +x3)) & ((x1 + x2 + x3) < 2)).float()   # 生成标签数据，满足条件的标签为1，不满足的标签为0
y3 = ((x1 + x2 + x3) >= 2).float()   # 生成标签数据，满足条件的标签为1，不满足的标签为0
data = torch.cat([x1, x2, x3, y1, y2, y3], axis =1)   # 将输入数据和标签数据拼接成一个数据集
print(data.shape)   # 输出数据集的形状
#划分训练集和测试集
train_size = int(len(data) *0.7)    # 计算训练集的大小，取数据集的70%
test_size = len(data) - train_size    # 计算测试集的大小，取数据集的剩余部分
data = data[torch.randperm(data.size(0)), : ]   # 打乱数据集的顺序
train_data = data[:train_size, : ]   # 取前train_size行作为训练集
test_data = data[train_size:, : ]    # 取剩余的行作为测试集
print(train_data.shape)   # 输出训练集的形状
print(test_data.shape)    # 输出测试集的形状
#搭建神经网络
class DNN(nn.Module):
    def __init__(self):
        super(DNN, self).__init__()   # 调用父类的构造函数
        self.net = nn.Sequential(   # 使用Sequential容器来定义神经网络的层次结构
            nn.Linear(3, 5), nn.ReLU(),   # 第一层全连接层，输入维度为3，输出维度为5，后接ReLU激活函数
            nn.Linear(5, 5), nn.ReLU(),   # 第二层全连接层，输入维度为5，输出维度为5，后接ReLU激活函数
            nn.Linear(5, 5), nn.ReLU(),   # 第三层全连接层，输入维度为5，输出维度为5，后接ReLU激活函数
            nn.Linear(5, 3)    # 第四层全连接层，输入维度为5，输出维度为3
        )   # 定义神经网络的层次结构
    def forward(self, x):     #前向传播函数，定义了神经网络的计算过程
        y = self.net(x)   # 通过神经网络的层次结构
        return y    #y为输出数据

#model = DNN().to('cuda:0')   # 创建神经网络模型，并将其搬到GPU上
model = DNN()   # 创建神经网络模型
print(model)   # 输出神经网络模型的结构
#内部参数：
#for name, param in model.named_parameters():   # 遍历神经网络模型的参数
    #print("参数：\n形状:\n数值:\n", name, param.shape, param)   # 输出参数的名称、形状和数值
#超参数：
#激活函数：详情看官网
#损失函数：
loss_fn = nn.MSELoss()   # 定义均方误差损失函数
#学习率与优化算法：
learning_rate = 0.01   # 定义学习率
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)   # 定义SGD优化器，传入模型的参数和学习率
#训练网络
epochs = 1000   # 定义训练的轮数
losses = []   # 创建一个空列表，用于存储每轮训练的损失值
#划分训练集的输入和输出
X = train_data[:, :3]   # 取训练集的前3列作为输入数据
Y = train_data[:, 3:]   # 取训练集的后3列作为标签数据
#循环训练
for epoch in range(epochs):   # 遍历每一轮训练
    pred = model(X)   # 通过神经网络模型进行前向传播，得到预测结果
    loss = loss_fn(pred, Y)   # 计算损失值，比较预测结果和真实标签
    losses.append(loss.item())   # 将损失值添加到列表中，使用item()方法将张量转换为Python数值
    optimizer.zero_grad()   # 清零梯度，准备进行反向传播
    loss.backward()   # 进行反向传播，计算梯度
    optimizer.step()   # 更新模型参数，执行优化算法
#画图
fig = plt.figure()  # 创建一个新的图形对象
plt.plot(range(epochs), losses, color='#7DEEEE', linestyle='-', linewidth=1)   # 绘制损失值随训练轮数变化的曲线图，设置颜色、线条样式、线条宽度和标记样式
plt.title('Loss Curve')  # 设置图表标题
plt.xlabel('epochs')  # 设置 x 轴标签
plt.ylabel('loss')  # 设置 y 轴标签
plt.legend(['loss'])  # 设置图例，参数为图例标签列表
#fig.savefig('loss.svg')  # 保存图形为 SVG 格式
#plt.show()  # 显示图形
#测试网络
X = test_data[:, :3]   # 取测试集的前3列作为输入数据
Y = test_data[:, 3:]   # 取测试集的后3列作为标签数据
with torch.no_grad():   # 在测试阶段，不需要计算梯度，使用no_grad()上下文管理器来禁用梯度计算
    pred = model(X)    # 通过神经网络模型进行前向传播，得到预测结果
    #规整数据
    pred[:, torch.argmax(pred, axis=1)] = 1   # 将预测结果中每行最大值所在位置的元素设置为1，表示预测的类别
    pred[pred != 1] = 0   # 将预测结果中不等于1的元素设置为0，表示其他类别
    correct = torch.sum((pred == Y).all(1))   # 计算预测结果与真实标签完全匹配的样本数量
    total = Y.shape[0]   # 计算测试集的总样本数量
    print(f'测试集准确率：{100 * correct / total:.2f}%')    # 输出测试集的准确率，使用f-string格式化字符串，保留两位小数
#保存与导入网络
#保存网络
torch.save(model, 'dnn.pth')   # 使用torch.save()函数将模型保存到文件中，参数为模型对象和文件名
#导入网络
#new_model = torch.load('dnn.pth')   # 使用torch.load()函数从文件中加载模型，参数为文件名

#批量梯度下降
#pandas导入的表格要先退化为numpy数组，再转换为张量才能使用pytorch进行训练

#小批量梯度下降
#DataSet、DataLoader、random_split
#制作数据集
class MyData(Dataset):   # 定义一个继承自torch.utils.data.Dataset的自定义数据集类
    def __init__(self, filepath):   # 构造函数，接受一个数据参数
        df = pd.read_csv(filepath, index_col = 0)   # 使用pandas库的read_csv函数读取CSV文件，导入数据
        arr = df.values   # 将pandas DataFrame对象转换为numpy数组
        arr = arr.astype(np.float32)   # 将数组的数据类型转换为float32，以便在PyTorch中使用
        ts = torch.tensor(arr)   # 将numpy数组转换为PyTorch张量
        #ts = ts.to('cuda:0')   # 将张量搬到GPU上
        self.X = ts[:, :-1]   # 取张量的前n-1列作为输入数据
        self.Y = ts[:, -1]    # 取张量的最后一列作为标签数据
        self.len = ts.shape[0]   # 获取数据集的样本数量

    def __len__(self):   # 定义返回数据集大小的方法
        return self.len   # 返回数据集的长度
    
    def __getitem__(self, index):   # 定义根据索引获取数据的方法
        return self.X[index], self.Y[index]   # 返回指定索引的输入数据和标签数据
#划分训练集和测试集
Data = MyData('data.csv')   # 创建自定义数据集对象，传入数据文件路径
train_size = int(len(Data) * 0.7)   # 计算训练集的大小，取数据集的70%
test_size = len(Data) - train_size   # 计算测试集的大小，取数据集的剩余部分
train_data, test_data = random_split(Data, [train_size, test_size])   # 使用random_split函数将数据集划分为训练集和测试集，参数为数据集对象和划分比例列表
#批次加载器
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)   # 创建训练集的批次加载器，参数为训练集对象、批次大小和是否打乱数据
test_loader = DataLoader(test_data, batch_size=32, shuffle=False)   # 创建测试集的批次加载器，参数为测试集对象、批次大小和是否打乱数据
#d搭建神经网络
class DNN(nn.Module):
    def __init__(self):
        super(DNN, self).__init__()   # 调用父类的构造函数
        self.net = nn.Sequential(   # 使用Sequential容器来定义神经网络的层次结构
            nn.Linear(3, 5), nn.ReLU(),   # 第一层全连接层，输入维度为3，输出维度为5，后接ReLU激活函数
            nn.Linear(5, 5), nn.ReLU(),   # 第二层全连接层，输入维度为5，输出维度为5，后接ReLU激活函数
            nn.Linear(5, 5), nn.ReLU(),   # 第三层全连接层，输入维度为5，输出维度为5，后接ReLU激活函数
            nn.Linear(5, 1)    # 第四层全连接层，输入维度为5，输出维度为1
        )   # 定义神经网络的层次结构
    def forward(self, x):     #前向传播函数，定义了神经网络的计算过程
        y = self.net(x)   # 通过神经网络的层次结构
        return y    #y为输出数据
model = DNN()   # 创建神经网络模型
print(model)   # 输出神经网络模型的结构
#训练网络
loss_fn = nn.MSELoss()   # 定义均方误差损失函数
learning_rate = 0.01   # 定义学习率
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)   # 定义SGD优化器，传入模型的参数和学习率
epochs = 1000   # 定义训练的轮数
losses = []   # 创建一个空列表，用于存储每轮训练的损失值
for epoch in range(epochs):   # 遍历每一轮训练
    for X, Y in train_loader:   # 遍历训练集的批次加载器，获取每个批次的输入数据和标签数据
        pred = model(X)   # 通过神经网络模型进行前向传播，得到预测结果
        loss = loss_fn(pred, Y)   # 计算损失值，比较预测结果和真实标签
        losses.append(loss.item())   # 将损失值添加到列表中，使用item()方法将张量转换为Python数值
        optimizer.zero_grad()   # 清零梯度，准备进行反向传播
        loss.backward()   # 进行反向传播，计算梯度
        optimizer.step()   # 更新模型参数，执行优化算法
#画图
fig = plt.figure()  # 创建一个新的图形对象
plt.plot(range(epochs), losses, color='#7DEEEE', linestyle='-', linewidth=1)   # 绘制损失值随训练轮数变化的曲线图，设置颜色、线条样式、线条宽度和标记样式
plt.title('Loss Curve')  # 设置图表标题
plt.xlabel('epochs')  # 设置 x 轴标签
plt.ylabel('loss')  # 设置 y 轴标签
plt.legend(['loss'])  # 设置图例，参数为图例标签列表
#fig.savefig('loss.svg')  # 保存图形为 SVG 格式
#plt.show()  # 显示图形
#测试网络
correct = 0   # 初始化正确预测的样本数量
total = 0   # 初始化测试集的总样本数量
with torch.no_grad():   # 在测试阶段，不需要计算梯度，使用no_grad()上下文管理器来禁用梯度计算
    for X, Y in test_loader:   # 遍历测试集的批次加载器，获取每个批次的输入数据和标签数据
        pred = model(X)    # 通过神经网络模型进行前向传播，得到预测结果
        pred[pred > 0.5] = 1.0
        pred[pred <= 0.5] = 0.0
        correct += torch.sum((pred == Y).all(1))   # 计算预测结果与真实标签匹配的样本数量，并累加到正确预测的样本数量中
        total += Y.shape[0]   # 累加测试集的总样本数量
print(f'测试集准确率：{100 * correct / total:.2f}%')    # 输出测试集的准确率，使用f-string格式化字符串，保留两位小数
