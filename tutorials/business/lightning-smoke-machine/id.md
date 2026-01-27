---
name: Lightning Smoke Machine
description: Memicu mesin asap dengan pembayaran Lightning melalui ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Pendahuluan



Mengubah mesin asap klasik menjadi perangkat yang dapat dibayarkan di Bitcoin melalui Lightning Network. Setiap pembayaran secara otomatis memicu semburan asap!





- Tingkat: Menengah
- Perkiraan waktu: 2-3 jam
- Kasus penggunaan: Acara Bitcoin, pertunjukan artistik, demo Petir, efek panggung otomatis



## Prasyarat



### Pengetahuan





 - Elektronika dasar (perkabelan, relai)
 - Pengelasan (atau penggunaan konektor Dupont)
 - Konfigurasi jaringan (WiFi, WebSocket)



### Akun yang diperlukan





- Server BTCPay: Instance fungsional (host sendiri atau host)
- Blink Wallet : Akun + akses API



### Akses





- Akses admin ke Server BTCPay
- Koneksi WiFi untuk ESP32



## Bahan yang dibutuhkan



### Perangkat keras - Komponen elektronik





- 1 Mikrokontroler - ESP32-WROOM-32


*ESP32-WROOM-32 adalah mikrokontroler WiFi/Bluetooth yang ringkas dan berbiaya rendah untuk menghubungkan perangkat elektronik ke Internet dan mengendalikannya dari jarak jauh*



![ESP32](assets/fr/1.webp)





- 1 Modul relai - 5V dengan optocoupler


*Relai seperti sakelar yang dapat dioperasikan oleh ESP32 untuk menghidupkan atau mematikan mesin asap*



![relay](assets/fr/2.webp)





- ~10 kabel Dupont - Pria/Pria dan Pria/Wanita



![dupont-cables](assets/fr/3.webp)





- 1 Catu daya untuk ESP32 - USB 5V atau baterai Li-Po



![battery](assets/fr/4.webp)





- 1 kabel micro-USB - koneksi antara ESP32 dan catu daya



![micro-usb-cables](assets/fr/5.webp)





- 1 mesin kabut 220V dengan remote control baterai 12V



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 botol cairan yang kompatibel dengan mesin asap Anda



### Perangkat Keras - Peralatan





- Besi solder + timah (jika menyolder)
- Obeng
- Multimeter (disarankan)



### Perangkat lunak





- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- Browser web yang kompatibel dengan WebSerial (Chrome/Edge/Brave)
- Server BTCPay telah dikonfigurasi. Untuk informasi lebih lanjut tentang cara membuat instance BTCPay Server, kunjungi tutorial ini: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Arsitektur sistem



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **PERINGATAN KESELAMATAN - BACA SEBELUM MELANJUTKAN** **⚠️**



Proyek ini melibatkan mesin kabut yang terhubung ke suplai listrik **220V**. Pengoperasian yang tidak tepat dapat mengakibatkan **kelumpuhan fatal** atau **kebakaran**.



**Aturan yang tidak dapat dinegosiasikan:**



1. **SELALU lepaskan mesin asap dari sumber listrik** sebelum membuka remote control atau merusak kabel


2. **Lepaskan baterai dari remote control** sebelum menangani (risiko korsleting dan kerusakan komponen)


3. **Pastikan semua koneksi Anda terisolasi** sebelum menyambungkan kembali apa pun


4. **Jangan pernah menyambungkan kembali 220V** sampai kotak remote control ditutup dan diamankan



Jika Anda tidak nyaman dengan penanganan seperti ini, ajaklah seseorang yang bisa membantu Anda.



---

## BAGIAN 1: Perakitan perangkat keras



### Langkah 1: Menyiapkan remote control



Tujuan: Hubungkan relai ke tombol ON/OFF pada remote control


1. Buka kendali jarak jauh




    - Identifikasi tombol ON/OFF
    - Buka tutup casing untuk membuka remote control


2. Menemukan koneksi




 - Temukan terminal + dan - dari
 - Uji kontinuitas dengan multimeter (opsional)



