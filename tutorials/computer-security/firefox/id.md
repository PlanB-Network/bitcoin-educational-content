---
name: Firefox
description: Bagaimana cara mengonfigurasi Firefox untuk melindungi privasi Anda?
---

![cover](assets/cover.webp)

## Pendahuluan

Kita semua menghabiskan waktu berjam-jam secara online, sering kali tanpa menyadari apa yang diungkapkan oleh browser kita. Setiap klik, setiap pencarian, setiap situs yang kita kunjungi memberi makan industri besar dari pengumpulan data pribadi.

![Statistiques navigateurs 2024](assets/fr/01.webp)

*Pangsa pasar peramban web: Chrome mendominasi dengan 65% pasar, diikuti oleh Safari dan Edge. Sumber: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*

Seperti yang ditunjukkan grafik ini, Google Chrome mendominasi secara masif, dengan lebih dari 65% penggunaan di seluruh dunia. Hegemoni ini berarti bahwa sebagian besar pengguna Internet mempercayakan data penjelajahan mereka kepada Google, sebuah perusahaan yang model bisnisnya didasarkan pada iklan bertarget. Firefox, dengan hanya 3% pasar, mewakili alternatif yang dikembangkan oleh Mozilla, sebuah organisasi nirlaba tanpa kepentingan komersial dalam mengeksploitasi data Anda.

Namun, memilih Firefox hanyalah langkah pertama. Secara default, bahkan Firefox memerlukan penyesuaian untuk memaksimalkan perlindungan Anda. Panduan ini membawa Anda langkah demi langkah, dari yang paling sederhana hingga yang paling canggih, untuk mengubah Firefox menjadi perisai yang sesungguhnya terhadap pelacakan sambil tetap mempertahankan pengalaman penjelajahan yang menyenangkan.

### Mengapa Firefox?

- **Gratis dan open source** (Gecko engine): kode yang dapat diaudit dan transparan.
- **Organisasi nirlab**a: Mozilla Foundation, misi untuk kepentingan umum.
- **Perlindungan bawaan**: Enhanced Tracking Protection (ETP), Total Cookie Protection (TCP), State Partitioning, HTTPS-only mode, DNS over HTTPS (DoH).
- **Kustomisasi tingkat lanjut**: tidak seperti Chrome, Firefox memungkinkan Anda memodifikasi perilakunya secara mendalam.

### Prinsip-prinsip penting sebelum Anda memulai

- **Tidak ada resep universal**: semakin Anda memodifikasi, semakin Anda berisiko terlihat menonjol (fingerprinting). Tujuannya adalah untuk lebih terlindungi tanpa menonjol dari keramaian.
- **Kemajuan langkah demi langkah**: Ubah satu pengaturan, uji situs yang biasa Anda kunjungi, lalu lanjutkan. Tidak perlu mengubah semuanya sekaligus.
- **Keseimbangan pribadi**: Temukan keseimbangan Anda antara privasi dan kemudahan penggunaan.

## Instalasi cepat

![Téléchargement Firefox](assets/fr/02.webp)

**Pengunduhan resmi:** Buka [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/). Pada halaman ini, pilih sistem operasi Anda (Windows, macOS, Linux) untuk mengakses halaman pengunduhan yang sesuai dengan petunjuk pemasangan yang spesifik.

- **Windows**: unduh penginstal `.exe`, klik dua kali dan ikuti wizard penginstalan
- **macOS**: unduh file `.dmg`, buka dan drag Firefox ke dalam folder Aplikasi
- **Linux**: tersedia beberapa pilihan - paket `.deb`/`.rpm`, Flatpak (Flathub), Snap, atau melalui pengelola paket (apt, dnf, pacman). Lebih memilih sumber resmi Mozilla.

**Tip:** Setelah terinstal, periksa pembaruan melalui Bantuan → **About Firefox** (penting untuk patch keamanan).

![Configuration initiale Firefox](assets/fr/03.webp)

*Tampilan pertama saat meluncurkan Firefox: tetapkan Firefox sebagai browser default Anda, tambahkan ke pintasan, lalu klik "Save and continue"*

![Création compte Firefox](assets/fr/04.webp)

*Langkah opsional: membuat atau masuk ke akun Firefox. Anda dapat melewati langkah ini dengan mengeklik "Not now" di kanan bawah*

