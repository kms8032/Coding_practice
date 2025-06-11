# 저작권이 있는 멜로디의 개수 / 앨범에 수록된 곡의 개수
# 평균갑은 항상 올림을 해서 정수로 만들어야 함

a_input = list(map(int, input("").split()))

b_output = a_input[0] * (a_input[1]-1)

c = b_output+1
print(c)