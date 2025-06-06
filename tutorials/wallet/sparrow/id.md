---
name: Sparrow Wallet
description: Menginstal, mengonfigurasi, dan menggunakan Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet adalah perangkat lunak manajemen portofolio Bitcoin yang dikembangkan oleh Craig Raw. Perangkat lunak sumber terbuka ini dihargai oleh para bitcoiners karena banyak fitur dan Interface yang intuitif.

Ada dua cara untuk menggunakan Sparrow:


- Seperti Hot Wallet, di mana kunci pribadi Anda disimpan di PC Anda.
- Sebagai manajer Cold Wallet, dimana kunci pribadi disimpan pada Hardware Wallet. Dalam mode ini, Sparrow hanya memanipulasi informasi Wallet publik, melacak dana, menghasilkan alamat, dan membuat transaksi, tetapi tanda tangan Hardware Wallet diperlukan untuk membuat transaksi ini valid. Oleh karena itu, Sparrow dapat menggantikan aplikasi seperti Ledger Live atau Trezor Suite.

Sparrow mendukung dompet dengan tanda tangan tunggal dan multi tanda tangan, dan memungkinkan manajemen yang lancar untuk beberapa dompet. Sebagai contoh, Anda dapat secara bersamaan mengontrol satu Wallet yang terhubung ke Ledger, satu lagi ke Trezor, dan juga memiliki Hot Wallet.

Perangkat lunak ini juga menawarkan fitur kontrol koin yang canggih, memungkinkan Anda untuk memilih dengan tepat UTXO mana yang akan digunakan dalam transaksi Anda untuk mengoptimalkan kerahasiaan Anda.

Dalam hal koneksi, Sparrow memungkinkan Anda terhubung ke node Bitcoin Anda sendiri, baik dari jarak jauh melalui Server Electrum, atau dengan Bitcoin Core. Anda juga dapat menggunakan node publik jika Anda belum memiliki node sendiri. Sambungan jarak jauh dibuat melalui Tor.

## Pasang Sparrow Wallet

