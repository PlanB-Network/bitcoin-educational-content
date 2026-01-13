---
name: Mempelajari Rust dengan Bitcoin
goal: Tingkatkan keterampilan pengembangan Rust Anda melalui pengkodean Bitcoin
objectives: 

  - Membiasakan diri dengan Bahasa Rust
  - Memahami mengapa menggunakan Rust untuk mengembangkan Bitcoin
  - Dapatkan dasar dari Lightning SDK

---

# Ekspedisi Rust untuk Pembangun Bitcoin



Dalam kursus ini, yang difilmkan selama seminar yang diselenggarakan oleh Fulgur 'Ventures pada bulan Oktober 2023, Anda akan mengembangkan keterampilan Rust Anda dengan membangun komponen dan proyek mini yang berfokus pada Bitcoin yang nyata. Kita akan membahas dasar-dasar Rust, mengapa Rust digunakan untuk pengembangan Bitcoin (keamanan memori, kinerja, dan konkurensi yang aman), dan bagaimana cara memulai dengan Lightning SDK untuk membangun fitur pembayaran.


Di seluruh bab, Anda akan mempraktikkan pola inti Rust (kepemilikan, masa pakai, sifat, sinkronisasi), bekerja dengan primitif Bitcoin (kunci, transaksi, skrip), dan secara progresif mengintegrasikan konsep-konsep Lightning (node, saluran, faktur).


Tidak diperlukan pengalaman dalam pengembangan Rust atau Bitcoin sebelumnya, meskipun pemahaman tentang pemrograman dasar akan membantu. Kursus ini ramah bagi pemula namun cukup praktis bagi para insinyur yang ingin beralih ke Bitcoin.


+++

# Pendahuluan

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Gambaran umum kursus

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Pendahuluan**


Selamat datang di kursus pemrograman yang ramah pemula tentang SDK. Dalam pelatihan ini, Anda akan mempelajari dasar-dasar Rust, kemudian fokus pada pemrograman Rust yang diterapkan pada pemrograman Bitcoin, dan diakhiri dengan beberapa kasus penggunaan menggunakan SDK.


Video pelatihan ini hanya akan tersedia dalam bahasa Inggris untuk saat ini dan merupakan bagian dari seminar langsung yang diselenggarakan pada bulan Oktober lalu di Tuscany oleh Fulgure Venture. Pelatihan ini akan fokus pada minggu pertama saja. Paruh kedua ditargetkan untuk RGB dan dapat ditemukan di kursus RGB.


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Pelatihan ini memberikan Anda kesempatan untuk mengembangkan keterampilan pemrograman Anda pada Lightning Network menggunakan Rust dan berbagai SDK. Kursus ini dirancang untuk para pengembang dengan latar belakang pemrograman yang solid yang ingin mendalami pengembangan khusus Lightning Network. Anda akan mempelajari dasar-dasar Rust, mengapa Rust cocok untuk pengembangan Bitcoin, dan kemudian beralih ke implementasi langsung menggunakan SDK khusus.


**Bagian 2: Belajar membuat kode dengan Rust**

Di bagian ini, Anda akan menemukan dasar-dasar Rust melalui serangkaian bab yang progresif. Anda akan belajar menulis kode Rust, memahami kekhususannya, dan menguasai fitur-fitur esensialnya melalui tujuh bagian yang terperinci. Modul ini sangat penting untuk memahami mengapa Rust adalah bahasa yang disukai untuk pengembangan Bitcoin.


**Bagian 3: Rust & Bitcoin**

Di sini, kita akan mengeksplorasi secara mendalam mengapa Rust adalah pilihan yang relevan untuk pengembangan Bitcoin. Anda akan belajar tentang model kesalahannya, alat UniFFI, dan sifat asinkron - semua elemen kunci dalam membangun perangkat lunak yang kuat dan aman.


**Bagian 4: Pengembangan LNP/BP dengan SDK**

Anda akan belajar cara mengembangkan node LN menggunakan berbagai SDK seperti Breez SDK dan Greenlight untuk Lipa. Anda akan melihat cara mengimplementasikan aplikasi Lightning Network menggunakan pustaka yang dirancang untuk menyederhanakan pengembangan Bitcoin dan Lightning.


Siap untuk mengembangkan keterampilan Lightning Network Anda dengan Rust? Mari kita mulai!

# Pelajari cara membuat kode dengan buku karat

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Pengantar ke Rust

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Memasang dan Mengelola Rust dengan Rustup


Ketika memulai perjalanan Anda dengan Rust, langkah pertama adalah menyiapkan lingkungan pengembangan yang tepat. Pendekatan yang paling banyak direkomendasikan untuk menginstal Rust adalah melalui Rustup, sebuah sistem manajemen toolchain yang menangani instalasi dan pembaruan di berbagai proyek dan platform.


Rustup berfungsi lebih dari sekadar penginstal - Rustup berfungsi sebagai alat manajemen yang komprehensif untuk lingkungan pengembangan Rust Anda. Dengan Rustup, Anda dapat dengan mudah menginstal target kompilasi tambahan untuk platform yang berbeda, seperti ARM64 untuk pengembangan Android atau arsitektur lain yang mungkin perlu Anda dukung. Alat ini juga menangani pembaruan Rust dengan lancar, yang sangat berharga mengingat Rust merilis versi stabil baru kira-kira setiap enam minggu. Ketika Anda perlu memperbarui ke rilis terbaru, perintah `rustup update` yang sederhana akan menangani semuanya secara otomatis.


Ketika menginstal Rustup, ada baiknya Anda memahami model keamanan yang terlibat. Proses instalasi mengunduh dan menjalankan skrip dari situs web resmi Rust melalui HTTPS, yang menyediakan keamanan kriptografi lapisan transport. Paket-paket yang diunduh oleh Rustup dan Cargo berasal dari sumber tepercaya (crates.io dan infrastruktur resmi Rust) dan mendapatkan manfaat dari enkripsi HTTPS. Meskipun pendekatan ini aman untuk sebagian besar skenario pengembangan, beberapa organisasi dengan kebijakan keamanan yang ketat mungkin lebih suka menginstal Rust melalui manajer paket distribusi Linux mereka, yang menyediakan lapisan kepercayaan tambahan melalui infrastruktur penandatanganan paket distribusi itu sendiri. Untuk tujuan pembelajaran dan pengembangan umum, Rustup adalah alat yang sudah mapan dan dipercaya secara luas dalam ekosistem Rust.


Untuk sebagian besar skenario pengembangan, Anda dapat menginstal Rustup dengan menjalankan skrip instalasi yang disediakan di situs web resmi Rust. Penginstal akan meminta Anda untuk memilih di antara opsi toolchain yang berbeda, dengan toolchain stabil sebagai pilihan yang direkomendasikan untuk sebagian besar pengguna. Instalasi terjadi di direktori rumah Anda, tidak memerlukan hak administrator, dan menyiapkan semua variabel lingkungan yang diperlukan untuk segera digunakan.


### Memahami Rangkaian Alat dan Komponen Rust


Ekosistem pengembangan Rust terdiri dari beberapa komponen utama yang bekerja sama untuk menyediakan lingkungan pemrograman yang lengkap. Memahami komponen-komponen ini membantu Anda menavigasi proses pengembangan Rust dengan lebih efektif dan memecahkan masalah ketika muncul.


Kompiler Rust, yang dikenal sebagai `rustc`, merupakan inti dari toolchain Rust. Meskipun secara teoritis Anda dapat menggunakan `rustc` secara langsung untuk mengkompilasi program Rust, sebagian besar pekerjaan pengembangan bergantung pada Cargo, manajer paket dan sistem pembangun Rust. Cargo berfungsi mirip dengan npm dalam ekosistem JavaScript, mengelola ketergantungan, mengoordinasikan build, dan menyediakan perintah-perintah yang mudah untuk tugas-tugas pengembangan yang umum. Ketika Anda menjalankan perintah seperti `cargo build` atau `cargo run`, Cargo mengatur proses kompilasi, menangani resolusi ketergantungan, dan mengelola struktur proyek secara keseluruhan.


Clippy adalah linter yang menganalisis kode Anda dan memberikan saran untuk perbaikan. Tidak seperti pemeriksa sintaksis dasar, Clippy memahami idiom Rust dan dapat merekomendasikan cara-cara yang lebih idiomatis untuk menyelesaikan tugas-tugas tertentu. Alat ini membantu dalam mempelajari praktik terbaik Rust dan menulis kode yang lebih mudah dipelihara.


Rangkaian alat Rust juga mencakup alat dokumentasi yang komprehensif dan dokumentasi pustaka standar, yang dapat diakses melalui situs web dokumentasi resmi Rust. Dokumentasi ini berfungsi sebagai referensi yang sangat diperlukan selama pengembangan, memberikan informasi terperinci tentang fungsi, jenis, dan modul pustaka standar. Dokumentasi ini mencakup contoh dan penjelasan ekstensif yang membantu Anda memahami tidak hanya fungsi apa yang dilakukan, tetapi juga bagaimana menggunakannya secara efektif dalam program Anda.


Rust mendukung beberapa saluran rilis: stabil, beta, dan malam. Saluran stabil menyediakan rilis yang telah teruji secara menyeluruh dan cocok untuk penggunaan produksi. Saluran beta menawarkan pratinjau rilis stabil berikutnya, terutama digunakan untuk pengujian akhir sebelum rilis resmi. Saluran nightly mencakup fitur eksperimental yang sedang dalam pengembangan aktif, yang dapat berguna untuk mencoba kemampuan Rust yang baru, meskipun fitur-fitur ini dapat berubah atau dihapus dalam rilis mendatang.


### Membuat dan Mengelola Proyek Rust dengan Kargo


Pengembangan Rust modern berpusat di sekitar Cargo, yang menyederhanakan pembuatan proyek, manajemen ketergantungan, dan proses pembangunan. Daripada membuat direktori dan file secara manual, Cargo menyediakan perintah `cargo new` untuk generate sebuah struktur proyek yang lengkap dengan default yang masuk akal.


Ketika Anda membuat proyek baru dengan `cargo new project_name`, Cargo membuat struktur direktori standar, membuat file `main.rs` dasar dengan program "Hello, world!", menginisialisasi repositori Git, dan membuat file `Cargo.toml` untuk konfigurasi proyek. File `Cargo.toml` berfungsi sebagai titik konfigurasi pusat untuk proyek Anda, yang berisi metadata tentang proyek Anda dan mencantumkan semua dependensi yang dibutuhkan kode Anda.


Cargo menyediakan beberapa perintah penting untuk pekerjaan pengembangan harian. Perintah `cargo build` mengkompilasi proyek Anda dan ketergantungannya, membuat file yang dapat dieksekusi dalam direktori `target`. Untuk iterasi cepat selama pengembangan, `cargo run` menggabungkan pembangunan dan eksekusi dalam satu langkah. Perintah `cargo check` melakukan semua pemeriksaan kompilasi tanpa menghasilkan file yang dapat dieksekusi akhir, membuatnya jauh lebih cepat daripada pembangunan penuh ketika Anda hanya ingin memverifikasi bahwa kode Anda dikompilasi dengan benar.


Saat menyiapkan kode untuk penerapan produksi, bendera `--release` memungkinkan pengoptimalan dan menghapus pernyataan debug. Release build berjalan lebih cepat dan menghasilkan file yang lebih kecil, tetapi membutuhkan waktu lebih lama untuk mengkompilasi dan menghapus informasi debug yang berguna. Kompiler menerapkan berbagai pengoptimalan selama proses build rilis dan menonaktifkan pemeriksaan runtime seperti deteksi integer overflow, yang meningkatkan kinerja tetapi menghilangkan beberapa jaminan keamanan yang ada dalam build debug.


### Variabel, Mutabilitas, dan Filosofi Keselamatan Rust


Rust mengambil pendekatan yang berbeda untuk manajemen variabel daripada kebanyakan bahasa. Secara default, semua variabel dalam Rust tidak dapat diubah, yang berarti nilainya tidak dapat diubah setelah penetapan awal. Keputusan desain ini bertujuan untuk mencegah kesalahan pemrograman umum yang muncul dari perubahan status yang tidak terduga.


Ketika Anda mendeklarasikan sebuah variabel dengan menggunakan `let x = 5`, variabel tersebut akan menjadi tidak berubah secara default. Setiap upaya untuk mengubah nilainya di kemudian hari akan mengakibatkan kesalahan kompilasi. Persyaratan keabadian ini memaksa pengembang untuk berpikir dengan hati-hati tentang kapan perubahan status benar-benar diperlukan dan membuat perilaku kode lebih dapat diprediksi. Banyak bug pemrograman berasal dari variabel yang berubah secara tidak terduga, dan keabadian default Rust membantu mencegah masalah ini.


Ketika Anda benar-benar perlu memodifikasi nilai sebuah variabel, Rust membutuhkan deklarasi eksplisit mutabilitas menggunakan kata kunci `mut`: `let mut x = 5`. Deklarasi eksplisit ini berfungsi sebagai sinyal yang jelas bagi kompiler dan pengembang lain bahwa nilai variabel ini dapat berubah selama eksekusi program. Persyaratan untuk mendeklarasikan mutabilitas secara eksplisit mendorong pertimbangan yang matang apakah mutabilitas benar-benar diperlukan untuk setiap variabel.


Rust juga mendukung shadowing, yang memungkinkan Anda untuk mendeklarasikan variabel baru dengan nama yang sama dengan variabel sebelumnya. Tidak seperti mutasi, shadowing menciptakan variabel yang sama sekali baru yang kebetulan memiliki nama yang sama, secara efektif menyembunyikan variabel sebelumnya. Teknik ini terbukti sangat berguna ketika mengubah data melalui beberapa langkah, seperti mengurai string menjadi angka dan kemudian memproses angka tersebut lebih lanjut. Dengan shadowing, Anda dapat mempertahankan nama variabel yang konsisten di seluruh proses transformasi sambil mengubah jenis variabel di setiap langkah.


Perbedaan antara shadowing dan mutasi menjadi penting ketika mempertimbangkan perubahan tipe. Dengan shadowing, Anda dapat mengubah nilai dan tipe variabel karena Anda membuat variabel baru. Dengan mutasi, Anda hanya dapat mengubah nilai dengan tetap mempertahankan tipe yang sama, karena Anda memodifikasi variabel yang sudah ada, bukan membuat variabel baru.


```rust
// Shadowing: creating new variables with the same name
let amount = "100000";           // amount is a &str (string slice)
let amount = amount.parse::<u64>().unwrap();  // amount is now u64
let amount = amount * 100;       // amount is still u64, new value

// Mutation: modifying the same variable
let mut balance = 50000_u64;
balance = balance + amount;      // OK: same type, different value
// balance = "empty";            // ERROR: cannot change type with mutation

// Practical example: processing a Bitcoin amount input
let user_input = "  0.001 ";                    // &str with whitespace
let user_input = user_input.trim();            // &str, whitespace removed
let satoshis: u64 = (user_input.parse::<f64>().unwrap() * 100_000_000.0) as u64;
println!("Amount in satoshis: {}", satoshis);  // 100000
```


### Tipe Data dan Dasar-dasar Sistem Tipe


Rust mengimplementasikan sistem tipe statis yang kuat di mana setiap nilai harus memiliki tipe yang terdefinisi dengan baik yang diketahui pada saat kompilasi. Meskipun hal ini mungkin terlihat membatasi dibandingkan dengan bahasa yang diketik secara dinamis, kemampuan inferensi tipe Rust berarti Anda jarang perlu menentukan tipe secara eksplisit. Kompiler biasanya dapat menentukan tipe yang sesuai berdasarkan cara Anda menggunakan nilai.


Namun, situasi tertentu membutuhkan anotasi tipe secara eksplisit. Ketika menggunakan fungsi umum seperti `parse()`, yang dapat mengonversi string menjadi berbagai tipe numerik, kompiler perlu mengetahui tipe spesifik yang Anda inginkan. Dalam kasus ini, Anda memberikan anotasi tipe menggunakan sintaks titik dua: `tebak: u32 = "42".parse().expect("Bukan angka!")`.


Tipe skalar Rust mencakup bilangan bulat, bilangan floating-point, boolean, dan karakter. Sistem tipe integer memberikan kontrol yang tepat atas penggunaan memori dan karakteristik kinerja. Tipe integer diberi nama secara sistematis: `i8`, `i16`, `i32`, `i64`, dan `i128` untuk bilangan bulat bertanda, dan `u8`, `u16`, `u32`, `u64`, dan `u128` untuk bilangan bulat tidak bertanda. Angka-angka tersebut menunjukkan lebar bit, sehingga penggunaan memori dan rentang nilai menjadi jelas.


Tipe `isize` dan `usize` perlu mendapat perhatian khusus karena keduanya beradaptasi dengan arsitektur target Anda. Pada sistem 64-bit, tipe ini memiliki lebar 64 bit, sedangkan pada sistem 32-bit, tipe ini memiliki lebar 32 bit. Tipe-tipe ini biasanya digunakan untuk pengindeksan larik dan offset memori karena cocok dengan ukuran kata alami dari arsitektur target, sehingga memungkinkan aritmatika penunjuk dan operasi memori yang efisien.


Rust menyediakan berbagai cara untuk menulis literal bilangan bulat, termasuk format desimal, heksadesimal (`0x`), oktal (`0o`), dan biner (`0b`). Anda juga dapat menggunakan garis bawah di mana saja di dalam literal numerik untuk meningkatkan keterbacaan, seperti menulis `1_000_000` alih-alih `1000000`. Garis bawah tidak berpengaruh pada nilai, namun dapat membuat angka yang besar menjadi lebih mudah dibaca.


Tipe floating-point dalam Rust sangat mudah: `f32` untuk presisi tunggal dan `f64` untuk angka floating-point presisi ganda. Jenis `f64` umumnya lebih disukai karena presisi yang lebih tinggi dan fakta bahwa prosesor modern sering kali dapat menangani operasi floating-point 64-bit seefisien operasi 32-bit.


### Jenis Senyawa dan Organisasi Data


Selain tipe skalar, Rust menyediakan tipe majemuk yang mengelompokkan beberapa nilai menjadi satu. Tupel memungkinkan Anda untuk menggabungkan nilai dari tipe yang berbeda ke dalam satu nilai gabungan. Anda membuat tupel menggunakan tanda kurung dan dapat menentukan tipe setiap elemen: `let tup: (i32, f64, u8) = (500, 6.4, 1)`.


Tuple mendukung destrukturisasi, yang memungkinkan Anda mengekstrak nilai individual: `let (x, y, z) = tup`. Sintaks ini menciptakan tiga variabel terpisah dari komponen tuple. Sebagai alternatif, Anda dapat mengakses elemen tupel secara langsung menggunakan notasi titik dengan indeks elemen: `tup.0`, `tup.1`, `tup.2`.


```rust
// Creating a tuple with different types
let transaction: (&str, u64, bool) = ("abc123", 50000, true);

// Destructuring: extract all values at once
let (txid, amount, confirmed) = transaction;
println!("Transaction {} for {} sats", txid, amount);

// Dot notation: access individual elements by index
println!("Confirmed: {}", transaction.2);  // true

// Practical example: function returning multiple values
fn parse_utxo(data: &str) -> (String, u32, u64) {
// Returns (txid, output_index, value_in_sats)
("a]1b2c3".to_string(), 0, 100000)
}

let (txid, vout, value) = parse_utxo("raw_data");
println!("UTXO {}:{} = {} sats", txid, vout, value);
```


Larik dalam Rust berbeda secara signifikan dari larik atau daftar dalam banyak bahasa lain karena memiliki ukuran tetap yang menjadi bagian dari tipenya. Larik lima bilangan bulat memiliki tipe `[i32; 5]`, di mana titik koma memisahkan tipe elemen dari panjang larik. Informasi ukuran pada tingkat tipe ini memungkinkan kompiler untuk melakukan pengecekan batas dan memastikan bahwa fungsi yang menerima larik mengetahui dengan tepat berapa banyak elemen yang diharapkan.


Anda dapat menginisialisasi larik dengan mencantumkan semua elemen secara eksplisit: `[1, 2, 3, 4, 5]`, atau dengan menggunakan sintaksis singkatan untuk larik dengan nilai yang diulang: `[3; 5]` membuat larik dengan lima elemen, semuanya dengan nilai 3. Singkatan ini berguna untuk menginisialisasi buffer atau membuat larik dengan nilai default.


Akses larik menggunakan notasi tanda kurung siku seperti kebanyakan bahasa, tetapi Rust menyediakan pemeriksaan batas waktu kompilasi dan waktu proses. Ketika Anda mengakses larik dengan indeks konstan yang dapat diverifikasi oleh kompiler, kompiler akan menangkap akses di luar batas pada waktu kompilasi. Untuk indeks dinamis yang ditentukan pada saat runtime, Rust menyisipkan pemeriksaan batas yang akan menyebabkan program panik jika Anda mencoba mengakses indeks yang tidak valid, mencegah pelanggaran keamanan memori.



## Ownership dan Keamanan Memori di Rust

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


### Memahami Pendekatan Unik Rust untuk Manajemen Memori


Bab ini membahas salah satu konsep Rust yang paling penting. Meskipun konsep sebelumnya mungkin terasa akrab bagi programmer yang berasal dari bahasa lain, kepemilikan adalah pendekatan Rust untuk memecahkan keamanan memori tanpa pengumpulan sampah.


Rust didesain dengan tujuan mendasar untuk mencegah bug terkait memori yang mengganggu bahasa tingkat rendah seperti C dan C++. Masalah ini termasuk bug yang digunakan setelah bebas, di mana memori diakses setelah dilepaskan, dan buffer meluap, di mana program menulis di luar batas memori yang dialokasikan. Solusi tradisional untuk masalah ini melibatkan trade-off yang ingin dihilangkan oleh Rust. Bahasa tingkat tinggi seperti Java dan Go memecahkan keamanan memori melalui pengumpulan sampah, di mana proses otomatis secara berkala mengidentifikasi dan membebaskan memori yang tidak digunakan. Namun, pengumpul sampah memperkenalkan overhead kinerja dan dapat menyebabkan jeda yang tidak dapat diprediksi selama eksekusi program, sehingga tidak cocok untuk pemrograman sistem yang membutuhkan kinerja yang konsisten.


Rust mencapai keamanan memori terutama melalui analisis statis yang dilakukan pada waktu kompilasi. Kompiler memeriksa kode sumber dan dapat menentukan apakah sebagian besar operasi memori aman tanpa memerlukan pengumpulan sampah. Untuk kasus-kasus yang tidak dapat diverifikasi secara statis-seperti akses larik dengan indeks yang dihitung pada saat runtime-Rust menyisipkan pemeriksaan batas yang membuat panik dan tidak mengizinkan perilaku yang tidak terdefinisi. Pendekatan ini berbeda secara mendasar dari penganalisis statis yang tersedia untuk C dan C++, yang dipasang pada bahasa yang pada awalnya tidak dirancang untuk analisis statis yang komprehensif. Sintaks dan aturan bahasa Rust dibuat dari bawah ke atas untuk memungkinkan verifikasi waktu kompilasi yang ekstensif, memastikan bahwa setelah program berhasil dikompilasi, program akan berjalan dengan aman atau panik yang dapat diprediksi, daripada menunjukkan perilaku yang tidak terdefinisi.


### Sistem Ownership: Aturan dan Prinsip


Landasan jaminan keamanan memori Rust adalah sistem kepemilikan, yang mengatur bagaimana memori dikelola selama eksekusi program. Ownership beroperasi dengan tiga aturan dasar yang diterapkan oleh kompiler setiap saat:


1. Setiap nilai dalam Rust memiliki pemilik (variabel yang menyimpan nilai)

2. Hanya boleh ada satu pemilik dalam satu waktu

3. Ketika pemiliknya keluar dari cakupan, nilainya akan dihapus


Lingkup dalam Rust biasanya didefinisikan dengan tanda kurung kurawal, baik dalam badan fungsi, blok bersyarat, atau blok lingkup yang dibuat secara eksplisit. Ketika sebuah variabel dideklarasikan dalam sebuah scope, scope tersebut menjadi pemilik dari nilai variabel tersebut. Variabel tetap dapat diakses dan valid selama masa pakai scope, tetapi begitu eksekusi meninggalkan scope, semua variabel yang dimiliki secara otomatis dibersihkan melalui proses yang disebut dropping.


Pembersihan otomatis ini diimplementasikan melalui mekanisme drop Rust, di mana bahasa ini secara implisit memanggil fungsi drop pada variabel yang berada di luar cakupan. Untuk tipe dasar, ini berarti memori ditandai sebagai tersedia untuk digunakan kembali. Untuk tipe yang lebih kompleks yang mengelola sumber daya, implementasi drop khusus dapat melakukan operasi pembersihan tambahan, seperti menutup pegangan file atau melepaskan koneksi jaringan. Pola ini, yang dipinjam dari RAII (Resource Acquisition Is Initialization) dari C++, memastikan bahwa sumber daya selalu dilepaskan dengan benar tanpa memerlukan kode pembersihan eksplisit dari programmer.


### Memindahkan Ownership dan Tata Letak Memori


Untuk memahami bagaimana transfer kepemilikan antar variabel, kita perlu memeriksa perbedaan antara tipe sederhana dan tipe kompleks dalam hal tata letak memori dan perilaku penyalinan. Tipe sederhana seperti bilangan bulat, boolean, dan bilangan floating-point memiliki ukuran yang tetap dan diketahui pada saat kompilasi dan dapat disalin secara efisien. Ketika Anda menetapkan satu variabel integer ke variabel lainnya, Rust membuat salinan nilai yang lengkap dan independen, memungkinkan kedua variabel ada secara bersamaan tanpa masalah kepemilikan.


Tipe kompleks seperti string menghadirkan tantangan yang berbeda karena mengelola memori yang dialokasikan secara dinamis. String di Rust terdiri dari tiga komponen yang disimpan di tumpukan: penunjuk ke data karakter yang dialokasikan di tumpukan, panjang string saat ini, dan total kapasitas buffer yang dialokasikan. Struktur ini memungkinkan string untuk tumbuh dan menyusut secara efisien sambil mempertahankan pengetahuan tentang batas-batasnya. Ketika Anda menetapkan satu variabel String ke variabel lainnya, Rust dihadapkan pada pilihan: Rust dapat menyalin struktur berbasis tumpukan (membuat dua penunjuk ke data tumpukan yang sama) atau melakukan penyalinan mendalam terhadap semua data tumpukan.


Perilaku default Rust adalah memindahkan kepemilikan daripada menyalin, mentransfer data heap dari variabel sumber ke variabel tujuan dan membatalkan sumber. Pendekatan ini mencegah skenario berbahaya di mana beberapa variabel dapat memodifikasi memori heap yang sama atau di mana memori yang sama dapat dibebaskan beberapa kali ketika variabel keluar dari cakupan. Operasi pemindahan ini efisien karena hanya menyalin struktur berbasis tumpukan kecil, bukan data heap yang berpotensi besar, sambil menjaga keamanan memori dengan memastikan kepemilikan tunggal.


### Referensi dan Peminjaman


Meskipun pemindahan kepemilikan memberikan keamanan, namun hal ini dapat membatasi ketika Anda perlu menggunakan suatu nilai di beberapa tempat tanpa memindahkan kepemilikan. Rust mengatasi hal ini melalui peminjaman, yang memungkinkan fungsi dan variabel untuk mengakses data secara sementara tanpa mengambil alih kepemilikan. Sebuah referensi, yang dibuat dengan menggunakan operator ampersand, menyediakan akses hanya-baca ke sebuah nilai sambil membiarkan kepemilikan tetap pada variabel aslinya.


Referensi memungkinkan fungsi untuk beroperasi pada data tanpa mengkonsumsinya, sehingga memungkinkan untuk menggunakan nilai yang sama beberapa kali di seluruh program. Ketika Anda memberikan referensi ke sebuah fungsi, Anda meminjamkan data untuk sementara waktu, dan fungsi tersebut harus mengembalikan referensi sebelum pemilik asli dapat memperoleh kembali kontrol penuh. Metafora peminjaman ini mencerminkan sifat akses yang bersifat sementara: seperti halnya Anda meminjamkan buku kepada teman dengan tetap mempertahankan kepemilikannya, referensi mengizinkan akses sementara dengan tetap mempertahankan hubungan kepemilikan yang asli.


Referensi yang dapat diubah memperluas konsep ini untuk memungkinkan modifikasi data yang dipinjam, tetapi dengan batasan ketat untuk menjaga keamanan. Rust hanya mengizinkan satu referensi yang dapat diubah ke sepotong data pada waktu tertentu, mencegah perlombaan data di mana beberapa bagian dari suatu program mungkin secara bersamaan memodifikasi memori yang sama. Selain itu, Anda tidak dapat memiliki referensi yang dapat diubah dan tidak dapat diubah ke data yang sama secara bersamaan, karena hal ini dapat menyebabkan situasi di mana kode mengasumsikan data stabil sementara kode lain secara aktif memodifikasinya. Aturan-aturan ini diberlakukan pada waktu kompilasi, menghilangkan seluruh kelas bug konkurensi yang mengganggu bahasa pemrograman sistem lainnya.


```rust
fn main() {
let mut wallet_balance: u64 = 100_000; // 100,000 satoshis

// Immutable borrow: read the balance
let balance_ref = &wallet_balance;
println!("Current balance: {} sats", balance_ref);
// balance_ref goes out of scope here

// Mutable borrow: update the balance
let balance_mut = &mut wallet_balance;
*balance_mut += 50_000; // Receive payment
println!("After deposit: {} sats", balance_mut);
// balance_mut goes out of scope here

// Function that borrows immutably
fn display_balance(balance: &u64) {
println!("Balance check: {} sats", balance);
}

// Function that borrows mutably
fn deduct_fee(balance: &mut u64, fee: u64) {
*balance -= fee;
}

display_balance(&wallet_balance);
deduct_fee(&mut wallet_balance, 1_000);
println!("After fee: {} sats", wallet_balance); // 149,000
}
```


### Jenis dan Irisan Senar


Rust membedakan antara string literal dan tipe String, yang mencerminkan strategi manajemen memori dan kasus penggunaan yang berbeda. String literal disematkan secara langsung dalam biner yang dikompilasi dan memiliki tipe &str (potongan string), yang merepresentasikan tampilan ke dalam data string yang tidak dapat diubah. Literal ini efisien karena tidak memerlukan alokasi runtime, tetapi tidak dapat dimodifikasi karena merupakan bagian dari kode program.


Sebaliknya, tipe String mengelola memori yang dialokasikan secara dinamis dan dapat bertambah, menyusut, dan dimodifikasi pada saat runtime. Anda dapat membuat String dari sebuah literal menggunakan String::from() atau metode serupa, yang mengalokasikan memori heap dan menyalin konten literal. Perbedaan ini memungkinkan Rust untuk mengoptimalkan performa (menggunakan literal jika memungkinkan) dan fleksibilitas (menggunakan String jika diperlukan modifikasi).


Irisan string (&str) menyediakan abstraksi yang kuat untuk bekerja dengan bagian dari string tanpa menyalin data. Irisan berisi penunjuk ke awal data string dan panjangnya, sehingga Anda dapat mereferensikan substring secara efisien. Sintaks slice menggunakan rentang (misalnya, &s[0..5]) untuk menentukan bagian mana dari string yang akan direferensikan. Karena irisan adalah referensi, maka irisan tunduk pada aturan peminjaman, sehingga mencegah string yang mendasarinya dimodifikasi selama irisan masih ada. Penegakan waktu kompilasi ini mencegah bug yang umum terjadi seperti mengakses memori yang tidak valid setelah string asli dibebaskan atau dimodifikasi.


### Array, Vektor, dan Irisan Umum


Konsep slice meluas di luar string ke urutan elemen apa pun, menyediakan cara terpadu untuk bekerja dengan array ukuran tetap dan vektor dinamis. Larik dalam Rust memiliki panjang yang dikodekan dalam jenisnya (misalnya, [i32; 5] untuk larik lima bilangan bulat 32-bit), sehingga cocok untuk situasi yang membutuhkan jaminan ukuran waktu kompilasi. Fungsi yang menerima larik dapat menerapkan persyaratan panjang yang tepat, berguna untuk operasi seperti fungsi kriptografi yang membutuhkan input dengan ukuran yang tepat.


Irisan (&[T]) memberikan alternatif yang lebih fleksibel, yang merepresentasikan tampilan ke dalam urutan elemen yang bersebelahan terlepas dari penyimpanan yang mendasarinya. Anda dapat membuat irisan dari larik, vektor, atau irisan lain, dan irisan yang sama dapat merujuk ke bagian data yang berbeda selama masa pakainya. Fleksibilitas ini membuat irisan ideal untuk fungsi yang perlu memproses urutan tanpa peduli dengan mekanisme penyimpanan tertentu atau ukuran yang tepat.


Hubungan antara tipe-tipe yang dimiliki (String, Vec<T>) dan tipe-tipe yang dipinjam (&str, &[T]) mengikuti pola yang konsisten di seluruh Rust. Tipe yang dimiliki mengelola memori mereka dan dapat dimodifikasi, sementara slice menyediakan akses yang efisien dan hanya-baca ke bagian data tersebut. Desain ini memungkinkan API yang fleksibel (menerima berbagai jenis input melalui slices) dan efisien (menghindari penyalinan yang tidak perlu), sambil mempertahankan jaminan keamanan Rust melalui sistem peminjaman.



## Struktur, Membangun Tipe Data Kompleks

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

Struktur dalam Rust berfungsi sebagai fondasi untuk membuat tipe data yang kompleks, mirip dengan kelas dalam bahasa pemrograman lainnya. Struktur memungkinkan Anda untuk mengelompokkan data yang terkait menjadi satu unit kohesif yang dapat berisi beberapa field dengan tipe yang berbeda. Sintaks untuk mendefinisikan struktur mengikuti pola yang mudah: Anda menggunakan kata kunci `struct` diikuti dengan nama struktur, kemudian mendefinisikan field dalam kurung kurawal menggunakan sintaks titik dua untuk menentukan tipe setiap field.


Rust mengikuti konvensi penamaan khusus untuk struktur yang akan diberlakukan oleh kompilator melalui peringatan. Nama struktur harus menggunakan CamelCase (juga dikenal sebagai PascalCase), sementara nama field dalam struktur harus menggunakan snake_case dengan garis bawah. Konvensi ini membantu menjaga konsistensi di seluruh basis kode Rust dan membuat kode lebih mudah dibaca oleh pengembang lain.


Membuat instance struktur mengharuskan Anda untuk menentukan nilai untuk semua field menggunakan nama struktur diikuti dengan tanda kurung kurawal yang berisi penugasan field. Setelah Anda memiliki sebuah instance struktur, Anda dapat mengakses dan memodifikasi setiap field menggunakan notasi titik, asalkan instance tersebut dinyatakan sebagai mutable. Notasi titik ini bekerja secara konsisten di Rust, tidak seperti bahasa seperti C++ di mana Anda dapat menggunakan operator yang berbeda untuk pointer dibandingkan dengan objek langsung.


### Fungsi Pembuat dan Pintasan Bidang


Rust tidak memiliki konstruktor bawaan seperti beberapa bahasa berorientasi objek, tetapi Anda dapat membuat fungsi yang mengembalikan contoh struktur untuk melayani tujuan yang sama. Fungsi-fungsi konstruktor ini biasanya mengambil parameter untuk beberapa atau semua field dan dapat menetapkan nilai default untuk yang lain. Ketika menulis fungsi-fungsi seperti itu, Rust menyediakan sebuah singkatan yang mudah digunakan: jika sebuah parameter memiliki nama yang sama dengan sebuah field struktur, Anda cukup menulis nama field sekali saja dan tidak perlu mengulanginya dalam format `field: value`.


Instance struktur juga dapat dibuat dengan menyalin nilai dari instance yang sudah ada dengan menggunakan sintaks struct update. Fitur ini memungkinkan Anda untuk membuat instance baru sambil menentukan hanya field yang ingin Anda ubah, dengan semua field lainnya disalin dari instance yang sudah ada. Namun, operasi ini mengikuti aturan kepemilikan Rust, yang berarti bahwa tipe non-Copy akan dipindahkan dari instance sumber, yang berpotensi membuat sebagian instance asli tidak dapat digunakan setelahnya. Kompiler melacak pemindahan parsial ini dengan cerdas, memungkinkan Anda untuk terus menggunakan field yang tidak dipindahkan sambil mencegah akses ke field yang dipindahkan.


### Struktur Tuple dan Struktur Unit


Rust mendukung struktur tuple, yang merupakan struktur dengan field tanpa nama yang diakses berdasarkan indeks dan bukan berdasarkan nama. Ini berguna untuk jenis pembungkus sederhana atau ketika Anda membutuhkan struktur tetapi tidak memerlukan bidang bernama. Anda mengakses field struktur tuple menggunakan notasi titik yang diikuti dengan indeks field, seperti `.0` untuk field pertama, `.1` untuk field kedua, dan seterusnya. Pendekatan ini bekerja dengan baik untuk struktur yang membungkus nilai tunggal atau hanya berisi beberapa nilai yang terkait erat di mana nama mungkin berlebihan.


Struktur unit merupakan bentuk struktur yang paling sederhana - struktur ini tidak mengandung data sama sekali. Meskipun ini mungkin tampak tidak berguna pada awalnya, struktur unit menjadi berharga ketika bekerja dengan sistem sifat Rust, karena mereka dapat mengimplementasikan perilaku tanpa menyimpan data apa pun. Struktur kosong ini berfungsi sebagai penanda atau penampung dalam pola Rust yang lebih canggih.


### Metode dan Fungsi Terkait


Struktur mendapatkan fungsionalitas tambahan ketika Anda menambahkan perilaku melalui blok implementasi. Dengan menggunakan kata kunci `impl` yang diikuti dengan nama struktur, Anda bisa mendefinisikan metode yang beroperasi pada instance struktur Anda. Metode adalah fungsi yang mengambil `self` sebagai parameter pertama, yang bisa berupa nilai yang dimiliki (`self`), referensi yang tidak dapat diubah (`&self`), atau referensi yang dapat diubah (`&mut self`), tergantung pada apa yang harus dilakukan oleh metode tersebut terhadap instance.


Pilihan tipe parameter `self` menentukan perilaku metode terkait kepemilikan. Metode yang mengambil `&self` dapat membaca dari instance tanpa mengambil kepemilikan, sehingga cocok untuk operasi yang tidak mengubah struktur. Metode yang mengambil `&mut self` dapat memodifikasi instance sambil tetap mengizinkan pemanggil untuk mempertahankan kepemilikan. Metode yang mengambil nilai `self` mengkonsumsi instance, yang sesuai untuk operasi yang mengubah struktur menjadi sesuatu yang lain atau ketika metode tersebut merepresentasikan operasi terakhir pada instance tersebut.


Fungsi terkait adalah fungsi yang didefinisikan dalam blok implementasi yang tidak menggunakan `diri` sebagai parameter. Fungsi ini mirip dengan metode statis dalam bahasa lain dan biasanya digunakan sebagai konstruktor atau fungsi utilitas yang terkait dengan tipe. Anda memanggil fungsi terkait menggunakan sintaks titik dua ganda (`Type::nama_fungsi()`), yang dengan jelas membedakannya dari metode yang dipanggil pada instance.


```rust
// Define a struct for a Lightning invoice
struct Invoice {
payment_hash: String,
amount_msat: u64,
description: String,
expiry_secs: u32,
}

impl Invoice {
// Associated function (constructor) - no self parameter
fn new(payment_hash: String, amount_msat: u64, description: String) -> Self {
Invoice {
payment_hash,
amount_msat,
description,
expiry_secs: 3600, // default 1 hour
}
}

// Method with &self - read-only access
fn amount_sats(&self) -> u64 {
self.amount_msat / 1000
}

// Method with &mut self - can modify the instance
fn extend_expiry(&mut self, additional_secs: u32) {
self.expiry_secs += additional_secs;
}

// Method with self - consumes the instance
fn into_payment_request(self) -> String {
format!("lnbc{}n1p{}", self.amount_msat, self.payment_hash)
}
}

fn main() {
// Use associated function to create instance
let mut invoice = Invoice::new(
"abc123".to_string(),
100_000_000, // 100,000 sats in millisats
"Coffee payment".to_string(),
);

println!("Amount: {} sats", invoice.amount_sats());
invoice.extend_expiry(1800); // Add 30 minutes

let request = invoice.into_payment_request();
// invoice is now consumed, cannot be used anymore
println!("Payment request: {}", request);
}
```


#### Pencacahan: Pilihan dan Varian Pemodelan


Enumerasi dalam Rust memiliki lebih banyak kemampuan daripada enum dalam banyak bahasa lain. Selain dapat mewakili kumpulan konstanta bernama yang sederhana, enum Rust juga dapat membawa data dalam setiap varian, sehingga cocok untuk memodelkan situasi di mana suatu nilai dapat berupa salah satu dari beberapa jenis atau status yang berbeda. Setiap varian enum dapat berisi jenis dan jumlah data yang berbeda, dari tidak ada data sama sekali hingga struktur kompleks dengan bidang bernama.


Kemampuan untuk melampirkan data ke varian enum menghilangkan banyak kesalahan pemrograman yang umum ditemukan dalam bahasa lain. Alih-alih mempertahankan variabel terpisah untuk indikator tipe dan data terkait - yang dapat dengan mudah menjadi tidak konsisten - enum Rust menggabungkan informasi tipe dengan data itu sendiri. Desain ini memastikan bahwa data selalu cocok dengan variannya, mencegah ketidakcocokan yang dapat menyebabkan kesalahan runtime.


Varian enum dapat berisi data dalam beberapa bentuk: tidak ada data untuk flag sederhana, data seperti tuple untuk field yang tidak bernama, atau data seperti struktur dengan field bernama. Anda bahkan dapat mencampur gaya ini dalam satu enum, memilih bentuk yang paling sesuai untuk setiap varian. Fleksibilitas ini membuat enum cocok untuk memodelkan konsep domain yang kompleks di mana kasus yang berbeda memerlukan informasi yang berbeda.


