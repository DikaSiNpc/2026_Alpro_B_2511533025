# Name: Dika Giowanda
# NIM: 2511533025
# Question 7

name = "dika giowanda"
nim = "2511533025"

clean = name.strip()
space = clean.find(" ")
if space == -1:
    first = clean
else:
    first = clean[:space]
username = first.lower() + nim[-3:]

intake = "20" + nim[:2]

print("=" * 30)
print(f"{'STUDENT CARD':^30}")
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)