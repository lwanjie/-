print("hello world")
print(3+1)
print('hello \n world') #\ +转义功能的首字母 n--newline的首字母表示换行
print('hello \t world')  #\t 水平制表符，一组4个空格的位置
print('helloooo \t world')
print('hello \r world') #\r 回车把hello覆盖
print('hello \b world') #\b 退一个格将o退没了
print('http:\\\\www.baidu.com') #\\输出一个\，\\\\输出2个\
print('  老师说：\’大家好\‘  ')
print(r'hello \n world\\')
# 汉字“乘”与进制数的转换
print(chr(0b100111001011000)) #0b代表二进制
print(ord('乘'))   #得到'乘'所代表的十进制数
import time
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current time:" + time.asctime(t)
print(str)
import keyword
print(keyword.kwlist)   #查看所有的保留字
x=1+20
y=1+10+x
name = '玛丽亚'
print(name)
print(y)
print('标识',id(name))
print('标识',id(y))
print('leixing',type(y))
print('类型',type(name))
print('zhi',y)
print('值',name)
name = '玛丽亚'
print(name)
name = '楚留冰'
print(name)
n1 = 90
n2 = -76
n3 = 0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

#整数可以表示为二进制，十进制，八进制，十六进制
print('十进制',118)
print('二进制',0b10101111) #二进制以0b开头，0，1
print('八进制',0o176) #八进制以0o开头，0-7
print('十六进制',0x1EAF) #十六进制以0x开头，0-9，A-F
y='jhvjhv'
print(y,type(y))

a = 3.14159
print(a,type(a))

n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n2+n3)   #结果出现很多0，计算不准确，二进制的底层问题，会有误差
print(n1+n3)

from decimal import Decimal  #导入模块decimal解决不准确的问题
print(Decimal('1.1')+Decimal('2.2'))

f1 = True
f2 = False
print(f1,type(f1))
print(f2,type(f2))
#布尔值转化为整数计算
print(f1+1)  #2   1+1的结果为2，True表示1
print(f2+1)  #1   0+1的结果为1，False表示0

str1 = '人生苦短，我用Python'
print(str1,type(str1))
str2 = "人生苦短，我用Python"
print(str2,type(str2))
str3 = '''人生苦短，
  我用Python'''
print(str3,type(str3))
str4 = """人生苦短，
  我用Python"""
print(str4,type(str4))

name = '张三'
age = 20
print(type(name),type(age)) #说明name和age的数据类型不同

print('我叫' + name + '今年' + str(age) + '岁') #将int类型通过str()转换为str类型

print('---str()将其他类型转换成str类型---')
a = 10
b = 198.8
c = False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print('---int()将其他类型转换成int类型---')
s1 = '128'
f1 = 98.7
s2 = '76.77'
ff = True
s3 = 'hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))  #str转换成int类型，字符串为数字串
print(int(f1),type(int(f1)))  #float转换成int类型，只截取整数部分，舍去小数部分
#print(int(s2),type(int(s2)))  #str转换成int类型报错，因为字符串为小数串
print(int(ff),type(int(ff)))  #bool转换成int类型
#print(int(s3),type(int(s3)))  #str转换成int类型报错，字符串必须是数字串且是整数，非数字串不允许转换

print('---float()函数，将其他数据类型转换成float类型---')
s4 = '128.96'
s5 = '76'
ff1 = True
s6 = 'hello'
i = 98
print(type(s4),type(s5),type(s6),type(ff1),type(i))
print(float(s4),type(float(s4)))
print(float(s5),type(float(s5)))
print(float(ff1),type(float(ff1)))
#print(float(s6),type(float(s6)))  #字符串中数据为非数字串，不允许转换
print(float(i),type(float(i)))