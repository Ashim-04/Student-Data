#creating the signin function
def signin(username, password, filename):

#opening the file in read mode
    myFile = open(filename, "r")

#.readline().strip is used to read each line one by one
    uName = myFile.readline().strip()
    pWord = myFile.readline().strip()

#closing the file
    myFile.close()

#condition to check if both username and password is correct or incorrect
    if (username == uName and password == pWord):
        status = True
    else:
        status = False

    return status
