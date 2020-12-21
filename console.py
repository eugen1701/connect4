from game import GameWonException, GameDrawException

class UI:
    def __init__(self, game):
        self._game = game
    def start(self):
        b = self._game.getBoard()
        playerTurn = True
        while True:
            try:
                print(b)
                if playerTurn == True:
                    colum = input('>>>')
                    self._game.playerMove(int(colum))
                else: self._game.computerMove()
                playerTurn = not playerTurn
            except GameWonException:
                if playerTurn == True:
                    print(b)
                    print("Congrats!")
                else:
                    print(b)
                    print("You were defeated!")
                return
            except GameDrawException:
                print(b)
                print("Game is a draw!")
                return
            except (ValueError, IndexError):
                print("bad move, user!")
                continue
