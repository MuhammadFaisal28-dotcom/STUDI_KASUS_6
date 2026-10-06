# STUDI_KASUS_6-SISTEM_PENCACATAN_NILAI_MAHASISWA

## Biodata Mahasiswa
* **Nama** : MUH.FAISAL 
* **NIM** : 2609116075
* **Kelas** : B
* **Topik** : Studi Kasus 6 (Sistem Pencatatan Nilai Mahasiswa)

  ---

## Deskripsi Program
Program ini merupakan aplikasi berbasis konsol (CLI) menggunakan bahasa pemrograman Python untuk mengelola dan mencatat riwayat nilai akademik mahasiswa. Data nilai disimpan secara permanen ke dalam berkas JSON (`nilai_mahasiswa.json`). Tampilan data disajikan secara rapi dan terstruktur dalam bentuk tabel menggunakan pustaka `prettytable`, dilengkapi perhitungan statistik seperti jumlah data dan nilai rata-rata.

---

## Struktur Penyimpanan Data (`nilai_mahasiswa.json`)
Data disimpan dalam format array of objects (list of dictionaries) pada file `nilai_mahasiswa.json`:
```json

[
    {
        "nim": "023",
        "nama": "reja",
        "mata_kuliah": "matdis",
        "nilai": 100.0
    },
    {
        "nim": "999",
        "nama": "ical",
        "mata_kuliah": "ksi",
        "nilai": 90.0
    }
]

```
---

## Fitur Utama Program
1. **Lihat Semua Nilai (Menu 1)**:
   
   <img width="408" height="168" alt="Cuplikan layar 2026-10-06 205110" src="https://github.com/user-attachments/assets/ed7f1142-a5a9-49f8-9361-271beebcf6b2" />

   - Menampilkan seluruh daftar mahasiswa, NIM, mata kuliah, dan nilai yang tercatat dalam tabel rapi.
   - Menghitung dan menampilkan total jumlah data dan nilai rata-rata secara otomatis.
2. **Baca Nilai per Mahasiswa (Menu 2)**:
   

   <img width="477" height="278" alt="Cuplikan layar 2026-10-06 205302" src="https://github.com/user-attachments/assets/0350987f-f680-41b2-9359-53ca96780e46" />

   -  Melakukan pencarian berdasarkan NIM (pencocokan penuh) atau Nama (pencocokan sebagian/substring, *case-insensitive*).
   - Menampilkan tabel riwayat mata kuliah yang diambil mahasiswa tersebut beserta nilai rata-ratanya.
3. **Tambah Nilai Baru (Menu 3)**:
   

   <img width="517" height="167" alt="image" src="https://github.com/user-attachments/assets/0a7f49bd-20d6-4c6a-8fe2-24cd0f494cce" />

   
   - Menambahkan catatan nilai baru (NIM, Nama, Mata Kuliah, dan Nilai).
   - Data otomatis disimpan ke berkas `nilai_mahasiswa.json`.
4. **Penyimpanan Permanen (JSON Persistence)**:
   

   <img width="597" height="506" alt="Cuplikan layar 2026-10-06 205513" src="https://github.com/user-attachments/assets/474b98f6-922d-46f8-885d-2f11bd8369f7" />

   - Data otomatis dimuat saat program berjalan dan langsung diperbarui ke disk saat penambahan data berhasil.
   - Dilengkapi *error handling* jika file belum ada atau terjadi kerusakan format JSON.
6. **Validasi Input Ketat**:
   - Memastikan teks NIM, Nama, dan Mata Kuliah tidak kosong.
   - Memastikan nilai berupa angka numerik (*handling* `ValueError`).
   - Memastikan rentang nilai berada di antara 0 sampai 100.

---

## Penjelasan Struktur Kode Program (`index.py`)

### 1. Pustaka / Modul yang Digunakan
* `import json`: Untuk membaca (*load*) dan menyimpan (*dump*) data list ke format JSON.
* `import os`: Untuk memeriksa keberadaan berkas `nilai_mahasiswa.json` melalui `os.path.exists`.
* `from prettytable import PrettyTable`: Untuk memformat keluaran data dalam bentuk tabel teks di terminal.

