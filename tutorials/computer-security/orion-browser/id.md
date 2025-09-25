---
name: Orion Browser
description: Bagaimana cara menggunakan Orion Browser untuk melindungi privasi Anda di Mac dan iPhone?
---

![cover](assets/cover.webp)

## Pendahuluan

Dalam konteks di mana mayoritas browser secara masif mengumpulkan data pribadi kita, pilihan browser yang ramah privasi menjadi sangat penting. Chrome mendominasi dengan 65% pasar global, tetapi model bisnisnya didasarkan pada eksploitasi data penjelajahan Anda. Safari, meskipun terintegrasi dalam ekosistem Apple, kurang memiliki fitur perlindungan canggih dan tidak secara fleksibel mendukung ekstensi pihak ketiga.

![Répartition du marché des navigateurs](assets/fr/01.webp)

*Perincian pasar browser web: Chrome mendominasi dengan pangsa pasar lebih dari 65%, diikuti oleh Safari, Edge, dan Firefox*

**Orion Browser** memposisikan dirinya sebagai alternatif inovatif untuk pengguna Apple. Dikembangkan oleh Kagi, browser ini menggabungkan kecepatan Engine WebKit dengan filosofi zero telemetry. Tidak seperti para pesaingnya, Orion tidak mengirimkan data ke server jarak jauh dan secara native memblokir 99,9% iklan dan pelacak, termasuk YouTube.

Fitur uniknya? Orion adalah **satu-satunya** browser WebKit yang secara native dapat memasang **ekstensi Chrome dan Firefox**, menawarkan yang terbaik dari kedua dunia. Kompatibilitas ini, dikombinasikan dengan konsumsi memori 2 hingga 3 kali lebih rendah daripada browser lain dan integrasi mulus dengan ekosistem Apple (iCloud, Keychain), menjadikannya pilihan ideal untuk pengguna Mac dan iPhone yang sadar privasi.

## Mengapa memilih Orion Browser?

### Manfaat utama

- **Perlindungan Maksimum Langsung**: Orion memblokir 99,9% iklan (termasuk YouTube) dan semua pelacak pihak pertama dan pihak ketiga secara default. Teknologinya menggabungkan Intelligent Tracking Prevention WebKit dengan daftar EasyPrivacy untuk efisiensi maksimum. Fitur unik: Orion memblokir script fingerprinting **sebelum dieksekusi**, membuat pelacakan benar-benar mustahil endekatan yang lebih radikal daripada browser lain yang hanya mencoba "menutupi" data.
- **Zero Telemetry yang Dapat Diverifikasi**: Orion mengambil pendekatan radikal terhadap privasi, dengan zero telemetry berdasarkan desain. Tidak seperti browser lain, yang membuat ratusan permintaan jaringan saat startup (IP exponent, browser fingerprint, informasi pribadi), Orion tidak pernah "phone home". Perbedaan mendasar ini sepenuhnya menghilangkan risiko kebocoran data yang tidak disengaja.
- **Performa Luar Biasa**: Berbasis pada versi WebKit yang dioptimalkan, Orion setara atau bahkan melampaui Safari dalam kecepatan di Mac. Tes Speedometer 2.0/2.1 secara konsisten menempatkannya di posisi pertama pada prosesor Apple Silicon. Pemblokiran iklan native semakin mempercepat pemuatan halaman sebesar 20 hingga 40%.
- **Dukungan Ekstensi Universal**: Sebuah inovasi besar, Orion memungkinkan Anda memasang ekstensi dari **Chrome Web Store dan Mozilla Add-ons**. Dukungan WebExtensions saat ini masih eksperimental, dengan target 100% kompatibilitas pada rilis beta. Anda dapat menggunakan banyak ekstensi populer seperti uBlock Origin, Bitwarden, bahkan di iPhone yang pertama di dunia pada iOS, meskipun beberapa mungkin tidak berfungsi dengan sempurna.

### Kekurangan yang harus diperhatikan

