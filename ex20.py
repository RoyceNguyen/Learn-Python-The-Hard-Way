from sys import argv

script, input_file = argv
#declaring function to read the file
def print_all(f):
    print(f.read())
#declaring function to move the pointer to start of file
def rewind(f):
    f.seek(0)
#declaring function to print out the line count read the current line
def print_a_line(line_count, f):
    print(line_count, f.readline())
#open the file from the prompt
current_file = open(input_file)

print("First let's print the whole file: \n")
#print the content of the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
#go back to start of the file
rewind(current_file)

print("Let's print three lines:")
#print current lines number and the string on the current line
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)
