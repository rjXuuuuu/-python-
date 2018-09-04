def my_subtraction(minuend , subtrahend):
    difference = minuend - subtrahend
    return difference#定义函数

i = 6; j = 2
d = my_subtraction(i,j)
d

d2 = my_subtraction(7,2.0)
d2#定义函数时函数及其参数类型都不需要声明

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x#表达式也可作为实际参数传入函数中
        
a=1

b=2

my_abs(a-b)

def hello():
    print('Hello World!')#函数也可不需要参数和返回值，但即使没有参数，函数名称之后的小括号仍不能遗漏
    
hello()

def donothing():
    pass#函数也可以完全没有任何执行动作，pass为空语句，一般被用作占位符

def my_arithmetic(x,y):
    z1 = x + y
    z2 = x - y
    return z1, z2
    
r1, r2 = my_arithmetic(7,5)
r1, r2
#如果需要回传一个以上的对象，可用tuple容器实现

my_subtraction(7,2)

my_subtraction(2,7)#函数调用时，传入的实参一般会按照位置顺序与形参绑定

my_subtraction(minuend = 7, subtrahend = 2)#也可在调用时写明实参与形参的绑定关系

my_subtraction(subtrahend = 2, minuend = 7)

# Notice: the next line will return an error message
my_subtraction(subtrahend = 2, 7)#若需同时传递位置参数与关键字参数，则位置参数的顺序应先于关键字参数，否则会报错

def my_print(arg1, arg2 = 'World!'):#定义参数时可以为参数指定默认值
    print(arg1, arg2)
    
my_print('Hi')
#指定参数默认值得b表达式只会被执行一次
expression = 'Hi'
def greeting(words = expression):
    print(words)
    
greeting()
expression = 'Hello'
greeting() # greeting() 的 预 设 值 仍 是 字 符 串 'Hi ’
#若函数中传递的参数属于可变对象，那么在函数内部对此对象的修改，会在函数执行后仍然有效并影响调用者
def change_obj(x,y):
    x[0] = 'A'
    y = 7
    
letters = ['a','b','c']
number = 6

change_obj(letters ,number)
letters , number
#若参数的默认值是可变对象，一旦函数内部修改了该可变对象，则默认值也随之改变
def growing_list(x,y=[]):
    y.append(x)
    print(y)
    
growing_list('a') # 默 认 值 本 来 是 空 列 表 ， 函 数 执 行 完 后 变 为 ['a']

growing_list('b')

growing_list('c')

growing_list('d')

#函数参数数目不确定时，可藉由容器类型的对象（如tuple、list、dict）进行传递
def my_addition0(addend):
    sum = 0
    for i in addend:
        sum = sum + i
    return sum
    
numbers0 = (1,2,3)

numbers1 = [1,2,3]

my_addition0(numbers0)

my_addition0(numbers1)

# 先把要传入的参数“打包”，否则会报错
my_addition0(1,2)

def my_addition1(*addend):
    sum = 0
    for i in addend:
        sum = sum + i
    return sum
    
my_addition1(1,2)

my_addition1(1,2,3)

def weighted_sum(x1,x2,*y):
    sum = 0
    size = len(y)
    weight = 0.3/size
    for i in y:
        sum = sum + weight*i
    sum = sum + 0.4*x1 + 0.3*x2
    return sum
    
weighted_sum(6,7,8,9,10)

# 匿名函数
#将一个无参数的函数greeting2改写为匿名函数greeting3
def greeting2():
    print('Hello World!')
    
greeting2()

greeting3 = lambda : print('Hello World!')
greeting3()
#在列表中嵌入函数的定义
def power2(x): return x**2

def power3(x): return x**3

def power4(x): return x**4

def power5(x): return x**5

L1 = [power2, power3, power4, power5]

for p in L1:
    print(p(3))
    
L2 = [lambda x: x**2, lambda x: x**3, lambda x: x**4, lambda x: x**5]

for p in L2:
    print(p(3))
    
# 作用域
#若变量名在代码文件内部、函数外部被fu赋值和创建，则其作用域是全局的
x = 6
x + 3

def fun1(value):
    return (x + value)

fun1(7)
#若在函作用数内部被复制和创建，则该变量作用域是本地的，在函数外部不可见
def fun2():
    y = 10
    
x + y
#若本地变量和全局变量名称相同，那么存取到的会是本地变量
def fun3(value):
    x = 60
    return (x + value)
#虽函数内部可访问到全局变量，但不能对其进行修改，或在变量前加上global声明语句
a = 10
def fun4():
    global a
    a = 20
    
fun4()
print(a)
