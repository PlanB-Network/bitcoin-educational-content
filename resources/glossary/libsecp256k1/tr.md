---
term: LIBSECP256K1
definition: Bitcoin tarafından kullanılan secp256k1 eliptik eğrisi üzerindeki imzalar ve işlemler için kriptografik C kütüphanesi.
---

Secp256k1 eliptik eğrisi üzerinde dijital imzalar ve diğer kriptografik ilkeller için yüksek performanslı, yüksek güvenlikli C kütüphanesi. Bu eğri Bitcoin dışında hiçbir zaman yaygın olarak kullanılmadığından (sıklıkla tercih edilen `secp256r1` eğrisinin aksine), bu kütüphane kullanımı için en kapsamlı referans olmayı amaçlamaktadır. Libsecp256k1'in geliştirilmesi öncelikle Bitcoin'ın ihtiyaçlarına yöneliktir ve diğer uygulamalar için tasarlanan özellikler daha az test edilmiş veya doğrulanmış olabilir. Bu kütüphanenin uygun kullanımı, Bitcoin dışındaki uygulamaların özel amaçlarına uygun olmasını sağlamak için dikkatli bir dikkat gerektirir.


Libsecp256k1 kütüphanesi, aşağıdakiler de dahil olmak üzere çeşitli özellikler sunar:




- ECDSA-secp256k1 imzası ve doğrulaması ve kriptografik anahtar üretimi ;
- Gizli ve açık anahtarlar üzerinde toplama ve çarpma işlemleri ;
- Gizli anahtarların, açık anahtarların ve imzaların serileştirilmesi ve analizi;
- Sabit bellek erişimi ile sabit zamanlı açık anahtar imzalama ve oluşturma;
- Ve bir dizi başka kriptografik ilkel.