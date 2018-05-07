#!/usr/bin/env python3

# Clear the screen for a fresh look
print("\033[H\033[J")

#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   TEith, 04/27/2018, Added code to complete assignment 5
#   TEith, 05/06/2018, Replaced several portions of code with functions
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

# Import 're' for Regex support and 'csv' for csv file manipulation
import re
import csv

# Define/set the variables
objFileName = ".\Todo.txt"
strData = ""
strDataInit = ""
dicRow = {}
lstTable = []

class routines(object):

	@staticmethod
	def menu():
		print ("""
		Menu of Options
		1) Show current data
		2) Add a new item.
		3) Remove an existing item.
		4) Save Data to File
		5) Exit Program
		""")
		# Recieve input from user
		strChoice = str(input("Which option would you like to perform? [1 to 5]: "))
		print()
		return strChoice

	@staticmethod
	def new():
		strTask = str(input("Task item: "))
		strTask = strTask.capitalize()
		strPriority = str(input("Set priority (high/low): "))
		tplData = (strTask,strPriority)
		return tplData, strTask, strPriority

	@staticmethod
	def list(table):
		strDataInit = ""
		for item in table:
			strDataInit = str(item)
			strDataInit = re.sub("[\[\]()']", "", strDataInit)	
			print(strDataInit)

# Load data from a file
# When the program starts, load each "row" of data 
# in "Todo.txt" into a python Dictionary.
print("Loading file...\n")
with open("Todo.txt", mode="r") as f:
	reader = csv.reader(f)
	dicRow = {rows[0]:rows[1] for rows in reader}
    
# Add the each dictionary "row" to a python list "table"
for key, value in dicRow.items():
	temp = (key,value)
	lstTable.append(temp)

# Display a menu of choices to the user
while(True):
	strChoice = routines.menu()

	# Show the current items in the table in a clean format
	if (strChoice.strip() == '1'):
		routines.list(lstTable)

	# Add a new item to the list/Table and Dictionary
	elif(strChoice.strip() == '2'):
		tplData, strTask, strPriority = routines.new()
		lstTable.append(tplData)
		print("\nTask: ", strTask)
		print("Priority: ", strPriority)
		print("has been added to the list")
	
	# Remove a new item from the Dictionary, clear the list, and compile it
	elif(strChoice == '3'):
		strDelTask = str(input("Task item to delete: "))
		for task in lstTable:
			if (task[0] == strDelTask.capitalize()):
				lstTable.remove(task)
				print("\nTask", strDelTask, "has been deleted")

	# Save tasks to the Todo.txt file after formatting the data
	elif(strChoice == '4'):
		for item in lstTable:
			strData += str(item) + "\n"
			strData = re.sub("[\[\]()']", "", strData)
			strData = strData.replace(", ", r",")
		objFileName = open("./Todo.txt", "w")
		objFileName.write(strData)
		objFileName.close()
		strData = ""
		print("All Tasks have been saved to 'Todo.txt'")

	# Exit the program	
	elif (strChoice == '5'):
		break

