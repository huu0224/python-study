from itertools import permutations


def get_score(guess, secret):
    """두 숫자 사이의 Strike와 Ball 개수를 계산하는 함수"""
    guess = str(guess)
    secret = str(secret)
    strike = 0
    ball = 0

    for i in range(4):
        if guess[i] == secret[i]:
            strike += 1
        elif guess[i] in secret:
            ball += 1

    return f"{strike}S {ball}B"


def solution(n, submit):
    # 1. 1~9 사이의 서로 다른 숫자 4개로 이루어진 모든 후보 생성
    # 주의: 문제에서 1000~9999 정수라 했으므로 0은 포함되지 않고 1~9만 사용합니다.
    candidates = [''.join(p) for p in permutations('123456789', 4)]

    while candidates:
        # 2. 후보군 중 첫 번째 숫자를 선택하여 제출
        # (더 효율적인 선택을 위해 Minimax를 쓸 수 있지만, n=6 수준에선 보통 첫 번째로 충분합니다)
        guess = candidates[0]
        result = submit(int(guess))

        # 정답이면 즉시 반환
        if result == "4S 0B":
            return int(guess)

        # 3. 현재 제출한 숫자와 결과가 모순되는 후보들 제거
        # 즉, '가상의 정답'이 candidate일 때, 방금 던진 guess와의 결과가
        # 실제 받은 result와 다른 것들을 필터링합니다.
        new_candidates = []
        for cand in candidates:
            if get_score(guess, cand) == result:
                new_candidates.append(cand)

        candidates = new_candidates

    return 0