- **Ketersediaan Terbatas**: Saat ini hanya tersedia untuk macOS dan iOS/iPadOS. Versi Linux sedang mencapai tahap pengembangan (Milestone 2 pada tahun 2025), tetapi tidak ada build publik yang tersedia. Windows dan Android tidak dalam pengembangan karena kekurangan sumber daya.
- **Source code Tertutup**: Meskipun beberapa komponen adalah open source, Orion sebagian besar tetap berlisensi, sebuah poin perdebatan dalam komunitas privasi.
- **Ekstensi Eksperimental**: Dukungan ekstensi masih dalam beta, dengan seringnya terjadi ketidaksesuaian. Ekstensi dapat memengaruhi performa, dan beberapa tidak berfungsi sama sekali.
- **Keamanan WebKit**: Tidak seperti Chromium, WebKit tidak menawarkan isolasi proses per-situs yang begitu kuat, yang dapat menimbulkan risiko keamanan dalam skenario tertentu.
- **Tes Pemblokiran**: Orion sengaja berkinerja buruk dalam tes iklan online (26-35%), karena Kagi menganggap tes ini "secara mendasar cacat". Efektivitas aktual dalam penggunaan sehari-hari jauh lebih unggul.

## Instalasi Browser Orion

### Di macOS

![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)

*Halaman awal Kagi menampilkan Orion Browser sebagai "Browser bebas iklan dengan perlindungan privasi total dan dukungan ekstensi universal"*

