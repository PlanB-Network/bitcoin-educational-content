---
term: BIP0072

definition: Ekstensi URI Bitcoin dengan parameter untuk permintaan pembayaran aman BIP70. Tidak pernah diadopsi secara luas.
---
BIP ini melengkapi BIP70 dan BIP71 dengan mendefinisikan ekstensi URI Bitcoin (BIP21) dengan parameter tambahan `r`. Parameter ini memungkinkan penyertaan tautan ke permintaan pembayaran aman yang ditandatangani oleh sertifikat SSL pedagang. Ketika klien mengklik _extended_ URI ini, dompet mereka akan menghubungi _server merchant_ untuk meminta detail pembayaran. Rincian ini secara otomatis terisi di antarmuka transaksi dompet, dan klien dapat mengetahui bahwa mereka membayar pemilik domain yang sesuai dengan sertifikat penandatanganan (misalnya, "pandul.fr"). Karena perangkat tambahan ini dibundel dengan BIP70, perangkat ini tidak pernah diadopsi secara luas.
