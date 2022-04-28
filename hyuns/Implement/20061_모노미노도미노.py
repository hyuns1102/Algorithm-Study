
def move_block(bl, bg, gr):

    t, x, y = bl
    ax, ay = 0, 0

    if t == 2:
        ax, ay = 0, 1
    elif t == 3:
        ax, ay = 1, 0

    # move to green
    row = 0
    gr_row, gr_col, bg_row, bg_col = 0, 0, 0, 0
    # fix y, ay
    while row != len(gr):
        if gr[row][y] == 1:
            break
        elif t == 2:
            if gr[row][y + ay] == 1:  # 오른쪽에 1이 있을 경우,
                break
        elif t == 3:
            if row < len(gr) - 1 and gr[row + ax][y] == 1:  # 아래에 1이 있을 경우,
                break
            elif row == len(gr) - 1:  # 끄트머리일 경우,
                break
        gr_row, gr_col = row, y
        row += 1

    gr[gr_row][gr_col], gr[gr_row + ax][gr_col + ay] = 1, 1

    # move to blue
    col = 0
    while col != len(bg[0]):
        if bg[x][col] == 1:
            break
        elif t == 2:
            if col < len(bg[0]) - 1 and bg[x][col + ay] == 1:  # 오른쪽에 1이 있을 경우,
                break
            elif col == len(bg[0]) - 1: # 끄트머리일 경우,
                break
        elif t == 3:
            if bg[x + ax][col] == 1:  # 아래에 1이 있을 경우,
                break

        bg_row, bg_col = x, col
        col += 1

    bg[bg_row][bg_col], bg[bg_row + ax][bg_col + ay] = 1, 1


def erase_graph(n_graph, select_row):

    for row in range(select_row, 0, -1):
        for col in range(len(n_graph[row])):
            n_graph[row][col] = n_graph[row-1][col]

    n_graph[0][:] = [0] * len(n_graph[0][:])
    return n_graph


def check_block(graph):
    score = 0
    erase_row_second = 0

    # erase block
    while True:
        erase_row = []
        for x, lst in enumerate(graph):
            if x <= 1:
                continue
            if lst.count(1) == len(lst):
                erase_row.append(x)

        if not erase_row:
            break

        for row in erase_row:
            graph = erase_graph(graph, row)
            score += 1

    # check blur block
    if 1 in graph[0][:]:
        erase_row_second += 1
    if 1 in graph[1][:]:
        erase_row_second += 1

    for _ in range(erase_row_second):
        graph = erase_graph(graph, len(graph) - 1)

    return score


def count_block():
    b_graph = list(zip(*blue_graph))
    cnt = 0
    for x in range(len(green_graph)):
        cnt += green_graph[x].count(1) + b_graph[x].count(1)

    return cnt


def graph_transpose(graph):
    row, col = len(graph), len(graph[0])
    n_graph = [[0] * row for _ in range(col)]

    for x in range(len(n_graph)):
        for y in range(len(n_graph[0])):
            n_graph[x][y] = graph[y][x]

    return n_graph


if __name__ == "__main__":
    N = int(input())
    block = [list(map(int, input().split())) for _ in range(N)]  # t, x, y

    blue_graph = [[0] * 6 for _ in range(4)]
    green_graph = [[0] * 4 for _ in range(6)]

    all_score, cnt = 0, 0
    i = -1
    while i != N - 1:
        i += 1

        # make block in red_graph
        t, x, y = block[i]

        move_block(block[i], blue_graph, green_graph)

        # transpose
        blue_graph = graph_transpose(blue_graph)

        # erase
        all_score += check_block(blue_graph)
        all_score += check_block(green_graph)
        blue_graph = graph_transpose(blue_graph)

    cnt += count_block()
    print(all_score)
    print(cnt)
