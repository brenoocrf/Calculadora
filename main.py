from tkinter import *

root = Tk()
root.title('Calculadora básica') 
root.geometry('408x355') 
root.minsize(408, 355) 
root.maxsize(408, 355)

num1 = ''
divide = False
multiplica = False
adicao = False
subtracao = False

root.configure(background='#282828') #Plano de fundo

#Entrada de dados
entrada = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)

#funções
def botao_click(num):
    entrada.insert(END, num) #Inserir no final, o número

def botao_divide():
    global num1
    global divide
    divide = True
    num1 = entrada.get()
    entrada.delete(0, END)

def botao_adicao():
    global num1
    global adicao
    adicao = True
    num1 = entrada.get()
    entrada.delete(0, END)

def botao_subtracao():
    global num1
    global subtracao
    subtracao = True
    num1 = entrada.get()
    entrada.delete(0, END)

def botao_multiplica():
    global num1
    global multiplica
    multiplica= True
    num1 = entrada.get()
    entrada.delete(0, END)

def botao_limpa():
    entrada.delete(0, END)

def botao_igual():
    global subtracao
    global multiplica
    global adicao
    global divide
    num2 = entrada.get()
    entrada.delete(0, END)
    if adicao == True:
        entrada.insert(0, int(num1) + int(num2))
        adicao = False

    if subtracao == True:
        entrada.insert(0, int(num1) - int(num2))
        subtracao = False

    if multiplica == True:
        entrada.insert(0, int(num1) * int(num2))
        multiplica = False

    if divide == True:
        entrada.insert(0, int(num1) / int(num2))
        divide = False

#grid() adiciona o objeto criado no root
entrada.grid(
    row=0, #linha zero
    column=0, #coluna zero
    columnspan=4,  #ocupar 4 colunas
    pady= 2 #distância entre o botão e o númer3
)

divide = Button(root,
                text= '÷',
                padx=42, 
                pady=20, 
                command=botao_divide, 
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
divide.grid(row=0, column=4)
multiplica = Button(root,
                text= 'x',
                padx=42, 
                pady=20, 
                command= botao_multiplica, 
                fg='#FFFFFF',
                activeforeground='#FFFFFF', 
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
multiplica.grid(row=1, column=4)
adicao = Button(root,
                text= '+',
                padx=42, 
                pady=20, 
                command=botao_adicao, 
                fg='#FFFFFF',
                activeforeground='#FFFFFF', 
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
adicao.grid(row=2, column=4)
subtracao= Button(root,
                text= '-', 
                padx=44, 
                pady=20, 
                command=botao_subtracao, 
                fg='#FFFFFF',
                activeforeground='#FFFFFF', 
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
subtracao.grid(row=3, column=4)
limpar = Button(root,
                text='C', 
                padx=38,
                pady=20, 
                command=botao_limpa, 
                fg='#FFFFFF',
                activeforeground='#FFFFFF', 
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
limpar.grid(row=4, column=3)
igual = Button(root,
                text='=', 
                padx=43, 
                pady=20, 
                command=botao_igual,
                fg='#FFFFFF',
                activeforeground='#FFFFFF', 
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
igual.grid(row=4, column=4)
#Primeira fileira
um = Button(root,
                text= '1', #texto do botão
                padx=40, #largura
                pady=20, #altura
                command=lambda: botao_click(1), #funcao do botão
                fg='#FFFFFF',
                activeforeground='#FFFFFF', 
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
um.grid(row=1, column=1)
dois = Button(root,
                text= '2', 
                padx=40, 
                pady=20, 
                command=lambda: botao_click(2), 
                fg='#FFFFFF',
                activeforeground='#FFFFFF', 
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
dois.grid(row=1, column=2)
tres = Button(root,
                text= '3', 
                padx=40, 
                pady=20, 
                command=lambda: botao_click(3), 
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
tres.grid(row=1, column=3)
#Segunda Fileira
quatro = Button(root,
                text= '4', 
                padx=40, 
                pady=20, 
                command=lambda: botao_click(4), 
                fg='#FFFFFF',
                activeforeground='#FFFFFF', 
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
quatro.grid(row=2, column=1)
cinco = Button(root,
                text= '5', 
                padx=40, 
                pady=20, 
                command=lambda: botao_click(5), 
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
cinco.grid(row=2, column=2)
seis = Button(root,
                text= '6',
                padx=40, 
                pady=20, 
                command=lambda: botao_click(6), 
                fg='#FFFFFF',
                activeforeground='#FFFFFF', 
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
seis.grid(row=2, column=3)
#Terceira Fileira
sete = Button(root,
                text= '7', 
                padx=40, 
                pady=20, 
                command=lambda: botao_click(7), 
                fg='#FFFFFF',
                activeforeground='#FFFFFF', 
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))

sete.grid(row=3, column=1)
oito = Button(root,
                text= '8', 
                padx=40, 
                pady=20,
                command=lambda: botao_click(8), 
                fg='#FFFFFF',
                activeforeground='#FFFFFF', 
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
oito.grid(row=3, column=2)
nove = Button(root,
                text= '9', 
                padx=40,
                pady=20, 
                command=lambda: botao_click(9), 
                fg='#FFFFFF',
                activeforeground='#FFFFFF', 
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
nove.grid(row=3, column=3)
zero = Button(root,
                text= '0', 
                padx=91, 
                pady=20, 
                command=lambda: botao_click(0),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'))
zero.grid(row=4, column=1, columnspan=2)

#Para a janela pernamecer aberta aguardando ação
root.mainloop()