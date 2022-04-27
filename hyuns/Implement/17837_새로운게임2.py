def update_info(player_info, player_group, player_num, param):

    for player in player_group:
        if player == player_num:  # diff direction
            player_info[player] = param
        else:  # same direction
            player_info[player] = [param[0], param[1], player_info[player][2]]


if __name__ == "__main__":
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    player_info = [list(map(int, input().split())) for _ in range(K)]

    T, answer = 0, -1
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    player_board = [[[] for _ in range(N)] for _ in range(N)]

    # register player
    for player_num, (r, c, d) in enumerate(player_info):
        player_board[r-1][c-1].append(player_num)

    # game start
    while True:
        T += 1
        if T > 1000 or answer > -1:
            break

        new_player_info = []
        for player_num, player in enumerate(player_info):
            r, c, d = player
            r, c = r - 1, c - 1
            mr, mc = r + dx[d], c + dy[d]  # move
            player_group = []

            # get player_group
            for idx in range(len(player_board[r][c])):
                if player_board[r][c][idx] == player_num:
                    player_group = player_board[r][c][idx:]
                    player_board[r][c] = player_board[r][c][:idx]
                    break

            # if you can move
            if 0 <= mr < N and 0 <= mc < N:

                if board[mr][mc] == 1:  # red
                    player_group = player_group[::-1]

                elif board[mr][mc] == 2:  # blue
                    d = d + 1 if d == 1 or d == 3 else d - 1
                    mr, mc = r + dx[d], c + dy[d]
                    if 0 <= mr < N and 0 <= mc < N:  # can move
                        if board[mr][mc] == 1:  # red
                            player_group = player_group[::-1]
                        elif board[mr][mc] == 2:  # blue
                            mr, mc = r, c
                    else:
                        mr, mc = r, c

            # if you can't move, same with blue
            else:
                d = d + 1 if d == 1 or d == 3 else d - 1
                mr, mc = r + dx[d], c + dy[d]
                if 0 <= mr < N and 0 <= mc < N:  # can move
                    if board[mr][mc] == 1:  # red
                        player_group = player_group[::-1]
                    elif board[mr][mc] == 2:  # blue
                        mr, mc = r, c
                else:  # can't move
                    mr, mc = r, c

            # move player group
            player_board[mr][mc] += player_group

            # condition of break
            if len(player_board[mr][mc]) >= 4:
                answer = T
                break

            # update player info
            update_info(player_info, player_group, player_num, [mr + 1, mc + 1, d])

    print(answer)
