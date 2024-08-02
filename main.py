from customtkinter import *
from tkinter import *
from tkinter import filedialog
from digest import checkdigest

# nouvelle fenêtre

root = CTk()
root.title("Enpa Digest")
root.geometry("800x600")
root.resizable(False, False)

#on force un peut pour que le texte soit bien collé
n_rows = 10
n_columns = 2
#permet de configurer plus facilement la grid (le but avoir une ui plutôt jolie)
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

def manipfile():
    """
    Fonction qui permet de manipuler un fichier
    :return: None
    """
    #on récupère le chemin du fichier
    file = fichier_dialogue()
    #on affiche le chemin du fichier
    path.configure(text=file)


#Le titre
title = CTkLabel(root, text="Enpa Digest", font=("Arial", 20))
#on utilise le grid (un truc bien sympa qui est un tableau en gros)
title.grid(row=0, column=0, columnspan=2)


# Juste du text
choosefileL = CTkLabel(root, text="Choisissez un fichier: ", font=("Arial", 15))
choosefileL.grid(row=1, column=0, columnspan=2)

#Le boutton pout les dialogues
fdialog = CTkButton(root, text="Choisir un fichier", command=manipfile)
fdialog.grid(row=1, column=1, columnspan=1)


#Le label pour afficher le chemin du fichier
path = CTkLabel(root, text="", font=("Arial", 10))
path.grid(row=2, column=0, columnspan=2)

#on met ici le boutton pour confirmer le calcul du hash

def calculhash():
    """
    Fonction qui permet de calculer le hash d'un fichier
    :return: None
    """
    #on récupère le chemin du fichier
    file = path.cget("text")
    #on calcul le hash du fichier
    digest = checkdigest(file)
    #on affiche le hash du fichier
    hashlabel.configure(text=digest)


hashbutton = CTkButton(root, text="Calculer le hash", command=calculhash)
hashbutton.grid(row=3, column=0, columnspan=2)

#Le label pour afficher le hash
hashlabel = CTkLabel(root, text="", font=("Arial", 10))
hashlabel.grid(row=4, column=0, columnspan=2)





root.mainloop()
