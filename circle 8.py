from tkinter import*
root = Tk()
def show():
    I = Label(root,text ="i am amzo ndiaye",fg ="red",bg ="yellow")
    root.configure(bg ="green")
    I.pack()
def blue():
    I = Label(root,text ="i am a genius",fg ="red",bg ="orange")
    root.configure(bg ="blue")
    I.pack()
b = Button(root,text ="click",command = show)
b.pack()
b1 = Button(root,text ="blue",command = blue)
b1.pack()
root.mainloop()