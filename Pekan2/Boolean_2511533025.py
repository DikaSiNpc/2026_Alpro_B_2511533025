# Buat file dengan nama Boolean_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus_3025 = True
is_cumlaude_3025 = True

# Menggunakan Boolean
nilai_3025 = 85
batas_lulus_3025 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_3025 = nilai_3025 >= batas_lulus_3025 # Hasilnya akan true

print("=== Check Kelulusan ===")
print("Nilai:", nilai_3025)
print("Apakah Lulus?:", status_kelulusan_3025)
if is_lulus_3025 and is_cumlaude_3025:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")