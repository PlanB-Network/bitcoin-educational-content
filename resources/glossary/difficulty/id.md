---
term: KESULITAN
---

Sebuah parameter yang dapat diatur yang menentukan kompleksitas dari bukti kerja yang diperlukan untuk menambahkan blok baru ke blockchain dan mendapatkan hadiah yang terkait. Kesulitan ini diwakili oleh target kesulitan, sebuah nilai 256-bit yang menetapkan batas atas yang harus dipenuhi oleh hash header blok agar dianggap valid. Tujuannya adalah agar hash, yang dicapai melalui eksekusi ganda SHA256 (SHA256d), harus lebih kecil atau sama dengan target ini. Untuk mencapai hash ini, penambang memanipulasi `nonce` di header blok. Kesulitan ini menyesuaikan setiap 2016 blok, atau kira-kira setiap dua minggu, untuk mempertahankan waktu pembuatan blok rata-rata sekitar 10 menit.