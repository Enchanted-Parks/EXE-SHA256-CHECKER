from customtkinter import *
from tkinter import *
from tkinter import filedialog
from digest import checkdigest
from tkinter import messagebox

# nouvelle fenêtre

root = CTk()
root.title("Enpa Checksum")
root.geometry("800x600")
root.iconbitmap("logoenpa.ico")
root.resizable(False, False)
calculable = False
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
    #on affiche le boutton pour calculer le hash
    hashbutton.grid(row=3, column=0, columnspan=2)

    #on affiche le chemin du fichier
    path.configure(text=file)



#Le titre
title = CTkLabel(root, text="Enpa Checksum", font=("Arial", 20))
#on utilise le grid (un truc bien sympa qui est un tableau en gros)
title.grid(row=0, column=0, columnspan=2)


# Juste du text
choosefileL = CTkLabel(root, text="Choisissez un fichier: ", font=("Arial", 15))
choosefileL.grid(row=1, column=0, columnspan=1)

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
    try:
        #on récupère le chemin du fichier
        if path.cget("text") == "":
            raise FileNotFoundError
        file = path.cget("text")
        #on calcul le hash du fichier
        digest = checkdigest(file)
        #on affiche le hash du fichier
        hashlabel.configure(text=digest)
        #on affiche le boutton pour copier le hash
        copybutton.grid(row=5, column=0, columnspan=2)
        hashentrylabel.grid(row=6, column=0, columnspan=1)
        hashentry.grid(row=6, column=0, columnspan=2)
        comparehashbutton.grid(row=7, column=0, columnspan=2)
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Veuillez choisir un fichier avant de calculer le hash")


hashbutton = CTkButton(root, text="Calculer le hash", command=calculhash)


#Le label pour afficher le hash
hashlabel = CTkLabel(root, text="", font=("Arial", 10))
hashlabel.grid(row=4, column=0, columnspan=2)


#un boutton pour copier le hash
def copyhash():
    """
    Fonction qui permet de copier le hash
    :return: None
    """
    #on copie le hash
    root.clipboard_clear()
    #root = fenêtre clipboard_append = ajouter au (copier coller enfin la mémoire en gros) hashlabel.cget("text") = on récupère le texte du label

    root.clipboard_append(hashlabel.cget("text"))
    root.update()


copybutton = CTkButton(root, text="Copier le hash", command=copyhash)
#on fait exprès de ne pas l'afficher tout de suite

#le texte pour dire quoi mettre
hashentrylabel = CTkLabel(root, text="Entrez un hash pour comparer: ", font=("Arial", 15))


#on ajoute une entré pour pouvoir coller un hash et le comparer
hashentry = CTkEntry(root)


def comphash():
    """
    Fonction qui permet de comparer les hash
    :return: None
    """
    #on récupère le hash du fichier
    if hashlabel.cget("text") == "":
        #en théorie impossible mais on ne sait jamais
        messagebox.showerror("Erreur", "Veuillez calculer le hash d'un fichier avant de comparer les hash")
        return
    hash = hashlabel.cget("text")
    #on récupère le hash entré par l'utilisateur
    hash2 = hashentry.get()
    #on compare les hash
    if hash == hash2:
        hashcompres.configure(text="Les hash sont identiques", fg_color="green")
        messagebox.showinfo("No problemo", "Les hash sont identiques")

    else:
        hashcompres.configure(text="Les hash ne sont pas identiques", fg_color="red")
        messagebox.showerror("Attention !!!", "Les hash ne sont pas identiques ⚠️")


#le boutton pour comparer les hash
comparehashbutton = CTkButton(root, text="Comparer les hash",command=comphash)


#ici pour le label
hashcompres = CTkLabel(root, text="", font=("Arial", 10))
hashcompres.grid(row=8, column=0, columnspan=2)


#credit
credit = CTkLabel(root, text="Fait par Snipeur060 pour ENCHANTED PARKS", font=("Arial", 10))
credit.grid(row=9, column=0, columnspan=2)


#un event
def paste(e):
    """
    Fonction qui permet de coller le hash dans l'entrée
    :param e: l'événement
    :return: None
    """
    #on colle le texte
    hashentry.insert(0, root.clipboard_get())
    #on empêche de continuer l'événement
    return "break"


def coll():
    hashentry.event_generate("<Control-v>")

#on ajoute le menu
menu = Menu(root, tearoff=0)

menu.add_command(label="Coller",background="#141414",foreground="white" ,command=coll)
#on ajoute le menu à l'entrée
#https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
#https://stackoverflow.com/questions/75259242/tkinter-processing-button-clicks-using-lambda-eval
hashentry.bind("<Button-3>", lambda e: menu.post(e.x_root, e.y_root))
hashentry.bind("<Control-v>", paste)




root.mainloop()
