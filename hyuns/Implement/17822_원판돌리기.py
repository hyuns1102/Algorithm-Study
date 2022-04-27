from collections import deque


def rotate_graph(graph, command):
    x, d, k = command
    k = k % M if k >= M else k
    for num in range(x, len(graph), x):
        if d == 0:
            graph[num] = graph[num][M - k:] + graph[num][:M - k]
        else:
            graph[num] = graph[num][k:] + graph[num][:k]


def bfs(x, y, ch_num):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append([x, y])

    while q:
        nx, ny = q.popleft()
        for i in range(4):
            mx, my = nx + dx[i], ny + dy[i]

            # This is circle
            if my == -1:
                my = M-1
            elif my == M:
                my = 0

            if 1 <= mx < N + 1 and 0 <= my < M and graph[mx][my] == ch_num:
                graph[nx][ny], graph[mx][my] = 0, 0
                q.append([mx, my])


def change_graph(graph, average):

    for x in range(1, N + 1):
        for y in range(M):
            if graph[x][y] == 0:
                continue
            if graph[x][y] > average:
                graph[x][y] -= 1
            elif graph[x][y] < average:
                graph[x][y] += 1


if __name__ == "__main__":
    N, M, T = map(int, input().split())
    graph = [[0] * M] + [list(map(int, input().split())) for _ in range(N)]
    total_commands = [list(map(int, input().split())) for _ in range(T)]

    for command in total_commands:
        # rotate
        rotate_graph(graph, command)

        # delete near Num
        origin_graph = [item[:] for item in graph]
        number_cnt = 0
        for x in range(1, N + 1):
            for y in range(M):
                if graph[x][y] != 0:
                    number_cnt += 1
                    bfs(x, y, graph[x][y])

        # No delete
        if number_cnt == 0:
            break
        if origin_graph == graph:
            change_graph(graph, sum(map(sum, graph)) / number_cnt)

    print(sum(map(sum, graph)))
