# =========================================================
# SISTEM LOKET TERPADU & AUDIT TRANSAKSI EKSPEDISI WAHANA
# Studi Kasus: Alpro Adventure Park
# Materi: Struktur Percabangan (Pekan 4)
# =========================================================

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# ---------------------------------------------------------
# 1. Input Data Pengunjung & String Handling
# ---------------------------------------------------------
nama_3025 = input("Masukkan Nama Pengunjung\t   : ")
umur_3025 = int(input("Input umur anda\t\t\t   : "))
sim_3025 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].strip().lower()

# ---------------------------------------------------------
# 2. Pemilihan Wahana menggunakan match-case (1-5 & default _)
# ---------------------------------------------------------
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba       (Rp 50,000)")
print("  2. Arung Jeram        (Rp 75,000)")
print("  3. Motor ATV Ekstrim  (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP     (Rp 220,000)")

pilihan_paket_3025 = int(input("Masukkan nomor paket anda (1-5)\t: "))

match pilihan_paket_3025:
    case 1:
        nama_paket_3025 = "Wahana Safari Rimba"
        harga_satuan_3025 = 50000
    case 2:
        nama_paket_3025 = "Wahana Arung Jeram"
        harga_satuan_3025 = 75000
    case 3:
        nama_paket_3025 = "Wahana Motor ATV Ekstrim"
        harga_satuan_3025 = 120000
    case 4:
        nama_paket_3025 = "Wahana Roller Coaster Kilat"
        harga_satuan_3025 = 100000
    case 5:
        nama_paket_3025 = "Wahana All-Access VIP"
        harga_satuan_3025 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

# ---------------------------------------------------------
# 1b. Input Jumlah Tiket + validasi if tunggal
# ---------------------------------------------------------
jumlah_tiket_3025 = int(input("Masukkan jumlah tiket anda\t: "))

if jumlah_tiket_3025 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")

# ---------------------------------------------------------
# 3. Validasi Izin Kendali Wahana (if-elif-else + operator logika)
#    Tidak menggunakan nested-if: syarat paket 3 digabung
#    langsung ke setiap cabang kondisi menggunakan 'and'
# ---------------------------------------------------------
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if pilihan_paket_3025 == 3 and umur_3025 >= 17 and sim_3025 == 'y':
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif pilihan_paket_3025 == 3 and umur_3025 >= 17 and sim_3025 != 'y':
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV "
          "(wajib didampingi instruktur).")
elif pilihan_paket_3025 == 3 and umur_3025 < 17 and sim_3025 == 'y':
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
elif pilihan_paket_3025 == 3:
    print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
elif umur_3025 >= 10:
    print(f"Status Akses: Anda cukup umur untuk menaiki {nama_paket_3025}.")
else:
    print(f"Status Akses: Anda belum cukup umur untuk menaiki {nama_paket_3025}.")

# ---------------------------------------------------------
# Input tambahan: status member & kode promo
# ---------------------------------------------------------
is_member_3025 = input("Apakah anda memiliki member? (y/t) : ").strip().lower()
kode_promo_valid_3025 = input("Apakah kode promo anda valid? (y/t): ").strip().lower()

# ---------------------------------------------------------
# 4. Akumulasi Diskon Bertingkat (Multi-IF terpisah)
# ---------------------------------------------------------
subtotal_3025 = harga_satuan_3025 * jumlah_tiket_3025
total_diskon_persen_3025 = 0

if subtotal_3025 >= 200000:
    total_diskon_persen_3025 += 10          # Diskon Belanja Besar

if is_member_3025 in ['y', 'ya']:
    total_diskon_persen_3025 += 5           # Diskon Member

if kode_promo_valid_3025 in ['y', 'ya']:
    total_diskon_persen_3025 += 15          # Diskon Voucher Promo

if jumlah_tiket_3025 >= 5:
    total_diskon_persen_3025 += 5           # Diskon Tambahan Rombongan

# ---------------------------------------------------------
# 5. Evaluasi Kelulusan Audit (if-else) + Rincian Pembayaran
# ---------------------------------------------------------
nominal_diskon_3025 = subtotal_3025 * (total_diskon_persen_3025 / 100)
total_bayar_3025 = subtotal_3025 - nominal_diskon_3025

print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_3025:,.0f}")
print(f"Total Diskon\t : {total_diskon_persen_3025}% (Rp {nominal_diskon_3025:,.0f})")
print(f"Total Bayar\t : Rp {total_bayar_3025:,.0f}")

if total_bayar_3025 > 300000:
    print("Catatan Layanan  : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else:
    print("Catatan Layanan  : Terima kasih telah berkunjung.")

print("Program Selesai")