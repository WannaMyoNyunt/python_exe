import random
import datetime

num = random.randint(0,5)

print(f"Your number is {num}")

students = ["May Thae", "Yamone", "Min Khant","Wanna","Thar Lin Htet"]

ran_std = random.choice(students)

print(f"Your name is {ran_std}")

today = datetime.datetime.now().strftime("%A")

print(f"Today is {today}")