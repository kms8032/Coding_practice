# 현재 시간 입력
now_clock = list(map(int, input("").split()))
# 추가 시간 입력
plus_clock = int(input(""))
# 현재 시간을 전부 초 단위로 변경 후 추가 시간 더하기
sec = now_clock[0] * 3600 + now_clock[1] * 60 + now_clock[2] + plus_clock
# 더한 시간을 시간으로 바꾸기
hour = sec // 3600
min = (sec%3600)//60
sec = sec - (hour * 3600 + min * 60)

# 24시가 될 시 0시로 전환
while hour >= 24:
    hour -= 24
print(hour, min, sec)