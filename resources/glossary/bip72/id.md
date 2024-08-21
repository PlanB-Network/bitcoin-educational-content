---
term: BIP72
---

Melengkapi BIP70 dan BIP71 dengan mendefinisikan ekstensi dari URI Bitcoin (BIP21) dengan parameter tambahan `r`. Parameter ini memungkinkan penambahan link ke permintaan pembayaran yang aman dan ditandatangani oleh sertifikat SSL pedagang. Ketika klien mengklik URI yang diperluas ini, dompet mereka menghubungi server pedagang untuk meminta detail pembayaran. Detail-detail ini secara otomatis diisi dalam antarmuka transaksi dompet, dan klien dapat diberitahu bahwa mereka membayar kepada pemilik domain yang sesuai dengan sertifikat penandatangan (misalnya, "pandul.fr"). Karena peningkatan ini dibundel dengan BIP70, ini tidak pernah secara luas diadopsi.