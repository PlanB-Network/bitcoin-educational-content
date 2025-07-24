---
name: JoinMarket

description: Panduan dan tutorial tentang cara menggunakan JoinMarket untuk melakukan CoinJoin melalui Bitcoin melalui baris perintah
---

![cover](assets/cover.webp)



---

Jika Anda menemukan halaman ini dengan mencari "JoinTmarket" secara online, Anda patut mendapatkan apresiasi yang tulus. Namun, Anda telah menemukan panduan yang membahas topik yang sama sekali berbeda, tetapi sangat menarik! 🚬🍁



Tujuan dari tutorial ini adalah untuk mengilustrasikan pengoperasian JoinMarket secara teoritis dan praktis, melalui baris perintah. 🐢 💚



## Definisi Teoritis JoinMarket



Kita dapat mendefinisikan JoinMarket sebagai alat, atau Wallet, yang memungkinkan CoinJoin dengan pengguna lain dengan cara yang sepenuhnya Trustless dan tanpa koordinator pusat.



Karena seluruh bagian teoretis dari alat ini sangat luas, saya memutuskan untuk menguraikannya dalam episode khusus podcast saya. Bagi mereka yang bisa memahami bahasa Italia, saya sangat menyarankan untuk melanjutkan membaca setelah mendengarkan episode ini, supaya dapat mengasimilasi konsep dasar untuk menggunakan program ini dengan baik.



