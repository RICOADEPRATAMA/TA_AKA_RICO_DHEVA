# TUGAS BESAR ANALISIS KOMPLEKSITAS ALGORITMA
# RICO ADE PRATAMA			(2311102138)
# DHEVA DEWA SEPTIANTONI	(2311102324)
# KELAS : S1IF-11-01

# PROGRAM PENYEWAAN PERALATAN SEPAK BOLA
import time
import sys
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

class peralatan:
    def __init__(self, id, nama, tersedia, harga):
        self.id = id
        self.nama = nama
        self.tersedia = tersedia
        self.harga = harga

class sewa:
    def __init__(self, id_peralatan, nama_peralatan, tanggal_sewa, tanggal_kembali, jumlah, total_harga, sudah_dikembalikan):
        self.id_peralatan = id_peralatan
        self.nama_peralatan = nama_peralatan
        self.tanggal_sewa = tanggal_sewa
        self.tanggal_kembali = tanggal_kembali
        self.jumlah = jumlah
        self.total_harga = total_harga
        self.sudah_dikembalikan = sudah_dikembalikan

peralatan_tersedia = [
    peralatan(101, "Bola Sepak", 8, 30000),
    peralatan(102, "Bola Futsal", 6, 30000),
    peralatan(103, "Sepatu Sepak Bola", 23, 50000),
    peralatan(104, "Sepatu Futsal", 14, 50000),
    peralatan(105, "Jersey Kaos Lengan Pendek (Warna Merah)", 24, 10000),
    peralatan(106, "Jersey Kaos Lengan Pendek (Warna Putih)", 24, 10000),
    peralatan(107, "Jersey Kaos Lengan Pendek (Warna Hitam)", 21, 10000),
    peralatan(108, "Jersey Kaos Lengan Panjang (Warna Merah)", 14, 11000),
    peralatan(109, "Jersey Kaos Lengan Panjang (Warna Putih)", 14, 11000),
    peralatan(110, "Jersey Kaos Lengan Panjang (Warna Hitam)", 11, 11000),
    peralatan(111, "Celana Pendek (Shorts Hitam)", 24, 5000),
    peralatan(112, "Kaos Kaki (Soccer Socks)", 21, 5000),
    peralatan(113, "Dekker (Pelindung Tulang Kering/Shin Guard)", 30, 5000),
    peralatan(114, "Sarung Tangan Kiper", 11, 20000),
    peralatan(115, "Rompi Latihan (Warna Putih)", 21, 5000),
    peralatan(116, "Rompi Latihan (Warna Hijau)", 21, 5000),
    peralatan(117, "Cone Latihan", 12, 5000),
    peralatan(118, "Gawang Portabel", 8, 100000),
    peralatan(119, "Pompa Bola", 6, 15000),
    peralatan(120, "Topeng Pelindung Kepala", 1, 20000),
    peralatan(121, "Peluit", 9, 5000),
    peralatan(122, "Setelan Baju Wasit", 5, 25000)
]

riwayat_sewa = []

def tampilkan_peralatan_tersedia():
    print("Daftar Peralatan yang Tersedia:")
    print("+-----+------------------------------------------------------------+------------------+--------------------+")
    print("| ID  | Nama Peralatan                                             | Jumlah Tersedia  | Harga Sewa (Rp)    |")
    print("+-----+------------------------------------------------------------+------------------+--------------------+")
    for eq in peralatan_tersedia:
        if eq.tersedia > 0:
            print(f"| {eq.id:<3} | {eq.nama:<58} | {eq.tersedia:<16} | Rp {eq.harga:<15.2f} |")
    print("+-----+------------------------------------------------------------+------------------+--------------------+")

def search_peralatan_nama_rekursif(peralatan_tersedia, nama, index=0):
    if index >= len(peralatan_tersedia):
        return False
    eq = peralatan_tersedia[index]
    found = nama.lower() in eq.nama.lower()
    return found or search_peralatan_nama_rekursif(peralatan_tersedia, nama, index + 1)

