#注释：以#开头
#声明变量：变量名=值
a = 10
b = 1 + 1
#基本数据类型：整数、浮点数、字符串、布尔值
str_v = "Hello, World!"
int_v = 10
float_v = 3.14
bool_v = True
#高级数据类型：列表、元组、字典、集合
#集合：{}
my_set = {1, 2, 3, 4, 5}
#列表：[]
my_list = [1, 2, 3, 4, 5]
#元组：()
my_tuple = (1, 2, 3, 4, 5)
#字典：{key: value}
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
#输出变量值
print(str_v)
#字符串
str_v2 = "Python"
str_v3 = 'Python'
#f拼接字符串
print(f"{str_v2} and {str_v3} are the same.")
#转义字符
str_v4 = "He said, \n\"Hello!\""
print(str_v4)
#集合
my_set2 = set([1, 2, 3, 4, 5])
print(my_set2)
print(2 in my_set2)   #in运算符检查元素是否在集合中
print(6 in my_set2)
#判断，带冒号:
if 2 > 5:
    print("1")
elif 2 < 5:
    print("2")
else:
    print("3")
#变量转换
num_str = "123"
num_v = 123
num_int = int(num_str)  #字符串转换为整数
print(num_int)
num_float = float(num_str)  #字符串转换为浮点数
print(num_float)
print(str(num_v))  #整数转换为字符串
print(str(num_float))  #浮点数转换为字符串
#集合
my_set3 = set([1, 2, 3, 4, 5])
my_set4 = {"1,2,3", "3,4", "5", "5"}
print(my_set4)
#元组
my_tuple2 = (1, 2, 3, 4, 5)
print(my_tuple2)
my_tuple3 = ('sad', 123, True, {12, 5}, [1, 2, 3], (4, 5))
print(my_tuple3)
#元组法输出
print("最终为: ", 45)
#元组拆分法：
a, b, c = (1, 2, 3)
print(a, b, c)
print(a)
print(b)
print(c)
b, a = a, b   #元组交换法
print(a, b, c)
print("最终为: ", a)
vlaue = 1, 2, 3, 4, 6, 9
d, e, *f = vlaue   #元组拆分法，*f表示剩余的元素会被放在一个列表中
print(d, e, f)
#列表
my_list2 = [1, 2, 3, 4, 5]
print(my_list2)
print(my_list2[-1])  #列表索引，-1表示最后一个元素
print(my_list2[0])   #列表索引，0表示第一个元素
#切片:左闭右开
print(my_list2[1:4])  #切片，包含索引1到3的元素，不包含索引4
print(my_list2[:3])   #切片，包含索引0到2的元素，不包含索引3
print(my_list2[2:])   #切片，包含索引2到最后一个元素
print(my_list2[ : : 2])  #切片，步长为2，包含索引0,2,4的元素
#列表元素添加
my_list2.append(6)  #在列表末尾添加元素
my_list2 = my_list2 + [7]  #使用+运算符添加元素
print(my_list2)
#字典:键+值
my_dict2 = {"name": "Alice", "age": 30, "city": "New York", 3: {4}, 5: [1, 2, 3]}
print(my_dict2[3])
print(my_dict2["name"])
#字典元素修改、增加、删减
my_dict2["age"] = 31  #修改键为"age"的值
my_dict2["country"] = "USA"  #增加键为"country"的键值对
del my_dict2[5]  #删除键为5的键值对
print(my_dict2)
#循环语句
for i in my_dict2:
    print("youe conutry is: ", my_dict2[i])
#循环键
for key in my_dict2.keys():
    print("your key is: ", key)
#循环值
for value in my_dict2.values():
    print("your value is: ", value)
#循环键值对
for key, value in my_dict2.items():
    print("your key is: ", key, "\nyour value is: ", value)
#高级变量类型转换
#转换为集合使用set()函数
#转换为列表使用list()函数
#转换为元组使用tuple()函数
#转换为字典使用dict()函数

#函数
def my_function():  #输入参数可以是各个类型的变量
    print("Hello, World!")
    return 0
my_function()
#多个输入参数
def add(a, b):
    return a + b
result = add(5, 3)
print(result)
#传入任意数量
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_all(1, 2, 3, 4, 5)
print(result)
#附带键值对的参数
def eva(in1, in2, **kwargs):
    '''评价函数'''
    kwargs['计算机'] = in1
    kwargs['土木'] = in2
    return kwargs
result = eva("打代码", "打灰", 其他="打工")
print(result)
#函数关键字调用
def eva1(in1, in2, in3):
    '''评价函数'''
    return f"{in1}打代码的, {in2}打灰的, {in3}打工的"
result = eva1( in2="计算机", in1="土木", in3="其他")
print(result)
#函数默认值
def greet(name="World"):
    return f"Hello, {name}!"
print(greet())  #使用默认值
print(greet(name = "Alice"))  #传入参数覆盖默认值
#类
class Person:
    def __init__(self, name, age):   #__init__方法是类的构造函数，在创建对象时会自动调用
        self.name = name
        self.age = age
    def greet(self):   #自定义方法
        return f"Hello, my name is {self.name} and I am {self.age} years old."
person1 = Person("Alice", 30)
print(person1.greet())
#创建类的实例
person2 = Person("Bob", 25)
print(person2.greet())
#属性的默认值
class Car:
    def __init__(self, make, model, year=2020):  #year属性有默认值
        self.make = make
        self.model = model
        self.year = year
car1 = Car("Toyota", "Camry")
print(car1.make)  #输出传入的值
print(car1.year)  #输出默认值
car2 = Car("Honda", "Civic", 2021)
print(car2.year)  #输出传入的值
car2.year = 2022  #修改类属性year的值
print(car2.year)  #输出修改后的值

#继承
class Student(Person):  #Student类继承自Person类
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  #调用父类的构造函数
        self.student_id = student_id
    def study(self):
        return f"{self.name} is studying."
student1 = Student("Charlie", 20, "S12345")
print(student1.greet())  #调用继承自Person类的方法
print(student1.study())  #调用Student类的方法
#掠夺
class Teacher:  #Teacher类作为掠夺者
    def __init__(self, name, age, subject, student_id="S00000"):
        self.name = name
        self.age = age
        self.subject = subject
        self.student_id = student_id
        self.cnt = Person(name, age)   #掠夺
        self.cnt1 = Student(name, age, self.student_id)  #掠夺
    def teach(self):
        return f"{self.name} is teaching {self.subject}."
    def greet(self):
        return self.cnt.greet()
    def study(self):
        return self.cnt1.study()
teacher1 = Teacher("David", 40, "Math")
print(teacher1.teach())  #调用Teacher类的方法
print(teacher1.greet())  #调用掠夺自Person类的方法
print(teacher1.study())  #调用掠夺自Student类的方法