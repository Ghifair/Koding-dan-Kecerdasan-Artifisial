# Program utama
import Penukaran

if __name__ == "__main__":
	jenis = input("jenis sampah: ").lower()
	berat = float(input("berat (kg): "))
	saldo = Penukaran.hitung(jenis, berat)
	print(f"Saldo yang diperoleh: Rp {saldo}")