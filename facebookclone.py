from tkinter import*
import webbrowser
fen = Tk()
fen['bg'] = "white"
fen.geometry("450x600")
#le titre comme facebook
titre = Label(fen, text = "Facebook",bg = "white",fg = "grey",font=("verdana",9,"bold"))
titre.place(x = 200 ,y = 30)

#creer une ligne
ligne = Entry(fen,text = "",bg = "dark grey")
ligne.place(x = 10,y =90 ,width = 400,height = 2 )

# la parametre ou
ligne1 = Entry(fen,text = "",bg = "dark grey")
ligne1.place(x = 14,y =450 ,width = 150,height = 2 )

ou = Label(fen,text = "ou",bg = "white",fg = "black",font = ("verdana",10))
ou.place(x = 194, y = 430)

ligne2 = Entry(fen,text = "",bg = "dark grey")
ligne2.place(x = 250,y =450 ,width = 158,height = 2 )

#les derniers phrases
#francais
fr = Label(fen,text = "Français (France)",bg = "white",fg = "black",font = ("verdana",9))
fr.place(x= 14, y = 460)
#anglais
ang = Button(fen,text = "English (US)",bg = "white",fg = "#4065A4",font = ("verdana",9),bd = 0, highlightthickness = 0,command = "")
ang.place(x= 14, y = 485)
#autres langues
al = Button(fen,text = "Autres langues...",bg = "white",fg = "#4065A4",font = ("verdana",9),bd = 0, highlightthickness = 0,command="")
al.place(x= 14, y = 510)

#ajouter une image
#photo = PhotoImage(file = "Pictures/Screenshot/Screenshot_20230728-161311.png")
#l = Label(fen, image = photo).pack()

# l'addresse email
labe = Label(fen, text = "Numéro de mobile ou e-mail",bg = "white",fg = "black",font = ("verdana",9))
labe.place(x= 10, y= 125)
email = StringVar()
entrer = Entry(fen,text = email,bg = "white",bd = 1,highlightthickness = 1)
entrer.place(x = 10,y = 160,width = 400,height = 35)

# le mot de passe
label = Label(fen, text = "Mot de passe",font = ("verdana",9),bg = "white",fg = "black")
label.place(x = 10, y = 210)
mdp = StringVar()
entree = Entry(fen,text = mdp,bg = "white",bd = 1,highlightthickness = 1,show = "*")
entree.place(x = 10, y= 240,width = 400,height = 35)

#creer une fonction avec des conditions
def show():
    if mdp.get() =="amzondiaye" and email.get() == "amzo10@":
        webbrowser.open_new("https://www.facebook.com/amzo.ndiaye.33")
    elif mdp.get() == "" or email.get() == "":
        lab = Label(fen,text = "svp veillez remplir vos informations de connexion", bg ="white" , fg = "red" ,font = ("verdana",8,"italic"))
        lab.place(x=10,y = 290 ,width=350)
    else:
        lab = Label(fen,text = "acces  refusee mot de passe  ou  email incorrect",font = ("verdana",8,"italic bold"), bg ="white" ,fg = "red")
        lab.place(x = 14,y = 290)
        
#creer un boutton
bout = Button(fen, text = "Connexion", command =show , bg = "#4065A4",fg = "white",font= ("verdana",9,"bold"))
bout.place(x = 10, y = 320,width = 400,height = 50)

#ouvrir un site internet
def mdpo():
    webbrowser.open_new("https://m.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fm.facebook.com%2Flogin.php%3Fnext%3Dhttps%253A%252F%252Fm.facebook.com%252Fmotdepasseoubli%2525C3%2525A9%253Fwtsid%253Drdr_0K3TJpXpUAIsVLVRW%26refsrc%3Ddeprecated&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&wtsid=rdr_1Kik1Rh3mjbl8W9kB&_rdr")

#mot de passe oublié
mdpo = Button(fen,text = "Mot de passe oublié?",bg = "white",fg = "#4065A4",font= ("verdana",9),bd = 0,highlightthickness = 0,command= mdpo)
mdpo.place(x = 10,y = 400)

def compte():
    webbrowser.open_new("https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk")

#boutton creer un compte
boutt = Button(fen,text = "Créer un compte",bg = "green",fg = "white",font = ("verdana",9,"bold"),command = compte)
boutt.place(x = 150,y = 530,height = 50)

fen.mainloop()