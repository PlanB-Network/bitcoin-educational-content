---
name: Jade Plus - Green
description: Konfigurasikan Jade Plus dengan mudah pakai Green
---
![cover](assets/cover.webp)

Jade Plus adalah dompet perangkat keras khusus Bitcoin yang dibuat oleh Blockstream. Dompet ini merupakan penerus Jade klasik, dengan peningkatan perangkat lunak, lebih banyak opsi, dan desain ergonomis yang dirancang ulang supaya lebih intuitif dipakai. Versi barunya punya layar LCD 1,9 inci yang keren, dengan gamut warna yang lebih luas dibanding versi sebelumnya. Tombol dan navigasi menunya juga sudah dioptimalkan.

Jade Plus bisa digunakan dengan berbagai cara: lewat kabel USB-C, dalam mode *Air-Gap* dengan kartu micro SD (pakai adaptor), lewat Bluetooth, atau bahkan dengan menukar kode QR berkat kamera bawaan. Dompet perangkat keras ini juga punya baterai sendiri.

Dompet ini dijual mulai dari $149,99 untuk versi hitam standar, dan bisa naik sekitar $20 untuk versi *Genesis Grey* atau *Lunar Silver.* Karena itu, Jade Plus jadi pilihan menarik dengan fitur canggih yang setara dengan dompet perangkat keras kelas atas seperti Coldcard Q atau Passport V2, tapi dengan harga yang lebih terjangkau, mendekati model kelas menengah

![JADE-PLUS-GREEN](assets/fr/01.webp)

Jade Plus kompatibel dengan sebagian besar perangkat lunak manajemen portofolio. Berikut ringkasan kompatibilitasnya pada saat penulisan (Januari 2025):

| Desktop | Seluler | USB | Bluetooth | QR | JadeLink | Perangkat lunak manajemen

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Hijau | 🟢 | 🟢 | 🟢 | 🟢 (Seluler) | 🟢 | 🔴 |

liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |

Sparrow | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 |

nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| Momok | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |

| keeper | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

Di tutorial ini, kita bakal nyiapin dan pakai Jade Plus bareng aplikasi seluler Green Wallet dari Blockstream lewat koneksi Bluetooth. Pengaturan ini paling pas buat kamu yang masih pemula. Tapi kalau kamu mau cara yang lebih advanced, coba cek tutorial ini, di mana kita pakai Jade Plus bareng Sparrow Wallet dalam mode kode QR.

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Model keamanan Jade Plus

Jade Plus pakai model keamanan berbasis *virtual secure element* yang diwujudkan lewat *blind oracle.* Secara sederhana, mekanisme ini menggabungkan PIN yang kamu pilih, rahasia yang disimpan di Jade, dan satu rahasia lagi yang dipegang oleh oracle (server yang dikelola Blockstream) untuk membuat kunci AES-256 yang dibagi ke dua pihak.

Saat proses inisialisasi, pertukaran ECDH dipakai untuk mengamankan komunikasi dengan oracle dan mengenkripsi seedphrase di dompet perangkat keras. Dalam praktiknya, kalau kamu mau mengakses seed buat menandatangani transaksi, kamu perlu akses ke:


- Ke perangkat Jade Plus itu sendiri;
- Ke PIN untuk membuka kunci perangkat ;
- Dan untuk rahasia peramal.

Keuntungan utama dari pendekatan ini adalah tidak adanya satu titik kegagalan di level perangkat keras. Kalau ada penyerang yang berhasil mendapatkan akses ke Jade kamu, mereka tetap nggak bisa mengekstrak kuncinya tanpa juga berhasil menembus oracle di waktu yang sama. Model ini juga memungkinkan Jade Plus tetap sepenuhnya open-source, jadi nggak terikat pada keterbatasan penggunaan elemen keamanan fisik seperti yang dipakai Ledger, misalnya.

Kekurangannya, Jade Plus bergantung pada oracle yang dikelola oleh Blockstream. Kalau oracle ini nggak bisa diakses, kamu nggak akan bisa lagi pakai dompet perangkat keras secara langsung dengan PIN. Tapi ini bukan berarti bitcoin kamu hilang. Kamu masih bisa memulihkannya dengan seedphrase kamu, yang bisa dimasukkan ke Jade Plus dalam mode *stateless.* Untuk menghindari ketergantungan ini, kamu juga bisa mengatur dan menjalankan server oracle kamu sendiri.

## Membuka kemasan Jade Plus

