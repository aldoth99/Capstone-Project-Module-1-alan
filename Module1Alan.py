ListBarang  = [
    {
    'Jenis barang' : 'tablet',
    'Merk' : 'apple',
    'Type' : 'ipad 10',
    'Kode'  : 'a101',
    'Harga' : 7500000,
    'Stok' : 55
    },
    {
    'Jenis barang' : 'tablet',
    'Merk' : 'apple',
    'Type' : 'ipad air5',
    'Kode'  : 'a102',
    'Harga' : 8500000,
    'Stok' : 70
    },
    {
    'Jenis barang' : 'tablet',
    'Merk' : 'samsung',
    'Type' : 'tab A8',
    'Kode'  : 'a111',
    'Harga' : 3500000,
    'Stok' : 20
    },
    {
    'Jenis barang' : 'tablet',
    'Merk' : 'samsung',
    'Type' : 'tab S7',
    'Kode'  : 'a112',
    'Harga' : 9000000,
    'Stok' : 12
    },
    {
    'Jenis barang' : 'handphone',
    'Merk' : 'apple',
    'Type' : 'iphone 12',
    'Kode'  : 'a201',
    'Harga' : 11500000,
    'Stok' : 30
    },
    {
    'Jenis barang' : 'handphone',
    'Merk' : 'apple',
    'Type' : 'iphone 13',
    'Kode'  : 'a202',
    'Harga' : 17500000,
    'Stok' : 22
    },
    {
    'Jenis barang' : 'handphone',
    'Merk' : 'samsung',
    'Type' : 'galaxy A33',
    'Kode'  : 'a211',
    'Harga' : 4500000,
    'Stok' : 12
    },
    {
    'Jenis barang' : 'handphone',
    'Merk' : 'samsung',
    'Type' : 'galaxy S22',
    'Kode'  : 'a212',
    'Harga' : 12000000,
    'Stok' : 30
    },   
]

## READ DATA

def menampilkanDaftarBarang():
    print('\n-----------------------------  List Stock Barang  ------------------------------\n')
    print('Kode\t| Jenis\t\t| Merk\t\t| Type\t\t| Harga\t\t| Stok')
    for i in range(len(ListBarang)):
        print( ListBarang[i]['Kode'], ' \t|', ListBarang[i]['Jenis barang'],'  \t|', ListBarang[i]['Merk'],'  \t|', ListBarang[i]['Type'],'  \t|', ListBarang[i]['Harga'],'  \t|', ListBarang[i]['Stok'])


def tampilanKode():
        kodeBarang = input('\n   Masukkan kode item : ').lower()
        print('\n-----------------------------  List Stock Barang  ------------------------------\n')
        print('Kode\t| Jenis\t\t| Merk\t\t| Type\t\t| Harga\t\t| Stok')
        for i in range(len(ListBarang)):
            if kodeBarang == ListBarang[i]['Kode']:
                print( ListBarang[i]['Kode'], ' \t|', ListBarang[i]['Jenis barang'],'  \t|', ListBarang[i]['Merk'],'  \t|', ListBarang[i]['Type'],'  \t|', ListBarang[i]['Harga'],'  \t|', ListBarang[i]['Stok'])
                break
        else:
            print('\n     "Data tidak ditemukan"')

def tampilanKataKunci():
        Search = input('\n    Masukkan kata kunci : ').lower()
        print('\n-----------------------------  List Stock Barang  ------------------------------\n')
        print('Kode\t| Jenis\t\t| Merk\t\t| Type\t\t| Harga\t\t| Stok')
        for i in range(len(ListBarang)):
            if  Search == ListBarang[i]['Jenis barang'] or Search == ListBarang[i]['Merk'] or Search == ListBarang[i]['Type']:
                print( ListBarang[i]['Kode'], ' \t|', ListBarang[i]['Jenis barang'],'  \t|', ListBarang[i]['Merk'],'  \t|', ListBarang[i]['Type'],'  \t|', ListBarang[i]['Harga'],'  \t|', ListBarang[i]['Stok'])
            
