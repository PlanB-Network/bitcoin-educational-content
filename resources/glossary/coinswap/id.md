---
term: PENUKARAN KOIN
---

Protokol untuk transfer rahasia Ownership antar pengguna. Metode ini bertujuan untuk mentransfer kepemilikan bitcoin dari satu orang ke orang lain, dan sebaliknya, tanpa Exchange ini secara eksplisit terlihat pada Blockchain. Coinwap menggunakan kontrak pintar untuk melakukan transfer tanpa memerlukan kepercayaan di antara kedua belah pihak.


Mari kita bayangkan sebuah contoh naif (yang tidak mungkin terjadi) dengan Alice dan Bob. Alice memiliki 1 BTC yang diamankan dengan private key $A$, dan Bob juga memiliki 1 BTC yang diamankan dengan private key $B$. Secara teoritis, mereka dapat melakukan Exchange pada private key mereka melalui saluran komunikasi eksternal untuk melakukan transfer rahasia. Akan tetapi, metode naif ini memiliki risiko yang tinggi dalam hal kepercayaan. Tidak ada yang menghalangi Alice untuk menyimpan salinan private key $A$ setelah Exchange dan menggunakannya nanti untuk mencuri bitcoin, ketika kunci tersebut sudah berada di tangan Bob. Terlebih lagi, tidak ada jaminan bahwa Alice tidak akan menerima private key $B$ milik Bob dan tidak akan pernah memberikan private key $A$ miliknya dalam Exchange. Oleh karena itu, Exchange ini bergantung pada kepercayaan yang berlebihan di antara kedua belah pihak, dan tidak efektif untuk memastikan transfer rahasia yang aman dari Ownership.


Untuk mengatasi masalah ini dan memungkinkan pertukaran koin antara pihak-pihak yang tidak saling percaya, kita akan menggunakan sistem Smart contract yang membuat Exchange menjadi "atomik". Sistem ini dapat berupa HTLC (*Hash Time-Locked Contracts*) atau PTLC (*Point Time-Locked Contracts*). Kedua protokol ini beroperasi dengan cara yang sama, menggunakan sistem penguncian waktu yang memastikan bahwa Exchange berhasil diselesaikan atau dibatalkan sepenuhnya, sehingga melindungi integritas dana kedua belah pihak. Perbedaan utama antara HTLC dan PTLC adalah bahwa HTLC menggunakan hash dan preimage untuk mengamankan transaksi, sedangkan PTLC menggunakan Tanda Tangan Adaptor.


Dalam skenario coinswap menggunakan HTLC atau PTLC antara Alice dan Bob, Exchange berlangsung dengan cara yang aman: berhasil dan masing-masing menerima BTC satu sama lain, atau gagal dan masing-masing menyimpan BTC-nya sendiri. Hal ini membuat salah satu pihak tidak mungkin menipu atau mencuri BTC pihak lain.


Penggunaan Tanda Tangan Adaptor sangat menarik dalam konteks ini, karena memungkinkan untuk membuang skrip tradisional (mekanisme yang kadang-kadang disebut sebagai "skrip tanpa skrip"). Hal ini mengurangi biaya yang terkait dengan Exchange. Keuntungan utama lain dari Tanda Tangan Adaptor adalah bahwa mereka tidak memerlukan penggunaan Hash yang sama untuk kedua belah pihak yang bertransaksi, sehingga menghindari kebutuhan untuk mengungkapkan hubungan langsung di antara mereka dalam jenis Exchange tertentu.