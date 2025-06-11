# R1 과 S는 기억하고 있어야 함
# 그렇다면 R2를 구할려면?

# S = (R1+R2)/2
# 
# R2 = 2 * S - R1 
R1_S = list(map(int, input().split()))
print(2 * R1_S[1] - R1_S[0])