'''
name=str(input("Name-"))
num=str(input("Phone Number-"))
file=open("data.txt","w")
file.write(name)
file.close()
file=open("data.txt","a")
file.write(num)
file.close()
'''
name=str(input("Name-"))
file=open("dataInput.txt","w+")
file.write(name)
file.seek(0)
print(file.read())
file.close()
