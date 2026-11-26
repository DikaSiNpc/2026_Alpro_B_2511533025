n = int(input("Number of deposits: "))
totals = {}

for _ in range(n):
    name, amount = input().split()
    totals[name] = totals.get(name, 0) + int(amount)

for name, total in totals.items():
    print(f"{name}: {total}")

top = max(totals, key=totals.get)
print(f"Total cash: {sum(totals.values())}")
print(f"Top contributor: {top} ({totals[top]})")