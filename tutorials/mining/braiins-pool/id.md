---
name: Braiins Pool

description: Pengenalan Braiins Pool
---

![signup](assets/cover.webp)

Braiins Pool, yang sebelumnya dikenal sebagai Slush Pool, merupakan pool penambangan Bitcoin pertama. pool ini didirikan pada November 2010 dan berhasil menambang blok pertamanya pada 16 Desember 2010, yaitu blok 97834.

Per Mei 2024, Braiins Pool memiliki kekuatan komputasi sebesar 13 EH/s, yang mewakili sekitar 1,8% dari total hashrate Bitcoin. Pool ini telah menambang total 1.307.188 bitcoin, atau sekitar 6% dari batas maksimum 21 juta bitcoin yang akan pernah ada.

### Sistem Kompensasi

Sejak akhir 2023, Braiins Pool telah mengubah sistem kompensasinya dengan mengadopsi FPPS (Full Pay Per Share). Artinya, penambang menerima pembayaran harian untuk seluruh pekerjaan yang mereka lakukan pada hari sebelumnya, bahkan jika pool tersebut tidak menemukan blok. Hal ini berbeda dari sistem sebelumnya, di mana penambang hanya menerima imbalan ketika pool berhasil menemukan blok.

**Penting untuk dicatat, [menurut sebuah tweet oleh Mononaut](https://x.com/mononautical/status/1777686545715089605) yang menganalisis Bitcoin TimeChain, bahwa banyak pool penambangan yang menggunakan sistem FPPS akan mengirimkan bitcoin yang ditambang ke alamat AntPool, yang berarti bahwa AntPool mengontrol hashrate dari semua pool ini, sekitar 47% dari hashrate Bitcoin global. Ini adalah berita buruk bagi desentralisasi jaringan.**

### Biaya Pool

Biaya untuk Braiins Pool adalah 2,5%, namun, jika kamu menggunakan BraiinsOS pada mesin kamu biayanya akan 0%

### Penarikan

**Penarikan Lightning**
Penarikan Lightning memungkinkan kamu untuk menarik hadiah kamu tanpa jumlah minimum sekali sehari melalui alamat Lightning.
Untuk menggunakan metode ini, kamu harus memiliki dompet yang kompatibel dengan alamat Lightning.

**Penarikan On-Chain**
Penarikan On-Chain dibatasi pada jumlah minimum dan mungkin dikenakan biaya.
Jumlah minimum: 20.000 sats
Biaya: 10.000 sats untuk jumlah kurang dari 500.000 sats
Gratis untuk jumlah di atas 500.000 sats
Penarikan dapat dipicu oleh interval waktu atau oleh jumlah.

## Pembuatan Akun

Untuk mulai menggunakan Braiins Pool [kunjungi situs web mereka](https://braiins.com/pool) dan klik "SIGN UP" di pojok kanan atas


![signup](assets/3.webp)

Masukkan informasi Anda dan validasi, Anda kemudian akan menerima email yang meminta konfirmasi alamat kamu. Konfirmasi dengan link dalam email yang kamu terima dan kemudian masuk ke platform

![signup](assets/4.webp)


## Menambahkan "worker"
Worker adalah penambang yang akan kamu hubungkan ke kolam. Untuk menambahkan penambang baru, klik pada "Workers" di menu sidebar kiri.
![signup](assets/7.webp)

Kemudian klik tombol "Connect Workers +" berwarna ungu.

Di jendela ini, pilih area geografis Anda.

Jika penambang yang ingin kamu hubungkan menggunakan BraiinsOS, pilih protokol "Stratum V2". Jika tidak, pilih "Stratum V1".

![signup](assets/8.webp)

Kamu akan memiliki informasi untuk dimasukkan pada halaman web penambang Anda (rujuk dokumentasi penambang kamu untuk mengetahui di mana memasukkan informasi ini).

Di sini, **"stratum+tcp://eu.stratum.braiins.com:3333"** adalah URL kolam.
**JimZap.workerName** adalah pengenal kamu dan nama penambang kamu, di mana JimZap adalah pengenal dan .workerName adalah nama penambang. Jika kamu memiliki beberapa penambang, kamu dapat memberi mereka nama yang sama, dalam hal ini kekuatan komputasi mereka akan dijumlahkan bersama di dashboard, atau beri mereka nama yang berbeda untuk memantau mereka secara individu.
Dan kata sandinya selalu sama **"anything123"**

Setelah kamu memasukkan informasi ini di halaman web penambang kamu dan telah mulai menambang, kamu akan melihatnya muncul setelah beberapa menit di Dashboard Braiins Pool.

## Ikhtisar Dashboard

![signup](assets/9.webp)

Di banner atas, kamu dapat melihat rata-rata total hashrate dari semua penambang kamu selama 5 menit, 1 jam, dan 24 jam. Dan ringkasan jumlah penambang yang online atau offline.
Di bawahnya, sebuah grafik memungkinkan kamu untuk mengikuti evolusi kekuatan komputasi kamu.

![signup](assets/10.webp)

Di bawah grafik ini, Anda memiliki beberapa informasi tentang hadiah kamu dalam sats.

**"Hadiah Penambangan Hari Ini"** Menunjukkan jumlah sats yang Anda tambang hari ini. Di akhir hari, nilai ini akan diatur ulang menjadi 0 dan sats akan dikirim ke akun kamu.

**"Total Hadiah Kemarin"** Jumlah sats yang kamu tambang hari sebelumnya

**"Est. Profitabilitas (1 TH/s)"** Ini adalah perkiraan jumlah sats yang kamu peroleh dalam satu hari untuk kekuatan komputasi 1 TH/s. Sebagai contoh, jika nilainya adalah 77 sats dan kamu memiliki kekuatan komputasi 10 TH/s yang berjalan terus-menerus sepanjang hari, maka secara teoritis kamu akan mendapatkan 77 x 10 = 770 sats per hari.

**"Hadiah Sepanjang Waktu"** Total sats yang kamu telah tambang dengan Braiins Pool

**"Skema Hadiah"** Tarif biaya yang diterapkan oleh pool

**"Perkiraan Waktu Pembayaran Selanjutnya"** Perkiraan waktu yang akan dibutuhkan sebelum kamu dapat menarik sats dari platform. Di sini, perkiraan tidak menunjukkan apa-apa karena penambangan baru saja berlangsung selama beberapa menit.

**"Saldo Akun"** Jumlah sats yang tersedia di akun kamu, yang kemudian dapat kamu tarik.
## Menyiapkan Penarikan
Kamu dapat menarik hadiah kamu baik secara on-chain maupun melalui lightning dengan alamat.

Di bagian atas, klik pada "Funds". Secara default, kamu memiliki "Akun Bitcoin". Kamu dapat membuat yang lain untuk membagi hadiah. Kami akan kembali ke ini di bagian selanjutnya.

Untuk sekarang, klik pada "Set up".

![signup](assets/17.webp)

Di jendela baru ini, Anda dapat memilih "Onchain payout".

Namai dompet ini, berikan alamat BTC, dan pilih jenis pemicu yang kamu inginkan. "Threshold" berarti pembayaran akan dipicu ketika kamu telah mengumpulkan jumlah BTC yang ditentukan, dan dengan "Interval Waktu", pembayaran akan dipicu pada interval reguler (hari/minggu/bulan).

Perhatikan bahwa jumlah minimum adalah 0.0002 BTC dan bahwa di bawah 0.005 BTC, biaya sebesar 0.0001 BTC akan diterapkan.

![signup](assets/18.webp)

Jika kamu ingin menggunakan penarikan Lightning, kamu akan memerlukan dompet yang menyediakan alamat Lightning. Sebagai contoh, kamu dapat menggunakan getAlby.

Klik di bagian atas jendela pada "Lightning payout".

Masukkan alamat Lightning Anda dan centang kotak "Saya mengerti..." kemudian validasi.

Dengan metode penarikan ini, hadiah akan dikirim ke dompet kamu setiap hari.

![signup](assets/14.webp)
Setelah kamu memvalidasi pengaturan pembayaran, kamu akan menerima email konfirmasi.
![signup](assets/15.webp)

## Berbagi Hadiah

Braiins Pool juga memungkinkan kamu untuk berbagi hadiah kamu ke beberapa dompet.

Untuk melakukan ini, klik di bagian atas pada "Mining" kemudian di sebelah kiri pada "Settings".

![signup](assets/19.webp)

Di halaman ini, kamu dapat menambahkan "Financial Account" lain dengan mengklik "Add Another Financial Account" dan mendistribusikan hadiah kamu dalam % ke berbagai akun tersebut yang harus kamu asosiasikan dengan sebuah dompet. Untuk mengasosiasikan dompet baru dengan Financial Account, silakan lihat bagian sebelumnya.
