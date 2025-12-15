# 이름 : 허윤정 (202258040)
# 프로그램 설명 : 사용자의 카페 방문 기록을 입력받아 방문 패턴을 분석하는 프로그램
# 사용한 내장 함수(내장 클래스) : print(), input(), len(), sum(), int(), round(), list(), tuple(), dict()
# 사용한 문자열 메소드 : strip(), lower(), title()
# 사용한 리스트 메소드 : append(), sort()
# 사용한 튜플 메소드 : count(), index()
# 사용한 딕셔너리 메소드 : get(), keys(), values()

# ==================================================
# 카페 방문 기록 관리 프로그램
# ==================================================

print("카페 방문 기록 관리 프로그램입니다.")

# 문자열 입력
name = input("이름을 입력하세요: ").strip().title()
favorite_drink = input("가장 좋아하는 음료를 입력하세요: ").strip().lower()

print(name, "님 환영합니다.")
print("선호 음료:", favorite_drink)

# 리스트: 방문 횟수 저장
visit_counts = []
day = 1

while day <= 5:
    count = int(input(f"{day}일차 방문 횟수를 입력하세요: "))
    visit_counts.append(count)
    day += 1

visit_counts.sort()

print("방문 횟수 기록:", visit_counts)

# 튜플: 고정된 요일 정보
weekdays = ("월", "화", "수", "목", "금")

print("요일 목록:", weekdays)
print("월요일 등장 횟수:", weekdays.count("월"))
print("수요일 위치:", weekdays.index("수"))

# 딕셔너리: 메뉴 가격표
menu = {
    "coffee": 4500,
    "latte": 5000,
    "tea": 4000
}

print("메뉴 목록:", list(menu.keys()))
print("가격 목록:", list(menu.values()))

if menu.get(favorite_drink):
    print(favorite_drink, "가격은", menu.get(favorite_drink), "원입니다.")
else:
    print("해당 음료는 메뉴에 없습니다.")

# 방문 횟수 분석
total_visits = sum(visit_counts)
average_visits = total_visits / len(visit_counts)

print("총 방문 횟수:", total_visits)
print("평균 방문 횟수:", round(average_visits, 2))

if average_visits >= 2:
    print("카페를 자주 방문하는 편입니다.")
else:
    print("카페 방문이 적은 편입니다.")

print("프로그램을 종료합니다. 감사합니다.")