from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
import time


def convert():
    fn = file_name.get()
    speech = gTTS(text=text.get(1.0, "end-1c"))
    speech.save(f"{fn}.mp3")
    play.config(state='normal', bg='#f82121')


def play_sound():
    fn = file_name.get()
    playsound(f"{fn}.mp3")


def clear_txt():
    text.delete(1.0, END)
    play.config(state='disabled', bg='#ff7777')


user = os.getlogin()
default_path = f"C:\\users\\{user}\\Music\\t2s"
root = Tk()
root.geometry('400x400')
root.minsize(600, 400)
root.maxsize(600, 400)
root.title("TEXT2SPEECH CONVERTER")
root.iconbitmap("logo.ico")

scrool = Scrollbar(root)
scrool.pack(side='right', fill='y')

# Heading

Label(root, text='TEXT2SPEECH CONVERTER', bg='#dfdcdc', font=(' ', 20, 'bold')).pack(side='top', anchor='n')

# Text Input Box
Label(root, text='Place your text here', bg='#dfdcdc', font=(' ', 11, 'bold'), pady=10).pack(side='top', anchor='nw',padx=10)
text = Text(root, height=10, width=65, yscrollcommand=scrool.set)
text.pack(anchor='n', padx=10, pady=5)
scrool.config(command=text.yview)

# File name
Label(root, text='File Name', bg='#dfdcdc', font=(' ', 11, 'bold'), pady=5).pack(side='top', anchor='nw',padx=10)
file_name = StringVar()
fn_entry=Entry(root, textvariable=file_name, width=96)
fn_entry.pack(anchor='nw', padx=25, pady=2)
fn_entry.insert(END, default_path)

# Convert Button
convert_btn = Button(root, text='Convert', padx=4, pady=2, bg='#85b90e', command=convert)
convert_btn.place(x=150, y=350)

# Clear Button
clear = Button(root, text='Clear', padx=10, pady=2, command=clear_txt)
clear.place(x=250, y=350)

# Play Button
play = Button(root, text='Play', padx=12, pady=2, bg='#ff7777', command=play_sound)
play.place(x=350, y=350)
play.config(state='disabled')

root.config(bg='#dfdcdc')
root.mainloop()
