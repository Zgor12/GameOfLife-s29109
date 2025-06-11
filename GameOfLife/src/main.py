"""
main.py - uruchamia GUI gry
"""

from gui import GameGUI


def main():
    """
    Inicjalizuje i uruchamia główną pętle gry.
    """
    game=GameGUI()
    game.run()


if __name__ == "__main__":
    main()