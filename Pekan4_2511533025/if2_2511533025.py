# Buat file dengan nama if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

ipk_3025 = float(input("Input IPK Anda = "))

if ipk_3025 > 2.75:
    print("Anda Lulus Sangat Memuaskan dengan IPK " + str(ipk_3025))
else:
    print("Anda tidak lulus")

print("Program Selesai")