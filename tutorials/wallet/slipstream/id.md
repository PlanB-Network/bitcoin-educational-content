---
name: Slipstream
description: Sending a signed transaction directly to a miner with Slipstream, without broadcasting it to the Bitcoin network
---

![cover](assets/cover.webp)

Biasanya, saat Anda menandatangani sebuah transaksi, transaksi tersebut secara otomatis disiarkan ke setiap node Bitcoin di jaringan. Transaksi kemudian menunggu untuk ditambang.

Namun, selama transaksi belum masuk ke dalam sebuah blok, seorang penyerang yang telah memperoleh private key Anda dapat menggantikannya dan mencuri dana tersebut. Ini biasanya terjadi jika Anda menggunakan dompet perangkat keras ColdCard.

Alat Slipstream dari perusahaan penambangan MARA memungkinkan Anda melewati penyiaran transaksi ke jaringan: transaksi dikirim langsung (dan hanya) ke seorang miner, sehingga tetap privat dan tidak terekspos di jaringan. Transaksi kemungkinan akan membutuhkan waktu lebih lama untuk ditambang, tetapi akan terlindungi dari serangan penggantian (replacement attack).

Di bawah ini, kami menyediakan tutorial yang memungkinkan pengguna [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), maupun pengguna dompet [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), untuk menggunakan alat Slipstream milik miner MARA melalui halaman [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Peringatan**: alat ini hanya ditujukan untuk profil tertentu, terutama dompet Liana, dompet miniscript, dan beberapa jenis multisig. Wizardsardine **secara eksplisit menyarankan untuk tidak** menggunakannya untuk dompet yang dananya sudah berada dalam risiko pencurian kritis, misalnya dompet yang frasa pemulihannya dihasilkan pada perangkat ColdCard yang terdampak kerentanan random number generator. Dalam situasi tersebut, perlombaan melawan penyerang adalah soal detik, dan transaksi yang dikirim ke satu miner saja membutuhkan waktu jauh lebih lama untuk dikonfirmasi dibandingkan transaksi yang disiarkan secara normal. Jika ini menjadi perhatian Anda, baca dulu tutorial khusus kami:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Untuk pengguna Liana

Liana dikelola oleh Wizardsardine, penerbit halaman [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), sehingga jalurnya langsung: Anda cukup mengekspor file PSBT yang sudah ditandatangani, alih-alih menyiarkannya.

*Prasyarat: memiliki dana di dompet Liana Anda.*

### Langkah 1: Buat transaksi Anda dengan Liana

Seperti biasa, buat transaksi Anda dengan menambahkan alamat tujuan, deskripsi, dan jumlah (di sini, jumlah maksimum yang tersedia di dompet).

Untuk mengatur fee rate:

- pilih coin yang ingin Anda belanjakan dengan mengklik kotak kecil di bagian kiri bawah, di bawah "Coins selection";
- lalu masukkan fee rate. Ingat untuk mengatur fee jauh lebih tinggi dari rate yang disarankan, sebagaimana dijelaskan di halaman ini: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Terakhir, klik "Next".

![Building the transaction in Liana](assets/fr/01.webp)

### Langkah 2: Periksa detail transaksi Anda

Sebelum mengklik "Sign", periksa detail transaksi Anda; khususnya:

- jumlah yang dikirim;
- jumlah satoshi yang dialokasikan untuk fee transaksi;
- namun yang terpenting, alamat tujuan pengiriman dana (ingat untuk memeriksa 5/6 karakter pertama, 5/6 karakter terakhir, dan 5/6 karakter di tengah alamat guna menghindari serangan "address poisoning").

![Checking the transaction details](assets/fr/02.webp)

### Langkah 3: Pilih dompet penandatangan

Selanjutnya, pilih dompet perangkat lunak dan/atau perangkat keras yang Anda butuhkan untuk menandatangani transaksi Anda. Pengingat singkat: dalam kasus dompet multisig 2-dari-2, Anda memerlukan 2 tanda tangan dari 2.

### Langkah 4: Ekspor file PSBT transaksi Anda

Transaksi Bitcoin sekarang telah ditandatangani oleh key yang sesuai. Jangan klik "Broadcast", karena jika Anda melakukannya, transaksi akan dibagikan ke seluruh jaringan dan, jika Anda menggunakan dompet perangkat keras ColdCard, transaksi Anda akan terekspos secara publik dan dana Anda akan berisiko.

Anda sekarang dapat mengklik "Export", lalu menyimpan file PSBT secara lokal di komputer Anda.

![Exporting the PSBT file from Liana](assets/fr/03.webp)

### Langkah 5: Kirim transaksi ke miner melalui outofband.wizardsardine.com

Sekarang untuk langkah-langkah terakhir. Untuk mengirim transaksi ke miner, yang perlu Anda lakukan hanyalah mengambil file PSBT dan men-drag-and-drop-nya ke area yang ditentukan.

![Dropping the PSBT file on outofband.wizardsardine.com](assets/fr/04.webp)

Transaksi kemudian akan ditampilkan seperti terlihat di bawah ini.

![Transaction in the queue](assets/fr/05.webp)

### Langkah 6: Kirim transaksi melalui Slipstream

Terakhir, yang perlu Anda lakukan hanyalah mengklik "Send" agar transaksi dikirim ke MARA melalui Slipstream.

![Sending the transaction via Slipstream](assets/fr/06.webp)

Dalam beberapa detik, transaksi kemudian berubah dari "Sending" menjadi "Accepted":

![Transaction accepted by Slipstream](assets/fr/07.webp)

Yang tersisa hanyalah menyalin identifier transaksi (TXID), lalu menempelkannya di [mempool.space](https://mempool.space/) untuk memantau proses penambangannya:

![Looking up the TXID on mempool.space](assets/fr/08.webp)

Perlu diperhatikan: transaksi akan menampilkan "Transaction not found" hingga miner, yaitu MARA, menambang sebuah blok dan menyertakan transaksi Anda di dalamnya. Ini bisa memakan waktu puluhan menit, bahkan berjam-jam, karena MARA hanya memegang sekitar 4,5% dari hash rate jaringan Bitcoin. Per 4 Agustus 2026, ini setara dengan kurang lebih satu blok ditambang setiap 3 jam 45 menit.

## Untuk pengguna dompet lain

Jika Anda tidak menggunakan [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) tetapi tetap ingin menggunakan alat ini, berikut adalah tutorial menggunakan dompet multisig 2-dari-2. Untuk melakukan ini, kita akan menggunakan dompet perangkat lunak [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Prasyarat: memiliki dana di dompet Sparrow Anda.*

### Langkah 1: Buat transaksi Anda

Dengan [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), buat transaksi pada dompet multisig Anda. Ingat untuk mengatur fee jauh lebih tinggi dari rate yang disarankan, sebagaimana dijelaskan di halaman ini: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Setelah dibuat, klik "Create Transaction".

![Creating the transaction in Sparrow](assets/fr/09.webp)

### Langkah 2: Finalisasi transaksi Anda

Untuk memfinalisasi transaksi Anda, Anda sekarang perlu menandatanganinya. Untuk melakukan ini, klik "Finalize Transaction for Signing".

![Finalizing the transaction for signing](assets/fr/10.webp)

### Langkah 3: Tandatangani transaksi Anda dengan key-key Anda yang berbeda

Sekarang saatnya menandatangani transaksi. Untuk melakukan ini, cukup tandatangani dengan dompet perangkat lunak atau perangkat keras yang Anda gunakan.

![Signing the transaction with the multisig keys](assets/fr/11.webp)

### Langkah 4: Unduh transaksi yang sudah ditandatangani, dan jangan siarkan ke jaringan

Transaksi Bitcoin sekarang telah ditandatangani oleh kedua key dari multisig 2-dari-2 kita. Jangan klik "Broadcast Transaction", karena jika Anda melakukannya, transaksi akan dibagikan ke seluruh jaringan dan, jika Anda menggunakan dompet perangkat keras ColdCard, transaksi Anda akan terekspos secara publik dan dana Anda akan berisiko.

![Signed transaction, ready but not broadcast](assets/fr/12.webp)

### Langkah 5: Tampilkan script transaksi yang ditandatangani, atau unduh file PSBT

Untuk menampilkan script transaksi Bitcoin yang sudah ditandatangani, sekarang klik "View Final Transaction". Anda kemudian dapat menyalin script transaksi Bitcoin yang sudah ditandatangani:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Displaying the signed transaction script](assets/fr/13.webp)

Jika Anda ingin mengunduh file transaksi, Anda dapat memilih:

- klik "File", lalu "Save transaction…";
- atau klik tombol koneksi jaringan di kanan bawah (tombol kuning), lalu klik "Save Final Transaction".

Transaksi kemudian akan disimpan secara lokal di komputer Anda.

![Saving the final transaction locally](assets/fr/14.webp)

### Langkah 6: Kirim transaksi ke miner melalui outofband.wizardsardine.com

Sekarang untuk langkah-langkah terakhir. Untuk mengirim transaksi ke miner, yang perlu Anda lakukan hanyalah:

- buka [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- tempel script transaksi yang sudah ditandatangani yang disalin pada langkah sebelumnya, lalu klik "ADD TO QUEUE" di bawahnya;

![Pasting the transaction script into the tool](assets/fr/15.webp)

- atau ambil filenya dan drag-and-drop ke area yang ditentukan.

![Dropping the transaction file on the tool](assets/fr/16.webp)

Transaksi kemudian akan ditampilkan seperti terlihat di bawah ini.

![Transaction in the queue](assets/fr/17.webp)

Jika sebuah pesan memberi tahu Anda bahwa jumlah total input satoshi dalam transaksi Anda tidak diketahui (dan akibatnya, jumlah satoshi untuk fee tidak dapat dihitung), Anda cukup memasukkan jumlah total input satoshi secara manual. Untuk menemukannya, cukup klik pada tampilan transaksi Anda di Sparrow, di bagian tengah diagram:

![Total input amount shown in Sparrow](assets/fr/18.webp)

Kemudian masukkan jumlah tersebut (15.904 sat dalam contoh kami) ke dalam alat [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Manually entering the total input amount](assets/fr/19.webp)

Terakhir, periksa bahwa fee rate sudah benar.

### Langkah 7: Kirim transaksi melalui Slipstream

Terakhir, yang perlu Anda lakukan hanyalah mengklik "Send" agar transaksi dikirim ke MARA melalui Slipstream.

![Sending the transaction via Slipstream](assets/fr/20.webp)

Dalam beberapa detik, transaksi kemudian berubah dari "Sending" menjadi "Accepted":

![Transaction accepted by Slipstream](assets/fr/21.webp)

Yang tersisa hanyalah menyalin identifier transaksi (TXID), lalu menempelkannya di [mempool.space](https://mempool.space/) untuk memantau proses penambangannya:

![Looking up the TXID on mempool.space](assets/fr/22.webp)

Perlu diperhatikan: transaksi akan menampilkan "Transaction not found" hingga miner, yaitu MARA, menambang sebuah blok dan menyertakan transaksi Anda di dalamnya. Ini bisa memakan waktu puluhan menit, bahkan berjam-jam, karena MARA hanya memegang sekitar 4,5% dari hash rate jaringan Bitcoin. Per 4 Agustus 2026, ini setara dengan kurang lebih satu blok ditambang setiap 3 jam 45 menit.
</content>
<parameter name="i">Write Indonesian translation of Slipstream tutorial