#### Jenis Opsi: Menangani Ketidakhadiran dengan Aman


Salah satu enum yang paling penting dalam Rust adalah `Option<T>`, yang merepresentasikan nilai yang mungkin ada atau tidak ada. Enum ini memiliki dua varian: `Some(T)` yang berisi nilai tipe T, dan `None` yang merepresentasikan ketiadaan nilai. Tipe Option berfungsi sebagai solusi Rust untuk masalah penunjuk nol yang menjangkiti banyak bahasa lain, memaksa pengembang untuk secara eksplisit menangani kasus-kasus di mana nilai mungkin hilang.


Menggunakan tipe Option membuat kode Anda lebih kuat karena kompiler mengharuskan Anda untuk menangani keberadaan dan ketiadaan nilai. Anda tidak dapat secara tidak sengaja menggunakan nilai yang berpotensi hilang tanpa terlebih dahulu memeriksa apakah nilai tersebut ada. Penanganan eksplisit ini mencegah pengecualian penunjuk nol dan kesalahan runtime yang serupa yang merupakan sumber umum bug dalam bahasa pemrograman lain.


Tipe Option terintegrasi dengan sistem pencocokan pola Rust, sehingga Anda dapat menangani kedua kasus tersebut. Metode seperti `unwrap_or()` menyediakan cara yang mudah untuk mengekstrak nilai dengan default fallback, sementara metode seperti `map()` dan `and_then()` memungkinkan pola pemrograman fungsional untuk bekerja dengan nilai opsional.


### Pencocokan Pola dengan Ekspresi Kecocokan


Pencocokan pola melalui ekspresi `match` menyediakan cara untuk bekerja dengan enum dan tipe data lainnya. Ekspresi pencocokan memeriksa sebuah nilai dan mengeksekusi kode yang berbeda berdasarkan pola mana yang cocok dengan nilai tersebut. Setiap pola dapat merusak nilai yang dicocokkan, mengikat bagian dari nilai tersebut ke variabel yang dapat digunakan dalam blok kode yang sesuai.


Ekspresi pencocokan harus lengkap, yang berarti ekspresi tersebut harus menangani setiap kasus yang mungkin terjadi pada tipe yang dicocokkan. Persyaratan ini mencegah bug yang dapat terjadi jika kasus tertentu secara tidak sengaja tidak ditangani. Jika Anda tidak ingin menangani setiap kasus secara eksplisit, Anda dapat menggunakan pola wildcard (`_`) untuk menangkap semua kasus yang tersisa, atau mengikat kasus yang tidak ditangani ke variabel jika Anda memerlukan akses ke nilai.


Konstruksi `if let` memberikan alternatif yang lebih ringkas untuk mencocokkan ketika Anda hanya peduli dengan satu pola tertentu. Sintaks ini sangat berguna ketika bekerja dengan tipe Option atau ketika Anda ingin mengeksekusi kode hanya jika sebuah nilai cocok dengan varian enum tertentu. Konstruksi `if let` dapat menyertakan klausa `else` untuk kasus-kasus di mana pola tidak cocok, menjadikannya cara yang efisien untuk menangani skenario pencocokan pola sederhana.


#### Koleksi: Mengelola Kelompok Data


Perpustakaan standar Rust menyediakan beberapa jenis koleksi untuk mengelola kelompok data terkait. Koleksi-koleksi ini bersifat umum, yang berarti mereka dapat menyimpan elemen jenis apa pun, dan mereka menangani manajemen memori secara otomatis. Koleksi yang paling umum digunakan adalah vektor untuk daftar terurut, peta hash untuk asosiasi nilai-kunci, dan string untuk data teks.


#### Vektor: Larik Dinamis


Vektor mewakili larik yang dapat berkembang yang dapat mengubah ukuran selama eksekusi program. Tidak seperti larik dengan ukuran tetap, vektor mengalokasikan memori pada heap dan dapat membesar atau mengecil sesuai kebutuhan. Membuat vektor sering kali membutuhkan anotasi tipe eksplisit ketika memulai dengan vektor kosong, karena kompiler perlu mengetahui jenis elemen apa yang akan berisi vektor tersebut.


Vektor menyediakan beberapa cara untuk mengakses elemen, masing-masing dengan karakteristik keamanan yang berbeda. Notasi indeks (`vec [0]`) menyediakan akses langsung tetapi akan panik jika indeks berada di luar batas. Metode `get () ` mengembalikan sebuah `Opsi`, yang memungkinkan Anda untuk menangani akses di luar batas dengan baik. Pilihan di antara pendekatan-pendekatan ini tergantung pada apakah Anda dapat menjamin indeks tersebut valid atau perlu menangani potensi kegagalan.


Aturan peminjaman Rust berlaku untuk vektor, sehingga mencegah masalah keamanan memori yang umum terjadi. Jika Anda memegang referensi ke elemen vektor, Anda tidak dapat memodifikasi vektor sampai referensi tersebut keluar dari cakupan. Hal ini mencegah situasi di mana referensi dapat mengarah ke memori yang tidak teralokasi setelah operasi vektor seperti memasukkan elemen baru atau menghapus vektor.


#### Peta Hash: Penyimpanan Nilai Kunci


Peta Hash menyediakan penyimpanan nilai-kunci yang efisien di mana Anda dapat dengan cepat mencari nilai berdasarkan kunci yang terkait. Kunci dan nilai dapat berupa jenis apa pun, meskipun kunci harus mengimplementasikan sifat-sifat yang diperlukan untuk hashing dan perbandingan kesetaraan. Peta Hash mengambil kepemilikan atas nilai yang disisipkan kecuali jika nilai tersebut mengimplementasikan sifat Copy.


Peta Hash menawarkan beberapa metode untuk menyisipkan dan memperbarui nilai. Metode dasar `insert () ` akan menimpa nilai yang sudah ada, sedangkan `entry () ` menyediakan logika penyisipan yang lebih fleksibel. Entri API memungkinkan Anda untuk menyisipkan nilai hanya jika nilai tersebut belum ada, atau untuk memperbarui nilai yang ada berdasarkan kondisi saat ini. API ini berguna untuk pola-pola seperti menghitung kejadian atau mempertahankan total yang sedang berjalan.


Ketika mengambil nilai dari peta hash, metode `get()` mengembalikan sebuah `Opsi` karena kunci yang diminta mungkin tidak ada. Anda dapat menggunakan metode seperti `copied()` untuk mengkonversi dari `Option<&T>` ke `Option<T>` untuk tipe Copy, dan `unwrap_or()` untuk memberikan nilai default ketika kunci tidak ada.


### Penanganan String dan Unicode


String dalam Rust dikodekan dengan UTF-8, yang menyediakan dukungan Unicode penuh tetapi menimbulkan kerumitan dibandingkan dengan string ASCII yang sederhana. Tipe `String` mewakili data teks yang dimiliki dan dapat dikembangkan, sedangkan potongan string (`&str`) menyediakan tampilan yang dipinjam ke dalam data string. Anda dapat mengkonversi antara tipe-tipe ini sesuai kebutuhan, dengan irisan string yang sering digunakan untuk parameter fungsi untuk menerima string yang dimiliki dan string literal.


Manipulasi string mencakup metode untuk menambahkan teks, memformat beberapa nilai secara bersamaan, dan mengekstrak substring. Metode `push_str()` menambahkan potongan string tanpa mengambil alih kepemilikan, sedangkan makro `format!` menyediakan cara yang fleksibel untuk membuat string dari beberapa komponen. Ketika bekerja dengan indeks string, Anda harus berhati-hati untuk menghormati batas karakter UTF-8 untuk menghindari kepanikan saat runtime.


Untuk pemrosesan karakter per karakter yang aman, string menyediakan metode iterator seperti `chars()` untuk nilai skalar Unicode dan `bytes()` untuk akses byte mentah. Iterator ini menangani pengkodean UTF-8 dengan benar, memastikan Anda tidak secara tidak sengaja membagi karakter multi-byte. Pendekatan ini lebih aman dan lebih dapat diandalkan daripada pengindeksan manual, terutama ketika bekerja dengan teks internasional yang mungkin berisi karakter Unicode yang kompleks.



## Sistem Penanganan Kesalahan Dua Kategori Rust

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

Rust mengambil pendekatan yang berbeda secara fundamental untuk penanganan kesalahan dibandingkan dengan kebanyakan bahasa pemrograman. Sementara banyak bahasa mengandalkan pengecualian, Rust membedakan antara dua kategori kesalahan yang berbeda dan menyediakan mekanisme khusus untuk menangani setiap jenis kesalahan. Bab ini membahas sistem penanganan kesalahan Rust yang komprehensif, yang mencakup kesalahan yang tidak dapat dipulihkan yang menghentikan eksekusi program dan kesalahan yang dapat dipulihkan yang memungkinkan program untuk terus berjalan dengan baik.


### Kesalahan dan Kepanikan yang Tidak Dapat Dipulihkan


Kesalahan yang tidak dapat dipulihkan mewakili situasi di mana program telah memasuki kondisi yang tidak konsisten atau tidak terduga yang tidak dapat dipulihkan dengan aman. Ini termasuk skenario seperti mengakses larik di luar batas, mencoba operasi yang melanggar keamanan memori, atau menghadapi kondisi yang mengindikasikan kesalahan logika program yang mendasar. Ketika kesalahan seperti itu terjadi, respons yang tepat adalah menghentikan program dengan segera daripada mengambil risiko kerusakan lebih lanjut atau perilaku yang tidak terdefinisi.


Dalam Rust, kesalahan yang tidak dapat dipulihkan memicu kepanikan, yang menyebabkan program mengalami crash secara terkendali. Sebelum mengakhiri, Rust melakukan proses yang disebut unwinding, di mana ia berjalan kembali melalui tumpukan panggilan untuk memberikan jejak tumpukan terperinci yang menunjukkan dengan tepat di mana kepanikan terjadi. Proses unwinding ini membantu pengembang mengidentifikasi sumber masalah selama debugging. Untuk aplikasi yang sangat penting dalam hal kinerja atau sistem tertanam, Anda dapat menonaktifkan unwinding dan mengonfigurasi Rust untuk segera membatalkan ketika terjadi kepanikan, meskipun hal ini mengorbankan informasi debugging untuk penghentian yang lebih cepat.


Anda dapat memicu kepanikan secara eksplisit menggunakan makro `panic!` dengan pesan khusus. Ketika kepanikan terjadi, Anda akan melihat output yang menunjukkan thread mana yang panik dan pesan terkait. Mengatur variabel lingkungan `RUST_BACKTRACE` menyediakan informasi debug tambahan, yang menunjukkan tumpukan panggilan lengkap yang menyebabkan kepanikan. Sebagai contoh, mencoba mengakses elemen 99 dari vektor yang hanya berisi tiga elemen akan membuat generate panik dengan pesan "indeks di luar batas", bersama dengan backtrace yang menunjukkan urutan yang tepat dari pemanggilan fungsi yang mengakibatkan kesalahan.


### Kesalahan yang Dapat Dipulihkan dengan Hasil


Kesalahan yang dapat dipulihkan mewakili kondisi kegagalan yang diharapkan yang dapat ditangani oleh program dengan baik tanpa harus dihentikan. Contohnya termasuk mencoba membuka file yang tidak ada, kegagalan koneksi jaringan, atau input pengguna yang tidak valid. Untuk situasi ini, Rust menyediakan enum `Result`, yang secara eksplisit merepresentasikan operasi yang mungkin gagal dan memaksa pengembang untuk menangani kasus sukses dan gagal.


Enum `Hasil` didefinisikan dengan dua varian: `Ok(T)` untuk operasi yang berhasil yang mengandung nilai tipe `T`, dan `Error(E)` untuk kegagalan yang mengandung kesalahan tipe `E`. Desain ini menggunakan sistem tipe Rust untuk memastikan bahwa potensi kegagalan tidak dapat diabaikan. Fungsi yang mungkin gagal mengembalikan `Hasil`, dan kode pemanggilan harus secara eksplisit menangani kasus keberhasilan dan kesalahan, biasanya menggunakan pencocokan pola dengan ekspresi `cocok`.


Perhatikan fungsi `File::open`, yang mengembalikan `Hasil<File, std::io::Error>`. Ketika membuka sebuah file, Anda akan menerima objek `File` jika berhasil atau `std::io::Error` jika operasi gagal. Anda dapat mencocokkan hasil ini untuk menangani setiap kasus dengan tepat. Pada kasus sukses, Anda dapat melanjutkan dengan operasi file, sedangkan pada kasus gagal, Anda dapat mencoba membuat file, mencoba pendekatan alternatif, atau menyebarkan kesalahan ke kode pemanggilan. Penanganan eksplisit ini memastikan bahwa program Anda membuat keputusan secara sadar tentang pemulihan kesalahan daripada crash secara tiba-tiba.


### Pola Penanganan Kesalahan dan Pintasan


Meskipun pencocokan pola eksplisit memberikan kontrol penuh atas penanganan kesalahan, Rust menawarkan beberapa metode kemudahan untuk pola penanganan kesalahan yang umum. Metode `unwrap` mengekstrak nilai keberhasilan dari `Hasil` tetapi panik jika terjadi kesalahan, membuatnya berguna untuk pembuatan prototipe cepat atau situasi di mana Anda yakin operasi akan berhasil. Metode `expect` bekerja dengan cara yang sama tetapi memungkinkan Anda untuk memberikan pesan panik khusus, membuat debugging lebih mudah ketika terjadi kesalahan.


Untuk penanganan kesalahan yang lebih fleksibel, metode seperti `unwrap_or_else` memungkinkan Anda untuk menyediakan penutupan yang dieksekusi ketika terjadi kesalahan, sehingga memungkinkan logika pemulihan khusus. Anda dapat merangkai operasi ini bersama-sama untuk menangani skenario yang rumit, seperti mencoba membuka file dan membuatnya jika tidak ada, dengan strategi penanganan kesalahan yang berbeda untuk setiap langkah.


Operator tanda tanya (`?`) menyediakan sintaks yang ringkas untuk penyebaran kesalahan, yang umum digunakan pada program Rust. Ketika Anda menambahkan `?` ke `Hasil`, maka secara otomatis akan membuka nilai yang berhasil dan mengembalikan kesalahan dengan segera dari fungsi yang sedang berjalan. Operator ini hanya dapat digunakan dalam fungsi yang mengembalikan tipe `Hasil`, memastikan bahwa kesalahan dapat disebarkan dengan benar ke atas tumpukan panggilan. Operator `?` membuat kode penanganan kesalahan menjadi lebih mudah dibaca dengan menghilangkan ekspresi pencocokan yang bertele-tele sambil mempertahankan semantik penyebaran kesalahan secara eksplisit.


```rust
use std::fs::File;
use std::io::{self, Read};

// Custom error type for wallet operations
#[derive(Debug)]
enum WalletError {
FileNotFound,
InvalidFormat,
InsufficientFunds,
}

// Function returning Result for recoverable errors
fn load_wallet_balance(path: &str) -> Result<u64, WalletError> {
// Simulate reading from file
let balance_str = "150000"; // Would normally read from file
balance_str
.parse::<u64>()
.map_err(|_| WalletError::InvalidFormat)
}

// Using the ? operator for clean error propagation
fn send_payment(amount: u64) -> Result<String, WalletError> {
let balance = load_wallet_balance("wallet.dat")?; // Propagates error if it fails

if balance < amount {
return Err(WalletError::InsufficientFunds);
}

Ok(format!("Sent {} sats, remaining: {}", amount, balance - amount))
}

fn main() {
// Handle the Result explicitly
match send_payment(50_000) {
Ok(msg) => println!("Success: {}", msg),
Err(WalletError::InsufficientFunds) => println!("Error: Not enough funds"),
Err(WalletError::FileNotFound) => println!("Error: Wallet file not found"),
Err(WalletError::InvalidFormat) => println!("Error: Corrupted wallet file"),
}

// Or use unwrap_or_else for custom fallback
let result = send_payment(200_000)
.unwrap_or_else(|e| format!("Payment failed: {:?}", e));
println!("{}", result);
}
```


### Perambatan Kesalahan dan Desain Fungsi


Perambatan kesalahan adalah konsep mendasar dalam penanganan kesalahan Rust, yang memungkinkan fungsi-fungsi melewatkan kesalahan pada tumpukan panggilan daripada menanganinya secara lokal. Ketika mendesain fungsi yang mungkin gagal, Anda harus mengembalikan tipe `Result` untuk memberikan fleksibilitas kepada pemanggil untuk memutuskan bagaimana menangani kesalahan. Pendekatan ini mendorong penanganan kesalahan yang dapat dikomposisikan di mana setiap fungsi dalam rantai pemanggilan dapat menangani kesalahan secara lokal atau meneruskannya ke kode tingkat yang lebih tinggi yang memiliki lebih banyak konteks untuk membuat keputusan pemulihan.


Operator tanda tanya menyederhanakan penyebaran kesalahan. Daripada menulis ekspresi pencocokan yang bertele-tele untuk setiap operasi yang berpotensi gagal, Anda dapat merangkai operasi bersama dengan operator `?`, membuat kode yang dapat dibaca yang menangani jalur keberhasilan sambil secara otomatis menyebarkan kesalahan yang terjadi. Pola ini sangat umum sehingga banyak fungsi Rust dirancang khusus untuk bekerja dengan baik dengan operator `?`, memungkinkan penanganan kesalahan yang lancar di seluruh basis kode Anda.


Ketika memutuskan antara panik dan mengembalikan kesalahan, pertimbangkan apakah kode pemanggilan dapat pulih secara wajar dari kegagalan. Jika kegagalan merupakan kesalahan pemrograman atau kondisi sistem yang tidak dapat dipulihkan, maka panik adalah hal yang tepat. Namun, jika kegagalan merupakan kondisi yang diharapkan yang mungkin ditangani oleh kode pemanggilan secara berbeda tergantung pada konteksnya, mengembalikan `Hasil` memberikan fleksibilitas dan kompabilitas yang lebih baik.


### Praktik Terbaik dan Pertimbangan Desain


Penanganan kesalahan yang efektif di Rust membutuhkan pertimbangan yang cermat tentang kapan harus panik versus kapan harus mengembalikan kesalahan. Gunakan panik untuk situasi yang mewakili kesalahan pemrograman atau kondisi yang seharusnya tidak pernah terjadi pada program yang benar, seperti mengakses data yang sudah dikodekan yang Anda ketahui valid. Sebagai contoh, mem-parsing string alamat IP yang sudah diverifikasi bahwa Anda sudah benar, bisa dengan aman menggunakan `expect` dengan pesan deskriptif yang menjelaskan mengapa operasi tidak boleh gagal.


Untuk input yang dikendalikan pengguna atau interaksi sistem eksternal, selalu lebih memilih untuk mengembalikan tipe `Hasil` daripada panik. Pengguna melakukan kesalahan, file terhapus, dan koneksi jaringan gagal - ini adalah kondisi normal yang harus ditangani oleh program yang dirancang dengan baik. Dengan mengembalikan kesalahan untuk situasi ini, Anda mengizinkan pemanggilan kode untuk mengimplementasikan strategi pemulihan yang tepat, apakah itu meminta pengguna untuk memasukkan input yang berbeda, kembali ke nilai default, atau menampilkan pesan kesalahan yang bermanfaat.


Pertimbangkan untuk membuat tipe khusus yang memberlakukan validasi pada saat konstruksi untuk mencegah state yang tidak valid menyebar ke seluruh program Anda. Sebagai contoh, jika program Anda membutuhkan angka dalam rentang tertentu, buat tipe pembungkus yang memvalidasi input selama konstruksi dan tidak menyediakan cara untuk membuat instance yang tidak valid. Pendekatan ini menggunakan sistem tipe Rust untuk menghilangkan seluruh kelas kesalahan dengan membuat state yang tidak valid tidak dapat direpresentasikan, sehingga mengurangi kebutuhan pemeriksaan kesalahan runtime di seluruh basis kode Anda.


## Fitur Pemrograman Fungsional, Penutupan, dan Penunjuk Cerdas


<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Meskipun Rust bukan bahasa pemrograman fungsional murni, Rust menggabungkan fitur-fitur yang terinspirasi oleh paradigma pemrograman fungsional. Fitur-fitur ini memungkinkan pengembang untuk menulis kode yang ringkas dengan memanfaatkan konsep-konsep seperti penutupan dan iterator. Rust menyertakan elemen-elemen fungsional ini untuk menyediakan alat yang fleksibel untuk pemrosesan data dan mekanisme pemanggilan kembali.


Fitur pemrograman fungsional dalam Rust mempertahankan prinsip-prinsip inti bahasa tentang keamanan memori dan abstraksi tanpa biaya. Ketika Anda menggunakan penutupan dan iterator, Anda tidak mengorbankan kinerja untuk ekspresif - kompiler Rust mengoptimalkan konstruksi ini untuk menghasilkan kode mesin yang efisien yang sebanding dengan pendekatan berbasis perulangan tradisional.


### Memahami Penutupan


