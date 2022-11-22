check_all = 11
middle_num = 5
forward_num = middle_num - 1
backward_num = middle_num + 1


def is_over_board(x, y):
    if x < 0 or x > 14 or y < 0 or y > 14:
        return True
    return False

def get_lines(OmokBoardPut, x, y):
    lines = []
    for dx, dy in (1, 0), (1, 1), (0, 1), (1, -1):
        lines.append([])
        tmp_x, tmp_y = x - backward_num * dx, y - backward_num * dy
        for _ in range(check_all):
            tmp_x, tmp_y = tmp_x + dx, tmp_y + dy
            if is_over_board(tmp_x, tmp_y):
                lines[-1].append(3)
            else:
                lines[-1].append(OmokBoardPut[tmp_y][tmp_x])
    return lines

def get_count(line, color):
    stone_cnt = 0
    for i in range(middle_num):
        if line[i] != color:
            break
        stone_cnt += 1
    return (stone_cnt, i)

def get_state(line, color, depth):
    # 끊기지 않ㅅ고
    preline = line[::-1][backward_num:]
    prelt = get_count(preline, color)
    postline = line[backward_num:]
    postlt = get_count(postline, color)
    hap = prelt[0] + postlt[0] + 1
    if hap == 5:
        return 'five'
    elif hap > 5:
        return 'over_six'
    if depth > 1:
        return 'default'
    line_num = []
    for i in range(forward_num - prelt[1], -1, -1):
        if line[i] == 0:
            tmp_line = line.copy()
            tmp_line[i] = color
            # print(tmp_line, i, color)
            line_num.append(get_state(tmp_line, color, depth + 1))
    for i in range(backward_num + postlt[1], check_all):
        if line[i] == 0:
            tmp_line = line.copy()
            tmp_line[i] = color
            # print(tmp_line, i, color)
            line_num.append(get_state(tmp_line, color, depth + 1))
    if 'five' in line_num:
        if line_num.count('five') > 1:
            if hap == 4:
                return 'straight_four'
            else:
                return 'four_four'
        else:
            return 'four'
    elif 'straight_four' in line_num:
        return 'three'
    elif hap == 3:
        return 'week_three'
    elif hap == 2:
        return 'two'
    return 'default'

# def can_put(line, color):

def get_value_stone(OmokBoardPut, x, y): # 오목, 장목, 쌍사, 쌍삼
    res = 0
    for color in 1, 2:
        states = []
        for line in get_lines(OmokBoardPut, x, y):
            states.append(get_state(line, color, 0))
        if color == 1:
            res += 10
        if 'five' in states:
            res += 200
        elif 'over_six' in states:
            if color == 1:
                res += 0
            else:
                res += 200
        elif 'four_four' in states:
            if color == 1:
                res += 0
            else:
                res += 150
        elif states.count('straight_four') + states.count('four') >= 2:
            if color == 1:
                res += 0
            else:
                res += 150
        elif states.count('three') >= 2:
            if color == 1:
                res += 0
            else:
                res += 130
        elif 'straight_four' in states and 'three' in states:
            res += 120
        elif 'four' in states and 'three' in states:
            res += 115
        elif 'straight_four' in states:
            res += 80
        elif 'four' in states:
            res += 50
        elif 'three' in states:
            res += 40
        elif 'week_three' in states:
            res += 30
        elif 'two' in states:
            res += 10 * states.count('two')
        else:
            res += 5
    return res

def get_information_stone(OmokBoardPut, x, y, color): # 오목, 장목, 쌍사, 쌍삼
    states = []
    for line in get_lines(OmokBoardPut, x, y):
        states.append(get_state(line, color, 0))
        # print(states[-1])
    if 'five' in states:
        return 2
    elif 'over_six' in states:
        return 0
    elif 'four_four' in states:
        return 0
    elif states.count('straight_four') + states.count('four') >= 2:
        return 0
    elif states.count('three') >= 2:
        return 0
    else:
        return 1

# OmokBoardPut = []
# for y in range(15):
#     OmokBoardPut.append([])
#     for x in range(15):
#         OmokBoardPut[-1].append(0)

# OmokBoardPut[6][5] = 1
# # OmokBoardPut[7][5] = 1
# OmokBoardPut[8][5] = 1
# OmokBoardPut[9][5] = 1

# get_information_stone(OmokBoardPut, 5, 5, 1)