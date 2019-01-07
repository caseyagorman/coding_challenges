# Remove spaces in string

def no_space(x):
    for l in x:
        if l == " ":
            x = x.replace(l, "")
    return x 


def no_space(x):
    return x.replace(' ' ,'')

# Notes: you don't have to loop through the string to replace something
# you can just do it and return the result
