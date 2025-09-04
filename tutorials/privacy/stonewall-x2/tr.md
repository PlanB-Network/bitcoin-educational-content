---
name: Stonewall x2
description: Stonewall x2 işlemlerini anlama ve kullanma
---
![cover stonewall x2](assets/cover.webp)


***UYARI:** Samourai Wallet'ın kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, Stonewallx2 işlemleri, her iki kullanıcının da kendi Dojo'larına bağlı olması koşuluyla, yalnızca ilgili taraflar arasında PSBT'lerin manuel olarak değiştirilmesiyle çalışır. Ancak, bu araçların önümüzdeki haftalarda yeniden kullanıma sunulması mümkündür. Bu arada, Stonewallx2'nin teorik işleyişini anlamak ve bunları manuel olarak nasıl yapacağınızı öğrenmek için bu makaleye başvurabilirsiniz.*


_Eğer manuel olarak bir Stonewallx2 gerçekleştirmeyi düşünüyorsanız, prosedür bu eğitimde anlatılana çok benzer. Temel fark, Stonewallx2 işlem türünün seçiminde yatmaktadır: `Online` seçeneğini seçmek yerine, `In Person / Manual` seçeneğine tıklayın. Ardından, Stonewallx2 işlemini oluşturmak için PSBT'leri manuel olarak Exchange yapmanız gerekecektir. İşbirlikçinize fiziksel olarak yakınsanız, QR kodlarını art arda tarayabilirsiniz. Eğer uzaktaysanız, JSON dosyaları güvenli bir iletişim kanalı üzerinden değiş tokuş edilebilir. Eğitimin geri kalanı değişmeden kalır


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

> *Her harcamayı bir CoinJoin.* yapın

## Stonewall x2 işlemi nedir?


Stonewall x2, bir harcama sırasında, bu harcamaya dahil olmayan üçüncü bir tarafla işbirliği yaparak kullanıcı gizliliğini artırmayı amaçlayan özel bir Bitcoin işlem biçimidir. Bu yöntem, üçüncü bir tarafa ödeme yaparken iki katılımcı arasında mini bir CoinJoin simülasyonu yapar. Stonewall x2 işlemleri hem Samourai Wallet uygulamasında hem de Sparrow wallet yazılımında mevcuttur. Her ikisi de birlikte çalışabilir.


İşlemi oldukça basittir: ödemeyi yapmak için elimizdeki bir UTXO'u kullanırız ve kendi UTXO'u ile katkıda bulunan üçüncü bir tarafın yardımını isteriz. İşlem dört çıktı ile sonuçlanır: ikisi eşit miktarda, biri ödeme alıcısının Address'sine, diğeri işbirlikçiye ait bir Address'ye gönderilir. Üçüncü bir UTXO, işbirlikçinin başka bir Address'sine geri dönerek ilk tutarı geri almalarını sağlar (onlar için nötr bir eylem, modulo Mining ücretleri) ve son bir UTXO, ödemeden kaynaklanan değişikliği oluşturan bize ait bir Address'ye geri döner.


Böylece Stonewall x2 işlemlerinde üç farklı rol tanımlanmıştır:


- Gönderen, asıl ödemeyi yapan kişi;
- İşbirlikçi, işlemin genel anonimliğini artırmak için bitcoin sağlarken, sonunda fonlarını tamamen geri alır (Mining ücretlerini modüle ederek onlar için tarafsız bir eylem);
- Alıcı, işlemin özel niteliğinden habersiz olabilir ve sadece göndericiden bir ödeme bekler.


Daha iyi anlamak için bir örnek verelim. Alice, fiyatı `4,000 Sats` olan bagetini almak için fırına gitmiştir. Ödemesi için belirli bir gizlilik seviyesini korurken bitcoin ile ödeme yapmak istiyor. Bu nedenle, bu süreçte kendisine yardımcı olacak arkadaşı Bob'ü çağırır.

![schema stonewall x2](assets/en/1.webp)

Bu işlemi analiz ederek, fırıncının baget için ödeme olarak gerçekten de `4,000 Sats` aldığını görebiliriz. Alice girdi olarak `10,000 Sats` kullanmış ve çıktı olarak `6,000 Sats` almış, sonuçta bagetin fiyatına karşılık gelen `-4,000 Sats` net bakiye elde etmiştir. Bob ise girdi olarak `15,000 Sats` sağlamış ve iki çıktı almıştır: biri `4,000 Sats` ve diğeri `11,000 Sats`, sonuçta `0` bakiye oluşmuştur.

Bu örnekte, anlamayı kolaylaştırmak için Mining ücretlerini kasıtlı olarak ihmal ettim. Gerçekte, işlem ücretleri ödemeyi gönderen ile işbirlikçi arasında eşit olarak paylaşılır.


## Stonewall ile Stonewall x2 arasındaki fark nedir?


