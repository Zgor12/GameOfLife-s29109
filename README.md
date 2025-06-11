# GameOfLife-s29109


Projekt implementuje klasyczną grę w życie Conwaya - dwuwymiarowy automat komórkowy, w którym komórki żyją,umierają lub odradzają się na podstawie liczby sąsiadów.
Aplikacja posiada interfejs graficzny użytkownika oraz ekran startowy z ustawieniami gry.


Wymagania:
    1. Zainstalowane biblioteki:
        - numpy
        - pygame


Instalacja:
    - pip install numpy pygame


Uruchomienie:

    1. Uruchom ekran startowy (z ustawieniami planszy):
        - przejdź do folderu, w którym znajduje się launcher.py
	-uruchom program: python launcher.py
    2. Wprowadź parametry (liczba kolumn,wierszy,FPS)
    3. Kliknij na przycisk 'Start gry', a uruchomi się plansza w pygame



Sterowanie:

    - [Spacja] - start/pauza symulacji
    - [C] - czyść planszę
    - [ESC] - zakończ grę
    - [Lewy Przycisk Myszy] - dodaj komórkę
    - [Prawy Przycisk Myszy] - usuń komórkę

Reguły gry Conwaya (23/3):
    - Żywa komórka przeżywa, jeśli ma 2 lub 3 sąsiadów,
    - Martwa komórka odradza się, jeśli ma dokładnie 3 sąsiadów,
    - W innych przypadkach komórka umiera lub pozostaje martwa

