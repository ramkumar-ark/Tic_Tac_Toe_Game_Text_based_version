
class TicTacToe:

    def __init__(self):
        self.player1: str = "Player 1"
        self.player2: str = "Player 2"
        self.optionX: str = "X"
        self.optionO: str = "O"
        self.player_dict: dict = {self.optionX: None, self.optionO: None}
        self.board_values: dict = {}
        self.player_control: str = self.optionX
        self.get_board_values()
        self.is_bingo: bool = False
        self.is_draw: bool = False

    def get_board_values(self) -> None:
        """Assigns a key for each box of the board and space as the value for that key in the dictionary board_values.
        :param: None
        :returns: None
        """
        for r in [1, 2, 3]:
            for c in [1, 2, 3]:
                self.board_values[str(r) + str(c)] = " "

    @staticmethod
    def welcome_message() -> None:
        """Displays welcome message to the user.
        :param: None
        :returns: None
        """
        print("Hi, Welcome to the Tic Tac Toe Game.")

    def get_user_choice(self) -> None:
        """Obtain the player1's choice among the symbols X and O.
        :param: None
        :returns: None
        """
        user_choice = input("Hello Player 1, Please type the symbol (X or O) which you want to play with: ")
        if user_choice.upper() in list(self.player_dict.keys()):
            if user_choice.upper() == self.optionX:
                self.player_dict[self.optionX] = self.player1
                self.player_dict[self.optionO] = self.player2
            else:
                self.player_dict[self.optionX] = self.player2
                self.player_dict[self.optionO] = self.player1
        else:
            print("Sorry, you have entered an invalid choice. Please try again.")
            self.get_user_choice()

    def print_play_board(self) -> None:
        """Display the Tic Tac Toe play board with current values of the board.
        :param: None
        :returns: None
        """
        board_value_list: list[str] = list(self.board_values.values())
        board = f" {board_value_list[0]} | {board_value_list[1]} | {board_value_list[2]} \n" \
                f"___________\n" \
                f" {board_value_list[3]} | {board_value_list[4]} | {board_value_list[5]} \n" \
                f"___________\n" \
                f" {board_value_list[6]} | {board_value_list[7]} | {board_value_list[8]} \n"
        print(board)

    def change_player_control(self) -> None:
        """Switches the value of variable player_control.
        :param:None
        :returns:None
        """
        if self.player_control == self.optionX:
            self.player_control = self.optionO
        else:
            self.player_control = self.optionX

    def get_player_input(self) -> None:
        """Obtain input from the player for the board and store the value in the dictionary board_values.
        :param: None
        :returns: None
        """
        player_input = input(f"{self.player_dict[self.player_control]}, enter the coordinates of board you want to"
                             f" occupy: ")
        if player_input in self.board_values.keys():
            if self.board_values[player_input] == " ":
                self.board_values[player_input] = self.player_control
            else:
                print(f"Sorry {self.player_dict[self.player_control]} Row no {player_input[0]} "
                      f"column no {player_input[1]} is already occupied. Type co-ordinates of empty box of the board.")
                self.get_player_input()
        else:
            print("Sorry, please enter valid co-ordinates (ex- '12' for 1st row and 2nd column")
            self.get_player_input()

    def check_bingo(self) -> bool:
        """Checks whether there is any bingo/match in the board values and returns true or false respectively.
        :param: None
        :returns: Boolean
        """
        row_list: list[list[str]] = [[self.board_values[s] for s in self.board_values.keys() if s[0] == r] for r in
                                     ["1", "2", "3"]]
        column_list: list[list[str]] = [[self.board_values[s] for s in self.board_values.keys() if s[-1] == c] for c in
                                        ["1", "2", "3"]]
        diagonal_list: list[list[str]] = [[self.board_values[s] for s in l] for
                                          l in [["11", "22", "33"], ["31", "22", "13"]]]
        for bingo_list in [row_list, column_list, diagonal_list]:
            for individual_list in bingo_list:
                if individual_list == [self.player_control, self.player_control, self.player_control]:
                    return True
        return False

    def check_draw(self) -> bool:
        """Checks whether all the boxes in the board are occupied .i.e., there is no 'space' value in the dictionary
        board_values.
        :param: None
        :returns: Boolean
        """
        if " " not in list(self.board_values.values()):
            self.is_draw = True
            return True
        return False

    def declare_winner(self) -> None:
        """Displays the winner of the game to the user.
        :param: None
        :returns: None
        """
        if self.is_draw:
            print("Sorry players, No one wins! The game has ended in draw.")
        else:
            print(f"Bingo!\n{self.player_dict[self.player_control]} wins the game.")


def main():
    game = TicTacToe()
    game.welcome_message()
    game.get_user_choice()
    game.print_play_board()
    while not game.is_bingo:
        game.get_player_input()
        game.print_play_board()
        if game.check_bingo():
            game.is_bingo = True
        else:
            if game.check_draw():
                game.is_bingo = True
            else:
                game.change_player_control()
    game.declare_winner()


if __name__ == "__main__":
    main()
