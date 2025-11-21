---
term: TANDA TANGAN ADAPTOR

---
Metode kriptografi yang memungkinkan penggabungan tanda tangan asli dengan tanda tangan tambahan (disebut "tanda tangan adaptor") untuk mengungkapkan bagian data rahasia. Metode ini bekerja sedemikian rupa sehingga dengan mengetahui dua elemen dari tiga elemen ini: tanda tangan yang sah, tanda tangan adaptor, dan sebuah rahasia (_secret_), kita dapat mengetahui elemen ketiga yang hilang. Salah satu sifat yang menarik dari metode ini adalah jika kita mengetahui tanda tangan adaptor dan titik tertentu pada kurva elips yang terhubung dengan rahasia yang digunakan untuk menghitung tanda tangan adaptor ini, kita dapat memperoleh tanda tangan adaptor kita sendiri yang akan cocok dengan rahasia yang sama, tanpa harus memiliki akses langsung ke rahasia itu sendiri. Dalam sebuah pertukaran antara dua pihak yang tidak saling mempercayai, teknik ini memungkinkan kedua informasi sensitif diungkapkan secara bersamaan kepada kedua belah pihak. Proses ini menghilangkan kebutuhan akan kepercayaan dalam transaksi instan seperti *Coin Swap* atau *Atomic Swap*. Mari kita ambil sebuah contoh untuk memahaminya dengan lebih baik. Alice dan Bob ingin saling mengirim 1 BTC, tetapi mereka percaya satu sama lain. Oleh karena itu, mereka akan menggunakan tanda tangan adaptor untuk menghilangkan kebutuhan akan kepercayaan pada pihak lain dalam pertukaran ini (sehingga menjadikannya pertukaran "atomik"). Mereka melanjutkan sebagai berikut:

- Alice memulai _Atomic Swap_ ini. Dia membuat transaksi $m_A$ untuk mengirimkan 1 BTC ke Bob. Dia membuat tanda tangan $s_A$ untuk memvalidasi transaksi ini menggunakan kunci pribadinya $p_A$ ($P_A = p_A \cdot G$), dan menggunakan _nonce_ $n_A$ dan rahasia $t$ ($N_A = n_A \cdot G$ dan $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$

- Alice menghitung tanda tangan adaptor $s_A'$ dari rahasia $t$ dan tanda tangan aslinya $s_A$:

$$s_A' = s_A - t$$

- Alice mengirimkan tanda tangan adaptor $s_A'$ kepada Bob, transaksi yang belum ditandatangani $m_A$, titik $T$ yang berhubungan dengan rahasia, dan titik $N_A$ yang berhubungan dengan _nonce_. Potongan-potongan informasi ini disebut "adaptor". Perhatikan bahwa hanya dengan informasi ini, Bob tidak dapat mendapat BTC milik Alice.
- Akan tetapi, Bob dapat memverifikasi bahwa Alice tidak sedang menipu. Untuk melakukan hal ini, dia memeriksa bahwa tanda tangan adaptor Alice $s_A'$ sesuai dengan transaksi yang dijanjikan $m_A$. Jika persamaan berikut ini benar, maka ia yakin bahwa tanda tangan adaptor Alice valid:

$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$

- Verifikasi ini memberikan jaminan kepada Bob dari Alice, sehingga ia dapat melanjutkan proses pertukaran atom tanpa khawatir. Dia kemudian akan membuat transaksinya sendiri $m_B$ yang mengirimkan 1 BTC kepada Alice dan tanda tangan adaptornya sendiri $s_B'$, yang akan ditautkan dengan rahasia $t$ yang sama yang hanya diketahui oleh Alice untuk saat ini (Bob tidak mengetahui nilai $t$ ini, tetapi hanya titik yang sesuai dengan $T$ yang diberikan oleh Alice): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$

- Bob mengirimkan tanda tangan adaptornya, $s_B'$, kepada Alice, transaksi yang belum ditandatangani $m_B$, titik yang berhubungan dengan rahasia $T$, dan titik yang berhubungan dengan _nonce_ $N_B$. Alice sekarang dapat menggabungkan tanda tangan adaptor Bob $s_B'$ dengan rahasia $t$, yang hanya diketahui olehnya, untuk menghitung tanda tangan yang valid $s_B$ untuk transaksi $m_B$ yang mengirimkan BTC Bob kepadanya:

$$s_B = s_B' + t$$

$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$

- Alice mengumumkan transaksi yang ditandatangani ini $m_B$ di _blockchain_ Bitcoin untuk mendapatkan kembali BTC yang dijanjikan Bob kepadanya. Bob mengetahui transaksi ini di _blockchain_. Dengan demikian, ia dapat mengetahui tanda tangan $s_B = s_B' + t$. Dari informasi ini, Bob dapat mengisolasi rahasia $t$ yang ia butuhkan:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$

- Akan tetapi, rahasia $t$ ini adalah satu-satunya informasi yang tak dimiliki oleh Bob untuk menghasilkan tanda tangan yang valid $s_A$, dari tanda tangan adaptor Alice, $s_A'$, yang akan memungkinkannya untuk validasi transaksi $m_A$ (Transaksi yang mengirimkan BTC dari Alice ke Bob). Dia kemudian menghitung $s_A$ dan mengumumkan transaksi $m_A$ secara bergantian: $$s_A = s_A' + t$$

$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
