---
name: Stonewall
description: Stonewall işlemlerini anlama ve kullanma
---
![cover stonewall](assets/cover.webp)


***UYARI:** Samourai Wallet kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, Samourai Wallet uygulamasını kullanmak artık düzgün çalışması için kendi Dojo'nuza bağlanmanızı gerektiriyor. Bunun yanı sıra, Stonewall işlemleri hiç etkilenmedi ve hala sorunsuz bir şekilde gerçekleştirilebilir. Aslında, bu tür işlemler Soroban aracılığıyla harici işbirliği veya bağlantıya ihtiyaç duymadan bağımsız olarak gerçekleştirilir.*


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

> *İşlemlerinizin göndericisi ve alıcısı arasında matematiksel olarak kanıtlanabilir şüphe ile Blockchain analizinin varsayımlarını kırın

## Stonewall işlemi nedir?

Stonewall, iki taraf arasındaki bir CoinJoin'yi taklit ederek bir işlem sırasında kullanıcı gizliliğini artırmayı amaçlayan belirli bir Bitcoin işlem biçimidir. Aslında bu işlem işbirliğine dayalı değildir. Bir kullanıcı bunu tek başına, yalnızca kendi UTXO'larını girdi olarak dahil ederek oluşturabilir. Bu nedenle, başka bir kullanıcıyla koordinasyon kurmanıza gerek kalmadan herhangi bir durum için bir Stonewall işlemi oluşturabilirsiniz.


Bir Stonewall işleminin işleyişi şu şekildedir: girdi olarak, gönderici kendisine ait olan 2 UTXO kullanır. Çıktı olarak işlem, 2'si tamamen aynı miktarda olmak üzere 4 çıktı üretir. Diğer 2'si değişim olacaktır. Aynı tutardaki 2 çıktıdan sadece biri ödeme alıcısına gidecektir.


Bir Stonewall işleminde sadece 2 rol vardır:


- Gönderen, asıl ödemeyi yapan kişi;
- Alıcı, işlemin özel niteliğinden habersiz olabilir ve sadece göndericiden bir ödeme bekler.


Bu işlem yapısını anlamak için bir örnek verelim. Alice, fiyatı `4,000 Sats` olan bagetini almak için fırına gitmiştir. Ödemesinde belirli bir gizlilik seviyesini korurken bitcoin ile ödeme yapmak istiyor. Bu nedenle, ödeme için bir Stonewall işlemi oluşturmaya karar verir.

![transaction stonewall bakery](assets/en/1.webp)

Bu işlem incelendiğinde, fırıncının baget için ödeme olarak gerçekten de `4,000 Sats` aldığını görebiliriz. Alice girdi olarak 2 UTXO kullanmıştır: biri `10,000 Sats` ve diğeri `15,000 Sats`. Çıktı olarak 3 UTXO almıştır: biri `4.000 Sats`, biri `6.000 Sats` ve biri `11.000 Sats`. Alice bu işlemde baget fiyatına karşılık gelen `-4,000 Sats` net bakiyeye sahiptir.


Bu örnekte, anlamayı kolaylaştırmak için Mining ücretlerini kasıtlı olarak atladım. Gerçekte, işlem ücretleri tamamen gönderen tarafından karşılanır.


## Stonewall ile Stonewall x2 arasındaki fark nedir?

Stonewall işlemi StonewallX2 işlemi ile aynı şekilde çalışır, tek fark klasik Stonewall işleminden farklı olarak ikincisinin işbirliği gerektirmesidir, bu nedenle "x2" olarak adlandırılmıştır. Aslında, Stonewall işlemi harici işbirliği gerektirmeden gerçekleştirilebilir: gönderen başka bir kişinin yardımı olmadan bunu gerçekleştirebilir. Ancak, Stonewall x2 işlemi için, "işbirlikçi" olarak adlandırılan ek bir katılımcı sürece katılır. İşbirlikçi, göndericinin bitcoinlerinin yanı sıra kendi bitcoinlerini de girdi olarak katar ve çıktı olarak tüm toplamı alır (Mining ücretleri hariç).


Fırındaki Alice örneğimizi tekrar gözden geçirelim. Eğer bir Stonewall x2 işlemi yapmak isteseydi, Alice işlemi oluştururken Bob (üçüncü bir taraf) ile işbirliği yapmak zorunda kalacaktı. Her biri UTXO'e bir girdi sağlamış olacaktı. Bob daha sonra girdisinin tamamını çıktı olarak alacaktı. Fırıncı, Stonewall işleminde olduğu gibi bageti için ödeme alırken, Alice başlangıçtaki bakiyesini bagetin maliyeti hariç geri alırdı.

