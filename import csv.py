import csv
f=open("student.csv","w",newline='')
writer=csv.writer(f)

writer.writerow(["name","marks"])
writer.writerow(["Amit",85])
writer.writerow(["Riya",90])
f.close

f=open('student.csv',"r")
reader=csv.reader(f)
print(reader)
f.close()