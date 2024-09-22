from tkinter import*
fenetre = Tk()

def function():
    if mot_de_passe.get() =="amzondiaye":
        an = Label(fenetre, text = "bienvenue amzo", font = ("verdana",10,"italic bold") , bg = "green")
        an.pack()
    else:
        an1 = Label(fenetre, text = "Erreur mot de passe Incorrect", bg = "red", font = ("verdana",11,"italic bold"))
        an1.pack()
        
mot_de_passe = StringVar()
label = Label(fenetre, text = "entrez votre mot de passe")
label.pack()
entree = Entry(fenetre, text = mot_de_passe)
entree.pack()
boutton = Button(fenetre, text = "valider", command = function)
boutton.pack()

fenetre.mainloop()