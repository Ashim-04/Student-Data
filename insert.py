import sys
from authentication import signin
userName = input("Enter your username: ")
passWord = input("Enter your password: ")
if (signin(userName,passWord,"secret.txt") == True):
    print("Welcome back!")
else:
    print("Username and password do not match!")
    sys.exit()
#opening the file in append mode
file = open("students.txt", "a")
#using this step, the program keeps asking the user to input until he says "done"
while True:
    iD = input("Enter student ID (or 'done' to finish): ")
#the program will stop once the user types in "done"
    if iD == "done":
        break
    name = input("Enter name: ")
    age = input("Enter age: ")
    location = input("Enter location: ")
#write the input data into the file with tab spaces in between
    file.write(iD+","+name+","+age+","+location+"\n")