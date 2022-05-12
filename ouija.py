import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkm
from PIL import ImageTk, Image

import os,time,sys
from os import system
from time import sleep

import pyttsx3 as pys
import speech_recognition as sr
import pyaudio

win=tk.Tk()
win.geometry('1536x864')
win.title("Ouija Board")
win.configure(background="Black")

image = Image.open("c:/Users/vishnu/OneDrive/Documents/python/ouija/home.png")
resize_image = image.resize((1400, 650))
img = ImageTk.PhotoImage(resize_image)
label1 = tk.Label(win,image=img).pack()
'''
# STARTING OF APP :
def callback():
    os.system('python start.py')
'''

def res():
	response=tkm.askquestion("Attention Please","Do you really wanna enter?")
	if response=="yes":
		page2()
	else:
		tkm.showinfo("EXIT Please","Good Bye!")

def bahr():
	exit()

def devops():
	win3=tk.Toplevel()
	win3.geometry('1536x864')
	win3.title("Ouija Board - Developer")
	win3.configure(background="Black")
	
	dev_img= Image.open("c:/Users/vishnu/OneDrive/Documents/python/ouija/3.png")
	resize_dev_img = dev_img.resize((1550,700))
	dev_f_img = ImageTk.PhotoImage(resize_dev_img)
	tk.Label(win3,image=dev_f_img).pack(side=TOP,anchor='n')
	def close():
		win3.destroy()
	tk.Label(win3, text="© Copyright 2021 : @VishnuSoniDhupad",fg="white",bg='gray6').pack(side='bottom',anchor='sw')
	exitdev=tk.Button(win3, text="Exit",width=10,height=2,fg='white',bg='gray20',command=close).pack(side=BOTTOM,expand=YES,anchor='se')
	win3.mainloop()

def code():
	win4=tk.Toplevel()
	win4.geometry('1536x864')
	win4.title("Ouija Board - Code")
	win4.configure(background="Black")
	
	code_img= Image.open("c:/Users/vishnu/OneDrive/Documents/python/ouija/2.png")
	resize_code_img = code_img.resize((1550,700))
	code_f_img = ImageTk.PhotoImage(resize_code_img)
	tk.Label(win4,image=code_f_img).pack(side=TOP,anchor='n')
	def close():
		win4.destroy()
	tk.Label(win4, text="© Copyright 2021 : @VishnuSoniDhupad",fg="white",bg='gray6').pack(side='bottom',anchor='sw')
	exitcode=tk.Button(win4, text="Exit",width=10,height=2,fg='white',bg='gray20',command=close).pack(side=BOTTOM, expand=YES,anchor='se')
	win4.mainloop()

def about():
	win5=tk.Toplevel()
	win5.geometry('1536x864')
	win5.title("Ouija Board - About")
	win5.configure(background="Black")

	tk.Label(win5, text="© Copyright 2021 : @VishnuSoniDhupad",fg="white",bg='gray6').pack(side='bottom',anchor='sw')
	abt_img= Image.open("c:/Users/vishnu/OneDrive/Documents/python/ouija/1.png")
	resize_abt_img = abt_img.resize((1550,700))
	abt_f_img = ImageTk.PhotoImage(resize_abt_img)
	tk.Label(win5,image=abt_f_img).pack(side=TOP,anchor='n')
	def close():
		win5.destroy()
	exitabt=tk.Button(win5, text="Exit",width=10,height=2,fg='white',bg='gray20',command=close).pack(side=BOTTOM, expand=YES,anchor='se')
	win5.mainloop()

def page2():
	win2=tk.Toplevel()
	win2.geometry('1536x864')
	win2.title("Ouija Board - Welcome")
	win2.configure(background="Black")

	p2img= Image.open("c:/Users/vishnu/OneDrive/Documents/python/ouija/ob.png")
	resize_imgp2 = p2img.resize((1500,500))
	imgp2 = ImageTk.PhotoImage(resize_imgp2)
	iconp2 = tk.Label(win2,image=imgp2).pack(side=TOP,anchor='n')

	Label=tk.Label(win2, text="-: Welcome to the world of Ouija Board :-",font=25,bg="gray20", fg="white").pack()
	def close():
		win2.destroy()
	def rec():
	## AUDIO - TO - TEXT
	
		r=sr.Recognizer()
	#	mic=sr.Microphone()
	#	mic.list_microphone_names() #list the available MIC in device. & give index from 0 to selective
		mic=sr.Microphone(device_index=3)
		with mic as source:
			audio=r.listen(source)
			
	#	type(audio) #audio type
		try:
			txt=r.recognize_google(audio) #recongnize the audio with google api's
			pys.speak("Question you asked is :")
			pys.speak(txt)
			
		# QUES
			Asked_ques = tk.Label(win2,text = "Asked Question :",bg="gray6",fg="white").place(x=670,y=600)
			asked_str= tk.Label(win2,text=str(txt),bg="black",fg="white").place(x=780,y=600)

	# check reply.py & dataset.py
			#import dataset as ds
			import reply as rp
			reply=rp.ans(txt)
			pys.speak(reply)

		except:
			pys.speak("Error, Please Try Again.")
			close()
		# ANS (RESPONSE)
		response = tk.Label(win2,text = "Response :",bg="gray6",fg="white").place(x=670,y=650)
		resp_str= tk.Label(win2,text=str(reply),bg="black",fg="white").place(x=780,y=650)

	tk.Label(win2,text='',bg="black").pack()
	tk.Button(win2,text="Press to Speak",width=10,height=1,command=rec,fg='white',bg='gray20').pack()
	tk.Label(win2,text='',bg="black").pack()

	exitp2=tk.Button(win2, text="Exit",width=10,height=2,fg='white',bg='gray20',command=close).pack(side=BOTTOM,expand=YES,anchor='se')
	tk.Label(win2, text="© Copyright 2021 : @VishnuSoniDhupad",fg="white",bg='gray6').place(x=1,y=750)
	win2.mainloop()

fm = Frame(win)
button1=tk.Button(win, text="Start",width=10,height=2,fg='white',bg='gray20', command=res).pack(side=LEFT, expand=YES)
button2=tk.Button(win, text="Exit",width=10,height=2,fg='white',bg='gray20',command=bahr).pack(side=LEFT, expand=YES)
button3=tk.Button(win, text="Developer",width=10,height=2,fg='white',bg='gray20',command=devops).pack(side=LEFT, expand=YES)
button4=tk.Button(win, text="Code",width=10,height=2,fg='white',bg='gray20',command=code).pack(side=LEFT, expand=YES)
button5=tk.Button(win, text="About",width=10,height=2,fg='white',bg='gray20',command=about).pack(side=LEFT, expand=YES)
label=tk.Label(win, text="© Copyright 2021 : @VishnuSoniDhupad",fg="white",bg='gray6').pack(side='bottom')
win.mainloop()