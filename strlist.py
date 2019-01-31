l=[]
for i in range(0,5):
    a=int(input("Enter the list elements:"))
    l.append(a)
str=input("Enter the string:")
str+='{0}'
l = [str.format(i) for i in l]
print(l)
