---
term: BIP8

---
Dikembangkan setelah perdebatan mengenai SegWit, yang menggunakan BIP9 untuk aktivasinya, BIP8 adalah metode aktivasi soft fork yang secara native menggunakan mekanisme UASF (*User-Activated Soft Fork*). Seperti BIP9, BIP8 menggunakan pensinyalan penambang tetapi menambahkan parameter `LOT` (*Lock-in On Time out*). Jika `LOT` diatur ke `true`, setelah berakhirnya periode pensinyalan tanpa mencapai ambang batas yang diperlukan, UASF secara otomatis dipicu, memaksa aktivasi soft fork. Pendekatan ini memaksa para penambang untuk bersikap kooperatif atau mengambil risiko UASF yang dipaksakan oleh pengguna. Selain itu, tidak seperti BIP9, BIP8 mendefinisikan periode pensinyalan berdasarkan tinggi blok, menghilangkan potensi manipulasi melalui hash rate oleh penambang. BIP8 juga memungkinkan untuk mengatur ambang batas voting variabel dan memperkenalkan parameter untuk tinggi blok minimum untuk aktivasi, memberikan waktu kepada para penambang untuk mempersiapkan dan memberi sinyal persetujuan mereka terlebih dahulu tanpa harus siap. Ketika sebuah soft fork diaktifkan melalui BIP8 dengan parameter `LOT=true`, ini menggunakan metode yang sangat agresif terhadap para penambang yang langsung berada di bawah tekanan UASF yang potensial. Memang, hal ini membuat mereka hanya memiliki 2 pilihan:


- Bersikaplah kooperatif, dan dengan demikian memfasilitasi proses aktivasi;
- Bersikaplah tidak kooperatif, dalam hal ini pengguna secara otomatis melakukan UASF untuk menerapkan soft fork.