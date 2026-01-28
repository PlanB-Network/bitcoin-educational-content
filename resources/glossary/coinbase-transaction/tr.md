---
term: Coinbase işlemi
definition: Blok ödülünü ve sübvansiyonu almak için madenci tarafından oluşturulan bloğun ilk işlemi.
---

Coinbase Transaction, Bitcoin Blockchain'ün her bloğunda yer alan özel ve benzersiz bir işlemdir. Bir bloğun ilk işlemini temsil eder ve Proof of Work'i (*Proof-of-Work*) doğrulayan, yani hedeften küçük veya hedefe eşit bir başlığı başarıyla bulan Miner tarafından oluşturulur.


Coinbase Transaction öncelikle iki amaca hizmet eder: Block reward'i Miner'e vermek ve dolaşımdaki para Supply'a yeni bitcoin birimleri eklemek. Madencilerin Proof of Work'ye katılmaları için ekonomik teşvik olan Block reward, blokta yer alan işlemler için birikmiş ücretleri ve yeni yaratılan bitcoinlerin belirli bir miktarını ex-nihilo (blok sübvansiyonu) içerir. Başlangıçta 2009 yılında blok başına 50 bitcoin olarak belirlenen bu miktar, "Halving" adı verilen bir etkinlik sırasında her 210.000 blokta (yaklaşık 4 yılda bir) yarıya indirilmektedir


Coinbase Transaction normal işlemlerden birkaç yönden farklıdır. İlk olarak, bir girdisi yoktur, yani mevcut hiçbir işlem çıktısı (UTXO) onun tarafından tüketilmez. Daha sonra, Coinbase Transaction için imza komut dosyası (`scriptSig`) tipik olarak özel mesajlar veya Mining yazılım sürümü bilgileri gibi ek verilerin dahil edilmesine izin veren rastgele bir alan içerir. Son olarak, Coinbase Transaction tarafından üretilen bitcoinler, zincirin yeniden düzenlenmesi durumunda var olmayan bitcoinlerin potansiyel olarak harcanmasını önlemek için harcanmadan önce 100 blokluk (101 onay) bir vade süresine tabidir.


