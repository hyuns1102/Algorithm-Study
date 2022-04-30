import sys

sys.stdin = open("sample_input_5650.txt", "r")

T = int(input())


def game_start(x, y, d):
    cnt = 0
    direction_info = [[0, 2, 2, 1, 3, 2], [0, 0, 3, 3, 2, 3], [0, 3, 1, 0, 0, 0], [0, 1, 0, 2, 1, 1]]
    start_x, start_y = x, y
    while True:
        x += dx[d]
        y += dy[d]

        # 벽일 경우,
        if x < 0 or y < 0 or x >= N or y >= N:
            cnt += 1
            d = direction_info[d][-1]

        elif board[x][y] == -1 or (x, y) == (start_x, start_y):
            break

        elif 1 <= board[x][y] <= 5:
            cnt += 1
            d = direction_info[d][board[x][y]]

        elif 6 <= board[x][y] <= 10:
            x, y = worm_hole_info[(x, y)]

    return cnt


for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    worm_hole = [0] * 11
    worm_hole_info = dict()

    for x in range(len(board)):
        for y in range(len(board[x])):
            if 6 <= board[x][y] <= 10:
                n = board[x][y]
                if worm_hole[n] == 0:
                    worm_hole[n] = (x, y)
                else:
                    worm_hole_info[worm_hole[n]] = (x, y)
                    worm_hole_info[(x, y)] = worm_hole[n]

    answer = -1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                for d in range(4):
                    answer = max(answer, game_start(x, y, d))
    print(f"#{test_case} {answer}")
