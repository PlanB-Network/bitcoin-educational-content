---
name: Ashigaru - Stonewall
description: Ashigaru'da Stonewall işlemlerini anlama ve kullanma
---
![cover stonewall](assets/cover.webp)



> *İşlemlerinizin göndericisi ve alıcısı arasında matematiksel olarak kanıtlanabilir şüphe ile blok zinciri analizinin varsayımlarını kırın

## Stonewall işlemi nedir?



Stonewall, kullanıcıların harcama yaparken gizliliğini artırmak için tasarlanmış, gerçekte iki kişi olmadan iki kişi arasındaki bir coinjoin'i taklit eden özel bir Bitcoin işlem biçimidir. Aslında bu işlem işbirliğine dayalı değildir. Bir kullanıcı, girdi olarak yalnızca sahip olduğu UTXO'ları kullanarak kendi başına oluşturabilir. Böylece, başka bir kullanıcıyla senkronize olmak zorunda kalmadan, herhangi bir durum için bir Stonewall işlemi oluşturabilirsiniz.



Stonewall işlemi şu şekilde çalışır: işlemin girdisi olarak, ihraççı kendisine ait olan 2 UTXO kullanır. Çıktı tarafında, işlem 2'si tamamen aynı miktarda olmak üzere 4 çıktı üretir. Diğer 2 tanesi döviz olacaktır. Aynı tutardaki 2 çıktıdan sadece biri alacaklıya gidecektir.



Yani bir Stonewall işleminde sadece 2 rol vardır:




- Asıl ödemeyi yapan ihraççı ;
- Alıcı, işlemin özel niteliğinden habersiz olabilir ve sadece göndericiden ödeme bekler.



Bu işlem yapısını anlamak için bir örnek verelim. Alice, `4,000 sats` değerindeki bagetini almak için fırıncıdadır. Ödemesi hakkında bir tür gizliliği korurken bitcoin ile ödeme yapmak istiyor. Bu yüzden ödeme için bir Stonewall işlemi oluşturmaya karar verir.



![image](assets/fr/01.webp)



Bu işlemi analiz ederek, fırıncının baget için ödeme olarak gerçekten de `4,000 sats` aldığını görebiliriz. Alice girdi olarak 2 UTXO kullanmıştır: biri `10,000 sats` ve diğeri `15,000 sats`. Çıktı tarafında ise 3 UTXO geri kazanmıştır: biri `4,000 sats`, biri `6,000 sats` ve biri `11,000 sats`. Dolayısıyla, Alice'ün bu işlemde 4.000 sats`lık net bir bakiyesi vardır ve bu da bagetin fiyatına iyi bir şekilde karşılık gelmektedir.



Bu örnekte, anlaşılmasını kolaylaştırmak için mining ücretlerini kasıtlı olarak ihmal ettim. Gerçekte, işlem maliyetleri tamamen ihraççı tarafından karşılanmaktadır.



## Stonewall ile Stonewall x2 arasındaki fark nedir?



Stonewall işlemi StonewallX2 işlemi ile aynı şekilde çalışır, ancak ikincisi klasik Stonewall işleminden farklı olarak işbirliği gerektirir, bu nedenle "x2" adı verilmiştir. Bunun nedeni, Stonewall işleminin harici bir işbirliğine ihtiyaç duymadan yürütülmesidir: gönderen, başka bir kişinin yardımı olmadan bunu gerçekleştirebilir. Buna karşılık, bir Stonewall x2 işlemi için, "işbirlikçi" olarak bilinen ek bir katılımcı sürece katılır. Bu kişi, göndericinin bitcoinlerinin yanı sıra kendi bitcoinlerini de işleme katar ve işlem sonunda tüm tutarı devralır (mining maliyetlerini modüle ederek).



Fırındaki Alice örneğimize geri dönelim. Eğer bir Stonewall x2 işlemi yapmak isteseydi, Alice işlemi ayarlarken Bob (üçüncü bir taraf) ile işbirliği yapmak zorunda kalacaktı. Her biri bir UTXO getirecekti. Bob daha sonra tüm katkısını geri almış olacaktı. Fırıncı, Stonewall işleminde olduğu gibi bageti için ödeme alırken, Alice başlangıçtaki bakiyesini bagetin maliyeti düşüldükten sonra geri alırdı.



![image](assets/fr/02.webp)



Dışarıdan bakan birinin bakış açısına göre, işlem tamamen aynı kalacaktı.



![image](assets/fr/03.webp)



Özetle, Stonewall ve Stonewall x2 işlemleri aynı yapıyı paylaşmaktadır. İkisi arasındaki fark, işbirliğine dayalı veya işbirliğine dayalı olmayan yapılarında yatmaktadır. Stonewall işlemi, işbirliğine ihtiyaç duyulmadan bireysel olarak geliştirilmektedir. Öte yandan Stonewall x2 işlemi, iki kişi arasındaki işbirliğine dayanır.



