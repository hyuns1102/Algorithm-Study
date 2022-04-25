from collections import deque


def comb_info(idx, v_info):  # how to use yield?
    if len(v_info) == M:
        info.append(v_info)
        return
    if idx == len(virus_info):
        return

    for ii in range(idx, len(virus_info)):
        comb_info(ii + 1, v_info + [virus_info[ii]])


def check(arr):
    for kx in range(len(arr)):
        for ky in range(len(arr[kx])):
            if arr[kx][ky] == -1 and graph[kx][ky] == 0:
                return False
    return True


def bfs(arr, que):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    distance = 0
    while que:
        nx, ny = que.popleft()
        for di in range(4):
            mx = nx + dx[di]
            my = ny + dy[di]

            if 0 <= mx < N and 0 <= my < N and graph[mx][my] != 1 and arr[mx][my] == -1:
                arr[mx][my] = arr[nx][ny] + 1
                if graph[mx][my] == 0:
                    distance = max(distance, arr[mx][my])
                que.append([mx, my])
    return distance


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    virus_info = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                virus_info.append([i, j])

    info = []
    comb_info(0, [])
    answer = 10e9

    for coord in info:
        dist_arr = [[-1] * N for _ in range(N)]

        q = deque()
        for x, y in coord:
            q.append([x, y])
            dist_arr[x][y] = 0
        dist = bfs(dist_arr, q)  # 최대 거리 재기

        if check(dist_arr):
            answer = min(answer, dist)

    if answer == 10e9:
        print(-1)
    else:
        print(answer)
