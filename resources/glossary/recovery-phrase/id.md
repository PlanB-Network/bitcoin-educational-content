---
term: FRASA PEMULIHAN

---
Frasa pemulihan, juga kadang-kadang disebut frasa mnemonik, _seed phrase_ atau frasa rahasia, adalah daftar yang biasanya terdiri dari 12 atau 24 kata, yang dihasilkan dengan cara acak semu dari sumber entropi. Urutan acak semu selalu dilengkapi dengan _checksum_. Frasa mnemonik, bersama dengan _passphrase_ opsional, digunakan untuk mendapatkan semua kunci yang terkait dengan dompet HD (_Hierarchical Deterministic_) secara deterministik. Ini berarti bahwa dari frasa ini, dimungkinkan untuk secara deterministik menghasilkan dan membuat ulang semua kunci privat dan publik dari dompet Bitcoin, dan mengakses dana yang terkait dengannya. Tujuan dari frasa pemulihan adalah untuk menyediakan sarana pencadangan dan pemulihan bitcoin yang aman dan mudah digunakan.

Sangatlah penting untuk menyimpan frasa ini di tempat yang aman dan terlindung, karena setiap orang yang memiliki _mnemonic_ ini akan memiliki akses ke dana dari dompet yang bersangkutan. Jika digunakan dalam konteks dompet tradisional, dan tanpa kata sandi opsional, frasa ini sering kali merupakan sebuah SPOF (_Single Point Of Failure_). Frasa pemulihan adalah sebuah pengkodean dari urutan _pseudo-random_ dan _checksum_ ke dalam kata-kata sehari-hari untuk memfasilitasi notasi dan keterbacaannya oleh manusia. Frasa ini dibuat sesuai dengan standar BIP39, yang mendefinisikan dan menyusun daftar 2048 kata yang digunakan untuk pengkodean ini.

> ► *Daftar 2048 kata dari BIP39 tersedia dalam beberapa bahasa, namun disarankan untuk hanya menggunakan versi bahasa Inggris, karena ini adalah versi yang paling banyak didukung oleh perangkat lunak dompet*
