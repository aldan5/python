print("--------------------")
print("--Program La_Kasir--")
print("--------------------")
tot = 0
while True:
    bg = input("masukkan Barang         : ")   
    jm = int(input("Berapa Pcs          : "))
    hr = int(input("masukkan Harga      :"))
    hasil = jm*hr
    tot+=hasil
    print(f'{tot:,}')
    qw = input("apakah masih ada? : ")
    if(qw == 'lanjut'):
        print(f"brg : {bg}")
        print(f"pcs : {jm}")
        print(f"price : {hr}")
        print(f"total sebesar Rp.{tot:,}")
        
    # *masukkan tabel untuk total belanjaan*
    elif(qw == 'stop'): 
        print(f"brg : {bg}")
        print(f"pcs : {jm}")
        print(f"price : {hr}")
        print(f"total sebesar Rp.{tot:,}")
        break
    else:
        print("nama tidak valid")

# struk
print("---STRUK PEMBAYARAN-----")
print("-" * 30)    
print(f"{"barang":<10} {"jumlah":<10} {"harga":<5}")
print("-" * 30)
print(f"{"mangga":<10} {"4":^7} {"30000":>8}")
print(f"{"mangga":<10} {"4":^7} {"30000":>8}")
print(f"{"mangga":<10} {"4":^7} {"30000":>8}")
print(f"{"mangga":<10} {"4":^7} {"30000":>8}")
print("-" * 30)



   



    

    


   
