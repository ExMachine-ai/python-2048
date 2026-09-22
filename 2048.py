import random
game_result = True
board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]
def merge(line):
    numbers = []
    for number in line:
        if number != 0:
            numbers.append(number)
    result = []
    i = 0
    while i < len(numbers):
        if i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:
            result.append(numbers[i] * 2)
            i += 2  
        else:
            result.append(numbers[i])
            i += 1
    while len(result) < 4:
        result.append(0)
    return result

def change_0(count):
    record_0 = []
    for i in range(4):
        for a in range(4):
            if board[i][a] == 0:
                record_0.append([i, a])
    if len(record_0) < count:
        count = len(record_0)
    new_record_0 = random.sample(record_0, count)
    population = [2, 4]
    weights = [0.9, 0.1]
    for i in range(count):
        change_num = random.choices(population, weights=weights, k=1)[0]
        hang = new_record_0[i][0]
        lie = new_record_0[i][1]
        board[hang][lie] = change_num

def game(userinput):
    if userinput == 'A':
        for i in range(4):
            line_A = []
            for a in range(4):
                line_A.append(board[i][a])
            result = merge(line_A)
            board[i] = result
    elif userinput == 'D':
        for i in range(4):
            line_A = []
            for a in range(3,-1,-1):
                line_A.append(board[i][a])
            result = merge(line_A)
            reverse_result = []
            for c in range (3,-1,-1):
                reverse_result.append(result[c])
            board[i] = reverse_result
    elif userinput == 'W':
        for i in range(4):
            colunm_A = []
            for a in range(4):
                colunm_A.append(board[a][i])
            result = merge(colunm_A)
            for c in range(4):
                board[c][i] = result[c]
    elif userinput == 'S':
        for i in range(4):
            colunm_A = []
            for a in range(3, -1, -1):
                colunm_A.append(board[a][i])
            result = merge(colunm_A)
            reverse_result = []
            for a in range(3, -1, -1):
                reverse_result.append(result[a])
            for c in range(4):
                board[c][i] = reverse_result[c]

def check_game():
    for i in range(4):
        if 2048 in board[i]:
            print("你赢了")
            return False
    for i in range(4):
        for a in range(4):
            if board[i][a] == 0:
                return True
            if a < 3 and board[i][a] == board[i][a + 1]:
                return True
            if i < 3 and board[i][a] == board[i + 1][a]:
                return True
    print("游戏结束")
    return False

change_0(2)

while game_result:
    for i in range(4):
        print(board[i])
    game_result = check_game()
    if game_result ==  False:
        break

    shangyici_board = []
    for i in range(4):
        old_line = []
        for a in range(4):
            old_line.append(board[i][a])
        shangyici_board.append(old_line)
    
    player_choice = input("选择上下左右 Use: W,S,A,D : ")
    game(player_choice)
    if board == shangyici_board:
        continue
    else:
        change_0(1)