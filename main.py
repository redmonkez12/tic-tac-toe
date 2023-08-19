import random


def draw_board(board: list[str]) -> None:
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])


def get_player_move(board: list[str]) -> int:
    move = -1
    available_moves = range(1, 10)  # omit index zero

    while move not in available_moves or not board[move] == " ":
        try:
            move = int(input("What is your next turn? (1-9)"))  # transform to integer
        except ValueError:
            # warn the user about bad input if they write
            # anything other than number from 1 to 9
            print("Choose a number between 1 to 9")

    return move


def input_letter_player() -> tuple[str, str]:
    """
    Ask player for the mark and after then
    add marks to player and computer
    """

    letter = ""

    while not (letter == "X" or letter == "O"):
        print("Do you want X or O")
        letter = input().upper()

    if letter == "X":
        return "X", "O"
    else:
        return "O", "X"


def who_goes_first():
    """
    Choose randomly who goes first
    """
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"


def is_winner(board: list[str], player_latter: str) -> bool:
    return (
            (board[7] == player_latter and board[8] == player_latter and board[9] == player_latter) or
            (board[4] == player_latter and board[5] == player_latter and board[6] == player_latter) or
            (board[1] == player_latter and board[2] == player_latter and board[3] == player_latter) or
            (board[7] == player_latter and board[4] == player_latter and board[1] == player_latter) or
            (board[8] == player_latter and board[5] == player_latter and board[2] == player_latter) or
            (board[9] == player_latter and board[6] == player_latter and board[3] == player_latter) or
            (board[7] == player_latter and board[5] == player_latter and board[3] == player_latter) or
            (board[9] == player_latter and board[5] == player_latter and board[1] == player_latter)
    )


def is_board_full(board: list[str]) -> bool:
    for i in range(1, 10):
        if board[i] == " ":
            return False

    return True


def choose_random_from_list(board: list[str], move_list: list[int]) -> int | None:
    possible_moves = []

    for move in move_list:
        if board[move] == " ":
            possible_moves.append(move)

    if len(possible_moves) > 0:
        return random.choice(possible_moves)

    return None


def get_computer_move(board: list[str], computer_letter: str) -> int:
    if computer_letter == "X":
        player_letter = "O"
    else:
        player_letter = "X"

    for i in range(1, 10):
        board_copy = board[:]
        if board_copy[i] == " ":
            board_copy[i] = computer_letter
            if is_winner(board_copy, computer_letter):
                return i

    for i in range(1, 10):
        board_copy = board[:]
        if board_copy[i] == " ":
            board_copy[i] = player_letter
            if is_winner(board_copy, player_letter):
                return i

    move = choose_random_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    if board[5] == " ":
        return 5

    return choose_random_from_list(board, [4, 6, 8, 2])


while True:
    game_board: list[str] = [" "] * 10

    player_letter, computer_letter = input_letter_player()
    print(player_letter, computer_letter)
    turn = who_goes_first()
    print(f"{turn} goes first")

    is_running = True

    while is_running:
        if turn == "player":
            draw_board(game_board)

            player_move = get_player_move(game_board)
            game_board[player_move] = player_letter if turn == "player" else computer_letter

            if is_winner(game_board, player_letter):
                draw_board(game_board)
                print("You won")
                is_running = False
            else:  # new
                if is_board_full(game_board):
                    draw_board(game_board)
                    print("It's a draw!")
                    is_running = False
                else:
                    turn = "computer"
        else:
            move = get_computer_move(game_board, computer_letter)
            game_board[move] = computer_letter

            if is_winner(game_board, computer_letter):
                draw_board(game_board)
                print("You lost! Computer won!")
                is_running = False
            else:
                if is_board_full(game_board):
                    draw_board(game_board)
                    print("It's a draw")
                    is_running = False
                else:
                    turn = "player"  # switch the players

    if not input("Do you want to play again?").lower().startswith("y"):
        break
