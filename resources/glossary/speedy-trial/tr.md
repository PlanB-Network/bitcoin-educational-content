---
term: Speedy trial
definition: Taproot için kullanılan, azaltılmış gecikmeli hızlı soft fork etkinleştirme yöntemi.
---

Bir Soft Fork'ı etkinleştirme yöntemi ilk olarak 2021'in başlarında David A. Harding tarafından Russell O'Connor'ın bir fikrine dayanarak Taproot için kavramsallaştırılmıştır. Prensibi, BIP8 yöntemini `LOT` parametresini `false` olarak ayarlayarak kullanmak ve aktivasyon süresini sadece 3 aya indirmektir. Bu kısaltılmış oylama süresi, Miner onayının hızlı bir şekilde doğrulanmasını sağlar. Dönemlerden birinde gerekli onay eşiğine ulaşılırsa, Soft Fork kilitlenir. Birkaç ay sonra etkinleştirilecek ve böylece madencilere yazılımlarını güncellemeleri için gerekli zaman tanınacaktır.


Bununla birlikte, Bitcoin topluluğu içinde geniş bir fikir birliği sağlayan bu yöntemin Taproot için başarısı, tüm güncellemeler için etkinliğini garanti etmez. Speedy Trial yöntemi daha hızlı aktivasyona olanak tanısa da, bazı geliştiriciler bu yöntemin gelecekteki kullanımına ilişkin endişelerini dile getirmektedir. Bu yöntemin, Soft protokolünün istikrarını ve güvenliğini tehdit edebilecek çok hızlı bir Bitcoin çatallanmasına yol açabileceğinden korkmaktadırlar. LOT=true` parametresine sahip BIP8 ile karşılaştırıldığında, Speedy Trial yöntemi madenciler için çok daha az tehdit oluşturmaktadır. Otomatik olarak hiçbir UASF planlanmamıştır. Bu aktivasyon yöntemi henüz bir BIP içinde resmileştirilmemiştir.


