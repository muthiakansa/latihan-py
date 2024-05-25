def kategori_nilai(nilai):
    if nilai <= 10:
        return "kurang"
    elif 10 < nilai <= 50:
        return "kurang"
    elif 50 < nilai <= 70:
        return "cukup"
    elif 70 < nilai <= 85:
        return "baik"
    elif nilai > 85:
        return "sangat baik"
    else:
        return "nilai tidak valid"
    # Contoh penggunaan
nilai = 78
print(f"Nilai {nilai} adalah {kategori_nilai(nilai)}")
