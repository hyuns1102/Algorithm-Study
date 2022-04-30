# 13 : 14


def move_shark(graph, direct):
    global shark_num
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    update_graph = [item[:] for item in graph]

    # 시뮬레이션 시,
    # 점검은 원본 그래프로
    # 이동은 새로운 그래프로

    for x in range(len(graph)):
        for y in range(len(graph[x])):

            if graph[x][y][2]:  # 현 위치에 상어가 있다면,
                s_num = graph[x][y][1]  # 현재 상어 번호
                s_direct = direct[s_num]  # 현재 상어 방향

                # 원본 그래프에서 우선 순위에 따른 위치 점검
                p_flag1, p_flag2 = [], []
                for d in priority_graph[s_num][s_direct]:
                    if p_flag1 and p_flag2:
                        break
                    mx, my = x + dx[d], y + dy[d]
                    # 우선 순위에 따른 위치 확인
                    if 0 <= mx < N and 0 <= my < N:
                        if graph[mx][my] == [0, 0, False] and not p_flag1:  # 1. 아무 냄새가 없는 칸 ( 빈칸 )
                            p_flag1 = [d, mx, my]
                        elif (graph[mx][my][1] == s_num) and not p_flag2:  # 2. 자신의 냄새가 있는 칸
                            p_flag2 = [d, mx, my]

                # 업데이트 그래프에 이동,
                if p_flag1:
                    d, mx, my = p_flag1
                    s_direct = d
                    if update_graph[mx][my] == [0, 0, False]:  # 빈칸일 경우,
                        update_graph[mx][my] = [k, s_num, True]
                    else:  # 상어가 있을 경우,
                        if update_graph[mx][my][1] > s_num:  # 번호가 작은 상어가 잡아먹음
                            update_graph[mx][my] = [k, s_num, True]
                        shark_num -= 1  # 누구든 한마리는 잡아먹힘.
                elif p_flag2:
                    d, mx, my = p_flag2
                    s_direct = d
                    update_graph[mx][my] = [k, s_num, True]

                # 조건에 만족하면, 상어 방향 update, 상어 현 위치 업데이트
                direct[s_num] = s_direct
                update_graph[x][y][2] = False

    return update_graph


def erase_smell(graph):
    # 1초당 냄새 없애기, 방금 옮겨진 상어의 냄새는 건들지 않기.  graph update
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            if graph[x][y][1] > 0 and not graph[x][y][2]:
                graph[x][y][0] -= 1
            if graph[x][y][0] == 0:
                graph[x][y] = [0, 0, False]


if __name__ == "__main__":
    """
    - 상어 1번 최강 ( 1 <= x <= M )
    - N, N 격자, M 개의 상어
    - 상어 : 현재, 냄새 뿌림 -> 상하좌우 중 하나로 이동 -> 냄새 뿌림 / K 번 이동 후 냄새 사라짐
    - 상어 : 아무 냄새 없는 칸으로 이동 없으면,  자신의 냄새 칸으로 이동 / 특정 우선순위를 따름
    - 이동 후, 한 칸에 여러 마리일 경우, 가장 작은 번호만 남고 나머지 out
    - 우선 순위 표 (1 : 위, 2 : 아래, 3 : 왼쪽, 4 : 오른쪽)
    
    """

    N, M, k = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    shark_dir = [0] + list(map(int, input().split()))
    priority_graph = [[[], [], [], [], []] for _ in range(M + 1)]
    shark_num, answer = 0, -1  # 전체 상어 마리 수, 정답

    # 위, 아래, 왼, 오
    for idx in range(1, M + 1):
        for d in range(1, 5):
            priority_graph[idx][d] += list(map(int, input().split()))

    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] > 0:
                board[x][y] = [k, board[x][y], True]  # [ 냄새 지속 시간, 상어 번호, 현재 상어 위치 여부]
                shark_num += 1
            else:
                board[x][y] = [0, 0, False]

    T = 0
    while T != 1000:
        T += 1
        # 상어 이동, 상하좌우, 우선 순위
        board = move_shark(board, shark_dir)
        # 냄새 없애기
        erase_smell(board)
        # 전체 상어 마리 수가 1이면, break ( 1번 상어가 최강이므로, 한마리만 남았을 때)
        if shark_num == 1:
            answer = T
            break

    print(answer)
