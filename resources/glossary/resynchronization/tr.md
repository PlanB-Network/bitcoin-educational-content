---
term: YENIDEN SENKRONIZASYON
---

Blockchain'ın aynı yükseklikteki rakip blokların varlığı nedeniyle yapısında bir değişikliğe uğradığı bir olguyu ifade eder. Bu, Blockchain'ın bir kısmı daha fazla miktarda birikmiş işe sahip başka bir zincirle değiştirildiğinde meydana gelir.


Bu yeniden senkronizasyonlar, farklı madencilerin neredeyse aynı anda yeni bloklar bulabildiği ve böylece Bitcoin ağını ikiye bölen Bitcoin'in doğal işleyişinin bir parçasıdır. Bu gibi durumlarda ağ geçici olarak rakip zincirlere bölünebilir. Sonunda, bu zincirlerden biri daha fazla iş biriktirdiğinde, diğer zincirler düğümler tarafından terk edilir ve blokları "eski bloklar" veya "yetim bloklar" olarak adlandırılır Bir zincirin diğeriyle değiştirildiği bu süreç yeniden senkronizasyondur.


![](../../dictionnaire/assets/9.webp)


Yeniden senkronizasyonların çeşitli sonuçları olabilir. İlk olarak, bir kullanıcı terk edildiği ortaya çıkan bir blokta bir işlemi onaylatmışsa, ancak bu işlem nihai olarak geçerli zincirde bulunmazsa, işlemi tekrar onaylanmamış hale gelir. Bu nedenle, bir işlemi gerçekten değişmez olarak kabul etmek için her zaman en az 6 onay beklemeniz önerilir. Derin 6 bloktan sonra, yeniden senkronizasyonlar o kadar düşük bir ihtimaldir ki, bir tanesinin gerçekleşme olasılığı neredeyse sıfır olarak kabul edilebilir.


Ayrıca, küresel sistem düzeyinde, yeniden senkronizasyonlar madencilerin hesaplama gücünün boşa harcanması anlamına gelir. Gerçekten de, bir bölünme meydana geldiğinde, bazı madenciler on chain `A`, diğerleri ise on chain `B` olacaktır. Eğer `B` zinciri bir yeniden senkronizasyon sırasında terk edilirse, madenciler tarafından bu zincir üzerinde kullanılan tüm hesaplama gücü tanım gereği boşa harcanmış olur. Bitcoin ağında çok fazla yeniden senkronizasyon varsa, ağın genel güvenliği bu nedenle azalır. Blok boyutunu artırmanın ya da her blok arasındaki aralığı (10 dakika) azaltmanın tehlikeli olmasının nedeni kısmen budur.


> ► *Bazı bitcoin kullanıcıları süresi dolmuş bir bloğu ifade etmek için "Orphan block" ifadesini kullanmayı tercih etmektedir. Ayrıca, İngilizcede "reorganizasyon" ya da "reorg" terimleri "yeniden senkronizasyon" terimine tercih edilir.*