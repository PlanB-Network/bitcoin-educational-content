---
name: JoinBot
description: Memahami dan menggunakan JoinBot
---

![DALL·E – robot samurai di hutan merah, render 3D](assets/cover.webp)

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, **layanan JoinBot tidak lagi tersedia**. Saat ini, tidak lagi mungkin untuk menggunakan alat ini. Namun, Anda masih dapat melakukan Stonewall X2, tetapi Anda perlu menemukan kolaborator dan bertukar PSBT secara manual. Layanan ini mungkin akan diluncurkan kembali dalam beberapa bulan mendatang tergantung pada perkembangan kasus.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka._

---

JoinBot adalah alat baru yang ditambahkan ke suite Samourai Wallet dengan pembaruan terbaru 0.99.98f dari perangkat lunak dompet Bitcoin yang terkenal. Ini memungkinkan Anda untuk dengan mudah melakukan transaksi kolaboratif untuk mengoptimalkan privasi Anda, tanpa harus mencari pasangan.

*Terima kasih kepada Fanis Michalakis yang luar biasa atas ide menggunakan DALL-E untuk thumbnail!*

## Apa itu transaksi kolaboratif di Bitcoin?

Bitcoin didasarkan pada buku besar akun yang terdistribusi dan transparan. Siapa pun dapat melacak transaksi pengguna sistem uang elektronik ini. Untuk memastikan tingkat privasi tertentu, pengguna Bitcoin dapat melakukan transaksi dengan struktur tertentu untuk menambahkan plausible deniability dalam interpretasi mereka.

Idenya bukan untuk langsung menyembunyikan informasi, tetapi untuk membingungkannya di antara yang lain. Tujuan ini digunakan dalam Coinjoins, transaksi yang memutus sejarah sebuah koin di Bitcoin dan membuat pelacakan menjadi kompleks. Untuk mencapai hasil ini, beberapa input dan output dengan jumlah yang sama harus dibuat dalam transaksi.

Input adalah input dari transaksi Bitcoin, dan output mewakili output. Transaksi mengonsumsi inputnya untuk menciptakan output baru dengan mengubah kondisi pengeluaran sebuah koin. Mekanisme ini memungkinkan bitcoin dipindahkan antar pengguna.
Saya membahas ini secara detail dalam artikel ini: Mekanisme Transaksi Bitcoin: UTXO, Input, dan Output.

Salah satu cara untuk mengaburkan jejak dalam transaksi Bitcoin adalah dengan melakukan transaksi kolaboratif. Seperti namanya, ini melibatkan kesepakatan antara beberapa pengguna, masing-masing menyetorkan sejumlah bitcoin sebagai input dalam transaksi yang sama dan menerima sejumlah sebagai output.

Seperti disebutkan sebelumnya, struktur transaksi kolaboratif yang paling dikenal adalah Coinjoin. Misalnya, pada protokol Coinjoin Whirlpool, transaksi melibatkan 5 peserta sebagai input dan output, masing-masing dengan jumlah bitcoin yang sama.

![Diagram transaksi Coinjoin pada Whirlpool](assets/1.webp)

Pengamat eksternal dari transaksi ini akan tidak dapat mengetahui output mana yang milik pengguna mana sebagai input. Jika kita mengambil contoh pengguna #4 (ungu), kita dapat mengenali UTXO input mereka, tetapi kita tidak akan tahu mana dari 5 output yang sebenarnya milik mereka. Informasi awal tidak disembunyikan, tetapi lebih kepada dibingungkan dalam sebuah grup.
Pengguna dapat menyangkal kepemilikan UTXO tertentu sebagai output. Fenomena ini disebut "plausible deniability", dan ini memungkinkan kerahasiaan dalam transaksi Bitcoin yang transparan.

