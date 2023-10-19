import random

# Lamda & List Comprehension
create_board = lambda width, height: [['-' for _ in range(width)] for _ in range(height)]
display_board = lambda board: [print(' '.join(row)) for row in board]

# Generator
def generate_random_positions(width, height):
    for _ in range(3):
        yield (random.randint(0, height - 1), random.randint(0, width - 1))

# Pure Function
def check_game_result(player_y, player_x, goal_y, goal_x):
    return player_y == goal_y and player_x == goal_x

def setup_board(width, height, create_board, generate_random_positions):
    board = create_board(width, height)
    player_pos, goal_pos = generate_random_positions(width, height), generate_random_positions(width, height)

    try:
        player_y, player_x = next(player_pos)   
        goal_y, goal_x = next(goal_pos)

        board[player_y][player_x] = 'A'
        board[goal_y][goal_x] = 'O'

        return board, player_y, player_x, goal_y, goal_x

    except StopIteration:
        return None

def play_game_board(width, height, setup_board, display_board, check_game_result, create_board, generate_positions):
    while True:
        attempts = 0
        max_attempts = 3
        for _ in range(max_attempts):
            board, player_y, player_x, goal_y, goal_x = setup_board(width, height, create_board, generate_positions)

            if board is not None:
                print("\nnew board generated")
                display_board(board)

                generate_again = input("New position [y/n] ? ").lower()
                if generate_again == 'n':
                    break
            else:
                print("Failed to generate position. Please Try Again!!!")

            attempts += 1

        if attempts >= max_attempts:
            print("\nMaximum number of attempts reached. Exiting the game.")
            break

        while True:
            print("\nLet's play... This is your game board")
            display_board(board)

            moves = input("Enter is your move [w/a/s/d]: ").lower()

            for move in moves:
                if move == 'w':
                    if player_y > 0:
                        board[player_y][player_x] = '-'
                        player_y -= 1
                elif move == 'a':
                    if player_x > 0:
                        board[player_y][player_x] = '-'
                        player_x -= 1
                elif move == 's':
                    if player_y < height - 1:
                        board[player_y][player_x] = '-'
                        player_y += 1
                elif move == 'd':
                    if player_x < width - 1:
                        board[player_y][player_x] = '-'
                        player_x += 1
                else:
                    print("Invalid Move! Use WASD to Move.")
                    continue

                board[player_y][player_x] = 'A'
                print("\n")
                display_board(board)

                if check_game_result(player_y, player_x, goal_y, goal_x):
                    print("You Win")
                    return

            if not check_game_result(player_y, player_x, goal_y, goal_x):
                print("You Lose")

                generate_again = input("Wanna try again [y/n] ? ").lower()
                if generate_again == 'n':
                    print("See you again...")
                    return

def display_menu(play_game_board, setup_board, display_board, check_game_result, create_board, generate_random_positions):
    print("\n~~ Selamat datang dipermainan board game pemrograman fungsional ~~")
    print("----------------------------------------------------------------------------------")
    print("Anda (A) dapat berjalan secara horizontal dan vertikal untuk menuju target (O)\nGunakan keyboard ASDW untuk bergerak")
    print("----------------------------------------------------------------------------------")
    print("~~ Selamat bermain ~~\n")

    while True:
        try:
            width = int(input("Enter the board width: "))
            height = int(input("Enter the board height: "))
            if width <= 0 or height <= 0:
                raise ValueError("Width and Height must be greater than 0.")
            play_game_board(width, height, setup_board, display_board, check_game_result, create_board, generate_random_positions)
            break
        except ValueError as e:
            print(f"\nInvalid input: {e}\n")

if __name__ == "__main__":
    display_menu(play_game_board, setup_board, display_board, check_game_result, create_board, generate_random_positions)