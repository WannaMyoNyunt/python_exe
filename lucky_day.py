import random
import datetime

def lucky_day_picker():
    print("Lucky Day Picker🦅")
    print("=" *30)

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    to_do = {
        "Monday" , "Goon to Ma Myint"
        "Tuesday" , "Goon to Andrew"
        "Wednesday" , "Goon to KaungKaung"
        "Thursday" , "Goon to Ricky"
        "Friday" , "Goon to Chris"
        "Saturday" , "Goon to Ethan"
        "Sunday" , "Goon to Rocky"
    }


    lucky_day = random.choice(days)

    print(f"Your lucky day is {lucky_day}")
    print(f"Suggested activity is {to_do{lucky_day}}")
    
    today = datetime.datetime.now().strftime("%A")
    print(f"Today is {today}")
    
    if (today == lucky_day):
        print("Wow! Today is your lucky day")
    
    else:
        print("Today is not ur lucky day ahahahahah")
     
    
lucky_day_picker()