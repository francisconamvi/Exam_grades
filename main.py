#!/usr/bin/python3
'''
class sub:
    def __init__(self):
        self.
'''

def Test():
    global name
    try:
        teste = open(name+".txt", "r")
        #if there isn't an error, it means that there is a file with the same name 
        des = input("There is a profile with this name. Do you want to overwrite it? (y/n) ")
        if des == "y":
            pass
        if des == "n":
            name = input("Choose a new name please: ")
            Test()
    except FileNotFoundError:
        #if the error occurs, the program can continue
        pass

def New():
    #Creating file
    new_file = open(name+".txt", "w")
    #Registering the subjects
    enter = "y"
    while enter != "n":
        subjects[input("Write the subject code: ")] = []
        enter = input("Want to register another subject?(y/n) ")
    print(subjects)
    
    #Add grades to each subject
    print("Put the grade, or 'c' if you want to calculate it")
    for subject in subjects:
        for ps in range(1,4):
            subjects[subject].append(input("%s P%d grade: "%(subject,ps)))
    print(subjects)
    
    #Putting it into a file
    for i in range(len(subjects)):
        new_file.write(str(list(subjects.keys())[i])+"\n")
        for j in range(3):
            if (str(list(subjects.values())[i][j])) != "": new_file.write(str(list(subjects.values())[i][j])+"\n")
        new_file.write("\n")

#MAIN
subjects = dict()
menu = input("New/Load: ")
name = input("What's your name and last name? ")
if menu == "New":
    Test()
    New()
