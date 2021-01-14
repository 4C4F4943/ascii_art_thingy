import os
import time
import random
import  pyfiglet

fils = os.listdir()
files=[]




import time
start = time.time()

#from animated_rainbow import animate_rainbow
def print_rainbow(txt,background=""):
  res = ""

  if background =="":
    b  = "1" 
  elif background == "-b": 
    b = "7" 
  x = ["37","33","31","35","34","32"] 
  z = 0 
  for i in range(len(txt)):
    res += "\033["+b+";"+x[z]+"m"+txt[i]+"\033[0m".strip()
    z += 1
    if i == len(txt)-1:
      res+= " " 
    if z == len(x):
      z = 0 
  return res 
"""
fil = open("test.txt","w")
import os
pr = ""
leng = os.get_terminal_size()
for i in range(leng[1]):
  inb = " "*leng[0]+"\n"
  pr += inb
fil.write(print_rainbow(pr,background="-b"))
print("took this long ",time.time()-start)
"""

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
		os.system("clear")
		cmd = "cat " + files[y]
		os.system(cmd)
		time.sleep(4)	
		print()
x = "n"
if x == "n":
	while True:
		print(what_print)
		print("-"*leng[0])
		inp = input("what art do you want to see: ")
		x = inp.split()
		if inp == "exit":
			exit()
		elif inp == "clear":
			os.system("clear")
		elif inp == "auto":
			auto()
		if x[0] == "rainbow":
			
			fil = open(files[int(x[1])],"r").read().split("\n")

			z = []
			for i in range(len(fil)):
  				z.append(print_rainbow(fil[i]+"\n"))
			print("".join(z))

	
		try:
			cmd = "cat " + files[int(inp)]
			os.system(cmd)
		except:
			pass
		
		print("\n")

l = pyfiglet.figlet_format("That's it :)",font="smkeyboard")
print(l)


