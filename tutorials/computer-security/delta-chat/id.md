---
name: Delta Chat
description: Panduan praktis untuk alat perpesanan yang terdesentralisasi
---

![image](assets/cover.webp)




## Pendahuluan - Kontrol Obrolan dan Privasi



Dalam beberapa tahun terakhir ini, ada peningkatan pembicaraan tentang Kontrol Obrolan, sebuah proposal peraturan yang bertujuan untuk memperkenalkan pemindaian otomatis pesan pribadi pada platform komunikasi utama. Tujuan yang dinyatakan adalah untuk memerangi konten ilegal, masalahnya adalah bahwa mekanisme ini pada kenyataannya akan melibatkan pengawasan massal, yang akan merusak enkripsi ujung ke ujung dan dengan demikian privasi semua pengguna, bukan hanya pelanggar.



Risiko yang sebenarnya adalah bahwa obrolan menjadi lingkungan yang terkendali, di mana setiap pesan, gambar, atau lampiran dapat diteliti bahkan sebelum mencapai penerima. Dan di sinilah salah satu solusi yang mungkin dilakukan: beralih dari platform yang terpusat dan menuju sistem perpesanan yang terdesentralisasi, yang tidak bergantung pada satu penyedia dan tidak dapat dengan mudah menjadi sasaran pengawasan semacam ini.



Salah satu solusi tersebut akan disajikan dalam tutorial ini: Delta Chat. Alat yang sudah matang dan sudah dapat digunakan.




## Mengapa Delta Chat dan cara kerjanya



Delta Chat adalah solusi perpesanan yang sudah sangat bagus untuk penggunaan sehari-hari: sangat berguna untuk berbicara dengan teman, keluarga, dan orang lain, seperti halnya WhatsApp yang sebenarnya.



Ini adalah sistem perpesanan terdesentralisasi yang sepenuhnya berbasis email. Pada dasarnya memanfaatkan infrastruktur email tradisional, tetapi membangun antarmuka dan pengalaman pengirim pesan instan modern di atasnya. Sekilas ini mungkin tampak sedikit improvisasi, tetapi sebenarnya bekerja dengan sangat baik dan sangat kuat. Anda bisa menggunakan server email khusus yang disebut ChatMail, tetapi juga bisa bekerja secara mulus dengan server email biasa. Ini berarti Anda bisa masuk dengan akun yang sudah ada jika Anda mau, tanpa harus membuat sesuatu yang baru.



Sorotan lainnya adalah dukungan untuk WebXDC, yang merupakan aplikasi Web kecil yang dapat digunakan secara langsung di dalam obrolan, mirip dengan aplikasi mini di Telegram. Perbedaan yang penting adalah aplikasi ini tidak memiliki akses Internet, sehingga tidak dapat melacak pengguna atau mengirim data secara eksternal.



Dari perspektif keamanan, Delta Chat menggunakan enkripsi ujung ke ujung yang terverifikasi, berdasarkan pada PGP tetapi dengan ekstensi modern yang membuatnya sebanding dengan tingkat proteksi dengan Signal. Satu-satunya kekurangan saat ini adalah Kerahasiaan Terusan Sempurna, tetapi itu merupakan aspek yang terus berkembang.



Karena hanya berbasis pada email, Delta Chat menghindarinya sama sekali:




- nomor telepon wajib
- ID terpusat
- pendaftaran yang ditautkan ke satu layanan



Dan itulah yang membuat alat ini sangat tahan terhadap peraturan invasif seperti Kontrol Obrolan.




## Instalasi



