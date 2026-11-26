all_students = input("Class numbers: ").split()
submitted = set(input("Submitted numbers: ").split())

print("Submitted:", len(submitted), "students")

not_submitted = set(all_students) - submitted
print("Not submitted:", len(not_submitted), "students")

for number in all_students:
    if number not in submitted:
        print(number)