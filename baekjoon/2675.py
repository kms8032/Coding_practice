# 문자열 S르 입력받은 후에, 각 문자열 R번을 반복해서 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번을 반복하는 식으로 P를 만들면 된다.
# S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다

# 첫째 줄에 테스트 케이스의 개수 T, 문자열 S가 공백을 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘자 않는다.

T = int(input(""))
for _ in range(T):
    S = list(map(str, input("").split()))
    chars = list(S[1])
    P = ""
    for a in range(len(chars)):
        P += chars[a] * int(S[0])

    print(P)