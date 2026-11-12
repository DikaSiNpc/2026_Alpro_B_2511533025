# Name: Dika Giowanda
# NIM: 2511533025
# Question 5B

nim = input("NIM: ")

if len(nim) == 10 and nim.isdigit():
    print("Valid, intake year 20" + nim[:2])
else:
    print("Invalid NIM")