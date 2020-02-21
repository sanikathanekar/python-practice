print("Open File")
try:
    file = open("Xfile.txt","r")
except IOError:
    print("An error was found. Either path is incorrect or file doesn't exist!")
finally:
    print("Terminating process!")

