# 단어 입력
s = input("")

# 알파벳을 나열
alpabet = 'abcdefghijklmnopqrstuvwxyz'

# 알파벳을 쪼개고 단어를 쪼개고 인덱스 값 저장
s_save = []
alpabet_save=[]
for i in range(len(alpabet)):
    for j in range(len(s)):
        if alpabet[i] == s[j]:
            s_save.append(j)
            alpabet_save.append(i)


alpa = []
for a in range(len(alpabet_save)):
    alpa.append(alpabet_save[a])
    if alpa[a] in alpa[:a]:
        del alpa[a]
output = [-1] * len(alpabet)

h = 0
for k in alpa:

    output[k] = s_save[h]
    h +=1 
# 저장한 인덱스를 통해서 
print(output)
