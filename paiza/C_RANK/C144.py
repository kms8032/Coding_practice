# 게임 판 수 입력
game = int(input())

# 게임에서 낸 것을 입력
result = []

for _ in range(game):
    result_input = list(map(str, input("").split()))

    result += result_input

# 그 입력에 대한 결과를 출력 (승리 횟수만 출력)
# G = 바위 C = 가위 P = 보
win = 0
lose = 0
draw = 0
for i in range(1, len(result),2):  
    if result[i-1] == result[i]: # 01 23 45 67 89 1011  
        draw +=1
    elif result[i-1] == 'G' and result[i] == 'C': # 승리
        win += 1
    elif result[i-1] == 'G' and result[i] == 'P': # 패배
        lose +=1
    elif result[i-1] == 'C' and result[i] == 'G': # 패배
        lose +=1
    elif result[i-1] == 'C' and result[i] == 'P': # 승리
        win += 1
    elif result[i-1] == 'P' and result[i] == 'C': # 패배
        lose +=1
    elif result[i-1] == 'P' and result[i] == 'G': # 승리
        win += 1

print(win)