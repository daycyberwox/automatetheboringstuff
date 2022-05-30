# Understanding global and local variables/scopes

# A "scope" covers an area of the source code
# A scope can also  be seen as a container of variables
# 1 - Code in a global scope cannot use any local variables
# 2 - Code in a clocal scope can access global variables
# 3 - Code in one function's local scope cannot use variables in another function's local scope
# 4 - The same name can be used for different variables if they are in different scopes



spam = 42 # global variable in the global scope

def eggs():
    spam = 42 # local variable in this function's local scope 