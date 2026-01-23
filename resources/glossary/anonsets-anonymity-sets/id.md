---
term: Anonsets (anonymity sets)

definition: Indikator yang mengukur tingkat privasi UTXO dengan menghitung jumlah UTXO yang tidak dapat dibedakan dalam satu set, biasanya setelah coinjoin.
---
Anonsets berfungsi sebagai indikator untuk menilai tingkat privasi dari suatu UTXO tertentu. Secara lebih spesifik, anonsets mengukur jumlah UTXO yang tidak dapat dibedakan dalam himpunan yang mencakup koin yang sedang dikaji. Karena diperlukan sekumpulan UTXO yang identik, anonsets umumnya dihitung dalam satu siklus coinjoins. Hal ini memungkinkan, jika diperlukan, untuk menilai kualitas coinjoins. Anonset yang berukuran besar menunjukkan tingkat anonimitas yang lebih tinggi, karena menjadi sulit untuk membedakan satu UTXO tertentu di dalam himpunan tersebut.

Terdapat dua jenis anonset: forward anonset (forward-looking metrics); dan backward anonset (backward-looking metrics). Istilah "*score*" juga terkadang digunakan untuk merujuk pada anonset.

Yang pertama menunjukkan ukuran kelompok tempat UTXO keluaran yang diteliti bersembunyi, dengan mengetahui UTXO masukan. Indikator ini memungkinkan pengukuran ketahanan privasi koin terhadap analisis dari masa lalu ke masa kini (masukan ke keluaran). Yang kedua menunjukkan jumlah sumber yang mungkin untuk suatu koin tertentu, dengan mengetahui UTXO keluaran. Indikator ini memungkinkan pengukuran ketahanan privasi koin terhadap analisis dari masa kini ke masa lalu (keluaran ke masukan).










