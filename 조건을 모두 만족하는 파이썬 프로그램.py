# 허윤정(202258040)

# 이 프로그램은 사용자의 하루 기분 점수를 입력받아
# 평균을 계산하고 상태를 분석해주는 간단한 기분 관리 프로그램이다.

# ▶ 사용한 수업 외 함수 설명
# sum() : 리스트에 저장된 숫자들의 총합을 계산해주는 내장 함수
# len() : 리스트에 저장된 데이터의 개수를 알려주는 내장 함수

print("하루 기분 점수 관리 프로그램입니다.")
print("기분 점수는 1점(매우 나쁨)부터 5점(매우 좋음)까지 입력하세요.")

mood_scores = []     # 기분 점수를 저장할 리스트
day = 1              # 날짜를 나타내는 변수

# 반복문을 사용하여 5일간의 기분 점수 입력받기
while day <= 5:
    score = int(input(f"{day}일차 기분 점수를 입력하세요: "))

    # 조건문을 사용하여 올바른 점수인지 검사
    if 1 <= score <= 5:
        mood_scores.append(score)
        day += 1
    else:
        print("1에서 5 사이의 숫자만 입력해주세요.")

# 평균 계산
average = sum(mood_scores) / len(mood_scores)

print("\n기분 점수 분석 결과")
print("입력한 점수:", mood_scores)
print("평균 기분 점수:", round(average, 2))

# 평균 점수에 따른 상태 분석 (조건문 사용)
if average >= 4:
    print("전반적으로 기분이 매우 좋은 상태입니다.")
elif average >= 3:
    print("기분이 비교적 안정적인 상태입니다.")
elif average >= 2:
    print("기분이 조금 가라앉아 있는 상태입니다.")
else:
    print("최근 스트레스가 많은 상태입니다. 휴식이 필요합니다.")

print("프로그램을 종료합니다.")