Untuk mempelajari lebih lanjut tentang Coinjoin, saya menjelaskan SEMUANYA dalam artikel panjang ini: Memahami dan menggunakan CoinJoin di Bitcoin.
Meskipun sangat efektif dalam memutus pelacakan UTXO, Coinjoin tidak cocok untuk pengeluaran langsung. Memang, strukturnya mengimplikasikan harus menggunakan input dengan jumlah yang telah ditentukan sebelumnya dan output dengan nilai yang sama (modulo biaya penambangan). Namun, transaksi pengeluaran pada Bitcoin adalah momen kritis untuk privasi karena seringkali menciptakan tautan fisik antara pengguna dan aktivitas mereka di rantai blok. Oleh karena itu, tampaknya penting untuk menggunakan alat privasi untuk pengeluaran. Ada struktur transaksi kolaboratif lain yang dirancang khusus untuk transaksi pembayaran yang sebenarnya.
## Transaksi StonewallX2

Di antara berbagai alat pengeluaran yang ditawarkan di Samourai Wallet, ada transaksi kolaboratif StonewallX2. Ini adalah mini Coinjoin antara dua pengguna yang dirancang untuk pembayaran. Dari luar, transaksi ini dapat mengarah pada beberapa interpretasi yang mungkin. Dengan demikian, ini memberikan plausible deniability dan akibatnya, kerahasiaan bagi pengguna.

Pengaturan transaksi kolaboratif StonewallX2 tersedia di Samourai Wallet dan Sparrow Wallet. Alat ini interoperable antara kedua perangkat lunak tersebut.

Mekanismenya cukup sederhana untuk dipahami. Berikut cara kerjanya dalam praktik:

> - Seorang pengguna ingin melakukan pembayaran dalam bitcoin (misalnya, kepada seorang pedagang).
> - Mereka mengambil alamat penerima dari penerima pembayaran yang sebenarnya (pedagang).
> - Mereka membuat transaksi khusus dengan beberapa input: setidaknya satu milik mereka dan satu milik kolaborator eksternal.
> - Transaksi akan memiliki 4 output, termasuk 2 dengan jumlah yang sama: satu ke alamat pedagang untuk pembayaran, satu sebagai kembalian yang kembali ke pengguna, satu output dengan nilai yang sama dengan pembayaran yang pergi ke kolaborator, dan output lain yang juga kembali ke kolaborator.

Sebagai contoh, berikut adalah transaksi StonewallX2 tipikal di mana saya melakukan pembayaran sebesar 50,125 sats. Input pertama sebesar 102,588 sats berasal dari dompet Samourai saya. Input kedua sebesar 104,255 sats berasal dari dompet kolaborator saya:

![Diagram transaksi StonewallX2](assets/2.webp)

Kita dapat mengamati 4 output, termasuk 2 dengan jumlah yang sama untuk mengaburkan jejak:

> - 50,125 sats yang pergi ke penerima pembayaran saya yang sebenarnya.
> - 52,306 sats yang mewakili kembalian saya dan oleh karena itu kembali ke alamat di dompet saya.
> - 50,125 sats yang kembali ke kolaborator saya.
> - 53,973 sats yang kembali ke kolaborator saya.
>   Di akhir operasi, kolaborator akan memiliki saldo awal mereka dipulihkan (minus biaya penambangan), dan pengguna akan telah membayar pedagang. Ini menambahkan jumlah entropi yang signifikan ke transaksi dan memutus tautan yang tidak terbantahkan antara pengirim dan penerima pembayaran.

Kekuatan transaksi StonewallX2 adalah bahwa itu sepenuhnya meniadakan salah satu aturan empiris yang digunakan oleh analis rantai: kepemilikan bersama input dalam transaksi multi-input. Dengan kata lain, dalam kebanyakan kasus, jika kita mengamati transaksi Bitcoin dengan beberapa input, kita dapat mengasumsikan bahwa semua input ini milik orang yang sama. Satoshi Nakamoto sudah mengidentifikasi masalah ini untuk privasi pengguna dalam White Paper-nya:

> "Sebagai firewall tambahan, pasangan kunci baru bisa digunakan untuk setiap transaksi untuk menjaga mereka dari dikaitkan dengan pemilik yang sama. Namun, keterkaitan tidak terhindarkan dengan transaksi multi-input, yang secara inheren mengungkapkan bahwa input mereka dimiliki oleh pemilik yang sama."

Ini adalah salah satu dari banyak aturan empiris yang digunakan dalam analisis on-chain untuk membentuk kluster alamat. Untuk mempelajari lebih lanjut tentang heuristik ini, saya merekomendasikan membaca seri empat artikel oleh Samourai, yang memperkenalkan topik ini dengan indah.
Kekuatan transaksi StonewallX2 terletak pada fakta bahwa pengamat eksternal akan berpikir bahwa input-input yang berbeda dari transaksi tersebut dimiliki oleh pemilik yang sama. Pada kenyataannya, mereka adalah dua pengguna yang berbeda yang berkolaborasi. Analisis pembayaran tersebut oleh karena itu mengarah ke pengalihan perhatian, dan privasi pengguna tetap terjaga.
Dari luar, transaksi StonewallX2 tidak dapat dibedakan dari transaksi Stonewall. Perbedaan efektif satu-satunya antara keduanya adalah Stonewall tidak bersifat kolaboratif. Ini hanya menggunakan UTXO dari satu pengguna saja. Namun, dalam struktur mereka pada buku besar akun, Stonewall dan StonewallX2 identik sempurna. Hal ini memungkinkan lebih banyak interpretasi yang mungkin dari struktur transaksi ini, karena pengamat eksternal tidak akan dapat membedakan apakah input berasal dari orang yang sama atau dari dua kolaborator.

Selain itu, keuntungan StonewallX2 dibandingkan dengan PayJoin tipe Stowaway adalah bahwa itu dapat digunakan dalam situasi apa pun. Penerima pembayaran sebenarnya tidak menyumbangkan input apa pun ke dalam transaksi. Dengan demikian, StonewallX2 dapat digunakan untuk membayar di pedagang mana pun yang menerima Bitcoin, bahkan jika pedagang tersebut tidak menggunakan Samourai atau Sparrow.
Di sisi lain, kerugian utama dari struktur transaksi ini adalah memerlukan kolaborator yang bersedia menggunakan bitcoin mereka untuk berpartisipasi dalam pembayaran Anda. Jika Anda memiliki teman bitcoin yang bersedia membantu Anda dalam situasi apa pun, ini bukan masalah. Namun, jika Anda tidak mengenal pengguna Dompet Samourai lainnya, atau jika tidak ada yang tersedia untuk berkolaborasi, maka Anda terjebak.

Untuk menyelesaikan masalah ini, tim Samourai baru-baru ini menambahkan fitur baru ke aplikasi mereka: JoinBot.

# Apa itu JoinBot?

Prinsip JoinBot sederhana. Jika Anda tidak dapat menemukan siapa pun untuk berkolaborasi dengan transaksi StonewallX2, Anda dapat berkolaborasi dengan JoinBot. Dalam praktiknya, Anda sebenarnya akan melakukan transaksi kolaboratif langsung dengan Dompet Samourai.

Layanan ini sangat nyaman, terutama bagi pengguna pemula, karena tersedia 24/7. Jika Anda perlu melakukan pembayaran mendesak dan ingin melakukan StonewallX2, Anda tidak perlu lagi menghubungi teman atau mencari kolaborator online. JoinBot akan membantu Anda.

Keuntungan lain dari JoinBot adalah bahwa UTXO yang disediakan sebagai input secara eksklusif berasal dari Whirlpool postmix, yang meningkatkan privasi pembayaran Anda. Selain itu, karena JoinBot selalu online, Anda harus berkolaborasi dengan UTXO yang memiliki Anonset prospektif yang besar.

Tentu saja, JoinBot memiliki beberapa kompromi yang harus diperhatikan:

> Seperti dengan StonewallX2 klasik, kolaborator Anda tentu saja mengetahui UTXO yang digunakan dan tujuannya. Dalam kasus JoinBot, Samourai mengetahui detail transaksi ini. Ini bukan hal yang buruk, tetapi harus diingat.
> Untuk menghindari spam, Samourai membebankan biaya layanan 3,5% dari jumlah transaksi sebenarnya, dengan batas maksimum 0,01 BTC. Misalnya, jika saya mengirim pembayaran nyata sebesar 100 kilosat dengan JoinBot, jumlah biaya layanan akan menjadi 3.500 sat.
> Untuk menggunakan JoinBot, Anda harus memiliki setidaknya dua UTXO yang tidak terkait dan tersedia di dompet Anda.
> Dalam StonewallX2 klasik, biaya penambangan dibagi rata antara dua kolaborator. Dengan JoinBot, Anda jelas harus membayar seluruh biaya penambangan.
Agar transaksi JoinBot persis sama dengan transaksi StonewallX2 atau Stonewall klasik, pembayaran biaya layanan dilakukan dalam transaksi yang sepenuhnya terpisah. Pengembalian setengah dari biaya penambangan yang awalnya dibayarkan oleh Samourai akan dilakukan selama transaksi kedua ini. Untuk mengoptimalkan privasi Anda sampai akhir, penyelesaian biaya dilakukan menggunakan transaksi terstruktur Stowaway (PayJoin).

## Bagaimana cara menggunakan JoinBot?

Untuk melakukan transaksi JoinBot, Anda harus memiliki Samourai Wallet. Anda dapat mengunduhnya di sini, atau dari Google Playstore.

Berbeda dengan sebagian besar alat yang dikembangkan oleh Samourai, Sparrow Wallet belum mengumumkan implementasi JoinBot. Alat ini oleh karena itu hanya tersedia di Samourai.

Temukan langkah demi langkah cara melakukan transaksi StonewallX2 dengan JoinBot dalam video ini:

![Cara menggunakan Joinbot](https://youtu.be/80MoMz2Ne5g)

Berikut adalah diagram transaksi yang baru saja kami lakukan dalam video:

![Diagram transaksi StonewallX2 saya dengan JoinBot.](assets/3.webp)

Kita dapat melihat 5 input:

> - 3 input sebesar 100 kilosat datang dari Samourai (JoinBot).
> - 2 input datang dari dompet pribadi saya, sebesar 3,524 sats dan 1.8 megasat.

Keempat output dari transaksi adalah sebagai berikut:

> - 1 sebesar 212,452 sats ke penerima pembayaran saya yang sebenarnya.
> - Satu lagi dengan jumlah yang sama yang kembali ke alamat Samourai.
> - 1 kembalian yang juga kembali ke Samourai sebesar 87,302 sats. Ini mewakili perbedaan antara total input mereka (300,000 sats) dan output pengaburan (212,452 sats) dikurangi biaya penambangan.
> - 1 kembalian yang kembali ke alamat lain di dompet saya. Ini mewakili perbedaan antara total input saya dan pembayaran sebenarnya, dikurangi biaya penambangan.

Sebagai pengingat, biaya penambangan tidak mewakili output transaksi. Mereka hanya mewakili perbedaan antara total input dan total output.

## Kesimpulan

JoinBot adalah alat tambahan yang menambah lebih banyak pilihan dan kebebasan bagi pengguna Samourai. Ini memungkinkan transaksi StonewallX2 kolaboratif langsung dengan Samourai sebagai kolaborator. Jenis transaksi ini membantu meningkatkan privasi pengguna.

Jika Anda dapat melakukan StonewallX2 klasik dengan teman, saya masih merekomendasikan menggunakan alat ini. Namun, jika Anda terjebak dan tidak dapat menemukan kolaborator untuk melakukan pembayaran, Anda tahu bahwa JoinBot akan tersedia 24/7 untuk berkolaborasi dengan Anda.

**Sumber eksternal:**
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin