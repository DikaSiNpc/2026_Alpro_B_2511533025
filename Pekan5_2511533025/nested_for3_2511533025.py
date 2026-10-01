# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_3025 = int(input("Masukan nilai batas: "))
for i_3025 in range(batas_3025+1):
    for j_3025 in range(batas_3025+1):
        print(i_3025+j_3025, end=" ")
    print() # pindah ke baris berikutnya