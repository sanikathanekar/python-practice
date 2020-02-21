'''
def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line
n=int(input("Enter a number-"))
print(pascal(n))

def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

print(pascal(6))
'''
'''
def pascal(n):
    if n == 1:
        return [1]
    else:
        p_line = pascal(n-1)
        line = [ p_line[i]+p_line[i+1] for i in range(len(p_line)-1)]
        line.insert(0,1)
        line.append(1)
    return line

print(pascal(6))
'''
def pascal(n):
    list=[1]
    for i in range(n):
        print(list)
        newlist=[]
        newlist.append(list[0])
        for i in range(len(list)-1):
            newlist.append(list[i]+list[i+1])
        newlist.append(list[-1])
        list=newlist
n = int(input("Enter the length- "))

if n<=0:
    print(pascal(5))
else:
    print(pascal(n))
