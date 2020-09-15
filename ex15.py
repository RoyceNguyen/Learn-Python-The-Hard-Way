from sys import argv
#get argument
script, filename = argv
#open the user provided file
txt = open(filename)
#print out the file name and print out the text in the file
print(f"Here's your file {filename}:")
print(txt.read())
#same result with similar process
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())