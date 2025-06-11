# 나의 레벨과 전투 횟수 입력
my_level_and_stage = list(map(int,input("").split()))

# 각 전투에 대한 적의 레벨 입력
emeny_level = [0] * int(my_level_and_stage[0])
for a in range(len(emeny_level)):
    emeny_level[a] = int(input())

# 레벨이 높은 쪽이 승리
# 승리한 쪽은 상대 레벨의 절반(소수점이하 반올림)만큼 레벨이 상승하고, 패배한 쪽은 레벨이 절반(소수점 이하 반올림)이 됩니다.
# 또한 레벨이 같은 경우 전투는 무승부가 되고 레벨의 변동은 일어나지 않는다.

for fight in range(my_level_and_stage[0]):
    if my_level_and_stage[1] > emeny_level[fight]:
        my_level_and_stage[1] += int(emeny_level[fight])//2
    elif my_level_and_stage[1] < emeny_level[fight]:
        my_level_and_stage[1] = int(my_level_and_stage[1])//2
    else :
        continue

print(my_level_and_stage[1])

