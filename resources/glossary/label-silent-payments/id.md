---
term: LABEL (PEMBAYARAN DIAM)

---
Dalam protokol Pembayaran Senyap, label adalah bilangan bulat yang digunakan untuk memodifikasi alamat statis awal untuk membuat banyak alamat statis lainnya. Penggunaan label ini memungkinkan pemisahan pembayaran yang dikirim melalui Silent Payments, dengan menggunakan alamat statis yang berbeda untuk setiap penggunaan, tanpa menambah beban operasional yang berlebihan untuk mendeteksi pembayaran ini (pemindaian). Bob menggunakan alamat statis $B$, yang terdiri dari dua kunci publik: $B_{\text{scan}}$ untuk pemindaian dan $B_{\text{spend}}$ untuk pengeluaran. Hash dari $b_{\text{scan}}}$ dan sebuah bilangan bulat $m$, yang dikalikan secara skalar dengan titik generator $G$, ditambahkan ke kunci publik pembelanjaan $B_{\text{spend}}}$ untuk membuat semacam kunci publik pembelanjaan baru $B_m$:

$$ B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G $$

Sebagai contoh, kunci pertama $B_1$ diperoleh dengan cara ini:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Alamat statis yang diterbitkan oleh Bob sekarang akan terdiri dari $B_{\text{scan}}$ dan $B_m$. Sebagai contoh, alamat statis pertama dengan label $ 1$ adalah:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Kita hanya akan memulai dari label $1$, karena label $0$ dicadangkan untuk uang kembalian. Alice, yang ingin mengirim bitcoin ke alamat statis berlabel yang disediakan oleh Bob, akan mendapatkan alamat pembayaran unik $P_0$ menggunakan $B_1$ yang baru, bukannya $B_{\text{spend}}$:

$$ P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$

Pada kenyataannya, Alice mungkin tidak mengetahui bahwa Bob memiliki alamat berlabel, karena dia hanya menggunakan bagian kedua dari alamat statis yang dia berikan, yang dalam hal ini adalah nilai $B_1$ daripada $B_{\text{pengeluaran}}$. Untuk memindai pembayaran, Bob akan selalu menggunakan nilai alamat statis awalnya dengan $B_{\text{spend}}$ dengan cara ini:

$$ P_0 = B_{\text{buang}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Kemudian, ia akan mengurangkan nilai yang ia temukan untuk $P_0$ dari setiap output satu per satu. Kemudian dia akan memeriksa apakah salah satu dari hasil pengurangan ini cocok dengan nilai dari salah satu label yang dia gunakan pada dompetnya. Jika cocok, sebagai contoh, untuk output #4 dengan label $1$, ini berarti bahwa output ini merupakan sebuah Silent Payment yang terkait dengan alamat statisnya yang berlabel $B_1$:

$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Ini berhasil karena:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Berkat metode ini, Bob dapat menggunakan banyak alamat statis (dengan $B_1$, $B_2$, $B_3$...), semua berasal dari alamat statis dasarnya ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), dalam rangka memisahkan penggunaan dengan benar.

Akan tetapi, pemisahan alamat statis ini hanya berlaku dari perspektif manajemen dompet pribadi, tetapi tidak memungkinkan untuk pemisahan identitas. Karena semuanya memiliki $B_{\text{scan}}$ yang sama, sangat mudah untuk mengasosiasikan semua alamat statis dan menyimpulkan bahwa mereka adalah milik satu entitas.