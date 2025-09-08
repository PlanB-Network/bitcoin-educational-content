---
term: redeemscript
---

Bir P2SH çıktısıyla ilişkili fonların kilidini açmak için girdilerin karşılaması gereken belirli koşulları tanımlayan bir komut dosyası. Bir P2SH UTXO'te, `scriptPubKey` `redeemscript`in Hash'ünü içerir. Bir işlem bu UTXO`i girdi olarak harcamak istediğinde, `scriptPubKey`de bulunan Hash ile eşleşen açık `redeemscript`i sağlamalıdır. Bu nedenle `redeemscript`, imzalar veya açık anahtarlar gibi komut dosyasının koşullarını karşılamak için gerekli diğer Elements ile birlikte girdinin `scriptSig` bölümünde verilir. Bu kapsüllenmiş yapı, bitcoinler gerçekten harcanana kadar harcama koşullarının ayrıntılarının gizli kalmasını sağlar. Özellikle Eski P2SH çoklu imza cüzdanları için kullanılır.