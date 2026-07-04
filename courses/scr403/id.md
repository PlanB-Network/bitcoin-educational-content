---
name: Menyelami Simplicity
goal: Menguasai filosofi desain, sistem tipe, dan siklus hidup penuh Simplicity
objectives:
  - Memahami tiga metode komposisi fundamental dan sembilan kombinator yang membentuk bahasa yang lengkap
  - Membangun logika boolean, aritmetika, dan SHA-256 dari sistem tipe minimal Simplicity
  - Memahami bagaimana efek samping Failure dan Reader memungkinkan interaksi blockchain yang nyata
  - Mempelajari bagaimana program Simplicity menjadi alamat Taproot dan ditebus dengan data witness
---

# Menyelami Simplicity

Sebuah penyelaman mendalam ke dalam teori dan keputusan desain di balik bahasa Simplicity, berdasarkan seri artikel lima bagian yang lengkap ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) oleh [Dr. Russell O'Connor](https://r6.ca/), pencipta Simplicity di Blockstream Research. Kursus ini menjelaskan *mengapa* Simplicity dirancang seperti itu, bukan cara menulisnya.

Kursus ini mengikuti artikel-artikel Dr. O'Connor melalui tiga cara fundamental menggabungkan komputasi, sistem tipe minimal dan teorema kelengkapannya, konstruksi tipe data praktis dan aritmetika dari prinsip dasar, pengenalan efek samping secara hati-hati untuk interaksi blockchain, dan akhirnya bagaimana program di-commit ke alamat dan ditebus di on-chain.

+++

# Pendahuluan

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Ikhtisar kursus

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Selamat datang di SCR403 — Menyelami Simplicity!

Kursus ini didasarkan pada seri artikel **"Delving Simplicity"** yang ditulis oleh [Dr. Russell O'Connor](https://r6.ca/), seorang Infrastructure Tech Developer di [Blockstream](https://blockstream.com/) dan pencipta Simplicity. Artikel-artikel aslinya diterbitkan di forum [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) dan menjadi sumber materi utama untuk kursus ini. Kami berterima kasih atas karya perintisnya, yang membuat konten edukasi ini dapat diwujudkan.

### Apa yang akan Anda pelajari

Kursus ini mengeksplorasi filosofi desain dan fondasi matematis di balik Simplicity, bahasa scripting generasi berikutnya yang diaktifkan di [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) pada Juli 2025. Kursus ini mengikuti seri artikel lima bagian secara lengkap dan disusun dalam dua bagian konten utama:

1. **Fondasi Simplicity** — Mengapa komputasi blockchain menuntut bahasa yang secara fundamental berbeda, tiga cara menggabungkan operasi (sekuensial, paralel, kondisional), dan sembilan kombinator inti yang membentuk bahasa yang lengkap secara matematis
2. **Dari Tipe Data ke Program** — Membangun logika boolean, aritmetika, dan SHA-256 dari prinsip dasar; memahami efek samping Failure dan Reader yang memungkinkan interaksi blockchain; dan mempelajari bagaimana program di-commit ke alamat Taproot melalui Commitment Merkle Root dan ditebus dengan data witness

### Prasyarat

Ini adalah kursus tingkat **ahli** (sekitar 10 jam). Anda sebaiknya sudah memahami:
- Konsep dasar scripting Bitcoin (apa yang dilakukan validasi transaksi)
- Konsep pemrograman fundamental (tipe, fungsi, komposisi)
- Sedikit familiaritas dengan notasi matematika akan membantu tetapi tidak wajib. Kami memperkenalkan semuanya seiring berjalannya kursus

### Sumber daya utama

- **Artikel asli**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) oleh Dr. Russell O'Connor di Delving Bitcoin
- **Repositori Simplicity**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — kode sumber dan bukti formal Rocq
- **Situs resmi**: [simplicity-lang.org](https://simplicity-lang.org/) — dokumentasi dan referensi SimplicityHL
- **Blog Blockstream**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — tinjauan teknis

Siap menyelami salah satu karya rekayasa Bitcoin yang paling elegan? Ayo mulai!

## Apa itu Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Jika Anda memulai kursus ini tanpa latar belakang tentang Simplicity, bab ini akan mengorientasikan Anda sebelum kita menyelam lebih dalam.

### Simplicity secara singkat

Simplicity adalah **bahasa kontrak pintar native Bitcoin**, yang telah aktif di Liquid Network hari ini. Pertama kali dibayangkan oleh Dr. Russell O'Connor sekitar tahun 2012 dan dijelaskan secara rinci dalam makalahnya tahun 2017 *Simplicity: A New Language for Blockchains*, bahasa ini diaktifkan di Liquid Network pada Juli 2025 setelah bertahun-tahun verifikasi formal dan pengembangan.

Berbeda dengan Solidity milik Ethereum, yang merupakan bahasa kontrak tingkat tinggi dan Turing-complete, Simplicity sengaja dibuat minimal. Bahasa ini memiliki:
- **Tiga pembentuk tipe** (unit, sum, product)
- **Sembilan kombinator** (operasi dasar dan aturan komposisi)
- **Tanpa loop, tanpa rekursi, tanpa alokasi memori dinamis**

Hanya dari primitif-primitif ini, Anda dapat membangun komputasi apa pun yang dibutuhkan untuk validasi transaksi, mulai dari logika boolean hingga hashing SHA-256 penuh.

### Apa yang bisa Anda lakukan dengan Simplicity hari ini?

Simplicity sudah menggerakkan aplikasi nyata di Liquid Network. Yang paling terkenal adalah [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), sebuah pasar opsi bebas oracle di mana pengguna memperdagangkan opsi call pada L-BTC menggunakan USDt sebagai kolateral (kontrak yang mendasarinya juga mendukung opsi put). Proyek Simplicity lain yang sudah aktif termasuk [Swaption](https://swaption.io/) oleh SideSwap (opsi) dan [Deadcat](https://github.com/Resolvr-io/deadcat) yang open-source oleh Resolvr (pasar prediksi). Di luar DeFi, Simplicity memungkinkan kondisi pengeluaran tingkat lanjut seperti vault, covenant, dan skema multisig kompleks yang akan mustahil atau tidak aman dalam Bitcoin Script.

### Apa yang menjadi cakupan kursus ini — dan apa yang bukan

Ini **bukan** tutorial pengkodean langsung. Anda tidak akan menulis program Simplicity di sini. Jika Anda mencari hal itu, lihat:
- [simplicity-lang.org](https://simplicity-lang.org/) — dokumentasi resmi dan bahasa tingkat tinggi SimplicityHL
- [Repositori GitHub Simplicity](https://github.com/BlockstreamResearch/simplicity) — implementasi referensi, contoh, dan bukti Rocq
- [Postingan blog Blockstream](https://blog.blockstream.com/en-simplicity-github/) tentang cara memulai

Apa yang **menjadi** cakupan kursus ini: **pilihan filosofis dan teknis** di balik desain Simplicity. Mengapa bahasa ini diciptakan seperti ini? Mengapa hanya sembilan kombinator? Mengapa tanpa rekursi? Mengapa penting bahwa sistem tipe terhubung dengan kalkulus sekuen Gentzen?

Anggap ini sebagai memahami **mengapa mesinnya dibangun seperti ini** alih-alih belajar mengemudikan mobilnya.

### Untuk siapa kursus ini?

Kursus ini ideal untuk:
- **Pengembang protokol** yang ingin memahami fondasi Simplicity sebelum menulis kode
- **Peneliti Bitcoin** yang tertarik pada verifikasi formal dan pendekatan berbasis teori tipe
- **Ilmuwan komputer** yang penasaran dengan hubungan antara kalkulus sekuen dan komputasi blockchain
- **Bitcoiner tingkat lanjut** yang ingin melampaui pemahaman permukaan tentang kemampuan scripting Liquid

Jika istilah seperti "sum type", "kombinator", atau "kalkulus sekuen" sepenuhnya baru bagi Anda, jangan khawatir, kami menjelaskan semuanya dari awal. Tetapi bersiaplah untuk perjalanan yang padat dan matematis.

### Dari artikel menjadi kursus

Seri "Delving Simplicity" asli oleh Dr. O'Connor disusun sebagai lima artikel teknis. Kursus ini menyusun ulang dan mengannotasi materi tersebut menjadi jalur pembelajaran progresif dengan kuis untuk menguji pemahaman Anda di sepanjang jalan. Ide, definisi, dan bukti adalah miliknya, dan kami telah mengadaptasi formatnya untuk pendidikan terstruktur.

# Fondasi Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Cara Fundamental Menggabungkan Komputasi

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Sekarang bahwa Simplicity telah diaktifkan di Liquid Network, saya ingin melakukan penyelaman mendalam ke dalam filosofi dan desain bahasa Simplicity.

Validasi transaksi Bitcoin adalah aplikasi yang sangat berbeda dari desain bahasa pemrograman biasa. Ruang blok berharga mahal sehingga program perlu ringkas. Program dalam transaksi Bitcoin hanya pernah dieksekusi pada satu input dan semua orang mengeksekusi program pada input yang sama. Selain itu, agen yang mengotorisasi transaksi sudah mengetahui hasil komputasi terlebih dahulu: bahwa transaksi tersebut valid.

Biasanya agen pengotorisasi akan menjalankan komputasi yang jauh lebih mahal untuk memperoleh data witness yang membuktikan validitas transaksi, sementara program yang berjalan di blockchain hanya perlu memeriksa validitas data witness. Memeriksa validitas seringkali jauh lebih murah daripada membuktikan validitas.

Kami merancang Simplicity dengan mempertimbangkan tantangan desain bahasa yang unik semacam ini. Misalnya, Simplicity mewajibkan cabang-cabang yang tidak dieksekusi untuk dipangkas sehingga tidak muncul di blockchain. Langkah-langkah preprocessing dirancang dengan hati-hati agar menunjukkan kompleksitas waktu (quasi-)linear terhadap ukuran program Simplicity. Analisis statis digunakan alih-alih "gas", yang tidak dapat dihitung tanpa mengeksekusi kode dengan cara yang telah ditentukan, sehingga detail model eksekusi tidak menjadi kritikal bagi konsensus. Tidak ada alokasi memori dinamis selama eksekusi. Dan seterusnya.

Sebelum menyelami detail desain Simplicity, saya ingin memulai seri ini dengan sedikit filosofi pemrograman tentang cara-cara umum menggabungkan blok bangunan dasar untuk menciptakan fungsionalitas baru.

### Komposisi

Misalkan seseorang sedang merancang bahasa untuk transaksi yang dapat diprogram bagi blockchain seperti Bitcoin. Secara khusus, program hanya memiliki akses ke data transaksi dan data UTXO dari input-inputnya, dan eksekusi hanya menentukan validitas transaksi (yang memungkinkan hasil eksekusi untuk di-cache). Katakanlah seseorang mulai dengan sekumpulan operasi dasar yang dapat melakukan berbagai tugas seperti komputasi dasar, membaca dan/atau memproses data dari transaksi, dan verifikasi tanda tangan. Setiap operasi mengonsumsi tipe input tertentu (mungkin kosong) dan mengembalikan tipe output tertentu. Apa saja cara kita bisa menggabungkan operasi-operasi dasar ini menjadi operasi yang lebih kompleks?

### Komposisi Sekuensial

![Sequential Composition](assets/en/001.webp)

Metode komposisi yang paling fundamental adalah komposisi sekuensial. Jika kita memiliki dua operasi dasar, yang tipe data outputnya cocok dengan tipe data input dari operasi lainnya, maka kita bisa menggabungkan kedua operasi ini menjadi operasi komposit baru. Operasi baru ini menjalankan kedua operasi dasar tersebut secara berurutan, mengambil input dari operasi pertama sebagai input, meneruskan output dari operasi pertama itu ke input operasi kedua, dan akhirnya mengembalikan output dari operasi kedua tersebut.

Tentu saja, kita tidak perlu membatasi diri hanya menggabungkan operasi dasar. Sekarang bahwa kita memiliki beberapa operasi komposit, kita juga bisa menggabungkan operasi-operasi tersebut menggunakan komposisi fungsional.

Dalam matematika, komposisi sekuensial ini seringkali hanya disebut "komposisi", dan orang mungkin berpikir bahwa ini adalah satu-satunya cara menggabungkan sesuatu. Namun, kita memiliki cara lain untuk menggabungkan operasi.

### Komposisi Paralel

![Parallel Composition](assets/en/002.webp)

Misalkan kita memiliki dua operasi, yang bisa berupa operasi dasar atau kompleks, dan keduanya mengambil tipe input yang sama. Cara kedua yang fundamental untuk menggabungkan kedua operasi ini adalah dengan mengeksekusi keduanya pada input yang sama. Ini disebut komposisi paralel, dan tipe outputnya adalah "product" dari tipe-tipe output operasi asli dan berisi pasangan dari kedua output tersebut.

Meskipun disebut komposisi "paralel", dan kedua operasi tersebut pada prinsipnya bisa dieksekusi secara paralel, eksekusi paralel bukanlah persyaratan operasional. Kita bisa mengimplementasikan komposisi paralel secara "sekuensial" dengan mengeksekusi satu operasi terlebih dahulu lalu operasi kedua. Kita tidak peduli dengan detail bagaimana komposisi paralel diimplementasikan selama outputnya sama.

### Komposisi Kondisional

![Conditional Composition](assets/en/003.webp)

Komposisi kondisional adalah dual dari komposisi paralel. Dalam kasus ini kita memiliki dua operasi yang menghasilkan output yang sama, dan kita menggabungkannya dengan memilih salah satu untuk dieksekusi. Input untuk operasi komposit ini adalah "sum" atau "tagged union" dari tipe-tipe input operasi asli. Dalam kasus ini tag, "Left" atau "Right", adalah satu bit dalam data input yang menentukan tipe data mana yang dibawa, dan dengan demikian operasi mana dari kedua operasi tersebut yang bisa dieksekusi.

Komposisi kondisional beroperasi dengan cara yang sama bahkan ketika input adalah sum dari dua tipe yang identik. Sum type tersebut tetap berisi tag, dan nilai tag tersebut menentukan operasi mana dari kedua operasi yang akan dieksekusi.

### Komposisi dalam Bitcoin Script

Ada banyak cara untuk mewujudkan ketiga jenis komposisi ini dalam berbagai bahasa pemrograman. Dalam Bitcoin Script, komposisi sekuensial diwujudkan (secara kurang lebih) melalui penggabungan dua rutin (inilah sebabnya Bitcoin Script disebut bahasa pemrograman concatenative) karena output dari satu rutin ditinggalkan di stack untuk dikonsumsi oleh rutin berikutnya. Komposisi paralel dicapai dengan menggunakan operasi duplicate dan swap untuk memanipulasi stack sehingga dua rutin bisa dijalankan pada input yang sama. Hal-hal tidak sepenuhnya sederhana karena apa yang kita sebut "product" dari tipe biasanya diwujudkan dengan memanfaatkan beberapa item stack. Semoga Anda bisa melihat gambaran umumnya.

Komposisi kondisional, tentu saja, diwujudkan oleh `OP_IF` yang bercabang berdasarkan nilai pada stack. Dalam kasus ini item stack teratas berperan sebagai tag, dan biasanya item atau item-item berikutnya pada stack memiliki "tipe" berbeda yang bergantung pada nilai tag tersebut. Untuk setiap kasus, tipe item stack mungkin hanya cocok untuk diproses oleh salah satu cabang dalam `OP_IF`. Namun setelah kita mencapai `OP_ENDIF`, item-item stack harus memiliki "tipe" yang konsisten sedemikian rupa sehingga skrip yang tersisa mampu berlanjut terlepas dari cabang mana yang sebelumnya diambil.

### Komposisi dalam Simplicity

Kami merancang Simplicity dengan kombinator yang secara langsung mengimplementasikan ketiga bentuk komposisi ini. Bersama dengan beberapa kombinator tambahan untuk mendukung operasi dasar lain yang terkait dengan tipe product dan sum, bahasa inti Simplicity pada akhirnya terdiri dari sembilan kombinator yang memadai untuk mengekspresikan komputasi apa pun yang bersifat finite. Kita akan membahas ini lebih detail di bab berikutnya.

### Jenis Komposisi Keempat

Sebelum mengakhiri, kita perlu menyebutkan bahwa ada setidaknya satu jenis komposisi lagi yang ditemukan dalam Ilmu Komputer, yaitu "komposisi rekursif". Dalam komposisi rekursif, satu operasi diiterasi berkali-kali.

Perhatikan bahwa Bitcoin Script tidak mendukung komposisi rekursif, dan demikian pula, kami secara eksplisit mengecualikan rekursi tak terbatas dari desain Simplicity. Tesis kami adalah bahwa komputasi iteratif tak terbatas lebih baik diimplementasikan menggunakan covenant rekursif yang menghitung melalui banyak transaksi. Ini memungkinkan pengguna menghindari kendala ruang blok dan standardness serta memprediksi biaya transaksi dengan lebih baik.

Meski begitu, ada cara untuk menyalahgunakan fitur delegasi Simplicity untuk menyediakan sesuatu yang menyerupai komposisi rekursif tak terbatas, yang mungkin kita bahas nanti dalam seri ini.

### Kesimpulan

Kita telah meninjau tiga bentuk utama komposisi untuk mengubah operasi dasar menjadi operasi kompleks:

- komposisi sekuensial
- komposisi paralel
- komposisi kondisional

Kita membahas bagaimana bentuk-bentuk komposisi ini diwujudkan dalam Bitcoin Script, dan mengisyaratkan bagaimana bentuk-bentuk tersebut memengaruhi desain bahasa Simplicity. Kita mencatat bahwa jenis komposisi keempat, komposisi rekursif, secara khusus dikecualikan baik dari Simplicity maupun Bitcoin Script.

Di bab berikutnya kita akan menjelaskan sembilan kombinator yang membentuk inti dari bahasa Simplicity, bagaimana mereka berfungsi untuk secara langsung mewujudkan ketiga bentuk komposisi ini, dan bagaimana ini membentuk bahasa yang lengkap untuk mendeskripsikan komputasi finite apa pun.

## Kelengkapan Kombinator Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

Di bab ini kita memperkenalkan bahasa inti Simplicity dan menunjukkan bahwa bahasa ini lengkap, artinya komputasi finite apa pun dapat diekspresikan di dalamnya.

### Tipe Simplicity

Simplicity mendukung tiga konstruktor tipe fundamental. Tipe product `A × B` merepresentasikan output komposisi paralel, sementara tipe sum `A + B` (tagged union) menangani input komposisi kondisional. Tipe ketiga adalah tipe unit.

### Tipe Unit

Tipe unit, dilambangkan `𝟙` atau `ONE`, berisi tepat satu nilai: tuple kosong `⟨⟩` atau `()`. Tipe data zero-bit ini tidak membawa informasi apa pun.

### Tipe Sum

Tipe sum `A + B` menggabungkan dua tipe dengan tag yang menunjukkan "left" atau "right". Nilai ditulis sebagai `σᴸ(a)` atau `inl(a)` untuk nilai bertag left dan `σᴿ(b)` atau `inr(b)` untuk nilai bertag right. Tag-tag ini tetap berbeda bahkan ketika menggabungkan tipe yang identik.

#### Tipe Boolean

Tipe `𝟙 + 𝟙`, dilambangkan `𝟚` atau `TWO`, merepresentasikan tipe satu bit dengan dua nilai. Menurut konvensi, `σᴸ⟨⟩` merepresentasikan false/nol, sementara `σᴿ⟨⟩` merepresentasikan true/satu.

### Tipe Product

Tipe product `A × B` berisi pasangan nilai yang ditulis sebagai `⟨a, b⟩` atau `(a, b)`. Tipe `𝟚 × 𝟚` memiliki empat nilai, berbeda dari empat nilai dalam `𝟚 + 𝟚`.

### Ekspresi Inti Simplicity

Operasi dilambangkan sebagai `f : A ⊢ B`, artinya tipe input `A` dan tipe output `B`. Simplicity bersifat "first-order" — bahasa ini tidak memiliki tipe fungsi.

### Dua Operasi Dasar

Bahasa inti menyediakan dua operasi dasar:

**Identity (`iden`).** Operasi identity meneruskan inputnya tanpa perubahan:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** Operasi unit membuang inputnya dan mengembalikan tuple kosong:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Ini membentuk keluarga dengan satu operasi per tipe.

### Tiga Kombinator Komposisi

Komposisi sekuensial menggunakan `comp f g` (ditulis `f ⨾ g` atau `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Komposisi paralel menggunakan `pair f g` (ditulis `f ▵ g` atau `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Komposisi kondisional menggunakan `case f g : (A + B) × C ⊢ D`, memberikan cabang-cabang akses ke environment bersama `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Mengapa komposisi kondisional mengambil bentuk ini — sum yang dipasangkan dengan environment bersama `C` — alih-alih `copair f g : A + B ⊢ C` yang lebih sederhana dan hanya memilih cabang? Karena `copair` yang polos tidak dapat mengekspresikan **distribusi**: fungsi `dist : (A + B) × C ⊢ A × C + B × C` yang mendorong input bersama ke cabang mana pun yang diambil. Dengan membangun environment `C` langsung ke dalam `case`, Simplicity memperoleh komposisi kondisional *dan* distribusi dari satu kombinator saja — salah satu keputusan desain kunci yang menjaga bahasa inti tetap hanya sembilan kombinator.

### Empat Kombinator Lagi

Konsumsi product menggunakan `take` dan `drop`:

**take** mengekstrak elemen kiri:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** mengekstrak elemen kanan:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Produksi sum menggunakan `injl` dan `injr`:

**injl** membungkus dengan tag left:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** membungkus dengan tag right:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Sembilan Kombinator Inti

Secara total, Simplicity memiliki tepat sembilan kombinator inti:

| Combinator | Purpose |
|---|---|
| `iden` | Pass input through |
| `unit` | Discard input |
| `comp` | Sequential composition |
| `pair` | Parallel composition |
| `case` | Conditional composition |
| `take` | Extract left from product |
| `drop` | Extract right from product |
| `injl` | Inject into left of sum |
| `injr` | Inject into right of sum |

### Simplicity dan Kalkulus Sekuen

Desain Simplicity berasal dari fragmen konjungtif-disjungtif kalkulus sekuen Gentzen. Lebih tepatnya, ini adalah varian dari *interpretasi fungsional* kalkulus sekuen, yang sendiri analog dengan korespondensi Curry-Howard antara deduksi natural dan kalkulus lambda. Aturan kombinator menunjukkan "tipe yang lebih kecil di premis dibandingkan konklusi", memungkinkan Bit Machine — interpreter mesin stack abstrak Simplicity — untuk meminimalkan penyalinan data selama eksekusi.

### Nilai Bukanlah Ekspresi

Ekspresi Simplicity melambangkan operasi, bukan nilai. Notasi `scribe b : A ⊢ B` merepresentasikan sebuah ekspresi unik yang selalu mengembalikan nilai `b`, berfungsi sebagai kemudahan notasi alih-alih kombinator. Ini mencerminkan Bitcoin Script, di mana operasi seperti `OP_1` mendorong nilai alih-alih mengekspresikannya secara langsung.

### Teorema Kelengkapan Simplicity

Dengan sembilan kombinator di tangan, bagaimana kita tahu kita tidak melewatkan sesuatu — bahwa kesembilan kombinator ini benar-benar cukup? Teorema Kelengkapan Simplicity menjawab ini: untuk fungsi apa pun antara tipe Simplicity (finite), ada ekspresi Simplicity yang melambangkannya. Buktinya bersifat konstruktif — ia menunjukkan cara membangun ekspresi tersebut:

1. **Dekomposisi input**: Menggunakan ekspresi `case` bersarang, dekomposisi input dari tipe apa pun secara penuh menjadi bit-bit penyusunnya
2. **Membangun tabel lookup**: Untuk setiap kemungkinan input, gunakan `scribe` untuk menghasilkan output yang sesuai
3. **Merakit**: Case dan scribe yang bersarang bersama-sama membentuk tabel lookup raksasa yang mengimplementasikan fungsi tersebut

Teorema ini diverifikasi secara formal dalam asisten bukti Rocq (sebelumnya Coq). Buktinya merupakan bagian dari repositori resmi Simplicity dan telah diperiksa oleh mesin untuk kebenarannya.

Meskipun teorema kelengkapan menjamin bahwa sembilan kombinator Simplicity dapat mengekspresikan fungsi apa pun antara tipe Simplicity (finite), ekspresi yang dihasilkan dari konstruksi tabel lookup ini berukuran sangat besar dan tidak praktis. Fungsi pada input 256-bit akan membutuhkan tabel lookup dengan 2²⁵⁶ entri. Inilah sebabnya bab-bab berikutnya berfokus pada membangun ekspresi yang efisien yang memanfaatkan struktur komputasi, alih-alih membrute-force segalanya melalui tabel lookup.

### Kesimpulan

Bahasa inti Simplicity mencakup sistem tipe dan kombinator yang memungkinkan komputasi finite apa pun. Meskipun Teorema Kelengkapan menjamin ekspresivitas, ekspresi yang dihasilkan dari konstruksi generik ini berukuran sangat besar dan tidak praktis. Pengembangan Simplicity yang praktis melibatkan pemanfaatan struktur komputasi untuk menghasilkan ekspresi yang ringkas. Bab-bab berikutnya mengeksplorasi struktur data, interaksi transaksi, dan kombinator tambahan.

# Dari Tipe Data ke Program

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Membangun Tipe Data

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

Di bab-bab sebelumnya, kita telah menunjukkan bagaimana kumpulan kombinator inti Simplicity cukup untuk mengimplementasikan komputasi murni finite apa pun. Bab ini menunjukkan cara membangun struktur data dan komputasi praktis dari primitif-primitif ini — dengan cara yang sama komputer dibangun dari gerbang logika.

### Logika Boolean

Tipe Boolean, dilambangkan `𝟚`, sama dengan `𝟙 + 𝟙` dan memiliki dua nilai: `σᴸ⟨⟩` (false) dan `σᴿ⟨⟩` (true). Menggunakan kombinator inti, operator logika Boolean dapat dikonstruksi.

#### Operasi And

Operasi logika `and : 𝟚 × 𝟚 ⊢ 𝟚` mengambil dua bit dan mengembalikan satu bit. Implementasinya bercabang pada bit pertama: jika false, kembalikan false; jika tidak, kembalikan bit kedua.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Pengujian dengan `⟨false, false⟩`:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

Pengujian dengan `⟨true, true⟩`:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Operasi Logika Lainnya

Operasi `not` membutuhkan kombinator pembantu:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

`iden ▵ unit : A ⊢ A × 𝟙` awal menambahkan "environment" kosong ke input, memungkinkan kombinator `case` untuk diterapkan. Penggunaan `take` di kedua cabang membuang environment kosong ini untuk mengeksekusi `f` atau `g`.

Operasi logika Boolean lainnya:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bit Adder

Sebuah "half-adder" mengambil dua bit dan menjumlahkannya, menghasilkan output dua bit: bit carry dan bit sum.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

Sebuah "full-adder" menjumlahkan tiga bit, menghasilkan output dua bit. Inputnya menggunakan tuple bersarang `(𝟚 × 𝟚) × 𝟚`.

Untuk tuple bersarang, digunakan notasi ringkas:

- `O f` melambangkan `take f`
- `I f` melambangkan `drop f`
- `H` melambangkan `iden`

Sebagai contoh, `I O H` berarti `drop (take iden) : A × (B × C) ⊢ B`, mengekstrak nilai tengah. Notasi ini mengingatkan pada digit biner: ketika memikirkan tuple bersarang sebagai pohon biner, notasi ini merepresentasikan digit biner terbalik dari posisi pohon. Ekspresi-ekspresi ini membentuk indeks De Bruijn untuk Simplicity.

**Catatan:** Notasi `I`, `O`, dan `H` hanya berlaku untuk subekspresi yang seluruhnya terdiri dari `take`, `drop`, dan `iden`.

Full-adder menggabungkan dua half-adder, mengambil `or` logika dari bit-bit carry:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

Pada baris pertama, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` menjalankan half-adder pada dua bit pertama, menyimpan bit terakhir.

Pada baris kedua, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` menyimpan bit pertama (carry-out dari half-adder pertama) dan menjalankan half-adder pada dua bit terakhir.

Pada baris terakhir, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` mengambil OR logika dari dua bit pertama (carry-out dari kedua half-adder) dan mengembalikan bit sum-out dari half-adder kedua.

Ini mendemonstrasikan pemrograman Simplicity: menggunakan notasi `I`, `O`, dan `H` untuk merujuk pada bit data, membentuk "environment" yang sesuai untuk memanggil fungsi lain melalui komposisi sekuensial.

Pengguna tidak mendefinisikan operasi tingkat rendah secara langsung. Nanti dalam seri ini akan dibahas jet pustaka standar yang mengimplementasikan fungsi umum. Pengguna akhir tidak diharapkan untuk memprogram langsung dalam Simplicity, mirip dengan Bitcoin Script. Sebaliknya, bahasa tingkat tinggi seperti SimplicityHL menghasilkan kode Simplicity, mengelola "environment" subekspresi dan menerjemahkan variabel bernama menjadi urutan `take` dan `drop` yang sesuai.

### Vektor

Vektor berpanjang tetap didefinisikan dengan membentuk product berulang dari tipe `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Ini juga bisa ditulis sebagai `A^2`, `A^4`, `A^8`, dsb.

Vektor hanya didefinisikan untuk panjang yang merupakan pangkat dua. Pangkat lainnya membutuhkan pemilihan konvensi pengurungan (bracketing).

Diberikan ekspresi `f : A ⊢ B`, pemasangan berulang "memetakan" (maps) fungsi tersebut ke seluruh vektor berpanjang tetap:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Diberikan fungsi `f : A × B ⊢ B`, iterasi atau "folding" pada vektor berpanjang tetap:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Banyak variasi lain tersedia. Diberikan `f : A × B ⊢ C`, "zip" pada vektor berpasangan dengan `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Diberikan `f : (A × B) × C ⊢ C`, fold pada vektor berpasangan dengan `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Menggabungkan `map` dan `fold-right` menciptakan kombinator akumulatif: `f : A × C ⊢ C × B` menghasilkan `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Masih banyak varian lain yang mungkin.

#### Word Multi-bit

Sebuah vektor bit menghasilkan integer multi-bit. Sebagai contoh, `𝟚³²` adalah tipe word 32-bit. `𝟚²⁵⁶` adalah tipe word 256-bit, cocok untuk hash dan operasi kriptografi.

Menggunakan full-adder, sebuah varian dari operasi vektor mendefinisikan "ripple carry adder" pada word multi-bit:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` mengambil dua bilangan biner n-bit dan satu carry-input satu bit, mengembalikan flag carry-out satu bit dan sebuah sum n-bit.

#### SHA-256

Dengan mendefinisikan secara rekursif operasi aritmetika pada word multi-bit — pengurangan, perkalian, pembagian — dan operasi logika bitwise seperti AND, OR, XOR logika, dan menggabungkan operasi-operasi ini secara berulang, bahkan fungsi kompresi blok SHA-256 pun bisa dibangun:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

Kompresi SHA-256 didefinisikan secara formal menggunakan Simplicity di dalam asisten bukti Rocq (sebelumnya Coq), dengan bukti formal bahwa implementasi `sha256-hash-block` sudah benar.

Kompresi ini berjalan terlalu lambat sebagai Simplicity mentah. Jet mengeksekusi fungsi umum seperti kompresi SHA-256 secara native. Implementasi Simplicity murni berfungsi sebagai spesifikasi formal untuk jet.

### Tipe Option

Tipe Option dihasilkan dengan mengambil sum bersama tipe unit:

```
Option A ≔ 𝟙 + A
```

Tipe `Option A` bisa ditulis sebagai `A?` atau `𝕊 A` (di mana `𝕊` berarti "successor"). Fungsi memetakan pada tipe option:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Kombinator monadik seperti bind dapat didefinisikan:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Buffer Berpanjang Variabel

"Buffer" adalah tipe untuk vektor yang terisi sebagian:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Tipe `Xᑉ⁸` berkembang menjadi `(1 + X⁴) × ((1 + X²) × (1 + X))`. Memperlakukan ini sebagai polinomial dan mengekspansinya menghasilkan `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Diinterpretasikan sebagai tipe, ini merepresentasikan sum dari semua kemungkinan tuple X hingga 7, termasuk tuple kosong. Ini persis tipe list dengan panjang yang secara ketat lebih kecil dari 8.

Seperti vektor, operasi mapping dan folding dapat didefinisikan pada buffer. Operasi stack termasuk `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` dan `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` menambahkan sebuah item ke buffer, mengembalikan vektor penuh jika terjadi overflow. `pop-<n` menghapus sebuah item, mengembalikan buffer yang lebih kecil dan item yang dihapus, secara opsional mengembalikan nothing jika buffer aslinya kosong.

Definisi `push-<n`, secara rekursif:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Simplicity mentah menjadi sulit diikuti melebihi tingkat kompleksitas tertentu. Pengguna akhir memanfaatkan bahasa tingkat tinggi seperti SimplicityHL untuk menghasilkan ekspresi idiomatik ini.

### Kesimpulan

Bab ini menunjukkan cara membangun operasi logika dari bit. Dari sini, aritmetika tingkat bit muncul, memungkinkan penalaran tentang eksekusi. Tipe vektor dikembangkan, mendemonstrasikan iterasi pada word multi-bit untuk mendefinisikan aritmetika. Melanjutkan hal ini, operasi kriptografi seperti SHA-256 dan validasi tanda tangan Schnorr dapat didefinisikan hanya menggunakan kombinator Simplicity — semuanya benar-benar didefinisikan menggunakan Simplicity.

Bab ini bukan panduan komprehensif untuk semua tipe data dan operasi yang mungkin dibangun dalam Simplicity, tetapi mengilustrasikan pencapaian fungsionalitas praktis dalam batasan Simplicity. Meskipun tipe-tipenya dibatasi secara finite, vektor, tipe buffer, dan operasi yang berguna yang beriterasi pada struktur-struktur ini dapat didefinisikan.

Spesifikasi operasi pustaka standar yang sebenarnya sedikit berbeda dari definisi di sini. Sebagai contoh, full-adder sebenarnya menggunakan XOR 3-arah dan fungsi logika "mayoritas" alih-alih dua half-adder.

Dalam praktiknya, program Simplicity menggunakan jet untuk operasi aritmetika dan kriptografi. Namun, jet hanya menggantikan ekspresi. Kombinator yang beriterasi pada buffer dan vektor tidak bisa digantikan oleh jet, dan tetap muncul dalam program Simplicity yang sebenarnya. Meski begitu, alih-alih menggunakan ini secara langsung, pengguna akhir memanfaatkan bahasa tingkat tinggi seperti SimplicityHL yang menghasilkan ekspresi semacam itu.

Kombinator yang didefinisikan secara rekursif tampak tumbuh secara eksponensial dalam ukuran ekspresi. Ini bukan masalah. Selama serialisasi, ekspresi dikodekan sebagai DAG (directed acyclic graph) alih-alih pohon. Representasi sebenarnya hanya tumbuh secara linear.

Sejauh ini, hanya komputasi murni yang dipertimbangkan. Interaksi dengan data transaksi untuk tugas seperti menandatangani transaksi membutuhkan suatu cara agar program bisa gagal jika tanda tangan tidak valid. Bab berikutnya membahas efek samping dalam Simplicity.

## Dua Efek Samping

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

Di bab-bab sebelumnya, kita telah menunjukkan cara membangun beberapa struktur data dan komputasi menggunakan kumpulan kombinator inti Simplicity. Seperti yang kita catat, kombinator inti sudah cukup untuk mengimplementasikan komputasi murni finite apa pun. Ini memunculkan pertanyaan: apa lagi yang bisa dicapai? Kita bisa menambahkan efek samping tambahan pada ekspresi kita.

Ada berbagai jenis efek samping yang mungkin untuk ekspresi: pembaruan state, penulisan ke log, melempar exception, membaca dari environment, memanggil continuation, dsb. Efek samping yang tersedia dalam Simplicity akan bergantung pada aplikasinya.

Untuk aplikasi Bitcoin dan Liquid, saat ini kita memiliki dua efek samping: efek Failure, yang merupakan efek exception di mana exception-nya bertipe `𝟙`, dan efek Reader yang memungkinkan data dari environment transaksi untuk diakses. Kombinator inti kita bersifat "murni"; mereka tidak memiliki efek samping. Namun, jet dapat memperkenalkan primitif baru yang memang memiliki efek samping.

### Jet dengan Efek

Kita akan membahas lebih lanjut tentang jet nanti dalam kursus ini, tetapi di sini kita memperkenalkan beberapa contoh jet untuk mengilustrasikan efek sampingnya.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` adalah jet untuk ekspresi yang mengambil x-only pubkey, sebuah pesan 256-bit, dan tanda tangan Schnorr, dan tidak mengembalikan apa pun! Menurut tipenya, seharusnya berperilaku sama seperti `unit`. Perbedaannya terletak pada efek samping jet ini: jika validasi tanda tangan gagal, maka seluruh komputasi dibatalkan dengan melempar exception (bertipe unit). Ini adalah efek Failure.

#### Verify

`verify : 𝟚 ⊢ 𝟙` adalah jet sederhana untuk mengekspresikan efek Failure. Jika input `verify` adalah `false`, seluruh komputasi dibatalkan dengan melempar exception. Jika inputnya `true`, tidak ada yang dikembalikan, tetapi komputasi bisa berlanjut.

#### Hash Transaksi

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` tampak seperti fungsi konstan, karena hanya ada satu kemungkinan nilai input: tuple kosong. Namun, jet ini membaca dari environment transaksi dan menghasilkan hash data transaksi yang analog dengan message digest `SIGHASH_ALL` yang digunakan dalam verifikasi tanda tangan Bitcoin Script. Ini adalah contoh efek Reader: nilai yang dikembalikan bergantung pada environment transaksi tempat jet ini dieksekusi. Ada beberapa jet hashing lain yang menghash berbagai subset data environment transaksi untuk membantu membangun message digest kustom untuk tanda tangan.

#### Jet Introspeksi

`input-sequence : 𝟚³² ⊢ 𝟚³²?` adalah fungsi yang mengambil indeks input dan mengembalikan nomor urut (sequence number) transaksi untuk input tersebut, secara opsional mengembalikan nothing jika indeksnya di luar batas. Sekali lagi, nilai output bukanlah fungsi murni dari indeks input, melainkan operasi ini menggunakan efek Reader untuk mengakses environment transaksi guna menentukan nilai output. Ada beberapa jet introspeksi lain yang mengembalikan berbagai fragmen data environment transaksi.

### Mengklasifikasikan Efek

Tidak semua efek samping diciptakan sama. Beberapa efek samping berperilaku lebih baik daripada yang lain. Kita bisa mengklasifikasikan efek berdasarkan seberapa mudahnya efek tersebut untuk transformasi program.

#### Efek Komutatif

Sebuah efek komutatif adalah efek di mana, jika Anda menukar output dari dua ekspresi, Anda bisa dengan aman menukar ekspresi itu sendiri tanpa mengubah efek ekspresi tersebut. Perhatikan `swap = I H ▵ O H : A × B ⊢ B × A`. Jika `f ▵ g ⨾ swap = g ▵ f` untuk setiap ekspresi `f` dan `g` dengan efek samping, maka efek-efek tersebut komutatif.

Membaca data transaksi dari environment adalah efek komutatif karena hasil pembacaan dari environment tetap sama, apa pun urutan pembacaan yang kita eksekusi.

Secara umum, melempar exception bukanlah efek komutatif. Jika `f` melempar exception `e₁` dan `g` melempar exception lain `e₂`, maka exception mana yang dilempar dari pasangan `f` dan `g` bergantung pada urutan eksekusinya.

Namun, dalam kasus khusus efek Failure, di mana hanya exception bertipe unit yang bisa dilempar, efeknya komutatif. Tidak peduli apakah `f` atau `g` yang melempar exception, exception yang dihasilkan akan sama, karena hanya ada satu kemungkinan nilai exception.

#### Efek Idempoten

Sebuah efek idempoten adalah efek di mana, jika Anda menduplikasi output dari sebuah ekspresi, Anda bisa dengan aman menduplikasi ekspresi itu sendiri tanpa mengubah efek ekspresi tersebut. Perhatikan `dup = iden ▵ iden : A ⊢ A × A`. Jika `f ⨾ dup = dup ⨾ f ▵ f` untuk setiap `f` dengan efek samping, maka efek-efek tersebut idempoten.

Membaca data transaksi dari environment adalah efek idempoten. Melempar exception juga merupakan efek idempoten. Meskipun hanya satu dari dua ekspresi yang diduplikasi yang akan dieksekusi, exception apa pun yang dilempar oleh `dup ⨾ f ▵ f` akan sama dengan exception yang dilempar oleh `f ⨾ dup`.

Namun, menulis ke log mungkin tidak idempoten, karena menduplikasi efek tersebut akan menyebabkan pesan log muncul dua kali. Namun, jika log terdiri dari sebuah _set_ pesan alih-alih _list_ pesan, maka efeknya akan idempoten (dan komutatif) karena penyisipan set itu sendiri adalah operasi idempoten.

#### Efek Uniter

Sebuah efek uniter adalah efek di mana, jika Anda membuang output dari sebuah ekspresi, Anda bisa dengan aman membuang ekspresi itu sendiri tanpa mengubah efek-efeknya. Jika selalu berlaku bahwa `f ⨾ unit = unit` untuk setiap `f` dengan efek samping, maka efek Anda uniter.

Membaca data dari environment adalah salah satu dari sedikit jenis efek uniter. Jika hasil dari pembacaan data transaksi dari environment dibuang, seluruh ekspresi yang melakukan pembacaan tersebut bisa dibuang.

Efek failure tidak uniter. Jika `f` melempar exception maka `f ⨾ unit` juga akan melempar exception; eksekusi bahkan tidak akan sampai ke kombinator `unit` sebelum komputasi dibatalkan. Di sisi lain, `unit` jelas tidak akan melempar exception apa pun, sehingga efek dari `f ⨾ unit` dan `unit` akan berbeda.

Sebagai ringkasan, berikut adalah bagaimana efek-efek yang dibahas di atas dinilai terhadap ketiga properti ini:

| Effect | Commutative | Idempotent | Unitary |
| --- | :---: | :---: | :---: |
| Reader (transaction environment) | ✓ | ✓ | ✓ |
| Failure (unit-typed exception) | ✓ | ✓ | ✗ |
| Writer (log as a set) | ✓ | ✓ | ✗ |
| General exceptions (arbitrary type) | ✗ | ✓ | ✗ |

### Efek yang Diizinkan dalam Simplicity

Semakin baik perilaku suatu jenis efek, semakin banyak ruang yang dimiliki optimizer Simplicity untuk mentransformasi program yang menggunakan efek-efek tersebut. Idealnya kita hanya akan mengizinkan efek yang memiliki ketiga properti: komutatif, idempoten, dan uniter. Ini akan memungkinkan optimizer melakukan transformasi program apa pun yang diinginkannya. Namun, membaca dari environment adalah satu-satunya efek yang memenuhi ketiga properti tersebut.

Sebaliknya, kita menuntut agar efek Simplicity bersifat komutatif dan idempoten. Kedua efek yang kita gunakan dalam Simplicity, efek Failure dan efek Reader, bersifat komutatif dan idempoten. Ini memungkinkan sejumlah besar optimisasi dilakukan pada kode Simplicity.

Namun, transformasi "discard" yang dijelaskan di atas, yang mencoba mengganti `f ⨾ unit` dengan `unit`, atau transformasi serupa apa pun tidak diizinkan jika `f` mungkin menghasilkan efek Failure. Memang, bayangkan jika `f` berisi assertion `bip0340-verify`. Akan menjadi bencana jika mencoba mengoptimalkan pemeriksaan itu sehingga hilang.

### Mengapa Mengizinkan Efek Samping Sama Sekali?

Mengapa Simplicity bahkan mengizinkan efek samping sama sekali? Bukankah lebih baik jika setiap program mengambil seluruh transaksi sebagai input dan mengembalikan output Boolean yang menentukan apakah transaksi valid atau tidak?

#### Verifikasi Batch

Salah satu alasan kita memiliki efek Failure adalah untuk mendukung [verifikasi batch](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) tanda tangan Schnorr. Dalam verifikasi batch, banyak pemeriksaan tanda tangan Schnorr individual dikumpulkan bersama sedemikian rupa sehingga jika satu pemeriksaan tanda tangan gagal, maka seluruh batch gagal.

Prosedur batching ini meningkatkan efisiensi dibandingkan memverifikasi setiap tanda tangan secara individual. Kekurangannya adalah jika verifikasi batch gagal, kita tidak mengetahui pemeriksaan tanda tangan mana secara spesifik yang gagal.

Dengan menggunakan efek samping failure, `bip0340-verify` memastikan bahwa jika satu pemeriksaan tanda tangan gagal, seluruh transaksi gagal. Jika `bip0340-verify` sebaliknya mengembalikan `𝟚`, sebuah tipe Boolean, untuk sukses atau gagal, maka pemeriksaan tanda tangan yang gagal masih bisa mengarah ke cabang di mana skrip berhasil. Dalam kasus seperti itu kita perlu tahu apakah tanda tangan tertentu valid atau tidak, sehingga kita tidak bisa memanfaatkan verifikasi batch.

#### Data Transaksi yang Dihitung Sebelumnya

Sebuah masalah pada Bitcoin Script di masa awal adalah fungsi hashing yang digunakan untuk membuat message digest untuk tanda tangan bersifat linear terhadap ukuran transaksi. Biasanya setiap input membuat setidaknya satu message digest untuk verifikasi tanda tangan, sehingga secara keseluruhan jumlah hashing bersifat kuadratik terhadap ukuran transaksi.

Masalah ini diperbaiki dalam Segwit dan iterasi Bitcoin Script berikutnya dengan mendefinisikan ulang message digest sehingga bisa dihitung dalam waktu konstan per pemeriksaan tanda tangan. Ini bergantung pada adanya `PrecomputedTransactionData`, yang menghitung sebelumnya hash data transaksi sekali dan kemudian dibagikan oleh setiap perhitungan sighash input. Jet hashing transaksi Simplicity bergantung pada jenis data transaksi yang dihitung sebelumnya yang sama untuk memastikan jet berjalan dalam waktu konstan.

Misalkan `sig-all-hash` tidak menggunakan efek Reader. Misalkan kita entah bagaimana berhasil membangun tipe Simplicity untuk environment transaksi. Sebut saja `TxEnv`, sehingga `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` adalah tipe jet tersebut. Definisi semacam itu akan mengharuskan jet `sig-all-hash` mampu menghitung hash dari transaksi apa pun, bukan hanya transaksi yang terlibat dengannya. Program Simplicity bisa menyalin `TxEnv` yang diberikan dan meneruskan salinan yang telah dimodifikasi ke `sig-all-hash`. Dalam kasus seperti itu `sig-all-hash` tidak bisa mengandalkan `PrecomputedTransactionData`, dan kita akan kembali membutuhkan waktu linear terhadap data transaksi apa pun yang diteruskan ke versi `sig-all-hash` ini.

Karena `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` menggunakan efek Reader untuk mengakses data transaksi, jet ini _hanya_ mendapatkan akses ke environment transaksi yang tetap. Untuk alasan itu, implementasi jet ini bisa dengan aman menggunakan `PrecomputedTransactionData` dan beroperasi dalam waktu konstan.

### Agregasi Tanda Tangan Lintas-Input

Meskipun baik Liquid maupun Bitcoin belum mendukung [agregasi tanda tangan lintas-input](https://hrf.org/latest/cisa-research-paper/) saat ini, kita ingin memastikan bahwa Simplicity bisa kompatibel dengan fitur tersebut ketika saatnya tiba.

Meskipun detailnya belum dikerjakan, kita membayangkan half-aggregation diimplementasikan menggunakan efek Writer. Artinya, sebuah jet baru dengan tipe seperti `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` akan mengambil kunci publik, message digest, dan komponen `r` dari tanda tangan Schnorr (sebuah tanda tangan Schnorr terdiri dari komponen `r` dan komponen `s`) dan menuliskannya ke log transaksi sebelum melanjutkan eksekusi. Kemudian, di tempat lain dalam transaksi atau bersama transaksi, sebuah komponen `s` agregat untuk semua tanda tangan Schnorr yang telah di-half-aggregate akan disediakan. Transaksi hanya akan valid ketika komponen `s` agregat semacam itu disediakan untuk semua kunci, pesan, dan komponen `r` yang tercatat dalam log.

Untuk memenuhi persyaratan Simplicity, efek Writer ini perlu idempoten dan komutatif. Ini bisa dipastikan dengan memperlakukan log writer sebagai sebuah set tuple kunci, pesan, komponen `r`. Ini berhasil karena operasi set bersifat idempoten dan komutatif. Memperlakukan log sebagai sebuah set nilai akan kompatibel dengan algoritme verifikasi half-aggregation.

### Kesimpulan

Di bab ini kita mempelajari penambahan efek samping pada komputasi yang bisa dilakukan Simplicity. Kita mengklasifikasikan berbagai jenis efek berdasarkan seberapa baik perilakunya terhadap berbagai jenis transformasi program. Kita memutuskan untuk membatasi efek Simplicity hanya pada yang komutatif dan idempoten.

Kedua efek yang kita gunakan untuk aplikasi Bitcoin dan Liquid adalah efek Reader, untuk mengakses environment transaksi, dan efek Failure, untuk membatalkan dan menggagalkan program. Beberapa jet memanfaatkan operasi primitif di mana jenis efek samping ini bisa terjadi.

Efek Failure menentukan output dari program Simplicity: programnya gagal, membuat transaksi tidak valid, atau programnya berhasil. Efek Reader menyediakan salah satu jenis input untuk program Simplicity: environment yang berisi data transaksi. Tetapi kita juga perlu menyediakan input lain, seperti tanda tangan digital, untuk program Simplicity.

Di bab berikutnya kita akan melihat apa itu program Simplicity, bagaimana mereka diubah menjadi alamat, dan bagaimana kita menambahkan input lain, seperti tanda tangan, ke program Simplicity.

## Program dan Alamat

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

Di bab sebelumnya kita menjelaskan dua efek samping yang digunakan dalam Simplicity: efek Failure, yang menentukan sukses atau gagalnya sebuah program, dan efek Reader, yang menyediakan akses ke environment transaksi. Sekarang kita beralih ke pertanyaan praktis: apa sebenarnya program Simplicity itu, dan bagaimana ia menjadi alamat di blockchain?

### Program Simplicity

Sebuah program Simplicity didefinisikan sebagai ekspresi Simplicity bertipe `𝟙 ⊢ 𝟙`. Signature tipe ini berarti program mengambil input yang tidak bermakna (hanya nilai unit) dan menghasilkan output yang tidak bermakna (hanya nilai unit). Efek Reader menangkap input environment transaksi, sementara efek Failure menunjukkan sukses atau gagal. Efek-efek ini menangani I/O alih-alih tipe Simplicity itu sendiri.

### Commitment Merkle Root

Alih-alih menyimpan program lengkap on-chain, Bitcoin menggunakan commitment — sebuah praktik yang berasal dari Pay-to-Script-Hash (P2SH). Simplicity menggunakan Commitment Merkle Root (CMR).

Setiap kombinator menerima tag SHA-256 yang diturunkan dari pola: `Simplicity␟Commitment␟[identifier]`, di mana `␟` merepresentasikan kode ASCII 31 (unit separator).

Setiap tag adalah hash SHA-256 dari string pre-image yang sesuai yang tercantum di bawah ini:

| Combinator | Tag pre-image (ASCII string) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

Sebuah ekspresi Simplicity kemudian di-hash secara rekursif menjadi CMR 256-bit dengan menghitung tagged SHA-256 midstate untuk setiap kombinator bersama dengan CMR dari argumen-argumennya (tulis `#ᶜ(e)` untuk CMR dari ekspresi `e`, dan `∥` untuk konkatenasi byte):

| Combinator | CMR rule |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Kombinator biner (`comp`, `pair`, `case`) mengonkatenasi CMR dari kedua anaknya; kombinator uner (`take`, `drop`, `injl`, `injr`) mengonkatenasi CMR dari satu anaknya setelah padding 32 byte `0x00`; dan daun nuler (`iden`, `unit`) menghash tag-nya saja. Dua konvensi ini menjaga agar tetap murah untuk dihitung: SHA-256 midstate digunakan sehingga **setiap ekspresi membutuhkan paling banyak satu panggilan ke fungsi kompresi SHA-256** (dengan asumsi midstate hingga tag konstan sudah dihitung sebelumnya), dan konstruktor satu-argumen memberi awalan argumennya dengan padding 32 byte `0x00`, yang memungkinkan sedikit prakomputasi tambahan bagi implementasi yang menginginkannya.

Untuk kombinator `unit` — sebuah konstruktor nuler tanpa sub-ekspresi argumen — aturan ini secara khusus menjadi `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, di mana `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (tag-nya dimasukkan dua kali). CMR yang dihasilkan untuk program `unit` yang trivial adalah:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Yang krusial, CMR tidak melakukan commit pada tipe ekspresi Simplicity, dan sebaliknya mengandalkan inferensi tipe selama penebusan (redemption).

### Alamat

Alamat menggunakan mekanisme Taproot dari BIP-0341 dengan CMR yang di-commit di bawah versi TapLeaf `0xbe`. Prosesnya melibatkan:

1. Menghitung tagged hash TapLeaf yang menggabungkan byte versi, panjang CMR, dan CMR itu sendiri
2. Men-tweak sebuah kunci publik internal (menggunakan titik NUMS ketika tidak diinginkan jalur key-spend)
3. Mengonversi ke format bech32m
4. Menambahkan checksum yang sesuai

Ketika tidak diinginkan jalur key-spend, kunci publik internal diatur ke titik **NUMS** ("Nothing-Up-My-Sleeve"): sebuah titik kurva yang dipilih secara sengaja sehingga tidak ada yang mengetahui logaritma diskritnya — dengan kata lain, sebuah titik tanpa kunci privat yang sesuai. Karena tidak seorang pun bisa pernah menghasilkan tanda tangan untuknya, jalur key-spend dapat dibuktikan tidak bisa digunakan, dan output tersebut hanya bisa dibelanjakan *melalui* jalur skrip Simplicity yang di-commit. Dalam aplikasi nyata, titik NUMS ini sebaiknya diacak sebagaimana direkomendasikan oleh BIP-0341, sehingga output tanpa jalur key-spend tidak bisa dibedakan dari output Taproot biasa (sebuah manfaat privasi).

#### Dari Simplicity ke Alamat

Mari kita telusuri seluruh derivasi untuk program paling sederhana yang mungkin: `unit : 𝟙 ⊢ 𝟙`, sebuah no-op yang selalu berhasil.

**1. Tag kombinator.** Pertama hitung tag `unit`:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Masukkan tag tersebut dua kali untuk memperoleh CMR program:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. Hash TapLeaf.** Beri awalan CMR dengan versi TapLeaf Simplicity `0xbe` dan panjang CMR `0x20` (32 byte), lalu ambil tagged hash TapLeaf Elements (sebuah tagged hash adalah `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Dengan hanya satu leaf ini tidak ada TapBranch, sehingga hash ini sudah menjadi root TapTree.

**4. TapTweak.** Karena kita tidak menginginkan jalur key-spend, kita menggunakan titik NUMS BIP-0341 sebagai kunci internal dan men-tweak-nya dengan root TapTree:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Kunci output.** Tweak kunci internal pada kurva, `output_pk = lift_x(internal_pk) ⊕ t·G` (aritmetika kurva eliptik dirangkum di sini), menghasilkan kunci output x-only `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Alamat Bech32m.** Encode kunci output x-only, beri awalan karakter `p` (karakter witness-version SegWit v1), tambahkan prefiks human-readable Liquid-testnet `tex1`, dan tambahkan checksum Bech32m. Alamat akhirnya adalah:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Itu banyak sekali pekerjaannya — tetapi sebagian besar diamanatkan oleh Taproot itu sendiri, bukan oleh Simplicity.

### Ekspresi Witness

Sebuah jenis kombinator baru mengatasi ketiadaan input pada program Simplicity: ekspresi witness. Kombinator `witness` memungkinkan data tanda tangan dan materi witness lainnya diintegrasikan ke dalam program.

```
      w : B
-----------------
witness w : A ⊢ B
```

Semantik dari ekspresi witness ini sederhana: ia mengabaikan inputnya dan hanya mengembalikan nilai `w` (yang bisa berupa tipe Simplicity apa pun), yaitu `⟦witness w⟧(a) = w`. Ini **tidak menambahkan ekspresivitas baru** — berdasarkan teorema kelengkapan, Simplicity sudah bisa membangun fungsi konstan semacam itu (ingat kembali macro `scribe` dari bab-bab sebelumnya). Inti dari kombinator `witness` sepenuhnya terletak pada **CMR**-nya: nilai `w` **dikecualikan** dari CMR ekspresi tersebut, sehingga alamat bisa dihitung sebelum `w` diketahui, dan `w` disediakan pada saat penebusan.

Pilihan desain ini mendukung pemangkasan (pruning) — cabang kondisional yang tidak dieksekusi tidak perlu diungkapkan on-chain, termasuk ekspresi witness yang terkait dengannya. Ketika sebuah cabang dipangkas, verifier hanya membutuhkan CMR dari subtree yang dipangkas, bukan konten sebenarnya.

### Nilai Witness

Mungkin terlihat sebagai keterbatasan bahwa ekspresi witness hanya bisa menyimpan sebuah *nilai*, bukan ekspresi Simplicity yang lebih umum. Tetapi program untuk blockchain berbasis UTXO hanya dieksekusi satu kali. Tidak perlu meneruskan sebuah sub-ekspresi utuh ke dalam node witness: pengguna cukup menjalankan sub-ekspresi tersebut sendiri, secara off-chain, dan menyalin outputnya ke dalam nilai witness untuk memperoleh hasil yang persis sama.

(Nanti dalam kursus ini kita akan berjumpa dengan kombinator `disconnect`, yang berperilaku mirip ekspresi witness tetapi *memang* mengambil seluruh ekspresi Simplicity sebagai argumennya.)

Sebuah desain alternatif akan memasukkan semua data witness sebagai argumen ke program Simplicity tingkat atas. Ekspresi witness lebih disukai karena dua alasan. Pertama, **pemangkasan (pruning)**: cabang yang tidak dieksekusi dari ekspresi `case` tidak pernah diungkapkan on-chain, dan ekspresi witness apa pun di dalam cabang-cabang tersebut ikut dipangkas bersamanya. Kedua, **lokalitas**: ekspresi witness memungkinkan kita menempatkan setiap nilai witness tepat di tempat ia digunakan, alih-alih meneruskannya dari input tingkat atas program.

### Inferensi Tipe

Karena CMR tidak melakukan commit pada tipe, sistem tipe direkonstruksi selama penebusan (redemption). Algoritme inferensi tipe Simplicity menentukan tipe minimal untuk setiap subekspresi berdasarkan struktur kombinatornya. Lebih tepatnya, inferensi menghitung tipe *principal* (paling umum) dari setiap subekspresi; variabel tipe apa pun yang tetap bebas kemudian dijadikan instance ke tipe unit `𝟙`, yang menghasilkan tipe yang unik dan minimal untuk program tersebut.

### Kesimpulan

Di bab ini kita menetapkan bahwa program Simplicity adalah ekspresi bertipe `𝟙 ⊢ 𝟙`, menjelaskan bagaimana Commitment Merkle Root dikonstruksi dari tagged SHA-256 hash setiap kombinator, dan menunjukkan bagaimana CMR diubah menjadi alamat on-chain melalui Taproot BIP-0341. Kita memperkenalkan ekspresi witness sebagai mekanisme untuk menyediakan data tanda tangan dan input lain pada saat pembelanjaan tanpa melakukan commit pada nilainya saat pembuatan alamat.

# Bagian Akhir

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Ulasan & Penilaian

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Ujian Akhir

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Kesimpulan

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
</content>
