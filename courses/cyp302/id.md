---
name: Pengantar ke Kriptografi Formal
goal: Pengantar mendalam ke dalam ilmu dan praktik kriptografi.
objectives:
  - Menjelajahi sandi Beale dan metode kriptografi modern untuk memahami konsep dasar dan historis kriptografi.
  - Mendalami teori bilangan, grup, dan bidang untuk menguasai konsep matematika kunci yang mendasari kriptografi.
  - Mempelajari stream cipher RC4 dan AES dengan kunci 128-bit untuk mempelajari tentang algoritma kriptografi simetris.
  - Menyelidiki sistem kripto RSA, distribusi kunci, dan fungsi hash untuk menjelajahi kriptografi asimetris.

---
# Mendalami Kriptografi

Sulit untuk menemukan banyak materi yang menawarkan titik tengah yang baik dalam pendidikan kriptografi.

Di satu sisi, ada tulisan formal yang panjang, yang benar-benar hanya dapat diakses oleh mereka yang memiliki latar belakang kuat dalam matematika, logika, atau disiplin formal lainnya. Di sisi lain, ada pengantar tingkat sangat tinggi yang benar-benar menyembunyikan terlalu banyak detail bagi siapa saja yang setidaknya sedikit penasaran.

Pengantar ini ke kriptografi berusaha untuk menangkap titik tengah tersebut. Meskipun seharusnya cukup menantang dan terperinci bagi siapa saja yang baru mengenal kriptografi, ini bukan lubang kelinci dari tulisan dasar yang tipikal.

+++

# Pengantar ke Kriptografi
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Deskripsi Singkat
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Buku ini menawarkan pengantar mendalam ke dalam ilmu dan praktik kriptografi. Di mana mungkin, fokusnya adalah pada eksposisi konseptual, daripada formal dari materi tersebut.

> Kursus ini berdasarkan [repo JWBurgers](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Semua hak miliknya. Konten ini belum selesai dan hanya di sini untuk menunjukkan bagaimana kita bisa mengintegrasikannya jika JWburger setuju.

### Motivasi dan Tujuan

Sulit untuk menemukan banyak materi yang menawarkan titik tengah yang baik dalam pendidikan kriptografi.

Di satu sisi, ada tulisan formal yang panjang, yang benar-benar hanya dapat diakses oleh mereka yang memiliki latar belakang kuat dalam matematika, logika, atau disiplin formal lainnya. Di sisi lain, ada pengantar tingkat sangat tinggi yang benar-benar menyembunyikan terlalu banyak detail bagi siapa saja yang setidaknya sedikit penasaran.

Pengantar ini ke kriptografi berusaha untuk menangkap titik tengah tersebut. Meskipun seharusnya cukup menantang dan terperinci bagi siapa saja yang baru mengenal kriptografi, ini bukan lubang kelinci dari tulisan dasar yang tipikal.

### Audiens Target

Dari pengembang hingga orang yang secara intelektual penasaran, buku ini berguna bagi siapa saja yang menginginkan pemahaman lebih dari sekadar permukaan tentang kriptografi. Jika tujuan Anda adalah untuk menguasai bidang kriptografi, maka buku ini juga merupakan titik awal yang baik.

### Pedoman Membaca

Buku ini saat ini berisi tujuh bab: "Apa itu Kriptografi?" (Bab 1), "Dasar-dasar Matematika Kriptografi I" (Bab 2), "Dasar-dasar Matematika Kriptografi II" (Bab 3), "Kriptografi Simetris" (Bab 4), "RC4 dan AES" (Bab 5), "Kriptografi Asimetris" (Bab 6), dan "Sistem Kripto RSA" (Bab 7). Sebuah bab terakhir, "Kriptografi dalam Praktik," masih akan ditambahkan. Fokusnya adalah pada berbagai aplikasi kriptografi, termasuk keamanan lapisan transport, perutean bawang, dan sistem pertukaran nilai Bitcoin.
Kecuali Anda memiliki latar belakang yang kuat dalam matematika, teori angka mungkin merupakan topik yang paling sulit dalam buku ini. Saya menawarkan gambaran umum tentang itu di Bab 3, dan itu juga muncul dalam paparan AES di Bab 5 dan kriptosistem RSA di Bab 7.
Jika Anda benar-benar kesulitan dengan detail formal dalam bagian-bagian buku ini, saya sarankan Anda untuk pertama kali membacanya secara garis besar.

### Pengakuan

Buku yang paling berpengaruh dalam membentuk buku ini adalah _Introduction to Modern Cryptography_ oleh Jonathan Katz dan Yehuda Lindell, CRC Press (Boca Raton, FL), 2015. Sebuah kursus pendamping tersedia di Coursera dengan nama "Cryptography."

Sumber tambahan utama yang telah membantu dalam membuat gambaran umum dalam buku ini adalah Simon Singh, _The Code Book_, Fourth Estate (London, 1999); Christof Paar dan Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) dan kursus berdasarkan buku oleh Paar yang berjudul “Introduction to Cryptography” (tersedia di https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); dan Bruce Schneier, Applied Cryptography, edisi ke-2, 2015 (Indianapolis, IN: John Wiley & Sons).

Saya hanya akan menyitir informasi dan hasil yang sangat spesifik yang saya ambil dari sumber-sumber ini, tetapi ingin mengakui secara umum hutang budi saya kepada mereka di sini.

Untuk pembaca yang ingin mencari pengetahuan lebih lanjut tentang kriptografi setelah pengantar ini, saya sangat merekomendasikan buku Katz dan Lindell. Kursus Katz di Coursera agak lebih mudah diakses daripada bukunya.

### Kontribusi

Silakan lihat file kontribusi di repositori untuk beberapa pedoman tentang cara mendukung proyek.

# Apa itu Kriptografi?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

