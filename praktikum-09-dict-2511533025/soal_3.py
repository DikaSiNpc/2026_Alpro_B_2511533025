rooms = {"IF101": "Lab 1", "IF102": "R. 204", "IF103": "R. 301"}

for code in input("Course codes: ").split():
    print(code, "->", rooms.get(code, "not found"))