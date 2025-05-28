---
term: BIP

---
Singkatan dari "_Bitcoin Improvement Proposal_" Bitcoin Improvement Proposal (BIP) adalah sebuah proses formal untuk mengajukan dan mendokumentasikan perbaikan dan perubahan pada protokol Bitcoin dan standar-standarnya. Karena Bitcoin tidak memiliki entitas pusat untuk memutuskan implementasi pembaruan, BIP memungkinkan komunitas untuk merekomendasikan, mendiskusikan, dan mengimplementasikan perbaikan secara terstruktur dan transparan. Setiap BIP memiliki rincian tujuan dari perbaikan yang diusulkan, alasan, potensi dampak terhadap kompatibilitas, serta keuntungan dan kerugiannya. BIP dapat ditulis oleh setiap anggota komunitas, tetapi harus disetujui oleh pengembang lain dan editor yang mengelola basis data Bitcoin Core GitHub: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun, dan Ruben Somsen. Namun, penting untuk dipahami bahwa peran individu-individu ini dalam mengedit BIP bukan berarti mereka yang mengendalikan Bitcoin. Jika seseorang mengusulkan perbaikan yang tidak diterima dalam kerangka kerja BIP formal, mereka masih dapat mempresentasikannya secara langsung kepada komunitas Bitcoin atau bahkan membuat sebuah _fork_ dengan versi termodifikasinya. Keuntungan dari proses BIP terletak pada formalitas dan sentralisasinya, yang memfasilitasi perdebatan untuk menghindari perpecahan di antara para pengguna Bitcoin, yang berusaha untuk mengimplementasikan pembaruan dengan cara yang konsensus. Pada akhirnya, prinsip mayoritas ekonomi lah yang menentukan dinamika kekuatan di dalam protokol.

BIP dapat diklasifikasikan ke dalam tiga kategori utama:

- *Standard Track BIP*: Modifikasi yang secara langsung memengaruhi implementasi Bitcoin, seperti aturan validasi transaksi dan blok;
- *BIP Informasi*: Memberikan informasi atau rekomendasi tanpa mengusulkan perubahan langsung pada protokol;
- *BIP Proses*: Menjelaskan perubahan dalam prosedur seputar Bitcoin, seperti proses tata kelola.

BIP Jalur Standar dan BIP Informasi juga diklasifikasikan berdasarkan "Lapisan":

- *Lapisan Konsensus*: BIP pada lapisan ini berkaitan dengan aturan konsensus Bitcoin, seperti modifikasi blok atau aturan validasi transaksi. Proposal ini dapat berupa _soft fork_ (modifikasi dengan kompatibilitas mundur) atau _hard fork_ (modifikasi yang tidak memiliki kompatibilitas mundur). Sebagai contoh, BIP untuk SegWit dan Taproot termasuk dalam kategori ini;
- *Layanan Peer*: Lapisan ini berkaitan dengan pengoperasian jaringan _node_ Bitcoin, yaitu bagaimana node menemukan dan berkomunikasi satu sama lain di Internet.
- *API/RPC*: BIP pada lapisan ini berkaitan dengan Antarmuka Pemrograman Aplikasi (API) dan Panggilan Prosedur Jarak Jauh (RPC) yang memungkinkan perangkat lunak Bitcoin berinteraksi dengan _node_;
- *Lapisan Aplikasi*: Lapisan ini berkaitan dengan aplikasi yang dibangun di atas Bitcoin. BIP dalam kategori ini biasanya berurusan dengan modifikasi pada tingkat standar dompet Bitcoin.

Proses pengajuan BIP dimulai dengan konseptualisasi dan diskusi ide di _mailing list_ *Bitcoin-dev*. Jika usulan terlihat menjanjikan, penulis membuat konsep BIP dengan mengikuti format tertentu dan mengirimkannya melalui _Pull Request_ di repositori Core GitHub. Para editor akan meninjau proposal ini untuk memverifikasi bahwa proposal tersebut memenuhi semua kriteria. BIP harus layak secara teknis, bermanfaat bagi protokol, sesuai dengan format yang diperlukan, dan sesuai dengan filosofi Bitcoin. Jika BIP memenuhi persyaratan ini, maka secara resmi diintegrasikan ke dalam repositori BIP GitHub. BIP tersebut kemudian akan diberi nomor. Nomor ini biasanya diputuskan oleh editor, biasanya Luke Dashjr, dan diberikan secara logis: BIP yang berhubungan dengan kategori yang serupa sering kali menerima nomor yang berurutan.

BIP kemudian melewati status yang berbeda selama siklus hidupnya. Status saat ini ditentukan dalam header setiap BIP:

- Draf: Proposal ini masih dalam tahap penyusunan dan perdebatan;
- Diusulkan: BIP dianggap lengkap dan siap untuk ditinjau oleh masyarakat;
- Ditangguhkan: BIP ditangguhkan untuk kemudian dipilih oleh pendukung atau editor;
- Ditolak: Sebuah BIP diklasifikasikan sebagai "ditolak" jika tidak menunjukkan aktivitas selama 3 tahun. Penulisnya dapat memilih untuk melanjutkannya nanti, yang akan memungkinkannya kembali ke status draf;
- Ditarik kembali: BIP telah ditarik oleh penulisnya;
- Final: BIP diterima dan diimplementasikan secara luas pada Bitcoin;
- Aktif: Hanya untuk proses BIP, status ini ditetapkan setelah konsensus tertentu tercapai;
- Diganti / Sudah Tidak Berlaku: BIP tidak lagi berlaku atau telah digantikan oleh proposal yang lebih baru yang membuat BIP ini tidak diperlukan lagi.

![](../../dictionnaire/assets/25.webp)

> ► *BIP adalah singkatan dari "Bitcoin Improvement Proposal". Dalam bahasa Indonesia, istilah ini dapat diterjemahkan sebagai "Proposal Pengembangan Bitcoin". Namun, "BIP" juga umum digunakan untuk merujuk pada istilah ini.*