Closures dalam Rust adalah fungsi anonim yang dapat menangkap variabel dari lingkungan sekitarnya. Dalam bahasa pemrograman lain, ini sering disebut fungsi lambda. Karakteristik utama dari closure adalah kemampuannya untuk "menutup" lingkungannya, yang berarti mereka dapat mengakses dan menggunakan variabel yang ada di dalam ruang lingkup di mana closure didefinisikan.


Sintaks untuk penutupan menggunakan karakter pipa (`|`) alih-alih tanda kurung untuk mendefinisikan parameter. Untuk closure tanpa parameter, Anda menulis `||`, dan untuk closure dengan parameter, Anda mencantumkannya di antara pipa seperti `|x, y|`. Jika badan penutup terdiri dari satu ekspresi, Anda dapat menghilangkan tanda kurung kurawal, sehingga sintaksnya menjadi sangat ringkas.


Pertimbangkan contoh praktis dari perusahaan kaos yang memberikan kaos eksklusif berdasarkan preferensi pelanggan. Jika pelanggan telah menentukan warna favorit, mereka akan menerima warna tersebut; jika tidak, mereka akan mendapatkan warna yang paling banyak tersedia sebagai default. Dengan menggunakan penutupan, logika ini menjadi: `user_preference.unwrap_or_else(|| self.most_stocked())`. Penutupan `|| self.most_stocked())` memberikan nilai default hanya jika diperlukan, dan dapat mengakses `self` dari lingkungannya.


### Inferensi dan Fleksibilitas Jenis Penutupan


Salah satu fitur Rust yang paling nyaman dengan penutupan adalah inferensi tipe otomatis. Tidak seperti fungsi biasa di mana Anda harus secara eksplisit menentukan tipe parameter dan tipe pengembalian, closure sering kali dapat menyimpulkan tipe-tipe ini dari konteks. Kompiler menganalisa bagaimana closure digunakan dan menentukan tipe yang sesuai secara otomatis. Namun, sekali sebuah closure dipanggil dengan tipe tertentu, tipe-tipe tersebut menjadi tetap untuk instance closure tersebut.


Anda dapat menyimpan closure dalam variabel seperti halnya nilai lainnya, menjadikannya warga kelas satu dalam bahasa. Ketika Anda menetapkan sebuah closure ke sebuah variabel, Anda bisa memanggilnya nanti dengan menggunakan tanda kurung: `let my_closure = |x| x + 1; let hasil = my_closure(5);`. Fleksibilitas ini memungkinkan Anda untuk memberikan closure sebagai argumen ke fungsi, mengembalikannya dari fungsi, dan menggunakannya dalam struktur data.


Jika kompiler tidak dapat menyimpulkan tipe atau jika Anda ingin lebih eksplisit, Anda dapat menganotasi parameter penutupan dan pengembalian tipe menggunakan sintaksis yang mirip dengan fungsi: `|x: i32| -> i32 { x + 1 }`. Pengetikan eksplisit ini terkadang diperlukan dalam skenario yang rumit di mana kompilator membutuhkan informasi tambahan untuk menyelesaikan tipe dengan benar.


### Menangkap Variabel Lingkungan


Penutup dapat menangkap variabel dari lingkungannya dengan tiga cara yang berbeda: dengan referensi yang tidak dapat diubah, dengan referensi yang dapat diubah, atau dengan mengambil kepemilikan. Kompiler Rust secara otomatis menentukan metode pengambilan yang paling ketat yang memenuhi kebutuhan closure Anda, mengikuti prinsip hak istimewa yang paling sedikit.


Ketika sebuah closure hanya perlu membaca sebuah nilai, maka closure tersebut akan menangkap dengan referensi yang tidak dapat diubah. Hal ini memungkinkan variabel asli tetap dapat diakses setelah closure didefinisikan dan dipanggil. Sebagai contoh, sebuah closure yang mencetak sebuah daftar akan meminjam daftar tersebut secara permanen, sehingga Anda dapat terus menggunakan daftar tersebut setelah closure dijalankan.


Jika sebuah closure perlu memodifikasi variabel yang ditangkap, maka closure tersebut harus menangkap dengan referensi yang dapat diubah. Dalam kasus ini, baik variabel yang ditangkap dan closure itu sendiri harus dideklarasikan sebagai mutable. Penutupan kemudian dapat memodifikasi variabel yang ditangkap, tetapi aturan peminjaman masih berlaku - Anda tidak dapat memiliki referensi lain ke variabel tersebut selama penutup yang dapat diubah ada.


Metode penangkapan yang paling ketat adalah mengambil kepemilikan, yang memindahkan variabel yang ditangkap ke dalam penutupan. Hal ini diperlukan ketika penutupan mungkin lebih lama dari ruang lingkup di mana variabel-variabel tersebut awalnya didefinisikan, seperti ketika memunculkan thread. Anda bisa memaksa pengambilan kepemilikan menggunakan kata kunci `move` sebelum parameter penutupan: `pindah |x| { /* badan penutupan */ }`. Hal ini penting untuk keamanan thread, karena thread tidak bisa meminjam dari thread lain yang mungkin menghentikan dan membuang variabelnya.


### Sifat dan Jenis Fungsi Penutupan


Rust merepresentasikan penutupan melalui sistem sifat dengan tiga sifat utama: `FnOnce`, `FnMut`, dan `Fn`. Sifat-sifat ini membentuk sebuah hirarki yang menjelaskan bagaimana penutupan dapat dipanggil dan apa yang dapat dilakukan dengan variabel yang ditangkap.


`FnOnce` adalah sifat paling dasar yang diimplementasikan oleh semua penutupan. Ini merepresentasikan penutupan yang dapat dipanggil setidaknya sekali. Beberapa closure, terutama yang memindahkan nilai yang diambil atau mengkonsumsinya dengan cara tertentu, hanya bisa dipanggil sekali karena mereka menghancurkan atau memindahkan data yang diambil selama eksekusi.


`FnMut` merepresentasikan penutupan yang dapat dipanggil beberapa kali dan dapat mengubah lingkungan yang ditangkap. Penutupan ini menangkap variabel dengan referensi yang dapat diubah dan dapat memodifikasinya di beberapa pemanggilan. Aturan peminjaman memastikan bahwa ketika sebuah closure `FnMut` aktif, ia memiliki akses eksklusif yang dapat diubah ke variabel yang ditangkap.


`Fn` adalah sifat yang paling ketat, mewakili penutupan yang dapat dipanggil beberapa kali tanpa mengubah lingkungan yang ditangkap. Penutupan ini hanya menangkap dengan referensi yang tidak dapat diubah dan dapat dipanggil secara bersamaan tanpa melanggar jaminan keamanan Rust. Jika sebuah closure mengimplementasikan `Fn`, maka secara otomatis mengimplementasikan `FnMut` dan `FnOnce` juga, karena dapat dipanggil beberapa kali tanpa mutasi mengimplikasikan dapat dipanggil dengan mutasi dan dapat dipanggil sekali.


### Bekerja dengan Iterator


Iterator dalam Rust menyediakan cara untuk memproses urutan data. Iterator bersifat malas, artinya tidak melakukan pekerjaan apa pun hingga Anda mengonsumsinya dengan memanggil metode yang benar-benar mengulang data. Evaluasi malas ini memungkinkan perangkaian operasi yang efisien tanpa membuat koleksi perantara.


Sifat `Iterator` mendefinisikan fungsionalitas inti dengan tipe terkait `Item` yang merepresentasikan apa yang dihasilkan oleh iterator, dan metode `next` yang menghasilkan `Option<Self::Item>`. Ketika `next` mengembalikan `None`, iterator akan habis. Desain ini memungkinkan iterator untuk merepresentasikan urutan yang terbatas dan berpotensi tak terbatas dengan aman.


Anda bisa membuat iterator dari koleksi menggunakan metode seperti `iter()` untuk meminjam iterasi, `iter_mut()` untuk meminjam iterasi yang dapat diubah, dan `into_iter()` untuk mengkonsumsi iterasi. Pilihan di antara metode-metode ini tergantung pada apakah Anda perlu memodifikasi elemen dan apakah Anda ingin mengkonsumsi koleksi asli.


### Adopter dan Konsumen Iterator


Adaptor iterator adalah metode yang mengubah satu iterator menjadi iterator lainnya, sehingga Anda dapat menggabungkan operasi secara berantai. Adapter yang umum termasuk `map` untuk mentransformasikan setiap elemen, `filter` untuk memilih elemen berdasarkan predikat, dan `enumerate` untuk menambahkan indeks. Adaptor ini bersifat malas - mereka tidak melakukan pekerjaan apa pun sampai digunakan.


Metode `map` menerapkan penutupan pada setiap elemen, mengubahnya menjadi sesuatu yang lain. Sebagai contoh, `numbers.iter().map(|x| x * 2)` membuat sebuah iterator yang menggandakan setiap angka. Metode `filter` hanya menyimpan elemen-elemen yang penutupan predikatnya bernilai benar: `numbers.iter().filter(|&x| x > 10)` hanya menyimpan angka-angka yang lebih besar dari sepuluh.


Metode konsumen sebenarnya mengulang data dan menghasilkan hasil akhir. Metode `collect` menggunakan iterator dan membuat koleksi darinya. Anda sering kali perlu menentukan tipe koleksi: `let vec: Vec<_> = iterator.collect()`. Konsumen lain termasuk `sum` untuk menambahkan elemen numerik, `fold` untuk mengumpulkan nilai dengan operasi khusus, dan `for_each` untuk mengeksekusi efek samping pada setiap elemen.


### Pola Iterator Tingkat Lanjut


Operasi iterator tambahan termasuk `zip` untuk menggabungkan dua iterator berdasarkan elemen, `chain` untuk menggabungkan iterator, dan `filter_map` untuk menggabungkan pemfilteran dan pemetaan dalam satu operasi. Metode `zip` membuat pasangan dari elemen-elemen yang sesuai dari dua iterator: `a.iter().zip(b.iter())` menghasilkan tupel `(a[0], b[0]), (a[1], b[1]), ...`.


Metode `fold` berguna untuk mengumpulkan nilai. Metode ini membutuhkan sebuah nilai awal dan sebuah penutup yang menggabungkan akumulator dengan setiap elemen: `numbers.iter().fold(0, |acc, x| acc + x)` menjumlahkan semua angka. Pola ini dapat mengimplementasikan banyak operasi lain seperti mencari nilai maksimum, membangun string, atau membuat struktur data yang kompleks.


Rangkaian iterator dapat mengekspresikan transformasi data yang kompleks secara ringkas. Sebagai contoh, pemrosesan data audio mungkin melibatkan: `coefficients.iter().zip(buffer.iter()).map(|(c, b)| c * b).sum::<i32>() >> 12`. Ini mengalikan koefisien dan nilai buffer yang sesuai, menjumlahkan hasilnya, dan menggeser nilai akhir, semua dalam satu ekspresi yang dapat dibaca.


```rust
fn main() {
// Sample UTXOs: (txid_suffix, amount_sats)
let utxos = vec![
("a1b2", 50_000u64),
("c3d4", 15_000),
("e5f6", 100_000),
("g7h8", 3_000),
("i9j0", 75_000),
];

// Using closures and iterators to process UTXOs

// 1. Filter UTXOs above dust threshold (10,000 sats)
let spendable: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000)
.collect();
println!("Spendable UTXOs: {:?}", spendable);

// 2. Calculate total balance with fold
let total_balance: u64 = utxos
.iter()
.map(|(_, amount)| amount)
.fold(0, |acc, amount| acc + amount);
println!("Total balance: {} sats", total_balance);

// 3. Find UTXOs needed to cover a 120,000 sat payment
let target = 120_000u64;
let mut accumulated = 0u64;
let selected: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000) // Skip dust
.take_while(|(_, amount)| {
if accumulated >= target {
false
} else {
accumulated += amount;
true
}
})
.collect();
println!("Selected for payment: {:?}", selected);

// 4. Transform to display format using map and collect
let display_strings: Vec<String> = utxos
.iter()
.map(|(txid, amount)| format!("{}...:{} sats", txid, amount))
.collect();
println!("Display: {:?}", display_strings);
}
```


### Pengantar ke Penunjuk Cerdas


Pointer pintar adalah struktur data yang berfungsi seperti pointer tradisional, namun menyediakan kemampuan tambahan dan manajemen memori otomatis. Tidak seperti referensi sederhana, smart pointer memiliki data yang mereka tunjuk dan dapat mengimplementasikan perilaku khusus untuk alokasi memori, deallokasi, dan pola akses. Mereka adalah alat penting untuk mengelola data yang dialokasikan di heap dan menerapkan pola kepemilikan kompleks yang melampaui sistem kepemilikan dasar Rust.


Aspek "pintar" berasal dari kemampuannya untuk secara otomatis menangani tugas manajemen memori yang jika tidak, akan memerlukan intervensi manual. Ketika penunjuk pintar keluar dari cakupan, penunjuk pintar dapat secara otomatis membebaskan memori terkait, mengurangi jumlah referensi, atau melakukan operasi pembersihan lainnya. Otomatisasi ini membantu mencegah kebocoran memori dan kesalahan penggunaan setelah bebas sekaligus memberikan fleksibilitas yang lebih besar daripada alokasi stack-only.


Penunjuk pintar biasanya menerapkan dua sifat utama: `Deref` dan `Drop`. Sifat `Deref` memungkinkan penunjuk pintar digunakan seolah-olah sebagai referensi ke data yang terkandung. Sifat `Drop` memungkinkan logika pembersihan khusus ketika penunjuk pintar dihancurkan. Bersama-sama, sifat-sifat ini memungkinkan penunjuk pintar untuk mengelola memori secara otomatis.


### Penunjuk Cerdas Kotak


`Box<T>` adalah penunjuk pintar yang paling sederhana, yang menyediakan alokasi heap untuk semua tipe `T`. Ketika Anda membuat `Box`, nilai yang terkandung disimpan di heap, bukan di stack, dan `Box` itu sendiri (yang hanya sebuah pointer) disimpan di stack. Pengarahan ini berguna ketika Anda perlu menyimpan data dalam jumlah besar tanpa memindahkannya, ketika Anda membutuhkan tipe dengan ukuran waktu kompilasi yang tidak diketahui, atau ketika Anda ingin memindahkan kepemilikan data tumpukan secara efisien.


Membuat sebuah `Box` sangatlah mudah: `let boxed_value = Box::new(42);` mengalokasikan sebuah bilangan bulat pada heap. `Box` secara otomatis mengelola memori ini - ketika `Box` keluar dari cakupan, ia secara otomatis mengalokasikan memori heap. Pembersihan otomatis ini mencegah kebocoran memori tanpa memerlukan manajemen memori secara manual.


Salah satu kasus penggunaan yang paling penting untuk `Box` adalah mengaktifkan struktur data rekursif. Pertimbangkan sebuah senarai berantai di mana setiap simpul berisi sebuah nilai dan sebuah penunjuk ke simpul berikutnya. Tanpa `Box`, Anda tidak dapat mendefinisikan struktur seperti itu karena kompilator tidak dapat menentukan ukuran tipe yang berisi dirinya sendiri. Dengan menggunakan `Box<Node>` untuk pointer berikutnya, Anda memecahkan masalah ukuran rekursif karena `Box` memiliki ukuran yang diketahui dan tetap, tidak peduli apa yang dikandungnya.


### Menerapkan Sifat Deref


Sifat `Deref` memungkinkan sebuah tipe untuk direferensikan menggunakan operator `*`, membuat penunjuk pintar berperilaku seperti referensi ke data yang dikandungnya. Ketika Anda mengimplementasikan `Deref` untuk penunjuk cerdas, Anda mengaktifkan dereferensi otomatis yang membuat penunjuk cerdas menjadi transparan untuk digunakan. Ini berarti Anda dapat memanggil metode pada tipe yang dikandung secara langsung melalui penunjuk pintar tanpa pengacuan secara eksplisit.


Sifat `Deref` mendefinisikan tipe terkait `Target` yang menentukan jenis referensi apa yang harus dihasilkan oleh operasi dereferensi. Sifat ini membutuhkan implementasi metode `deref` yang mengembalikan referensi ke tipe target. Untuk `Box<T>`, implementasi mengembalikan referensi ke nilai `T` yang terkandung.


Rust melakukan pemaksaan deref otomatis, yang berarti kompiler dapat secara otomatis menyisipkan panggilan ke `deref` bila diperlukan untuk membuat tipe-tipe yang kompatibel. Inilah sebabnya mengapa Anda dapat mengoper `String` ke fungsi yang mengharapkan `&str` - kompiler secara otomatis melakukan dereferensi terhadap `String` untuk mendapatkan potongan string. Pemaksaan ini dapat merantai beberapa level, sehingga `Box<String>` dapat secara otomatis dikonversi menjadi `&str` melalui beberapa operasi dereferensi.


### Implementasi Drop Khusus


Sifat `Drop` memungkinkan Anda untuk menentukan kode pembersihan khusus yang berjalan ketika sebuah nilai berada di luar cakupan. Hal ini sangat penting untuk penunjuk pintar yang mengelola sumber daya di luar memori sederhana, seperti pegangan file, koneksi jaringan, atau jumlah referensi. Sifat `Drop` memiliki metode tunggal, `drop`, yang mengambil referensi yang dapat diubah ke `diri` dan melakukan pembersihan.


Sebagian besar tipe tidak memerlukan implementasi `Drop` khusus karena Rust secara otomatis menangani penurunan field mereka. Namun, penunjuk pintar sering kali membutuhkan logika khusus untuk membersihkan sumber daya yang mereka kelola dengan benar. Sebagai contoh, penunjuk pintar yang dihitung dengan referensi perlu mengurangi jumlah referensi dan berpotensi mengalokasikan data bersama ketika referensi terakhir dijatuhkan.


Anda juga dapat secara eksplisit membuang nilai sebelum nilai tersebut keluar dari ruang lingkup dengan menggunakan `std::mem::drop()`. Fungsi ini mengambil kepemilikan nilai dan segera membuangnya, yang dapat berguna untuk melepaskan sumber daya lebih awal atau memastikan pembersihan terjadi pada titik tertentu dalam program Anda. Fungsi drop eksplisit hanyalah sebuah fungsi identitas yang mengambil kepemilikan - pekerjaan yang sebenarnya terjadi ketika nilai tersebut didrop di akhir fungsi.


Fondasi penutupan, iterator, dan penunjuk pintar ini memberikan alat bantu bagi para pengembang Rust untuk menulis kode yang ekspresif, aman, dan efisien. Fitur-fitur ini bekerja bersama untuk memungkinkan pola pemrograman umum sambil mempertahankan jaminan inti Rust untuk keamanan dan kinerja memori.



## Penghitungan Referensi dan Mutabilitas Interior

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### Penghitungan Referensi dengan RC


Penghitungan referensi merupakan jenis penunjuk pintar mendasar lainnya di Rust, yang dirancang khusus untuk memungkinkan beberapa skenario kepemilikan. Tidak seperti Box, yang mengikuti aturan kepemilikan tunggal tradisional di mana satu entitas memiliki data, RC (Penghitung Referensi) memungkinkan beberapa bagian kode Anda untuk berbagi kepemilikan data yang sama secara bersamaan. Model kepemilikan bersama ini bekerja melalui mekanisme penghitungan yang melacak berapa banyak referensi yang ada pada bagian data tertentu.


Sistem penghitungan referensi beroperasi dengan mempertahankan penghitung internal yang bertambah setiap kali Anda mengkloning RC dan berkurang ketika RC dijatuhkan. Memori hanya dibebaskan ketika penghitung ini mencapai nol, memastikan bahwa data tetap valid selama referensi masih ada. Pendekatan ini mencegah pengalokasian dini sekaligus memungkinkan pola berbagi data yang fleksibel yang tidak mungkin dilakukan dengan kepemilikan Box yang sederhana.


Contoh praktis di mana RC berguna adalah membuat struktur data bersama seperti senarai berantai di mana beberapa senarai dapat mereferensikan bagian ekor yang sama. Pertimbangkan untuk mencoba membuat dua daftar terpisah yang keduanya mereferensikan bagian ekor yang sama. Dengan kepemilikan Box, hal ini menjadi tidak mungkin karena memindahkan bagian yang digunakan bersama ke dalam daftar pertama akan memindahkan kepemilikan, sehingga tidak dapat digunakan pada daftar kedua. RC memecahkan masalah ini dengan mengizinkan Anda mengkloning referensi daripada data yang mendasarinya, sehingga struktur bersama dapat digunakan sambil menjaga keamanan memori.


Ketika Anda mengkloning RC, Anda tidak menduplikasi data internal terlepas dari ukuran atau kerumitannya. Sebaliknya, Anda membuat referensi lain ke lokasi memori yang sama dan menambah penghitung referensi. Hal ini membuat kloning instance RC menjadi efisien bahkan untuk struktur data yang besar, karena hanya referensi itu sendiri yang disalin sementara data yang mendasarinya tetap ada.


### Mutabilitas Interior dengan RefCell


RefCell memperkenalkan mutabilitas interior, yang memungkinkan Anda untuk mengubah data bahkan ketika Anda hanya memiliki referensi yang tidak dapat diubah. Kemampuan ini secara fundamental mengubah bagaimana aturan peminjaman Rust ditegakkan dengan memindahkan pemeriksaan dari waktu kompilasi ke waktu proses. Sementara referensi normal bergantung pada kompiler untuk memverifikasi keamanan peminjaman, RefCell melakukan pemeriksaan ini selama eksekusi program, memberikan fleksibilitas yang lebih besar dengan mengorbankan potensi kepanikan saat runtime.


Prinsip utama di balik RefCell adalah mempertahankan aturan peminjaman yang sama seperti yang biasanya diterapkan oleh Rust pada saat kompilasi, tetapi memeriksanya secara dinamis. Pada saat tertentu, Anda dapat memiliki satu referensi yang dapat diubah atau sejumlah referensi yang tidak dapat diubah pada data di dalam RefCell. Jika kode Anda mencoba melanggar aturan ini dengan membuat peminjaman yang saling bertentangan secara bersamaan, program akan panik dan bukannya menghasilkan perilaku yang tidak terdefinisi.


Pengecekan runtime ini memungkinkan pola pemrograman tertentu yang mungkin ditolak oleh kompiler meskipun pola tersebut sebenarnya aman. Analisis statis kompilator tidak selalu dapat membuktikan bahwa pola peminjaman yang kompleks adalah benar, sehingga membuat kompilator melakukan kesalahan dengan berhati-hati. RefCell memungkinkan Anda untuk mengesampingkan batasan konservatif ini ketika Anda yakin akan kebenaran kode Anda, tetapi kepercayaan diri ini disertai dengan tanggung jawab untuk memastikan penggunaan yang tepat untuk menghindari kerusakan saat proses berjalan.


Kasus penggunaan yang umum untuk RefCell melibatkan objek tiruan dalam skenario pengujian. Ketika mengimplementasikan sebuah trait yang hanya menyediakan akses yang tidak dapat diubah ke dirinya sendiri, tetapi implementasi mock Anda perlu melacak perubahan state secara internal, RefCell memungkinkan pola ini. Anda dapat membungkus state internal dalam RefCell, sehingga mock dapat mengubah data pelacakan bahkan melalui antarmuka yang tidak dapat diubah.


### Menggabungkan RC dan RefCell untuk Status Mutasi Bersama


Kombinasi RC dan RefCell menciptakan pola untuk status mutasi bersama, di mana beberapa pemilik berpotensi memodifikasi data yang sama. RC menyediakan kemampuan kepemilikan bersama, sementara RefCell memungkinkan mutasi melalui referensi yang tidak dapat diubah. Kombinasi ini berguna dalam skenario seperti struktur grafik, cache, atau situasi apa pun di mana beberapa bagian dari program Anda membutuhkan akses baca dan tulis ke data bersama.


Ketika Anda membungkus RefCell di dalam RC, Anda membuat sebuah struktur yang dapat dikloning dan didistribusikan ke seluruh program Anda, dengan setiap klon menyediakan akses ke data dasar yang dapat diubah yang sama. Semua pemilik dapat memodifikasi data menggunakan metode borrow_mut dari RefCell, tetapi mereka harus tetap mematuhi aturan peminjaman pada saat runtime. Pola ini memungkinkan skenario berbagi data yang kompleks dengan tetap mempertahankan jaminan keamanan Rust melalui pemeriksaan runtime.


Namun, fleksibilitas ini datang dengan peringatan penting mengenai kebocoran memori dan siklus referensi. Ketika menggunakan RC dengan RefCell, menjadi mungkin untuk secara tidak sengaja membuat referensi melingkar di mana struktur data mereferensikan diri mereka sendiri, baik secara langsung atau melalui rantai referensi. Siklus ini mencegah jumlah referensi mencapai nol, menyebabkan kebocoran memori karena data tampaknya selalu memiliki referensi aktif bahkan ketika tidak lagi dapat diakses dari program lainnya.


Solusi untuk siklus referensi melibatkan penggunaan referensi lemah, yang tidak berkontribusi pada jumlah referensi yang digunakan untuk keputusan manajemen memori. Referensi lemah memungkinkan Anda untuk mempertahankan koneksi antara struktur data tanpa membiarkannya tetap hidup, memutus siklus potensial sambil mempertahankan kemampuan untuk mengakses data terkait ketika masih ada.


```rust
use std::rc::Rc;
use std::cell::RefCell;

// Simulating a channel state that multiple components need to access and modify
#[derive(Debug)]
struct ChannelState {
channel_id: String,
local_balance_msat: u64,
remote_balance_msat: u64,
is_active: bool,
}

fn main() {
// Rc<RefCell<T>> allows multiple owners with interior mutability
let channel = Rc::new(RefCell::new(ChannelState {
channel_id: "abc123".to_string(),
local_balance_msat: 1_000_000_000,  // 1M sats in msats
remote_balance_msat: 500_000_000,
is_active: true,
}));

// Clone Rc to share ownership (cheap - only increments counter)
let channel_for_ui = Rc::clone(&channel);
let channel_for_router = Rc::clone(&channel);

// Reference count is now 3
println!("Reference count: {}", Rc::strong_count(&channel));

// UI component reads the state (immutable borrow)
{
let state = channel_for_ui.borrow();
println!("UI shows balance: {} msats", state.local_balance_msat);
} // borrow ends here

// Router updates the state after a payment (mutable borrow)
{
let mut state = channel_for_router.borrow_mut();
state.local_balance_msat -= 100_000_000; // Sent 100k sats
state.remote_balance_msat += 100_000_000;
println!("Router updated balances");
} // mutable borrow ends here

// Original reference can still read the updated state
let state = channel.borrow();
println!("New local balance: {} msats", state.local_balance_msat);

// WARNING: This would panic at runtime!
// let borrow1 = channel.borrow();
// let borrow2 = channel.borrow_mut(); // PANIC: already borrowed
}
```


### Dasar-dasar Keamanan dan Konkurensi Benang


Pendekatan Rust terhadap konkurensi berpusat pada pencegahan perlombaan data dan masalah keamanan memori pada waktu kompilasi. Sistem tipe memberlakukan keamanan thread melalui sifat-sifat seperti `Send` dan `Sync`, yang menandai tipe sebagai aman untuk transfer antar thread atau aman untuk akses bersamaan. Verifikasi waktu kompilasi ini menangkap banyak bug konkurensi yang hanya akan muncul pada saat runtime dalam bahasa pemrograman sistem lain.


Membuat thread di Rust mengikuti pola langsung menggunakan thread::spawn, yang mengambil closure untuk dieksekusi di thread baru dan mengembalikan sebuah handle untuk mengelola siklus hidup thread. Thread yang di-spawn berjalan bersamaan dengan thread utama, dan Anda bisa menggunakan metode join pada handle untuk menunggu penyelesaiannya. Tanpa penggabungan eksplisit, spawned thread dapat dihentikan ketika thread utama keluar, sehingga berpotensi memotong pekerjaan yang belum selesai.


Kata kunci move menjadi sangat penting ketika bekerja dengan thread karena penutupan yang diteruskan ke thread yang dibangkitkan sering kali perlu memiliki datanya sendiri daripada meminjamnya. Karena spawned thread dapat hidup lebih lama dari scope yang membuatnya, meminjam dari scope induk menciptakan potensi pelanggaran seumur hidup. Memindahkan data ke dalam thread closure akan memindahkan kepemilikan, memastikan data tetap valid selama masa pakai thread tersebut sekaligus mencegah akses dari lingkup asli.


Message passing menyediakan alternatif untuk konkurensi status bersama melalui saluran yang memungkinkan thread berkomunikasi dengan mengirim data daripada berbagi memori. Pustaka standar Rust menyediakan saluran Multiple Producer Single Consumer (MPSC), di mana beberapa thread dapat mengirim pesan ke satu thread penerima. Pola ini menghilangkan banyak masalah sinkronisasi dengan menghindari status yang dapat berubah sepenuhnya, alih-alih mengandalkan pertukaran pesan untuk koordinasi.


### Konkurensi Status Bersama dengan Mutex dan Arc


Ketika message passing tidak cocok, Rust menyediakan konkurensi keadaan bersama tradisional melalui Mutex (pengecualian timbal balik) yang dikombinasikan dengan Arc (Penghitung Referensi Atom). Mutex memastikan bahwa hanya satu thread yang dapat mengakses data yang dilindungi pada satu waktu dengan mengharuskan thread mendapatkan kunci sebelum mengakses data. Kunci secara otomatis dilepaskan ketika objek penjaga yang dikembalikan oleh operasi kunci keluar dari cakupan, mencegah skenario kebuntuan umum yang disebabkan oleh pembukaan kunci yang terlupakan.


Arc berfungsi sebagai padanan thread-safe dari RC, menggunakan operasi atomik untuk mengelola penghitungan referensi dengan aman di beberapa thread. Meskipun RC bekerja dengan sempurna untuk skenario thread tunggal, penghitungan referensi non-atomiknya menciptakan kondisi balapan ketika diakses dari beberapa thread. Penghitung atomik Arc memastikan bahwa modifikasi penghitungan referensi terjadi dengan aman bahkan di bawah akses bersamaan, sehingga cocok untuk berbagi data melintasi batas-batas thread.


Kombinasi Arc dan Mutex menciptakan pola untuk status mutable yang dapat digunakan bersama dalam program yang berjalan bersamaan. Dengan membungkus Mutex dalam Arc, Anda dapat mengkloning Arc untuk mendistribusikan akses ke mutex yang sama di beberapa thread, dengan setiap thread dapat memperoleh kunci dan memodifikasi data yang dilindungi dengan aman. Pola ini memberikan fleksibilitas status bersama sambil mempertahankan jaminan keamanan Rust melalui verifikasi waktu kompilasi dan penguncian waktu proses.


Sifat Send dan Sync bekerja di belakang layar untuk memastikan keamanan thread pada waktu kompilasi. Send mengindikasikan bahwa sebuah tipe dapat ditransfer dengan aman ke thread lain, sementara Sync mengindikasikan bahwa referensi ke sebuah tipe dapat dibagikan dengan aman antar thread. Sebagian besar tipe secara otomatis mengimplementasikan sifat-sifat ini ketika komponennya aman untuk di- thread, tetapi beberapa tipe seperti RC dan RefCell secara eksplisit tidak mengimplementasikannya karena tidak didesain untuk akses secara bersamaan. Implementasi sifat otomatis ini mencegah terjadinya pelanggaran keamanan thread yang tidak disengaja sekaligus memungkinkan tipe yang aman untuk bekerja dengan mulus dalam konteks konkuren.


## Memahami Makro Rust

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Pengantar ke Makro di Rust


Makro dalam Rust adalah fitur metaprogramming yang memungkinkan pengembang untuk menulis kode yang menghasilkan kode lain pada waktu kompilasi. Tidak seperti fungsi, yang dipanggil pada saat runtime, makro diperluas di awal proses kompilasi, sebelum pemeriksaan tipe dan tahap selanjutnya. Perbedaan mendasar ini membuat makro sangat berguna untuk mengurangi pengulangan kode dan membuat bahasa khusus domain dalam program Rust.


Indikator yang paling mudah dikenali dari pemanggilan makro adalah tanda seru (!) yang mengikuti nama makro. Sebagai contoh, ketika menggunakan `println!("Hello, world!")`, Anda tidak memanggil sebuah fungsi, tetapi memanggil sebuah makro. Makro ini berkembang menjadi kode yang lebih kompleks yang menangani operasi pemformatan dan keluaran. Tanda seru berfungsi sebagai isyarat visual bagi pengembang bahwa pembuatan kode waktu kompilasi sedang terjadi dan bukan pemanggilan fungsi standar.


Rust menyediakan tiga jenis makro yang berbeda, masing-masing melayani tujuan yang berbeda dalam ekosistem bahasa:



- Makro yang menyerupai fungsi**: Menyerupai pemanggilan fungsi namun beroperasi pada waktu kompilasi (misalnya, `vec!`, `println!`)
- Menurunkan makro**: Secara otomatis mengimplementasikan sifat untuk tipe (misalnya, `#[derive(Debug, Clone)]`)
- Makro mirip atribut**: Memodifikasi perilaku elemen kode yang diterapkan padanya (misalnya, `#[test]`, `#[tokio::main]`)


Memahami jenis makro yang berbeda ini sangat penting untuk pemrograman Rust yang efektif, karena masing-masing menangani kasus penggunaan dan pola pemrograman yang spesifik.


### Jenis-jenis Makro dan Aplikasinya


Makro mirip fungsi merupakan jenis makro yang paling sering ditemui dalam pemrograman Rust. Makro ini menggunakan sintaks yang mirip dengan pemanggilan fungsi tetapi melakukan pencocokan pola pada input mereka ke kode generate yang sesuai. Makro `vec!` adalah contoh umum dari kategori ini, yang memungkinkan pengembang untuk membuat dan menginisialisasi vektor dengan sintaks yang ringkas. Ketika Anda menulis `vec![1, 2, 3, 4]`, makro memperluas ini menjadi kode yang membuat vektor baru, mendorong setiap elemen satu per satu, dan mengembalikan vektor yang telah selesai.


Makro Derive menyediakan implementasi sifat otomatis untuk tipe khusus, yang secara signifikan mengurangi kode boilerplate. Ketika Anda menambahkan `#[derive(Debug)]` ke definisi struct atau enum, Anda menginstruksikan kompilator untuk generate implementasi lengkap dari sifat Debug untuk tipe tersebut. Implementasi yang dihasilkan ini menangani logika pemformatan yang diperlukan untuk menampilkan isi tipe dalam format yang dapat dibaca manusia. Mekanisme derive mendukung banyak sifat pustaka standar, termasuk Clone, PartialEq, menjadikannya alat yang umum digunakan untuk mengurangi boilerplate.


Makro yang mirip atribut memodifikasi perilaku elemen kode yang mereka anotasi, menyediakan cara untuk menambahkan metadata atau mengubah perilaku kompilasi. Makro ini muncul sebagai atribut yang ditempatkan di atas definisi tipe, fungsi, atau konstruksi kode lainnya. Sebagai contoh, atribut `#[non_exhaustive]` pada sebuah enum mengindikasikan bahwa varian tambahan dapat ditambahkan pada versi mendatang, yang membutuhkan ekspresi pencocokan untuk menyertakan kasus default. Mekanisme ini memastikan kompatibilitas ke depan sekaligus menyediakan dokumentasi yang jelas tentang potensi evolusi tipe.


### Membuat Makro Seperti Fungsi Khusus


Penulisan makro yang menyerupai fungsi khusus melibatkan pemahaman sintaks pencocokan pola Rust untuk definisi makro. Definisi makro menggunakan pendekatan deklaratif di mana Anda menentukan pola yang cocok dengan bentuk input yang berbeda dan templat pembuatan kode yang sesuai. Setiap makro dapat berisi beberapa cabang, memungkinkannya menangani berbagai pola input dan kode generate yang sesuai untuk setiap kasus.


Pertimbangkan untuk membuat makro vektor khusus yang mendemonstrasikan prinsip-prinsip dasar konstruksi makro. Definisi makro dimulai dengan `macro_rules!` diikuti dengan nama makro dan serangkaian cabang pencocokan pola. Setiap cabang terdiri dari pola yang cocok dengan sintaks input tertentu dan templat kode yang menghasilkan kode Rust yang sesuai. Sebagai contoh, sebuah cabang sederhana dapat mencocokkan tanda kurung kosong `[]` dan kode generate untuk membuat vektor kosong, sementara cabang lain mencocokkan ekspresi tunggal dan menghasilkan kode untuk membuat vektor dengan satu elemen.


Makro menjadi sangat berguna ketika mengimplementasikan pola argumen variabel menggunakan sintaks pengulangan. Pola `$($x:expr),*` cocok dengan nol atau lebih ekspresi yang dipisahkan dengan koma, memungkinkan makro untuk menangani sejumlah argumen secara acak. Templat pembuatan kode yang sesuai menggunakan `$(vec.push($x);)*` untuk mengulang semua ekspresi yang cocok dan pernyataan push individual generate untuk masing-masing ekspresi. Mekanisme pengulangan ini memungkinkan makro untuk kode generate yang tidak mungkin atau sangat bertele-tele untuk ditulis secara manual.


```rust
// A macro to create a HashMap with Bitcoin-related data
macro_rules! btc_map {
// Empty case
() => {
std::collections::HashMap::new()
};
// Key-value pairs case
($($key:expr => $value:expr),+ $(,)?) => {
{
let mut map = std::collections::HashMap::new();
$(
map.insert($key, $value);
)+
map
}
};
}

// A macro for logging with context (simulating a derive-like pattern)
macro_rules! log_payment {
($level:ident, $($arg:tt)*) => {
println!(
"[{}] [PAYMENT] {}",
stringify!($level).to_uppercase(),
format!($($arg)*)
)
};
}

fn main() {
// Using the btc_map! macro
let fee_rates = btc_map! {
"high_priority" => 50_u64,    // sats/vbyte
"medium" => 25_u64,
"low" => 10_u64,
};

println!("Fee rates: {:?}", fee_rates);

// Using the log_payment! macro
log_payment!(info, "Sending {} sats to {}", 100_000, "bc1q...");
log_payment!(warn, "Fee rate {} sats/vB is above average", 75);
log_payment!(error, "Payment failed: insufficient funds");

// Standard vec! macro usage comparison
let utxos = vec![50_000_u64, 30_000, 20_000];
let total: u64 = utxos.iter().sum();
println!("Total UTXOs: {} sats", total);
}
```


Proses kompilasi mengubah panggilan makro menjadi kode yang diperluas sebelum pemeriksaan jenis dan pengoptimalan terjadi. Ketika kompiler menemukan pemanggilan makro, kompiler akan mencocokkan input dengan pola yang telah ditentukan dan mengganti pemanggilan makro dengan kode yang dihasilkan. Kode yang diperluas ini kemudian menjalani proses kompilasi normal, termasuk pemeriksaan tipe dan optimasi. Alat bantu seperti `cargo expand` memungkinkan pengembang untuk memeriksa kode yang dihasilkan, memberikan kemampuan debugging yang berharga saat mengembangkan makro yang kompleks.


### Konsep Makro Tingkat Lanjut dan Debugging


Pengembangan makro memerlukan pemahaman tentang perbedaan antara eksekusi saat kompilasi dan eksekusi saat runtime. Makro dieksekusi selama kompilasi, menghasilkan kode yang akan berjalan pada saat runtime. Pemisahan temporal ini berarti bahwa logika makro tidak dapat bergantung pada nilai runtime, tetapi juga memungkinkan pengoptimalan di mana komputasi yang kompleks dapat dilakukan sekali selama kompilasi daripada berulang kali selama eksekusi.


Sistem pencocokan pola dalam makro mendukung berbagai penentu fragmen yang mendefinisikan jenis elemen kode yang dapat dicocokkan. Penentu `expr` mencocokkan ekspresi, `ty` mencocokkan tipe, `ident` mencocokkan pengenal, dan beberapa lainnya memberikan kontrol yang sangat halus terhadap validasi input. Penentu ini memastikan bahwa makro menerima input yang valid secara sintaksis dan memberikan pesan kesalahan yang jelas ketika sintaks yang tidak valid ditemukan.


Debugging makro menghadirkan tantangan unik karena sifatnya yang bersifat kompilasi. Perintah `cargo expand` berguna untuk pengembangan makro, karena perintah ini menampilkan kode yang diperluas sepenuhnya yang dihasilkan oleh pemanggilan makro. Alat ini memungkinkan pengembang untuk memverifikasi bahwa makro mereka generate kode yang dimaksud dan mengidentifikasi masalah dalam logika perluasan. Ketika kode yang dihasilkan makro mengandung kesalahan, output yang diperluas membantu menentukan apakah masalahnya terletak pada definisi makro atau struktur kode yang dihasilkan.


Makro yang kompleks dapat mengimplementasikan pola rekursif, di mana makro memanggil dirinya sendiri dengan argumen yang dimodifikasi untuk menangani pembuatan kode bersarang atau berulang. Namun, makro rekursif memerlukan desain yang hati-hati untuk menghindari ekspansi tak terbatas dan masalah kinerja kompilasi. Sifat ekspansi makro yang terjadi pada saat kompilasi berarti bahwa implementasi makro yang tidak efisien hanya memengaruhi kecepatan kompilasi, bukan kinerja runtime, tetapi makro yang terlalu rumit dapat memperlambat proses build secara signifikan.



# Rust & Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Mengapa Rust untuk Pengembangan Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


Pemilihan Rust untuk pengembangan Bitcoin dan Lightning bukanlah suatu kebetulan. Pengembangan Bitcoin memiliki tanggung jawab unik yang membedakannya dari pengembangan perangkat lunak pada umumnya. Ketika bekerja dengan Bitcoin, pengembang sering menangani dana pengguna di lingkungan di mana kesalahan bisa jadi tidak dapat diubah. Tidak seperti sistem keuangan tradisional dengan perlindungan peraturan dan mekanisme tolak bayar, sifat desentralisasi Bitcoin berarti bahwa setelah transaksi disiarkan, tidak ada otoritas yang dapat dimintakan pemulihan dana. Kenyataan ini menuntut tingkat tanggung jawab dan ketelitian yang lebih tinggi dalam pengembangan perangkat lunak.


