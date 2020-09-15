from sys import argv
#get filname as argument
script, filename = argv
#print out the user prompt
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit ENTER.")
#wait for input
input("?")
#open the file and write to it using w argument
print("Opening the file...")
target = open(filename, 'w')
#remove whats in the file, not needed since we're passing w as arugment to the file
print("Truncating the file. Goodbye!")
target.truncate()
#ask user input
print("Now I'm going to ask you for three lines.")
#get user input
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#write user input to the file, seperated by new lines
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#close the file
print("And finally, we close it.")
target.close()