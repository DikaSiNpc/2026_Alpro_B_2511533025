# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_3025 = int(input("Input angka-1: "))
angka2_3025 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_3025)
print("Nilai angka2 =", angka2_3025)
# Assignment biasa
hasil_3025 = angka1_3025
print("\nAssignment biasa (=)")
print("Hasil =", hasil_3025)
# Assignment penambahan
hasil_3025 = angka1_3025
hasil_3025 += angka2_3025
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_3025)

# Assignment pengurangan
hasil_3025 = angka1_3025
hasil_3025 -= angka2_3025
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_3025)

# Assignment perkalian
hasil_3025 = angka1_3025
hasil_3025 *= angka2_3025
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_3025)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3025 != 0:
    hasil_3025 = angka1_3025
    hasil_3025 /= angka2_3025
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_3025)
    # Operator tambahan
    hasil_3025 = angka1_3025
    hasil_3025 //= angka2_3025
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_3025)
    hasil_3025 = angka1_3025
    hasil_3025 %= angka2_3025
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_3025)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_3025 = angka1_3025
hasil_3025 **= angka2_3025
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_3025)