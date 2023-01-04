#Chung Li Qing  #Kong Jia Heng
#TP063092       #TPTP059472

from datetime import datetime
from datetime import date

#writing a (list containing lists) into a file; for writing the master lists into the original files = creationOfFiles()
def writeListsIntoFile(listName, fileName):
    fileHandler = open(fileName, 'w')
    for list in listName:
        for item in list:
            fileHandler.write(item)
            fileHandler.write(", ")
        fileHandler.write("\n")
    fileHandler.close()

def creationOfFiles(): #creating credential, admin, customer, category, event, order, and payment files
	listsOfCredentials = [["Username", "Password", "Role"],
							["liqing", "cliqing", "Admin"],
							["henry", "kjiaheng", "Admin"],
							["achuachu", "achu123", "Customer"],
							["booleanking", "ancient", "Customer"],
							["jettama", "jetty", "Customer"],
							["haozhetama", "fang", "Customer"],
							["milotama", "miloo", "Customer"]]
	
	writeListsIntoFile(listsOfCredentials, 'credentials.txt') #writing the fixed credential records/log in details into 'credentials.txt' file

	listsOfAdmins =	[["AdminUsername", "AdminName", "AdminContact", "AdminEmail"],
						["liqing", "Chung Li Qing", "0182805327", "TP063092@mail.apu.edu.my"],
						["henry", "Kong Jia Heng", "01116474038", "TP059472@mail.apu.edu.my"]]

	writeListsIntoFile(listsOfAdmins, 'admins.txt') #writing the master admin records into 'admins.txt' file

	listsOfCustomers = [["CustomerUsername", "CustomerName", "CustomerContact", "CustomerEmail"],
						["achuachu", "Achreen Kaur", "0123701928", "achreen@gmail.com"],
						["booleanking", "Alex Chiew", "0163457432", "chiew@gmail.com"],
						["jettama", "Jet", "0112334123", "jet@gmail.com"],
						["haozhetama", "Hao Zhe", "0167829384", "haozhe@gmail.com"],
						["milotama", "Milo Jet", "019456283929", "milo@gmail.com"]]
						
	writeListsIntoFile(listsOfCustomers, 'customers.txt') #writing list of customer information records into 'customers.txt' file

	listsOfCategories =	[["CategoryID", "CategoryName"],
							["C1", "Babies"],
							["C2", "Children & Teens"],
							["C3", "Adults"],
							["C4", "Celebrations"],
							["C5", "Company"],
							["C6", "Concerts"],
							["C7", "Sports"]]

	writeListsIntoFile(listsOfCategories, 'categories.txt') #writing the list of categories into 'categories.txt' file

	listsOfEvents = [["EventID", "CategoryID", "EventName", "EventType", "EventVenue", "EventDate", "EventTime", "EventPrice"], 
						["E1", "C1", "Full Moon", "Host", "set venue", "set date", "set time", "2000"], 
						["E2", "C1", "First Year", "Host", "set venue", "set date", "set time", "600"],
						["E3", "C2", "Birthday Party", "Host", "set venue", "set date", "set time", "800"],
						["E4", "C2", "Coming of Age", "Host", "set venue", "set date", "set time", "500"],
						["E5", "C2", "Victorious", "Host", "set venue", "set date", "set time", "300"],
						["E6", "C3", "Wedding Proposal", "Host", "set venue", "set date", "set time", "8000"],
						["E7", "C3", "Wedding Ceremony", "Host", "set venue", "set date", "set time", "12000"],
						["E8", "C3", "Baby Shower", "Host", "set venue", "set date", "set time", "1000"],
						["E9", "C3", "Gender Reveal", "Host", "set venue", "set date", "set time", "1000"],
						["E10", "C3", "Birthday Party", "Host", "set venue", "set date", "set time", "3000"],
						["E11", "C3", "Old Folk Birthday", "Host", "set venue", "set date", "set time", "3500"],
						["E12", "C3", "Anniversary Party", "Host", "set venue", "set date", "set time", "400"],
						["E13", "C4", "Chinese New Year", "Host", "set venue", "set date", "set time", "1500"],
						["E14", "C4", "Valentine's", "Host", "set venue", "set date", "set time", "200"],
						["E15", "C4", "Hari Raya", "Host", "set venue", "set date", "set time", "1500"],
						["E16", "C4", "Christmas", "Host", "set venue", "set date", "set time", "1500"],
						["E17", "C4", "Deepavali", "Host", "set venue", "set date", "set time", "1500"],
						["E18", "C4", "Full Moon Festival", "Host", "set venue", "set date", "set time", "600"],
						["E19", "C4", "Thanksgiving Dinner", "Host", "set venue", "set date", "set time", "600"],
						["E20", "C5", "Farewell Party", "Host", "set venue", "set date", "set time", "2500"],
						["E21", "C5", "Annual Dinner", "Host", "set venue", "set date", "set time", "3000"],
						["E22", "C5", "Company Trip", "Host", "set venue", "set date", "set time", "2000"],
						["E23", "C6", "Classical Concert", "Join", "APU - Auditorium 1", "Every Saturday", "7:00pm - 8:00pm", "13"],
						["E24", "C6", "Rock Concert", "Join", "APU - Auditorium 7", "Every Sunday", "7:00pm - 8:00pm", "10"],
						["E25", "C6", "Jazz Concert", "Join", "APU - Auditorium 4", "Every Friday", "7:00pm - 8:00pm", "10"],
						["E26", "C7", "Running Marathon", "Join", "APU", "Every Thursday", "7:00am - 9:00am", "10"],
						["E27", "C7", "Cycling", "Join", "Balik Pulau - Penang", "Every Sunday", "7:00am - 9:00am", "10"]]
	
	writeListsIntoFile(listsOfEvents, 'events.txt') #writing the list of events into 'events.txt' file

	listsOfOrders = [["OrderID", "Username", "EventID", "EventName", "EventType", "EventVenue", "EventDate", "EventTime", "EventPrice", "Quantity", "Total"],				
					["2022-05-24 10:36:54.935865", "achuachu", "E23", "Classical Concert", "Join", "APU - Auditorium 1", "Every Saturday", "7:00pm - 8:00pm", "13", "1", "13"],	
					["2022-05-26 11:35:55.230394", "booleanking", "E22", "Company Trip", "Join", "North Pole", "2069-06-24", "8:00pm - 12:00pm", "2000", "1", "2000"],
					["2022-05-25 12:12:12.121212", "jettama", "E26", "Running Marathon", "Join", "APU - Auditorium 7", "Every Thursday", "7:00am - 9:00am", "10", "1", "10"],
					["2022-05-27 13:14:15.151617", "haozhetama", "E27", "Cycling", "Join", "Balik Pulau, Penang", "Every Sunday", "7:00am - 9:00am", "10", "1", "10"],
					["2022-05-28 09:23:34.120938", "milotama", "E25", "Jazz Concert", "Join", "APU - Auditorium 4", "Every Friday", "7:00pm - 9:00pm", "10", "1", "10"]]

	writeListsIntoFile(listsOfOrders, 'orders.txt') #writing the order list made by customers into 'orders.txt' file

	listsOfPayments = [["PaymentID", "OrderID", "Username", "PaymentDate", "Total", "TransactionNumber"],
					  ["2022-05-24 10:37:04.939875", "2022-05-24 10:36:54.935865", "achuachu", "2022-05-24", "13", "0758358"],
					  ["2022-05-26 11:36:55.684594", "2022-05-26 11:35:55.230394", "booleanking", "2022-05-26", "2000", "8368443"],
					  ["2022-05-25 12:13:10.234612", "2022-05-25 12:12:12.121212", "jettama", "2022-05-25", "10", "192735"],
					  ["2022-05-27 13:15:15.567637", "2022-05-27 13:14:15.151617", "haozhetama", "2022-05-27", "10", "973462"],
					  ["2022-05-28 09:24:34.463688", "2022-05-28 09:23:34.120938", "milotama", "2022-05-28", "10", "542765"]]

	writeListsIntoFile(listsOfPayments, 'payments.txt') #writing the list of payment records made by customers into 'payments.txt' file

