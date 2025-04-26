---
term: KESULITAN

---
Parameter yang dapat disesuaikan yang menentukan kompleksitas bukti kerja yang diperlukan untuk menambahkan blok baru ke blockchain dan mendapatkan reward terkait. Kesulitan ini diwakili oleh target kesulitan, sebuah nilai 256-bit yang menetapkan batas atas yang harus dipenuhi oleh hash header blok untuk dianggap valid. Tujuannya adalah agar hash, yang dicapai melalui eksekusi ganda SHA256 (SHA256d), kurang dari atau sama dengan target ini. Untuk mencapai hash ini, penambang memanipulasi `nonce` pada header blok. Tingkat kesulitan menyesuaikan setiap 2016 blok, atau kira-kira setiap dua minggu, untuk mempertahankan waktu pembuatan blok rata-rata sekitar 10 menit.