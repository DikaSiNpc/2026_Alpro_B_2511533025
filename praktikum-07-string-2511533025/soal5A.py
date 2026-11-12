# Name: Dika Giowanda
# NIM: 2511533025
# Question 5

username = input("Username: ")

# Check the rules in a safe order and print the first rule that fails.
# Messages:

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")