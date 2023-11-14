from tkinter import *
from tkinter import ttk

cor1 = "#1e1f1e" # preta
cor2 = "#feffff" # branco
cor3 = "#38576b" # azul
cor4 = "#ECEFF1" # cinza
cor5 = "#FFAB40" # Laranja
cor6 = "#6be8c9" # Azulverde

janela = Tk()
janela.title("Ncorreiaf Calculator")
janela.geometry("235x310")
janela.config(bg=cor1)

#Criando Frames
frame_tela = Frame(janela, width=235, height=50, bg= cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#variável todos valores
todos_valores = ""
valortexto = StringVar()
#Criando função calcular
def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str(event)
    #Passando o valor para tela
    valortexto.set(todos_valores)


#Função para calcular
def calcular():
    resultado = eval(todos_valores)
    valortexto.set(resultado)





#Criando Label
app_label = Label(frame_tela, textvariable=valortexto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font= ("Ivy 18"), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


#Criando Botões
b_1 = Button(frame_corpo, text="C", width=11, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo,command=lambda: entrar_valores("%"), text="%", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, command=lambda: entrar_valores("/"), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, command=lambda: entrar_valores("7"), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=53)

b_5 = Button(frame_corpo, command=lambda: entrar_valores("8"), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=53)

b_6 = Button(frame_corpo, command=lambda: entrar_valores("9"), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=53)

b_7 = Button(frame_corpo, command=lambda: entrar_valores("*"), text="x", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=53)

b_8 = Button(frame_corpo, command=lambda: entrar_valores("4"), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=106)

b_9 = Button(frame_corpo, command=lambda: entrar_valores("5"), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=106)

b_10 = Button(frame_corpo, command=lambda: entrar_valores("6"), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=106)

b_11 = Button(frame_corpo, command=lambda: entrar_valores("-"), text="-", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=180, y=106)

b_12 = Button(frame_corpo, command=lambda: entrar_valores("1"), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=159)

b_13 = Button(frame_corpo, command=lambda: entrar_valores("2"), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=159)

b_14 = Button(frame_corpo, command=lambda: entrar_valores("3"), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=159)

b_15 = Button(frame_corpo, command=lambda: entrar_valores("+"), text="+", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=180, y=159)

b_16 = Button(frame_corpo, command=lambda: entrar_valores("0"), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=212)

b_17 = Button(frame_corpo, command=lambda: entrar_valores("."), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=212)

b_18 = Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=212)



janela.mainloop()
