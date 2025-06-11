# 정수 x의 배수의 몇번째 음모자는 선물 A
# 정수 Y의 배수의 몇번째 응모자는 선물 B

# 인원수
person = list(map(int, input("").split()))

for num  in range(1, person[0]+1):
    if num%person[1] == 0 and num%person[2] == 0:
        print('AB')
    elif num%person[1] == 0:
        print('A')
    elif num%person[2] == 0:
        print("B")
    else:
        print('N')

