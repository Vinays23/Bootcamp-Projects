x=[]
y=[]
for i in range(0,4):
    name=input("Enter name")
    usn=int(input("Enter Usn"))
    x.append(name)
    y.append(usn)
print(x)
print(y)

dictionary = dict(zip(y, x))
print(dictionary)
print("\n")

a=[]
n=int(input("Enter the total no of words"))
for i in range(0,n):
    word=input("Enter the list words")
    a.append(word)

print(a)    
