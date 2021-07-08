from os import listdir
from time import sleep
from random import choice

WINDOW_BOUNDS = {"tl":[0,0],"br":[500,500]}
COLORS = ["Blue", "Red", "Green", "White", "Black", "Orange", "Yellow"]

def chanceDeath(x):
	return 0.01*pow(1.045,x)

class RBT:
	def __init__(self):
		self.color = choice(COLORS)
		self.pos = [0,0]
		self.name = "Bob"
		self.age = 0
		print("A RBT named " + self.name + " was born. It is " + self.color +".")

	def __del__(self): return

	def getPos(self):
		return self.pos

	def getColor(self):
		return self.color

	def checkDeath(self):
		return

	def tick(self):
		self.age += 1


	def move(self):
		self.pos = [self.pos[0]+1,self.pos[1]+1]

	def kill(self):
		print("The RBT named " + self.name + " died.")
		self.__del__()

class game:
	def __init__(self):
		self.RBTs = []

		self.main()

	def __del__(self):
		print("End game")

	def main(self):
		while True:
			sleep(0.25)
			print("Running")
			self.birthRBT()

	def birthRBT(self):
		newRBT = RBT()
		self.RBTs.append(newRBT)

class gameFrame:
	def __init__(self):
		#Load data files
		self.saves = [ {"name" : x[:-5], "file" : x} for x in listdir("saves")]

		#Open menu
		self.mainMenu()

	def __del__(self):
		#Save and close
		print("Closed")

	def mainMenu(self):
		#if there are no save files, show only the "New game, options, exit" options
		print("Welcome to RBTS!"+"\n")
		while True:
			print("Choose an option:"+"\n")
			if len(self.saves)>0:
				print("Resume game")
			print("New game"+"\n"+"Options"+"\n"+"Exit"+"\n")
			sel = input("Selection:"+"\n")
			if sel == "Resume game":
				while True:
					print("File select"+"\n")
					print("\n".join([x["name"] for x in self.saves])+"\n")
					saveSel = input("File selection:"+"\n")
					if saveSel in [x["name"] for x in self.saves]:
						while True:
							print("Options:"+"\n"+"\n"+"Start"+"\n"+"Edit"+"\n"+"Delete"+"\n"+"Back"+"\n")
							sel = input("Selection:"+"\n")
							if sel == "Start":
								print("\n"+"Start save: "+saveSel)
								self.startSave([x["file"] for x in self.saves if x["name"]==saveSel][0])
								break
							elif sel == "Edit":
								print("\n"+"Edit save:"+saveSel)
								break
							elif sel == "Delete":
								print("\n"+"Delete save:"+saveSel)
								break
							elif sel == "Back":
								break
							else:
								print("Invalid selection.")
						break
					else:
						print("Invalid selection.")
			elif sel == "New game":
				print("New game")
			elif sel == "Options":
				print("Options")
			elif sel == "Exit":
				self.__del__()
				break
			else:
				print("Invalid selection.")

	def startSave(self,file):
		print("Opened "+file)

#newGameFrame = gameFrame()

#newRbt = RBT()

#newRbt.getColor()
#newRbt.move()
#print(newRbt.getPos())

#newGame = game()

print(chanceDeath(100))
print("Test GIT")