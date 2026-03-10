---
name: COLDCARD Mk4
description: Panduan untuk menyiapkan dan menggunakan COLDCARD Mk4 dengan Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


**Perangkat keras wallet adalah perangkat fisik yang dibuat hanya untuk menyimpan kunci pribadi Bitcoin dengan aman. Perangkat ini menyimpan private key secara offline, yang berarti peretas tidak dapat menjangkaunya melalui internet. Sementara **software wallet** terutama digunakan untuk transaksi sehari-hari, **hardware wallet** sering kali digunakan untuk menyimpan bitcoin dalam jumlah yang lebih besar dengan aman untuk waktu yang lama. Ketika melakukan transaksi Bitcoin menggunakan **perangkat keras wallet**, wallet dapat menandatangani transaksi di dalam perangkat, sehingga kunci pribadi tidak pernah terekspos ke lingkungan yang terhubung ke internet.


Dalam tutorial ini, kita akan membahas salah satu perangkat keras wallet yang paling populer yang diproduksi oleh Coinkite, yaitu Coldcard Mk4. Kita akan melihat cara mengatur dan menggunakan perangkat keras wallet ini untuk melakukan transaksi Bitcoin.


## Gambaran Umum Coldcard Mk4


Coldcard Mk4 adalah perangkat keras khusus Bitcoin yang diproduksi oleh Coinkite. Perangkat ini dilengkapi dengan layar, keypad numerik dan penutup geser pelindung. Selain itu, perangkat ini menawarkan beberapa cara untuk terhubung dan berinteraksi, termasuk USB-C, operasi celah udara menggunakan kartu MicroSD, NFC, dan mode disk virtual. Mk4 juga menyertakan fitur keamanan canggih seperti BIP39 passphrase dan PIN jebakan, sehingga memberikan kontrol dan perlindungan yang lebih besar kepada pengguna atas Bitcoin mereka.


## Pengaturan Awal: PIN dan Kata-kata Anti-Phishing


