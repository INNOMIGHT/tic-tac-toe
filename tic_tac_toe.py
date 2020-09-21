the_board = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '
}


def print_board(board):

    print(the_board['7'] + ' | ' + the_board['8'] + ' | ' + the_board['9'])
    print("---------")
    print(the_board['4'] + ' | ' + the_board['5'] + ' | ' + the_board['6'])
    print("---------")
    print(the_board['1'] + ' | ' + the_board['2'] + ' | ' + the_board['3'])


def game():

    turn = 'X'
    count = 0

    print("Player " + turn + " Goes First")

    for i in range(10):

        print_board(the_board)

        user_input = input()
        if the_board[user_input] == " ":
            the_board[user_input] = turn
            count += 1
        else:
            print("Error! The space is already filled up.")
            continue

        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':  # across the top
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':  # across the middle
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':  # across the bottom
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':  # down the left side
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':  # down the middle
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':  # down the right side
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':  # diagonal
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':  # diagonal
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

                # If neither X nor O wins and the the_board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


game()




