from tkinter import*

fen = Tk()
fen.geometry("300x500")
question = StringVar()
lab1 = Label(fen,text = "POSER VOTRE QUESTION, JE SERAIS RAVIS DE VOUS REPONDRE").pack()
entre = Entry(fen,text = question , width=50).pack()

frame = Frame(fen,bg="sky blue")

#reponse = StringVar()
lab2= StringVar()
def repondre():
    
    if question.get() =="bonjour"or question.get() =="salut"or question.get() =="coucou":
        reponse = question.get()+"\n"+question.get() + " a vous aussi, en quoi puis-je vous aidez ?"
        lab2 = Label(frame,text=reponse,bg="sky blue").pack()
    elif question.get() =="qui est tu"or question.get() =="tu es qui"or question.get() =="comment tu t'appelle":
        reponse = question.get()+"\nje m'appelle AMZO AI je suis un assistant virtuelle en phase de developpement"
        lab2 = Label(frame,text=reponse,bg="sky blue").pack()
    else:
        lab2 = Label(frame,text="svp enter une question sinon verifier si votre question est valide",bg="sky blue").pack()
#def effacer():
#    lab2.delete(0,END)
frame.pack(pady=20)
boutton = Button(fen, text="valider",command=repondre).place(x=770,y=20)
#boutton = Button(fen, text="effacer",command=effacer).place(x=770,y=50)
fen.mainloop()