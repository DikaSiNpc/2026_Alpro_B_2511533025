# ============================================================
# SISTEM SIMULASI TRANSAKSI DAN VALIDASI AKSES TOKO
# ============================================================

print("=== SISTEM TRANSAKSI TOKO ===")

# ============================================================
# INPUT DATA PELANGGAN
# ============================================================

nama_3025 = input("\nMasukkan Nama Pelanggan : ")
status_3025 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_3025 = int(input("Masukkan Total Belanja : "))
jumlah_barang_3025 = int(input("Masukkan Jumlah Barang : "))
kode_promo_3025 = input("Masukkan Kode Promo : ").upper()

# ============================================================
# OPERATOR PERBANDINGAN
# ============================================================

belanja_minimal_3025 = total_belanja_3025 >= 200000
jumlah_minimal_3025 = jumlah_barang_3025 >= 3
status_member_3025 = status_3025 == "member"

# ============================================================
# OPERATOR KEANGGOTAAN (MEMBERSHIP)
# ============================================================

daftar_promo_3025 = [
    "HEMAT10",
    "HEMAT20",
    "GRATISONGKIR"
]

promo_tersedia_3025 = kode_promo_3025 in daftar_promo_3025
promo_tidak_tersedia_3025 = kode_promo_3025 not in daftar_promo_3025

# ============================================================
# OPERATOR LOGIKA
# ============================================================

# AND: member DAN belanja minimal Rp200.000
mendapat_diskon_3025 = status_member_3025 and belanja_minimal_3025

# AND: member DAN jumlah barang minimal DAN promo tersedia
mendapat_promo_3025 = (
    status_member_3025
    and jumlah_minimal_3025
    and promo_tersedia_3025
)

# OR: salah satu kondisi terpenuhi
akses_pelanggan_3025 = (
    status_member_3025 or promo_tersedia_3025
)

# NOT: membalik nilai kondisi
bukan_member_3025 = not status_member_3025

# ============================================================
# OPERATOR ARITMATIKA
# ============================================================

diskon_3025 = 0
if mendapat_diskon_3025:
    diskon_3025 = total_belanja_3025 * 10 / 100

# Operator -=
total_pembayaran_3025 = total_belanja_3025
total_pembayaran_3025 -= diskon_3025

# Operator /
rata_rata_harga_3025 = total_belanja_3025 / jumlah_barang_3025

# Operator %
sisa_pembagian_3025 = total_belanja_3025 % jumlah_barang_3025

# ============================================================
# OPERATOR PENUGASAN
# ============================================================

poin_3025 = 0
poin_3025 += jumlah_barang_3025

# Contoh operator *=
nilai_poin_3025 = poin_3025
nilai_poin_3025 *= 2

# ============================================================
# OPERATOR IDENTITAS
# ============================================================

# Membuat dua objek berbeda tetapi memiliki isi yang sama
objek_a_3025 = ["member"]
objek_b_3025 = ["member"]

# == membandingkan isi/nilai
nilai_sama_3025 = objek_a_3025 == objek_b_3025

# is membandingkan identitas objek
identitas_sama_3025 = objek_a_3025 is objek_b_3025

# is not untuk memeriksa bahwa objek berbeda
identitas_berbeda_3025 = objek_a_3025 is not objek_b_3025

# ============================================================
# OPERATOR BITWISE
# ============================================================

# Nilai bit berdasarkan kondisi:
# 0001 = Member
# 0010 = Belanja >= Rp200.000
# 0100 = Jumlah barang >= 3
# 1000 = Kode promo tersedia

bit_member_3025 = 1 if status_member_3025 else 0
bit_belanja_3025 = 2 if belanja_minimal_3025 else 0
bit_jumlah_3025 = 4 if jumlah_minimal_3025 else 0
bit_promo_3025 = 8 if promo_tersedia_3025 else 0

# Operator OR (|)
kode_status_3025 = (
    bit_member_3025
    | bit_belanja_3025
    | bit_jumlah_3025
    | bit_promo_3025
)

# Kode biner
kode_biner_3025 = format(kode_status_3025, "04b")

# Kode pembanding
kode_cek_3025 = 15
kode_referensi_3025 = 11

# Operator AND (&)
cek_member_3025 = kode_status_3025 & 1
cek_promo_3025 = kode_status_3025 & 8

# Operator XOR (^)
hasil_xor_3025 = kode_status_3025 ^ kode_referensi_3025

# Operator SHIFT (<<)
hasil_shift_3025 = kode_status_3025 << 1

# ============================================================
# HASIL PROGRAM
# ============================================================

print("\n=== DATA TRANSAKSI ===")

