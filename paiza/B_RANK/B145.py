import random

# 입력: 빙고판 크기 N과 추첨 숫자 개수 K
value_N_K = list(map(int, input("빙고판 크기 N과 추첨 수 K를 입력: ").split()))

# 빙고판 초기화 (N x N)
bingo = [0] * value_N_K[0]
for i in range(len(bingo)):
    bingo[i] = [0] * value_N_K[0]

# 빙고판 숫자 입력 받기
print("빙고판 숫자 입력:")
for i in range(value_N_K[0]):
    rand_input = list(map(int, input().split()))
    for j in range(value_N_K[0]):
        bingo[i][j] = rand_input[j]

# 추첨 숫자 입력 받기
choice_num = list(map(int, input("추첨된 숫자들을 입력: ").split()))

# 빙고판에서 추첨된 숫자를 0으로 바꿔서 체크 표시
for i in range(len(bingo)):
    for j in range(len(bingo)):
        for k in range(len(choice_num)):
            if bingo[i][j] == choice_num[k]:
                bingo[i][j] = 0  # 선택된 숫자는 0으로 처리 (빙고 체크용)

# 빙고 카운트 변수
bingo_ok = 0

# 가로 빙고 체크
for i in range(value_N_K[0]):
    if bingo[i] == [0] * value_N_K[0]:
        bingo_ok += 1

# 세로 빙고 체크
for j in range(value_N_K[0]):
    check = 0
    for i in range(value_N_K[0]):
        if bingo[i][j] == 0:
            check += 1
    if check == value_N_K[0]:
        bingo_ok += 1

# 대각선 (\ 방향) 빙고 체크
check = 0
for i in range(value_N_K[0]):
    if bingo[i][i] == 0:
        check += 1
if check == value_N_K[0]:
    bingo_ok += 1

# 대각선 (/ 방향) 빙고 체크
check = 0
for i in range(value_N_K[0]):
    if bingo[i][value_N_K[0]-1-i] == 0:
        check += 1
if check == value_N_K[0]:
    bingo_ok += 1

# 최종 빙고 개수 출력
print(bingo_ok)