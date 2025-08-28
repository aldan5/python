
print("--------------------")
print("--Program La_Kasir--")
print("--------------------")
tot = 0
struks = []
while True:
    bg = input("masukkan Barang         :     ")
    jm = int(input("Berapa Pcs          :     "))
    hr = int(input("masukkan Harga      :     "))
    hasil = jm*hr
    tot+=hasil
    struks.append([bg,jm,hr])
    print(f"total {hasil:,}")
    print(f'Total Keseluruhan {tot:,}')
    qw = input("apakah masih ada? : ")
    if(qw == 'lanjut'):
        print(f"Tot : {hasil:,}")
        print(f"total sebesar Rp.{tot:,}")
    elif(qw == 'stop'):
        print("      ")
        print("-" * 30)   
        print("-------STRUK PEMBAYARAN-------")
        print("-" * 30)
        print(f"{"barang":<10} {"jumlah":<10} {"harga":<5} {"total":<10}")
        print("-" * 30)
        print(f"{bg:<10} {jm:<10} {hr:<5}")
        break
    else:
        print("nama tidak valid")

