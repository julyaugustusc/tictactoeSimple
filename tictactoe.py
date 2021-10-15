board_values = [" "] * 9
user_values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def fill_blank():
    global board_values
    board_values = {key: " " for key in board_values}

def fill_valid_num():
    global board_values
    temp_list = list(range(1, 10))
    board_values = []
    for x in temp_list:
        board_values.append(str(x))

    for index, value in enumerate(user_values):
        if value != " ":
            board_values[index] = user_values[index]

def fill_user_values():
    global board_values
    board_values = user_values

def show_tictactoe():
    board = ["|-------|-------|-------|",
             "|   " + board_values[0] + "   |   " + board_values[1] + "   |   " + board_values[2] + "   |",
             "|-------|-------|-------|",
             "|   " + board_values[3] + "   |   " + board_values[4] + "   |   " + board_values[5] + "   |",
             "|-------|-------|-------|",
             "|   " + board_values[6] + "   |   " + board_values[7] + "   |   " + board_values[8] + "   |",
             "|-------|-------|-------|",
             ]
    for x in board:
        print(x)

def check_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def check_win():
    Xs_index = []
    Os_index = []

    #Check for possible wins: 1-2-3, 4-5-6, 7-8-9, 1-4-7, 2-5-8, 3-6-9, 1-5-9, or 7-5-3
    #indexs are -1 from these

    for index, value in enumerate(user_values):
        if value == "X":
            Xs_index.append(index)
        elif value == "O":
            Os_index.append(index)

    if all(x in Xs_index for x in [0, 1, 2]):
        print("X Wins!")
        return True
    elif all(x in Xs_index for x in [3, 4, 5]):
        print("X Wins!")
        return True
    elif all(x in Xs_index for x in [6, 7, 8]):
        print("X Wins!")
        return True
    elif all(x in Xs_index for x in [0, 3, 6]):
        print("X Wins!")
        return True
    elif all(x in Xs_index for x in [1, 4, 7]):
        print("X Wins!")
        return True
    elif all(x in Xs_index for x in [2, 5, 8]):
        print("X Wins!")
        return True
    elif all(x in Xs_index for x in [0, 4, 8]):
        print("X Wins!")
        return True
    elif all(x in Xs_index for x in [2, 4, 6]):
        print("X Wins!")
        return True
    elif all(x in Os_index for x in [0, 1, 2]):
        print("O Wins!")
        return True
    elif all(x in Os_index for x in [3, 4, 5]):
        print("O Wins!")
        return True
    elif all(x in Os_index for x in [6, 7, 8]):
        print("O Wins!")
        return True
    elif all(x in Os_index for x in [0, 3, 6]):
        print("O Wins!")
        return True
    elif all(x in Os_index for x in [1, 4, 7]):
        print("O Wins!")
        return True
    elif all(x in Os_index for x in [2, 5, 8]):
        print("O Wins!")
        return True
    elif all(x in Os_index for x in [0, 4, 8]):
        print("O Wins!")
        return True
    elif all(x in Os_index for x in [2, 4, 6]):
        print("O Wins!")
        return True
    else:
        return False

def play_game():
    global board_values

    count_turns = 1
    win = False

    print("Hello! Welcome to the game of tictactoe! Please note that X player goes first.")

    while not (count_turns > 9 or win):

        fill_valid_num()
        show_tictactoe()

        input_place = -1
        check_input = False
        while not (
                1 <= input_place <= 9 and user_values[input_place - 1] == " "
        ):
            input_place_temp = input("Please input a valid number and unused space to indicate which selection: ")
            if check_int(input_place_temp) == True:
                input_place = int(input_place_temp)

        board_values[input_place - 1] = " "

        if count_turns % 2 == 0:
            input_symbol = "O"
        else:
            input_symbol = "X"

        user_values[input_place - 1] = input_symbol

        count_turns+=1

        win = check_win()

    fill_user_values()
    show_tictactoe()
    if win == False:
        print("Cat's Game! No Winners!")


if __name__ == '__main__':
    play_game()