def generalPath(path): #all types of menus for different options, validates and return menu selection
    if path == "unregistered": #first page's menu
        print("\nKindly select an action from the 4 available courses of action. Example: 1")
        print("\n1. View all events") #to view by category, all events, or to go back
        print("2. Sign up as a Customer") #register customer's information
        print("3. Log in") #users login; leads into admin or customer paths
        print("4. Exit") #close the program
        print("__________________________________________________________________________")
        
        while True: 
            unregisteredPath = input("\nSelection: ") #get the selection which choose which options what they want
            print("___________________________________________________________________________________________")
            
            if unregisteredPath == "1" or unregisteredPath == "2" or unregisteredPath == "3" or unregisteredPath == "4":
                break #return these specific selections only
            else:
                print("\nSelection Error. Kindly ensure input is an integer that is among the available actions.") #selection error info message if users enter blank or wrong option
                print("____________________________________________________________________________________________")
                continue  
        return unregisteredPath      
    elif path == "customer": #main menu for customers
        print("\nWelcome, Customer!") #Welcome! Amardeep!
        print("\nKindly select an action from the 4 available courses of action. Example: 1") 
        print("\n1. View all events") #to view all
        print("2. View events by category") #to view by category
        print("3. Make an order") #customers making order  
        print("4. View my orders") #customers check their own orders
        print("5. View my payments") #customers check their own payment made
        print("6. Exit") #close program
        print("____________________________________________________________________________________________")

        while True:
            customerPath = input("\nSelection: ") #customer selection of options
            print("____________________________________________________________________________________________")
            
            if customerPath == "1" or  customerPath == "2" or customerPath == "3" or  customerPath == "4" or customerPath == "5" or customerPath == "6":
                break #accept and return these specific selections only
            else:
                print("\nSelection Error. Kindly ensure input is an integer that is among the available actions.") #selection error info message if users choose wrong options
                print("____________________________________________________________________________________________")
                continue
        return customerPath
    elif path == "admin": #main menu for admin
        print("\nWelcome, Admin!")
        print("\nKindly select an action from the 4 available courses of action. Example: 1")
        print("\n1. Add category")
        print("2. Add event")
        print("3. Modify event record")
        print("4. View events by category")
        print("5. View all customers' records")
        print("6. View all customers' payment")
        print("7. Search for customer's record")
        print("8. Search for payment record")
        print("9. Exit")
        print("____________________________________________________________________________________________")

        while True:
            adminPath = input("\nSelection: ")
            print("____________________________________________________________________________________________")
            
            if adminPath == "1" or adminPath == "2" or adminPath == "3" or adminPath =="4" or adminPath == "5" or adminPath == "6" or adminPath == "7" or adminPath == "8" or adminPath == "9":
                break
            else:
                print("\nSelection Error. Kindly ensure answer is an integer that is among the available actions.")
                print("____________________________________________________________________________________________")
                continue
        return adminPath
    elif path == "view": #menu for viewing events, either to view all events or view by selected category
        print("\nKindly select an action from the 3 available courses of action:")
        print("\n1. View all catagories to view events by Category")
        print("2. View all events")
        print("3. Go back")
        print("____________________________________________________________________________________________")

        while True:
            viewPath = input("\nSelection: ")
            print("____________________________________________________________________________________________")
        
            if viewPath == "1" or viewPath == "2" or viewPath == "3":
                break
            else:
                print("\nSelection Error. Kindly ensure answer is an integer that is among the available actions.")
                print("____________________________________________________________________________________________")
                continue    
        return viewPath
    elif path == "category": #menu for viewing categories and whether to go back or exit the program
        print("\nKindly select a CategoryID to view its available events. Example: C1\nAlternatively, select 'B' to go back or 'E' to exit. Example: B")
        print("____________________________________________________________________________________________")
        
        while True:
            categoryPath = input("\nSelection: ")
            print("___________________________________________________________________________________________")
            categoryPath = categoryPath.capitalize()
            
            if categoryPath == "B" or categoryPath == "E" or "C" in categoryPath:
                break
            else:
                print("\nSelection Error. Kindly ensure answer is either following the CategoryID displayed or is either 'B' or 'E'. Example: C1")
                print("____________________________________________________________________________________________")
                continue
        return categoryPath
    elif path == "cart": #menu for add items into cart; whether to add more or continue to payment
        while True:
            print("\nKindly select an action to proceed: ")
            print("\n1. Add item")
            print("2. Make payment") 
            print("____________________________________________________________________________________________")
            
            cartPath = input("\nSelection: ")
            print("____________________________________________________________________________________________")
            
            if cartPath == "1" or cartPath == "2":
                break
            else:
                print("\nSelection Error. Kindly ensure input is an integer that is among the available actions.") #selection error info out if users choose wrong options
                print("____________________________________________________________________________________________")
                continue
        return cartPath
    elif path == "modifyEvent": #message to validate and retrieve specific eventID that the admin wishes to modify
        while True:    
            print("\nKindly select an event to modify. Example: E1")
            print("____________________________________________________________________________________________")
            
            modifyPath = input("\nSelection: ")
            print("____________________________________________________________________________________________")
            modifyPath = modifyPath.capitalize()
            
            if modifyPath == "" or "E" not in modifyPath:
                print("\nSelection Error. Kindly ensure answer is following the EventID displayed. Example: E1")
                print("____________________________________________________________________________________________")
                continue
            else:
                break
        return modifyPath  
    elif path == "search": #menu to retrieve the admin's wishes to continue to search for another record or go back to previous page
        while True:
            print("\nKindly select an action to proceed.")
            print("\n1. Search for a record")
            print("2. Go back")
            print("____________________________________________________________________________________________")
            
            searchPath = input("\nSelection: ")
            print("____________________________________________________________________________________________")

            if searchPath == "1" or searchPath == "2":
                break
            else:
                print("\nSelection Error. Kindly ensure answer is an integer that is among the available options. Example: 1")
                print("____________________________________________________________________________________________")
                continue
        return searchPath
    elif path == "button": #menu to get know if users want to go back or exit program
        while True:
            print("\nKindly select 'B' to go back or 'E' to exit program.")
            selection = input("Selection: ")
            print("____________________________________________________________________________________________")
            selection = selection.capitalize()
                
            if selection == "B" or selection == "E":
                return selection
            else:
                print("____________________________________________________________________________________________")
                print("\nSelection Error. Kindly ensure input is either 'B' or 'E'. Example: B")
                print("____________________________________________________________________________________________")
                continue
            
