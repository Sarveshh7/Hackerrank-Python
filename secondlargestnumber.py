#to get the list input from user
a=list(map(int,input().split()))
#this removes the first max of a
a.remove(max(a))
#this prints the second largest max of a
print(max(a))
