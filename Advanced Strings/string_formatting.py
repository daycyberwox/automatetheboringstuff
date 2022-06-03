# String formatting - interpolating

name = "Alice"
place = "Main Street"
time = "6PM"
food = "Turnips"

# Normal concatonating
print("Hello " + name + ", you are invited to a party at " + place + " at " + time + ". Please bring " + food + ".")


# Proper formatting using - %s
print("Hello %s, you are invited to a party at %s at %s. Please bring %s." % (name, place, time, food))