Filosofi "bergerak cepat dan hancurkan sesuatu" yang berlaku di banyak sektor teknologi tidak berlaku untuk pengembangan Bitcoin. Sebaliknya, ekosistem ini membutuhkan bahasa dan alat yang membantu pengembang menciptakan perangkat lunak yang kuat dan aman di mana kegagalan dapat dicegah atau ditangani dengan baik. Inilah sebabnya mengapa banyak proyek Bitcoin terkemuka telah beralih ke Rust, termasuk Bitcoin Development Kit (BDK), Lightning Development Kit (LDK), dan BreezSDK.


Rust menawarkan tiga properti penting yang membuatnya sangat cocok untuk pengembangan Bitcoin: sistem tipe statis yang kuat, perkakas modern yang kaya, dan kompatibilitas lintas platform. Setiap karakteristik ini berkontribusi pada kemampuan bahasa untuk membantu pengembang menulis kode yang lebih aman dan lebih dapat diandalkan untuk menangani operasi mata uang kripto.


### Sistem Tipe Kuat Statis Rust


Sistem tipe Rust menyediakan karakteristik pengetikan yang statis dan kuat yang bekerja sama untuk menangkap kesalahan sebelum dapat mempengaruhi pengguna. Sifat statis berarti bahwa pemeriksaan tipe terjadi pada waktu kompilasi, mengharuskan pengembang untuk menyelesaikan ketidaksesuaian tipe bahkan sebelum program dapat dibangun. Hal ini berbeda dengan bahasa yang diketik secara dinamis di mana kesalahan pengetikan hanya muncul pada saat runtime, yang mungkin terjadi setelah perangkat lunak digunakan dan menangani dana pengguna yang sebenarnya.


Kekuatan sistem tipe Rust mengacu pada ekspresifitas dan ketelitiannya dalam memodelkan masalah. Tidak seperti bahasa dengan sistem tipe yang lebih lemah seperti C, di mana pengembang terbatas pada tipe dasar seperti angka dan struktur, Rust memungkinkan pemodelan tipe yang kaya yang dapat merepresentasikan konsep domain yang kompleks secara akurat. Misalnya, Anda dapat membuat tipe yang membedakan antara berbagai jenis daftar atau memberlakukan bahwa operasi tertentu hanya dilakukan pada tipe objek tertentu.


Apa yang membuat sistem tipe Rust relevan untuk pengembangan Bitcoin adalah pendekatannya terhadap keamanan memori. Sistem tipe yang sama yang memodelkan logika bisnis juga menangani kepemilikan memori dan kontrol akses bersama. Tanggung jawab ganda ini berarti bahwa kelas kerentanan yang umum terjadi, seperti kebocoran memori, kesalahan bebas ganda, dan kondisi balapan, dieliminasi sepenuhnya oleh kompiler. Sistem tipe memberlakukan jaminan keamanan ini melalui konsep-konsep seperti kepemilikan, peminjaman, dan penghitungan referensi, sehingga sangat sulit untuk memperkenalkan bug terkait memori yang dapat membahayakan keamanan atau stabilitas.


```rust
// Example: Type-safe Bitcoin amount handling
// Using newtypes to prevent mixing up satoshis and other values

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Satoshis(u64);

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct FeeRate(u64); // sats per vbyte

impl Satoshis {
fn from_btc(btc: f64) -> Self {
Satoshis((btc * 100_000_000.0) as u64)
}

fn as_btc(&self) -> f64 {
self.0 as f64 / 100_000_000.0
}
}

// Calculate fee given tx size - type system ensures we can't mix up values
fn calculate_fee(tx_size_vbytes: u32, rate: FeeRate) -> Satoshis {
Satoshis(tx_size_vbytes as u64 * rate.0)
}

fn main() {
let payment = Satoshis::from_btc(0.001); // 100,000 sats
let fee_rate = FeeRate(25);              // 25 sats/vbyte
let tx_size = 250_u32;                   // vbytes

let fee = calculate_fee(tx_size, fee_rate);
println!("Payment: {:?} ({} BTC)", payment, payment.as_btc());
println!("Fee: {:?}", fee);

// This would NOT compile - type safety prevents mixing values:
// let bad_fee = calculate_fee(tx_size, payment); // ERROR: expected FeeRate, found Satoshis
}
```


### Perkakas Modern dan Dukungan Lintas Platform


Ekosistem perkakas Rust menyediakan alat bagi para pengembang yang membantu produktivitas dan kualitas kode. Kompiler Rust sendiri dirancang tidak hanya untuk menerjemahkan kode ke dalam bentuk biner, tetapi juga berfungsi sebagai alat edukasi yang membantu pengembang belajar dan berkembang. Ketika terjadi kesalahan kompilasi, kompiler memberikan penjelasan rinci tentang apa yang salah dan sering kali menyarankan perbaikan spesifik. Pendekatan ini sangat berharga bagi pengembang yang baru mengenal Rust, karena kompiler secara efektif mengajarkan praktik-praktik yang baik dan membantu mencegah kesalahan umum.


Bahasa ini mencakup Cargo, manajer paket terpadu yang menangani manajemen ketergantungan, pembangunan, pengujian, dan pembuatan dokumentasi. Standarisasi ini menghilangkan fragmentasi yang terlihat pada bahasa yang lebih tua seperti C++, di mana beberapa alat yang saling bersaing menciptakan ketidakkonsistenan di seluruh proyek. Cargo juga mendukung ekstensi seperti rustfmt untuk pemformatan kode dan Clippy untuk analisis statis, memastikan bahwa kode mengikuti pedoman gaya yang konsisten dan menangkap potensi masalah sebelum menjadi masalah.


Kemampuan lintas platform Rust melampaui sistem operasi tradisional untuk menyertakan platform seluler seperti Android dan iOS, serta WebAssembly untuk aplikasi berbasis browser. Dukungan lintas platform ini berguna untuk aplikasi Bitcoin yang perlu dijalankan di berbagai lingkungan. Sebagai contoh, proyek seperti Mutiny Wallet memanfaatkan kompilasi WebAssembly Rust untuk membuat dompet Lightning yang berjalan langsung di browser web, sesuatu yang tidak praktis jika hanya menggunakan teknologi web tradisional.


### Memahami Jenis Kesalahan dan Implikasinya


Penanganan kesalahan yang efektif dimulai dengan memahami berbagai kategori kesalahan yang dapat terjadi selama eksekusi program. Pertimbangkan sebuah aplikasi perutean sederhana yang menghitung jalur di antara titik-titik geografis. Contoh ini mengilustrasikan tiga jenis kesalahan mendasar yang harus ditangani oleh pengembang: kesalahan input yang tidak valid, kesalahan sumber daya saat proses berjalan, dan kesalahan logika.


Kesalahan input yang tidak valid terjadi ketika sebuah fungsi menerima parameter yang tidak memenuhi persyaratan. Sebagai contoh, jika sistem koordinat geografis menggunakan bilangan bulat bertanda untuk bujur tetapi menerima nilai negatif di mana hanya nilai positif yang valid, fungsi tidak dapat berjalan dengan baik. Kesalahan ini merupakan pelanggaran kontrak antara pemanggil dan fungsi, dan respons yang tepat biasanya menolak input dan mengembalikan indikasi kesalahan.


Kesalahan sumber daya runtime terjadi ketika dependensi eksternal tidak tersedia atau tidak dapat diakses. Membaca file peta mungkin gagal karena file tersebut tidak ada, aplikasi tidak memiliki izin yang tepat, atau perangkat penyimpanan tidak tersedia. Kesalahan-kesalahan ini berada di luar logika program dan sering kali membutuhkan perbaikan lingkungan daripada perubahan kode. Namun, aplikasi yang kuat harus mengantisipasi dan menangani skenario ini dengan baik.


Kesalahan logika mewakili bug dalam implementasi program atau kesalahpahaman tentang bagaimana komponen berinteraksi. Jika algoritme perutean mengembalikan jalur kosong ketika diberikan titik awal dan akhir yang valid, ini mengindikasikan kesalahan logika yang perlu diperbaiki di dalam kode itu sendiri. Tidak seperti jenis kesalahan lainnya, kesalahan logika biasanya memerlukan debugging dan modifikasi kode untuk menyelesaikannya.


### Strategi untuk Manajemen Kesalahan yang Kuat


Membangun perangkat lunak yang andal membutuhkan strategi proaktif yang meminimalkan peluang kesalahan dan menangani kesalahan yang tidak dapat dihindari dengan baik. Strategi pertama melibatkan pembatasan kemungkinan kesalahan melalui desain tipe yang cermat. Dengan memilih tipe yang hanya dapat mewakili nilai yang valid, pengembang dapat mengeliminasi seluruh kelas kesalahan input yang tidak valid. Sebagai contoh, menggunakan bilangan bulat tidak bertanda untuk nilai yang tidak boleh negatif mencegah kesalahan nilai negatif pada saat kompilasi.


Asersi memberikan lapisan perlindungan lain dengan secara eksplisit memeriksa bahwa kondisi yang diharapkan berlaku selama eksekusi program. Pemeriksaan ini memiliki beberapa tujuan: menangkap bug selama pengujian, menyebabkan program gagal lebih awal saat terjadi masalah (membuat debugging lebih mudah), dan berfungsi sebagai dokumentasi yang dapat dieksekusi yang menjelaskan asumsi programmer. Ketika sebuah pernyataan gagal, hal ini mengindikasikan bahwa asumsi dasar tentang keadaan program telah dilanggar, biasanya menunjukkan kesalahan logika yang perlu diselidiki.


Prinsip abstraksi berlapis membantu mengelola kompleksitas dengan memastikan bahwa kesalahan ditangani pada tingkat sistem yang sesuai. Detail implementasi internal, termasuk jenis kesalahan spesifik dari pustaka tingkat yang lebih rendah, tidak boleh menyebar di luar batas subsistem. Sebaliknya, setiap lapisan harus menerjemahkan kesalahan ke dalam istilah yang bermakna pada tingkat abstraksi tersebut. Sebagai contoh, aplikasi wallet yang menggunakan pustaka Bitcoin harus menerjemahkan kesalahan penguraian deskriptor tingkat rendah ke dalam pesan tingkat yang lebih tinggi seperti "konfigurasi wallet tidak valid" yang memberikan informasi yang dapat ditindaklanjuti kepada pengguna atau kode pemanggilan.


Pendekatan penanganan kesalahan ini, dikombinasikan dengan sistem tipe dan perkakas Rust, membantu menangkap potensi masalah di awal proses pengembangan, sebelum masalah tersebut dapat memengaruhi pengguna atau membahayakan keamanan aplikasi Bitcoin.



## Model kesalahan

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

Rust menyediakan pendekatan komprehensif untuk penanganan kesalahan yang menyeimbangkan keamanan dengan kepraktisan. Meskipun konsep model kesalahan umum berlaku di seluruh bahasa pemrograman, Rust menawarkan alat dan pola khusus yang membuat penanganan kesalahan menjadi eksplisit dan mudah dikelola. Memahami mekanisme ini sangat penting untuk menulis aplikasi Rust yang kuat yang dapat menangani situasi yang tidak terduga dengan anggun sambil mempertahankan kinerja dan keamanan.


### Kepanikan dan Penggunaannya yang Tepat


Mekanisme panik Rust merupakan cara yang paling langsung untuk menangani kesalahan yang tidak dapat dipulihkan. Ketika Anda memanggil makro `panic!`, program segera menghentikan eksekusi, baik membatalkan atau melepaskan tergantung pada konfigurasi Anda. Makro panic menerima pesan string yang menjelaskan apa yang salah, menyediakan konteks untuk debugging. Selain itu, metode seperti `unwrap()` dan `expect()` pada tipe Result dan Option berfungsi sebagai jalan pintas untuk panik ketika tipe-tipe ini mengandung nilai kesalahan atau None. Metode `expect()` memungkinkan Anda untuk memberikan pesan khusus, membuatnya sedikit lebih informatif daripada `unwrap()` ketika men-debug kegagalan.


Meskipun sederhana, panic harus digunakan secara bijaksana dalam kode produksi. Ada beberapa skenario di mana panic tidak hanya dapat diterima, tetapi juga direkomendasikan. Ketika menulis contoh atau prototipe, panic menyediakan cara yang bersih untuk fokus pada fungsionalitas inti tanpa mengacaukan kode dengan penanganan kesalahan yang komprehensif. Dalam lingkungan pengujian, kepanikan sering kali merupakan perilaku yang diinginkan ketika pernyataan gagal, karena hal ini dengan jelas menunjukkan bahwa ada sesuatu yang tidak terduga terjadi. Komunitas Rust juga mengakui situasi di mana pengembang memiliki lebih banyak pengetahuan daripada kompiler, seperti ketika mengurai alamat IP yang dikodekan dengan benar yang diketahui valid.


Namun, keamanan yang tampak dari kepanikan "compiler-verified" dapat menipu. Pertimbangkan sebuah skenario di mana Anda mengkodekan alamat IP dan menggunakan `expect()` karena Anda tahu bahwa alamat tersebut valid. Seiring berjalannya waktu, ketika kode berkembang, nilai yang dikodekan dengan keras tersebut dapat direformasi menjadi sebuah konstanta, dan kemudian konstanta tersebut dapat diubah menjadi sesuatu seperti "localhost" untuk pengalaman pengguna yang lebih baik. Tiba-tiba, kepanikan Anda yang "aman" menjadi kegagalan runtime. Evolusi ini menunjukkan mengapa secara umum lebih baik menghindari kepanikan dalam kode produksi dan sebaliknya mengembalikan jenis kesalahan yang sesuai yang dapat ditangani dengan baik.


Satu pengecualian penting dari aturan "hindari kepanikan" adalah operasi mutex. Ketika Anda memanggil `lock()` pada mutex, maka akan mengembalikan sebuah Result karena penguncian dapat gagal jika thread lain panik ketika memegang mutex tersebut. Hal ini menciptakan situasi yang membingungkan di mana kode lokal Anda menerima kesalahan untuk sesuatu yang terjadi dalam konteks yang sama sekali berbeda. Karena Anda tidak dapat menangani kesalahan yang berasal dari kepanikan thread lain, banyak pengembang menganggap bahwa membuka kunci mutex dapat diterima, terutama jika Anda mempertahankan basis kode yang bebas dari kepanikan di tempat lain.


### Bekerja dengan Jenis Hasil dan Opsi


Tipe Result membentuk tulang punggung sistem penanganan kesalahan Rust. Sebagai sebuah enum yang dapat menampung sebuah `Ok(nilai)` atau `Error(kesalahan)`, Result memaksa Anda untuk secara eksplisit mengakui bahwa operasi dapat gagal. Tipe Option memiliki tujuan yang sama untuk kasus-kasus di mana sebuah nilai mungkin tidak ada, yang berisi `Beberapa (nilai) ` atau `Tidak Ada`. Meskipun Option tidak memberikan informasi kesalahan yang rinci, namun sangat cocok untuk situasi di mana ketiadaan nilai sangat berarti dan diharapkan.


Baik Result maupun Option menyediakan beberapa metode utilitas yang membuat penanganan kesalahan menjadi lebih ergonomis. Metode `unwrap_or()` mengembalikan nilai yang ada jika ada, atau nilai default jika ada kesalahan atau Tidak Ada. Pola ini sangat berguna ketika Anda memiliki fallback yang masuk akal, seperti mem-parsing input pengguna dengan default yang masuk akal ketika parsing gagal. Metode `unwrap_or_default()` bekerja dengan cara yang sama tetapi menggunakan nilai default tipe alih-alih mengharuskan Anda untuk menentukannya. Meskipun metode-metode ini tidak secara teknis menangani kesalahan dalam arti tradisional, metode-metode ini menyediakan cara untuk menurunkan fungsionalitas dengan baik ketika terjadi masalah.


Operator tanda tanya (`?`) adalah sintaks ringkas untuk penyebaran kesalahan. Ketika diterapkan pada Hasil atau Opsi, operator ini mengekstrak nilai keberhasilan jika ada, atau segera mengembalikan kesalahan dari fungsi saat ini jika ada masalah. Operator ini menghilangkan pola pengecekan kesalahan yang bertele-tele yang umum terjadi pada bahasa seperti Go, di mana Anda harus mengecek dan mengembalikan kesalahan secara manual pada setiap langkah. Operator tanda tanya pada dasarnya menyediakan gula sintaksis untuk pengembalian awal, memungkinkan Anda untuk menulis kode yang bersih dan linier yang berfokus pada jalur yang baik sambil secara otomatis menangani penyebaran kesalahan.


### Pola Penanganan Kesalahan Tingkat Lanjut


Metode `map()` pada tipe Result dan Option memungkinkan penanganan kesalahan gaya fungsional yang dapat membuat kode lebih ekspresif dan dapat disusun. Ketika Anda memanggil `map()` pada Hasil, fungsi yang disediakan diterapkan pada nilai sukses jika ada, sementara kesalahan secara otomatis disebarkan tanpa modifikasi. Pola ini berguna ketika merantai operasi, karena Anda dapat fokus pada transformasi nilai tanpa berulang kali menangani kasus kesalahan. Metode `map_err () ` menyediakan fungsionalitas kebalikannya, memungkinkan Anda untuk mengubah jenis kesalahan sambil membiarkan nilai keberhasilan tidak berubah.


Transformasi kesalahan menjadi sangat penting ketika membangun aplikasi berlapis di mana komponen yang berbeda membutuhkan jenis kesalahan yang berbeda. Pertimbangkan sebuah fungsi yang mem-parsing input pengguna dan perlu mengubah kesalahan parsing tingkat rendah menjadi kesalahan spesifik domain. Dengan menggunakan `map_err()`, Anda dapat dengan mudah menerjemahkan kesalahan umum "format angka tidak valid" menjadi kesalahan "usia tidak valid" yang lebih kontekstual yang masuk akal dalam domain aplikasi Anda. Transformasi ini terjadi tepat pada titik di mana kesalahan terjadi, membuat kode lebih mudah dibaca dan dipelihara daripada blok try-catch tradisional di mana penanganan kesalahan dipisahkan dari operasi yang bisa gagal.


Kombinasi operator tanda tanya dengan pemetaan kesalahan menciptakan pola penanganan kesalahan yang ringkas. Anda dapat merantai operasi, mengubah kesalahan sesuai kebutuhan, dan menyebarkannya ke atas tumpukan panggilan dengan boilerplate minimal. Pendekatan ini menjaga penanganan kesalahan tetap dekat dengan operasi yang dapat gagal sambil mempertahankan pemisahan yang jelas antara jalur sukses dan jalur kesalahan.


```rust
use std::fmt;

// Layered error types for a wallet application
#[derive(Debug)]
enum NetworkError {
ConnectionFailed(String),
Timeout,
}

#[derive(Debug)]
enum WalletError {
Network(NetworkError),
InvalidAddress(String),
InsufficientFunds { required: u64, available: u64 },
}

// Implement Display for user-friendly messages
impl fmt::Display for WalletError {
fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
match self {
WalletError::Network(e) => write!(f, "Network error: {:?}", e),
WalletError::InvalidAddress(addr) => write!(f, "Invalid address: {}", addr),
WalletError::InsufficientFunds { required, available } =>
write!(f, "Need {} sats but only have {} available", required, available),
}
}
}

// Convert from lower-level error to domain error
impl From<NetworkError> for WalletError {
fn from(err: NetworkError) -> Self {
WalletError::Network(err)
}
}

// Simulated network call
fn fetch_balance(address: &str) -> Result<u64, NetworkError> {
if address.starts_with("bc1") {
Ok(500_000) // 500k sats
} else {
Err(NetworkError::ConnectionFailed("Invalid endpoint".into()))
}
}

// Higher-level function using ? with automatic error conversion
fn send_payment(from: &str, amount: u64) -> Result<String, WalletError> {
let balance = fetch_balance(from)?; // NetworkError auto-converts to WalletError

if balance < amount {
return Err(WalletError::InsufficientFunds {
required: amount,
available: balance,
});
}

Ok(format!("Sent {} sats", amount))
}

fn main() {
match send_payment("bc1qtest...", 100_000) {
Ok(msg) => println!("Success: {}", msg),
Err(e) => println!("Failed: {}", e), // User-friendly message
}
}
```


### Pustaka Eksternal dan Ekosistem Penanganan Kesalahan


Ekosistem Rust mencakup beberapa pustaka populer yang memperluas kemampuan penanganan kesalahan pustaka standar. Pustaka `bagaimanapun` menyediakan pendekatan yang disederhanakan untuk penanganan kesalahan dengan menawarkan jenis kesalahan universal yang dapat secara otomatis mengkonversi dari jenis kesalahan apa pun yang mengimplementasikan sifat Kesalahan standar. Konversi otomatis ini memungkinkan Anda untuk menggunakan operator tanda tanya dengan jenis kesalahan yang berbeda tanpa konversi manual, sehingga sangat berguna untuk aplikasi di mana Anda tidak perlu secara terprogram membedakan antara jenis kesalahan yang berbeda.


