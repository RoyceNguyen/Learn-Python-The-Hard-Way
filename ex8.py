#assign a variable a string with 4 placeholders
formatter = "{} {} {} {}"
#using format function and pass 1 ,2 ,3 ,4 numberics as the values for placeholders
print(formatter.format(1,2,3,4))
#using format function and pass string as the values for placeholders
print(formatter.format("one", "two", "three", "four"))
#using format function and pass boolean values as the values for placeholders
print(formatter.format(True, False, False, True))
#using format function and pass the varriable to itself, printing out 16 placeholders {}
print(formatter.format(formatter, formatter, formatter, formatter))
#using format function and pass string as the values for placeholders
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "OR a song about fear"
))