# Things to improve after watching the Solution Overview for this Milestone project:
# - Some expressions can be simplified.
from random import randint

player_1 = ""  # Player_1 marker.
player_2 = ""  # Player_2 marker.
game_round = 1  # It counts rounds.
player1_turn = True  # Variable to know if it is player_1's turn.
game_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # It acts like Matrix.


def display_board(g_list):  # It shows the Tic Tac Toe board and its current values.

    print("---Tic Tac Board---\n"
          "     |     |    \n"
          f"   {g_list[6]} |  {g_list[7]}  | {g_list[8]}  \n"
          "-----------------\n"
          f"   {g_list[3]} |  {g_list[4]}  | {g_list[5]}  \n"
          "-----------------\n"
          f"   {g_list[0]} |  {g_list[1]}  | {g_list[2]}  \n"
          "     |     |    \n"
          )


def position_choice(g_list, player_one_turn):  # It selects a position on the board.

    # This original choice value can be anything that isn't in the acceptable_values list.
    choice = "0"
    acceptable_values = list(map(str, range(1, 10)))
    # While the choice is not in acceptable_values or g_list[choice] is different to " ", keep asking for input.
    while choice not in acceptable_values or g_list[int(choice) - 1] != " ":
        # We shouldn't convert here, otherwise we get an error on a wrong input.
        if player_one_turn:
            choice = input("Player 1 pick a position from 1 to 9 ")
        else:
            choice = input("Player 2 pick a position from 1 to 9 ")

        if choice not in acceptable_values:
            # This clears the current output below the cell.
            clear_output()
            display_board(g_list)
            print("Sorry, invalid value! choose a number from 1 to 9!")
        elif g_list[int(choice) - 1] != " ":  # Needs attention.
            clear_output()
            display_board(g_list)
            print("Sorry, invalid position! choose a free position!")

    # We can convert once the while loop above has confirmed we have a digit.
    return int(choice) - 1  # It is returned this way so that it matches the values in the list.


def coin_flip():
    who_stars = randint(0, 1)
    if who_stars == 0:
        return True  # If it is 0 Player_1 stars.
    else:
        return False  # If it is 1 Player_2 stars.


def clear_output():  # It cleans the Pycharm console.

    print("\n" * 20)


def new_match():  # It sets the game to its default state.

    clear_output()
    new_g_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    return "", "", 1, True, new_g_list


def replacement_choice(g_list, index_position, player1, player2, player_one_turn):  # It replaces a value on the board.

    if player_one_turn:
        g_list[index_position] = player1
        return g_list, False
    else:
        g_list[index_position] = player2
        player_one_turn = True

    return g_list, player_one_turn


def gameon_choice():  # It asks if the players want to play again.

    # This original choice value can be anything that isn't a Y or N.
    choice = "null"
    acceptable_values = ["Y", "N"]

    # While the choice is not in acceptable_values, keep asking for input.
    while choice not in acceptable_values:

        # We shouldn't convert here, otherwise we get an error on a wrong input.
        choice = input("Would you like to play again? Y or N ")

        if choice not in acceptable_values:
            # This clears the current output below the cell.
            clear_output()
            print("Invalid value, choose a valid letter (Y or N)")

    if choice == acceptable_values[0]:
        # Game is still on.
        return True
    else:
        # Game is over.
        return False


