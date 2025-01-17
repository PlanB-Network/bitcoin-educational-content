---
term: FILTER MEKAR

---
Struktur data probabilistik yang digunakan untuk menguji apakah sebuah elemen merupakan bagian dari sebuah himpunan. Bloom Filter memungkinkan pemeriksaan keanggotaan secara cepat tanpa menguji seluruh dataset. Filter ini sangat berguna dalam konteks di mana ruang dan kecepatan sangat penting, tetapi tingkat kesalahan yang rendah dan terkendali masih dapat diterima. Memang, Bloom Filter tidak menghasilkan false negative, tetapi menghasilkan sejumlah false positive. Ketika sebuah elemen ditambahkan ke filter, beberapa fungsi hash menghasilkan posisi dalam larik bit. Untuk memeriksa keanggotaan, fungsi hash yang sama digunakan. Jika semua bit yang sesuai di-set, elemen tersebut mungkin ada di dalam set, tetapi dengan risiko positif palsu. Filter Bloom banyak digunakan dalam bidang database dan jaringan. Google diketahui menggunakan filter ini untuk sistem manajemen basis data terkompresi *BigTable*. Dalam protokol Bitcoin, mereka digunakan terutama untuk dompet SPV menurut BIP37.

> ► *Ketika secara khusus berbicara tentang penggunaan Filter Bloom dalam konteks transaksi Bitcoin, istilah "Pemfilteran Bloom Transaksi" terkadang ditemukan.*