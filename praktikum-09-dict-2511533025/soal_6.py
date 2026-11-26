schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# 6a
busiest = ""
most = 0
for day, courses in schedule.items():
    if len(courses) > most:
        busiest = day
        most = len(courses)
print("Busiest day: " + busiest + " (" + str(most) + " courses)")

# 6b
course = input("Course name: ")
count = 0
for day, courses in schedule.items():
    if course in courses:
        count = count + 1
print(course + ": " + str(count) + " days")