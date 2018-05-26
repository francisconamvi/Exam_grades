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
        print("There is a profile with this name. Do you want to overwrite it? (y/n)")
        des = input()
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
        subjects.append(input("Write the subject code: "))
        #new_file.write(subjects[-1]+"/n")
        enter = input("Want to register another subject?(y/n) ")
    print(subjects)

#MAIN
subjects = list()
menu = input("New/Load: ")
name = input("What's your name and last name? ")
if menu == "New":
    Test()
    New()

'''
path = '/home/francisconavy/Projetos/notas_comp/workfile.txt'
arq = open(path,'r')
print(arq.read())
'''
