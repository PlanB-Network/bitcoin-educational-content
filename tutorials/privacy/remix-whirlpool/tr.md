---
name: Remix - Whirlpool
description: Whirlpool'de kaç tane remiks yapılmalı?
---
![cover remix- wp](assets/cover.webp)


***UYARI:** Samourai Wallet'ün kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, Samourai'nin Gitlab'ında barındırıldığı için Whirlpool İstatistik Aracı artık indirilemiyor. Bu aracı daha önce yerel olarak makinenize indirmiş olsanız veya RoninDojo düğümünüze yüklemiş olsanız bile, WST şu anda çalışmayacaktır. Çalışması için OXT.me tarafından sağlanan verilere dayanıyordu ve bu siteye artık erişilemiyor. Şu anda, Whirlpool protokolü etkin olmadığından WST özellikle kullanışlı değildir. Bununla birlikte, bu yazılımların önümüzdeki haftalarda eski haline getirilmesi mümkündür. Ayrıca, bu makalenin teorik kısmı, genel olarak eş birleşmelerin ilkelerini ve hedeflerini (sadece Whirlpool değil) anlamanın yanı sıra Whirlpool modelinin etkinliğini anlamak için de geçerliliğini korumaktadır. Ayrıca CoinJoin döngüleri tarafından sağlanan gizliliğin nasıl ölçüleceğini de öğrenebilirsiniz.*


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

> *Paralarınızın geride bıraktığı bağı kırın*

Bu bana sıkça sorulan bir soru. **Whirlpool ile eş birleştirmeler yaparken, tatmin edici sonuçlar elde etmek için kaç remiks yapılmalıdır?


CoinJoin'nın amacı, Coin'nizi bir grup ayırt edilemeyen madeni parayla karıştırarak makul bir inkar edilebilirlik sunmaktır. Bu işlemin amacı hem geçmişten günümüze hem de günümüzden geçmişe olan izlenebilirlik bağlantılarını kırmaktır. Başka bir deyişle, CoinJoin döngülerinin girişindeki ilk işleminizi bilen bir analist, remiks döngülerinin çıkışındaki UTXO'inizi kesin olarak belirleyememelidir (giriş döngülerinden çıkış döngülerine analiz).

![past-present links diagram](assets/en/1.webp)


Tersine, CoinJoin döngülerinin çıkışındaki UTXO'unuzu bilen bir analist, döngülerin girişindeki orijinal işlemi belirleyememelidir (çıkış döngülerinden giriş döngülerine analiz).

![present-past links diagram](assets/en/2.webp)

Bununla birlikte, remiks sayısı bir analistin geçmiş ile günümüz arasında bağlantı kurmakta karşılaşacağı güçlüğü değerlendirmek için güvenilir bir kriter değildir. Daha uygun bir gösterge, Coin'nizin içinde saklandığı grupların büyüklüğü olacaktır. Bu göstergeler "anonsetler" olarak adlandırılır. Whirlpool durumunda, iki tür anonset vardır.


İlk olarak, UTXO'ünüzün CoinJoin döngülerinin çıkışında gizlendiği grubun boyutunu, yani bu grup içinde bulunan ayırt edilemeyen madeni paraların sayısını belirleyebiliriz.

![probable UTXOs at exit](assets/en/3.webp)

Fransızca'da "prospective anonset", İngilizce'de "forward anonset" veya "forward-looking metrics" olarak adlandırılan bu gösterge, Coin'nızın CoinJoin döngülerinin girişinden çıkışına kadar izlediği yolu takip eden analizlere karşı direncini değerlendirmemizi sağlar. Bu metrik, UTXO'nizin CoinJoin sürecindeki giriş noktasından çıkış noktasına kadar olan geçmişini yeniden yapılandırma girişimlerine karşı ne ölçüde korunduğunu tahmin eder. Örneğin, işleminiz ilk CoinJoin döngüsüne katılmış ve iki ek aşağı akış döngüsü gerçekleştirilmişse, Coin'nızın olası anonseti `13` olacaktır:

![forward anonset](assets/en/4.webp)

İkinci olarak, parçanızın bugünden geçmişe doğru bir analize direncini değerlendirmek için başka bir gösterge hesaplanabilir. Döngülerin sonunda UTXO'unuzu bilerek, bu gösterge CoinJoin döngülerinde girdinizi oluşturabilecek potansiyel Tx0 işlemlerinin sayısını belirler (döngülerin sonundan başına kadar analiz). Bu gösterge, bir analistin eş birleşmelerden geçtikten sonra parçanızın kaynağını izlemesinin ne kadar zor olduğunu ölçer![Girişteki olası kaynaklar](assets/en/5.webp)

Bu göstergenin adı "geriye dönük anonset" veya "geriye dönük metrikler "dir. Fransızca'da ben buna "anonset rétrospectif" demeyi seviyorum. Aşağıdaki diyagramda bu, tüm turuncu Tx0 baloncuklarına karşılık gelmektedir:

![backward anonset](assets/en/6.webp)

Bu göstergelerin hesaplama yöntemi hakkında daha fazla bilgi edinmek için bu konudaki [Twitter başlığımı] (https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) okumanızı tavsiye ederim. Ayrıca PlanB Ağı hakkında daha kapsamlı bir makale hazırlıyoruz.


