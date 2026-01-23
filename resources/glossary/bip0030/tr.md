---
term: BIP0030
definition: İki işlemin aynı kimliğe sahip olabildiği bir kusuru gideren ve mükerrer işlem tanımlayıcılarını (TXID) yasaklayan soft fork.
---

Mükerrer işlem tanımlayıcıları sorununu çözmek için 15 Mart 2012 tarihinde uygulamaya konulan Soft Fork'i içeren iyileştirme önerisi. BIP30'dan önce, Blockchain'da aynı işlem tanımlayıcısına (txid) sahip iki farklı işlemin olması teknik olarak mümkündü. Bu durum coinbase işlemleri için özellikle iki kez gerçekleşmiştir: 91.880 numaralı bloktaki işlem 91.722 numaralı bloktaki coinbase ile aynı txid'ye sahiptir ve 91.842 numaralı bloktaki işlem 91.812 numaralı bloktaki coinbase ile aynı txid'ye sahiptir. BIP30 bu kusuru yeni ve basit bir kural getirerek çözmüştür: orijinal işlem tamamen harcanmadıkça (yani tüm çıktıları kullanılmadıkça) hiçbir yeni işlem daha önce kaydedilmiş bir işlemle aynı txid'ye sahip olamaz. Bu Soft Fork, bayrak günü yöntemi kullanılarak etkinleştirilmiştir. Dolayısıyla, ilk UASF'lerden biridir.