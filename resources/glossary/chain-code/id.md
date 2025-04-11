---
term: KODE RANTAI

---
Dalam konteks derivasi hirarkis deterministik (HD) dari dompet Bitcoin, kode rantai adalah sebuah nilai garam kriptografi 256-bit yang digunakan untuk menghasilkan anak kunci dari kunci induk, sesuai dengan standar BIP32. Kode rantai digunakan dalam kombinasi dengan kunci induk dan indeks anak untuk secara deterministik menghasilkan sepasang kunci baru (kunci pribadi dan kunci publik) tanpa mengungkapkan kunci induk atau kunci turunan lainnya.

Oleh karena itu, terdapat sebuah kode rantai yang unik untuk setiap pasangan kunci. Kode rantai didapatkan dengan melakukan hashing pada seed wallet dan mengambil setengah bagian bit yang tepat. Dalam hal ini, ini disebut sebagai kode rantai master, yang berhubungan dengan kunci pribadi master. Sebagai alternatif, kode ini dapat diperoleh dengan melakukan hashing pada kunci induk dengan kode rantai induk dan indeks, kemudian menyimpan bit yang tepat. Ini kemudian disebut sebagai kode rantai anak.

Tidak mungkin untuk mendapatkan kunci tanpa mengetahui kode rantai yang terkait dengan setiap pasangan induk. Ini memperkenalkan data acak semu ke dalam proses derivasi untuk memastikan bahwa pembuatan kunci kriptografi tetap tidak dapat diprediksi oleh penyerang dan tetap deterministik untuk pemegang dompet.

> ► *Dalam bahasa Inggris, "code de chaîne" disebut "kode rantai", dan "code de chaîne maître" disebut "kode rantai utama".*