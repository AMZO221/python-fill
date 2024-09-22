from tkinter import*
fen = Tk()
fen['bg'] = "aqua"
#le titre comme bienvenue
titre = Label(fen, text = "BIENVENUE",bg = "aqua",fg = "dark blue" ,font = ("verdana",30,"italic"))
titre.pack()

#ajouter une image
#photo = PhotoImage(file = "Pictures/Screenshot/Screenshot_20230728-161311.png")
#l = Label(fen, image = photo).pack()

# le mot de passe
label = Label(fen, text = "entrez votre mot de passe",font = ("verdana",9,"italic bold"),bg = "aqua")
label.pack()
mdp = StringVar()
entree = Entry(fen,text = mdp).pack()

# l'addresse email
labe = Label(fen, text = "entrez votre addresse email",bg = "aqua",font = ("verdana",9,"italic bold"))
labe.pack()
email = StringVar()
entrer = Entry(fen,text = email).pack()

#creer un fonction avec des conditions
def show():
    if mdp.get() =="amzondiaye" and email.get() == "amzo10@":
        lab = Label(fen, text = "salut ndiaw ndiaye",font = ("verdana",11,"italic bold"), bg ="aqua" ,fg = "blue")
        lab.pack()
    elif mdp.get() == "" or email.get() == "":
        lab1 = Label(fen,text = "svp veillez entrez un texte", bg ="aqua" , fg = "black" ,font = ("verdana",9,"italic"))
        lab1.pack()
    else:
        lab2 = Label(fen,text = "acces refusee mot de passe ou email incorrect",font = ("verdana",8,"italic bold"), bg ="aqua" ,fg = "red")
        lab2.pack()
        
#creer un boutton
bout = Button(fen, text = "connexion", command = show, bg = "green")
bout.pack()

fen.mainloop()