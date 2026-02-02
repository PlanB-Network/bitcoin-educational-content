---
name: Sparrow Wallet - Stonewall
description: Sparrow'de Stonewall işlemlerini anlama ve kullanma
---

![cover](assets/cover.webp)




> *İşlemlerinizin göndericisi ve alıcısı arasında matematiksel olarak kanıtlanabilir şüphe ile blok zinciri analizinin varsayımlarını kırın

## Stonewall işlemi nedir?



Stonewall, kullanıcıların harcama yaparken gizliliğini artırmak için tasarlanmış, gerçekte iki kişi olmadan iki kişi arasındaki bir coinjoin'i taklit eden özel bir Bitcoin işlem biçimidir. Aslında bu işlem işbirliğine dayalı değildir. Bir kullanıcı, girdi olarak yalnızca kendisine ait UTXO'ları kullanarak kendi başına oluşturabilir. Böylece, başka bir kullanıcıyla senkronize olmak zorunda kalmadan, herhangi bir durum için bir Stonewall işlemi oluşturabilirsiniz.



Stonewall işlemi şu şekilde çalışır: işlemin girdisi olarak, ihraççı kendisine ait olan 2 UTXO kullanır. Çıktı tarafında, işlem 2'si tamamen aynı miktarda olmak üzere 4 çıktı üretir. Diğer 2 tanesi döviz olacaktır. Aynı tutardaki 2 çıktıdan sadece biri alacaklıya gidecektir.



Yani bir Stonewall işleminde sadece 2 rol vardır:




- Asıl ödemeyi yapan ihraççı ;
- Alıcı, işlemin özel niteliğinden habersiz olabilir ve sadece göndericiden ödeme bekler.



Bu işlem yapısını anlamak için bir örnek verelim. Alice, `4,000 sats` tutarındaki bagetini almak için fırıncıya gitmiştir. Ödemesi hakkında bir tür gizliliği korurken bitcoin ile ödeme yapmak istiyor. Bu yüzden ödeme için bir Stonewall işlemi oluşturmaya karar verir.



![image](assets/fr/01.webp)



Bu işlemi analiz ederek, fırıncının baget için ödeme olarak gerçekten de `4.000 sats` aldığını görebiliriz. Alice girdi olarak 2 UTXO kullanmıştır: biri `10,000 sats` ve diğeri `15,000 sats`. Çıktı olarak ise 3 UTXO geri kazanmıştır: biri `4,000 sats`, biri `6,000 sats` ve biri `11,000 sats`. Dolayısıyla Alice'nin bu işlemde net bakiyesi 4.000 sats`dur ve bu da bagetin fiyatına uygundur.



Bu örnekte, anlaşılmasını kolaylaştırmak için mining ücretlerini kasıtlı olarak ihmal ettim. Gerçekte, işlem maliyetleri tamamen ihraççı tarafından karşılanmaktadır.



## Stonewall ile Stonewall x2 arasındaki fark nedir?



Stonewall işlemi StonewallX2 işlemi ile aynı şekilde çalışır, ancak ikincisi klasik Stonewall işleminden farklı olarak işbirliği gerektirir, bu nedenle "x2" adı verilmiştir. Bunun nedeni, Stonewall işleminin harici bir işbirliğine ihtiyaç duymadan yürütülmesidir: gönderen, başka bir kişinin yardımı olmadan bunu gerçekleştirebilir. Buna karşılık, bir Stonewall x2 işlemi için, "işbirlikçi" olarak bilinen ek bir katılımcı sürece katılır. Bu kişi, gönderenin bitcoinlerinin yanı sıra kendi bitcoinlerini de işleme katar ve sonunda tüm tutarı devralır (mining maliyetleri hariç).



Fırındaki Alice örneğimize geri dönelim. Eğer bir Stonewall x2 işlemi yapmak isteseydi, Alice işlemi ayarlarken Bob (üçüncü bir taraf) ile işbirliği yapmak zorunda kalacaktı. Her ikisi de bir UTXO getirecekti. Bob daha sonra çıkışta katkısının tamamını alacaktı. Fırıncı, Stonewall işleminde olduğu gibi bageti için ödeme alırken, Alice başlangıçtaki bakiyesini bagetin maliyeti düşüldükten sonra geri almış olacaktır.



![image](assets/fr/02.webp)



Dışarıdan bakan birinin bakış açısına göre, işlem tamamen aynı kalacaktı.



![image](assets/fr/03.webp)



Özetle, Stonewall ve Stonewall x2 işlemleri aynı yapıyı paylaşmaktadır. İkisi arasındaki fark, işbirliğine dayalı veya işbirliğine dayalı olmayan yapılarında yatmaktadır. Stonewall işlemi, işbirliğine ihtiyaç duyulmadan bireysel olarak geliştirilmektedir. Öte yandan Stonewall x2 işlemi, iki kişi arasındaki işbirliğine dayanır.



