# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무언인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력 (대소문자로 이루어진 단어가 주어진다.)
# 문자열로 입력받기
word = input("")

# 출력은 대문자로 하기 때문에 대문자로 모두 변환
word = word.upper()

# 내가 작성한 입력값과 알파벳 순서대로 나열한 문자열을 비교하여 몇번 나와는지 확인
alpabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 알파벳이 몇번 나오는지 카운트하는 리스트 생성
letter_count = [0] * len(alpabet)

# 단어를 쪼개서 각 알파벳들이 몇번 나왔는지 카운트
for i in range(len(word)):
    for j in range(len(alpabet)):
        if word[i] == alpabet[j]:
            letter_count[j] += 1

# 리스트 컴프리헨션을 통해서 많이 나온 알파벳의 인덱스값을 저장 ( 최대값과 같은 최대값을 가진 모든 인덱스 찾기)
index = [ i for i, v in enumerate(letter_count) if v == max(letter_count)]
# enumerate(letter_count)
# 리스트를 인덱스와 값 쌍으로 만들어줌
# 동작 절차를 풀이하자면
# index = []
# for i, v in enumerate(letter_count):
#     if v == 3:
#         index.append(i)
# 즉, 리스트의 형태로 딕셔너리를 만든다고 생각하면 좋을듯
# v가 letter_count의 최대값이 같을때만 i(인덱스)값을 저장

# 출력 (가장 많이 사용된 알파벳을 대문자로 출력한다. 단 가장 만힝 사용된 알페벳이 여러 개 존재하는 경우에는 ?를 출력한다.)
if len(index) == 1:
    print(alpabet[index[0]])
else :
    print("?")