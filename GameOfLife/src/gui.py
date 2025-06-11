"""
gui.py - interfejs graficzny gry

Zawiera klasę GameGUI odpowiedzialną za obsługę okna gry, planszy i interakcji
z użytkownikiem za pomocą Pygame.

"""


import numpy as np
import pygame
import settings
from game import next_generation
from settings import *


class GameGUI:
    """
    Klasa odpowiedzialna za graficzną obsługę gry przy pomocy pygame.

    Obejmuje:
     - tworzenie planszy
     - obsługę zdarzeń użytkownika
     - rysowanie planszy
     - uruchmienie pętli głównej
    """


    def __init__(self):
        """
        Inicjalizuje ustawienia okna gry, planszy oraz zmiennych sterujących.
        """

        pygame.init()
        self.rows= settings.DEFAULT_ROWS
        self.cols= settings.DEFAULT_COL
        self.fps= settings.FPS
        self.cell_size = settings.CELL_SIZE
        self.width=self.cols *self.cell_size
        self.height=self.rows *self.cell_size

        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Gra w życie Conwaya")
        self.clock = pygame.time.Clock()
        self.font=pygame.font.SysFont("Arial",20)
        self.running=False
        self.board = np.zeros((self.rows,self.cols), dtype=int)





    def board_draw(self):
        """
        Rysuje planszę gry oraz instrukcje sterowania w dolnej części okna.
        """

        self.screen.fill((0,0,0))

        for x in range(self.rows):
            for y in range(self.cols):

                rect = pygame.Rect(y*self.cell_size, x*self.cell_size, self.cell_size-1,self.cell_size-1)
                color = (0,255,0) if self.board[x,y] else (30,30,30)
                pygame.draw.rect(self.screen,color, rect)

        info = "[Spacja] Start/Pauza     [LPM] Dodaj Komórkę     [PPM] Usuń komórkę     [C] Czyść     [ESC] Wyjście"
        self.screen.blit(self.font.render(info,True, (255,255,255)), (10, WINDOW_HEIGHT-30))
        pygame.display.flip()



    def handle_events(self):
        """
        Obsługuje zdarzenia użytkownika: klawiatura i myszka:

         - [Spacja]:  start/pauza gry
         - [C]:  czyści planszę
         - [ESC]:  kończy grę
         - Lewy przycis myszy:  dodaj komórkę
         - Prawy przyscisk myszy:  usuwa komórkę


        :return: False jeśli użytkownik zakończył działanie, True w przeciwnym przypadku
        :rtype: bool
        """

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.running= not self.running

                elif event.key == pygame.K_ESCAPE:
                    return False

                elif event.key == pygame.K_c:
                    self.board = np.zeros_like(self.board)

            elif pygame.mouse.get_pressed()[0]:
                x,y = pygame.mouse.get_pos()
                row,col = y //CELL_SIZE, x //CELL_SIZE
                if 0 <= row <DEFAULT_ROWS and 0<=col<DEFAULT_COL:
                    self.board[row,col] = 1

            elif pygame.mouse.get_pressed()[2]:
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE
                if 0 <= row < DEFAULT_ROWS and 0 <= col < DEFAULT_COL:
                    self.board[row, col] = 0

        return  True



    def update(self):
        """
        Aktualizuje planszę gry do kolejnej generacji, jeśli gra jest uruchomiona.
        :return:
        """
        if self.running:
            self.board = next_generation(self.board)



    def run(self):
        """
        Uruchamia główną pętle gry:
         - reaguje na zdarzenia,
         - aktualizuje i rysuje planszę,
         - utrzymuje płynność (FPS).
        """
        while True:
            if not self.handle_events():
                break

            self.update()
            self.board_draw()
            self.clock.tick(FPS)
