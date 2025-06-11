N = int(input())

score = [0] * N

ranking = [0] * N
for a in range(N):
    score[a] = int(input())

for b in range(0, N-1):
    if score[b+1] > score[b] :
        ranking[1] += 1
    if score[b+2] > score[b]:
        ranking[2] += 1
    if score[b+3] > score[b]:
        ranking[3] += 1


print(score)

print(ranking)