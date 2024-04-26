# Membuat dictionary untuk menyimpan data biaya kuliah
biaya_kuliah = {
    'SI': {'Nama Prodi': 'Sistem Informasi', 'Harga': 2400000},
    'SIA': {'Nama Prodi': 'Sistem Informasi Akuntansi', 'Harga': 2000000}
}

# Fungsi untuk melakukan pendaftaran mahasiswa baru
def pendaftaran_mahasiswa():
    print("Selamat datang di sistem pendaftaran mahasiswa baru!")
    nis = input("Masukkan NIS calon mahasiswa: ")
    nama = input("Masukkan nama calon mahasiswa: ")
    print("Daftar jurusan:")
    for kode, prodi in biaya_kuliah.items():
        print(f"{kode}: {prodi['Nama Prodi']} - Biaya: Rp{prodi['Harga']}")
    jurusan = input("Masukkan kode jurusan yang dipilih: ")
    if jurusan in biaya_kuliah:
        print("Pendaftaran berhasil!")
        print("Data Mahasiswa:")
        print(f"NIS: {nis}")
        print(f"Nama: {nama}")
        print(f"Jurusan: {biaya_kuliah[jurusan]['Nama Prodi']}")
        print(f"Biaya Kuliah: Rp{biaya_kuliah[jurusan]['Harga']}")
    else:
        print("Jurusan tidak valid.")

# Memanggil fungsi pendaftaran_mahasiswa
pendaftaran_mahasiswa()
