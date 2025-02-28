---
name: Boltzmann Calculator
description: Memahami konsep entropi dan cara menggunakan Boltzmann
---
![cover](assets/cover.webp)

***PERINGATAN:** Menyusul penangkapan para pendiri Samourai Wallet dan penyitaan server mereka pada tanggal 24 April, situs web KYCP.org saat ini tidak dapat diakses. Gitlab yang menyimpan kode Kalkulator Boltzmann Python juga telah disita. Saat ini, tidak lagi mungkin untuk mengunduh alat ini. Namun, ada kemungkinan kode tersebut dapat dipublikasikan kembali oleh pihak lain dalam beberapa minggu mendatang. Sementara itu, Anda masih dapat memanfaatkan tutorial ini untuk memahami cara kerja Kalkulator Boltzmann. Indikator yang disediakan oleh alat ini berlaku untuk setiap transaksi Bitcoin dan juga dapat dihitung secara manual. Saya akan menyediakan semua perhitungan yang diperlukan dalam tutorial ini. Jika Anda telah mengunduh alat Python di mesin Anda atau jika Anda menggunakan RoninDojo, Anda dapat terus menggunakan alat tersebut dan mengikuti tutorial ini seperti biasa, itu masih berfungsi.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka._

---

Kalkulator Boltzmann adalah alat untuk menganalisis transaksi Bitcoin dengan mengukur tingkat entropinya bersama dengan metrik lanjutan lainnya. Alat ini memberikan wawasan tentang hubungan antara input dan output dari sebuah transaksi. Indikator-indikator ini menawarkan penilaian kuantitatif tentang privasi transaksi dan membantu mengidentifikasi potensi kesalahan.

Alat Python ini dikembangkan oleh tim di Samourai Wallet dan OXT, tetapi dapat digunakan pada transaksi Bitcoin apa pun.

## Bagaimana cara menggunakan Kalkulator Boltzmann?
Untuk menggunakan Kalkulator Boltzmann, ada dua opsi yang tersedia untuk Anda. Yang pertama adalah menginstal alat Python langsung di mesin Anda. Sebagai alternatif, Anda dapat memilih situs web KYCP.org (_Know Your Coin Privacy_), yang menawarkan platform penggunaan yang disederhanakan. Untuk pengguna [RoninDojo](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8), perhatikan bahwa alat ini sudah terintegrasi ke dalam node Anda.

Menggunakan situs KYCP cukup mudah: cukup masukkan identifikasi transaksi (TXID) yang ingin Anda analisis ke dalam bilah pencarian dan tekan `ENTER`.
![KYCP](assets/1.webp)
Anda kemudian akan menemukan informasi berbeda tentang transaksi, termasuk tautan antara input dan output. Klik pada `deterministic links`.
![KYCP](assets/2.webp)
Anda akan tiba di halaman yang didedikasikan untuk indikator Kalkulator Boltzmann.
![KYCP](assets/3.webp)
Bagi mereka yang lebih suka menggunakan alat tersebut langsung dari node RoninDojo mereka, alat ini dapat diakses melalui `RoninCLI > Samourai Toolkit > Kalkulator Boltzmann`.

Seperti halnya situs KYCP.org, setelah alat Python diinstal, Anda hanya perlu menempelkan TXID dari transaksi yang ingin Anda analisis.

![KYCP](assets/7.webp)

Kemudian, tekan tombol `ENTER` untuk mendapatkan hasilnya.

![KYCP](assets/8.webp)

## Apa saja indikator dari Kalkulator Boltzmann?
### Kombinasi / Interpretasi:
Indikator pertama yang dihitung oleh perangkat lunak adalah jumlah total kombinasi yang mungkin, ditunjukkan di bawah `nb combinations` atau `interpretations` dalam alat tersebut.
Mengingat nilai-nilai UTXO yang terlibat dalam transaksi, indikator ini menghitung jumlah cara di mana input dapat dikaitkan dengan output. Dengan kata lain, ini menentukan jumlah interpretasi yang masuk akal yang dapat ditimbulkan dari transaksi dari perspektif pengamat eksternal yang menganalisisnya. Sebagai contoh, sebuah coinjoin yang terstruktur menurut model Whirlpool 5x5 menampilkan `1,496` kombinasi yang mungkin: ![KYCP](assets/4.webp)
Sebaliknya, sebuah Whirlpool Surge Cycle 8x8 coinjoin, menampilkan `9,934,563` interpretasi yang mungkin: ![KYCP](assets/5.webp)
Sebaliknya, transaksi tradisional dengan 1 input dan 2 output hanya akan menampilkan satu interpretasi: ![KYCP](assets/6.webp)

