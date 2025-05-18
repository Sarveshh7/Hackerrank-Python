#write a program to print the following pattern
''' *
    **
    ***
    ****
    *****'''
a=int(input())
for i in range(1,a+1):
    print("*"*i)
#right angle triangle
for i in range(1,a+1):
    print(" "*(a-i),"*"*i)
