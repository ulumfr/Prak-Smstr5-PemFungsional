# Fungsi untuk menghitung nilai akhir
def total_nilai_akhir(uts, uas):
    return (uts + uas) / 2

# Fungsi untuk menghitung semua nilai akhir
def total_nilai_akhir_semua_mhs(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = total_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Fungsi untuk menampilkan hasil nilai akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa\n")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        'Bahrul': {'uts': 86, 'uas': 94},
        'Gusnadir': {'uts': 80, 'uas': 90},
        'Amin': {'uts': 90, 'uas': 89},
    }

    data_nilai_akhir = total_nilai_akhir_semua_mhs(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()