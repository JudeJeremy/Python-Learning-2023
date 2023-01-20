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


def EditContacts():
    print("Which contact would you like to edit:")
    for x in contacts:
        print(x)
    editinput = int(input("Enter 0 to edit the first contact, enter 1 to edit the second contact etc "))
    newname = input("Enter the new name of this contact ")
    newphone = input("Enter the new phone number of this contact ")
    newemail = input("Enter the new email address of this contact ")
    updatecone = contacts[editinput]
    updatecone["name"] = newname
    updatecone["phone"] = newphone
    updatecone["email"] = newemail
    print(x)
    print("Contact succesfully updated")

def DeleteContacts():
    print("Which contact would you like to delete ")
    for x in contacts:
        print(x)
    deleteinput = int(input("Enter '0' to delete the first contact, enter 1 to delete the second contact etc "))
    contacts.pop(deleteinput)
    print("Contact successfully deleted")

def CreateFile():
    file = open("MyContactsList.txt", "x")
    print("A new file has been succesfully created")


def StartSequence():
    print("Welcome to Dariels AddressBook\nWhat would you like to do?")
    userinp = input("Enter 1 to view all your contacts\nEnter 2 to add a new contact\nEnter 3 to search your contacts\nEnter 4 to edit an existing contact\nEnter 5 to delete an existing contact\nEnter 6 to create a new file containing the list of your contacts\n")
    if userinp == "1":
        ViewContacts()
        ReturnHome()
    if userinp == "2":
        AddContacts()
        print("Contact has been succesfully added")
        ReturnHome()
    if userinp == "3":
        SearchContacts()
    if userinp == "4":
        EditContacts()
        ReturnHome()
    if userinp == "5":
        DeleteContacts()
        ReturnHome()
    if userinp == "6":
        CreateFile()
        ReturnHome()
    
def ReturnHome():
        backinput = input("type 'back' to return to the home screen ")
        if backinput == "back":
            StartSequence()

StartSequence()

