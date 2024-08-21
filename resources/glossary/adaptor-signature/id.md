---
term: TANDA TANGAN ADAPTOR
---

Metode kriptografi yang memungkinkan penggabungan tanda tangan asli dengan tanda tangan tambahan (disebut "tanda tangan adaptor") untuk mengungkapkan sepotong data rahasia. Metode ini bekerja sedemikian rupa sehingga mengetahui dua elemen di antara tanda tangan yang valid, tanda tangan adaptor, dan rahasia memungkinkan untuk mendeduksi elemen ketiga yang hilang. Salah satu properti menarik dari metode ini adalah jika kita mengetahui tanda tangan adaptor pihak lawan dan titik spesifik pada kurva elips yang terkait dengan rahasia yang digunakan untuk menghitung tanda tangan adaptor ini, kita kemudian dapat menurunkan tanda tangan adaptor kita sendiri yang akan cocok dengan rahasia yang sama, tanpa pernah memiliki akses langsung ke rahasia itu sendiri. Dalam pertukaran antara dua pemangku kepentingan yang tidak saling percaya, teknik ini memungkinkan pengungkapan simultan dua potongan informasi sensitif antara para peserta. Proses ini menghilangkan kebutuhan akan kepercayaan dalam transaksi instan seperti Coin Swap atau Atomic Swap. Mari kita ambil contoh untuk memahaminya lebih baik. Alice dan Bob ingin saling mengirim 1 BTC, tetapi mereka tidak saling percaya. Mereka akan menggunakan tanda tangan adaptor untuk meniadakan kebutuhan akan kepercayaan pada pihak lain dalam pertukaran ini (sehingga menjadikannya pertukaran "atomik"). Mereka melanjutkan sebagai berikut:
* Alice memulai pertukaran atomik ini. Dia membuat transaksi $m_A$ yang mengirim 1 BTC ke Bob. Dia membuat tanda tangan $s_A$ yang memvalidasi transaksi ini menggunakan kunci privatnya $p_A$ ($P_A = p_A \cdot G$), dan menggunakan nonce $n_A$ dan rahasia $t$ ($N_A = n_A \cdot G$ dan $T = t \cdot G$): 
$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$
&nbsp;
* Alice menghitung tanda tangan adaptor $s_A'$ dari rahasia $t$ dan tanda tangan aslinya $s_A$:  
$$s_A' = s_A - t$$
&nbsp;
* Alice mengirimkan kepada Bob tanda tangan adaptor $s_A'$, transaksi yang belum ditandatangani $m_A$, titik yang sesuai dengan rahasia $T$, dan titik yang sesuai dengan nonce $N_A$. Kita menyebut potongan informasi ini sebagai "adaptor". Perhatikan bahwa dengan hanya informasi ini, Bob tidak dapat memulihkan BTC Alice.
* Namun, Bob dapat memverifikasi bahwa Alice tidak menipunya. Untuk melakukan ini, dia memeriksa bahwa tanda tangan adaptor Alice $s_A'$ cocok dengan transaksi yang dijanjikan $m_A$. Jika persamaan berikut ini benar, maka dia yakin bahwa tanda tangan adaptor Alice valid: 
$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;
* Verifikasi ini memberikan Bob jaminan dari Alice, sehingga dia dapat melanjutkan proses pertukaran atomik dengan tenang. Dia kemudian akan membuat transaksi sendiri $m_B$ yang mengirim 1 BTC ke Alice dan tanda tangan adaptornya sendiri $s_B'$, yang akan terkait dengan rahasia $t$ yang sama yang hanya diketahui Alice untuk saat ini (Bob tidak mengetahui nilai $t$ ini, tetapi hanya titiknya $T$ yang telah diberikan Alice kepadanya): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$
&nbsp;
* Bob mengirimkan kepada Alice tanda tangan adaptornya $s_B'$, transaksi yang belum ditandatangani $m_B$, titik yang sesuai dengan rahasia $T$, dan titik yang sesuai dengan nonce $N_B$. Alice sekarang dapat menggabungkan tanda tangan adaptor Bob $s_B'$ dengan rahasia $t$, yang hanya dia yang tahu, untuk menghitung tanda tangan yang valid $s_B$ untuk transaksi $m_B$ yang mengirimkan BTC Bob kepadanya: $$s_B = s_B' + t$$
&nbsp;
$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$
&nbsp;
* Alice menyiarkan transaksi yang telah ditandatangani ini $m_B$ di blockchain Bitcoin untuk memulihkan BTC yang dijanjikan Bob kepadanya. Bob mengetahui transaksi ini di blockchain. Dengan demikian, ia dapat mengekstrak tanda tangan $s_B = s_B' + t$. Dari informasi ini, Bob dapat mengisolasi rahasia terkenal $t$ yang dia butuhkan:
$$t = (s_B' + t) - s_B' = s_B - s_B'$$
&nbsp;
* Namun, rahasia $t$ ini adalah satu-satunya informasi yang hilang bagi Bob untuk menghasilkan tanda tangan yang valid $s_A$, dari tanda tangan adaptor Alice $s_A'$, yang akan memungkinkannya untuk memvalidasi transaksi $m_A$ yang mengirim BTC dari Alice ke Bob. Dia kemudian menghitung $s_A$ dan menyiarkan transaksi $m_A$ secara bergantian: $$s_A = s_A' + t$$
&nbsp;
$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$