![Page d'accueil Firefox](assets/fr/05.webp)

*Tampilan beranda Firefox setelah konfigurasi selesai. Perhatikan menu ☰ di kanan atas, yang memberikan akses ke Pengaturan dan Ekstensi untuk menyesuaikan Firefox*

## Perlindungan yang sudah diaktifkan secara default (meyakinkan)

- **Site isolation (Fission)**: dalam penyebaran progresif. Fitur ini menjalankan setiap situs dalam proses terpisah untuk mencegah satu tab berbahaya mengakses data tab lainnya. Periksa statusnya melalui `about:support` (cari "Fission"). Jika tidak diaktifkan, Anda dapat mengaktifkannya secara manual di `about:config` dengan `fission.autostart = true`.
- **Total Cookie Protection (TCP)**: aktif secara default. Cookie dan penyimpanan lainnya dibatasi pada situs pihak pertama (satu "jar" per situs), yang menetralkan pelacakan lintas-situs. Pengecualian sementara dibuat melalui Storage Access API bila diperlukan (tombol login terintegrasi).
- **Bounce/Redirect Tracking Protection**: Firefox secara otomatis mendeteksi dan membersihkan cookie yang ditinggalkan oleh situs bounce (tautan yang mengarahkan Anda melalui pelacak sebelum tujuan), mengurangi saluran pelacakan ini tanpa tindakan apa pun dari Anda.

## Level 1 - Esensial (≤ 10 menit)

Tujuan: keuntungan privasi besar tanpa merusak web. Untuk 90% pengguna.

Untuk mengakses pengaturan, klik menu ☰ di kanan atas, lalu "**Settings**".

![Paramètres généraux](assets/fr/07.webp)

*Halaman pengaturan Firefox - tab "General". Di sinilah Anda mengonfigurasi sebagian besar opsi privasi Anda*

**Perlindungan pelacakan (ETP)**

- Alihkan **ETP ke Strict**. Anda memblokir lebih banyak pelacak (cookie lintas-situs, fingerprinting, cryptomining, widget sosial...).
- Jika sebuah situs rusak (video, tombol login...), nonaktifkan perlindungan hanya untuk situs tersebut melalui perisai 🛡️, lalu segarkan tab.

Berikut ini adalah tingkat keamanan ETP yang berbeda:

- **Standard** (seimbang, kompatibilitas maksimum)
  - Blokir: pelacak sosial, cookie lintas-situs (semua jendela), melacak konten di penjelajahan privat, cryptocurrency miners, detektor fingerprinting.
  - Termasuk Total Cookie Protection (TCP): satu jar per situs.
- **Strict** (direkomendasikan untuk kerahasiaan)
  - Juga memblokir pelacakan konten di semua jendela + fingerprinting yang diketahui dan dicurigai.
  - Mungkin merusak beberapa situs; gunakan perisai 🛡️ untuk pengecualian lokal.
- **Custom** (tingkat lanjut)
  - Penyesuaian halus: cookie, pelacakan konten, minors, fingerprinting (diketahui/dicurigai).

![Paramètres protection contre le pistage](assets/fr/06.webp)

**Cookie dan data situs**

- Aktifkan **"Delete cookies and site data on close"** untuk memulai ulang dengan bersih setiap kali Anda memulai ulang.
- Tambahkan **Exceptions** untuk 2-3 situs penting jika Anda menginginkannya (email, bank).

**Entri data otomatis, saran, dan halaman beranda**

- **Search**: nonaktifkan "**Show search suggestions**".
- **Address bar**: nonaktifkan "S**ponsored suggestions**" dan "**Contextual suggestions**".
- **Home**: nonaktifkan **Pocket** dan **sponsored content**.

![Paramètres cookies et mots de passe](assets/fr/08.webp)

**Hanya untuk HTTPS**

- Aktifkan **"HTTPS mode only in all windows"**.

![Configuration DNS over HTTPS](assets/fr/09.webp)

**Pengukuran telemetri dan iklan**

- Di "**Data collection by Firefox**", hapus semua checklist.
- Nonaktifkan "**Privacy-friendly advertising measures**" (PPA).
- **Safe Browsing**: biarkan tetap diaktifkan (direkomendasikan). Firefox memeriksa situs terhadap daftar ancaman melalui kueri hashed dan pemeriksaan lokal, melindungi dari phishing dan malware dengan dampak privasi minimal.

**Kontrol Privasi Global (opsional)**

- Aktifkan **GPC** untuk menandakan penolakan Anda untuk menjual/membagi data.

**Mesin pencari**

- Beralih ke **DuckDuckGo**, **Startpage**, **Qwant** atau **Brave Search** (Pengaturan → Pencarian).

![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)

**Navigasi pribadi**

- Window privat (Ctrl/Cmd+Shift+P) untuk sesi satu kali (hadiah, akun sekunder...). Hindari mode "always private": ekstensi mungkin tidak aktif dan pengecualian cookie kurang berguna.

**Ekstensi penting** (instal dari katalog resmi)

- **uBlock Origin**: memblokir iklan dan pelacakan saat ini, ringan.
- **Privacy Badger**: belajar memblokir apa yang mengikuti Anda; mengirimkan Do Not Track / GPC.
- **ClearURLs** (opsional): Firefox (ETP Strict) dan uBO sudah banyak membersihkan; simpan jika Anda masih melihat URL yang "kotor" (utm, fbclid).
- **Firefox Multi-Account Containers**: mengisolasi cookie/sesi dan penyimpanan per container; multi-akun paralel; lebih sedikit pelacakan lintas-situs. Ekstensi resmi: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.

![Extension Multi-Account Containers](assets/fr/12.webp)

**Kata sandi dan 2FA**

- Gunakan pengelola kata sandi khusus (Bitwarden, KeePassXC). **Hindari** menyimpan kata sandi di browser. **Aktifkan 2FA** jika memungkinkan.

## Level 2 - Diperkuat (Kompartementalisasi & Jaringan)

Tujuan: mengelompokkan aktivitas dan mengurangi kebocoran jaringan.

**DNS melalui HTTPS (DoH)**

- **Status default**: Diaktifkan secara otomatis di beberapa wilayah (Amerika Serikat, Kanada, Rusia, Ukraina). Di tempat lain, diperlukan aktivasi manual.
- **Konfigurasi**: Settings → General → Network settings → **Enable DoH** → **Cloudflare atau Quad9** → **Maximum protection**.
- **Maximum protection** = **TRR-only** (tanpa kembali ke DNS sistem). Jika jaringan perusahaan/hotel memblokir, beralih kembali ke **Standard** atau nonaktifkan DoH.
- **Redundansi**: Jika Anda sudah menggunakan VPN tepercaya dengan DNS-nya sendiri yang aman, DoH bisa jadi berlebihan.
- **Verification test**: `https://www.dnsleaktest.com/` seharusnya hanya menampilkan penyedia layanan kesehatan yang dipilih.

![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)

**Kompartementalisasi dengan wadah dan profil**

**Multi-Account Containers**: buat ruang (Personal, Work, Finance, Social Networks, Shopping, Disposable). Konfigurasi "**Always open in this container**" untuk situs berulang Anda. Ekstensi resmi: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.

Mengapa menggunakannya?
- **Isolasi** kuat dari cookie/sesi/penyimpanan berdasarkan ruang.
- **Mengurangi pelacakan lintas-situs**: dari perusahaan raksasa (Facebook, Google).
- **Multi-akun simultan** pada layanan yang sama.
- Mengurangi risiko **CSRF/XSS** antara identitas yang tersegmentasi.
  - Tip: paling tidak, wadah khusus untuk Jejaring Sosial/Google, Pekerjaan, Keuangan.
- **Facebook Container** (opsional): versi sederhana yang didedikasikan untuk FB/Instagram.
- **Profil terpisah**: melalui `about:profiles` (profil utama, profil "ultra-secure" minimal, profil tes). Total kompartementalisasi data dan ekstensi.


**Ekstensi tingkat lanjut** (disarankan untuk pengguna tertentu)

- **Cookie AutoDelete**: menghapus cookie situs segera setelah tab ditutup (berguna jika Firefox dibuka untuk waktu yang lama).
- **LocalCDN**: menyajikan library saat ini secara lokal (mengurangi panggilan ke Google/Microsoft). Kompatibilitasnya parsial.

**Mobile (Android)**

- **Firefox Android + uBlock Origin**: perlindungan serupa saat bepergian.

## Level 3 - Ahli (tentang: konfigurasi & Arkenfox)

Tujuan: penguatan tingkat lanjut dengan resiko yang dapat diterima. Direkomendasikan pada **profil terpisah**.

Pilih hanya satu dari dua pendekatan berikut:

**Pendekatan A - Modifikasi manual**: Beberapa penyesuaian yang ditargetkan melalui `about:config` (kontrol yang lebih sederhana dan lebih tepat)

**Pendekatan B - Arkenfox user.js**: Konfigurasi sepenuhnya otomatis (lebih kompleks, perlindungan maksimum)

➡️ **Arkenfox sudah menyertakan SEMUA perubahan about:config yang disebutkan di bawah** + ratusan lainnya. Jika Anda memilih Arkenfox, abaikan bagian about:config.

### Pendekatan A: Modifikasi manual melalui about:config

Ketik `about:config` pada Address bar → Terima risiko.

![Avertissement about:config](assets/fr/13.webp)

![Interface about:config](assets/fr/14.webp)

![Préférences about:config](assets/fr/15.webp)

- Resistensi terhadap sidik jari (diwarisi dari Tor Browser)

```text
privacy.resistFingerprinting = true
```

Efek: Zona waktu UTC, **letterboxing** (ukuran window standar), User-Agent/kebijakan standar, pembatasan Canvas/WebGL/AudioContext. Lebih seragam, tetapi beberapa "kekhasan" (waktu bergeser, kadang-kadang sedikit bahasa Inggris).

- Nonaktifkan WebRTC (menghindari kebocoran IP; merusak Web visio)

```text
media.peerconnection.enabled = false
```

- Referer lebih kompatibel (default)

```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```

Opsi ketat (dapat memutus pembayaran/SSO):

```text
network.http.referer.XOriginPolicy = 2
```

- Membatasi komunikasi API dan spekulasi

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

Golden rule: jika ada yang rusak, kembalilah ke perubahan terakhir.

### Pendekatan B: Arkenfox user.js (Konfigurasi yang sepenuhnya otomatis)

Proyek **Arkenfox** menyediakan file `user.js` yang dikelola oleh komunitas yang secara otomatis menerapkan ratusan preferensi Firefox yang berorientasi pada privasi dan keamanan. Saat memulai ulang, Firefox membaca file ini dari profil Anda dan menerapkan pengaturan ini.

- Apa tujuannya? Mulai dari **dasar yang diperkuat secara konsisten** tanpa "mengklik di mana-mana"; mengurangi kekeliruan; menghemat waktu.
- Apa yang diubahnya (contoh): pemotongan telemetri, cookies/cache/referrer/HTTPS diperkuat, **RFP** + letterboxing, **WebRTC dinonaktifkan**, penyesuaian DoH/TLS, API yang banyak berbicara dibatasi.
- Kapan menggunakannya: jika Anda ingin Firefox diperkuat dalam 10 menit dan menerima beberapa pengecualian (DRM/streaming, Web visio, SSO/pembayaran).
- Keuntungan: cepat, konsisten, diperbarui (selaras dengan ESR), **didokumentasikan dengan sangat baik** (wiki + komentar), **dapat disesuaikan** melalui overrides.
- Keterbatasan: kompatibilitas (beberapa aplikasi web), kenyamanan (UTC, ukuran jendela), dan sebagai pengingat: **itu bukan Tor** (tidak ada anonimitas jaringan).

Instalasi (idealnya pada **profil khusus**)

1. Simpan profil/favorit dan daftarkan situs Anda dengan pengecualian cookie.
2. Unduh `user.js` dari `https://github.com/arkenfox/user.js` (ESR/versi stabil).
3. Temukan folder profil Anda melalui `about:profiles`:
   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Perpustakaan/Dukungan Aplikasi/Firefox/Profiles/...`
4. Tutup Firefox dan pindahkan `user.js` ke akar folder profil.
5. Mulai ulang; sesuaikan melalui `about:config` atau file penggantian.

Pembaruan

- Ikuti rilis Arkenfox (ESR selaras), ganti `user.js`, mulai kembali Firefox; baca catatan rilis.

**Kustomisasi melalui Penggantian**

Arkenfox sengaja membatasi secara default. Untuk menyesuaikan pengaturan tertentu dengan kebutuhan Anda (streaming, visio, situs tertentu), Anda dapat membuat file `user-overrides.js` di folder yang sama dengan `user.js`. File ini memungkinkan Anda untuk "mengganti" preferensi Arkenfox tertentu tanpa memodifikasi file utama.

Buat `user-overrides.js` dan tambahkan penyesuaian Anda:

```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (jika Anda lebih suka menyimpannya)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Riwayat kurang dibatasi
user_pref("places.history.expiration.max_pages", 200000);

// Sinkronisasi Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (jika visio diperlukan)
user_pref("media.peerconnection.enabled", true);

// Referer lebih kompatibel
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```

Penggunaan terbaik

- Gunakan **profil "Arkenfox" yang terpisah** dan simpan profil "normal" untuk kenyamanan.
- Minimalkan ekstensi (uBlock Origin OK) untuk membatasi celah serangan dan keunikan.
- Tambahkan pengecualian situs-demi-situs (perisai 🛡️, uBO, NoScript jika digunakan) bila diperlukan.
- Uji setelah setiap perubahan: kebocoran WebRTC/DNS, Cover Your Tracks, CreepJS.
  
## Penggunaan terbaik

- **Pembaruan**: Firefox dan ekstensi terbaru.
- **Ekstensi**: Masuk akal dan tepercaya; waspadai "penebusan yang meragukan".
- **Unduhan**: hati-hati; uji file sensitif di VirusTotal.
- **Kata sandi**: **manajer khusus** (Bitwarden, KeePassXC); **2FA** diaktifkan; hindari menyimpan di browser.
- **Kebersihan**: batasi Google/Facebook pada wadah; tutup/buka secara teratur untuk "mengatur ulang" konteks.

## Batasan & Alternatif

- Browser yang diperkuat ≠ anonimitas jaringan: tanpa **VPN**, IP Anda tetap terlihat; bahkan dengan itu, korelasi tetap mungkin.
- Memodifikasi terlalu banyak dapat membuat Anda **unik**. **RFP** menstandarisasi; aplikasi pengacak (misalnya Chameleon) dapat... membedakan Anda. Uji, bandingkan, sesuaikan.
- Alternatif/pelengkap:
  - Tor Browser: anonimitas jaringan melalui Tor; lebih lambat. Lihat panduan instalasi dan konfigurasi lengkap kami: https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb
  - Mullvad Browser: "Tor tanpa Tor", untuk digabungkan dengan VPN; jejak yang distandarisasi. Cari tahu cara memasangnya di tutorial khusus kami: https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e
- Kombinasi yang direkomendasikan: Firefox (Level 2) + VPN untuk penggunaan sehari-hari; Tor/Mullvad untuk aktivitas sensitif; profil terpisah untuk kompartementalisasi.

## Kesimpulan

Dengan mengikuti panduan langkah demi langkah ini, Anda telah mengubah Firefox menjadi benteng sejati melawan pengawasan digital. Dari pengaturan Level 1 yang esensial hingga konfigurasi Arkenfox tingkat lanjut, setiap perubahan memperkuat privasi Anda tanpa mengorbankan pengalaman penjelajahan Anda.

**Privasi Anda sekarang lebih terlindungi**: pelacak iklan diblokir, cookie dikompartementalisasi, kebocoran alamat IP dinetralkan, telemetry dinonaktifkan. Firefox bukan lagi hanya sebuah browser, tetapi aplikasi perlawanan digital yang disesuaikan dengan kebutuhan Anda.

**Ingat: kerahasiaan tidak pernah diberikan. Uji perlindungan Anda secara teratur, perbarui pengaturan Anda, dan jangan ragu untuk menyesuaikan konfigurasi Anda saat kebiasaan Anda berubah. Anonimitas daring Anda bergantung pada aplikasi Anda sama seperti pada kebiasaan Anda.**

## Sumber daya

### Plan ₿ Network

- SCU 202 - Meningkatkan keamanan digital pribadi Anda: Untuk mempelajari lebih lanjut tentang konsep keamanan digital yang tercakup dalam tutorial ini

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Dokumentasi Mozilla

- [Perlindungan Pelacakan yang Ditingkatkan](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Panduan resmi untuk perlindungan pelacakan yang ditingkatkan
- [Pemisahan Negara](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Dokumentasi teknis tentang partisi state
- [Keamanan Web MDN](https://developer.mozilla.org/docs/Web/Security): Referensi lengkap tentang keamanan web

### Arkenfox

- [Wiki dan panduan instalasi](https://github.com/arkenfox/user.js/wiki): Dokumentasi proyek Arkenfox yang lengkap
- [Deposit dan rilis](https://github.com/arkenfox/user.js): Unduh file user.js dan lacak pembaruan

### Panduan & komunitas

- [PrivacyGuides - Browser Desktop](https://www.privacyguides.org/en/desktop-browsers/): Rekomendasi dan perbandingan browser
- **Reddit**: r/firefox, r/privacy untuk umpan balik dan dukungan
- **Forum PrivacyGuides**: diskusi teknis yang mendalam

### Alat uji

- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/): Fingerprint digital dan efektivitas anti-pelacakan
- [Tes Kebocoran DNS](https://www.dnsleaktest.com/): Uji kebocoran DNS dan efisiensi DoH
- [BrowserLeaks](https://browserleaks.com/): Rangkaian pengujian lengkap (WebRTC, Kanvas, Font, dll.)
- [BadSSL](https://badssl.com/): Tes validasi sertifikat SSL/TLS
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): Analisis lanjutan dari 50+ celah fingerprinting
- [Uji DNS Cloudflare](https://1.1.1.1/help): Memeriksa apakah Cloudflare DoH berfungsi dengan baik
