# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_3025 = int(input("Input angka-1: "))
angka2_3025 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_3025 = angka1_3025 > angka2_3025
print("\nOperator lebih besar dari")
print("angka1_3025 > angka2_3025 =", hasil_3025)

# Lebih kecil dari
hasil_3025 = angka1_3025 < angka2_3025
print("\nOperator lebih kecil dari")
print("angka1_3025 < angka2_3025 =", hasil_3025)

# Lebih besar dari atau sama dengan
hasil = angka1_3025 >= angka2_3025
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_3025 >= angka2_3025 =", hasil_3025)

# Lebih kecil dari atau sama dengan
hasil = angka1_3025 <= angka2_3025
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1_3025 <= angka2_3025 =", hasil_3025)

# Sama dengan
hasil = angka1_3025 == angka2_3025
print("\nOperator sama dengan")
print("angka1_3025 == angka2_3025 =", hasil_3025)

# Tidak sama dengan
hasil = angka1_3025 != angka2_3025
print("\nOperator tidak sama dengan")
print("angka1_3025 != angka2_3025 =", hasil_3025)

# Tambahan: perbandingan berantai dalam Python
hasil = 0 < angka1_3025 < 100
print("\nPerbandingan berantai")
print("0 < angka1_3025 < 100 =", hasil_3025)

hasil = 0 < angka2_3025 < 100
print("0 < angka2_3025 < 100 =", hasil_3025)