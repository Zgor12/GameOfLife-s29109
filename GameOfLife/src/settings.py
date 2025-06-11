"""
settings.py - konfiguracja gry w życie Conwaya

Zawiera stałe decydujące parametry okna i planszy gry.
"""


DEFAULT_ROWS=40
"""Liczba wierszy na planszy"""

DEFAULT_COL=60
"""Liczba kolumn na planszy"""


CELL_SIZE=15
"""Rozmiar jednej komórki w pikselach"""


WINDOW_WIDTH=DEFAULT_COL * CELL_SIZE
""" Szerokość okna gry w pikselach"""



WINDOW_HEIGHT = DEFAULT_ROWS*CELL_SIZE
"""Wysokość okna gry w pikselach"""


FPS=10
""" Liczba klatek na sekundę (tempo symulacji)"""