def check_winner(g_list, player1_marker, player2_marker):  # It checks for a winner or tied game.

    if (g_list[6] == player1_marker and g_list[7] == player1_marker and g_list[8] == player1_marker or
            g_list[3] == player1_marker and g_list[4] == player1_marker and g_list[5] == player1_marker or
            g_list[0] == player1_marker and g_list[1] == player1_marker and g_list[2] == player1_marker or
            g_list[0] == player1_marker and g_list[3] == player1_marker and g_list[6] == player1_marker or
            g_list[1] == player1_marker and g_list[4] == player1_marker and g_list[7] == player1_marker or
            g_list[2] == player1_marker and g_list[5] == player1_marker and g_list[8] == player1_marker or
            g_list[0] == player1_marker and g_list[4] == player1_marker and g_list[8] == player1_marker or
            g_list[2] == player1_marker and g_list[4] == player1_marker and g_list[6] == player1_marker):
        print("Congratulations!\n"
              "Player 1 Won!")
        return True  # We have a winner.
    elif (g_list[6] == player2_marker and g_list[7] == player2_marker and g_list[8] == player2_marker or
          g_list[3] == player2_marker and g_list[4] == player2_marker and g_list[5] == player2_marker or
          g_list[0] == player2_marker and g_list[1] == player2_marker and g_list[2] == player2_marker or
          g_list[0] == player2_marker and g_list[3] == player2_marker and g_list[6] == player2_marker or
          g_list[1] == player2_marker and g_list[4] == player2_marker and g_list[7] == player2_marker or
          g_list[2] == player2_marker and g_list[5] == player2_marker and g_list[8] == player2_marker or
          g_list[0] == player2_marker and g_list[4] == player2_marker and g_list[8] == player2_marker or
          g_list[2] == player2_marker and g_list[4] == player2_marker and g_list[6] == player2_marker):
        print("Congratulations!\n"
              "Player 2 Won!")
        return True  # We have a winner.
    elif " " in g_list:  # If there are free spaces on the board the game continues.
        pass
    else:
        print("Tied game!")
        return True

    return False  # We still don't have a winner.


def game_round_logic(g_round):  # It is executed every round.

    if g_round == 1:  # If it is the first round.
        clear_output()
        choice = "null"
        acceptable_values = ["X", "O"]
        player_one_turn = coin_flip()  # Deciding who goes first.

        # While the choice is not in acceptable_values, keep asking for input.
        while choice not in acceptable_values:

            if player_one_turn:
                # We shouldn't convert here, otherwise we get an error on a wrong input.
                choice = input("Hello Player 1, do you want to use 'X' or 'O'? ")
            else:
                choice = input("Hello Player 2, do you want to use 'X' or 'O'? ")

            if choice not in acceptable_values:
                # This clears the current output below the cell.
                clear_output()
                print("Invalid value, choose a valid symbol (X or O)")

        if player_one_turn:
            player1_selection = choice  # Saving the player1's selection.
            # It pops off(removes) the value player1 selected of the list and the other value is assigned to player2.
            acceptable_values.pop(acceptable_values.index(player1_selection))
            player2_selection = acceptable_values[0]  # Saving the player2's selection.
        else:
            player2_selection = choice  # Saving the player2's selection.
            # It pops off(removes) the value player2 selected of the list and the other value is assigned to player1.
            acceptable_values.pop(acceptable_values.index(player2_selection))
            player1_selection = acceptable_values[0]  # Saving the player1's selection.

        clear_output()
        print(f"Round: {g_round}")
        display_board(game_list)
        g_round += 1  # It adds up 1 to the variable.
        return player1_selection, player2_selection, g_round, player_one_turn
    else:  # If it is not the first round.
        g_round += 1  # It adds up 1 to the variable.
        return g_round


# Game Logic >>>
# Variable to keep playing:
game_on = True

while game_on:
    # If it is the first round of the match.
    if game_round == 1:
        player_1, player_2, game_round, player1_turn = game_round_logic(game_round)

    else:
        # If it is not the first round.
        game_round = game_round_logic(game_round)
    # Have player choose position.
    position = position_choice(game_list, player1_turn)

    # Rewrite that position and update game_list.
    game_list, player1_turn = replacement_choice(game_list, position, player_1, player_2, player1_turn)

    # Clear screen and show the updated game list.
    clear_output()
    print(f"Round: {game_round}")
    display_board(game_list)

    # Checking for the winner.
    if check_winner(game_list, player_1, player_2):
        game_on = gameon_choice()  # game_on state changes depending on the user's choice.
        if game_on:  # If game_on is true then this is executed:
            player_1, player_2, game_round, player1_turn, game_list = new_match()
else:
    clear_output()
    print("---Adios---")
