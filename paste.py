import pyperclip
import winsound

link=""
pyperclip.copy(link)

while(1):
	a=pyperclip.paste()
	if(link!=a):
		link = link + "\n"+a
		print a
		pyperclip.copy(link)
		winsound.Beep(2000,500)