[**-> Stonewall işlemleri hakkında daha fazla bilgi edinin x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Stonewall işleminin amacı nedir?



Stonewall yapısı işleme muazzam miktarda entropi ekleyerek zincir analizinin sınırlarını bulanıklaştırır. Dışarıdan bakıldığında, böyle bir işlem iki kişi arasında küçük bir coin birleşmesi olarak yorumlanabilir. Ancak gerçekte, Stonewall x2 işlemi gibi, bu da bir ödemedir. Dolayısıyla bu yöntem zincir analizinde belirsizlikler yaratır, hatta yanlış ipuçlarına yol açar.



Fırıncıdaki Alice örneğini ele alalım. Blok zincirindeki işlem şu şekilde görünecektir:



![image](assets/fr/04.webp)



Genel zincir analizi sezgisel yöntemlerine güvenen bir dış gözlemci yanlış bir şekilde "**iki kişi, her biri girdi olarak bir UTXO ve her biri çıktı olarak iki UTXO ile küçük bir coinjoin yapmıştır**" sonucuna varabilir.



![image](assets/fr/05.webp)



Bu yorum yanlıştır, çünkü bildiğiniz gibi fırıncıya bir UTXO gönderildi, gelen 2 UTXO Alices'ten geldi ve 3 döviz kuru çıktısını geri aldı.



![image](assets/fr/01.webp)



Dışarıdan bir gözlemci Stonewall işleminin muhatabını tespit etmeyi başarsa bile, tüm bilgilere sahip olmayacaktır. Aynı tutardaki iki UTXO'dan hangisinin ödemeye karşılık geldiğini belirleyemeyecektir. Buna ek olarak, girilen iki UTXO'nun iki farklı kişiden mi yoksa bunları birleştiren tek bir kişiye mi ait olduğunu belirleyemeyecektir. Bu son nokta, yukarıda bahsedilen Stonewall x2 işlemlerinin Stonewall işlemleriyle tamamen aynı modeli izlemesinden kaynaklanmaktadır. Dışarıdan bakıldığında ve ek bağlamsal bilgi olmadan, bir Stonewall işlemi ile bir Stonewall x2 işlemi arasındaki farkı söylemek imkansızdır. Birincisi işbirliğine dayalı işlemler değilken, ikincisi öyledir. Bu da harcamalara daha da fazla şüphe katmaktadır.



![image](assets/fr/03.webp)



## Ashigaru'da nasıl Stonewall işlemi yapabilirim?



Aslen Samourai Wallet ekibi tarafından geliştirilen Stonewall işlemleri, Samourai geliştiricilerinin tutuklanmasının ardından oluşturulan orijinal fork'in bir wallet'si olan Ashigaru uygulaması tarafından devralındı. Ashigaru'yu yüklemeniz ve bir wallet oluşturmanız gerekecek:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Stowaway veya Stonewall x2 (*cahoots*) işlemlerinin aksine, Stonewall işlemleri Paynyms kullanımını gerektirmez. Önceden hazırlık yapmadan veya başka bir kullanıcıyla işbirliği yapmadan doğrudan gerçekleştirilebilirler.



Aslında, Taşduvar işlemleri yapmak için bir öğreticiye ihtiyacınız yoktur, çünkü Ashigaru, wallet'unuz yeterli UTXO içerdiği anda her harcama yaptığınızda bunları otomatik olarak oluşturur.



Ekranın sağ alt köşesindeki `+` düğmesine tıklayın ve ardından `Gönder` seçeneğini seçin.



![Image](assets/fr/06.webp)



Harcama yapmak istediğiniz hesabı seçin.



![Image](assets/fr/07.webp)



Ardından işlem ayrıntılarını girin: alıcının adresi ve gönderilecek tutar ve onaylamak için oka basın.



![Image](assets/fr/08.webp)



Burada elbette varsayılan işlem ücretlerini piyasa koşullarına göre ayarlayabilirsiniz. Ancak bu sayfadaki en ilginç unsur işlem türüdür. Ashigaru'nun otomatik olarak `STONEWALL'yi seçtiğini fark edeceksiniz. Daha fazlasını öğrenmek için `ÖNİZLEME` düğmesine tıklayın.



![Image](assets/fr/09.webp)



İşlemin gerçekten de Stonewall tipinde olduğunu görebilirsiniz: aynı tutarda 2 girdi, aynı tutarda 2 çıktının yanı sıra değişim çıktıları ve benim durumumda ödeme toplamını karşılamak için ek bir girdi içerir.



![Image](assets/fr/10.webp)



Stonewall işlemi yapmak istemiyor, ancak geleneksel bir ödemeyi tercih ediyorsanız, ekranın sağ üst köşesindeki kalem simgesine tıklayın ve ardından `STONEWALL` yerine `Basit` seçeneğini seçin.



![Image](assets/fr/11.webp)



Tüm ayrıntıları kontrol ettikten sonra, işlemi imzalamak ve serbest bırakmak için ekranın altındaki yeşil oku sürükleyin.



![Image](assets/fr/12.webp)



Artık bir Stonewall işleminin nasıl gerçekleştirileceğini ve daha da önemlisi nasıl çalıştığını biliyorsunuz. Daha fazla bilgi edinmek isterseniz, Ashigaru Terminal'de Whirlpool aracılığıyla nasıl coin birleşimi yapılacağını anlatan eğitimime bir göz atın.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add