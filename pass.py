
username = input()
user_password = input()
while user_password != "wannachoupro":
    if(username == "admin" and user_password == "wannachoupro"):
        print("Welcome Chou Pro")
    else:
        print("invalid username or password")
        print("Access Denied")