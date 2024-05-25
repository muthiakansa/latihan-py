#argumen kata kunci (keywoard argument)
#definisi fugsi
def print_info( nama , usia ):
    """fungsi ini menampilkan info yang dimasukkan"""
    print ("Nama: ", nama)
    print ("Usia: ", usia)

#memanggil fungsi
#output
#Name: budi
#Usia: 25
print_info(usia = 25, nama = "budi" )


#ardumen dafault
#definisi fungsi
def print_info( nama, usia= 17 ):
    """Fungsi ini menampilkan info yang dimasukan"""
    print("Nama: ",nama)
    print("Usia", usia)

#membangun fungsi print_info
print_info( usia = 29, nama = "galih" )
#pemanggilan fungsi tidak menyediakan argumen usia
print_info(nama = "galih")
