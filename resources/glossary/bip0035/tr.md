---
term: BIP0035
definition: Düğümlerin mempool bilgilerini (bekleyen işlemler) ağdaki diğer katılımcılarla paylaşmasına olanak tanıyan teklif.
---

Bir Bitcoin düğümünün Mempool hakkında, yani onay bekleyen işlemler hakkında bilgi açmasına izin veren öneri. Bu sayede, diğer katılımcılar bir düğüme belirli bir mesaj göndererek onaylanmamış işlemler hakkında gerçek zamanlı veri alabilirler. BIP35'in benimsenmesinden önce, düğümler yalnızca halihazırda onaylanmış işlemlerle ilgili bilgilere erişebiliyordu. Bu iyileştirme, SPV cüzdanlarına onaylanmamış işlemler hakkında bilgi alma olanağı sunmakta, bir Miner'nin yeniden başlatma sırasında yüksek ücretli işlemleri kaçırmasını önlemekte ve Mempool bilgilerinin harici hizmetler tarafından analiz edilmesini kolaylaştırmaktadır.