---
name: Braiins Pool

description: Pengenalan Braiins Pool
---

![signup](assets/cover.webp)

Braiins Pool, yang sebelumnya dikenal sebagai Slush Pool, adalah kolam penambangan Bitcoin pertama. Didirikan pada November 2010, kolam ini menambang blok pertamanya pada 16 Desember 2010, blok 97834.

Per Mei 2024, Braiins Pool memiliki kekuatan komputasi sebesar 13 EH/s, yang mewakili sekitar 1,8% dari total hashrate Bitcoin. Kolam ini telah menambang total 1.307.188 bitcoin, yang kira-kira 6% dari maksimum 21 juta bitcoin yang akan pernah ada.

### Sistem Kompensasi

Sejak akhir 2023, Braiins Pool telah mengubah sistem kompensasinya untuk mengadopsi sistem FPPS (Full Pay Per Share). Ini berarti bahwa penambang menerima hadiah setiap hari untuk seluruh pekerjaan mereka dari hari sebelumnya, bahkan jika kolam tidak menemukan blok. Ini berbeda dari sistem lama di mana penambang hanya menerima hadiah ketika kolam menemukan blok.

**Penting untuk dicatat, [menurut sebuah tweet oleh Mononaut](https://x.com/mononautical/status/1777686545715089605) yang menganalisis Bitcoin TimeChain, bahwa banyak kolam penambangan yang menggunakan sistem FPPS akan mengirimkan bitcoin yang ditambang ke alamat AntPool, yang berarti bahwa AntPool mengontrol hashrate dari semua kolam ini, sekitar 47% dari hashrate Bitcoin global. Ini adalah berita buruk bagi desentralisasi jaringan.**

### Biaya Kolam

Biaya untuk Braiins Pool adalah 2,5%, namun, jika Anda menggunakan BraiinsOS pada mesin Anda biayanya akan 0%

### Penarikan

**Penarikan Lightning**
Penarikan Lightning memungkinkan Anda untuk menarik hadiah Anda tanpa jumlah minimum sekali sehari melalui alamat Lightning.
Untuk menggunakan metode ini, Anda harus memiliki dompet yang kompatibel dengan alamat Lightning.

**Penarikan On-Chain**
Penarikan On-Chain dibatasi pada jumlah minimum dan mungkin dikenakan biaya.
Jumlah minimum: 20.000 sats
Biaya: 10.000 sats untuk jumlah kurang dari 500.000 sats
Gratis untuk jumlah di atas 500.000 sats
Penarikan dapat dipicu oleh interval waktu atau oleh jumlah.

## Pembuatan Akun

Untuk mulai menggunakan Braiins Pool [kunjungi situs web mereka](https://braiins.com/pool) dan klik "SIGN UP" di pojok kanan atas


![signup](assets/3.webp)

Masukkan informasi Anda dan validasi, Anda kemudian akan menerima email yang meminta konfirmasi alamat Anda. Konfirmasi dengan link dalam email yang Anda terima dan kemudian masuk ke platform

![signup](assets/4.webp)


## Menambahkan "worker"
Worker adalah penambang yang akan Anda hubungkan ke kolam. Untuk menambahkan penambang baru, klik pada "Workers" di menu sidebar kiri.
![signup](assets/7.webp)

Kemudian klik tombol "Connect Workers +" berwarna ungu.

Di jendela ini, pilih area geografis Anda.

Jika penambang yang ingin Anda hubungkan menggunakan BraiinsOS, pilih protokol "Stratum V2". Jika tidak, pilih "Stratum V1".

![signup](assets/8.webp)

Anda akan memiliki informasi untuk dimasukkan pada halaman web penambang Anda (rujuk dokumentasi penambang Anda untuk mengetahui di mana memasukkan informasi ini).

Di sini, **"stratum+tcp://eu.stratum.braiins.com:3333"** adalah URL kolam.
**JimZap.workerName** adalah pengenal Anda dan nama penambang Anda, di mana JimZap adalah pengenal dan .workerName adalah nama penambang. Jika Anda memiliki beberapa penambang, Anda dapat memberi mereka nama yang sama, dalam hal ini kekuatan komputasi mereka akan dijumlahkan bersama di dashboard, atau beri mereka nama yang berbeda untuk memantau mereka secara individu.
Dan kata sandinya selalu sama **"anything123"**

Setelah Anda memasukkan informasi ini di halaman web penambang Anda dan telah mulai menambang, Anda akan melihatnya muncul setelah beberapa menit di Dashboard Braiins Pool.

## Ikhtisar Dashboard

![signup](assets/9.webp)

Di banner atas, Anda dapat melihat rata-rata total hashrate dari semua penambang Anda selama 5 menit, 1 jam, dan 24 jam. Dan ringkasan jumlah penambang yang online atau offline.
Di bawahnya, sebuah grafik memungkinkan Anda untuk mengikuti evolusi kekuatan komputasi Anda.

![signup](assets/10.webp)

Di bawah grafik ini, Anda memiliki beberapa informasi tentang hadiah Anda dalam sats.

**"Hadiah Penambangan Hari Ini"** Menunjukkan jumlah sats yang Anda tambang hari ini. Di akhir hari, nilai ini akan diatur ulang menjadi 0 dan sats akan dikirim ke akun Anda.

**"Total Hadiah Kemarin"** Jumlah sats yang Anda tambang hari sebelumnya

**"Est. Profitabilitas (1 TH/s)"** Adalah perkiraan jumlah sats yang Anda peroleh dalam satu hari untuk kekuatan komputasi 1 TH/s. Sebagai contoh, jika nilainya adalah 77 sats, dan Anda memiliki kekuatan komputasi 10 TH/s secara terus-menerus sepanjang hari, maka secara teoritis Anda akan mendapatkan 77 x 10 = 770 sats per hari.

**"Hadiah Sepanjang Waktu"** Total sats yang Anda telah tambang dengan Braiins Pool

**"Skema Hadiah"** Tarif biaya yang diterapkan oleh pool

**"Perkiraan Waktu Pembayaran Selanjutnya"** Perkiraan waktu yang akan dibutuhkan sebelum Anda dapat menarik sats dari platform. Di sini, perkiraan tidak menunjukkan apa-apa karena penambangan baru saja berlangsung selama beberapa menit.

**"Saldo Akun"** Jumlah sats yang tersedia di akun Anda, yang kemudian dapat Anda tarik.
## Menyiapkan Penarikan
Anda dapat menarik hadiah Anda baik secara on-chain maupun melalui lightning dengan alamat.

Di bagian atas, klik pada "Funds". Secara default, Anda memiliki "Akun Bitcoin". Anda dapat membuat yang lain untuk membagi hadiah. Kami akan kembali ke ini di bagian selanjutnya.

Untuk sekarang, klik pada "Set up".

![signup](assets/17.webp)

Di jendela baru ini, Anda dapat memilih "Onchain payout".

Namai dompet ini, berikan alamat BTC, dan pilih jenis pemicu yang Anda inginkan. "Threshold" berarti pembayaran akan dipicu ketika Anda telah mengumpulkan jumlah BTC yang ditentukan, dan dengan "Interval Waktu", pembayaran akan dipicu pada interval reguler (hari/minggu/bulan).

Perhatikan bahwa jumlah minimum adalah 0.0002 BTC dan bahwa di bawah 0.005 BTC, biaya sebesar 0.0001 BTC akan diterapkan.

![signup](assets/18.webp)

Jika Anda ingin menggunakan penarikan Lightning, Anda akan memerlukan dompet yang menyediakan alamat Lightning. Sebagai contoh, Anda dapat menggunakan getAlby.

Klik di bagian atas jendela pada "Lightning payout".

Masukkan alamat Lightning Anda dan centang kotak "Saya mengerti..." kemudian validasi.

Dengan metode penarikan ini, hadiah Anda akan dikirim ke dompet Anda setiap hari.

![signup](assets/14.webp)
Setelah Anda memvalidasi pengaturan pembayaran Anda, Anda akan menerima email konfirmasi.
![signup](assets/15.webp)

## Berbagi Hadiah

Braiins Pool juga memungkinkan Anda untuk berbagi hadiah Anda ke beberapa dompet.

Untuk melakukan ini, klik di bagian atas pada "Mining" kemudian di sebelah kiri pada "Settings".

![signup](assets/19.webp)

Di halaman ini, Anda akan dapat menambahkan "Financial Account" lain dengan mengklik pada "Add Another Financial Account" dan mendistribusikan hadiah Anda dalam % ke berbagai akun tersebut yang harus Anda asosiasikan dengan sebuah dompet. Untuk mengasosiasikan dompet baru dengan Financial Account, lihat pada bagian sebelumnya.