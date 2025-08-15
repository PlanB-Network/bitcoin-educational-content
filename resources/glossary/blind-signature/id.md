---
term: BLIND SIGNATURE

---
_Chaum Blind Signature_ adalah bentuk tanda tangan digital di mana pemberi tanda tangan tidak mengetahui isi pesan yang mereka tandatangani. Namun, tanda tangan tersebut nantinya dapat diverifikasi dengan pesan aslinya. Teknik ini dikembangkan oleh kriptografer David Chaum pada tahun 1983.

Pertimbangkan contoh sebuah perusahaan yang ingin melakukan autentikasi dokumen rahasia, seperti kontrak, tanpa mengungkapkan isinya. Perusahaan menerapkan proses penyembunyian yang secara kriptografis mengubah dokumen asli dengan reversibel. Dokumen yang telah dimodifikasi ini dikirim ke otoritas sertifikasi yang menerapkan _blind signature_ tanpa mengetahui konten yang mendasarinya. Setelah menerima dokumen dengan _blind signature_, perusahaan membuka penyamaran tanda tangan tersebut. Hasilnya adalah dokumen asli yang diautentikasi oleh tanda tangan pemilik, dan otoritas tidak pernah melihat konten aslinya.

Dengan demikian, tanda tangan buta Chaum memungkinkan sertifikasi keaslian dokumen tanpa mengetahui isinya, memastikan kerahasiaan data pengguna dan keaslian dokumen yang ditandatangani.

Dalam Bitcoin, protokol ini digunakan dalam sistem bank-bank Chaumian sebagai overlay (Cashu, Fedimint, dll.), tetapi terutama dalam protokol coinjoin Chaumian, untuk memastikan bahwa koordinator tidak dapat mengetahui hubungan input dan output.
