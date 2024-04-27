def hitung_kelereng(jumlah_aldi):
    # Hitung jumlah kelereng Budi
    jumlah_budi = jumlah_aldi - 15

    # Hitung jumlah kelereng Anto
    jumlah_anto = 2 * jumlah_aldi

    # Hitung jumlah kelereng Agung
    jumlah_agung = jumlah_aldi + jumlah_budi + jumlah_anto - 5

    return jumlah_budi, jumlah_anto, jumlah_agung

def main():
    # Masukkan jumlah kelereng Aldi
    jumlah_aldi = int(input("Masukkan jumlah kelereng Aldi: "))

    # Hitung jumlah kelereng Budi, Anto, dan Agung
    jumlah_budi, jumlah_anto, jumlah_agung = hitung_kelereng(jumlah_aldi)

    # Tampilkan jumlah kelereng Budi, Anto, dan Agung
    print("Jumlah kelereng Budi:", jumlah_budi)
    print("Jumlah kelereng Anto:", jumlah_anto)
    print("Jumlah kelereng Agung:", jumlah_agung)

if __name__ == "__main__":
    main()