#search list in file for condition and print list.
def printSelectedListFromFile(location, condition, fileName):
    fileHandler = open(fileName, "r")
    for line in fileHandler:
        list = line[:-3].split(", ") #split the string into a list
        if condition == list[location]:
            print(line[:-3])
        else:
            continue
    fileHandler.close()

#add each item from ONE list into a file.
def appendListIntoFile(listName, fileName):
    fileHandler = open(fileName, "a") #opens file in append mode
    for item in listName: 
        fileHandler.write(item) #write item to file
        fileHandler.write(", ") #write ", " right after the item
    fileHandler.write("\n") #after each item in the list has been apppended, add a line break
    fileHandler.close()

#print input for user to verify input, otherwise re-enter input, return Y/N.//
def getConfirmInputChoice(choice, variable): #get user to confirm their input, retrive, validate and return Y or N
    if choice == 1: #get confirm input; prints the variable
        print("\nYour input is:")
        print(variable)
        print("____________________________________________________________________________________________")
        
        while True:
            confirmChoice = input("\nConfirm input? Y/N: ")
            confirmChoice = confirmChoice.capitalize()
            print("____________________________________________________________________________________________")
            
            if confirmChoice == "Y" or confirmChoice == "N":
                return confirmChoice
            else:
                print("\nKindly ensure choice is either Y or N.")
                print("____________________________________________________________________________________________")
                continue
    elif choice == 2: #get confirm input but doesnt print the variable
        print("____________________________________________________________________________________________")
        
        while True:
            confirmChoice = input("\nConfirm input? Y/N: ")
            confirmChoice = confirmChoice.capitalize()
            print("____________________________________________________________________________________________")
            
            if confirmChoice == "Y" or confirmChoice == "N":
                return confirmChoice
            else:
                print("Kindly ensure choice is either Y or N.")
                print("____________________________________________________________________________________________")
                continue
        
    
#get registration details to place into credential and customer lists and write lists into respective files.
def customerRegistrationProcess():
    registrationStatus = False #false if not registered yet; true if registration is completed
	
    while registrationStatus == False:
        customerRecord = [] 
        credentialRecord = []
        
        customerUsername = input("\nEnter username: ")
        print("____________________________________________________________________________________________")
        
        fileHandler = open('credentials.txt', 'r') #checks if username exists
        for line in fileHandler:
            line = line[:-3]
            list = line.split(", ")
            if customerUsername == list[0]:
                print("\nRecord exists. Kindly log in.")
                print("____________________________________________________________________________________________")
                fileHandler.close()
                registrationStatus = True
                return registrationStatus #True = continues from general unregistered page
            else:
                continue #search new list
        fileHandler.close ()
        
        if customerUsername == "":
            print("\nKindly ensure input is correct.")
            print("____________________________________________________________________________________________")
            continue #gets username again
        else:
            confirmInput = getConfirmInputChoice(1, customerUsername) #checks if username is as intended
            if confirmInput == "N":
                continue #get password again
            else: 
                customerRecord.append(customerUsername) #adds username into customerRecord
                credentialRecord.append(customerUsername) #adds username into credentialRecord
                
        while True:
            customerPassword = input("\nEnter password: ")
            print("____________________________________________________________________________________________")
            length = len(customerPassword)
                
            if customerRecord == "" or length < 7: #password mustn't be blank and must be more than 7+
                print("\nKindly ensure input is correct and is 7 characters or more.")
                print("____________________________________________________________________________________________")
                continue #get password again    
            else:
                confirmInput = getConfirmInputChoice(1, customerPassword)
                if confirmInput == "N":
                    continue #get password again
                else: 
                    credentialRecord.append(customerPassword) #adds password into credential Record
                    break #get new customer detail
        while True:
            customerName = input("\nEnter customer's name: ")
            print("____________________________________________________________________________________________")
            
            if customerName == "":
                print("\nKindly ensure input is correct.")
                print("____________________________________________________________________________________________")
                continue
            else:
                confirmInput = getConfirmInputChoice(1, customerName)
                if confirmInput == "N":
                    continue
                else:
                    customerRecord.append(customerName)
                    break
        while True:
            print("\nExample: 0123456789")
            customerContact = input("Enter customer's contact: ")
            print("____________________________________________________________________________________________")
            length = len(customerContact)
                
            if customerContact == "" or length < 10: #contact mustn't be blank and must be 10+
                print("\nKindly ensure input is correct.")
                print("____________________________________________________________________________________________")
                continue
            else:
                confirmInput = getConfirmInputChoice(1, customerContact)
                if confirmInput == "N":
                    continue
                else:
                    customerRecord.append(customerContact)
                    break		
        while True:
            customerEmail = input("\nEnter email address: ")
            print("____________________________________________________________________________________________")
            
            if customerEmail == "" or "@" not in customerEmail: #@ must be in
                print("\nKindly ensure input or format is correct.")
                print("____________________________________________________________________________________________")
                continue
            else:
                confirmInput = getConfirmInputChoice(1, customerEmail)
                if confirmInput == "N":
                    continue
                else:
                    customerRecord.append(customerEmail)
                    break #print input details for user verification
                    
        print("\n" + customerRecord[1] + "'s Customer Record:") #customer's name
        print("\nUsername: " + customerRecord[0])
        print("Password: " + credentialRecord[1])
        print("Customer's Name: " + customerRecord[1])
        print("Customer's Contact: " + customerRecord[2])
        print("Customer's Email: " + customerRecord[3])
            
        confirmInput = getConfirmInputChoice(2, None) #none because the function has a 2nd parameter that's not used here; it cannot be empty 
        if confirmInput == "N":
            continue
        else:
            credentialRecord.append("Customer") #add customer's role into credential; will be used to give admin or user access
            appendListIntoFile(credentialRecord, 'credentials.txt') #appends crendentialRecord to credentials file
            appendListIntoFile(customerRecord, 'customers.txt') #appends customerRecord to customer file
            print("\nRegistration is completed. Kindly log in to have access to the system.")
            print("____________________________________________________________________________________________")
            registrationStatus = True #indicates registration completed
            
    return registrationStatus #returns to continue from unregistered page(for log in)

    # log in and return username and role for use when customers make an order
