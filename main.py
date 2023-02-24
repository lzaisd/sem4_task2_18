import json


def read_from_file():
    f = open('input.json')
    load = json.load(f)
    f.close()
    return load


def write_to_file(arr):
    f = open('output.json', 'w')
    json.dump(arr, f)


def solve_elem(arr, flags, y, x, value):
    if y < 0 or x < 0 or x == len(arr[0]) or y == len(arr) or flags[y][x] < 0 or arr[y][x] != value:
        return 0
    flags[y][x] = -1
    result = 1
    result += solve_elem(arr, flags, y - 1, x, value)
    result += solve_elem(arr, flags, y, x - 1, value)
    result += solve_elem(arr, flags, y + 1, x, value)
    result += solve_elem(arr, flags, y, x + 1, value)
    return result


def fill(arr, flags, answer, y, x, number, friends_amount):
    if y < 0 or x < 0 or x == len(arr[0]) or y == len(arr) or flags[y][x] == -2 or arr[y][x] != number:
        return None
    flags[y][x] = -2
    answer[y][x] = friends_amount
    fill(arr, flags, answer, y - 1, x, number, friends_amount)
    fill(arr, flags, answer, y, x - 1, number, friends_amount)
    fill(arr, flags, answer, y + 1, x, number, friends_amount)
    fill(arr, flags, answer, y, x + 1, number, friends_amount)


inp_arr = read_from_file()
answer_arr = [[0] * len(inp_arr[0]) for _ in range(len(inp_arr))]
flag_arr = [[0] * len(inp_arr[0]) for _ in range(len(inp_arr))]

for row in range(len(inp_arr)):
    for col in range(len(inp_arr[0])):
        if flag_arr[row][col] == 0:
            friends_count = solve_elem(inp_arr, flag_arr, row, col, inp_arr[row][col])
            fill(inp_arr, flag_arr, answer_arr, row, col, inp_arr[row][col], friends_count - 1)


write_to_file(answer_arr)
