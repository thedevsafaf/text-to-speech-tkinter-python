## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound


################### Initialized window ####################

window = Tk()
window.geometry('600x400')
window.resizable(1, 1)
window.config(bg='#D14D72')
window.title('TTS Software - Zafe 2023')
# Set the icon
window.iconbitmap("text-to-speech.ico")


# heading
Label(window, text='Text To Speech Software', font='Tahoma 20 bold', bg='#FFABAB').pack()
Label(window, text='Developed by Safaf', font='Tahoma 10 bold', bg='#FFABAB').pack(side=BOTTOM)


# input label for entry field
Label(window, text='Enter your text here...', font='Calibri 14 bold', bg='#D14D72').place(x=20, y=70)


# text variable
Msg = StringVar()

# text style for entry
entry_font = ("Tahoma", 12, "bold")

# Entry
entry_field = Entry(window, font=entry_font, textvariable=Msg, width='55')
entry_field.place(x=20, y=100)
entry_field.config(fg="#DB005B")


###################define function##############################

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save('Audio.mp3')
    playsound('Audio.mp3')


def Exit():
    window.destroy()


def Reset():
    Msg.set("")


# Button
Button(window, text="Play", font='verdana 10 bold',
       command=Text_to_speech, bg='green', width=9, fg="white", bd=3, relief=RIDGE).place(x=20, y=140)
Button(window, text='Exit', font='verdana 10 bold',
       command=Exit, bg='red', width=9, fg="white", bd=3, relief=RIDGE).place(x=120, y=140)
Button(window, text='Reset', font='verdana 10 bold',
       command=Reset, bg='grey',width=9, fg="white", bd=3, relief=RIDGE).place(x=220, y=140)


# infinite loop to run program
window.mainloop()
