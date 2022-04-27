def make_district(graph, boundary1, boundary2, district):
    [x1, x2], [y1, y2] = boundary1, boundary2
    cnt = 0
    if district == 1 or district == 3:
        for dx in range(x1, x2):
            for dy in range(y1, y2):
                if graph[dx][dy] == 5:  # start with begin
                    break
                graph[dx][dy] = district
                cnt += people_graph[dx-1][dy-1]

    if district == 2 or district == 4:
        for dx in range(x1, x2):
            for dy in range(N, y1 - 1, -1):  # start with end
                if graph[dx][dy] == 5:
                    break
                graph[dx][dy] = district
                cnt += people_graph[dx-1][dy-1]

    return cnt


def draw_boundary(kx, ky, dist1, dist2):
    graph = [[0] * (N+1) for _ in range(N+1)]
    graph[kx][ky] = 5

    # make boundary
    for bd1 in range(1, dist1 + 1):
        graph[kx + bd1][ky - bd1] = 5
        graph[kx + dist2 + bd1][ky + dist2 - bd1] = 5
    for bd2 in range(1, dist2 + 1):
        graph[kx + bd2][ky + bd2] = 5
        graph[kx + dist1 + bd2][ky - dist1 + bd2] = 5

    # get_district
    cnt_1 = make_district(graph, [1, kx + dist1], [1, ky + 1], 1)  # district 1
    cnt_2 = make_district(graph, [1, kx + dist2 + 1], [ky + 1, N + 1], 2)  # district 2
    cnt_3 = make_district(graph, [kx + dist1, N + 1], [1, ky - dist1 + dist2], 3)  # district 3
    cnt_4 = make_district(graph, [kx + dist2 + 1, N + 1], [ky - dist1 + dist2, N + 1], 4)  # district 4

    all_cnt = sum([sum(item[:]) for item in people_graph])
    cnt_5 = all_cnt - (cnt_1 + cnt_2 + cnt_3 + cnt_4)
    max_cnt, min_cnt = max(cnt_1, cnt_2, cnt_3, cnt_4, cnt_5), min(cnt_1, cnt_2, cnt_3, cnt_4, cnt_5)
    return max_cnt - min_cnt


if __name__ == "__main__":
    N = int(input())
    people_graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 10e9

    # Boundary coord
    boundary_coord = []
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            boundary_coord.append([x, y])

    for x, y in boundary_coord:
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if 1 <= x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
                    answer = min(answer, draw_boundary(x, y, d1, d2))

    print(answer)