Begitu kamu menerima Jade Plus, pastikan kotak dan segelnya masih dalam kondisi baik untuk memastikan kalau paket kamu belum pernah dibuka.

![JADE-PLUS-GREEN](assets/fr/02.webp)

Di dalam kotak Anda akan menemukan :


- Le Jade Plus;
- Kabel USB-C;
- Kartu untuk merekam frasa mnemonik milikmi sebagai kata-kata atau sebagai "*CompactSeedQR*";
- Beberapa petunjuk penggunaan ;
- Sebuah kabel;
- Beberapa stiker.

![JADE-PLUS-GREEN](assets/fr/03.webp)

Perangkat ini memiliki 4 tombol navigasi:


- Tombol di kanan bawah menyalakan Jade;
- Tombol besar pada bagian depan perangkat digunakan untuk memilih item;
- Dua tombol kecil di bagian atas memungkinkanmu menavigasi ke kiri dan ke kanan;
- Kamu juga bisa memilih item dengan mengklik secara bersamaan pada dua tombol di bagian atas perangkat.

![JADE-PLUS-GREEN](assets/fr/04.webp)

## Menyiapkan dompet Bitcoin baru

Klik pada tombol mulai.

![JADE-PLUS-GREEN](assets/fr/05.webp)

Klik "*Setup Jade*".

![JADE-PLUS-GREEN](assets/fr/06.webp)

Pilih "Begin Setup" (Mulai Penyiapan). Opsi "*Advanced Setup*" melakukan hal yang sama, tetapi dengan akses ke pengaturan lanjutan.

![JADE-PLUS-GREEN](assets/fr/07.webp)

Kemudian klik "*Buat Dompet Baru*" untuk menghasilkan seed baru.

![JADE-PLUS-GREEN](assets/fr/08.webp)

Klik tombol "*Lanjutkan*" untuk menampilkan frasa pemulihan baru Anda.

![JADE-PLUS-GREEN](assets/fr/09.webp)

Jade Plus kamu akan menampilkan seedphrase berisi 12 kata. Seedphrase ini memberi kamu akses penuh ke semua bitcoin kamu. **Siapa pun yang punya frasa ini bisa mencuri dana kamu, bahkan tanpa harus memegang Jade Plus kamu secara fisik.** Frasa 12 kata ini juga berfungsi untuk memulihkan akses ke bitcoin kamu kalau Jade hilang, dicuri, atau rusak. Karena itu, sangat penting untuk menyimpannya dengan hati-hati di tempat yang aman.

Kamu bisa menuliskannya di kartu yang disertakan dalam kotak, atau kalau mau keamanan ekstra, disarankan untuk mengukirnya di lempengan baja tahan karat supaya tahan terhadap kebakaran, banjir, atau keruntuhan.

![JADE-PLUS-GREEN](assets/fr/10.webp)

Kalau kamu mau tahu lebih lanjut tentang cara yang benar untuk menyimpan dan mengelola seedphrase, aku sangat nyaranin kamu buat ikuti tutorial lain yang udah tersedia, terutama kalau kamu masih pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Tentu saja, kamu tidak boleh membagikan kata-kata seedphrase ini di internet, seperti yang aku tunjukkan dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.**

Klik panah di sebelah kanan layar untuk menampilkan kata-kata berikut.

![JADE-PLUS-GREEN](assets/fr/11.webp)

Setelah kamu menyimpan seedphrase-nya, Jade Plus akan minta kamu buat mengonfirmasinya. Pilih kata yang benar sesuai urutannya dengan tombol di bagian atas perangkat, lalu tekan tombol tengah untuk lanjut ke kata berikutnya.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Menghubungkan Jade Plus ke Green Wallet

Di tutorial ini, kita bakal pakai aplikasi Green Wallet buat mengelola dompet yang tersimpan di Jade Plus. Cara ini paling cocok buat kamu yang masih pemula. Tapi kalau kamu pengin ngatur dompet Bitcoin kamu dengan lebih detail, kamu juga bisa pakai Sparrow Wallet, yang bakal kita bahas di tutorial terpisah:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Untuk petunjuk tentang cara menginstal dan menyiapkan aplikasi Blockstream Green, silakan lihat bagian pertama dari tutorial ini:

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Setelah berada di aplikasi Blockstream Green, klik tombol "*Konfigurasi portofolio baru*".

![JADE-PLUS-GREEN](assets/fr/13.webp)

Pilih "*Pada Dompet Perangkat Keras*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Aktifkan Bluetooth pada smartphone milikmu, kemudian klik tombol "*Hubungkan Jade Anda*".