Buka [halaman unduhan resmi Sparrow Wallet] (https://sparrowwallet.com/download/) dan pilih versi perangkat lunak yang sesuai dengan sistem operasi Anda.

![Image](assets/fr/01.webp)

Penting untuk memeriksa integritas dan keaslian perangkat lunak sebelum menginstalnya. Jika Anda tidak tahu cara melakukannya, Anda bisa menemukan tutorial lengkapnya di sini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Setelah Sparrow terinstal, Anda bisa melewatkan layar penjelasan awal dan langsung menuju ke layar manajemen koneksi.

![Image](assets/fr/02.webp)

## Menghubungkan ke jaringan Bitcoin

Untuk berinteraksi dengan jaringan Bitcoin dan menyiarkan transaksi Anda, Sparrow harus terhubung ke node Bitcoin. Ada tiga cara utama untuk membuat koneksi ini:


- 🟡 Menggunakan simpul publik, yaitu menyambung ke simpul pihak ketiga yang mengizinkan koneksi tersebut. Jika Anda tidak memiliki node Bitcoin Anda sendiri, opsi ini memungkinkan Anda untuk memulai Sparrow dengan cepat. Akan tetapi, node yang Anda sambungkan akan melihat semua transaksi Anda, yang dapat membahayakan kerahasiaan Anda. Memiliki kontrol atas kunci Anda sangat penting, tetapi memiliki node Anda sendiri bahkan lebih baik. Jadi, gunakan opsi ini hanya jika Anda baru memulai, dengan tetap menyadari risiko privasi Anda.
- 🟢 Menghubungkan ke node Bitcoin Core. Jika Anda memiliki node Bitcoin Core Anda sendiri, Anda dapat menyambungkannya ke Sparrow Wallet, baik secara lokal jika Bitcoin Core diinstal pada mesin yang sama, atau dari jarak jauh.
- 🔵 Koneksi melalui server Electrum. Jika node Bitcoin Anda dilengkapi dengan Electrs, seperti halnya dengan solusi node-in-a-box seperti Umbrel atau Start9, Anda dapat menyambungkannya dari jarak jauh dari Sparrow.

**Lebih baik menggunakan koneksi melalui Electrs atau Bitcoin Core pada node Anda sendiri untuk mengurangi kebutuhan untuk mempercayai pihak ketiga dan mengoptimalkan kerahasiaan Anda**

### Terhubung ke simpul publik 🟡

Menghubungkan ke node publik sangat sederhana. Klik pada tab "*Public Server*".

![Image](assets/fr/03.webp)

Pilih simpul dari daftar tarik-turun.

![Image](assets/fr/04.webp)

Kemudian klik "*Test Connection*".

![Image](assets/fr/05.webp)

Setelah terhubung, Sparrow Wallet akan menampilkan tanda centang kuning di sudut kanan bawah Interface untuk mengindikasikan bahwa Anda terhubung ke simpul publik.

![Image](assets/fr/06.webp)

### Menghubungkan ke Bitcoin Core 🟢

Metode kedua untuk menyambung ke node Bitcoin adalah dengan menghubungkan Sparrow ke Bitcoin Core. Jika Bitcoin Core diinstal pada mesin yang sama, autentikasi akan dilakukan melalui file cookie. Jika Bitcoin Core berada di mesin jarak jauh, Anda harus menggunakan kata sandi yang ditetapkan dalam file `Bitcoin.conf`.

Harap diperhatikan bahwa jika Anda menggunakan Bitcoin Core node yang dipangkas, Anda tidak akan dapat memulihkan Wallet yang berisi transaksi sebelum blok yang disimpan secara lokal. Akan tetapi, untuk Wallet baru yang dibuat di Sparrow, hal ini tidak akan menjadi masalah: transaksi baru Anda akan terlihat, bahkan dengan node yang dipangkas.

Untuk mengonfigurasi node Bitcoin Core, Anda dapat membaca salah satu tutorial berikut, tergantung pada sistem operasi Anda:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed
Pada Sparrow, buka tab "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Dengan Bitcoin Core lokal:**

Jika Bitcoin Core terinstal di komputer Anda, cari file `Bitcoin.conf` di antara file perangkat lunak. Jika file ini tidak ada, Anda dapat membuatnya. Buka file tersebut dengan editor teks dan masukkan baris berikut:

```ini
server=1
````
Sauvegardez ensuite vos modifications.
Vous pouvez également effectuer cette configuration via l'interface graphique de Bitcoin-QT en naviguant dans "*Settings*" > "*Options...*" et en activant l'option "*Enable RPC server*".
N'oubliez pas de redémarrer le logiciel après ces modifications.
![Image](assets/fr/08.webp)
Revenez ensuite à Sparrow Wallet et renseignez le chemin vers votre fichier de cookie, généralement situé dans le même dossier que le `bitcoin.conf`, selon votre système d'exploitation :
| **macOS**   | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin                     |
| **Linux**   | ~/.bitcoin                            |
![Image](assets/fr/09.webp)
Laissez les autres paramètres par défaut, l'URL `127.0.0.1` et le port `8332`, puis cliquez sur "*Test Connection*".
![Image](assets/fr/10.webp)
La connexion est établie. Une coche verte apparaîtra en bas à droite pour indiquer que vous êtes connecté à un nœud Bitcoin Core.
![Image](assets/fr/11.webp)
**Avec Bitcoin Core à distance :**
Si Bitcoin Core est installé sur une autre machine connectée sur le même réseau, commencez par localiser le fichier `bitcoin.conf` parmi les fichiers du logiciel. Si ce fichier n'existe pas encore, vous pouvez le créer. Ouvrez ce fichier avec un éditeur de texte et ajoutez la ligne suivante :
```

server=1

```
Après avoir modifié le fichier, assurez-vous de l'enregistrer dans le dossier approprié selon votre système d'exploitation :
| **macOS**   | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin                     |
| **Linux**   | ~/.bitcoin                            |
Il est également possible de réaliser cette manipulation via l'interface graphique de Bitcoin-QT. Accédez au menu "*Settings*", puis "*Options...*", et activez l'option "*Enable RPC server*" en cochant la case correspondante. Si le fichier `bitcoin.conf` n'existe pas, vous pouvez le créer directement depuis cette interface en cliquant sur "*Open Configuration File*".
![Image](assets/fr/12.webp)
Trouvez l'adresse IP de la machine qui héberge Bitcoin Core dans votre réseau local. Pour cela, vous pouvez utiliser un outil tel que [Angry IP Scanner](https://angryip.org/). Supposons, pour l'exemple, que l'adresse IP de votre nœud soit `192.168.1.18`.
Dans le fichier `bitcoin.conf`, ajoutez les lignes suivantes, en configurant `rpcbind=192.168.1.18` pour correspondre à l'adresse IP de votre nœud.
```

[tangan]

rpcbind = 127.0.0.1

rpcbind = 192.168.1.18

rpcallowip = 127.0.0.1

rpcallowip=192.168.1.0/24

```
![Image](assets/fr/13.webp)
Ajoutez également dans le fichier `bitcoin.conf` un identifiant et un mot de passe pour les connexions à distance. Assurez-vous de remplacer `loic` par votre nom d'utilisateur et `my_password` par un mot de passe fort :
```

rpcuser = loic

rpcpassword = kata sandi saya

```