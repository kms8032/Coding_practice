# 과목 갯수 입력
N = int(input())
# 점수 입력
score = list(map(int, input().split()))

# 점수 중 최댓값으로 평균내기 ( 최댓값이 M 이라고 할 때, 점수/M * 100 을 모두 더한 후 과목 갯수로 나누기)
# 최대값은 100보다 작아야 함?
max_score = max(score)

avg = 0
for i in range(N):
    avg += score[i] / max_score * 100


print(avg/N)