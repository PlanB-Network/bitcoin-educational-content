---
term: Dandelion
definition: İşlemlerin kökenini önce bir gövde sonra bir tüy yayılım aşamasıyla bulanıklaştıran gizlilik protokolü.
---

Anonimleştirmeye karşı koymak için Bitcoin ağında işlem yönlendirmesinin gizliliğini iyileştirmeyi amaçlayan bir öneri. Bitcoin'in standart işleyişinde işlemler anında birden fazla düğüme yayınlanır. Bu olgu, gözlemcilerin normalde anonim olan işlemleri IP adresleriyle ilişkilendirmesine potansiyel olarak izin verebilir. BIP156'nın amacı bu sorunu Address yapmaktır. Bunu yapmak için, genel yayılımdan önce anonimliği korumak için yayın sürecine ek bir aşama getirmektedir. Bu nedenle Dandelion, "fluff" aşamasında tüm ağa yayınlanmadan önce işlemin rastgele bir düğüm yolu üzerinden gönderildiği bir "stem" aşaması kullanır. Kök ve tüy, işlemin ağ boyunca yayılma davranışına atıfta bulunur ve bir karahindiba şeklini andırır. Bu yönlendirme yöntemi, kaynak düğüme geri giden izi gizleyerek bir işlemin ağ üzerinden kaynağına kadar izlenmesini zorlaştırır.


