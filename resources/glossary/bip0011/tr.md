---
term: BIP0011
definition: Bitcoin'de günümüzde bare-multisig veya P2MS olarak bilinen M-of-N çoklu imza işlemlerini tanıtan standart.
---

Gavin Andresen tarafından Mart 2012'de tanıtılan ve Bitcoin üzerinde çoklu imza işlemleri oluşturmak için standart bir yöntem öneren BIP. Bu öneri, bir işlemi doğrulamak için birden fazla imza gerektirerek bitcoinlerin güvenliğini artırmayı amaçlamaktadır. BIP11, "M-of-N Multisig" olarak adlandırılan yeni bir komut dosyası türü sunar; burada `M`, `N` potansiyel açık anahtar arasından gerekli minimum imza sayısını temsil eder. Bu standart, Bitcoin'de zaten mevcut olan ancak daha önce düğümlerin standardizasyon kurallarıyla uyumlu olmayan `OP_CHECKMULTISIG` işlem kodunu kullanır. Bu tür bir komut dosyası artık gerçek Multisig cüzdanları için yaygın olarak kullanılmasa da, P2SH veya P2WSH'yi tercih etse de, kullanımı mümkün olmaya devam etmektedir. Özellikle Stamps gibi meta-protokollerde kullanılmaktadır. Bununla birlikte, düğümler `permitbaremultisig=0` parametresiyle bu P2MS işlemlerini aktarmamayı seçebilir.


> ► *Günümüzde bu standart "bare-Multisig" veya "P2MS" olarak bilinmektedir*