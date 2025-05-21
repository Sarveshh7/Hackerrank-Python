#hackerrank question
student_marks={}
for i in range(int(input())):
    data=input().split()
    name=data[0]
    scores=list(map(float,data[1:]))
    student_marks[name]=scores
query=input()
print(f"{sum(student_marks[query]) / 3:.2f}")
