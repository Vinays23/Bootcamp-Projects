import csv
a=1
b=2
while True:
    c=int(input("what would you like to do? \n 1.Add Participants \n 2.See participants\n"))
    if(c==a):
        name=input("Enter name")
        event=int(input("Select Event-\n 1.CS  2.Googleit  3.Treasure Hunt \n"))
        if(event==1):
            eve="CS"
        elif(event==2):
            eve="Googleit"
        else:
            eve="Treasure Hunt"
        record=[name,eve]
        with open('data.csv','a', newline='') as file:
            writer=csv.writer(file)
            writer.writerow(record)
    elif(c==b):
        with open('data.csv', newline='') as file:  
            reader = csv.reader(file)
            for row in reader:
                 print(" ".join(row))

    else:
        break


