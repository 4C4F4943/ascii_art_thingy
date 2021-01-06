import os
import time
import random
import  pyfiglet

fils = os.listdir()
files=[]

for i in range(len(fils)):
	if fils[i] != "view.py" and fils[i] != ".view.py.swo " and fils[i] != "README.md" and fils[i] != ".git":
		files.append(fils[i])
what_print = ""
for i in range(len(files)):
	what_print += "[%.1i] "%(i) + files[i]+" "
x = input("auto ?y/n: ")

def auto():
	for y in range(len(files)):
		cmd = "cat " + files[y]
		os.system(cmd)
		time.sleep(4)	


if x == "y":
	auto()
elif x == "n":
	while True:
		print("\n")
		print(what_print)
		leng = os.get_terminal_size()
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


l = pyfiglet.figlet_format("That's it :)",font="smkeyboard")
print(l)