Meskipun `anyhow` unggul dalam menyederhanakan penanganan kesalahan untuk aplikasi di mana kesalahan terutama ditampilkan kepada pengguna, ia memiliki keterbatasan dalam pengembangan pustaka. Karena `anyhow` pada dasarnya mengubah semua kesalahan menjadi pesan string, pengguna pustaka Anda tidak dapat dengan mudah merespons kondisi kesalahan yang berbeda secara terprogram. Keterbatasan ini membuat `anyhow` lebih cocok untuk aplikasi pengguna akhir daripada untuk pustaka yang perlu memberikan informasi kesalahan terstruktur kepada konsumen mereka.


Pendekatan penanganan kesalahan yang lebih canggih melibatkan pembuatan jenis kesalahan khusus yang memodelkan mode kegagalan spesifik aplikasi atau pustaka Anda. Model kesalahan yang dirancang dengan baik dapat membedakan antara input yang tidak valid (yang dapat diperbaiki oleh pemanggil), kesalahan saat proses (yang dapat diperbaiki), dan kegagalan permanen (yang mengindikasikan adanya bug atau kondisi yang tidak dapat dipulihkan). Pendekatan terstruktur ini memungkinkan konsumen kode Anda untuk membuat keputusan cerdas tentang bagaimana menanggapi berbagai jenis kegagalan, apakah itu berarti mencoba kembali operasi, meminta masukan yang berbeda kepada pengguna, atau melaporkan bug kepada pengembang.


## UniFFI, Menjembatani Perpustakaan Rust ke Berbagai Bahasa


<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### Pengantar UniFFI dan Pengembangan Lintas Platform


UniFFI adalah alat untuk membuat pustaka Rust dapat diakses di berbagai bahasa pemrograman dan platform. Dikembangkan oleh Mozilla, alat ini menjawab tantangan mendasar dalam pengembangan perangkat lunak modern: bagaimana memanfaatkan manfaat kinerja dan keamanan Rust sambil mempertahankan kompatibilitas dengan ekosistem pengembangan yang beragam. Alat ini secara otomatis menghasilkan binding bahasa untuk pustaka Rust, sehingga pengembang tidak perlu lagi membuat kode antarmuka secara manual untuk setiap bahasa target.


Masalah utama yang dipecahkan oleh UniFFI berasal dari sifat Rust sebagai bahasa yang dikompilasi. Ketika kode Rust dikompilasi, kode ini menghasilkan keluaran biner dengan Fungsi Asing Interface (FFI) yang menyajikan antarmuka tingkat rendah yang bisa jadi sulit untuk digunakan secara langsung dari bahasa tingkat tinggi seperti Python, Swift, atau Kotlin. Secara tradisional, setiap pengembang pustaka perlu menulis kode pengikatan khusus untuk setiap bahasa target, sehingga menciptakan penghalang yang signifikan untuk adopsi lintas platform. UniFFI menghilangkan redundansi ini dengan menyediakan pendekatan standar untuk menghasilkan binding ini secara otomatis.


Filosofi desain alat ini berpusat pada memungkinkan pengembang Rust untuk fokus pada logika bisnis inti mereka sambil membuat pustaka mereka dapat diakses oleh pengembang yang bekerja dalam bahasa lain. Pengembang iOS yang menggunakan Swift, misalnya, dapat menggunakan pustaka Rust melalui binding yang dibuat oleh UniFFI yang menyajikan antarmuka Swift yang sepenuhnya asli, tanpa ada indikasi bahwa implementasi yang mendasarinya ditulis dalam Rust. Integrasi yang mulus ini memungkinkan tim untuk memanfaatkan manfaat kinerja Rust tanpa mengharuskan semua anggota tim mempelajari Rust.


### Memahami Arsitektur dan Alur Kerja UniFFI


UniFFI beroperasi melalui alur kerja yang terdefinisi dengan baik yang mengubah pustaka Rust menjadi paket yang kompatibel dengan berbagai bahasa. Prosesnya dimulai dengan pembuatan file Unified Definition Language (UDL), yang berfungsi sebagai spesifikasi antarmuka yang menjelaskan bagian mana dari pustaka Rust Anda yang harus diekspos ke bahasa lain. File UDL ini bertindak sebagai kontrak antara implementasi Rust Anda dan binding bahasa yang dihasilkan.


Arsitekturnya mengikuti pemisahan yang jelas. Pengembang memelihara pustaka Rust mereka dengan idiom dan pola Rust standar, kemudian membuat file UDL terpisah yang memetakan antarmuka publik ke sistem tipe UniFFI. Generator pengikatan UniFFI memproses pustaka Rust dan spesifikasi UDL untuk menghasilkan binding bahasa asli untuk platform target yang diminta. Binding yang dihasilkan ini menangani semua marshaling dan unmarshaling data yang kompleks antara runtime bahasa asing dan kode Rust.


Pada saat runtime, arsitektur ini menciptakan pendekatan berlapis di mana kode aplikasi yang ditulis dalam bahasa target (seperti Kotlin untuk Android) berinteraksi dengan kode pengikatan yang dihasilkan yang tampak sepenuhnya asli untuk bahasa tersebut. Lapisan pengikatan ini menangani terjemahan antara jenis bahasa tertentu dan jenis Rust, mengelola memori dengan aman melintasi batas-batas bahasa, dan menyediakan penanganan kesalahan yang mengikuti konvensi bahasa target. Logika bisnis Rust yang mendasari tetap tidak berubah dan tidak menyadari antarmuka beberapa bahasa yang dibangun di atasnya.


### Bekerja dengan UDL: Interface Definisi dan Pemetaan Jenis


Bahasa Definisi Terpadu berfungsi sebagai landasan fungsionalitas UniFFI, menyediakan cara deklaratif untuk menentukan bagian mana dari pustaka Rust yang harus diekspos dan bagaimana mereka harus disajikan dalam bahasa target. File UDL harus berisi setidaknya satu namespace, yang bertindak sebagai wadah untuk fungsi yang dapat dipanggil secara langsung tanpa memerlukan instansiasi objek. Fungsi ruang nama ini biasanya menangani operasi sederhana yang mengambil nilai sebagai parameter dan mengembalikan hasil.


UDL mendukung serangkaian tipe bawaan yang komprehensif yang dipetakan secara alami ke tipe Rust yang sesuai. Tipe dasar mencakup primitif standar seperti boolean, berbagai ukuran bilangan bulat (u8, u32, dll.), bilangan floating-point, dan string. Tipe yang lebih kompleks termasuk vektor, peta hash, dan konsep khusus Rust seperti tipe Option (diwakili dengan sintaks tanda tanya) dan tipe Result untuk penanganan kesalahan. Sistem tipe juga mendukung enumerasi, baik enum berbasis nilai sederhana maupun enum kompleks yang berisi data terkait, yang memungkinkan pemodelan data yang dapat diterjemahkan melintasi batas-batas bahasa.


Struktur dalam Rust diterjemahkan ke kamus dalam UDL, mempertahankan korespondensi yang hampir satu-ke-satu sambil beradaptasi dengan konvensi sintaksis UDL. Ketika struktur Rust memiliki metode yang terkait, mereka dapat diekspos sebagai antarmuka dalam UDL, yang generate sebagai kelas dengan metode dalam bahasa target berorientasi objek seperti Kotlin atau Swift. Pemetaan ini mempertahankan pola desain berorientasi objek yang diharapkan pengembang dalam bahasa-bahasa ini sambil mempertahankan struktur dan perilaku implementasi Rust yang mendasarinya.


```
// Example UDL file for a Bitcoin wallet library (wallet.udl)
namespace wallet {
// Namespace functions - called directly without object
string generate_mnemonic();
Wallet create_wallet(string mnemonic);
};

// Dictionary (struct) - becomes data class in Kotlin, struct in Swift
dictionary Balance {
u64 confirmed_sats;
u64 pending_sats;
};

// Interface (class with methods) - becomes class with methods
interface Wallet {
// Constructor
constructor(string mnemonic);

// Methods
Balance get_balance();
string get_new_address();
string send_to_address(string address, u64 amount_sats);
};

// Enum with data - maps to sealed class (Kotlin) or enum with associated values (Swift)
[Enum]
interface TransactionStatus {
Pending(u32 confirmations_needed);
Confirmed(u32 block_height);
Failed(string reason);
};

// Error enum for Result types
[Error]
enum WalletError {
"InsufficientFunds",
"InvalidAddress",
"NetworkError",
};

// Function that can fail - throws in target language
interface Wallet {
[Throws=WalletError]
string send_to_address(string address, u64 amount_sats);
};
```


Implementasi Rust yang sesuai akan mendefinisikan tipe-tipe ini dan mengimplementasikan atribut `uniffi::export` ke binding generate untuk Kotlin, Swift, Python, dan bahasa lain yang didukung.


### Penanganan Kesalahan dan Fitur Lanjutan


UniFFI menyediakan penanganan kesalahan yang mempertahankan model kesalahan berbasis HasRust sekaligus menerjemahkannya dengan tepat untuk bahasa target. Fungsi yang mengembalikan tipe Hasil dalam Rust dapat ditandai dengan kata kunci "throws" dalam UDL, yang menentukan jenis kesalahan yang mungkin dihasilkan. Kesalahan ini harus didefinisikan sebagai enum kesalahan dalam file UDL dan harus mengimplementasikan sifat Kesalahan standar Rust dalam kode Rust yang mendasarinya. Peti thiserror menyediakan makro yang nyaman untuk mengimplementasikan sifat ini, mengurangi kode boilerplate secara signifikan.


Penerjemahan penanganan kesalahan menunjukkan pendekatan UniFFI yang sadar bahasa. Di Kotlin, fungsi-fungsi yang ditandai sebagai lemparan dalam metode UDL generate yang melempar pengecualian mengikuti konvensi Java/Kotlin. Binding Python juga menggunakan model pengecualian Python. Penerjemahan ini memastikan bahwa penanganan kesalahan terasa alami dan idiomatis di setiap bahasa target sambil mempertahankan makna semantik dari jenis kesalahan Rust yang asli.


Antarmuka callback merupakan fitur canggih lainnya yang memungkinkan komunikasi dua arah antara pustaka Rust dan aplikasi yang menggunakan. Ketika pustaka Rust perlu memanggil kembali ke dalam kode aplikasi, pengembang dapat mendefinisikan sifat-sifat dalam Rust dan menandainya sebagai antarmuka callback dalam UDL. Aplikasi yang menggunakan mengimplementasikan antarmuka ini dalam bahasa aslinya, dan UniFFI menangani marshalling kompleks yang diperlukan untuk memanggil callback ini dari kode Rust. Pola ini membutuhkan pertimbangan yang cermat terhadap keamanan thread, karena callback dapat melintasi batas thread, sehingga membutuhkan batas Send dan Sync di sisi Rust.


### Aplikasi Dunia Nyata dan Keterbatasan Saat Ini


UniFFI telah diadopsi dalam komunitas pengembangan mata uang kripto dan blockchain, dengan proyek-proyek besar seperti BDK (Bitcoin Development Kit), LDK (Lightning Development Kit), dan berbagai implementasi wallet yang menggunakannya untuk menyediakan SDK seluler. Proyek-proyek ini menunjukkan penggunaan UniFFI dalam lingkungan produksi.


Memeriksa file UDL dunia nyata dari proyek-proyek ini mengungkapkan pola dan praktik terbaik yang muncul dari penggunaan praktis. File UDL BDK, misalnya, menunjukkan bagaimana model domain yang kompleks dengan beberapa enum, struktur, dan antarmuka dapat dipetakan secara efektif untuk membuat SDK seluler yang komprehensif. Konsistensi sintaks UDL di berbagai proyek berarti bahwa pengembang yang terbiasa dengan satu pustaka yang mendukung UniFFI dapat dengan cepat memahami dan bekerja sama dengan yang lain, sehingga menciptakan efek jaringan yang bermanfaat bagi seluruh ekosistem.


Namun, UniFFI memiliki keterbatasan penting yang harus dipertimbangkan oleh para pengembang. Yang paling signifikan adalah kurangnya dukungan untuk antarmuka asinkron. Semua binding yang dihasilkan bersifat sinkron, mengharuskan pengembang untuk menangani operasi asinkron dalam kode Rust mereka dan menyajikan antarmuka sinkron ke aplikasi yang menggunakan. Selain itu, penempatan dokumentasi menghadirkan tantangan: dokumentasi yang ditulis dalam kode Rust tidak ditransfer ke binding yang dihasilkan, sementara dokumentasi dalam file UDL tidak tersedia untuk mengarahkan konsumen Rust ke perpustakaan. Meskipun ada upaya yang sedang berlangsung untuk mengatasi keterbatasan ini melalui penguraian dan pembuatan otomatis, hal ini tetap menjadi pertimbangan untuk implementasi saat ini. Terakhir, UniFFI menghasilkan binding bahasa tetapi tidak menangani pengemasan dan distribusi khusus platform, sehingga para pengembang harus mengatur langkah terakhir dalam membuat paket yang dapat didistribusikan untuk setiap platform target.


# Mengembangkan LNP/BP dengan SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## Node LN pada SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### Memahami Arsitektur Modular LDK


Lightning Development Kit (LDK) mengambil pendekatan yang berbeda untuk implementasi Lightning Network dibandingkan dengan perangkat lunak node tradisional seperti CLightning atau LND. Sementara node Lightning konvensional beroperasi sebagai aplikasi daemon lengkap yang berjalan terus menerus di mesin, LDK berfungsi sebagai pustaka Rust modular yang menyediakan komponen primitif untuk membangun solusi Lightning khusus. Perbedaan arsitektur ini membuat LDK fleksibel, memungkinkan pengembang untuk merakit fungsionalitas Lightning dengan cara yang sesuai dengan kebutuhan proyek mereka.


Filosofi inti di balik LDK berpusat pada modularitas dan kemampuan beradaptasi. Alih-alih menyediakan solusi monolitik, LDK menawarkan komponen individual yang dapat digabungkan, dikustomisasi, atau diganti seluruhnya. Setiap komponen dilengkapi dengan implementasi default yang dapat langsung digunakan, tetapi pengembang tetap memiliki kebebasan untuk mengganti implementasi mereka sendiri jika diperlukan. Sebagai contoh, LDK menyertakan implementasi default untuk pemantauan blockchain, penandatanganan transaksi, dan komunikasi jaringan, namun semua ini dapat diganti dengan solusi khusus yang disesuaikan dengan kasus penggunaan atau lingkungan tertentu.


Desain modular ini memungkinkan LDK berfungsi di berbagai platform dan skenario yang akan menjadi tantangan bagi node Lightning tradisional. Aplikasi seluler, browser web, perangkat yang disematkan, dan perangkat keras khusus dapat memanfaatkan komponen LDK dengan cara yang sesuai dengan batasan dan persyaratan unik mereka. Arsitektur perpustakaan memastikan bahwa pengembang dapat membuat aplikasi yang mendukung Lightning tanpa terkunci ke dalam pola operasional yang telah ditentukan atau ketergantungan sistem.


### Kasus Penggunaan LDK dan Fleksibilitas Platform


Fleksibilitas arsitektur LDK membuka banyak kasus penggunaan yang jauh melampaui penyebaran node Lightning tradisional. Pengembangan Mobile wallet merupakan salah satu aplikasi yang paling menarik, di mana LDK memungkinkan pembuatan dompet Lightning non-kustodian yang mirip dengan Phoenix wallet. Implementasi seluler ini dapat mempertahankan kontrol pengguna atas kunci pribadi sambil melakukan sinkronisasi dengan Penyedia Layanan Lightning (LSP) saat online, memungkinkan penerimaan pembayaran yang lancar dan manajemen saluran bahkan dengan konektivitas yang terputus-putus.


Integrasi Modul Keamanan Perangkat Keras (HSM) menampilkan kasus penggunaan lain yang kuat untuk LDK. Dengan mengekstraksi komponen penandatanganan dan verifikasi transaksi, pengembang dapat membuat perangkat penandatanganan Lightning-aware yang memahami konteks dan implikasi transaksi Lightning. Kemampuan ini lebih dari sekadar penandatanganan transaksi sederhana, tetapi juga mencakup analisis cerdas atas penerusan pembayaran, operasi saluran, dan keputusan yang sangat penting bagi keamanan. HSM dapat mengevaluasi apakah suatu transaksi merupakan pembayaran yang sah, operasi perutean, atau upaya yang berpotensi berbahaya, sehingga memberikan wawasan keamanan yang berarti bagi pengguna.


Aplikasi Lightning berbasis web mendapatkan manfaat yang signifikan dari filosofi desain bebas-panggilan sistem LDK. Karena lingkungan WebAssembly tidak memiliki akses langsung ke sumber daya sistem seperti sistem file, soket jaringan, atau sumber entropi, pendekatan murni LDK memungkinkan fungsionalitas Lightning beroperasi dengan mulus di lingkungan browser. Pengembang dapat mengimplementasikan lapisan jaringan khusus menggunakan WebSockets dan menyediakan sumber persistensi dan keacakan yang kompatibel dengan browser sambil mempertahankan kepatuhan protokol Lightning sepenuhnya.


### Komponen Inti dan Arsitektur Berbasis Peristiwa


Arsitektur internal LDK berkisar pada beberapa komponen utama yang bekerja bersama melalui sistem yang digerakkan oleh peristiwa. Sistem manajemen peer menangani semua komunikasi dengan node Lightning lainnya, mengimplementasikan protokol noise untuk enkripsi dan mengelola struktur pesan agar sesuai dengan protokol Lightning. Komponen ini beroperasi secara independen dari mekanisme transportasi yang mendasarinya, memungkinkan pengembang untuk mengimplementasikan jaringan melalui soket TCP, WebSockets, koneksi serial USB, atau saluran komunikasi dua arah lainnya.


Manajer saluran berfungsi sebagai koordinator pusat untuk operasi saluran Lightning, bekerja sama dengan manajer rekan untuk menjalankan operasi pembukaan, penutupan, dan pembayaran saluran. Ketika pengembang memulai pembukaan saluran, manajer saluran membuat pesan protokol yang diperlukan dan berkoordinasi dengan manajer peer untuk menangani proses negosiasi multi-langkah. Pemisahan masalah ini memungkinkan abstraksi yang jelas antara logika protokol Lightning dan detail komunikasi jaringan.


Sistem peristiwa LDK menyediakan pemberitahuan asinkron untuk semua operasi dan perubahan status yang signifikan. Peristiwa mencakup spektrum penuh operasi Lightning, mulai dari koneksi peer dan pemutusan hingga keberhasilan dan kegagalan pembayaran, perubahan status saluran, dan konfirmasi blockchain. Pendekatan berbasis peristiwa ini memungkinkan aplikasi untuk merespons aktivitas jaringan Lightning dengan tepat sambil mempertahankan pemisahan yang bersih antara fungsionalitas inti LDK dan logika khusus aplikasi. Pengembang dapat mengimplementasikan penangan peristiwa khusus yang memperbarui antarmuka pengguna, memicu pemberitahuan, atau memulai tindakan lanjutan berdasarkan peristiwa jaringan Lightning.


### Integrasi dan Manajemen Data Blockchain


Integrasi data Blockchain mewakili salah satu lapisan abstraksi LDK, yang dirancang untuk mengakomodasi segala sesuatu mulai dari node Bitcoin penuh hingga klien seluler yang ringan. LDK mendukung dua mode utama interaksi blockchain, masing-masing dioptimalkan untuk kendala sumber daya dan persyaratan operasional yang berbeda. Mode blok penuh memungkinkan aplikasi dengan akses ke data blockchain lengkap untuk meneruskan seluruh blok ke LDK, memungkinkan pemantauan transaksi yang komprehensif dan respons langsung terhadap peristiwa blockchain yang relevan.


Untuk lingkungan dengan sumber daya terbatas, LDK menyediakan pendekatan berbasis pemfilteran yang mengurangi kebutuhan bandwidth dan penyimpanan. Dalam mode ini, LDK mengkomunikasikan kepentingan pemantauannya melalui antarmuka abstrak, meminta pengawasan terhadap ID transaksi tertentu, UTXO, atau pola skrip. Lapisan aplikasi kemudian dapat mengimplementasikan pemantauan ini menggunakan server Electrum, penjelajah blok, atau sumber data blockchain ringan lainnya. Pendekatan ini memungkinkan dompet seluler dan aplikasi web untuk mempertahankan fungsionalitas Lightning tanpa memerlukan sinkronisasi blockchain penuh.


Lapisan persistensi dalam LDK mengikuti prinsip abstraksi yang sama, menyediakan aplikasi dengan gumpalan data biner yang harus disimpan dan diambil dengan andal. LDK menangani semua kerumitan serialisasi dan deserialisasi status saluran Lightning, data gosip jaringan, dan informasi penting lainnya. Aplikasi hanya perlu mengimplementasikan mekanisme penyimpanan yang andal, baik menggunakan sistem file lokal, layanan penyimpanan cloud, atau sistem basis data khusus. Desain ini memastikan bahwa manajemen status Lightning tetap kuat sekaligus memungkinkan aplikasi untuk memilih solusi penyimpanan yang sesuai dengan persyaratan operasional dan model keamanan mereka.


