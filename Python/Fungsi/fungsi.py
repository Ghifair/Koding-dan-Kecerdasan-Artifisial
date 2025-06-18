# fungsi_dasar.py

def sapa_dunia():
    """Fungsi sederhana yang mencetak salam."""
    print("Halo, Dunia!")

def sapa_nama(nama):
    """Fungsi yang menyapa seseorang berdasarkan nama."""
    print(f"Halo, {nama}!")

def tambah_dua_angka(angka1, angka2):
    """Fungsi yang menjumlahkan dua angka dan mengembalikan hasilnya."""
    hasil = angka1 + angka2
    return hasil

# Memanggil fungsi
print("--- Contoh Fungsi Tanpa Parameter ---")
sapa_dunia()

print("\n--- Contoh Fungsi Dengan Parameter ---")
sapa_nama("Alice")
sapa_nama("Bob")

print("\n--- Contoh Fungsi Dengan Return Value ---")
jumlah = tambah_dua_angka(5, 3)
print(f"Hasil penjumlahan 5 dan 3 adalah: {jumlah}")

hasil_lain = tambah_dua_angka(10, 20)
print(f"Hasil penjumlahan 10 dan 20 adalah: {hasil_lain}")

# Fungsi bisa dipanggil langsung dalam print jika mengembalikan nilai
print(f"Hasil penjumlahan 7 dan 8 adalah: {tambah_dua_angka(7, 8)}")