Untuk memulai, Coldcard Mk4 dapat dibeli langsung dari [situs web Coinkite] (https://store.coinkite.com/store). Pembeli juga dapat memilih untuk membayar menggunakan mata uang fiat atau Bitcoin. Selain itu, Anda juga membutuhkan kartu MicroSD (4 GB sudah cukup) dan sumber daya yang dapat dihubungkan melalui kabel USB-C (Coldcard Mk4 hanya memiliki port input daya USB-C). Harap diperhatikan, bahwa karena Mk4 tidak memiliki baterai built-in, maka kamera ini harus selalu terhubung ke sumber daya sewaktu digunakan.


Anda akan menerima Mk4 Anda dalam tas anti rusak. Mohon pastikan bahwa tas tersebut tidak mengalami kerusakan. Jika Anda menemukan sesuatu yang mungkin menjadi masalah seperti kerusakan atau sobekan pada tas, Anda dapat memberi tahu Coinkite dengan mengirim email ke support@coinkite.com. Selain itu, Anda juga dapat menemukan 12 digit nomor pada tas yang tahan terhadap kerusakan, yang akan kami sebut sebagai nomor tas Mk4. Nomor tas ini nantinya akan digunakan untuk memverifikasi bahwa perangkat belum dirusak selama pengiriman dan bahwa perangkat tersebut berasal langsung dari Coinkite. Nomor kantong disimpan dengan aman di dalam Coldkartu secure element menggunakan memori flash OTP (One-Time-Programmable), yang berarti tidak dapat diubah setelah diprogram. Ketika Anda menyalakan perangkat untuk pertama kalinya, nomor yang ditampilkan pada layar harus sama dengan yang ada di tas. Hal ini memastikan bahwa Mk4 yang Anda terima adalah perangkat asli dari pabrik dan belum diganti atau dimodifikasi. Meskipun verifikasi ini hanya mengonfirmasi integritas perangkat pada saat pertama kali dinyalakan, secure element terus melindungi kunci pribadi, PIN, dan passphrase Anda, sehingga sangat sulit bagi perusakan apa pun untuk membahayakan Bitcoin Anda. Selain itu, praktik yang baik, seperti mengamankan data terkait wallet Anda dengan benar, akan bermanfaat bagi keamanan keseluruhan kartu Cold itu sendiri. Untuk informasi lebih lanjut, Anda dapat merujuk ke [artikel] (https://blog.coinkite.com/understanding-mk4-security-model/) yang menguraikan model keamanan Coldcard.


Papan tombol terdiri dari 10 tombol numerik, tombol OK (`✓`), dan tombol batal (`✕`). Beberapa tombol numerik juga dapat digunakan untuk navigasi: `5` untuk menavigasi ke atas (`^`), `7` untuk menavigasi ke kiri (`<`), `8` untuk menavigasi ke bawah (`˅`), dan `9` untuk menavigasi ke kanan (`>`).


![01](assets/en/01.webp)


Jika tidak ada masalah dengan kemasannya, Anda dapat membuka tasnya. Mk4 akan dilengkapi dengan kartu cadangan wallet yang dapat digunakan untuk menyimpan informasi mengenai PIN perangkat, kata-kata anti-phishing, dan seedphrase. Ikuti langkah-langkah berikut untuk inisialisasi:


1. Siapkan selembar kertas dan pena.

2. Sambungkan Mk4 ke sumber daya (kabel USB-C) dan masukkan kartu MicroSD.

3. Setelah perangkat dihidupkan untuk pertama kalinya, layar akan menampilkan pesan mengenai Ketentuan Penjualan dan Penggunaan Coldcard. Arahkan ke bawah, lalu tekan `✓` untuk melanjutkan.

4. Selanjutnya, nomor 12 digit akan ditampilkan di layar. Periksa nomor ini dengan nomor yang ada di kantong anti rusak dan salinan nomor kantong tambahan yang disertakan dalam kantong anti rusak untuk memastikan perangkat belum dirusak. Jika nomornya tidak cocok, segera hubungi dukungan Coinkite sebelum melanjutkan. Jika tidak, tekan `✓` untuk melanjutkan.


![02](assets/en/02.webp)


5. Pilih `Pilih Kode PIN`.

6. Arahkan ke bawah saat Anda membaca petunjuk untuk melanjutkan ke langkah berikutnya.


![03](assets/en/03.webp)


7. Pada Mk4, buat dan masukkan awalan PIN (harus sepanjang 2 hingga 6 karakter) dan tuliskan, lalu tekan `✓` untuk melanjutkan.

8. Tuliskan dua kata yang ditampilkan di layar. Ini adalah kata-kata anti-phishing. Tekan `✓` untuk melanjutkan.


![04](assets/en/04.webp)


9. Buat dan masukkan akhiran PIN (atau sisa PIN, harus terdiri dari 2 hingga 6 karakter) dan tuliskan. Tekan `✓` untuk melanjutkan.

10. Masukkan kembali awalan PIN Anda. Tekan `✓` untuk melanjutkan.


![05](assets/en/05.webp)


11. Periksa apakah kata-kata anti-phishing sama dengan yang Anda tulis pada langkah 8. Tekan `✓` untuk melanjutkan.

12. Masukkan kembali akhiran PIN Anda (atau sisa PIN). Tekan `✓` untuk melanjutkan.


![06](assets/en/06.webp)


13. PIN Mk4 Anda dan kata-kata anti-phishing sekarang berhasil dibuat dan disimpan oleh perangkat.


![07](assets/en/07.webp)


Perhatikan bahwa Mk4 akan selalu meminta Anda untuk memasukkan PIN setiap kali Anda menyalakan perangkat. Tanpa PIN ini, Anda tidak dapat mengakses Coldcard Mk4 Anda. Jadi, pastikan Anda membuat cadangan yang cukup untuk PIN dan kata-kata anti-phishing.


## Menyiapkan Wallet Anda


Langkah berikutnya adalah menyiapkan wallet Anda. Ada tiga cara bagi Anda untuk melakukan ini:


- Membuat wallet baru (standar)
- Membuat wallet baru dengan lemparan dadu
- Mengimpor wallet


### Membuat wallet baru (standar)


Untuk membuat wallet baru, cukup lakukan langkah-langkah berikut.


1. Pilih `New Wallet` (atau `New Seed Words`) > Pilih `12 Kata` atau `24 Kata (default)`, tergantung preferensi Anda.


![08](assets/en/08.webp)


2. Perangkat akan menghasilkan 12 atau 24 kata sebagai seedphrase berdasarkan pilihan Anda. Arahkan ke bawah saat Anda menuliskan setiap kata dengan hati-hati dalam urutan yang benar. Kemudian, tekan `✓` untuk melanjutkan.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Perangkat akan meminta Anda untuk memverifikasi seedphrase Anda dengan menanyakan urutan acak (misalnya, `Kata 1 adalah`, lalu `Kata 5 adalah`, lalu `Kata 12 adalah`, dan seterusnya) dan akan ada tiga pilihan kata untuk setiap pertanyaan. Lihat catatan dari Langkah 2 dan pilihlah kata dengan benar (dengan menekan `1`, `2` atau `3`, mana saja yang sesuai dengan kata yang benar) untuk menyelesaikan pembuatan wallet.


![09](assets/en/09.webp)


4. Mk4 kemudian akan menanyakan, apakah Anda ingin mengaktifkan NFC/Tap atau tidak. Untuk saat ini, pilih `✕` untuk opsi ini. Hal ini dapat diubah dalam pengaturan di kemudian hari.

5. Terakhir, Mk4 juga dapat digunakan jika Anda ingin menonaktifkan Port USB (yang dapat digunakan untuk transfer data non-airgapped). Untuk saat ini, pilih `✓` untuk opsi ini. Hal ini dapat diubah dalam pengaturan di kemudian hari.

6. Layar sekarang akan menampilkan menu utama dengan `Siap untuk Ditandatangani` di bagian atas. Ini menandai selesainya proses pembuatan wallet.


![10](assets/en/10.webp)


### Membuat wallet baru dengan lemparan dadu


Sebagai alternatif, Anda juga bisa memilih untuk menghasilkan seedphrase baru dengan entropi. Lakukan ini jika Anda tidak mempercayai seedphrase yang baru dibuat oleh Mk4.


Prosedur pada Coldcard Mk4 adalah sebagai berikut:


1. Pilih `New Wallet` (atau `Kata Benih Baru`) > Pilih `Gulungan Dadu 12 Kata` atau `Gulungan Dadu 24 Kata` tergantung pada preferensi Anda.

2. Anda akan diminta untuk memasukkan hasil lemparan dadu Anda. Setiap lemparan dadu menambah keacakan pada proses pembuatan wallet, memastikan bahwa seedphrase Anda dibuat dengan cara yang sepenuhnya aman dan tidak dapat diprediksi. Jumlah minimum lemparan adalah 50 untuk seedphrase 12 kata dan 99 untuk seedphrase 24 kata. Tekan `✓` setelah Anda memasukkan setidaknya 99 nilai lemparan dadu.


![11](assets/en/11.webp)


3. Perangkat akan menghasilkan 12 atau 24 kata sebagai seedphrase berdasarkan pilihan Anda. Arahkan ke bawah saat Anda menuliskan setiap kata dengan hati-hati dalam urutan yang benar. Kemudian, tekan `✓` untuk melanjutkan.

4. Perangkat akan meminta Anda untuk memverifikasi seedphrase Anda dengan menanyakan urutan acak (misalnya, `Kata 1 adalah`, lalu `Kata 5 adalah`, lalu `Kata 12 adalah`, dan seterusnya) dan akan ada tiga pilihan kata untuk setiap pertanyaan. Lihat catatan dari Langkah 3 dan pilihlah kata dengan benar (dengan menekan `1`, `2` atau `3`, mana saja yang sesuai dengan kata yang benar) untuk menyelesaikan pembuatan wallet.


![12](assets/en/12.webp)


5. Mk4 kemudian akan menanyakan, apakah Anda ingin mengaktifkan NFC/Tap atau tidak. Untuk saat ini, pilih `✕` untuk opsi ini. Hal ini dapat diubah dalam pengaturan di kemudian hari.

6. Terakhir, Mk4 juga dapat digunakan jika Anda ingin menonaktifkan Port USB (yang dapat digunakan untuk transfer data non-airgapped). Untuk saat ini, pilih `✓` untuk opsi ini. Hal ini dapat diubah dalam pengaturan di kemudian hari.

7. Layar sekarang akan menampilkan menu utama dengan `Siap untuk Ditandatangani` di bagian atas. Hal ini menandai selesainya proses pembuatan wallet.


![13](assets/en/13.webp)


### Mengimpor wallet


Opsi terakhir adalah Anda dapat mengimpor wallet. Anda dapat melakukan ini jika Anda ingin memulihkan wallet dari seedphrase yang sudah Anda miliki. Anda dapat mengikuti langkah-langkah berikut:


1. Pilih `Import Existing`.

2. Pilih `24 Kata`, `18 Kata`, atau `12 Kata`, tergantung pada jumlah kata seedphrase Anda.


![14](assets/en/14.webp)


3. Coldcard Mk4 kemudian akan menanyakan kepada Anda apa arti dari setiap kata secara berurutan. Untuk setiap kata, arahkan ke bawah atau ke atas hingga Anda menemukan awalan tulis untuk setiap kata. Perangkat akan mempersempit kemungkinan sampai Anda dapat menemukan kata yang benar. Lakukan hal ini untuk kata-kata lainnya.

4. Untuk kata terakhir, Coldcard Mk4 hanya akan menampilkan sejumlah kata yang mungkin. Jika tidak ada yang cocok, Anda mungkin salah memasukkan kata. Jika tidak, pilih kata yang cocok dengan kata yang ada di seedphrase Anda.


![15](assets/en/15.webp)


5. Mk4 kemudian akan menanyakan, apakah Anda ingin mengaktifkan NFC/Tap atau tidak. Untuk saat ini, pilih `✕` untuk opsi ini. Hal ini dapat diubah dalam pengaturan di kemudian hari.

6. Terakhir, Mk4 juga dapat digunakan jika Anda ingin menonaktifkan Port USB (yang dapat digunakan untuk transfer data non-airgapped). Untuk saat ini, pilih `✓` untuk opsi ini. Hal ini dapat diubah dalam pengaturan di kemudian hari.

7. Layar sekarang akan menampilkan menu utama dengan `Siap untuk Ditandatangani` di bagian atas. Hal ini menandai selesainya proses pembuatan wallet.


![16](assets/en/16.webp)


Harap diperhatikan bahwa seedphrase adalah satu-satunya akses untuk memulihkan wallet Anda. Buatlah cadangan seedphrase Anda dan simpan di tempat yang aman. **Bukan kunci Anda, bukan koin Anda**, siapa pun yang memiliki seedphrase Anda memiliki akses ke bitcoin Anda!


## Menyiapkan passphrase Anda


Salah satu praktik terbaik dalam Bitcoin adalah menggunakan passphrase. passphrase berfungsi sebagai kata ke-13 atau ke-25 sebagai tambahan untuk seedphrase. Yang membuatnya berbeda, Anda dapat memilih frasa apa pun yang Anda inginkan, sedangkan seedphrase dipilih dari daftar 2048 kata yang sudah ditentukan sebelumnya. Secara default, setelah menyiapkan wallet, Anda akan memulai dengan wallet dengan passphrase yang kosong. Untuk menyiapkan passphrase yang tidak kosong, cukup lakukan langkah-langkah berikut:


1. Buka `Passphrase`.

2. Arahkan ke bawah untuk membaca deskripsi tentang passphrase, lalu tekan `✓` untuk melanjutkan.

3. Pilih `Edit Frasa`.


![17](assets/en/17.webp)


4. Masukkan passphrase Anda:


   - Tekan `1` (huruf), `2` (angka), atau `3` (simbol) untuk memilih jenis karakter.
   - Tekan `4` untuk menukar antara huruf kecil dan huruf besar (hanya dapat digunakan saat memasukkan huruf).
   - Navigasi dengan menggunakan `^` atau `˅` untuk memilih karakter passphrase Anda.
   - Navigasi dengan menggunakan `<` atau `>` untuk berpindah di antara karakter. Anda juga dapat menggunakan `>` untuk menambahkan spasi.
   - Tekan `✕` untuk menghapus karakter.
   - Tekan `✓` setelah Anda selesai mengedit passphrase.

5. Selain itu, opsi lainnya memiliki fungsi sebagai berikut:


   - `Tambah Kata` atau `Tambah Angka` dapat digunakan untuk menambahkan huruf/angka ke passphrase yang sedang Anda edit.
   - Tekan `Clear ALL` untuk mengatur ulang passphrase yang sedang Anda edit.
   - Tekan `CANCEL` untuk kembali ke menu utama.

6. Catatlah passphrase Anda sebagai cadangan.

7. Tekan `TERAPKAN` untuk mengakses wallet dengan passphrase yang baru saja Anda tetapkan.

8. Mk4 kemudian akan menampilkan sidik jari kunci master sepanjang 8 karakter. Ini dapat dianggap sebagai "ID" dari wallet. Tulis sidik jari ini dan tekan `✓` untuk melanjutkan.


![18](assets/en/18.webp)


9. Sekarang, wallet akan menampilkan menu utama wallet dengan passphrase yang sudah Anda masukan.

10. Penting untuk diperhatikan bahwa wallet tidak akan memberi tahu Anda bahwa Anda telah memasukkan passphrase yang salah, karena setiap passphrase sesuai dengan masing-masing wallet dengan identitas unik (sidik jari kunci utama). Oleh karena itu, merupakan praktik yang baik untuk memasukkan kembali passphrase yang sama dan memeriksa apakah itu menghasilkan sidik jari wallet yang sama, untuk memastikan bahwa Anda telah memasukkannya dengan benar. Untuk melakukannya, lakukan Langkah 11 hingga 14.

11. Pada menu utama, pilih `Restore Master`, lalu tekan `✓`. Anda sekarang kembali ke menu utama wallet dengan passphrase kosong.


![19](assets/en/19.webp)


12. Buka `Passphrase` lagi, lalu tekan `✓` untuk melanjutkan.

13. Masukkan kembali passphrase yang telah Anda tuliskan pada Langkah 6, lalu tekan `TERAPKAN`.

14. Periksa sidik jari kunci master sepanjang 8 karakter dengan sidik jari yang telah Anda tuliskan pada Langkah 8. Jika kedua sidik jari tidak cocok, Anda mungkin telah mengetik karakter yang tidak cocok. Anda dapat memilih passphrase yang baru dan mengulangi proses dari Langkah 1. Tetapi jika kedua sidik jari cocok, berarti Anda telah memasukkan passphrase dengan benar.

15. wallet dengan passphrase yang Anda pilih siap digunakan.


## Mengekspor Wallet ke Sparrow


Seperti perangkat keras wallet lainnya, Coldcard Mk4 tidak dapat digunakan sendiri. Alat ini harus dihubungkan dengan perangkat lunak wallet yang berfungsi sebagai antarmuka. Perangkat lunak wallet memungkinkan Anda untuk melihat saldo Anda, membuat transaksi, dan mengelola alamat, sementara Coldcard dengan aman menandatangani transaksi-transaksi tersebut tanpa harus membuka kunci pribadi Anda.


Dalam tutorial ini, kita akan menggunakan Sparrow Wallet sebagai antarmuka. Prosedur untuk mengekspor wallet adalah sebagai berikut:


1. Pastikan Anda memiliki kartu MicroSD yang dimasukkan ke dalam Mk4.

2. Lakukan langkah "Menyiapkan passphrase Anda" pada wallet dengan passphrase yang ingin Anda ekspor. Jika Anda ingin mengekspor wallet dengan passphrase kosong, Anda dapat melewati langkah ini.

3. Buka `Advanced/Tools (Alat Lanjutan/Peralatan) > Pilih `Export Wallet` > Pilih `Generic JSON` > Gulir ke bawah saat Anda membaca petunjuk, lalu tekan `✓`.


![20](assets/en/20.webp)


4. Mk4 sekarang telah membuat file dengan format `.json` dalam kartu MicroSD.


![21](assets/en/21.webp)


5. Keluarkan kartu MicroSD dari kartu Cold dan masukkan ke dalam perangkat di mana Sparrow Wallet dipasang.

6. Buka Sparrow Wallet.

7. Klik pada `File`


![22](assets/en/22.webp)


Selanjutnya, klik `New Wallet`


![23](assets/en/23.webp)


Kemudian, masukkan nama untuk wallet


![24](assets/en/24.webp)


Setelah itu, klik `Create Wallet`


![25](assets/en/25.webp)


8. Pilih `Jenis Naskah`.


![26](assets/en/26.webp)


9. Pada bagian Keystore, pilih `Airgapped Hardware Wallet`.


![27](assets/en/27.webp)


10. Cari kartu Cold dan klik `Import File...`.


![28](assets/en/28.webp)


11. Pilih file yang telah dibuat pada Langkah 4 (file dengan format `.json`).


![29](assets/en/29.webp)


12. Pada Mk4, kembali ke menu utama dan arahkan ke `Advanced/Tools` > `Lihat Identitas`. Pastikan sidik jari yang ditampilkan pada layar Mk4 sesuai dengan sidik jari yang ada di Sparrow Wallet (sidik jari Master pada bagian Keystore)

13. Klik tombol `Apply` di sudut kanan bawah.


![30](assets/en/30.webp)


14. Secara opsional, Anda juga dapat menambahkan kata sandi untuk wallet yang diekspor. Kata sandi ini diperlukan setiap kali Anda membuka aplikasi Sparrow Wallet untuk mengakses wallet. Jika Anda lupa kata sandi di kemudian hari, Anda cukup mengulangi Langkah 1-13 dan memilih kata sandi yang baru.


![31](assets/en/31.webp)


15. wallet kini telah berhasil diekspor dan siap untuk digunakan.


![32](assets/en/32.webp)


## Menerima bitcoin


Selanjutnya, kita akan mempelajari cara menerima Bitcoin menggunakan Mk4. Proses ini cukup sederhana karena Anda tidak perlu menggunakan perangkat Mk4 itu sendiri. Selama Anda sudah mengekspor wallet Anda ke Sparrow, Anda bisa menerima Bitcoin secara langsung melalui Sparrow Wallet. Ikuti langkah-langkah berikut untuk menerima bitcoin dengan Mk4:


1. Buka Sparrow Wallet.

2. Pilih `Buka Wallet` > Pilih file wallet yang ingin Anda terima bitcoinnya > Masukkan kata sandi yang terkait dengan wallet tersebut.


![33](assets/en/33.webp)


3. Pada antarmuka Sparrow, klik pada tab `Receive` di sisi kiri antarmuka.


![34](assets/en/34.webp)


4. Alamat beserta kode QR akan muncul di bagian atas. Anda bisa menyalin dan menempelkan alamat tersebut atau memindai kode QR menggunakan wallet yang akan Anda gunakan untuk mengirim bitcoin ke Sparrow Wallet. Secara opsional, Anda bisa mengetikkan label untuk bitcoin yang Anda terima.


![35](assets/en/35.webp)


5. Setelah Anda mengirim bitcoin, pada antarmuka Sparrow, klik pada tab `Transactions` di sisi kiri antarmuka. Anda akan melihat entri baru di bagian atas riwayat transaksi, yang sesuai dengan transaksi yang baru saja Anda lakukan.


![36](assets/en/36.webp)


6. Anda juga bisa menavigasi pada tab `UTXOs` di sisi kiri antarmuka untuk melihat bitcoin yang baru saja Anda terima.


![37](assets/en/37.webp)


## Mengirim bitcoin


Tidak seperti menerima bitcoin, membelanjakan bitcoin yang terkait dengan kartu Cold Anda mengharuskan Anda menggunakan kartu Cold untuk menandatangani transaksi. Prosedur pengiriman bitcoin dengan Mk4 adalah sebagai berikut:


1. Masukkan kartu MicroSD ke dalam perangkat tempat Sparrow Wallet Anda dipasang.

2. Buka Sparrow Wallet.

3. Pilih `Buka Wallet` > Pilih file wallet yang ingin Anda gunakan untuk mengirim bitcoin > Masukkan kata sandi yang terkait dengan wallet tersebut.


![38](assets/en/38.webp)


4. Pada antarmuka Sparrow, klik pada tab `Kirim` di sisi kiri antarmuka.


![39](assets/en/39.webp)


5. Pada tab `Bayar ke`, masukkan alamat yang ingin Anda kirimi bitcoin.

6. Tambahkan label untuk transaksi.

7. Masukkan jumlah bitcoin yang ingin Anda kirim.

8. Masukkan biaya dengan menggeser `Range` atau langsung memasukkan angka ke dalam bagian `Fee`.


![40](assets/en/40.webp)


9. Di sudut kanan bawah, klik `Buat Transaksi`.


![41](assets/en/41.webp)


10. Anda akan dibawa ke tab transaksi baru yang namanya sama dengan label yang Anda masukkan pada Langkah 6. Klik `Finalisasi Transaksi untuk Penandatanganan`.


![42](assets/en/42.webp)


11. Klik `Save Transaction` dan simpan transaksi dalam kartu MicroSD. Ganti nama file jika perlu. Langkah ini akan menyimpan transaksi sebagai file PSBT.


![43](assets/en/43.webp)


12. Keluarkan kartu MicroSD dan masukkan ke dalam Coldcard Mk4.

13. Nyalakan Mk4 Anda dengan menghubungkannya ke sumber daya.

14. Masukkan PIN Anda.

15. Buka `Passphrase` dan masukkan passphrase dari wallet yang ingin Anda gunakan untuk mengirim bitcoin. Jika Anda ingin menggunakan wallet dengan passphrase kosong, lewati langkah ini.

16. Pastikan sidik jari kunci utama sama dengan sidik jari yang ada pada Sparrow Wallet Anda. Anda dapat memeriksanya pada tab `Settings` Sparrow Wallet di sisi kiri antarmuka. Kemudian, tekan `✓` pada Mk4 Anda untuk melanjutkan. Ini akan membawa Anda ke menu utama.

17. Pada menu utama Mk4, pilih `Siap untuk Menandatangani`. Layar akan menampilkan pesan `OKAY UNTUK MENGIRIM`. Pastikan jumlah bitcoin yang ingin Anda kirimkan dan alamat penerima sudah benar. Tekan `✓` untuk mengonfirmasi atau `✕` untuk membatalkan.

18. Jika ada beberapa file PSBT yang dapat dipilih, Mk4 akan menampilkan pesan `Pilih file PSBT yang akan ditandatangani`. Tekan `✓` untuk melanjutkan. Kemudian, pilih file PSBT yang ingin Anda tandatangani dengan menavigasi ke bawah atau ke atas. 17. Lakukan Langkah 17 pada transaksi tersebut.


![44](assets/en/44.webp)


19. Mk4 sekarang akan menampilkan pesan `PSBT Ditandatangani` bersama dengan nama file PSBT yang ditandatangani. Tekan `✓` untuk melanjutkan.

20. Keluarkan kartu MicroSD dari kartu Cold dan masukkan ke dalam perangkat di mana Sparrow Wallet dipasang.

21. Pada Sparrow Wallet, klik `Muat Transaksi`.


![45](assets/en/45.webp)


22. Pilih file dengan nama yang sama dengan nama yang dibuat pada Langkah 19.


![46](assets/en/46.webp)


23. Klik `Transaksi Siaran`.


![47](assets/en/47.webp)


24. Transaksi Anda telah disiarkan dan sedang diproses. Anda dapat membuka tab `Transaksi` untuk melihat status konfirmasi transaksi Anda.


![48](assets/en/48.webp)


## Peningkatan Firmware


### Memeriksa Versi Firmware Anda


Firmware Coldcard Mk4 selalu dapat ditingkatkan ke versi yang lebih baru. Untuk memeriksa apakah Mk4 Anda telah ditingkatkan ke versi terbaru atau belum, lakukan langkah-langkah berikut:

1. Nyalakan Mk4 Anda dengan menghubungkannya ke sumber daya.

2. Masukkan PIN Anda.

3. Buka `Advanced/Tools (Alat Lanjutan/Peralatan) > Pilih `Upgrade Firmware (Tingkatkan Firmware) > Pilih `Show Version (Tampilkan Versi).


![49](assets/en/49.webp)


Periksa versi yang ditampilkan pada layar Mk4 dengan versi yang ada di [situs web Coinkite] (https://coldcard.com/downloads). Jika versinya berbeda, Anda dapat meng-upgrade firmware ke versi yang lebih baru.


![50](assets/en/50.webp)


### Meningkatkan Firmware Anda


Jika Anda ingin meng-upgrade firmware ke versi terbaru, lakukan langkah-langkah berikut:


1. Masukkan kartu MicroSD ke dalam laptop/PC Anda.

2. Kunjungi [situs web Coinkite] (https://coldcard.com/downloads) dan unduh firmware terbaru ke kartu MicroSD Anda (Tombol merah di sebelah kanan gambar Mk4 dengan nomor versi di atasnya).


![51](assets/en/51.webp)


Anda juga dapat mengunduh versi lain dengan mengeklik `Semua File pada Mk4` dan menjelajahi versi yang ingin Anda unduh. File yang diunduh akan dalam format `.dfu`.


![52](assets/en/52.webp)


3. Keluarkan kartu MicroSD dan masukkan ke dalam Mk4 Anda.

4. Nyalakan Mk4 Anda dengan menghubungkannya ke sumber daya.

5. Masukkan PIN Anda.

6. Buka `Advanced/Tools` > Pilih `Upgrade Firmware` > Pilih `Dari MicroSD` > Gulir ke bawah saat Anda membaca petunjuk, lalu tekan `✓`.


![53](assets/en/53.webp)


7. Pilih file `.dfu` yang telah Anda unduh di Langkah 2.

8. Coldcard Mk4 akan menampilkan pesan `Instal firmware baru ini? Gulir ke bawah saat Anda membaca petunjuk, lalu tekan `✓`.


![54](assets/en/54.webp)


9. Tunggu hingga Mk4 selesai menginstal firmware baru. Jangan putuskan sambungan sumber daya selama penginstalan.

10. Setelah selesai, Mk4 akan memulai ulang dengan sendirinya. Anda dapat memasukkan PIN dan melakukan langkah-langkah "Memeriksa Versi Firmware Anda" untuk memeriksa apakah firmware telah ditingkatkan atau belum.


## Fitur Lanjutan


### Ubah PIN Anda


Jika Anda ingin mengubah PIN login Anda, cukup lakukan langkah-langkah berikut:


1. Siapkan pena dan selembar kertas.

2. Nyalakan Mk4 Anda dengan menghubungkannya ke sumber daya.

3. Masukkan PIN Anda.

4. Buka `Pengaturan` > Pilih `Pengaturan Masuk` > Pilih `Ubah PIN Utama`

5. Arahkan ke bawah saat Anda membaca pesan, lalu tekan `✓` untuk melanjutkan.


![55](assets/en/55.webp)


6. Masukkan PIN lama Anda.

7. Masukkan awalan PIN baru Anda (harus terdiri dari 2 hingga 6 karakter) dan tuliskan.

8. Mk4 sekarang akan menampilkan dua kata anti-phishing baru, tuliskan kata tersebut, lalu tekan `✓` untuk melanjutkan.

9. Masukkan akhiran PIN baru Anda (atau sisa PIN, harus terdiri dari 2 hingga 6 karakter) dan tuliskan.


![56](assets/en/56.webp)


10. Masukkan kembali awalan PIN baru Anda.

11. Periksa apakah kata-kata anti-phishing cocok dengan yang Anda tulis di Langkah 8.

12. Masukkan kembali akhiran PIN baru Anda (atau sisa PIN).


![57](assets/en/57.webp)


13. PIN Anda telah berhasil diubah.


### Trik PIN - Tambahkan Trik Baru


Trick PIN adalah kode PIN alternatif yang berbeda dengan yang Anda gunakan untuk mengatur Coldcard Mk4 untuk pertama kalinya. Saat Anda mengaktifkan Mk4, Anda dapat memasukkan PIN trik alih-alih PIN Utama untuk memicu tindakan tertentu. Untuk mengonfigurasi PIN trik di Mk4, Anda dapat melakukan langkah-langkah berikut:


1. Siapkan pena dan selembar kertas.

2. Nyalakan Mk4 Anda dengan menghubungkannya ke sumber daya.

3. Masukkan PIN Anda.

4. Buka `Pengaturan` > Pilih `Pengaturan Masuk` > Pilih `PIN Trik` > Pilih `Tambah Trik Baru`.


![58](assets/en/58.webp)


5. Masukkan awalan PIN trik Anda (harus terdiri dari 2 hingga 6 karakter) dan tuliskan.

6. Mk4 sekarang akan menampilkan dua kata anti-phishing baru, tuliskan kata tersebut, lalu tekan `✓` untuk melanjutkan.

7. Masukkan akhiran PIN trik Anda (atau sisa PIN, harus terdiri dari 2 hingga 6 karakter) dan tuliskan.


![59](assets/en/59.webp)


8. Arahkan ke bawah atau ke atas untuk memilih tindakan yang ingin Anda pasangkan dengan PIN trik yang baru saja Anda buat. Daftar tindakan tersebut adalah:


    - `Brick Self`, bila dipilih, chip Mk4 Anda akan dihancurkan setelah PIN dimasukkan, sehingga Mk4 Anda tidak dapat digunakan secara permanen.
    - `Wipe Seed`, Anda dapat memilih di antara tindakan berikut:
      - `Hapus & Reboot`: seed akan dihapus dan kartu Cold akan di-boot ulang setelah PIN dimasukkan.
      - 'Penghapusan Senyap': seed dihapus tanpa suara, namun kartu Cold akan bertindak seolah-olah PIN yang dimasukkan salah.
      - `Hapus -> Wallet`: seed dihapus secara diam-diam, dan kartu Cold akan membawa Anda ke wallet paksa.
    - `Duress Wallet`, ketika dipilih, Mk4 Anda akan mengarah ke duress wallet setelah PIN dimasukkan.
    - pada `Login Countdown`, Anda dapat memilih di antara tindakan berikut:
      - `Seka & Hitung Mundur`: seed segera diseka, kemudian Mk4 akan mulai menampilkan hitungan mundur.
      - 'Hitung Mundur & Bata': Hitung mundur dimulai dan Mk4 akan berbunyi sendiri setelah waktu habis.
      - 'Hitung Mundur': Mk4 akan memulai hitungan mundur dan akan melakukan boot ulang sendiri setelah waktu habis.
    - `Look Blank`, bila dipilih, setelah PIN trik dimasukkan, kartu Cold akan bertindak seolah-olah seedphrase terhapus, tetapi sebenarnya masih ada dalam memori.
    - 'Just Reboot', bila dipilih, kartu Cold akan melakukan reboot sendiri setelah PIN trik dimasukkan.
    - `Delta Mode`, Fitur canggih ini ditujukan untuk pengguna berpengalaman dan dirancang untuk melindungi dari ancaman serius, seperti pemaksaan oleh seseorang yang memiliki pengetahuan orang dalam. Ketika Delta Mode diaktifkan, COLDCARD tampak membuka wallet yang asli, memungkinkan penyerang untuk menelusuri dan mengonfirmasi bahwa wallet tersebut terlihat asli. Akan tetapi, secara diam-diam memblokir semua penandatanganan transaksi, sehingga tidak ada bitcoin yang dapat dikirim. Ia juga menonaktifkan akses ke frasa seed, dan setiap upaya untuk melihatnya akan menghapusnya sepenuhnya. Untuk membuat wallet palsu terlihat lebih meyakinkan, Trick PIN yang digunakan untuk Delta Mode harus dimulai dengan angka yang sama dengan PIN yang asli (sehingga menampilkan kata-kata anti-phishing yang sama) tetapi diakhiri dengan cara yang berbeda.
    - `Policy Unlock`, bila dipilih, Kebijakan Pengeluaran Penandatangan Tunggal (SSSP) akan dinonaktifkan setelah PIN trik dimasukkan.
    - `Policy Unlock & Wipe`, ketika dipilih, berpura-pura menonaktifkan SSSP tetapi akan menghapus seedphrase dalam prosesnya.

9. Setelah Anda memilih tindakan yang ingin dipasangkan dengan PIN trik, konfirmasikan pilihan Anda dengan menekan `✓`. PIN jebakan Anda berhasil dikonfigurasi.

10. Dalam `Pengaturan` > `Pengaturan Masuk` > `PIN Trik`, Anda dapat melihat daftar PIN trik yang telah Anda buat dan tindakan yang dipasangkan dengannya. Anda dapat memilih untuk mengonfigurasi ulang PIN trik dan tindakan yang dipasangkan dengannya. Anda juga dapat menyembunyikan atau menghapusnya dengan memilih PIN, lalu pilih `Sembunyikan Trik` atau `Hapus Trik`.


![60](assets/en/60.webp)


### Trik PIN - Tambahkan Jika Salah


Atau, Anda dapat menambahkan tindakan `Tambahkan Jika Salah` yang akan dipicu setelah PIN yang salah dimasukkan beberapa kali. Anda dapat mengonfigurasi ini dengan melakukan langkah-langkah berikut:


1. Nyalakan Mk4 Anda dengan menghubungkannya ke sumber daya.

2. Masukkan PIN Anda.

3. Buka `Pengaturan` > Pilih `Pengaturan Masuk` > Pilih `Pengaturan PIN` > Pilih `Tambahkan Jika Salah`.


![61](assets/en/61.webp)


4. Mk4 akan menampilkan pesan mengenai pengaturan ini. Arahkan ke bawah saat Anda membaca penjelasannya, lalu tekan `✓` untuk melanjutkan.

5. Masukkan jumlah percobaan salah yang diperlukan untuk memicu tindakan. Catatan: Jumlah percobaan maksimum adalah `12`. Hal ini karena Mk4 dirancang sedemikian rupa sehingga ketika PIN yang salah dimasukkan sebanyak `13` kali, perangkat akan memblokir dirinya sendiri, membuatnya tidak dapat digunakan secara permanen. Setelah Anda memasukkan nomor, tekan `✓` untuk melanjutkan.

6. Arahkan ke atas atau ke bawah untuk memilih tindakan. Tindakan yang tersedia adalah sebagai berikut:


   - "Bersihkan, Berhenti": seedphrase dihapus dan perangkat menampilkan "Seed is wiped, Stop."
   - `Hapus & Mulai Ulang`: seedphrase akan terhapus dan perangkat dihidupkan ulang tanpa pesan apa pun.
   - 'Penghapusan Senyap': seedphrase dihapus secara diam-diam dan perangkat berperilaku seperti upaya salah PIN (tidak ada pesan penghapusan yang jelas).
   - `Brick Self`: Perangkat dinonaktifkan secara permanen dan hanya menampilkan "Bricked."
   - `Kesempatan Terakhir`: seedphrase akan terhapus tetapi Anda mendapatkan satu kali percobaan PIN terakhir; masukkan PIN yang salah lagi dan perangkat akan diblokir.
   - `Just Reboot`: Perangkat hanya dihidupkan ulang dan tidak ada perubahan apa pun.

Pilih tindakan yang ingin Anda terapkan dan tekan `✓` untuk melanjutkan


![62](assets/en/62.webp)


7. Anda akan dibawa kembali ke direktori `Pengaturan > Pengaturan Login > Trik PIN`. Di bawah `Trick PINs:`, Anda akan menemukan daftar pin trik bersama dengan tindakan `WRONG PIN`. Anda juga dapat menyembunyikan atau menghapusnya dengan memilih PIN lalu pilih `Sembunyikan Trik` atau `Hapus Trik`.


![63](assets/en/63.webp)



## Kesimpulan


Tutorial ini telah memberikan panduan tentang cara mengatur Mk4, cara melakukan transaksi Bitcoin dengan Mk4 dan cara menggunakan beberapa fitur canggih Mk4. Mk4 menawarkan cara yang aman dan fleksibel untuk menyimpan dan mengelola bitcoin Anda. Desainnya memastikan bahwa kunci pribadi tidak pernah meninggalkan perangkat, sementara fitur-fitur seperti passphrase, PIN tipuan, dan transaksi celah udara memberikan kontrol penuh atas pengaturan keamanan mereka. Ini dapat dipasangkan dengan Sparrow Wallet untuk pengalaman yang mudah digunakan untuk membuat, menandatangani, dan mengelola transaksi Bitcoin tanpa mengorbankan privasi atau keamanan.


Jika Anda ingin menjelajahi fungsi-fungsi lainnya, Anda dapat memeriksa dokumentasi di situs web Coinkite [di sini] (https://coldcard.com/docs/). Saya harap tutorial ini bermanfaat bagi Anda ketika Anda menggunakan Coldcard Mk4. Terima kasih dan sampai jumpa di lain waktu!