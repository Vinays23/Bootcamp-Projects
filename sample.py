import csv
csv_columns = ['Name','Usn']
record=[]
name=input("Enter name")
usn=input("Enter Usn")
record=[name,usn]
with open('data.csv','a', newline='') as csvfile:
    #writer=csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer=csv.writer(csvfile)
    writer.writerow(record)
    
