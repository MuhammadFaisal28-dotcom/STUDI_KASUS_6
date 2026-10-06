import json
import os
from prettytable import PrettyTable

FILE_DATA = "nilai_mahasiswa.json"


def muat_data():
    if not os.path.exists(FILE_DATA):
        return []
    try:
        with open(FILE_DATA, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("file data tidak ada atau tidak bisa dibaca, memulai dari data kosong.")
        return []


def simpan_data(data):
    with open(FILE_DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def tampilkan_data():
    data = muat_data()
    if not data:
        print("\nBelum ada data nilai.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "NIM", "Nama", "Mata Kuliah", "Nilai"]
    tabel.align["Nama"] = "l"
    tabel.align["Mata Kuliah"] = "l"
    for i, d in enumerate(data, start=1):
        tabel.add_row([i, d["nim"], d["nama"], d["mata_kuliah"], d["nilai"]])

    print()
    print(tabel)
    rata = sum(d["nilai"] for d in data) / len(data)
    print(f"Jumlah data: {len(data)} | Rata-rata nilai: {rata:.2f}")


def input_nilai():
    while True:
        try:
            nilai = float(input("Nilai (0-100)   : "))
            if 0 <= nilai <= 100:
                return nilai
            print("Nilai harus antara 0 sampai 100.")
        except ValueError:
            print("Input harus berupa angka.")


def input_teks(label):
    while True:
        teks = input(label).strip()
        if teks:
            return teks
        print("Input tidak boleh kosong.")


def tambah_data():
    print("\n--- Tambah Nilai Baru ---")
    nim = input_teks("NIM             : ")
    nama = input_teks("Nama            : ")
    matkul = input_teks("Mata Kuliah    : ")
    nilai = input_nilai()

    data = muat_data()
    data.append({"nim": nim, "nama": nama, "mata_kuliah": matkul, "nilai": nilai})
    simpan_data(data)
    print("Data berhasil ditambahkan dan disimpan ke file.")


def baca_nilai_mahasiswa():
    print("\n--- Baca Nilai Per Mahasiswa ---")
    kata = input_teks("Masukkan NIM atau nama: ").lower()

    data = muat_data()
    hasil = [
        d for d in data
        if kata == d["nim"].lower() or kata in d["nama"].lower()
    ]

    if not hasil:
        print("Data mahasiswa tidak ditemukan.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["NIM", "Nama", "Mata Kuliah", "Nilai"]
    tabel.align["Nama"] = "l"
    tabel.align["Mata Kuliah"] = "l"
    for d in hasil:
        tabel.add_row([d["nim"], d["nama"], d["mata_kuliah"], d["nilai"]])

    print()
    print(tabel)
    rata = sum(d["nilai"] for d in hasil) / len(hasil)
    print(f"Jumlah riwayat: {len(hasil)} | Rata-rata nilai: {rata:.2f}")


def main():
    while True:
        print("\n=== SISTEM PENCATATAN NILAI MAHASISWA ===")
        print("1. Lihat semua nilai")
        print("2. Baca nilai per mahasiswa")
        print("3. Tambah nilai baru")
        print("4. Keluar")
        print("\n=========================================")
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            baca_nilai_mahasiswa()
        elif pilihan == "3":
            tambah_data()
        elif pilihan == "4":
            print("Terima kasih telah memakai program ini.")
            break
        else:
            print("Pilihan tidak valid, silahkan pilih menu yang tersedia.")


if __name__ == "__main__":
    main()