def tampilanRangeHarga():
        while True:
            try:
                HargaMin = int(input('\n    Masukkan minimum harga : '))
                break
            except ValueError: 
                print('Masukan kembali harga yang tepat!')
                continue
        while True:
            try:
                HargaMax = int(input('    Masukkan maksimum harga : '))
                break
            except ValueError:
                print('Masukkan kembali harga yang tepat!')
        print('\n-----------------------------  List Stock Barang  ------------------------------\n')
        print('Kode\t| Jenis\t\t| Merk\t\t| Type\t\t| Harga\t\t| Stok')
        for i in range(len(ListBarang)):
            if HargaMin <= ListBarang[i]['Harga'] <= HargaMax:
              print( ListBarang[i]['Kode'], ' \t|', ListBarang[i]['Jenis barang'],'  \t|', ListBarang[i]['Merk'],'  \t|', ListBarang[i]['Type'],'  \t|', ListBarang[i]['Harga'],'  \t|', ListBarang[i]['Stok'])

def tampilanStokBarang():
        Stok = int(input('\n    Masukkan stok minimum yang dicari : '))
        print('\n-----------------------------  List Stock Barang  ------------------------------\n')
        print('Kode\t| Jenis\t\t| Merk\t\t| Type\t\t| Harga\t\t| Stok')
        for i in range(len(ListBarang)):
            if ListBarang[i]['Stok'] <= Stok:
              print( ListBarang[i]['Kode'], ' \t|', ListBarang[i]['Jenis barang'],'  \t|', ListBarang[i]['Merk'],'  \t|', ListBarang[i]['Type'],'  \t|', ListBarang[i]['Harga'],'  \t|', ListBarang[i]['Stok'])

def menampilkanDaftarBarang1():
    while True:
        menuMenampilkanDaftarBarang1 = input ('''
    1. Tampilkan data berdasarkan kode 
    2. Tampilkan data berdasarkan kata kunci
    3. Tampilkan data berdasarkan range harga
    4. Tampilkan data berdasarkan jumlah stok yang ada
    5. Kembali ke menu sebelumnya
    Silahkan pilih angka sub-menu [1-5] untuk menampilkan data  : ''')

        if menuMenampilkanDaftarBarang1 == '1' :
            tampilanKode()
        elif menuMenampilkanDaftarBarang1 == '2' :
            tampilanKataKunci()
        elif menuMenampilkanDaftarBarang1 == '3':
            tampilanRangeHarga()
        elif menuMenampilkanDaftarBarang1 == '4':
            tampilanStokBarang()
        elif menuMenampilkanDaftarBarang1 == '5':
            break

def menuReadData():
    while True:
        inputMenuRead = input('''

    1. Tampilkan seluruh data barang di gudang
    2. Tampilkan data berdasarkan kode/kelompok barang
    3. Kembali ke menu utama
    Silahkan pilih angka sub-menu [1-3] untuk menampilkan data barang  : ''')

        if inputMenuRead == '1' :
            menampilkanDaftarBarang()
        elif inputMenuRead == '2' :
            menampilkanDaftarBarang1()
        elif inputMenuRead == '3' :
            break


## CREATE DATA

def menambahListBarang():
    while True:
        inputJenis = input('\nMasukkan jenis barang : ').lower()
        inputMerk = input('Masukkan merk barang : ').lower()
        inputType = input('Masukkan tipe barang : ').lower()
        inputKode = input('Masukkan kode barang : ').lower()
        while True:
            try:
                inputHarga = int(input('Masukkan harga : '))
                break
            except ValueError: 
                print('Masukan kembali harga yang tepat!')
                continue
        while True:
            try:
                inputStok = int(input('Masukkan jumlah stok : '))
                break
            except ValueError:
                print('Masukkan kembali jumlah stock yang tepat!')
        databaru = {
        'Jenis barang' : '{}'.format(inputJenis),
        'Merk' : '{}'.format(inputMerk),
        'Type' : '{}'.format(inputType),
        'Kode' : '{}'.format(inputKode),
        'Harga': '{}'.format(inputHarga),
        'Stok' : '{}'.format(inputStok)
        }
    
        print('\nItem yang akan ditambahkan yaitu : ',databaru)
        checkDataBaru = input('\n     Apakah sudah benar? (Y/N) : ').lower()
        if checkDataBaru == 'y':
            ListBarang.append(databaru)
            print('\n     "Barang sudah berhasil ditambahkan"')
            break
        elif checkDataBaru == 'n':
            print('\n     "Barang tidak ditambahkan"')
            break
        else:
            break

