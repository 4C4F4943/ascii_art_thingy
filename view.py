import os
import time
import random
import  pyfiglet

fils = os.listdir()
files=[]

leng = os.get_terminal_size()
for i in range(len(fils)):
	if fils[i][-4:] == ".txt":
		files.append(fils[i])
what_print = ""
how_many_times_bigger = 0
for i in range(len(files)):
	inb = what_print + files[i][:-4]
	if len(inb) >= leng[0]*how_many_times_bigger:
		how_many_times_bigger += 1
		what_print += "\n"
	what_print += "[%.1i] "%(i) + files[i][:-4]+" "

def auto():
	for y in range(len(files)):
		cmd = "cat " + files[y]
		os.system(cmd)
		time.sleep(4)	

x = "n"
if x == "n":
	while True:
		print(what_print)
		print("-"*leng[0])
		inp = input("what art do you want to see: ")
		if inp == "exit":
			exit()
		elif inp == "clear":
			os.system("clear")
		elif inp == "auto":
			auto()
		try:
			cmd = "cat " + files[int(inp)]
			os.system(cmd)
		except:
			pass
		
		print("\n")

l = pyfiglet.figlet_format("That's it :)",font="smkeyboard")
print(l)