Bir StonewallX2 işlemi tam olarak bir Stonewall işlemi gibi çalışır, ancak birincisi işbirlikçi iken ikincisi değildir. Gördüğümüz gibi, bir Stonewall x2 işlemi, ödemenin dışında olan ve işlem gizliliğini artırmak için bitcoinlerini sağlayacak olan üçüncü bir tarafın katılımını içerir. Tipik bir Stonewall işleminde, işbirlikçi rolü gönderen tarafından üstlenilir.


Fırındaki Alice örneğimizi tekrar gözden geçirelim. Eğer harcamalarında kendisine eşlik edecek Bob gibi birini bulamasaydı, tek başına bir Stonewall işlemi yapabilirdi. Böylece, iki giriş UTXO'su onun olacak ve çıkışta 3 alacaktı.

![transaction stonewall](assets/en/2.webp)


Dışarıdan bakıldığında, işlem modeli aynı kalacaktır.

![Stonewall or Stonewall x2?](assets/en/5.webp)

Bu nedenle, bir Samourai harcama aracı kullanılırken mantık aşağıdaki gibi olmalıdır:


- Satıcı PayJoin Stowaway'i desteklemiyorsa, Stonewall x2 kullanılarak ödeme dışında başka bir kişiyle ortak bir işlem yapılabilir.
- Stonewall x2 işlemi yapacak kimse bulunamazsa, Stonewall x2 işleminin davranışını taklit eden bir Stonewall işlemi tek başına yapılabilir.
- Son olarak, Samourai tarafından yönetilen ve talep üzerine bir Stonewall x2 işleminde işbirlikçi olarak hareket edebilen bir sunucu olan JoinBot ile bir işlem yapmak son seçenek olacaktır.


