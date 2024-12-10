---
name: Stonewall
description: Memahami dan menggunakan transaksi Stonewall
---
![cover stonewall](assets/cover.webp)

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, penggunaan aplikasi Samourai Wallet kini memerlukan koneksi ke Dojo milik Anda sendiri agar dapat berfungsi dengan baik. Selain itu, transaksi Stonewall sama sekali tidak terpengaruh dan masih dapat dilakukan tanpa masalah. Memang, jenis transaksi ini dilakukan secara otomatis, tanpa perlu kolaborasi eksternal atau koneksi melalui Soroban.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang berhubungan. Yakinlah bahwa kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna adalah untuk mematuhi hukum di yurisdiksi mereka._

---

> *"Pecahkan asumsi analisis blockchain dengan keraguan yang dapat dibuktikan secara matematis antara pengirim dan penerima transaksi Anda."*

## Apa itu transaksi Stonewall?
Stonewall adalah bentuk khusus dari transaksi Bitcoin yang bertujuan untuk meningkatkan privasi pengguna selama transaksi dengan meniru coinjoin antara dua pihak, tanpa benar-benar menjadi satu. Faktanya, transaksi ini tidak kolaboratif. Seorang pengguna dapat membangunnya sendiri, hanya melibatkan UTXO mereka sendiri sebagai input. Oleh karena itu, Anda dapat membuat transaksi Stonewall untuk setiap kesempatan tanpa perlu berkoordinasi dengan pengguna lain.

Operasi transaksi Stonewall adalah sebagai berikut: sebagai input, pengirim menggunakan 2 UTXO yang milik mereka. Sebagai output, transaksi menghasilkan 4 output, termasuk 2 yang akan berjumlah sama persis. 2 lainnya akan menjadi kembalian. Di antara 2 output dengan jumlah yang sama, hanya satu yang sebenarnya akan pergi ke penerima pembayaran.

Hanya ada 2 peran dalam transaksi Stonewall:
- Pengirim, yang melakukan pembayaran sebenarnya;
- Penerima, yang mungkin tidak menyadari sifat khusus dari transaksi dan hanya mengharapkan pembayaran dari pengirim.

Mari kita ambil contoh untuk memahami struktur transaksi ini. Alice berada di toko roti untuk membeli baguette-nya, yang harganya `4,000 sats`. Dia ingin membayar dengan bitcoin sambil mempertahankan tingkat privasi tertentu dalam pembayarannya. Oleh karena itu, dia memutuskan untuk membuat transaksi Stonewall untuk pembayaran tersebut.
![transaction stonewall bakery](assets/en/1.webp)
Menganalisis transaksi ini, kita dapat melihat bahwa tukang roti memang menerima `4,000 sats` sebagai pembayaran untuk baguette. Alice menggunakan 2 UTXO sebagai input: satu sebesar `10,000 sats` dan satu lagi `15,000 sats`. Sebagai output, dia menerima 3 UTXO: satu sebesar `4,000 sats`, satu `6,000 sats`, dan satu lagi `11,000 sats`. Alice memiliki saldo bersih `-4,000 sats` dalam transaksi ini, yang sesuai dengan harga baguette.

Dalam contoh ini, saya sengaja menghilangkan biaya penambangan untuk memudahkan pemahaman. Dalam kenyataannya, biaya transaksi sepenuhnya ditanggung oleh pengirim.

## Apa perbedaan antara Stonewall dan Stonewall x2?
Transaksi Stonewall beroperasi dengan cara yang sama seperti transaksi StonewallX2, dengan satu-satunya perbedaan adalah yang terakhir memerlukan kolaborasi, tidak seperti transaksi Stonewall klasik, oleh karena itu penamaan "x2". Memang, transaksi Stonewall dapat dilaksanakan tanpa memerlukan kerjasama eksternal: pengirim dapat melakukannya tanpa bantuan orang lain. Namun, untuk transaksi Stonewall x2, seorang peserta tambahan, yang disebut "kolaborator," bergabung dalam proses tersebut. Kolaborator tersebut menyumbangkan bitcoin mereka sendiri sebagai input, bersama dengan bitcoin pengirim, dan menerima jumlah total sebagai output (dikurangi biaya penambangan).

Mari kita kembali ke contoh kita dengan Alice di toko roti. Jika dia ingin melakukan transaksi Stonewall x2, Alice harus berkolaborasi dengan Bob (pihak ketiga) saat membuat transaksi. Mereka masing-masing akan menyediakan sebuah input UTXO. Bob kemudian akan menerima jumlah penuh dari inputnya sebagai output. Penjual roti akan menerima pembayaran untuk baguetnya dengan cara yang sama seperti dalam transaksi Stonewall, sementara Alice akan menerima kembali saldo awalnya, dikurangi biaya baguet.
![transaksi stonewall x2](assets/en/2.webp)

Dari perspektif eksternal, pola transaksi akan tetap sama persis.
![Stonewall atau Stonewall x2 ?](assets/en/3.webp)

Secara ringkas, transaksi Stonewall dan Stonewall x2 memiliki struktur yang identik. Perbedaan antara keduanya terletak pada sifat kolaboratif mereka. Transaksi Stonewall dikembangkan secara individu, tanpa kebutuhan akan kolaborasi. Sebaliknya, transaksi Stonewall x2 mengandalkan kerjasama antara dua individu untuk implementasinya.

[**-> Pelajari lebih lanjut tentang transaksi Stonewall x2**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)

## Apa tujuan dari transaksi Stonewall?
Struktur Stonewall menambahkan jumlah entropi yang signifikan ke dalam transaksi dan menyamarkan analisis rantai. Dari perspektif eksternal, transaksi seperti itu dapat diinterpretasikan sebagai coinjoin kecil antara dua orang. Namun pada kenyataannya, sama seperti transaksi Stonewall x2, itu adalah pembayaran. Metode ini oleh karena itu menciptakan ketidakpastian dalam analisis rantai, dan bahkan dapat mengarah pada kesimpulan yang salah.

Mari kita kembali ke contoh Alice di toko roti. Transaksi di blockchain akan tampak sebagai berikut:
![Stonewall atau Stonewall x2 ?](assets/en/4.webp)
Seorang pengamat eksternal yang mengandalkan heuristik analisis rantai umum dapat keliru menyimpulkan bahwa "*dua orang telah melakukan coinjoin kecil, dengan satu UTXO masing-masing sebagai input dan dua UTXO masing-masing sebagai output*".
![Stonewall atau Stonewall x2 ?](assets/en/5.webp)
Interpretasi ini salah karena, seperti yang Anda tahu, sebuah UTXO dikirim ke penjual roti, 2 UTXO dalam input berasal dari Alice, dan dia menerima 3 output kembalian.

![transaksi stonewall penjual roti](assets/en/1.webp)
Meskipun seorang pengamat dari luar berhasil mengidentifikasi pola transaksi Stonewall, mereka tidak akan memiliki semua informasi. Mereka tidak akan dapat menentukan mana dari dua UTXO dengan jumlah yang sama yang sesuai dengan pembayaran. Selain itu, mereka tidak akan dapat menentukan apakah dua UTXO dalam input berasal dari dua orang yang berbeda atau jika mereka milik satu orang yang menggabungkannya. Poin terakhir ini disebabkan oleh fakta bahwa transaksi Stonewall x2, yang telah kita bahas di atas, mengikuti pola yang sama persis dengan transaksi Stonewall. Dari luar dan tanpa informasi tambahan tentang konteksnya, mustahil untuk membedakan transaksi Stonewall dari transaksi Stonewall x2. Namun, yang pertama bukanlah transaksi kolaboratif, sedangkan yang terakhir adalah. Ini menambahkan lebih banyak keraguan tentang pengeluaran ini.
![Stonewall atau Stonewall x2?](assets/en/3.webp)
## Bagaimana cara melakukan transaksi Stonewall di Samourai Wallet?
Berbeda dengan transaksi Stowaway atau Stonewall x2 (cahoots), transaksi Stonewall tidak memerlukan penggunaan Paynyms. Ini dapat dilakukan langsung, tanpa langkah persiapan apa pun. Untuk melakukan ini, ikuti tutorial video kami di Samourai Wallet:
![Tutorial Stonewall - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)

## Bagaimana cara melakukan transaksi Stonewall di Sparrow Wallet?
Berbeda dengan transaksi Stowaway atau Stonewall x2 (cahoots), transaksi Stonewall tidak memerlukan penggunaan Paynyms. Ini dapat dilakukan langsung, tanpa langkah persiapan apa pun. Untuk melakukan ini, ikuti tutorial video kami di Sparrow Wallet:
![Tutorial Stonewall - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)

**Sumber Eksternal:**
- https://docs.samourai.io/en/spend-tools#stonewall.