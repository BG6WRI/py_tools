import pyperclip
import time
from googletrans import Translator
from tkinter import *

translator = Translator(service_urls=[
		'translate.google.cn',
	])
textBuff=''


def translate():
	global text
	global textBuff
	global translator
	if pyperclip.paste()!=textBuff :
		textBuff = pyperclip.paste()
		textNoBlank = textBuff.replace('\r\n', ' ').replace('\n', ' ')
		textResult=translator.translate(textNoBlank, dest='zh-CN').text
		text.delete('1.0','end')
		text.insert(END, textResult)
	root.after(500, translate)



root = Tk()
root.title("WRI_Translator")
root.wm_minsize(300, 300) 
root.attributes("-topmost", 1)



Label(root, text="Author : BG6WRI").pack()

global text
text=Text(font=40)
text.pack()
text.insert(END,'Study? \nStudy a P.')



root.after(0, translate)
root.mainloop()




