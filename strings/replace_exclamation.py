# In a string, remove character ! n number of times. 
# remove("!Hi",1) === "Hi"
# remove("!Hi!",1) === "Hi!"
# remove("!Hi!",100) === "Hi"
# remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"

def remove(s, n):
    return s.replace("!", "", n)


def remove(s, n):
    count = 0
    new_string = ""

    for char in s:
        if char != "!":
            new_string = new_string + char
        elif char == "!":
            if count == n:
                new_string = new_string + char
                   
            elif count < n:
                count += 1
                continue
                   
              
    return new_string

    # Notes: replace is a string method that takes an option argument for 
    # number of times to make replacement