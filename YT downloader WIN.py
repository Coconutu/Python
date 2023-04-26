
from tkinter import *
from tkinter import Tk
from pytube import YouTube
import pyperclip
import os

def Lipeste_si_descarca():
    try:
        linkul=pyperclip.paste()
        labelID.config(text=linkul)
        url = YouTube(str(linkul))
        audio_stream = url.streams.filter(abr='128kbps',only_audio=True).first()
        destination = '.'
        out_file = audio_stream.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        labelStatus.config(text= f'{new_file} a fost descărcat cu succes.')

    except Exception as eroare:
        labelStatus.config(text = eroare)



window=Tk()
window.title('YouTube -> *.mp3')
window.config(bg='Blue')
width=900
height=280
window.geometry(f'{width}x{height}')

labelID=Label(window,bg='Yellow',text='Link...',font=('Serif',12),wraplength=850, justify="left")
labelID.place(x=10,y=5)
Buton_Download=Button(window,text='Lipește și descarcă *.mp3!',fg='blue',font=('Sans',16),bg='white',command=Lipeste_si_descarca)
Buton_Download.place(x=250,y=60,width=400, height=120)
labelStatus=Label(window,bg='Yellow',text='Status:',font=('Serif',13),wraplength=850, justify="left")
labelStatus.place(x=10,y=200)

window.mainloop()