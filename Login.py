#LOGIN 

username = "Adam@gmail.com" #Username
password = "Okbro123" #Password

email = input("Enter the email: ")
password1 = input("Enter the password: ")
if email == username:
    if password == password1:
        print("Welcome to brightchamps")
    else:
        print("Wrong password")    
else:
    print("Please enter the right email/username")