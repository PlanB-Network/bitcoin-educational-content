---
term: KODE RANTAI

---
Dalam konteks derivasi hirarkis deterministik (HD) dari dompet Bitcoin, kode rantai adalah sebuah nilai garam kriptografi 256-bit yang digunakan untuk menghasilkan anak kunci dari kunci induk, sesuai dengan standar BIP32. Kode rantai digunakan dalam kombinasi dengan kunci induk dan indeks anak untuk secara deterministik menghasilkan sepasang kunci baru (kunci pribadi dan kunci publik) tanpa mengungkapkan kunci induk atau kunci turunan lainnya.

Oleh karena itu, terdapat sebuah kode rantai yang unik untuk setiap pasangan kunci. Kode rantai didapatkan dengan melakukan _hashing_ pada _seed_ dompet dan mengambil setengah bagian bit yang tepat. Dalam hal ini, ini disebut sebagai kode rantai _master_, yang berhubungan dengan kunci pribadi _master_. Sebagai alternatif, kode ini dapat diperoleh dengan melakukan _hashing_ pada kunci induk dengan kode rantai induk dan indeks, kemudian menyimpan bit yang tepat. Ini kemudian disebut sebagai kode rantai anak.

Tidak mungkin untuk mendapatkan kunci tanpa mengetahui kode rantai yang terkait dengan setiap pasangan induk. Ini memperkenalkan data acak semu ke dalam proses derivasi untuk memastikan bahwa pembuatan kunci kriptografi tetap tidak dapat diprediksi oleh penyerang dan tetap deterministik untuk pemegang dompet.

> ► *Dalam bahasa Inggris, kode rantai disebut "chain code".*
