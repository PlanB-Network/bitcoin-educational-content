---
term: SIGHASH_ANYPREVOUT
definition: İmzanın belirli bir UTXO'ya bağlanmamasını sağlayan SigHash teklifi.
---

Bitcoin'de BIP118 ile tanıtılan yeni bir SigHash Bayrağı değiştiricisinin uygulanması için öneri. sIGHASH_ANYPREVOUT`, özellikle Lightning Network'daki ödeme kanalları ve Eltoo güncellemesi gibi gelişmiş uygulamalar için işlem yönetiminde daha fazla esneklik sağlar. SIGHASH_ANYPREVOUT` imzanın herhangi bir önceki UTXO`ye (*A Any Previous Output*) bağlı olmamasını sağlar. SIGHASH_ALL` ile birlikte kullanıldığında, bir işlemin tüm çıktılarının imzalanmasına izin verir, ancak girdilerin hiçbirini imzalamaz. Bu, belirtilen belirli koşullar karşılandığı sürece imzanın farklı işlemler için yeniden kullanılmasını sağlayacaktır.


> ► *Bu SigHash değiştiricisi SIGHASH_ANYPREVOUT, ilk olarak Joseph Poon tarafından 2016 yılında Lightning Network.* kavramını geliştirmek için önerilen SIGHASH_NOINPUT fikrinden türetilmiştir