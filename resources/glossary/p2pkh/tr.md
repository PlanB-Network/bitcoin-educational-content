---
term: P2PKH
definition: Bitcoinleri bir genel anahtarın hash'ine kilitleyen betik, adresler 1 ile başlar.
---

P2PKH *Açık Anahtar Hash'e Ödeme* anlamına gelir. Bir UTXO üzerinde harcama koşulları oluşturmak için kullanılan standart bir komut dosyası modelidir. Bir açık anahtarın Hash'ünde, yani alıcı bir Address'da bitcoinlerin kilitlenmesine izin verir. Bu komut dosyası Eski standart ile ilişkilidir ve Bitcoin'in ilk sürümlerinde Satoshi Nakamoto tarafından tanıtılmıştır.


Açık anahtarın senaryoya açıkça dahil edildiği P2PK'dan farklı olarak, P2PKH açık anahtarın kriptografik parmak izini kullanır. Bu komut dosyası, açık anahtarın `SHA256` kısmının `RIPEMD160` Hash'ini içerir ve fonlara erişmek için alıcının bu Hash ile eşleşen bir açık anahtarın yanı sıra ilişkili özel anahtardan üretilen geçerli bir dijital imza sağlaması gerektiğini şart koşar. P2PKH adresleri `Base58Check` formatı kullanılarak kodlanır, bu da onlara bir sağlama toplamı kullanımı yoluyla tipografik hatalara karşı sağlamlık kazandırır. Bu adresler her zaman `1` sayısı ile başlar.