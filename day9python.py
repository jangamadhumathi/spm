'''
Usage/Importance of underscores in python
->Single Underscore-->'_'
->Single Trailing underscore-->'var_'
-->Double leading underscore-->'__var'
-->Double leading and Double trailing underscore
(Python Special methods-->__var__)
'''
#Single Underscore:It is generally used for
#temporary purposes/to join multiple words
#snake case convention
'''
for _ in range(1,11):
    print(_,end='')

email_id ="jangamadhu128@gmail.com"
print(email_id)
mobile_no=2356897441
print(mobile_no)
'''

#Single Trailing underscore-->var_
#It is generally used in order to avoid name
#conflicts with Python Keywords
'''
def students(name,age,class_):
    print(f'{name} is of {age} years old in {class_} class')
students("madhu",19,15)
'''
#Double leading underscore-->__var
'''
class Details:
    """Usage of double leading underscore"""
    def __init__(self):
        self.name="madhu"
        self.place="Addanki"
        self.__age=20
a=Details()
print(dir(a))
#print(f'{a.name} is in {a._place} of {a.__age} old ')
print(f'{a.name} is in {a.place} of \
{a._Details__age} years old')
'''

#Special methods
'''
class Students:
    """Students class with basic details"""
    #def details(self):
    def __init__(self):#replace your mthd name with
        self.name="suresh"
        self.place="addanki"
        self.branch="EEE"
#a=Students()
#a.details()
#print(a.name)
a= Students()
print(a.name,"is in",a.place)
print(a.__dict__)#namespace
'''
#we pronounce as dunders
a=5;b=3
#print(a+b)

#print(a.__add__(25))
#print(a.__divmod__(b))#5//3-->1,5%3-->2
#print(a.__ge__(b))

a=[1,5,8,9,6]#aiwys check type first
#print(len(a))

#print(a.__getitem__(2))#a[2]

#Those Special Methods for any object are term as magic methods
'''
class Students:
    """Student class with Constructor"""
    def __init__(self,name="abc",marks=100):
        self.name=name
        self.marks=marks
        #instance methods
    def display(self):
            print(f'Student name is {self.name}')
            print(f'He/She got {self.marks} marks')
#a=Students()#default altributes
#a.display()
#b=Students("madhu",250)
#b.display()
    #Instance methodto evaluate grades
    def evaluate(self):
        if self.marks>=700:
            print(f'He/She secured First grade')
        elif self.marks>-500:
            print(f'He/She secured Second grade')
        else:
            print(f'Sorry you are failed prepare well')
#a=Students()
#a.display()
#a.evaluate()
#let's make it dynamic to accept n number
n=int(input("Enter the number of students"))
for i in range(n):
    x=input("Enter the student name")
    y=int(input("Enter the marks"))
    a=Students(x,y)
    a.display()
    a.evaluate()
    print('---------------')
'''
#A Function is like a House whereas class is like a power House

#Exception handling
#Errors that occur during executioncan be
#handled by try,except statements along with finally keyword
#Errors-->Runtime Errors,logical errors,Syntax errors

#Syntax errors-->invaild syntax,indentation,
#mismatch braces... learner

a,b=map(int,input("Enter the values").split(','))
#usage of assert(mainly for debugging)
#Syntax for assert-->assert expression,message
#assert a>0,"Enter only +ve numbers"
#print(a**b)
'''
try:
    a,b=map(int,input("Enter the values").split(','))
    print(a,b)
    assert a>0,"Enter only +ve numbers"
    print(a**b)
#except:
    #print("Wrong input")
except Exception as e:
    print(e)
'''
#Now we will write individual except blocks
try:
    a,b=map(int,input("Enter the values").split(','))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Enter Denominator other than zero")
except ValueError:
    print("Float/Str cannot be taken")
except Exception as e:
    print(e)
finally:
    print("Done")















