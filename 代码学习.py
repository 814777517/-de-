import unittest

from tools1 import login1

print("hello world")





str='abcdefg'
print(str[0:3:1])
print(str[0:3])
print(str[:3])
print(str[4:7])
print(str[4:])
print(str[:])
print(str[0:7:2])
print(str[::-1])



#num+1表示从这一位开始
str="hello world and itcast and itheima and Python"
num=str.find('and')
print(num)
num1=str.find('and',num+1)
print(num1)

#字符串替换
str2=str.replace('world','g')
print(str2)

#2代表最大次数
a='good good study'
a1=a.replace('good','GOOD',2)
a2=a.replace('good','GOOD',1)
print(a1)
print(a2)



#列表

list5=['小明',198,18,True]
print(list5[0])
print(list5[-1])
print(len(list5))

#列表查询

#列表中找出某个值第一个匹配项的索引位置
mylist=[1,2,3,4,5,6]
num=mylist.index(4)
print(num)

if 7 in mylist:
    num1=mylist.index(7)
    print(num1)
else:
    print('不在列表中')

if mylist.count(7)>0:
    num2=mylist.index(7)
    print(num2)
else: print('不在家中')


#列表添加
mylist=[]
print(mylist)
#列表末尾加入新的元素
mylist.append('卡卡罗特')
print(mylist)

mylist.append('贝吉塔')
print(mylist)
#插入到指定位置
mylist.insert(1,'布罗利')
print(mylist)

mylist4=['弗利萨','克林']
mylist.append(mylist4)
print(mylist)
#列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
mylist.extend(mylist4)
print(mylist)


#列表推导式
#从0-5不包括5
num=['hello'for i in range(5)]
print(num)

num1=[i for i in range(5)]
print(num1)

#列表的修改
mylist=[1,3,5,7,9]
mylist[2]=6
print(mylist)


#列表的删除
#移除列表中的值默认是最后一位
mylist=[9,8,7,6,5,4]
num=mylist.pop()
print('删除的数据为:',num)
print(mylist)

mylist.pop(1)
print(mylist)
#删除列表中指定的元素
mylist.remove(7)
print(mylist)

#列表的反转

mylist=[1,2,3,4,5,6,7,8,9]
mylist.reverse()
print('mylist:',mylist)


mylist=[10,11,12,13]
num=mylist[::-1]
print('num:',num)
print('mylist:',mylist)

print('....................')

#列表的复制

mylist=[1,2,3]
#切片[:]复制
mylist1=mylist[:]
print('mylist:',mylist)
print('mylist1:',mylist1)

mylist2=mylist.copy()
print('mylist:',mylist)
print('mylist2:',mylist2)


#列表的排序


mylist=[11,5,9,6,2,3]
#对列表进行排序
mylist.sort()
print(mylist)


#元祖
#tuple()将列表转换为元组
mytuple2=tuple([1,2,3,4,5])
print(mytuple2)

mytuble3=tuple('hello')
print(mytuble3)


mytuple4=('小王',1,3.14,False)
print(mytuple4)


mytuple5=(1)
print(mytuple5)


#字典
mydict=dict()
print(type(mydict),mydict)


mydict1={}
print(type(mydict1),mydict1)


mydict2={"name":"小明","age":18,"height":1.71,"is_men":True,"like":["抽烟","喝酒","烫头"]}
print(mydict2)

#字典的增加和修改
mydict2["sex"]="男"

mydict2["age"]=20

print((mydict2))

mydict2["like"].append("学习")
print(mydict2)

#删除
mydict10={"name":"小明","age":20,"height":1.75,"is_men":True,"like":["抽烟","喝酒","烫头"]}
del mydict10["name"]
print(mydict10)

mydict10.pop("height")
print(mydict10)


mydict10["like"].remove("抽烟")
print(mydict10)

print('.............................')
#获取
mydict11={"name":"小明","age":20,"height":1.75,"is_men":True,"like":["抽烟","喝酒","烫头"]}

print(mydict11["age"])

print(mydict11.get("name"))


print(mydict11["like"][1])
print(mydict11.get("like")[0])

print('........................')





#字典的遍历
mydict12={"name":"小明","age":20,"height":1.75,"is_men":True}
for i in  mydict12.keys():
    print(i)



mydict13={"name":"小明","age":20,"height":1.75,"is_men":True}
for i in mydict13:
    print(i)

mydict14={"name":"小明","age":20,"height":1.75,"is_men":True}
for i in mydict14.values():
    print(i)

mydict15 = {"name": "小明", "age": 20, "height": 1.75, "is_men": True}
for i,m in mydict15.items():
    print(i,m)
    #break;


print("hello "*3)
print((1,2)*3)
print([1,2]*3)


#函数
def sayhell():
    print("hello")

sayhell()


#列表去重



my_list=[1,2,5,3,7,6,1,5]

newmy_list=[]
for i in my_list:
    if i in newmy_list:
        pass
    else:
        newmy_list.append(i)
print(newmy_list)

#交换两个变量的值
a=10
b=20
a,b=b,a
print('a:',a,'b:',b)

#局部
def func1():
    num = 10
    print(f"func1 函数中{num}")
