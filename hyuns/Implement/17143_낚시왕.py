
def move(arr, row, col, speed, direct, size):
    if direct == 1:
        row -= speed % ((R - 1) * 2)
        if row < 1:
            row = abs(row) + 2
            direct += 1
        if row > R:
            row = R - (row - R)
            direct -= 1
    elif direct == 2:
        row += speed % ((R - 1) * 2)
        if row > R:
            row = R - (row - R)
            direct -= 1
        if row < 1:
            row = abs(row) + 2
            direct += 1
    elif direct == 3:
        col += speed % ((C - 1) * 2)
        if col > C:
            col = C - (col - C)
            direct += 1
        if col < 1:
            col = abs(col) + 2
            direct -= 1
    else:
        col -= speed % ((C - 1) * 2)
        if col < 1:
            col = abs(col) + 2
            direct -= 1
        if col > C:
            col = C - (col - C)
            direct += 1

    # count shark
    shark = 0
    if not arr[row][col]:
        arr[row][col] = [speed, direct, size]
    elif arr[row][col][2] < size:
        shark += 1
        arr[row][col] = [speed, direct, size]

    return shark


if __name__ == "__main__":
    R, C, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]
    graph = [[0] * (C+1) for _ in range(R+1)]

    for r, c, s, d, z in info:
        graph[r][c] = [s, d, z]

    person_col = 0
    answer = 0
    # 1 : up, 2 : down, 3 : right, 4 : left

    while person_col < C:
        person_col += 1

        # get shark
        for r in range(1, R+1):
            if graph[r][person_col]:
                s, d, z = graph[r][person_col]
                answer += z
                graph[r][person_col] = 0
                M -= 1
                break

        if M == 0:
            break

        # move shark
        new_graph = [[0] * (C+1) for _ in range(R+1)]
        for x in range(R+1):
            for y in range(C+1):
                if graph[x][y]:
                    s, d, z = graph[x][y]
                    M -= move(new_graph, x, y, s, d, z)
        graph = [item[:] for item in new_graph]

    print(answer)


