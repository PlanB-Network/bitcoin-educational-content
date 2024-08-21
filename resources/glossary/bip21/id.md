---
term: BIP21
---

Proposal ini ditulis oleh Nils Schneider dan Matt Corallo, berdasarkan BIP20 yang ditulis oleh Luke Dashjr, yang pada gilirannya berasal dari dokumen lain yang ditulis oleh Nils Schneider. BIP21 mendefinisikan bagaimana alamat penerima harus dikodekan dalam URI (*Uniform Resource Identifier*) untuk memfasilitasi pembayaran. Sebagai contoh, sebuah URI Bitcoin yang mengikuti BIP21 di mana saya akan meminta di bawah label “*Pandul*” untuk mengirimkan saya 0.1 BTC akan terlihat seperti ini:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

Standarisasi ini meningkatkan pengalaman pengguna transaksi Bitcoin dengan memungkinkan untuk mengklik tautan atau memindai kode QR untuk menginisiasi parameter mereka. Standar BIP21 kini telah banyak diadopsi dalam perangkat lunak dompet Bitcoin.