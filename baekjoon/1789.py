# 서로 다른 n개의 자연수의 합 S라고 한다. S를 알때 자연수 n의 최대값은 얼마일까

# 자연수 입력
N = int(input())

sum = 0
i = 1
while True:
    sum += i
    i += 1
    if N < sum:
        i -= 2
        break

print(i)