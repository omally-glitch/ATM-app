#Atm program
#assign username and password
username = input("Enter your username \n")
allowedusers = ['Oma', 'Seyi','Ella']
allowedpassword = ['passoma','passseyi','passella']

#identify password through the use of index
if (username in allowedusers):
    password = input("Enter your password \n")
    userId = allowedusers.index(username)

    if (password ==allowedpassword[userId]):
        print("welcome " + username)
        print("these are the available option:") #creation of other options
        print('1 Withdrawal')
        print("2 Cash Deposit")
        print("3. Complaint")

        selectedoption = int(input("Please select an option: "))
        
        if(selectedoption == 1):
            print("You selected %s" % selectedoption)
            
        elif(selectedoption == 2):
            print("You selected %s" % selectedoption)
            
        elif(selectedoption == 3):
            print("You selected %s" % selectedoption)
            
        else:
            print("Invalid option selected please try again")
    
    else:
        print("password Incorrect, please try again")

else:
    print("Name not found, Please try again")


