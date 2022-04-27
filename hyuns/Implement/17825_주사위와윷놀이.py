# 다시 다시 다시

from collections import deque


def bfs(dice, player, path_mode):
    global answer
    q = deque()
    q.append([0, player, [-1, -1, -1, -1], 0])  # trial, player, path, all_sum

    while q:
        t, player_info, path, all_sum = q.popleft()
        if t == 10:
            answer = max(answer, all_sum)
            continue

        for idx in range(len(player_info)):
            tmp_playerInfo = player_info[:]  # for backtracking
            next_num, next_path = -1, path[:]

            # if arrival
            if tmp_playerInfo == -1:
                continue

            # if on blue
            if tmp_playerInfo[idx] >= 10 and tmp_playerInfo[idx] % 10 == 0:
                path_num = tmp_playerInfo[idx] // 10 - 1
                if path_num == 3:
                    break
                elif len(path_mode[path_num]) <= dice[t]:
                    step = dice[t] - len(path_mode[path_num])
                    next_num = path_mode[path_num][-1] + step * 5
                    next_path[idx] = -1
                else:
                    next_num = path_mode[path_num][dice[t]]
                    next_path[idx] = path_num

            # if in new_path
            elif path[idx] > 0:
                path_num = path[idx]
                now_pathIdx = path_mode[path_num].index(tmp_playerInfo[idx])
                if len(path_mode[path_num]) <= now_pathIdx + dice[t]:
                    step = now_pathIdx + dice[t] - len(path_mode[path_num])
                    next_num = path_mode[path_num][-1] + step * 5
                    next_path[idx] = -1
                else:
                    next_num = path_mode[path_num][dice[t]]
                    next_path[idx] = path_num

            # if 25
            elif tmp_playerInfo[idx] >= 25 and tmp_playerInfo[idx] % 5 == 0:
                if tmp_playerInfo[idx] + dice[t] * 5 > 40:
                    break
                else:
                    next_num = tmp_playerInfo[idx] + dice[t] * 5
                    next_path[idx] = -1

            else:
                next_num = tmp_playerInfo[idx] + dice[t] * 2

            # if arrival or Add
            if next_num == -1 or next_num in player_info:
                continue
            else:
                tmp_playerInfo[idx] = next_num
                q.append([t + 1, tmp_playerInfo, next_path, all_sum + next_num])


if __name__ == "__main__":
    dice = list(map(int, input().split()))
    start, arrival = 0, -1
    player = [start] * 4
    path_mode = [[13, 16, 19, 25], [22, 24, 25], [28, 27, 26, 25]]
    answer = 0

    bfs(dice, player, path_mode)

    print(answer)
