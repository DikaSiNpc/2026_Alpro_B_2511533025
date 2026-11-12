# Name: Dika Giowanda
# NIM: 2511533025
# Question 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

# ---- Username builder ----
full_name = "  Dika Giowanda  "
nim = "2511533025"

clean = full_name.strip()
space = clean.find(" ")        
if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)