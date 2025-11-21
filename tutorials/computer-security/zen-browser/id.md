---
name: Zen Browser
description: Bagaimana cara menggunakan Zen Browser untuk penjelajahan yang produktif dan rahasia?
---

![cover](assets/cover.webp)

Dalam perkembangan web browser saat ini, Google Chrome mendominasi dengan lebih dari 65% pangsa pasar, tetapi hegemoni ini menimbulkan pertanyaan penting tentang privasi dan keragaman teknologi. Chrome, seperti kebanyakan browser populer, secara masif mengumpulkan data penjelajahan untuk memberi makan algoritma periklanan Google.

![Parts de marché des navigateurs](assets/fr/01.webp)

Menghadapi kenyataan ini, browser-browser baru bermunculan dengan filosofi yang berbeda: memadukan pengalaman pengguna yang modern dengan penghormatan terhadap privasi. Zen Browser, yang diluncurkan pada tahun 2024, adalah bagian dari pendekatan ini, menawarkan alternatif inovatif yang berbasis pada Firefox tetapi didesain ulang untuk pengguna masa kini.

Zen Browser menonjol karena Interface uniknya dengan vertical tabs (tab vertikal), workspaces (ruang kerja) untuk mengatur sesi Anda, dan fitur produktivitas seperti Split View. Namun, di luar inovasi ergonomis ini, di atas segalanya adalah komitmennya terhadap privasi yang membuatnya menarik: tanpa telemetri, perlindungan anti-pelacakan yang diperkuat, dan pengembangan komunitas yang transparan.

Dalam tutorial ini, kita akan menemukan bagaimana Zen Browser dapat mengubah cara Anda menjelajah dengan menggabungkan produktivitas, personalisasi, dan privasi.

## Menginstal Zen Browser

### Unduhan resmi

Zen Browser tersedia untuk Windows, macOS dan Linux. Kunjungi situs web resminya: https://zen-browser.app/download

![Site officiel Zen Browser](assets/fr/02.webp)

Situs ini secara otomatis mendeteksi sistem Anda dan mengusulkan tautan yang sesuai:

![Page de téléchargement](assets/fr/03.webp)

- **Windows**: File .exe untuk Windows 10/11 (versi x64 dan ARM64)
- **macOS**: Image disk .dmg yang kompatibel dengan Intel dan Apple Silicon (macOS Monterey dan yang lebih baru)
- **Linux:** Tersedia beberapa opsi:
  - **Flatpak** (disarankan): `flatpak instal flathub app.zen_browser.Zen`
  - **AppImage**: Portabel, dapat dieksekusi secara langsung
  - **Arsipkan tar.gz**: Untuk diekstrak secara manual
  - **AUR** (Arch Linux): Paket browser Zen

### Instalasi langkah demi langkah

**Pada Windows:**

- Unduh file .exe
- Jalankan instalasi (jika SmartScreen memperingatkan, klik "Additional information" lalu "Run anyway")
- Pilih direktori penginstalan
- Biarkan "Launch Zen Browser" dicentang untuk segera memulai

**Pada macOS:**

- Unduh file .dmg
- Memasang image disk
- Seret Zen Browser ke dalam folder Aplikasi
- Saat pertama kali diluncurkan: klik kanan > "Buka" untuk beralih ke Gatekeeper

**Di Linux:**

- **Flatpak:** Instalasi otomatis melalui manajer paket
- **AppImage:** `chmod +x ZenBrowser.AppImage` lalu klik dua kali
- **tar.gz:** Ekstrak dan jalankan eksekusi zen-browser

### Peluncuran pertama dan konfigurasi awal

Pada awal pengaktifan, Zen Browser akan memandu Anda melalui beberapa langkah konfigurasi:

![Import de données](assets/fr/04.webp)

*Impor opsional data Anda dari browser lain (favorit, riwayat, kata sandi)*

![Configuration initiale](assets/fr/05.webp)

