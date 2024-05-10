# Variabel yang berulang menggunakan list/matriks
list_nim = []
list_uts = []
list_uas = []
list_total = []
ulang = 2

# Pengulangan untuk meminta input
for i in range(ulang):
    print("Data Ke - " + str(i + 1))
    list_nim.append(input("Masukkan Nim anda: "))
    list_uts.append(int(input("Masukkan Nilai UTS anda: ")))
    list_uas.append(int(input("Masukkan Nilai UAS anda: ")))

# Proses perhitungan total
for i in range(ulang):
    list_total.append((list_uas[i] + list_uts[i]) / 2)

# Cetak
print("====================================================")
print("Nim\tNilai UTS\tNilai UAS\tTotal")
print("====================================================")

for i in range(ulang):
    print("%s\t%i\t\t%i\t\t%i" % (list_nim[i], list_uts[i], list_uas[i], list_total[i]))

print("====================================================")