def loginProcess():
    username = input("\nEnter username: ")
    antenna = False #True if username exists
    
    fileHandler = open('credentials.txt', "r")
    for line in fileHandler:
        line = line[0:-3]
        list = line.split(", ")
        if username == list[0]:
            antenna = True #username exists so get password
            record = list #retrieve user details
            break
        else:
            continue
    fileHandler.close
    
    if antenna == True:
        while True:
            password = input("\nEnter password: ")
            print("____________________________________________________________________________________________")
            if password == record[1]: #checks if username match the password in the credential record
                print("\nLog in successful.")
                print("____________________________________________________________________________________________")
                return record[0], record[2] #returns username and role to get into admin/customer path
            else:
                print("\nPassword incorrect. Kindly enter again.") #gets password again
                print("____________________________________________________________________________________________")
                continue
    else:
        print("____________________________________________________________________________________________")
        print("\nRecord does not exist. Kindly register.")
        print("____________________________________________________________________________________________")
        return "go back" #returns to unregistered page to register

#view events by category and return whether to continue from the unregistered page (to register or log in) or to exit the program.//
def viewEventsByCategory():
    while True:
        print("\nAll Categories:\n") #prints all available categories for users to pick 1
        fileHandler = open("categories.txt", "r")
        for list in fileHandler:
            print(list[0:-3])
        fileHandler.close()
        print("____________________________________________________________________________________________")
        
        byCategoryPath = generalPath("category") #returns validated path for category or to go back/exit
        if byCategoryPath == "B" or byCategoryPath == "E":
            return byCategoryPath #return "B" to continue from unregistered or other main menu or "E" to exit program
        else:
            existenceOfEvents = False #True if categoryID exists in file
            fileHandler = open('events.txt', 'r')
            for line in fileHandler:
                list = line[:-3].split(", ")
                if list[1] == byCategoryPath:
                    existenceOfEvents = True #categoryID found 
                    break #moves to next block
                else:
                    continue #continue searching
            fileHandler.close()
            if existenceOfEvents == True: #prints all events available for the categoryID
                print("\nAll events for " + byCategoryPath + "\n")
                fileHandler = open('events.txt', 'r')
                for line in fileHandler:
                    list = line[:-3].split(", ")
                    if list[1] == byCategoryPath:
                        print(line[:-3])
                    else:
                        continue
                fileHandler.close()
                print("____________________________________________________________________________________________")
                continue
            else: #events with the categoryID doesn't exist, so print none message
                print("\nThere are currently no events under this category. Kindly select another.")
                print("____________________________________________________________________________________________")
                continue
            
#customer's program.
def customer(userDetails):
    username = userDetails #
    cart = [] #cart to put items
    
    while True:
        customerOption = generalPath("customer")
        if customerOption == "1": #view all events
            print("\nAll events:\n")
            
            fileHandler = open('events.txt', "r")
            for list in fileHandler:
                print(list[:-3])
            fileHandler.close()
            print("____________________________________________________________________________________________")
            continue
        elif customerOption == "2": #view events by category
            categoryPath = viewEventsByCategory() #returns only "E" or "B"
            if categoryPath == "E": #exitprog
                exit = True
                break
            else: #back
                continue
        elif customerOption == "3": #make order
            orderProcess(username)
        elif customerOption == "4": #view orders
            print("\n" + username + "'s Order History\n")
            print("OrderID, Username, EventID, EventName, EventType, EventVenue, EventDate, EventTime, EventPrice, Quantity, Total")
            
            printSelectedListFromFile(1, username, 'orders.txt')
            print("____________________________________________________________________________________________")
            continue
        elif customerOption == "5": #view payment
            print("\n" + username + "'s Payment History\n")
            print("PaymentID, OrderID, Username, PaymentDate, Total, TransactionNumber")
            
            printSelectedListFromFile(2, username, 'payments.txt')
            print("____________________________________________________________________________________________")
            continue
        else:
            exit = True 
            break #exit program
    return exit #exit program

def retrieveEvent(eventID): #get particular event record for use during order making
    fileHandler = open("events.txt", "r")
    for line in fileHandler:
        list = line[0:-3].split(", ")
        if eventID != list[0]:
            continue
        else:
            event = list #store list in event and return
            fileHandler.close
            break
    fileHandler.close()
    return event

