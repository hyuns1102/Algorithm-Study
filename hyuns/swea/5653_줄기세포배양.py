import sys
sys.stdin = open("input_5653.txt", "r")

T = int(input())


def update_status():
    spread_coord = []
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            if graph[x][y][2] == 0:  # no cell
                continue

            graph[x][y][1] += 1  # time update

            # update status
            if graph[x][y][0] == 1 and graph[x][y][1] == graph[x][y][2]:  # 비활성 -> 활성 상태
                graph[x][y][0] = 2

            elif graph[x][y][0] == 2 and graph[x][y][1] == graph[x][y][2] + 1:  # 활성 -> 번식 시작
                spread_coord.append([x, y])

            if graph[x][y][0] == 2 and graph[x][y][1] >= 2 * graph[x][y][2]:  # 활성 -> 죽음
                graph[x][y][0] = 0

    return spread_coord


def stretch_graph(n_graph, n_visit, flag):
    new_N, new_M = len(n_graph), len(n_graph[0])
    if flag == 0:
        n_graph += [[[0, 0, 0]] * new_M]
        n_visit += [[False] * new_M]
    elif flag == 1:
        for row in range(new_N):
            n_graph[row] += [[0, 0, 0]]
            n_visit[row] += [False]
    elif flag == 2:

        n_graph = [[[0, 0, 0]] * new_M] + n_graph
        n_visit = [[False] * new_M] + n_visit
    else:
        for row in range(new_N):
            n_graph[row] = [[0, 0, 0]] + n_graph[row]
            n_visit[row] = [False] + n_visit[row]

    return n_graph, n_visit


def spread_cell(graph, coord, n_visit):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    new_graph = [item[:] for item in graph]
    new_coord = coord[:]

    origin_N, origin_M = len(graph), len(graph[0])
    flag1 = flag2 = flag3 = flag4 = False
    # 배열 크기 증가
    for x, y in coord:
        if flag1 and flag2 and flag3 and flag4:
            break
        for i in range(4):
            mx, my = x + dx[i], y + dy[i]

            # x 가 끄트머리일 때,
            if mx == origin_N and not flag1:
                new_graph, n_visit = stretch_graph(new_graph, n_visit, 0)
                flag1 = True

            # y 가 끄트머리일 때,
            elif my == origin_M and not flag2:
                new_graph, n_visit = stretch_graph(new_graph, n_visit, 1)
                flag2 = True

            # x 가 0일 때
            elif mx == -1 and not flag3:
                new_graph, n_visit = stretch_graph(new_graph, n_visit, 2)
                new_coord = [[cx + 1, cy] for cx, cy in new_coord]
                flag3 = True
            elif my == -1 and not flag4:
                new_graph, n_visit = stretch_graph(new_graph, n_visit, 3)
                new_coord = [[cx, cy + 1] for cx, cy in new_coord]
                flag4 = True

    # 생명력 비교 후, 번식
    for x, y in new_coord:
        for i in range(4):
            mx, my = x + dx[i], y + dy[i]
            if not n_visit[mx][my] and new_graph[mx][my][2] <= new_graph[x][y][2]:
                new_graph[mx][my] = [1, 0, new_graph[x][y][2]]

    return new_graph, n_visit


def update_visit(n_visit):

    for x in range(len(graph)):
        for y in range(len(graph[0])):
            if graph[x][y][2] > 0:
                n_visit[x][y] = True


def count_cell():
    all_cnt = 0
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            if graph[x][y][0] > 0 and graph[x][y][2] > 0:
                all_cnt += 1
    return all_cnt


for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())  # K 배양 시간
    graph = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False] * M for _ in range(N)]

    # K 시간 후, 살아있는 줄기세포 ( 비활성 + 활성 )
    # 초기 배열 [ 상태, 시간, 생명력 수치 ] 로 변경
    # 초기 상태 , 죽은 상태 : 0, 비활성 상태 : 1, 활성 상태 : 2
    for x in range(N):
        for y in range(M):
            lst = [0, 0, 0]
            if graph[x][y] != 0:
                lst = [1, 0, graph[x][y]]
                visit[x][y] = True
            graph[x][y] = lst

    time = 0
    while time != K:
        time += 1
        coord = update_status()  # graph 소요시간 증가, 상태 update, 번식할 애들 좌표 가져오기
        graph, visit = spread_cell(graph, coord, visit)  # 번식하기 ( 배열 늘리기, 번식하기 )
        update_visit(visit)  # 활성, 비활성 cell 가져오기

    print(f"#{test_case} {count_cell()}")

