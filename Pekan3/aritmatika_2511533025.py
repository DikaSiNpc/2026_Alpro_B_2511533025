# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam python
# Nama variable ditambah 4 digit nim terakhir contoh: nama_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukan akan dikonvesi menjadi data tipe integer

angka1_3025 = int(input("Input angka-1: "))
angka2_3025 = int(input("Input angka-2: "))

# Penjumlahan
hasil_3025 = angka1_3025 + angka2_3025
print("\nOperator Penjumlahan")
print("Hasil =", hasil_3025)

# Pengurangan
hasil_3025 = angka1_3025 - angka2_3025
print("\nOperator Pengurangan")
print("Hasil =", hasil_3025)

# Perkalian
hasil_3025 = angka1_3025 * angka2_3025
print("\nOperator Perkalian")
print("Hasil =", hasil_3025)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_3025 != 0:
    hasil_3025 = angka1_3025 / angka2_3025
    print("\nOperator Pembagian")
    print("Hasil =", hasil_3025)

    hasil_3025 = angka1_3025 // angka2_3025
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_3025)

    hasil_3025 = angka1_3025 % angka2_3025
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_3025)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_3025 = angka1_3025 ** angka2_3025
print("\nOperator Pangkat")
print("Hasil =", hasil_3025)