Anda dapat mengikuti episode ini di tautan langsung berikut ini:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor] (https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (di sini Anda dapat mendengarkannya langsung dari browser).
- [Antenna pod](https://antennapod.org/) adalah pengelola podcast gratis dan sumber terbuka yang tidak memerlukan registrasi. Untuk menemukan episode, unduh aplikasinya, tambahkan podcast saya secara manual dengan menempelkan [tautan ini] (https://Anchor.fm/s/bd5d5b20/podcast/rss) di bagian _feed rss_, lalu cari episode yang didedikasikan untuk JoinMarket.



## Instalasi



Sistem operasi:





- Raspiblitz
- Payung
- MyNode
- Raspibolt



## File Konfigurasi



JoinMarket adalah perangkat lunak yang dapat disesuaikan dengan jumlah pengaturan yang tidak terbatas; pengaturan ini ditentukan dalam file konfigurasi yang terletak di direktori program utama yang disebut `Joinmarket.cfg`.



Pada bagian ini, kita akan membahas beberapa bidang yang mungkin menarik untuk Anda jelajahi dan/atau modifikasi, tergantung kebutuhan Anda. Saya ingin menekankan bahwa semua perubahan yang tercantum di bawah ini berguna untuk diketahui, untuk menyesuaikan pengoperasian perangkat lunak dengan kebutuhan pribadi, tetapi tidak bersifat wajib.



Pertama, mari kita masuk ke folder `joinmarket/scripts` dan jalankan perintah:



```bash
python wallet-tool.py generate
```


Pada titik ini kita akan mendapatkan kesalahan, tetapi hal ini akan menyebabkan perangkat lunak untuk generate file pengaturan yang telah ditetapkan sebelumnya untuk kita. Kita dapat pergi dan mengedit file pengaturan dari terminal dengan:



```bash
nano joinmarket.cfg
```



atau:



```bash
vim joinmarket.cfg
```



setelah dibuka, kita akan melihat banyak baris dengan berbagai pengaturan dan penjelasannya dalam bahasa Inggris. Secara khusus kami akan menganalisis variabel yang paling menarik di bawah ini:





- `merge_algorithm` jika kita sebagai pembuat, bidang ini menyesuaikan seberapa agresif perangkat lunak akan mengkonsolidasikan Output yang tidak terpakai. Jika kita memiliki banyak UTXO untuk dikonsolidasikan, mungkin masuk akal untuk beralih dari _gradual_ ke _greedy_
- `tx_fees` menyesuaikan sebagai pengambil biaya untuk membayar transaksi, akan sangat berguna untuk mengubah pengaturan ini jika Anda sering menggunakan tumbler (kita akan membahasnya nanti) karena jika terjadi lonjakan biaya selama eksekusi transaksi, jika kita tidak mengatur bidang ini dengan benar, kita berisiko menghabiskan banyak Sats untuk CoinJoin. Dengan menetapkan nilai dalam ribuan (seperti 2000), ini akan setara dengan 2 Sats/vBytes, 3500 hingga 3,5 Sats/vBytes, dan seterusnya. Saya akan merekomendasikan angka yang berkisar antara 1500 hingga 6000, tergantung kebutuhan Anda.
- `max_cj_fee_abs` digunakan untuk menentukan berapa banyak yang bersedia kita bayarkan secara absolut untuk pembuat yang kita pilih selama CoinJoin. Secara default, bidang ini untuk pembuat adalah 200 Sats, pilihan yang baik mungkin adalah angka yang berkisar antara 200 hingga 1000 Sats per mitra (ini didasarkan pada berapa banyak yang ingin Anda belanjakan dan berapa banyak anon-set yang Anda cari untuk CoinJoins Anda)
- `max_cj_fee_rel` memiliki fungsi yang sama dengan bidang di atas, tetapi menentukan biaya relatif (persentase) yang bersedia kita bayarkan kepada setiap rekanan. Karena ini adalah nilai `persentase`, berhati-hatilah untuk tidak menetapkan nilai yang tinggi untuk menghindari biaya yang tinggi di CoinJoins dengan jumlah yang besar. Nilai default untuk pembuat adalah _0.00002_, saya merekomendasikan nilai yang sama atau sedikit lebih tinggi.
- `minimum_makers` adalah bidang yang menentukan berapa banyak rekanan lain yang melakukan CoinJoin dengan kita, secara default joinMarket selalu memilih dari 4 hingga 9 rekanan, jika kita ingin, untuk privasi yang lebih baik, kita dapat meningkatkan nilai ini menjadi 5 atau 6 (ini akan membuat transaksi lebih mahal).
- `cjfee_a` menentukan, jika kita bertindak sebagai pembuat, berapa banyak Sats secara absolut yang ingin kita kumpulkan untuk menyewa likuiditas kita. Kolom ini sangat subjektif, nilai defaultnya sudah sangat bagus (dengan demikian kita akan memiliki privasi yang lebih baik sebagai pembuat), kita dapat mempertimbangkan untuk mengubahnya menjadi 0 jika kita ingin menghasilkan lebih banyak CoinJoin dalam waktu yang lebih singkat.
- `cjfee_r` sama seperti kolom di atas tetapi dalam bentuk persentase dan bukan absolut. Sekali lagi saya sarankan untuk membiarkan nilai default atau menurunkannya untuk menarik lebih banyak peminat.
- `ordertype` dengan bidang ini kita memilih dari pembuat apakah akan menagih secara absolut (absoffer) atau persentase (reloffer). Biasanya pengambil lebih memilih penawaran absolut untuk masalah ekonomi.
- 'minsize' jika sebagai pembuat kita tidak ingin memiliki UTXO yang terlalu kecil, kita dapat menentukan CoinJoin minimum untuk berpartisipasi. Bidang ini dinyatakan dalam Satoshi dan benar-benar subjektif. Kita dapat membiarkan bidang ini pada 0 atau meningkatkannya menjadi 500000 (Sats), 1000000 (Sats), dan seterusnya.



Berhati-hatilah untuk tidak mengedit bidang yang salah, beberapa variabel dalam file joinmarket.cfg jika diatur dengan tidak benar dapat membahayakan fungsionalitas perangkat lunak atau benar-benar memusnahkan privasi Anda, buka mata dan waspadalah secara maksimal!



## Pengaturan Lingkungan Kerja



Beberapa node secara otomatis menetapkan nilai yang benar untuk bidang-bidang ini di dalam file joinmarket.cfg, saya sarankan untuk memeriksa ulang secara manual:





- `rpc_user = nama pengguna Anda-seperti-dalam-Bitcoin.conf`
- `rpc_password = kata sandi Anda-seperti-dalam-Bitcoin.conf`
- `rpc_host = localhost #default biasanya benar`
- `rpc_port = 8332 # default untuk Mainnet`



Pada titik ini kita dapat melanjutkan dengan pembuatan Wallet kita di dalam JoinMarket:



```bash
python wallet-tool.py generate
```



Perintah ini akan meminta kita memasukkan kata sandi untuk mengenkripsi Wallet dan nama yang ingin kita berikan, ketika ditanya apakah Anda ingin mendukung fidelity bonds atau tidak, saya sarankan untuk menggunakan opsi _yes_, output yang dikembalikan akan terlihat seperti ini:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


jika terjadi kesalahan, kemungkinan besar kami telah salah mengatur 4 bidang RPC yang ditentukan di atas. Dalam hal ini, mungkin akan membantu jika Anda mengikuti [panduan ini] (https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) yang terdapat pada dokumentasi asli JoinMarket.



Kita telah menyelesaikan pengaturan lingkungan kerja kita dan dapat mulai menjelajahi perintah yang akan paling berguna bagi kita. Semua skrip yang akan kita bahas dapat dijalankan di konsol diikuti dengan `--help` untuk penjelasan yang lebih mendalam.



Sekarang kita bisa mencoba meluncurkannya:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



perintah ini akan menunjukkan kepada Anda semua berbagai mixdepth Wallet dengan berbagai alamat yang dikategorikan:




- Baru (Address tidak pernah digunakan)
- Penukaran (sisa transaksi sebelumnya)
- Cj-out (output dari CoinJoin)



berikut ini adalah contoh praktis dari hasilnya:



```bash
JM wallet
mixdepth	0	xpub6CMAJ67vZWVXuzjzYXUoJgWrmuvFRiqiUG4dwoXNFmJtpTH3WgviANNxGyZYo27zxbMuqhDDym6fnBxmGaYoxr6LHgNDo1eEghkXHTX4Jnx
external addresses	m/84'/0'/0'/0	xpub6FFUn4AxdqFbnTH2fyPrkLreEkStNnMFb6R1PyAykZ4fzN3LzvkRB4VF8zWrks4WhJroMYeFbCcfeooEVM6n2YRy1EAYUvUxZe6JET6XYaW
m/84'/0'/0'/0/0     	bc1qt493axn3wl4gzjxvfg03vkacre0m6f2gzfhv5t	0.00000000	new
m/84'/0'/0'/0/1     	bc1q2av9emer8k2j567yzv6ey6muqkuew4nh4rl85q	0.00000000	new
m/84'/0'/0'/0/2     	bc1qggpg0q7cn4mpe98t29wte2rfn2rzjtn3zdmqye	0.00000000	new
m/84'/0'/0'/0/3     	bc1qnnkqz8vcdjan7ztcpr68tyec7dw2yk8gjnr9ze	0.00000000	new
m/84'/0'/0'/0/4     	bc1qud5s2ln88ktg83hkr6gv9s576zvt249qn2lepx	0.00000000	new
m/84'/0'/0'/0/5     	bc1qw0lhq7xlhj7ww2jdaknv23vcyhnz6qxg23uthy	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/0'/1
Balance:	0.00000000
Balance for mixdepth 0:	0.00000000
mixdepth	1	xpub6CMAJ67vZWVXyTJEaZndxZy9ACUufsmNuJwp9k5dHHKa22zQdsgALxXvMRFSwtvB8BRJzsd8h17pKqoAyHtkBrAoSqC9AUcXB1cPrSYATsZ
external addresses	m/84'/0'/1'/0	xpub6FNSLcHuGnoUbaiKgwXuKpfcbR63ybrjaqHCudrma13NDqMfKgBtZRiPZaHjSbCY3P3cgEEcdzZCwrLKXeT5jeuk8erdSmBuRgJJzfNnVjj
m/84'/0'/1'/0/0     	bc1qhrvm7kd9hxv3vxs8mw2arcrsl9w37a7d6ccwe4	0.00000000	new
m/84'/0'/1'/0/1     	bc1q0sccdfrsnjtgfytul5zulst46wxgahtcf44tcw	0.00000000	new
m/84'/0'/1'/0/2     	bc1qst6p8hr8yg280zcpvvkxahv42ecvdzq63t75su	0.00000000	new
m/84'/0'/1'/0/3     	bc1q0gkarwg8y3nc2mcusuaw9zsn3gvzwe8mp3ac9h	0.00000000	new
m/84'/0'/1'/0/4     	bc1qkf5wlcla2qlg5g5sym9gk6q4l4k5c98vvyj33u	0.00000000	new
m/84'/0'/1'/0/5     	bc1qz6zptlh3cqty2tqyspjk6ksqelnvrrrvmyqa5v	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/1'/1
Balance:	0.00000000
Balance for mixdepth 1:	0.00000000
mixdepth	2	xpub6CMAJ67vZWVY2cq5fmVxXw92fcgTchphGNFxweSiupYH1xYfjBiK6dj5wEEVAQeA4JcGDQGm2xcuz2UsMnDkzVmi2ESZ3xey63mQMY4x2w2
external addresses	m/84'/0'/2'/0	xpub6DqkbMG3tj2oixGYniEQTFamLCHTZx9CeAbUdBttiGuYwgfGZbrLMor8LWeJBUqTpsa81JcJqAUXuDxhXdLpKDxJAEqKMqPgJyXstj5dp3o
m/84'/0'/2'/0/0     	bc1qwtdgg928wma8jz32upkje7e4cegtef7yrv233l	0.00000000	new
m/84'/0'/2'/0/1     	bc1qhkuk2gny4gumrxcaw999uq3jm3fjrjvcwz7lz3	0.00000000	new
m/84'/0'/2'/0/2     	bc1qvu753lkltc8akfasclnq89tdv8yylu2alyg76y	0.00000000	new
m/84'/0'/2'/0/3     	bc1qal3r040k26cw2f08337huzcf00hrnws5rhfrz3	0.00000000	new
m/84'/0'/2'/0/4     	bc1qpv4nm7wwtxesgwsr0g0slxls33u0w02gqx2euk	0.00000000	new
m/84'/0'/2'/0/5     	bc1qk3ekjzlvw3uythw738z7nvwe2sg93w2rtuy6ml	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/2'/1
Balance:	0.00000000
Balance for mixdepth 2:	0.00000000
mixdepth	3	xpub6CMAJ67vZWVY3uty61M6jeGheGU5ni5mQmqMW2QLQbEa8ZQXuBw1K2umKFZsmU8EMEafJZKQkGS1trtWE5dtz4XmDbvLvUccAPn26ZC5i2o
external addresses	m/84'/0'/3'/0	xpub6EvT4QFPRdkt2sji3QdLLZjkJQmk7G2y3umT99ceomKTXGYvZ5S9TLaGos6cEugXEuxS6s9kvSUj1Xvpiu65dn5yzK7CgdZLzXawpKC9Mpe
m/84'/0'/3'/0/0     	bc1q9ph5l2gknjezcmzv84rnhu4df566jgputzef7l	0.00000000	new
m/84'/0'/3'/0/1     	bc1qrlvmmxfuryr3mfhssjv45h0fl6s43g3vzrkwca	0.00000000	new
m/84'/0'/3'/0/2     	bc1q40xkajgv9q42ve92zstwjc9v4jgauxme9su6uc	0.00000000	new
m/84'/0'/3'/0/3     	bc1q38pfk8yfnu97v4mckkuk2dhk9u8geuyzu9c0hc	0.00000000	new
m/84'/0'/3'/0/4     	bc1q2qzxyw56em9qdxc5z5s5xjz3j6s2qlzn3juvtu	0.00000000	new
m/84'/0'/3'/0/5     	bc1qd2f8f3dau5pfjqu7dpuvt6fahj36w4rgl3xevr	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/3'/1
Balance:	0.00000000
Balance for mixdepth 3:	0.00000000
mixdepth	4	xpub6CMAJ67vZWVY7gT4oJQBMc1fhbausT57yNVLCLCMwaGed5spHKaQY1EMQxvL2vTgDfhEimuAy7bzBE1qx5uY6D7cpUjQtXPHpyJzFuUtQPN
external addresses	m/84'/0'/4'/0	xpub6EQWpKsBTG3N9TFU4v6WtCcBJuLAeTZTcUwVJTxYUAsHeVPFdey4qT1dg4G7MqvnFFgHZDxqTo37S81UWUA2BqKKoTff1pcHTcSFzxyp5JG
m/84'/0'/4'/0/0     	bc1qdpjh3ewm367jm5eazqdf8wfrm09py50wn47urs	0.00000000	new
m/84'/0'/4'/0/1     	bc1q2x0fmtms5nr3wz3x3660c8wampg7t22e6m30t8	0.00000000	new
m/84'/0'/4'/0/2     	bc1q23595yg3dkj8gd3jrgup0hyzslhzf9skrg50r5	0.00000000	new
m/84'/0'/4'/0/3     	bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl	0.00000000	new
m/84'/0'/4'/0/4     	bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes	0.00000000	new
m/84'/0'/4'/0/5     	bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/4'/1
Balance:	0.00000000
Balance for mixdepth 4:	0.00000000
Total balance:	0.00000000
```


Sekarang kita dapat melanjutkan untuk menyimpan Satoshi pertama kita dalam satu atau beberapa alamat mengingat bahwa terlepas dari pembuat atau pengambil, perangkat lunak tidak akan pernah pergi dan mengkonsolidasikan UTXO ke dalam kedalaman campuran yang berbeda secara langsung, dengan cara ini kita dapat menjaga Satoshi dengan tingkat privasi yang berbeda tetap terpisah di dalam Wallet.



## Mengirim Bitcoin dengan CoinJoin Single



Sekarang kita bisa menggerakkan Satoshi kita. Salah satu perintah utama dalam perangkat lunak ini adalah skrip:



```bash
pyhton sendpayment.py
```


yang memungkinkan kita mengirim transaksi ke alamat lain dengan atau tanpa CoinJoin. Mari kita bahas bagaimana cara kerjanya dan beberapa contoh praktis. Secara default, format perintahnya adalah (ingatlah untuk mengganti teks yang diapit oleh simbol < dan >):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



contoh penggunaan yang mendasar:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


dalam hal ini kita akan mengirim ke Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc yaitu 5000000 Satoshi dari mixdepth 0 (default) dengan memilih 4 hingga 9 pasangan untuk CoinJoin (opsi default).



Untuk memiliki kontrol lebih besar atas bagaimana dan UTXO mana yang akan dibelanjakan, kita dapat melihat opsi tambahan untuk perintah ini:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


dalam contoh ini kita telah menambahkan dua spesifikasi: -N menunjukkan berapa banyak rekanan yang akan kita campur, -m kedalaman campuran dari mana kita akan menarik dana. Faktanya, kita telah mengirim 100.000.000 Sats (1 btc) ke Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c dengan dana di mixdepth 1 dan dicampur dengan 5 mitra pengimbang.



Jika kita memasukkan 0 sebagai nilai kirim dengan menentukan mixdepth, joinMarket akan melakukan apa yang disebut `sweep`, yaitu, ia akan mengirim semua dana dalam mixdepth tersebut dengan menggabungkannya satu sama lain:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



di sini kami mengirim semua dana dari mixdepth 0 (kami bisa saja tidak menentukannya karena itu adalah default) pencampuran dengan 7 rekan.



Perintah sendpayment digunakan untuk memindahkan dana dari joinMarket ke Wallet eksternal atau untuk mengirim Satoshi ke seseorang dengan menambahkan Layer privasi antara kita dan dia. Untuk mendapatkan tingkat privasi yang memadai pada UTXO kita, akan lebih tepat jika kita menggunakan perintah tumbler.py yang akan kita jelaskan nanti dalam panduan ini.



## Menjadi Seorang Pembuat



Skrip yang akan kita bahas dalam bagian ini adalah:



```bash
yg-privacyenhanced.py
```



Program ini digunakan untuk bertindak sebagai pembuat di joinMarket. Perangkat lunak ini akan terhubung ke node Bitcoin kami dan ke pasar internal platform tempat pembuat menampilkan diri mereka sebagai penawar dan pengambil likuiditas untuk mencari rekanan. Jika Anda ingin menggunakan fidelity bond, Anda dapat membuatnya dengan format ini:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



misalnya:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



output yang akan dikembalikan kepada kami adalah Bitcoin Address (yaitu, yang Anda perlukan untuk menyetor dana yang ingin Anda alokasikan ke fidelity).



**Perhatian**: Ada dua hal yang perlu diperhatikan jika Anda akan membuat Fidelity Bond (alias FB);





- setelah dana disetorkan, dana tersebut tidak dapat dipindahkan lagi hingga masa berlakunya habis. Perhatikan berapa banyak Satss yang Anda kirimkan ke Address dan bagaimana Anda memformat tanggalnya. Kesalahan tidak diperbolehkan!
- Fidelity bond mudah dikenali di blockchain, jadi disarankan untuk menyetor dana melalui CoinJoin dan dengan asal yang tidak terkait dengan identitas Anda. Hal yang sama juga disarankan untuk dilakukan ketika Anda ingin memindahkan fidelity bond yang sudah kedaluwarsa dari JoinMarket.



Penting untuk diingat bahwa Anda dapat mengisi ulang obligasi kesetiaan hanya dengan satu transaksi, dalam kasus kelipatan UTXO hanya kelipatan terbesar yang akan dianggap valid untuk FB.



Sekarang mari kita bahas skrip yang disebutkan di awal paragraf ini, setelah kita membuat fidelity bond (yang perlu diingat bahwa ini bersifat opsional), kita siap untuk menjalankan eksekusi yang dapat digunakan sebagai pembuat di joinMarket. Setelah Satss disimpan di berbagai alamat dan mixdepth, kita dapat menjalankan perintah:



```bash
python yg-privacyenhanced.py <wallet name>
```



Mulai saat ini (setelah beberapa menit terhubung ke jaringan) dan sampai kita menghentikan skrip, klien JoinMarket kita akan muncul di daftar pembuat aktif di protokol dan menawarkan likuiditas kita ke berbagai rekanan untuk membuat CoinJoin. Jangan mengharapkan puluhan CoinJoins per hari (kecuali Anda memiliki fidlity yang sangat besar dan likuiditas yang besar yang disimpan di Wallet), juga ingat bahwa faktor-faktor seperti biaya yang diperlukan dan Satoshi yang disimpan mempengaruhi seberapa sering Anda akan menjadi pembuat.



Dengan menjalankan perintah di bawah ini, Anda akan dapat melihat riwayat semua transaksi yang dilakukan pada Wallet dan setiap keuntungan (jika Anda adalah pembuat) atau pengeluaran biaya (jika Anda adalah pengambil) yang Anda miliki selama masa pakai Wallet.



```bash
python wallet-tool.py <wallet name> history
```



Setelah Satoshi Anda melakukan CoinJoin, mereka akan berpindah dari satu mixdepth ke mixdepth lainnya hingga mencapai mixdepth terakhir. Setelah melewati yang keempat, mereka akan kembali ke mixdepth 0, terserah Anda berapa banyak privasi yang didapat sebelum memindahkannya ke Cold Wallet, disarankan untuk menyelesaikan satu siklus Wallet penuh.



## Tumbler



Akhirnya kita sampai pada bagian paling menarik dari JoinMarket, yaitu tumbler! Jika Anda sudah mendengarkan podcastnya, Anda pasti sudah tahu tentang apa yang dimaksud. Satu rekomendasi sebelum kita mulai: **Waspadalah terhadap biaya!** Ingatlah untuk mengatur batasan dalam file joinmarket.cfg (seperti yang dijelaskan di awal) dan pertimbangkan untuk menjalankan program ini hanya jika biaya onchain relatif rendah (di bawah 10 Sats/vB).



Untuk meluncurkan tumbler, Anda harus menghentikan skrip dari pembuatnya (jika masih aktif), setelah itu kita dapat menjalankan perintah:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Sangat penting untuk memasukkan **setidaknya** 3 alamat keluaran untuk tumbler: ini untuk memastikan privasi yang baik dan tidak membuat hubungan yang jelas antara UTXO selama proses berlangsung. Seperti biasa, dengan menambahkan `--help` pada perintah, Anda dapat melihat semua detail tambahan. Mari kita lihat contoh yang lebih kompleks dengan aturan yang lebih lanjut:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



Dalam hal ini kita telah meluncurkan skrip tumbling yang tidak akan menggunakan jumlah counterpart default (parameter -N menunjukkan bahwa kita membutuhkan 7 counterpart dengan varians maksimum 2, sehingga jumlah pembuat acak dari 5 hingga 9) dan dengan jumlah CoinJoin yang lebih besar per mixdepth (secara default skrip ini membuat jumlah acak CoinJoin per bagian Wallet mulai dari 1 hingga 3, dengan menggunakan perintah -c 3 1 sebagai gantinya adalah 2 hingga 4). Dengan cara ini kita akan menghabiskan lebih banyak Sats dalam biaya tetapi memiliki set anonimitas yang lebih besar.



Anda juga dapat menambahkan alamat keluaran sebanyak yang Anda inginkan (minimal 3, tidak ada maksimum selain akal sehat). Namun, karena masalah privasi, tidak mungkin untuk memutuskan bagaimana Satoshi akan didistribusikan di antara alamat-alamat yang ditentukan sebagai output.



Tumbler adalah proses yang sengaja dibuat lama, kadang-kadang mungkin terjadi sesuatu yang berhenti bekerja, dalam banyak kasus ini akan menyelesaikannya sendiri dalam beberapa jam. Jika terjadi kerusakan total, kita dapat mencoba memulai ulang dengan perintah:



```bash
python tumbler.py --restart
```



Atau cukup mulai ulang perintah tumbling yang baru. Ini tidak akan memulai penjadwalan tumbler sebelumnya tetapi akan memulai siklus pencampuran yang baru. Jika menutup terminal SSH ke node Anda juga menghentikan skrip, Anda dapat memanfaatkan program `TMUX` yang dapat diinstal dengan perintah tersebut:



```bash
sudo apt install tmux
```



Meluncurkannya dari shell dengan mengetikkan `tmux` akan membuka terminal untuk Anda yang akan tetap aktif di latar belakang meskipun Anda menutup koneksi jarak jauh. Ketika Anda menyambungkan kembali ke node Anda dengan perintah: `tmux attach` Anda akan membuka kembali shell yang tetap aktif di latar belakang.



## Kesimpulan



JoinMarket adalah perangkat lunak yang tidak terbatas dan dapat disesuaikan. Dalam panduan ini kita telah menemukan fungsi-fungsi utama sehingga memungkinkan bagi siapa saja (atau setidaknya saya telah mencobanya, saya menyadari bahwa menggunakan perangkat lunak ini bukanlah hal yang mudah) untuk menggunakannya. Salah satu masalah terbesar dengan JoinMarket adalah: jumlah orang yang menggunakannya dan menjadi pembuatnya. Jika hanya sedikit pengguna yang memanfaatkan perangkat lunak ini, maka privasi secara keseluruhan (anon-set) akan berkurang. Itulah mengapa saya berharap panduan ini akan mendorong penggunaan dan meyakinkan Anda untuk mengunduh dan menginstal perangkat lunak favorit saya untuk membuat CoinJoin. Jika Anda ingin mendalami lebih dalam beberapa aspek, saya sarankan Anda untuk membaca berbagai dokumen mendalam di github, dokumen-dokumen tersebut dibuat dengan sangat baik dan Anda dapat menemukannya di sini.



Selamat bercengkerama dengan kura-kura!🐢 💚



[Di sini] (https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) Anda dapat mendukung Turtlecute