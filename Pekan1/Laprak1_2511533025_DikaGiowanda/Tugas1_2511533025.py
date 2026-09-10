# Program Tugas1_2511533025.py
"""
Praktikum Algoritma dan Pemrograman
Hitung Nilai Akhir Mahasiswa
"""
# Deklarasi data dan variabel
nama_mahasiswa_3025 = "Dika Giowanda"
nim_3025 = "2511533025"
nilai_tugas_3025 = 100
nilai_uts_3025 = 95
nilai_uas_3025 = 100

# Proses perhitungan nilai akhir secara otomatis
# (Tugas 20%, UTS 30%, UAS 50%)
nilai_akhir_3025 = (nilai_tugas_3025 * 0.2) + (nilai_uts_3025 * 0.3) + (nilai_uas_3025 * 0.5)

# Tampilan Output
print("====== KARTU HASIL STUDI ======")
print("Nama Mahasiswa\t:", nama_mahasiswa_3025)
print("NIM\t\t:", nim_3025)
print("-------------------------------")
print("Nilai Tugas\t:", nilai_tugas_3025)
print("Nilai UTS\t:", nilai_uts_3025)
print("Nilai UAS\t:", nilai_uas_3025)
print("-------------------------------")
print("Nilai Akhir\t:", nilai_akhir_3025)
print("===============================")
print("Laporan ini" + " dibuat oleh\n" 
      + "Asisten Laboratorium Alpro.")