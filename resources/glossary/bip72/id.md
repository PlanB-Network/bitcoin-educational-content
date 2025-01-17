---
term: BIP72

---
Melengkapi BIP70 dan BIP71 dengan mendefinisikan ekstensi URI Bitcoin (BIP21) dengan parameter tambahan `r`. Parameter ini memungkinkan untuk menyertakan tautan ke permintaan pembayaran aman yang ditandatangani oleh sertifikat SSL pedagang. Ketika klien mengklik URI yang diperluas ini, dompet mereka akan menghubungi server merchant untuk meminta detail pembayaran. Rincian ini secara otomatis terisi di antarmuka transaksi dompet, dan klien dapat mengetahui bahwa mereka membayar pemilik domain yang sesuai dengan sertifikat penandatanganan (misalnya, "pandul.fr"). Karena perangkat tambahan ini dibundel dengan BIP70, perangkat ini tidak pernah diadopsi secara luas.