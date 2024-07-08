from datetime import datetime

def KonversiFormatTanggal(tanggal, FormatAwal):
    try:
        TanggalObj = datetime.strptime(tanggal, FormatAwal)
        TanggalTujuan = TanggalObj.strftime("%d %B %Y") 
        return TanggalTujuan
    except ValueError:
        return "Format Invalid Coba Lagi"

TanggalInput = input("Masukkan tanggal (contoh: 06-05-2024): ")
FormatAwal = '%d-%m-%Y'
TanggalHasil = KonversiFormatTanggal(TanggalInput, FormatAwal)

KodeKatalog = input ("Masukan Kode Katalog :")
if KodeKatalog == "a" :
    JenisTenda = "Tenda Kapasitas 2 Orang"
    Harga = 100000
elif KodeKatalog == "b" :
    JenisTenda = "Tenda Kapasitas 3 Orang"
    Harga = 150000
elif KodeKatalog == "c" :
    JenisTenda = "Tenda Kapasitas 5 Orang"
    Harga = 250000
elif KodeKatalog == "d" :
    JenisTenda = "Tenda Kapasitas 8 Orang"
    Harga = 350000
else :
    print ("Out Of Stock")

LamaPemesanan = input("Masukan Lama Pemesanan :")
DendaKeterlambatan = input("Lama Keterlambatan :")
if DendaKeterlambatan == "0" :
    HargaDenda = 0
else :
    HargaDenda = ((int(Harga)*0.15)+ int(Harga))*int(DendaKeterlambatan)
TotalHarga = (int(LamaPemesanan) * int(Harga))+ int(HargaDenda)

print(f"Tanggal Pemesanan: {TanggalHasil}")
print(f"Harga Barang: Rp {Harga:,.2f}")
print(f"lama Pemesanan: {LamaPemesanan} Hari")
print(f"Lama Keterlambatan: {DendaKeterlambatan} Hari")
print(f"Denda Keterlambatan: Rp {HargaDenda:,.2f}")
print(f"Total Harga: Rp {TotalHarga:,.2f}")

CustBayar = int(input("Masukan Nominal:"))
Kembalian = (int(CustBayar)-int(TotalHarga))

print("="*40)
print(""*30)
print(TanggalHasil)
print(""*30)
print(f"Kode Barang         : {KodeKatalog}")
print(f"Jenis Tenda         : {JenisTenda}")
print(f"Harga Barang        : Rp {Harga:,.2f}")
print(f"lama Pemesanan      : {LamaPemesanan} Hari")
print(f"Lama Keterlambatan  : {DendaKeterlambatan} Hari")
print(f"Denda Keterlambatan : Rp {HargaDenda:,.2f}")
print(f"Total Harga         : Rp {TotalHarga:,.2f}")
print(f"Bayar               : Rp {CustBayar:,.2f}")
print(f"Kembalian           : Rp {Kembalian:,.2f}")
print(""*30)
print("="*40)