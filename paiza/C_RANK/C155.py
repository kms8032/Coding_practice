# 광고 키워드 입력
S = input().strip()
# .strip()은 앞뒤 공백을 제거
print(S)
# 메일 개수 입력
N = int(input())

# 메일 제목 입력 및 판정
for _ in range(N):
    title = input().strip()
    if S in title: # 특정 문자열이 다른 무낮열에 포함되어 있는지를 확인 예: "apple" in "pineapple" (True)
        print("Yes")
    else:
        print("No")