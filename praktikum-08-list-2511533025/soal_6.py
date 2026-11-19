LAST_DIGIT = 5  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
for day in range(1, 8):
    expenses.append(int(input(f"Day {day}: ")))

total = 0
for e in expenses:
    total += e
average = total / len(expenses)

highest_day = 1
highest_value = expenses[0]
for i in range(1, len(expenses)):
    if expenses[i] > highest_value:
        highest_value = expenses[i]
        highest_day = i + 1

days_above = 0
for e in expenses:
    if e > daily_limit:
        days_above += 1

print("Daily limit:", daily_limit)
print("Total:", total)
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest_value})")
print("Days above limit:", days_above)