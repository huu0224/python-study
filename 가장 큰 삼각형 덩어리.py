from collections import deque


def solution(grid):
    n = len(grid)
    m = len(grid[0])

    # 방문 여부 체크 (n * m * 2 크기)
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    max_area = 0

    for i in range(n):
        for j in range(m):
            for k in range(2):
                if not visited[i][j][k]:
                    # 새로운 연결된 덩어리(Component) 탐색 시작
                    queue = deque([(i, j, k)])
                    visited[i][j][k] = True

                    count_a = 0
                    count_b = 0

                    while queue:
                        r, c, t = queue.popleft()

                        # 이분 그래프 컬러링: 한 칸에서 한 쪽만 선택되도록 그룹화
                        # (r + c + t)의 홀짝을 이용하면 인접한 삼각형은 반드시 다른 그룹이 됨
                        if (r + c + t) % 2 == 0:
                            count_a += 1
                        else:
                            count_b += 1

                        # 인접한 삼각형 찾기 (변을 공유하는 경우)
                        neighbors = []
                        if grid[r][c] == 1:  # '/' 방향 대각선
                            if t == 0:  # 왼쪽-위 삼각형
                                if r > 0: neighbors.append((r - 1, c, 1))  # 위쪽 칸의 아래쪽
                                if c > 0: neighbors.append((r, c - 1, 1))  # 왼쪽 칸의 오른쪽
                            else:  # 오른쪽-아래 삼각형
                                if r < n - 1: neighbors.append((r + 1, c, 0))  # 아래쪽 칸의 위쪽
                                if c < m - 1: neighbors.append((r, c + 1, 0))  # 오른쪽 칸의 왼쪽
                        else:  # '\' 방향 대각선
                            if t == 0:  # 오른쪽-위 삼각형
                                if r > 0: neighbors.append((r - 1, c, 1))  # 위쪽 칸의 아래쪽
                                if c < m - 1: neighbors.append((r, c + 1, 1))  # 오른쪽 칸의 왼쪽
                            else:  # 왼쪽-아래 삼각형
                                if r < n - 1: neighbors.append((r + 1, c, 0))  # 아래쪽 칸의 위쪽
                                if c > 0: neighbors.append((r, c - 1, 0))  # 왼쪽 칸의 오른쪽

                        for nr, nc, nt in neighbors:
                            if not visited[nr][nc][nt]:
                                visited[nr][nc][nt] = True
                                queue.append((nr, nc, nt))

                    # 해당 덩어리에서 선택 가능한 최대 삼각형 개수 갱신
                    max_area = max(max_area, count_a, count_b)

    return max_area


# 테스트 케이스 확인
print(solution([[-1, -1, -1], [1, 1, -1], [1, 1, 1]]))  # 결과: 5
print(solution([[1, -1, 1], [-1, 1, -1]]))  # 결과: 4
print(solution([[1]]))  # 결과: 1