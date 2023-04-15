##############################################################################
# FILE: board.py
# WRITERS: Dana Aviran, 211326608, dana.av
# EXERCISE: Intro2cs2 ex9 2021-2022
# DESCRIPTION: A class of a general board
##############################################################################

class Board:
    """
    this is the class Board - which creates a board of many kinds
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        # this function creates a board of size 7 - a two dimensional list.
        # it also has a list of cars that were added to the board.
        self.length = 7
        self.board = []
        for i in range(self.length):
            self.board.append([])
            for j in range(self.length + 1):
                self.board[i].append([])
        for i in range(self.length):
            for j in range(self.length + 1):
                if j == self.length and i != 3:
                    self.board[i][j] = ("*")
                elif j == self.length and i == 3:
                    self.board[i][j] = ("E")
                elif j < self.length:
                    self.board[i][j] = ("_")
        self.car_lst = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        print_board = ""
        for i in range(self.length):
            for j in range(self.length + 1):
                if type(self.board[i][j]) != str:
                    self.board[i][j] = self.board[i][j].get_name()
        for i in range(self.length):
            print_board += (str(self.board[i]))
            print_board += '\n'
        return print_board

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        cell_lst = []
        for i in range(self.length):
            for j in range(self.length):
                cell_lst.append((i, j))
        cell_lst.append(self.target_location())
        return cell_lst

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        row = car.location[0]
        col = car.location[1]
        if self.board[row][col] != '_' and self.board[row][col] != 'E':
            return False
        else:
            for i in range(len(self.car_lst)):
                if self.car_lst[i] == car or self.car_lst[i].get_name() == car.get_name():
                    return False
            if car.location[0] < 0 or car.location[0] >= self.length or \
                    car.location[1] < 0 or car.location[1] >= self.length:
                return False
            elif car.orientation == 0:
                boolean = True
                i = row
                counter = 0
                while i < self.length and counter < car.length:
                    if self.board[i][col] == '_':
                        counter += 1
                        i += 1
                    else:
                        boolean = False
                        break
                if boolean and counter == car.length:
                    i = row
                    counter = 0
                    while counter < car.length:
                        self.board[i][col] = car
                        counter += 1
                        i += 1
                    self.car_lst.append(car)
                    return True
                else:
                    return False
            elif car.orientation == 1:
                boolean = True
                j = col
                counter = 0
                while (j < self.length or (row == self.target_location()[0] and j == self.target_location()[1])) and counter < car.length:
                    if self.board[row][j] == '_' or self.board[row][j] == 'E':
                        counter += 1
                        j += 1
                    else:
                        boolean = False
                        break
                if boolean and counter == car.length:
                    j = col
                    counter = 0
                    while counter < car.length:
                        self.board[row][j] = car
                        counter += 1
                        j += 1
                    self.car_lst.append(car)
                    return True
                else:
                    return False

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        num_of_cars = len(self.car_lst)
        pos_move_lst = []
        for k in range(num_of_cars):
            location = self.car_lst[k].location
            i = location[0]
            j = location[1]
            possible_moves_of_car = self.car_lst[k].possible_moves()
            if "u" in possible_moves_of_car:
                if i - 1 >= 0:
                    if self.board[i - 1][j] == '_':
                        pos_move_lst.append((self.board[i][j], 'u', "up"))
                if i + 1 < self.length:
                    length_of_car = self.car_lst[k].length
                    if length_of_car + i < self.length:
                        if self.board[i + length_of_car][j] == '_':
                            pos_move_lst.append(
                                (self.board[i][j], 'd', "down"))
            elif "l" in possible_moves_of_car:
                length_of_car = self.car_lst[k].length
                target_location = self.target_location()
                if i != target_location[0]:
                    if j + length_of_car < self.length:
                        if self.board[i][j + length_of_car] == '_':
                            pos_move_lst.append(
                                (self.board[i][j], 'r', "right"))
                elif i == target_location[0]:
                    if j + length_of_car < self.length + 1:
                        if self.board[i][j + length_of_car] == '_' or \
                                self.board[i][j + length_of_car] == 'E':
                            pos_move_lst.append(
                                (self.board[i][j], 'r', "right"))
                if j - 1 >= 0:
                    if self.board[i][j - 1] == '_':
                        pos_move_lst.append((self.board[i][j], 'l', "left"))
        return pos_move_lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return 3, 7

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        row = coordinate[0]
        col = coordinate[1]
        if self.board[row][col] == '_' or self.board[row][col] == '*' or self.board[row][col] == 'E':
            return None
        else:
            return self.board[row][col]

    def move_car_in_board(self, movekey, location, length, orientation):
        """
        not in the API
        :param movekey:
        :param location:
        :param length:
        :param orientation:
        :return: None
        this function changes the board according to the valid move
        """
        row = location[0]
        col = location[1]
        if orientation == 0:
            if movekey == 'd':
                last_row_of_car = row + length - 1
                self.board[last_row_of_car + 1][col] = self.board[row][col]
                if row != 0:
                    self.board[row][col] = '_'
            elif movekey == 'u':
                last_row_of_car = row + length
                self.board[row - 1][col] = self.board[row][col]
                self.board[last_row_of_car - 1][col] = '_'
        elif orientation == 1:
            if movekey == 'r':
                last_col_of_car = col + length - 1
                self.board[row][last_col_of_car + 1] = self.board[row][col]
                if col >= 0:
                    self.board[row][col] = '_'
            elif movekey == 'l':
                last_col_of_car = col + length - 1
                self.board[row][col - 1] = self.board[row][col]
                self.board[row][last_col_of_car] = '_'

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        possible_move_lst = self.possible_moves()
        length_of_pos_moves = len(possible_move_lst)
        for k in range(length_of_pos_moves):
            if name in possible_move_lst[k] and movekey in possible_move_lst[k]:
                for i in range(len(self.car_lst)):
                    if self.car_lst[i].get_name() == name:
                        current_car = self.car_lst[i]
                        location = current_car.location
                        orientation = current_car.orientation
                        length_of_car = current_car.length
                        self.move_car_in_board(movekey, location,
                                               length_of_car,
                                               orientation)
                        current_car.move(movekey)
                        return True
        return False
