---
term: PSEUDO-RANDOM
---

Bu sıfat, deterministik bir sürecin sonucu olmasına rağmen, ideal bir gerçekten rastgele dizinin özelliklerine yakın özellikler gösteren bir sayı dizisini tanımlamak için kullanılır. İdeal rastgelelik kavramı, birbirini izleyen Elements'lar arasında tam bir öngörülebilirlik ve korelasyon yokluğu anlamına gelir. Bir sözde rastgele sayı, deterministik bir algoritma tarafından üretilir ve bu nedenle, teorik olarak, üretecin başlangıç durumu biliniyorsa tamamen öngörülebilirdir.


Sözde rasgele sayı üreteci (PRNG) bu tür sayıları üretmek için kullanılan bir algoritmadır. Genellikle bir başlangıç değerinden veya "seed "ten başlar ve ardından sayı dizisini üretmek için bir dizi matematiksel dönüşüm uygular. Bu belirlenebilirlik nedeniyle, başlangıçtaki seed'ün gizli kalması kriptografik güvenlik açısından önemlidir. Sözde rastgele diziler, birçok uygulama için yeterli olan görünüşte rastgele davranış sergiledikleri için kriptografi de dahil olmak üzere çeşitli alanlarda yaygın olarak kullanılmaktadır. Bir PRNG'nin kalitesinin değerlendirilmesi, çıktısının dağılım, korelasyonlar ve diğer istatistiksel özellikler açısından gerçek rastgeleliğe ne ölçüde yaklaştığına dayanır. Bitcoin bağlamında, sözde rastgele sayılar özel anahtarlar üretmek için veya deterministik ve hiyerarşik cüzdanlar için generate a seed için kullanılır.