import torch  # 导入 PyTorch 库
import torch.nn as nn  # 导入神经网络模块
import torch.optim as optim  # 导入优化器模块
import numpy as np  # 导入 NumPy 库

print("PyTorch 版本:", torch.__version__)  # 输出 PyTorch 版本
print("--------------------")

# 1. 张量基础
# 张量是 PyTorch 的核心数据结构，类似于 NumPy 的数组
# 创建张量
t1 = torch.tensor([1, 2, 3, 4, 5])  # 从列表创建张量
print("一维张量:", t1)  # 输出一维张量

t2 = torch.tensor([[1, 2, 3], [4, 5, 6]])  # 创建二维张量
print("二维张量:\n", t2)  # 输出二维张量
print("张量形状:", t2.shape)  # 输出张量形状
print("张量维度:", t2.ndim)  # 输出张量维度
print("--------------------")

# 创建特殊张量
t3 = torch.zeros(2, 3)  # 创建全零张量
print("全零张量:\n", t3)  # 输出全零张量

t4 = torch.ones(2, 3)  # 创建全一张量
print("全一张量:\n", t4)  # 输出全一张量

t5 = torch.randn(2, 3)  # 创建随机张量（标准正态分布）
print("随机张量:\n", t5)  # 输出随机张量

t6 = torch.arange(0, 10, 2)  # 创建递增张量
print("递增张量:", t6)  # 输出递增张量
print("--------------------")

# 2. 张量操作
# 张量与标量的运算
t7 = torch.tensor([1, 2, 3, 4, 5])
print("原始张量:", t7)
print("加法:", t7 + 10)  # 每个元素加10
print("乘法:", t7 * 2)  # 每个元素乘以2
print("幂运算:", t7 ** 2)  # 每个元素的平方
print("--------------------")

# 张量之间的运算
t8 = torch.tensor([1, 2, 3])
t9 = torch.tensor([4, 5, 6])
print("张量1:", t8)
print("张量2:", t9)
print("对应相加:", t8 + t9)  # 对应元素相加
print("对应相乘:", t8 * t9)  # 对应元素相乘
print("点积:", torch.dot(t8, t9))  # 点积运算
print("--------------------")

# 张量索引和切片
t10 = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("张量:\n", t10)
print("访问元素 [0, 1]:", t10[0, 1])  # 访问第0行第1列的元素
print("第0行:", t10[0, :])  # 访问第0行
print("第1列:", t10[:, 1])  # 访问第1列
print("切片 [0:2, 1:3]:\n", t10[0:2, 1:3])  # 切片操作
print("--------------------")

# 张量变形
t11 = torch.arange(12)
print("原始张量:", t11)
t12 = t11.reshape(3, 4)  # 重塑为3行4列
print("重塑后:\n", t12)
print("转置:\n", t12.T)  # 转置操作
print("--------------------")

# NumPy 数组与张量转换
arr = np.array([1, 2, 3, 4, 5])
t13 = torch.from_numpy(arr)  # NumPy 数组转张量
print("NumPy 转 PyTorch:", t13)
arr2 = t13.numpy()  # 张量转 NumPy 数组
print("PyTorch 转 NumPy:", arr2)
print("--------------------")

# 3. 自动求导（Autograd）
# PyTorch 的核心功能：自动计算梯度
x = torch.tensor([2.0], requires_grad=True)  # 创建需要求导的张量
y = x ** 2 + 3 * x + 1  # 定义函数
print("函数值:", y.item())  # 输出函数值

y.backward()  # 反向传播计算梯度
print("梯度 dy/dx:", x.grad.item())  # 输出梯度值（理论值：2*2+3=7）
print("--------------------")

# 4. 简单线性回归示例
# 准备数据
# 真实关系：y = 2x + 3
X = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]], dtype=torch.float32)
y = torch.tensor([[5.0], [7.0], [9.0], [11.0], [13.0]], dtype=torch.float32)

print("输入数据 X:\n", X)
print("输出数据 y:\n", y)
print("--------------------")

# 定义线性回归模型
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(1, 1)  # 输入维度1，输出维度1

    def forward(self, x):
        return self.linear(x)

model = LinearRegression()  # 创建模型实例
print("模型结构:", model)
print("--------------------")

# 定义损失函数和优化器
criterion = nn.MSELoss()  # 均方误差损失函数
optimizer = optim.SGD(model.parameters(), lr=0.01)  # 随机梯度下降优化器，学习率0.01

# 训练模型
print("开始训练...")
epochs = 1000  # 训练轮数
for epoch in range(epochs):
    # 前向传播
    y_pred = model(X)  # 预测值
    loss = criterion(y_pred, y)  # 计算损失

    # 反向传播
    optimizer.zero_grad()  # 清零梯度
    loss.backward()  # 反向传播
    optimizer.step()  # 更新参数

    if (epoch + 1) % 200 == 0:  # 每200轮输出一次
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

print("训练完成！")
print("--------------------")

# 查看训练结果
# 提取模型参数（权重和偏置）
weight = model.linear.weight.item()
bias = model.linear.bias.item()
print(f"学习到的参数: weight = {weight:.4f}, bias = {bias:.4f}")
print(f"理论参数: weight = 2.0000, bias = 3.0000")

# 进行预测
test_input = torch.tensor([[6.0]])
prediction = model(test_input).item()
print(f"预测 x=6 时的 y 值: {prediction:.4f}")
print(f"理论值 y = 2*6 + 3 = {2*6+3:.4f}")
print("--------------------")

# 5. 简单神经网络示例
# 创建一个简单的多层感知机（MLP）
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.hidden = nn.Linear(2, 4)  # 隐藏层：2个输入，4个神经元
        self.output = nn.Linear(4, 1)  # 输出层：4个输入，1个输出
        self.relu = nn.ReLU()  # ReLU 激活函数

    def forward(self, x):
        x = self.hidden(x)  # 隐藏层计算
        x = self.relu(x)  # ReLU 激活
        x = self.output(x)  # 输出层计算
        return x

nn_model = SimpleNN()  # 创建神经网络模型
print("神经网络模型结构:")
print(nn_model)
print("--------------------")

# 测试神经网络
test_data = torch.tensor([[1.0, 2.0]])
nn_output = nn_model(test_data)
print(f"输入: {test_data.numpy()}")
print(f"输出: {nn_output.item():.4f}")
print("--------------------")

# 6. 保存和加载模型
# 保存模型
torch.save(model.state_dict(), 'linear_model.pth')
print("模型已保存到 linear_model.pth")

# 加载模型
new_model = LinearRegression()
new_model.load_state_dict(torch.load('linear_model.pth'))
print("模型已加载")
print("加载的模型参数:", new_model.linear.weight.item(), new_model.linear.bias.item())
print("--------------------")

print("PyTorch 学习脚本执行完成！")
print("核心概念总结：")
print("1. 张量（Tensor）：PyTorch 的核心数据结构")
print("2. 自动求导（Autograd）：自动计算梯度")
print("3. 神经网络（nn.Module）：构建深度学习模型")
print("4. 优化器（Optimizer）：更新模型参数")
print("5. 损失函数（Loss Function）：衡量预测误差")
