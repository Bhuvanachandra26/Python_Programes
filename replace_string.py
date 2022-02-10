import string

str1 = "Hello, \n"
str2 = "How are you?"
str3 = "User"
print("The Statement is ")
print("'", str1, str3, str2, "'")

rep = input("\nEnter the Replacing String for 'User': ")

if len(rep) >= 3:
    print("\nString can be Replaced")
    print("\nStatement Before Replacing")
    print(str1, str3, str2)
    print("\nStatement After Replacing")

    repl = str.replace(str3, str3, rep)  # Replacing Logic for the String
    print("'", str1, repl, str2, "'")

else:
    print("!!! String cannot be Replaced !!!")