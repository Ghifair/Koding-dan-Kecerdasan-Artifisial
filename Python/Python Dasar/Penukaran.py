# Modul penukaran sampah
harga = {"plastik": 500, "kertas": 300, "kaca": 700}

def hitung(jenis, berat):
	return harga.get(jenis, 0) * berat