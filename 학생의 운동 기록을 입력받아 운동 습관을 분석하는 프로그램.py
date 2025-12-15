# 이름 : 허윤정 (202258040)
# 프로그램 설명 : 사용자의 일주일 운동 기록을 입력받아 운동 습관을 분석하는 프로그램
# 사용한 내장 함수(내장 클래스) : print(), input(), len(), sum(), int(), round(), list(), tuple(), dict()
# 사용한 문자열 메소드 : strip(), lower(), title()
# 사용한 리스트 메소드 : append(), sort()
# 사용한 튜플 메소드 : count(), index()
# 사용한 딕셔너리 메소드 : get(), keys(), values()

# ==================================================
# 운동 기록 관리 프로그램
# ==================================================

print("운동 기록 관리 프로그램입니다.")

# 문자열 입력
name = input("이름을 입력하세요: ").strip().title()
favorite_exercise = input("가장 좋아하는 운동을 입력하세요: ").strip().lower()

print(name, "님 환영합니다.")
print("선호 운동:", favorite_exercise)

# 리스트: 운동 시간 저장
exercise_times = []
day = 1

while day <= 5:
    time = int(input(f"{day}일차 운동 시간을 입력하세요(분): "))
    exercise_times.append(time)
    day += 1

exercise_times.sort()
print("운동 시간 기록:", exercise_times)

# 튜플: 요일 정보
weekdays = ("월", "화", "수", "목", "금")

print("요일 목록:", weekdays)
print("월요일 등장 횟수:", weekdays.count("월"))
print("수요일 위치:", weekdays.index("수"))

# 딕셔너리: 운동별 소모 칼로리
calorie_table = {
    "running": 600,
    "walking": 300,
    "yoga": 200
}

print("운동 종류:", list(calorie_table.keys()))
print("칼로리 정보:", list(calorie_table.values()))

if calorie_table.get(favorite_exercise):
    print(favorite_exercise, "운동 시 평균 소모 칼로리는",
          calorie_table.get(favorite_exercise), "kcal입니다.")
else:
    print("해당 운동 정보가 없습니다.")

# 운동 분석
total_time = sum(exercise_times)
average_time = total_time / len(exercise_times)

print("총 운동 시간:", total_time, "분")
print("평균 운동 시간:", round(average_time, 2), "분")

if average_time >= 30:
    print("운동을 꾸준히 하는 편입니다.")
else:
    print("운동량이 부족한 편입니다.")

print("프로그램을 종료합니다. 감사합니다.")