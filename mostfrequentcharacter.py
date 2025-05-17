#most frequent character in a list
a = list(map(int,input().split()))
print(a)
#this hashmap stores the frequency of each integers in this list
freq={}
#running a loop through each element
for num in a:
#if the number has already arrived we add +1 to its frequency
    if num in freq:
        freq[num]+=1
#else the number arrive for first time means we make its frequency 1
    else:
        freq[num]=1
#this gets the most frequent number in the list
most_frequent=max(freq,key=freq.get)
#this prints the most frequent number
print(most_frequent)