Mari kita mulai penyelidikan kita ke dalam bidang kriptografi dengan salah satu episode yang lebih menarik dan menghibur dalam sejarahnya: yaitu sandi Beale.<sup>[1](#footnote1)</sup>

Menurut saya, cerita tentang sandi Beale lebih mungkin fiksi daripada kenyataan. Namun, konon berlangsung sebagai berikut.

## Sandi Beale
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>

Pada musim dingin tahun 1820 dan 1822, seorang pria bernama Thomas J. Beale menginap di sebuah penginapan milik Robert Morriss di Lynchburg (Virginia). Di akhir masa inap Beale yang kedua, ia menyerahkan sebuah kotak besi yang berisi kertas-kertas berharga kepada Morriss untuk disimpan dengan aman.

Beberapa bulan kemudian, Morriss menerima surat dari Beale bertanggal 9 Mei 1822. Surat itu menekankan nilai besar dari isi kotak besi tersebut dan menyampaikan beberapa instruksi kepada Morriss: jika Beale atau salah satu rekanannya tidak pernah datang untuk mengklaim kotak tersebut, ia harus membukanya tepat sepuluh tahun dari tanggal surat itu (yaitu, 9 Mei 1832). Beberapa kertas di dalamnya akan ditulis dalam teks biasa. Beberapa lainnya, bagaimanapun, akan “tidak dapat dimengerti tanpa bantuan kunci.” “Kunci” ini, kemudian, akan disampaikan kepada Morriss oleh seorang teman tak dikenal dari Beale pada Juni 1832.
Meskipun telah diberi instruksi yang jelas, Morriss tidak membuka kotak tersebut pada Mei 1832 dan teman misterius Beale juga tidak muncul pada Juni tahun itu. Baru pada tahun 1845 pemilik penginapan tersebut akhirnya memutuskan untuk membuka kotak itu. Di dalamnya, Morriss menemukan sebuah catatan yang menjelaskan bagaimana Beale dan rekan-rekannya menemukan emas dan perak di Barat dan menguburnya bersama beberapa perhiasan untuk penyimpanan yang aman. Selain itu, kotak tersebut berisi tiga **ciphertext**: yaitu, teks yang ditulis dalam kode yang memerlukan **kunci kriptografi**, atau sebuah rahasia, dan algoritma pendamping untuk membukanya. Proses membuka sebuah ciphertext dikenal sebagai **dekripsi**, sementara proses menguncinya dikenal sebagai **enkripsi**. (Seperti dijelaskan dalam Bab 3, istilah cipher dapat memiliki berbagai makna. Dalam nama "Beale ciphers", ini adalah singkatan dari ciphertexts.)
Ketiga ciphertext yang Morriss temukan dalam kotak besi masing-masing terdiri dari serangkaian angka yang dipisahkan oleh koma. Menurut catatan Beale, ciphertext ini secara terpisah memberikan lokasi harta karun, isi dari harta karun, dan daftar nama dengan ahli waris yang sah untuk harta karun tersebut dan bagiannya (informasi terakhir ini relevan jika Beale dan rekan-rekannya tidak pernah datang untuk mengklaim kotak tersebut).

Morris mencoba mendekripsi ketiga ciphertext selama dua puluh tahun. Ini akan mudah dengan kunci tersebut. Namun Morriss tidak memiliki kunci dan tidak berhasil dalam upayanya untuk memulihkan teks asli, atau **plaintext** seperti yang biasa disebut dalam kriptografi.

Mendekati akhir hidupnya, Morriss menyerahkan kotak tersebut kepada seorang teman pada tahun 1862. Teman ini kemudian menerbitkan sebuah pamflet pada tahun 1885, dengan nama samaran J.B. Ward. Ini mencakup deskripsi sejarah (yang diduga) dari kotak tersebut, ketiga ciphertext, dan solusi yang dia temukan untuk ciphertext kedua. (Tampaknya, ada satu kunci untuk setiap ciphertext, dan bukan satu kunci yang berfungsi pada ketiga ciphertext seperti yang awalnya Beale usulkan dalam suratnya kepada Morriss.)

Anda dapat melihat ciphertext kedua di *Gambar 2* di bawah ini.<sup>[2](#footnote2)</sup> Kunci untuk ciphertext ini adalah Deklarasi Kemerdekaan Amerika Serikat. Prosedur dekripsi ini didasarkan pada penerapan dua aturan berikut:

* Untuk setiap angka n dalam ciphertext, temukan kata ke-n dalam Deklarasi Kemerdekaan Amerika Serikat
* Gantikan angka n dengan huruf pertama dari kata yang Anda temukan

*Gambar 1: Beale cipher no. 2*

![Gambar 1: Beale cipher no 2.](assets/Figure1-1.webp "Gambar 1: Beale cipher no. 2")

Misalnya, angka pertama dari ciphertext kedua adalah 115. Kata ke-115 dari Deklarasi Kemerdekaan adalah “instituted,” jadi huruf pertama dari plaintext adalah “i.” Ciphertext tidak secara langsung menunjukkan spasi kata dan kapitalisasi. Namun, setelah mendekripsi beberapa kata pertama, Anda dapat secara logis menyimpulkan bahwa kata pertama dari plaintext adalah sederhana “I.” (Plaintext dimulai dengan frasa “I have deposited in the county of Bedford.”)
Setelah dekripsi, pesan kedua memberikan isi harta karun secara detail (emas, perak, dan permata), dan menyarankan bahwa harta tersebut dikubur dalam pot besi dan ditutupi dengan batu di Bedford County (Virginia). Orang-orang menyukai misteri yang baik, sehingga usaha besar telah dikeluarkan untuk mendekripsi dua sandi Beale lainnya, terutama yang mendeskripsikan lokasi harta karun. Bahkan berbagai kriptografer terkemuka telah mencoba tangan mereka pada mereka. Namun, hingga saat ini, belum ada yang dapat mendekripsi dua ciphertext lainnya.

## Kriptografi Modern
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Cerita-cerita penuh warna seperti sandi Beale adalah apa yang kebanyakan dari kita asosiasikan dengan kriptografi. Namun, kriptografi modern berbeda dalam setidaknya empat cara penting dari contoh-contoh historis ini.

Pertama, secara historis kriptografi hanya berkaitan dengan **kerahasiaan** (atau kerahasiaan).<sup>[3](#footnote3)</sup> Ciphertext akan dibuat untuk memastikan bahwa hanya pihak-pihak tertentu yang dapat mengetahui informasi dalam plaintext, seperti dalam kasus sandi Beale. Agar skema enkripsi dapat melayani tujuan ini dengan baik, mendekripsi ciphertext hanya harus dapat dilakukan jika Anda memiliki kunci.

Kriptografi modern berkaitan dengan berbagai tema yang lebih luas daripada sekedar kerahasiaan. Tema-tema ini terutama meliputi (1) **integritas pesan**—yaitu, memastikan bahwa pesan tidak telah diubah; (2) **keaslian pesan**—yaitu, memastikan bahwa pesan benar-benar berasal dari pengirim tertentu; dan (3) **non-repudiasi**—yaitu, memastikan bahwa pengirim tidak dapat menyangkal nanti bahwa dia mengirim pesan.<sup>[4](#footnote4)</sup>

Sebuah perbedaan penting untuk diingat adalah, dengan demikian, antara **skema enkripsi** dan **skema kriptografi**. Skema enkripsi hanya berkaitan dengan kerahasiaan. Sementara skema enkripsi adalah skema kriptografi, sebaliknya tidak benar. Skema kriptografi juga dapat melayani tema utama lainnya dari kriptografi, termasuk integritas, keaslian, dan non-repudiasi.

Tema integritas dan keaslian sama pentingnya dengan kerahasiaan. Sistem komunikasi modern kita tidak akan dapat berfungsi tanpa jaminan mengenai integritas dan keaslian komunikasi. Non-repudiasi juga merupakan kekhawatiran penting, seperti untuk kontrak digital, tetapi kurang diperlukan secara luas dalam aplikasi kriptografi daripada kerahasiaan, integritas, dan keaslian.

Kedua, skema enkripsi klasik seperti sandi Beale selalu melibatkan satu kunci yang dibagi di antara semua pihak yang relevan. Namun, banyak skema kriptografi modern melibatkan tidak hanya satu, tetapi dua kunci: sebuah **kunci pribadi** dan **kunci publik**. Sementara yang pertama harus tetap pribadi dalam aplikasi apa pun, yang terakhir biasanya merupakan pengetahuan umum (karenanya, nama mereka masing-masing). Dalam ranah enkripsi, kunci publik dapat digunakan untuk mengenkripsi pesan, sementara kunci pribadi dapat digunakan untuk dekripsi.

Cabang kriptografi yang berurusan dengan skema di mana semua pihak berbagi satu kunci dikenal sebagai **kriptografi simetris**. Kunci tunggal dalam skema tersebut biasanya disebut **kunci pribadi** (atau kunci rahasia). Cabang kriptografi yang berurusan dengan skema yang memerlukan pasangan kunci pribadi-publik dikenal sebagai **kriptografi asimetris**. Cabang-cabang ini terkadang juga disebut sebagai **kriptografi kunci pribadi** dan **kriptografi kunci publik**, masing-masing (meskipun ini dapat menimbulkan kebingungan, karena skema kriptografi kunci publik juga memiliki kunci pribadi).
Kemunculan kriptografi asimetris pada akhir tahun 1970-an telah menjadi salah satu peristiwa terpenting dalam sejarah kriptografi. Tanpa itu, sebagian besar sistem komunikasi modern kita, termasuk Bitcoin, tidak akan mungkin ada, atau setidaknya sangat tidak praktis.
Pentingnya, kriptografi modern tidak eksklusif mempelajari skema kriptografi kunci simetris dan asimetris (meskipun itu mencakup sebagian besar bidang). Misalnya, kriptografi juga berkaitan dengan fungsi hash dan generator angka pseudorandom, dan Anda dapat membangun aplikasi berdasarkan primitif ini yang tidak terkait dengan kriptografi kunci simetris atau asimetris.

Ketiga, skema enkripsi klasik, seperti yang digunakan dalam sandi Beale, lebih merupakan seni daripada sains. Keamanan yang dirasakan mereka sebagian besar didasarkan pada intuisi mengenai kompleksitas mereka. Mereka biasanya akan diperbaiki ketika serangan baru terhadap mereka diketahui, atau ditinggalkan sepenuhnya jika serangan tersebut sangat parah. Namun, kriptografi modern adalah sains yang ketat dengan pendekatan formal dan matematis untuk mengembangkan dan menganalisis skema kriptografi.

Secara khusus, kriptografi modern berpusat pada **bukti keamanan** formal. Setiap bukti keamanan untuk skema kriptografi berlangsung dalam tiga langkah:

1. Pernyataan **definisi keamanan kriptografi**, yaitu, serangkaian tujuan keamanan dan ancaman yang ditimbulkan oleh penyerang.
2. Pernyataan asumsi matematis terkait dengan kompleksitas komputasi dari skema tersebut. Misalnya, skema kriptografi mungkin mengandung generator angka pseudorandom. Meskipun kita tidak dapat membuktikan keberadaan mereka, kita dapat mengasumsikan bahwa mereka ada.
3. Paparan **bukti keamanan** matematis dari skema berdasarkan konsep keamanan formal dan asumsi matematis apa pun.

Keempat, sedangkan secara historis kriptografi terutama digunakan dalam pengaturan militer, kini telah meresap ke dalam aktivitas sehari-hari kita di era digital. Apakah Anda berbanking online, memposting di media sosial, membeli produk dari Amazon dengan kartu kredit Anda, atau memberi tip bitcoin kepada teman, kriptografi adalah sine qua non dari era digital kita.

Mengingat empat aspek kriptografi modern ini, kita mungkin menggambarkan **kriptografi** modern sebagai ilmu yang berhubungan dengan pengembangan formal dan analisis skema kriptografi untuk mengamankan informasi digital terhadap serangan adversarial. Keamanan di sini harus dipahami secara luas sebagai pencegahan serangan yang merusak kerahasiaan, integritas, autentikasi, dan/atau non-repudiasi dalam komunikasi.

Kriptografi terbaik dilihat sebagai subdisiplin dari **cybersecurity**, yang berkaitan dengan pencegahan pencurian, kerusakan, dan penyalahgunaan sistem komputer. Perlu dicatat bahwa banyak kekhawatiran keamanan siber memiliki sedikit atau hanya koneksi parsial dengan kriptografi.

Misalnya, jika sebuah perusahaan menyimpan server mahal secara lokal, mereka mungkin khawatir dengan mengamankan perangkat keras ini dari pencurian dan kerusakan. Meskipun ini adalah kekhawatiran keamanan siber, ini sedikit berkaitan dengan kriptografi.

Untuk contoh lain, **serangan phishing** adalah masalah umum di era modern kita. Serangan ini mencoba menipu orang melalui e-mail atau media pesan lainnya untuk menyerahkan informasi sensitif seperti kata sandi atau nomor kartu kredit. Meskipun kriptografi dapat membantu mengatasi serangan phishing hingga batas tertentu, pendekatan komprehensif memerlukan lebih dari sekedar menggunakan beberapa kriptografi.

## Komunikasi Terbuka

Modern kriptografi dirancang untuk memberikan jaminan keamanan dalam lingkungan **komunikasi terbuka**. Jika saluran komunikasi kita sangat terlindungi sehingga penyadap tidak memiliki kesempatan untuk memanipulasi atau bahkan hanya mengamati pesan kita, maka kriptografi menjadi tidak perlu. Namun, sebagian besar saluran komunikasi kita, tidaklah sebaik itu terjaga.
Tulang punggung komunikasi di dunia modern adalah jaringan besar kabel serat optik. Melakukan panggilan telepon, menonton televisi, dan menjelajahi web di rumah modern umumnya bergantung pada jaringan kabel serat optik ini (persentase kecil mungkin hanya bergantung pada satelit). Memang benar Anda mungkin memiliki koneksi data yang berbeda di rumah Anda, seperti kabel koaksial, (asimetris) digital subscriber line, dan kabel serat optik. Namun, setidaknya di dunia maju, berbagai media data ini dengan cepat bergabung di luar rumah Anda ke sebuah node dalam jaringan besar kabel serat optik yang menghubungkan seluruh dunia. Pengecualian adalah beberapa area terpencil di dunia maju, seperti di Amerika Serikat dan Australia, di mana lalu lintas data mungkin masih juga bergerak jarak jauh melalui kabel telepon tembaga tradisional.
Akan mustahil untuk mencegah penyerang potensial dari mengakses secara fisik jaringan kabel ini dan infrastrukturnya. Faktanya, kita sudah tahu bahwa sebagian besar data kita diintersepsi oleh berbagai agen intelijen nasional di persimpangan krusial Internet.<sup>[7](#footnote7)</sup> Ini termasuk segala sesuatu dari pesan Facebook hingga alamat situs web yang Anda kunjungi.

Meskipun mengawasi data dalam skala besar memerlukan lawan yang kuat, seperti agen intelijen nasional, penyerang dengan sedikit sumber daya dapat dengan mudah mencoba menyadap dalam skala lebih lokal. Meskipun ini bisa terjadi pada level menyadap kabel, jauh lebih mudah untuk hanya mengintersepsi komunikasi nirkabel.

Sebagian besar data jaringan lokal kita—baik di rumah, di kantor, atau di kafe—kini bergerak melalui gelombang radio ke titik akses nirkabel pada router serba guna, daripada melalui kabel fisik. Jadi, seorang penyerang memerlukan sedikit sumber daya untuk mengintersepsi lalu lintas lokal Anda. Ini sangat mengkhawatirkan karena sebagian besar orang sangat sedikit melakukan perlindungan terhadap data yang bergerak melintasi jaringan lokal mereka. Selain itu, penyerang potensial juga dapat menargetkan koneksi broadband seluler kita, seperti 3G, 4G, dan 5G. Semua komunikasi nirkabel ini adalah target yang mudah bagi penyerang.

Oleh karena itu, gagasan untuk menjaga komunikasi tetap rahasia dengan melindungi saluran komunikasi adalah aspirasi yang sangat ilusif bagi sebagian besar dunia modern. Semua yang kita ketahui menjamin paranoia yang parah: Anda harus selalu mengasumsikan bahwa seseorang sedang mendengarkan. Dan kriptografi adalah alat utama yang kita miliki untuk mendapatkan jenis keamanan apa pun dalam lingkungan modern ini.

### Catatan
[^1]: Untuk ringkasan cerita yang baik, lihat Simon Singh, *The Code Book*, Fourth Estate (London, 1999), hal. 82-99. Sebuah film pendek dari cerita tersebut dibuat oleh Andrew Allen pada tahun 2010. Anda dapat menemukan film tersebut, “The Thomas Beale Cipher,” di situs webnya [^1].

[^2]: Gambar ini tersedia di halaman Wikipedia untuk sandi Beale [^2].

[^3]: Untuk lebih tepatnya, aplikasi penting dari skema kriptografi telah berhubungan dengan kerahasiaan. Anak-anak, misalnya, sering menggunakan skema kriptografi sederhana untuk “kesenangan”. Kerahasiaan bukanlah hal yang benar-benar menjadi perhatian dalam kasus tersebut [^3].

[^4]: Bruce Schneier, *Applied Cryptography*, edisi ke-2, 2015 (Indianapolis, IN: John Wiley & Sons), hal. 2 [^4].

[^5]: Lihat Jonathan Katz dan Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), khususnya hal. 16–23, untuk deskripsi yang baik [^5].

[^6]: Cf. Katz dan Lindell, ibid., hal. 3. Saya pikir karakterisasi mereka memiliki beberapa masalah, jadi saya menyajikan versi pernyataan mereka yang sedikit berbeda di sini [^6].
[^7]: Lihat, sebagai contoh, Olga Khazan, "The creepy, long-standing practice of undersea cable tapping", *The Atlantic*, 16 Juli 2013 (tersedia di [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)) [^7].

# Dasar Matematika Kriptografi I
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

Kriptografi bergantung pada matematika. Dan jika Anda ingin membangun pemahaman tentang kriptografi yang lebih dari sekedar permukaan, Anda perlu merasa nyaman dengan matematika tersebut.

Bab ini memperkenalkan sebagian besar matematika dasar yang akan Anda temui dalam mempelajari kriptografi. Topik-topik tersebut meliputi variabel acak, operasi modulo, operasi XOR, dan pseudorandomness. Anda harus menguasai materi dalam bagian-bagian ini untuk pemahaman tentang kriptografi yang tidak sekedar permukaan.

Bab berikutnya membahas tentang teori bilangan, yang jauh lebih menantang.

## Variabel Acak
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Variabel acak biasanya ditandai dengan huruf kapital yang tidak dicetak tebal. Jadi, misalnya, kita mungkin berbicara tentang variabel acak X, variabel acak Y, atau variabel acak Z. Ini adalah notasi yang juga akan saya gunakan dari sini ke depan.

Sebuah **variabel acak** dapat mengambil dua atau lebih nilai yang mungkin, masing-masing dengan probabilitas positif tertentu. Nilai-nilai yang mungkin tersebut terdaftar dalam **himpunan hasil**.

Setiap kali Anda **mengambil sampel** dari variabel acak, Anda menarik nilai tertentu dari himpunan hasilnya sesuai dengan probabilitas yang telah ditentukan.

Mari kita lihat contoh sederhana. Misalkan variabel X yang didefinisikan sebagai berikut:

* X memiliki himpunan hasil {1,2}
* Pr [X = 1] = 0.5
* Pr [X = 2] = 0.5

Mudah untuk melihat bahwa X adalah variabel acak. Pertama, ada dua atau lebih nilai yang mungkin diambil oleh X, yaitu 1 dan 2. Kedua, setiap nilai yang mungkin memiliki probabilitas positif terjadi setiap kali Anda mengambil sampel X, yaitu 0.5.

Yang dibutuhkan oleh variabel acak hanyalah himpunan hasil dengan dua atau lebih kemungkinan, di mana setiap kemungkinan memiliki probabilitas positif terjadi saat pengambilan sampel. Pada prinsipnya, maka, variabel acak dapat didefinisikan secara abstrak, tanpa konteks apa pun. Dalam kasus ini, Anda mungkin berpikir tentang "pengambilan sampel" sebagai menjalankan beberapa eksperimen alami untuk menentukan nilai dari variabel acak tersebut.

Variabel X di atas didefinisikan secara abstrak. Anda mungkin, dengan demikian, berpikir tentang mengambil sampel dari variabel X di atas sebagai melempar koin yang adil dan menetapkan "2" dalam kasus kepala dan "1" dalam kasus ekor. Untuk setiap sampel dari X, Anda melempar koin lagi.

Atau, Anda juga mungkin berpikir tentang mengambil sampel X, sebagai melempar dadu yang adil dan menetapkan "2" jika dadu mendarat pada 1, 3, atau 4, dan menetapkan "1" jika dadu mendarat pada 2, 5, atau 6. Setiap kali Anda mengambil sampel X, Anda melempar dadu lagi.

Sebenarnya, setiap eksperimen alami yang memungkinkan Anda untuk mendefinisikan probabilitas dari nilai-nilai yang mungkin dari X di atas dapat dibayangkan berkaitan dengan penggambaran.
Sering kali, variabel acak tidak hanya diperkenalkan secara abstrak. Sebaliknya, himpunan nilai hasil yang mungkin memiliki makna nyata di dunia nyata (bukan hanya sebagai angka). Selain itu, nilai hasil ini mungkin didefinisikan terhadap beberapa jenis eksperimen tertentu (bukan sebagai eksperimen alami apa pun dengan nilai-nilai tersebut).
Mari kita pertimbangkan contoh variabel X yang tidak didefinisikan secara abstrak. X didefinisikan sebagai berikut untuk menentukan tim mana yang memulai permainan sepak bola:

* X memiliki himpunan hasil {tim merah memulai, tim biru memulai}
* Lempar koin tertentu C: ekor = “tim merah memulai”; kepala = “tim biru memulai”
* Pr [X = tim merah memulai] = 0,5
* Pr [X = tim biru memulai] = 0,5

Dalam kasus ini, himpunan hasil dari X diberikan dengan makna konkret, yaitu tim mana yang memulai dalam permainan sepak bola. Selain itu, hasil yang mungkin dan probabilitas terkait mereka ditentukan oleh eksperimen konkret, yaitu melempar koin tertentu C.

Dalam diskusi tentang kriptografi, variabel acak biasanya diperkenalkan terhadap himpunan hasil dengan makna dunia nyata. Ini mungkin himpunan semua pesan yang dapat dienkripsi, dikenal sebagai ruang pesan, atau himpunan semua kunci yang dapat dipilih oleh pihak-pihak yang menggunakan enkripsi, dikenal sebagai ruang kunci.

Namun, variabel acak dalam diskusi tentang kriptografi biasanya tidak didefinisikan terhadap eksperimen alami tertentu, tetapi terhadap eksperimen apa pun yang mungkin menghasilkan distribusi probabilitas yang tepat.

Variabel acak dapat memiliki distribusi probabilitas diskrit atau kontinu. Variabel acak dengan **distribusi probabilitas diskrit**—yaitu, variabel acak diskrit—memiliki jumlah hasil yang mungkin terbatas. Variabel acak X dalam kedua contoh yang diberikan sejauh ini adalah diskrit.

**Variabel acak kontinu** sebaliknya dapat mengambil nilai dalam satu atau lebih interval. Anda mungkin mengatakan, misalnya, bahwa variabel acak, saat pengambilan sampel, akan mengambil nilai nyata apa pun antara 0 dan 1, dan bahwa setiap angka nyata dalam interval ini sama-sama mungkin. Dalam interval ini, ada nilai yang tak terbatas.

Untuk diskusi kriptografi, Anda hanya perlu memahami variabel acak diskrit. Setiap diskusi tentang variabel acak dari sini ke depan harus, oleh karena itu, dipahami sebagai merujuk pada variabel acak diskrit, kecuali dinyatakan sebaliknya.

### Menggambarkan variabel acak

Nilai-nilai yang mungkin dan probabilitas terkait untuk variabel acak dapat dengan mudah divisualisasikan melalui grafik. Misalnya, pertimbangkan variabel acak X dari bagian sebelumnya dengan himpunan hasil {1,2}, dan Pr [X = 1] = 0,5 dan Pr [X = 2] = 0,5. Kita biasanya akan menampilkan variabel acak semacam itu dalam bentuk grafik batang seperti di *Gambar 1*.

*Gambar 1: Variabel acak X*

![Gambar 1: Variabel acak X.](assets/Figure2-1.webp)

Bar yang lebar di *Gambar 1* jelas tidak dimaksudkan untuk menyarankan bahwa variabel acak X sebenarnya kontinu. Sebaliknya, bar dibuat lebar agar lebih menarik secara visual (hanya garis lurus ke atas memberikan visualisasi yang kurang intuitif).

### Variabel Seragam

Dalam ekspresi “variabel acak,” istilah “acak” hanya berarti “probabilistik”. Dengan kata lain, itu hanya berarti bahwa dua atau lebih hasil yang mungkin dari variabel terjadi dengan probabilitas tertentu. Namun, hasil-hasil ini tidak harus selalu sama kemungkinannya (meskipun istilah “acak” memang dapat memiliki makna itu dalam konteks lain).
Sebuah **variabel seragam** adalah kasus khusus dari variabel acak. Variabel ini dapat mengambil dua atau lebih nilai dengan probabilitas yang sama. Variabel acak X yang digambarkan dalam *Gambar 1* jelas merupakan variabel seragam, karena kedua hasil yang mungkin terjadi dengan probabilitas 0,5. Namun, banyak variabel acak yang bukan merupakan contoh dari variabel seragam.
Misalnya, pertimbangkan variabel acak Y. Ia memiliki himpunan hasil {1,2,3,8,10} dan distribusi probabilitas berikut: Pr [Y = 1] = 0,25; Pr [Y = 2] = 0,35; Pr [Y = 3] = 0,1; Pr [Y = 8] = 0,25; Pr [Y = 10] = 0,05.

Meskipun dua hasil yang mungkin memang memiliki probabilitas yang sama untuk terjadi, yaitu 1 dan 8, Y juga dapat mengambil nilai tertentu dengan probabilitas yang berbeda dari 0,25 saat pengambilan sampel. Oleh karena itu, meskipun Y memang merupakan variabel acak, ia bukan variabel seragam.

Sebuah penggambaran grafis dari Y disediakan dalam *Gambar 2*.

*Gambar 2: Variabel acak Y*

![Gambar 2: Variabel acak Y.](assets/Figure2-2.webp "Gambar 2: Variabel acak Y")

Sebagai contoh terakhir, pertimbangkan variabel acak Z. Ia memiliki himpunan hasil {1,3,7,11,12} dan distribusi probabilitas berikut: Pr (2) = 0,2; Pr (3) = 0,2; Pr (9) = 0,2; Pr (11) = 0,2; Pr (12) = 0,2. Anda dapat melihatnya digambarkan dalam Gambar 3. Variabel acak Z, berbeda dengan Y, memang merupakan variabel seragam, karena semua probabilitas untuk nilai yang mungkin saat pengambilan sampel adalah sama.

*Gambar 3: Variabel acak Z*

![Gambar 3: Variabel acak Z.](assets/Figure2-3.webp "Gambar 3: Variabel acak Z")


### Probabilitas Kondisional

Anggaplah Bob berniat untuk secara seragam memilih sebuah hari dari tahun kalender terakhir. Apa yang harus kita simpulkan adalah probabilitas hari yang dipilih berada di Musim Panas?

Selama kita berpikir proses Bob memang benar-benar seragam, kita harus menyimpulkan bahwa ada probabilitas 1/4 Bob memilih hari di Musim Panas. Ini adalah **probabilitas tak bersyarat** dari hari yang dipilih secara acak berada di Musim Panas.

Sekarang bayangkan jika, alih-alih secara seragam menarik hari kalender, Bob hanya memilih secara seragam dari hari-hari di mana suhu siang di Crystal Lake (New Jersey) adalah 21 derajat Celcius atau lebih tinggi. Dengan informasi tambahan ini, apa yang bisa kita simpulkan tentang probabilitas Bob akan memilih hari di Musim Panas?

Kita seharusnya benar-benar menarik kesimpulan yang berbeda dari sebelumnya, bahkan tanpa informasi spesifik lebih lanjut (misalnya, suhu siang setiap hari tahun kalender terakhir).

Mengetahui bahwa Crystal Lake berada di New Jersey, kita tentu tidak mengharapkan suhu siang mencapai 21 derajat Celsius atau lebih tinggi di Musim Dingin. Sebaliknya, jauh lebih mungkin menjadi hari yang hangat di Musim Semi atau Musim Gugur, atau hari di suatu tempat di Musim Panas. Oleh karena itu, mengetahui suhu siang di Crystal Lake pada hari yang dipilih adalah 21 derajat Celsius atau lebih tinggi, probabilitas hari yang dipilih oleh Bob berada di Musim Panas menjadi jauh lebih tinggi. Ini adalah **probabilitas kondisional** dari hari yang dipilih secara acak berada di Musim Panas, mengingat suhu siang di Crystal Lake adalah 21 derajat Celsius atau lebih tinggi.
Berbeda dengan contoh sebelumnya, probabilitas dua kejadian juga bisa sepenuhnya tidak terkait. Dalam kasus tersebut, kita mengatakan bahwa mereka adalah **independen**.
Misalkan, sebagai contoh, sebuah koin adil telah mendarat di sisi kepala. Dengan fakta ini, apa, lalu, probabilitas akan hujan besok? Probabilitas bersyarat dalam kasus ini seharusnya sama dengan probabilitas tanpa syarat bahwa akan hujan besok, karena lemparan koin pada umumnya tidak memiliki dampak apa pun terhadap cuaca.

Kita menggunakan simbol “|” untuk menuliskan pernyataan probabilitas bersyarat. Misalnya, probabilitas kejadian A mengingat kejadian B telah terjadi dapat ditulis sebagai berikut: Pr[A|B]. Jadi, ketika dua kejadian, A dan B, adalah independen, maka Pr[A|B] = Pr[A] dan Pr[B|A] = Pr[B]. Kondisi untuk independensi dapat disederhanakan sebagai berikut: Pr[A,B] = Pr[A]*Pr[B].

Hasil kunci dalam teori probabilitas dikenal sebagai **Teorema Bayes**. Pada dasarnya menyatakan bahwa Pr[A|B] dapat ditulis ulang sebagai berikut:

Pr[A|B] = (Pr[B|A] • Pr[A]) / Pr[B]

Alih-alih menggunakan probabilitas bersyarat dengan kejadian spesifik, kita juga dapat melihat probabilitas bersyarat yang terlibat dengan dua atau lebih variabel acak atas serangkaian kejadian yang mungkin. Misalkan dua variabel acak, X dan Y. Kita dapat menunjukkan nilai apa pun untuk X dengan x, dan nilai apa pun untuk Y dengan y. Kita mungkin mengatakan, lalu, bahwa dua variabel acak adalah independen jika pernyataan berikut berlaku:

Pr[X = x,Y = y] = Pr[X = x] • Pr[Y = y] untuk semua x dan y

Mari kita lebih eksplisit tentang apa arti pernyataan ini.

Misalkan bahwa himpunan hasil untuk X dan Y didefinisikan sebagai berikut: **X** = {x<sub>1</sub>,x<sub>2</sub>….,x<sub>i</sub>,….x<sub>n</sub>} dan **Y** = {y<sub>1</sub>,y<sub>2</sub>….,y<sub>i</sub>,….y<sub>m</sub>}. (Biasanya himpunan nilai-nilai ditunjukkan dengan huruf tebal, huruf besar.)

Sekarang misalkan Anda mengambil sampel Y dan mengamati y<sub>1</sub>. Pernyataan di atas memberi tahu kita bahwa probabilitas sekarang mendapatkan x<sub>1</sub> dari pengambilan sampel X persis sama seperti jika kita tidak pernah mengamati y<sub>1</sub>. Ini berlaku untuk setiap y<sub>i</sub> yang bisa kita dapatkan dari pengambilan sampel awal Y. Akhirnya, ini berlaku tidak hanya untuk x<sub>1</sub>. Untuk setiap x<sub>i</sub> probabilitas terjadinya tidak dipengaruhi oleh hasil dari pengambilan sampel Y. Semua ini juga berlaku untuk kasus di mana X diambil sampel terlebih dahulu.

Mari kita akhiri diskusi kita pada titik yang sedikit lebih filosofis. Dalam setiap situasi dunia nyata, probabilitas suatu kejadian selalu dinilai terhadap serangkaian informasi tertentu. Tidak ada "probabilitas tanpa syarat" dalam arti kata yang sangat ketat.

Misalnya, bayangkan saya bertanya kepada Anda tentang probabilitas babi akan terbang pada tahun 2030. Meskipun saya tidak memberi Anda informasi lebih lanjut, Anda jelas tahu banyak tentang dunia yang dapat mempengaruhi penilaian Anda. Anda belum pernah melihat babi terbang. Anda tahu bahwa kebanyakan orang tidak akan mengharapkannya terbang. Anda tahu bahwa mereka sebenarnya tidak dibangun untuk terbang. Dan seterusnya.
Oleh karena itu, ketika kita berbicara tentang "probabilitas tanpa syarat" dari suatu peristiwa dalam konteks dunia nyata, istilah tersebut hanya dapat memiliki makna jika kita menganggapnya berarti sesuatu seperti "probabilitas tanpa informasi tambahan yang eksplisit". Pemahaman tentang "probabilitas bersyarat" harus, oleh karena itu, selalu dipahami terhadap suatu informasi spesifik. 
Misalnya, saya mungkin bertanya kepada Anda probabilitas babi akan terbang pada tahun 2030, setelah memberi Anda bukti bahwa beberapa kambing di Selandia Baru telah belajar terbang setelah beberapa tahun pelatihan. Dalam kasus ini, Anda mungkin akan menyesuaikan penilaian Anda tentang probabilitas babi akan terbang pada tahun 2030. Jadi, probabilitas babi akan terbang pada tahun 2030 bersyarat pada bukti ini tentang kambing di Selandia Baru.

## Operasi modulo
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

Ekspresi paling dasar dengan **operasi modulo** adalah dalam bentuk berikut: x mod y.

Variabel x disebut sebagai pembagi dan variabel y sebagai pembilang. Untuk melakukan operasi modulo dengan pembagi positif dan pembilang positif, Anda hanya menentukan sisa dari pembagian tersebut.

Misalnya, pertimbangkan ekspresi 25 mod 4. Angka 4 masuk ke dalam angka 25 sebanyak 6 kali. Sisa dari pembagian tersebut adalah 1. Oleh karena itu, 25 mod 4 sama dengan 1. Dengan cara yang serupa, kita dapat mengevaluasi ekspresi di bawah ini:

* 29 mod 30 = 29 (karena 30 masuk ke dalam 29 sebanyak 0 kali dan sisanya adalah 29)
* 42 mod 2 = 0 (karena 2 masuk ke dalam 42 sebanyak 21 kali dan sisanya adalah 0)
* 12 mod 5 = 2 (karena 5 masuk ke dalam 12 sebanyak 2 kali dan sisanya adalah 2)
* 20 mod 8 = 4 (karena 8 masuk ke dalam 20 sebanyak 2 kali dan sisanya adalah 4)

Ketika pembagi atau pembilang negatif, operasi modulo dapat ditangani secara berbeda oleh bahasa pemrograman.

Anda pasti akan menemukan kasus dengan pembagi negatif dalam kriptografi. Dalam kasus tersebut, pendekatan yang biasa adalah sebagai berikut:

* Pertama tentukan nilai terdekat *lebih rendah dari atau sama dengan* pembagi di mana pembilang membagi dengan sisa nol. Sebut nilai tersebut p.
* Jika pembagi adalah x, maka hasil dari operasi modulo adalah nilai dari x – p.

Misalnya, anggap bahwa pembagi adalah – 20 dan pembilang 3. Nilai terdekat lebih rendah dari atau sama dengan – 20 di mana 3 membagi secara merata adalah – 21. Nilai dari x – p dalam kasus ini adalah – 20 – – 21. Ini sama dengan 1 dan, oleh karena itu, – 20 mod 3 sama dengan 1. Dengan cara yang serupa, kita dapat mengevaluasi ekspresi di bawah ini:

* – 8 mod 5 = 2
* – 19 mod 16 = 13
* – 14 mod 6 = 4

Mengenai notasi, Anda biasanya akan melihat jenis ekspresi berikut: x = [y mod z]. Karena kurung, operasi modulo dalam kasus ini hanya berlaku untuk sisi kanan dari ekspresi. Jika y sama dengan 25 dan z sama dengan 4, misalnya, maka x dievaluasi menjadi 1.
Tanpa tanda kurung, operasi modulo berlaku pada *kedua sisi* dari sebuah ekspresi. Misalkan, contoh berikut ini: x = y mod z. Jika y sama dengan 25 dan z sama dengan 4, maka yang kita ketahui adalah x mod 4 bernilai 1. Ini konsisten dengan nilai x dari himpunan {….– 7, – 3, 1, 5, 9….}.

Cabang matematika yang melibatkan operasi modulo pada angka dan ekspresi disebut **aritmetika modular**. Anda dapat memikirkan cabang ini sebagai aritmetika untuk kasus-kasus di mana garis bilangan tidak terbatas panjangnya. Meskipun kita biasanya menemui operasi modulo untuk bilangan bulat (positif) dalam kriptografi, Anda juga dapat melakukan operasi modulo menggunakan bilangan real apa pun.

### Sandi geser

Operasi modulo sering dijumpai dalam kriptografi. Untuk mengilustrasikan, mari kita pertimbangkan salah satu skema enkripsi historis yang paling terkenal: sandi geser.

Mari kita definisikan terlebih dahulu. Misalkan sebuah kamus *D* yang menyamakan semua huruf alfabet Inggris, secara berurutan, dengan himpunan angka {0,1,2…,25}. Asumsikan sebuah ruang pesan **M**. **Sandi geser**, maka, adalah skema enkripsi yang didefinisikan sebagai berikut:

- Pilih secara seragam sebuah kunci k dari ruang kunci **K**, di mana **K** = {0,1,2,…,25}<sup>[1](#footnote1)</sup>
- Enkripsi sebuah pesan m є **M**, sebagai berikut:
    - Pisahkan m menjadi huruf-huruf individunya m<sub>0</sub>, m<sub>1</sub>,….m<sub>i</sub>….,m<sub>l</sub>
    - Konversi setiap m<sub>i</sub> menjadi angka menurut *D*
    - Untuk setiap m<sub>i</sub>, c<sub>i</sub> = [(m<sub>i</sub> + k) mod 26]
    - Konversi setiap c<sub>i</sub> kembali menjadi huruf menurut *D*
    - Kemudian gabungkan c<sub>0</sub>, c<sub>1</sub>,….,c<sub>l</sub> untuk menghasilkan teks tersandi c
- Dekripsi sebuah teks tersandi c sebagai berikut:
    -- Konversi setiap c<sub>i</sub> menjadi angka menurut *D*
    -- Untuk setiap c<sub>i</sub>, m<sub>i</sub> = [(c<sub>i</sub> – k) mod 26]
    -- Konversi setiap m<sub>i</sub> kembali menjadi huruf menurut *D*
    -- Kemudian gabungkan m<sub>0</sub>, m<sub>1</sub>,….,m<sub>l</sub> untuk menghasilkan pesan asli m

Operator modulo dalam sandi geser memastikan bahwa huruf-huruf berputar, sehingga semua huruf teks tersandi didefinisikan. Untuk mengilustrasikan, pertimbangkan penerapan sandi geser pada kata “DOG”.

Misalkan Anda secara seragam memilih sebuah kunci dengan nilai 17. Huruf “O” sama dengan 15. Tanpa operasi modulo, penambahan angka teks asli ini dengan kunci akan menghasilkan angka teks tersandi sebesar 32. Namun, angka teks tersandi tersebut tidak dapat diubah menjadi huruf teks tersandi, karena alfabet Inggris hanya memiliki 26 huruf. Operasi modulo memastikan bahwa angka teks tersandi sebenarnya adalah 6 (hasil dari 32 mod 26), yang sama dengan huruf teks tersandi “G”.

Enkripsi seluruh kata “DOG” dengan nilai kunci 17 adalah sebagai berikut:
* Pesan = DOG = D,O,G = 3,15,6* c<sub>0</sub> = [(3 + 17) Mod 26] = [(20) Mod 26] = 20 = U
* c<sub>1</sub> = [(15 + 17) Mod 26] = [(32) Mod 26] = 6 = G
* c<sub>2</sub> = [(6 + 17) Mod 26] = [(23) Mod 26] = 23 = X
* c = UGX

Semua orang dapat secara intuitif memahami bagaimana sandi pergeseran bekerja dan mungkin menggunakan sendiri. Namun, untuk meningkatkan pengetahuan Anda tentang kriptografi, penting untuk mulai merasa lebih nyaman dengan formalisasi, karena skema akan menjadi jauh lebih sulit. Oleh karena itu, mengapa langkah-langkah untuk sandi pergeseran diformalisasi.

## Operasi XOR
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Semua data komputer diproses, disimpan, dan dikirim melintasi jaringan pada tingkat bit. Skema kriptografi apa pun yang diterapkan pada data komputer juga beroperasi pada tingkat bit.

Misalnya, anggaplah Anda telah mengetik e-mail ke dalam aplikasi e-mail Anda. Enkripsi apa pun yang Anda terapkan tidak terjadi pada karakter ASCII dari e-mail Anda secara langsung. Sebaliknya, itu diterapkan pada representasi bit dari huruf dan simbol lain dalam e-mail Anda.

Operasi matematika kunci untuk dipahami untuk kriptografi modern, selain operasi modulo, adalah operasi **XOR**, atau operasi "exclusive or". Operasi ini mengambil dua bit sebagai input dan menghasilkan bit lain sebagai output. Operasi XOR akan hanya ditandai sebagai "XOR". Ini menghasilkan 0 jika kedua bit sama dan 1 jika kedua bit berbeda. Anda dapat melihat keempat kemungkinan di bawah ini.

* 0 XOR 0 = 0
* 0 XOR 1 = 1
* 1 XOR 0 = 1
* 1 XOR 1 = 0

Anda dapat melakukan operasi XOR pada dua pesan yang lebih panjang dari satu bit dengan menyelaraskan bit dari kedua pesan tersebut dan melakukan operasi XOR pada setiap pasangan bit secara individu.

Untuk mengilustrasikan, anggaplah Anda memiliki pesan m<sub>1</sub> (01111001) dan pesan m<sub>2</sub> (01011001). Operasi XOR dari kedua pesan ini dapat dilihat di bawah ini.

* m<sub>1</sub> XOR m<sub>2</sub> = 01111001 XOR 01011001 = 00100000

Prosesnya sederhana. Anda pertama kali melakukan XOR pada bit paling kiri dari m<sub>1</sub> dan m<sub>2</sub>. Dalam kasus ini adalah 0 XOR 0 = 0. Kemudian Anda melakukan XOR pada pasangan bit kedua dari kiri. Dalam kasus ini adalah 1 XOR 1 = 0. Anda melanjutkan proses ini sampai Anda telah melakukan operasi XOR pada bit paling kanan.
Mudah untuk dilihat bahwa operasi XOR bersifat komutatif, yaitu m<sub>1</sub> XOR m<sub>2</sub> = m<sub>2</sub> XOR m<sub>1</sub>. Selain itu, operasi XOR juga bersifat asosiatif. Artinya, (m<sub>1</sub> XOR m<sub>2</sub>) XOR m<sub>3</sub> = m<sub>1</sub> XOR (m<sub>2</sub> XOR m<sub>3</sub>).
Operasi XOR pada dua string dengan panjang yang berbeda dapat memiliki interpretasi yang berbeda, tergantung pada konteksnya. Kami tidak akan membahas operasi XOR pada string dengan panjang yang berbeda di sini.

Operasi XOR setara dengan kasus khusus melakukan operasi modulo pada penjumlahan bit ketika pembaginya adalah 2. Anda dapat melihat kesetaraan dalam hasil berikut:

* (0 + 0) mod 2 = 0 XOR 0 = 0
* (1 + 0) mod 2 = 1 XOR 0 = 1
* (0 + 1) mod 2 = 0 XOR 1 = 1
* (1 + 1) mod 2 = 1 XOR 1 = 0

## Pseudorandomness
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

Dalam pembahasan kami tentang variabel acak dan seragam, kami membuat perbedaan spesifik antara "acak" dan "seragam". Perbedaan ini biasanya dipertahankan dalam praktek ketika mendeskripsikan variabel acak. Namun, dalam konteks kami saat ini, perbedaan ini perlu diabaikan dan "acak" serta "seragam" digunakan secara sinonim. Saya akan menjelaskan alasannya di akhir bagian ini.

Untuk memulai, kita dapat menyebut sebuah string biner dengan panjang n **acak** (atau **seragam**), jika itu adalah hasil dari pengambilan sampel variabel seragam S yang memberikan setiap string biner dengan panjang n probabilitas seleksi yang sama.

Misalkan, contohnya, himpunan semua string biner dengan panjang 8: {0000 0000,0000 0001,….,1111 1111}. (Biasanya, sebuah string 8-bit ditulis dalam dua kuartet, masing-masing disebut **nibble**.) Mari kita sebut himpunan string ini **S<sub>8</sub>**.

Berdasarkan definisi di atas, kita dapat, kemudian, menyebut sebuah string biner tertentu dengan panjang 8 acak (atau seragam), jika itu adalah hasil dari pengambilan sampel variabel seragam S yang memberikan setiap string dalam **S<sub>8</sub>** probabilitas seleksi yang sama. Mengingat bahwa himpunan **S<sub>8</sub>** mencakup 2<sup>8</sup> elemen, probabilitas seleksi saat pengambilan sampel haruslah 1/2<sup>8</sup> untuk setiap string dalam himpunan.

Aspek kunci dari keacakan sebuah string biner adalah bahwa itu didefinisikan dengan referensi pada proses dimana itu dipilih. Oleh karena itu, bentuk dari string biner tertentu sendiri, tidak mengungkapkan apa pun tentang keacakannya dalam seleksi.

Sebagai contoh, banyak orang secara intuitif memiliki ide bahwa string seperti 1111 1111 tidak mungkin dipilih secara acak. Namun ini jelas salah.
Mendefinisikan variabel seragam S untuk semua string biner dengan panjang 8, kemungkinan memilih 1111 1111 dari himpunan **S<sub>8</sub>** sama dengan string lain seperti 0111 01001. Dengan demikian, Anda tidak dapat mengatakan apa-apa tentang keacakan sebuah string, hanya dengan menganalisis string itu sendiri.
Kita juga dapat berbicara tentang string acak tanpa secara spesifik berarti string biner. Misalnya, kita dapat berbicara tentang string heksadesimal acak AF 02 82. Dalam kasus ini, string tersebut dipilih secara acak dari himpunan semua string heksadesimal dengan panjang 6. Ini setara dengan memilih secara acak string biner dengan panjang 24, karena setiap digit heksadesimal mewakili 4 bit.

Biasanya ekspresi “sebuah string acak”, tanpa kualifikasi, merujuk pada string yang dipilih secara acak dari himpunan semua string dengan panjang yang sama. Inilah cara saya mendeskripsikannya di atas. Sebuah string dengan panjang n, tentu saja, juga dapat dipilih secara acak dari himpunan yang berbeda. Satu, misalnya, yang hanya merupakan subset dari semua string dengan panjang n, atau mungkin himpunan yang mencakup string dengan panjang yang bervariasi. Dalam kasus tersebut, bagaimanapun, kita tidak akan menyebutnya sebagai “string acak”, melainkan “sebuah string yang dipilih secara acak dari beberapa himpunan **S**”.

Konsep kunci dalam kriptografi adalah pseudorandomness. Sebuah **string pseudorandom** dengan panjang n tampak *seolah-olah* itu adalah hasil dari pengambilan sampel variabel seragam S yang memberikan setiap string di **S<sub>n</sub>** probabilitas yang sama untuk dipilih. Namun, sebenarnya, string tersebut adalah hasil dari pengambilan sampel variabel seragam S' yang hanya mendefinisikan distribusi probabilitas—tidak necessarily dengan probabilitas yang sama untuk semua hasil yang mungkin—pada subset dari **S<sub>n</sub>**. Poin penting di sini adalah tidak ada yang benar-benar dapat membedakan antara sampel dari S dan S', bahkan jika Anda mengambil banyak di antaranya.

Misalkan, sebagai contoh, variabel acak S. Himpunan hasilnya adalah **S<sub>256</sub>**, ini adalah himpunan semua string biner dengan panjang 256. Himpunan ini memiliki 2<sup>256</sup> elemen. Setiap elemen memiliki probabilitas yang sama untuk dipilih, 1/2<sup>256</sup>, saat pengambilan sampel.

Selain itu misalkan variabel acak S’. Himpunan hasilnya hanya mencakup 2<sup>128</sup> string biner dengan panjang 256. Ini memiliki beberapa distribusi probabilitas atas string tersebut, tetapi distribusi ini tidak necessarily seragam.

Misalkan sekarang saya mengambil 1000an sampel dari S dan 1000an sampel dari S' dan memberikan kedua himpunan hasil kepada Anda. Saya memberitahu Anda himpunan hasil mana yang terkait dengan variabel acak mana. Selanjutnya, saya mengambil sampel dari salah satu dari dua variabel acak tersebut. Tapi kali ini saya tidak memberitahu Anda variabel acak mana yang saya sampel. Jika S' adalah pseudorandom, maka ideanya adalah probabilitas Anda membuat tebakan yang benar tentang variabel acak mana yang saya sampel praktis tidak lebih baik dari 1/2.

Biasanya, sebuah string pseudorandom dengan panjang n dihasilkan dengan memilih secara acak sebuah string berukuran n – x, di mana x adalah bilangan bulat positif, dan menggunakannya sebagai input untuk algoritma ekspansioner. String acak berukuran n – x ini dikenal sebagai **seed**.
String pseudorandom adalah konsep kunci untuk membuat kriptografi menjadi praktis. Pertimbangkan, misalnya, stream cipher. Dengan stream cipher, kunci yang dipilih secara acak dimasukkan ke dalam algoritma ekspansioner untuk menghasilkan string pseudorandom yang jauh lebih besar. String pseudorandom ini kemudian digabungkan dengan plaintext melalui operasi XOR untuk menghasilkan ciphertext.
Jika kita tidak dapat menghasilkan jenis string pseudorandom ini untuk stream cipher, maka kita akan memerlukan kunci yang sepanjang pesan untuk keamanannya. Ini bukan opsi yang sangat praktis dalam kebanyakan kasus.

Konsep pseudorandomness yang dibahas di bagian ini dapat didefinisikan secara lebih formal. Ini juga berlaku untuk konteks lain. Namun, kita tidak perlu membahasnya di sini. Yang benar-benar perlu Anda pahami secara intuitif untuk sebagian besar kriptografi adalah perbedaan antara string random dan pseudorandom.

Alasan menghilangkan perbedaan antara "random" dan "uniform" dalam diskusi kita sekarang juga harus jelas. Dalam praktiknya, semua orang menggunakan istilah pseudorandom untuk menunjukkan string yang tampak **seolah-olah** itu adalah hasil dari pengambilan sampel variabel uniform S. Secara ketat, kita seharusnya menyebut string seperti itu "pseudo-uniform," mengadopsi bahasa kita dari sebelumnya. Karena istilah "pseudo-uniform" baik canggung dan tidak digunakan oleh siapa pun, kita tidak akan memperkenalkannya di sini untuk kejelasan. Sebagai gantinya, kita hanya menghilangkan perbedaan antara "random" dan "uniform" dalam konteks saat ini.

## Catatan

[^1]: Kita dapat mendefinisikan pernyataan ini secara tepat, menggunakan terminologi dari bagian sebelumnya. Misalkan variabel uniform K memiliki **K** sebagai himpunan hasil yang mungkin. Jadi Pr [K = 0] = 1/26, Pr [K = 1] = 1/26, dan seterusnya. Sampel variabel uniform K sekali untuk menghasilkan kunci tertentu [^1].

[^2]: Jika tertarik pada eksposisi yang lebih formal tentang hal-hal ini, Anda dapat berkonsultasi dengan *Introduction to Modern Cryptography* oleh Katz dan Lindell, khususnya bab 3 [^2].

# Dasar-dasar Matematika Kriptografi II

Bab ini membahas topik lanjutan tentang dasar-dasar matematika kriptografi: teori bilangan. Meskipun teori bilangan penting untuk kriptografi simetris (seperti dalam Rijndael Cipher), ini sangat penting dalam pengaturan kriptografi kunci publik.

Jika Anda merasa detail dari teori bilangan memberatkan, saya akan merekomendasikan membaca tingkat tinggi pertama kali. Anda selalu dapat kembali ke itu di kemudian hari.

## Apa itu teori bilangan?

Anda mungkin mengkarakterisasi **teori bilangan** sebagai studi tentang sifat-sifat bilangan bulat dan fungsi matematika yang bekerja dengan bilangan bulat.

Pertimbangkan, misalnya, bahwa dua bilangan a dan N adalah **koprima** (atau **prima relatif**) jika pembagi terbesar bersama mereka sama dengan 1. Misalkan sekarang sebuah bilangan bulat N. Berapa banyak bilangan bulat yang lebih kecil dari N adalah koprima dengan N? Bisakah kita membuat pernyataan umum tentang jawaban untuk pertanyaan ini? Ini adalah jenis pertanyaan tipikal yang ingin dijawab oleh teori bilangan.
Teori angka modern bergantung pada alat-alat dari aljabar abstrak. Bidang **aljabar abstrak** adalah subdisiplin matematika di mana objek utama analisis adalah objek abstrak yang dikenal sebagai struktur aljabar. Sebuah **struktur aljabar** adalah sekumpulan elemen yang digabungkan dengan satu atau lebih operasi, yang memenuhi beberapa aksioma. Melalui struktur aljabar, matematikawan dapat memperoleh wawasan tentang masalah matematika tertentu, dengan mengabstraksi dari detailnya.
Bidang aljabar abstrak terkadang juga disebut aljabar modern. Anda mungkin juga menemukan konsep **matematika abstrak** (atau **matematika murni**). Istilah terakhir ini bukan merujuk pada aljabar abstrak, tetapi lebih berarti studi matematika demi matematika itu sendiri, dan tidak hanya dengan pandangan pada aplikasi potensial.

Himpunan dari aljabar abstrak dapat menangani banyak jenis objek, dari transformasi yang mempertahankan bentuk pada segitiga sama sisi hingga pola kertas dinding. Untuk teori angka, kita hanya mempertimbangkan himpunan elemen yang mengandung bilangan bulat atau fungsi yang bekerja dengan bilangan bulat.

## Grup
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Konsep dasar dalam matematika adalah himpunan elemen. Himpunan biasanya ditandai dengan tanda kurung kurawal dengan elemen dipisahkan oleh koma.

Misalnya, himpunan semua bilangan bulat adalah {…,-2,-1,0,1,2,…}. Elips di sini berarti bahwa suatu pola tertentu berlanjut ke arah tertentu. Jadi, himpunan semua bilangan bulat juga mencakup 3,4,5,6 dan seterusnya, serta -3,-4,-5,-6 dan seterusnya. Himpunan semua bilangan bulat ini biasanya ditandai dengan ℤ.

Contoh lain dari sebuah himpunan adalah ℤ mod 11, atau himpunan semua bilangan bulat modulo 11. Berbeda dengan seluruh himpunan ℤ, himpunan ini hanya mengandung sejumlah elemen terbatas, yaitu {0,1,…,9,10}.

Kesalahan umum adalah berpikir bahwa himpunan ℤ mod 11 sebenarnya adalah {-10,-9,….,0,….,9,10}. Tetapi ini bukan kasusnya, mengingat cara kita mendefinisikan operasi modulo sebelumnya. Setiap bilangan bulat negatif yang direduksi oleh modulo 11 dibungkus ke {0,1,….,9,10}. Misalnya, ekspresi -2 mod 11 dibungkus menjadi 9, sementara ekspresi -27 mod 11 dibungkus menjadi 5.

Konsep dasar lain dalam matematika adalah operasi biner. Ini adalah operasi apa pun yang mengambil dua elemen untuk menghasilkan yang ketiga. Misalnya, dari aritmatika dasar dan aljabar, Anda akan familiar dengan empat operasi biner fundamental: penjumlahan, pengurangan, perkalian, dan pembagian.

Dua konsep matematika dasar ini, himpunan dan operasi biner, digunakan untuk mendefinisikan gagasan tentang grup, struktur paling esensial dalam aljabar abstrak.

Secara spesifik, anggaplah beberapa operasi biner ◌. Selain itu, anggaplah beberapa himpunan elemen **S** yang dilengkapi dengan operasi tersebut. Semua "dilengkapi" di sini berarti adalah operasi ◌ dapat dilakukan antara dua elemen apa pun dalam himpunan **S**.

Kombinasi 〈**S**, ◌〉, kemudian, adalah **grup** jika memenuhi empat kondisi spesifik, yang dikenal sebagai aksioma grup.

1. Untuk setiap a dan b yang merupakan elemen dari **S**, a ◌ b juga merupakan elemen dari **S**. Ini dikenal sebagai **kondisi penutupan**.
2. Untuk setiap a, b, dan c yang merupakan elemen dari **S**, berlaku bahwa (a ◌ b) ◌ c = a ◌ (b ◌ c). Ini dikenal sebagai **kondisi asosiativitas**. 3. Ada satu elemen unik e di **S**, sehingga untuk setiap elemen a di **S**, persamaan berikut berlaku: e ◌ a = a ◌ e = a. Karena hanya ada satu elemen e seperti itu, ini disebut **elemen identitas**. Kondisi ini dikenal sebagai **kondisi identitas**.
4. Untuk setiap elemen a di **S**, ada elemen b di **S**, sehingga persamaan berikut berlaku: a ◌ b = b ◌ a = e, di mana e adalah elemen identitas. Elemen b di sini dikenal sebagai **elemen invers**, dan umumnya ditandai sebagai a<sup>-1</sup>. Kondisi ini dikenal sebagai **kondisi invers** atau **kondisi kebalik**.

Mari kita jelajahi grup lebih lanjut. Nyatakan himpunan semua bilangan bulat dengan ℤ. Himpunan ini dikombinasikan dengan penambahan standar, atau 〈ℤ, +〉, jelas memenuhi definisi grup, karena memenuhi empat aksioma di atas.

1. Untuk setiap x dan y yang merupakan elemen dari ℤ, x + y juga merupakan elemen dari ℤ. Jadi 〈ℤ, +〉 memenuhi kondisi penutupan.
2. Untuk setiap x, y, dan z yang merupakan elemen dari ℤ, (x + y) + z = x + (y + z). Jadi 〈ℤ, +〉 memenuhi kondisi asosiativitas.
3. Ada elemen identitas di 〈ℤ, +〉, yaitu 0. Untuk setiap x di ℤ, berlaku bahwa: 0 + x = x + 0 = x. Jadi 〈ℤ, +〉 memenuhi kondisi identitas.
4. Akhirnya, untuk setiap elemen x di ℤ, ada y sehingga x + y = y + x = 0. Jika x adalah 10, misalnya, y akan menjadi –10 (dalam kasus x adalah 0, y juga 0). Jadi 〈ℤ, +〉 memenuhi kondisi invers.

Penting untuk dicatat, bahwa himpunan bilangan bulat dengan penambahan merupakan grup tidak berarti itu merupakan grup dengan perkalian. Anda dapat memverifikasi ini dengan menguji 〈ℤ, •〉 terhadap empat aksioma grup (di mana • berarti perkalian standar).

Dua aksioma pertama jelas berlaku. Selain itu, di bawah perkalian elemen 1 dapat berfungsi sebagai elemen identitas. Setiap bilangan bulat x dikalikan dengan 1, menghasilkan x. Namun, 〈ℤ, •〉 tidak memenuhi kondisi invers. Artinya, tidak ada elemen unik y di ℤ untuk setiap x di ℤ, sehingga x • y = 1.

Misalnya, anggap bahwa x = 22. Nilai y apa dari himpunan ℤ yang dikalikan dengan x akan menghasilkan elemen identitas 1? Nilai 1/22 akan berfungsi, tetapi ini tidak termasuk dalam himpunan ℤ. Faktanya, Anda akan menghadapi masalah ini untuk setiap bilangan bulat x, selain nilai 1 dan -1 (di mana y harus 1 dan -1 masing-masing).
Jika kita mengizinkan angka riil untuk himpunan kita, maka masalah kita sebagian besar hilang. Untuk setiap elemen x dalam himpunan, perkalian dengan 1/x menghasilkan 1. Karena pecahan termasuk dalam himpunan angka riil, sebuah invers dapat ditemukan untuk setiap angka riil. Pengecualian adalah nol, karena setiap perkalian dengan nol tidak akan pernah menghasilkan elemen identitas 1. Oleh karena itu, himpunan angka riil non-nol yang dilengkapi dengan perkalian memang merupakan sebuah grup.

Beberapa grup memenuhi kondisi umum kelima, yang dikenal sebagai **kondisi komutativitas**. Kondisi ini adalah sebagai berikut:

* Misalkan sebuah grup G dengan himpunan **S** dan operator biner ◌. Misalkan a dan b adalah elemen dari **S**. Jika berlaku bahwa a ◌ b = b ◌ a untuk setiap dua elemen a dan b dalam **S**, maka G memenuhi kondisi komutativitas.

Setiap grup yang memenuhi kondisi komutativitas dikenal sebagai **grup komutatif**, atau **grup Abelian** (setelah Niels Henrik Abel). Mudah untuk memverifikasi bahwa baik himpunan angka riil atas penambahan maupun himpunan bilangan bulat atas penambahan adalah grup Abelian. Himpunan bilangan bulat atas perkalian sama sekali bukan grup, sehingga tidak bisa menjadi grup Abelian. Sebaliknya, himpunan angka riil non-nol atas perkalian juga merupakan grup Abelian.

Anda harus memperhatikan dua konvensi penting tentang notasi. Pertama, tanda “+” atau “x” sering digunakan untuk mensimbolkan operasi grup, meskipun elemennya sebenarnya bukan angka. Dalam kasus ini, Anda tidak harus menginterpretasikan tanda-tanda ini sebagai penambahan atau perkalian aritmatika standar. Sebaliknya, mereka adalah operasi dengan kesamaan abstrak saja dengan operasi aritmatika tersebut.

Kecuali Anda secara spesifik merujuk pada penambahan atau perkalian aritmatika, lebih mudah menggunakan simbol seperti ◌ dan ◊ untuk operasi grup, karena simbol-simbol ini tidak memiliki konotasi budaya yang sangat tertanam.

Kedua, dengan alasan yang sama bahwa “+” dan “x” sering digunakan untuk menunjukkan operasi non-aritmatika, elemen identitas dari grup sering disimbolkan dengan “0” dan “1”, meskipun elemen dalam grup tersebut bukan angka. Kecuali Anda merujuk pada elemen identitas dari grup dengan angka, lebih mudah menggunakan simbol yang lebih netral seperti “e” untuk menunjukkan elemen identitas.

Banyak himpunan nilai yang sangat berbeda dan sangat penting dalam matematika yang dilengkapi dengan operasi biner tertentu adalah grup. Namun, aplikasi kriptografi hanya bekerja dengan himpunan bilangan bulat atau setidaknya elemen yang dijelaskan oleh bilangan bulat, yaitu, dalam domain teori bilangan. Oleh karena itu, himpunan dengan angka riil selain bilangan bulat tidak digunakan dalam aplikasi kriptografi.

Mari kita selesaikan dengan memberikan contoh elemen yang dapat “dijelaskan oleh bilangan bulat”, meskipun mereka bukan bilangan bulat. Contoh yang baik adalah titik-titik pada kurva eliptik. Meskipun setiap titik pada kurva eliptik jelas bukan bilangan bulat, titik tersebut memang dijelaskan oleh dua bilangan bulat.

Kurva eliptik, misalnya, sangat penting untuk Bitcoin. Setiap pasangan kunci privat dan publik Bitcoin standar dipilih dari himpunan titik yang didefinisikan oleh kurva eliptik berikut: x<sup>3</sup> + 7 = y<sup>2</sup> mod 2<sup>256</sup> – 232 – 29 – 28 – 27 – 26 - 24 - 1 (bilangan prima terbesar kurang dari 2<sup>256</sup>). Koordinat x adalah kunci privat dan koordinat y adalah kunci publik Anda.
Transaksi dalam Bitcoin biasanya melibatkan penguncian output ke satu atau lebih kunci publik dalam beberapa cara. Nilai dari transaksi ini kemudian dapat dibuka dengan membuat tanda tangan digital menggunakan kunci privat yang sesuai.

## Grup Siklik
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Sebuah perbedaan utama yang dapat kita tarik adalah antara **grup terbatas** dan **grup tak terbatas**. Yang pertama memiliki jumlah elemen yang terbatas, sementara yang terakhir memiliki jumlah elemen yang tak terbatas. Jumlah elemen dalam setiap grup terbatas dikenal sebagai **orde grup**. Semua kriptografi praktis yang melibatkan penggunaan grup bergantung pada grup terbatas (berbasis teori angka).

Dalam kriptografi kunci publik, sebuah kelas tertentu dari grup Abelian terbatas yang dikenal sebagai grup siklik sangat penting. Untuk memahami grup siklik, kita pertama-tama perlu memahami konsep eksponensiasi elemen grup.

Anggaplah sebuah grup G dengan operasi grup ◌, dan bahwa a adalah elemen dari G. Ekspresi a<sup>n</sup> harus, kemudian, diinterpretasikan sebagai elemen a dikombinasikan dengan dirinya sendiri sebanyak n – 1 kali. Misalnya, a<sup>2</sup> berarti a ◌ a, a<sup>3</sup> berarti a ◌ a ◌ a, dan seterusnya. (Catat bahwa eksponensiasi di sini tidak harus eksponensiasi dalam arti aritmetika standar.)

Mari beralih ke sebuah contoh. Anggaplah bahwa G = 〈ℤ mod 7,+〉, dan nilai a kita sama dengan 4. Dalam kasus ini, a<sup>2</sup> = [4 + 4 mod 7] = [8 mod 7] = 1 mod 7. Sebagai alternatif, a<sup>4</sup> akan mewakili [4 + 4 + 4 + 4 mod 7] = [16 mod 7] = 2 mod 7.

Beberapa grup Abelian memiliki satu atau lebih elemen, yang dapat menghasilkan semua elemen grup lainnya melalui eksponensiasi berkelanjutan. Elemen-elemen ini disebut **generator** atau **elemen primitif**.

Sebuah kelas penting dari grup seperti ini adalah 〈ℤ* mod N, •〉, di mana N adalah bilangan prima. Notasi ℤ* di sini berarti bahwa grup tersebut berisi semua bilangan bulat positif, bukan nol, yang kurang dari N. Sehingga, grup tersebut selalu memiliki N – 1 elemen.

Pertimbangkan, misalnya, G = 〈ℤ* mod 11, •〉. Grup ini memiliki elemen-elemen berikut: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}. Orde dari grup ini adalah 10 (yang memang sama dengan 11 – 1).

Mari kita jelajahi eksponensiasi elemen 2 dari grup ini. Perhitungan hingga 2<sup>12</sup> ditunjukkan di bawah ini. Perhatikan bahwa di sisi kiri persamaan, eksponen mengacu pada eksponensiasi elemen grup. Dalam contoh khusus kita, ini memang melibatkan eksponensiasi aritmetika di sisi kanan persamaan (tetapi ini juga bisa melibatkan, misalnya, penambahan). Untuk memperjelas, saya telah menuliskan operasi berulang, bukan dalam bentuk eksponen di sisi kanan.

* 2<sup>1</sup> = 2 mod 11
* 2<sup>2</sup> = 2 · 2 mod 11 = 4 mod 11
* 2<sup>3</sup> = 2 · 2 · 2 mod 11 = 8 mod 11
* 2<sup>4</sup> = 2 · 2 · 2 · 2 mod 11 = 16 mod 11 = 5 mod 11
* 2<sup>5</sup> = 2 · 2 · 2 · 2 · 2 mod 11 = 32 mod 11 = 10 mod 11
* 2<sup>6</sup> = 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 64 mod 11 = 9 mod 11
* 2<sup>7</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 128 mod 11 = 7 mod 11
* 2<sup>8</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 256 mod 11 = 3 mod 11
* 2<sup>9</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 512 mod 11 = 6 mod 11
* 2<sup>10</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 1024 mod 11 = 1 mod 11
* 2<sup>11</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 2048 mod 11 = 2 mod 11
* 2<sup>12</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 4096 mod 11 = 4 mod 11

Jika Anda memperhatikan dengan seksama, Anda dapat melihat bahwa melakukan eksponensiasi pada elemen 2 menghasilkan siklus melalui semua elemen dari 〈ℤ* mod 11, •〉 dalam urutan berikut: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Setelah 2<sup>10</sup>, eksponensiasi berkelanjutan dari elemen 2 mengulangi siklus melalui semua elemen lagi dan dalam urutan yang sama. Oleh karena itu, elemen 2 adalah generator dalam 〈ℤ* mod 11, •〉.

Meskipun 〈ℤ* mod 11, •〉 memiliki beberapa generator, tidak semua elemen dari grup ini adalah generator. Pertimbangkan, misalnya, elemen 3. Melalui 10 eksponensiasi pertama, tanpa menunjukkan perhitungan yang rumit, menghasilkan hasil berikut:

* 3<sup>1</sup> = 3 mod 11
* 3<sup>2</sup> = 9 mod 11
* 3<sup>3</sup> = 5 mod 11
* 3<sup>4</sup> = 4 mod 11
* 3<sup>5</sup> = 1 mod 11
* 3<sup>6</sup> = 3 mod 11
* 3<sup>7</sup> = 9 mod 11
* 3<sup>8</sup> = 5 mod 11
* 3<sup>9</sup> = 4 mod 11
* 3<sup>10</sup> = 1 mod 11

Alih-alih mengulang semua nilai dalam 〈ℤ* mod 11, •〉, eksponensiasi elemen 3 hanya menghasilkan sebagian nilai tersebut: 3, 9, 5, 4, dan 1. Setelah eksponensiasi kelima, nilai-nilai ini mulai berulang.

Kita sekarang dapat mendefinisikan **grup siklik** sebagai grup apa pun dengan setidaknya satu generator. Artinya, ada setidaknya satu elemen grup dari mana Anda dapat menghasilkan semua elemen grup lainnya melalui eksponensiasi.

Anda mungkin telah memperhatikan dalam contoh di atas bahwa baik 2<sup>10</sup> maupun 3<sup>10</sup> sama dengan 1 mod 11. Faktanya, meskipun kita tidak akan melakukan perhitungan, eksponensiasi oleh 10 dari elemen apa pun dalam grup 〈ℤ* mod 11, •〉 akan menghasilkan 1 mod 11. Mengapa ini bisa terjadi?

Ini adalah pertanyaan penting, tetapi membutuhkan beberapa pekerjaan untuk menjawabnya.

Untuk memulai, anggap dua bilangan bulat positif a dan N. Sebuah teorema penting dalam teori bilangan menyatakan bahwa a memiliki invers perkalian modulo N (yaitu, bilangan bulat b sehingga a • b = 1 mod N) jika dan hanya jika faktor persekutuan terbesar antara a dan N sama dengan 1. Artinya, jika a dan N adalah koprima.

Jadi, untuk setiap grup bilangan bulat yang dilengkapi dengan perkalian modulo N hanya koprima yang lebih kecil dengan N yang termasuk dalam set. Kita dapat menandai set ini dengan ℤ<sup>c</sup> mod N.

Misalnya, anggap N adalah 10. Hanya bilangan bulat 1,3,7, dan 9 yang merupakan koprima dengan 10. Jadi set ℤ<sup>c</sup> mod 10 hanya mencakup {1,3,7,9}. Anda tidak dapat membuat grup dengan perkalian bilangan bulat modulo 10 menggunakan bilangan bulat lain antara 1 dan 10. Untuk grup khusus ini, inversnya adalah pasangan 1 dan 9, serta 3 dan 7.

Dalam kasus di mana N itu sendiri adalah prima, semua bilangan bulat dari 1 hingga N – 1 adalah koprima dengan N. Grup seperti itu, dengan demikian, memiliki ordo N – 1. Menggunakan notasi sebelumnya, ℤ<sup>c</sup> mod N sama dengan ℤ* mod N ketika N adalah prima. Grup yang kami pilih untuk contoh sebelumnya, 〈ℤ* mod 11, •〉, adalah contoh khusus dari kelas grup ini.

Selanjutnya, fungsi φ(N) menghitung jumlah koprima hingga suatu bilangan N, dan dikenal sebagai **Fungsi Phi Euler**.<sup>[1](#footnote1)</sup> Menurut **Teorema Euler**, kapan pun dua bilangan bulat a dan N adalah koprima, berlaku:

* a<sup>φ(N)</sup> mod N = 1 mod N
Ini memiliki implikasi penting untuk kelas grup 〈ℤ* mod N, •〉 di mana N adalah bilangan prima. Untuk grup ini, eksponensiasi elemen grup mewakili eksponensiasi aritmetika. Artinya, a<sup>φ(N)</sup> mod N mewakili operasi aritmetika a<sup>φ(N)</sup> mod N. Karena setiap elemen a dalam grup-grup perkalian ini koprima dengan N, ini berarti bahwa a<sup>φ(N)</sup> mod N = a<sup>N – 1</sup> mod N = 1 mod N.
Teorema Euler adalah hasil yang sangat penting. Untuk memulai, ini menyiratkan bahwa semua elemen dalam 〈ℤ* mod N, •〉 hanya dapat berputar melalui sejumlah nilai melalui eksponensiasi yang membagi N – 1. Dalam kasus 〈ℤ* mod 11, •〉, ini berarti bahwa setiap elemen hanya dapat berputar melalui 2, 5, atau 10 elemen. Nilai grup yang dilalui setiap elemen melalui eksponensiasi dikenal sebagai **orde elemen**. Sebuah elemen dengan orde yang setara dengan orde grup adalah generator.

Selanjutnya, teorema Euler menyiratkan bahwa kita selalu dapat mengetahui hasil dari a<sup>N – 1</sup> mod N untuk setiap grup 〈ℤ* mod N, •〉 di mana N adalah bilangan prima. Ini berlaku terlepas dari seberapa rumit perhitungan sebenarnya mungkin.

Misalnya, anggap grup kita adalah ℤ* mod 160,481,182 (di mana 160,481,182 memang merupakan bilangan prima). Kita tahu bahwa semua bilangan bulat 1 hingga 160,481,181 harus menjadi elemen dari grup ini, dan bahwa φ(n) = 160,481,181. Meskipun kita tidak dapat melakukan semua langkah dalam perhitungan, kita tahu bahwa ekspresi seperti 514<sup>160,481,181</sup>, 2,005<sup>160,481,181</sup>, dan 256,212<sup>160,481,181</sup> semuanya harus mengevaluasi menjadi 1 mod 160,481,182.

## Bidang
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Grup adalah struktur aljabar dasar dalam aljabar abstrak, tetapi masih ada banyak lagi. Struktur aljabar lain yang perlu Anda kenal adalah bidang, khususnya bidang terbatas. Jenis struktur aljabar ini sering digunakan dalam kriptografi, seperti dalam Advanced Encryption Standard. Yang terakhir adalah skema enkripsi simetris utama yang akan Anda temui dalam praktik.

Sebuah bidang berasal dari konsep grup. Secara spesifik, sebuah **bidang** adalah himpunan elemen **S** yang dilengkapi dengan dua operator biner ◌ dan ◊, yang memenuhi kondisi berikut:

1. Himpunan **S** yang dilengkapi dengan ◌ adalah grup Abelian.
2. Himpunan **S** yang dilengkapi dengan ◊ adalah grup Abelian untuk elemen "non-nol".
3. Himpunan **S** yang dilengkapi dengan kedua operator memenuhi apa yang dikenal sebagai kondisi distributif: Misalkan a, b, dan c adalah elemen dari **S**. Maka **S** yang dilengkapi dengan kedua operator memenuhi sifat distributif ketika a ◌ (b ◊ c) = a ◌ b ◊ a ◌ c.
Perhatikan bahwa, seperti halnya dengan grup, definisi sebuah lapangan sangat abstrak. Ini tidak membuat klaim tentang jenis elemen dalam **S**, atau tentang operasi ◌ dan ◊. Ini hanya menyatakan bahwa sebuah lapangan adalah setiap himpunan elemen dengan dua operasi di mana ketiga kondisi di atas berlaku. (Elemen "nol" dalam grup Abelian kedua dapat diinterpretasikan secara abstrak.)
Jadi, apa contoh dari sebuah lapangan? Contoh yang baik adalah himpunan ℤ mod 7, atau {0,1,…,7} yang didefinisikan atas penjumlahan standar (menggantikan ◌ di atas) dan perkalian standar (menggantikan ◊ di atas).

Pertama, ℤ mod 7 memenuhi kondisi untuk menjadi grup Abelian atas penjumlahan, dan itu memenuhi kondisi untuk menjadi grup Abelian atas perkalian jika Anda hanya mempertimbangkan elemen non-nol. Kedua, kombinasi dari himpunan dengan dua operator memenuhi kondisi distributif.

Sangat bermanfaat secara didaktis untuk menjelajahi klaim ini dengan menggunakan beberapa nilai tertentu. Mari kita ambil nilai eksperimental 5, 2, dan 3, beberapa elemen yang dipilih secara acak dari himpunan ℤ mod 7, untuk menginspeksi lapangan 〈ℤ mod 7, +, •〉. Kami akan menggunakan tiga nilai ini secara berurutan, sesuai kebutuhan untuk menjelajahi kondisi tertentu.

Mari kita pertama-tama menjelajahi apakah ℤ mod 7 yang dilengkapi dengan penjumlahan adalah grup Abelian.

1. Kondisi penutupan: Mari kita ambil 5 dan 2 sebagai nilai kita. Dalam hal ini, [5 + 2] mod 7 = 7 mod 7 = 0. Ini memang merupakan elemen dari ℤ mod 7, jadi hasilnya konsisten dengan kondisi penutupan.
2. Kondisi asosiativitas: Mari kita ambil 5, 2, dan 3 sebagai nilai kita. Dalam hal ini, [(5 + 2) + 3] mod 7 = [5 + (2 + 3)] mod 7 = 10 mod 7 = 3. Ini konsisten dengan kondisi asosiativitas.
3. Kondisi identitas: Mari kita ambil 5 sebagai nilai kita. Dalam hal ini, [5 + 0] mod 7 = [0 + 5] mod 7 = 5. Jadi 0 tampaknya menjadi elemen identitas untuk penjumlahan.
4. Kondisi invers: Pertimbangkan invers dari 5. Perlu agar [5 + d] mod 7 = 0, untuk beberapa nilai d. Dalam hal ini, nilai unik dari ℤ mod 7 yang memenuhi kondisi ini adalah 2.
5. Kondisi komutativitas: Mari kita ambil 5 dan 3 sebagai nilai kita. Dalam hal ini, [5 + 3] mod 7 = [3 + 5] mod 7 = 1. Ini konsisten dengan kondisi komutativitas.

Himpunan ℤ mod 7 yang dilengkapi dengan penjumlahan jelas tampaknya merupakan grup Abelian. Mari sekarang kita jelajahi apakah ℤ mod 7 yang dilengkapi dengan perkalian adalah grup Abelian untuk semua elemen non-nol.

1. Kondisi penutupan: Mari kita ambil 5 dan 2 sebagai nilai kita. Dalam hal ini, [5 • 2] mod 7 = 10 mod 7 = 3. Ini juga merupakan elemen dari ℤ mod 7, jadi hasilnya konsisten dengan kondisi penutupan.
2. Kondisi Asosiativitas: Mari kita ambil 5, 2, dan 3 sebagai nilai kita. Dalam kasus ini, [(5 • 2) • 3] mod 7 = [5 • (2 • 3)] mod 7 = 30 mod 7 = 2. Ini konsisten dengan kondisi asosiativitas.
3. Kondisi Identitas: Mari kita ambil 5 sebagai nilai kita. Dalam kasus ini, [5 • 1] mod 7 = [1 • 5] mod 7 = 5. Jadi 1 tampaknya menjadi elemen identitas untuk perkalian.
4. Kondisi Invers: Pertimbangkan invers dari 5. Haruslah demikian bahwa [5 • d] mod 7 = 1, untuk beberapa nilai d. Nilai unik dari ℤ mod 7 yang memenuhi kondisi ini adalah 3. Ini konsisten dengan kondisi invers.
5. Kondisi Komutativitas: Mari kita ambil 5 dan 3 sebagai nilai kita. Dalam kasus ini, [5 • 3] mod 7 = [3 • 5] mod 7 = 15 mod 7 = 1. Ini konsisten dengan kondisi komutativitas.

Himpunan ℤ mod 7 jelas tampak memenuhi aturan untuk menjadi grup Abelian ketika digabungkan dengan baik penambahan atau perkalian atas elemen non-nol.

Akhirnya, himpunan ini dikombinasikan dengan kedua operator tampaknya memenuhi kondisi distributif. Mari kita ambil 5, 2, dan 3 sebagai nilai kita. Kita dapat melihat bahwa [5 • (2 + 3)] mod 7 = [5 • 2 + 5 • 3] mod 7 = 25 mod 7 = 4.

Kita sekarang telah melihat bahwa ℤ mod 7 yang dilengkapi dengan penambahan dan perkalian memenuhi aksioma untuk sebuah lapangan hingga ketika diuji dengan nilai tertentu. Tentu saja kita juga dapat menunjukkan hal itu secara umum, tetapi tidak akan melakukannya di sini.

Sebuah perbedaan kunci adalah antara dua jenis lapangan: lapangan hingga dan lapangan tak hingga.

Sebuah **lapangan tak hingga** melibatkan lapangan di mana himpunan **S** adalah tak terbatas besar. Himpunan bilangan real ℝ yang dilengkapi dengan penambahan dan perkalian adalah contoh dari lapangan tak hingga. Sebuah **lapangan hingga**, juga dikenal sebagai **lapangan Galois**, adalah lapangan di mana himpunan **S** adalah terbatas. Contoh kita di atas dari 〈ℤ mod 7, +, •〉 adalah lapangan hingga.

Dalam kriptografi, kita terutama tertarik pada lapangan hingga. Secara umum, dapat ditunjukkan bahwa lapangan hingga ada untuk beberapa himpunan elemen **S** jika dan hanya jika memiliki elemen p<sup>m</sup>, di mana p adalah bilangan prima dan m adalah bilangan bulat positif lebih besar atau sama dengan satu. Dengan kata lain, jika urutan dari beberapa himpunan **S** adalah bilangan prima (p<sup>m</sup> di mana m = 1) atau beberapa kekuatan prima (p<sup>m</sup> di mana m > 1), maka Anda dapat menemukan dua operator ◌ dan ◊ sehingga kondisi untuk sebuah lapangan terpenuhi.

Jika beberapa lapangan hingga memiliki bilangan prima elemen, maka itu disebut **lapangan prima**. Jika jumlah elemen dalam lapangan hingga adalah kekuatan prima, maka lapangan tersebut disebut **lapangan ekstensi**. Dalam kriptografi, kita tertarik pada kedua lapangan prima dan lapangan ekstensi.<sup>[2](#footnote2)</sup>
Bidang utama yang menarik dalam kriptografi adalah bidang di mana himpunan semua bilangan bulat dimodulasi oleh beberapa bilangan prima, dan operatornya adalah penjumlahan dan perkalian standar. Kelas bidang terbatas ini akan mencakup ℤ mod 2, ℤ mod 3, ℤ mod 5, ℤ mod 7, ℤ mod 11, ℤ mod 13, dan seterusnya. Untuk setiap bidang prima ℤ mod p, himpunan bilangan bulat dari bidang tersebut adalah sebagai berikut: {0,1,….,p – 2, p – 1}.
Dalam kriptografi, kita juga tertarik pada bidang ekstensi, khususnya bidang apa pun dengan 2<sup>m</sup> elemen di mana m > 1. Bidang terbatas seperti itu, misalnya, digunakan dalam Rijndael Cipher, yang merupakan dasar dari Advanced Encryption Standard. Sementara bidang prima relatif intuitif, bidang ekstensi basis 2 ini mungkin tidak demikian bagi siapa pun yang tidak familiar dengan aljabar abstrak.

Untuk memulai, memang benar bahwa setiap himpunan bilangan bulat dengan 2<sup>m</sup> elemen dapat diberi dua operator yang akan membuat kombinasi mereka menjadi sebuah bidang (selama m adalah bilangan bulat positif). Namun, hanya karena sebuah bidang ada tidak berarti bahwa ia mudah ditemukan atau secara khusus praktis untuk aplikasi tertentu.

Ternyata, bidang ekstensi yang sangat aplikatif dari 2<sup>m</sup> dalam kriptografi adalah bidang yang didefinisikan atas himpunan ekspresi polinomial tertentu, bukan beberapa himpunan bilangan bulat.

Misalnya, anggaplah kita ingin sebuah bidang ekstensi dengan 2<sup>3</sup> (yaitu, 8) elemen dalam himpunan. Meskipun mungkin ada banyak himpunan yang berbeda yang dapat digunakan untuk bidang ukuran tersebut, satu himpunan termasuk semua polinomial unik dari bentuk a<sub>2</sub>x<sup>2</sup> + a<sub>1</sub>x + a<sub>0</sub>, di mana setiap koefisien a<sub>i</sub> adalah 0 atau 1. Oleh karena itu, himpunan ini **S** mencakup elemen-elemen berikut:

1. 0: Kasus di mana a<sub>2</sub> = 0, a<sub>1</sub> = 0, dan a<sub>0</sub> = 0.
2. 1: Kasus di mana a<sub>2</sub> = 0, a<sub>1</sub> = 0, dan a<sub>0</sub> = 1.
3. x: Kasus di mana a<sub>2</sub> = 0, a<sub>1</sub> = 1, dan a<sub>0</sub> = 0.
4. x + 1: Kasus di mana a<sub>2</sub> = 0, a<sub>1</sub> = 1, dan a<sub>0</sub> = 1.
5. x<sup>2</sup>: Kasus di mana a<sub>2</sub>= 1, a<sub>1</sub> = 0, dan a<sub>0</sub> = 0.
6. x<sup>2</sup> + 1: Kasus di mana a<sub>2</sub> = 1, a<sub>1</sub> = 0, dan a<sub>0</sub> = 1.
7. x<sup>2</sup> + x: Kasus dimana a<sub>2</sub> = 1, a<sub>1</sub> = 1, dan a<sub>0</sub> = 0. 8. x<sup>2</sup> + x + 1: Kasus dimana a<sub>2</sub> = 1, a<sub>1</sub> = 1, dan a<sub>0</sub> = 1.

Jadi **S** akan menjadi himpunan {0,1,x,x + 1, x<sup>2</sup>,x<sup>2</sup> + 1, x<sup>2</sup> + x, x<sup>2</sup> + x + 1}. Operasi apa saja yang dapat didefinisikan atas himpunan elemen ini untuk memastikan kombinasinya merupakan sebuah lapangan?

Operasi pertama pada himpunan S (◌) dapat didefinisikan sebagai penjumlahan polinomial standar modulo 2. Yang perlu Anda lakukan adalah menambahkan polinomial seperti biasa, dan kemudian menerapkan modulo 2 ke setiap koefisien dari polinomial hasil. Berikut adalah beberapa contoh:

* [(x<sup>2</sup>) + (x<sup>2</sup> + x + 1)] mod 2 = [2x<sup>2</sup> + x + 1] mod 2 = x + 1
* [(x<sup>2</sup> + x) + (x)] mod 2 = [x<sup>2</sup> + 2x] mod 2 = x<sup>2</sup>
* [(x + 1) + (x<sup>2</sup> + x + 1)] mod 2 = [x<sup>2</sup> + 2x + 2] mod 2 = x<sup>2</sup> + 1

Operasi kedua pada himpunan S (◌) yang diperlukan untuk menciptakan lapangan lebih rumit. Ini adalah jenis perkalian, tetapi bukan perkalian standar dari aritmatika. Sebaliknya, Anda harus melihat setiap elemen sebagai vektor dan memahami operasi sebagai perkalian dua vektor tersebut modulo polinomial tak tereduksi.

Mari kita beralih ke ide tentang polinomial tak tereduksi. Sebuah **polinomial tak tereduksi** adalah polinomial yang tidak dapat difaktorkan (sama seperti angka prima tidak dapat difaktorkan menjadi komponen selain dari 1 dan angka prima itu sendiri). Untuk tujuan kita, kita tertarik pada polinomial yang tak tereduksi dengan respect terhadap himpunan semua bilangan bulat. (Perhatikan bahwa Anda mungkin dapat memfaktorkan polinomial tertentu dengan, misalnya, bilangan real atau kompleks, meskipun Anda tidak dapat memfaktorkannya menggunakan bilangan bulat.)

Misalnya, pertimbangkan polinomial x<sup>2</sup> - 3x + 2. Ini dapat ditulis ulang sebagai (x – 1)(x – 2). Oleh karena itu, ini bukan polinomial tak tereduksi. Sekarang pertimbangkan polinomial x<sup>2</sup> + 1. Menggunakan hanya bilangan bulat, tidak ada cara untuk lebih lanjut memfaktorkan ekspresi ini. Oleh karena itu, ini adalah polinomial tak tereduksi dengan respect terhadap bilangan bulat.
Selanjutnya, mari kita beralih ke konsep perkalian vektor. Kita tidak akan menjelajahi topik ini secara mendalam, Anda hanya perlu memahami satu aturan dasar: Pembagian vektor dapat terjadi selama pembilang memiliki derajat yang lebih tinggi atau sama dengan pembagi. Jika pembilang memiliki derajat lebih rendah dari pembagi, maka pembilang tidak lagi dapat dibagi oleh pembagi.

Sebagai contoh, pertimbangkan ekspresi x<sup>6</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Ini jelas dapat direduksi lebih lanjut karena derajat pembilang, 6, lebih tinggi dari derajat pembagi, 5. Sekarang pertimbangkan ekspresi x<sup>5</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Ini juga dapat direduksi lebih lanjut, karena derajat pembilang, 5, dan pembagi, 5, adalah sama.

Namun, sekarang pertimbangkan ekspresi x<sup>4</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Ini tidak dapat direduksi lebih lanjut, karena derajat pembilang, 4, lebih rendah dari derajat pembagi, 5.

Berdasarkan informasi ini, kita sekarang siap untuk menemukan operasi kedua untuk himpunan {0,1,x,x + 1,x<sup>2</sup>,x<sup>2</sup> + 1,x<sup>2</sup> + x,x<sup>2</sup> + x + 1}.

Saya sudah mengatakan bahwa operasi kedua harus dipahami sebagai perkalian vektor modulo suatu polinomial tak tereduksi. Polinomial tak tereduksi ini harus memastikan bahwa operasi kedua mendefinisikan grup Abelian atas **S** dan konsisten dengan kondisi distributif. Jadi, polinomial tak tereduksi apa yang seharusnya?

Karena semua vektor dalam himpunan memiliki derajat 2 atau lebih rendah, polinomial tak tereduksi tersebut harus berderajat 3. Jika perkalian dua vektor dalam himpunan menghasilkan polinomial derajat 3 atau lebih tinggi, kita tahu bahwa modulo polinomial derajat 3 selalu menghasilkan polinomial derajat 2 atau lebih rendah. Ini terjadi karena polinomial apa pun derajat 3 atau lebih tinggi selalu dapat dibagi oleh polinomial derajat 3. Selain itu, polinomial yang berfungsi sebagai pembagi harus tak tereduksi.

Ternyata, ada beberapa polinomial tak tereduksi derajat 3 yang bisa kita gunakan sebagai pembagi. Masing-masing polinomial ini mendefinisikan bidang yang berbeda bersama dengan himpunan S kita dan penjumlahan modulo 2. Ini berarti Anda memiliki beberapa opsi saat menggunakan bidang perluasan 2<sup>m</sup> dalam kriptografi.

Untuk contoh kita, anggaplah kita memilih polinomial x<sup>3</sup> + x + 1. Ini memang tak tereduksi, karena Anda tidak dapat memfaktorkannya menggunakan bilangan bulat. Selain itu, ini akan memastikan bahwa perkalian dua elemen akan menghasilkan polinomial derajat 2 atau kurang.
Mari kita pelajari sebuah contoh dari operasi kedua menggunakan polinomial x<sup>3</sup> + x + 1 sebagai pembagi untuk mengilustrasikan bagaimana cara kerjanya. Bayangkan Anda mengalikan elemen x<sup>2</sup> + 1 dengan x<sup>2</sup> + x dalam set **S** kita. Kemudian, kita perlu menghitung ekspresi [(x<sup>2</sup> + 1) • (x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1. Ini dapat disederhanakan sebagai berikut:
* [(x<sup>2</sup> + 1) • (x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1 =
* [x<sup>2</sup> • x<sup>2</sup> + x<sup>2</sup> • x + 1 • x<sup>2</sup> + 1 • x] mod x<sup>3</sup> + x + 1 = 
* [x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x] mod x<sup>3</sup> + x + 1
    
Kita tahu bahwa [x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x] mod x<sup>3</sup> + x + 1 dapat direduksi karena derajat pembilang (4) lebih tinggi dari pembagi (3).

Untuk memulai, Anda dapat melihat bahwa ekspresi x<sup>3</sup> + x + 1 masuk ke dalam x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x sebanyak x kali. Anda dapat memverifikasinya dengan mengalikan x<sup>3</sup> + x + 1 dengan x, yang merupakan x<sup>4</sup> + x<sup>2</sup> + x. Karena istilah terakhir memiliki derajat yang sama dengan pembilang, yaitu 4, kita tahu ini berhasil. Anda dapat menghitung sisa dari pembagian ini oleh x sebagai berikut:

* [(x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x) – (x<sup>4</sup> + x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1 = 
* [x<sup>3</sup>] mod x<sup>3</sup> + x + 1 =
* x<sup>3</sup>

Jadi setelah membagi x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x dengan x<sup>3</sup> + x + 1 sebanyak x kali, kita memiliki sisa sebesar x<sup>3</sup>. Apakah ini dapat dibagi lebih lanjut dengan x<sup>3</sup> + x + 1?
Secara intuitif, mungkin menarik untuk mengatakan bahwa x<sup>3</sup> tidak lagi dapat dibagi oleh x<sup>3</sup> + x + 1, karena istilah terakhir tampak lebih besar. Namun, ingatlah diskusi kita sebelumnya tentang pembagian vektor. Selama pembilang memiliki derajat yang lebih besar atau sama dengan pembagi, ekspresi dapat direduksi lebih lanjut. Secara spesifik, ekspresi x<sup>3</sup> + x + 1 dapat masuk ke dalam x<sup>3</sup> tepat 1 kali. Sisa hasil bagi dihitung sebagai berikut:
[(x<sup>3</sup>) – (x<sup>3</sup> + x + 1)] mod x<sup>3</sup> + x + 1 = 
[x + 1] mod x<sup>3</sup> + x + 1 = 
x + 1

Anda mungkin bertanya-tanya mengapa (x<sup>3</sup>) – (x<sup>3</sup> + x + 1) bernilai x + 1 dan bukan – x – 1. Ingatlah bahwa operasi pertama dari lapangan kita didefinisikan modulo 2. Oleh karena itu, pengurangan dua vektor menghasilkan hasil yang sama persis dengan penjumlahan dua vektor.

Untuk merangkum perkalian x<sup>2</sup> + 1 dan x<sup>2</sup> + x: Ketika Anda mengalikan kedua istilah tersebut Anda mendapatkan polinomial derajat 4, x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x, yang perlu direduksi modulo x<sup>3</sup> + x + 1. Polinomial derajat 4 dapat dibagi oleh x<sup>3</sup> + x + 1 tepat x + 1 kali. Sisa setelah membagi x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x oleh x<sup>3</sup> + x + 1 tepat x + 1 kali adalah x + 1. Ini memang merupakan elemen dalam set kita {0,1,x,x + 1,x<sup>2</sup>,x<sup>2</sup> + 1,x<sup>2</sup> + x,x<sup>2</sup> + x + 1}.

Mengapa lapangan perluasan dengan basis 2 atas set polinomial, seperti dalam contoh di atas, berguna untuk kriptografi? Alasannya adalah Anda dapat melihat koefisien dalam polinomial dari set tersebut, baik 0 atau 1, sebagai elemen dari string biner dengan panjang tertentu. Set **S** dalam contoh kita di atas, misalnya, dapat dilihat sebagai set S yang mencakup semua string biner dengan panjang 3 (000 hingga 111). Operasi pada **S**, kemudian, juga dapat digunakan untuk melakukan operasi pada string biner ini dan menghasilkan string biner dengan panjang yang sama.

## Aljabar Abstrak dalam Praktik
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>
Meskipun bahasa formal dan abstraksi dari diskusi, konsep grup seharusnya tidak terlalu sulit untuk dipahami. Ini hanya sekumpulan elemen bersama dengan operasi biner, di mana pelaksanaan operasi biner tersebut pada elemen-elemen tersebut memenuhi empat kondisi umum. Sebuah grup Abelian hanya memiliki kondisi tambahan yang dikenal sebagai komutativitas. Sebuah grup siklik, pada gilirannya, adalah jenis khusus dari grup Abelian, yaitu yang memiliki generator. Sebuah lapangan hanyalah konstruksi yang lebih kompleks dari konsep grup dasar.

Tetapi jika Anda adalah orang yang cenderung praktis, Anda mungkin bertanya-tanya pada titik ini: Siapa yang peduli? Apakah mengetahui beberapa kumpulan elemen dengan operator adalah grup, atau bahkan grup Abelian atau siklik, memiliki relevansi dunia nyata? Apakah mengetahui sesuatu adalah lapangan?

Tanpa terlalu detail, jawabannya adalah "ya". Grup pertama kali diciptakan pada abad ke-19 oleh matematikawan Prancis Evariste Galois. Dia menggunakannya untuk menarik kesimpulan tentang penyelesaian persamaan polinomial dengan derajat lebih dari lima.

Sejak itu konsep grup telah membantu menerangi sejumlah masalah dalam matematika dan bidang lainnya. Berdasarkan konsep ini, misalnya, fisikawan Murray-Gellman dapat memprediksi keberadaan sebuah partikel sebelum sebenarnya diamati dalam eksperimen. Sebagai contoh lain, ahli kimia menggunakan teori grup untuk mengklasifikasikan bentuk molekul. Matematikawan bahkan telah menggunakan konsep grup untuk menarik kesimpulan tentang sesuatu yang konkret seperti kertas dinding!

Pada dasarnya menunjukkan bahwa sekumpulan elemen dengan beberapa operator adalah grup, berarti apa yang Anda deskripsikan memiliki simetri tertentu. Bukan simetri dalam pengertian umum kata, tetapi dalam bentuk yang lebih abstrak. Dan ini dapat memberikan wawasan substansial ke dalam sistem dan masalah tertentu. Konsep yang lebih kompleks dari aljabar abstrak hanya memberi kita informasi tambahan.

Yang paling penting, Anda akan melihat pentingnya grup teori bilangan dan lapangan dalam praktik melalui aplikasi mereka dalam kriptografi, khususnya kriptografi kunci publik. Kami telah melihat dalam diskusi kami tentang lapangan, misalnya, bagaimana lapangan ekstensi digunakan dalam Rijndael Cipher. Kami akan membahas contoh tersebut di *Bab 5*.

## Eksplorasi Lebih Lanjut

Untuk diskusi lebih lanjut tentang aljabar abstrak, saya akan merekomendasikan seri video yang sangat baik tentang aljabar abstrak oleh Socratica. Saya khususnya merekomendasikan video-video berikut: “What is abstract algebra?”, “Group definition (expanded)”, “Ring definition (expanded)”, dan “Field definition (expanded).” Keempat video ini akan memberi Anda beberapa wawasan tambahan ke dalam sebagian besar diskusi di atas. (Kami tidak membahas cincin, tetapi lapangan hanyalah jenis khusus dari cincin.)

Untuk diskusi lebih lanjut tentang teori bilangan modern, Anda dapat berkonsultasi dengan banyak diskusi lanjutan tentang kriptografi. Saya akan menawarkan sebagai saran Introduction to Modern Cryptography oleh Jonathan Katz dan Yehuda Lindell atau Understanding Cryptography oleh Christof Paar dan Jan Pelzl untuk diskusi lebih lanjut.

### Catatan
[^1]: Fungsi ini bekerja sebagai berikut. Setiap bilangan bulat N dapat difaktorkan menjadi produk dari bilangan prima. Misalkan sebuah N tertentu difaktorkan sebagai berikut: p<sub>1</sub><sup>e1</sup> • p<sub>2</sub><sup>e2</sup> …. • p<sub>m</sub><sup>em</sup> di mana semua p adalah bilangan prima dan semua e adalah bilangan bulat yang lebih besar atau sama dengan 1. Maka, φ(N) = Sum<sub>i=1…m</sub>[p<sub>i</sub><sup>ei</sup> – p<sub>i</sub><sup>ei - 1</sup>] [^1].
[^2]: Bidang ekstensi menjadi sangat kontra-intuitif. Alih-alih memiliki elemen dari bilangan bulat, mereka memiliki himpunan polinomial. Selain itu, setiap operasi dilakukan modulo beberapa polinomial tak tereduksi [^2].

[^3]: Lihat [Video YouTube](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be) [^3].

[^4]: Socratica, [Aljabar Abstrak](https://www.socratica.com/subject/abstract-algebra) [^4].

[^5]: Katz dan Lindell, *Pengantar Kriptografi Modern*, edisi ke-2, 2015 (CRC Press: Boca Raton, FL). Paar dan Pelzl, *Memahami Kriptografi*, 2010 (Springer-Verlag: Berlin) [^5].

# Kriptografi Simetris
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

Salah satu dari dua cabang utama kriptografi adalah kriptografi simetris. Ini mencakup skema enkripsi serta skema yang berkaitan dengan autentikasi dan integritas. Sampai tahun 1970-an, seluruh kriptografi akan terdiri dari skema enkripsi simetris.

Diskusi utama dimulai dengan melihat skema enkripsi simetris dan membuat perbedaan penting antara cipher aliran dan cipher blok. Kemudian, kita beralih ke kode autentikasi pesan, yang merupakan skema untuk memastikan integritas dan keaslian pesan. Akhirnya, kita menjelajahi bagaimana skema enkripsi simetris dan kode autentikasi pesan dapat digabungkan untuk memastikan komunikasi yang aman.

Bab ini membahas berbagai skema kriptografi simetris dari praktik secara singkat. Bab berikutnya menawarkan eksposisi terperinci tentang enkripsi dengan cipher aliran dan cipher blok dari praktik, yaitu RC4 dan AES masing-masing.

Sebelum memulai diskusi kami tentang kriptografi simetris, saya ingin secara singkat membuat beberapa catatan tentang ilustrasi Alice dan Bob dalam bab ini dan bab-bab berikutnya.

## Alice dan Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Dalam mengilustrasikan prinsip-prinsip kriptografi, orang sering mengandalkan contoh yang melibatkan Alice dan Bob. Saya akan melakukan hal yang sama.

Terutama jika Anda baru dalam kriptografi, penting untuk menyadari bahwa contoh-contoh Alice dan Bob ini hanya dimaksudkan untuk berfungsi sebagai ilustrasi dari prinsip-prinsip kriptografi dan konstruksi dalam lingkungan yang disederhanakan. Namun, prinsip-prinsip dan konstruksi tersebut dapat diterapkan pada berbagai konteks kehidupan nyata yang lebih luas.

Berikut adalah lima poin kunci yang perlu diingat tentang contoh yang melibatkan Alice dan Bob dalam kriptografi:

1. Mereka dapat dengan mudah diterjemahkan ke dalam contoh dengan jenis aktor lain seperti perusahaan atau organisasi pemerintah.
2. Mereka dapat dengan mudah diperluas untuk mencakup tiga atau lebih aktor.
3. Dalam contoh-contoh tersebut, Bob dan Alice biasanya merupakan peserta aktif dalam menciptakan setiap pesan dan dalam penerapan skema kriptografi pada pesan tersebut. Namun, dalam kenyataannya, komunikasi elektronik sebagian besar otomatis. Misalnya, ketika Anda mengunjungi sebuah situs web menggunakan keamanan lapisan transportasi, kriptografi biasanya sepenuhnya ditangani oleh komputer Anda dan server web. 4. Dalam konteks komunikasi elektronik, "pesan" yang dikirim melalui saluran komunikasi biasanya adalah paket TCP/IP. Ini bisa termasuk e-mail, pesan Facebook, percakapan telepon, transfer file, sebuah situs web, unggahan perangkat lunak, dan sebagainya. Mereka bukan pesan dalam pengertian tradisional. Namun, para kriptografer sering menyederhanakan kenyataan ini dengan menyatakan bahwa pesannya, misalnya, adalah sebuah e-mail.
5. Contoh-contoh tersebut biasanya berfokus pada komunikasi elektronik, tetapi juga bisa diperluas ke bentuk komunikasi tradisional seperti surat.

## Skema enkripsi simetris
<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Kita dapat mendefinisikan **skema enkripsi simetris** secara longgar sebagai skema kriptografi dengan tiga algoritma:

1. Sebuah **algoritma generasi kunci**, yang menghasilkan kunci privat.
2. Sebuah **algoritma enkripsi**, yang mengambil kunci privat dan plaintext sebagai input dan menghasilkan ciphertext.
3. Sebuah **algoritma dekripsi**, yang mengambil kunci privat dan ciphertext sebagai input dan menghasilkan plaintext asli.

Biasanya sebuah skema enkripsi—baik simetris maupun asimetris—menawarkan sebuah templat untuk enkripsi berdasarkan algoritma inti, bukan spesifikasi yang tepat.

Misalnya, pertimbangkan Salsa20, sebuah skema enkripsi simetris. Ini dapat digunakan dengan panjang kunci 128- dan 256-bit. Pilihan mengenai panjang kunci mempengaruhi beberapa detail kecil dari algoritma (jumlah ronde dalam algoritma untuk tepatnya).

Tetapi seseorang tidak akan mengatakan bahwa menggunakan Salsa20 dengan kunci 128-bit adalah skema enkripsi yang berbeda dari Salsa20 dengan kunci 256-bit. Algoritma inti tetap sama. Hanya ketika algoritma inti berubah kita benar-benar berbicara tentang dua skema enkripsi yang berbeda.

Skema enkripsi simetris biasanya berguna dalam dua jenis kasus: (1) Kasus di mana dua atau lebih agen berkomunikasi dari jarak jauh dan ingin menjaga isi komunikasi mereka tetap rahasia; dan (2) kasus di mana satu agen ingin menjaga isi pesan tetap rahasia sepanjang waktu.

Anda dapat melihat penggambaran situasi (1) di *Gambar 1* di bawah ini. Bob ingin mengirim pesan M ke Alice dari jarak jauh, tetapi tidak ingin orang lain dapat membaca pesan tersebut.

Bob pertama-tama mengenkripsi pesan M dengan kunci privat K. Kemudian, dia mengirim ciphertext C ke Alice. Setelah Alice menerima ciphertext, dia dapat mendekripsinya menggunakan kunci K dan membaca plaintext. Dengan skema enkripsi yang baik, setiap penyerang yang mencegat ciphertext C seharusnya tidak dapat mempelajari apa pun yang benar-benar signifikan tentang pesan M.

Anda dapat melihat penggambaran situasi (2) di *Gambar 2* di bawah ini. Bob ingin mencegah orang lain dari melihat informasi tertentu. Situasi tipikal mungkin adalah bahwa Bob adalah seorang karyawan yang menyimpan data sensitif di komputernya, yang tidak seharusnya dibaca oleh orang luar maupun rekan kerjanya.
Bob mengenkripsi pesan M pada waktu T<sub>0</sub> dengan kunci K untuk menghasilkan teks tersandi C. Pada waktu T<sub>1</sub> dia membutuhkan pesan tersebut lagi, dan mendekripsi teks tersandi C dengan kunci K. Setiap penyerang yang mungkin menemukan teks tersandi C dalam waktu tersebut seharusnya tidak dapat menarik kesimpulan yang signifikan tentang M darinya.
*Gambar 1: Kerahasiaan melintasi ruang*

![Gambar 1: Kerahasiaan melintasi ruang](assets/Figure4-1.webp "Gambar 1: Kerahasiaan melintasi ruang")

*Gambar 2: Kerahasiaan sepanjang waktu*

![Gambar 2: Kerahasiaan sepanjang waktu](assets/Figure4-2.webp "Gambar 2: Kerahasiaan sepanjang waktu")

## Sebuah contoh: Sandi geser
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

Di Bab 2, kita menemui sandi geser yang merupakan contoh dari skema enkripsi simetris yang sangat sederhana. Mari kita lihat lagi di sini.

Misalkan sebuah kamus *D* yang menyamakan semua huruf dalam alfabet Inggris, secara berurutan, dengan set angka {0,1,2…,25}. Asumsikan sebuah set pesan yang mungkin **M**. Sandi geser, maka, adalah skema enkripsi yang didefinisikan sebagai berikut:

- Pilih secara acak sebuah kunci k dari set kunci yang mungkin **K**, di mana **K** = {0,1,2,…,25}
- Enkripsi sebuah pesan m є **M**, sebagai berikut:
    - Pisahkan m menjadi huruf-huruf individunya m<sub>0</sub>, m<sub>1</sub>,….m<sub>i</sub>….,m<sub>l</sub>
    - Konversi setiap m<sub>i</sub> menjadi angka menurut *D*
    - Untuk setiap m<sub>i</sub>, c<sub>i</sub> = [(m<sub>i</sub> + k) mod 26]
    - Konversi setiap c<sub>i</sub> menjadi huruf menurut *D*
    - Kemudian gabungkan c<sub>0</sub>, c<sub>1</sub>,….,c<sub>l</sub> untuk menghasilkan teks tersandi c
- Dekripsi sebuah teks tersandi c sebagai berikut:
    - Konversi setiap c<sub>i</sub> menjadi angka menurut *D*
    - Untuk setiap c<sub>i</sub>, m<sub>i</sub> = [(c<sub>i</sub> – k) mod 26]
    - Konversi setiap m<sub>i</sub> menjadi huruf menurut *D*
    - Kemudian gabungkan m<sub>0</sub>, m<sub>1</sub>,….,m<sub>l</sub> untuk menghasilkan pesan asli m

Apa yang membuat sandi geser menjadi skema enkripsi simetris adalah penggunaan kunci yang sama untuk proses enkripsi dan dekripsi. Misalnya, anggaplah Anda ingin mengenkripsi pesan “DOG” menggunakan sandi geser, dan Anda secara acak memilih "24" sebagai kunci. Mengenkripsi pesan dengan kunci ini akan menghasilkan “BME”. Satu-satunya cara untuk mendapatkan pesan asli adalah dengan menggunakan kunci yang sama, "24", untuk proses dekripsi.
Shift cipher ini adalah contoh dari **monoalphabetic substitution cipher**: skema enkripsi di mana alfabet ciphertext tetap (yaitu, hanya menggunakan satu alfabet). Dengan asumsi bahwa algoritma dekripsi bersifat deterministik, setiap simbol dalam ciphertext substitusi paling banyak dapat berkaitan dengan satu simbol dalam plaintext.
Hingga tahun 1700-an, banyak aplikasi enkripsi sangat bergantung pada monoalphabetic substitution ciphers, meskipun seringkali ini jauh lebih kompleks daripada Shift cipher. Misalnya, Anda dapat secara acak memilih sebuah huruf dari alfabet untuk setiap huruf teks asli dengan batasan bahwa setiap huruf hanya muncul sekali dalam alfabet ciphertext. Ini berarti Anda akan memiliki 26 faktorial kemungkinan kunci privat, yang sangat besar di era sebelum komputer.

Perhatikan bahwa Anda akan sering menemukan istilah **cipher** dalam kriptografi. Sadarilah bahwa istilah ini memiliki berbagai makna. Faktanya, saya tahu setidaknya ada lima makna berbeda dari istilah ini dalam kriptografi.

Dalam beberapa kasus, itu merujuk pada skema enkripsi, seperti dalam Shift cipher dan monoalphabetic substitution cipher. Namun, istilah tersebut juga dapat merujuk khusus pada algoritma enkripsi, kunci privat, atau hanya ciphertext dari skema enkripsi tersebut.

Terakhir, istilah cipher juga dapat merujuk pada algoritma inti dari mana Anda dapat membangun skema kriptografi. Ini dapat mencakup berbagai algoritma enkripsi, tetapi juga jenis skema kriptografi lainnya. Makna istilah ini menjadi relevan dalam konteks block ciphers (lihat bagian "Block Ciphers" di bawah).

Anda juga mungkin menemukan istilah **encipher** atau **decipher**. Istilah-istilah ini hanyalah sinonim untuk enkripsi dan dekripsi.

## Serangan brute force dan prinsip Kerckhoff
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Shift cipher adalah skema enkripsi simetris yang sangat tidak aman, setidaknya di dunia modern.<sup>[1](#footnote1)</sup> Seorang penyerang hanya bisa mencoba dekripsi dari ciphertext apa pun dengan semua 26 kunci yang mungkin untuk melihat hasil mana yang masuk akal. Jenis serangan ini, di mana penyerang hanya mengulangi kunci untuk melihat apa yang berhasil, dikenal sebagai **brute force attack** atau **exhaustive key search**.

Untuk setiap skema enkripsi memenuhi konsep minimal keamanan, itu harus memiliki satu set kunci yang mungkin, atau **keyspace**, yang sangat besar sehingga serangan brute-force tidak layak. Semua skema enkripsi modern memenuhi standar ini. Ini dikenal sebagai **prinsip key space yang cukup**. Prinsip serupa biasanya berlaku dalam berbagai jenis skema kriptografi.

Untuk mendapatkan gambaran tentang ukuran key space yang masif dalam skema enkripsi modern, anggaplah bahwa sebuah file telah dienkripsi dengan menggunakan standar enkripsi lanjutan 128-bit. Ini berarti seorang penyerang memiliki satu set 2<sup>128</sup> kunci yang perlu dia ulangi untuk serangan brute force. Peluang sukses 0,78% dengan strategi ini akan memerlukan penyerang untuk mengulangi sekitar 2,65 x 10<sup>36</sup> kunci.
Misalkan kita secara optimis mengasumsikan bahwa seorang penyerang dapat mencoba 10 kuadriliun kunci per detik (yaitu, 10<sup>16</sup> kunci per detik). Untuk menguji 0,78% dari semua kunci dalam ruang kunci, serangannya harus berlangsung selama 2,65 x 10<sup>20</sup> detik. Ini sekitar 8,4 triliun tahun. Jadi, bahkan serangan brute force oleh lawan yang sangat kuat tidak realistis dengan skema enkripsi 128-bit modern. Ini adalah prinsip ruang kunci yang cukup bermain.

Apakah cipher shift lebih aman jika penyerang tidak mengetahui algoritma enkripsi? Mungkin, tapi tidak banyak.

Dalam hal apapun, kriptografi modern, selalu mengasumsikan bahwa keamanan dari setiap skema enkripsi simetris hanya bergantung pada menjaga kunci privat tetap rahasia. Penyerang selalu diasumsikan mengetahui semua detail lainnya, termasuk ruang pesan, ruang kunci, ruang ciphertext, algoritma pemilihan kunci, algoritma enkripsi, dan algoritma dekripsi.

Ide bahwa keamanan dari skema enkripsi simetris hanya dapat bergantung pada kerahasiaan kunci privat dikenal sebagai **Prinsip Kerckhoffs**.

Seperti yang awalnya dimaksudkan oleh Kerckhoffs, prinsip ini hanya berlaku untuk skema enkripsi simetris. Namun, versi yang lebih umum dari prinsip ini, juga berlaku untuk semua jenis skema kriptografi modern lainnya: Desain dari setiap skema kriptografi tidak harus dirahasiakan agar dapat aman; kerahasiaan hanya dapat meluas ke beberapa string informasi, biasanya kunci privat.

Prinsip Kerckhoffs adalah pusat dari kriptografi modern untuk empat alasan.<sup>[2](#footnote2)</sup> Pertama, hanya ada sejumlah terbatas skema kriptografi untuk jenis aplikasi tertentu. Misalnya, sebagian besar aplikasi enkripsi simetris modern menggunakan cipher Rijndael. Jadi, kerahasiaan Anda mengenai desain skema hanya sangat terbatas. Namun, ada lebih banyak fleksibilitas dalam menjaga beberapa kunci privat untuk cipher Rijndael tetap rahasia.

Kedua, lebih mudah untuk mengganti beberapa string informasi daripada seluruh skema kriptografi. Misalkan bahwa semua karyawan sebuah perusahaan memiliki perangkat lunak enkripsi yang sama, dan setiap dua karyawan memiliki kunci privat untuk berkomunikasi secara rahasia. Kompromi kunci adalah masalah dalam skenario ini, tapi setidaknya perusahaan dapat menjaga perangkat lunak dengan pelanggaran keamanan tersebut. Jika perusahaan bergantung pada kerahasiaan skema, maka setiap pelanggaran kerahasiaan tersebut akan memerlukan penggantian semua perangkat lunak.

Ketiga, prinsip Kerckhoffs memungkinkan standarisasi dan kompatibilitas antar pengguna skema kriptografi. Ini memiliki manfaat besar untuk efisiensi. Misalnya, sulit untuk membayangkan bagaimana jutaan orang dapat terhubung secara aman ke server web Google setiap hari, jika keamanan tersebut memerlukan menjaga skema kriptografi tetap rahasia.

Keempat, prinsip Kerckhoff memungkinkan pengawasan publik terhadap skema kriptografi. Jenis pengawasan ini mutlak diperlukan untuk mencapai skema kriptografi yang aman. Sebagai ilustrasi, algoritma inti utama dalam kriptografi simetris, cipher Rijndael, adalah hasil dari kompetisi yang diselenggarakan oleh National Institute of Standards and Technology antara 1997 dan 2000.

Setiap sistem yang mencoba mencapai **keamanan melalui obskuritas** adalah sistem yang bergantung pada menjaga detail desain dan/atau implementasinya tetap rahasia. Dalam kriptografi, ini khususnya adalah sistem yang bergantung pada menjaga detail desain dari skema kriptografi tetap rahasia. Jadi, keamanan melalui obskuritas adalah kontras langsung dengan Prinsip Kerckhoffs.
Kemampuan keterbukaan untuk meningkatkan kualitas dan keamanan juga berlaku lebih luas di dunia digital daripada hanya kriptografi. Distribusi Linux yang bebas dan sumber terbuka seperti Debian, misalnya, umumnya memiliki beberapa keunggulan dibandingkan dengan pesaingnya Windows dan MacOS dalam hal privasi, stabilitas, keamanan, dan fleksibilitas. Meskipun hal itu mungkin memiliki beberapa penyebab, prinsip yang paling penting mungkin, seperti yang diungkapkan Eric Raymond dalam esainya yang terkenal "The Cathedral and the Bazaar," bahwa "[d]engan cukup banyak mata, semua bug menjadi dangkal."<sup>[3](#footnote3)</sup> Ini adalah prinsip kebijaksanaan dari kerumunan yang memberikan kesuksesan terbesar kepada Linux.
Seseorang tidak pernah bisa menyatakan secara tegas bahwa sebuah skema kriptografi itu "aman" atau "tidak aman." Sebaliknya, ada berbagai konsep keamanan untuk skema kriptografi. Setiap **definisi keamanan kriptografi** harus menentukan (1) tujuan keamanan, serta (2) kemampuan dari penyerang. Menganalisis skema kriptografi terhadap satu atau lebih konsep keamanan tertentu memberikan wawasan tentang aplikasi dan keterbatasannya.

Meskipun kita tidak akan membahas semua detail dari berbagai konsep keamanan kriptografi, Anda harus tahu bahwa dua asumsi adalah umum untuk semua konsep keamanan kriptografi modern yang berkaitan dengan skema simetris dan asimetris (dan dalam beberapa bentuk ke primitif kriptografi lainnya):

* Pengetahuan penyerang tentang skema sesuai dengan prinsip Kerckhoffs.
* Penyerang tidak dapat melakukan serangan brute force pada skema secara layak. Secara spesifik, model ancaman dari konsep keamanan kriptografi biasanya bahkan tidak memperbolehkan serangan brute force, karena mereka mengasumsikan bahwa ini bukan pertimbangan yang relevan.

## Stream ciphers
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Skema enkripsi simetris secara standar dibagi menjadi dua tipe: stream ciphers dan block ciphers. Namun, perbedaan ini agak bermasalah, karena orang menggunakan istilah ini secara tidak konsisten. Dalam beberapa bagian berikut, saya akan menjelaskan perbedaan tersebut dengan cara yang menurut saya terbaik. Namun, Anda harus sadar bahwa banyak orang akan menggunakan istilah ini secara berbeda dari yang saya jelaskan.

Mari kita pertama kali membahas tentang stream ciphers. Sebuah **stream cipher** adalah skema enkripsi simetris di mana enkripsi terdiri dari dua langkah.

Pertama, sebuah string sepanjang plaintext dihasilkan melalui kunci privat. String ini disebut **keystream**.

Selanjutnya, keystream secara matematis digabungkan dengan plaintext untuk menghasilkan ciphertext. Kombinasi ini biasanya adalah operasi XOR. Untuk dekripsi, Anda bisa saja membalik operasi tersebut. (Perhatikan bahwa A XOR B = B XOR A, dalam kasus A dan B adalah bit-string. Jadi, urutan operasi XOR dalam stream cipher tidak mempengaruhi hasil. Sifat ini dikenal sebagai komutativitas.)

Sebuah XOR stream cipher yang tipikal digambarkan dalam *Figure 3*. Anda pertama kali mengambil kunci privat K dan menggunakannya untuk menghasilkan keystream. Keystream tersebut, kemudian, digabungkan dengan plaintext melalui operasi XOR untuk menghasilkan ciphertext. Setiap agen yang menerima ciphertext dapat dengan mudah mendekripsinya jika mereka memiliki kunci K. Yang dia butuhkan hanyalah membuat keystream sepanjang ciphertext sesuai dengan prosedur yang ditentukan oleh skema dan XOR itu dengan ciphertext.

*Figure 3: Sebuah XOR stream cipher*

![Figure 3: Sebuah XOR stream cipher](assets/Figure4-3.webp "Figure 3: Sebuah XOR stream cipher")
Ingatlah bahwa skema enkripsi biasanya merupakan templat untuk enkripsi dengan algoritma inti yang sama, bukan spesifikasi yang tepat. Sebagai perluasan, stream cipher biasanya merupakan templat untuk enkripsi di mana Anda dapat menggunakan kunci dengan panjang yang berbeda. Meskipun panjang kunci dapat mempengaruhi beberapa detail kecil dari skema tersebut, hal itu tidak akan mempengaruhi bentuk esensialnya.

Shift cipher adalah contoh dari stream cipher yang sangat sederhana dan tidak aman. Menggunakan satu huruf (kunci privat), Anda dapat menghasilkan rangkaian huruf sepanjang pesan (keystream). Keystream ini, kemudian, digabungkan dengan plaintext melalui operasi modulo untuk menghasilkan ciphertext. (Operasi modulo ini dapat disederhanakan menjadi operasi XOR ketika merepresentasikan huruf dalam bit).

Contoh terkenal lain dari stream cipher adalah **Vigenere cipher**, setelah Blaise de Vigenere yang sepenuhnya mengembangkannya pada akhir abad ke-16 (meskipun orang lain telah melakukan banyak pekerjaan sebelumnya). Ini adalah contoh dari **polyalphabetic substitution cipher**: skema enkripsi di mana alfabet ciphertext untuk simbol plaintext berubah tergantung pada posisinya dalam teks. Berbeda dengan monoalphabetic substitution cipher, simbol ciphertext dapat dikaitkan dengan lebih dari satu simbol plaintext.

Seiring dengan popularitas enkripsi di Eropa Renaisans, demikian juga **cryptanalysis**—yaitu, pemecahan ciphertext—khususnya, menggunakan **frequency analysis**. Teknik terakhir menggunakan regularitas statistik dalam bahasa kita untuk memecahkan ciphertext, dan ditemukan oleh para sarjana Arab sudah pada abad kesembilan. Ini adalah teknik yang bekerja dengan sangat baik dengan teks yang lebih panjang. Dan bahkan monoalphabetic substition cipher yang paling canggih pun tidak lagi cukup melawan frequency analysis pada tahun 1700-an di Eropa, khususnya dalam pengaturan militer dan keamanan. Karena Vigenere cipher menawarkan kemajuan signifikan dalam keamanan, cipher ini menjadi populer di periode ini dan tersebar luas pada akhir tahun 1700-an.

Secara informal, skema enkripsi bekerja sebagai berikut:

1.	Pilih kata dengan beberapa huruf sebagai kunci privat
2.	Untuk setiap pesan, terapkan shift cipher pada setiap huruf dari pesan menggunakan huruf yang sesuai dalam kata kunci sebagai shift
3.	Jika Anda telah melewati kata kunci tetapi masih belum sepenuhnya mengenkripsi plaintext, lagi terapkan huruf-huruf kata kunci sebagai shift cipher pada huruf-huruf yang sesuai dalam sisa teks
4.	Lanjutkan proses ini sampai seluruh pesan telah dienkripsi

Untuk mengilustrasikan, anggaplah kunci privat Anda adalah GOLD dan Anda ingin mengenkripsi pesan "CRYPTOGRAPHY". Dalam hal ini Anda akan melanjutkan sebagai berikut menurut Vigenere cipher:

- c<sub>0</sub> = [(2 + 6) Mod 26] = 8 = I
- c<sub>1</sub> = [(17 + 14) Mod 26] = 5 = F
- c<sub>2</sub> = [(24 + 11) Mod 26] = 9 = J
- c<sub>3</sub> = [(15 + 3) Mod 26] = 18 = S
- c<sub>4</sub> = [(19 + 6) Mod 26] = 25 = Z
- c<sub>5</sub> = [(14 + 14) Mod 26] = 2 = C
- c<sub>6</sub> = [(6 + 11) Mod 26] = 17 = R
- c<sub>7</sub> = [(17 + 3) Mod 26] = 20 = U
- c<sub>8</sub> = [(0 + 6) Mod 26] = 6 = G
- c<sub>9</sub> = [(15 + 14) Mod 26] = 3 = D
- c<sub>10</sub> = [(7 + 11) Mod 26] = 18 = S
- c<sub>11</sub> = [(24 + 3) Mod 26] = 1 = B
- c = "IFJSZCRUGDSB"

Contoh terkenal lain dari sandi aliran adalah **one-time pad**. Dengan one-time pad, Anda cukup membuat rangkaian bit acak sepanjang pesan teks asli dan menghasilkan teks sandi melalui operasi XOR. Oleh karena itu, kunci privat dan aliran kunci sama dengan one-time pad.

Sementara sandi Shift dan sandi Vigenere sangat tidak aman di zaman modern, one-time pad sangat aman jika digunakan dengan benar. Mungkin aplikasi paling terkenal dari one-time pad adalah, setidaknya sampai tahun 1980-an, untuk **hotline Washington-Moskow**.<sup>[4](#footnote4)</sup>

Hotline adalah tautan komunikasi langsung antara Washington dan Moskow untuk urusan mendesak yang dipasang setelah Krisis Rudal Kuba. Teknologi untuk hotline telah berubah seiring berjalannya waktu. Saat ini, itu mencakup kabel serat optik langsung serta dua tautan satelit (untuk redundansi), yang memungkinkan e-mail dan pesan teks. Tautan berakhir di berbagai tempat di AS. Pentagon, Gedung Putih, dan Gunung Raven Rock adalah titik akhir yang diketahui. Bertentangan dengan opini populer, hotline tidak pernah melibatkan telepon.

Pada intinya, skema one-time pad bekerja sebagai berikut. Baik Washington dan Moskow akan memiliki dua set angka acak. Satu set angka acak, dibuat oleh Rusia, berkaitan dengan enkripsi dan dekripsi pesan dalam bahasa Rusia. Satu set angka acak, dibuat oleh Amerika, berkaitan dengan enkripsi dan dekripsi pesan dalam bahasa Inggris. Dari waktu ke waktu, lebih banyak angka acak akan dikirimkan ke pihak lain oleh kurir yang dipercaya.

Washington dan Moskow kemudian, dapat berkomunikasi secara rahasia dengan menggunakan angka acak ini untuk membuat one-time pads. Setiap kali Anda perlu berkomunikasi, Anda akan menggunakan bagian angka acak berikutnya untuk pesan Anda.

Meskipun sangat aman, one-time pad menghadapi batasan praktis yang signifikan: kunci harus sepanjang pesan dan tidak ada bagian dari one-time pad yang dapat digunakan kembali. Ini berarti bahwa Anda perlu melacak di mana Anda berada dalam one-time pad, menyimpan sejumlah besar bit, dan bertukar bit acak dengan pihak lawan dari waktu ke waktu. Akibatnya, one-time pad tidak sering digunakan dalam praktik.

Sebaliknya, sandi aliran pseudorandom yang dominan digunakan dalam praktik adalah **sandi aliran pseudorandom**. Salsa20 dan varian yang sangat terkait yang disebut ChaCha adalah contoh sandi aliran pseudorandom yang umum digunakan.

Dengan sandi aliran pseudorandom ini, Anda pertama-tama secara acak memilih kunci K yang lebih pendek dari panjang teks asli. Kunci acak K seperti itu biasanya dibuat oleh komputer kita berdasarkan data yang tidak dapat diprediksi yang dikumpulkannya dari waktu ke waktu, seperti waktu antara pesan jaringan, gerakan mouse, dan sebagainya.
Kunci acak K kemudian dimasukkan ke dalam algoritma ekspansi yang menciptakan aliran kunci pseudorandom sepanjang pesan. Anda dapat menentukan dengan tepat seberapa panjang aliran kunci yang dibutuhkan (misalnya, 500 bit, 1000 bit, 1200 bit, 29.117 bit, dan seterusnya).
Aliran kunci pseudorandom tampak *seolah-olah* dipilih secara acak dari semua rangkaian dengan panjang yang sama. Oleh karena itu, enkripsi dengan aliran kunci pseudorandom tampak seolah-olah telah dilakukan dengan one-time pad. Namun, tentu saja, hal itu tidak benar.

Karena kunci privat kita lebih pendek dari aliran kunci dan algoritma ekspansioner kita perlu deterministik agar proses enkripsi/dekripsi dapat berfungsi, tidak setiap aliran kunci dengan panjang tertentu dapat dihasilkan sebagai output dari operasi ekspansioner kita.

Misalkan, contohnya, kunci privat kita memiliki panjang 128 bit dan kita dapat memasukkannya ke dalam algoritma ekspansioner untuk menciptakan aliran kunci yang jauh lebih panjang, katakanlah 2.500 bit. Karena algoritma ekspansioner kita perlu deterministik, algoritma kita paling banyak dapat memilih 1/2<sup>128</sup> rangkaian dengan panjang 2.500 bit. Jadi aliran kunci seperti itu tidak pernah bisa dipilih sepenuhnya secara acak dari semua rangkaian dengan panjang yang sama.

Definisi kita tentang cipher aliran memiliki dua aspek: (1) aliran kunci sepanjang teks asli dihasilkan dengan bantuan kunci privat; dan (2) aliran kunci ini digabungkan dengan teks asli, biasanya melalui operasi XOR, untuk menghasilkan teks tersandi.

Terkadang orang mendefinisikan kondisi (1) lebih ketat, dengan menyatakan bahwa aliran kunci harus secara spesifik pseudorandom. Ini berarti bahwa baik cipher pergeseran maupun one-time pad tidak akan dianggap sebagai cipher aliran.

Menurut pandangan saya, mendefinisikan kondisi (1) lebih luas memberikan cara yang lebih mudah untuk mengorganisir skema enkripsi. Selain itu, ini berarti kita tidak harus berhenti menyebut skema enkripsi tertentu sebagai cipher aliran hanya karena kita mengetahui bahwa sebenarnya tidak mengandalkan aliran kunci pseudorandom.

## Block ciphers
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Cara pertama yang umumnya dipahami sebagai **block cipher** adalah sebagai sesuatu yang lebih primitif dari cipher aliran: Algoritma inti yang melakukan transformasi yang mempertahankan panjang pada rangkaian dengan panjang yang sesuai dengan bantuan kunci. Algoritma ini dapat digunakan untuk menciptakan skema enkripsi dan mungkin juga jenis skema kriptografi lainnya.

Seringkali, block cipher dapat mengambil rangkaian input dengan panjang yang bervariasi seperti 64, 128, atau 256 bit, serta kunci dengan panjang yang bervariasi seperti 128, 192, atau 256 bit. Meskipun beberapa detail dari algoritma mungkin berubah tergantung pada variabel ini, algoritma inti tidak berubah. Jika berubah, kita akan berbicara tentang dua block cipher yang berbeda. Perhatikan bahwa penggunaan terminologi algoritma inti di sini sama seperti untuk skema enkripsi.

Penggambaran tentang cara kerja block cipher dapat dilihat di *Gambar 4* di bawah ini. Pesan M dengan panjang L dan kunci K berfungsi sebagai input untuk Block cipher. Ini menghasilkan pesan M’ dengan panjang L. Kunci tidak harus memiliki panjang yang sama dengan M dan M’ untuk sebagian besar block cipher.

*Gambar 4: Sebuah block cipher*

![Gambar 4: Sebuah block cipher](assets/Figure4-4.webp "Gambar 4: Sebuah block cipher")
Sebuah cipher blok sendirian bukanlah skema enkripsi. Namun, sebuah cipher blok dapat digunakan dengan berbagai **mode operasi** untuk menghasilkan skema enkripsi yang berbeda. Mode operasi hanya menambahkan beberapa operasi tambahan di luar cipher blok.

Untuk mengilustrasikan bagaimana ini bekerja, anggap sebuah cipher blok (BC) yang memerlukan string input 128-bit dan kunci privat 128-bit. Gambar 5 di bawah ini menunjukkan bagaimana cipher blok tersebut dapat digunakan dengan **mode buku kode elektronik** (**mode ECB**) untuk menciptakan skema enkripsi. (Titik-titik di sebelah kanan menunjukkan bahwa Anda dapat mengulangi pola ini sepanjang yang diperlukan).

*Gambar 5: Sebuah cipher blok dengan mode ECB*

![Gambar 5: Sebuah cipher blok dengan mode ECB](assets/Figure4-5.webp "Gambar 5: Sebuah cipher blok dengan mode ECB")

Proses untuk enkripsi buku kode elektronik dengan cipher blok adalah sebagai berikut. Lihat apakah Anda dapat membagi pesan teks Anda menjadi blok 128-bit. Jika tidak, tambahkan **padding** ke pesan, sehingga hasilnya dapat dibagi rata dengan ukuran blok 128 bit. Ini adalah data Anda yang digunakan untuk proses enkripsi.

Sekarang bagi data menjadi potongan string 128-bit (M<sub>1</sub>, M<sub>2</sub>, M<sub>3</sub>, dan seterusnya). Jalankan setiap string 128-bit melalui cipher blok dengan kunci 128-bit Anda untuk menghasilkan potongan ciphertext 128-bit (C<sub>1</sub>, C<sub>2</sub>, C<sub>3</sub>, dan seterusnya). Potongan-potongan ini digabungkan kembali membentuk ciphertext lengkap.

Dekripsi hanyalah proses terbalik, meskipun penerima memerlukan cara yang dapat dikenali untuk menghilangkan padding apa pun dari data yang didekripsi untuk menghasilkan pesan teks asli.

Meskipun relatif sederhana, sebuah cipher blok dengan mode buku kode elektronik kekurangan dalam keamanan. Ini karena mengarah ke **enkripsi deterministik**. Dua string data 128-bit yang identik dienkripsi dengan cara yang sama persis. Informasi tersebut dapat dimanfaatkan.

Sebaliknya, setiap skema enkripsi yang dibangun dari cipher blok seharusnya **probabilistik**: yaitu, enkripsi dari pesan M apa pun, atau potongan spesifik dari M, seharusnya umumnya menghasilkan hasil yang berbeda setiap kali.<sup>[5](#footnote5)</sup>

**Mode penggabungan blok cipher** (**mode CBC**) mungkin adalah mode yang paling umum digunakan dengan cipher blok. Kombinasi, jika dilakukan dengan benar, menghasilkan skema enkripsi probabilistik. Anda dapat melihat gambaran dari mode operasi ini di Gambar 6 di bawah ini.

*Gambar 6: Sebuah cipher blok dengan mode CBC*

![Gambar 6: Sebuah cipher blok dengan mode CBC](assets/Figure4-6.webp "Gambar 6: Sebuah cipher blok dengan mode CBC")

Anggap ukuran bloknya lagi-lagi 128 bit. Jadi untuk memulai, Anda sekali lagi perlu memastikan bahwa pesan teks asli Anda menerima padding yang diperlukan.

Kemudian, Anda XOR bagian 128-bit pertama dari teks Anda dengan **vektor inisialisasi** 128-bit. Hasilnya dimasukkan ke dalam cipher blok untuk menghasilkan ciphertext untuk blok pertama. Untuk blok kedua dari 128 bit, Anda pertama-tama XOR teks dengan ciphertext dari blok pertama, sebelum memasukkannya ke dalam cipher blok. Anda melanjutkan proses ini sampai Anda telah mengenkripsi seluruh pesan teks Anda.

Ketika selesai, Anda mengirim pesan yang dienkripsi bersama dengan vektor inisialisasi yang tidak dienkripsi ke penerima. Penerima perlu mengetahui vektor inisialisasi, jika tidak, dia tidak dapat mendekripsi ciphertext.
Konstruksi ini jauh lebih aman daripada mode buku kode elektronik ketika digunakan dengan benar. Pertama-tama, Anda harus memastikan bahwa vektor inisialisasi adalah string acak atau semuacak. Selain itu, Anda harus menggunakan vektor inisialisasi yang berbeda setiap kali Anda menggunakan skema enkripsi ini.
Dengan kata lain, vektor inisialisasi Anda harus menjadi nonce acak atau semuacak, di mana **nonce** berarti "angka yang hanya digunakan sekali." Jika Anda menjaga praktik ini, maka mode CBC dengan cipher blok memastikan bahwa dua blok teks biasa yang identik umumnya akan dienkripsi secara berbeda setiap kali.

Akhirnya, mari kita alihkan perhatian kita ke **mode umpan balik keluaran** (**OFB mode**). Anda dapat melihat gambaran mode ini di *Gambar 7*.

*Gambar 7: Cipher blok dengan mode OFB*

![Gambar 7: Cipher blok dengan mode OFB](assets/Figure4-7.webp "Gambar 7: Cipher blok dengan mode OFB")

Dengan mode OFB, Anda juga memilih vektor inisialisasi. Namun, di sini, untuk blok pertama, vektor inisialisasi langsung dimasukkan ke dalam cipher blok dengan kunci Anda. 128-bit yang dihasilkan, kemudian, dianggap sebagai aliran kunci. Aliran kunci ini di-XOR dengan teks biasa untuk menghasilkan teks terenkripsi untuk blok tersebut. Untuk blok selanjutnya, Anda menggunakan aliran kunci dari blok sebelumnya sebagai input ke dalam cipher blok dan mengulangi langkah-langkah tersebut.

Jika Anda melihat dengan seksama, apa yang sebenarnya telah diciptakan di sini dari cipher blok dengan mode OFB adalah cipher aliran. Anda menghasilkan bagian aliran kunci sebesar 128-bit sampai Anda memiliki panjang teks biasa (membuang bit yang tidak Anda butuhkan dari bagian aliran kunci 128-bit terakhir). Kemudian, Anda XOR aliran kunci dengan pesan teks biasa Anda untuk mendapatkan teks terenkripsi.

Di bagian sebelumnya tentang cipher aliran, saya menyatakan bahwa Anda menghasilkan aliran kunci dengan bantuan kunci privat. Untuk lebih tepatnya, tidak hanya harus diciptakan dengan kunci privat. Seperti yang Anda lihat dalam mode OFB, aliran kunci dihasilkan dengan dukungan baik kunci privat maupun vektor inisialisasi.

Perhatikan bahwa seperti dengan mode CBC, penting untuk memilih nonce semuacak atau acak untuk vektor inisialisasi setiap kali Anda menggunakan cipher blok dalam mode OFB. Jika tidak, string pesan 128-bit yang sama yang dikirim dalam komunikasi yang berbeda akan dienkripsi dengan cara yang sama. Ini adalah salah satu cara untuk menciptakan enkripsi probabilistik dengan cipher aliran.

Beberapa cipher aliran hanya menggunakan kunci privat untuk membuat aliran kunci. Untuk cipher aliran tersebut, penting bagi Anda untuk menggunakan nonce acak untuk memilih kunci privat untuk setiap instansi komunikasi. Jika tidak, hasil enkripsi dengan cipher aliran tersebut juga akan deterministik, yang mengarah pada masalah keamanan.

Cipher blok modern yang paling populer adalah **cipher Rijndael**. Ini adalah entri pemenang dari lima belas pengajuan ke kompetisi yang diadakan oleh National Institute of Standards and Technology (NIST) antara tahun 1997 dan 2000 untuk menggantikan standar enkripsi yang lebih tua, **data encryption standard** (**DES**).
Sandi Rijndael dapat digunakan dengan spesifikasi yang berbeda untuk panjang kunci dan ukuran blok, serta dalam berbagai mode operasi. Komite untuk kompetisi NIST mengadopsi versi terbatas dari sandi Rijndael—yaitu yang memerlukan ukuran blok 128-bit dan panjang kunci baik 128 bit, 192 bit, atau 256 bit—sebagai bagian dari **standar enkripsi lanjutan** (**AES**). Ini benar-benar standar utama untuk aplikasi enkripsi simetris. Ini sangat aman sehingga bahkan NSA tampaknya bersedia menggunakannya dengan kunci 256-bit untuk dokumen rahasia tingkat tinggi.<sup>[6](#footnote6)</sup>
Sandi blok AES akan dijelaskan secara detail di *Bab 5*.

## Mengklarifikasi kebingungan
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Kebingungan tentang perbedaan antara sandi blok dan sandi aliran muncul karena terkadang orang akan memahami istilah sandi blok sebagai merujuk khusus pada *sandi blok dengan mode enkripsi blok*.

Pertimbangkan mode ECB dan CBC di bagian sebelumnya. Ini secara khusus memerlukan data untuk enkripsi yang dapat dibagi oleh ukuran blok (berarti Anda mungkin harus menggunakan padding untuk pesan asli). Selain itu, data dalam mode ini juga dioperasikan langsung oleh sandi blok (dan tidak hanya dikombinasikan dengan hasil operasi sandi blok seperti dalam mode OFB).

Oleh karena itu, sebagai alternatif, Anda dapat mendefinisikan **sandi blok** sebagai skema enkripsi apa pun, yang beroperasi pada blok pesan berukuran tetap setiap saat (di mana setiap blok harus lebih panjang dari satu byte, jika tidak, itu berubah menjadi sandi aliran). Baik data untuk enkripsi maupun ciphertext harus dibagi rata ke dalam ukuran blok ini. Biasanya, ukuran blok adalah 64, 128, 192, atau 256 bit panjangnya. Sebaliknya, sandi aliran dapat mengenkripsi pesan apa pun dalam potongan satu bit atau byte setiap saat.

Dengan pemahaman yang lebih spesifik tentang sandi blok ini, Anda memang dapat menyatakan bahwa skema enkripsi modern adalah sandi aliran atau sandi blok. Dari sini ke depan, saya akan menggunakan istilah sandi blok dalam pengertian yang lebih umum kecuali dinyatakan lain.

Diskusi tentang mode OFB di bagian sebelumnya juga mengangkat poin menarik lainnya. Beberapa sandi aliran dibuat dari sandi blok, seperti Rijndael dengan OFB. Beberapa seperti Salsa20 dan ChaCha tidak dibuat dari sandi blok. Anda mungkin menyebut yang terakhir sebagai **sandi aliran primitif**. (Tidak benar-benar ada istilah standar untuk merujuk pada jenis sandi aliran ini.)

Ketika orang berbicara tentang kelebihan dan kekurangan sandi aliran dan sandi blok, mereka biasanya membandingkan sandi aliran primitif dengan skema enkripsi berbasis sandi blok.

Meskipun Anda selalu dapat dengan mudah membangun sandi aliran dari sandi blok, biasanya sangat sulit untuk membangun beberapa jenis konstruksi dengan mode enkripsi blok (seperti dengan mode CBC) dari sandi aliran primitif.

Dari diskusi ini, Anda sekarang harus memahami *Gambar 8*. Ini memberikan gambaran umum tentang skema enkripsi simetris. Kami menggunakan tiga jenis skema enkripsi: sandi aliran primitif, sandi aliran sandi blok, dan sandi blok dalam mode blok (juga disebut "sandi blok" dalam diagram).

*Gambar 8: Gambaran umum skema enkripsi simetris*

![Gambar 8: Gambaran umum skema enkripsi simetris](assets/Figure4-8.webp "Gambar 8: Gambaran umum skema enkripsi simetris")

## Kode autentikasi pesan
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>
Enkripsi berkaitan dengan kerahasiaan. Namun, kriptografi juga berkaitan dengan tema yang lebih luas, seperti integritas pesan, keaslian, dan non-repudiasi. Yang disebut **kode otentikasi pesan** (MACs) adalah skema kriptografi kunci simetris yang mendukung keaslian dan integritas dalam komunikasi.

Mengapa sesuatu selain kerahasiaan diperlukan dalam komunikasi? Misalkan Bob mengirim Alice sebuah pesan menggunakan enkripsi yang praktis tidak bisa dipecahkan. Penyerang mana pun yang mencegat pesan ini tidak akan dapat memperoleh wawasan yang signifikan mengenai isi pesannya. Namun, penyerang masih memiliki setidaknya dua vektor serangan lain yang tersedia untuknya:

1. Dia bisa mencegat ciphertext, mengubah isinya, dan mengirimkan ciphertext yang telah diubah tersebut kepada Alice.
2. Dia bisa memblokir pesan Bob sepenuhnya dan mengirimkan ciphertext buatannya sendiri.

Dalam kedua kasus ini, penyerang mungkin tidak memiliki wawasan apa pun tentang isi dari ciphertext (1) dan (2). Namun, dia masih bisa menyebabkan kerusakan yang signifikan dengan cara ini. Inilah mengapa kode otentikasi pesan menjadi penting.

Kode otentikasi pesan didefinisikan secara longgar sebagai skema kriptografi simetris dengan tiga algoritma: algoritma generasi kunci, algoritma generasi tag, dan algoritma verifikasi. MAC yang aman memastikan bahwa tag adalah **existentially unforgeable** bagi penyerang mana pun—yaitu, mereka tidak dapat berhasil membuat tag pada pesan yang diverifikasi, kecuali mereka memiliki kunci privat.

Bob dan Alice dapat melawan manipulasi pesan tertentu menggunakan MAC. Misalkan untuk saat ini mereka tidak peduli tentang kerahasiaan. Mereka hanya ingin memastikan bahwa pesan yang diterima oleh Alice memang dari Bob dan tidak diubah dengan cara apa pun.

Proses ini digambarkan dalam *Gambar 9*. Untuk menggunakan MAC, mereka pertama-tama akan menghasilkan kunci privat K yang dibagi antara mereka berdua. Bob membuat tag T untuk pesan menggunakan kunci privat K. Kemudian, dia mengirim pesan serta tag pesan kepada Alice. Dia kemudian dapat memverifikasi bahwa Bob memang membuat tag tersebut, dengan menjalankan kunci privat, pesan, dan tag melalui algoritma verifikasi.

*Gambar 9: Ikhtisar skema enkripsi simetris*

![Gambar 9: Ikhtisar skema enkripsi simetris](assets/Figure4-9.webp "Gambar 9: Ikhtisar skema enkripsi simetris")

Karena keunforgeability eksistensial, penyerang tidak dapat mengubah pesan M dengan cara apa pun atau membuat pesan sendiri dengan tag yang valid. Ini berlaku, bahkan jika penyerang mengamati tag dari banyak pesan antara Bob dan Alice yang menggunakan kunci privat yang sama. Paling banyak, penyerang bisa memblokir Alice dari menerima pesan M (masalah yang tidak dapat diatasi oleh kriptografi).

MAC menjamin bahwa pesan sebenarnya dibuat oleh Bob. Keaslian ini, secara otomatis menyiratkan integritas pesan—yaitu, jika Bob telah membuat pesan tertentu, maka, ipso facto, itu tidak diubah dengan cara apa pun oleh penyerang. Jadi dari sini ke depan, setiap kekhawatiran untuk otentikasi harus secara otomatis dipahami untuk menyiratkan kekhawatiran untuk integritas.

Sementara saya telah membuat perbedaan antara keaslian pesan dan integritas dalam diskusi saya, juga umum untuk menggunakan istilah tersebut sebagai sinonim. Mereka kemudian merujuk pada ide pesan yang dibuat oleh pengirim tertentu dan tidak diubah dengan cara apa pun. Dalam semangat ini, kode otentikasi pesan sering juga disebut **kode integritas pesan**.


## Enkripsi Terotentikasi
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>
Biasanya, Anda ingin menjamin baik kerahasiaan maupun keaslian dalam komunikasi, dan oleh karena itu, skema enkripsi dan skema MAC biasanya digunakan bersama-sama. **Skema enkripsi terotentikasi** adalah skema yang menggabungkan enkripsi dengan MAC secara sangat aman. Secara spesifik, skema ini harus memenuhi standar untuk ketidakmampuan pemalsuan eksistensial serta konsep kerahasiaan yang sangat kuat, yaitu yang tahan terhadap **serangan teks sandi terpilih**.<sup>[7](#footnote7)</sup>

Agar skema enkripsi tahan terhadap serangan teks sandi terpilih, skema tersebut harus memenuhi standar untuk **non-malleability**: yaitu, setiap modifikasi teks sandi oleh penyerang harus menghasilkan teks sandi yang tidak valid atau teks sandi yang didekripsi menjadi teks biasa yang tidak memiliki hubungan dengan teks asli.<sup>[8](#footnote8)</sup>

Karena skema enkripsi terotentikasi memastikan bahwa teks sandi yang dibuat oleh penyerang selalu tidak valid (karena tag tidak akan diverifikasi), skema ini memenuhi standar untuk ketahanan terhadap serangan teks sandi terpilih. Menariknya, Anda dapat membuktikan bahwa skema enkripsi terotentikasi selalu dapat dibuat dari kombinasi MAC yang tidak dapat dipalsukan secara eksistensial dan skema enkripsi yang memenuhi konsep keamanan yang kurang kuat, yang dikenal sebagai **keamanan serangan teks biasa terpilih**.

Kita tidak akan membahas semua detail tentang pembuatan skema enkripsi terotentikasi. Namun, penting untuk mengetahui dua detail dari konstruksinya.

Pertama, skema enkripsi terotentikasi pertama-tama menangani enkripsi dan kemudian membuat tag pesan pada teks sandi. Ternyata, pendekatan lain—seperti menggabungkan teks sandi dengan tag pada teks biasa, atau pertama-tama membuat tag dan kemudian mengenkripsi baik teks biasa maupun tag—tidak aman. Selain itu, kedua operasi memiliki kunci privat yang dipilih secara acak sendiri-sendiri, jika tidak keamanan Anda akan sangat terkompromi.

Prinsip yang disebutkan di atas berlaku lebih umum: *Anda harus selalu menggunakan kunci yang berbeda ketika menggabungkan skema kriptografi dasar*.

Skema enkripsi terotentikasi digambarkan dalam *Gambar 10*. Bob pertama-tama membuat teks sandi C dari pesan M menggunakan kunci K<sub>C</sub> yang dipilih secara acak. Kemudian, dia membuat tag pesan T dengan menjalankan teks sandi dan kunci yang berbeda K<sub>T</sub> yang dipilih secara acak melalui algoritma pembuatan tag. Baik teks sandi maupun tag pesan dikirimkan kepada Alice.

Alice sekarang pertama-tama memeriksa apakah tag valid dengan teks sandi C dan kunci K<sub>T</sub>. Jika valid, dia kemudian dapat mendekripsi pesan menggunakan kunci K<sub>C</sub>. Tidak hanya dia yakin akan konsep kerahasiaan yang sangat kuat dalam komunikasi mereka, dia juga tahu pesan tersebut dibuat oleh Bob.

*Gambar 10: Skema enkripsi terotentikasi*

![Gambar 10: Skema enkripsi terotentikasi](assets/Figure4-10.webp "Gambar 10: Skema enkripsi terotentikasi")

Bagaimana MAC dibuat? Meskipun MAC dapat dibuat melalui berbagai metode, cara yang umum dan efisien untuk membuatnya adalah melalui fungsi hash kriptografi.

Kita akan memperkenalkan fungsi hash kriptografi lebih mendalam di *Bab 6*. Untuk sekarang, cukup ketahui bahwa **fungsi hash** adalah fungsi yang dapat dihitung secara efisien yang mengambil input berukuran sembarang dan menghasilkan output berukuran tetap. Sebagai contoh, fungsi hash populer **SHA-256** (secure hash algorithm 256) selalu menghasilkan output 256-bit terlepas dari ukuran input. Beberapa fungsi hash, seperti SHA-256, memiliki aplikasi yang berguna dalam kriptografi.
Jenis tag yang paling umum dihasilkan dengan fungsi hash kriptografis adalah **hash-based message authentication code** (HMAC). Proses ini digambarkan dalam *Gambar 11*. Sebuah pihak menghasilkan dua kunci berbeda dari kunci privat K, kunci dalam K<sub>1</sub> dan kunci luar K<sub>2</sub>. Teks asli M atau teks tersandi C, kemudian, di-hash bersama dengan kunci dalam. Hasil T' ini, kemudian, di-hash dengan kunci luar untuk menghasilkan tag pesan T.
Ada palet fungsi hash yang dapat digunakan untuk membuat HMAC. Fungsi hash yang paling sering digunakan adalah SHA-256.

*Gambar 11: HMAC*

![Gambar 11: HMAC](assets/Figure4-11.webp "Gambar 11: HMAC")

## Sesi komunikasi yang aman
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Bayangkan dua pihak berada dalam sesi komunikasi, sehingga mereka mengirimkan banyak pesan bolak-balik.

Skema enkripsi terotentikasi memungkinkan penerima pesan untuk memverifikasi bahwa pesan tersebut dibuat oleh pasangannya dalam sesi komunikasi (selama kunci privat tidak bocor). Ini bekerja cukup baik untuk satu pesan. Biasanya, namun, dua pihak mengirim pesan bolak-balik dalam sesi komunikasi. Dan dalam pengaturan tersebut, skema enkripsi terotentikasi biasa seperti yang dijelaskan di bagian sebelumnya kurang dalam memberikan keamanan.

Alasan utamanya adalah skema enkripsi terotentikasi tidak memberikan jaminan bahwa pesan tersebut sebenarnya juga dikirim oleh agen yang menciptakannya dalam sesi komunikasi. Pertimbangkan tiga vektor serangan berikut:

1. **Serangan ulang**: Seorang penyerang mengirim ulang ciphertext dan tag yang dia tangkap antara dua pihak pada titik sebelumnya.
2. **Serangan pengurutan ulang**: Seorang penyerang menangkap dua pesan pada waktu yang berbeda, dan mengirimkannya kepada penerima dalam urutan terbalik.
3. **Serangan refleksi**: Seorang penyerang mengamati pesan yang dikirim dari A ke B, dan juga mengirim pesan itu ke A.

Meskipun penyerang tidak memiliki pengetahuan tentang ciphertext dan tidak dapat membuat ciphertext palsu, serangan di atas masih dapat menyebabkan kerusakan signifikan dalam komunikasi.

Bayangkan, misalnya, bahwa pesan tertentu antara dua pihak melibatkan transfer dana keuangan. Serangan ulang mungkin mentransfer dana untuk kedua kalinya. Skema enkripsi terotentikasi vanilla tidak memiliki pertahanan terhadap serangan semacam itu.

Untungnya, jenis serangan ini dapat dengan mudah diminimalisir dalam sesi komunikasi menggunakan **identifier** dan **indikator waktu relatif**.

Identifier dapat ditambahkan ke pesan teks asli sebelum enkripsi. Ini akan menghalangi serangan refleksi. Indikator waktu relatif bisa, misalnya, menjadi nomor urut dalam sesi komunikasi tertentu. Setiap pihak menambahkan nomor urut ke pesan sebelum enkripsi, sehingga penerima tahu dalam urutan apa pesan tersebut dikirim. Ini menghilangkan kemungkinan serangan pengurutan ulang. Ini juga menghilangkan serangan ulang. Setiap pesan yang dikirim penyerang nantinya akan memiliki nomor urut lama, dan penerima akan tahu untuk tidak memproses pesan lagi.

Untuk mengilustrasikan bagaimana sesi komunikasi yang aman bekerja, bayangkan lagi Alice dan Bob. Mereka mengirim total empat pesan bolak-balik. Anda dapat melihat bagaimana skema enkripsi terotentikasi dengan identifier dan nomor urut bekerja di bawah ini dalam *Gambar 11*.
Sesi komunikasi dimulai dengan Bob mengirimkan sebuah ciphertext C<sub>0,B</sub> kepada Alice dengan sebuah tag pesan T<sub>0,B</sub>. Ciphertext tersebut berisi pesan, serta sebuah identifikasi (BOB) dan nomor urut (0). Tag T<sub>0,B</sub> dibuat untuk seluruh ciphertext. Dalam komunikasi berikutnya, Alice dan Bob mempertahankan protokol ini, memperbarui field sesuai kebutuhan.
*Gambar 12: Sesi komunikasi yang aman*

![Gambar 12: Sesi komunikasi yang aman](assets/Figure4-12.webp "Gambar 12: Sesi komunikasi yang aman")


## Catatan
<chapterId>b96d38dd-c9cb-56a7-8764-4af8526bc63f</chapterId>

[^1]: Menurut Seutonius, sebuah shift cipher dengan nilai kunci konstan 3 digunakan oleh Julius Caesar dalam komunikasi militer. Jadi A akan selalu menjadi D, B selalu E, C selalu F, dan seterusnya. Versi khusus dari Shift cipher ini, dengan demikian, menjadi dikenal sebagai **Caesar Cipher** (meskipun sebenarnya bukan cipher dalam pengertian modern kata, karena nilai kunci konstan). Caesar cipher mungkin aman pada abad pertama SM, jika musuh-musuh Roma sangat tidak familiar dengan enkripsi. Tapi jelas tidak akan menjadi skema yang sangat aman di zaman modern [^1].

[^2]: Jonathan Katz dan Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), hlm. 7f [^2].

[^3]: Eric Raymond, “The Cathedral and the Bazaar,” makalah disajikan pada Linux Kongress, Würzburg, Jerman (27 Mei 1997). Ada sejumlah versi berikutnya yang tersedia serta sebuah buku. Kutipan saya berasal dari halaman 30 dalam buku: Eric Raymond, *The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary*, edisi revisi. (2001), O’Reilly: Sebastopol, CA [^3].

[^4]: Crypto Museum, "Washington-Moscow hotline," 2013, tersedia di [Crypto Museum](https://www.cryptomuseum.com/crypto/hotline/index.htm) [^4].

[^5]: Pentingnya enkripsi probabilistik pertama kali ditekankan oleh Shafi Goldwasser dan Silvio Micali, “Probabilistic encryption,” *Journal of Co [^5].

# RC4 dan AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

Dalam Bab ini, kita akan membahas detail dari sebuah skema enkripsi dengan cipher stream primitif modern, RC4 (atau "Rivest cipher 4"), dan sebuah block cipher modern, AES. Meskipun cipher RC4 telah jatuh dalam ketidakpopuleran sebagai metode enkripsi, AES adalah standar untuk enkripsi simetris modern. Dua contoh ini harus memberikan gambaran yang lebih baik tentang bagaimana enkripsi simetris bekerja secara internal.

## Cipher stream RC4
<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>
Untuk memahami bagaimana cara kerja cipher stream pseudorandom modern, saya akan fokus pada cipher stream RC4. Ini adalah cipher stream pseudorandom yang digunakan dalam protokol keamanan titik akses nirkabel WEP dan WAP serta dalam TLS. Karena RC4 memiliki banyak kelemahan yang terbukti, cipher ini menjadi tidak disukai. Bahkan, Internet Engineering Task Force sekarang melarang penggunaan suite RC4 oleh aplikasi klien dan server dalam semua instansi TLS.<sup>[3](#footnote3)</sup> Namun, ini berfungsi dengan baik sebagai contoh untuk mengilustrasikan bagaimana cipher stream primitif bekerja.
Untuk memulai, saya akan pertama-tama menunjukkan cara mengenkripsi pesan teks biasa dengan cipher RC4 versi sederhana. Misalkan pesan teks biasa kita adalah "SOUP." Enkripsi dengan cipher RC4 versi sederhana kita, kemudian, berlangsung dalam empat langkah.

### Langkah 1

Pertama, definisikan sebuah array S dengan S[0] = 0 hingga S[7] = 7. Array di sini hanya berarti kumpulan nilai yang dapat diubah yang disusun oleh indeks, juga disebut daftar dalam beberapa bahasa pemrograman (misalnya, Python). Dalam kasus ini, indeks berjalan dari 0 hingga 7, dan nilai-nilainya juga berjalan dari 0 hingga 7. Jadi S adalah sebagai berikut:

- S = [0,1,2,3,4,5,6,7]

Nilai di sini bukanlah angka ASCII, tetapi representasi nilai desimal dari string 1 byte. Jadi nilai 2 akan sama dengan 0000 0011. Panjang array S adalah, dengan demikian, 8 byte.

### Langkah 2

Kedua, definisikan sebuah array kunci K dengan panjang 8 byte dengan memilih kunci antara 1 dan 8 byte (tanpa pecahan byte yang diizinkan). Karena setiap byte adalah 8 bit, Anda dapat memilih angka apa saja antara 0 dan 255 untuk setiap byte dari kunci Anda.

Misalkan kita memilih kunci kita k sebagai [14,48,9], sehingga memiliki panjang 3 byte. Setiap indeks dari array kunci kita, kemudian, ditetapkan sesuai dengan nilai desimal untuk elemen kunci tertentu tersebut, secara berurutan. Jika Anda menjalankan seluruh kunci, mulai lagi dari awal, sampai Anda telah mengisi 8 slot dari array kunci. Oleh karena itu, array kunci kita adalah sebagai berikut

- K = [14,48,9,14,48,9,14,48]

### Langkah 3

Ketiga, kita akan mentransformasi array S menggunakan array kunci K, dalam proses yang dikenal sebagai penjadwalan kunci. Prosesnya adalah sebagai berikut dalam pseudocode:

- Buat variabel j dan i
- Setel variabel j = 0
- Untuk setiap i dari 0 hingga 7:
	- Setel j = j + S[i] + K[i] mod 8
	- Tukar S[i] dan S[j]

Transformasi array S ditangkap oleh *Tabel 1*.

Untuk memulai, Anda dapat melihat keadaan awal S sebagai [0,1,2,3,4,5,6,7] dengan nilai awal 0 untuk j. Ini akan ditransformasi menggunakan array kunci [14,48,9,14,48,9,14,48].
Perulangan for dimulai dengan i = 0. Menurut pseudocode di atas, nilai baru dari j menjadi 6 (j = j + S[0] + K[0] mod 8 = 0 + 0 + 14 mod 8 = 6 mod 8). Menukar S[0] dan S[6], keadaan S setelah 1 ronde menjadi [6,1,2,3,4,5,0,7]. 
Pada baris selanjutnya, i = 1. Melalui perulangan for lagi, j mendapatkan nilai 7 (j = j + S[1] + K[1] mod 8 = 6 + 1 + 48 mod 8 = 55 mod 8 = 7 mod 8). Menukar S[1] dan S[7] dari keadaan S saat ini, [6,1,2,3,4,5,0,7], menghasilkan [6,7,2,3,4,5,0,1] setelah ronde 2.

Kita melanjutkan proses ini sampai kita menghasilkan baris akhir di bagian bawah untuk array S, [6,4,1,0,3,7,5,2].

*Tabel 1: Tabel penjadwalan kunci*

![Tabel 1: Tabel penjadwalan kunci](assets/Table5-1.webp "Tabel 1: Tabel penjadwalan kunci")

### Langkah 4

Sebagai langkah keempat, kita menghasilkan keystream. Ini adalah string pseudorandom dengan panjang yang sama dengan pesan yang ingin kita kirim. Ini yang akan digunakan untuk mengenkripsi pesan asli "SOUP." Karena keystream perlu sepanjang pesan, kita memerlukan satu yang memiliki 4 byte.

Keystream dihasilkan oleh pseudocode berikut:

- Buat variabel j, i, dan t
- Tetapkan j = 0
- Untuk setiap i dari plaintext, dimulai dengan i = 1 dan berlanjut sampai i = 4, setiap byte dari keystream dihasilkan sebagai berikut:
    - j = j + S[i] mod 8
	- Tukar S[i] dan S[j]
	- t = S[i] + S[j] mod 8
	- Byte ke-i dari keystream = S[t]

Anda dapat mengikuti perhitungan di *Tabel 2*.

Keadaan awal S = S = [6,4,1,0,3,7,5,2]. Menetapkan i = 1, nilai j menjadi 4 (j = j + S[i] mod 8 = 0 + 4 mod 8 = 4). Kemudian, kita menukar S[1] dan S[4] untuk menghasilkan transformasi S di baris kedua, [6,3,1,0,4,7,5,2]. Nilai t kemudian, 7 (t = S[i] + S[j] mod 8 = 3 + 4 mod 8 = 7). Akhirnya, byte untuk keystream adalah, kemudian, S[7], atau 2.

Kita kemudian, dapat melanjutkan untuk menghasilkan byte lainnya sampai kita memiliki empat byte berikut: 2, 6, 3, dan 7. Masing-masing byte ini kemudian, dapat digunakan untuk mengenkripsi setiap huruf dari plaintext, "SOUP".
Untuk memulai, menggunakan tabel ASCII, kita dapat melihat bahwa "SOUP" yang dikodekan oleh nilai desimal dari string byte yang mendasarinya adalah "83 79 85 80". Kombinasi dengan keystream "2 6 3 2" menghasilkan "85 85 88 82", yang tetap sama setelah operasi modulo 256. Dalam ASCII, ciphertext "85 85 88 82" sama dengan "UUXR".
Apa yang terjadi jika kata yang akan dienkripsi lebih panjang dari array S? Dalam kasus tersebut, array S terus bertransformasi dengan cara yang ditampilkan di atas untuk setiap byte i dari plaintext, sampai kita memiliki jumlah byte dalam keystream yang sama dengan jumlah huruf dalam plaintext.

*Tabel 2: Generasi Keystream*

![Tabel 2: Generasi Keystream](assets/Table5-2.webp "Tabel 2: Generasi Keystream")

Contoh yang baru saja kita bahas adalah versi yang disederhanakan dari cipher stream RC4. Cipher stream RC4 yang sebenarnya memiliki array S sepanjang 256 byte, bukan 8 byte, dan kunci yang bisa antara 1 dan 256 byte, bukan antara 1 dan 8 byte. Array kunci dan keystream, kemudian, semua diproduksi dengan mempertimbangkan panjang 256 byte dari array S. Perhitungan menjadi sangat lebih kompleks, tetapi prinsipnya tetap sama. Menggunakan kunci yang sama, [14,48,9], dengan cipher RC4 standar, pesan plaintext "SOUP" dienkripsi sebagai 67 02 ed df dalam format heksadesimal.

Cipher stream di mana keystream diperbarui secara independen dari pesan plaintext atau ciphertext adalah **cipher stream sinkron**. Keystream hanya bergantung pada kunci. Jelas, RC4 adalah contoh dari cipher stream sinkron, karena keystream tidak memiliki hubungan dengan plaintext atau ciphertext. Semua cipher stream primitif kami yang disebutkan di bab sebelumnya, termasuk cipher shift, cipher Vigenere, dan one-time pad, juga merupakan jenis sinkron.

Sebaliknya, **cipher stream asinkron** memiliki keystream yang diproduksi oleh baik kunci dan elemen-elemen sebelumnya dari ciphertext. Tipe cipher ini juga disebut **cipher self-synchronizing**.

Penting, keystream yang diproduksi dengan RC4 harus diperlakukan sebagai one-time pad, dan Anda tidak dapat menghasilkan keystream dengan cara yang sama persis untuk waktu berikutnya. Daripada mengubah kunci setiap waktu, solusi praktis adalah menggabungkan kunci dengan nonce untuk menghasilkan bytestream.

## AES dengan kunci 128-bit
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Seperti yang disebutkan di bab sebelumnya, National Institute of Standards and Technology (NIST) mengadakan kompetisi antara 1997 dan 2000 untuk menentukan standar enkripsi simetris baru. Cipher Rijndael ternyata menjadi entri yang menang. Nama tersebut adalah permainan kata dari nama pencipta Belgia, Vincent Rijmen en Joan Daemen.

Cipher Rijndael adalah block cipher, yang berarti ada algoritma inti, yang dapat digunakan dengan spesifikasi yang berbeda untuk panjang kunci dan ukuran blok. Anda, kemudian, dapat menggunakannya dengan mode operasi yang berbeda untuk membangun skema enkripsi.
Komite untuk kompetisi NIST mengadopsi versi terbatas dari cipher Rijndael—yaitu satu yang memerlukan ukuran blok 128-bit dan panjang kunci baik 128 bit, 192 bit, atau 256 bit—sebagai bagian dari standar enkripsi lanjutan. Versi terbatas dari cipher Rijndael ini juga dapat digunakan dalam beberapa mode operasi. Spesifikasi untuk standar ini dikenal sebagai Advanced Encryption Standard (AES).

Untuk menunjukkan bagaimana cipher Rijndael bekerja, inti dari AES, saya akan mengilustrasikan proses enkripsi dengan kunci 128-bit. Ukuran kunci memiliki dampak pada jumlah ronde yang diadakan untuk setiap blok enkripsi. Untuk kunci 128-bit, diperlukan 10 ronde. Dengan 192 bit dan 256 bit, akan ada 12 dan 14 ronde masing-masing.

Selain itu, saya akan asumsikan bahwa AES digunakan dalam mode ECB. Ini membuat penjelasan sedikit lebih mudah dan tidak masalah untuk algoritma Rijndael. Untuk memastikan, mode ECB tidak aman dalam praktik karena mengarah pada enkripsi deterministik. Mode aman yang paling sering digunakan dengan AES adalah CBC.

Mari kita sebut kunci tersebut K<sub>0</sub>. Konstruksi dengan parameter di atas, maka, terlihat seperti pada Gambar 1, di mana M<sub>i</sub> merupakan bagian dari pesan teks asli sebesar 128 bit dan C<sub>i</sub> untuk bagian dari ciphertext sebesar 128 bit. Padding ditambahkan ke teks asli untuk blok terakhir, jika teks asli tidak dapat dibagi rata oleh ukuran blok.

*Gambar 1: AES-ECB dengan kunci 128-bit*

![Gambar 1: AES-ECB dengan kunci 128-bit](assets/Figure5-1.webp "Gambar 1: AES-ECB dengan kunci 128-bit")

Setiap blok teks 128-bit melewati sepuluh ronde dalam skema enkripsi Rijndael. Ini memerlukan kunci ronde terpisah untuk setiap ronde (K<sub>1</sub> hingga K<sub>10</sub>). Ini diproduksi untuk setiap ronde dari kunci 128-bit asli K<sub>0</sub> menggunakan algoritma ekspansi kunci. Oleh karena itu, untuk setiap blok teks yang akan dienkripsi, kita akan menggunakan kunci asli K<sub>0</sub> serta sepuluh kunci ronde terpisah. Perhatikan bahwa 11 kunci yang sama ini digunakan untuk setiap blok teks asli 128-bit yang memerlukan enkripsi.

Algoritma ekspansi kunci panjang dan kompleks. Mengerjakannya memiliki sedikit manfaat didaktik. Anda dapat melihat algoritma ekspansi kunci sendiri, jika Anda mau. Setelah kunci ronde diproduksi, cipher Rijndael akan memanipulasi blok teks asli 128-bit pertama, M<sub>1</sub>, seperti terlihat pada Gambar 2. Sekarang kita akan melalui langkah-langkah ini.

*Gambar 2: Manipulasi M<sub>1</sub> dengan cipher Rijndael*

![Gambar 2: AES-ECB dengan kunci 128-bit](assets/Figure5-2.webp "Gambar 2: AES-ECB dengan kunci 128-bit")

### Ronde 0

Ronde 0 dari cipher Rijndael adalah sederhana. Sebuah array S<sub>0</sub> diproduksi oleh operasi XOR antara teks asli 128-bit dan kunci privat. Yaitu,

- S<sub>0</sub> = M<sub>1</sub> XOR K<sub>0</sub>
Pada putaran 1, array S<sub>0</sub> pertama kali digabungkan dengan kunci putaran K<sub>1</sub> menggunakan operasi XOR. Ini menghasilkan keadaan baru dari S.
Kedua, operasi substitusi byte dilakukan pada keadaan S saat ini. Ini bekerja dengan mengambil setiap byte dari array S 16-byte dan menggantinya dengan byte dari sebuah array yang disebut **Rijndael’s S-box**. Setiap byte memiliki transformasi unik, dan keadaan baru dari S dihasilkan sebagai akibatnya. Rijndael's S-box ditampilkan dalam *Gambar 3*.

*Gambar 3: Rijndael's S-Box*

![Gambar 3: Rijndael's S-Box](assets/Figure5-3.webp "Gambar 3: Rijndael's S-Box")

S-Box ini adalah salah satu tempat di mana aljabar abstrak berperan dalam cipher Rijndael, khususnya lapangan Galois.

Untuk memulai, Anda mendefinisikan setiap elemen byte yang mungkin dari 00 hingga FF sebagai vektor 8-bit. Setiap vektor tersebut adalah elemen dari lapangan Galois GF(2<sup>8</sup>) di mana polinomial tak tereduksi untuk operasi modulo adalah x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Lapangan Galois dengan spesifikasi ini juga disebut Lapangan Hingga Rijndael.

Selanjutnya, untuk setiap elemen yang mungkin di lapangan, kita membuat apa yang disebut **Nyberg S-Box**. Dalam kotak ini, setiap byte dipetakan pada invers perkaliannya (yaitu, sehingga produk mereka sama dengan 1). Kemudian, kita memetakan nilai-nilai tersebut dari Nyberg S-box ke Rijndael’s S-Box menggunakan transformasi afin.

Operasi ketiga pada array S adalah operasi shift rows. Ini mengambil keadaan S dan mencantumkan semua enam belas byte dalam sebuah matriks. Pengisian matriks dimulai di kiri atas dan bergerak mengelilingi dengan cara dari atas ke bawah dan kemudian, setiap kali sebuah kolom terisi, bergeser satu kolom ke kanan dan ke atas.

Setelah matriks S telah dibangun, keempat barisnya digeser. Baris pertama tetap sama. Baris kedua bergerak satu ke kiri. Baris ketiga bergerak dua ke kiri. Baris keempat bergerak tiga ke kiri. Sebuah contoh prosesnya disediakan dalam *Gambar 4*. Keadaan asli dari S ditampilkan di atas, keadaan hasil setelah operasi shift rows ditampilkan di bawahnya.

*Gambar 4: Operasi shift rows*

![Gambar 4: Operasi shift rows](assets/Figure5-4.webp "Gambar 4: Operasi shift rows")

Pada langkah keempat, lapangan Galois muncul lagi. Untuk memulai, setiap kolom dari matriks S dikalikan dengan kolom dari matriks 4 x 4 yang terlihat dalam *Gambar 5*. Namun, bukan perkalian matriks biasa, ini adalah perkalian vektor modulo polinomial tak tereduksi, x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Koefisien vektor yang dihasilkan mewakili bit individu dari sebuah byte.

*Gambar 5: Matriks mix columns*

![Gambar 5: Matriks mix columns](assets/Figure5-5.webp "Gambar 5: Matriks mix columns")

Perkalian kolom pertama dari matriks S dengan matriks 4 x 4 di atas menghasilkan hasil dalam *Gambar 6*.
*Gambar 6: Perkalian kolom pertama*
![Gambar 6: Perkalian kolom pertama](assets/Figure5-6.webp "Gambar 6: Perkalian kolom pertama")

Sebagai langkah selanjutnya, semua istilah dalam matriks harus diubah menjadi polinomial. Misalnya, F1 mewakili 1 byte dan akan menjadi x<sup>7</sup> + x<sup>6</sup> + x<sup>5</sup> + x<sup>4</sup> + 1 dan 03 mewakili 1 byte dan akan menjadi x + 1.

Semua perkalian kemudian dilakukan modulo x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Ini menghasilkan penambahan empat polinomial di setiap empat sel kolom. Setelah melakukan penambahan tersebut modulo 2, Anda akan mendapatkan empat polinomial. Setiap polinomial ini mewakili string 8-bit, atau 1 byte, dari S. Kami tidak akan melakukan semua perhitungan ini di sini pada matriks di *Gambar 6* karena mereka cukup luas.

Setelah kolom pertama diproses, tiga kolom lain dari matriks S diproses dengan cara yang sama. Akhirnya ini akan menghasilkan matriks dengan enam belas byte yang dapat diubah menjadi sebuah array.

Sebagai langkah akhir, array S digabungkan dengan kunci ronde lagi dalam operasi XOR. Ini menghasilkan keadaan S<sub>1</sub>. Yaitu,

- S<sub>1</sub> = S XOR K<sub>0</sub>

### Ronde 2 hingga 10

Ronde 2 hingga 9 hanyalah pengulangan dari ronde 1, *mutatis mutandis*. Ronde terakhir terlihat sangat mirip dengan ronde sebelumnya, kecuali langkah mix columns dihilangkan. Yaitu, ronde 10 dilaksanakan sebagai berikut:

- S<sub>9</sub> XOR K<sub>10</sub>
- Substitusi Byte
- Shift Rows
- S<sub>10</sub> = S XOR K<sub>10</sub>

Keadaan S<sub>10</sub> sekarang ditetapkan menjadi C<sub>1</sub>, 128 bit pertama dari ciphertext. Melanjutkan melalui blok plaintext 128-bit yang tersisa menghasilkan ciphertext C secara penuh.

### Operasi dari cipher Rijndael

Apa alasan di balik operasi yang berbeda yang terlihat dalam cipher Rijndael?

Tanpa masuk ke dalam detail, skema enkripsi dinilai berdasarkan sejauh mana mereka menciptakan kebingungan dan difusi. Jika skema enkripsi memiliki tingkat **kebingungan** yang tinggi, itu berarti ciphertext terlihat sangat berbeda dari plaintext. Jika skema enkripsi memiliki tingkat **difusi** yang tinggi, itu berarti setiap perubahan kecil pada plaintext menghasilkan ciphertext yang sangat berbeda.

Alasan untuk operasi di balik cipher Rijndael adalah mereka menghasilkan kedua tingkat kebingungan dan difusi yang tinggi. Kebingungan dihasilkan oleh operasi Substitusi Byte, sementara difusi dihasilkan oleh operasi shift rows dan mix columns.

# Kriptografi Asimetris
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

Sama seperti kriptografi simetris, skema asimetris dapat digunakan untuk memastikan baik kerahasiaan maupun autentikasi. Namun, berbeda dengan itu, skema ini menggunakan dua kunci daripada satu: kunci privat dan kunci publik.
Kami memulai penyelidikan kami dengan penemuan kriptografi asimetris, khususnya masalah-masalah yang mendorongnya. Selanjutnya, kami membahas bagaimana skema asimetris untuk enkripsi dan autentikasi bekerja pada level tinggi. Kemudian, kami memperkenalkan fungsi hash, yang merupakan kunci untuk memahami skema autentikasi asimetris, dan juga memiliki relevansi dalam konteks kriptografi lainnya, seperti untuk kode autentikasi pesan berbasis hash yang kami bahas di Bab 4.

## Masalah distribusi dan manajemen kunci
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Bayangkan jika Bob ingin membeli jas hujan baru dari Jim’s Sporting Goods, sebuah pengecer perlengkapan olahraga online dengan jutaan pelanggan di Amerika Utara. Ini akan menjadi pembelian pertamanya dari mereka dan dia ingin menggunakan kartu kreditnya. Jadi, Bob pertama-tama perlu membuat akun dengan Jim’s Sporting Goods, yang memerlukan pengiriman detail pribadi seperti alamat dan informasi kartu kreditnya. Kemudian, dia dapat melalui langkah-langkah yang diperlukan untuk membeli jas hujan tersebut.

Bob dan Jim’s Sporting Goods akan ingin memastikan bahwa komunikasi mereka aman sepanjang proses ini, mengingat bahwa Internet adalah sistem komunikasi terbuka. Mereka akan ingin memastikan, misalnya, bahwa tidak ada penyerang potensial yang dapat mengetahui detail kartu kredit dan alamat Bob, dan bahwa tidak ada penyerang potensial yang dapat mengulangi pembeliannya atau membuat pembelian palsu atas namanya.

Skema enkripsi otentikasi lanjutan seperti yang dibahas di bab sebelumnya tentu saja dapat membuat komunikasi antara Bob dan Jim’s Sporting Goods aman. Namun, jelas ada hambatan praktis untuk menerapkan skema seperti itu.

Untuk mengilustrasikan hambatan praktis ini, bayangkan jika kita hidup di dunia di mana hanya alat-alat kriptografi simetris yang ada. Apa yang bisa Jim’s Sporting Goods dan Bob lakukan untuk memastikan komunikasi yang aman?

Dalam keadaan tersebut, mereka akan menghadapi biaya substansial untuk berkomunikasi dengan aman. Karena Internet adalah sistem komunikasi terbuka, mereka tidak bisa hanya bertukar satu set kunci melaluinya. Oleh karena itu, Bob dan perwakilan untuk Jim’s Sporting Goods perlu melakukan pertukaran kunci secara langsung.

Salah satu kemungkinan adalah Jim’s Sporting Goods membuat lokasi pertukaran kunci khusus, di mana Bob dan pelanggan baru lainnya dapat mengambil satu set kunci untuk komunikasi yang aman. Ini jelas akan menimbulkan biaya organisasi yang substansial dan sangat mengurangi efisiensi dengan mana pelanggan baru dapat melakukan pembelian.

Sebagai alternatif, Jim’s Sporting Goods dapat mengirimkan Bob sepasang kunci dengan kurir yang sangat terpercaya. Ini mungkin lebih efisien daripada mengorganisir lokasi pertukaran kunci. Namun, ini masih akan menimbulkan biaya yang substansial, terutama jika banyak pelanggan hanya melakukan satu atau beberapa pembelian.

Selanjutnya, skema simetris untuk enkripsi otentikasi juga memaksa Jim’s Sporting Goods untuk menyimpan set kunci terpisah untuk semua pelanggan mereka. Ini akan menjadi tantangan praktis yang signifikan untuk ribuan pelanggan, apalagi jutaan.

Untuk memahami poin terakhir ini, bayangkan jika Jim’s Sporting Goods memberikan setiap pelanggan sepasang kunci yang sama. Ini akan memungkinkan setiap pelanggan—atau siapa pun yang bisa mendapatkan sepasang kunci ini—untuk membaca dan bahkan memanipulasi semua komunikasi antara Jim’s Sporting Goods dan pelanggannya. Anda mungkin, kemudian, sama sekali tidak menggunakan kriptografi dalam komunikasi Anda.

Bahkan mengulangi satu set kunci hanya untuk beberapa pelanggan adalah praktik keamanan yang buruk. Setiap penyerang potensial dapat mencoba mengeksploitasi fitur skema tersebut (ingat bahwa penyerang diasumsikan mengetahui segalanya tentang skema kecuali kunci, sesuai dengan prinsip Kerckhoffs.)

Jadi, Jim’s Sporting Goods harus menyimpan sepasang kunci untuk setiap pelanggan, terlepas dari bagaimana pasangan kunci tersebut didistribusikan. Ini jelas menyajikan beberapa masalah praktis.

- Jim’s Sporting Goods harus menyimpan jutaan pasang kunci, satu set untuk setiap pelanggan.
- Kunci-kunci ini harus diamankan dengan baik, karena mereka akan menjadi target utama bagi peretas. Setiap pelanggaran keamanan akan memerlukan pengulangan pertukaran kunci yang mahal, baik di lokasi pertukaran kunci khusus atau melalui kurir. - Setiap pelanggan dari Jim’s Sporting Goods harus menyimpan sepasang kunci di rumah dengan aman. Kehilangan dan pencurian akan terjadi, memerlukan pengulangan pertukaran kunci. Pelanggan juga harus melalui proses ini untuk toko online lainnya atau jenis entitas lain yang ingin mereka komunikasikan dan bertransaksi dengannya melalui Internet.

Dua tantangan utama yang baru saja dijelaskan adalah kekhawatiran yang sangat mendasar hingga akhir tahun 1970-an. Mereka dikenal sebagai **masalah distribusi kunci** dan **masalah manajemen kunci**, masing-masing.

Masalah-masalah ini selalu ada, tentu saja, dan seringkali menyebabkan sakit kepala di masa lalu. Misalnya, pasukan militer harus terus-menerus mendistribusikan buku dengan kunci untuk komunikasi yang aman kepada personel di lapangan dengan risiko dan biaya yang besar. Namun, masalah-masalah ini menjadi semakin buruk karena dunia semakin bergerak ke era komunikasi digital jarak jauh, terutama untuk entitas non-pemerintah.

Jika masalah-masalah ini tidak terselesaikan pada tahun 1970-an, belanja yang efisien dan aman di Jim’s Sporting Goods kemungkinan tidak akan ada. Bahkan, sebagian besar dunia modern kita dengan e-mail yang praktis dan aman, perbankan online, dan belanja mungkin hanya akan menjadi fantasi yang jauh. Apapun yang menyerupai Bitcoin sama sekali tidak akan bisa ada.

Jadi, apa yang terjadi pada tahun 1970-an? Bagaimana mungkin kita bisa langsung melakukan pembelian online dan menjelajahi World Wide Web dengan aman? Bagaimana mungkin kita bisa mengirim Bitcoin secara instan ke seluruh dunia dari ponsel pintar kita?

## Arah Baru dalam Kriptografi
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

Pada tahun 1970-an, masalah distribusi kunci dan manajemen kunci telah menarik perhatian sekelompok kriptografer akademik Amerika: Whitfield Diffie, Martin Hellman, dan Ralph Merkle. Di tengah skeptisisme berat dari sebagian besar rekan-rekan mereka, mereka berusaha untuk merancang solusi untuk itu.

Setidaknya satu motivasi utama untuk usaha mereka adalah wawasan bahwa komunikasi komputer terbuka akan sangat mempengaruhi dunia kita. Seperti yang dicatat oleh Diffie dan Hellman pada tahun 1976,

> Pengembangan jaringan komunikasi yang dikontrol komputer menjanjikan kontak yang mudah dan murah antara orang atau komputer di sisi dunia yang berlawanan, menggantikan sebagian besar surat dan banyak perjalanan dengan telekomunikasi. Untuk banyak aplikasi, kontak-kontak ini harus dibuat aman terhadap baik penyadapan maupun penyuntikan pesan ilegitim. Saat ini, bagaimanapun, solusi untuk masalah keamanan jauh tertinggal dibandingkan dengan area teknologi komunikasi lainnya. *Kriptografi kontemporer tidak dapat memenuhi persyaratan, karena penggunaannya akan memberikan ketidaknyamanan yang begitu berat pada pengguna sistem, sehingga menghilangkan banyak manfaat dari teleprosesing.*<sup>[1](#footnote1)</sup>

Ketekunan Diffie, Hellman, dan Merkle terbayar. Publikasi pertama dari hasil mereka adalah sebuah makalah oleh Diffie dan Hellman pada tahun 1976 berjudul “New Directions in Cryptography.” Di dalamnya, mereka menyajikan dua cara asli untuk mengatasi masalah distribusi kunci dan masalah manajemen kunci.
Solusi pertama yang mereka tawarkan adalah protokol *pertukaran kunci jarak jauh*, yaitu, serangkaian aturan untuk pertukaran satu atau lebih kunci simetris melalui saluran komunikasi yang tidak aman. Protokol ini sekarang dikenal sebagai *pertukaran kunci Diffie-Helmann* atau *pertukaran kunci Diffie-Helmann-Merkle*.<sup>[2](#footnote2)</sup>
Dengan pertukaran kunci Diffie-Helmann, dua pihak pertama-tama bertukar beberapa informasi secara publik melalui saluran yang tidak aman seperti Internet. Berdasarkan informasi tersebut, mereka kemudian, secara independen menciptakan kunci simetris (atau sepasang kunci simetris) untuk komunikasi yang aman. Meskipun kedua pihak menciptakan kunci mereka secara independen, informasi yang mereka bagikan secara publik memastikan bahwa proses penciptaan kunci ini menghasilkan hasil yang sama untuk keduanya.

Penting untuk dicatat, meskipun semua orang dapat mengamati informasi yang ditukar secara publik oleh kedua pihak melalui saluran yang tidak aman, hanya dua pihak yang terlibat dalam pertukaran informasi tersebut yang dapat menciptakan kunci simetris darinya.

Ini, tentu saja, terdengar sangat kontra-intuitif. Bagaimana mungkin dua pihak bertukar beberapa informasi secara publik yang hanya memungkinkan mereka untuk menciptakan kunci simetris darinya? Mengapa orang lain yang mengamati pertukaran informasi tidak dapat menciptakan kunci yang sama?

Ini bergantung pada beberapa matematika yang indah tentu saja. Pertukaran kunci Diffie-Helmann bekerja melalui fungsi satu arah dengan pintu perangkap. Mari kita bahas arti dari kedua istilah ini secara bergantian.

Anggaplah Anda diberi fungsi f(x) dan hasil f(a) = y, di mana a adalah nilai tertentu untuk x. Kita mengatakan bahwa f(x) adalah **fungsi satu arah** jika mudah untuk menghitung nilai y ketika diberi a dan f(x), tetapi secara komputasi tidak mungkin untuk menghitung nilai a ketika diberi y dan f(x). Nama fungsi satu arah, tentu saja, berasal dari fakta bahwa fungsi tersebut hanya praktis untuk dihitung dalam satu arah.

Beberapa fungsi satu arah memiliki apa yang dikenal sebagai pintu perangkap. Meskipun secara praktis tidak mungkin untuk menghitung a hanya dengan y dan f(x), ada sepotong informasi Z yang membuat menghitung a dari y secara komputasi menjadi layak. Potongan informasi Z ini dikenal sebagai **pintu perangkap**. Fungsi satu arah yang memiliki pintu perangkap dikenal sebagai **fungsi pintu perangkap**.

Kita tidak akan membahas detail dari pertukaran kunci Diffie-Helmann di sini. Namun pada dasarnya setiap peserta menciptakan beberapa informasi, yang sebagiannya dibagikan secara publik dan sebagian lagi tetap rahasia. Setiap pihak, kemudian, mengambil bagian informasi rahasia mereka dan informasi publik yang dibagikan oleh pihak lain untuk menciptakan kunci pribadi. Dan agak ajaib, kedua pihak akan berakhir dengan kunci pribadi yang sama.

Setiap pihak yang hanya mengamati informasi yang dibagikan secara publik antara dua pihak dalam pertukaran kunci Diffie Helmann tidak dapat mereplikasi perhitungan ini. Mereka memerlukan informasi pribadi dari salah satu dari dua pihak untuk melakukannya.

Meskipun versi dasar dari pertukaran kunci Diffie-Helmann yang disajikan dalam makalah tahun 1976 tidak sangat aman, versi canggih dari protokol dasar tersebut tentu masih digunakan hingga hari ini. Yang paling penting, setiap protokol pertukaran kunci dalam versi terbaru dari protokol keamanan lapisan transportasi (versi 1.3) pada dasarnya adalah versi yang diperkaya dari protokol yang disajikan oleh Diffie dan Hellman pada tahun 1976. Protokol keamanan lapisan transportasi adalah protokol dominan untuk pertukaran informasi yang aman yang diformat menurut protokol transfer hiperteks (http), standar untuk pertukaran konten Web.
Penting untuk diperhatikan, pertukaran kunci Diffie-Helmann bukanlah skema asimetris. Secara ketat, ini bisa dibilang termasuk dalam ranah kriptografi kunci simetris. Namun, karena baik pertukaran kunci Diffie-Helmann maupun kriptografi asimetris mengandalkan fungsi teori bilangan satu arah dengan pintu perangkap, mereka biasanya dibahas bersama-sama.
Cara kedua yang ditawarkan oleh Diffie dan Helmann untuk mengatasi masalah distribusi dan manajemen kunci dalam makalah mereka tahun 1976 adalah, tentu saja, melalui kriptografi asimetris.

Berbeda dengan presentasi mereka tentang pertukaran kunci Diffie-Hellman, mereka hanya menyediakan garis besar umum tentang bagaimana skema kriptografi asimetris bisa dibangun secara masuk akal. Mereka tidak menawarkan fungsi satu arah tertentu yang bisa secara spesifik memenuhi kondisi yang diperlukan untuk keamanan yang masuk akal dalam skema tersebut.

Namun, implementasi praktis dari skema asimetris ditemukan setahun kemudian oleh tiga kriptografer dan matematikawan akademik yang berbeda: Ronald Rivest, Adi Shamir, dan Leonard Adleman. Sistem kriptografi yang mereka perkenalkan dikenal sebagai **sistem kriptografi RSA** (dari nama belakang mereka).

Fungsi pintu perangkap yang digunakan dalam kriptografi asimetris (dan pertukaran kunci Diffie Helmann) semuanya terkait dengan dua masalah **komputasi yang sulit** utama: faktorisasi bilangan prima dan perhitungan logaritma diskrit.

**Faktorisasi bilangan prima** memerlukan, seperti namanya, memecah bilangan bulat menjadi faktor-faktor primanya. Masalah RSA adalah contoh paling terkenal dari sistem kriptografi yang terkait dengan faktorisasi bilangan prima.

**Masalah logaritma diskrit** adalah masalah yang terjadi dalam grup siklik. Diberikan sebuah generator dalam grup siklik tertentu, ini memerlukan perhitungan eksponen unik yang diperlukan untuk menghasilkan elemen lain dalam grup dari generator tersebut.

Skema berbasis logaritma diskrit mengandalkan dua jenis grup siklik utama: grup perkalian bilangan bulat dan grup yang mencakup titik-titik pada kurva eliptik. Pertukaran kunci Diffie Helmann asli seperti yang dipresentasikan dalam "New Directions in Cryptography" bekerja dengan grup perkalian siklik bilangan bulat. Algoritma tanda tangan digital Bitcoin dan skema tanda tangan Schnorr yang baru diperkenalkan (2021) keduanya berbasis pada masalah logaritma diskrit untuk grup siklik kurva eliptik tertentu.

Selanjutnya, kita akan beralih ke gambaran tingkat tinggi tentang kerahasiaan dan autentikasi dalam pengaturan asimetris. Namun, sebelum melakukannya, kita perlu membuat catatan sejarah singkat.

Sekarang tampaknya masuk akal bahwa sekelompok kriptografer dan matematikawan Inggris yang bekerja untuk Government Communications Headquarters (GCHQ) telah secara independen membuat penemuan di atas beberapa tahun sebelumnya. Kelompok ini terdiri dari James Ellis, Clifford Cocks, dan Malcolm Williamson.

Menurut akun mereka sendiri dan GCHQ, James Ellis yang pertama kali merancang konsep kriptografi kunci publik pada tahun 1969. Konon, Clifford Cocks kemudian menemukan sistem kriptografi RSA pada tahun 1973, dan Malcolm Williamson konsep pertukaran kunci Diffie Helmann pada tahun 1974. Penemuan mereka, bagaimanapun, konon tidak diungkapkan sampai tahun 1997, mengingat sifat rahasia dari pekerjaan yang dilakukan di GCHQ.

## Enkripsi dan otentikasi asimetris
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Gambaran umum tentang enkripsi asimetris dengan bantuan Bob dan Alice disediakan dalam *Gambar 1*.
Alice pertama kali membuat sepasang kunci, yang terdiri dari satu kunci publik (K<sub>P</sub>) dan satu kunci privat (K<sub>S</sub>), di mana “P” dalam K<sub>P</sub> berarti “publik” dan “S” dalam K<sub>S</sub> untuk “rahasia”. Kemudian, ia mendistribusikan kunci publik ini secara bebas kepada orang lain. Kita akan kembali ke detail proses distribusi ini sedikit lagi. Namun untuk saat ini asumsikan bahwa siapa pun, termasuk Bob, dapat memperoleh kunci publik Alice K<sub>P</sub> secara aman.
Pada suatu titik nanti, Bob ingin menulis pesan M kepada Alice. Karena pesan tersebut mengandung informasi sensitif, ia ingin isi pesan tetap rahasia untuk semua orang kecuali Alice. Jadi, Bob pertama-tama mengenkripsi pesannya M menggunakan K<sub>P</sub>. Kemudian ia mengirimkan ciphertext C yang dihasilkan kepada Alice, yang mendekripsi C dengan K<sub>S</sub> untuk menghasilkan pesan asli M.

*Gambar 1: Enkripsi Asimetris*

![Gambar 1: Enkripsi Asimetris](assets/Figure6-1.webp "Gambar 1: Enkripsi Asimetris")

Setiap penyerang yang mendengarkan komunikasi antara Bob dan Alice dapat mengamati C. Dia juga mengetahui K<sub>P</sub> dan algoritma enkripsi E(·). Namun, penting untuk dicatat, informasi ini tidak memungkinkan penyerang untuk mendekripsi ciphertext C secara layak. Dekripsi secara spesifik memerlukan K<sub>S</sub>, yang tidak dimiliki oleh penyerang.

Skema enkripsi simetris umumnya perlu aman terhadap penyerang yang dapat mengenkripsi pesan teks biasa secara valid (dikenal sebagai keamanan serangan ciphertext terpilih). Namun, ini tidak dirancang dengan tujuan eksplisit untuk memungkinkan penciptaan ciphertext valid tersebut oleh penyerang atau siapa pun.

Ini sangat berbeda dengan skema enkripsi asimetris, di mana tujuan utamanya adalah untuk memungkinkan siapa pun, termasuk penyerang, untuk menghasilkan ciphertext yang valid. Oleh karena itu, skema enkripsi asimetris dapat dilabeli sebagai **multiple access ciphers**.

Untuk lebih memahami apa yang terjadi, bayangkan jika alih-alih mengirim pesan secara elektronik, Bob ingin mengirim surat fisik secara rahasia. Salah satu cara untuk memastikan kerahasiaan adalah dengan Alice mengirim gembok aman kepada Bob, tetapi menyimpan kunci untuk membukanya. Setelah menulis suratnya, Bob dapat memasukkan surat tersebut ke dalam kotak dan menguncinya dengan gembok Alice. Kemudian, ia dapat mengirim kotak yang terkunci dengan pesan tersebut kepada Alice yang memiliki kunci untuk membukanya.

Sementara Bob mampu mengunci gembok, baik dia maupun orang lain yang mencegat kotak tersebut tidak dapat membuka gembok jika memang aman. Hanya Alice yang dapat membukanya dan melihat isi surat Bob karena dia memiliki kuncinya.

Skema enkripsi asimetris, secara kasar, adalah versi digital dari proses ini. Gembok tersebut serupa dengan kunci publik dan kunci gembok serupa dengan kunci privat. Karena gemboknya digital, bagaimanapun, jauh lebih mudah dan tidak terlalu mahal bagi Alice untuk mendistribusikannya kepada siapa pun yang mungkin ingin mengirim pesan rahasia kepadanya.

Untuk autentikasi dalam pengaturan asimetris, kita menggunakan **tanda tangan digital**. Ini, oleh karena itu, memiliki fungsi yang sama dengan kode autentikasi pesan dalam pengaturan simetris. Ikhtisar tanda tangan digital disediakan dalam *Gambar 2*.
Bob pertama-tama membuat sepasang kunci, yang terdiri dari kunci publik (K<sub>P</sub>) dan kunci privat (K<sub>S</sub>), dan mendistribusikan kunci publiknya. Ketika ia ingin mengirimkan pesan yang terautentikasi kepada Alice, ia pertama-tama mengambil pesannya M dan kunci privatnya untuk membuat tanda tangan digital D. Kemudian, Bob mengirimkan kepada Alice pesannya bersama dengan tanda tangan digital tersebut. Alice memasukkan pesan, kunci publik, dan tanda tangan digital ke dalam algoritma verifikasi. Algoritma ini menghasilkan true untuk tanda tangan yang valid, atau false untuk tanda tangan yang tidak valid.
Tanda tangan digital, seperti yang jelas diimplikasikan oleh namanya, adalah setara digital dari tanda tangan tertulis pada surat, kontrak, dan sebagainya. Bahkan, tanda tangan digital biasanya jauh lebih aman. Dengan beberapa usaha, Anda dapat memalsukan tanda tangan tertulis; proses yang dibuat lebih mudah oleh fakta bahwa tanda tangan tertulis seringkali tidak diverifikasi dengan cermat. Namun, tanda tangan digital yang aman, sama seperti kode autentikasi pesan yang aman, **tidak dapat dipalsukan secara eksistensial**: yaitu, dengan skema tanda tangan digital yang aman, tidak ada yang dapat secara layak membuat tanda tangan untuk pesan yang lulus prosedur verifikasi, kecuali mereka memiliki kunci privat.

*Gambar 2: Autentikasi Asimetris*

![Gambar 2: Autentikasi Asimetris](assets/Figure6-2.webp "Gambar 2: Autentikasi Asimetris")

Seperti dengan enkripsi asimetris, kita melihat kontras yang menarik antara tanda tangan digital dan kode autentikasi pesan. Untuk yang terakhir, algoritma verifikasi hanya dapat digunakan oleh salah satu pihak yang terlibat dalam komunikasi yang aman. Ini karena memerlukan kunci privat. Namun, dalam pengaturan asimetris, siapa pun dapat memverifikasi tanda tangan digital S yang dibuat oleh Bob.

Semua ini membuat tanda tangan digital menjadi alat yang sangat kuat. Ini merupakan dasar, misalnya, dari pembuatan tanda tangan pada kontrak yang dapat diverifikasi untuk tujuan hukum. Jika Bob telah membuat tanda tangan pada kontrak dalam pertukaran di atas, Alice dapat menunjukkan pesan M, kontrak, dan tanda tangan S ke pengadilan. Pengadilan, kemudian, dapat memverifikasi tanda tangan menggunakan kunci publik Bob.<sup>[5](#footnote5)</sup>

Sebagai contoh lain, tanda tangan digital adalah aspek penting untuk mengamankan perangkat lunak dan distribusi pembaruan perangkat lunak. Jenis verifikasi publik ini tidak pernah bisa diciptakan hanya dengan menggunakan kode autentikasi pesan.

Sebagai contoh terakhir dari kekuatan tanda tangan digital, pertimbangkan Bitcoin. Salah satu kesalahpahaman paling umum tentang Bitcoin, terutama di media, adalah bahwa transaksi dienkripsi: mereka tidak. Sebaliknya, transaksi Bitcoin bekerja dengan tanda tangan digital untuk memastikan keamanan.

Bitcoin ada dalam kelompok yang disebut output transaksi yang belum dihabiskan (atau UTXO). Misalkan Anda menerima tiga pembayaran pada alamat Bitcoin tertentu sebesar 2 bitcoin masing-masing. Secara teknis Anda sekarang tidak memiliki 6 bitcoin pada alamat tersebut. Sebaliknya, Anda memiliki tiga kelompok dari 2 bitcoin yang dikunci oleh masalah kriptografi yang terkait dengan alamat tersebut. Untuk setiap pembayaran yang Anda lakukan, Anda dapat menggunakan satu, dua, atau ketiga kelompok ini, tergantung pada berapa banyak yang Anda butuhkan untuk transaksi.

Bukti kepemilikan atas output transaksi yang belum dihabiskan biasanya ditunjukkan melalui satu atau lebih tanda tangan digital. Bitcoin bekerja dengan tepat karena tanda tangan digital yang valid pada output transaksi yang belum dihabiskan secara komputasi tidak mungkin dibuat, kecuali Anda memiliki informasi rahasia yang diperlukan untuk membuatnya.
Saat ini, transaksi Bitcoin secara transparan mencakup semua informasi yang perlu diverifikasi oleh peserta dalam jaringan, seperti asal dari output transaksi yang belum terpakai yang digunakan dalam transaksi tersebut. Meskipun mungkin untuk menyembunyikan sebagian informasi tersebut dan masih memungkinkan untuk verifikasi (seperti yang dilakukan oleh beberapa kriptokurensi alternatif seperti Monero), hal ini juga menciptakan risiko keamanan tertentu.

Kadang-kadang kebingungan muncul antara tanda tangan digital dan tanda tangan tertulis yang ditangkap secara digital. Dalam kasus terakhir, Anda menangkap gambar tanda tangan tertulis Anda dan menempelkannya ke dokumen elektronik seperti kontrak kerja. Namun, ini bukan tanda tangan digital dalam pengertian kriptografi. Yang terakhir hanyalah sebuah angka panjang yang hanya dapat diproduksi dengan memiliki kunci privat.

Sama seperti dalam pengaturan kunci simetris, Anda juga dapat menggunakan skema enkripsi dan otentikasi asimetris bersama-sama. Prinsip yang sama berlaku. Pertama-tama, Anda harus menggunakan pasangan kunci privat-publik yang berbeda untuk enkripsi dan membuat tanda tangan digital. Selain itu, Anda harus terlebih dahulu mengenkripsi pesan dan kemudian mengotentikasinya.

Pentingnya, dalam banyak aplikasi kriptografi asimetris tidak digunakan sepanjang proses komunikasi. Sebaliknya, biasanya hanya akan digunakan untuk *menukar kunci simetris* antara pihak-pihak yang akan berkomunikasi.

Ini adalah kasusnya, misalnya, ketika Anda membeli barang secara online. Mengetahui kunci publik penjual, dia dapat mengirimkan pesan yang ditandatangani secara digital yang dapat Anda verifikasi untuk keasliannya. Berdasarkan ini, Anda dapat mengikuti salah satu dari beberapa protokol untuk menukar kunci simetris untuk berkomunikasi secara aman.

Alasan utama untuk frekuensi pendekatan yang disebutkan di atas adalah bahwa kriptografi asimetris jauh lebih tidak efisien daripada kriptografi simetris dalam menghasilkan tingkat keamanan tertentu. Ini adalah salah satu alasan mengapa kita masih membutuhkan kriptografi kunci simetris di samping kriptografi publik. Selain itu, kriptografi kunci simetris jauh lebih alami dalam aplikasi tertentu seperti pengguna komputer yang mengenkripsi data mereka sendiri.

Jadi, bagaimana sebenarnya tanda tangan digital dan enkripsi kunci publik mengatasi masalah distribusi kunci dan manajemen kunci?

Tidak ada satu jawaban di sini. Kriptografi asimetris adalah sebuah alat dan tidak ada satu cara untuk menggunakan alat tersebut. Tapi mari kita ambil contoh sebelumnya dari Jim’s Sporting Goods untuk menunjukkan bagaimana masalah tersebut biasanya diatasi dalam contoh ini.

Untuk memulai, Jim’s Sporting Goods mungkin akan mendekati **otoritas sertifikat**, sebuah organisasi yang mendukung distribusi kunci publik. Otoritas sertifikat akan mendaftarkan beberapa detail tentang Jim’s Sporting Goods dan memberikannya sebuah kunci publik. Kemudian, akan mengirimkan Jim’s Sporting Goods sebuah sertifikat, yang dikenal sebagai **sertifikat TLS/SSL**, dengan kunci publik Jim’s Sporting Goods ditandatangani secara digital menggunakan kunci publik otoritas sertifikat sendiri. Dengan cara ini, otoritas sertifikat menegaskan bahwa kunci publik tertentu memang milik Jim’s Sporting Goods.

Kunci untuk memahami proses ini dengan sertifikat TLS/SSL adalah bahwa, meskipun Anda umumnya tidak akan memiliki kunci publik Jim’s Sporting Goods tersimpan di mana pun di komputer Anda, kunci publik dari otoritas sertifikat yang diakui memang tersimpan di browser Anda atau di sistem operasi Anda. Ini disimpan dalam apa yang disebut **sertifikat root**.

Oleh karena itu, ketika Jim’s Sporting Goods memberikan Anda sertifikat TLS/SSL-nya, Anda dapat memverifikasi tanda tangan digital otoritas sertifikat melalui sertifikat root di browser atau sistem operasi Anda. Jika tanda tangan valid, Anda dapat cukup yakin bahwa kunci publik pada sertifikat memang milik Jim’s Sporting Goods. Berdasarkan ini, mudah untuk menyiapkan protokol untuk komunikasi yang aman dengan Jim’s Sporting Goods.
Distribusi kunci kini menjadi jauh lebih sederhana bagi Jim’s Sporting Goods. Tidak sulit untuk melihat bahwa manajemen kunci juga menjadi sangat disederhanakan. Alih-alih harus menyimpan ribuan kunci, Jim’s Sporting Goods hanya perlu menyimpan sebuah kunci privat yang memungkinkannya membuat tanda tangan untuk kunci publik pada sertifikat SSL-nya. Setiap kali pelanggan mengunjungi situs Jim’s Sporting Goods, mereka dapat menetapkan sesi komunikasi aman dari kunci publik ini. Pelanggan juga tidak perlu menyimpan informasi apa pun (selain kunci publik dari otoritas sertifikat yang diakui dalam sistem operasi dan browser mereka).

## Fungsi Hash
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Fungsi hash sangat umum dalam kriptografi. Mereka bukan skema simetris maupun asimetris, tetapi masuk ke dalam kategori kriptografi tersendiri.

Kita sudah menemui fungsi hash di Bab 4 dengan pembuatan pesan otentikasi berbasis hash. Fungsi hash juga penting dalam konteks tanda tangan digital, meskipun untuk alasan yang sedikit berbeda: Tanda tangan digital biasanya dibuat atas nilai hash dari beberapa pesan (terenkripsi), bukan pesan (terenkripsi) itu sendiri. Dalam bagian ini, saya akan menawarkan pengenalan yang lebih menyeluruh tentang fungsi hash.

Mari kita mulai dengan mendefinisikan fungsi hash. Sebuah **fungsi hash** adalah fungsi yang dapat dihitung secara efisien yang mengambil input berukuran sembarang dan menghasilkan output berukuran tetap.

Sebuah **fungsi hash kriptografi** hanyalah fungsi hash yang berguna untuk aplikasi dalam kriptografi. Output dari fungsi hash kriptografi biasanya disebut **hash**, **nilai-hash**, atau **ringkasan pesan**.

Dalam konteks kriptografi, "fungsi hash" biasanya mengacu pada fungsi hash kriptografi. Saya akan mengadopsi praktik tersebut dari sini ke depan.

Contoh fungsi hash yang populer adalah **SHA-256** (secure hash algorithm 256). Terlepas dari ukuran input (misalnya, 15 bit, 100 bit, atau 10.000 bit), fungsi ini akan menghasilkan nilai hash 256-bit. Di bawah ini Anda dapat melihat beberapa contoh output dari fungsi SHA-256.

* “Hello”: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
* “52398”: a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90
* “Cryptography is fun”: 3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c

Semua output persis 256 bit ditulis dalam format heksadesimal (setiap digit heks dapat diwakili oleh empat digit biner). Jadi, meskipun Anda memasukkan buku *The Lord of the Rings* karya Tolkien ke dalam fungsi SHA-256, outputnya tetap akan 256 bit.

Fungsi hash seperti SHA-256 digunakan untuk berbagai tujuan dalam kriptografi. Properti apa yang dibutuhkan dari fungsi hash benar-benar tergantung pada konteks aplikasi tertentu. Ada dua properti utama yang umumnya diinginkan dari fungsi hash dalam kriptografi:

1. Tahan Benturan (Collision-resistance)
2. Menyembunyikan (Hiding)

Sebuah fungsi hash H dikatakan tahan benturan jika tidak mungkin menemukan dua nilai, x dan y, sedemikian sehingga x ≠ y, namun H(x) = H(y).
Fungsi hash yang tahan terhadap tabrakan sangat penting, misalnya, dalam verifikasi perangkat lunak. Bayangkan jika Anda ingin mengunduh rilis Windows dari Bitcoin Core 0.21.0 (sebuah aplikasi server untuk memproses lalu lintas jaringan Bitcoin). Langkah utama yang harus Anda lakukan untuk memverifikasi keaslian perangkat lunak tersebut adalah sebagai berikut:
1. Anda pertama-tama perlu mengunduh dan mengimpor kunci publik dari satu atau lebih kontributor Bitcoin Core ke dalam perangkat lunak yang dapat memverifikasi tanda tangan digital (misalnya, Kleopetra). Anda dapat menemukan kunci publik ini [di sini](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Disarankan untuk memverifikasi perangkat lunak Bitcoin Core dengan kunci publik dari beberapa kontributor.
2. Selanjutnya, Anda perlu memverifikasi kunci publik yang telah Anda impor. Setidaknya satu langkah yang harus Anda lakukan adalah memverifikasi bahwa kunci publik yang Anda temukan sama dengan yang dipublikasikan di berbagai lokasi lain. Anda mungkin, misalnya, berkonsultasi dengan halaman web pribadi, halaman Twitter, atau halaman Github dari orang-orang yang kunci publiknya Anda impor. Biasanya perbandingan kunci publik ini dilakukan dengan membandingkan hash pendek dari kunci publik yang dikenal sebagai sidik jari.
3. Selanjutnya, Anda perlu mengunduh eksekutabel untuk Bitcoin Core dari [situs web](www.bitcoincore.org) mereka. Akan ada paket yang tersedia untuk sistem operasi Linux, Windows, dan MAC.
4. Selanjutnya, Anda harus menemukan dua file rilis. Yang pertama berisi hash SHA-256 resmi untuk eksekutabel yang Anda unduh bersama dengan hash untuk semua paket lain yang dirilis. File rilis lainnya akan berisi tanda tangan dari berbagai kontributor atas file rilis dengan hash paket. Kedua file rilis ini harus berada di situs web Bitcoin Core.
5. Selanjutnya, Anda perlu menghitung hash SHA-256 dari eksekutabel yang Anda unduh dari situs web Bitcoin Core di komputer Anda sendiri. Kemudian, bandingkan hasil ini dengan hash paket resmi untuk eksekutabel tersebut. Keduanya harus sama.
6. Akhirnya, Anda harus memverifikasi bahwa satu atau lebih tanda tangan digital atas file rilis dengan hash paket resmi memang sesuai dengan satu atau lebih kunci publik yang Anda impor (rilis Bitcoin Core tidak selalu ditandatangani oleh semua orang). Anda dapat melakukan ini dengan aplikasi seperti Kleopetra.

Proses verifikasi perangkat lunak ini memiliki dua manfaat utama. Pertama, itu memastikan bahwa tidak ada kesalahan dalam transmisi saat mengunduh dari situs web Bitcoin Core. Kedua, itu memastikan bahwa tidak ada penyerang yang bisa membuat Anda mengunduh kode yang dimodifikasi, berbahaya, baik dengan meretas situs web Bitcoin Core atau dengan mencegat lalu lintas.

Bagaimana tepatnya proses verifikasi perangkat lunak di atas melindungi dari masalah-masalah ini?

Jika Anda dengan teliti memverifikasi kunci publik yang Anda impor, maka Anda bisa cukup yakin bahwa kunci-kunci tersebut memang milik mereka dan tidak telah dikompromikan. Mengingat tanda tangan digital memiliki ketidakmungkinan pemalsuan eksistensial, Anda tahu bahwa hanya kontributor-kontributor tersebut yang bisa membuat tanda tangan digital atas hash paket resmi pada file rilis.

Anggaplah tanda tangan pada file rilis yang Anda unduh terverifikasi. Sekarang Anda dapat membandingkan nilai hash yang Anda hitung secara lokal untuk eksekutabel Windows yang Anda unduh dengan yang termasuk dalam file rilis yang ditandatangani dengan benar. Karena Anda tahu fungsi hash SHA-256 tahan terhadap tabrakan, kesesuaian berarti eksekutabel Anda persis sama dengan eksekutabel resmi.

Sekarang mari kita beralih ke properti umum kedua dari fungsi hash: penyembunyian. Fungsi hash H dikatakan memiliki properti penyembunyian, jika, untuk x yang dipilih secara acak dari rentang yang sangat besar, tidak mungkin untuk menemukan x hanya dengan diberikan H(x).
Di bawah ini, Anda dapat melihat output SHA-256 dari sebuah pesan yang saya tulis. Untuk memastikan keacakan yang cukup, pesan tersebut mencakup string karakter yang dihasilkan secara acak di bagian akhir. Mengingat SHA-256 memiliki properti penyembunyian, tidak ada yang akan dapat menafsirkan pesan ini.
* b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded

Tetapi saya tidak akan membuat Anda penasaran sampai SHA-256 menjadi lebih lemah. Pesan asli yang saya tulis adalah sebagai berikut:

* “Ini adalah pesan yang sangat acak, atau ya, semacam acak. Bagian awal ini tidak, tetapi saya akan mengakhiri dengan beberapa karakter yang relatif acak untuk memastikan pesan yang sangat tidak terduga. XLWz4dVG3BxUWm7zQ9qS”.

Salah satu cara umum di mana fungsi hash dengan properti penyembunyian digunakan adalah dalam manajemen kata sandi (resistensi terhadap tabrakan juga penting untuk aplikasi ini). Setiap layanan berbasis akun online yang layak seperti Facebook atau Google tidak akan menyimpan kata sandi Anda secara langsung untuk mengelola akses ke akun Anda. Sebaliknya, mereka hanya akan menyimpan hash dari kata sandi tersebut. Setiap kali Anda mengisi kata sandi di browser, hash terlebih dahulu dihitung. Hanya hash itu yang dikirim ke server penyedia layanan dan dibandingkan dengan hash yang disimpan di basis data back-end. Properti penyembunyian dapat membantu memastikan bahwa penyerang tidak dapat memulihkannya dari nilai hash.

Manajemen kata sandi melalui hash, tentu saja, hanya berfungsi jika pengguna benar-benar memilih kata sandi yang sulit. Properti penyembunyian mengasumsikan bahwa x dipilih secara acak dari rentang yang sangat besar. Memilih kata sandi seperti “1234”, “mypassword”, atau tanggal ulang tahun Anda tidak akan memberikan keamanan yang nyata. Daftar panjang kata sandi umum dan hash mereka ada yang dapat dimanfaatkan oleh penyerang jika mereka pernah mendapatkan hash dari kata sandi Anda. Jenis serangan ini dikenal sebagai **serangan kamus**. Jika penyerang mengetahui beberapa detail pribadi Anda, mereka mungkin juga mencoba beberapa tebakan yang berdasarkan informasi. Oleh karena itu, Anda selalu membutuhkan kata sandi yang panjang dan aman (sebaiknya string acak yang panjang dari manajer kata sandi).

Terkadang sebuah aplikasi mungkin memerlukan fungsi hash yang memiliki resistensi terhadap tabrakan dan penyembunyian. Tetapi tentu saja tidak selalu. Proses verifikasi perangkat lunak yang kami bahas, misalnya, hanya memerlukan bahwa fungsi hash menampilkan resistensi terhadap tabrakan, penyembunyian tidak penting.

Sementara resistensi terhadap tabrakan dan penyembunyian adalah properti utama yang dicari dari fungsi hash dalam kriptografi, dalam beberapa aplikasi jenis properti lain mungkin juga diinginkan.

### Catatan
[^1]: Whitfield Diffie dan Martin Hellman, “New directions in cryptography,” *IEEE Transactions on Information Theory* IT-22 (1976), hal. 644–654, pada hal. 644 [^1].

[^2]: Ralph Merkle juga membahas protokol pertukaran kunci dalam “Secure communications over insecure channels”, *Communications of the Association for Computing Machinery*, 21 (1978), 294–99. Meskipun Merkle sebenarnya mengajukan makalah ini sebelum makalah oleh Diffie dan Hellman, itu diterbitkan kemudian. Solusi Merkle tidak aman secara eksponensial, tidak seperti Diffie-Hellman [^2].

[^3]: Ron Rivest, Adi Shamir, dan Leonard Adleman, “A method for obtaining digital signatures and public-key cryptosystems”, *Communications of the Association for Computing Machinery*, 21 (1978), hal. 120–26 [^3].

[^4]: Sejarah yang baik dari penemuan-penemuan ini disediakan oleh Simon Singh, *The Code Book*, Fourth Estate (London, 1999), Bab 6 [^4].
[^5]: Setiap skema yang berusaha mencapai non-repudiation, tema lain yang kita bahas di *Bab 1*, pada dasarnya perlu melibatkan tanda tangan digital [^5].
[^6]: Terminologi "menyembunyikan" bukanlah bahasa umum, tetapi diambil secara spesifik dari Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller, dan Steven Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Bab 1 [^6].

# Sistem Kriptografi RSA
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

Meskipun kriptografi simetris biasanya cukup intuitif bagi kebanyakan orang, hal ini biasanya tidak berlaku untuk kriptografi asimetris. Meskipun Anda mungkin nyaman dengan deskripsi tingkat tinggi yang ditawarkan di bagian sebelumnya, Anda mungkin bertanya-tanya apa sebenarnya fungsi satu arah itu dan bagaimana tepatnya mereka digunakan untuk membangun skema asimetris.

Dalam bab ini, saya akan menghilangkan beberapa misteri yang mengelilingi kriptografi asimetris, dengan melihat lebih dalam ke contoh spesifik, yaitu sistem kriptografi RSA. Di bagian pertama, saya akan memperkenalkan masalah faktorisasi yang menjadi dasar masalah RSA. Saya kemudian akan membahas sejumlah hasil kunci dari teori bilangan. Di bagian terakhir, kita akan menggabungkan informasi ini untuk menjelaskan masalah RSA, dan bagaimana ini dapat digunakan untuk menciptakan skema kriptografi asimetris.

Menambahkan kedalaman pada diskusi kita bukanlah tugas yang mudah. Ini memerlukan pengenalan beberapa teorema dan proposisi teori bilangan. Tapi jangan biarkan matematika membuat Anda mundur. Bekerja melalui diskusi ini akan sangat meningkatkan pemahaman Anda tentang apa yang mendasari kriptografi asimetris dan merupakan investasi yang berharga.

Mari kita sekarang beralih ke masalah faktorisasi.

## Masalah Faktorisasi
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Kapanpun Anda mengalikan dua bilangan, katakanlah a dan b, kita menyebut bilangan a dan b sebagai **faktor**, dan hasilnya sebagai **produk**. Mencoba menuliskan sebuah bilangan N menjadi perkalian dua atau lebih faktor disebut **faktorisasi** atau **faktoring**.<sup>[1](#footnote1)</sup> Anda dapat menyebut masalah apa pun yang memerlukan ini sebagai **masalah faktorisasi**.

Sekitar 2.500 tahun yang lalu, matematikawan Yunani Euclid dari Alexandria menemukan sebuah teorema kunci tentang faktorisasi bilangan bulat. Ini umumnya disebut **teorema faktorisasi unik** dan menyatakan hal berikut:

*Teorema 1*. Setiap bilangan bulat N yang lebih besar dari 1 adalah bilangan prima, atau dapat dinyatakan sebagai produk dari faktor-faktor prima.

Semua bagian akhir dari pernyataan ini berarti adalah bahwa Anda dapat mengambil bilangan bulat non-prima N apa pun yang lebih besar dari 1, dan menuliskannya sebagai perkalian bilangan prima. Di bawah ini adalah beberapa contoh bilangan bulat non-prima yang ditulis sebagai produk dari faktor-faktor prima.

* 18 = 2 • 3 • 3 = 2 • 3<sup>2</sup>
* 84 = 2 • 2 • 3 • 7 = 2<sup>2</sup> • 3 • 7
* 144 = 2 • 2 • 2 • 2 • 3 • 3 = 2<sup>4</sup> • 3<sup>2</sup>
Untuk ketiga bilangan bulat di atas, menghitung faktor prima mereka relatif mudah, bahkan jika Anda hanya diberi N. Anda mulai dengan bilangan prima terkecil, yaitu 2, dan lihat berapa kali bilangan bulat N dapat dibagi olehnya. Kemudian, Anda beralih untuk menguji pembagian N oleh 3, 5, 7, dan seterusnya. Anda melanjutkan proses ini sampai bilangan bulat N Anda dituliskan sebagai hasil kali dari bilangan prima saja.
Ambil contoh bilangan bulat 84. Di bawah ini Anda dapat melihat proses untuk menentukan faktor prima-nya. Di setiap langkah kita mengambil faktor prima terkecil yang tersisa (di sebelah kiri) dan menentukan sisa istilah yang akan difaktorkan. Kita teruskan sampai istilah sisa juga merupakan bilangan prima. Di setiap langkah, faktorisasi saat ini dari 84 ditampilkan di sebelah kanan.

* Faktor prima = 2: sisa istilah = 42 	(84 = 2 • 42)
* Faktor prima = 2: sisa istilah = 21 	(84 = 2 • 2 • 21)
* Faktor prima = 3: sisa istilah = 7 		(84 = 2 • 2 • 3 • 7)
* Karena 7 adalah bilangan prima, hasilnya adalah 2 • 2 • 3 • 7, atau 2<sup>2</sup> • 3 • 7.

Sekarang bayangkan jika N sangat besar. Seberapa sulitkah untuk mereduksi N menjadi faktor prima-nya?

Itu benar-benar tergantung pada N. Misalkan, misalnya, bahwa N adalah 50,450,400. Meskipun angka ini terlihat menakutkan, perhitungannya tidak begitu rumit dan dapat dengan mudah dilakukan dengan tangan. Seperti di atas, Anda hanya mulai dengan 2 dan bekerja jalan Anda ke depan. Di bawah ini, Anda dapat melihat hasil dari proses ini dengan cara yang serupa seperti di atas.

* 2: 25,225,200 	(50,450,400 = 2 • 25,225,200)
* 2: 12,612,600 	(50,450,400 = 2<sup>2</sup> • 12,612,600)
* 2: 6,306,300 		(50,450,400 = 2<sup>3</sup> • 6,306,300)
* 2: 3,153,150 		(50,450,400 = 2<sup>4</sup> • 3,153,150)
* 2: 1,576,575 		(50,450,400 = 2<sup>5</sup> • 1,576,575)
* 3: 525,525 		(50,450,400 = 2<sup>5</sup> • 3 • 525,525)
* 3: 175,175 		(50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 175,175)
* 5: 35,035 		(50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5 • 35,035)
* 5: 7,007		    (50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7,007)
* 7: 1.001		    (50.450.400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7 • 1.001)
* 7: 143			(50.450.400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 143)
* 11: 13			(50.450.400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 11 • 13)
* Karena 13 adalah bilangan prima, hasilnya adalah 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 11 • 13.

Menyelesaikan masalah ini dengan tangan membutuhkan waktu. Tentu saja, sebuah komputer dapat melakukan semua ini dalam sebagian kecil dari detik. Bahkan, komputer seringkali bahkan dapat memfaktorkan bilangan bulat yang sangat besar dalam sebagian kecil dari detik.

Namun, ada beberapa pengecualian. Anggaplah kita pertama-tama secara acak memilih dua bilangan prima yang sangat besar. Biasanya, bilangan ini dilabeli sebagai p dan q, dan saya akan mengadopsi konvensi tersebut di sini.

Untuk kejelasan, katakanlah bahwa p dan q keduanya adalah bilangan prima 1024-bit, dan bahwa mereka memang memerlukan setidaknya 1024 bit untuk dapat direpresentasikan (jadi bit pertama harus 1). Jadi, misalnya, 37 tidak bisa menjadi salah satu dari bilangan prima tersebut. Anda tentu saja dapat merepresentasikan 37 dengan 1024 bit. Tapi jelas *Anda tidak memerlukan* banyak bit untuk merepresentasikannya. Anda dapat merepresentasikan 37 dengan string apa pun yang memiliki 6 bit atau lebih. (Dalam 6 bit, 37 akan direpresentasikan sebagai 100101).

Penting untuk menghargai seberapa besar p dan q jika dipilih di bawah kondisi di atas. Sebagai contoh, saya telah memilih sebuah bilangan prima acak yang memerlukan setidaknya 1024 bit untuk representasi di bawah ini.

* 14.752.173.874.503.595.484.930.006.383.670.759.559.764.562.721.397.166.747.289.220.945.457.932.666.751.048.198.854.920.097.085.690.793.755.254.946.188.163.753.506.778.089.706.699.671.722.089.715.624.760.049.594.106.189.662.669.156.149.028.900.805.928.183.585.427.782.974.951.355.515.394.807.209.836.870.484.558.332.897.443.152.653.214.483.870.992.618.171.825.921.582.253.023.974.514.209.142.520.026.807.636.589

Anggap sekarang setelah secara acak memilih bilangan prima p dan q, kita mengalikannya untuk mendapatkan sebuah bilangan bulat N. Bilangan bulat yang terakhir ini, oleh karena itu, adalah bilangan 2048 bit yang memerlukan setidaknya 2048 bit untuk representasinya. Ini jauh, jauh lebih besar daripada p atau q.
Bayangkan Anda hanya memberikan sebuah komputer N, dan memintanya untuk menemukan dua faktor prima 1024 bit dari N. Kemungkinan bahwa komputer menemukan p dan q sangatlah kecil. Anda bisa mengatakan itu adalah mustahil untuk semua tujuan praktis. Ini berlaku, bahkan jika Anda menggunakan superkomputer atau bahkan jaringan superkomputer.

Untuk memulai, bayangkan bahwa komputer mencoba menyelesaikan masalah dengan mengitari angka-angka 1024 bit, menguji dalam setiap kasus apakah mereka prima dan jika mereka adalah faktor dari N. Kumpulan bilangan prima yang akan diuji kemudian kira-kira 1,265 • 10<sup>305</sup>.<sup>[2](#footnote2)</sup>

Bahkan jika Anda mengambil semua komputer di planet ini dan membuat mereka mencoba menemukan dan menguji bilangan prima 1024-bit dengan cara ini, kesempatan 1 dalam satu miliar untuk berhasil menemukan faktor prima dari N akan memerlukan periode perhitungan yang jauh lebih lama daripada usia Semesta.

Sekarang dalam praktiknya sebuah komputer bisa melakukan lebih baik daripada prosedur kasar yang baru saja dijelaskan. Ada beberapa algoritma yang bisa diterapkan komputer untuk mencapai faktorisasi lebih cepat. Namun, poinnya adalah bahwa bahkan menggunakan algoritma yang lebih efisien ini, tugas komputer masih secara komputasi tidak layak.<sup>[3](#footnote3)</sup>

Pentingnya, kesulitan faktorisasi di bawah kondisi yang baru saja dijelaskan didasarkan pada asumsi bahwa tidak ada algoritma yang efisien secara komputasi untuk menghitung faktor prima. Kita tidak bisa benar-benar membuktikan bahwa algoritma yang efisien tidak ada. Namun, asumsi ini sangat masuk akal: meskipun upaya ekstensif yang berlangsung ratusan tahun, kita belum menemukan algoritma yang efisien secara komputasi.

Oleh karena itu, masalah faktorisasi, dalam keadaan tertentu, dapat dengan masuk akal diasumsikan sebagai masalah yang sulit. Secara khusus, ketika p dan q adalah bilangan prima yang sangat besar, produk mereka N tidak sulit untuk dihitung; tetapi faktorisasi hanya dengan diberikan N praktis tidak mungkin.

## Hasil teori bilangan
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Sayangnya, masalah faktorisasi tidak dapat digunakan langsung untuk skema kriptografi asimetris. Namun, kita dapat menggunakan masalah yang lebih kompleks tetapi terkait untuk efek ini: masalah RSA.

Untuk memahami masalah RSA, kita perlu memahami sejumlah teorema dan proposisi dari teori bilangan. Ini disajikan dalam bagian ini dalam tiga subbagian: (1) urutan dari N, (2) kebalikan modulo N, dan (3) teorema Euler.

Beberapa materi dalam tiga subbagian ini telah diperkenalkan di *Bab 3*. Tapi saya akan di sini menyatakan kembali materi tersebut untuk kenyamanan.

### Urutan dari N

Sebuah bilangan bulat a adalah **koprima** atau **prima relatif** dengan bilangan bulat N, jika pembagi terbesar bersama antara mereka adalah 1. Meskipun 1 secara konvensi bukan bilangan prima, itu adalah koprima dari setiap bilangan bulat (seperti juga – 1).

Misalnya, pertimbangkan kasus ketika a = 18 dan N = 37. Ini jelas koprima. Bilangan bulat terbesar yang membagi kedua 18 dan 37 adalah 1. Sebaliknya, pertimbangkan kasus ketika a = 42 dan N = 16. Ini jelas bukan koprima. Kedua bilangan tersebut dapat dibagi oleh 2, yang lebih besar dari 1.
Kita sekarang dapat mendefinisikan urutan dari N sebagai berikut. Anggaplah bahwa N adalah bilangan bulat lebih dari 1. **Urutan dari N** adalah, jumlah semua bilangan koprima dengan N sehingga untuk setiap koprima a, kondisi berikut berlaku: 1 ≤ a < N.
Sebagai contoh, jika N = 12, maka 1, 5, 7, dan 11 adalah satu-satunya koprima yang memenuhi persyaratan di atas. Oleh karena itu, urutan dari 12 sama dengan 4.

Anggaplah bahwa N adalah bilangan prima. Maka setiap bilangan bulat yang lebih kecil dari N tetapi lebih besar atau sama dengan 1 adalah koprima dengannya. Ini termasuk semua elemen dalam set berikut: {1,2,3….,N – 1}. Oleh karena itu, ketika N adalah prima, urutan dari N adalah N – 1. Ini dinyatakan dalam proposisi 1, di mana φ(N) menunjukkan urutan dari N.

**Proposisi 1**. φ(N) = N – 1 ketika N adalah prima

Anggaplah bahwa N bukan bilangan prima. Anda, kemudian, dapat menghitung urutannya menggunakan **Fungsi Phi Euler**. Meskipun menghitung urutan dari bilangan bulat kecil relatif mudah, Fungsi Phi Euler menjadi sangat penting untuk bilangan bulat yang lebih besar. Proposisi dari Fungsi Phi Euler dinyatakan di bawah ini.

*Teorema 2*. Misalkan N sama dengan p<sub>1</sub><sup>e_1</sup> • p<sub>2</sub><sup>e_2</sup> • … • p<sub>i</sub><sup>e_i</sup> • … • p<sub>n</sub><sup>e_n</sup>, di mana set {p<sub>i</sub>} terdiri dari semua faktor prima yang berbeda dari N dan setiap e_i menunjukkan berapa kali faktor prima p<sub>i</sub> terjadi untuk N. Maka, φ(N) = p<sub>1</sub><sup>e_1 - 1</sup> • (p<sub>1</sub> - 1) • p<sub>2</sub><sup>e_2 - 1</sup> • (p<sub>2</sub> - 1) • … • p<sub>n</sub><sup>e_n - 1</sup> • (p<sub>n</sub> - 1).

*Teorema 2* menunjukkan bahwa setelah Anda memecah N non-prima apa pun menjadi faktor prima yang berbeda, mudah untuk menghitung urutan dari N.

Sebagai contoh, anggaplah bahwa N = 270. Ini jelas bukan bilangan prima. Memecah N menjadi faktor prima memberikan ekspresi: 2 • 3<sup>3</sup> • 5. Menurut Fungsi Phi Euler, urutan dari N kemudian adalah sebagai berikut:

* φ(N) = 2<sup>1 – 1</sup> (2 – 1) + 3<sup>3 – 1</sup> (3 – 1) + 5<sup>1 – 1</sup> (5 – 1) = 1 (1) + 9 (2) + 1 (4) = 1 + 18 + 4 = 23
Misalkan selanjutnya bahwa N adalah hasil kali dari dua bilangan prima, p dan q. *Teorema 2* di atas, maka, menyatakan bahwa urutan dari N adalah sebagai berikut: p<sup>1 – 1</sup> (p – 1) x q<sup>1 – 1</sup> (q – 1) = (p – 1) x (q – 1). Ini adalah hasil kunci untuk masalah RSA khususnya, dan dinyatakan dalam *Proposisi 2* di bawah ini.
*Proposisi 2*. Jika N adalah hasil kali dari dua bilangan prima, p dan q, maka urutan dari N adalah produk (p – 1) x (q – 1).

Untuk mengilustrasikan, misalkan bahwa N = 119. Bilangan bulat ini dapat difaktorkan menjadi dua bilangan prima, yaitu 7 dan 17. Oleh karena itu, fungsi Phi Euler menyarankan bahwa urutan dari 119 adalah sebagai berikut:

* φ(119) = (7 – 1) • (17 – 1) = 6 • 16 = 96.

Dengan kata lain, bilangan bulat 119 memiliki 96 koprima dalam rentang dari 1 sampai 119. Sebenarnya, himpunan ini mencakup semua bilangan bulat dari 1 sampai 119, yang bukan kelipatan dari 7 atau 17.

Dari sini, mari kita sebut himpunan koprima yang menentukan urutan dari N sebagai **C<sub>N</sub>**. Untuk contoh kita dimana N = 119, himpunan **C<sub>119</sub>** terlalu besar untuk dicantumkan secara lengkap. Namun, beberapa elemennya adalah sebagai berikut: **C<sub>119</sub>** = {1,2,….6,8….13,15,16,18,….,33,35….,96}.

### Keterbalikan modulo N

Kita dapat mengatakan bahwa sebuah bilangan bulat a adalah **terbalik modulo N**, jika ada setidaknya satu bilangan bulat b sehingga a x b modulo N = 1 modulo N. Bilangan bulat b seperti itu disebut sebagai **invers** (atau **invers perkalian**) dari a yang diberikan reduksi oleh modulo N.

Misalkan, sebagai contoh, bahwa a = 5 dan N = 11. Ada banyak bilangan bulat yang dapat Anda kalikan dengan 5, sehingga 5 x b mod 11 = 1 mod 11. Pertimbangkan, misalnya, bilangan bulat 20 dan 31. Mudah untuk melihat bahwa kedua bilangan bulat ini adalah invers dari 5 untuk reduksi modulo 11.

* 5 x 20 mod 11 = 100 mod 11 = 1 mod 11
* 5 x 31 mod 11 = 155 mod 11 = 1 mod 11

Sementara 5 memiliki banyak invers reduksi modulo 11, Anda dapat menunjukkan bahwa hanya satu invers positif dari 5 yang ada yang kurang dari 11. Sebenarnya, ini bukan unik untuk contoh khusus kita, tetapi hasil umum.

*Proposisi 3*. Jika bilangan bulat a dapat dibalik modulo N, maka harus demikian bahwa tepat satu invers positif dari a kurang dari N. (Jadi, invers unik dari a ini harus berasal dari himpunan {1,…,N – 1}).
Mari kita nyatakan invers unik dari a dari Proposisi 3 sebagai a<sup>-1</sup>. Untuk kasus ketika a = 5 dan N = 11, Anda dapat melihat bahwa a<sup>-1</sup> = 9, mengingat 5 x 9 mod 11 = 45 mod 11 = 1 mod 11.
Perhatikan bahwa Anda juga dapat memperoleh nilai 9 untuk a<sup>-1</sup> dalam contoh kita dengan hanya mengurangi invers lain dari a dengan modulo 11. Misalnya, 20 mod 11 = 31 mod 11 = 9 mod 11. Jadi, kapan pun sebuah bilangan bulat a > N dapat diinverskan modulo N, maka a mod N juga harus dapat diinverskan modulo N.

Bukan berarti selalu ada invers dari a eksis reduksi modulo N. Misalkan, sebagai contoh, bahwa a = 2 dan N = 8. Tidak ada b, atau a<sup>-1</sup> secara spesifik, sehingga 2 x b mod 8 = 1 mod 8. Ini karena nilai b apapun akan selalu menghasilkan kelipatan dari 2, jadi tidak ada pembagian oleh 8 yang dapat menghasilkan sisa yang sama dengan 1.

Bagaimana kita tahu jika beberapa bilangan bulat a memiliki invers untuk N tertentu? Seperti yang mungkin Anda perhatikan dalam contoh di atas, pembagi terbesar antara 2 dan 8 lebih tinggi dari 1, yaitu 2. Dan ini sebenarnya menggambarkan hasil umum berikut:

*Proposisi 4*. Sebuah invers eksis dari sebuah bilangan bulat a diberikan reduksi modulo N, dan secara spesifik sebuah invers positif unik kurang dari N, jika dan hanya jika pembagi terbesar antara a dan N adalah 1 (yaitu, jika mereka adalah koprima).

Untuk kasus ketika a = 5 dan N = 11, kita menyimpulkan bahwa a<sup>-1</sup> = 9, mengingat 5 x 9 mod 11 = 45 mod 11 = 1 mod 11. Penting untuk dicatat bahwa kebalikannya juga benar. Yaitu, ketika a = 9 dan N = 11, kasusnya adalah a<sup>-1</sup> = 5.

### Teorema Euler

Sebelum beralih ke masalah RSA, kita perlu memahami satu teorema penting lagi, yaitu **Teorema Euler**. Teorema ini menyatakan sebagai berikut:

*Teorema 3*. Anggap dua bilangan bulat a dan N adalah koprima. Maka, a<sup>φ(N)</sup> mod N = 1 mod N.

Ini adalah hasil yang luar biasa, tapi sedikit membingungkan pada awalnya. Mari kita beralih ke sebuah contoh untuk memahaminya.

Anggap bahwa a = 5 dan N = 7. Ini memang koprima seperti yang dibutuhkan oleh teorema Euler. Kita tahu bahwa urutan dari 7 sama dengan 6, mengingat 7 adalah bilangan prima (lihat **Proposisi 1**).

Apa yang sekarang dinyatakan oleh teorema Euler adalah bahwa 5<sup>6</sup> mod 7 harus sama dengan 1 mod 7. Berikut adalah perhitungan untuk menunjukkan bahwa ini memang benar.

* 5<sup>6</sup> mod 7 = 15,625 mod 7 = 1 mod N

Bilangan bulat 7 membagi 15,624 sebanyak 2,233 kali. Oleh karena itu, sisa dari pembagian 16,625 oleh 7 adalah 1.

Selanjutnya, menggunakan fungsi Phi Euler, *Teorema 2*, Anda dapat menurunkan *Proposisi 5* di bawah ini.
*Proposisi 5*. φ(a • b) = φ(a) • φ(b) untuk setiap bilangan bulat positif a dan b.
Kami tidak akan menjelaskan mengapa hal ini terjadi. Namun, perlu dicatat bahwa Anda telah melihat bukti dari proposisi ini dengan fakta bahwa φ(p • q) = φ(p) • φ(q) = (p – 1) • (q – 1) ketika p dan q adalah bilangan prima, seperti yang dinyatakan dalam *Proposisi 2*.

Teorema Euler bersama dengan *Proposisi 5* memiliki implikasi penting. Lihat apa yang terjadi, misalnya, dalam ekspresi di bawah ini, di mana a dan N adalah koprima.

* a<sup>2 • φ(N)</sup> mod N = a<sup>φ(N)</sup> • a<sup>φ(N)</sup> mod N = 1 • 1 mod N = 1 mod N
* a<sup>φ(N) + 1</sup> mod N = a<sup>φ(N)</sup> • a<sup>1</sup> mod N = 1 • a<sup>1</sup> mod N = a mod N
* a<sup>8 • φ(N) + 3</sup> mod N = a<sup>8 • φ(N)</sup> • a<sup>3</sup> mod N = 1 • a<sup>3</sup> mod N = a<sup>3</sup> mod N

Dengan demikian, kombinasi dari teorema Euler dan *Proposisi 5* memungkinkan kita untuk menghitung sejumlah ekspresi dengan sederhana. Secara umum, kita dapat merangkum wawasan ini seperti dalam *Proposisi 6*.

*Proposisi 6*. a<sup>x</sup> mod N = a<sup>x mod φ(N)</sup>

Sekarang kita harus menyatukan semuanya dalam langkah terakhir yang rumit.

Sama seperti N memiliki orde φ(N) yang mencakup elemen dari himpunan **C<sub>N</sub>**, kita tahu bahwa bilangan bulat φ(N) pada gilirannya juga harus memiliki orde dan himpunan koprima. Mari kita tetapkan φ(N) = R. Maka kita tahu bahwa ada juga nilai untuk φ(R) dan himpunan koprima **C<sub>R</sub>**.

Anggaplah kita sekarang memilih sebuah bilangan bulat e dari himpunan **C<sub>R</sub>**. Kita tahu dari *Proposisi 3* bahwa bilangan bulat e ini hanya memiliki satu invers positif unik yang kurang dari R. Artinya, e memiliki satu invers unik dari himpunan **C<sub>R</sub>**. Mari kita sebut invers ini d. Dengan definisi sebuah invers, ini berarti bahwa e • d = 1 mod R.

Kita dapat menggunakan hasil ini untuk membuat pernyataan tentang bilangan bulat asli kita N. Ini dirangkum dalam *Proposisi 7*.

*Proposisi 7*. Anggaplah e • d mod φ(N) = 1 mod φ(N). Maka untuk setiap elemen a dari himpunan **C<sub>N</sub>** haruslah kasus bahwa a<sup>e • d mod φ(N)</sup> = a<sup>1 mod φ(N)</sup> = a mod N.

Kita sekarang memiliki semua hasil teori bilangan yang diperlukan untuk menyatakan masalah RSA dengan jelas.


## Sistem Kriptografi RSA
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>
Kita sekarang siap untuk menjelaskan masalah RSA. Bayangkan Anda membuat satu set variabel yang terdiri dari p, q, N, φ(N), e, d, dan y. Sebut set ini Π. Set ini dibuat sebagai berikut:
1. Hasilkan dua bilangan prima acak p dan q dengan ukuran yang sama dan hitung hasil kali mereka N.
2. Hitung ordo dari N, φ(N), dengan produk berikut: (p – 1) • (q – 1).
3. Pilih sebuah e > 2 sedemikian rupa sehingga lebih kecil dan koprima dengan φ(N).
4. Hitung d dengan menetapkan e • d mod φ(N) = 1.
5. Pilih nilai acak y yang lebih kecil dan koprima dengan N.

Masalah RSA terdiri dari menemukan sebuah x sedemikian rupa sehingga x<sup>e</sup> = y, sambil hanya diberikan sebagian informasi mengenai Π, yaitu variabel N, e, dan y. Ketika p dan q sangat besar, biasanya disarankan agar mereka berukuran 1024 bit, masalah RSA dianggap sulit. Anda sekarang dapat melihat mengapa ini adalah kasusnya berdasarkan diskusi sebelumnya.

Cara mudah untuk menghitung x ketika x<sup>e</sup> mod N = y mod N adalah dengan menghitung y<sup>d</sup> mod N. Kita tahu y<sup>d</sup> mod N = x mod N dengan perhitungan berikut:

* y<sup>d</sup> mod N = x<sup>e • d</sup> mod N = x<sup>e • d mod φ(N)</sup> mod N = x<sup>1 mod φ(N)</sup> mod N = x mod N.

Masalahnya adalah kita tidak mengetahui nilai d, karena tidak diberikan dalam masalah. Oleh karena itu, kita tidak dapat langsung menghitung y<sup>d</sup> mod N untuk menghasilkan x mod N.

Namun, kita mungkin dapat secara tidak langsung menghitung d dari ordo N, φ(n), karena kita tahu bahwa e • d mod φ(N) = 1 mod φ(N). Tetapi dengan asumsi masalah tidak memberikan nilai untuk φ(N) juga.

Akhirnya, ordo dapat dihitung secara tidak langsung dengan faktor prima p dan q, sehingga kita akhirnya dapat menghitung d. Tetapi dengan asumsi, nilai p dan q juga tidak diberikan kepada kita.

Secara ketat, meskipun masalah faktorisasi dalam masalah RSA sulit, kita tidak dapat membuktikan bahwa masalah RSA juga sulit. Mungkin saja ada cara lain untuk menyelesaikan masalah RSA selain melalui faktorisasi. Namun, umumnya diterima dan diasumsikan bahwa jika masalah faktorisasi dalam masalah RSA sulit, maka masalah RSA itu sendiri juga sulit.

Jika masalah RSA memang sulit, maka itu menghasilkan fungsi satu arah dengan pintu perangkap. Fungsi di sini adalah f(g) = g<sup>e</sup> mod N. Dengan pengetahuan tentang f(g), siapa pun dapat dengan mudah menghitung nilai y untuk g tertentu = x. Namun, praktis tidak mungkin untuk menghitung nilai x tertentu hanya dari mengetahui nilai y dan fungsi f(g). Kecuali jika Anda diberikan sepotong informasi d, pintu perangkap. Dalam kasus itu, Anda dapat dengan mudah menghitung y<sup>d</sup> untuk memberikan x.

Mari kita lalui contoh spesifik untuk mengilustrasikan masalah RSA. Saya tidak dapat memilih masalah RSA yang akan dianggap sulit di bawah kondisi di atas, karena angkanya akan terlalu besar. Sebaliknya, contoh ini hanya untuk mengilustrasikan bagaimana masalah RSA umumnya bekerja.
Untuk memulai, anggap Anda memilih dua bilangan prima acak 13 dan 31. Jadi p = 13 dan q = 31. Hasil kali N dari kedua prima ini sama dengan 403. Kita dapat dengan mudah menghitung orde dari 403. Ini setara dengan (13 – 1) • (31 – 1) = 360.
Selanjutnya, seperti yang ditentukan oleh langkah 3 dari masalah RSA, kita perlu memilih sebuah coprime untuk 360 yang lebih besar dari 2 dan kurang dari 360. Kita tidak harus memilih nilai ini secara acak. Anggap bahwa kita memilih 103. Ini adalah coprime dari 360 karena pembagi terbesar bersama dengan 103 adalah 1.

Langkah 4 sekarang mengharuskan kita untuk menghitung nilai d sedemikian rupa sehingga 103 • d mod 360 = 1. Ini bukan tugas yang mudah secara manual ketika nilai untuk N besar. Ini memerlukan kita menggunakan prosedur yang disebut **algoritma Euclidean yang diperluas**.

Meskipun saya tidak menunjukkan prosedurnya di sini, itu menghasilkan nilai 7 ketika e = 103. Anda dapat memverifikasi bahwa pasangan nilai 103 dan 7 memang memenuhi kondisi umum e • d mod φ(n) = 1 melalui perhitungan di bawah ini.

* 103 • 7 mod 360 = 721 mod 360 = 1 mod 360

Pentingnya, diberikan *Proposisi 4*, kita tahu bahwa tidak ada bilangan bulat lain antara 1 dan 360 untuk d yang akan menghasilkan hasil bahwa 103 • d = 1 mod 360. Selain itu, proposisi tersebut menyiratkan bahwa memilih nilai yang berbeda untuk e, akan menghasilkan nilai unik yang berbeda untuk d.

Dalam langkah 5 dari masalah RSA, kita harus memilih beberapa bilangan bulat positif y yang merupakan coprime yang lebih kecil dari 403. Anggap bahwa kita menetapkan y = 2<sup>103</sup>. Eksponensiasi 2 oleh 103 menghasilkan hasil di bawah ini.

* 2<sup>103</sup> mod 403 = 10,141,204,801,825,835,211,973,625,643,008 mod 403 = 349 mod 403

Masalah RSA dalam contoh khusus ini sekarang adalah sebagai berikut: Anda diberikan dengan N = 403, e = 103, dan y = 349 mod 403. Anda sekarang harus menghitung x sedemikian rupa sehingga x<sup>103</sup> = 349 mod 403. Artinya, Anda harus menemukan bahwa nilai asli sebelum eksponensiasi oleh 103 adalah 2.

Ini akan mudah (setidaknya untuk komputer) untuk menghitung x jika kita tahu bahwa d = 7. Dalam kasus tersebut, Anda bisa saja menentukan x sebagai berikut.

* x = y<sup>7</sup> mod 403 = 349<sup>7</sup> mod 403 = 630,634,881,591,804,949 mod 403 = 2 mod 403

Masalahnya adalah Anda tidak diberikan informasi bahwa d = 7. Tentu saja, Anda bisa menghitung d dari fakta bahwa 103 • d = 1 mod 360. Masalahnya adalah Anda juga tidak diberikan informasi bahwa orde dari N = 360. Akhirnya, Anda juga bisa menghitung orde dari 403 dengan menghitung produk berikut: (p – 1) • (q – 1). Tapi Anda juga tidak diberitahu bahwa p = 13 dan q = 31.
Tentu saja, sebuah komputer masih bisa dengan relatif mudah menyelesaikan masalah RSA untuk contoh ini, karena angka prima yang terlibat tidak besar. Namun, ketika angka prima menjadi sangat besar, komputer tersebut menghadapi tugas yang hampir mustahil.

Kami telah memperkenalkan masalah RSA, serangkaian kondisi di mana masalah tersebut sulit, dan matematika yang mendasarinya. Bagaimana semua ini membantu dengan kriptografi asimetris? Secara spesifik, bagaimana kita dapat mengubah kesulitan masalah RSA dalam kondisi tertentu menjadi skema enkripsi atau skema tanda tangan digital?

Salah satu pendekatan adalah mengambil masalah RSA dan membangun skema dengan cara yang langsung. Misalnya, anggaplah Anda menghasilkan serangkaian variabel Π seperti yang dijelaskan dalam masalah RSA, dan memastikan bahwa p dan q cukup besar. Anda menetapkan kunci publik Anda sama dengan (N, e) dan membagikan informasi ini ke dunia. Seperti yang dijelaskan di atas, Anda menyimpan nilai untuk p, q, φ(n), dan d sebagai rahasia. Faktanya, d adalah kunci privat Anda.

Siapa pun yang ingin mengirimkan Anda pesan m yang merupakan elemen dari **C<sub>N</sub>** bisa dengan mudah mengenkripsinya sebagai berikut: c = m<sup>e</sup> mod N. (Ciphertext c di sini setara dengan nilai y dalam masalah RSA.) Anda dapat dengan mudah mendekripsi pesan ini hanya dengan menghitung c<sup>d</sup> mod N.

Anda mungkin mencoba membuat skema tanda tangan digital dengan cara yang sama. Misalkan Anda ingin mengirim seseorang pesan m dengan tanda tangan digital S. Anda bisa saja menetapkan S = m<sup>d</sup> mod N dan mengirimkan pasangan (m,S) ke penerima. Siapa pun dapat memverifikasi tanda tangan digital hanya dengan memeriksa apakah S<sup>e</sup> mod N = m mod N. Namun, penyerang mana pun akan memiliki waktu yang sangat sulit untuk membuat S yang valid untuk sebuah pesan, mengingat mereka tidak memiliki d.

Sayangnya, mengubah masalah yang sendirinya sulit, masalah RSA, menjadi skema kriptografi tidaklah sesederhana itu. Untuk skema enkripsi yang langsung, Anda hanya dapat memilih coprime dari N sebagai pesan Anda. Ini tidak meninggalkan kita dengan banyak pesan yang mungkin, tentu saja tidak cukup untuk komunikasi standar. Selain itu, pesan-pesan ini harus dipilih secara acak. Ini tampaknya agak tidak praktis. Akhirnya, setiap pesan yang dipilih dua kali akan menghasilkan ciphertext yang sama persis. Ini sangat tidak diinginkan dalam skema enkripsi apa pun, dan tidak memenuhi standar keamanan modern yang ketat dalam enkripsi.

Masalahnya menjadi lebih buruk untuk skema tanda tangan digital kita yang langsung. Seperti adanya, penyerang mana pun dapat dengan mudah memalsukan tanda tangan digital hanya dengan terlebih dahulu memilih coprime dari N sebagai tanda tangan dan kemudian menghitung pesan asli yang sesuai. Ini jelas melanggar persyaratan ketidakmungkinan pemalsuan eksistensial.

Namun demikian, dengan menambahkan sedikit kompleksitas yang cerdas, masalah RSA dapat digunakan untuk menciptakan skema enkripsi kunci publik yang aman serta skema tanda tangan digital yang aman. Kami tidak akan memasuki detail konstruksi seperti itu di sini.<sup>[4](#footnote4)</sup> Namun, penting untuk dicatat, kompleksitas tambahan ini tidak mengubah masalah RSA yang mendasari fundamental di mana skema ini didasarkan.

### Catatan

[^1]: Faktorisasi juga bisa penting untuk bekerja dengan objek matematika lain selain angka. Misalnya, itu bisa berguna untuk memfaktorkan ekspresi polinomial seperti x^2 – 2x + 1. Dalam diskusi kami, kami hanya akan fokus pada faktorisasi angka, khususnya bilangan bulat [^1].
[^2]: Menurut teorema bilangan prima, jumlah bilangan prima yang kurang dari atau sama dengan N adalah kira-kira N/ln(N). Ini berarti Anda dapat mengaproksimasi jumlah bilangan prima dengan panjang 1024 bit dengan 2^1024/ln(2^1024) - 2^1023/ln(2^1023) yang kira-kira sama dengan 1.265 x 10^305 [^2].

# Kontribusi
<partId>4556aab1-4876-552a-b6db-df6837bbf27a</partId>

## Tentang
<chapterId>ff08a57b-740f-5d7e-8cf2-81db0908166e</chapterId>

Setiap kontribusi sangat kami hargai. Sebelum melakukan hal tersebut, silakan lihat di bawah ini untuk informasi latar belakang tentang rencana saya sendiri untuk buku ini serta pedoman untuk membuat kontribusi.

### Rencana Saat Ini

Rencana saya saat ini untuk pengembangan lebih lanjut dari buku ini adalah sebagai berikut:

- Membuat bab akhir yang membahas detail aplikasi kriptografi praktis, seperti keamanan lapisan transportasi, pengarahan ulang onion, dan pertukaran nilai dalam Bitcoin
- Membuat gambar dan diagram yang lebih baik dan lebih banyak untuk mendukung diskusi tertulis
- Menggunakan LaTeX Math atau aplikasi pengetikan lainnya untuk notasi formal (daripada hanya Markdown)

### Pedoman untuk Kontribusi

Jika Anda memiliki koreksi kecil atau saran terkait teks yang ada, Anda dapat membuat pull request atau mengajukan masalah. Jika Anda membuat pull request, harap perhatikan pedoman berikut:

- Buat commit pada cabang terpisah di fork repositori Anda
- Beri label pada commit dengan jelas
- Buat commit terpisah untuk masalah yang secara logis berbeda untuk memudahkan proses review

Jika Anda memiliki saran yang lebih substansial terkait buku ini, silakan ajukan masalah atau hubungi saya langsung di **jaburgers@protonmail.com**.

### Lisensi

Karya dalam repositori ini dilisensikan di bawah Lisensi Internasional Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 (CC BY-NC-ND 4.0).

Anda dapat menemukan deskripsi singkat lisensi [di sini](https://creativecommons.org/licenses/by-nc-nd/4.0/).

Anda dapat menemukan versi lengkap dari lisensi [di sini](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode).

## Notasi
<chapterId>07250f8d-ad7c-5531-a70c-4417d6d1b865</chapterId>

### Istilah Kunci

Istilah kunci dalam primer diperkenalkan dengan membuatnya tebal. Misalnya, pengenalan cipher Rijndael sebagai istilah kunci akan terlihat sebagai berikut: **cipher Rijndael**.

Istilah kunci didefinisikan secara eksplisit, kecuali mereka adalah nama proper atau maknanya jelas dari diskusi.

Definisi biasanya diberikan pada saat pengenalan istilah kunci, meskipun terkadang lebih nyaman untuk meninggalkan definisi sampai titik yang lebih lanjut.

### Kata dan Frasa yang Ditekankan

Kata dan frasa ditekankan melalui kursif. Misalnya, frasa "Ingatlah password Anda" akan terlihat sebagai berikut: *Ingatlah password Anda*.

### Notasi Formal

Notasi formal terutama menyangkut variabel, variabel acak, dan himpunan.

* Variabel: Ini biasanya hanya ditunjukkan oleh huruf kecil (misalnya, "x" atau "y"). Terkadang mereka dikapitalisasi untuk kejelasan (misalnya, "M" atau "K").
* Variabel acak: Ini selalu ditunjukkan oleh huruf kapital (misalnya, "X" atau "Y").
* Himpunan: Ini selalu ditunjukkan dengan huruf tebal, huruf besar (misalnya, **S**)