---
term: BIP21

---
Proposal yang ditulis oleh Nils Schneider dan Matt Corallo, berdasarkan BIP20 yang ditulis oleh Luke Dashjr, yang pada gilirannya berasal dari dokumen lain yang ditulis oleh Nils Schneider. BIP21 mendefinisikan bagaimana alamat penerima harus dikodekan dalam URI (*Uniform Resource Identifier*) untuk memfasilitasi pembayaran. Sebagai contoh, URI Bitcoin yang mengikuti BIP21 di mana saya akan meminta di bawah label "*Pandul*" untuk mengirimkan 0,1 BTC akan terlihat seperti ini:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```

Standarisasi ini meningkatkan pengalaman pengguna dalam transaksi Bitcoin dengan mengizinkan untuk mengklik sebuah tautan atau memindai sebuah kode QR untuk memulai parameternya. Standar BIP21 sekarang diadopsi secara luas dalam perangkat lunak dompet Bitcoin.