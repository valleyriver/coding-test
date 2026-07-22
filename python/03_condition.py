# 03. 조건문 if / elif / else
# 기억할 것
# - if를 따로 쓰면 각각 독립 판단, elif로 묶으면 하나만 실행됨 (이거 때문에 결과가 갈림)
# - elif는 "위 조건이 거짓이고 + 자기 조건이 참"일 때만 실행
# - else는 위 조건들이 모두 거짓일 때 실행

# 헷갈렸던 부분: 아래는 if가 두 덩어리라 둘 다 검사됨
# a = 4 -> 첫 if 통과('오삼') + 아래 블록의 else('만세') 까지 출력
# 하나만 나오게 하려면 두 번째 if를 elif로 바꿔서 하나의 체인으로 합쳐야 함
a = int(input())
if a > 3:
    print('오삼')
if a < 1:
    print('냉면')
elif a > 5:
    print('불고기')
else:
    print('만세')

# 실습 1. 홀수/짝수 판별
n = int(input())
if n % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 실습 2. 양수 / 0 / 음수 판별
n = int(input())
if n > 0:
    print('양수')
elif n == 0:
    print('0')
else:
    print('음수')