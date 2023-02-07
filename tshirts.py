
def size(cms):
    if cmd is None:
        return None
        #raise ValueError("Input is missing") the input is missing,raise an error or return a message indicating that the input is missing
    elif cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
assert(size(None) == None)
print("All is well (maybe!)\n")
