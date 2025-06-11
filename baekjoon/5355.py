'''
@ = *3
% = +5
# = -7
'''

# 첫째 줄에는 테스트 게이스의 개수 T가 주언지다 다음 줄에는 화성 수학식이 한 줄에 하나씩 주어진다. 입력으로 주어지는 수는 정수이거나 소수 첫째자리까지 주어지며,
# 0 이상 100이하이다, 연산자는 최대 3개 주어진다.

T = int(input(""))

for _ in range(T):
    a = list(map( str, input("").split()))
    b = float(a[0])

    for num in range(len(a)) :
        if '@' == a[num]:
            b *= 3
        elif '#' == a[num]:
            b -= 7
        elif '%' == a[num]:
            b += 5
    print(f"{b:.2f}")