![smoke-machine-remote](assets/fr/8.webp)



3. Kabel tombol (solder atau konektor)




    - Solder kabel hitam ke terminal - tombol
    - Solder kabel merah ke terminal + umum



![smoke-machine-remote](assets/fr/9.webp)



### Langkah 2: Menghubungkan ke modul relai



**Pengingat: Terminologi relai




| **Terminal**         | **Deskripsi**           | **Fungsi**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Biasanya Terbuka)   | Sirkuit terbuka secara default | Menutup saat relay diaktifkan |
| NC (Biasanya Tertutup) | Sirkuit tertutup secara default  | Membuka saat relay diaktifkan  |
| COM (Umum)         | Terminal pusat          | Beralih antara NO dan NC              |

**Pengkabelan dari remote control ke modul relai:**




- Kabel hitam dari tombol ON/OFF **→** NO (Biasanya Terbuka)
- Kabel merah (umum) **→** COM (Umum)



**Logika:**


Ketika ESP32 mengaktifkan relai, ini menghubungkan COM dan NO, yang persis sama dengan menekan tombol remote control.


Ketika ESP32 memutus relai, COM dan NO akan terpisah, yang setara dengan melepaskan tombol.



![remote-relay](assets/fr/10.webp)



### Langkah 3: Menghubungkan ESP32 ke modul relai



**Diagram pengkabelan:**




| **ESP32** | **→** | **Modul Relai** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Masukan)        |

**Verifikasi:**




- VCC dan GND tersambung dengan baik (polaritas)
- GPIO 21 digunakan untuk sinyal kontrol
- Tidak ada korsleting yang terlihat



![relay-esp32](assets/fr/11.webp)



**Perangkat Keras Pos Pemeriksaan**


Sebelum beralih ke perangkat lunak, centang :




- Kendali jarak jauh berkabel dengan benar
- Modul relai yang terhubung ke ESP32
- Tidak ada kabel telanjang yang menyentuh komponen lain
- 220V selalu terputus



![relay-esp32](assets/fr/12.webp)





---


## BAGIAN 2: Konfigurasi perangkat lunak



Kami akan menggunakan *Blink* sebagai contoh, tetapi *BTCPay Server* juga menawarkan *Strike, Breez dan Boltz* jika Anda lebih memilih opsi lain.



### Langkah 1: Plugin, Instalasi *BitcoinSwitch* + *Blink



1 - Masuk ke instance *BTCPay Server* Anda dengan akun admin



2 - Buat tirai pertama Anda



3 - Di sisi kiri *BTCPay Server*, gulir ke bagian bawah dan buka *"Kelola Plugin "*



![btcpay-plugins](assets/fr/13.webp)



4 - Kita akan memasang plugin *BitcoinSwitch* dan juga *Blink*



![btcpay-plugins](assets/fr/14.webp)



5 - Gulir ke bawah daftar pengaya dan klik *"Instal "*: *BitcoinSwitch dan Blink* (atau wallet yang tersedia sesuai pilihan Anda)



![btcpay-plugins](assets/fr/15.webp)



6 - Setelah penginstalan selesai, mulai ulang *BTCPay Server* dan tunggu 1 menit hingga instance dimulai ulang



![btcpay-plugins](assets/fr/16.webp)



7 - Saat Anda kembali ke *"Kelola plugin "*, periksa apakah kedua plugin telah diinstal



![btcpay-plugins](assets/fr/17.webp)



### Langkah 2: Backend: *Konfigurasi Server BTCPay + Blink*



**1 - Buat wallet *Blink***




- Kunjungi https://www.blink.sv
- Buat akun Anda. Silakan lihat tutorial :



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Hasilkan kunci API *Blink***




- Mengakses antarmuka API: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** dan masuk dengan akun yang sama dengan yang Anda gunakan untuk membuat *wallet* dan *Blink*



![blink-api](assets/fr/18.webp)





   - Setelah terhubung, buka tab *API Keys*