Bir Stonewall X2 işleminde size yardımcı olmak isteyen bir işbirlikçi bulmak istiyorsanız, göndericileri ve işbirlikçileri birbirine bağlamak için Samourai kullanıcıları tarafından sürdürülen bu Telegram grubunu (resmi olmayan) da ziyaret edebilirsiniz: [Make Every Spend a CoinJoin](https://t.me/EverySpendACoinjoin).


[**-> Stonewall işlemleri hakkında daha fazla bilgi edinin**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


## Stonewall x2 işleminin amacı nedir?


Stonewall x2 yapısı işleme önemli miktarda entropi ekler ve zincir analizini karıştırır. Dışarıdan bakıldığında, böyle bir işlem iki kişi arasında küçük bir CoinJoin olarak yorumlanabilir. Ancak gerçekte bu bir ödemedir. Bu yöntem zincir analizinde belirsizlikler yaratır ve hatta yanlış ipuçlarına yol açar.


Alice, Bob ve Baker örneğine geri dönelim. Blockchain üzerindeki işlem şu şekilde görünecektir:

![stonewall x2 public](assets/en/3.webp)

Genel zincir analizi sezgisel yöntemlerine güvenen bir dış gözlemci yanlışlıkla "Alice ve Bob, her biri girdi olarak bir UTXO ve her biri çıktı olarak iki UTXO ile küçük bir CoinJoin gerçekleştirdi" sonucuna varabilir![yanlış yorumlama taş duvarı x2](assets/en/4.webp)

Bu yorum yanlıştır, çünkü bildiğiniz gibi Baker'a bir UTXO gönderilmiştir, Alice'in yalnızca bir değişiklik çıkışı vardır ve Bob'ün iki çıkışı vardır.

![transaction stonewall x2](assets/en/1.webp)

Dış gözlemci Stonewall x2 işleminin modelini tespit etmeyi başarsa bile, tüm bilgilere sahip olmayacaktır. Aynı tutardaki iki UTXO'dan hangisinin ödemeye karşılık geldiğini belirleyemeyeceklerdir. Ayrıca, ödemeyi yapanın Alice mü yoksa Bob mi olduğunu da bilemeyeceklerdir. Son olarak, iki girdi UTXO'sunun iki farklı kişiden mi geldiğini yoksa bunları birleştiren tek bir kişiye mi ait olduğunu belirleyemeyeceklerdir. Bu son nokta, yukarıda ele aldığımız klasik Stonewall işlemlerinin Stonewall x2 işlemleri ile tamamen aynı modeli izlemesinden kaynaklanmaktadır. Dışarıdan bakıldığında ve bağlam hakkında ek bilgi olmadan, bir Stonewall işlemini bir Stonewall x2 işleminden ayırt etmek imkansızdır. Ancak, birincisi işbirliğine dayalı işlemler değilken, ikincisi öyledir. Bu durum, bu harcamaya ilişkin şüpheleri daha da artırmaktadır.

![Stonewall or Stonewall x2 ?](assets/en/5.webp)



## Soroban üzerinden işbirliği yapabilmek için Paynym'ler arasında nasıl bağlantı kurulur?


Samourai'deki diğer işbirlikçi işlemlerde olduğu gibi (*Cahoots*), bir Stonewall x2 gerçekleştirmek, gönderen ve işbirlikçi arasında kısmen imzalanmış işlemlerin Exchange'sını içerir. Bu Exchange, işbirlikçinizle fiziksel olarak birlikte olmanız durumunda manuel olarak veya Soroban iletişim protokolü aracılığıyla otomatik olarak yapılabilir.


İkinci seçeneği seçerseniz, bir Stonewall x2 gerçekleştirmeden önce Paynym'ler arasında bir bağlantı kurmanız gerekecektir. Bunu yapmak için, Paynym'iniz işbirlikçinizin Paynym'ini "takip etmeli" ve bunun tersi de geçerlidir.


**İşbirlikçinin Paynym'ine erişme:**


Başlamak için, işbirlikçinizin Paynym'inin ödeme kodunu almanız gerekir. Samourai Wallet uygulamasında, işbirlikçiniz ekranın sol üst köşesinde bulunan Paynym simgesine (küçük robot) basmalı, ardından `+...` ile başlayan Paynym takma adına tıklamalıdır. Örneğin, benimki `+namelessmode0aF`.


![samourai paynym](assets/notext/6.webp)

Ortak çalışanınız Sparrow wallet kullanıyorsa, 'Araçlar' sekmesine ve ardından 'PayNym'i Göster' seçeneğine tıklamalıdır![paynym Sparrow](assets/notext/7.webp)

**Samourai Wallet'tan işbirlikçinizin PayNym'ini takip edin:**


Samourai Wallet kullanıyorsanız, uygulamayı başlatın ve 'PayNyms' menüsüne aynı şekilde erişin. PayNym'inizi ilk kez kullanıyorsanız, tanımlayıcısını edinmeniz gerekecektir.


![request paynym samourai](assets/notext/8.webp)


Ardından ekranın sağ altındaki mavi '+' işaretine tıklayın.

![add collaborator paynym](assets/notext/9.webp)

Daha sonra 'ÖDEME KODU YAPIŞTIR'ı seçerek iş ortağınızın ödeme kodunu yapıştırabilir veya 'QR KODU TARA'ya basarak QR kodunu taramak için kamerayı açabilirsiniz.

![paste paynym identifier](assets/notext/10.webp)


'TAKİP ET' düğmesine tıklayın.

![follow paynym](assets/notext/11.webp)

'EVET'e tıklayarak onaylayın.

![confirm follow paynym](assets/notext/12.webp)

Yazılım daha sonra size bir 'BAĞLAN' düğmesi sunacaktır. Eğitimimiz için bu düğmeye tıklamanız gerekli değildir. Bu adım yalnızca BIP47'nin bir parçası olarak diğer PayNym'e ödeme yapmayı planlıyorsanız gereklidir, ki bu da eğitimimizle ilgili değildir.

![connect paynym](assets/notext/13.webp)

PayNym'iniz işbirlikçinizin PayNym'ini takip etmeye başladığında, işbirlikçinizin de sizi takip edebilmesi için bu işlemi ters yönde tekrarlayın. Daha sonra bir Stonewall x2 işlemi gerçekleştirebilirsiniz.


**İşbirlikçinizin Sparrow wallet'deki PayNym'ini takip edin:**


Sparrow wallet kullanıyorsanız, Wallet'ünüzü açın ve 'PayNym'i Göster' menüsüne erişin. PayNym'nizi ilk kez kullanıyorsanız, 'PayNym Al' seçeneğine tıklayarak bir tanımlayıcı edinmeniz gerekecektir.

![request paynym sparrow](assets/notext/14.webp)

Ardından 'Kişi Bul' kutusuna işbirlikçinizin PayNym tanımlayıcısını (takma adı '+...' veya ödeme kodu 'PM...') girin ve 'Kişi Ekle' düğmesine tıklayın.

![add contact paynym](assets/notext/15.webp)

Yazılım daha sonra size bir 'İletişim Bağlantısı' düğmesi sunacaktır. Eğitimimiz için bu düğmeye tıklamanız gerekli değildir. Bu adım yalnızca BIP47'nin bir parçası olarak belirtilen PayNym'e ödeme yapmayı planlıyorsanız gereklidir, ki bu da eğitimimizle ilgili değildir.


PayNym'iniz işbirlikçinizin PayNym'ini takip etmeye başladığında, işbirlikçinizin de sizi takip edebilmesi için bu işlemi ters yönde tekrarlayın. Daha sonra bir Stonewall x2 işlemi gerçekleştirebilirsiniz.

## Samourai Wallet'te Stonewall x2 işlemi nasıl yapılır?


Paynyms'i bağlamanın önceki adımlarını tamamladıysanız, nihayet Stonewall x2 işlemini yapmaya hazırsınız! Bunu yapmak için Samourai Wallet hakkındaki video eğitimimizi izleyin:

![Stonewall x2 Tutorial - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)


## Sparrow wallet'de Stonewall x2 işlemi nasıl yapılır?


Paynyms'i bağlamak için önceki adımları tamamladıysanız, nihayet Stonewall x2 işlemini yapmaya hazırsınız! Bunu yapmak için Sparrow wallet ile ilgili video eğitimimizi izleyin:

![Stonewall x2 Tutorial - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)


**Harici kaynaklar:**


- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.