![JADE-PLUS-GREEN](assets/fr/15.webp)

Mengesahkan aplikasi Green untuk mengakses koneksi Bluetooth.

![JADE-PLUS-GREEN](assets/fr/16.webp)

Aplikasi sedang mencari Jade Plus milikmu.

![JADE-PLUS-GREEN](assets/fr/17.webp)

Pada Jade Plus, klik menu "*Bluetooth*".

![JADE-PLUS-GREEN](assets/fr/18.webp)

Pilih perangkatmu pada aplikasi Hijau.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Konfirmasikan kode pemasangan pada Jade Plus milikmu.

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green menyediakan tes untuk memastikan kalau Jade kamu asli. Klik tombol yang muncul untuk menjalankan tesnya.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Konfirmasikan pada Jade.

![JADE-PLUS-GREEN](assets/fr/22.webp)

Warna hijau menandakan kalau perangkat kamu asli.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## Mengatur kode PIN

Klik tombol "*Lanjutkan*" untuk memilih kode PIN Jade Anda.

![JADE-PLUS-GREEN](assets/fr/24.webp)

Kode PIN digunakan untuk membuka kunci Jade kamu. Karena itu, kode ini berfungsi sebagai perlindungan dari akses fisik yang tidak sah. PIN ini tidak terlibat dalam proses pembuatan kunci kriptografi dompet kamu, jadi bahkan tanpa PIN, siapa pun yang punya seedphrase 12 kata tetap bisa memulihkan akses ke bitcoin kamu. Disarankan untuk memilih kode PIN yang benar-benar acak dan menyimpannya di tempat terpisah dari Jade kamu, misalnya di pengelola kata sandi.

Pilih PIN 6 digit langsung di Jade kamu, gunakan tombol kanan dan kiri untuk menggulir angka, lalu tekan tombol tengah untuk mengonfirmasi setiap angka.

![JADE-PLUS-GREEN](assets/fr/25.webp)

Konfirmasikan PIN milikmu untuk kedua kalinya.

![JADE-PLUS-GREEN](assets/fr/26.webp)

Dompet bitcoin telah dibuat.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Membuat akun Bitcoin

Sekarang kamu perlu membuat akun di portofolio kamu. Klik tombol *Buat akun.*
![JADE-PLUS-GREEN](assets/fr/28.webp)

Pilih "*Standard*" jika kamu ingin membuat portofolio single-sig klasik.

![JADE-PLUS-GREEN](assets/fr/29.webp)

Untuk informasi lebih lanjut tentang opsi "*2FA*", kamu bisa mengikuti tutorial lainnya:

https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Akun sudah dibuat.

![JADE-PLUS-GREEN](assets/fr/30.webp)

Kalau kamu mau menyesuaikan tampilan portofolio Green kamu, klik tiga titik kecil di pojok kanan atas.

![JADE-PLUS-GREEN](assets/fr/31.webp)

Opsi *Rename* memungkinkan kamu mengubah nama portofolio kamu, yang berguna banget kalau kamu mengelola beberapa portofolio di aplikasi yang sama. Menu *Unit* memungkinkan kamu mengganti satuan dasar portofolio, misalnya menampilkannya dalam satoshi daripada bitcoin. Terakhir, menu *Parameter* memberi kamu akses ke opsi lain. Di sini kamu bisa menemukan extended public key dan deskriptornya, yang berguna kalau kamu berencana membuat watch-only wallet dari Jade kamu.

![JADE-PLUS-GREEN](assets/fr/32.webp)

Untuk menyambungkan kembali ke Jade kamu setelah dimatikan, tekan tombol on/off di bagian bawah perangkat. Di aplikasi Green, pilih perangkat kamu dari halaman beranda:

![JADE-PLUS-GREEN](assets/fr/33.webp)

Lalu masukkan kode PIN di Jade kamu, dan kamu akan langsung terhubung kembali.

![JADE-PLUS-GREEN](assets/fr/34.webp)

