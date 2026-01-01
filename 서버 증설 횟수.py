def serverCount(serverList, startTime, endTime):
    count = 0
    if len(serverList) > 0:
        for idx, val in enumerate(serverList):
            s, e, l = val
            if e == startTime:
                serverList[idx][2] = -1

    for x, y, e in serverList:
        if e == 0:
            count += 1

    return count


def solution(players, m, k):
    answer = 0
    serverList = []
    maxPlayer = m

    for idx, playerCount in enumerate(players):
        startTime = idx + 1
        endTime = startTime + k

        aliveServer = serverCount(serverList, startTime, endTime)

        if playerCount >= (aliveServer + 1) * m:

            serverAddCount = (playerCount - ((aliveServer + 1) * m)) // m + 1

            for _ in range(serverAddCount):
                serverList.append([startTime, endTime, 0])

            answer += serverAddCount

    return answer