![blink-api](assets/fr/19.webp)





   - Klik pada *" "+" * di sudut kanan atas untuk mengakses konfigurasi Kunci API Anda



![blink-api](assets/fr/20.webp)





   - Beri nama Kunci API Anda dan biarkan pengaturan default. Kemudian, pada langkah ketiga, catat Kunci API Anda - Anda hanya akan melihatnya sekali saja: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Setelah dibuat, kunci ini akan muncul di daftar Kunci API yang aktif.



![blink-api](assets/fr/22.webp)



**3 - Hubungkan *Blink* ke *Server BTCPay***




- Buka *BTCPay Server* Anda
- Arahkan ke : *Wallet* **→** *Petir*



![btcpay-server](assets/fr/23.webp)





- Klik pada *Gunakan simpul khusus*
- Rekatkan string koneksi berikut ini:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Penting** :




- Jangan memodifikasi bagian pertama: `type = blink; server = https://api.blink.sv/graphql`;
- Ganti saja:
    - api-key= *dengan kunci API Blink* Anda
    - wallet-id= *dengan ID wallet Blink* Anda
- Kemudian klik *Test connection*, lalu *Save*



![btcpay-server](assets/fr/24.webp)





 - Periksa apakah koneksi telah dibuat (status hijau)



![btcpay-server](assets/fr/25.webp)



**4 - Membuat Point of Sale (PoS) **




- Di BTCPay Server, buka tab *Plugins* dan klik *Penjualan



![btcpay-server](assets/fr/26.webp)





- Beri nama PoS Anda dan klik *Buat*



![btcpay-server](assets/fr/27.webp)





- Konfigurasi PoS :
    - Pilih gaya titik penjualan = *Tampilan cetak*
    - Mata uang = *SATS*
    - Klik pada *SIMPAN*



![btcpay-server](assets/fr/28.webp)





- Konfigurasi produk:
    - Menghapus semua produk default
    - Kemudian klik *tambahkan item*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Mengkonfigurasi produk:
    - Judul : *mesin asap*
    - Harga: *10 sats *
    - Sakelar GPIO Bitcoin: 21
    - Durasi sakelar Bitcoin (dalam milidetik) : 5000
    - Klik *Tutup* lalu *Simpan* untuk menyimpan produk baru



![btcpay-server](assets/fr/31.webp)



### Langkah 3: Firmware: Mem-flash ESP32



**1 - Buka situs flash




- Pergi ke : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash firmware BitcoinSwitch**




- Sambungkan ESP32 ke komputer Anda dengan kabel USB/Micro-USB
- Kemudian klik *Hubungkan ke Perangkat*
- Sebuah jendela akan terbuka, pilih port USB pada ESP32 Anda, lalu klik *Connect*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Setelah ESP32 Anda terhubung, kami akan mem-flash firmware BitcoinSwitch. Pada bagian *T-Display*, klik *Upload Firmware* untuk versi terbaru yang tersedia (saat ini: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Tunggu unggahannya, prosesnya selesai ketika log menunjukkan *"Meninggalkan... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Cabut sambungan ESP32



**3 - Periksa instalasi firmware BitcoinSwitch




- Muat ulang halaman: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Sambungkan kembali ESP32 ke komputer Anda dengan kabel USB/Micro-USB
- Kemudian klik *Hubungkan ke perangkat
- Pilih port USB pada ESP32 Anda, lalu klik *Hubungkan* seperti yang dijelaskan di atas
- Setelah tersambung, tekan tombol **RESET** pada ESP32
- Periksa di log bahwa baris terakhir menunjukkan :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Ini normal, artinya belum ada konfigurasi, tetapi firmware telah diinstal)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - Menghasilkan URL WebSocket LNURL** URL



Format akhir yang diharapkan :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Langkah-langkah pembuatan :




- Buka instans Server BTCPay Anda, lalu buka PoS yang telah kita buat sebelumnya.
- Kemudian klik "View" untuk membuka PoS Anda di browser



![btcpay-server-https](assets/fr/37.webp)





