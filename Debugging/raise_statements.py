# make a custom message for an error
# raise Exception("This is the error message.")

# create a box printing function


def boxPrint(symbol, width, height):
    if len(symbol) !=1:
        raise Exception('"symbol" needs to be a string of length 1.')  # Adds the error exception
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2')
    print(symbol * width)

    for i in range(height -2 ):
        print(symbol + (' ' *  (width - 2)) + symbol)

    print(symbol * width)


print(boxPrint('*', 15, 5))
print(boxPrint('o', 5, 16))
#print(boxPrint('**', 15, 5))
print(boxPrint('*', 1, 1))