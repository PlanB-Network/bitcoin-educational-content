---
term: ÇIKIŞ NOKTASI
---

Harcanmamış bir işlem çıktısına (UTXO) benzersiz bir referans. İki Elements'dan oluşur:


- `txid`: çıktıyı oluşturan işlemin tanımlayıcısı;
- `vout`: işlemdeki çıktının indeksi.


Bu iki Elements kombinasyonu tam olarak bir UTXO'ü tanımlar. Örneğin, bir işlem `abc...123` şeklinde bir `txid`e sahipse ve çıkış indeksi `0` ise, çıkış noktası şu şekilde belirtilecektir:


```text
abc...123:0
```


Çıkış noktası, hangi UTXO'nın harcandığını belirtmek için yeni bir işlemin girdilerinde (`vin`) kullanılır.


> ► *"Dış nokta" terimi genellikle "UTXO" ile eşanlamlı olarak kullanılır