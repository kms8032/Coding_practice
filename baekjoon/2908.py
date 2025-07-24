# 두 수를 입력 (두 수는 같지 않은 세자리)
a, b = map(str, input().split())
# 두 수를 반대로 나열
re_a = ""
re_b = ""
for i in range(3):
    re_a += a[2-i]
    re_b += b[2-i]
# 반대로 나열한 두 수를 비교
if int(re_a) > int(re_b):
    # 더 큰 수를 출력
    print(re_a)
else :
    print(re_b)
