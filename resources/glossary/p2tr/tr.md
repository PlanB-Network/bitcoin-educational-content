---
term: P2TR
definition: Bir genel anahtar veya Merkle betikleri aracılığıyla harcamaya izin veren Taproot betiği, bc1p adresleri.
---

P2TR, UTXO (Harcanmamış İşlem Çıktısı) üzerinde harcama koşulları oluşturmak için kullanılan standart bir senaryo modeli olan *Taproot'e Öde* anlamına gelir. Kasım 2021'de Taproot'in uygulanmasıyla birlikte tanıtılmıştır. P2TR, kriptografik anahtarları bir araya getirmek için Schnorr protokolünün yanı sıra MAST (*Merkelized Alternative Script Tree*) olarak bilinen alternatif senaryolar için Merkle ağaçlarını kullanır. Harcama koşullarının kamuya açık olduğu geleneksel işlemlerin aksine (bazen alım sırasında, bazen de harcama sırasında), P2TR karmaşık senaryoların tek bir görünür açık anahtarın arkasına gizlenmesine olanak tanır.


Teknik olarak, bir P2TR betiği bitcoinleri $K$ olarak gösterilen benzersiz bir Schnorr açık anahtarına kilitler. Ancak bu $K$ anahtarı aslında $P$ açık anahtarı ile $M$ açık anahtarının bir toplamıdır ve ikincisi `scriptPubKey` listesinin Merkle Root'ünden hesaplanır. Bir P2TR betiği ile kilitlenen bitcoinler iki farklı şekilde harcanabilir: ya açık anahtar $P$ için bir imza yayınlayarak ya da Merkle Tree'te bulunan betiklerden birini yerine getirerek. İlk seçenek "*anahtar yolu*" ve ikincisi "*komut dosyası yolu*" olarak adlandırılır.


Böylece P2TR, kullanıcıların bitcoinleri bir açık anahtara ya da seçtikleri birden fazla komut dosyasına göndermelerine olanak tanır. Bu betiğin bir diğer avantajı da, bir P2TR çıktısını harcamanın birden fazla yolu olmasına rağmen, harcama sırasında yalnızca kullanılanın açıklanması gerekmesi ve kullanılmayan alternatiflerin gizli kalmasına izin vermesidir. P2TR bir versiyon 1 SegWit çıktısıdır, yani P2TR girdileri için imzalar `scriptSig`de değil, bir işlemin tanığında saklanır. P2TR adresleri bir `Bech32m` kodlaması kullanır ve `bc1p` ile başlar.