---
term: P2MS
definition: Eşik değerde imza gerektiren, bitcoinleri birden fazla genel anahtarla kilitleyen çoklu imza betiği.
---

P2MS'nin açılımı *Pay to Multisig* olup "birden fazla imzaya ödeme" anlamına gelmektedir. Bir UTXO üzerinde harcama koşulları oluşturmak için kullanılan standart bir komut dosyası modelidir. Birden fazla açık anahtara sahip bitcoinlerin kilitlenmesine olanak tanır. Bu bitcoinleri harcamak için, önceden tanımlanmış sayıda ilişkili özel anahtara sahip bir imza gereklidir. Örneğin, bir `P2MS 2/3`, `3` ilişkili gizli özel anahtara sahip `3` açık anahtar içerir. Bu P2MS betiği ile kilitlenen bitcoinleri harcamak için, `3` özel anahtardan en az `2` tanesine sahip bir imza gereklidir. Bu bir eşik güvenlik sistemidir.


Bu betik 2011 yılında Gavin Andresen tarafından ana Bitcoin istemcisinin bakımını devraldığında icat edilmiştir. Bugün, P2MS sadece bazı uygulamalar tarafından marjinal olarak kullanılmaktadır. Modern çoklu imzaların büyük çoğunluğu P2SH veya P2WSH gibi diğer betikleri kullanmaktadır. Bunlarla karşılaştırıldığında, P2MS son derece önemsizdir. İçerdiği açık anahtarlar işlemin alınmasıyla ortaya çıkar. P2MS kullanmak diğer çoklu imza betiklerine göre daha pahalıdır.