func1();

#全局
num1=11
def func2():
    print(f"func2 函数中{num1}")
func2()


def cal(a,b):
    num=a+b
    num1=a-b
    return num,num1


#方法一
result=cal(10,5)
print(result)

#方法二：拆包
x,y=cal(20,5)
print(x,y)






def cl(a,b,c):
    print(f'a:{a},b:{b},c:{c}')


#位置传参
cl(4,5,6)
#关键字传参
cl(a=4,b=5,c=6)




#缺省参数

def ca(name,sex='保密'):
    print(name,sex)

ca('刘聪')
ca('刘聪','男')

#不定长传参 *args为不定长位置参数（不定长元组参数）**kwargs不定长关键字参数（不定长字典参数）
def my_sum(*args,**kwargs):
    num=0#定义变量，保存求和的结果

    #for i in args:
        #num+=i

    for j in kwargs.values():
        num+=j

    print(num)

#my_list=[1,2,3,4,5]
my_dict={'a':1,'b':2,'c':3,'d':4,'e':5}
#my_sum(*my_list)
my_sum(**my_dict)

#匿名函数
func1=lambda a,b:a*b
print(func1(2,3))




#面向对象
#创建类
class Cat:
    #方法
    def eat(self):
        print(f'小猫{self.name}爱吃鱼')
    def drink(self):
        print(f'小猫{self.name}爱喝水')

#创建对象
blue_cat=Cat()
blake_cat=Cat()
#对象.属性名
blue_cat.name='蓝猫'
blake_cat.name='黑猫'
#通过对象调用类中的方法
blue_cat.eat()
blake_cat.drink()

#魔法方法
#_init_

#定义添加属性的方法，此方法创建对象时自动调用。
class Cat:
  def __init__(self):
    self.name='刘聪'
    self.age='25'
  print('11111')
  def show_info(self):
   print(f'名字是:{self.name},年龄为:{self.age}')

cat=Cat()#创建对象时调用__init__方法
cat.show_info()






#传参
class Cat:
  def __init__(self,name,age):
    self.name=name
    self.age=age
    print('11111')
  def show_info(self):
    print(f'名字是:{self.name},年龄为:{self.age}')

cat=Cat('刘聪','20')#创建对象时调用__init__方法
cat.show_info()


#公有
class Persion:
    def __init__(self,name,age):
        #公有属性
        self.name=name
        self.age=age
    def __str__(self):
        return f'名字:{self.name},年龄:{self.age}'

xm=Persion('小明',18)
print(xm)
#在类的外部直接访问age属性
print(xm.age)
#修改age属性
xm.age=20
print(xm)



#私有

class Persion:
    def __init__(self,name,age):
        #私有属性
        self.__name=name
        self.__age=age
    def __str__(self):
        return f'名字:{self.__name},年龄:{self.__age}'

xm=Persion('小明',30)
#可以访问私有属性
print(xm)
#在类的外部无法直接访问age属性
#print(xm.__age)
#修改age属性
#xm.__age=40   无法修改日趋
#print(xm)



#继承
#创建父类
class Animal:
 def eat(self):
     print('要吃东西')

#创建子类，继承父类的方法
class Dog(Animal):
    def bark(self):
        print('汪汪叫')
#调用自己类中的方法
ani=Animal()
ani.eat()



#子类可直接调用父类方法
dog=Dog()
dog.eat()
dog.bark()


#重写
#覆盖
class Dog():
    def eat(self):
        print('666')

class XTQ(Dog):
    def eat(self):
        print('555')


xtq=XTQ()
xtq.eat()





#扩展

class pig():
    def aa(self):
        print('777')

class XQQ(pig):
    def aa(self):
        super().aa()
        print('888')


xqq=XQQ()
xqq.aa()



#实例属性
#在init方法中 ,self.属性名=属性值 定义
#self.属性名 调用

#类属性   类内部方法外部直接定义变量
#类对象.属性名=属性值 or 类名.属性名=属性值
#类对象.属性名 or 类名.属性名


class Dog:
#定义类属性
  count=0
#定义实例属性，init方法中
  def __init__(self,name):
      self.name=name
      #类名.类属性名
      Dog.count+=1
#类外部
#打印输出目前创建几个对象
print(f'当前对象为:{Dog.count}个') #0
dog1=Dog('笑话')
#打印输出目前创建几个对象
print(f'当前对象为:{Dog.count}个')



#实例方法 在类中直接定义的方法
class Demo:
    def func(self):
        pass
#类方法
class Demo:
    @classmethod
    def func(cls):
        pass


import random
class Game:
    #类属性游戏的最高分
    top_score=0
    def __init__(self,name):
        self.name=name
    def show_help(self):
        print('游戏的帮助信息')
    def show_top_score(self):
        #类名.类属性
        print(f'游戏的最高分为{Game.top_score}')
    def start_game(self):
        print(f'{self.name}开始一局游戏',end='')
        score=random.randint(10,100)#本次游戏的得分10-100之间
        print(f'本次游戏得分为{score}')
        if score>Game.top_score:
            Game.top_score=score