def menuCreateData():
    while True:
        pilihMenuDataBaru = input('''
    1. Tambahkan data barang baru
    2. Kembali ke menu utama
    Silahkan masukan angka [1-2] sub-menu untuk membuat data baru : ''')
    
        if pilihMenuDataBaru == '1' :
            menambahListBarang()
        elif pilihMenuDataBaru == '2' :
            break


## UPDATE DATA


def UpdateBarang():
    updateCode = input('\n      Masukkan kode barang yang ingin diupdate : ')
    print('\n-----------------------------  List Stock Barang  ------------------------------\n')
    for i in range(len(ListBarang)):
        if updateCode == ListBarang[i]['Kode']:
            print('Kode\t| Jenis\t\t| Merk\t\t| Type\t\t| Harga\t\t| Stok')
            print( ListBarang[i]['Kode'], ' \t|', ListBarang[i]['Jenis barang'],'  \t|', ListBarang[i]['Merk'],'  \t|', ListBarang[i]['Type'],'  \t|', ListBarang[i]['Harga'],'  \t|', ListBarang[i]['Stok'])
            confup = input('\n        Apakah data ini yang ingin diupdate? (Y/N) : ' ).lower()
            if confup == 'y':
                while True:
                    pilihanMenuUpdate = input('''
    1. Update jenis barang
    2. Update merk barang
    3. Update type item
    4. Update kode item
    5. Update harga item
    6. Update stock item
    7. Update selesai
                    
    Silahkan masukkan angka sub-menu (1-7) untuk memilih data yang akan di update : ''')
                   
                    if pilihanMenuUpdate == '1':
                        ListBarang[i]['Jenis Barang'] = input('\n        Update jenis barang : ').lower()
                        print('\n        "Data berhasil diupdate"\n')
                        print('Kode\t| Jenis\t\t| Merk\t\t| Type\t\t| Harga\t\t| Stok')
                        print( ListBarang[i]['Kode'], ' \t|', ListBarang[i]['Jenis barang'],'  \t|', ListBarang[i]['Merk'],'  \t|', ListBarang[i]['Type'],'  \t|', ListBarang[i]['Harga'],'  \t|', ListBarang[i]['Stok'])
                    elif pilihanMenuUpdate == '2':
                        ListBarang[i]['Merk'] = input('\n        Update merk barang : ').lower()
                        print('\n        "Data berhasil diupdate"\n')
                        print('Kode\t| Jenis\t\t| Merk\t\t| Type\t\t| Harga\t\t| Stok')
                        print( ListBarang[i]['Kode'], ' \t|', ListBarang[i]['Jenis barang'],'  \t|', ListBarang[i]['Merk'],'  \t|', ListBarang[i]['Type'],'  \t|', ListBarang[i]['Harga'],'  \t|', ListBarang[i]['Stok'])
                    elif pilihanMenuUpdate == '3':
                        ListBarang[i]['Type'] = input('\n        Update type barang : ').lower()
                        print('\n        "Data berhasil diupdate"\n')
                        print('Kode\t| Jenis\t\t| Merk\t\t| Type\t\t| Harga\t\t| Stok')
                        print( ListBarang[i]['Kode'], ' \t|', ListBarang[i]['Jenis barang'],'  \t|', ListBarang[i]['Merk'],'  \t|', ListBarang[i]['Type'],'  \t|', ListBarang[i]['Harga'],'  \t|', ListBarang[i]['Stok'])
                    elif pilihanMenuUpdate == '4':
                        ListBarang[i]['Kode'] = input('\n        Update kode barang : ').lower()
                        print('\n        "Data berhasil diupdate"\n')
                        print('Kode\t| Jenis\t\t| Merk\t\t| Type\t\t| Harga\t\t| Stok')
                        print( ListBarang[i]['Kode'], ' \t|', ListBarang[i]['Jenis barang'],'  \t|', ListBarang[i]['Merk'],'  \t|', ListBarang[i]['Type'],'  \t|', ListBarang[i]['Harga'],'  \t|', ListBarang[i]['Stok'])
                    elif pilihanMenuUpdate == '5':
                        while True:
                            try:
                                ListBarang[i]['Harga'] = int(input('\n        Update harga barang : '))
                                break
                            except ValueError: 
                                print('Masukan kembali harga yang tepat!')
                                continue
                        print('\n        "Data berhasil diupdate"\n')
                        print('Kode\t| Jenis\t\t| Merk\t\t| Type\t\t| Harga\t\t| Stok')
                        print( ListBarang[i]['Kode'], ' \t|', ListBarang[i]['Jenis barang'],'  \t|', ListBarang[i]['Merk'],'  \t|', ListBarang[i]['Type'],'  \t|', ListBarang[i]['Harga'],'  \t|', ListBarang[i]['Stok'])
                    elif pilihanMenuUpdate == '6':
                        while True:
                            try:
                                ListBarang[i]['Stok'] = int(input('\n        Update stok barang : '))
                                break
                            except ValueError: 
                                print('Masukan kembali jumlah stok yang tepat!')
                                continue
                        print('\n        "Data berhasil diupdate"\n')
                        print('Kode\t| Jenis\t\t| Merk\t\t| Type\t\t| Harga\t\t| Stok')
                        print( ListBarang[i]['Kode'], ' \t|', ListBarang[i]['Jenis barang'],'  \t|', ListBarang[i]['Merk'],'  \t|', ListBarang[i]['Type'],'  \t|', ListBarang[i]['Harga'],'  \t|', ListBarang[i]['Stok'])
                    elif pilihanMenuUpdate == '7':
                        break
            elif confup == 'n':
                print('\n      "Tidak ada data yang diupdate"')
                break
            else:
                print('\n      "Perintah yang anda masukkan salah"')
                break


