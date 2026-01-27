---
name: Electrum OP_RETURN
description: Daftarkan pesan pada Blockchain Bitcoin dengan Electrum
---

![cover](assets/cover.webp)




Tutorial langkah demi langkah ini menunjukkan kepada Anda cara menulis pesan pada Blockchain Bitcoin menggunakan Wallet Electrum. Operasi ini menggunakan instruksi OP_RETURN untuk memasukkan teks ke dalam transaksi, yang dapat dilihat oleh publik pada Blockchain. Ikuti langkah-langkah sederhana ini untuk pendaftaran yang sukses.



---
## Prasyarat





- Komputer (Windows, macOS atau Linux).
- Koneksi internet.
- Beberapa satoshi (Sats) atau bitcoin (BTC) di Wallet Anda untuk menutupi jumlah transaksi dan biaya.
- Konverter teks-ke-hex (misalnya situs online) atau alat khusus seperti [generator skrip OP_RETURN ini](https://resources.davidcoen.it/opreturnelectrum/).



---

## Langkah 1: Unduh dan pasang Electrum



![image](assets/fr/01.webp)



1. Kunjungi situs web resmi Electrum: [electrum.org](https://electrum.org/).


2. Unduh versi yang sesuai dengan sistem operasi Anda (Windows, macOS, Linux).


3. Pasang Electrum sesuai dengan petunjuk pemasang.


4. Periksa integritas file yang diunduh (opsional, tetapi disarankan untuk alasan keamanan) dengan membandingkan tanda tangan file atau Hash.



→ Detail selengkapnya pada tutorial Electrum :



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Langkah 2: Membuat atau mengimpor Wallet



1. Luncurkan Electrum.


2. Pilih Buat Wallet baru atau Pulihkan Wallet yang sudah ada jika Anda sudah memiliki frasa seed (frasa pemulihan).


3. Ikuti petunjuk untuk mengkonfigurasi Wallet Anda:




 - Untuk Wallet yang baru, catatlah kalimat seed Anda dan simpanlah di tempat yang aman (kertas, brankas, dll.).
 - Untuk Wallet yang sudah ada, masukkan frasa seed Anda untuk memulihkannya.


4. Tetapkan kata sandi untuk mengamankan Wallet Anda.



→ Detail selengkapnya pada tutorial Electrum :



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Langkah 3: Periksa dana yang tersedia



Pastikan Wallet Anda berisi cukup bitcoin (BTC) atau satoshi (Sats) untuk :




- Jumlah transaksi (misalnya, 0,00001 BTC atau 1000 Sats).
- Biaya transaksi, yang bervariasi sesuai dengan ukuran jaringan (umumnya beberapa ribu Sats).



Lihat Saldo di Electrum untuk memeriksa dana Anda.



![image](assets/fr/02.webp)



Jika perlu, transfer BTC atau Sats untuk mengisi Wallet Anda. Untuk melakukannya, buka tab 'Terima' dan klik 'Buat Permintaan':



![image](assets/fr/03.webp)



Ini akan menunjukkan penerimaan Address:



![image](assets/fr/04.webp)



→ Detail selengkapnya pada tutorial Electrum :



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Langkah 4: Siapkan pesan yang akan dituliskan



Pilih pesan yang ingin Anda masukkan (misalnya, `Terima kasih Satoshi`). Catatan: Pesan OP_RETURN dibatasi hingga 80 byte, yaitu sekitar 80 karakter ASCII.



*Luangkan waktu sejenak untuk berpikir: apa yang Anda tulis pada Blockchain Bitcoin bersifat abadi dan dapat diakses oleh semua orang, jadi :*




- meninggalkan ekspresi indah dari kemanusiaan kita,
- hindari memasukkan konten yang mungkin Anda sesali



*Ruang Blockchain dan bitcoin Anda sangat berharga, gunakanlah dengan bijak dan dengan niat*



Mengonversi pesan Anda ke heksadesimal:




- Anda dapat menggunakan [alat online](https://www.rapidtables.com/convert/number/ascii-to-hex.html), tetapi berhati-hatilah untuk tidak memproses data sensitif di sana (meskipun, pada prinsipnya, informasi yang dimaksudkan untuk publikasi pada Blockchain Bitcoin melalui OP_RETURN tidak menimbulkan masalah kerahasiaan);
- Untuk kerahasiaan yang lebih baik, lakukan konversi secara lokal menggunakan Python kecil:



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Contoh: `Terima kasih Satoshi` dalam ASCII menghasilkan `5468616e6b73205361746f736869` dalam heksadesimal.



Siapkan naskah transaksi. Berikut adalah contoh format yang diharapkan:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



yang terdiri dari :





- **Tujuan Address**: Bitcoin Address yang valid. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Ini bisa berupa Address Anda sendiri, jika Anda ingin mengembalikan dana yang ditransfer ke Anda sendiri;
- **Jumlah yang ditransfer**: jumlah transaksi, di sini `0,00001` BTC. **Harap diperhatikan**: karena unit yang digunakan dalam Electrum adalah BTC, jumlah yang ditunjukkan dalam skrip transaksi juga harus dinyatakan dalam BTC, dan bukan dalam Sats;
- Skrip **OP_RETURN**: Pesan yang dikonversi ke heksadesimal yang diawali dengan skrip (`OP_RETURN <pesan>`), 0. Di sini, `5468616e6b73205361746f736869` untuk pesan dalam heksadesimal.



⚠️ **Perhatian**: Sangat penting untuk menunjukkan `0` setelah OP_RETURN, karena opcode ini menandai skrip sebagai tidak valid, membuat output secara permanen tidak dapat digunakan. Node jaringan akan menghapus output ini dari set UTXO mereka. Jika Anda memasukkan nilai selain `0`, maka nilai tersebut akan hilang secara permanen: bitcoin Anda akan dianggap terbakar. Oleh karena itu, Anda harus selalu memasukkan `0` dengan OP_RETURN untuk merekam data yang diinginkan, tetapi tanpa mengasosiasikan dana dengannya, yang akan hilang.



Tip: Gunakan alat [OP_RETURN Generator](https://resources.davidcoen.it/opreturnelectrum/) untuk melakukan generate skrip secara otomatis. Meskipun alat ini menyarankan untuk memasukkan jumlah dalam BTC, tetap konfigurasikan unit dalam Electrum.



![image](assets/fr/05.webp)



Untuk mengubah satuan yang digunakan oleh Electrum, di bilah menu temukan "Preferensi", lalu di tab "Unit" pilih BTC / mBTC / bit atau Sats :



![image](assets/fr/06.webp)




---

## Langkah 5: Kirim transaksi



Di Electrum, buka tab Kirim.



![image](assets/fr/07.webp)



Pada kolom "Bayar ke", tempelkan skrip yang sudah disiapkan (misalnya, skrip di atas).



![image](assets/fr/08.webp)



Kolom "Bayar ke" harus ditampilkan di Green, dan jumlah transaksi akan muncul pada baris di bawahnya.



Periksa jumlah dan satuannya di bidang Jumlah.



Klik "Bayar..." dan sesuaikan biaya transaksi Anda sesuai dengan jumlah yang ingin Anda bayarkan dan kecepatan transaksi yang Anda inginkan untuk diproses oleh Miner dan diintegrasikan ke dalam blok.



![image](assets/fr/09.webp)



Klik OK dan konfirmasikan transaksi dengan kata sandi Anda. Jendela konfirmasi akan muncul.




---

## Langkah 6: Verifikasi pendaftaran



Setelah transaksi dikonfirmasi (ini mungkin memerlukan waktu beberapa menit), buka tab "Riwayat".



![image](assets/fr/10.webp)



Klik kanan pada transaksi dan pilih "View on Explorer" untuk melihat detailnya.



Atau, salin tujuan Address (misalnya, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) dan lihat di penjelajah Blockchain seperti [Mempool.space](https://Mempool.space/) atau [blockstream.info](https://blockstream.info/).



Cari kolom OP_RETURN di rincian transaksi untuk melihat pesan Anda.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Kiat dan praktik terbaik





- Uji coba dengan jumlah kecil: Mulailah dengan transaksi kecil (mis. Sats 1000) untuk menghindari kesalahan yang merugikan.
- Pastikan output yang berisi OP_RETURN sama dengan nol, jika tidak, bitcoin Anda akan hilang secara permanen.
- Periksa unit: Pastikan jumlah yang dimasukkan sesuai dengan unit yang ditampilkan di Electrum (BTC, mBTC, atau Sats).
- Biaya transaksi: Jika jaringan padat, naikkan biaya untuk konfirmasi yang lebih cepat.
- Pesan singkat: Entri OP_RETURN dibatasi hingga 80 byte. Rencanakan pesan Anda dengan tepat.



---

## Sumber daya yang berguna





- Unduh Electrum: [electrum.org](https://electrum.org/)
- Generator skrip OP_RETURN: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Penjelajah: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)