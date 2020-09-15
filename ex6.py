#declaring a variable and assign it 10
types_of_people = 10
#declaring a variable, assigning it a string, 
# using f to format it and passing it the variable types_of_people
x = f"there are {types_of_people} types of people."
#declaring 2 variables and assign it strings
binary = "binary"
do_not = "don't"
#declaring a variable, assigning it a string, 
# using f to format it and passing it the variable binary and do_not
y = f"Those who know {binary} and those who {do_not}."
#printing the two string x and y
print(x)
print(y)
#printing x and y using string format
print(f"I said: {x}")
print(f"I also said: '{y}'")
#declaring 2 variables, assigning one with a boolean value and a string which takes an argument
hilarious = False
joke_avaluation = "Isn't that joke so funny ?! {}"
#print out joke_evaluation string, using .format() function and passing it the value of var hilarious
#var hilarious's value will replace the {} in the string joke_evaluation
print(joke_avaluation.format(hilarious))
#declaring two variables
w="This is the left side of..."
e = "a string with a right side."
#print out the two strings with one print statement using concatenation
print(w + e)