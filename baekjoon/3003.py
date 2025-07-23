# 킹 1 퀸 1 룩 2 비숍 2 나이트 2 폰 8

horses = [1,1,2,2,2,8]

n = list(map(int,input().split()))

cal = [0,0,0,0,0,0]

for i in range(len(horses)):
    cal[i] = horses[i] - n[i]

print(*cal)