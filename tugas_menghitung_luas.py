print('by : muthia kansa')
print('program menghitung luas & keliling bangun datar')
print('-----------------------------------------------')
print('[1] luas dan keliling persegi')
print('[2] luas dan keliling segitiga')
print('[3] luas dan keliling lingkaran')
print('----------------------------------------------1-')
pilihan = int(input('pilih salah satu program (1-3): '))

if pilihan == 1:
    print('/nprogram menghitung luas persegi')

    s = int(input('masukkan nilai sisi : '))

    luas = s**2
    keliling = 4*s
    print('/nluas persegi =', str(luas))

elif pilihan == 2:
    print('/nprogram menghitung luas & keliling segitiga')
    print('---------------------------------------------')

    a = float(input('masukan nilai alas   :'))
    t = float(input('masukan nilai tinggi :'))

    luas = 0.5*a*t
    keliling = a+a+a
    print('/nluas segitiga =', str(luas))
    print('keliling segitiga =', str(keliling))

elif pilihan == 3:
    print('/nprogram menghitung luas & keliling lingkaran')
    print('----------------------------------------------')

    r = float(input('masukkan jari - jari :'))

    phi = 3.14
    diameter = 2*r

    luas = phi*r*r
    keliling = phi*diameter
    print('/nluas lingkaran =', str(luas))
    print('keliling lingkaran =', str(keliling))