#whole order process from order to payment.//
def orderProcess(userDetails):
    username = userDetails #user's username
    fileHandler = open("events.txt", "r") #print all events to pick
    print("\nAll available events:\n")
    for line in fileHandler:
        print(line[0:-3])
    fileHandler.close()
    print("____________________________________________________________________________________________")
    
    cart = []
    orderRecord = []
    
    while True:
        print("\nKindly select an event from the available events. Example: E1")
        print("____________________________________________________________________________________________")
        
        eventItem = input("\nSelection: ")
        print("____________________________________________________________________________________________")
        
        if eventItem == "":
            print("\nSelection error. Kindly ensure input is from among the available events such as E1 or E2.")
            print("____________________________________________________________________________________________")
            continue
        else:
            eventItem = eventItem.capitalize()
            cart.append(eventItem) #add item to cart
            
            print("\nYou have selected:")
            print(cart)
            print("____________________________________________________________________________________________")
            
            cartOption = generalPath("cart") #to add more items or make payment
            
            if cartOption == "1": #add item
                continue
            else: #make payment
                for item in cart:
                    eventDetails = retrieveEvent(item) #get record details
                    orderID = str(datetime.now()) #create orderID 
                    orderRecord.append(orderID) #append orderID to orderRecord
                    orderRecord.append(username) #append username to orderRecord
                    
                    orderRecord.append(eventDetails[0]) #append eventID to orderRecord
                    orderRecord.append(eventDetails[2]) #append eventName to orderRecord
                    orderRecord.append(eventDetails[3]) #append eventType to orderRecord
                    
                    if eventDetails[3] == "Host":
                        eventVenue = getDetails("venue") #get venue details
                        orderRecord.append(eventVenue) #append eventVenue to orderRecord
                        
                        eventDate = getDetails("date") #get date details
                        orderRecord.append(eventDate) #append eventDate to orderRecord
                        
                        eventTime = getDetails("time") #get time details
                        orderRecord.append(eventTime) #append eventTime to orderRecord
                        
                        eventPrice = eventDetails[7] #retrive price from eventDetails
                        eventPrice = int(eventPrice) #change to int to do calculations
                        quantity = 1 #one each for hosting
                        total = eventPrice * quantity #multiply eventPrice and quantity
                        
                        orderRecord.append(str(eventPrice)) #append eventPrice to orderRecord
                        orderRecord.append(str(quantity)) #append eventQuantity to orderRecord
                        orderRecord.append(str(total)) #append eventTotal to orderRecord
                        
                        appendListIntoFile(orderRecord, 'orders.txt') #add list into file
                        paymentDetails = paymentProcess(orderRecord) #make payment
                        
                        print("\nOrder made succesfullly.\n")
                        print("Order Details:")
                        print("['OrderID', 'Username', 'EventID', EventName', 'EventType', 'EventVenue', 'EventTime', 'EventDate', 'EventPrice', 'Quantity', 'Total']")
                        print(orderRecord)
                        print("\nPayment Details:")
                        print("['PaymentID', 'OrderID', 'Username', 'PaymentDate', 'Total', 'TransactionNumber']")
                        print(paymentDetails)
                        print("____________________________________________________________________________________________")
                        orderRecord = [] #clear list for next order
                    else:
                        orderRecord.append(eventDetails[4]) #append event venue to record
                        orderRecord.append(eventDetails[5]) #append event date to record
                        orderRecord.append(eventDetails[6]) #append event time to record
                    
                        eventPrice = eventDetails[7] #append eventPrice to record
                        eventPrice = int(eventPrice) #convert to do calculations
                        
                        quantity = int(getDetails("quantity")) #get quantity of ticket
                        total = eventPrice * quantity
                        
                        orderRecord.append(str(eventPrice)) #append eventPrice to record
                        orderRecord.append(str(quantity)) #append quantity to record
                        orderRecord.append(str(total)) #append total to record
                        
                        appendListIntoFile(orderRecord, 'orders.txt') #append list into file
                        paymentDetails = paymentProcess(orderRecord) #make payment
                        
                        print("\nOrder made succesfullly.\n")
                        print("Order Details:")
                        print("['OrderID', 'Username', 'EventID', EventName', 'EventType', 'EventVenue', 'EventTime', 'EventDate', 'EventPrice', 'Quantity', 'Total']")
                        print(orderRecord)
                        print("\nPayment Details:")
                        print("['PaymentID', 'OrderID', 'Username', 'PaymentDate', 'Total', 'TransactionNumber']")
                        print(paymentDetails)
                        print("____________________________________________________________________________________________")
                        orderRecord = [] #clear list for new order   
                break       			
    
#get details with validation for making orders and payment.
def getDetails(info):
    if info == "venue":
        while True:
            venue = input("\nKindly insert the desired venue: ")
            print("____________________________________________________________________________________________")
            
            if venue == "":
                print("\nKindly ensure input is correct.")
                print("____________________________________________________________________________________________")
                continue
            else:
                confirmInput = getConfirmInputChoice(1, venue)
                if confirmInput == "N":
                    continue
                else:
                    break
        return venue
    elif info == "date":
        while True:
            date = input("\nExample: 19-06-2022\nKindly insert the desired date: ")
            print("____________________________________________________________________________________________")
            
            if date == "":
                print("\nKindly ensure input is correct.")
                print("____________________________________________________________________________________________")
                continue
            else:
                confirmInput = getConfirmInputChoice(1, date)
                if confirmInput == "N":
                    continue
                else:
                    break
        return date
    elif info == "time":
        while True:
            time = input("\nExample: 2pm-5pm\nKindly insert the desired time: " )
            print("____________________________________________________________________________________________")
            
            if time == "":
                print("\nKindly ensure input is correct.")
                print("____________________________________________________________________________________________")
                continue
            else:
                confirmInput = getConfirmInputChoice(1, time)
                if confirmInput == "N":
                    continue
                else:
                    break
        return time
    elif info == "quantity":
        while True:
            quantity = input("\nKindly insert the desired quantity: ")
            print("____________________________________________________________________________________________")
            
            if quantity == "":
                print("\nKindly ensure input is correct.")
                print("____________________________________________________________________________________________")
                continue
            else:
                confirmInput = getConfirmInputChoice(1, quantity)
                if confirmInput == "N":
                    continue
                else:
                    break
        return quantity
    elif info == "transaction":
        while True: 
            print("\nOrder will only be processed once payment is confirmed.")
            transactionNumber = input("Kindly enter transaction number and ensure its accuracy for a smooth order process: ")
            print("____________________________________________________________________________________________")
            
            if transactionNumber == "":
                print("\nKindly ensure input is correct.")
                print("____________________________________________________________________________________________")
                continue
            else: 
                confirmInput = getConfirmInputChoice(1, transactionNumber)
                if confirmInput == "N":
                    continue
                else:
                    break	
        return transactionNumber