### Entropy:
Indikator kedua yang dihitung adalah entropi dari sebuah transaksi, yang ditandai dengan `Entropy`.

Dalam konteks umum kriptografi dan informasi, entropi adalah ukuran kuantitatif dari ketidakpastian atau ketidakdugaan yang terkait dengan sumber data atau proses acak. Dengan kata lain, entropi adalah cara mengukur seberapa sulit informasi untuk diprediksi atau ditebak.

Dalam konteks khusus analisis rantai, entropi juga merupakan nama dari sebuah indikator, yang berasal dari entropi Shannon dan [ditemukan oleh LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), yang dihitung dengan alat Boltzmann.

Ketika sebuah transaksi menampilkan jumlah kombinasi yang tinggi, seringkali lebih relevan untuk merujuk pada entropinya. Indikator ini memungkinkan pengukuran kurangnya pengetahuan analis tentang konfigurasi tepat dari transaksi. Dengan kata lain, semakin tinggi entropi, semakin sulit tugas mengidentifikasi pergerakan bitcoin antara input dan output menjadi bagi analis.

Dalam praktik, entropi mengungkapkan apakah, dari perspektif pengamat eksternal, sebuah transaksi menampilkan beberapa interpretasi yang mungkin, hanya berdasarkan jumlah input dan output, tanpa mempertimbangkan pola dan heuristik eksternal atau internal lainnya. Entropi yang tinggi kemudian sinonim dengan kerahasiaan yang lebih baik untuk transaksi.

Entropi didefinisikan sebagai logaritma biner dari jumlah kombinasi yang mungkin. Berikut adalah rumus yang digunakan:
```plaintext
E: entropi dari transaksi
C: jumlah kombinasi yang mungkin untuk transaksi

E = log2(C)
```

Dalam matematika, logaritma biner (logaritma basis-2) sesuai dengan operasi invers dari memangkatkan 2. Dengan kata lain, logaritma biner dari `x` adalah eksponen yang harus `2` dinaikkan untuk mendapatkan `x`. Indikator ini dengan demikian dinyatakan dalam bit.

Mari kita ambil contoh perhitungan entropi untuk transaksi coinjoin yang terstruktur menurut model Whirlpool 5x5, yang, seperti disebutkan sebelumnya, menawarkan sejumlah kombinasi yang mungkin sebanyak `1,496`:
```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bit
```
Dengan demikian, transaksi coinjoin ini menampilkan entropi sebesar `10.5469 bit`, yang dianggap sangat memuaskan. Semakin tinggi nilai ini, semakin banyak interpretasi yang berbeda yang diakui oleh transaksi, sehingga memperkuat tingkat privasinya.
Untuk transaksi coinjoin 8x8 yang menampilkan `9,934,563` interpretasi, entropinya akan menjadi:
```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bit
```
Mari kita ambil contoh lain dengan transaksi konvensional yang lebih umum, yang memiliki satu input dan dua output: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) Dalam kasus transaksi ini, satu-satunya interpretasi yang mungkin adalah: `(In.0) > (Out.0 ; Out.1)`. Akibatnya, entropinya ditetapkan pada `0`:
```plaintext
C = 1
E = log2(1)
E = 0 bit
```

### Efisiensi:
Indikator ketiga yang disediakan oleh Kalkulator Boltzmann dinamakan `Efisiensi Dompet`. Indikator ini menilai efisiensi transaksi dengan membandingkannya dengan transaksi optimal yang dapat dibayangkan dalam konfigurasi yang identik.

Hal ini membawa kita untuk membahas konsep entropi maksimum, yang sesuai dengan entropi tertinggi yang secara teoritis bisa dicapai oleh struktur transaksi tertentu. Efisiensi transaksi kemudian dihitung dengan menghadapkan entropi maksimum ini dengan entropi aktual dari transaksi yang dianalisis.

Rumus yang digunakan adalah sebagai berikut:
```plaintext
ER: entropi aktual dari transaksi yang dinyatakan dalam bit
EM: entropi maksimum yang mungkin untuk struktur transaksi tertentu yang dinyatakan dalam bit
Ef: efisiensi dari transaksi dalam bit

Ef = ER - EM
```

Sebagai contoh, untuk struktur coinjoin Whirlpool 5x5, entropi maksimum ditetapkan pada `10.5469`:
```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bit
```

Indikator ini juga dinyatakan sebagai persentase, rumusnya kemudian adalah:
```plaintext
CR: jumlah kombinasi yang mungkin aktual
CM: jumlah maksimum kombinasi yang mungkin dengan struktur yang sama
Ef: efisiensi yang dinyatakan sebagai persentase

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```

