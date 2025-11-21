---
term: BLOOM FILTER

---
Struktur data probabilistik yang digunakan untuk menguji apakah sebuah elemen merupakan bagian dari sebuah himpunan. _Bloom Filter_ memungkinkan pemeriksaan keanggotaan secara cepat tanpa menguji seluruh dataset. Filter ini sangat berguna dalam konteks di mana ruang dan kecepatan sangat penting, tetapi tingkat kesalahan yang rendah dan terkendali masih dapat diterima. Memang, _Bloom Filter_ tidak menghasilkan _false negative_, tetapi menghasilkan sejumlah _false positive_. Ketika sebuah elemen ditambahkan ke filter, beberapa fungsi _hash_ menghasilkan posisi dalam larik bit. Untuk memeriksa keanggotaan, fungsi _hash_ yang sama digunakan. Jika semua bit yang sesuai di-set, elemen tersebut mungkin ada di dalam set, tetapi dengan risiko _false positive_. _Bloom Filter_ banyak digunakan dalam bidang database dan jaringan. Google diketahui menggunakan filter ini untuk sistem manajemen basis data terkompresi *BigTable*. Dalam protokol Bitcoin, mereka digunakan terutama untuk dompet SPV menurut BIP37.

> ► *Ketika secara khusus berbicara tentang penggunaan Bloom Filter dalam konteks transaksi Bitcoin, istilah "Pemfilteran Bloom Transaksi" terkadang ditemukan.*
