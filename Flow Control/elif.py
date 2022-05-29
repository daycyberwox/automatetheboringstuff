# Using Elif


print("What is the password?")
pwd = input()
if pwd == "swordfish":
    print("Access granted!")
else:  
    print("Wrong password!")


print("How long is it?")
pwdlen = int(input())
if pwdlen == 15:
    print("You're in!")
elif pwdlen < 15:
    print("Not enough characters for provided password")
elif pwdlen > 15:
    print("Too many password characters!")