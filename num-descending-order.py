# Make a function that can take any non-negative integer 
# as a argument and return it with its digits in descending order.
# Rearrange the digits to create the highest possible number.

def Descending_Order(num):
    num =int("".join(sorted(str(num), reverse=True)))

    return num


# Notes: "sorted works on a string, you do not need to turn a string into a list before 
# using sorted. Sorted will turn a string into a list and sort it. Sorted can also be given
# multiple arguments such as a key or reverse=True"