*Pilihan mesin pencari default dan konfigurasi tab pin*

![Personnalisation visuelle](assets/fr/06.webp)

*Pilih warna workspace Anda dan validasi untuk mengakses browser*

![Page d'accueil Zen Browser](assets/fr/07.webp)

*Halaman beranda Zen Browser dengan side bar yang khas*

## Memperkenalkan Zen Browser

**Zen Browser** adalah web browser open source dan gratis yang berasal dari Mozilla Firefox, dikembangkan oleh komunitas sukarelawan yang bersemangat sejak Maret 2024. Tidak seperti browser dari perusahaan teknologi besar, Zen Browser tidak didukung oleh perusahaan komersial mana pun, dan didanai semata-mata oleh kontribusi dari komunitasnya.

**Catatan Penting**: Zen Browser saat ini berada dalam versi **Beta**. Meskipun stabil untuk penggunaan sehari-hari, Anda mungkin akan mengalami pembaruan yang sering dan adanya bug sesekali.

Filosofi proyek ini diringkas oleh slogannya: "Welcome to a calmer Internet" (Selamat datang di Internet yang lebih tenang). Pendekatan ini diterjemahkan menjadi browser yang peduli pada pengalaman pengguna Anda daripada data pribadi Anda, mencari keseimbangan sempurna antara keindahan, kecepatan, dan privasi.

### Interface yang didesain ulang untuk produktivitas

Zen Browser merevolusi pengalaman menjelajah dengan beberapa inovasi:

- **Vertical Tabs (Tab Vertikal)**: Tidak seperti browser tradisional, Zen menampilkan tab Anda di side bar vertikal daripada horizontal. Pilihan ergonomis ini, yang terinspirasi oleh Arc Browser, memaksimalkan ruang tampilan dan meningkatkan navigasi, terutama ketika Anda memiliki banyak tab terbuka.
- **Workspaces (Ruang Kerja)**: Atur tab Anda berdasarkan proyek atau tema di ruang khusus. Misalnya, ruang "Work" untuk tab profesional Anda, ruang "Watch" untuk bacaan Anda, dan seterusnya. Anda dapat beralih secara instan dari satu ruang ke ruang lain.
- **Split View (Tampilan Terpisah)**: Tampilkan beberapa situs secara berdampingan dalam satu window, ideal untuk membandingkan informasi atau bekerja pada banyak sumber secara bersamaan.
- **Glance (Sekilas)**: Pratinjau cepat tautan dalam window modal sementara tanpa membuka tab baru, sempurna untuk melihat referensi tanpa kehilangan konteks.

### Privasi secara default

Zen Browser secara native mengintegrasikan perlindungan privasi yang kuat:

- **Enhanced Anti-Tracking (Anti-Pelacakan yang Ditingkatkan)**: Pemblokiran otomatis pelacak (trackers), third-party cookies (cookie pihak ketiga), dan fingerprinting scripts.
- **Telemetry Disabled (Telemetri Dinonaktifkan)**: Tidak ada data yang dikirim ke server eksternal.
- **DNS over HTTPS**: Mengenkripsi permintaan DNS Anda untuk mencegah pemantauan.
- **Reduced Google Dependencies (Mengurangi Ketergantungan Google)**: Zen Browser menghapus sebagian besar koneksi ke layanan Google, meskipun beberapa mungkin tetap ada (penjelajahan aman, pembaruan).

### Kustomisasi tingkat lanjut dengan Zen Mods

Zen menawarkan ekosistem kustomisasi unik dengan Zen Mods: galeri tema dan modifikasi yang dibuat oleh komunitas untuk mengubah tampilan dan perilaku browser.

Zen Mods Populer yang Direkomendasikan:

- **SuperPins** ⭐: Mengubah tab yang disematkan menjadi tombol bergaya untuk tampilan Interface yang lebih profesional.
- **Cohesion**: Penataan gaya yang konsisten dan transparan yang menyatukan URL bar, sidebar, dan bookmarks.
- **Better Find Bar**: Memindahkan bar pencarian ke atas untuk ergonomi yang lebih baik.
- **Sidebar Expand on Hover**: Perluasan side bar otomatis saat diarahkan, memaksimalkan ruang layar.
- **Better Unloaded Tabs**: Mengoptimalkan manajemen memori dengan indikator visual untuk tab yang tidak aktif.
- **Cleaned URL Bar**: Memurnikan Interface address bar, menghapus elemen yang tidak perlu.
- **Transparent Zen**: Efek transparansi elegan dengan animasi yang mulus.

**instalasi Zen Mod:**

- Kunjungi [galeri resmi Zen Mods](https://zen-browser.app/mods)
- Jelajahi galeri tema yang tersedia

![Galerie Zen Mods](assets/fr/12.webp)

- Klik "Install" untuk mod yang diinginkan

![Installation SuperPins](assets/fr/13.webp)

*Contoh: Menginstal mod SuperPins yang populer*

- Tema ini berlaku secara instan
- Anda dapat menonaktifkannya atau mencoba yang lain kapan saja

Zen Mods tidak terbatas pada tema visual: beberapa memodifikasi perilaku Interface (animasi, tata letak elemen, pintasan yang disesuaikan). Pendekatan modular ini memungkinkan setiap pengguna untuk menciptakan lingkungan penelusuran yang ideal.

![Gestion des Zen Mods](assets/fr/16.webp)

*Interface untuk mengelola Zen Mods yang diinstal dalam parameter*

**⚠️ Catatan penting tentang personalisasi dan fingerprinting:**

Semakin Anda menyesuaikan Zen Browser (themes, ekstensi, mods), semakin unik dan karena itu semakin mudah dilacak **jejak digital** Anda. Ini adalah celah mendasar:

- **Personalisasi Maksimum** = Pengalaman pengguna optimal TAPI jejak yang unik dan mudah diidentifikasi.
- **Konfigurasi Default** = Jejak yang lebih umum TAPI pengalaman yang kurang personal.

Zen Browser telah memilih pengalaman pengguna di atas anonimitas sempurna. Jika prioritas Anda adalah anonimitas absolut, lebih baik pilih Tor Browser atau Mullvad Browser, yang memaksakan konfigurasi seragam pada semua pengguna.

Selain itu, karena berbasis Firefox, Zen kompatibel dengan seluruh ekosistem ekstensi Firefox.

## Keuntungan dan kerugian

### ✅ Keuntungan

- **Rancangan Privasi**: Perlindungan anti-pelacakan aktif, telemetry disabled (telemetri dinonaktifkan), tidak ada pengumpulan data.
- **Interface Inovatif**: Vertical tabs (tab vertikal), workspaces, Split View secara dramatis meningkatkan produktivitas.
- **Pembaruan Cepat**: Sinkronisasi dengan Firefox dalam waktu kurang dari 72 jam untuk patch keamanan.
- **Kustomisasi Tingkat Lanjut**: Themes komunitas, penyesuaian yang halus, kompatibilitas ekstensi Firefox.
- **Open Source dan Komunitas**: Kode yang transparan, pengembangan kolaboratif, kemandirian dari Big Tech.

### ❌ kerugian

- **Tidak Ada Versi Seluler**: Hanya tersedia di PC (Windows, macOS, Linux).
- **Inkompatibilitas DRM**: Netflix, Disney+, Spotify, dan layanan streaming lainnya saat ini tidak berfungsi.
- **Proyek Baru**: Tim kecil, dukungan komunitas, bug sesekali.
- **Learning Curve (Kurva Pembelajaran)**: Interface berbeda, membutuhkan adaptasi bagi mereka yang terbiasa dengan tab horizontal.

## Konfigurasi lanjutan untuk privasi dan keamanan

Untuk mengakses pengaturan Zen Browser:

![Accès aux paramètres](assets/fr/14.webp)

*Klik pada ikon ekstensi, lalu pada "Zen Settings" di bagian bawah*

![Interface des paramètres](assets/fr/15.webp)

*Tampilan umum parameter Zen dengan semua tab yang tersedia*

### Pengaturan default yang dioptimalkan

Sejak awal, Zen Browser menerapkan konfigurasi privasi tinggi yang mengungguli sebagian besar browser:

- **Perlindungan Anti-Pelacakan Ketat**: Level "Standard" diaktifkan secara default, memblokir:
  - Cross-site tracking cookies dan supercookies.
  - Script pelacak iklan (Google Analytics, Facebook Pixel, dll.).
  - Cryptominters yang menggunakan CPU Anda untuk menambang cryptocurrency.
  - Fingerprinting via Canvas, WebGL, AudioContext.
- **Isolasi Cookie Total**: First Party Isolation mencegah satu situs membaca cookie situs lain.
- **Telemetri Sebagian Besar Dinonaktifkan**: Sebagian besar pengumpulan data telah dihapus, meskipun beberapa koneksi ke layanan Mozilla/Google mungkin tersisa dan emerlukan konfigurasi manual tambahan.
- **DNS Aman Secara Default**: DNS-over-HTTPS diaktifkan untuk mencegah pengintaian pada permintaan Anda.
- **HTTPS-Only Diaktifkan**: Memaksa koneksi terenkripsi pada semua situs.

### Pengaturan privasi yang disarankan

**1. Pilih tingkat perlindungan anti-pelacakan:**

Settings > Privacy & Security > Enhanced Tracking Protection

![Protection anti-pistage](assets/fr/18.webp)

**Standar (standar yang disarankan):**

- Keseimbangan antara perlindungan dan kinerja, halaman dimuat secara normal
- Memblokir: pelacak sosial, cookie lintas situs, pelacakan konten di window pribadi, cryptomining, dan fingerprinters.
- Mencakup **Total Cookie Protection**: mengisolasi cookie berdasarkan situs untuk mencegah pelacakan lintas situs

**Ketat (perlindungan maksimum):**

- Perlindungan yang ditingkatkan tetapi dapat merusak situs atau konten tertentu
- Memblokir: pelacak sosial, cookie lintas situs, melacak konten di **semua** window, browser yang dikenal dan dicurigai
- Direkomendasikan untuk pengguna berpengalaman

**Disesuaikan (kontrol granular):**

- Pilih dengan tepat pelacak dan skrip mana yang akan diblokir
- Opsi terpisah: Cookie, Melacak konten, Cryptomining, Pelacak yang diketahui/dicurigai
- Ideal untuk menyesuaikan dengan kebutuhan Anda

**2. Mengubah mesin pencarian:**

Settings > Search > Default search engine:

![Configuration moteur de recherche](assets/fr/20.webp)


- **DuckDuckGo**: Tidak ada profil, tidak ada filter, hasil netral
- **Startpage**: hasil Google yang dianonimkan, berbasis di Belanda (RGPD)
- **Searx**: Mesin metasearch terdesentralisasi, tanpa log, open source
- **Brave Search**: Indeks independen, bukan dari Google
- **Avoid**: Google, Bing, Yahoo (pengumpulan data besar-besaran)

**3. Mengonfigurasi DNS aman (DNS melalui HTTPS):**

Settings > Privacy and security > DNS over HTTPS (bottom of page)

![Configuration DNS sur HTTPS](assets/fr/19.webp)

**Perlindungan Default:**

- Zen secara otomatis memutuskan kapan harus menggunakan DNS aman.
- Menggunakan DNS aman di wilayah di mana layanan tersebut tersedia.
- Kembali ke DNS default sistem jika ada masalah dengan penyedia aman.
- Dinonaktifkan secara otomatis saat menggunakan VPN, kontrol orang tua, atau kebijakan perusahaan.

**Perlindungan yang Ditingkatkan (disarankan):**

- Anda dapat mengontrol kapan menggunakan DNS aman dan memilih penyedia
- Menggunakan penyedia yang dipilih dengan fallback ke sistem DNS jika perlu
- **Penyedia default:** Cloudflare (log yang cepat dan anonim)
- **Alternatif:** Beralih ke Quad9, NextDNS tergantung ketersediaan

**Perlindungan Maksimum (pengguna tingkat lanjut):**

- Zen **selalu** menggunakan DNS yang aman saja
- Peringatan keamanan sebelum menggunakan sistem DNS
- **Peringatan:** Situs mungkin tidak dapat dimuat jika DNS aman tidak tersedia

**4. Aktifkan mode HTTPS saja:**

Settings > Privacy and security > HTTPS mode only > **Enabled**

- Paksa semua koneksi ke HTTPS
- Peringatan jika situs hanya mendukung HTTP

**5. Mengelola izin default:**

Settings > Privacy & Security > Permissions:

- **Lokasi**: Blokir (kecuali layanan kartu)
- **Kamera/Mikrofon**: Blokir (otorisasi berdasarkan kasus per kasus)
- **Pemberitahuan**: Blokir (mencegah spam)
- **Pemutaran otomatis**: Memblokir audio dan video

### Ekstensi keamanan yang disarankan

**Ekstensi penting:**

- **uBlock Origin**: Pemblokir dan pelacak iklan paling efektif
  - Daftar yang direkomendasikan: EasyList, EasyPrivacy, Peter Lowe's Iklan dan daftar server pelacakan
  - Mode lanjutan untuk pengguna berpengalaman
- **ClearURLs**: Menghapus parameter pelacakan URL (utm_source, fbclid, dll.)
- **Cookie AutoDelete**: secara otomatis menghapus cookie dan data penelusuran saat tab ditutup
- **Decentraleyes**: Menyajikan libary JS secara lokal untuk menghindari CDN Google/Cloudflare

**Ekstensi tingkat lanjut (pengguna berpengalaman):**

- **NoScript**: Kontrol JavaScript granular (dapat merusak banyak situs)
- **Privacy Badger** (EFF): Deteksi perilaku pelacak
- **Temporary Containers**: Pisahkan setiap tab dalam wadah terpisah

## Memahami ketiadaan DRM di Zen Browser

### Apa yang dimaksud dengan DRM?

**DRM (Digital Rights Management)** adalah teknologi perlindungan yang mengenkripsi konten digital untuk mencegah penyalinan. Teknologi ini memerlukan modul browser berpemilik (seperti **Google Widevine**) untuk mendekripsi dan membaca media yang dilindungi.

**Layanan yang memerlukan DRM:**

- **Streaming video:** Netflix, Disney+, HBO Max, Amazon Prime Video
- **Musik premium:** Spotify Premium, YouTube Music, Deezer
- **Pelatihan online:** Udemy, Coursera (video yang dilindungi)

### Mengapa Zen Browser tidak memiliki DRM

**Alasan utama:**


1. **Biaya dan kerumitan:** Lisensi Google Widevine tidak gratis dan memerlukan proses persetujuan yang rumit
2. **Filosofi proyek:** DRM adalah "kotak hitam" berpemilik yang tidak sesuai dengan pendekatan open source dan kemandirian dari Google
3. **Sumber daya terbatas:** Tim berfokus pada inovasi dan kerahasiaan Interface

### Dampak praktis

**❌ Layanan tidak dapat diakses:**

Netflix, Disney+, Spotify Premium, YouTube Premium, kursus pelatihan berbayar Udemy/Coursera

![Erreur DRM Prime Video](assets/fr/17.webp)

*Pesan kesalahan yang umum terjadi saat mencoba memutar konten yang dilindungi DRM*

**✅ Layanan dapat diakses:**

YouTube, Twitch, Vimeo, situs berita, jejaring sosial, podcast gratis

**Solusi pintas:**

- Gunakan Firefox/Chrome hanya untuk streaming
- Aplikasi asli (Netflix, Spotify)
- Memilih konten bebas DRM (YouTube, Twitch, Bandcamp, PeerTube)

**Status saat ini:** Tim Zen telah memulai proses untuk mendapatkan lisensi Widevine, tetapi belum ada jadwal yang diberikan. Proses ini sepenuhnya bergantung pada persetujuan Google.

## Penggunaan sehari-hari

### Interface dan navigasi

**Side bar dengan tab:**

- Judul dan gambar mini untuk setiap halaman
- tombol "+" untuk tab baru
- Reorganisasi Drag-and-drop
- Tindakan yang peka terhadap konteks: klik kanan untuk menduplikasi, menutup, memindahkan

**Area kerja:**

- Selector di bagian atas sidebar
- Penciptaan area bertema
- Peralihan cepat antar konteks
- Tab yang disematkan tersedia di semua ruang

![Création d'un nouvel espace](assets/fr/11.webp)

*Interface untuk membuat ruang kerja baru*

**Fitur-fitur canggih:**

- **Pisahkan Tampilan**: Pilih beberapa tabs > right-click > "Split x tabs"
- **Sekilas**: Alt + klik pada tautan untuk pratinjau
  
### Pintasan yang berguna

- `ctrl + T`: Tab baru
- `ctrl + Spasi`: Menu ruang kerja
- `ctrl + B`: Menampilkan/menyembunyikan bilah sisi
- `ctrl + Shift + P`: Window pribadi
- `alt + klik`: Sekilas (pratinjau)
  
### Penggunaan terbaik

- **Mengatur ruang Anda**: Membuat ruang bertema (Bekerja, Menonton, Pribadi)
- **Gunakan pin tab**: Untuk situs yang paling sering Anda kunjungi
- **Memanfaatkan Tampilan Terpisah**: Ideal untuk multitasking pada layar besar
- **Tetap up to date**: Periksa pembaruan secara teratur
- Jelajahi **Zen Mods**: sesuaikan tampilan agar sesuai dengan selera Anda

## Kesimpulan

Zen Browser merupakan angin segar dalam ekosistem web browser. Dengan menggabungkan Interface yang inovatif dan produktif dengan penghormatan yang ketat terhadap privasi, Zen Browser menawarkan alternatif yang kredibel untuk browser raksasa teknologi.

Vertical tabs dan workspaces-nya benar-benar mengubah pengalaman menjelajah bagi mereka yang sering menangani banyak proyek. Filosofi "no Google" dan pengembangannya oleh komunitas menjadikannya pilihan yang koheren bagi pengguna yang peduli terhadap kedaulatan digital mereka.

Meskipun masih memiliki beberapa keterbatasan (tidak ada versi seluler, kekurangan DRM), Zen Browser cukup matang untuk penggunaan sehari-hari, dan terus meningkat pesat berkat komunitasnya yang aktif.

Bagi bitcoiners dan pengguna teknologi yang menghargai produktivitas dan privasi, Zen Browser patut untuk dicoba. Anda mungkin akan mengadopsi cara menjelajah yang baru, lebih tenang, dan lebih efisien ini.

## Sumber daya

### Tautan resmi

- [Situs web resmi Zen Browser](https://zen-browser.app)
- [Dokumentasi lengkap](https://docs.zen-browser.app)
- [Source code GitHub](https://github.com/zen-browser/desktop)
- [Halaman unduhan](https://zen-browser.app/download)

### Komunitas dan dukungan

- [Discord Resmi](https://discord.gg/zen-browser)
- [Reddit r/zen_browser](https://reddit.com/r/zen_browser)
- [Zen Mods Gallery](https://zen-browser.app/mods)
