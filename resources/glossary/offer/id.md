---
term: PENAWARAN
---

Di BOLT12, *offers* adalah kode QR statis untuk melakukan beberapa pembayaran pada Lightning Network. Tidak seperti faktur konvensional, *offers* dapat digunakan kembali. Kode ini dapat digunakan untuk generate dan beberapa permintaan Invoice. Ketika pengguna memindai kode QR yang berisi *offer*, kode tersebut akan mengirimkan pesan yang meminta Invoice baru ke node Lightning yang terkait. Node tersebut merespons dengan Invoice yang dapat digunakan oleh pembayar. Dengan demikian, *offer* memberikan pengenal unik untuk menerima beberapa pembayaran dari pengguna yang berbeda di Lightning.