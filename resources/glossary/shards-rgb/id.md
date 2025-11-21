---
term: SHARDS (RGB)
---

Dalam konteks protokol RGB, sebuah _Shard_ mewakili sebuah cabang yang berbeda dalam _acyclic directed graph_ (DAG) yang menelusuri sejarah transisi keadaan _Contract_. Hal ini merupakan subset yang koheren dari set transisi, yang sesuai, misalnya, dengan urutan operasi yang diperlukan untuk membuktikan validitas aset tertentu sejak _Genesis_. Mekanisme ini memungkinkan isolasi segmen tertentu dari keseluruhan riwayat, untuk memfasilitasi verifikasi dari sisi klien.