[**-> Stonewall işlemleri hakkında daha fazla bilgi edinin x2**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Stonewall işleminin amacı nedir?



Stonewall yapısı işleme muazzam miktarda entropi ekleyerek zincir analizinin sınırlarını bulanıklaştırır. Dışarıdan bakıldığında, böyle bir işlem iki kişi arasında küçük bir coin birleşmesi olarak yorumlanabilir. Ancak gerçekte, Stonewall x2 işlemi gibi, bu da bir ödemedir. Dolayısıyla bu yöntem zincir analizinde belirsizlikler yaratır, hatta yanlış ipuçlarına yol açar.



Fırıncıdaki Alice örneğini ele alalım. Blok zincirindeki işlem şu şekilde görünecektir:



![image](assets/fr/04.webp)



Genel zincir analizi sezgiselliğine güvenen dışarıdan bir gözlemci yanlış bir şekilde "*iki kişi, her biri girdi olarak bir UTXO ve her biri çıktı olarak iki UTXO ile küçük bir coinjoin yapmıştır*" sonucuna varabilir.



![image](assets/fr/05.webp)



Bu yorum yanlıştır, çünkü bildiğiniz gibi fırıncıya bir UTXO gönderildi, gelen 2 UTXO Alices'ten geldi ve 3 değişim çıktısını geri aldı.



![image](assets/fr/01.webp)



Dışarıdan bir gözlemci Stonewall işleminin muhatabını tespit etmeyi başarsa bile, tüm bilgilere sahip olmayacaktır. Aynı tutardaki iki UTXO'dan hangisinin ödemeye karşılık geldiğini belirleyemeyecektir. Buna ek olarak, iki UTXO girişinin iki farklı kişiden mi geldiğini yoksa bunları birleştiren tek bir kişiye mi ait olduğunu belirleyemeyecektir. Bu son nokta, yukarıda bahsedilen Stonewall x2 işlemlerinin Stonewall işlemleriyle tamamen aynı modeli izlemesinden kaynaklanmaktadır. Dışarıdan bakıldığında ve ek bağlamsal bilgiler olmadan, bir Stonewall işlemi ile bir Stonewall x2 işlemi arasındaki farkı söylemek imkansızdır. Birincisi işbirliğine dayalı işlemler değilken, ikincisi öyledir. Bu durum harcamalara daha da fazla şüphe katmaktadır.



![image](assets/fr/03.webp)



## Sparrow üzerinde nasıl Stonewall işlemi yapabilirim?



Başlangıçta Samurai Wallet ekibi tarafından geliştirilen Stonewall işlemleri, Samurai geliştiricilerinin tutuklanmasının ardından oluşturulan orijinal portföyden bir fork olan Ashigaru uygulaması ve ayrıca Sparrow Wallet tarafından devralındı.



Sparrow'ü yüklemeniz ve bir :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Stowaway veya Stonewall x2 (*cahoots*) işlemlerinin aksine, Stonewall işlemleri Paynyms kullanımını gerektirmez. Herhangi bir özel hazırlık veya başka bir kullanıcıyla işbirliği yapmadan doğrudan gerçekleştirilebilirler.



Sparrow üzerinde bir Stonewall işlemi gerçekleştirmek için prosedür çok basittir: ya `Gönder' menüsünden ya da *Coin Kontrolü* yapmak istiyorsanız `UTXOs' menüsünden her zamanki gibi bir işlem oluşturarak başlayın.



![Image](assets/fr/06.webp)



Ardından işlem ayrıntılarını girin: alıcının adresi, bir etiket, gönderilecek miktar ve piyasa koşullarına bağlı olarak ücret miktarı veya oranı.



![Image](assets/fr/07.webp)



Onaylamadan önce, burası Stonewall yapısını seçebileceğiniz yerdir. Arayüzün alt kısmında `Efficiency` seçeneğini `Privacy` ile değiştirin. Bu seçenek görünmezse, portföyünüzde bu tür bir işlem oluşturmak için yeterli sayıda UTXO olmadığı anlamına gelir.



![Image](assets/fr/08.webp)



Gizlilik' seçeneğini seçtikten sonra, işlemin yapısının tamamen değiştiğini fark edeceksiniz: bu işlem, girdi olarak UTXO'larınızdan birkaçını tüketen ve aynı miktarlarda iki çıktı üreten bir Stonewall işlemi haline gelir; bunlardan biri, takas çıktılarına ek olarak `100.000 sats' tutarındaki gerçek ödemeye karşılık gelir.



![Image](assets/fr/09.webp)



Her şey doğruysa, `İşlem Oluştur` seçeneğine tıklayın.



Ardından işlem ayrıntılarınızı son bir kez kontrol edebilir ve `İmzalama için İşlemi Sonlandır` seçeneğine tıklayabilirsiniz.



![Image](assets/fr/10.webp)



Ardından, işlemi portföyünüze özgü yönteme göre imzalayın ve Bitcoin ağında yayınlamak için `İşlemi Yayınla` seçeneğine tıklayarak onay bekleyin.



![Image](assets/fr/11.webp)



Artık bir Stonewall işleminin Sparrow Wallet'da nasıl çalıştığını ve nasıl oluşturulacağını biliyorsunuz. Zincir üzerindeki gizliliğinizi güçlendirmek için tasarlanmış bu araçlara hakimiyetinizi derinleştirmek için sizi Plan ₿ Academy'deki BTC 204 eğitimimi takip etmeye davet ediyorum:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c