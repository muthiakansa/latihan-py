#definisi fungsi
def print_info( arg1, *vartuple ):
    """Fungsi untuk menampilkan nilai argumen sembarang yang dilewatkan"""
    print ("outputnya adalah: ")
    print (arg1)
    for var in vartuple:
        print (var)

#pemanggilan fungsi
#satu argumen
print_info( 10 )

#empat argumen
print_info( 10, 30, 50, 70)
