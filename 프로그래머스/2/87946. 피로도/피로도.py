def solution(k, dungeons):
    return dfs(dungeons, [False] * len(dungeons), k, 0, 0)
    
def dfs(dungeons, visited, tired, maxCnt, cnt):
    # 가장 큰 값을 변경해서 반환하기 위한 m
    m = maxCnt
    # 던전을 탐색합니다.
    for i in range(len(dungeons)):
        # 방문하지 않은 던전이면서 입장이 가능한지 확인합니다.
        if not visited[i] and tired >= dungeons[i][0]:
            # 방문처리하고
            visited[i] = True
            # dungeonCnt를 들어가 다시 탐색합니다.
            m = dfs(dungeons, visited, tired - dungeons[i][1], m, cnt + 1)
            # i번을 들어갔다가 나온 경우 i+1을 들렸다가 갈 경우를 위해 false로 돌립니다.
            visited[i] = False
    # 둘 중에 큰 값을 반환합니다.
    return max(m, cnt)
