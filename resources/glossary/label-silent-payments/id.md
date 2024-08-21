---
term: LABEL (PEMBAYARAN SILENT)
---

Dalam protokol Pembayaran Silent, label adalah bilangan bulat yang digunakan untuk memodifikasi alamat statis awal agar dapat menciptakan banyak alamat statis lainnya. Penggunaan label ini memungkinkan untuk segregasi pembayaran yang dikirim melalui Pembayaran Silent, dengan menggunakan alamat statis yang berbeda untuk setiap penggunaan, tanpa meningkatkan beban operasional untuk mendeteksi pembayaran ini (pemindaian). Bob menggunakan alamat statis $B$, yang terdiri dari dua kunci publik: $B_{\text{scan}}$ untuk pemindaian dan $B_{\text{spend}}$ untuk pengeluaran. Hash dari $b_{\text{scan}}$ dan sebuah bilangan bulat $m$, dikalikan skalar dengan titik generator $G$, ditambahkan ke kunci publik pengeluaran $B_{\text{spend}}$ untuk menciptakan semacam kunci publik pengeluaran baru $B_m$:

$$  B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$

Sebagai contoh, kunci pertama $B_1$ diperoleh dengan cara ini:

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

Alamat statis yang dipublikasikan oleh Bob sekarang akan terdiri dari $B_{\text{scan}}$ dan $B_m$. Sebagai contoh, alamat statis pertama dengan label $1$ akan menjadi:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Kita hanya memulai dari label $1$, karena label $0$ disediakan untuk kembalian. Alice, yang ingin mengirim bitcoin ke alamat statis berlabel yang disediakan oleh Bob, akan menurunkan alamat pembayaran unik $P_0$ menggunakan $B_1$ baru daripada $B_{\text{spend}}$:

$$  P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Dalam kenyataannya, Alice mungkin bahkan tidak tahu bahwa Bob memiliki alamat berlabel, karena dia hanya menggunakan bagian kedua dari alamat statis yang dia berikan, yang dalam kasus ini adalah nilai $B_1$ daripada $B_{\text{spend}}$. Untuk memindai pembayaran, Bob akan selalu menggunakan nilai dari alamat statis awalnya dengan $B_{\text{spend}}$ dengan cara ini:

$$   P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$
Kemudian, dia akan sekedar mengurangkan nilai yang dia temukan untuk $P_0$ dari setiap output satu per satu. Dia kemudian memeriksa apakah salah satu hasil dari pengurangan ini cocok dengan nilai salah satu label yang dia gunakan di dompetnya. Jika cocok, misalnya, untuk output #4 dengan label $1$, ini berarti bahwa output ini adalah Pembayaran Silent yang terkait dengan alamat statis berlabelnya $B_1$:
$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Ini berhasil karena:
Berdasarkan metode ini, Bob dapat menggunakan berbagai alamat statis (dengan $B_1$, $B_2$, $B_3$...), semua berasal dari alamat statis dasarnya ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), untuk memisahkan penggunaan dengan tepat.

Namun, pemisahan alamat statis ini hanya valid dari perspektif manajemen dompet pribadi, tetapi tidak memungkinkan untuk pemisahan identitas. Karena semuanya memiliki $B_{\text{scan}}$ yang sama, sangat mudah untuk mengasosiasikan semua alamat statis bersama-sama dan menyimpulkan bahwa mereka milik entitas tunggal.