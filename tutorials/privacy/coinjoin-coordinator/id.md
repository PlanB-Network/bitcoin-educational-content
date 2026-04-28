---
name: Koordinator Coinjoin - WabiSabi
description: Cara mengatur dan menjalankan koordinator coinjoin mengikuti protokol WabiSabi (digunakan dalam Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Pendahuluan 👋


Dalam panduan ahli ini, kami akan membantu Anda menyiapkan koordinator coinjoin, yang pada dasarnya adalah server yang menyatukan orang-orang yang ingin menghemat biaya transaksi atau meningkatkan privasi onchain mereka dalam transaksi kolaboratif. Karena tidak ada lagi koordinator yang dijalankan oleh perusahaan yang dibundel dengan Wasabi Wallet, pengguna harus mencari dan memilih server koordinator pilihan mereka sendiri. Hanya beberapa koordinator yang telah muncul meminta biaya koordinasi 0%, sehingga pengembang Wasabi Wallet telah bekerja keras untuk membuatnya semudah mungkin untuk mulai menjalankan koordinator komunitas Anda sendiri (pada perangkat keras sekecil Raspberry Pi5!). Koordinator yang saat ini aktif dan meminta biaya koordinasi 0% dapat ditemukan di [LiquiSabi] (https://liquisabi.com) dan yang lebih penting lagi di [nostr] (https://github.com/Kukks/WasabiNostr).


## Persyaratan 🫴



- VPS (simpul yang dihosting) atau komputer/server (simpul yang dihosting sendiri)
- Node Bitcoin Core yang dipangkas/Penuh (diuji dengan v29.0)


Opsional:


- (sub) Domain meneruskan lalu lintas ke node (mis. coinjoin.[domain Anda].io)


Disarankan untuk memiliki pengalaman dengan prompt baris perintah dan bash, karena tidak semua langkah dapat diotomatisasi.


Dari segi perangkat keras, disarankan untuk memiliki sistem dengan:


- 4 inti
- rAM 16 GB
- 2 TB SSD atau NVMe (untuk node penuh) / 128 GB SSD (untuk node pruned)


Persyaratan seperti itu dapat disediakan oleh Raspberry Pi 5 hanya dengan 120 $, tidak termasuk penyimpanan yang harganya sekitar 100 $ untuk stik NVMe 2TB.


VPS murah biasanya hanya dilengkapi dengan 1 core dan RAM 4GB, yang menurut saya terlalu kecil untuk menyinkronkan dan memverifikasi seluruh bitcoin blockchain pada blockheight 911817.


Dari segi penyimpanan, sebuah node penuh akan membutuhkan penyimpanan disk minimal 2TB, lebih disukai jenis SSD atau NVMe. Ketika memangkas blockchain, drive penyimpanan yang jauh lebih kecil dapat diterima (misalnya SSD 128GB).


Jika Anda berniat menjalankan koordinator untuk coinjoin yang besar (300+ input), disarankan untuk memilih sistem dengan core yang lebih cepat/lebih baru dengan kinerja yang lebih tinggi untuk semua verifikasi tanda tangan.


## Instalasi 🛠️


Pada node kita ingin mengunduh dan menginstal versi terbaru dari Wasabi Wallet, yang mencakup backend dan koordinator sebagai eksekusi mandiri di samping wallet.


Temukan versi terbaru: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) dan verifikasi tanda tangan PGP dari rilis tersebut dengan kunci: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Rincian penerapan berbeda tergantung pada perangkat keras (arsitektur CPU) dan pilihan OS, di bawah ini rincian yang berbeda diberikan untuk Raspberry Pi (ARM-64) dengan Debian berbasis RaspiBlitz sebagai titik awal. Lanjutkan ke depan untuk penerapan OS (X86-64) Ubuntu menggunakan Nix.


Temukan petunjuk instalasi di sini: [Dokumen Wasabi](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Penyebaran RaspiBlitz/Debian


Untuk node RaspiBlitz (diuji dengan v1.11), penyebaran script yang dibangun dari kode sumber dapat digunakan: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Penyebaran yang mudah


Untuk penerapan minimal, Anda hanya perlu mengekstrak file eksekusi untuk platform Anda dalam sebuah folder.

Contoh kode baris perintah untuk Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Ini akan menghasilkan pesan tanda tangan yang valid sebagai berikut:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Dan Anda dapat melanjutkan untuk menginstal paket yang telah diunduh:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Konfigurasi 🧾


Sebelum menjalankan koordinator, Anda perlu mengedit file Config.json dengan file:


- Kredensial Bitcoin RPC
- Parameter putaran yang disukai
- Koordinator Kunci Publik yang Diperluas (buat SegWit wallet baru untuk menerima debu yang terkumpul)

**Peringatan**: Taproot wallet akan menghasilkan UTXO yang tidak dapat digunakan! Gunakan Segwit Native wallet di sini.


- Jenis alamat masukan dan keluaran yang diizinkan
- Konfigurasi penyiar untuk penerbitan melalui nostr (nama, deskripsi, Uri, input minimum, relai nostr, kunci privat nostr)


Anda bisa menjalankan koordinator yang hanya bisa diakses melalui alamat .onion, atau menggunakan domain clearnet khusus Anda.


Temukan atau buat file konfigurasi pada jalur ini:


`~/.walletwasabi/coordinator/Config.json`


Edit dengan perintah:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Lihat contoh berikut ini Config.json:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Konfigurasi Tor 🧅


Untuk mengisi OnionServicePrivateKey, Anda mungkin perlu membuatnya terlebih dahulu.


Wasabi Wallet akan menghasilkan kunci privat untuk Anda jika Anda menjalankannya untuk pertama kali dengan ```"PublishAsOnionService": true,``` yang diatur dalam file Config.json.


Jalankan koordinator sekali dengan perintah:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Untuk melihat alamat layanan tersembunyi Onion Anda, periksa log koordinator dengan:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


dan Anda akan menemukan sesuatu seperti:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


URL panjang yang diakhiri dengan .onion adalah alamat layanan tersembunyi Anda atau CoordinatorUri.


Atau periksa lagi file konfigurasi koordinator Anda dengan:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Yang secara otomatis harus diisi sekarang.


## Menjalankan ⚡


Setelah semua parameter konfigurasi ditetapkan, Anda dapat menjalankan layanan koordinator dan mulai mengumumkan putaran pertama Anda 🕶️


Cukup jalankan koordinator dengan perintah tersebut:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Anda dapat memantau putaran saat ini dan jumlah UTXO yang terdaftar dengan memeriksa (di browser Tor untuk .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Opsional: server koordinator debugging


Anda dapat memantau masalah atau kesalahan apa pun dalam file log di ```~/.walletwasabi/backend/Logs.txt```


Masalah yang umum terjadi adalah masalah koneksi RPC, ini harus diaktifkan di ```~/.bitcoin/bitcoin.conf``` dengan:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Opsional: Menjalankan server backend


Bersama dengan koordinator, Anda juga dapat menyediakan server backend untuk pengguna yang tidak memiliki node bitcoin sendiri untuk terhubung untuk estimasi biaya dan filter blokir.


Mulai layanan ini dengan perintah:


```
wbackend
```


## Mengundang pengguna Wasabi ke koordinator Anda 🫂


Agar pengguna lain dapat menemukan layanan Anda, Anda dapat mengandalkan penyiar nostr, atau berbagi tautan ajaib dengan domain Anda (clearnet) atau layanan tersembunyi (tautan .onion) dan parameter bulat seperti ini:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Ketika pengguna menyalin tautan ajaib dan membuka Wasabi Wallet mereka, perangkat lunak akan secara otomatis menampilkan dialog koordinator dengan domain dan parameter Anda.


![detected](assets/en/02.webp)


💚🍣 Selamat atas desentralisasi privasi bitcoin 🕶️


Ingatlah pelatihan Anda [wasabika] (https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet hanya untuk pertahanan 🛡️