#function for appending details into paymentRecord; append record into file later
def paymentProcess(listName):
    paymentRecord = []
    
    paymentID = str(datetime.now()) #create payment ID
    paymentRecord.append(paymentID) #append paymentID to record
    paymentRecord.append(listName[0]) #append orderID to record
    paymentRecord.append(listName[1]) #append username to record
    paymentDate = str(date.today()) #get today's date
    paymentRecord.append(paymentDate) #app payment date to record
    paymentRecord.append(listName[-1]) #append total amount to record
    transactionNumber = getDetails("transaction") #get transaction number
    paymentRecord.append(transactionNumber) #append transaction number to record
    
    appendListIntoFile(paymentRecord, 'payments.txt') #append record to file
    return paymentRecord

def admin(adminDetails):
    exit = True #to exit or not
    username = adminDetails
    while True:
        adminOption = generalPath("admin")
        if adminOption == "1": #add category
            addCategory()
            continue
        elif adminOption == "2": #add event
            addEvent()
            continue
        elif adminOption == "3": #modify event
            modifyEventMain()
            continue
        elif adminOption == "4": #view all events
            categoryOption = viewEventsByCategory() #return b/e only; viewing done in func
            if categoryOption == "B":
                continue
            else:
                break #exit
        elif adminOption == "5": #view all customers records
            print("\nAll Customers' Records:\n")
            
            fileHandler = open("customers.txt", "r")
            for line in fileHandler:
                print(line[:-3])
            fileHandler.close()
            print("____________________________________________________________________________________________")            
            continue
        elif adminOption == "6": # view all customers payment
            print("\nAll Payments' Records:\n")
            fileHandler = open("payments.txt", "r")
            for line in fileHandler:
                print(line[:-3])
            fileHandler.close()
            print("____________________________________________________________________________________________")
            continue
        elif adminOption == "7": #search for customer's record
            while True:
                searchOption = generalPath("search") #whether to search or go back
                
                if searchOption == "1": #get keyword
                    keyword = input("\nEnter keyword to search: ")
                    print("____________________________________________________________________________________________")
                    
                    print("\nRecords Available:\n")
                    
                    fileHandler = open("customers.txt", "r")
                    for line in fileHandler:
                        if keyword not in line:
                            continue
                        else:
                            print(line[:-3])
                    fileHandler.close()
                    print("____________________________________________________________________________________________")
                    continue #search or go back
                else:
                    break #continue to admin menu
            continue
        elif adminOption == "8": #search for payment record
            while True:
                searchOption = generalPath("search") #continue search or go ack
                
                if searchOption == "1": #get keyword
                    keyword = input("\nEnter keyword to search: ")
                    print("____________________________________________________________________________________________")
                    
                    print("\nRecords Available:\n")
                    fileHandler = open("payments.txt", "r")
                    for line in fileHandler:
                        if keyword not in line:
                            continue
                        else:
                            print(line[:-3])
                    fileHandler.close()
                    print("____________________________________________________________________________________________")
                    continue #search or go back
                else:
                    break #continue to admin menu
            continue
        else:
            break
    return exit #exit program

def addCategory():
    addStatus = False #false = category not added 
    continueStatus = False #true = category exists, enter another id
    
    while addStatus == False:
        categoryRecord = []
        
        print("\nAll categories:\n") #show available categories
        
        fileHandler = open("categories.txt", "r")
        for list in fileHandler:
            print(list[:-3])
        fileHandler.close
        print("____________________________________________________________________________________________")

        categoryID = input("\nEnter new Category ID: ")
        categoryID = categoryID.capitalize()
        print("____________________________________________________________________________________________")
        
        if categoryID == "" or "C" not in categoryID:
            print("\nKindly ensure input is correct.")
            print("____________________________________________________________________________________________")
            continue
        else: #check if categoryID already exists
            fileHandler = open("categories.txt", "r")
            for list in fileHandler:
                list = list[:-3].split(", ")
                if categoryID != list[0]:
                    continueStatus = False
                    continue 
                else:
                    print("\nRecord exists. Kindly insert a new CategoryID.")
                    print("____________________________________________________________________________________________")
                    fileHandler.close()
                    continueStatus = True
                    break
            fileHandler.close()
            
            if continueStatus == False: #confirm new categoryID
                confirmInput = getConfirmInputChoice(1, categoryID)
                
                if confirmInput == "N":
                    continue
                else:
                    categoryRecord.append(categoryID) #append ID to record
            else: #continue to insert new categoryID
                continue
        while True:
            categoryName = input("\nEnter new Category Name: ")
            print("____________________________________________________________________________________________")
            
            if categoryName == "":
                print("\nKindly ensure input is correct.\n")
                continue
            else:
                confirmInput = getConfirmInputChoice(1, categoryName)

                if confirmInput == "N":
                    continue
                else: 
                    categoryRecord.append(categoryName) #append categoryName to record
                    break #print record to confirm
                
        print("\nCategory ID: " + categoryRecord[0])
        print("Category Name: " + categoryRecord[1])

        confirmInput = getConfirmInputChoice(2, None) #confirm category record or not
        if confirmInput == "N": #re-enter new category record
            continue
        else:
            appendListIntoFile(categoryRecord, "categories.txt") #append record into list
            print("\nCategory added successfully.")
            print("____________________________________________________________________________________________")
            addStatus = True #break loop 

