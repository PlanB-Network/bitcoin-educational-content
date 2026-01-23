---
term: BIP0118
definition: İmzaların işlemler arasında yeniden kullanılmasına olanak tanıyan yeni SigHash Flag'lerini sunan ANYPREVOUT teklifi, Eltoo için kullanışlıdır.
---

Bitcoin'in geliştirilmesine yönelik öneri, iki yeni SigHash Bayrak değiştiricisinin tanıtılmasını amaçlamaktadır: `SIGHASH_ANYPREVOUT` ve `SIGHASH_ANYPREVOUTANYSCRIPT`. Bu özellikler, özellikle akıllı sözleşmeler ve Lightning Network gibi bindirme çözümleri açısından Bitcoin işlemlerinin yeteneklerini genişletmektedir. BIP118 özellikle Eltoo kullanımını mümkün kılacaktır. SIGHASH_ANYPREVOUT`un ana avantajı, imzaların birden fazla işlemde yeniden kullanılmasına izin vermektir, bu da daha fazla esneklik sunar. Özellikle, bu SigHash'ler işlemin girdilerinin hiçbirini kapsamayan bir imzaya izin verir.