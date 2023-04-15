##############################################################################
# FILE: game.py
# WRITERS: Dana Aviran, 211326608, dana.av
# EXERCISE: Intro2cs2 ex9 2021-2022
# DESCRIPTION: A class of Game and the main program
##############################################################################


from car import Car
from board import Board
import sys
import helper


class Game:
    """
    this is a class of a general RUSH HOUR Game
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.board = board
        self.valid_colors = "YBOGRW"
        self.valid_directions = "udrl"

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it.

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        pass

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        boolean = True
        if self.board.cell_content(self.board.target_location()):
            print(board)
            print("you won the game")
            return None
        while boolean:
            print(board)
            user_input = input("insert move")
            if user_input == '!':
                boolean = False
                break
            name_of_car = user_input[0]
            direction = user_input[2]
            if name_of_car not in self.valid_colors:
                print("the color is not valid")
                continue
            elif direction not in self.valid_directions:
                print("the direction is not valid")
                continue
            else:
                if self.board.move_car(name_of_car, direction):
                    if self.board.cell_content(self.board.target_location()):
                        print(board)
                        print("you won the game")
                        boolean = False
                        break
                else:
                    print("your direction is not supported by the board")


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    board = Board()
    dictionary_of_cars = helper.load_json(sys.argv[1])
    lst_of_keys = list(dictionary_of_cars)
    list_of_valid_cars = []
    for i in range(len(lst_of_keys)):
        if lst_of_keys[i] in 'YBOWGR':
            name = lst_of_keys[i]
            parameters_of_car = dictionary_of_cars.get(lst_of_keys[i])
            length = parameters_of_car[0]
            location_row = parameters_of_car[1][0]
            location_column = parameters_of_car[1][1]
            orientation = parameters_of_car[2]
            if 2 <= length <= 4:
                if 0 <= location_column < 8 and 0 <= location_row < 8 or \
                        (location_row == 3 and location_column == 7):
                    if orientation == 1 or orientation == 0:
                        valid_car = Car(name, length, (location_row,
                                                       location_column),
                                        orientation)
                        if valid_car not in list_of_valid_cars:
                            list_of_valid_cars.append(valid_car)
    for i in range(len(list_of_valid_cars)):
        board.add_car(list_of_valid_cars[i])
    game = Game(board)
    game.play()
