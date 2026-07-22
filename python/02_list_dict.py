# 02. 리스트 & 딕셔너리
# 기억할 것
# - 슬라이싱 [1:4] 는 인덱스 1,2,3 (끝 인덱스 미포함)
# - print(*리스트) 하면 대괄호/쉼표 없이 값만 펼쳐서 출력
# - 딕셔너리는 해시 기반, key로 바로 접근 -> 조회가 빠름 (코테에서 자주 씀)
# - 중첩 구조는 바깥에서 안쪽으로 순서대로 [] 를 이어서 접근

# ---------- 리스트 ----------
my_list = ['java', 'django', 'c++', 'HTML', 'python']

print(my_list[0])       # 원소 접근
my_list[0] = 'python'   # 값 변경
print(my_list)
print(len(my_list))     # 길이

my_list = ['java', 'django', 'c++', 'HTML', 'python']
print(my_list[1:4])     # ['django', 'c++', 'HTML']
print(*my_list[1:4])    # django c++ HTML

# 실습: 장바구니 리스트
cart = ['키보드', '마우스', '모니터']
print(cart[0])
cart[1] = '헤드셋'
print(*cart)

# ---------- 딕셔너리 ----------
user = {'이름': '홍길동', '나이': 20, '성별': '남'}
print(user['나이'])
user['나이'] = 21
print(user['나이'])

my_info = {'name': '홍길동', 'age': 20, 'msg': '안녕하세요'}
print(my_info['msg'])

# 중첩 딕셔너리
profile = {
    'id': 'user01',
    'nickname': '길동',
    'level': 3,
    'studyterm': {
        'stcamp': '3days',
        'python': '2weeks',
        'algorithm': '6weeks',
    },
    111: '숫자도 key로 사용 가능',
}
print(profile['studyterm']['python'])

# ---------- 연습문제: 중첩 자료구조 탐색 ----------
book = {
    'bookInfo': {
        'title': '자료구조 입문',
        'titleEn': 'Introduction to Data Structures',
        'pages': '420',
        'publishedYear': '2023',
        'publishedDate': '20230310',
        'category': '전공서적',
        'languages': [{'languageNm': '한국어'}],
        'topics': [{'topicNm': '알고리즘'}, {'topicNm': '자료구조'}],
        'authors': [{'authorNm': '김저자', 'authorNmEn': 'KIM Jeoja'}],
        'reviewers': [
            {'reviewerNm': '이감수', 'reviewerNmEn': 'LEE Gamsu', 'role': '전체 감수'},
            {'reviewerNm': '박검토', 'reviewerNmEn': 'PARK Geomto', 'role': '예제 검증'},
            {'reviewerNm': '최교정', 'reviewerNmEn': 'CHOI Gyojeong', 'role': '교정'},
        ],
    }
}

# 1. 책 제목을 출력하시오.
print(book['bookInfo']['title'])

# 2. 저자의 영어 이름을 출력하시오. (리스트 안 딕셔너리 -> 인덱스 먼저)
print(book['bookInfo']['authors'][0]['authorNmEn'])

# 3. 감수에 참여한 인원 수를 출력하시오.
print(len(book['bookInfo']['reviewers']))

# 4. 두 번째 주제(topic)의 이름을 출력하시오.
print(book['bookInfo']['topics'][1]['topicNm'])