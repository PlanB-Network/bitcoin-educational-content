---
term: HASH160
definition: Bitcoin adreslerini oluşturmak için kullanılan, önce SHA256 ve ardından RIPEMD160'ı birleştiren fonksiyon.
---

Bitcoin'da, özellikle Eski ve SegWit v0 alıcı adreslerini oluşturmak için kullanılan kriptografik işlev. Girdi üzerinde art arda çalıştırılan iki Hash işlevini birleştirir: önce SHA256, sonra RIPEMD160. Bu nedenle bu işlevin çıktısı 160 bittir.


$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$