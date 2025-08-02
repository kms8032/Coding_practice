# 단어 입력
s = input("")

# 알파벳을 나열
alpabet = 'abcdefghijklmnopqrstuvwxyz'

# 각 알파벳을 처음 등장한 위치를 저장할 리스트들
s_save = []
alpabet_save=[]

for i in range(len(alpabet)): # 
    for j in range(len(s)):
        if alpabet[i] == s[j]: # 현재 알파벳이 문자열에 있으면
            if i not in alpabet_save: # 중복 제거
                s_save.append(j)
                alpabet_save.append(i)

# 초기값은 모두 -1로 채운 결과 리스트
output = [-1] * len(alpabet)

# 저장해둔 알파벳 인덱스를 기준으로, 그 알파벳이 처음 등장한 위치를 기록
h = 0
for k in alpabet_save: # 저장해둔 알파벳 인덱스를 꺼내면서
    output[k] = s_save[h] # 해당 알파벳 위치에 첫 등장 위치 저장
    h +=1  # 1:1 매칭되도록 인덱스 동기화

# 결과 출력 ( 리스트 형태가 아닌 공백으로 구분된 숫자 형태)
print(" ".join(map(str, output)))
