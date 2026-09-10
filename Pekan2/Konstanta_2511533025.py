# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstantas untuk menghitung luas lingkaran
# Nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_3025 = float(input('Masukan nilai jari-jari: '))
luas_3025 = PI * jari_3025 * jari_3025
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3025, luas_3025))