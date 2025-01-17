---
term: PERJANJIAN

---
Sebuah mekanisme yang memungkinkan pengenaan kondisi tertentu tentang bagaimana suatu mata uang dapat digunakan, termasuk dalam transaksi di masa depan. Di luar kondisi yang biasanya diizinkan oleh bahasa skrip pada UTXO, covenant memberlakukan batasan tambahan tentang bagaimana Bitcoin ini dapat digunakan dalam transaksi selanjutnya. Secara teknis, pembentukan covenant terjadi ketika `scriptPubKey` dari sebuah UTXO mendefinisikan batasan pada `scriptPubKey` dari output transaksi yang membelanjakan UTXO tersebut. Dengan memperluas cakupan skrip, covenant akan memungkinkan berbagai pengembangan pada Bitcoin seperti penambatan bilateral drivechain, implementasi brankas, atau peningkatan sistem overlay seperti Lightning. Proposal perjanjian dibedakan berdasarkan tiga kriteria:


- Ruang lingkup mereka;
- Penerapannya;
- Rekursifitas mereka.

Ada banyak proposal yang memungkinkan penggunaan perjanjian pada Bitcoin. Yang paling maju dalam proses implementasi adalah: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO), dan `OP_VAULT`. Di antara proposal-proposal lainnya, ada: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, dan lain-lain.

Untuk lebih memahami konsep perjanjian, pertimbangkan analogi ini: bayangkan sebuah brankas yang berisi uang kertas pecahan kecil senilai 500€. Jika Anda berhasil membuka brankas ini dengan kunci yang tepat, maka Anda bebas menggunakan uang tersebut sesuai keinginan. Ini adalah situasi normal dengan Bitcoin. Sekarang, bayangkan brankas yang sama tidak berisi uang kertas 500€, melainkan voucher makan dengan nilai yang setara. Jika Anda berhasil membuka brankas ini, Anda bisa menggunakan uang tersebut. Namun, kebebasan Anda untuk membelanjakan uang tersebut dibatasi, karena Anda hanya bisa menggunakan voucher ini untuk membayar di restoran tertentu. Jadi, ada syarat pertama untuk membelanjakan uang ini, yaitu berhasil membuka brankas dengan kunci yang sesuai. Tetapi ada juga syarat tambahan mengenai penggunaan uang ini di masa depan: uang tersebut harus dibelanjakan secara eksklusif di restoran yang bermitra, dan tidak bisa digunakan secara bebas. Sistem pembatasan transaksi di masa depan inilah yang disebut dengan perjanjian.

> dalam bahasa Prancis, tidak ada istilah yang secara tepat menangkap arti kata "perjanjian". Kita dapat berbicara tentang "klausul", "pakta", atau "komitmen", tetapi istilah-istilah tersebut tidak sesuai dengan istilah "perjanjian". Istilah ini dipinjam dari terminologi hukum yang memungkinkan untuk menggambarkan klausul kontrak yang membebankan kewajiban yang terus menerus pada sebuah properti*