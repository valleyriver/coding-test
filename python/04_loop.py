# 04. 반복문 for / while
# 기억할 것
# - range(10) 은 0~9, range(1, 11) 이 1~10
# - print('*', end=' ') 로 줄바꿈 대신 다른 문자로 마무리 가능
# - while은 증가식(x += 1)을 빼먹으면 무한루프
# - 리스트 순회는 for n in number (값), 인덱스가 필요하면 range(len(number))

# while 기본
x = 0
while x < 10:
    print('*')
    x += 1

x = 1
while x <= 10:
    print('*', end=' ')
    x += 1
print()

# for + range
for x in range(10):
    print('*')

for x in range(1, 11):
    print(x)

# ---------- 실습: 리스트에서 홀수만 출력 ----------
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1) 값으로 순회 (가장 파이썬다운 방식)
for n in number:
    if n % 2 == 1:
        print(f'{n}은(는) 홀수입니다.')

print()

# 2) 인덱스로 순회
for idx in range(len(number)):
    if number[idx] % 2 == 1:
        print(f'{number[idx]}은(는) 홀수입니다.')

print()

# 3) while로 순회
x = 0
while x < len(number):
    if number[x] % 2 == 1:
        print(f'{number[x]}은(는) 홀수입니다.')
    x += 1

print()
 
# 4) enumerate: 인덱스와 값을 한 번에 받기
# range(len()) 보다 짧고 읽기 쉬움. 시작 번호는 enumerate(number, 1) 처럼 지정 가능
for idx, n in enumerate(number):
    if n % 2 == 1:
        print(f'{idx}번째 원소 {n}은(는) 홀수입니다.')
 
print()
 
# 5) 리스트 컴프리헨션: 조건에 맞는 값만 모아 새 리스트 만들기
# n % 2 는 1이면 True, 0이면 False -> == 1 생략 가능
odds = [n for n in number if n % 2]
print(odds)
 
# TODO 다음 복습
# - zip() 으로 여러 리스트 동시에 순회
# - sorted(key=...) 로 정렬 기준 지정 2]