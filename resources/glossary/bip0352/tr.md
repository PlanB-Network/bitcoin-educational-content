---
term: BIP0352
---

Josibake ve Ruben Somsen tarafından, Address yeniden kullanımı, etkileşimi ve farklı ödemeler arasında görünür bir On-Chain bağlantısı olmadan ödeme almak için statik Bitcoin adreslerini kullanma yöntemi olan Sessiz Ödemeleri tanıtan iyileştirme önerisi. Bu teknik, her işlem için yeni, kullanılmayan alıcı adresleri generate ihtiyacını ortadan kaldırır, böylece alıcının ödeyene yeni bir Address sağlaması gereken Bitcoin'teki olağan etkileşimlerden kaçınır.


Bu sistemde, ödeme yapan kişi alıcının açık anahtarını ve kendi özel anahtarını kullanarak her ödeme için yeni bir generate Address oluşturur. Yalnızca alıcı, kendi özel anahtarıyla bu Address'ye karşılık gelen özel anahtarı hesaplayabilir. Bir kriptografik anahtar Exchange algoritması olan ECDH (*Elliptic-Curve Diffie-Hellman*), daha sonra alıcı Address'yi ve özel anahtarı (yalnızca alıcı tarafında) türetmek için kullanılan ortak bir sır oluşturmak için kullanılır. Kendilerine yönelik Sessiz Ödemeleri belirlemek için alıcılar Blockchain'ü taramalı ve Sessiz Ödemeler kriterleriyle eşleşen her işlemi incelemelidir. Ödeme kanalını oluşturmak için bir bildirim işlemi kullanan BIP47'nin aksine, Sessiz Ödemeler bu adımı ortadan kaldırarak bir işlem tasarrufu sağlar. Bununla birlikte, alıcının ECDH uygulayarak kendisine yönelik olup olmadığını belirlemek için tüm potansiyel işlemleri taraması gerekir.