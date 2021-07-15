from os import listdir, remove
from time import sleep
from random import choice, uniform, randint
from names import get_first_name
import json

WINDOW_BOUNDS = {"tl":[0,0],"br":[500,500]}
COLORS = ["Blue", "Red", "Green", "White", "Black", "Orange", "Yellow"]
CHANCE_BIRTH = 0.5

def chanceDeath(x):
	return 0.01*pow(1.045,x)

class RBT:
	def __init__(self, name, 
		color, pos = [0,0], age = 0):
		self.color = color
		self.pos = pos
		self.name = name
		self.age = age
		self.deadFLG = False

	def __del__(self):
		return

	def getPos(self):
		return self.pos

	def getColor(self):
		return self.color

	def checkDeath(self):
		randomVar = uniform(0,1)
		if(randomVar<chanceDeath(self.age)):
			self.deadFLG = True
			print("The RBT named " + self.name + " died.")
		#print(randomVar,chanceDeath(self.age),self.age)

	def tick(self):
		self.age += 1
		self.checkDeath()

	def move(self):
		self.pos = [self.pos[0]+1,self.pos[1]+1]

	def save(self):
		return { "name" : self.name, "age" : self.age, 
							"color": self.color, "pos" : self.pos}

	def print(self):
		print(self.name,self.age,self.color,self.pos)

class game:
	def __init__(self,name,rbts = []):
		self.rbts = rbts
		self.name = name
		self.main()

	def __del__(self):
		print("End game")

	def main(self):
		while True:
			sleep(0.25)
			print("Running")
			self.tick()
			if(len(self.rbts) > 7):
				print(self.save())
				break

	def tick(self):
		if(uniform(0,1)<CHANCE_BIRTH):
			self.birthRBT()
		for rbt in self.rbts:
			rbt.tick()
			#print(rbt.deadFLG)
			if rbt.deadFLG == True:
				self.rbts.remove(rbt)
				del rbt

	def birthRBT(self):
		newRBT = RBT(name = get_first_name(), 
		color = choice(COLORS))
		self.rbts.append(newRBT)
		print("A RBT named " + newRBT.name + " was born. It is " + newRBT.color +".")

	def save(self):
		return {"gameName" : self.name, "rbts" : [x.save() for x in self.rbts]}

	def print(self):
		print(self.name)
		for rbt in self.rbts:
			rbt.print()

class gameFrame:
	def __init__(self):
		#Load data files
		self.saves = [ {"name" : x[:-5], "file" : "saves\\"+x} for x in listdir("saves")]
		self.gameSaveFile = None
		self.game = None

		self.mainMenu()

	def __del__(self):
		#Save and close
		return

	def mainMenu(self):
		#if there are no save files, show only the "New game, options, exit" options
		print("Welcome to RBTS!"+"\n")
		while True:
			self.saves = [ {"name" : x[:-5], "file" : "saves\\"+x} for x in listdir("saves")]
			print("Choose an option:"+"\n")
			if len(self.saves)>0:
				print("Game select")
			print("New game"+"\n"+"Options"+"\n"+"Exit"+"\n")
			sel = input("Selection:"+"\n")
			if sel == "Game select":
				while True:
					print("File select"+"\n")
					print("\n".join([x["name"] for x in self.saves])+"\n")
					saveSel = input("File selection:"+"\n")
					if saveSel in [x["name"] for x in self.saves]:
						self.gameSaveFile = [x for x in self.saves if x["name"]==saveSel][0]
						while True:
							print("Options:"+"\n"+"\n"+"Start"+"\n"+"Edit"+"\n"+"Delete"+"\n"+"Back"+"\n")
							sel = input("Selection:"+"\n")
							if sel == "Start":
								print("\n"+"Start save: "+saveSel)
								print(self.gameSaveFile)
								self.startSave()
								self.saveGame()
								break
							elif sel == "Edit":
								print("\n"+"Edit save: "+saveSel)
								break
							elif sel == "Delete":
								print("\n"+"Delete save: "+saveSel)
								sel = input("Are you sure you want to delete save "+saveSel+"? [Y] or [N]")
								if sel == "Y":
									remove(self.gameSaveFile["file"])
									print("Deleted")
								else:
									print("Canceled")
								break
							elif sel == "Back":
								break
							else:
								print("Invalid selection.")
						break
					else:
						print("Invalid selection.")
			elif sel == "New game":
				sel = input("New game name: ")
				self.game = game(sel)
				self.gameSaveFile = {"name" : sel, "file" : "saves\\"+sel+".json"}
				self.saveGame()
			elif sel == "Options":
				print("Options")
			elif sel == "Exit":
				self.__del__()
				break
			else:
				print("Invalid selection.")

	def startSave(self):
		print("Opened "+self.gameSaveFile['file'][6:])
		tmpRbts = []
		with open(self.gameSaveFile['file'], 'r') as fin:
			fin = json.load(fin)
			for rbtJson in fin['rbts']:
				tmpRbt = RBT(rbtJson['name'],rbtJson['color'],rbtJson['pos'],rbtJson['age'])
				tmpRbts.append(tmpRbt)
			self.game = game(fin['gameName'],tmpRbts)

	def saveGame(self):
		with open(self.gameSaveFile['file'], 'w') as fout:
			fout.write(json.dumps(self.game.save()))

newGameFrame = gameFrame()
#newGame = game("NewGame")
#newRbt = RBT("Steve")
#print(newRbt.save())

#newRbt.move()
#print(newRbt.getPos())