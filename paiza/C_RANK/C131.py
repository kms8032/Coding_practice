# 독특한 방 번호
# 6, 9번은 회전하면 다른 숫자가 되는 특징이 있음 180도 회전해도 방 번호를어떤 정수로 읽을 수 있음
# 예 : 1068 -> 8901

# 이 성질을 가진 방 번호가 몇 개인지 궁금
# a번으로 시작하여 b번으로 긑나는 연속적인 방 번호의 방을 가지고 있습니다.
# 이 방 번호 중에서, 180도 회전하기 전과 후에 같은 번호로 읽을 수 있는 것이 몇개 ㅇㄴ찌 구하는 프로그램 작성
# 또한, 어느 방의 번호도 0으로 시작하는 일은 없다.

# a, b 입력
key_number = list(map(int, input().split()))

# 회전 매핑 정의
rotate_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
valid_digits = set(rotate_map.keys())

count = 0
for ii in range(key_number[0], key_number[1] + 1):
    sep = [int(d) for d in str(ii)]

    # 0으로 시작하는 경우는 제외
    if sep[0] == 0:
        continue

    # 유효한 숫자로만 이루어진 경우
    if all(d in valid_digits for d in sep):
        # 180도 회전한 숫자 만들기
        rotated = [rotate_map[d] for d in reversed(sep)]
        
        if sep == rotated:
            count += 1

# 결과 출력
print(count)
