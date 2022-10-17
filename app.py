total = 0
barang = []
harga= []

while True:
    print("""Daftar Barang/n
    1. Pulpen \t\t 5000
    2. Pensil \t\t 3000
    3. Penghapus \t 3500
    4. Penggaris \t 6000
    5. Buku Tulis \t 4000
    6. Buku Gambar \t 7000
    7. TipEx \t\t 5000""")

    kode = int(input("Masukan Kode Barang : "))
    if kode == 1:
        barang.append("Pulpen")
        harga.append(5000)
        total += 5000
    elif kode == 2 :
        barang.append("Pensil")
        harga.append(3000)
        total += 3000
    elif kode == 3 :
        barang.append("Penghapus")
        harga.append(3500)
        total += 3500
    elif kode == 4 :
        barang.append("Peggaris")
        harga.append(6000)
        total += 6000
    elif kode == 5 :
        barang.append("Buku Tulis")
        harga.append(4000)
        total += 4000
    elif kode == 6 :
        barang.append("Buku Gambar")
        harga.append(7000)
        total += 7000
    elif kode == 7 :
        barang.append("TipEx")
        harga.append(5000)
        total += 5000
    else:
        print("Kode Yang Anda Masukan Tidak Valid")

    lanjut = input("Lanjut Berbelanja ? (Y/T): ")
    if lanjut == "T":
        print("")
        break

print("Barang yang di Beli: ",barang)
print("Harga Barang : ", harga)
print("Total yang harus di bayar: ",total, "\n")

uang = int(input("Masukan Jumlah Uang Pembayaran : Rp."))
if uang>total:
    print("Uang Kembali : Rp.",uang-total)
elif uang == total:
    print("Uang Pas")
else:
    print("Uangnya Kurang Rp.",uang-total)