def menuUpdateData():
    while True:
        inputMenuUpdate = input('''
    1. Update data barang
    2. Kembali ke menu utama
        
    Silahkan pilih angka Sub-Menu [1-2] Update Data Barang  : ''')

        if inputMenuUpdate == '1' :
            UpdateBarang()
        elif inputMenuUpdate == '2':
            break


## DELETE DATA


def DeleteData():
    while True:
        del_code = input('\n    Masukkan kode barang yang akan dihapus : ').lower()
        for i in range(len(ListBarang)):
            if del_code == ListBarang[i]['Kode']:
                print('\nData barang yang akan dihapus adalah : ', ListBarang[i])
                confirm_Del = input('\n        Apakah yakin ingin menghapus data ini? (Y/N) : ').lower()
                if confirm_Del == 'y':
                    del ListBarang[i]
                    print('\n        "Data berhasil dihapus"') 
                    break
                elif confirm_Del == 'n':
                    print('\n        "Tidak ada data yang dihapus"')
                    break
                else:
                    print('\n        "Perintah yang anda masukkan salah"')
                    break

        else:
            print('\n        "Data tidak ditemukan"')
        break


def menuDeleteData():
    while True:
        pilihMenuDelete = input('''
    1. Delete Data
    2. Kembali ke menu utama
        
    Silahkan pilih angka [1-2] Sub-Menu untuk hapus data barang  : ''')

        if pilihMenuDelete == '1' :
            DeleteData()
        elif pilihMenuDelete == '2':
            break


## MAIN MENU

while True:
    menuUtama = input ('''
    Selamat Datang di Aplikasi Gudang Alan Amdani Cell!

    1. Menampilkan Daftar Barang
    2. Menambahkan Barang Baru
    3. Update Barang
    4. Delete Barang
    5. Keluar
    Silahkan masukkan angka [1 - 5] untuk memilih menu yang akan Anda jalankan :''')
    
    if menuUtama == '1':
        menuReadData()
    if menuUtama == '2':
        menuCreateData()
    if menuUtama == '3':
        menuUpdateData()
    if menuUtama == '4' :
        menuDeleteData()
    elif menuUtama == '5':
        print('\n        Terima kasih, sampai jumpa!\n')
        break