# 어떤 사람의 c언어 성적이 주어졌을때 , 평점은 몇점인지 출력하는 프로그램을 작성하시오
"""
A+: 4.3, A0: 4.0, A-: 3.7

B+: 3.3, B0: 3.0, B-: 2.7

C+: 2.3, C0: 2.0, C-: 1.7

D+: 1.3, D0: 1.0, D-: 0.7

F: 0.0
"""

# 입력
C = input("")
# 입력값에 대한 평점 출력
if C == "A+":
    print(4.3)
elif C == "A0":
    print(4.0)
elif C == "A-":
    print(3.7)
elif C == "B+":
    print(3.3)
elif C == "B0":
    print(3.0)
elif C == "B-":
    print(2.7)
elif C == "C+":
    print(2.3)
elif C == "C0":
    print(2.0)
elif C == "C-":
    print(1.7)
elif C == "D+":
    print(1.3)
elif C == "D0":
    print(1.0)
elif C == "D-":
    print(0.7)
elif C == "F":
    print(0.0)