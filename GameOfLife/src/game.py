"""
game.py - logika gry w życie Conwaya

Zawiera funkcje realizujące reguły automatu komórkowego Conwaya:
 - liczenie sąsiadów
 - generowanie nowego stanu planszy
"""

import numpy as np


SURVIVE={2,3}
"""Zestaw liczby sąsiadów, przy których żywa komórka przeżywa."""
BORN = {3}
"""Zestaw liczby sąsiadów, przy których martwa komórka się odradza."""



def count_neighbors(board,x,y):
    """
    Liczy liczbę żywych sąsiadów komórki w pozycji (x,y),
    uwzględniając tylko komórki w obrębie planszy (bez cyklicznych brzegów).

    :param board: Aktualna plansza gry (tablica 2D numpy)
    :type board: numpy.ndarray
    :param x: Wiersz komórki
    :type x: int
    :param y: Kolumna komórki
    :type y: int
    :return: Liczba sąsiadów żywych komórek
    :rtype: int
    """
    rows,cols=board.shape
    neighbors=0

    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx==0 and dy ==0:
                continue

            new_x,new_y=x+dx,y+dy
            if 0<=new_x <rows and 0<=new_y<cols:
                neighbors +=board[new_x,new_y]

    return neighbors


def next_generation(board):
    """
    Tworzy nową planszę na podstawie obecnego stanu i klasycznych reguł Conwaya.

     - Żywa komórka przeżywa jeśi ma 2 lub 3 sąsiadów
     - Martwa komórka odradza się, jeśli ma dokładnie 3 sąsiadów
     - Wszystkie inne komórki umierają lub pozostają martwe

    :param board: Aktualna plansza gry
    :type board: numpy.ndarray
    :return: Nowa plansza (kolejna generacja)
    :rtype: numpy.ndarray
    """
    rows,cols=board.shape
    new_board = np.zeros((rows,cols),dtype=int)

    for x in range(rows):
        for y in range(cols):
            neighbors=count_neighbors(board,x,y)

            if board[x,y] == 0 and neighbors in BORN:
                new_board[x,y]=1
            elif board[x,y] ==1 and neighbors in SURVIVE:
                new_board[x,y] =1

    return new_board