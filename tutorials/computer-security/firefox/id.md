---
name: Firefox
description: Bagaimana cara mengonfigurasi Firefox untuk melindungi privasi Anda?
---

![cover](assets/cover.webp)



## Pendahuluan



Kita semua menghabiskan waktu berjam-jam saat online, sering kali tanpa menyadari apa yang diungkapkan oleh peramban kita tentang diri kita. Setiap klik, setiap pencarian, setiap situs yang kita kunjungi memberi makan industri pengumpulan data pribadi yang sangat besar.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Pangsa pasar peramban web: Chrome mendominasi dengan 65% pasar, diikuti oleh Safari dan Edge. Sumber: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Seperti yang ditunjukkan oleh grafik ini, Google Chrome mendominasi secara besar-besaran, dengan lebih dari 65% penggunaan di seluruh dunia. Hegemoni ini berarti bahwa mayoritas pengguna Internet mempercayakan data penjelajahan mereka kepada Google, sebuah perusahaan yang model bisnisnya didasarkan pada iklan bertarget. Firefox, dengan hanya 3% dari pasar, merupakan alternatif yang dikembangkan oleh Mozilla, sebuah organisasi nirlaba yang tidak memiliki kepentingan komersial dalam mengeksploitasi data Anda.



Tetapi memilih Firefox hanyalah langkah pertama. Secara default, bahkan Firefox memerlukan penyesuaian untuk memaksimalkan perlindungan Anda. Panduan ini akan membawa Anda selangkah demi selangkah, dari yang paling sederhana hingga yang paling canggih, untuk mengubah Firefox menjadi perisai yang benar-benar melindungi dari pelacakan sambil mempertahankan pengalaman menjelajah yang menyenangkan.



### Mengapa Firefox?





- Gratis dan sumber terbuka** (mesin Gecko): kode yang dapat diaudit dan transparan
- Organisasi nirlaba**: Mozilla Foundation, misi kepentingan umum
- Perlindungan asli bawaan**: Perlindungan Pelacakan yang Ditingkatkan (ETP), Perlindungan Cookie Total (TCP), Pemisahan Status, mode khusus HTTPS, DNS melalui HTTPS (DoH)
- Kustomisasi tingkat lanjut**: tidak seperti Chrome, Firefox memungkinkan Anda memodifikasi perilakunya secara mendalam



### Prinsip-prinsip penting sebelum Anda memulai





- Tidak ada resep universal**: semakin banyak Anda memodifikasi, semakin besar risiko Anda terlihat menonjol (sidik jari). Tujuannya adalah untuk lebih terlindungi tanpa terlihat menonjol dari yang lain.
- Kemajuan langkah demi langkah**: Ubah pengaturan, uji situs yang biasa Anda gunakan, lalu lanjutkan. Tidak perlu mengubah semuanya sekaligus.
- Saldo pribadi**: Temukan kompromi ANDA antara privasi dan kemudahan penggunaan.



## Instalasi cepat



![Téléchargement Firefox](assets/fr/02.webp)



**Pengunduhan resmi:** Buka [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/). Pada halaman ini, pilih sistem operasi Anda (Windows, macOS, Linux) untuk mengakses halaman pengunduhan yang sesuai dengan petunjuk pemasangan yang spesifik.





- Windows**: unduh penginstal `.exe`, klik dua kali dan ikuti wizard penginstalan
- macOS**: unduh file `.dmg`, buka dan seret Firefox ke dalam folder Aplikasi
- Linux**: tersedia beberapa pilihan - paket `.deb`/`.rpm`, Flatpak (Flathub), Snap, atau melalui pengelola paket (apt, dnf, pacman). Lebih memilih sumber resmi Mozilla.



**Tip:** Setelah terinstal, periksa pembaruan melalui Bantuan → **Tentang Firefox** (penting untuk patch keamanan).



![Configuration initiale Firefox](assets/fr/03.webp)


*Layar pertama saat meluncurkan Firefox: tetapkan Firefox sebagai peramban default Anda, tambahkan ke pintasan, lalu klik "Simpan dan lanjutkan "*



![Création compte Firefox](assets/fr/04.webp)


*Langkah opsional: membuat atau masuk ke akun Firefox. Anda dapat melewati langkah ini dengan mengeklik "Tidak sekarang" di kanan bawah*



