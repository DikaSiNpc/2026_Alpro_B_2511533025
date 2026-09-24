# Buat file dengan nama multi_if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: total_belanja_1234
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_3025 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3025 = input("Apakah Anda memiliki member? (y/t): ").strip().lower()
is_member_3025 = input_member_3025 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3025 = input("Apakah kode promo anda valid? (y/t): ").strip().lower()
kode_promo_valid_3025 = input_promo_3025 in ["y", "ya"]

total_diskon_persen_3025 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_3025 > 1000000:
    total_diskon_persen_3025 += 10  # Diskon belanja besar

if is_member_3025:
    total_diskon_persen_3025 += 5   # Diskon member
if kode_promo_valid_3025:
    total_diskon_persen_3025 += 15  # Diskon voucher

# Menhitung nominal diskon dan total bayar
nominal_diskon_3025 = total_belanja_3025 * (total_diskon_persen_3025 / 100)
total_bayar_3025 = total_belanja_3025 - nominal_diskon_3025

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen_3025}% (Rp {nominal_diskon_3025:,.0f})")
print(f"Total Bayar   : Rp {total_bayar_3025:,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_3025}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid