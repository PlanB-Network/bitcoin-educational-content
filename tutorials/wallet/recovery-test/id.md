---
name: Tes Pemulihan
description: Bagaimana Cara Menguji Cadanganmu supaya Kamu Nggak Sampai Kehilangan Bitcoin?
---
![cover](assets/cover.webp)

Saat bikin dompet Bitcoin, kamu diminta untuk mencatat frasa mnemonik yang biasanya terdiri dari 12 atau 24 kata. Frasa ini memungkinkan kamu memulihkan akses ke bitcoin kalau perangkat penyimpan dompetmu hilang, rusak, atau dicuri. Sebelum mulai pakai dompet Bitcoin barumu, sangat penting untuk memverifikasi apakah frasa mnemonik ini benar. Cara terbaik untuk melakukannya adalah dengan melakukan tes pemulihan secara simulasi.

Tes ini melibatkan simulasi pemulihan dompet sebelum kamu menyetorkan bitcoin apa pun ke dalamnya. Selama dompet masih kosong, kita mensimulasikan situasi di mana perangkat penyimpan kunci hilang, dan yang tersisa hanya frasa mnemonik untuk mencoba memulihkan bitcoin kita.

![TES PEMULIHAN](assets/notext/01.webp)

## Apa tujuannya?

Proses pengujian ini bikin kamu bisa memastikan kalau cadangan fisik dari frasa mnemonikmu, baik di kertas maupun logam, memang berfungsi. Kalau gagal saat tes pemulihan, itu berarti ada kesalahan dalam cadangan frasa, dan otomatis bikin bitcoinmu dalam risiko. Sebaliknya, kalau tes berhasil, itu mengonfirmasi kalau frasa mnemonikmu sepenuhnya bisa dipakai, jadi kamu bisa lebih tenang mengamankan bitcoin dengan dompet ini.

Melakukan tes pemulihan secara simulasi punya dua keuntungan. Bukan cuma memastikan keakuratan frasa mnemonik, tapi juga bikin kamu terbiasa dengan proses pemulihan dompet. Dengan begitu, kamu bisa nemuin potensi masalah sebelum situasi beneran terjadi. Jadi ketika suatu hari kamu memang perlu memulihkan dompet, kamu nggak akan terlalu stres karena sudah tahu alurnya, dan risiko kesalahan jadi lebih kecil. Itulah kenapa langkah pengujian ini penting banget, dan kamu perlu meluangkan waktu untuk melakukannya dengan benar.

## Apa itu tes pemulihan?

Proses tes ini cukup sederhana:

- Setelah bikin dompet Bitcoin baru, dan sebelum menyetorkan satoshi pertamamu, catat dulu informasi saksi seperti xpub, alamat penerimaan pertama, atau bahkan sidik jari kunci utama;
- Lalu, hapus dompet yang masih kosong itu, misalnya dengan mereset dompet perangkat kerasmu ke pengaturan pabrik;
- Setelah itu, lakukan simulasi pemulihan dompet hanya dengan cadangan kertas dari frasa mnemonik dan passphrase (kalau kamu memang memakainya);
- Terakhir, cek apakah informasi saksi cocok dengan dompet yang berhasil diregenerasi. Kalau semua cocok, artinya cadangan fisikmu bisa diandalkan, dan kamu bisa dengan tenang mengirim bitcoin pertamamu ke dompet ini.

Hati-hati, selama tes pemulihan **kamu harus pakai perangkat yang sama dengan dompet akhir yang memang akan kamu gunakan**, supaya nggak nambahin permukaan serangan. Misalnya, kalau kamu bikin dompet di Trezor Safe 5, pastikan tes pemulihan juga dilakukan di Trezor Safe 5 yang sama. Penting banget untuk tidak pernah memasukkan frasa pemulihan ke perangkat lunak lain, karena itu bakal mengompromikan keamanan yang diberikan dompet perangkat kerasmu, bahkan meskipun dompetnya masih kosong.

## Bagaimana cara melakukan tes pemulihan?

Di tutorial ini, aku bakal nunjukin cara melakukan tes pemulihan di dompet perangkat lunak Bitcoin, pakai Sparrow Wallet (untuk dompet panas). Tapi sebenarnya, prosesnya sama aja buat jenis perangkat lain. Ingat ya, kalau kamu pakai dompet perangkat keras, **jangan lakukan tes pemulihan di Sparrow Wallet** (lihat bagian sebelumnya).

Aku baru aja bikin dompet panas baru di Sparrow Wallet. Saat ini, aku belum kirim bitcoin apa pun ke sana. Dompet ini masih kosong.
![UJI PEMULIHAN](assets/notext/02.webp)

Aku sudah dengan hati-hati mencatat frasa mnemonik 12 kata di selembar kertas. Dan karena pengin ningkatin keamanan dompet ini, aku juga menyiapkan frasa sandi BIP39 yang kusimpan di kertas lain:

```txt
1. shield
2. brass
3. sentence
4. cube
5. marble
6. glad
7. satoshi
8. door
9. project
10. panic
11. prepare
12. general
```

```text
Passphrase: YfaicGzXH9t5C#g&47Kzbc$JL
```

***Jelas, kamu seharusnya nggak pernah membagikan frasa mnemonik dan frasa sandimu di internet, beda dengan yang aku lakukan di tutorial ini. Dompet contoh ini nggak akan dipakai dan bakal dihapus setelah tutorial selesai.***

Sekarang aku bakal mencatat di draf sebuah informasi saksi dari dompetku. Kamu bisa pilih berbagai macam informasi, seperti alamat penerimaan pertama, xpub, atau sidik jari kunci utama. Secara pribadi, aku lebih nyaranin pakai alamat penerimaan pertama. Soalnya, ini bikin kamu bisa memverifikasi kalau jalur derivasi pertama lengkap yang menuju ke alamat itu memang bisa ditemukan.

Di Sparrow, klik pada tab "*Alamat*".

![UJI PEMULIHAN](assets/notext/03.webp)

Lalu, catat di selembar kertas alamat penerimaan pertama dari dompetmu. Dalam contohnya aku, alamatnya adalah:

```txt
tb1qxv56mma5x5r7uhdkn0ldvcx6m0gj6f3kre0gwd
```

Setelah mencatat informasinya, buka menu "*File*", lalu pilih "*Hapus Dompet*". Aku ingetin lagi, dompet Bitcoinmu harus benar-benar kosong sebelum lanjut ke langkah ini.

![UJI PEMULIHAN](assets/notext/04.webp)

Kalau dompetmu memang kosong, lanjutkan dengan mengonfirmasi penghapusan dompet itu.

![UJI PEMULIHAN](assets/notext/05.webp)

Sekarang kamu perlu ngulang proses bikin dompet, tapi kali ini pakai cadangan kertas yang udah kamu catat. Klik menu "*File*", lalu pilih "*Dompet Baru*".

![UJI PEMULIHAN](assets/notext/06.webp)

Masukkan nama dompet lagi.

![UJI PEMULIHAN](assets/notext/07.webp)

Di menu "*Tipe Skrip*", kamu perlu memilih tipe skrip yang sama dengan dompet yang sebelumnya kamu hapus.

![UJI PEMULIHAN](assets/notext/08.webp)

Kemudian klik pada tombol "*Dompet Perangkat Lunak Baru atau Diimpor*".

![UJI PEMULIHAN](assets/notext/09.webp)

Pilih jumlah kata yang benar untuk seed.

![UJI PEMULIHAN](assets/notext/10.webp)

Masukkan frasa mnemonikmu ke dalam perangkat lunak. Kalau muncul pesan "*Checksum Tidak Valid*", itu berarti cadangan frasa mnemonikmu salah. Dalam kasus ini, kamu harus mulai lagi dari awal bikin dompet, karena tes pemulihanmu dianggap gagal.

![UJI PEMULIHAN](assets/notext/11.webp)

Kalau kamu punya frasa sandi, kayak di kasusku, masukkan juga.

![UJI PEMULIHAN](assets/notext/12.webp)

Klik pada "*Buat Keystore*", lalu pada "*Impor Keystore*".

![UJI PEMULIHAN](assets/notext/13.webp)

Dan akhirnya, klik pada tombol "*Terapkan*".

![UJI PEMULIHAN](assets/notext/14.webp)

Sekarang kamu bisa kembali ke tab "*Alamat*".

![UJI PEMULIHAN](assets/notext/15.webp)
Terakhir, pastikan alamat penerima pertama sama dengan yang sudah kamu catat sebagai saksi di drafmu.![RECOVERY TEST](assets/notext/16.webp)

Kalau alamat penerima cocok, berarti tes pemulihanmu berhasil dan kamu bisa langsung pakai dompet Bitcoin barumu. Tapi kalau nggak cocok, itu mungkin karena ada kesalahan dalam pemilihan jenis skrip yang bikin jalur derivasinya nggak benar, atau ada masalah di cadangan frasa mnemonik maupun passphrase-mu. Dalam dua kasus ini, aku sangat nyaranin buat mulai dari awal lagi dan bikin dompet Bitcoin baru supaya aman. Kali ini, pastikan frasa mnemonik dicatat tanpa ada kesalahan.

Selamat, sekarang kamu udah paham cara melakukan tes pemulihan! Aku nyaranin kamu buat membiasakan proses ini setiap kali bikin dompet Bitcoin baru. Kalau kamu merasa tutorial ini bermanfaat, aku bakal sangat menghargai kalau kamu bisa kasih jempol ke atas di bawah ini. Jangan ragu juga buat bagiin artikel ini ke jejaring sosialmu. Makasih banyak!
