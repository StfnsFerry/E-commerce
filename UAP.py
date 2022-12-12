import json, requests

iphone = 31530154
ipad = 31530572
iwatch = 31530571
mac = 31530570
aksesoris = 31530569

def get_data(id):
    data = {}

    headers = {
        'cookie' : '_gcl_au=1.1.2039428886.1665158597; REC_T_ID=8e445e97-4659-11ed-88d7-f4ee08144ba4; SPC_IA=-1; SPC_F=SXu4UHq2h8soeq78jJIoOXIs33WqtaVR; REC_T_ID=8e46e6f6-4659-11ed-bacc-2e82ab78cbf0; _fbp=fb.2.1665158597343.565393092; _tt_enable_cookie=1; _ttp=e47857a0-204c-4918-9be3-7f79a7d60f0c; _gcl_aw=GCL.1665158961.Cj0KCQjwnP-ZBhDiARIsAH3FSRedua7LhrKlUX7UaBV7afOavDn7BUYzq9_PTXnrugjFASRYPG5GaNAaAmfeEALw_wcB; _gac_UA-61904553-8=1.1665158965.Cj0KCQjwnP-ZBhDiARIsAH3FSRedua7LhrKlUX7UaBV7afOavDn7BUYzq9_PTXnrugjFASRYPG5GaNAaAmfeEALw_wcB; G_ENABLED_IDPS=google; SPC_CLIENTID=U1h1NFVIcTJoOHNvtijzjdatvfjvqzls; SPC_T_ID="McGT19hErVq97Xns3dvQjk2R4k70+QCeqavlTEwiFOh7g8Sl1TBA9sC52WMJ/1yX0a1/paa01rBR0z0xKZBE/Rc8k2HVrFMgPBSDgSG6Cok="; SPC_T_IV="8cWOl5clokvhelDsObdlEQ=="; SPC_SI=YIGHYwAAAAAzQXNuQ281d+7tsQEAAAAAVmlqc1lRNXM=; _gid=GA1.3.2118628594.1670685006; SPC_ST=.V1Q3b1JDcFVRd0Y3c3dQWu6+DwQYdbFSrHHbN9zY9jYGmIheEOPPeV/kDv8FcAc36aIRWMxaxXuT3xt/RzNnRj1KqQ6VHxBaVnqH2LkF3/nlaw8QjSCScBNiGVL+m/YDIh/8oABKUxex/SymX7Rkz8ZDVZK6//FdjmMM9Hxo86L1MPNmy7le9c2EN3Xso0GKaaYCT1XPIBwxdTh8/Gew8A==; SPC_U=399878749; SPC_R_T_ID=ylwmZ3NtyN6KsNm4Ybx5D06j00pr92KTdbz9gSV6vjqgrnLWUokJos56EDFZ7Zam27VQwB++VVTUlGuyN56xoXoKz4t0vjJOkyAZWcOtd4bCRpcaNxPtZikC5Zj8WnlKuk5le9pWJEliUoJBXHFLle9jPHKLLbBVLYICrX6J5D4=; SPC_R_T_IV=eU5nYkcxcEticGVDYXB6Nw==; SPC_T_ID=ylwmZ3NtyN6KsNm4Ybx5D06j00pr92KTdbz9gSV6vjqgrnLWUokJos56EDFZ7Zam27VQwB++VVTUlGuyN56xoXoKz4t0vjJOkyAZWcOtd4bCRpcaNxPtZikC5Zj8WnlKuk5le9pWJEliUoJBXHFLle9jPHKLLbBVLYICrX6J5D4=; SPC_T_IV=eU5nYkcxcEticGVDYXB6Nw==; __LOCALE__null=ID; csrftoken=l3XujiHVgMDN2OHgBsSJtcb7UeAmq97i; _QPWSDCXHZQA=f16fc9c3-c7ce-47a9-9041-842f3b1c8e41; cto_bundle=o63lUF95dkJTM2FTR3A1WlJ3aUNHQlpMN3klMkZFWlhuZVVsOUNLa1dOUWRUSVB4YXRsekVHSXRIT2JPJTJGUkVlN2oyTko0cVVJN3Ryckl2OTBmMU5RYUJFeDBlV3p6VSUyRnRtTW10VHBRdEI1dkRBSW9HOVZUUFptQUVYbzJ4aUV5WTlJSkkxNUdqbHhBJTJGWXhOYU53c0NYaDhxVXBpQSUzRCUzRA; AMP_TOKEN=%24NOT_FOUND; shopee_webUnique_ccd=oYZq4%2BtTLJOchg8vLoq0tw%3D%3D%7CMryRNBIf6ZDfT9Sr3awXnzUXRjMSeAHE2mEdES5lcL5zTmF9LMBPgElUSvkXiic316MTQaqHRcDifuG9R8B%2FfRDbqTdh22gXtpg%3D%7CL7DIctah8TBgJ%2Bp4%7C06%7C3; ds=56c55619a43f282d3ea4ee7bca03e296; _ga=GA1.1.1958763726.1665158601; _ga_SW6D8G0HXK=GS1.1.1670728267.9.1.1670728834.60.0.0; SPC_EC=TXV6TEhVeURLSmRDbThDcENTgbdJQlGUAEwRT3zE/NFZPp3V6rzSSou4kNEyBfYxTQ6asKxI30XUdQ30w/zh58aihNouAOMBudXiAnkoiQggM3kmdv6HIaZAmO1dgG2b2ShE2F6l5l4yVmYPkahK7Wfh3j7BHXH/7XNSzmS8BM8=',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-api-source' : 'pc',
        'x-requested-with' : 'XMLHttpRequest',
        'if-none-match-' : '55b03-8f16645ce8bb8b4e37f91d80cbf51347',
        'referer': 'https://shopee.co.id/iboxofficial?page=0&shopCollection='+str(id),
    }
    try:
        shopee = requests.get('https://shopee.co.id/api/v4/recommend/recommend?bundle=shop_page_category_tab_main&catid='+str(id)+'&is_generated=false&item_card=2&keyword=ibox&limit=30&offset=0&section=shop_page_category_tab_main_sec&shopid=241308147&sort_type=1&tab_name=popular&upstream=search',headers = headers)
        body = shopee.json()

        i=0 
        for result in body['data']['sections'][0]['data']['item']:
            data[i] = {
                'itemid' : result['itemid'],
                'name' : result['name'],
                'price' : int(result['price']/100000)
            }
            i+=1
        return data
    except:
        print("Error Get Data")

