
# Sistem Manajemen Proyek Digital

Program ini digunakan untuk menentukan apakah sebuah ide bisnis layak untuk dijalankan. Dalam konteks freelance digital, program ini bisa menjadi alat pribadi seorang freelancer untuk menilai apakah sebuah proyek tertentu memiliki potensi keuntungan berdasarkan estimasi biaya dan tingkat kesulitannya.

## Flowchart

![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/flowchart.jpg)


## Screenshot Hasil Program

Berikut adalah hasil pengujian output program secara keseluruhan beserta penjelasannya : 

1. Halaman Login

Saat program pertama kali dijalankan, pengguna akan diarahkan ke halaman login. Di sini, pengguna diminta memasukkan username dan password. Password tidak ditampilkan secara terbuka karena menggunakan library pwinput, sehingga lebih aman.

![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/login.png)

- Terdapat 2 role, yaitu admin dan user / freelancer. admin bisa melakukan operasi CRUD, sedangkan untuk freelancer / user hanya dapat melihat list proyek dan rekomendasi proyek yang bisa diambil. 
- Untuk proses login, jika data sesuai dengan akun yang ada dalam sistem (admin/123 atau freelancer/abc), maka login berhasil.
- Jika salah, pengguna akan mendapatkan pesan error dan harus mencoba lagi.

2. Tampilan Jika Login Gagal

![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/login_gagal.png)

Jika pengguna salah mengetikkan username atau password, program akan memberikan peringatan:

"Login gagal. Username atau password salah."

Pengguna tetap dapat mencoba login kembali atau keluar program dengan memilih opsi y/n pada pertanyaan apakah ingin keluar dari program.

3. Menu Utama (Admin)

![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/menu_admin.png)

Admin memiliki hak akses penuh terhadap seluruh fitur program, termasuk CRUD (Create, Read, Update, Delete) dan fitur Rekomendasi Proyek. Menu ditampilkan dengan daftar pilihan angka, di mana admin dapat menambahkan proyek baru, melihat daftar proyek, mengubah data proyek, menghapus proyek, melihat rekomendasi, logout, atau keluar dari program.

4. Menu Utama (Freelancer / User)

![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/menu_user.png)

Role freelancer hanya memiliki hak akses terbatas, yaitu:

- Melihat daftar proyek (Read)
- Melihat rekomendasi proyek

Dengan demikian, freelancer tidak bisa melakukan perubahan pada data proyek (tidak bisa menambah, mengedit, maupun menghapus). Ini untuk membedakan batasan akses admin dan user.

5. Tambah Proyek (Create)

![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/create.png)

Fitur ini memungkinkan admin menambahkan proyek baru dengan mengisi jumlah data yang ingin diinputkan (2 sampai 5 proyek), kemudian akan dilakukan looping untuk mengisi :

- Nama proyek
- Estimasi harga (Rp)
- Tingkat kesulitan (mudah/sedang/sulit)

Data yang valid akan langsung tersimpan dalam list data_proyek. Program juga sudah memiliki validasi input agar data sesuai format, misalnya harga harus berupa angka, dan tingkat kesulitan hanya bisa diisi dengan salah satu dari tiga pilihan.

6. Lihat Proyek (Read)

Tampilan read dari admin : 
![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/read.png)
Tampilan read dari freelancer / user : 
![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/read_user.png)

Fitur ini menampilkan seluruh proyek yang sudah ada, menggunakan library PrettyTable agar lebih rapi. Kolom yang ditampilkan adalah:

- ID: Nomor urut proyek
- Nama Proyek: Judul atau nama proyek
- Estimasi Harga: Biaya yang ditawarkan untuk proyek tersebut
- Tingkat Kesulitan: Mudah, Sedang, atau Sulit

Jika belum ada proyek, maka akan muncul pesan bahwa daftar masih kosong.

7. Edit Proyek (Update)

![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/update.png)

Admin dapat memperbarui data proyek berdasarkan ID. Proses ini meliputi:

- Mengubah nama proyek
- Mengubah estimasi harga
- Mengubah tingkat kesulitan

8. Hapus Proyek (Delete)

![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/delete.png)

Admin dapat menghapus proyek berdasarkan ID. Setelah proyek dihapus, data proyek tersebut hilang dari list. Sistem kemudian akan otomatis menyesuaikan ulang ID proyek agar tetap berurutan dan konsisten.

9. Rekomendasi Proyek

Tampilan rekomendasi proyek dari admin : 
![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/rekomendasi.png)
Tampilan rekomendasi proyek dari freelancer / user : 
![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/rekomendasi_user.png)

Fitur ini menampilkan rekomendasi proyek dengan harga tertinggi sesuai standar minimum dari tingkat kesulitannya:

- Proyek mudah → minimal Rp 1.000.000
- Proyek sedang → minimal Rp 2.000.000
- Proyek sulit → minimal Rp 3.000.000

Jika ada beberapa proyek yang memenuhi syarat, maka sistem memilih yang paling mahal sebagai rekomendasi utama.

10. Logout

![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/logout.png)

Saat memilih opsi Logout, user keluar dari sesi login saat ini dan diarahkan kembali ke halaman login. Fitur ini berguna jika perangkat digunakan secara bergantian oleh beberapa pengguna.

11. Keluar Program

![Flowchart](https://github.com/sitinursinta044-design/Mini_project_2_DDP/blob/main/file/keluar.png)

Jika user memilih menu keluar program, maka sistem akan menampilkan pesan:

"Program ditutup..."

dan seluruh proses telah selesai dijalankan.