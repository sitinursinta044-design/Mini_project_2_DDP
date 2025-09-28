# Nama    : Siti Nursinta
# Nim     : 2509116087
# Kelas   : Information System C 2025
# program : Mini project 2 (Praktikum DDP)
# Tema    : Sistem Manajemen Proyek Digital

from prettytable import PrettyTable
import pwinput

data_proyek = []
users = {
    "admin": {"password": "123", "role": "admin"},
    "freelancer": {"password": "abc", "role": "user"}
}

def input_proyek():
    nama_proyek = []
    harga_proyek = []
    kesulitan_proyek = []

    while True:
        try:
            jumlah = int(input("Masukkan jumlah proyek (2-5): "))
            if 2 <= jumlah <= 5:
                break
            else:
                print("Jumlah proyek harus antara 2 sampai 5.")
        except ValueError:
            print("Jumlah proyek tidak valid!")

    for i in range(jumlah):
        print(f"\n---------------------- Input Proyek {i+1} -----------------------")
        try:
            nama = input(f"Masukkan nama proyek {i+1}: ")

            while True:
                try:
                    harga = float(input(f"Masukkan harga proyek {i+1}: "))
                    if harga <= 0:
                        print("Estimasi harga harus lebih dari 0!")
                    else:
                        break
                except ValueError:
                    print("Estimasi harga yang dimasukan tidak valid!")

            while True:
                kesulitan = input(f"Masukkan tingkat kesulitan proyek {i+1} (mudah/sedang/sulit): ").lower()
                if kesulitan in ["mudah", "sedang", "sulit"]:
                    break
                else:
                    print("Tingkat kesulitan proyek tidak valid!")

            nama_proyek.append(nama)
            harga_proyek.append(harga)
            kesulitan_proyek.append(kesulitan)
            print("-- Data proyek berhasil disimpan --")

        except Exception as e:
            print(f"Terjadi error saat input proyek {i+1}: {e}")

    data_proyek = []
    for i in range(len(nama_proyek)):
        proyek = {
            "id": i+1,
            "detail": (nama_proyek[i], harga_proyek[i], kesulitan_proyek[i])
        }
        data_proyek.append(proyek)

    return data_proyek

def tampilkan_proyek(data_proyek):
    print("\n========================== List Proyek ==========================")

    if not data_proyek:
        print("Belum ada proyek yang dimasukkan.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Nama Proyek", "Estimasi Harga", "Tingkat Kesulitan"]

        for p in data_proyek:
            nama, harga, sulit = p["detail"]
            table.add_row([p["id"], nama, f"Rp {harga:,.0f}", sulit])

        print(table)

    print("\n=================================================================")
def edit_proyek(data_proyek):
    tampilkan_proyek(data_proyek)
    try:
        idx = int(input("Masukkan ID proyek yang ingin diupdate: "))
        proyek = None
        for p in data_proyek:
            if p["id"] == idx:
                proyek = p
                break

        if proyek:
            nama = input("Masukkan nama proyek baru: ")
            while True:
                try:
                    harga = float(input("Masukkan estimasi harga baru: "))
                    if harga > 0:
                        break
                    else:
                        print("Harga harus lebih dari 0!")
                except ValueError:
                    print("Input harga tidak valid!")

            while True:
                kesulitan = input("Masukkan tingkat kesulitan baru (mudah/sedang/sulit): ").lower()
                if kesulitan in ["mudah", "sedang", "sulit"]:
                    break
                else:
                    print("Input tingkat kesulitan tidak valid!")

            proyek["detail"] = (nama, harga, kesulitan)
            print("Proyek berhasil diupdate!")
        else:
            print("ID proyek tidak ditemukan.")
    except ValueError:
        print("Input tidak valid!")

def hapus_proyek(data_proyek):
    tampilkan_proyek(data_proyek)
    try:
        idx = int(input("Masukkan ID proyek yang ingin dihapus: "))
        proyek = None
        for p in data_proyek:
            if p["id"] == idx:
                proyek = p
                break

        if proyek:
            data_proyek.remove(proyek)
            for i, p in enumerate(data_proyek):
                p["id"] = i + 1
            print("Proyek berhasil dihapus!")
        else:
            print("ID proyek tidak ditemukan.")
    except ValueError:
        print("Input tidak valid!")

def rekomendasi_proyek(data_proyek):
    rekomendasi = None
    harga_tertinggi = 0

    standar_harga = {"mudah": 1000000, "sedang": 2000000, "sulit": 3000000}

    for p in data_proyek:
        nama, harga, kesulitan = p["detail"]
        min_harga = standar_harga.get(kesulitan, 0)

        if harga >= min_harga and harga > harga_tertinggi:
            rekomendasi = p
            harga_tertinggi = harga

    print("\nHasil Rekomendasi Proyek : ")
    if rekomendasi:
        nama, harga, sulit = rekomendasi["detail"]
        print("Nama Proyek       :", nama)
        print("Estimasi Harga    :", harga)
        print("Tingkat Kesulitan :", sulit)
    else:
        print("Tidak ada proyek yang memenuhi kriteria.")

def login():
    print("=== Login Sistem Manajemen Proyek Digital ===")
    username = input("Username: ")
    password = pwinput.pwinput("Password: ")

    if username in users and users[username]["password"] == password:
        print(f"Login berhasil. Selamat datang, {username}!")
        return users[username]["role"]
    else:
        print("Login gagal! Username atau password salah.")
        return None
    
role = None
data_proyek = []
pilihan = -1

while pilihan != 0:
    if not role:
        role = login()
        if not role:
            keluar = input("Keluar dari program? (y/n): ").lower()
            if keluar == "y":
                print("Program ditutup...")
                break
            else:
                continue

    print("")
    print("=================================================================")
    print("=              Sistem Manajemen Proyek Digital                  =")
    print("=================================================================")
    if role == "admin":
        print("1. Tambah Proyek (Create)")
        print("2. Lihat Proyek (Read)")
        print("3. Edit Proyek (Update)")
        print("4. Hapus Proyek (Delete)")
        print("5. Rekomendasi Proyek")
    else: 
        print("1. Lihat Daftar Proyek (Read)")
        print("2. Rekomendasi Proyek")
    print("9. Logout")
    print("0. Keluar Program")
    print("\n=================================================================")

    pilihan = int(input("Pilih menu: "))

    if pilihan == 1 and role == "admin":
        data_proyek = input_proyek()
    elif pilihan == 1 and role == "user":
        tampilkan_proyek(data_proyek)
    elif pilihan == 2 and role == "admin":
        tampilkan_proyek(data_proyek)
    elif pilihan == 2 and role == "user":
        rekomendasi_proyek(data_proyek)
    elif pilihan == 5 and role == "admin":
        rekomendasi_proyek(data_proyek)
    elif pilihan == 3 and role == "admin":
        edit_proyek(data_proyek)
    elif pilihan == 4 and role == "admin":
        hapus_proyek(data_proyek)
    elif pilihan == 9:
        print("Anda berhasil logout.")
        role = None
    elif pilihan == 0:
        print("Program ditutup...")
    else:
        print("Pilihan tidak valid!")
