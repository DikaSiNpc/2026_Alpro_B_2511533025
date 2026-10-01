# Buat file dengan nama jumlah_genap_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_3025 = int(input("Masukan nilai batas: "))

jumlah_3025 = 0
for i_3025 in range(1, ulang_3025 + 1):
    if i_3025 % 2 == 0:
        print(i_3025, end=" ")
        jumlah_3025 = jumlah_3025 + i_3025
        if i_3025 < ulang_3025:
            print(" + ", end="")
        else:
            print(" = ", jumlah_3025, end="")
print()
print("Jumlah =", jumlah_3025)