# 첫째 줄에는 양의 정수 A가 주어진다
# 두째 줄에는 연산자 + *가 주어진다.
# 셋쨰 줄에 양의 정수 B가 주어진다.
# A와 B는 모두 10의 제곱 형태이고, 길이는 최대 100자리이다.

A = int(input())
operator = input()
B = int(input())

if operator == "+":
    C = A + B
elif operator == "*":
    C = A * B

print(C)