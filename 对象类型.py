dir()#查看系统已经定义的名称

#Python区分大小写字母
a = 6
A = 4
a-A
print(a,A)

#观察对象类型
a = 9
type(a)

#0b、0o、0x分别表示二进位、八进位、十六进位
0b100
0o77
0x123

#浮点数
b = 9.0
b
type(b)

#浮点数在电脑中用二进制储存，故表达的是近似值
0.1 + 0.1 + 0.1

#布尔类型
False
True
False == 0
True == 1
True + 3
False + 3

#查看对象的布尔值
bool({})
bool("False")
bool(False)
bool(2)
bool(1)
bool(None)

#复数
ComplexNumber1=complex(3,6)
ComplexNumber1

#虚数单位不是用i表示，而是用j表示
# Note: Code in the next line will return an error message
3+6i
3+6j
4+7J
ComplexNumber2=4+6j
type(ComplexNumber2)

# 字符串
Job = 'Quant'
type(Job)
Job[0]
Job[1]

# 列表
L0 = [1, 2, 3]
L0[2]
L1 = ['Stock A','Stock B', 'Stock C']
L1[0]
L1[3]
L2 = [10, 'Price', ['Industry 1','Industry 2']]
L2
L2[2]
L2[2][1]

# 是否可变
x = 7
y = 7
print(id(x))
print(id(y))

z = x
x
z
print(id(z))
z = 8
x
id(x)
id(z)
x = 9
id(x)
x1 = 7
id(x1)
s1 = 'Hello World'
id(s1)
s1 = 'Hi World'
id(s1)
s1[0]
s1[0] = 'W'
L2[0] = 20
L2
L4 = L1
L4
L4[2] = 'Stock D'
L1

# 元组tuple
M = ('Market', 3.0, [10, 20, 30])
#若没加逗号，会理解为字符串
t1 = ('Single')
type(t1)
t2 = ('Single',)
type(t2)
#语义明确时可省略括号
t3 = 'x', 'y', 'z'
t3
type(t3)
#元组类型不可变
M[1]
M[1] = 2.0

# 字典dict
d1 = {'Stock A':30, 'Stock B':40}
d1['Stock A']

# 集合set
Winners = {'Company A','Company B'}
type(Winners)
Losers = set(['Company C', 'Company D'])
type(Losers)

#集合中的元素y故没有顺序关系，故以索引存取会报错
Winners[0]

#空集合只能用set（）函数创建，没包含任何元素的大括号表示的是空字典
S0 = {}
S1 = set()
type(S0)
type(S1)

set('Quant')
type( set('Quant') )

{'Quant'}
type( {'Quant'} )

L1 = [1, 2, 3]
L2 = [2, 2, 1, 3, 3]
set(L1)
set(L2)

set(L1) == set(L2)

class Asset(object):
    pass#创建类
asset1=Asset()
asset1
asset.id=001
asset2=Asset
asset2.price=12
asset2.price

class Asset(object):
    """
    Asset class with specified attributes "id" and "price".
    """
    
    def __init__(self, id, price):
        self.id = id
        self.price = price
        
    def print_id(self):
        print("The ID of the asset is: %s" %(self.id))
        #创建类并绑定一些非填不可的属性