Sebuah efisiensi sebesar `100%` menunjukkan bahwa transaksi memaksimalkan potensinya untuk privasi sesuai dengan strukturnya.

### Kepadatan Entropi:
Indikator keempat adalah kepadatan entropi, dicatat pada alat `Kepadatan Entropi`. Ini memberikan perspektif tentang entropi relatif terhadap setiap input atau output dari transaksi. Indikator ini berguna untuk mengevaluasi dan membandingkan efisiensi transaksi dengan ukuran yang berbeda. Untuk menghitungnya, cukup bagi total entropi transaksi dengan total jumlah input dan output yang terlibat:
```plaintext
ED: kepadatan entropi yang dinyatakan dalam bit
E: entropi dari transaksi yang dinyatakan dalam bit
T: total jumlah input dan output dalam transaksi

ED = E / T
```

Mari kita ambil contoh coinjoin Whirlpool 5x5:
```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bit
```

Mari kita juga hitung kepadatan entropi untuk coinjoin Whirlpool 8x8:
```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bit
```
Informasi kelima yang disampaikan oleh Kalkulator Boltzmann adalah tabel probabilitas kecocokan antara input dan output. Tabel ini menunjukkan, melalui skor Boltzmann, probabilitas bersyarat bahwa input tertentu terkait dengan output tertentu.
Ini merupakan ukuran kuantitatif dari probabilitas bersyarat bahwa sebuah asosiasi antara input dan output dalam sebuah transaksi terjadi, berdasarkan rasio jumlah kejadian yang menguntungkan dari peristiwa ini terhadap jumlah total kemungkinan kejadian, dalam satu set interpretasi.

Mengambil contoh coinjoin Whirlpool lagi, tabel probabilitas bersyarat akan menyoroti peluang keterkaitan antara setiap input dan output, memberikan ukuran kuantitatif dari ambiguitas asosiasi dalam transaksi:

| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Di sini, kita dapat dengan jelas melihat bahwa setiap input memiliki peluang yang sama untuk dikaitkan dengan output mana pun, yang meningkatkan kerahasiaan transaksi.
Menghitung skor Boltzmann melibatkan pembagian jumlah interpretasi di mana suatu peristiwa terjadi dengan jumlah total interpretasi yang tersedia. Jadi, untuk menentukan skor yang mengasosiasikan input No. 0 dengan output No. 3 (`512` interpretasi), prosedur berikut digunakan:
```plaintext
Interpretasi (IN.0 > OUT.3) = 512
Total Interpretasi = 1496
Skor = 512 / 1496 = 34%
```

Mengambil contoh coinjoin Whirlpool 8x8 (siklus surge), tabel Boltzmann akan terlihat seperti ini:

|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Namun, dalam kasus transaksi sederhana dengan satu input dan dua output, situasinya berbeda:

| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Di sini, diamati bahwa probabilitas untuk setiap output berasal dari input No. 0 adalah `100%`. Probabilitas yang lebih rendah dengan demikian berarti privasi yang lebih besar dengan mengencerkan tautan langsung antara input dan output.

### Tautan Deterministik:
Informasi keenam yang diberikan adalah jumlah tautan deterministik, dilengkapi dengan rasio dari tautan ini. Indikator ini mengungkapkan berapa banyak koneksi antara input dan output dalam transaksi yang dianalisis adalah tidak dapat disangkal, dengan probabilitas `100%`. Rasio, di sisi lain, menawarkan perspektif tentang bobot tautan deterministik ini dalam keseluruhan set tautan transaksi.
Misalnya, transaksi coinjoin tipe Whirlpool tidak memiliki tautan deterministik, dan oleh karena itu menampilkan indikator dan rasio `0%`. Sebaliknya, dalam transaksi sederhana kedua yang kami periksa (dengan satu input dan dua output), indikatornya ditetapkan pada `2` dan rasionya mencapai `100%`. Dengan demikian, indikator nol menandakan kerahasiaan yang sangat baik karena tidak adanya tautan langsung dan tidak dapat disangkal antara input dan output.

**Sumber Eksternal:**

- Kode Boltzmann di Samourai
- [Transaksi Bitcoin & Privasi (Bagian I) oleh Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Transaksi Bitcoin & Privasi (Bagian II) oleh Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Transaksi Bitcoin & Privasi (Bagian III) oleh Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- Situs Web KYCP
- [Artikel Medium tentang Pengenalan Skrip Boltzmann oleh Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)