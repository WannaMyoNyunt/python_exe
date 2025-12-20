import random
import datetime

def lucky_day_picker():
    print("Lucky Day Picker🦅")
    print("=" *30)

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    to_do = {    
        "Monday" : "Goon to Ma Myint",
        "Tuesday" : "Goon to Andrew",
        "Wednesday" : "Goon to KaungKaung",
        "Thursday" : "Goon to Ricky",
        "Friday" : "Goon to Chris",
        "Saturday" : "Goon to Ethan",
        "Sunday" : "Goon to Rocky"
    }
    

    lucky_day = random.choice(days)

    print(f"Your lucky day is {lucky_day}")
    
    
    today = datetime.datetime.now().strftime("%A")
    print(f"Today is {today}")
    print(f"Suggested Activity: {to_do[lucky_day]}")
    
    if (today == lucky_day):
        print("Wow! Today is your lucky day you should do the activity to make your day more lucky")
    
    else:
        print("Today is not your lucky day but do the activity to make your day lucky")
     
    

while True:
    user_input = input("\nPress 1 to pick a lucky day or 0 to exit")
    if user_input == "1":
        lucky_day_picker()
    elif user_input == "0":
        print ("Bye Bye")
        break
    else:
        print("Invalid input, please try again.")
    