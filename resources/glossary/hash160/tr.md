---
term: HASH160
---

Bitcoin'da, özellikle Eski ve SegWit v0 alıcı adreslerini oluşturmak için kullanılan kriptografik işlev. Girdi üzerinde art arda çalıştırılan iki Hash işlevini birleştirir: önce SHA256, sonra RIPEMD160. Bu nedenle bu işlevin çıktısı 160 bittir.


$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$