print("Nama Pelanggan       :", nama_3025)
print("Status Pelanggan    :", status_3025)
print("Total Belanja       : Rp", int(total_belanja_3025))
print("Jumlah Barang       :", jumlah_barang_3025)
print("Kode Promo          :", kode_promo_3025)

print("\n=== HASIL VALIDASI ===")

print("Belanja >= Rp200000 :", belanja_minimal_3025)
print("Jumlah Barang >= 3  :", jumlah_minimal_3025)
print("Status Member       :", status_member_3025)
print("Kode Promo Tersedia :", promo_tersedia_3025)
print("Mendapatkan Diskon  :", mendapat_diskon_3025)
print("Mendapatkan Promo   :", mendapat_promo_3025)

print("\n=== HASIL PERHITUNGAN ===")

print("Diskon              : Rp", int(diskon_3025))
print("Total Pembayaran    : Rp", int(total_pembayaran_3025))
print("Rata-rata Harga     : Rp", int(rata_rata_harga_3025))
print("Sisa Pembagian      :", sisa_pembagian_3025)

print("\n=== HAK AKSES PELANGGAN ===")

print("Member Access       :", status_member_3025)
print("Promo Access        :", promo_tersedia_3025)
print("Free Shipping Access:", mendapat_promo_3025)

print("\n=== HASIL OPERATOR ===")

# Operator aritmatika
print("\n--- Operator Aritmatika ---")
print("Total Belanja       :", total_belanja_3025)
print("Diskon 10%          :", diskon_3025)
print("Total Setelah Diskon:", total_pembayaran_3025)
print("Rata-rata Barang    :", rata_rata_harga_3025)
print("Sisa Pembagian (%)  :", sisa_pembagian_3025)

# Operator perbandingan
print("\n--- Operator Perbandingan ---")
print("Belanja >= 200000   :", belanja_minimal_3025)
print("Jumlah >= 3         :", jumlah_minimal_3025)
print("Status == member    :", status_member_3025)

# Operator logika
print("\n--- Operator Logika ---")
print("Member AND Belanja  :", status_member_3025 and belanja_minimal_3025)
print("Member AND Promo    :", status_member_3025 and promo_tersedia_3025)
print("Member OR Promo     :", status_member_3025 or promo_tersedia_3025)
print("NOT Member          :", not status_member_3025)

# Operator penugasan
print("\n--- Operator Penugasan ---")
print("Poin awal           :", jumlah_barang_3025)
print("Poin setelah +=     :", poin_3025)
print("Nilai poin setelah *=:", nilai_poin_3025)

# Operator membership
print("\n--- Operator Keanggotaan ---")
print("Kode promo IN daftar:", kode_promo_3025 in daftar_promo_3025)
print("Kode promo NOT IN   :", kode_promo_3025 not in daftar_promo_3025)

# Operator identity
print("\n--- Operator Identitas ---")
print("Isi objek sama (==) :", nilai_sama_3025)
print("Identitas sama (is) :", identitas_sama_3025)
print("Identitas berbeda   :", identitas_berbeda_3025)

# Operator bitwise
print("\n=== OPERASI BITWISE ===")

print("\n--- Kode Status Transaksi ---")
print("0001 = Member")
print("0010 = Belanja >= Rp200000")
print("0100 = Jumlah Barang >= 3")
print("1000 = Kode Promo Tersedia")

print("\nKode Status :", kode_biner_3025)
print("Kode Desimal:", kode_status_3025)

print("\n--- Pemeriksaan Status ---")

print("\nCek Member")
print(format(kode_status_3025, "04b"), "& 0001")
print("Hasil Biner :", format(cek_member_3025, "04b"))
print("Hasil Desimal:", cek_member_3025)

print("\nCek Promo")
print(format(kode_status_3025, "04b"), "& 1000")
print("Hasil Biner :", format(cek_promo_3025, "04b"))
print("Hasil Desimal:", cek_promo_3025)

print("\n--- OR ---")
print(
    format(bit_member_3025, "04b"),
    "|",
    format(bit_belanja_3025, "04b"),
    "=",
    format(bit_member_3025 | bit_belanja_3025, "04b")
)

print("\n--- XOR ---")
print("Kode Transaksi :", format(kode_status_3025, "04b"))
print("Kode Referensi :", format(kode_referensi_3025, "04b"))
print(
    format(kode_status_3025, "04b"),
    "^",
    format(kode_referensi_3025, "04b")
)
print("Hasil Biner    :", format(hasil_xor_3025, "04b"))
print("Hasil Desimal  :", hasil_xor_3025)

print("\n--- SHIFT ---")
print(format(kode_status_3025, "04b"), "<< 1")
print("Hasil Biner   :", format(hasil_shift_3025, "05b"))
print("Hasil Desimal :", hasil_shift_3025)

print("\n=== SELESAI ===")