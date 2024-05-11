# Buat list 2 dimensi
list_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Tampilkan nilai yang diminta
print("Baris Pertama, Kolom Pertama:", list_2d[0][0])
print("Baris Pertama, Kolom Kedua:", list_2d[0][1])
print("Baris Pertama, Kolom Ketiga:", list_2d[0][2] if len(list_2d[0]) > 2 else "N/A")
print("Baris Ketiga, Kolom Ketiga:", list_2d[2][2])
print("Baris Ke Empat, Kolom Pertama:", list_2d[3][0] if len(list_2d[3]) > 0 else "N/A")
