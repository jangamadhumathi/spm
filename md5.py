'''
A Module is python file consisting of functions
'''
'''
import day5
#print(dir(day5))
day5.check()
#print(type(day5.data))
#print(day5.data.keys())


#python provides a bunch of modules in-built
#such as time,random,os,math....

#math module-->it contains all mathematical
#constants,function,trigonometric...
import math
#help(math)
print(math.pi)
print(math.factorial(5))
print(math.log(1))
print(math.log10(1))
print(math.sqrt(25))
a = 25**0.5
print(a)
'''
#time module-->ftech current time,timer
#logic..
import time
#help(time)
d=time.time()#returns epoch time
#from 1970 jan1st
#print(d)
#we can check execution time of a program
'''for i in range(10):
    print(i**2)
    time.sleep(5)#sleep(seconds)halts
e = time.time()
print(e-d)#seconds
'''
#to get current date and time
#ctime
d=time.ctime()
print(d)
print(len(d))

e=time.localtime()
print(e)
#pick only date
d=e.tm_mday
m=e.tm_mon
y=e.tm_year
print(f'{d}/{m}/{y}')

















