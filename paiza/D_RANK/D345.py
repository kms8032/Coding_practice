# 당신으 아침, 낮, 밤 3번의 기온을 측정
# 개행 구분응로 아침, 낮 , 밤의 기온이 개행 구분으로 주어지므로 최고 기온을 출력

#입력
morning = int(input())
afternoon = int(input())
bam = int(input())

# 값을 리스트에 입력
temp_list = [morning, afternoon, bam]

# 오름차순으로 변경
re_temp_list = sorted(temp_list)
print(re_temp_list[2])

