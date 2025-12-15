# 이름 : 허윤정
# 프로그램 설명 : 직원의 주간 업무 성과 데이터를 입력받아 근무 성과를 요약·분석하는 프로그램
# 사용한 내장 함수(내장 클래스) : print(), input(), len(), sum(), int(), round(), list(), tuple(), dict()
# 사용한 문자열 메소드 : strip(), lower(), title()
# 사용한 리스트 메소드 : append(), sort()
# 사용한 튜플 메소드 : count(), index()
# 사용한 딕셔너리 메소드 : get(), keys(), values()

# ==================================================
# 직원 업무 성과 분석 프로그램
# ==================================================

print("직원 업무 성과 분석 시스템입니다.")

# 직원 정보 입력
staff_name = input("직원 이름을 입력하세요: ").strip().title()
role = input("담당 직무를 입력하세요: ").strip().lower()

print(staff_name, "님의 성과 데이터를 분석합니다.")
print("담당 직무:", role)

# 리스트: 일별 업무 처리 건수
task_counts = []
day = 1

while day <= 5:
    tasks = int(input(f"{day}일차 처리한 업무 건수를 입력하세요: "))
    task_counts.append(tasks)
    day += 1

task_counts.sort()
print("일별 업무 처리 기록:", task_counts)

# 튜플: 근무 요일
workdays = ("월", "화", "수", "목", "금")

print("근무 요일 정보:", workdays)
print("월요일 포함 여부:", workdays.count("월"))
print("수요일 위치:", workdays.index("수"))

# 딕셔너리: 직무별 평균 처리 기준
performance_standard = {
    "development": 8,
    "design": 6,
    "planning": 5
}

print("직무 기준 목록:", list(performance_standard.keys()))
print("일 평균 기준:", list(performance_standard.values()))

if performance_standard.get(role):
    print(role, "직무의 일 평균 처리 기준은",
          performance_standard.get(role), "건입니다.")
else:
    print("해당 직무의 기준 데이터가 없습니다.")

# 성과 분석
total_tasks = sum(task_counts)
average_tasks = total_tasks / len(task_counts)

print("총 업무 처리 건수:", total_tasks, "건")
print("일 평균 처리 건수:", round(average_tasks, 2), "건")

if performance_standard.get(role) and average_tasks >= performance_standard.get(role):
    print("성과 기준을 충족하고 있습니다.")
else:
    print("성과 개선 여지가 있습니다.")

print("성과 분석을 종료합니다.")