
from tabulate import tabulate

nama = []
cari_pesanan = []

# List Daftar Menu
menuMakanan = [
    ["1", "Steak", "Rp. 15.000"],
    ["2", "Beef Burger", "Rp. 12.000"],
    ["3", "Spaghetti Bolognese", "Rp. 12.000"],
    ["4", "Magelangan", "Rp. 10.000"],
    ["5", "Nasi Goreng", "Rp. 13.000"],
    ["6", "Mie Ayam", "Rp. 10.000"],
    ["7", "Dimsum", "Rp. 9.000"],
    ["8", "Onion Rings", "Rp. 7.000"],
    ["9", "French Fries", "Rp. 7.000"],
    ["10", "Keripik Ubi", "Rp. 5.000"],
    ["11", "Tanpa Makanan", "Rp. 0"]
]
hargaMakanan = [15000, 12000, 12000, 10000, 13000, 
                10000, 9000, 7000, 7000, 5000, 0]

menuMinuman = [
    ["1", "Es Teh", "Rp. 4.000"],
    ["2", "Es Jeruk", "Rp. 4.000"],
    ["3", "Mix Fruit Juice", "Rp. 12.000"],
    ["4", "Matcha", "Rp. 8.000"],
    ["5", "Cappucino", "Rp. 8.000"],
    ["6", "Mocha", "Rp. 8.000"],
    ["7", "Americano", "Rp. 8.500"],
    ["8", "Tanpa Minuman", "Rp. 0"]
]
hargaMinuman = [4000, 4000, 12000, 8000, 8000, 8000, 8500, 0]

menuTambahan = [
    ["A", "Nasi Uduk", "Rp. 4.000"],
    ["B", "Nasi Putih", "Rp. 3.000"],
    ["C", "Kuah Soto", "Rp. 3.000"],
    ["D", "Tanpa Menu Tambahan", "Rp. 0"]
]
hargaTambahan = [4000, 3000, 3000, 0]

print("================================================")
print("Daftar Menu Cafe Relasi")
print("================================================")
print("\n Menu Makanan")
print(tabulate(menuMakanan, tablefmt="grid", headers=[
      "No.", "Menu Makanan", "Tarif"], numalign="center", stralign="center"))
print("\n Menu Minuman")
print(tabulate(menuMinuman, tablefmt="grid", headers=[
      "No.", "Menu Minuman", "Tarif"], numalign="center", stralign="center"))
print("\n Menu Tambahan")
print(tabulate(menuTambahan, tablefmt="grid", headers=[
      "Pilihan", "Menu Tambahan", "Tarif"], numalign="center", stralign="center"))
print("\t")


