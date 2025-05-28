---
term: ANONSET (HIMPUNAN ANONIMITAS)

---
_Anonset_ berfungsi sebagai indikator untuk menilai tingkat privasi dari UTXO tertentu. Mereka mengukur jumlah UTXO yang tidak dapat dibedakan di dalam himpunan yang mencakup koin yang sedang dianalisis. Karena melibatkan sekelompok UTXO yang identik, _anonset_ biasanya dihitung dalam siklus _Coinjoin_. _Anonset_ memungkinkan, jika diperlukan, untuk menilai efektivitas _Coinjoin_. _Anonset_ yang besar berarti tingkat anonimitas yang besar, karena sulit untuk membedakan UTXO tertentu di dalam himpunan. Ada dua jenis _anonset_:

- Himpunan anonimitas prospektif;
- Himpunan anonimitas retrospektif.

Himpunan anonimitas prospektif menunjukkan ukuran himpunan di mana UTXO yang dipelajari disembunyikan, dengan mengetahui UTXO pada input. Indikator ini memungkinkan untuk mengukur ketahanan privasi koin terhadap analisis dari masa lalu ke masa sekarang (input ke output). Dalam bahasa Inggris, nama indikator ini adalah "*forward anonset*," atau "*forward-looking metrics*."

![](../../dictionnaire/assets/39.webp)

Himpunan anonimitas retrospektif menunjukkan jumlah kemungkianan asal suatu UTXO, dengan mengetahui UTXO pada output. Indikator ini memungkinkan untuk mengukur ketahanan privasi koin terhadap analisis dari masa kini ke masa lalu (output ke input). Dalam bahasa Inggris, nama indikator ini adalah "*backward anonset*," atau "*backward-looking metrics*."

![](../../dictionnaire/assets/40.webp)

> ► *Dalam bahasa Inggris, istilah "score" juga terkadang digunakan untuk merujuk pada anonset ("_prospective score_" dan "_retrospective score_")*
