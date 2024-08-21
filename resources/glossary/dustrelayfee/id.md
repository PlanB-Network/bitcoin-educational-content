---
term: DUSTRELAYFEE
---

Sebuah aturan standarisasi yang digunakan oleh node jaringan untuk menentukan apa yang mereka anggap sebagai "batas debu." Parameter ini menetapkan tarif biaya dalam satoshi per kilobyte virtual (sats/kvB) yang berfungsi sebagai referensi untuk menghitung apakah nilai dari sebuah UTXO kurang dari biaya yang diperlukan untuk memasukkannya dalam sebuah transaksi. Memang, sebuah UTXO dianggap "debu" pada Bitcoin jika biaya yang diperlukan untuk mentransfernya lebih besar daripada nilai yang diwakilinya sendiri. Perhitungan batas ini adalah sebagai berikut:

```text
limit = (ukuran input + ukuran output) * tarif biaya
```

Karena tarif biaya yang diperlukan untuk sebuah transaksi agar dapat dimasukkan dalam blok Bitcoin terus berubah-ubah, parameter `DustRelayFee` memungkinkan setiap node untuk mendefinisikan tarif biaya yang digunakan dalam perhitungan ini. Secara default, pada Bitcoin Core, nilai ini ditetapkan menjadi 3,000 sats/kvB. Sebagai contoh, untuk menghitung batas debu untuk input dan output P2PKH, yang masing-masing berukuran 148 dan 34 byte, perhitungannya akan menjadi:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Ini berarti bahwa node yang bersangkutan tidak akan meneruskan transaksi yang mencakup UTXO yang diamankan P2PKH dengan nilai kurang dari 546 sats.