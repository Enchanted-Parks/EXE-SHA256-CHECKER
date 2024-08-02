from customtkinter import *
from tkinter import *
from tkinter import filedialog
from digest import checkdigest

# nouvelle fenêtre

root = CTk()
root.title("Enpa Digest")
root.geometry("800x600")
root.resizable(False, False)

n_rows = 10
n_columns = 2
for i in range(n_rows):
    root.grid_rowconfigure(i, weight=1)
for i in range(n_columns):
    root.grid_columnconfigure(i, weight=1)

def fichier_dialogue():
    """
    Fonction qui permet de choisir un fichier
    :return: le chemin du fichier
    """
    return filedialog.askopenfilename()

#Le titre
title = CTkLabel(root, text="Enpa Digest", font=("Arial", 20))
#on utilise le grid (un truc bien sympa qui est un tableau en gros)
title.grid(row=0, column=0, columnspan=2)


# Juste du text
choosefileL = CTkLabel(root, text="Choisissez un fichier: ", font=("Arial", 15))
choosefileL.grid(row=1, column=0, columnspan=2)

#Le boutton pout les dialogues
fdialog = CTkButton(root, text="Choisir un fichier", command=fichier_dialogue)
fdialog.grid(row=1, column=1, columnspan=1)





root.mainloop()
