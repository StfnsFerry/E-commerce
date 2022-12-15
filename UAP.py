import API_iBox, os, time
from Tampilan import hias

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

def login() :
    global user, unem, alamat
    while True :
        os.system('cls')
        hias.shopee()
        print('\n[1] LOG IN')
        print('[2] SIGN UP')
        print('[3] EXIT')
        try :
            akun = int(input('\nMasuk dengan : '))
            if akun != 1 and akun != 2 and akun != 3 :
                raise ValueError
            if akun == 1 :
                os.system('cls')
                hias.log()
                unem = input('\nUsername\t: ')
                pw = input('Password\t: ')
                for cek in user :
                    if cek['username'] == unem  and cek['password'] == pw :
                        alamat = cek['alamat']
                        os.system('cls')
                        menu() 
                else :
                    os.system('cls')
                    hias.error()
                    print('\nHarap Masukkan Username atau Password yang terdaftar!')
                    time.sleep(2)
                    login()
            elif akun == 2 :
                os.system('cls')
                hias.sign()
                unem = input('\nUsername\t: ')
                pw = input('Password\t: ')
                for cek in user :
                    if cek['username'] == unem :
                        os.system('cls')
                        hias.error()
                        print('Username sudah digunakan!')
                        time.sleep(2)
                        login()
                else :
                    new['username'] = unem
                    new['password'] = pw
                    user.append(new)
                    print('\nAkun tersimpan!\nSilahkan login')
                    time.sleep(2)
                    login()
            elif akun == 3 :
                os.system('cls')
                hias.bye()
                quit()
        except ValueError:
            os.system('cls')
            hias.error()
            print('\nMasukan anda tidak sesuai')
            time.sleep(2)

def menu() :

    while True :
        hias.ibox()
        try :
            pilih = int(input("\n[Ibox Official Shop]\n\n [1] iPhone \n [2] iPad\n [3] Apple Watch\n [4] Mac\n [5] Aksesoris Apple\n\n Pilih : "))
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
            else :
                raise ValueError
            os.system('cls')
            break
        except  ValueError:
            print()
            hias.error()
            print("\nMasukan anda tidak sesuai.")
            time.sleep(2)
            os.system('cls')

    while True:
        hias.ibox()
        product_list(data)
        print("[0] Back")
        try :
            index = int(input("\n\nPilih : "))
            if index == 0 :
                os.system('cls')
                menu()
            if index > 29 or index < 0 :
                raise ValueError
            os.system('cls')
            break
        except ValueError:
            os.system('cls')
            hias.error()
            print("\nMasukan anda tidak sesuai.")
            time.sleep(2)
            os.system('cls')
    
    while True:
        os.system('cls')
        hias.ibox()
        get_detail(index,data)
        print("[0] Back\n")
        try:
            qty = int(input('Jumlah Beli : '))  
            if qty > data[index-1]['stock'] :
                print(f"\nStok Tidak Cukup!\n[Stock] : {data[index-1]['stock']}")
                raise ValueError
            elif qty < 0 :
                print("\nJumlah beli tidak dapat diproses.")
                raise ValueError
            elif qty == 0 :
                os.system('cls')
                menu()
            else :
                payment(index,qty,data)
                break
        except ValueError:
            print()
            hias.error()
            time.sleep(2)
    
def payment(index, qty, data):

    global unem, alamat
    os.system('cls')
    hias.co()
    index -= 1
    harga = int(data[index]['price']*qty) 
    print(f"\n[Nama Barang]\t: {data[index]['name']}")
    print(f'[Jumlah Barang]\t: {qty}')
    print(f'[Total Harga]\t: Rp {harga}')
    if alamat == '' :
        alamat = input('\n[Masukkan Alamat]\t: ') 
    else :
        print(f'\n[Alamat Pengiriman]\t: {alamat}')
        ubah = input("\nIngin mengubah alamat?\n[Y/T] : ")
        change = ubah.lower()
        if change == 'y' :
            alamat = input('\n[Masukkan Alamat]\t: ')
                
    while True :
        try :
            pil = input("\nCheckout?\n[Y/T] : ")
            co = pil.upper()
            print(co)
            if co != 'Y' and co != 'T' :
                raise ValueError
            elif co == 'T' :
                os.system('cls')
                menu()
            elif co == 'Y' :
                os.system('cls')
                hias.co()
                while True :
                    data[index]['stock'] -= qty
                    print('\n[BERHASIL MELAKUKAN CHECKOUT]\n')
                    print(f'[Nama Akun]\t\t: {unem}\n')
                    print(f"[Nama Barang]\t\t: {data[index]['name']}")
                    print(f"[Harga Barang]\t\t: Rp {data[index]['price']}")
                    print(f'[Jumlah Barang]\t\t: {qty}')
                    print(f'[Total Harga]\t\t: Rp {harga}\n')
                    print(f'[Alamat Pengiriman]\t: {alamat}')
                    try :
                        bukti = input("\nIngin mengunduh bukti transaksi?\n[Y/T] : ")
                        unduh = bukti.upper()
                        if unduh != 'Y' and unduh != 'T' :
                            raise ValueError
                        elif unduh == 'Y' :
                            file = open("Shopee Transaction.txt","w")
                            file.write("[SHOPEE CHECKOUT]\n\n")
                            file.write(f'[Nama Akun]\t\t\t: {unem}\n')
                            file.write(f"[Nama Barang]\t\t: {data[index]['name']}\n")
                            file.write(f"[Harga Barang]\t\t: {data[index]['price']}\n")
                            file.write(f'[Jumlah Barang]\t\t: {qty}\n')
                            file.write(f'[Total Harga]\t\t: Rp.{harga}\n')
                            file.write(f'[Alamat Pengiriman]\t: {alamat}\n')
                            file.close()
                            os.system('cls')
                            hias.co()
                            print("\nFile Sudah Diunduh.")
                        elif unduh == 'T' :
                            os.system('cls')
                            hias.co()
                        time.sleep(2)
                        break
                    except ValueError :
                        os.system('cls')
                        print()
                        hias.error()
                        time.sleep(2)
                main()
        except ValueError:
            os.system('cls')
            hias.error()
            time.sleep(2)

def main() :
    while True:
        try :
            ulang = input("\nIngin membeli lagi?\n[Y/T]")
            jawab = ulang.upper()
            if jawab != 'Y' and jawab != 'T' :
                raise ValueError
            if jawab == 'Y' :
                login()
            if jawab == 'T' :
                os.system('cls')
                hias.bye()
                quit()
        except ValueError :
            os.system('cls')
            hias.error()
            print("\nMasukan anda tidak sesuai.")
            time.sleep(2)    

login()
