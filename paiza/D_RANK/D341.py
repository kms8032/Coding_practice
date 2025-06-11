first = int(input())

second = int(input())

third = int(input())

vegetable = [first, second, third]
ranking = [0] * 3

if first > second:
    ranking[0] += 1
elif first < second:
    ranking[1] += 1

if second < third :
    ranking[2] += 1

elif second > third:
    ranking[1] += 1

if first < third :
    ranking[2] += 1
elif first > third:
    ranking[0] += 1

for a in range(3):
    if ranking[a] == 0:
        print(vegetable[a])