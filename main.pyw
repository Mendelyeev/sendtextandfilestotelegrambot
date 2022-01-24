from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import time
import sys
from turtle import width
import requests  # nesse caso para a função enviar2 https://www.geeksforgeeks.org/get-post-requests-using-python/
import webbrowser


TOKEN = ""
URL3 = "/sendDocument?chat_id=&files="
USERNAME_BOT = ""


def enviararquivo():
    filetypes = (
    ('All files', '*.*'),
    ('text files', '*.txt'))

    filename = fd.askopenfilename(
        title='Escolha o Arquivo...',
        filetypes=filetypes)

    files = {'document': open(filename, 'rb')}
    requests.post(URL3, files=files)
    entry_1.delete(0, END)
    entry_1.insert(END, "Arquivo enviado !")
    messagebox.showinfo(title="Sucesso", message="O Arquivo [" + filename + "] foi enviado ao Bot do Telegram com Sucesso !")


def enviar2(event):
    URL = "&text=" + Textoaenviar.get()
    r = requests.get(url=URL)
    entry_1.delete(0, END)
    entry_1.insert(END, "Texto enviado !")
    # time.sleep(1)
    # root.destroy()
    

def enviar3(): #esse é com o botao sem o 'event'
    URL = "&text=" + Textoaenviar.get()
    r = requests.get(url=URL)
    entry_1.delete(0, END)
    entry_1.insert(END, "Texto enviado !")
    # time.sleep(1)
    # root.destroy()

def abrirchat():
    webbrowser.open('https://web.telegram.org/z/#5015257201')

# def enviar():
#     webbrowser.open(
#         '&text=' + Textoaenviar.get())
#     time.sleep(1)
#     pyautogui.hotkey('ctrl', 'w')
#     entry_1.delete(0, END)
#     entry_1.insert(END, "Texto enviado !")
#     time.sleep(1)
#     root.destroy()


def click(event):
    entry_1.configure(state=NORMAL)
    entry_1.delete(0, END)
    entry_1.unbind('<Button-1>', clicked)


def close(event):
    sys.exit()  # if you want to exit the entire thing


root = Tk()
root.geometry('350x190')
root.title("Telegram Pusher by Mendel")


Textoaenviar = StringVar()
arquivoaenviar = StringVar()

label_0 = Label(root, text="Telegram Pusher", width=20, font=("bold", 20))
label_0.place(relx=0.5, rely=0.1, anchor=CENTER)

label_1 = Label(root, text="Texto a ser enviado", width=20, font=("bold", 10))
label_1.place(x=00, y=80)

entry_1 = Entry(root, textvar=Textoaenviar)
entry_1.place(x=150, y=70, width=180, height=50)
entry_1.insert(0, 'Digite o texto aqui...')

label_2 = Label(root, text="Enviar Arquivo:", width=20, font=("bold", 10))
label_2.place(x=00, y=150)

Button(root, text='Enviar', width=20, bg='brown',
       fg='white', command=enviar3).place(x=150, y=120, height=20, width=180)

Button(root, text='Procurar...', width=20, bg='blue',
       fg='white', command=enviararquivo).place(x=150, y=150, height=20, width=180)

Button(root, text='Abrir Chat Bot no Telegram', width=20, bg='red',
       fg='white', command=abrirchat).place(relx=0.5, rely=0.23, anchor=CENTER, height=20, width=180)

clicked = root.bind('<Button-1>', click)

root.bind('<Escape>', close)
root.bind('<Return>', enviar2)

root.mainloop()
