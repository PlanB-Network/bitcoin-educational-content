---
term: P2PK
definition: Bitcoinleri hashleme yapmadan doğrudan bir genel anahtara kilitleyen betik.
---

P2PK *Açık Anahtara Ödeme* anlamına gelir. Bir UTXO üzerinde harcama koşulları oluşturmak için Bitcoin üzerinde kullanılan standart bir komut dosyası modelidir. Bitcoinlerin bir Address yerine doğrudan bir açık anahtara kilitlenmesini sağlar.

Teknik olarak, P2PK komut dosyası bir açık anahtar ve fonların kilidini açmak için karşılık gelen bir dijital imza talep eden bir talimat içerir. Sahibi bitcoinleri harcamak istediğinde, ilişkili özel anahtarla üretilen bir imza sağlamalıdır. Bu imza ECDSA (*Eliptik Eğri Dijital İmza Algoritması*) kullanılarak doğrulanır. P2PK, Bitcoin'ün ilk sürümlerinde, özellikle de Satoshi Nakamoto tarafından sıklıkla kullanılmıştır. Bugün artık neredeyse hiç kullanılmamaktadır.