xw=Game('小王')
xw.start_game()
xw.show_top_score()
xw.start_game()
xw.show_top_score()



print('..............')




import random
class Game:
    #类属性游戏的最高分
    top_score=0
    show_top_score_player=''
    def __init__(self,name):
        self.name=name
    def show_help(self):
        print('游戏的帮助信息')
    def show_top_score(self):
        #类名.类属性
        print(f'游戏的最高分为{Game.top_score}')
    def start_game(self):
        print(f'{self.name}开始一局游戏',end='')
        score=random.randint(10,100)#本次游戏的得分10-100之间
        print(f'本次游戏得分为{score}')
        if score>Game.top_score:
            Game.top_score=score
            #修改最高分玩家名字
            Game.show_top_score_player=self.name
xw=Game('小王')
xw.start_game()
xw.show_top_score()
xw=Game('小红')
xw.start_game()
xw.show_top_score()
xw=Game('小绿')
xw.start_game()
xw.show_top_score()
xw=Game('小马')
xw.start_game()
xw.show_top_score()




#1.打开文件
f=open('a.txt','w',encoding='utf-8')
#2.写文件
f.write('好好学习')
#3.关闭文件
f.close()



f=open('a.txt','r',encoding='utf-8')
#2.读文件
buf=f.read()
print(buf)
f.close()


#a方式打开文件，文件不存在会创建文件，文件存在，在文件的末尾写入内容
with open('a.txt','a',encoding='utf-8')as f:
    f.write('good good study')









with open('a.txt',encoding='utf-8')as f:
    for i in f:
        print(1,end='')

with open('a.txt',encoding='utf-8')as f:
    buf=f.readline()
    print(buf)
    print(f.readline())


#向文件中写入指定内容，前提是文件的打开方式是w或者a，将文件中的内容读取出来，文件的打开方式需要是r。


#json文件的读取
#1.导入json
import json
with open('info.json',encoding='utf-8')as f:
    #读文件
    result=json.load(f)
    #姓名
    print(result.get('name'))
    #年龄
    print(result.get('age'))
    #城市
    print(result.get('address').get('city'))
    pass



#都要转换成列表套元组。
import json

#def read_data():

with open('info1.json', encoding='utf-8') as f:
    data = json.load(f)  # 列表
    # print(data)
    new_list = []  # 定义一个列表存放元组。
    for i in data:  # i字典
        #print(i.get('username'), i.get('password'), i.get('expect'))
        print((i.get('username'), i.get('password'), i.get('expect')))# 元组
        new_list.append((i.get('username'), i.get('password'), i.get('expect')))
    print(new_list)
    #return new_list



#json的写入
import json

my_list = [('admin', '456789', '登陆成功'), ('root', '98653', '登陆失败')]

with open('info2.json', 'w', encoding='utf-8') as f:
    json.dump(my_list, f, ensure_ascii=False, indent=4)





#异常的捕获

try:
    num = input('请输入数字:')
    num = int(num)
    print(num)
except:
    print('请重新输入数字:')

try:
    num = input('请输入数字:')
    num = int(num)
    print(num)
except ValueError:#异常的类型
    print('请重新输入数字:')



#捕获多个指定类型的异常


try:
    num = input('请输入数字:')
    num = int(num)
    print(num)
    a = 10 / num
    print(f'a:{a}')
except ValueError:  # 异常的类型
    print('发生了异常请重新输入数字:')
except ZeroDivisionError:
    print('除数不能为0')


#异常捕获的完整版

try:
    num = input('请输入数字:')
    num = int(num)
    print(num)
    a = 10 / num
    print(f'a:{a}')
except Exception as e:
    print(f"错误信息为:{e}")
else:
    print('没有发生会异常执行')
finally:
    print('不管有没有发生异常，都会执行')


#模块的导入
#方式一:import 模块名
#方式二：from 模块名 import 工具名




#__name__作用

import tools#导入模块，执行tools模块中的代码
print(tools.add(100,200))



#断言
#self.assertEqual
#self.assertIn
#跟tools1配合使用
class TestLogin(unittest.TestCase):
   def test_username_password_ok(self):
      self.assertEqual('登陆成功',login1('admin','123456'))
      #self.assertIn('失败',login1('aa','123'))
   def test_user_name_error(self):
       self.assertEqual('登陆失败',login1('root','456'))




#HTMLTestRunner第三方的类库
#注：测试多个用例时用这种
import unittest
from HTMLTestRunner import HTMLTestRunner
#使用套件对象，加载对象去添加用例方法
suite=unittest.defaultTestLoader.discover()
#4.实例化第三方的运行对象 并运行套件对象
with open('文件名','wb')as f:
  runner=HTMLTestRunner(f)
  runner.run(suite)



  #流程:1.组织用例文件(TestCase里面)，写参数化，断言，Fixture,跳过。单个测试用例直接运行
  #生成测试用例，多个测试文件，需组装运行，生成测试报告。
  #    2.使用套件对象组装，或使用加载对象组装
  #    3.运行对象 运行  运行对象需要第四步传参
  #    4.运行对象=第三方的运行类（文件对象)，需要使用wb方式打开文件
  #    5.运行对象.run(套件对象)







  