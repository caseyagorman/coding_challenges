
# Write a function that accepts an array of 10 integers (between 0 and 9), 
# that returns a string of those numbers in the form of a phone number.


# Solution using .format with args, constant time
def create_phone_number(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


# Solution using insert, n time
def create_phone_number(n):
    n = list(map(str, n))
    n.insert(0, "(")
    n.insert(4, ")")
    n.insert(5, " ")
    n.insert(9, "-")
    return "".join(n)

# Notes: don't forget to reassign and use list when using map.
#  If you just use map and don't use list you will get map object. 
# If you don't reassign it won't work. 
