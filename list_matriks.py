#variabel yang diulang menggunakan list/matriks
list_nim = []
list_nama = []
list_uts = []
list_uas = []
list_total = []

ulang = 2
for i in range(ulang):
    print("Data Ke - " + str(i + 1))
    list_nim.append(input("Masukkan Nim : "))
    list_nim.append(input("Masukkan Nama : "))
    list_uts.append(int(input("Masukkan Nilai UTS : ")))
    list_uas.append(int(input("Masukkan Nilai UAS : ")))

#proses
for i in range(ulang):
    list_total.append((list_uas[i] + list_uts[i]) / 2)

tamu = {
    "nim" : list_nim,
    "nama lengkap" : list_nama,
    "nilai uts" : list_uts,
    "nilai uas" : list_uas,
    "rata rata" : list_total
}
data_tamu = pd.DataFrame(tamu)
#cetak
print("=======================Daftar Nilai====================")
print(data_tamu)
print("=======================================================")
