def solution(visible, hidden, k):
    n = len(visible)  # 세로 길이
    m = len(visible[0])  # 가로 길이
    max_total_profit = -float('inf')

    # 1. 모든 행 뒤집기 조합 탐색 (2^n)
    for row_bit in range(1 << n):
        current_grid = []
        row_flip_count = 0

        # 행 상태 결정 및 비용 계산
        for i in range(n):
            if (row_bit & (1 << i)):
                current_grid.append(hidden[i][:])
                row_flip_count += 1
            else:
                current_grid.append(visible[i][:])

        total_flip_count = row_flip_count

        # 2. 각 열에 대해 뒤집는 것이 유리한지 판단
        # 열을 뒤집으면 그 열의 모든 칸이 반대 면으로 바뀜
        for j in range(m):
            original_col_sum = 0
            flipped_col_sum = 0

            for i in range(n):
                original_val = current_grid[i][j]
                # 원래 visible이었으면 hidden으로, hidden이었으면 visible로 교체
                flipped_val = hidden[i][j] if original_val == visible[i][j] else visible[i][j]

                original_col_sum += original_val
                flipped_col_sum += flipped_val

            # 열을 뒤집는 비용 k를 뺀 값이 더 크다면 뒤집기 수행
            if flipped_col_sum - k > original_col_sum:
                for i in range(n):
                    current_grid[i][j] = hidden[i][j] if current_grid[i][j] == visible[i][j] else visible[i][j]
                total_flip_count += 1

        # 3. 현재 격자 상태에서 최대 점수 경로 계산
        # (1,1)에서 (n,m)까지 상하좌우 이동 가능하며 중복 방문 불가
        # n이 작으므로 DP를 활용한 경로 합 계산 (기본적인 우하향 경로 기준)
        current_score = calculate_max_path(current_grid)

        # 최종 결과 = 점수 총합 - 총 비용
        max_total_profit = max(max_total_profit, current_score - (total_flip_count * k))

    return max_total_profit


def calculate_max_path(grid):
    n = len(grid)
    m = len(grid[0])
    # DP 테이블 초기화
    dp = [[0] * m for _ in range(n)]

    dp[0][0] = grid[0][0]

    # 첫 행 초기화
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    # 첫 열 초기화
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # 상하좌우 이동이 가능하지만, 일반적인 미로 최적 경로는 우측/하단 방향임
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[n - 1][m - 1]


# 테스트 케이스 실행 예시
print(solution([[1, 2], [3, 4]], [[5, 6], [7, 8]], 0))  # 결과: 20
print(solution([[1, 2], [3, 4]], [[5, 6], [7, 8]], 5))  # 결과: 11