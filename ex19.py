#defining a function that takes in 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #print out string passing it the argument in placeholders
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly:")
#calling function and passing it numbers
cheese_and_crackers(20, 30)
#declaring variables and give them values
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50 
#calling the function and passinging it the variables
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
#calling the function and passing it equations
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
#calling the functiong and passing it equation and variables
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
