---
term: COINSWAP
---

Protokol untuk transfer rahasia kepemilikan antar pengguna. Metode ini bertujuan untuk mentransfer kepemilikan bitcoin dari satu orang ke orang lain, dan sebaliknya, tanpa pertukaran ini secara eksplisit terlihat pada _Blockchain_. Coinwap menggunakan kontrak pintar untuk melakukan transfer tanpa memerlukan kepercayaan di antara kedua belah pihak.


Mari kita bayangkan sebuah contoh yang tidak mungkin terjadi dengan Alice dan Bob. Alice memiliki 1 BTC yang diamankan dengan kunci privat $A$, dan Bob juga memiliki 1 BTC yang diamankan dengan kunci privat $B$. Secara teoritis, mereka dapat melakukan pertukaran pada kunci privat mereka melalui saluran komunikasi eksternal untuk melakukan transfer rahasia. Akan tetapi, metode ini memiliki risiko yang tinggi dalam hal kepercayaan. Tidak ada yang menghalangi Alice untuk menyimpan salinan kunci privat $A$ setelah pertukaran terjadi, dan bisa jadi Alice menggunakannya nanti untuk mencuri bitcoin, ketika kunci tersebut sudah berada di tangan Bob. Terlebih lagi, tidak ada jaminan bahwa Alice tidak akan menerima kunci privat $B$ milik Bob dan tidak akan pernah memberikan kunci privat $A$ miliknya dalam pertukaran. Oleh karena itu, pertukara ini bergantung pada kepercayaan yang berlebihan di antara kedua belah pihak, dan tidak efektif untuk memastikan transfer kepemilikan secara rahasia dan aman.


Untuk mengatasi masalah ini dan memungkinkan _coinswap_ antara pihak-pihak yang tidak saling percaya, kita akan menggunakan sistem kontrak pintar yang membuat pertukaran menjadi "atomik". Sistem ini dapat berupa HTLC (*Hash Time-Locked Contracts*) atau PTLC (*Point Time-Locked Contracts*). Kedua protokol ini beroperasi dengan cara yang sama, menggunakan sistem penguncian waktu yang memastikan bahwa pertukaran berhasil diselesaikan atau dibatalkan sepenuhnya, sehingga melindungi dana kedua belah pihak. Perbedaan utama antara HTLC dan PTLC adalah bahwa HTLC menggunakan _hash_ dan _preimage_ untuk mengamankan transaksi, sedangkan PTLC menggunakan Tanda Tangan Adaptor.


Dalam skenario _coinswap_ menggunakan HTLC atau PTLC antara Alice dan Bob, pertukaran berlangsung dengan cara yang aman: berhasil dan masing-masing menerima BTC satu sama lain, atau gagal dan masing-masing masih menyimpan BTC-nya sendiri. Hal ini membuat salah satu pihak tidak mungkin menipu atau mencuri BTC pihak lain.


Penggunaan Tanda Tangan Adaptor sangat menarik dalam konteks ini, karena memungkinkan untuk membuang skrip tradisional (mekanisme yang kadang-kadang disebut sebagai "skrip tanpa skrip"). Hal ini mengurangi biaya yang terkait dengan pertukaran. Keuntungan utama lain dari Tanda Tangan Adaptor adalah bahwa mereka tidak memerlukan penggunaan _hash_ yang sama untuk kedua belah pihak yang bertransaksi, sehingga menghindari kebutuhan untuk mengungkapkan hubungan langsung di antara mereka dalam jenis pertukaran tertentu.
