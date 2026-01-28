---
term: SPV düğümü (hafif düğüm)
definition: Yalnızca blok başlıklarını saklayarak ve Merkle kanıtlarını doğrulayarak işlemleri onaylayan hafif istemci.
---

Bazen "hafif düğüm" olarak da adlandırılan SPV (*Basit Ödeme Doğrulama*) düğümü, kullanıcıların tüm Blockchain'i saklamak zorunda kalmadan işlemleri doğrulamasına olanak tanıyan bir Bitcoin düğümünün hafif bir istemcisidir. Bunun yerine, bir SPV düğümü yalnızca blok başlıklarını depolar ve gerektiğinde tam düğümleri sorgulayarak belirli işlemler hakkında bilgi edinir. Bu doğrulama prensibi, bir kriptografik akümülatör (Merkle Tree) içinde organize edilen Bitcoin bloklarındaki işlemlerin yapısı ile mümkün olmaktadır.


Bu yaklaşım, cep telefonları gibi sınırlı kaynaklara sahip cihazlar için avantajlıdır. Bununla birlikte, SPV düğümleri bilginin kullanılabilirliği için tam düğümlere güvenir, bu da ek bir güven seviyesi ve sonuç olarak tam düğümlere kıyasla daha az güvenlik anlamına gelir. SPV düğümleri işlemleri otonom olarak doğrulayamaz, ancak Merkle kanıtlarına başvurarak bir işlemin bir bloğa dahil olup olmadığını doğrulayabilirler.