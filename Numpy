# Section 10.1.1
import numpy as np
array1=np.array(range(6))#创建一维数组
print(array1)
array1.shape#查看数据结构
array1.shape=2,3#修改数据结构，改为二维，两行三列
print(array1)

array2=array1.reshape(3,2)#在array1基础上创建一个新结构的数组
print(array2)
array2.shape
array1.shape
array1[1,2]=88#1和2共用内存中的数据储存值，若更改其中任意一个数组的元素取值，另一个也改变
print(array1)
print(array2)

array3=np.array([[1,2,3], [4,5,6], [7,8,9]])#直接创建多维数组
print(array3)
array3.shape

array4=np.arange(13,1,-1)#创建等差序列形式的数组，不包含结束值（起始值、结束值、步长）
print(array4)
array4.shape=2,2,3
print(array4)

array5=array4.reshape(3,2,2)
array5

array6=np.linspace(1,12,12)#创建等差序列形式的数组，包含结束值（起始值、结束值、元素个数）
print(array6)
array6.dtype

array7=np.linspace(1,12,12,dtype=int)
print(array7)

a = np.zeros( (4,5) ) # 利用zeros()函数生成数组，全部为0
a
a.dtype#数据类型参数

np.ones((2,5,4),dtype=np.int16)

np.empty( (3,2) )

# Section 10.1.2
a1=np.linspace(1,26,6,dtype=int)
a1
a1[3]#索引
a1[1:3]
a1[:5]
a1[2:]
a1[-1]
a1[-3]
a1[:-1]
a1[2:-1]

a2=a1[0:3:1]#切片，1表示步长
a2
a1[0]=19
a2[0]#a1中元素值改了以后，a2元素值也改变



a1[[0,1,4]]
a3=a1[[0,3,2]]
a3
a1[0]=23
a3[0]

na1=np.array(np.arange(24),dtype=int).reshape(4,6)
print(na1)
na1[:2,1:]
na1[[2,3],[2,4]]
na1[2:,[2,4]]
na2=na1.reshape(2,3,4)
na2
na2[(1,1,2)]
na2[1,1,2]
na2[[1,1,0],[0,1,2],[2,3,1]]
na2[(1,1,1),(0,1,2),(2,3,1)]

# Section 10.1.3
ar1=np.array(np.arange(5))
ar1
np.add(ar1,4)#数组中每个元素都加4
ar2=np.array([2,3,4,5,6])
ar2
ar1+ar2#两个数组相加
np.add(ar1,ar2)
np.add(ar1,ar2,ar1)#将相加后的结果返回给ar1
ar1

a = np.array( [10,20,30,50,60] )
b = np.arange( 5 )
b
c=a-b
c
b**2
10*np.cos(a)
a<40