def pesanan():

    # Percabangan Menu Makanan
    nama_pelanggan = input("Masukkan Nama Pelanggan: ")
    kode_makanan = input("Masukkan Kode Makanan: ")
    if kode_makanan == "1":
        Makanan = (menuMakanan[0][1])
        tarif_makanan = (hargaMakanan[0])
    elif kode_makanan == "2":
        Makanan = (menuMakanan[1][1])
        tarif_makanan = (hargaMakanan[1])
    elif kode_makanan == "3":
        Makanan = (menuMakanan[2][1])
        tarif_makanan = (hargaMakanan[2])
    elif kode_makanan == "4":
        Makanan = (menuMakanan[3][1])
        tarif_makanan = (hargaMakanan[3])
    elif kode_makanan == "5":
        Makanan = (menuMakanan[4][1])
        tarif_makanan = (hargaMakanan[4])
    elif kode_makanan == "6":
        Makanan = (menuMakanan[5][1])
        tarif_makanan = (hargaMakanan[5])
    elif kode_makanan == "7":
        Makanan = (menuMakanan[6][1])
        tarif_makanan = (hargaMakanan[6])
    elif kode_makanan == "8":
        Makanan = (menuMakanan[7][1])
        tarif_makanan = (hargaMakanan[7])
    elif kode_makanan == "9":
        Makanan = (menuMakanan[8][1])
        tarif_makanan = (hargaMakanan[8])
    elif kode_makanan == "10":
        Makanan = (menuMakanan[9][1])
        tarif_makanan = (hargaMakanan[9])
    elif kode_makanan == "11":
        Makanan = (menuMakanan[10][1])
        tarif_makanan = (hargaMakanan[10])
    else:
        print("Kode Yang Anda Masukkan Tidak Ada Di Daftar Menu!!")

    # Percabangan Menu Minuman
    kode_minuman = input("Masukkan Kode Minuman: ")
    if kode_minuman == "1":
        Minuman = (menuMinuman[0][1])
        tarif_Minuman = (hargaMinuman[0])
    elif kode_minuman == "2":
        Minuman = (menuMinuman[1][1])
        tarif_Minuman = (hargaMinuman[1])
    elif kode_minuman == "3":
        Minuman = (menuMinuman[2][1])
        tarif_Minuman = (hargaMinuman[2])
    elif kode_minuman == "4":
        Minuman = (menuMinuman[3][1])
        tarif_Minuman = (hargaMinuman[3])
    elif kode_minuman == "5":
        Minuman = (menuMinuman[4][1])
        tarif_Minuman = (hargaMinuman[4])
    elif kode_minuman == "6":
        Minuman = (menuMinuman[5][1])
        tarif_Minuman = (hargaMinuman[5])
    elif kode_minuman == "7":
        Minuman = (menuMinuman[6][1])
        tarif_Minuman = (hargaMinuman[6])
    elif kode_minuman == "8":
        Minuman = (menuMinuman[7][1])
        tarif_Minuman = (hargaMinuman[7])
    else:
        print("Kode Yang Anda Masukkan Tidak Ada Di Daftar Menu!!")

    # Percabangan Menu Tambahan
    kode_tambahan = input("Masukkan Kode Menu Tambahan: ")
    print()
    if kode_tambahan == "A":
        Tambahan = (menuTambahan[0][1])
        tarif_Tambahan = (hargaTambahan[0])
    elif kode_tambahan == "B":
        Tambahan = (menuTambahan[1][1])
        tarif_Tambahan = (hargaTambahan[1])
    elif kode_tambahan == "C":
        Tambahan = (menuTambahan[2][1])
        tarif_Tambahan = (hargaTambahan[2])
    elif kode_tambahan == "D":
        Tambahan = (menuTambahan[3][1])
        tarif_Tambahan = (hargaTambahan[3])
    else:
        print("Kode Yang Anda Masukkan Tidak Ada Di Daftar Menu!!")

    # Jumlah Bayar
    jumlah = tarif_makanan + tarif_Minuman + tarif_Tambahan

    # PPN
    ppn = int(jumlah * 0.11)

    # Total Yang harus Di Bayar
    Total_bayar = jumlah + ppn
    total_bayar = "Rp. {:,d}".format(Total_bayar)

    # Output Struk Pembayaran
    print("-------------------------------------------------")
    print("             STRUK PEMBAYARAN CAFE RELASI           ")
    print("-------------------------------------------------")
    print("Nama Pelanggan\t\t:", nama_pelanggan)
    print("Kode Makanan\t\t:", kode_makanan)
    print("Nama Makanan\t\t:", Makanan)
    print("Tarif Makanan\t\t: Rp.", format(tarif_makanan, ',d'))
    print("Kode Minuman\t\t:", kode_minuman)
    print("Nama Minuman\t\t:", Minuman)
    print("Tarif Minuman\t\t: Rp.", format(tarif_Minuman, ',d'))
    print("Kode Menu Tambahan\t:", kode_tambahan)
    print("Menu Tambahan\t\t:", Tambahan)
    print("Tarif Menu Tambahan\t: Rp. ", format(tarif_Tambahan, ',d'))
    print("Jumlah Bayar\t\t: Rp. ", format(jumlah, ',d'))
    print("PPN 11%\t\t\t: Rp. ", format(ppn, ',d'))
    print("Total Bayar\t\t: Rp. ", format(Total_bayar, ',d'))
    print("-------------------------------------------------")
    nama.append([nama_pelanggan, Makanan, Minuman, Tambahan, total_bayar])

pesanan()

# fungsi untuk menampilkan table output
def data():
    nomor_tabel = 1
    data_dengan_nomor = [[str(nomor_tabel)] + data for nomor_tabel,
                         data in enumerate(nama, start=1)]
    print(tabulate(data_dengan_nomor, headers=["No", "Nama Pelanggan", "Makanan",
          "Minuman", "Menu Tambahan", "Total Bayar"], tablefmt="fancy_grid"))

data()

# fungsi untuk mencari data pelanggan
def Pencarian(nama, val):
    hasil_pencarian = []
    for data in nama:
        if val.lower() in data[0].lower():
            hasil_pencarian.append(data)
    return hasil_pencarian

# fungsi untuk memilih menu
def menu_transaksi():
    print()
    print("-------------------------------------------------")
    print("                     MENU                        ")
    print("-------------------------------------------------")
    print("[1] Tambahkan Pesanan ")
    print("[2] Lihat Daftar Pembayaran ")
    print("[3] Cari Daftar Pembayaran ")
    print("[4] Exit")
    print("-------------------------------------------------")

    menu = int(input("Pilih Menu : "))
    print("\n")

    # Percabangan untuk memilih menu
    if menu == 1:
        pesanan()
    elif menu == 2:
        data()
    elif menu == 3:
        nomor_tabel = 1
        nama_pesanan = input("Nama Pelanggan: ")
        hasil_pencarian = Pencarian(nama, nama_pesanan)
        print(tabulate(hasil_pencarian, headers=[
              "Nama Pelanggan", "Makanan", "Minuman", "Menu Tambahan", "Total Bayar"], tablefmt="fancy_grid"))
        cari_pesanan.extend(hasil_pencarian)
    elif menu == 4:
        exit()
    else:
        print("Pilihan Yang Anda Pilih Tidak Ada Di Menu!!")


if __name__ == "__main__":
    while (True):
        menu_transaksi()
