"""
launcher.py - Ekran startowy gry

Tworzy graficzne okno startowe za pomocą tkintera, w którym użytkownik może:
 - ustawić rozmiar planszy (kolumny,wiersze)
 - ustawić tempo symulacji (fps)
 - przeczytać instrukcje sterowania i reguły Conwaya
 - uruchomić grę klikając w przycisk 'Start gry'
"""
import os.path
import tkinter as tk
import subprocess
import settings
import sys


def start_game():
    """
    Pobiera dane z pól tekstowych i ustawia parametry gry (rozmiar planszy, tempo symulacji).
    Następnie zamyka okno tkintera i uruchamia 'main.py' w tym interpreterze Pythona.


    :raises ValueError: Jeśli użytkownik wpisze niepoprawne wartości (mają być same liczby)
    """
    try:
        settings.DEFAULT_ROWS = int(rows_entry.get())
        settings.DEFAULT_COL = int(cols_entry.get())
        settings.FPS= int(fps_entry.get())
    except ValueError:
        error_label.config(text= "Wprowadź poprawne liczby!")
        return

    root.destroy()
    main_path = os.path.join(os.path.dirname(__file__),"main.py")
    subprocess.run([sys.executable,main_path])




root = tk.Tk()
root.title("Gra w życie Conwaya")
root.geometry("500x500+350+100")


tk.Label(root,text="Ustawienia gry:",font=("Arial",14,"bold")).pack(pady=10)

frame =tk.Frame(root)
frame.pack()

tk.Label(frame,text="Wiersze (np.40)").pack()
rows_entry=tk.Entry(frame)
rows_entry.insert(0, str(settings.DEFAULT_ROWS))
rows_entry.pack()

tk.Label(frame,text="Kolumny (np.40)").pack()
cols_entry=tk.Entry(frame)
cols_entry.insert(0, str(settings.DEFAULT_COL))
cols_entry.pack()

tk.Label(frame,text="FPS - tempo symulacji (np.20)").pack()
fps_entry = tk.Entry(frame)
fps_entry.insert(0, str(settings.FPS))
fps_entry.pack()


info_label = tk.Label(root,text="Sterowanie:",font=("Arial",12,"bold"))
info_label.pack(pady=5)

lines = [
            "[LPM] – Dodaj komórki",
            "[PPM] – Usuń komórki",
            "[Spacja] – Start/Pauza",
            "[C] – Czyść planszę",
            "[Esc] – Wyjście w trakcie gry"
]

for line in lines:
    tk.Label(root,text=line).pack()



tk.Label(root,text="Gramy według reguły Conway'a 23/3",font=("Arial",11,"bold")).pack(pady=5)
rules = [
            "Komórka przeżyje, jeśli ma 2 lub 3 sąsiadów,",
            "Martwa komórka odrodzi się, jeśli ma dokłądnie 3 sąsiadów,",
            "W innych przypadkach komórka umiera / pozostaje martwa."
]

for rule in rules:
    tk.Label(root,text=rule).pack()

error_label = tk.Label(root,text="",fg="red")
error_label.pack()

start_button = tk.Button(root,text="Start Gry", command=start_game, bg="lightgreen")
start_button.pack(pady=20)


root.mainloop()