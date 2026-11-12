# Name: Dika Giowanda
# NIM: 2511533025
# Question Bonus

sentence = input("Sentence: ")

clean = sentence.lower().replace(" ", "")

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")