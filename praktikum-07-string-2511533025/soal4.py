# Name: Dika Giowanda
# NIM: 2511533025
# Question 4

phone = "082511533025"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)