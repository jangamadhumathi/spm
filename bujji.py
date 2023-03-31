#control Structures-->if,elif,else,,
#for(collection/range),while,,,

#Repetition part
'''print(2*3)
print('2'*4)

for i in range(1,11):
     #print(i,end='')
     print('*'*i)#pattern repetition
'''
#nested loops--> one loop inside another
#for inside for..while inside while...
 #once internal loop is executed it goes for external loop
#loop
'''
for i in range(1,5):
    for j in range(1,5):
        print(f'i = {i},j {j}')

for i in range(1,6):
    for j in range(1,i+1):
        print(f'i = {i},j = {j}')

#below seenario also gives pattern
#of rght angled trngle with bettr look
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print("madhu")
    print()

#write a program to generate table pattern from 1 to 5
'''
'''1 2.....5
2 4     10
3 6     15
4
5
6
7
8
9
10..........50'''
'''
for i in range(1,6):
    for j in range(1,11):
        print(i*j,end='\t')#'\t'-->tab space
    print()
'''
#while -->only on test condition
#when we don't know the enndpoint we rely only
#on test expression
'''
while <test_expression>:
  statement(s).....
  ......

#print 1 to 10 numbers
for i in range(1,11)
  print(i)

i=1
while i<=10:
    print(i)
    i=i+1#counter variable 
'''
a=(1,5,8,9,3)
d=0 #output variable
'''
for i in a:
    d=d+i
print(d)

i=0 #counter variable
while i<len(a):
    #print(i,a[i])
    d=d+a[i]#indexing
    i=i+1
    print(d)
'''
#Write a program to print the below pattern
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

rows = int(input("Enter the number of rows"))
for i in range(rows):
    for j in range(i+1):
        print(j+1,end='')
    print()
'''
#A program to print inverted pyramid pattern
'''
* * * * *
* * * *
* * *
* *
*

rows = int(input("Enter"))
for i in range(rows,0,-1):
    print('*'*i)
for i in range(rows,0,-1):
    for j in range(0,i):
        print('*',end='')
    print()
'''
#Python-->Procedure Oriented + Object Orient
#Function -->A block of code that performs
#a specific task
#Syntax for Function:
'''
def fname(args): #fn defn
   """doc string(descrptn of fn)"""
   statement(s)...... #body of fn
   ......
   return value(s)...
print(fname(args))''' #fn call
'''
#Create a Function to perform sum of two integer
def add(a,b):
    """Sample demo"""
    return a+b
print(add(15,32))
print(add('code','gnan'))
print(add([1,2,5],[7,8,9]))
'''
#Create an Arithmetic function which takes
#3 args as a,b,c and performs addtn,multiplctn
#division,power
'''
def arth(a,b,c):
    """Arthmatic Function"""
    #c=a+b+c
    #d=a*b*c
    #return c,d
    return a+b+c,a*b*c,a/b/c,a**b**c
print(arth(5,2,3))
d,e,f = map(int,input("enter:").split(','))
print(arth(d,e,f))
'''
#Write a function  to get the Factorial of a given number
#5! = 5*4*3*2*1 or 1*2*3*4*5.....

n = int(input("Enter a value"))
def fact(n):
  d = 1 #output variable
  for i in range(1,n+1):
    d = d*i #d*=i
    return d
print(fact(n))
                 

















  