![transaction stonewall x2](assets/en/2.webp)


Dışarıdan bakıldığında, işlemin şekli tamamen aynı kalacaktır.

![Stonewall or Stonewall x2 ?](assets/en/3.webp)


Özetle, Stonewall ve Stonewall x2 işlemleri aynı yapıyı paylaşmaktadır. İkisi arasındaki fark işbirliğine dayalı olmalarında yatmaktadır. Stonewall işlemi, işbirliğine ihtiyaç duyulmadan bireysel olarak geliştirilir. Buna karşın, Stonewall x2 işlemi, uygulanması için iki kişi arasındaki işbirliğine dayanır.


[**-> Stonewall x2 işlemleri hakkında daha fazla bilgi edinin**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)


## Stonewall işleminin amacı nedir?

Stonewall yapısı işleme önemli miktarda entropi ekler ve zincir analizini belirsizleştirir. Dışarıdan bakıldığında, böyle bir işlem iki kişi arasında küçük bir CoinJoin olarak yorumlanabilir. Ancak gerçekte, tıpkı Stonewall x2 işleminde olduğu gibi, bu bir ödemedir. Dolayısıyla bu yöntem zincir analizinde belirsizlikler yaratır ve hatta yanlış ipuçlarına yol açabilir.


Alice'nın fırındaki örneğini tekrar ele alalım. Blockchain üzerindeki işlem aşağıdaki gibi görünecektir:

![Stonewall or Stonewall x2 ?](assets/en/4.webp)

Yaygın zincir analizi sezgiselliğine güvenen bir dış gözlemci yanlışlıkla "*iki kişi, her biri girdi olarak bir UTXO ve her biri çıktı olarak iki UTXO ile küçük bir CoinJoin gerçekleştirdi*" sonucuna varabilir.

![Stonewall or Stonewall x2 ?](assets/en/5.webp)

Bu yorum yanlıştır çünkü bildiğiniz gibi fırıncıya bir UTXO gönderildi, girdideki 2 UTXO Alice'dan geliyor ve 3 değişim çıktısı aldı.


![transaction stonewall baker](assets/en/1.webp)

Dışarıdan bir gözlemci Stonewall işleminin modelini tespit etmeyi başarsa bile, tüm bilgilere sahip olmayacaktır. Aynı tutardaki iki UTXO'dan hangisinin ödemeye karşılık geldiğini belirleyemeyeceklerdir. Ayrıca, girdideki iki UTXO'nun iki farklı kişiden mi geldiğini yoksa bunları birleştiren tek bir kişiye mi ait olduğunu belirleyemeyeceklerdir. Bu son nokta, yukarıda bahsettiğimiz Stonewall x2 işlemlerinin Stonewall işlemleri ile tamamen aynı modeli izlemesinden kaynaklanmaktadır. Dışarıdan bakıldığında ve bağlam hakkında ek bilgi olmadan, bir Stonewall işlemini bir Stonewall x2 işleminden ayırt etmek imkansızdır. Ancak, birincisi işbirliğine dayalı işlemler değilken, ikincisi öyledir. Bu durum, bu harcama hakkındaki şüpheleri daha da artırmaktadır.

![Stonewall or Stonewall x2 ?](assets/en/3.webp)

## Samourai Wallet'de Stonewall işlemi nasıl yapılır?

Stowaway veya Stonewall x2 (cahoots) işlemlerinin aksine, Stonewall işlemi Paynyms kullanımını gerektirmez. Herhangi bir hazırlık adımı olmadan doğrudan yapılabilir. Bunu yapmak için Samourai Wallet ile ilgili video eğitimimizi izleyin:

![Stonewall Tutorial - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)


## Sparrow wallet'te Stonewall işlemi nasıl yapılır?

Stowaway veya Stonewall x2 (cahoots) işlemlerinin aksine, Stonewall işlemi Paynyms kullanımını gerektirmez. Herhangi bir hazırlık adımı olmadan doğrudan yapılabilir. Bunu yapmak için Sparrow wallet ile ilgili video eğitimimizi izleyin:

![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)



**Harici Kaynaklar:**


- https://docs.samourai.io/en/spend-tools#stonewall.