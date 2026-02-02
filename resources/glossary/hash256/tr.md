---
term: HASH256
definition: Çeşitli Bitcoin uygulamalarında kullanılan, SHA256'yı ardışık iki kez uygulayan fonksiyon.
---

Bitcoin üzerinde çeşitli uygulamalar için kullanılan kriptografik işlev. SHA256 işlevinin giriş verilerine iki kez uygulanmasını içerir. Mesaj SHA256'dan bir kez geçirilir ve bu işlemin sonucu SHA256'dan ikinci bir geçiş için girdi olarak kullanılır. Dolayısıyla bu işlevin çıktısı 256 bittir.


$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$