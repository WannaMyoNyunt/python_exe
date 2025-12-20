scores = [85, 92, 45, 78, 90, 63, 58, 88]

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "E"
    
    print(f"Score {score}: Grade {grade}")