#!/usr/bin/python
import sys
print ("hello")

#dynamic typed
#int ,str

var=5.2

print(type(var))

var2="World"

var3=str(var)+var2


print(var3)


var4=6/7

print(var4)


#taking input from user from argument and keyboard
#string ,numbers,data types 

input_var=input("Enter a number")

print(input_var)


#taking input as argument

num1=sys.argv[1]
num2=sys.argv[2]
print (type(num2))
sum=int(num1)+int(num2)

print (sum)

#literals processing 

#string literals numeric literals boolean

test="""gtkjkjtjtjkjdkjd
jfjjfjjfkjfkfkkf"""

print(test)
#escaping the \ 
newline=r"Hey ! How are you  windows path \now i am  here?"

print (newline)

#boolean literals

ten=0b1010

print(ten)

hexd=0xa

print (hexd)