- Kunjungi [kagi.com/orion](https://kagi.com/orion/)
- Klik "**Download Orion for macOS**"

![Page de téléchargement d'Orion Browser](assets/fr/03.webp)

*Halaman unduhan Orion Browser yang menunjukkan ketersediaan untuk macOS dan iOS, dengan tautan ke App Store*

- Buka file `.dmg` yang telah diunduh
- Drag aplikasi Orion ke dalam folder Aplikasi
- Saat pertama kali dijalankan, macOS akan meminta Anda untuk mengonfirmasi pembukaan

**Alternatif Homebrew**:

```bash
brew install --cask orion
```

### Pada iPhone/iPad

- Buka **App Store**
- Cari "**Browser Orion by Kagi**"
- Instal aplikasi gratis (kompatibel dengan iOS 15+)

### Konfigurasi awal

Saat pertama kali diluncurkan, Orion akan memandu Anda melalui beberapa langkah:

**1. Layar selamat datang**

![Écran de bienvenue d'Orion](assets/fr/04.webp)

*Layar selamat datang Orion Browser menyoroti fitur-fitur utama: penjelajahan yang lebih cepat, tanpa telemetri, pemblokiran iklan, dan dukungan ekstensi*

**2. Kustomisasi Interface**

![Options de personnalisation](assets/fr/05.webp)

*Layar kustomisasi memungkinkan Anda mengonfigurasi tampilan tab dan Interface agar sesuai dengan preferensi Anda*

- **Impor data**: Mentransfer favorit dan kata sandi dengan mudah dari Safari, Chrome, atau Firefox
- **Sinkronisasi iCloud**: Aktifkan untuk menemukan favorit dan tab di semua perangkat Apple Anda

**3. Pemasangan pada perangkat seluler**

![Installation sur iOS](assets/fr/06.webp)

*Layar instalasi pada iOS yang menunjukkan kode QR untuk mengunduh Orion Browser dengan cepat dari App Store*

**4. Interface sambutan untuk aplikasi penting**

![Page d'accueil Orion](assets/fr/07.webp)

*Halaman beranda Orion Browser Interface: tanda panah menunjukkan tiga aplikasi utama yang dapat diakses langsung dari Address Bar*

Setelah konfigurasi selesai, Anda akan menemukan Interface yang ramping dari Orion dengan **tiga Tools penting** (ditunjukkan oleh tanda panah):

- **Perisai 🛡️**: Menampilkan Laporan Privasi dengan jumlah item yang diblokir pada halaman saat ini
- **Sikat 🖌️**: Menyesuaikan tampilan halaman (tema, font, menghapus Elements yang mengganggu)
- **Gear ⚙️**: Mengonfigurasi parameter khusus situs web (izin, pemblokiran, dll.)

Tools ini selalu tersedia dan memungkinkan Anda untuk mengontrol pengalaman penjelajahan Anda berdasarkan situs per situs.

**Penting**: Orion gratis dan tidak memerlukan registrasi atau pembuatan akun untuk beroperasi.

![Orion+ dans les préférences](assets/fr/08.webp)

*Layar langganan Orion+ di preferensi, menawarkan langganan opsional untuk mendukung pengembangan*

**Orion+ (opsional)**: Untuk mendukung pengembangan proyek, Kagi menawarkan Orion+ ($5/bulan, $50/tahun, atau $150 seumur hidup). Langganan sukarela ini memungkinkan:

- Berkomunikasi langsung dengan tim pengembangan.
- Mempengaruhi evolusi browser sesuai dengan kebutuhan Anda.
- Mengakses versi Nightly dengan fitur eksperimental terbaru.
- Mendapatkan manfaat dari engine WebKit terbaru.
- Mendapatkan badge khas di forum feedback.

Orion+ menjamin independensi proyek: "Kontribusi finansial Anda membantu kami tetap independen dan menepati janji kami untuk menjadi browser terbaik bagi pengguna kami". Model pendanaan pengguna inilah yang membuat Orion bebas iklan dan bebas telemetry.

## Konfigurasi untuk kerahasiaan maksimum

### Parameter penting

Akses preferensi melalui **Orion → Preferences** (atau ⌘,):

**1. Penelusuran - Search engine pribadi**

![Configuration du moteur de recherche](assets/fr/09.webp)

*Konfigurasi search engine default: DuckDuckGo dipilih untuk privasi maksimum*

- **Mesin pencari bawaan**: Pilih **DuckDuckGo**, **Startpage** atau **Kagi** untuk privasi yang optimal (hindari Google/Bing)
- **Saran pencarian**: Nonaktifkan untuk mencegah kebocoran data dari penekanan tombol ke server mesin pencari

**2. Privasi - Perlindungan umum**

![Content Blocker dans les préférences](assets/fr/12.webp)

*Pengaturan privasi Orion menunjukkan Pemblokir Konten dengan 119.156 aturan aktif, opsi penghapusan pelacak, dan agen pengguna khusus*

**Pemblokir Konten aktif secara default**:

- **EasyList**: 119 ribu+ aturan pemblokiran iklan
- **EasyPrivacy**: Perlindungan terhadap pelacakan
- **Manage Filter Lists**: Menambahkan daftar tambahan (disarankan oleh Hagezi)

**Opsi privasi**:

- **Remove trackers from URLs**: "For Private Browsing only" membersihkan tautan yang disalin.
- **Share crash reports**: "After asking for approval" menghormati persetujuan Anda.
- **Custom user agent**: Dapat dimodifikasi untuk melewati pemblokiran tertentu.

![YouTube avec Privacy Report](assets/fr/10.webp)

*Contoh YouTube yang dilihat dengan Orion: tidak ada iklan yang terlihat dan Laporan Privasi yang menunjukkan banyak Elements yang diblokir*

**3. Pengaturan Situs Web - Kontrol berdasarkan situs**

![Website Settings pour YouTube](assets/fr/11.webp)

*Pengaturan Situs Web untuk YouTube yang menampilkan opsi kompatibilitas, pemblokiran konten, dan izin khusus situs*

**Akses cepat**: Klik pada gear ⚙️ di Address bar untuk menyesuaikan:

- **Compatibility Mode**: Menyelesaikan masalah tampilan dengan menangguhkan ekstensi.
- **Content Blockers**: Nonaktifkan pemblokiran untuk situs tertentu jika perlu.
- **JavaScript/Cookies**: Kontrol granular berdasarkan situs.
- **Permissions**: Kamera, mikrofon, lokasi dikonfigurasi secara individual.

**4. Filter Khusus Tingkat Lanjut** (lihat di bawah)

**Membuat filter khusus** (Privacy → Manage Filter Lists → Custom Filters):

**Sintaks yang disederhanakan** (Kompatibel dengan Adblock Plus):

- `reddit.com##.promotedlink`: Menyembunyikan postingan Reddit yang disponsori
- `|ads.example.com^`: Memblokir domain iklan sepenuhnya
- `@@||situs-utile.com^`: Membuat pengecualian untuk sebuah situs

**Tip: Kunjungi [FilterLists.com](https://filterlists.com) untuk mendapatkan ribuan daftar khusus yang siap digunakan.**

### Ekstensi yang disarankan

Orion secara bawaan mendukung ekstensi Chrome dan Firefox. Instal langsung dari toko resmi:

**Penting**:

- ****asal uBlock****: Menambahkan kontrol granular ke pemblokir asli
- **Bitwarden**: Pengelola kata sandi sumber terbuka
- **ClearURLs**: Menghapus parameter pelacakan URL

**Opsional**:

- **LocalCDN**: Menyajikan library bersama secara lokal.
- **Cookie AutoDelete**: Secara otomatis menghapus cookie setelah menutup tab
- **NoScript**: Kontrol penuh atas eksekusi JavaScript (pengguna tingkat lanjut)

Untuk menginstal file:

- Kunjungi [chrome.google.com/webstore](https://chrome.google.com/webstore) atau [addons.mozilla.org](https://addons.mozilla.org)
- Klik "Add to Chrome/Firefox"
- Orion akan mencegat dan memasang ekstensi secara otomatis

**Perhatian**: Karena dukungan ekstensi bersifat eksperimental, banyak ekstensi mungkin tidak berfungsi dengan baik atau dapat memengaruhi performa. Jika terjadi masalah (situs tidak berfungsi lagi, lambat), nonaktifkan ekstensi satu per satu untuk mengidentifikasi sumber masalah.

## Penggunaan sehari-hari

### Interface dan fitur-fitur unik

![Outil de personnalisation pinceau](assets/fr/13.webp)

_Menu kuas Orion untuk menyesuaikan tampilan: ukuran font, tema (terang/gelap), penonaktifan sticky headers, dan penghapusan elemen yang mengganggu_

**Tool kuas: kustomisasi tingkat lanjut**

Tool **brush** Orion adalah fitur unik yang memungkinkan Anda menyesuaikan tampilan setiap situs web:

**Pilihan tema**:

- Beralih antara tema terang dan gelap untuk setiap situs
- Adaptasi otomatis dengan preferensi sistem Anda

**Kontrol tipografi**:

- **Ukuran huruf**: Sesuaikan keterbacaan dengan tombol A- dan A+
- **Gaya huruf**: Mengubah jenis huruf (default atau kustom)

**Pembersihan Interface**:

- **Disable sticky headers**: Menghapus header yang tetap tersangkut di bagian atas saat menggulir
- **Erase Elements**: Menghapus Elements yang mengganggu secara permanen (iklan, pop-up, spanduk cookie)
  - Klik "+ Erase" lalu pilih item yang akan disembunyikan
  - Sangat berguna untuk situs dengan iklan persisten atau pelacakan visual Elements

**Persistensi**: Semua pengaturan ini disimpan per domain dan diterapkan kembali secara otomatis saat kunjungi kembali.

**Manajemen tab lanjutan**:

- **Tab vertikal**: Aktifkan melalui menu bar (Fungsi Tab di Samping)
- **Tab yang ringkas**: Di Preferences → Tabs → Layout "Compact" untuk menghemat ruang
- **Grup tab**: Atur sesi Anda berdasarkan tema
- **Beberapa profil**: Buat identitas terpisah melalui bilah menu (fungsi Profil) dengan data yang sepenuhnya terisolasi

**Low Power Mode (Mode Daya Rendah)**: Terinspirasi oleh iPhone, mode ini secara otomatis menangguhkan tab yang tidak aktif setelah 5 menit dan dapat mengurangi konsumsi energi hingga 90%. Aktifkan melalui menu bar Orion di Mac, atau di pengaturan pada iOS.

**Tool bantu bawaan** (Menu edit dan lainnya):

- **Edit Teks di Halaman**: mengubah teks apa pun untuk sementara (menu Edit)
- **Allow Copy & Paste**: Melewati pembatasan penyalinan (menu Edit)
- **Copy Clean Link**: Klik kanan pada tautan untuk menghapus parameter pelacakan
- **Focus Mode**: navigasi layar penuh yang bebas gangguan
- **Picture-in-Picture**: Menonton video di window mengambang
- **Open in Internet Archive**: Akses langsung ke versi arsip
- **Privacy Report**: Klik pada perisai 🛡️ untuk melihat item yang diblokir berdasarkan halaman

### Manajemen penjelajahan pribadi

Penawaran navigasi pribadi Orion (⌘⇧N):

- Isolasi lengkap cookies dan sesi.
- Penghapusan otomatis saat ditutup.
- Penonaktifan riwayat dan cache.
- Peningkatan perlindungan terhadap fingerprinting.

**Tip**: Untuk kompartementalisasi tingkat lanjut, buat **profil terpisah** via menu bar (Profiles function). Setiap profil muncul sebagai aplikasi terpisah di Dock, dengan pengaturan, ekstensi, dan data yang sepenuhnya terisolasi.

### Optimalisasi kinerja dan privasi

Untuk menjaga Orion tetap cepat dan privat:

- **Ekstensi**: Batasi seminimal mungkin (dapat mengurangi performa).
- **Low Power Mode**: Aktifkan untuk sesi panjang (kemungkinan penghematan 90%).
- **Privacy Report**: Klik pada perisai 🛡️ untuk melihat pemblokiran secara real time.
- **Kustomisasi Visual**: Gunakan kuas 🖌️ untuk menyesuaikan tampilan dan menghapus elemen yang mengganggu.
- **Copy Clean Link**: Klik kanan untuk menyalin tautan tanpa pelacak.
- **Profil Terpisah**: Gunakan profil khusus untuk mengkompartementalisasi aktivitas Anda.
- **Website Setting**s: Klik pada gear ⚙️ untuk menyesuaikan permissions per situs.
- **Pembersihan Rutin**: Bersihkan cache via Orion → Clear Browsing Data.

## Perbandingan dengan alternatif

|Kriteria |	Orion	| Safari	| Chrome |	Firefox |	Brave |
|---------|-------|--------|---------|----------|--------|
|**Telemetry** |	Tidak Ada |	Minimal |	Ekstensif |	Sedang |	Minimal |
|**Blokir Bawaan**| 99,9% efektif |	Dasar |Tidak Ada	|Parsial	|Lengkap |
|**Ekstensi** |	Chrome + Firefox |	Terbatas |	Chrome saja |	Firefox saja |	Chrome saja |
|**Performa Mac** |	Sangat Baik |	Sangat Baik |	Baik |	Sedang |	Baik |
|**Konsumsi RAM**|	Sangat Rendah |	Rendah |	Tinggi |	Sedang |	Sedang |
|**Open Source** | 	Parsial |	Parsial (WebKit) |	Parsial |	Lengkap |	Lengkap |
|**Platform**	| Mac/iOS |	Mac/iOS |	Semua |	Semua	| Semua |

**VS Safari**: Orion menawarkan perlindungan superior dengan pemblokir canggih dan dukungan ekstensinya, sambil mempertahankan performa WebKit.
**VS Chrome**: privasi yang tak tertandingi tanpa mengorbankan kompatibilitas, berkat dukungan untuk ekstensi Chrome.
**VS Firefox**: Lebih cepat di Mac, Interface lebih intuitif, tetapi kontrolnya kurang terperinci dan bukan open source.
**VS Brave**: Filosofi yang serupa, tetapi Orion menghindari kontroversi kripto/BAT dan menawarkan integrasi Apple yang lebih baik.

## Kasus penggunaan yang disarankan

**Ideal untuk**:

- Pengguna Apple yang mencari privasi lebih dari Safari.
- Orang yang ingin memblokir semua iklan (termasuk YouTube) tanpa ekstensi.
- Pengembang yang membutuhkan devtools WebKit dengan perlindungan privasi terintegrasi.
- Pengguna iPhone yang menginginkan ekstensi desktop di seluler (inovasi unik).
- Profesional yang perlu mengkompartementalisasi aktivitas mereka (multiple profiles).
- Pengguna seluler yang mencari manajemen baterai yang lebih baik (Low Power Mode).

**Hindari jika**:

- Anda sebagian besar menggunakan Windows/Linux (tidak ada versi tersedia).
- Open source penuh sangat penting untuk model ancaman Anda.
- Anda bergantung pada ekstensi spesifik yang mungkin tidak berfungsi.
- Anda membutuhkan sinkronisasi lintas-platform di luar ekosistem Apple.
- Anda lebih memilih solusi yang teruji dan stabil (status beta permanen sejak 2021).

## Poin-poin yang perlu diperhatikan dan keamanan

### Fitur keamanan yang unik

- **Perlindungan anti-fingerprinting revolusioner**: Orion adalah satu-satunya browser yang sepenuhnya memblokir eksekusi script fingerprinting sebelum mereka dapat memindai sistem Anda. Pendekatan "tidak ada script berjalan = tidak ada fingerprinting yang mungkin" ini mengungguli metode penyamaran tradisional yang digunakan oleh browser lain.
- **Transparent Whitelist**: Orion mempertahankan beberapa daftar web publik (browserbench.org, wizzair.com) di mana pemblokiran secara otomatis dinonaktifkan untuk menghindari malfungsi. Transparansi ini memungkinkan pengguna untuk memahami secara pasti kapan dan mengapa pemblokiran diringankan.
- **Ekstensi yang belum diaudit**: Dukungan untuk ekstensi Chrome/Firefox menimbulkan risiko tambahan, karena ekstensi ini tidak dirancang untuk WebKit dan tidak diaudit secara khusus untuk lingkungan ini.

### Pemeliharaan dan pembaruan

- **Pembaruan otomatis**: Orion diperbarui secara otomatis di macOS melalui Sparkle
- **Pelacakan kerentanan**: Periksa perilisan secara teratur untuk mengetahui patch keamanan
- **Pelaporan bug**: Gunakan [orionfeedback.org](https://orionfeedback.org) untuk melaporkan masalah

## Kesimpulan

Orion Browser merepresentasikan langkah maju yang signifikan untuk privasi pada macOS dan iOS. Pendekatan tanpa telemetry-nya, dikombinasikan dengan pemblokir native yang sangat efisien dan dukungan unik untuk ekstensi universal, menjadikannya pilihan yang sangat baik bagi pengguna Apple yang sadar privasi.

**Penting**: Orion tetap dalam status beta permanen sejak 2021, dengan keterbatasan kompatibilitas ekstensi dan risiko WebKit yang melekat. Nilai kekurangan ini sesuai dengan model ancaman Anda.

Untuk penggunaan sehari-hari di Mac atau iPhone, ini mungkin merupakan alternaif terbaik antara kerahasiaan, kinerja, dan kemudahan penggunaan yang tersedia di ekosistem Apple, asalkan Anda menerima keterbatasannya.

**Ingat**: melindungi privasi Anda tidak hanya bergantung pada browser Anda. Gabungkan Orion dengan kebiasaan baik (kata sandi kuat, 2FA, VPN jika perlu) untuk keamanan online yang optimal.

## Sumber daya dan dukungan

### Dokumentasi resmi

- **Situs web resmi**: [kagi.com/orion](https://kagi.com/orion/)
- **Pertanyaan Umum Lengkap**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- **Forum komunitas**: [community.kagi.com](https://community.kagi.com)
- **Pelacakan bug**: [orionfeedback.org](https://orionfeedback.org)
- **GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Komponen open source
- **Blog Kagi**: [blog.kagi.com](https://blog.kagi.com) - Berita dan pembaruan

### Tes verifikasi yang disarankan

Setelah konfigurasi, uji pengaturan Anda:

- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - Tes fingerprinting
- [Tes Kebocoran DNS](https://www.dnsleaktest.com/) - Periksa kebocoran DNS
- [BrowserLeaks](https://browserleaks.com/) - Rangkaian lengkap tes privasi

### Alternatif pada Plan ₿ Network

Untuk perlindungan maksimal, bacalah panduan kami yang lain:

- [Firefox yang diperkuat](https://planb.network/tutorials/computer-security/communication/firefox-11814cec-3415-4ed9-a06e-f6fda5c9510f) - Konfigurasi multi-platform tingkat lanjut
- [Tor Browser](https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb) - Anonimitas jaringan lengkap
- [Browser Mullvad](https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e) - Perlindungan fingerprinting maksimum

Jika Anda ingin mempelajari lebih lanjut tentang sejarah dan pengoperasian browser, serta objek digital utama dalam kehidupan sehari-hari, saya mengundang Anda untuk menemukan kursus pelatihan gratis kami yang baru, SCU 202, yang tersedia di Plan ₿ Network:

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
