from tkinter import*
fenetre = Tk()
fenetre.geometry("680x1000")
fenetre.title("amzo")
fenetre['bg'] = "orange"
label = Label(fenetre, text = "bonjour tout le monde", font =("verdana", 15, "italic bold"), bg = "orange")
label.pack()
sous_label = Label(fenetre, text = "je suis amzo ndiaye", font =("verdana", 15, "italic bold"), bg = "orange")
sous_label.pack()

photo = PhotoImage(file = "Pictures/Screenshot/Screenshot_20230718-102020.png",)
label = Label(fenetre, image = photo)
label.pack()

fenetre.mainloop()