![Page d'accueil Firefox](assets/fr/05.webp)


*Layar beranda Firefox setelah konfigurasi selesai. Perhatikan menu ☰ di kanan atas, yang memberikan akses ke Pengaturan dan Ekstensi untuk menyesuaikan Firefox*



## Perlindungan yang sudah diaktifkan secara default (meyakinkan)





- Isolasi situs (Fission)**: dalam penyebaran progresif. Fitur ini menjalankan setiap situs dalam proses terpisah untuk mencegah satu tab berbahaya mengakses data yang lain. Periksa statusnya melalui `about:support` (cari "Fission"). Jika tidak diaktifkan, Anda dapat mengaktifkannya secara manual di `about:config` dengan `fission.autostart = true`.
- Perlindungan Cookie Total (TCP)**: aktif secara default. Cookie dan penyimpanan lainnya terbatas pada situs pihak pertama (satu "jar" per situs), yang menetralkan pelacakan lintas situs. Pengecualian sementara dibuat melalui API Akses Penyimpanan bila diperlukan (tombol login terintegrasi).
- Perlindungan Pelacakan Lambungan/Pengalihan**: Firefox secara otomatis mendeteksi dan membersihkan cookie yang ditinggalkan oleh situs bounce (tautan yang mengarahkan Anda melalui pelacak sebelum sampai ke tempat tujuan), sehingga mengurangi jalur pelacakan ini tanpa tindakan apa pun dari Anda.



## Level 1 - Esensial (≤ 10 menit)



Tujuan: keuntungan privasi yang besar tanpa merusak web. Untuk 90% pengguna.



Untuk mengakses pengaturan, klik pada menu ☰ di kanan atas, kemudian **"Pengaturan "**:



![Paramètres généraux](assets/fr/07.webp)


*Halaman pengaturan Firefox - tab "Umum". Di sinilah Anda mengonfigurasi sebagian besar opsi privasi Anda*



**Perlindungan pelacakan (ETP)**




- Alihkan **ETP** ke **Batasi**. Anda memblokir lebih banyak pelacak (kuki lintas situs, sidik jari, cryptomining, widget sosial...).
- Jika sebuah situs rusak (video, tombol masuk...), nonaktifkan perlindungan hanya untuk situs tersebut melalui perisai 🛡️, lalu refresh tab.



Berikut ini adalah tingkat keamanan ETP yang berbeda:




- Standar** (seimbang, kompatibilitas maksimum)
  - Blokir: pelacak sosial, cookie lintas situs (semua jendela), melacak konten dalam penjelajahan pribadi, penambang mata uang kripto, detektor sidik jari.
  - Termasuk **Perlindungan Cookie Total** (TCP): satu toples per situs.
- Ketat** (disarankan untuk kerahasiaan)
  - Juga memblokir konten pelacakan di semua jendela + sidik jari yang diketahui dan dicurigai.
  - Dapat merusak beberapa situs; gunakan perisai 🛡️ untuk pengecualian lokal.
- Kustom** (lanjutan)
  - Penyempurnaan: cookie, pelacakan konten, anak di bawah umur, sidik jari (diketahui/diduga).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Cookie dan data situs




- Aktifkan **"Hapus cookie dan data situs saat menutup "** untuk memulai ulang dengan bersih setiap kali Anda memulai ulang.
- Tambahkan **Pengecualian** untuk 2-3 situs penting jika Anda menginginkannya (email, bank).


**Entri data otomatis, saran, dan halaman beranda**




- Nonaktifkan **pengisian otomatis** (ID, alamat, kartu). Gunakan pengelola kata sandi sebagai gantinya.
- Pencarian**: nonaktifkan **"Tampilkan saran pencarian "**.
- Bar Address**: potong **"Saran bersponsor "** dan **"Saran kontekstual "**.
- Beranda**: nonaktifkan **Saku** dan **konten bersponsor**.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**Hanya untuk HTTPS**




- Aktifkan **"Mode HTTPS hanya di semua jendela "**.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Pengukuran telemetri dan iklan




- Pada "Pengumpulan data oleh Firefox", **hapus centang semua**.
- Nonaktifkan **"Langkah-langkah periklanan yang ramah privasi "** (PPA).
- Penjelajahan Aman**: tetap aktifkan (disarankan). Firefox memeriksa situs-situs dari daftar ancaman melalui kueri hash dan pemeriksaan lokal, melindungi dari phishing dan malware dengan dampak privasi yang minimal.



**Kontrol Privasi Global (opsional)**




- Aktifkan **GPC** untuk menandakan penolakan Anda untuk menjual/membagi data.



** Mesin pencari




- Beralih ke **DuckDuckGo**, **Startpage**, **Qwant** atau **Brave Search** (Pengaturan → Pencarian).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Navigasi pribadi**




- Jendela privat (Ctrl/Cmd+Shift+P) untuk sesi satu kali (hadiah, akun sekunder...). Hindari mode "selalu pribadi": ekstensi mungkin tidak aktif dan pengecualian cookie kurang berguna.



**Ekstensi penting** (instal dari katalog resmi)




- uBlock Origin**: memblokir iklan dan pelacakan saat ini, ringan.
- Privacy Badger**: belajar memblokir apa yang mengikuti Anda; mengirimkan Do Not Track / GPC.
- Hapus URL** (opsional): Firefox (ETP Strict) dan uBO sudah banyak membersihkan; pertahankan jika anda masih melihat URL "kotor" (utm, fbclid).
- Wadah Multi-Akun Firefox**: **Mengisolasi cookie/sesi dan penyimpanan per kontainer; multi-akun paralel; pelacakan lintas situs yang lebih sedikit**. Ekstensi resmi: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**Kata sandi dan 2FA**




- Gunakan pengelola kata sandi khusus** (Bitwarden, KeePassXC). **Hindari** menyimpan kata sandi di peramban. **Aktifkan 2FA** jika memungkinkan.



## Level 2 - Diperkuat (Kompartementalisasi & Jaringan)



Tujuan: mengkotak-kotakkan aktivitas dan mengurangi kebocoran jaringan.



**DNS melalui HTTPS (DoH)**




- Status default**: Diaktifkan secara otomatis di beberapa wilayah (Amerika Serikat, Kanada, Rusia, Ukraina). Di tempat lain, diperlukan aktivasi manual.
- Konfigurasi**: Pengaturan → Umum → Pengaturan jaringan → **Aktifkan DoH** → **Cloudflare** atau **Quad9** → **Perlindungan maksimum**.
- Perlindungan maksimum = Hanya TRR** (tidak ada fallback ke DNS sistem). Jika jaringan perusahaan/hotel memblokir, alihkan kembali ke **Standar** atau nonaktifkan DoH.
- Redundansi**: Jika Anda sudah menggunakan VPN tepercaya dengan DNS-nya sendiri yang aman, DoH bisa jadi berlebihan.
- Uji verifikasi**: `https://www.dnsleaktest.com/` seharusnya hanya menampilkan penyedia layanan kesehatan yang dipilih.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Kompartementalisasi dengan wadah dan profil




- Wadah Multi-Akun**: buat ruang (Pribadi, Pekerjaan, Keuangan, Jejaring Sosial, Belanja, Sekali Pakai). Konfigurasikan **"Selalu buka di wadah ini "** untuk situs berulang Anda. Ekstensi resmi: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Mengapa menggunakannya?
  - Isolasi** yang kuat dari cookie/sesi/penyimpanan berdasarkan ruang.
  - Mengurangi pelacakan lintas situs**: membatasi raksasa (Facebook, Google).
  - Multi-rekening secara bersamaan** pada layanan yang sama.
  - Lebih sedikit risiko CSRF/XSS** di antara identitas yang tersegmentasi.
  - Tip: paling tidak, wadah khusus untuk Jejaring Sosial/Google, Pekerjaan, Keuangan.
- Facebook Container** (opsional): versi sederhana yang didedikasikan untuk FB/Instagram.
- Profil terpisah**: melalui `about:profiles` (profil utama, profil minimal "sangat aman", profil uji). Kompartementalisasi data total dan ekstensi.



**Ekstensi tingkat lanjut** (untuk dipesan)




- Cookie AutoDelete**: menghapus cookie situs segera setelah tab ditutup (berguna jika Firefox dibuka untuk waktu yang lama).
- LocalCDN**: menyajikan pustaka saat ini secara lokal (mengurangi panggilan ke Google/Microsoft). Kompatibilitas sebagian.



**Mobile (Android)**




- Firefox Android + uBlock Origin**: perlindungan serupa saat bepergian.



## Level 3 - Ahli (tentang: konfigurasi & Arkenfox)



Tujuan: pengerasan tingkat lanjut dengan kompromi yang dapat diterima. Direkomendasikan pada **profil terpisah**.



Pilih hanya satu dari dua pendekatan berikut:



**Pendekatan A - Modifikasi manual**: Beberapa penyesuaian yang ditargetkan melalui `about:config` (kontrol yang lebih sederhana dan lebih tepat)


**Pendekatan B - Arkenfox user.js**: Konfigurasi otomatis penuh (lebih kompleks, perlindungan maksimum)



➡️ **Arkenfox sudah menyertakan SEMUA perubahan about:config yang disebutkan di bawah** + ratusan lainnya. Jika Anda memilih Arkenfox, abaikan bagian about:config.



### Pendekatan A: Modifikasi manual melalui about:config



Ketik `about:config` pada bilah Address → Terima risiko.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Resistensi terhadap sidik jari (diwarisi dari Tor Browser)


```text
privacy.resistFingerprinting = true
```


Efek: Zona waktu UTC, **kotak huruf** (ukuran jendela standar), kebijakan/agensi Pengguna yang terstandardisasi, pembatasan Canvas/WebGL/AudioContext. Lebih banyak keseragaman, tetapi ada beberapa "keanehan" (waktu offset, terkadang sedikit bahasa Inggris).





- Nonaktifkan WebRTC (menghindari kebocoran IP; mematahkan visio Web)


```text
media.peerconnection.enabled = false
```





- Kompatibel dengan Pengarah Plus (standar)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Opsi ketat (dapat memutus pembayaran/SSO):


```text
network.http.referer.XOriginPolicy = 2
```





- Membatasi API obrolan dan spekulasi


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



Aturan emas: jika ada yang rusak, kembalilah ke perubahan terakhir.



### Pendekatan B: Arkenfox user.js (Konfigurasi yang sepenuhnya otomatis)



Proyek **Arkenfox** menyediakan berkas `user.js` yang dikelola oleh komunitas yang secara otomatis menerapkan ratusan preferensi Firefox yang berorientasi pada privasi dan keamanan. Pada saat dimulai ulang, Firefox membaca berkas ini dari profil anda dan menerapkan pengaturan ini.





- Apa gunanya? Mulailah dari **dasar yang konsisten** tanpa "mengklik di mana-mana"; mengurangi kekeliruan; menghemat waktu.
- Apa yang diubah (contoh): pemotongan telemetri, cookie/cache/referrer/HTTPS diperkuat, **RFP** + kotak surat, **WebRTC dinonaktifkan**, penyesuaian DoH/TLS, API yang cerewet dibatasi.
- Kapan menggunakannya: jika Anda ingin Firefox dikeraskan dalam 10 menit dan menerima beberapa pengecualian (DRM/streaming, Web visio, SSO/pembayaran).
- Keunggulan: cepat, konsisten, **diperbaharui** (selaras dengan ESR), **didokumentasikan dengan sangat baik** (wiki + komentar), **dapat disesuaikan** melalui penggantian.
- Keterbatasan: kompatibilitas (beberapa aplikasi web), kenyamanan (UTC, ukuran jendela), dan pengingat: **ini bukan Tor** (tidak ada anonimitas jaringan).



Instalasi (idealnya pada **profil khusus**)


1. Simpan profil/favorit dan daftarkan situs Anda dengan pengecualian cookie.


2. Unduh `user.js` dari `https://github.com/arkenfox/user.js` (ESR/versi stabil).


3. Temukan folder profil Anda melalui `about:profiles`:




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Perpustakaan/Dukungan Aplikasi/Firefox/Profiles/...`


4. Tutup Firefox dan pindahkan `user.js` ke akar folder profil.


5. Luncurkan ulang; sesuaikan melalui `about:config` atau file penggantian.



Pembaruan




- Ikuti rilis Arkenfox (ESR selaras), ganti `user.js`, luncurkan kembali Firefox; baca catatan rilis.



**Kustomisasi melalui Penggantian**



Arkenfox sengaja membatasi secara default. Untuk menyesuaikan pengaturan tertentu dengan kebutuhan Anda (streaming, visio, situs tertentu), Anda dapat membuat file `user-overrides.js` di folder yang sama dengan `user.js`. File ini memungkinkan Anda untuk "mengganti" preferensi Arkenfox tertentu tanpa mengubah file utama.



Buat `user-overrides.js` dan tambahkan penyesuaian Anda:


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



Praktik terbaik




- Gunakan **profil "Arkenfox" yang terpisah** dan simpan profil "normal" untuk kenyamanan.
- Meminimalkan ekstensi (uBlock Origin OK) untuk membatasi permukaan serangan dan keunikan.
- Tambahkan pengecualian situs per situs (perisai 🛡️, uBO, NoScript jika digunakan) jika diperlukan.
- Uji setelah setiap perubahan: Kebocoran WebRTC/DNS, Cover Your Tracks, CreepJS.



## Praktik terbaik





- Pembaruan**: Firefox dan ekstensi terbaru.
- Ekstensi**: masuk akal dan dapat diandalkan; waspadai penebusan yang "meragukan".
- Unduhan**: hati-hati; uji file sensitif di VirusTotal.
- Kata sandi**: **manajer khusus** (Bitwarden, KeePassXC); **2FA** diaktifkan; hindari menyimpan di peramban.
- Kebersihan**: batasi Google/Facebook pada wadah; tutup/buka secara teratur untuk "mengatur ulang" konteks.



## Batasan & Alternatif





- Peramban yang dikeraskan ≠ anonimitas jaringan: tanpa **VPN**, IP Anda tetap terlihat; bahkan dengan itu pun, korelasi tetap dimungkinkan.
- Terlalu banyak memodifikasi dapat membuat Anda menjadi **unik**. **RFP** menjadi standar; alat pengacakan (mis. Chameleon) dapat... membuat Anda berbeda. Uji, bandingkan, sesuaikan.
- Alternatif/pelengkap:
 - Tor Browser: anonimitas jaringan melalui Tor; lebih lambat. Lihat panduan instalasi dan konfigurasi lengkap kami**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Peramban Mullvad: "Tor tanpa Tor", untuk digabungkan dengan VPN; jejak standar. Cari tahu cara menginstalnya di tutorial khusus kami**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Kombinasi yang disarankan: Firefox (Level 2) + VPN untuk penggunaan sehari-hari; Tor/Mullvad untuk aktivitas sensitif; profil terpisah untuk kompartementalisasi.



## Kesimpulan



Dengan mengikuti panduan langkah demi langkah ini, Anda telah mengubah Firefox menjadi benteng pertahanan yang sesungguhnya terhadap pengawasan digital. Dari pengaturan Level 1 yang penting hingga konfigurasi Arkenfox tingkat lanjut, setiap perubahan akan memperkuat privasi Anda tanpa mengorbankan pengalaman menjelajah Anda.



**Privasi Anda kini terlindungi dengan lebih baik**: pelacak iklan diblokir, cookie dikotak-kotakkan, kebocoran IP Address dinetralisir, telemetri dinonaktifkan. Firefox bukan lagi sekadar peramban, tetapi sebuah alat perlawanan digital yang disesuaikan dengan kebutuhan Anda.



**Ingat: kerahasiaan tidak pernah diberikan. Uji proteksi Anda secara teratur, perbarui pengaturan Anda, dan jangan ragu untuk menyesuaikan konfigurasi Anda seiring dengan perubahan kebiasaan Anda. Anonimitas online Anda sangat bergantung pada peralatan Anda dan juga pada praktik Anda.



## Sumber daya



### Plan ₿ Network




- SCU 202 - Meningkatkan keamanan digital pribadi Anda: Untuk mempelajari lebih lanjut tentang konsep keamanan digital yang tercakup dalam tutorial ini**



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Dokumentasi Mozilla




- [Perlindungan Pelacakan yang Ditingkatkan](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Panduan resmi untuk perlindungan pelacakan yang ditingkatkan
- [Pemisahan Negara](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Dokumentasi teknis tentang partisi state
- [Keamanan Web MDN](https://developer.mozilla.org/docs/Web/Security): Referensi lengkap tentang keamanan web



### Arkenfox




- [Wiki dan panduan instalasi](https://github.com/arkenfox/user.js/wiki): Dokumentasi proyek Arkenfox yang lengkap
- [Deposit dan rilis] (https://github.com/arkenfox/user.js): Unduh file user.js dan lacak pembaruan



### Panduan & komunitas




- [PrivacyGuides - Peramban Desktop](https://www.privacyguides.org/en/desktop-browsers/): Rekomendasi dan perbandingan peramban
- Reddit**: r/firefox, r/privacy untuk umpan balik dan dukungan
- Forum PrivacyGuides**: diskusi teknis yang mendalam



### Alat uji




- [Cover Your Tracks (EFF)] (https://coveryourtracks.eff.org/): Sidik jari digital dan efektivitas anti-pelacakan
- [Tes Kebocoran DNS](https://www.dnsleaktest.com/): Uji kebocoran DNS dan efisiensi DoH
- [BrowserLeaks](https://browserleaks.com/): Rangkaian pengujian lengkap (WebRTC, Kanvas, Font, dll.)
- [BadSSL] (https://badssl.com/): Tes validasi sertifikat SSL/TLS
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): Analisis lanjutan dari 50+ vektor sidik jari
- [Uji DNS Cloudflare](https://1.1.1.1/help): Memeriksa apakah Cloudflare DoH berfungsi dengan baik
