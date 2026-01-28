---
term: Mempool
definition: Bir bloğa dahil edilmeyi bekleyen işlemlerin her bir düğüm tarafından saklandığı alan.
---

"Bellek" ve "havuz" terimlerinin kısaltmasıdır. Bu, bir bloğa dahil edilmeyi bekleyen Bitcoin işlemlerinin bir arada gruplandırıldığı sanal bir alanı ifade eder. Bir işlem oluşturulduğunda ve Bitcoin ağında yayınlandığında, ilk olarak ağın düğümleri tarafından doğrulanır. Geçerli kabul edilirse, daha sonra her düğümün Mempool'sine yerleştirilir ve burada bir bloğa dahil edilmek üzere bir Miner tarafından seçilene kadar kalır.


Bitcoin ağındaki her bir düğümün kendi Mempool'sını tuttuğunu ve bu nedenle herhangi bir zamanda farklı düğümler arasında Mempool'nın içeriğinde farklılıklar olabileceğini unutmamak önemlidir. Özellikle, her düğümün `Bitcoin.conf` dosyasındaki `maxmempool` parametresi, operatörlerin düğümlerinin Mempool'da bekleyen işlemleri depolamak için kullanacağı RAM (rastgele erişim belleği) miktarını kontrol etmelerine olanak tanır. Düğüm operatörleri Mempool'nın boyutunu sınırlandırarak sistemlerinde çok fazla kaynak tüketmesini önleyebilirler. Bu parametre megabayt (MB) cinsinden belirtilir. Bitcoin core için bugüne kadarki varsayılan değer 300 MB'dir.


Mempool'de bulunan işlemler geçicidir. Bir bloğa dahil edilene kadar ve belirli sayıda onaydan sonra değişmez olarak kabul edilmemelidirler. Bunlar genellikle değiştirilebilir veya temizlenebilir.