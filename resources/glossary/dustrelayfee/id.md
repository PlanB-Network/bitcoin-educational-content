---
term: DUSTRELAYFEE

---
Aturan standardisasi yang digunakan oleh node jaringan untuk menentukan apa yang mereka anggap sebagai "batas debu" Parameter ini menetapkan tingkat biaya dalam satuan per kilobyte virtual (sats/kvB) yang berfungsi sebagai referensi untuk menghitung jika nilai UTXO kurang dari biaya yang diperlukan untuk menyertakannya dalam sebuah transaksi. Memang, UTXO dianggap sebagai "debu" pada Bitcoin jika membutuhkan lebih banyak biaya untuk ditransfer daripada nilai yang diwakilinya. Perhitungan batas ini adalah sebagai berikut:

```text
limit = (input size + output size) * fee rate
```

Karena tingkat biaya yang diperlukan agar transaksi dapat dimasukkan ke dalam blok Bitcoin selalu bervariasi, parameter `DustRelayFee` memungkinkan setiap node untuk menentukan tingkat biaya yang digunakan dalam penghitungan ini. Secara default, pada Bitcoin Core, nilai ini diatur ke 3.000 sats/kvB. Sebagai contoh, untuk menghitung batas debu untuk input dan output P2PKH, yang masing-masing berukuran 148 dan 34 byte, perhitungannya adalah

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Ini berarti bahwa node yang bersangkutan tidak akan merelay transaksi termasuk UTXO yang dijamin P2PKH yang nilainya kurang dari 546 sat.