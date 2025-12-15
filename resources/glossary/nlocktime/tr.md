---
term: NLOCKTIME
---

İşlemlerde, işlemin geçerli bir bloğa eklenemeyeceği zamana dayalı bir koşul belirleyen gömülü bir alan. Bu parametre, işlemin geçerli sayılması için koşul olarak tam bir zamanın (Unix Timestamp) veya belirli bir blok sayısının belirtilmesine olanak tanır. Bu nedenle, mutlak bir zaman kilididir (göreceli değil). NLockTime` tüm işlemi etkiler ve zaman doğrulamasını etkin bir şekilde sağlarken, `OP_CHECKLOCKTIMEVERIFY` işlem kodu yalnızca yığının en üst değerini `nLockTime` değeriyle karşılaştırmaya izin verir.