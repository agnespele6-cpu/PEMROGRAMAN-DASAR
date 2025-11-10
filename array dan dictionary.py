# Membuat dictionary
siswa = {
    "nama": "Agnes lani",
    "umur": 20,
    "jurusan": "sistem informasi"
}

# Menampilkan isi dictionary
print("Data siswa:", siswa)

# Mengakses nilai menggunakan key
print("Nama:", siswa["nama"])
from array import array

# Membuat array bertipe integer
angka = array('i', [10, 20, 30, 40, 50])

# Menampilkan semua elemen array
print("Isi array:", angka)

# Mengakses elemen array
print("Elemen pertama:", angka[0])
print("Elemen terakhir:", angka[-1])

# Menambah elemen
angka.append(60)
print("Setelah ditambah:", angka)
# Menambah data baru
siswa["nilai"] = 90
print("Setelah ditambah:", siswa)

# Mengubah nilai
siswa["umur"] = 20
print("Setelah diubah:", siswa)

# Menghapus data
del siswa["jurusan"]
print("Setelah dihapus:", siswa)