def addEvent():
    addStatus = False #false = category not added yet
    continueStatus = False #true = category exists, enter another id
    
    while addStatus == False:
        eventRecord = []
        
        print("\nAll Events:\n") #view all available events
        
        fileHandler = open("events.txt", "r")
        for list in fileHandler:
            print(list[:-3])
        fileHandler.close()
        print("____________________________________________________________________________________________")
        
        eventID = input("\nEnter new Event ID: ")
        eventID = eventID.capitalize()
        print("____________________________________________________________________________________________")
        
        if eventID == "" or "E" not in eventID:
            print("\nKindly ensure input is correct.")
            print("____________________________________________________________________________________________")
            continue
        else: #check if eventID already exists
            fileHandler = open("events.txt", "r")
            for list in fileHandler:
                list = list[:-3].split(", ")
                if eventID != list[0]:
                    continueStatus = False
                    continue 
                else:
                    print("\nRecord exists. Kindly insert a new eventID.")
                    print("____________________________________________________________________________________________")
                    continueStatus = True
                    break
            fileHandler.close() 

            if continueStatus == False: #confirm new eventID
                confirmInput = getConfirmInputChoice(1, eventID)
                if confirmInput == "N":
                    continue
                else:
                    eventRecord.append(eventID) #append ID to record
            else: #continue to insert new categoryID
                continue
        while True:
            print("\nAll Categories:\n") #print all available categories
            fileHandler = open("categories.txt", "r")
            for list in fileHandler:
                print(list[0:-3])
            fileHandler.close
            print("____________________________________________________________________________________________")

            categoryID = input("\nEnter Category ID: ")
            categoryID = categoryID.capitalize()
            print("____________________________________________________________________________________________")
            
            if categoryID == "" or "C" not in categoryID:
                print("\nKindly ensure input is correct and starts with 'C'.")
                print("____________________________________________________________________________________________")
                continue
            else:
                confirmInput = getConfirmInputChoice(1, categoryID)
                if confirmInput == "N":
                    continue
                else:
                    eventRecord.append(categoryID) #append categoryID to record
                    break
        while True:
                eventName = input("\nEnter new Event Name: ")
                eventName = eventName.title()
                print("____________________________________________________________________________________________")
                
                if eventName == "":
                    print("\nKindly ensure input is correct.")
                    print("____________________________________________________________________________________________")
                    continue
                else:
                    confirmInput = getConfirmInputChoice(1, eventName)
                    if confirmInput == "N":
                        continue
                    else:
                        eventRecord.append(eventName) #append eventName to record
                        break
        while True:
            eventType = input("\nEnter Event Type: ")
            eventType = eventType.capitalize()
            print("____________________________________________________________________________________________")
            
            if eventType == "Host" or eventType == "Join":
                eventRecord.append(eventType) #append eventType to record
                break
            else:
                print("\nKindly ensure input is correct and is either 'Join' or 'Host'.")
                print("____________________________________________________________________________________________")
                continue
        if eventType == "Host": #host event so user has to input these later on
            eventRecord.append("set venue")
            eventRecord.append("set date")
            eventRecord.append("set time")
            
            while True:
                eventPrice = int(input("\nEnter Event Price: "))
                print("____________________________________________________________________________________________")
                
                if eventPrice == "" or eventPrice < 0:
                    print("\nKindly ensure input is correct and is greater than 0.")
                    print("____________________________________________________________________________________________")
                    continue
                else:
                    eventPrice = str(eventPrice)
                    eventRecord.append(eventPrice) #append price to record
                    break

            appendListIntoFile(eventRecord, 'events.txt') #append record to file
            print("\nEvent added successfully.")
            print("____________________________________________________________________________________________")
            addStatus = True #break loop
        elif eventType == "Join":
            while True: 
                eventVenue = input("\nEnter Event Venue: ")
                print("____________________________________________________________________________________________")

                if eventVenue == "":
                    print("\nKindly ensure input is correct.")
                    print("____________________________________________________________________________________________")
                    continue
                else:
                    confirmInput = getConfirmInputChoice(1, eventVenue)
                    if confirmInput == "N":
                        continue
                    else:
                        eventRecord.append(eventVenue) #append venue to record
                        break
            while True:
                eventDate = input("\nEnter Event Date: ")
                print("____________________________________________________________________________________________")
                
                if eventDate == "":
                    print("\nKindly ensure input is correct.")
                    print("____________________________________________________________________________________________")
                    continue
                else:
                    confirmInput = getConfirmInputChoice(1, eventDate)
                    
                    if confirmInput == "N":
                        continue
                    else:
                        eventRecord.append(eventDate)
                        break
            while True:
                eventTime = input("\nEnter Event Time: ")
                print("____________________________________________________________________________________________")
                
                if eventTime == "":
                    print("\nKindly ensure input is correct.")
                    print("____________________________________________________________________________________________")
                    continue
                else:
                    confirmInput = getConfirmInputChoice(1, eventTime)
                    if confirmInput == "N":
                        continue
                    else:
                        eventRecord.append(eventTime)
                        break
            while True:
                eventPrice = int(input("\nEnter Event Price: "))
                print("____________________________________________________________________________________________")
                
                if eventPrice == "" or eventPrice < 0:
                    print("\nKindly ensure input is correct and is greater than 0.")
                    print("____________________________________________________________________________________________")
                    continue
                else:
                    eventPrice = str(eventPrice)
                    eventRecord.append(eventPrice)
                    break
            
            appendListIntoFile(eventRecord, "events.txt") #append list into file
            print("\nEvent added succesfully.")
            print("____________________________________________________________________________________________")
            addStatus = True
        break
           
