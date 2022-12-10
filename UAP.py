import json, requests


def get_data():
    data = {}

    headers = {
        'cookie' : '_gcl_au=1.1.2039428886.1665158597; REC_T_ID=8e445e97-4659-11ed-88d7-f4ee08144ba4; SPC_IA=-1; SPC_F=SXu4UHq2h8soeq78jJIoOXIs33WqtaVR; REC_T_ID=8e46e6f6-4659-11ed-bacc-2e82ab78cbf0; _fbp=fb.2.1665158597343.565393092; _tt_enable_cookie=1; _ttp=e47857a0-204c-4918-9be3-7f79a7d60f0c; _gcl_aw=GCL.1665158961.Cj0KCQjwnP-ZBhDiARIsAH3FSRedua7LhrKlUX7UaBV7afOavDn7BUYzq9_PTXnrugjFASRYPG5GaNAaAmfeEALw_wcB; _gac_UA-61904553-8=1.1665158965.Cj0KCQjwnP-ZBhDiARIsAH3FSRedua7LhrKlUX7UaBV7afOavDn7BUYzq9_PTXnrugjFASRYPG5GaNAaAmfeEALw_wcB; G_ENABLED_IDPS=google; SPC_CLIENTID=U1h1NFVIcTJoOHNvtijzjdatvfjvqzls; SPC_T_ID="McGT19hErVq97Xns3dvQjk2R4k70+QCeqavlTEwiFOh7g8Sl1TBA9sC52WMJ/1yX0a1/paa01rBR0z0xKZBE/Rc8k2HVrFMgPBSDgSG6Cok="; SPC_T_IV="8cWOl5clokvhelDsObdlEQ=="; __LOCALE__null=ID; csrftoken=493l33fZ5nx78ii8izUuG7y9YxbsJe2B; SPC_SI=YIGHYwAAAAAzQXNuQ281d+7tsQEAAAAAVmlqc1lRNXM=; _QPWSDCXHZQA=f16fc9c3-c7ce-47a9-9041-842f3b1c8e41; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.2118628594.1670685006; SPC_ST=.V1Q3b1JDcFVRd0Y3c3dQWu6+DwQYdbFSrHHbN9zY9jYGmIheEOPPeV/kDv8FcAc36aIRWMxaxXuT3xt/RzNnRj1KqQ6VHxBaVnqH2LkF3/nlaw8QjSCScBNiGVL+m/YDIh/8oABKUxex/SymX7Rkz8ZDVZK6//FdjmMM9Hxo86L1MPNmy7le9c2EN3Xso0GKaaYCT1XPIBwxdTh8/Gew8A==; SPC_U=399878749; SPC_R_T_ID=ylwmZ3NtyN6KsNm4Ybx5D06j00pr92KTdbz9gSV6vjqgrnLWUokJos56EDFZ7Zam27VQwB++VVTUlGuyN56xoXoKz4t0vjJOkyAZWcOtd4bCRpcaNxPtZikC5Zj8WnlKuk5le9pWJEliUoJBXHFLle9jPHKLLbBVLYICrX6J5D4=; SPC_R_T_IV=eU5nYkcxcEticGVDYXB6Nw==; SPC_T_ID=ylwmZ3NtyN6KsNm4Ybx5D06j00pr92KTdbz9gSV6vjqgrnLWUokJos56EDFZ7Zam27VQwB++VVTUlGuyN56xoXoKz4t0vjJOkyAZWcOtd4bCRpcaNxPtZikC5Zj8WnlKuk5le9pWJEliUoJBXHFLle9jPHKLLbBVLYICrX6J5D4=; SPC_T_IV=eU5nYkcxcEticGVDYXB6Nw==; _ga=GA1.3.1958763726.1665158601; cto_bundle=0t4ZMV95dkJTM2FTR3A1WlJ3aUNHQlpMN3kyZVl0RVAyQXhVenNSWnN6cEhPRXVRUlR0SFBYM01jUUZ1VGoxRmxlOEp2aW0zUDZMMktPaXlSU1BUdzFVRFRsYWNIa1cyS0hGUUU4VVdtOTFRRXVmOTNFUkRwR1ZMSWZMTW1CSHNOV1d2UjZEbXA0RlJmbzN1V090bzlzaG5MVWclM0QlM0Q; shopee_webUnique_ccd=GfNwtzq2X3YNQ%2BHfZ35toQ%3D%3D%7CcFXgDWHvl%2BcaA4SoWrgm6Hvv28h6zeIDY0EzntoXGfxdU%2FqVRzQTIdAsMTBpWmSKMemS9yM6dOdGqcH44OEEkJMmJ3IkmVbo6us%3D%7CR%2BhOeGMED4iCh4Bf%7C06%7C3; ds=02c57611099674a10a423c087fd11c09; _ga_SW6D8G0HXK=GS1.1.1670685003.6.1.1670685594.60.0.0; SPC_EC=NHVyTGc1UGRXa3hMaXFMY2SZGGDPRDD2eUGwnvawydjEeHZgm8Krq5JepkFx7f/4ZDHD0xC3GPvIWP197UIIeod2GGoawYdI07ajKY59fbaSttVJyvpgv/s59EnTJsC6ef6bQWUAxZ6LbqdArIuS+TX138KQCFWoXR2sMfxpAiw=',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-api-source' : 'pc',
        'x-requested-with' : 'XMLHttpRequest'
    }

    shopee = requests.get('https://shopee.co.id/api/v4/shop/search_items?filter_sold_out=1&limit=30&offset=0&order=desc&shopid=241308147&sort_by=pop&use_case=4',headers = headers)
    toko = shopee.json() 

    i=0 
    for result in toko['items']:
        # index += 1
        # print(f"[{index}] {result['item_basic']['name']}")
        data[i] = {
            'itemid' : result['itemid'],
            'name' : result['item_basic']['name'],
            'price' : int(result['item_basic']['price']/100000)
        }
        i+=1

    return data

def product_list(data):
    for x in data:
        print(f"[{x+1}] {data[x]['name']}")

def get_detail(index,data):
    index -= 1
    print(f"[Item ID]\t: {data[index]['itemid']}")
    print(f"[Nama Produk]\t: {data[index]['name']}")
    print(f"[Price]\t\t: Rp {data[index]['price']}")
    

if __name__ == '__main__':

    
    pilih = int(input("Ibox Official Shop\n 1. Semua Produk \nPilih : "))

    if pilih == 1 :
        data = get_data()
        product_list(data) 
        choice = int(input("Pilih : "))
        get_detail(choice,data)



    