- Salin URL halaman, misalnya :



![btcpay-server-https](assets/fr/38.webp)



Mari kita bongkar URL ini:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → domain instance Server BTCPay Anda
- 
- `/pos` → menunjukkan Point of Sale



Mengubahnya:




- Ganti `https://` dengan `wss://`
- Tambahkan `/bitcoinswitch` di bagian akhir



Hasil:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Simpan URL ini untuk konfigurasi di masa mendatang, karena URL ini akan memungkinkan ESP32 Anda berkomunikasi secara real time dengan Server BTCPay. Protokol WebSocket (`wss://`) membuat koneksi permanen antara keduanya: segera setelah pembayaran Lightning dikonfirmasi di PoS Anda, BTCPay langsung mengirimkan informasi tersebut ke ESP32, yang kemudian dapat memicu mesin asap Anda.



**5 - Mengkonfigurasi WiFi dan WebSocket




- Kembali ke halaman: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) dengan ESP32 Anda terhubung
- Buka *Konfigurasi Perangkat* → *Pengaturan Wi-Fi*



Menginformasikan :




- SSID WiFi: nama jaringan WiFi Anda
- Kata Sandi WiFi: kata sandi WiFi Anda



![bitcoinswitch-lnbits](assets/fr/39.webp)





- Pada bagian *LNbits Device URL*, tempelkan URL WebSocket yang telah dibuat pada langkah sebelumnya
- Klik pada *Upload konfigurasi*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Tunggu hingga unggahan selesai; log seharusnya menampilkan parameter yang baru saja Anda masukkan (SSID, kata sandi, dan URL WebSocket)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Tunggu sementara ESP32 membuat sambungan WebSocket. Anda akan melihat :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Anda sekarang dapat memutuskan sambungan ESP32



---
## Perangkat Lunak Pos Pemeriksaan



Sebelum tes akhir, periksa :





- Blink terhubung ke BTCPay
- PoS dibuat dengan setidaknya 1 item
- ESP32 di-flash dengan BitcoinSwitch
- WiFi dikonfigurasi pada ESP32
- URL WebSocket benar
- Log ESP32 yang bebas dari kesalahan



---

## Pengujian dan debugging



### Menyelesaikan tes akhir



1. Colokkan mesin asap (220V) dan nyalakan


2. Memberi daya pada ESP32 (baterai atau USB)


3. Buka PoS BTCPay Anda di browser Anda


4. Memindai item "mesin asap"


5. Bayar dengan wallet Lightning (Blink atau wallet lainnya)


6. Amati:




 - Klik relai (suara terdengar dan LED relai menyala)
 - Mesin asap diaktifkan
 - Asap yang dihasilkan!



### Masalah dan solusi keadilan




| **Masalah**                        | **Penyebab Kemungkinan**              | **Solusi**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 tidak terhubung            | Driver USB hilang             | Pasang [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relay tidak mengklik                | Kabel GPIO salah            | Periksa GPIO 21 → IN                                                                        |
| Mesin asap tidak merespons         | Kontrol jarak jauh terkabel dengan salah         | Periksa NO/NC/COM                                                                           |
| Waktu tunggu WebSocket                   | URL tidak benar                  | Periksa wss:// dan /bitcoinswitch                                                            |
| WiFi tidak terhubung             | SSID/Password salah            | Flash ulang config WiFi                                                                    |
| Pembayaran diterima tetapi tidak ada yang terjadi | ESP32 tidak terhubung ke WebSocket | Periksa log RESET                                                                      |

## Sumber daya



### Tautan yang berguna





- Firmware BitcoinSwitch: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Dokumen Server BTCPay : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- Pinout ESP32: [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Komunitas & Dukungan





- Server BTCPay** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Resmi Paling
- BTCPay Server Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Telegram resmi, komunitas aktif
- BitcoinSwitch (bug firmware)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Kode sumber





- Kode sumber firmware BitcoinSwitch: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Tumpuk sats, buatlah asap, bersenang-senanglah, tetaplah rendah hati! **⚡**