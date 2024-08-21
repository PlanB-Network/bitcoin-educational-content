---
term: ANONSETS (SET ANONIMITAS)
---

Anonsets berfungsi sebagai indikator untuk menilai tingkat privasi dari UTXO tertentu. Lebih spesifik lagi, mereka mengukur jumlah UTXO yang tidak dapat dibedakan dalam set yang mencakup koin yang sedang diteliti. Karena diperlukan sekelompok UTXO yang identik, anonsets umumnya dihitung dalam siklus coinjoins. Mereka memungkinkan, jika sesuai, untuk menilai kualitas dari coinjoins tersebut. Anonset yang besar berarti tingkat anonimitas yang meningkat, karena menjadi sulit untuk membedakan UTXO spesifik dalam set tersebut. Ada dua jenis anonsets:
* Set anonimitas prospektif;
* Set anonimitas retrospektif.

Yang pertama menunjukkan ukuran kelompok di mana UTXO yang diteliti tersembunyi, dengan mengetahui UTXO pada input. Indikator ini memungkinkan pengukuran ketahanan privasi koin terhadap analisis dari masa lalu ke masa kini (input ke output). Dalam bahasa Inggris, nama indikator ini adalah “*forward anonset*,” atau “*forward-looking metrics*.”

![](../../dictionnaire/assets/39.png)

Yang kedua menunjukkan jumlah sumber yang mungkin untuk sebuah koin tertentu, dengan mengetahui UTXO pada output. Indikator ini memungkinkan pengukuran ketahanan privasi koin terhadap analisis dari masa kini ke masa lalu (output ke input). Dalam bahasa Inggris, nama indikator ini adalah “*backward anonset*,” atau “*backward-looking metrics*.”

![](../../dictionnaire/assets/40.png)

> ► *Dalam bahasa Prancis, umumnya diterima untuk menggunakan istilah “anonset.” Namun, ini dapat diterjemahkan sebagai “ensemble d'anonymat” atau “potentiel d'anonymat.” Baik dalam bahasa Inggris maupun Prancis, istilah “score” juga terkadang digunakan untuk merujuk pada anonsets (prospective score dan retrospective score).*