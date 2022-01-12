###Created by Aaron Sloan (WTC ISS 2021)###

#Pull system OS functions to allow in file.#
import os
#Pull sleep support.#
import time
#Pull saved Item definition and saved List from file.#
from LoadoutSave import Items
#Call function to clear screen.#
def clear():
	 _ = os.system("clear")
#Creates visual line on output.#
def separation():
	print(35*"=")
clear()
Welcome = "Welcome to the Armory!"
print(Welcome)
separation()
#Prints list on separate lines.#
print("Your last saved Loadout:", *Items, sep = "\n")
separation()
#Working list in volital memory.#
Loadout = []
#Adds saved list to volital memory.#
Loadout.extend(Items)
#Prints number of items in list.#
def numItems():
	print("You have", len(Loadout), "item(s) in your Loadout.")
separation()
#Ask user if they want to :
#Show List, Add to List, Remove from List, Save Changes, Exit#
def userChoice():
	print("1: Show Loadout")
	print("2: Add Item")
	print("3: Remove Item")
	print("4: Save Loadout")
	print("5: Exit")
#ValueError base 10 handling.###
	while True:
		try:
			choice = input("Please make a selection: ")
			choice = int(choice)
			break
		except ValueError:
			print("Please make a valid selection.(1-5)")
	if choice == 1:
		clear()
		print("This is your current Loadout:", *Loadout, sep = "\n")
		separation()
#Keep running until exit.#
		return userChoice()
	elif choice == 2:
		addItem()
	elif choice == 3:
		removeItem()
	elif choice == 4:
		saveLoadout()
	elif choice == 5:
		exit()
	else:
		return userChoice()
#Adds item to volital memory list.#
def addItem():
	newItem = str(input("What item are you adding? "))
	Loadout.append(newItem)
	clear()
	print("Your current Loadout has been updated: ", *Loadout, sep = "\n")
	separation()
	numItems()
	separation()
	return userChoice()
#Removes item to volital memory list.#
def removeItem():
	delItem = str(input("Which item will you be removing? "))
	Loadout.remove(delItem)
	clear()
	print("Your current Loadout has been updated: ", *Loadout, sep = "\n")
	separation()
	numItems()
	separation()
	return userChoice()
#Commit volital memory list to file.#
def saveLoadout():
	while True:
		try:
			saveChoice = input("Do you want to save your Loadout? (1)Yes (2)No ")
			saveChoice = int(saveChoice)
			break
		except ValueError:
			print("Please make a valid selection.(1-2)")
	if saveChoice == 1:
		with open("LoadoutSave.py", "w") as file:
			file.write("Items = %s" % Loadout)
			file.close
		from LoadoutSave import Items
		clear()
		print("Your Loadout has been saved.")
		separation()
		print("This is your saved Loadout: ", *Loadout, sep = "\n")
		separation()
		numItems()
		separation()
		return userChoice()
	elif saveChoice == 2:
		clear()
		print("Your Loadout was not saved.")
		return userChoice()
	else:
		return saveLoadout()
#Save upon exit.#
def exit():
	while True:
		try:
			askExit = input("Do you want to save before exiting? (1)Yes/(2)No ")
			askExit = int(askExit)
			break
		except ValueError:
			print("Please make a valid selection.(1-2)")
	if askExit == 1:
		with open("LoadoutSave.py", "w") as file:
			file.write("Items = %s" % Loadout)
			file.close
		separation()
		print("The Armory was Saved before Exit.")
#Pause screen for 5 seconds before next process.#
		time.sleep(5)
		clear()
	elif askExit == 2:
		separation()
		print("The Armory was NOT saved before exit.")
		time.sleep(5)
		clear()
	else:
		return exit()
userChoice()