def move_fish(n_graph, dead):

    fish_cnt = 0
    while fish_cnt != 16:
        fish_cnt += 1
        cnt_flag = False
        if fish_cnt in dead:
            continue
        for x in range(len(n_graph)):
            for y in range(len(n_graph)):
                c, d = n_graph[x][y][0], n_graph[x][y][1]
                if c <= 0:  # 상어 or 빈칸
                    continue
                if c == fish_cnt:
                    cnt_flag = True
                    cnt_d = 0
                    while cnt_d != 9:
                        cnt_d += 1
                        mx, my = x + dx[d], y + dy[d]
                        if 0 <= mx < 4 and 0 <= my < 4 and n_graph[mx][my][0] >= 0:  # if fish, change
                            n_graph[x][y] = c, d
                            n_graph[x][y], n_graph[mx][my] = n_graph[mx][my], n_graph[x][y]
                            break
                        else:
                            d = 1 if d + 1 == 9 else d + 1
                    break
            if cnt_flag:
                break


def move(nx, ny, graph, dead):
    global all_sum
    move_fish(graph, dead)
    _, direct = graph[nx][ny]
    for mv in range(1, 5):
        shark_mx, shark_my = nx + dx[direct] * mv, ny + dy[direct] * mv
        # 상어 이동
        if 0 <= shark_mx < 4 and 0 <= shark_my < 4 and graph[shark_mx][shark_my][0] > 0:
            c_board = [item[:] for item in graph]
            m_fish_num, m_fish_direct = c_board[shark_mx][shark_my]
            dead.append(m_fish_num)
            c_board[nx][ny] = [0, 0]  # shark_empty
            c_board[shark_mx][shark_my] = [-1, m_fish_direct]  # shark_move
            move(shark_mx, shark_my, c_board, dead)
            dead.pop()

    all_sum = max(all_sum, sum(dead))
    return


if __name__ == "__main__":
    graph = [list(map(int, input().split())) for _ in range(4)]
    # info = [0] * 17
    board = []
    all_sum = 0

    for row in range(len(graph)):
        lst = []
        for col in range(0, len(graph[0]), 2):
            lst.append([graph[row][col], graph[row][col + 1]])
            # info[graph[row][col]] = [row, col, graph[row][col + 1]]
        board.append(lst)

    # 초기 상태
    num, direct = board[0][0]
    board[0][0] = [-1, direct]
    all_sum += num

    # 방향
    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

    # board : [fish_num, fish_dir]
    if direct == 5 or direct == 6 or direct == 7:
        move(0, 0, board, [num])
    print(all_sum)
