---
term: BIP0008

---
Usulan yang dikembangkan setelah perdebatan mengenai SegWit, yang menggunakan BIP9 untuk aktivasinya. BIP0008 adalah metode aktivasi _soft fork_ yang secara dasar menggunakan mekanisme UASF (*User-Activated Soft Fork*). Seperti BIP9, BIP0008 menggunakan metode sinyal penambang, tetapi menambahkan parameter `LOT` (*Lock-in On Time out*). Jika `LOT` diatur ke `true` setelah berakhirnya periode pensinyalan tanpa mencapai ambang batas yang diperlukan, UASF secara otomatis akan dijalankan, memaksa aktivasi _soft fork_. Pendekatan ini memaksa para penambang untuk bersikap kooperatif atau mengambil risiko UASF yang dipaksakan oleh pengguna. Selain itu, tidak seperti BIP9, BIP0008 mendefinisikan periode pensinyalan berdasarkan tinggi blok, sehingga menghilangkan potensi manipulasi melalui _hash rate_ oleh penambang. BIP0008 juga memungkinkan pengaturan ambang batas variabel pengambilan suara dan memperkenalkan parameter tinggi blok minimum untuk aktivasi, memberikan waktu kepada para penambang untuk mempersiapkan dan memberi sinyal persetujuan mereka terlebih dahulu. Aktivasi _soft fork_ melalui BIP0008 dengan parameter `LOT=true` merupakan pendekatan yang cukup agresif, karena memberi tekanan langsung kepada para penambang melalui ancaman UASF. Hal ini membuat mereka hanya memiliki 2 pilihan:


- Bersikap kooperatif dengan memfasilitasi proses aktivasi;
- Bersikap tidak kooperatif, dimana dalam hal ini, pengguna secara otomatis melakukan UASF untuk menerapkan _soft fork._