def search_peralatan_and_visualize(nama, previous_times=None):
    if previous_times is None:
        previous_times = {'Iteratif': {}, 'Rekursif': {}}

    dataset_sizes = [100, 500, 1000, 5000, 10000, 20000]
    waktu_iteratif = []
    waktu_rekursif = []

    found_iterative = False
    found_recursive = False

    waktu_iteratif_mulai = time.time()
    found_iterative = any(nama.lower() in eq.nama.lower() for eq in peralatan_tersedia)
    waktu_iteratif_berakhir = time.time()

    waktu_rekursif_mulai = time.time()
    found_recursive = search_peralatan_nama_rekursif(peralatan_tersedia, nama)
    waktu_rekursif_berakhir = time.time()

    print(f"\nHasil Pencarian untuk '{nama}':")
    if found_iterative or found_recursive:
        print("Peralatan ditemukan!")
        # Display table in the desired format
        print("+-----+------------------------------------------------------------+------------------+--------------------+")
        print("| ID  | Nama Peralatan                                             | Jumlah Tersedia  | Harga Sewa (Rp)    |")
        print("+-----+------------------------------------------------------------+------------------+--------------------+")
        for eq in peralatan_tersedia:
            if nama.lower() in eq.nama.lower():
                print(f"| {eq.id:<3} | {eq.nama:<58} | {eq.tersedia:<16} | Rp {eq.harga:<15.2f} |")
        print("+-----+------------------------------------------------------------+------------------+--------------------+")
    else:
        print("Peralatan tidak ditemukan!")
    # Store execution times
    previous_times['Iteratif'][nama] = waktu_iteratif_berakhir - waktu_iteratif_mulai
    previous_times['Rekursif'][nama] = waktu_rekursif_berakhir - waktu_rekursif_mulai

    print("\nWaktu eksekusi (Iteratif):")
    for item, time_taken in previous_times['Iteratif'].items():
        print(f"- {item}: {time_taken:.6f} detik")

    print("\nWaktu eksekusi (Rekursif):")
    for item, time_taken in previous_times['Rekursif'].items():
        print(f"- {item}: {time_taken:.6f} detik")

    # Uji waktu berdasarkan ukuran dataset
    for size in dataset_sizes:
        temp_list = peralatan_tersedia * (size // len(peralatan_tersedia))

        # Pencarian Iteratif
        waktu_iteratif_mulai = time.time()
        any(nama.lower() in eq.nama.lower() for eq in temp_list)
        waktu_iteratif_berakhir = time.time()

        # Pencarian Rekursif
        waktu_rekursif_mulai = time.time()
        search_peralatan_nama_rekursif(temp_list, nama)
        waktu_rekursif_berakhir = time.time()

        waktu_iteratif.append(waktu_iteratif_berakhir - waktu_iteratif_mulai)
        waktu_rekursif.append(waktu_rekursif_berakhir - waktu_rekursif_mulai)

    # Plot perbandingan waktu
    plt.figure(figsize=(10, 6))
    plt.plot(dataset_sizes, waktu_iteratif, label="Iteratif", color='red', marker="o", linestyle="-", linewidth=2)
    plt.plot(dataset_sizes, waktu_rekursif, label="Rekursif", color='blue', marker="o", linestyle="-", linewidth=2)
    plt.title("Perbandingan Waktu Eksekusi Pencarian")
    plt.xlabel("Ukuran Dataset")
    plt.ylabel("Waktu (detik)")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def display_peralatan_table(peralatan_tersedia):
    """Menampilkan tabel peralatan."""
    print("Daftar Peralatan:")
    print("+-----+------------------------------------------------------------+------------------+--------------------+")
    print("| ID  | Nama Peralatan                                             | Jumlah Tersedia  | Harga Sewa (Rp)    |")
    print("+-----+------------------------------------------------------------+------------------+--------------------+")
    for eq in peralatan_tersedia:
        print(f"| {eq.id:<3} | {eq.nama:<58} | {eq.tersedia:<16} | Rp {eq.harga:<15.2f} |")
    print("+-----+------------------------------------------------------------+------------------+--------------------+")

def sort_peralatan(by, order):
    global peralatan_tersedia 
    if by == "id":
        peralatan_tersedia.sort(key=lambda x: x.id, reverse=(order == "desc")) 
    elif by == "nama":
        peralatan_tersedia.sort(key=lambda x: x.nama, reverse=(order == "desc")) 
    elif by == "harga":  
        peralatan_tersedia.sort(key=lambda x: x.harga, reverse=(order == "desc"))
    elif by == "tersedia":  
        peralatan_tersedia.sort(key=lambda x: x.tersedia, reverse=(order == "desc"))  
    else:
        print("Kriteria urutkan tidak valid.")
        return

    dataset_sizes = [100, 500, 1000, 5000, 10000, 20000]
    waktu_iteratif = []
    waktu_rekursif = []
    reverse = order == 'desc'
    display_peralatan_table(peralatan_tersedia)

    # Iterative Sort
    waktu_iteratif_mulai = time.time()
    waktu_iteratif_berakhir = time.time()

    # Recursive Sort
    def quicksort_recursive(arr, by, reverse=False):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        less = [x for x in arr[1:] if (getattr(x, by) <= getattr(pivot, by)) != reverse]
        greater = [x for x in arr[1:] if (getattr(x, by) > getattr(pivot, by)) != reverse]
        
        result = []
        stack = [(less, by, reverse), (greater, by, reverse)] 
        while stack:
            sub_list, by, reverse = stack.pop()
            if len(sub_list) <= 1:
                result.extend(sub_list)
            else:
                pivot = sub_list[0]
                less = [x for x in sub_list[1:] if (getattr(x, by) <= getattr(pivot, by)) != reverse]
                greater = [x for x in sub_list[1:] if (getattr(x, by) > getattr(pivot, by)) != reverse]
                stack.append((greater, by, reverse))
                stack.append((less, by, reverse))

        return result + [pivot] 
    
    waktu_rekursif_mulai = time.time()
    peralatan_tersedia = quicksort_recursive(peralatan_tersedia, by, reverse)
    waktu_rekursif_berakhir = time.time()

    print(f"Waktu Eksekusi (Iteratif): {waktu_iteratif_berakhir - waktu_iteratif_mulai:.6f} detik")
    print(f"Waktu Eksekusi (Rekursif): {waktu_rekursif_berakhir - waktu_rekursif_mulai:.6f} detik")

    # Plot waktu berdasarkan ukuran dataset
    for size in dataset_sizes:
        temp_list = peralatan_tersedia * (size // len(peralatan_tersedia))

        # Iterative Sorting Time
        waktu_iteratif_mulai = time.time()
        temp_list.sort(key=lambda x: getattr(x, by), reverse=reverse) 
        waktu_iteratif_berakhir = time.time()

        # Recursive Sorting Time
        waktu_rekursif_mulai = time.time()
        quicksort_recursive(temp_list, by, reverse)
        waktu_rekursif_berakhir = time.time()

        waktu_iteratif.append(waktu_iteratif_berakhir - waktu_iteratif_mulai)
        waktu_rekursif.append(waktu_rekursif_berakhir - waktu_rekursif_mulai)

    plt.figure(figsize=(10, 6))
    plt.plot(dataset_sizes, waktu_iteratif, label="Iteratif", color='red', marker="o", linestyle="-", linewidth=2)
    plt.plot(dataset_sizes, waktu_rekursif, label="Rekursif", color='blue', marker="o", linestyle="-", linewidth=2)
    plt.title("Perbandingan Waktu Eksekusi Sorting")
    plt.xlabel("Ukuran Dataset")
    plt.ylabel("Waktu (detik)")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def rent_peralatan(id_peralatan, jumlah):
    if jumlah <= 0:
        print("Jumlah sewa harus lebih dari 0.")
        return
    for eq in peralatan_tersedia:
        if eq.id == id_peralatan and eq.tersedia >= jumlah:
            eq.tersedia -= jumlah
            total_harga = jumlah * eq.harga
            new_sewa = sewa(eq.id, eq.nama, time.time(), 0, jumlah, total_harga, False)
            riwayat_sewa.append(new_sewa)
            print(f"Anda telah menyewa {jumlah} unit {eq.nama} (ID: {eq.id}) dengan total harga Rp{total_harga} pada {datetime.fromtimestamp(new_sewa.tanggal_sewa)}")
            return
    print("Peralatan tidak tersedia dalam jumlah yang diminta atau ID tidak valid.")

def return_peralatan(id_peralatan, jumlah):
    for sewa in riwayat_sewa:
        if sewa.id_peralatan == id_peralatan and not sewa.sudah_dikembalikan:
            if sewa.jumlah < jumlah:
                print("Jumlah pengembalian melebihi jumlah yang disewa.")
                return
            sewa.jumlah -= jumlah
            if sewa.jumlah == 0:
                sewa.sudah_dikembalikan = True
            for eq in peralatan_tersedia:
                if eq.id == id_peralatan:
                    eq.tersedia += jumlah
            print(f"Peralatan {sewa.nama_peralatan} (ID: {id_peralatan}) sebanyak {jumlah} unit berhasil dikembalikan.")
            return
    print("Tidak ada penyewaan peralatan yang sesuai untuk pengembalian ini.")

def display_sewa_history():
    print("Histori Penyewaan:")
    for sewa in riwayat_sewa:
        status = "Dikembalikan" if sewa.sudah_dikembalikan else "Belum Dikembalikan"
        print(f"- {sewa.nama_peralatan} (ID: {sewa.id_peralatan}, Jumlah: {sewa.jumlah}, Total Harga: Rp{sewa.total_harga}, Disewa pada: {datetime.fromtimestamp(sewa.tanggal_sewa)}, Status: {status})")

# Tambahkan validasi input pada fungsi main
def main():
    previous_search_times = None
    while True:
        try:
            print("\n===================================================================")
            print(">>>>>>>>>>>>>>> Menu Penyewaan Peralatan Sepak Bola <<<<<<<<<<<<<<<")
            print("===================================================================")
            print("1. Tampilkan peralatan yang tersedia -------------------- (•⊙ω⊙•)")
            print("2. Cari peralatan ------------------------- (Perbandingan Eksekusi)")
            print("3. Urutkan peralatan ---------------------- (Perbandingan Eksekusi)")
            print("4. Sewa peralatan ---------------------------------------- (๑>ᴗ<๑)")
            print("5. Pengembalian peralatan -------------------------------- (•̀‿⊹ )")
            print("6. Tampilkan histori penyewaan --------------------------- (☞ﾟヮﾟ)☞")
            print("7. Keluar ------------------------------------------------ (✖╭╮✖)")
            print("===================================================================")
            pilih = int(input("Masukkan pilihan: "))
        except ValueError:
            print("Input tidak valid! Silakan masukkan angka.")
            continue

        if pilih == 1:
            tampilkan_peralatan_tersedia() 
        elif pilih == 2:
            search_number = 1 
            while True:
                nama = input(f"Pencarian {search_number} (jika tidak maka ketik 'selesai')\nMasukkan nama peralatan yang ingin dicari: ")
                if nama.lower() == "selesai":
                    break  
                previous_search_times = search_peralatan_and_visualize(nama, previous_search_times)  
                search_number += 1  
        elif pilih == 3:
            by = input("Urutkan berdasarkan (ID/nama/harga/tersedia): ").lower()
            order = input("Urutan (asc/desc): ").lower()
            sort_peralatan(by, order)
        elif pilih == 4:
            try:
                id = int(input("Masukkan ID peralatan yang ingin disewa: "))
                qty = int(input("Masukkan jumlah yang ingin disewa: "))
                rent_peralatan(id, qty)
            except ValueError:
                print("Input tidak valid! ID dan jumlah harus berupa angka.")
        elif pilih == 5:
            try:
                id = int(input("Masukkan ID peralatan yang ingin dikembalikan: "))
                qty = int(input("Masukkan jumlah yang ingin dikembalikan: "))
                return_peralatan(id, qty)
            except ValueError:
                print("Input tidak valid! ID dan jumlah harus berupa angka.")
        elif pilih == 6:
            display_sewa_history()
        elif pilih == 7:
            print("Terima kasih telah menggunakan layanan penyewaan peralatan olahraga!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()