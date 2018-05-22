#!/usr/bin/env python3

# --------------------------------------------------------------#
# Title: Working with Classes
# Dev:   TEith
# Date:  May 20, 2018
# ChangeLog: (Who, When, What)
#   TEith, 05/20/2018, Modified assignment 8 template to include
#   adding a class
# NOTE: Products.txt must exist for this to run
# --------------------------------------------------------------#

# Clear the screen for a fresh look
print("\033[H\033[J")


# Class
class FileHelper(object):
    strUserInput = None  # A string which holds user input

    def write_product_user_input(self, file):  # Method for looping data entry
        try:
            print("Type in a Product Id, Name, and Price you want to add to the file")
            print("(Enter 'Exit' to quit!)")
            while True:
                self.strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")  # Collect input
                if self.strUserInput.lower() == "exit":  # Allow for program exit
                    break
                else:
                    file.write(self.strUserInput + "\n")  # Write contents of strUserInput to file
        except Exception as err:  # Error handling
            print("Error: " + str(err))

    @staticmethod
    def read_all_file_data(file, message="Contents of File"):
        try:
            print(message)  # Print contents read in from myFileHelper.read_all_file_data
            file.seek(0)  # Start at the beginning of txt file
            print(file.read())  # Print it out
        except Exception as err:  # Error handling
            print("Error: " + str(err))


# Data
objFile = None  # File Handle

# I/O
myFileHelper = FileHelper()  # Class I/0 set to variable

try:
    objFile = open("Products.txt", "r+")  # Set the File object
    myFileHelper.read_all_file_data(objFile, "Here is the current data:")  # Reads data from read_all_file_data method
    myFileHelper.write_product_user_input(objFile)  # Write File with data from write_product_user_input method
    myFileHelper.read_all_file_data(objFile, "Here is this data was saved:")  # Reread data

except FileNotFoundError as e:
    print("Error: " + str(e) + "\n Please check the file name")  # Did the file Products.txt get created?

except Exception as e:
    print("Error: " + str(e))  # All other errors

finally:
    if objFile is not None:
        objFile.close()  # Close the file
