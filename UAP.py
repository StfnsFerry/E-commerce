import json, requests
import API_iBox 
import os, time
# from Tampilan import hias

jihan = {'username' : 'jihannhayaa', 
         'password' : '2117051095',
         'alamat' : 'Jl. Soekarno - Hatta No.114, Delima, Kec. Tampan, Kota Pekanbaru, Riau 28292'}

ferry = {'username' : 'stfnsferry', 
         'password' : '2117051025',
         'alamat' : 'Jl. Teuku Umar Jl. Sultan Agung No.1, Labuhan Ratu, Kec. Kedaton, Kota Bandar Lampung, Lampung 35132'}

abiy = {'username' : 'abiqyanisa', 
        'password' : '2117051088',
        'alamat' : 'Jl. BSD Raya Utama, Pagedangan, Kec. Pagedangan, Kabupaten Tangerang, Banten 15345'}

new = {'username' : 'none',
       'password' : 'none',
       'alamat' : 'none'}

user = [jihan,ferry,abiy,new]
unem, alamat = '',''

def product_list(data):
    print('\n')
    for x in data:
        print(f"[{x+1}] {data[x]['name']}")

def get_detail(index,data):
    index -= 1
    print(f"\n[Item ID]\t: {data[index]['itemid']}")
    print(f"[Nama Produk]\t: {data[index]['name']}")
    print(f"[Price]\t\t: Rp {data[index]['price']}")
    print(f"[Stock]\t\t: {data[index]['stock']}\n")
    print("[SEE IMAGE] :")
    print(f"https://cf.shopee.co.id/file/{data[index]['image']}\n")

def menu() :
    try:
        pilih = int(input("Ibox Official Shop\n [1] iPhone \n [2] iPad\n [3] Apple Watch\n [4] Mac\n [5] Aksesoris Apple\n Pilih : "))
        os.system('cls')
        if pilih == 1 :
            data = API_iBox.get_data(API_iBox.iphone)   

        elif pilih == 2 : 
            data = API_iBox.get_data(API_iBox.ipad)

        elif pilih == 3 : 
            data = API_iBox.get_data(API_iBox.iwatch)

        elif pilih == 4 : 
            data = API_iBox.get_data(API_iBox.mac)

        elif pilih == 5 : 
            data = API_iBox.get_data(API_iBox.aksesoris)

        else:
            print("Kategori Tidak Ada!")  
            quit()   

        product_list(data) 
        index = int(input("\nPilih : "))
        get_detail(index,data)
        qty = int(input('Jumlah Beli\t : '))  
        if qty > data[index-1]['stock'] :
            print(f"Stok Tidak Cukup!\n[Stock]\t\t: {data[index-1]['stock']}")
            menu()
        elif qty <= 0 :
            print("Jumlah beli tidak dapat diproses.")
            menu()
         else:
            payment(index,qty,data)
                                                          
    except ValueError :
        print("Inputan Salah!")   

def login() :
    global user, unem, alamat
    os.system('cls')
    # hias.shopee()
    print('\n[1] LOG IN')
    print('[2] SIGN UP')
    akun = int(input('\nMasuk dengan : '))
    if akun == 1 :
        os.system('cls')
        # hias.log()
        unem = input('\nUsername\t: ')
        pw = input('Password\t: ')
        for cek in user :
            if cek['username'] == unem  and cek['password'] == pw :
                alamat = cek['alamat']
                os.system('cls')
                menu()   
                quit()           
        else :
            os.system('cls')
            print('\nHarap Masukkan Username atau Password yang terdaftar!')
            time.sleep(2)
            login()
    elif akun == 2 :
        unem = input('Username\t: ')
        pw = input('Password\t: ')
        for cek in user :
            if cek['username'] == unem :
                print('Username sudah digunakan!')
                time.sleep(2)
                login()
        else :
            new['username'] = unem
            new['password'] = pw
            user.append(new)
            print('Akun tersimpan!\n Silahkan login')
            time.sleep(2)
            login()
    else :
        print("Harap Masuk dengan 1 atau 2.")
        time.sleep(2)
        login()


def payment(index,qty,data):
    global unem, alamat
    index -= 1
    harga = int(data[index]['price']*qty) 
    print(f'\nQty : {qty}')
    print(f'Total Harga : Rp {harga}')
    if alamat == 'none' :
        alamat = input('Masukkan Alamat : ') 
    else :
        print(f'Alamat Pengiriman : {alamat}')
        # alamat = ''
        ubah = input("Ubah Alamat? (y/t) ")
        change = ubah.lower()
        if change == 'y' :
            alamat = input('Masukkan Alamat : ')
    pil = input("\nCheckout? (y/t) ")
    co = pil.upper()
    print(co)
    if co == 'Y' :
        data[index]['stock'] = 0
        print(f'Nama Akun : {unem}\n')
        print(f"Nama Barang : {data[index]['name']}")
        print(f"Harga Barang : {data[index]['price']}")
        print(f'Qty : {qty}')
        print(f'Total Harga : Rp {harga}\n')
        print(f'Alamat Pengiriman : {alamat}')

        bukti = input("Apakah anda ingin mengunduh bukti transaksi?")
        unduh = bukti.upper()
        
        if unduh == 'Y' :
            file = open("Shopee Transaction.txt","w")
            file.write("SHOPEE CHECKOUT\n")

            file.write(f'Nama Akun : {unem}\n\n\n')
            file.write(f"Nama Barang : {data[index]['name']}\n")
            file.write(f"Harga Barang : {data[index]['price']}\n")
            file.write(f'Qty : {qty}\n')
            file.write(f'Total Harga : Rp {harga}\n\n')
            file.write(f'Alamat Pengiriman : {alamat}')
            file.close()
            print("File Sudah Diunduh")
            print()
   
login()
