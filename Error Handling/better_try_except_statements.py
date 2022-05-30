# Handling errors with try and except statements


def div42by(divideByNum):  # function to divide 42 by any number
    try:         # Adding the try statement
        return 42 / divideByNum
    except ZeroDivisionError:
        print("Error: You tried to divide by zero.")

print(div42by(2))
print(div42by(12))
print(div42by(0))   # will cause an error since python does not know how to divide by 0
print(div42by(1))