def product_list(data):
    print('\n')
    for x in data:
        print(f"[{x+1}] {data[x]['name']}")

def get_detail(index,data):
    index -= 1
    print(f"\n[Item ID]\t: {data[index]['itemid']}")
    print(f"[Nama Produk]\t: {data[index]['name']}")
    print(f"[Price]\t\t: Rp {data[index]['price']}\n")
    
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
        qty = int(input('Jumlah Beli : '))  
        if qty > data[index]['stock'] :
            print(f"Stok Tidak Cukup!\n[Stock]\t\t: {data[index]['stock']}")
            menu()
        elif qty <= 0 :
            print("Jumlah beli tidak dapat diproses.")
            menu()
        payment(index,qty,data)
                                                          
    except ValueError :
        print("Inputan Salah!")   

def login() :
    global user, unem, alamat
    os.system('cls')
    # hias.shopee()
    print('[1] LOG IN')
    print('[2] SIGN UP')
    akun = int(input('\nMasuk dengan : '))
    if akun == 1 :
        unem = input('Username\t: ')
        pw = input('Password\t: ')
        for cek in user :
            if cek['username'] == unem  and cek['password'] == pw :
                alamat = cek['alamat']
                os.system('cls')
                menu()   
                quit()           
        else :
            print('Harap Masukkan Username atau Password yang terdaftar!')
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
    if alamat == '' :
        alamat = input('Masukkan Alamat : ') 
    else :
        print(f'Alamat Pengiriman : {alamat}')
        alamat = ''
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


# if __name__ == '__main__':

#     try:
#         pilih = int(input("Ibox Official Shop\n 1. iPhone \n 2. iPad\n 3. Apple Watch\n 4. Mac\n 5. Aksesoris Apple\n Pilih : "))
#         if pilih == 1 :
#             data = get_data(iphone)
#             product_list(data)
#             index = int(input("\nPilih : "))
#             try:
#                 get_detail(index,data)
#                 qty = int(input('Jumlah Beli : '))
#                 payment(index,qty,data)
#             except:
#                 print("Barang tidak ada!")    

#         elif pilih == 2 : 
#             data = get_data(ipad)
#             product_list(data) 
#             index = int(input("\nPilih : "))
#             try:
#                 get_detail(index,data)
#                 qty = int(input('Jumlah Beli : '))
#                 payment(index,qty,data)
#             except:
#                 print("Barang tidak ada!")

#         elif pilih == 3 : 
#             data = get_data(iwatch)
#             product_list(data) 
#             index = int(input("\nPilih : "))
#             try:
#                 get_detail(index,data)
#                 qty = int(input('Jumlah Beli : '))
#                 payment(index,qty,data)
#             except:
#                 print("Barang tidak ada!")   

#         elif pilih == 4 : 
#             data = get_data(mac)
#             product_list(data) 
#             index = int(input("\nPilih : "))
#             try:
#                 get_detail(index,data)
#                 qty = int(input('Jumlah Beli : '))
#                 payment(index,qty,data)
#             except:
#                 print("Barang tidak ada!")

#         elif pilih == 5 : 
#             data = get_data(aksesoris)
#             product_list(data) 
#             index = int(input("\nPilih : "))
#             try:
#                 get_detail(index,data)
#                 qty = int(input('Jumlah Beli : '))
#                 payment(index,qty,data)
#             except:
#                 print("Barang tidak ada!")   

#         else:
#             print("Kategori Tidak Ada!")                                                  
#     except:
#         print("Inputan Salah!")   
        
        
        
