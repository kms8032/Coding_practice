# 자연수를 담을 리스트 저장
numbers = []
# 자연수를 리스트에 저장
for i in range(10):
    numbers.append(int(input()))

# 리스트의 원소를 42로 나눈 나머지 구하기
mul_num = []
for i in range(10):
    mul_num.append(numbers[i]%42)

# 동일한 숫자가 있을 경우 지우기
re_mul_num = list(set(mul_num))

# 출력
print(re_mul_num)
print(len(re_mul_num))