---
term: P2SH
---

P2SH, *Pay to Script Hash* anlamına gelmektedir. Bir UTXO üzerinde harcama koşulları oluşturmak için kullanılan standart bir komut dosyası modelidir. Harcama koşullarının önceden tanımlandığı P2PK ve P2PKH komut dosyalarının aksine P2SH, bir işlem komut dosyasına keyfi harcama koşullarının ve ek işlevlerin entegre edilmesine olanak tanır.


Teknik olarak, bir P2SH işleminde, `scriptPubKey` açık harcama koşulları yerine bir `redeemscript`ün kriptografik Hash'sını içerir. Bu Hash, bir `SHA256` Hash kullanılarak elde edilir. Bir P2SH Address'e bitcoin gönderirken, altta yatan `redeemscript` açığa çıkmaz. İşleme yalnızca Hash dahil edilir. P2SH adresleri `Base58Check` ile kodlanır ve `3` sayısı ile başlar. Alıcı aldığı bitcoinleri harcamak istediğinde, `scriptPubKey`de bulunan Hash ile eşleşen bir `redeemscript` ve bu `redeemscript`ün koşullarını yerine getirmek için gerekli verileri sağlamalıdır. Örneğin, bir P2SH çoklu imza komut dosyasında, komut dosyası birden fazla özel anahtardan imza gerektirebilir.


P2SH kullanımı, göndericinin ayrıntıları bilmeden rastgele komut dosyalarının oluşturulmasına izin verdiği için daha fazla esneklik sunar. P2SH 2012 yılında BIP16 ile tanıtılmıştır.