Jade kamu akan terbuka lewat *virtual secure element* dari Blockstream (lihat bagian pertama tutorial ini). Proses ini butuh koneksi Bluetooth dengan aplikasi Green. Kalau kamu mengalami masalah saat membuka kunci lewat Bluetooth, coba lepaskan dulu koneksi antarperangkat lalu sambungkan lagi. Kalau masih belum berhasil, kamu bisa membuka kunci Jade dengan memilih opsi *QR Scan* dan mengikuti petunjuk yang tersedia. [di situs web Blockstream] (https://jadefw.blockstream.com/pinqr/index.html).

Sebelum kamu menerima bitcoin pertama di dompet kamu, **aku sangat nyaranin buat melakukan tes pemulihan kosong.** Catat beberapa informasi penting seperti xpub atau alamat penerima pertamamu, lalu hapus wallet kamu di aplikasi Green dan di Jade Plus saat masih kosong (`Options -> Device -> Factory Reset`). Setelah itu, coba pulihkan dompet kamu pakai cadangan kertas berisi seedphrase. Cek apakah data seperti xpub yang muncul setelah pemulihan sama dengan yang kamu catat sebelumnya. Kalau sama, berarti cadangan kertas kamu bisa diandalkan. Untuk tahu lebih lanjut soal cara melakukan pemulihan uji coba, kamu bisa baca tutorial lainnya:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Menerima bitcoin

Setelah dompet Bitcoin kamu siap, kamu udah siap buat menerima satoshi pertamamu! Cukup klik tombol *Terima* di aplikasi Green.

![JADE-PLUS-GREEN](assets/fr/35.webp)

Warna hijau akan menampilkan alamat penerimaan, tapi sebelum kamu menggunakannya, penting banget buat memverifikasi alamat itu di Jade supaya kamu yakin kalau alamat tersebut benar-benar milik portofolio kamu. Untuk melakukannya, klik tombol *Verify on device.*

![JADE-PLUS-GREEN](assets/fr/36.webp)

Cek di Jade apakah alamatnya sama persis dengan yang ditampilkan di Green, lalu tekan tombol untuk mengonfirmasi.

![JADE-PLUS-GREEN](assets/fr/37.webp)

Sekarang kamu bisa membagikan alamat itu ke pengirim untuk menerima bitcoin di dompet kamu. Begitu transaksinya disiarkan ke jaringan, transaksi itu akan muncul di dompet kamu. Tunggu sampai kamu menerima cukup konfirmasi supaya transaksinya bisa dianggap benar-benar final.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Kirim bitcoin

Setelah ada bitcoin di dompet kamu, sekarang kamu juga bisa mengirimnya. Klik Kirim.

![JADE-PLUS-GREEN](assets/fr/39.webp)

Pada halaman berikutnya, masukkan alamat penerima. Kamu bisa memasukkannya secara manual atau memindai kode QR.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Pilih jumlah pembayaran.

![JADE-PLUS-GREEN](assets/fr/41.webp)

Di bagian bawah layar, kamu bisa memilih tarif biaya untuk transaksi ini. Kamu bisa mengikuti rekomendasi dari aplikasi atau menyesuaikan biayanya sendiri. Semakin tinggi biaya dibandingkan transaksi lain yang masih menunggu, semakin cepat transaksi kamu akan diproses. Untuk melihat informasi pasar biaya, kunjungi: [Mempool.space] (https://mempool.space/) di bagian "*Biaya Transaksi*".

![JADE-PLUS-GREEN](assets/fr/42.webp)

Klik "*Selanjutnya*" untuk mengakses layar ringkasan transaksi. Periksa apakah alamat, jumlah, dan biaya sudah benar.

![JADE-PLUS-GREEN](assets/fr/43.webp)

Jika semua berjalan lancar, geser tombol hijau di bagian bawah layar ke kanan untuk menandatangani dan menyiarkan transaksi di jaringan Bitcoin.

![JADE-PLUS-GREEN](assets/fr/44.webp)

Sekarang kamu akan diminta untuk mengonfirmasi transaksi di Jade.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Pastikan alamat penerima sudah benar. Klik tanda centang untuk mengonfirmasi.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Periksa apakah jumlah tagihan sudah benar, lalu validasi.

![JADE-PLUS-GREEN](assets/fr/47.webp)

Transaksi kamu sudah ditandatangani dan disiarkan lewat Green.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Selamat, sekarang kamu sudah tahu cara mengatur dan menggunakan Jade Plus dengan aplikasi seluler Blockstream Green melalui koneksi Bluetooth. Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih kalau kamu memberi jempol hijau di bawah. Jangan ragu untuk membagikan artikel ini di jejaring sosialmu. Terima kasih sudah membagikannya!

Untuk langkah selanjutnya, aku rekomendasikan tutorial Jade Plus ini, di mana kita mengonfigurasi perangkat dengan Sparrow Wallet dalam mode QR. Kamu juga akan mempelajari cara memakai pengaturan lanjutan pada dompet perangkat kerasmu.:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

