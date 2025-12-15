# 이름 : 허윤정 (202258040)
# 프로그램 설명 : 사용자의 도서관 이용 기록을 입력받아 이용 습관을 분석하는 프로그램
# 사용한 내장 함수(내장 클래스) : print(), input(), len(), sum(), int(), round(), list(), tuple(), dict()
# 사용한 문자열 메소드 : strip(), lower(), title()
# 사용한 리스트 메소드 : append(), sort()
# 사용한 튜플 메소드 : count(), index()
# 사용한 딕셔너리 메소드 : get(), keys(), values()

# ==================================================
# 도서관 이용 기록 분석 프로그램
# ==================================================

print("도서관 이용 기록 분석 프로그램입니다.")

# 사용자 정보 입력
user_name = input("이름을 입력하세요: ").strip().title()
favorite_genre = input("가장 좋아하는 책 장르를 입력하세요: ").strip().lower()

print(user_name, "님 환영합니다.")
print("선호 장르:", favorite_genre)

# 리스트: 하루 이용 시간(시간 단위)
use_times = []
day = 1

while day <= 5:
    hours = int(input(f"{day}일차 도서관 이용 시간을 입력하세요(시간): "))
    use_times.append(hours)
    day += 1

use_times.sort()
print("이용 시간 기록:", use_times)

# 튜플: 고정된 요일 정보
days = ("월", "화", "수", "목", "금")

print("이용 요일:", days)
print("월요일 횟수:", days.count("월"))
print("목요일 위치:", days.index("목"))

# 딕셔너리: 장르별 추천 도서 수
books = {
    "novel": 120,
    "essay": 80,
    "science": 60
}

print("장르 목록:", list(books.keys()))
print("추천 도서 수:", list(books.values()))

if books.get(favorite_genre):
    print(favorite_genre, "장르 추천 도서 수는",
          books.get(favorite_genre), "권입니다.")
else:
    print("해당 장르는 등록되어 있지 않습니다.")

# 이용 시간 분석
total_time = sum(use_times)
average_time = total_time / len(use_times)

print("총 이용 시간:", total_time, "시간")
print("평균 이용 시간:", round(average_time, 2), "시간")

if average_time >= 2:
    print("도서관을 자주 이용하는 편입니다.")
else:
    print("도서관 이용이 적은 편입니다.")

print("프로그램을 종료합니다. 감사합니다.")