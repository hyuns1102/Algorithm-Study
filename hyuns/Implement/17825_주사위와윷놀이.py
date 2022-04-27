def dfs(player, player_path, all_sum, d_num):
    global answer
    if d_num >= 10:
        answer = max(answer, all_sum)
        return

    for i in range(4):
        now_idx, board_idx = player[i], player_path[i]

        if now_idx == -1:  # 도착한 말
            continue

        step = dice[d_num]  # 주사위 step

        line = board[board_idx]  # 현재 라인

        next_idx = now_idx + step  # 다음 위치
        next_num = 0

        # 다음 위치가 배열을 넘어설 때, 도착
        if next_idx >= len(line):
            next_idx = -1

        # 다음 위치가 배열 안에 있을 때,
        else:
            next_num = line[next_idx]
            # 다음 위치가 다른 라인에 빠지는 지
            if board_idx == 0:
                if next_num == 10:
                    board_idx, next_idx = 1, 0
                elif next_num == 20:
                    board_idx, next_idx = 2, 0
                elif next_num == 30:
                    board_idx, next_idx = 3, 0

        # 다음 위치에 player가 있는지 검증, 도착 검증 x, 라인이랑 인덱스 일치 시, 분기점 체크
        same = False
        if next_idx != -1:
            for d in range(4):
                visit_idx, visit_path = player[d], player_path[d]
                if visit_idx == -1: continue
                if d != i and next_num == board[visit_path][visit_idx]:
                    if next_num == 30:
                        if visit_path == 3 and board_idx == 3 and next_idx == 0 and visit_idx == 0:
                            same = True
                            break
                        elif visit_path != 3 and board_idx != 3 and next_idx != 0 and visit_idx != 0:
                            same = True
                            break
                    elif next_num in [16, 22, 24, 26, 28]:
                        if visit_path == board_idx and visit_idx == next_idx:
                            same = True
                            break
                    else:
                        same = True
                        break

        # 다음 위치에 아무도 없다면, dfs
        if not same:
            c_player, c_player_path = player[:], player_path[:]  # copy for backtracking
            c_player[i], c_player_path[i] = next_idx, board_idx
            dfs(c_player, c_player_path, all_sum + next_num, d_num + 1)


if __name__ == "__main__":
    dice = list(map(int, input().split()))
    player_direction = [0] * 4
    board = [[i * 2 for i in range(21)],
             [10, 13, 16, 19, 25, 30, 35, 40],
             [20, 22, 24, 25, 30, 35, 40],
             [30, 28, 27, 26, 25, 30, 35, 40]]
    answer = 0

    # player 위치 (idx) , 라인 위치 (board idx), 누적 합, step
    dfs(player_direction, [0, 0, 0, 0], 0, 0)

    print(answer)

