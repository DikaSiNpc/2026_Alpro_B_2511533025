all_students = input("Class numbers: ").split()
submitted = set(input("Submitted numbers: ").split())
missing = set(all_students) - submitted

print(f"Submitted: {len(submitted)} students")
print(f"Not submitted: {len(missing)} students")

for number in all_students:
    if number in missing:
        print(number)