Dari situs web resmi [Delta Chat] (https://delta.chat/download) Anda dapat pergi ke bagian Download. Di Linux, aplikasi ini tersedia dengan mudah melalui Flathub, tetapi ada juga paket untuk Arch, NixOS, Snap dan versi mandiri.



![image](assets/it/01.webp)



Ini juga tersedia untuk:




- [F-Droid] (https://f-droid.org/app/com.b44t.messenger)
- [Play Store](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS] (https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- dan toko-toko lainnya...



Jika Anda mencari panduan untuk menginstal F-Droid, tutorial ini dapat membantu Anda:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Satu hal yang sangat penting: versi desktop tidak memerlukan ponsel. Tidak seperti WhatsApp atau SimpleX Chat, Anda tidak perlu mendaftar dari ponsel terlebih dahulu. Anda bisa membuat profil langsung di PC atau mentransfernya dari perangkat lain.




## Pembuatan profil



Setelah aplikasi terbuka, Delta Chat akan menanyakan apakah Anda ingin membuat profil baru atau menggunakan profil yang sudah ada.



![image](assets/it/02.webp)



Dengan membuat profil baru, Anda dapat masuk:




- sebuah nama
- gambar (opsional)



Server ChatMail diusulkan secara default, tetapi dimungkinkan:




- memilih server ChatMail lain
- menggunakan akun email klasik
- mengkonfigurasi IMAP dan SMTP secara manual
- mendaftar menggunakan kode undangan pengguna lain



Setelah beberapa detik, profil sudah siap dan Anda dapat mulai menggunakan aplikasi.



![image](assets/it/03.webp)




## Interface dan obrolan



Antarmukanya sangat sederhana dan mudah:




- Pesan perangkat, yang merupakan komunikasi lokal
- Pesan yang disimpan, serupa dengan yang ada di Telegram dan dapat disinkronkan di antara perangkat



![image](assets/it/04.webp)



Untuk menambahkan kontak secara sederhana:




- Menampilkan kode QR Anda
- Memindai orang lain
- Undang melalui tautan (bagikan tautan undangan).



![image](assets/it/05.webp)



Setelah koneksi dibuat, enkripsi ujung ke ujung dikonfigurasikan secara otomatis. Antarmuka pengguna obrolan sangat mirip dengan WhatsApp:




- pesan teks dan suara
- foto, video, dan file
- tanggapan terhadap pesan
- reaksi
- pesan pop-up
- pemberitahuan yang dapat disesuaikan.



![image](assets/it/06.webp)



## WebXDC: aplikasi dalam obrolan:



Delta Chat memungkinkan penggunaan WebXDC, yaitu aplikasi kecil yang disematkan dalam percakapan. Berikut ini adalah daftar singkat yang paling berguna yang teridentifikasi:




- survei
- papan gambar
- obrolan pribadi sementara
- permainan dengan skor obrolan bersama



Permainan yang lebih kompleks juga dapat dimulai, yang menunjukkan fleksibilitas alat ini.



![image](assets/it/07.webp)



## Grup, saluran, dan fitur lanjutan



Anda dapat membuat grup, menggunakan stiker (khususnya pada desktop) dan, dengan mengaktifkan opsi eksperimental, bahkan saluran, mirip dengan yang ada di Telegram.



Dalam pengaturan lanjutan, Anda dapat mengaktifkan:




- panggilan suara (masih dalam tahap percobaan)
- manajemen profil email tingkat lanjut
- cadangan penuh.



![image](assets/it/08.webp)



## Multiperangkat dan pencadangan



Delta Chat sepenuhnya mendukung multidevice:




- anda dapat menambahkan perangkat kedua melalui kode QR
- anda dapat melakukan transfer penuh melalui cadangan.



Dalam hitungan detik, Anda akan menemukan obrolan, grup, dan riwayat lengkap Anda lagi, tanpa bergantung pada server pusat.



![image](assets/it/09.webp)




## Kesimpulan



Pada saat ada peningkatan pembicaraan tentang pengendalian komunikasi pribadi, Delta Chat mewakili jawaban konkret: pesan yang terdesentralisasi dan terenkripsi yang benar-benar dapat digunakan setiap hari.



Ini adalah solusi yang, dari semua solusi yang pernah saya coba, paling meyakinkan saya dalam hal kesederhanaan, privasi, dan kebebasan. Jika Anda mau, Anda juga bisa menghubungi saya di Delta Chat melalui [tautan undangan] berikut ini (https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats)



Jika Anda menikmati panduan ini, Anda bisa mendukung saya dengan memberikan donasi dan memberikan jempol. Dan ingat: hanya dengan menggunakan dan menjelajahi Delta Chat dari ponsel dan desktop, Anda akan benar-benar menemukan fungsionalitas penuhnya.



Sampai jumpa lagi.