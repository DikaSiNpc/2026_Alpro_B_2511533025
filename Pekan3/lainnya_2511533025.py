# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("========================================")
print("1. OPERATOR KEANGGOTAAN")
print("========================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3025 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3025 = [int(angka.strip()) for angka in input_data_3025.split(",")]

nilai_dicari = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_3025 = nilai_dicari in data_3025
print("\nOperator keanggotaan IN")
print(nilai_dicari, "in", data_3025, "=", hasil_3025)

# Operator not in
hasil_3025 = nilai_dicari not in data_3025
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari, "not in", data_3025, "=", hasil_3025)


print("\n========================================")
print("2. OPERATOR IDENTITAS")
print("========================================")

# objek1 menggunakan list dari input pengguna
objek1_3025 = data_3025

# objek2 merujuk pada objek yang sama dengan objek1
objek2_3025 = objek1_3025

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3025 = data_3025.copy()

print("objek1 =", objek1_3025)
print("objek2 =", objek2_3025)
print("objek3 =", objek3_3025)

# Operator is
hasil_3025 = objek1_3025 is objek2_3025
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_3025)

# Operator is not
hasil_3025 = objek1_3025 is not objek3_3025
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_3025)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_3025 is objek3_3025)
print("objek1 == objek3 =", objek1_3025 == objek3_3025)