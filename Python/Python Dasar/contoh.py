import biner
import oktal
import heksa

# Program utama
if __name__ == "__main__":
	angka = int(input("Input desimal: "))
	print(f"Biner: {biner.tobinary(angka)}")
	print(f"Oktal: {oktal.tooctal(angka)}")
	print(f"Heksa: {heksa.tohexa(angka)}")