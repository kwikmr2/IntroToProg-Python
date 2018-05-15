#!/usr/bin/env python3

#-------------------------------------------------#
# Title: Exception handling and Pickle saving method
# Dev:   TEith
# Date:  May 14, 2018
# ChangeLog: (Who, When, What)
#   TEith, 05/13/2018, Initial release
#-------------------------------------------------#

# Clear the screen for a fresh look
print("\033[H\033[J")

# Import the Regex and pickle module
import re
import pickle

# Define the binary dat file to be written
objFile = open("FarmInventory.dat", "wb")

# Provide instructions
print("Please enter the type of Farm Animal and their Quantity")
print("When done, just hit ENTER at an empty 'Animal Type:' prompt\n")

# Define empty variables
myList = []
strData = ""
formData = ""

# Create a function for removing regular expressions
def formatting(item):
	strData = ""
	strData += str(item) + "\n"
	strData = re.sub("[()' ]", "", strData)
	strData = strData.replace(",", ":\t")
	return strData

# The start of the exception handling
try:
	# Loop through until strType is null
	while(True):
		# Collect the first item and check to see if
		# it is null otherwise get input for intQuantity
		strType = str(input("Animal Type: "))
		strType = strType.capitalize()
		if strType == "":
			break
		else:
			intQuantity = int(input("Quantity: "))
		# Tuple creation
		tplData = (strType, intQuantity)

		# Merge the tuples together to make a list
		myList.append(tplData)

	# For loop for formatting list contents
	for item in myList:
		formData += formatting(item)

	# Ask to save the data or exit
	decision = str(input("\nWould you like to write the data to file (yes/no)?: "))
	if decision.strip() == "yes":
		# Using pickle to dump data as binary
		pickle.dump(formData, objFile)
		print("Data written!")
		print(formData)
		input("\n\nPress ENTER to end program...")
	else:
		input("\n\nPress ENTER to end program...")

	# Don't forget to close the file
	objFile.close()

# Error exception statement for invalid data for intQuantity
except ValueError as e:
	print("You did not provide a numerical quantity!")
	print("Exiting program! Please re run the program.")
