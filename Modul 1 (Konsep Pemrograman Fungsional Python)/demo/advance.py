db_dataAkun_temp = {
    'users': {
        'ulum': {
            'name': 'Bahrul Ulum',
            'password': 'userUlum',
            'db_pinjam': []
        },
        'amin': {
            'name': 'Aminudin Muhibbulah',
            'password': 'userAmin',
            'db_pinjam': []
        }
    },
    'admin': {
        'perpus': {
            'name': 'Staff Perpus',
            'password': 'adminPerpus',
        },
        'owner': {
            'name': 'Owner Perpus',
            'password': 'adminOwner',
        }
    }
}
db_dataBuku_temp = []

def login():
    while True:
        print('\n===== LOGIN PERPUSTAKAAN =====')
        username = input('\nUsername: ')
        password = input('Password: ')
        
        if username in db_dataAkun_temp['admin'] and password == db_dataAkun_temp['admin'][username]['password']:
            nama = db_dataAkun_temp['admin'][username]['name']
            print('\n==============================')
            print(f'\n\nSelamat Datang, {nama}')
            admin_dashboard()
        elif username in db_dataAkun_temp['users'] and password == db_dataAkun_temp['users'][username]['password']:
            nama = db_dataAkun_temp['users'][username]['name']
            print('\n==============================')
            print(f'\n\nSelamat Datang, {nama}')
            user_dashboard(username)
        else: 
            print('\n### Account tidak ditemukan, Coba lagi...')

def admin_dashboard():
    while True:
        print('\n=== Admin Dashboard ===')
        print('1. Input Buku\n2. List Buku\n0. Logout')

        pilih = int(input('Pilih menu (1/2/0): '))
        if pilih == 1:
            input_buku()
        elif pilih == 2:
            list_buku()
        elif pilih == 0:
            print('\n## Berhasil Logout..')
            login()
        else:
            print('\n### Pilihan tidak ada, Coba lagi...')
        
def user_dashboard(username):
    while True:
        print('\n=== User Dashboard ===')
        print('1. Pinjam Buku\n2. List Buku\n3. Kembali Buku\n0. Logout')
        
        pilih = int(input('Pilih menu (1/2/3/0): '))
        if pilih == 1:
            pinjam_buku(username)
        elif pilih == 2:
            list_buku()
        elif pilih == 3:
            kembali_buku(username)
        elif pilih == 0:
            print('\n## Berhasil Logout..')
            login()
        else:
            print('\n### Pilihan tidak ada, Coba lagi...')
    
def input_buku():
    print('\n=== Input Buku ===\n')
    title = input('\nMasukan judul buku\t: ')
    author = input('Masukan pengarang buku\t: ')
    year = input('Masukan tahun terbit\t: ')
    category = input('Masukan kateogri buku\t: ')

    book_data = {'judul': title, 'penulis': author, 'tahun': year, 'kategori': category, 'available': True}

    db_dataBuku_temp.append(book_data)
    print(f'\n## Buku *{book_data["judul"]}* berhasil ditambahkan.')

def view_list(info_buku):
    print(f'Judul\t\t: {info_buku["judul"]}')
    print(f'Penulis\t\t: {info_buku["penulis"]}')
    print(f'Tahun Terbit\t: {info_buku["tahun"]}')
    print(f'Kategori\t: {info_buku["kategori"]}\n')

def list_buku():
    print('\n=== List Buku ===\n')
    if len(db_dataBuku_temp) == 0:
        print('### (List) Database Buku masih kosong...')
    else:
        for id_buku, info_buku in enumerate(db_dataBuku_temp):
            print(f'{id_buku + 1}.')
            view_list(info_buku)

            if info_buku['available']:
                print('Status\t\t: Buku tersedia\n')
            else:
                print('Status\t\t: Buku tidak tersedia\n')

def pinjam_buku(username):
    print('\n=== Pinjam Buku (Tersedia) ===\n')

    if len(db_dataBuku_temp) == 0:
        print('### (Pinjam) Database Buku masih kosong...')
    else:
        list_buku_tersedia = [info_buku for info_buku in db_dataBuku_temp if info_buku['available']]

        if len(list_buku_tersedia) == 0:
            print('### Tidak ada buku yang tersedia untuk dipinjam.')
        else:
            for id_buku, info_buku in enumerate(list_buku_tersedia):
                print(f'{id_buku + 1}.')
                view_list(info_buku)

            pilih_buku = int(input('\nPilih nomor buku yang ingin dipinjam: '))
            if pilih_buku >= 1 and pilih_buku <= len(list_buku_tersedia):
                pinjamBuku = list_buku_tersedia[pilih_buku - 1]
                pinjamBuku['available'] = False
                db_dataAkun_temp['users'][username]['db_pinjam'].append(pinjamBuku)
                print(f'\n## Anda berhasil meminjam buku *{pinjamBuku["judul"]}*')
            else:
                print('\n### Nomor buku yang Anda pilih tidak ada.')

def kembali_buku(username):
    print('\n=== Kembalikan Buku yang dipinjam ===\n')

    if len(db_dataAkun_temp['users'][username]['db_pinjam']) == 0:
        print('### Anda belum meminjam buku.')
    else:
        for id_buku, info_buku in enumerate(db_dataAkun_temp['users'][username]['db_pinjam']):
            print(f'{id_buku + 1}.')
            view_list(info_buku)

        pilih_buku = int(input('\nPilih nomor buku yang ingin Anda kembalikan: '))
        
        if pilih_buku >= 1 and pilih_buku <= len(db_dataAkun_temp['users'][username]['db_pinjam']):
            buku_kembali = db_dataAkun_temp['users'][username]['db_pinjam'].pop(pilih_buku - 1)
            buku_kembali['available'] = True
            print(f'\n## Anda telah mengembalikan buku *{buku_kembali["judul"]}*')
        else:
            print('\n### Nomor buku yang Anda pilih tidak ada.')
    
if __name__ == '__main__':
    login()