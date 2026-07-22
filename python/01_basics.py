# 01. 파이썬 기본 문법
# 기억할 것
# - input()으로 받은 값은 항상 문자열 -> 숫자로 쓰려면 int() 형변환 필수
# - '3' + 5 는 TypeError, int('3') + 5 는 8
# - 출력 포매팅은 f-string만 써도 충분 (% / .format 은 옛날 문법)

# 변수 선언과 할당
a = 1        # int
b = '1'      # str
c = True     # bool

# 여러 변수에 동시 할당
a, b, c = 1, '1', True

# 같은 값을 여러 변수에 할당
americano = latte = 2000

# 타입 확인
print(type(1))       # <class 'int'>
print(type('1'))     # <class 'str'>
print(type(True))    # <class 'bool'>

# 비교 연산 결과는 bool
print(200 > 300)     # False

# 형변환 (casting)
string_number = '3'
# print(string_number + 5)   # TypeError
print(int(string_number) + 5)  # 8

# 문자열 포매팅
name = '홍길동'
age = 20

print("제 이름은 %s 이고 %d살 입니다." % (name, age))          # 구식
print("제 이름은 {0} 이고 {1}살 입니다.".format(name, age))     # 구버전
print(f'제 이름은 {name} 이고 {age}살 입니다.')                # 권장

# TODO 다음 복습: 코테용 입력 처리
# - sys.stdin.readline
# - map(int, input().split())