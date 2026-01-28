---
term: İşlem ücretleri
definition: Bir işlemi bir bloğa dahil ettikleri için madencilere verilen, girişler ve çıkışlar arasındaki fark olarak hesaplanan miktar.
---

İşlem ücretleri, madencilerin Proof of Work mekanizmasına katılımlarını telafi etmeyi amaçlayan bir tutarı temsil eder. Bu ücretler madencileri oluşturdukları bloklara işlemleri dahil etmeye teşvik eder. Bir işlemdeki toplam girdi miktarı ile toplam çıktı miktarı arasındaki farktan kaynaklanırlar:


```text
fees = inputs - outputs
```


Bunlar `Sats/vBytes` olarak ifade edilir, yani ücretler gönderilen bitcoin miktarına değil, işlemin ağırlığına bağlıdır. Bir işlemin göndericisi tarafından serbestçe seçilirler ve bir açık artırma mekanizması aracılığıyla bir bloğa dahil edilme hızını belirlerler. Örneğin, diyelim ki `100,000 Sats` girdisi, `40,000 Sats` çıktısı ve `58,500 Sats` başka bir çıktısı olan bir işlem yaptım. Çıktıların toplamı `98,500 Sats`tür. Bu işleme tahsis edilen ücretler `1,500 Sats`tür. İşlemimi içeren Miner, çıktılarımda geri kazanmadığım `1.500 Sats` için Exchange`deki Coinbase Transaction`lerinde `1.500 Sats` oluşturabilir.


Büyüklüklerine göre daha yüksek ücrete sahip işlemler madenciler tarafından öncelikli olarak değerlendirilir ve bu da onay sürecini hızlandırabilir. Bunun tersine, düşük ücretli işlemler yoğunluğun yüksek olduğu dönemlerde gecikebilir. Bitcoin işlem ücretlerinin, madenciler için ek bir teşvik olan blok sübvansiyonundan farklı olduğunu belirtmek gerekir. Block reward, her kazılan blokla (blok sübvansiyonu) yaratılan yeni bitcoinlerin yanı sıra toplanan işlem ücretlerinden oluşur. Blok sübvansiyonu, toplam Supply bitcoin limiti nedeniyle zaman içinde azalırken, işlem ücretleri madencileri katılmaya teşvik etmede önemli bir rol oynamaya devam edecektir.


Protokol düzeyinde, kullanıcıların bir bloğa herhangi bir ücret içermeyen işlemler dahil etmesini engelleyen hiçbir şey yoktur. Gerçekte, bu tür ücret içermeyen işlemler istisnaidir. Varsayılan olarak, Bitcoin düğümleri `1 sat/vByte`dan daha düşük ücrete sahip işlemleri aktarmaz. Bazı ücret içermeyen işlemler geçtiyse, bunun nedeni bunların düğüm ağını dolaşmadan doğrudan kazanan Miner tarafından entegre edilmiş olmasıdır. Örneğin, aşağıdaki işlem hiçbir ücret içermez:


```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```


Bu özel örnekte, F2Pool Mining pool'un yöneticisi tarafından başlatılan bir işlemdi. Normal bir kullanıcı olarak, mevcut alt limit bu nedenle `1 sat/vByte`dır.

Ayrıca temizleme sınırlarını da göz önünde bulundurmak gerekir. Yüksek tıkanıklık dönemlerinde, düğümlerin mempool'ları, kendilerine tahsis edilen RAM sınırına uymak için bekleyen işlemlerini belirli bir eşiğin altında temizler. Bu sınır kullanıcı tarafından serbestçe seçilir, ancak çoğu Bitcoin core'in varsayılan değerini 300 MB olarak bırakır. Bu değer `Bitcoin.conf` dosyasında `maxmempool` parametresi ile değiştirilebilir.

