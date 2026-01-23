---
term: Bech32 ve bech32m
definition: SegWit adresleri (bc1 ile başlayan) için kodlama formatları, Legacy adreslerine kıyasla daha iyi hata tespiti ve gelişmiş okunabilirlik sunar.
---

bech32` ve `Bech32m` bitcoin almak için kullanılan iki Address kodlama biçimidir. Biraz değiştirilmiş 32 tabanına dayanmaktadırlar. BCH (*Bose-Chaudhuri-Hocquenghem*) adı verilen bir hata düzeltme algoritmasına dayalı bir sağlama toplamı içerirler. Base58check` ile kodlanan eski adreslerle karşılaştırıldığında, `Bech32` ve `Bech32m` adresleri daha verimli bir sağlama toplamına sahiptir ve yazım hatalarının tespit edilmesine ve potansiyel olarak otomatik olarak düzeltilmesine olanak tanır. Formatları ayrıca sadece küçük harf karakterleri ile daha iyi okunabilirlik sunar. İşte 10 tabanından bu format için toplama matrisi:


| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

Bech32 ve Bech32m, SegWit adreslerini temsil etmek için kullanılan kodlama formatlarıdır. Bech32, 2017 yılında BIP173 tarafından tanıtılan bir Address kodlama biçimidir. Yazım hatalarını en aza indirmek ve okumayı kolaylaştırmak için sayılardan ve küçük harflerden oluşan belirli bir karakter kümesi kullanır. Bech32 adresleri genellikle SegWit'e özgü olduklarını belirtmek için `bc1` ile başlar. Bu format yalnızca SegWit V0 adreslerinde, P2WPKH (Pay to Witness Public Key Hash) ve P2WSH (Pay to Witness Script Hash) komut dosyalarında kullanılır. Ancak, Bech32 formatına özgü küçük, beklenmedik bir kusur vardır. Address'in son karakteri `p` olduğunda, hemen öncesine herhangi bir sayıda `q` karakteri eklemek veya çıkarmak sağlama toplamını geçersiz kılmaz. Bu, SegWit V0 adreslerinin (BIP173) mevcut kullanımlarını, tanımlanmış iki uzunlukla sınırlandırılmaları nedeniyle etkilemez. Ancak, bu durum Bech32 kodlamasının gelecekteki kullanımlarını etkileyebilir. Bech32m formatı basitçe bu hatanın düzeltildiği bir Bech32 formatıdır. BIP350 ile 2020 yılında tanıtılmıştır. Bech32m adresleri de `bc1` ile başlar, ancak özellikle SegWit V1 (Taproot) ve sonraki sürümlerle, P2TR (Pay to Taproot) komut dosyasıyla uyumlu olacak şekilde tasarlanmıştır.