---
term: HTLC
---

"*Hashed Timelock Contract*" anlamına gelir. Bu, çoğunlukla Lightning'de kullanılan bir Smart contract mekanizmasıdır. Bazen atomik takaslarda da bulunur. Temel olarak, HTLC bir para transferini bir sırrın açığa çıkmasına bağlı hale getirir ve ayrıca başarısız bir işlem durumunda gönderenin parasını korumak için bir zaman koşulu içerir.


Lightning'de HTLC, doğrudan bir kanalınız olmayan bir düğüme, yol boyunca güvene ihtiyaç duymadan birkaç kanaldan geçerek bitcoin göndermenize olanak tanır. Her bir düğüm arasındaki ödeme, bir ön imajın (hash edildiğinde üzerinde anlaşılan bir değere karşılık gelen sır) sağlanması koşuluna bağlıdır. Nihai alıcı bu ön görüntüyü sağlarsa, fonları talep edebilir ve zorunlu olarak her bir ara düğümün fonları kademeli olarak talep etmesini sağlar.


Örneğin, Alice David'e 1 BTC göndermek istiyorsa, ancak onunla doğrudan bir kanalı yoksa, birbirleriyle ödeme kanalları olan Bob ve Carol üzerinden gitmek zorundadır. İşlem şu şekilde gerçekleşir:




- David Alice'e bir Invoice Lightning sunar. Bu, sadece David'in bildiği gizli bir $s$'nin (ön görüntü) Hash $h$'sini içerir. Yani elimizde: $h = \text{Hash}(s)$ ;
- Alice, Bob ile bir HTLC oluşturur ve Bob'ün kendisine Hash $h$ 'ye karşılık gelen bir gizli $s$ (ön görüntü) sağlaması koşuluyla kendisine 1 BTC göndermeyi teklif eder;
- Bob, Carol ile bir HTLC yaratır ve Carol aynı $s$ sırrını vermesi koşuluyla kendisine 1 BTC göndermeyi teklif eder;
- Carol, $s$ ön görüntüsünü ortaya çıkarması halinde 1 BTC daha teklif eden David ile bir HTLC oluşturur;
- David 1 BTC almak için $s$'yi (sadece kendisinin bildiği) Carol'a açıklar. Carol artık BTC'yi Bob'den almak için $s$'yi kullanabilir. Artık $s$'yi bilen Bob de Alice ile aynı şeyi yapar.


Son olarak, Alice, Bob ve Carol aracılığıyla David'e 1 BTC gönderdi (ikincisi için tarafsız bir eylem), her şey HTLC'lerin koşulları tarafından kademeli olarak güvence altına alındığı için kimsenin birbirine güvenmesine gerek kalmadı.


HTLC'ler böylece "atomik" takasları mümkün kılar: transfer ya tamamen başarılı olur ya da başarısız olur ve fonlar iade edilir. Bu, güvene ihtiyaç duymayan birden fazla katılımcı arasında bile işlemlerin güvenliğini garanti eder.