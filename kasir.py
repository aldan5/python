print("--------------------")
print("--Program La_Kasir--")
print("--------------------")
tot = 0
barang = []
jumlah = []
harga = []
while True:
    bg = input("masukkan Barang         :     ")
    jm = int(input("Berapa Pcs          :     "))
    hr = int(input("masukkan Harga      :     "))
    hasil = jm*hr
    tot+=hasil
    print(f"total {hasil:,}")
    print(f'Total Keseluruhan {tot:,}')
    qw = input("apakah masih ada? : ")
    if(qw == 'lanjut'):
        print(f"Tot : {hasil:,}")
        print(f"total sebesar Rp.{tot:,}")
    elif(qw == 'stop'):
        print("---STRUK PEMBAYARAN-----")
        print("-" * 30)    
        print(f"{"barang":<10} {"jumlah":<10} {"harga":<5}")
        print("-" * 30)
        break
    else:
        print("nama tidak valid")