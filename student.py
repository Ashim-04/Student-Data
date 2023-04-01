import sys

from authentication import signin
userName = input("Enter your username: ")
passWord = input("Enter your password: ")
if (signin(userName,passWord,"secret.txt") == True):
    print("Welcome back!")
else:
    print("Username and password do not match!")
    sys.exit()

import prettytable

#open the file for reading
file = open ("students.txt", "r")
#create a new table object
table = prettytable.PrettyTable()

#read the first line of the file and split it into column headings
headings = file.readline().strip().split(',')

#add the column headings to the table object
table.field_names = headings

#read the remaining lines of the file and add them to the table
for line in file:
#strip any whitespace and split the line into individual values
    values = line.strip().split(',')

#add the values to the table
    table.add_row(values)

#print the table to the console
print(table)

#this part is to count the total students
file = open ("students.txt", "r")
#count = -1 because we dont need the header to be counted
count = -1
#using for loop, the program adds 1 to count each time it reads the next line
for line in file:
    count = count + 1

print ("No of Students: ", count)

#this is the maximum age part
import csv
#maximum age must be assigned to 0
maxAge = 0
file = open("students.txt", newline='')
#here we use CSV(Comma-Separated Values) to read, because each value is split by commas
reader = csv.reader(file)
#the term next is used for reader becuase we
# dont need the header to be taken as age so that we can avoid errors.
next(reader)
#here, through looping we assign age = row[2].
# using the knowledge of arrays, the age section is in the 2nd index (0, 1, 2(age))
for row in reader:
    age = int(row[2])
    if (age > maxAge):
        maxAge = age
print("Highest age among Students: ", maxAge)
file.close()

#same concept for minimum age
#but we use sys.maxsize to assign minAge, because any age value read from the file will be smaller than it
minAge = sys.maxsize
file = open("students.txt", newline='')
reader = csv.reader(file)
next(reader)
for row in reader:
    age = int(row[2])
    if (age < minAge):
        minAge = age
print("Lowest age among Students: ", minAge)
file.close()
#closing the file is a good practice