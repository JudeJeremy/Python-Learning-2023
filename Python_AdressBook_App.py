import time

contacts = []


def AddContacts():
    nameinput = input("Enter the name of your new contact ")
    phoneinput = input("Enter the phone number of your new contact ")
    emailinput = input("Enter the email address of your new contact ")
    
    global Details
    Details = {
        "name": nameinput,
        "phone": phoneinput,
        "email": emailinput,
    }
    contacts.append(Details)


def ViewContacts():
    for x in contacts:
        print(x)


def SearchContacts():
    searchinput = input("Enter the name of the contact that you want to view ")
    
    for x in contacts:
        if x == searchinput:
            print(x)
        elif x != searchinput:
            print("Invalid Name")
        else: 
            print("error")

def startsequence():
    print("Welcome to Dariels AddressBook\nWhat would you like to do?")
    userinp = input("Enter 1 to view all your contacts\nEnter 2 to add a new contact\nEnter 3 to search your contacts\n")
    if userinp == "1":
        ViewContacts()
        returnhome()
        
    if userinp == "2":
        AddContacts()
        print("Contact has been succesfully added")
        returnhome()
    if userinp == "3":
        SearchContacts()
    
def returnhome():
        backinput = input("type 'back' to return to the home screen ")
        if backinput == "back":
            startsequence()

startsequence()