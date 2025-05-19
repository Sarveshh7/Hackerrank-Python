#To Remove duplicate elements
arr= list(map(int,input().split()))
#this prints the entered numbers
print(arr)
#this stores the non duplicated values
brr=[]
#loop through the original arr
for num in arr:
    #this adds the element only if it doesnt already exist in brr 
    if num not in brr:
        brr.append(num)
    #if the element exist in brr it breaks
    else:
        break
#this prints the non duplicate list
print(brr)
