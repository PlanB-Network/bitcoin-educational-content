---
term: BIP
---

Singkatan dari "Bitcoin Improvement Proposal" (Usulan Peningkatan Bitcoin). Sebuah Bitcoin Improvement Proposal (BIP) adalah proses formal untuk mengusulkan dan mendokumentasikan peningkatan serta perubahan pada protokol Bitcoin dan standar-standarnya. Karena Bitcoin tidak memiliki entitas pusat untuk memutuskan pembaruan, BIP memungkinkan komunitas untuk menyarankan, mendiskusikan, dan mengimplementasikan peningkatan secara terstruktur dan transparan. Setiap BIP merinci tujuan dari peningkatan yang diusulkan, justifikasi, dampak potensial terhadap kompatibilitas, serta kelebihan dan kekurangan. BIP dapat ditulis oleh anggota komunitas mana pun, tetapi harus disetujui oleh pengembang lain dan editor yang memelihara basis data GitHub Bitcoin Core: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun, dan Ruben Somsen. Namun, penting untuk dipahami bahwa peran individu-individu ini dalam mengedit BIP tidak berarti mereka mengontrol Bitcoin. Jika seseorang mengusulkan peningkatan yang tidak diterima dalam kerangka kerja BIP formal, mereka masih dapat menyajikannya langsung kepada komunitas Bitcoin atau bahkan membuat fork yang mencakup modifikasi mereka. Keuntungan dari proses BIP terletak pada formalitas dan sentralisasinya, yang memfasilitasi debat untuk menghindari perpecahan di antara pengguna Bitcoin, berupaya mengimplementasikan pembaruan secara konsensual. Pada akhirnya, prinsip mayoritas ekonomi yang menentukan dinamika kekuasaan dalam protokol.

BIP diklasifikasikan ke dalam tiga kategori utama:
* *Standards Track BIPs*: Menyangkut modifikasi yang secara langsung mempengaruhi implementasi Bitcoin, seperti aturan validasi transaksi dan blok;
* *Informational BIPs*: Memberikan informasi atau rekomendasi tanpa mengusulkan perubahan langsung pada protokol;
* *Process BIPs*: Mendeskripsikan perubahan dalam prosedur yang mengelilingi Bitcoin, seperti proses tata kelola.

Standards Track dan Informational BIP juga diklasifikasikan berdasarkan "Layer":
* *Consensus Layer*: BIP di lapisan ini menyangkut aturan konsensus Bitcoin, seperti modifikasi pada aturan validasi blok atau transaksi. Proposal ini bisa berupa soft forks (modifikasi yang kompatibel ke belakang) atau hard forks (modifikasi yang tidak kompatibel ke belakang). Sebagai contoh, BIP untuk SegWit dan Taproot termasuk dalam kategori ini;
* *Peer Services*: Lapisan ini menyangkut operasi jaringan node Bitcoin, yaitu bagaimana node menemukan dan berkomunikasi satu sama lain di Internet.
* *API/RPC*: BIP di lapisan ini menyangkut Application Programming Interfaces (API) dan Remote Procedure Calls (RPC) yang memungkinkan perangkat lunak Bitcoin berinteraksi dengan node;
* *Applications Layer*: Lapisan ini berkaitan dengan aplikasi yang dibangun di atas Bitcoin. BIP dalam kategori ini biasanya menangani modifikasi pada tingkat standar dompet Bitcoin.

Proses pengajuan BIP dimulai dengan konseptualisasi dan diskusi ide di milis *Bitcoin-dev*. Jika ide tersebut menjanjikan, penulis merancang BIP mengikuti format tertentu dan mengirimkannya melalui Pull Request di repositori GitHub Core. Editor meninjau proposal ini untuk memverifikasi bahwa semua kriteria terpenuhi. BIP harus secara teknis layak, bermanfaat bagi protokol, mematuhi format yang diperlukan, dan sesuai dengan filosofi Bitcoin. Jika BIP memenuhi kondisi ini, secara resmi diintegrasikan ke dalam repositori GitHub BIP. Kemudian, BIP tersebut diberi nomor. Nomor ini umumnya diputuskan oleh editor, sering kali Luke Dashjr, dan diberikan secara logis: BIP yang menangani subjek serupa sering menerima nomor berurutan.

BIP kemudian melalui status yang berbeda selama siklus hidupnya. Status saat ini ditentukan dalam header setiap BIP:
* Draft: Proposal masih dalam fase perancangan dan debat;
* Diajukan: BIP dianggap lengkap dan siap untuk ditinjau oleh komunitas;
* Ditunda: BIP ditahan untuk nanti oleh juara atau editor;
* Ditolak: Sebuah BIP diklasifikasikan sebagai ditolak jika tidak menunjukkan aktivitas selama 3 tahun. Penulisnya dapat memilih untuk melanjutkannya lagi, yang akan memungkinkannya kembali ke status draf;
* Ditarik: BIP telah ditarik oleh penulisnya;
* Final: BIP diterima dan secara luas diimplementasikan pada Bitcoin;
* Aktif: Hanya untuk BIP proses, status ini ditetapkan setelah konsensus tertentu tercapai;
* Digantikan / Usang: BIP tidak lagi berlaku atau telah digantikan oleh usulan yang lebih baru yang membuatnya tidak perlu.

![](../../dictionnaire/assets/25.png)

> ► *BIP adalah akronim untuk "Bitcoin Improvement Proposal". Dalam bahasa Prancis, ini dapat diterjemahkan sebagai "Proposition d'amélioration de Bitcoin". Namun, kebanyakan teks Prancis langsung menggunakan akronim "BIP" sebagai kata benda umum, terkadang feminin, terkadang maskulin.*