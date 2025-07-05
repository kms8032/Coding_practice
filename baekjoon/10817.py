# 세 정수, a b c가 주어진다. 이때 두 번째 큰 정수를 출력하는 프로그램을 작성

# a, b, c 입력 ( 공백을 기준으로 입력 )

a = list(map(int, input().split()))

# 오름차순 변경
a.sort()
print(a[1])