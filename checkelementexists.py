#To check for the numbers existence in a list
arr= list(map(int,input().split()))
#this prints the entered numbers
print(arr)
#asking the user to enter a number to check
x=input("number to check in list")
#returns a boolean value based on numbers existance
print(x in arr)