Belirli bir remiks sayısı beklediğiniz için verilen cevabın tatmin edici görünmediğinin farkındayım ve sizi belgelere yönlendiriyorum. Bunun nedeni, remiks sayısının CoinJoin döngülerinde kazanılan anonimliği değerlendirmek için güvenilir olmayan bir gösterge olmasıdır. Bu nedenle, mutlak ve evrensel bir güvenlik eşiği olarak sabit bir remiks sayısı tanımlamak mümkün değildir.


Parçanızın her ek remiksinin anonimlik setlerini artırdığı doğrudur. Ancak, muhtemel anonsetinizin büyümesine katkıda bulunan şeyin öncelikle eşleriniz tarafından gerçekleştirilen remiksler olduğunu anlamak önemlidir. Whirlpool modeliyle, işleminiz yalnızca iki ya da üç CoinJoin döngüsüyle, yalnızca önceki coinjoin'lere katılan eşlerin faaliyetleriyle önemli düzeyde muhtemel anonimlik elde edebilir.


Öte yandan, geriye dönük anonset bizim durumumuzda bir endişe kaynağı değildir. Aslında, ilk CoinJoin'ünüzden itibaren, önceki havuz işlemlerinin mirasından faydalanırsınız, bu da parçanıza hemen yüksek bir geriye dönük anonset verir ve sonraki her döngüde marjinal bir artış olur.

Ayrıca, makul inkar edilebilirlik yaratmanın asla tam olmadığını anlamak da önemlidir. Coin'inizin izini sürme olasılığına dayanır. Bu olasılık, onu gizleyen grupların büyüklüğü arttıkça azalır. Bu nedenle, anonslar açısından hedeflerinizi kişisel beklentilerinize göre ayarlamalısınız. Sizi coinjoins kullanmaya iten nedenleri ve bu hedeflere ulaşmak için gerekli anonimlik seviyelerini kendinize sorun. Örneğin, coinjoins kullanımı sadece vaftiz çocuğunuza doğum günü için birkaç Sats gönderirken Wallet'ünüzün gizliliğini korumayı amaçlıyorsa, çok yüksek anonimlik seviyeleri gerekli değildir. Vaftiz çocuğunuz muhtemelen derinlemesine zincir analizi yapamayacaktır ve yapsa bile bunun hayatınız üzerindeki etkileri felaket boyutunda olmayacaktır. Ancak, en ufak bir bilginin hapisle sonuçlanabileceği otoriter bir rejimin hedefindeyseniz, eylemlerinizin çok daha katı kriterlere göre yönlendirilmesi gerekecektir.


Bu ünlü anonset göstergelerini belirlemek için **WST** (Whirlpool Stats Tool) adlı bir Python aracını kullanabilirsiniz.


Bununla birlikte, her bir madeni paranızın anonsetlerini hesaplamak her zaman gerekli değildir. Whirlpool'in tasarımı zaten size garanti sağlamaktadır. Daha önce de belirtildiği gibi, geriye dönük anonset nadiren bir endişe kaynağıdır. İlk karışımınızdan zaten özellikle yüksek bir geriye dönük puan elde edersiniz. İleriye dönük anonsete gelince, Coin'unuzu yeterince uzun bir süre boyunca post-mix hesabında tutmanız yeterlidir. Örneğin, işte CoinJoin havuzunda iki ay geçirdikten sonra `100.000 Sats` coin'lerimden birinin anonset skorları:

![WST anonsets](assets/en/7.webp)

Geçmişe dönük puan `34,593` ve geleceğe dönük puan `45,202` olarak gösterilmektedir. Somut olarak bu iki anlama gelmektedir:


- Eğer bir analist döngülerin sonunda benim Coin'mi bilir ve kaynağının izini sürmeye çalışırsa, her biri benim olma olasılığı eşit olan `34,593' potansiyel kaynakla karşılaşacaktır.
- Eğer bir analist döngülerin başında benim Coin'ümü bilir ve sonunda bunun karşılığını belirlemeye çalışırsa, her biri benim olma olasılığı aynı olan `45.202` olası UTXO ile karşı karşıya kalacaktır.

Bu nedenle Whirlpool kullanımının özellikle `HODL -> Karıştır -> Harca -> Değiştir` stratejisiyle ilgili olduğunu düşünüyorum. Bence en mantıklı yaklaşım, kişinin birikimlerinin çoğunu Cold Wallet'da bitcoin olarak tutarken, günlük harcamaları karşılamak için Samourai'de sürekli olarak CoinJoin'te belirli sayıda coin bulundurmasıdır. Coinjoins'ten gelen bitcoinler harcandığında, tanımlanmış karışık coin eşiğine geri dönmek için yenileriyle değiştirilirler. Bu yöntem, UTXO'larımızın anons edilmesi endişesinden kurtulmamızı sağlarken, coinjoins'in etkili olması için gereken süreyi çok daha az kısıtlayıcı hale getiriyor.


Umarım bu cevap Whirlpool modeline biraz ışık tutmuştur. Bitcoin'ta coinjoins'in nasıl çalıştığı hakkında daha fazla bilgi edinmek istiyorsanız, bu konudaki kapsamlı makalemi okumanızı tavsiye ederim:


https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

**Harici kaynaklar:**


- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://estudiobitcoin.com/como-instalar-y-utilizar-Whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/
- https://medium.com/samourai-Wallet/diving-head-first-into-Whirlpool-anonymity-sets-4156a54b0bc7.