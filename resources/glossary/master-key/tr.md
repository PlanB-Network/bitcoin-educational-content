---
term: Ana anahtar
definition: Seed'den türetilen ve bir HD cüzdanındaki tüm anahtarlar için başlangıç noktası görevi gören özel anahtar.
---

HD (Hiyerarşik Deterministik) cüzdanlar bağlamında, ana özel anahtar Wallet'nin seed'ünden türetilen benzersiz bir özel anahtardır. Ana anahtarı elde etmek için `HMAC-SHA512` işlevi seed'e uygulanır ve anahtar olarak "*Bitcoin seed*" kelimeleri kullanılır. Bu işlemin sonucu 512 bitlik bir çıktı üretir; ilk 256 bit ana anahtarı, kalan 256 bit ise ana chain code'ı oluşturur. Ana anahtar ve ana chain code, HD Wallet'nin ağaç yapısındaki tüm alt özel ve açık anahtarların türetilmesi için başlangıç noktası görevi görür. Bu nedenle, ana özel anahtar türetme işleminin 0. derinliğindedir.


