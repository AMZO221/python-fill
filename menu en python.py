from tkinter import*
fenetre = Tk()
fenetre['bg'] = "white"

def function():
    if mot_de_passe.get() =="amzondiaye":
        an = Label(fenetre, text = "bienvenue amzo", font = ("verdana",11,"italic bold") , bg = "white")
        an.pack()
    else:
        an1 = Label(fenetre, text = "Erreur mot de passe Incorrect", bg = "white", font = ("verdana",11,"italic bold"), fg = "red")
        an1.pack()
        
mot_de_passe = StringVar()
label = Label(fenetre, text = "entrez votre mot de passe",bg = "white",font = ("verdana",15,"italic bold"))
label.pack()

boite = Frame(fenetre, bg = "white")
entree = Entry(boite, text = mot_de_passe)
entree.pack()
boutton = Button(boite, text = "valider", bg ="green" , fg ="white" , command = function)
boutton.pack()
boite.pack()
#boite.place(x = 200, y = 100, width = 350)


mon_menu = Menu(fenetre)
#sous onglet fichier
fichier = Menu(mon_menu, tearoff = 0)
fichier.add_command(label = "enregistre sous...",command = fichier)

#sous onglet options
options = Menu(mon_menu, tearoff = 0)
options.add_command(label = "Modifier la taille",command = options)

#les 2 principaux onglets
#onglet Fichier
mon_menu.add_cascade(label = "Fichier",menu = fichier)
#onglet Options
mon_menu.add_cascade(label = "Options", menu = options)

fenetre.config(menu = mon_menu)

fenetre.mainloop()