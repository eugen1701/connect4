from game import  Board, Game
from console import UI
from AIalgorithms import BasicAlgorithm


b = Board()
AI = BasicAlgorithm()
g = Game(AI, b)
start = UI(g)
start.start()