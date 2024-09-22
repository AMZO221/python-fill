from tkinter import*
from random import randint , choice
import string
fen = Tk()
fen['bg'] ="aqua"

la = Label(fen,text ="Générateur de mot de passe",bg = "aqua",fg = "red", font= ("verdana",12,"bold"))
la.pack()

label = Label(fen,text = "Bienvenue",bg = "aqua",fg = "red",font = ("verdana",15,"italic bold"))
label.pack()

#photo = PhotoImage(file = "Pictures/Screenshot/Screenshot_20230731-145837.png")
#label = Label(fen, image = photo)
#label.pack()
#canvas = Canvas(fen,width = 400,height= 450,bg = "red")
#canvas.create_image(200,220,image = photo)
#canvas.pack()

def generate_pw():
    password_min = 4
    password_max = 12
    all_chars = string.ascii_letters + string.digits
    password = "".join(choice(all_chars)for x in range(randint(password_min , password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

frame = Frame(fen,bg ="aqua")

label = Label(frame,text = "Mot de passe",bg = "aqua",fg = "black",font = ("verdana",10,"italic"))
label.pack()

password_entry = Entry(frame)
password_entry.pack()

bout = Button(frame,text = "Générer",bg = "dark orange",command = generate_pw)
bout.pack()

frame.pack()

fen.mainloop()