from typing import Final

# ==========================================
# SISTEM REGISTRASI PRAKTIKAN ALPRO 2026
# ==========================================

# Konstanta batas kelulusan
BATAS_LULUS_3025: Final[float] = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

# ==========================================
# INPUT DATA PRAKTIKAN
# ==========================================

nama_3025 = input("Masukkan Nama Mahasiswa     : ")
jenis_kelamin_3025 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3025 = int(input("Masukkan Umur               : "))
nilai_3025 = float(input("Masukkan Skor Tes Awal      : "))

# Alamat menggunakan string multiline
alamat_3025 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""

# Token identifikasi menggunakan tipe Complex
id_token_sinyal_3025 = 100 + 3j

# ==========================================
# PROSES VALIDASI KELULUSAN
# ==========================================

lulus_3025 = nilai_3025 >= BATAS_LULUS_3025

# ==========================================
# MENAMPILKAN DATA DAN TIPE DATA
# ==========================================

print()
print("=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

print("Nama Mahasiswa :", nama_3025,
      "| Tipe:", type(nama_3025))

print("Jenis Kelamin  :", jenis_kelamin_3025,
      "| Tipe:", type(jenis_kelamin_3025))
print("Alamat Domisili:")
print(alamat_3025,
      "| Tipe:", type(alamat_3025))

print("Umur           :", umur_3025, "tahun",
      "| Tipe:", type(umur_3025))

print("Skor Tes Awal  :", nilai_3025,
      "| Tipe:", type(nilai_3025))
print("ID Token Sinyal:", id_token_sinyal_3025,
      "| Tipe:", type(id_token_sinyal_3025))

# ==========================================
# MENAMPILKAN STATUS KELULUSAN
# ==========================================

print()
print("=== STATUS KELULUSAN PRAKTIKUM ===")

print("Batas Minimum Nilai:", BATAS_LULUS_3025)

print("Apakah Dinyatakan Lulus?:",
      lulus_3025,
      "| Tipe:", type(lulus_3025))