<img width="453" height="65" alt="Cuplikan layar 2026-10-06 205617" src="https://github.com/user-attachments/assets/0362052f-176d-4461-a9aa-e4e0cb8318ab" />

### 2. Fungsi-Fungsi Program

#### `muat_data()`
Membaca berkas `nilai_mahasiswa.json` dengan enkoding `utf-8`. Jika berkas belum ditemukan atau isi berkas tidak valid, fungsi akan menangani eksepsi `(json.JSONDecodeError, OSError)` dan mengembalikan list kosong `[]`.


<img width="895" height="261" alt="Cuplikan layar 2026-10-06 205748" src="https://github.com/user-attachments/assets/b2881598-21a6-44f0-a2bc-2b29392d1fdd" />

#### `simpan_data(data)`
Menyimpan struktur data list ke berkas `nilai_mahasiswa.json` dengan format `indent=4` dan `ensure_ascii=False` agar file tertata rapi dan mudah dibaca.

<img width="602" height="100" alt="Cuplikan layar 2026-10-06 205811" src="https://github.com/user-attachments/assets/a54ca315-b3d4-4117-a00c-e335ec3a6637" />

#### `tampilkan_data()`
Memuat seluruh data dari berkas, lalu menampilkannya dalam tabel `PrettyTable` dengan kolom `No`, `NIM`, `Nama`, `Mata Kuliah`, dan `Nilai`. Jika data tersedia, fungsi juga menghitung nilai rata-rata seluruh data:
$$\text{Rata-rata} = \frac{\sum \text{Nilai}}{n}$$

<img width="827" height="462" alt="Cuplikan layar 2026-10-06 205840" src="https://github.com/user-attachments/assets/12442864-bf88-4230-a375-3fee504428ae" />

#### `input_nilai()`
Fungsi pembantu (*helper*) untuk meminta masukan nilai dari pengguna. Fungsi ini mengulang permintaan input hingga pengguna memasukkan angka valid dalam rentang $0 \le \text{nilai} \le 100$.


<img width="632" height="257" alt="Cuplikan layar 2026-10-06 205909" src="https://github.com/user-attachments/assets/d0b606a7-39a2-4152-9057-17c6711d0cda" />

#### `input_teks(label)`
Fungsi pembantu untuk meminta input teks dengan validasi tidak boleh berupa string kosong atau hanya spasi (`.strip()`).


<img width="533" height="207" alt="Cuplikan layar 2026-10-06 205928" src="https://github.com/user-attachments/assets/8b72932c-400d-49ea-a2ec-6999963bfded" />

#### `tambah_data()`
Mengumpulkan input NIM, Nama, Mata Kuliah, dan Nilai dari pengguna, menambahkan dictionary baru ke dalam list data, lalu memanggil `simpan_data(data)`.


<img width="887" height="308" alt="Cuplikan layar 2026-10-06 210024" src="https://github.com/user-attachments/assets/ab1d2916-1e97-4e6b-b066-b309e864b656" />

#### `baca_nilai_mahasiswa()`
Meminta kata kunci pencarian (NIM atau Nama). Melakukan penyaringan (*filter*) dengan membandingkan kata kunci terhadap NIM atau nama mahasiswa (huruf kecil / *lowercase*). Menampilkan hasil filter dalam tabel `PrettyTable` beserta total riwayat dan rata-rata nilai mahasiswa yang dicari.


<img width="778" height="625" alt="Cuplikan layar 2026-10-06 210104" src="https://github.com/user-attachments/assets/922e80c9-8f23-40da-895f-b3c34b1187d0" />

#### `main()`
Fungsi alur utama (*main loop*) yang menyajikan menu interaktif pilihan 1 sampai 4:
- `1`: Lihat semua nilai
- `2`: Baca nilai per mahasiswa
- `3`: Tambah nilai baru
- `4`: Keluar program


  <img width="791" height="623" alt="Cuplikan layar 2026-10-06 210204" src="https://github.com/user-attachments/assets/77d9a73f-9c43-4a80-a67a-fc8929d2f367" />

  ---
