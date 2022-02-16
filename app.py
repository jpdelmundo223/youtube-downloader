from calendar import LocaleHTMLCalendar
import re
from pytube import YouTube
from tkinter import *
from tkinter import messagebox

def downloader(link, directory, filename):
    link_str = link.get()
    directory_str = link.get()
    filename_str = link.get()

    try:
        yt = YouTube(link_str)
        video = yt.streams.first()
        video.download(directory_str, filename_str)
    except:
        messagebox.showerror('Error', 'Connection Error! You are offline!')

def reset(l_strvar, d_strvar, fn_strvar):
    l_strvar.set('')
    d_strvar.set('')
    fn_strvar.set('')

root = Tk()
root.title('Youtube Downloader')
root.geometry('700x200')
root.resizable(0, 0)
root.config(bg='Coral')

Label(root, text='Youtube Downloader').place(relx=0.25, rely=0.0)

Label(root, text='Enter the Youtube link:').place(relx=0.05, rely=0.2)

link_strvar = StringVar(root)
link_entry = Entry(root, width=50, textvariable=link_strvar)
link_entry.place(relx=0.5, rely=0.2)

Label(root, text='Enter the save location:').place(relx=0.05, rely=0.4)

dir_strvar = StringVar(root)
dir_entry = Entry(root, width=50, textvariable=dir_strvar)
dir_entry.place(relx=0.5, rely=0.4)

Label(root, text='Enter the filename:').place(relx=0.05, rely=0.6)

fileneme_strvar = StringVar(root)
filename_entry = Entry(root, width=50, textvariable=fileneme_strvar)
filename_entry.place(relx=0.5, rely=0.6)

download_btn = Button(root, text='Download', command=lambda:downloader(link_entry, dir_entry, filename_entry)).place(relx=0.5, rely=0.75)

root.update()
root.mainloop()