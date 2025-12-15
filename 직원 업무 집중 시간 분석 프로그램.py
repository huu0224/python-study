# 이름 : 허윤정 (202258040)
# 프로그램 설명 : 직원의 일주일 업무 집중 시간을 입력받아 근무 패턴을 분석하는 프로그램
# 사용한 내장 함수(내장 클래스) : print(), input(), len(), sum(), int(), round(), list(), tuple(), dict()
# 사용한 문자열 메소드 : strip(), lower(), title()
# 사용한 리스트 메소드 : append(), sort()
# 사용한 튜플 메소드 : count(), index()
# 사용한 딕셔너리 메소드 : get(), keys(), values()

# ==================================================
# 업무 집중 시간 분석 프로그램
# ==================================================

print("업무 집중 시간 분석 시스템을 시작합니다.")

# 직원 기본 정보 입력
employee_name = input("직원 이름을 입력하세요: ").strip().title()
main_task = input("주요 담당 업무를 입력하세요: ").strip().lower()

print(employee_name, "님, 시스템에 접속하였습니다.")
print("주요 담당 업무:", main_task)

# 리스트: 일일 집중 근무 시간 저장
focus_hours = []
work_day = 1

while work_day <= 5:
    hours = int(input(f"{work_day}일차 집중 근무 시간을 입력하세요(시간): "))
    focus_hours.append(hours)
    work_day += 1

focus_hours.sort()
print("집중 근무 시간 기록:", focus_hours)

# 튜플: 근무 요일 정보
work_days = ("월", "화", "수", "목", "금")

print("근무 요일:", work_days)
print("월요일 근무 여부 확인:", work_days.count("월"))
print("목요일 위치:", work_days.index("목"))

# 딕셔너리: 업무별 평균 생산성 점수
productivity = {
    "development": 90,
    "design": 85,
    "planning": 80
}

print("업무 유형:", list(productivity.keys()))
print("평균 생산성 점수:", list(productivity.values()))

if productivity.get(main_task):
    print(main_task, "업무의 평균 생산성 점수는",
          productivity.get(main_task), "점입니다.")
else:
    print("해당 업무 유형에 대한 데이터가 없습니다.")

# 근무 패턴 분석
total_hours = sum(focus_hours)
average_hours = total_hours / len(focus_hours)

print("총 집중 근무 시간:", total_hours, "시간")
print("일 평균 집중 근무 시간:", round(average_hours, 2), "시간")

if average_hours >= 6:
    print("업무 집중도가 높은 편입니다.")
else:
    print("업무 집중도 개선이 필요합니다.")

print("시스템을 종료합니다. 수고하셨습니다.")