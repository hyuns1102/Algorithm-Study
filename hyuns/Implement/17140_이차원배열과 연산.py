# from collections import Counter
#
#
# def make_graph(graph, new_arr, large_idx, row_col):
#     if row_col == 0:
#         cal_graph = [[0] * len(new_arr[large_idx]) for _ in range(len(graph))]
#         row_idx = 0
#         while row_idx != len(cal_graph):
#             cal_graph[row_idx][:len(new_arr[row_idx])] = new_arr[row_idx][:]
#
#             if len(cal_graph[row_idx][:]) > 100:
#                 cal_graph[row_idx][:] = cal_graph[row_idx][:100]
#             row_idx += 1
#     else:
#         cal_graph = [[0] * len(graph[0]) for _ in range(len(new_arr[large_idx]))]
#         col_idx = 0
#         while col_idx != len(cal_graph[0]):
#             for r in range(len(new_arr[col_idx])):
#                 if r < 100:
#                     cal_graph[r][col_idx] = new_arr[col_idx][r]
#                 else:
#                     break
#             col_idx += 1
#
#     return [item[:] for item in cal_graph]
#
#
# def calculate_R(graph):
#     new_row_array, large_row_size, large_row_idx = [], 0, 0
#     for row in range(len(graph)):
#         arr = graph[row]
#         sort_row, new_row = [], []
#         for number, count in Counter(arr).items():
#             if number != 0:
#                 sort_row.append([number, count])
#         sort_row = sorted(sort_row, key=lambda x: (x[1], x[0]))
#
#         for num, cnt in sort_row:
#             new_row.append(num)
#             new_row.append(cnt)
#
#         if len(new_row) > large_row_size:
#             large_row_idx = row
#             large_row_size = len(new_row)
#
#         new_row_array.append(new_row)
#
#     return make_graph(graph, new_row_array, large_row_idx, 0)
#
#
# def calculate_C(graph):
#     new_col_array, large_col_size, large_col_idx = [], 0, 0
#
#     for col in range(len(graph[0])):
#         arr, sort_col, new_col = [], [], []
#         for row in range(len(graph)):
#             arr.append(graph[row][col])
#
#         for number, count in Counter(arr).items():
#             if number != 0:
#                 sort_col.append([number, count])
#         sort_col = sorted(sort_col, key=lambda x: (x[1], x[0]))
#
#         for num, cnt in sort_col:
#             new_col.append(num)
#             new_col.append(cnt)
#
#         if len(new_col) > large_col_size:
#             large_col_idx = col
#             large_col_size = len(new_col)
#
#         new_col_array.append(new_col)
#
#     return make_graph(graph, new_col_array, large_col_idx, 1)
#
#
# if __name__ == "__main__":
#     want_row, want_column, want_k = map(int, input().split())
#     A_array = [list(map(int, input().split())) for _ in range(3)]
#
#     T, answer = 0, -1
#
#     if want_row - 1 < len(A_array) and want_column - 1 < len(A_array[0]):
#         if A_array[want_row - 1][want_column - 1] == want_k:
#             answer = T
#
#     if answer == -1:
#         while T != 100:
#             T += 1
#
#             if len(A_array) >= len(A_array[0]):
#                 A_array = calculate_R(A_array)
#             else:
#                 A_array = calculate_C(A_array)
#
#             if want_row - 1 < len(A_array) and want_column - 1 < len(A_array[0]):
#                 if A_array[want_row - 1][want_column - 1] == want_k:
#                     answer = T
#                     break
#
#     print(answer)


# 전치행렬 이용해서 다시 ㄱ