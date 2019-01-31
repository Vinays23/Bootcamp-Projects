my_dict = dict()
 
key = input("Enter the usn: ")
value = input("Enter the name: ")
 
my_dict[key] = value

for key,val in my_dict.items():
    print(key, "=>", val)