def modifyAddEvent():
    addStatus = False #false = modification not completed
    continueStatus = False #eventID exist, re-enter another eventID
    while addStatus == False:
        eventRecord = []
        eventID = input("\nEnter new Event ID: ")
        print("____________________________________________________________________________________________")
        eventID = eventID.capitalize()
        
        if eventID == "" or "E" not in eventID:
            print("\nKindly ensure input is correct and starts with 'E'.")
            print("____________________________________________________________________________________________")
            continue
        else:
            fileHandler = open("events.txt", "r") #search if new id exists
            
            for list in fileHandler:
                list = list[:-3].split(", ")
                if eventID != list[0]:
                    continue 
                else:
                    print("\nRecord exists. Kindly insert a new eventID.")
                    print("____________________________________________________________________________________________")
                    fileHandler.close() 
                    continueStatus = True
                    break
            fileHandler.close() 

            if continueStatus == False: #confirm new categoryID
                confirmInput = getConfirmInputChoice(1, eventID)
                if confirmInput == "N":
                    continue
                else:
                    eventRecord.append(eventID)
            else: #eventID exists, so re-enter another ID   
                continue                    
        while True:
            print("\nAvailable Categories:\n") #print all available categories
            
            fileHandler = open("categories.txt", "r")
            for list in fileHandler:
                print(list[0:-3])
            fileHandler.close
            print("____________________________________________________________________________________________")

            categoryID = input("\nEnter new Category ID: ")
            categoryID = categoryID.capitalize()
            print("____________________________________________________________________________________________")
            
            if categoryID == "" or "C" not in categoryID:
                print("\nKindly ensure input is correct and starts with 'C'.")
                print("____________________________________________________________________________________________")
                continue
            else:
                confirmInput = getConfirmInputChoice(1, categoryID)
                if confirmInput == "N":
                    continue
                else:
                    eventRecord.append(categoryID)
                    break
        while True:
            eventName = input("\nEnter new Event Name: ")
            eventName = eventName.title()
            print("____________________________________________________________________________________________")
                
            if eventName == "":
                print("\nKindly ensure input is correct.")
                print("____________________________________________________________________________________________")
                continue
            else:
                confirmInput = getConfirmInputChoice(1, eventName)
                if confirmInput == "N":
                    continue
                else:
                    eventRecord.append(eventName)
                    break
        while True:
            eventType = input("\nEnter Event Type: ")
            eventType = eventType.capitalize()
            print("____________________________________________________________________________________________")
        
            if eventType == "Host" or eventType == "Join":
                eventRecord.append(eventType)
                break
            else:
                print("\nKindly ensure input is correct and is either 'Join or 'Host'.")
                print("____________________________________________________________________________________________")
                continue           
        if eventType == "Host":
            eventRecord.append("set venue")
            eventRecord.append("set date")
            eventRecord.append("set time")
            
            while True:
                eventPrice = int(input("\nEnter Event Price: "))
                print("____________________________________________________________________________________________")
                
                if eventPrice == "" or eventPrice < 0:
                    print("\nKindly ensure input is correct and is greater than 0.")
                    print("____________________________________________________________________________________________")
                    continue
                else:
                    eventPrice = str(eventPrice)
                    eventRecord.append(eventPrice)
                    break
            addStatus = True #break loop
        elif eventType == "Join":
            while True: 
                eventVenue = input("\nEnter Event Venue: ")
                print("____________________________________________________________________________________________")

                if eventVenue == "":
                    print("\nKindly ensure input is correct.")
                    print("____________________________________________________________________________________________")
                    continue
                else:
                    confirmInput = getConfirmInputChoice(1, eventVenue)
                    
                    if confirmInput == "N":
                        continue
                    else:
                        eventRecord.append(eventVenue)
                        break
            while True:
                eventDate = input("\nEnter Event Date: ")
                print("____________________________________________________________________________________________")
                
                if eventDate == "":
                    print("\nKindly ensure input is correct.")
                    print("____________________________________________________________________________________________")
                    continue
                else:
                    confirmInput = getConfirmInputChoice(1, eventDate)
                    if confirmInput == "N":
                        continue
                    else:
                        eventRecord.append(eventDate)
                        break
            while True:
                eventTime = input("\nEnter Event Time: ")
                print("____________________________________________________________________________________________")
                
                if eventTime == "":
                    print("\nKindly ensure input is correct")
                    print("____________________________________________________________________________________________")
                    continue
                else:
                    confirmInput = getConfirmInputChoice(1, eventTime)
                    if confirmInput == "N":
                        continue
                    else:
                        eventRecord.append(eventTime)
                        break
            while True:
                eventPrice = int(input("\nEnter Event Price: "))
                print("____________________________________________________________________________________________")
                
                if eventPrice == "" or eventPrice < 0:
                    print("\nKindly ensure input is correct and is greater than 0.")
                    print("____________________________________________________________________________________________")
                    continue
                else:
                    eventPrice = str(eventPrice)
                    eventRecord.append(eventPrice)
                    break
            addStatus = True
    return eventRecord #return modified event record

def modifyEventMain():
    print("\nAll events:\n") #print all events
    fileHandler = open('events.txt', 'r')
    for line in fileHandler:
        line = line[:-3]
        print(line)
    fileHandler.close()
    print("____________________________________________________________________________________________")
    
    while True:
        eventPath = generalPath("modifyEvent") #retrive eventID to modify
        if eventPath == "" or "E" not in eventPath:
            print("\nKindly ensure input is correct.")
            print("____________________________________________________________________________________________")
            continue
        else:
            confirmInput = getConfirmInputChoice(1, eventPath)
            if confirmInput == "N":
                continue
            else:
                break

    newEvent = modifyAddEvent() #get new event details, returned as a list(eventRecord)
   
    events = []
    fileHandler = open('events.txt', 'r') #store each list in the file into events
    for line in fileHandler:
        line = line[:-3].split(", ")
        events.append(line)
    fileHandler.close()

    for list in events: #search through events for the particular eventID's location
        for item in list:
            if eventPath == item:
                eventLocation = events.index(list)
                break
            else:
                continue
        
    events[eventLocation] = newEvent #replace the old with the new
    
    writeListsIntoFile(events, 'events.txt') #write events list into the file

    print("\nEvent modifed succesfully.")
    print("____________________________________________________________________________________________")
   
#program start
print("__________________________________________________________________________")
print("\nWelcome to Asian Event Management Services")
exit = False

while exit == False:
    unregisteredOption = generalPath("unregistered")

    if unregisteredOption == "1": #view all events
        viewOption = generalPath("view")
        
        if viewOption == "1": #view events by category
            categoryOption = viewEventsByCategory()
            
            if categoryOption == "B":
                continue
            else:
                print("\nThank you for using Asian Event Management Services")
                print("____________________________________________________________________________________________")
                break
        elif viewOption == "2": #view all events
            print("\nAll Events:\n")
            fileHandler = open("events.txt", "r")
            for list in fileHandler:
                print(list[:-3])
            fileHandler.close
            print("____________________________________________________________________________________________")
            
            button = generalPath("button")
            if button == "B":
                continue
            elif button == "E":
                print("\nThank you for using Asian Event Management Services")
                print("____________________________________________________________________________________________")
                break
        else:
            continue
    elif unregisteredOption == "2": #register
        registered = customerRegistrationProcess()
        
        if registered == True:
            continue
    elif unregisteredOption == "3": #log in
        loginDetails = loginProcess() #returns [username, role]/go back
        
        if loginDetails == "go back":
            continue
        elif loginDetails[1] == "Admin":
            exit = admin(loginDetails[0]) #puts username
            
            if exit == True: #exit program
                print("\nThank you for using Asian Event Management Services")
                print("____________________________________________________________________________________________\n")
                break
        elif loginDetails[1] == "Customer":
            exit = customer(loginDetails[0]) #puts username
            
            if exit == True: #exit program
                print("\nThank you for using Asian Event Management Services")
                print("____________________________________________________________________________________________\n")
                break
    else: #exit
        print("\nThank you for using Asian Event Management Services")
        print("____________________________________________________________________________________________\n")
        break