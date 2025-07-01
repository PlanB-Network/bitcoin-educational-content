---
term: KESULITAN

---
Parameter yang dapat disesuaikan yang menentukan kompleksitas _proof-of-work_ yang diperlukan untuk menambahkan blok baru ke _blockchain_ dan mendapatkan _block reward_ terkait. Kesulitan ini diwakili oleh target kesulitan, sebuah nilai 256-bit yang menetapkan batas atas yang harus dipenuhi oleh _hash header_ blok untuk dianggap valid. Tujuannya adalah agar _hash_, yang dicapai melalui eksekusi ganda SHA256 (SHA256d), kurang dari atau sama dengan target ini. Untuk mencapai hash ini, penambang memanipulasi `nonce` pada _header_ blok. Tingkat kesulitan disesuaikan setiap 2016 blok, atau kira-kira setiap dua minggu, untuk mempertahankan waktu penambangan blok rata-rata sekitar 10 menit.
