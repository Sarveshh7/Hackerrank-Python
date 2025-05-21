n = int(input())
scores = set()
records = []

for _ in range(n):
    name = input()
    score = float(input())
    
    records.append([name, score])
    scores.add(score)

sortedScores = sorted(scores)
secondLowest = sortedScores[1]

names = [i[0] for i in records if i[1] == secondLowest]
names.sort()  

print(*names, sep="\n")
