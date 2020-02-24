def set_playground_size():
    valid = False
    while not valid:
        answer = input('Введи размер поля (от 3-х до 5-ти): ')
        try:
            answer = int(answer)
        except:
            print('На вход принимаются только числа')
            continue
        if answer >= 3 and answer <= 5:
            valid = True
        else:
            print(f'{answer} не входит в диапозон')
    return answer


def draw_board(size: int, board: list):
    print('--'*(size+1))
    for i in range(size):
        print('|', end = '')
        for j in range(size):
            if j<size-1:
                print(board[i][j], end = '|')
            else:
                print(board[i][j] + '|')
        print('--'*(size+1))

def counter(size: int, board: list):
    counter = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] != ' ':
               counter += 1
    return counter


def take_input(size: int, board: list, current_player: int, players_tokens: dict):
    valid = False
    while not valid:
        try:
            row, column = map(int, input(f'Игрок {current_player}, введите координаты ячейки через пробел: ').split())
            if row>0 and row<=size and column>0 and column<=size:
                if (str(board[row - 1][column - 1]) not in "XO"):
                    board[row-1][column - 1] = players_tokens[current_player]
                    valid = True
                else:
                    print('Эта ячейка занята, попробуйте снова')
            else:
                print('Такой ячейки нет')
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue

def check_win(size: int, board: list, current_player: int, players_tokens: dict):
    needed_token = players_tokens[current_player]
    for i in range(size):
        count_of_tokens = 0
        for j in range(size):
            if board[i][j] == needed_token:
                count_of_tokens += 1
        if count_of_tokens == size:
            return True
    for j in range(size):
        count_of_tokens = 0
        for i in range(size):
            if board[i][j] == needed_token:
                count_of_tokens += 1
        if count_of_tokens == size:
            return True
    count_of_tokens = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == needed_token and i==j:
                count_of_tokens += 1
        if count_of_tokens == size:
            return True
    count_of_tokens = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == needed_token and i+j==size:
                count_of_tokens += 1
        if count_of_tokens == size:
            return True
    return False

def change_player(current_player:int):
    if current_player == 1:
        return 2
    else:
        return 1

def game():
    current_player = 2
    players_tokens = {1: 'X', 2: 'O'}
    size = set_playground_size()
    board = [[' '] * size for i in range(size)]
    valid = False
    while not valid:
        current_player = change_player(current_player)
        take_input(size, board, current_player, players_tokens)
        draw_board(size, board)
        valid = check_win(size, board, current_player, players_tokens)
        if counter(size, board) == size ** 2:
            return print(f'Ничья!')
    return print(f'Игра окончена, выиграл игрок {current_player}!')

game()