### Fitur-fitur Canggih dan Pola Integrasi


Kemampuan LDK meluas ke fitur-fitur Lightning Network seperti pembayaran multi-path, optimasi rute, dan manajemen gosip jaringan. Sistem perutean mempertahankan pandangan komprehensif tentang topologi Lightning Network melalui partisipasi protokol gosip, memungkinkan pencarian jalur cerdas untuk pembayaran. Aplikasi dapat memengaruhi keputusan perutean melalui parameter konfigurasi dan bahkan dapat menerapkan logika perutean khusus untuk kasus penggunaan khusus.


Sistem pengikatan bahasa library memungkinkan integrasi LDK di berbagai lingkungan pemrograman, mendukung Java, Kotlin, Swift, TypeScript, JavaScript, dan C++. Kompatibilitas lintas platform ini memungkinkan aplikasi seluler yang ditulis dalam bahasa asli untuk menggabungkan fungsionalitas Lightning dengan tetap mempertahankan karakteristik kinerja yang optimal. Sistem pengikatan mempertahankan arsitektur LDK yang digerakkan oleh peristiwa dan desain modular di semua bahasa yang didukung, memastikan pengalaman pengembang yang konsisten terlepas dari platform target.


Estimasi biaya dan penyiaran transaksi merupakan area tambahan di mana LDK memberikan fleksibilitas. Aplikasi dapat menerapkan strategi estimasi biaya khusus yang memperhitungkan pola operasional dan kebutuhan pengguna yang spesifik. Demikian pula, penyiaran transaksi dapat disesuaikan untuk bekerja dengan berbagai antarmuka jaringan Bitcoin, dari koneksi full node langsung ke layanan penyiaran pihak ketiga. Fleksibilitas ini memastikan bahwa aplikasi berbasis LDK dapat mengoptimalkan interaksi blockchain mereka untuk kasus penggunaan khusus mereka dengan tetap mempertahankan kepatuhan protokol Lightning dan standar keamanan.


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### Tantangan Pengembangan Lightning


Mengembangkan aplikasi yang mengintegrasikan pembayaran Lightning menghadirkan hambatan yang signifikan bagi sebagian besar pengembang. Untuk membuat aplikasi dengan fungsionalitas pembayaran Lightning, pengembang pada dasarnya harus menjadi ahli Lightning, memahami konsep yang rumit seperti manajemen saluran, penyeimbangan likuiditas, dan topologi jaringan. Persyaratan keahlian ini menciptakan masalah mendasar untuk adopsi Lightning: meskipun jaringan Lightning itu sendiri beroperasi dan pembayaran dapat diandalkan, kompleksitas teknis mencegah integrasi yang luas ke dalam aplikasi sehari-hari.


Tantangan utamanya terletak pada kesenjangan antara apa yang dibutuhkan oleh pengembang dan apa yang ingin mereka berikan. Para pengembang biasanya bekerja di bawah tenggat waktu yang ketat dan lebih memilih solusi langsung yang memungkinkan mereka untuk fokus pada fungsionalitas inti aplikasi mereka daripada menjadi ahli dalam infrastruktur pembayaran. Ketika integrasi Lightning sulit dilakukan, para pengembang secara alami tertarik pada solusi kustodian karena solusi ini menawarkan jalur yang paling sedikit hambatannya. Namun, kecenderungan terhadap layanan kustodian ini merusak proposisi nilai fundamental Bitcoin tentang kedaulatan keuangan non-kustodian.


### Visi Breez, Petir di Mana Saja


Breez muncul dari visi yang sederhana namun ambisius: membuat semua orang terhubung ke jaringan Lightning melalui antarmuka yang intuitif ke ekonomi Lightning. Pendekatan perusahaan mengakui bahwa meskipun jaringan Lightning berfungsi dengan baik secara teknis, jaringan ini sangat membutuhkan adopsi pengguna untuk mencapai potensi penuhnya. Tantangan adopsi ini melampaui pengguna individu untuk mencakup seluruh ekosistem aplikasi dan layanan yang dapat memperoleh manfaat dari integrasi Lightning.


Aplikasi Breez yang asli mendemonstrasikan visi ini dengan menyediakan pengguna dengan simpul Lightning non-kustodian yang berjalan langsung di ponsel mereka. Aplikasi ini memamerkan kemampuan Lightning seperti streaming pembayaran mikro ke podcaster dan fungsionalitas tempat penjualan. Namun, aplikasi Breez juga mengungkapkan batasan arsitektur yang kritis: ekosistem aplikasi seluler tidak memfasilitasi komunikasi yang mudah antar aplikasi, memaksa pengembang untuk membangun semua fitur yang berhubungan dengan Lightning ke dalam satu aplikasi daripada mengizinkan aplikasi khusus untuk memanfaatkan infrastruktur Lightning bersama.


Pembelajaran perusahaan dari aplikasi Breez menghasilkan wawasan yang sangat penting: masa depan adopsi Lightning bergantung pada kemenangan para pengembang. Jika integrasi Lightning non-kustodian menjadi pilihan termudah bagi pengembang, maka ini menjadi pilihan default. Pendekatan ini juga menawarkan keuntungan dari segi regulasi, karena perangkat lunak non-kustodian menghadapi rintangan regulasi yang lebih sedikit dibandingkan layanan kustodian, sehingga memudahkan pengembang untuk mengirimkan aplikasi mereka secara global.


### Arsitektur SDK Breez


Breez SDK menyediakan pendekatan alternatif untuk mengintegrasikan fungsionalitas Lightning ke dalam aplikasi. Daripada mengharuskan setiap aplikasi untuk menjalankan node Lightning-nya sendiri, SDK menyediakan arsitektur yang mempertahankan prinsip-prinsip non-kustodian sambil menyederhanakan pengalaman pengembang. Pada intinya, SDK memberikan setiap pengguna akhir node Lightning pribadi mereka sendiri yang berjalan pada infrastruktur Greenlight, layanan hosting node Lightning berbasis cloud dari Blockstream.


Arsitektur ini memecahkan beberapa masalah penting secara bersamaan. Pengguna tidak perlu khawatir tentang manajemen basis data, waktu aktif server, atau pemeliharaan infrastruktur-kekhawatiran yang akan sangat membebani konsumen pada umumnya. Namun, tidak seperti solusi kustodian tradisional, Greenlight tidak pernah memiliki akses ke kunci pengguna. Node Lightning di cloud tidak dapat melakukan operasi apa pun tanpa aplikasi yang terhubung secara aktif yang dapat menandatangani transaksi dan pesan. Desain ini mempertahankan manfaat keamanan dari penyimpanan mandiri sekaligus menghilangkan kerumitan operasional.


SDK juga mendukung interoperabilitas. Beberapa aplikasi dapat terhubung ke simpul Lightning pengguna yang sama menggunakan frasa seed yang sama, sehingga pengguna dapat mempertahankan keseimbangan Lightning tunggal di berbagai aplikasi khusus. Sebagai contoh, pengguna mungkin memiliki aplikasi Lightning wallet umum dan aplikasi podcasting khusus, keduanya mengakses dana dan saluran Lightning yang sama. Arsitektur ini memungkinkan pengembangan aplikasi yang terfokus dan terspesialisasi dengan tetap mempertahankan infrastruktur keuangan yang terpadu.


### Penyedia Layanan Kilat dan Likuiditas Just-in-Time


Komponen penting dari Breez SDK adalah integrasinya dengan Lightning Service Provider (LSP), yang berfungsi serupa dengan Internet Service Provider tetapi untuk jaringan Lightning. LSP memecahkan salah satu tantangan Lightning yang paling kompleks: manajemen likuiditas. Di saluran Lightning, dana hanya dapat mengalir ke arah yang memiliki likuiditas, mirip dengan manik-manik pada sempoa yang hanya dapat bergerak ke tempat yang memiliki ruang.


SDK mengimplementasikan saluran "just-in-time" melalui LSP, yang secara otomatis mengelola likuiditas tanpa campur tangan pengguna. Ketika pengguna perlu menerima pembayaran tetapi tidak memiliki likuiditas masuk yang cukup, LSP secara otomatis membuka saluran Lightning baru pada saat pembayaran tiba. Proses ini terjadi dengan mulus di latar belakang, memastikan pengguna selalu dapat menerima pembayaran tanpa memahami mekanisme saluran yang mendasarinya.


Integrasi LSP ini lebih dari sekadar manajemen likuiditas sederhana. SDK mencakup fungsionalitas Lightning yang komprehensif di luar kotak: layanan menara pengawas bawaan untuk keamanan, interoperabilitas on-chain melalui pertukaran kapal selam, fiat on-ramp melalui layanan seperti MoonPay, dan dukungan untuk protokol LNURL. Sistem ini juga menyediakan pencadangan dan pemulihan tanpa batas, memastikan pengguna tidak pernah kehilangan akses ke dana mereka meskipun penyedia infrastruktur berubah atau tidak tersedia.


### Pengalaman Implementasi dan Pengembang


Breez SDK memprioritaskan pengalaman pengembang melalui pendekatan yang komprehensif dan sudah termasuk baterai. SDK ini menyediakan binding untuk berbagai bahasa pemrograman termasuk Rust, Swift, Kotlin, Python, Go, React Native, Flutter, dan C#, yang memungkinkan pengembang untuk mengintegrasikan pembayaran Lightning menggunakan alat pengembangan pilihan mereka. Arsitektur ini mengabstraksikan kompleksitas Lightning melalui API dengan tetap menjaga keamanan jaringan Lightning.


Komponen-komponen utama bekerja sama untuk memberikan pengalaman yang disederhanakan ini. Pengurai input secara otomatis menangani format pembayaran yang berbeda, menentukan apakah sebuah string mewakili faktur, LNURL, atau metode pembayaran lainnya dan mengarahkannya ke fungsi penanganan yang sesuai. Penandatangan terintegrasi mengelola semua operasi kriptografi di latar belakang, sementara penukar menangani interaksi on-chain secara transparan. Desain ini memungkinkan pengembang untuk fokus pada proposisi nilai unik aplikasi mereka daripada menjadi ahli infrastruktur Lightning.


Arsitektur tanpa kepercayaan dari SDK memastikan bahwa meskipun Greenlight dapat mengamati status saluran dan informasi perutean, mereka tidak dapat mengakses dana pengguna atau melakukan operasi yang tidak sah. Pengguna memiliki kontrol penuh atas kunci pribadi mereka, yang tidak pernah meninggalkan perangkat mereka. Pendekatan ini mewakili pertukaran yang dipertimbangkan dengan cermat antara kesederhanaan operasional dan privasi, menyediakan jalur praktis untuk adopsi Lightning arus utama sambil mempertahankan prinsip-prinsip inti kedaulatan keuangan Bitcoin.


## LDK vs Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### Memahami Keterbatasan Lightning Development Kit (LDK)


Lightning Development Kit adalah kumpulan pustaka Rust yang dirancang untuk memberikan fleksibilitas kepada pengembang saat membangun aplikasi Lightning Network. Namun, fleksibilitas ini hadir dengan tantangan implementasi yang signifikan yang menjadi nyata selama pengembangan dunia nyata di Lipa. Sifat LDK yang low-level berarti pengembang harus menangani berbagai tugas kompleks secara mandiri, mulai dari sinkronisasi grafik jaringan hingga optimalisasi perutean pembayaran. Meskipun pendekatan ini menawarkan kontrol penuh atas implementasi Lightning, pendekatan ini membutuhkan sumber daya pengembangan yang substansial dan keahlian teknis yang mendalam untuk mencapai keandalan yang siap produksi.


Salah satu fitur yang paling penting yang hilang dalam LDK adalah dukungan untuk LNURL, standar yang diadopsi secara luas yang menyederhanakan interaksi Lightning Network untuk pengguna akhir. Selain itu, tidak adanya output jangkar menghadirkan tantangan operasional yang serius, terutama di lingkungan dengan biaya tinggi. Output Anchor memecahkan masalah mendasar dengan penutupan paksa saluran Lightning: ketika biaya jaringan melonjak secara dramatis, saluran dengan biaya yang telah ditentukan sebelumnya mungkin menjadi tidak mungkin untuk ditutup secara sepihak karena biaya yang telah ditentukan sebelumnya menjadi tidak mencukupi untuk konfirmasi transaksi. Keterbatasan ini terbukti sangat bermasalah untuk aplikasi wallet seluler, di mana pengguna mungkin meninggalkan wallet tanpa mengoordinasikan penutupan saluran yang kooperatif, sehingga dana berpotensi terdampar selama lonjakan biaya.


Ketidakdewasaan relatif LDK juga termanifestasi dalam perutean pembayaran yang tidak dapat diandalkan, sebuah masalah penting untuk aplikasi Lightning mana pun. Meskipun secara teknis merupakan implementasi yang baik, cakupan LDK yang luas sebagai solusi umum membuatnya sulit untuk mengatasi masalah tertentu dengan cepat. Tim pengembangan mendapati diri mereka menghabiskan banyak waktu untuk memecahkan masalah perutean dan mengimplementasikan fitur yang idealnya ditangani di tingkat library, yang pada akhirnya berdampak pada kecepatan pengembangan dan kualitas pengalaman pengguna.


### Menemukan Keunggulan Breez SDK dan Greenlight


Transisi ke Breez SDK mewakili pergeseran dalam pendekatan arsitektur, beralih dari simpul Lightning yang dikelola sendiri ke solusi berbasis cloud yang didukung oleh layanan Greenlight Blockstream. Perubahan ini segera mengatasi beberapa masalah kritis yang dialami dengan implementasi LDK. Peningkatan yang paling signifikan terjadi pada keandalan pembayaran, terutama karena kemampuan Greenlight untuk mempertahankan grafik jaringan yang selalu lancar. Tidak seperti implementasi Lightning seluler tradisional yang harus menyinkronkan informasi jaringan saat aplikasi dimulai, node Greenlight berjalan terus menerus di cloud, menjaga kesadaran jaringan waktu nyata dan langsung menyediakan data grafik lengkap saat pengguna terhubung.


Arsitektur ini memanfaatkan implementasi Core Lightning (CLN) yang telah teruji dalam pertempuran, yang telah berhasil merutekan pembayaran selama bertahun-tahun sebagai salah satu implementasi Lightning Network yang asli. Akumulasi pengalaman dan keandalan CLN yang telah terbukti memberikan peningkatan stabilitas yang cepat pada proyek LDK yang lebih muda. Ketika pengguna mengaktifkan wallet bertenaga Greenlight mereka, mereka langsung mewarisi pengetahuan jaringan penuh dan kemampuan perutean dari node Lightning yang terus berjalan, menghilangkan penundaan sinkronisasi dan ketidakpastian perutean yang mengganggu implementasi sebelumnya.


Filosofi desain Breez SDK yang memiliki pendapat sangat berguna untuk pengembangan wallet. Daripada menyediakan toolkit Lightning generik, Breez berfokus secara khusus pada aplikasi wallet pengguna akhir, yang memungkinkan tim pengembangan untuk memusatkan upaya mereka dalam menciptakan solusi komprehensif untuk kasus penggunaan khusus ini. Pendekatan yang ditargetkan ini memungkinkan Breez untuk mengintegrasikan layanan penting secara langsung ke dalam SDK, termasuk fungsionalitas Penyedia Layanan Lightning (LSP) yang memungkinkan pengguna untuk menerima pembayaran segera setelah instalasi wallet, tanpa memerlukan prosedur pembukaan saluran manual.


### Fitur Komprehensif dan Peningkatan Pengalaman Pengguna


Pendekatan terintegrasi Breez SDK melampaui fungsionalitas dasar Lightning, dengan menggabungkan fitur-fitur yang meningkatkan pengalaman pengguna. Integrasi LSP bawaan menghilangkan hambatan tradisional yang mengharuskan pengguna untuk memahami manajemen saluran, memungkinkan penerimaan pembayaran langsung untuk instalasi wallet yang baru. Proses orientasi ini membantu adopsi arus utama, karena pengguna dapat mulai menerima pembayaran Lightning tanpa pengetahuan teknis atau prosedur penyiapan.


Fungsionalitas swap on-chain menyediakan lapisan lain dari pengoptimalan pengalaman pengguna dengan memungkinkan penyajian saldo terpadu kepada pengguna. Daripada memaksa pengguna untuk memahami perbedaan antara Lightning dan on-chain Bitcoin, layanan swap memungkinkan konversi otomatis di antara lapisan-lapisan ini sesuai kebutuhan. Ketika pengguna perlu melakukan pembayaran on-chain, sistem dapat dengan mulus menukar dana Lightning ke on-chain Bitcoin di belakang layar, mempertahankan ilusi saldo tunggal yang likuid sambil menangani kompleksitas teknis secara internal.


Dukungan SDK untuk cadangan saluran nol mengatasi tantangan pengalaman pengguna yang signifikan dalam implementasi Lightning tradisional. Cadangan saluran biasanya mencegah pengguna untuk menggunakan saldo penuh yang ditampilkan, sehingga menimbulkan kebingungan ketika pembayaran gagal meskipun dana yang tersedia cukup. Dengan menghilangkan cadangan ini, Breez memungkinkan pengguna untuk menggunakan saldo penuh yang ditampilkan, meskipun hal ini mengharuskan LSP untuk menerima risiko tambahan. Pertukaran ini mencontohkan pendekatan Breez yang berpusat pada pengguna, di mana kompleksitas teknis dan risiko diserap oleh penyedia layanan untuk menciptakan pengalaman pengguna yang intuitif.


Fitur tambahan seperti dukungan LNURL, layanan nilai tukar, dan sinkronisasi multi-perangkat lebih lanjut menunjukkan pendekatan komprehensif SDK untuk pengembangan wallet. Arsitektur berbasis cloud memungkinkan pengguna untuk mengakses node Lightning mereka dari berbagai perangkat atau aplikasi, dengan Breez menangani sinkronisasi status di seluruh titik akses yang berbeda ini. Item peta jalan di masa depan mencakup fungsionalitas spend-all untuk drainase wallet yang lengkap, penyambungan untuk manajemen saluran dinamis, dan pasar LSP yang bersaing untuk memperkenalkan persaingan yang sehat dalam penyediaan layanan.


### Mengevaluasi Trade-off dan Kekhawatiran Sentralisasi


Transisi ke Breez SDK dan Greenlight memperkenalkan pertukaran sentralisasi penting yang harus dipertimbangkan dengan cermat dalam konteks prinsip-prinsip desentralisasi Bitcoin. Arsitektur berbasis cloud berarti node Lightning pengguna beroperasi pada infrastruktur Blockstream, menciptakan ketergantungan pada operasi Greenlight yang berkelanjutan dan pengembangan Breez yang sedang berlangsung. Sentralisasi ini lebih dari sekadar kenyamanan, yang berpotensi berdampak pada kemampuan pengguna untuk memulihkan dana jika layanan tidak tersedia atau jika terjadi penyensoran.


Skenario pemulihan menghadirkan tantangan khusus dalam arsitektur ini. Meskipun pengguna tetap memegang kendali atas private key mereka, mengakses dana tanpa infrastruktur Greenlight akan membutuhkan keahlian teknis untuk menjalankan node Core Lightning independen dan memulihkan status saluran. Untuk pengguna individu, proses pemulihan ini kemungkinan besar akan terbukti sangat rumit, dan bahkan penyedia wallet akan menghadapi tantangan yang signifikan untuk memigrasikan seluruh basis pengguna ke infrastruktur alternatif jika layanan Greenlight dihentikan.


Pertimbangan privasi juga bergeser dengan perubahan arsitektur ini. Perutean berbasis cloud berarti Greenlight berpotensi mendapatkan visibilitas ke tujuan pembayaran, sedangkan arsitektur LSP saja sebelumnya membatasi kebocoran informasi pada jumlah dan waktu pembayaran. Generasi Invoice di cloud semakin memperluas potensi eksposur informasi, karena faktur yang tidak terpakai yang sebelumnya tetap bersifat pribadi di perangkat pengguna sekarang melewati infrastruktur Blockstream.


Terlepas dari masalah sentralisasi ini, manfaat praktisnya sering kali lebih besar daripada risiko teoretis untuk banyak kasus penggunaan. Keandalan yang ditingkatkan, rangkaian fitur yang komprehensif, dan pengalaman pengguna yang unggul memungkinkan pengembang wallet untuk fokus pada inovasi lapisan aplikasi daripada manajemen infrastruktur Lightning. Pembagian kerja ini mencerminkan ekosistem yang matang di mana penyedia layanan khusus menangani tantangan teknis yang kompleks, sehingga pengembang aplikasi dapat berkonsentrasi pada pengalaman pengguna dan logika bisnis. Kuncinya terletak pada pemahaman yang jelas tentang trade-off ini dan membuat keputusan yang tepat berdasarkan persyaratan kasus penggunaan tertentu dan tingkat toleransi risiko.




# Bagian Akhir

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Ulasan & Peringkat

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Kesimpulan

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>