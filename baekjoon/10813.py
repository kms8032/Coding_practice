# 입력
n, m = map(int, input().split())

# 리스트 컴프리헨션을 이용하여 리스트 안에 n개의 숫자를 나열
basket = [ i+1 for i in range(n)]

# 리스트 안에 숫자 i, j번째 수를 바꾸기
for m in range(m):
    # i, j 입력
    i, j = map(int, input().split())
    
    # i번째 공을 미리 다른 변수로 저장 ( j번째로 i번째를 덮을꺼라서 따로 저장 )
    k = basket[i-1]

    # i번째 공을 j번째 공으로  덮음
    basket[i-1] = basket[j-1]

    # 미리 따로 저장해놓은 i번째 공을 j번째 공으로 덮음
    basket[j-1] = k

# 출력
print(*basket)