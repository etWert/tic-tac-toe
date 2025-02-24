from Player import Player


class Game:
    def __init__(self, board, players, current_player, moves, winner, turn_count):
        self.board = board
        self.players = players
        self.current_player = current_player
        self.moves = moves
        self.winner = winner
        self.turn_count = turn_count

    def display_board(self):
        print("------------")
        for line in self.board:
            for cell in line:
                if cell == 'x' or cell == 'o':
                    print("| " + cell + " ", end="")
                else:
                    print("|   ", end="")
            print("|")
            print("____________")

    def make_move(self, row, col):
        try:
            row = int(row)
            col = int(col)
            self.board[row][col] = self.current_player
        except IndexError:
            print("the place is not avalible")
            return False
        except ValueError:
            print("this is not a number' enter again")
            return False
        self.moves.add((row, col))
        return True

    def check_winner(self):
        # רוחב
        for line in self.board:
            if line == [self.current_player, self.current_player, self.current_player]:
                self.winner = self.players[self.current_player]
        # אורך
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                self.winner = self.players[self.current_player]
        # אלכסונים
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.winner = self.players[self.current_player]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            self.winner = self.players[self.current_player]
        if self.winner is not None:
            file=open("winners.txt","a")
            file.write("The winner is "+self.winner+"!\n")
            file.close()
    def switch_player(self):
        self.current_player = "o" if self.current_player == "x" else "x"

    def is_draw(self):
        # תיקו- אולי להוסיף בדיקות
        if self.turn_count == 8:
            return True
        return False

    #דקורטור שלא צריך כעת כי יש את ההדפסה בתוך הפונקציה שמנהלת את המשחק
    # def show_turn(func):
    #     def wrapper(self,*args,**kwargs):
    #         print(f'{self.players[self.current_player]} now is your turn')
    #         return func(self,*args,**kwargs)
    #     return wrapper

    # @show_turn
    def play(self):
        while True:
            print(f'{self.players[self.current_player]} now is your turn')
            row = input(f'enter row number')
            col = input(f'enter column number')
            while (row, col) in self.moves:
                print("the cell is not avalible")
                row = input(f'enter row number')
                col = input(f'enter column number')
            valid_cell=self.make_move(row,col)
            while valid_cell is False:
                row = input(f'enter row number')
                col = input(f'enter column number')
                valid_cell = self.make_move(row, col)
            self.display_board()
            if self.turn_count >= 5:
                self.check_winner()
                if self.winner is not None:
                    print(f'the winner is {self.winner}')
                    break
            if self.turn_count == 8:
                # זה במקום לזמן את הפונקציה של התיקו כי עדיין אין שם שום בדיקה
                print("the game over...")
                break
            self.switch_player()
            self.turn_count += 1
