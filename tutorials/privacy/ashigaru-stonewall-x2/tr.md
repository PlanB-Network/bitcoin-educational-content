---
name: Ashigaru - Stonewall x2
description: Ashigaru'da Stonewall x2 işlemlerini anlama ve kullanma
---
![cover stonewall x2](assets/cover.webp)



> *Her harcamayı bir coinjoin yapın

## Stonewall x2 işlemi nedir?



Stonewall x2, harcamaya dahil olmayan üçüncü bir tarafla işbirliği yaparak harcama yaparken kullanıcı gizliliğini artırmak için tasarlanmış özel bir Bitcoin işlem biçimidir. Bu yöntem, üçüncü bir tarafa ödeme yaparken iki katılımcı arasında bir mini-coinjoin simülasyonu yapar. Stonewall x2 işlemleri, Samourai fork'den (bu tür bir işlemin yaratılmasının arkasındaki ekip) bir Wallet olan Ashigaru uygulamasında mevcuttur.



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Çalışma şekli oldukça basit: ödemeyi yapmak için elinizdeki bir UTXO'ü kullanıyorsunuz ve kendi UTXO'leriyle katkıda bulunan üçüncü bir tarafın yardımını alıyorsunuz. İşlem dört çıktı ile sonuçlanır: ikisi eşit miktarda, biri alacaklının adresine, diğeri işbirlikçiye ait bir adrese gönderilir. Üçüncü bir UTXO, işbirlikçiye ait başka bir adrese geri gönderilir, bu da ilk tutarı geri almasını sağlar (mining maliyetlerini modüle ederek onun için tarafsız bir eylem) ve son bir UTXO bize ait bir adrese geri döner, bu da ödeme değişimini oluşturur.



Böylece Stonewall x2 işlemlerinde üç farklı rol tanımlanmıştır:




- Asıl ödemeyi yapan ihraççı ;
- İşlemin anonimliğini artırmak için bitcoinleri kullanıma sunan ve sonunda fonlarını tam olarak geri alan işbirlikçi (mining maliyetlerini modüle ederek kendisi için tarafsız bir eylem);
- Alıcı, işlemin özel niteliğinden habersiz olabilir ve sadece göndericiden ödeme bekler.



Bir örnek verelim. Alice, fiyatı `4,000 sats` olan bagetini almak için fırıncıya gitmiştir. Ödemesiyle ilgili gizliliği koruyarak bitcoin ile ödeme yapmak istiyor. Bu yüzden kendisine bu konuda yardımcı olacak arkadaşı Bob'i arar.



![image](assets/fr/01.webp)



Bu işlemi analiz ettiğimizde, fırıncının baget için ödeme olarak aslında `4,000 sats` aldığını görebiliriz. Alice girdide `10,000 sats` kullanmış ve çıktıda `6,000 sats` geri kazanmıştır, bu da bagetin fiyatına karşılık gelen `-4,000 sats` net bakiye vermektedir. Bob ise `15.000 sats` girdi sağlamış ve biri `4.000 sats` diğeri `11.000 sats` olmak üzere iki çıktı almış ve `0` bakiye elde etmiştir.



Bu örnekte, anlaşılmasını kolaylaştırmak için mining ücretlerini kasıtlı olarak ihmal ettim. Gerçekte, işlem ücretleri ödemeyi yapan kuruluş ile işbirlikçi arasında eşit olarak paylaşılır.



## Stonewall ile Stonewall x2 arasındaki fark nedir?



Bir StonewallX2 işlemi, bir Stonewall işlemiyle tamamen aynı şekilde çalışır, ancak birincisi işbirliğine dayalı iken ikincisi değildir. Gördüğümüz gibi, bir Stonewall x2 işlemi, ödemenin dışında olan ve işlemin gizliliğini artırmak için bitcoinlerini kullanıma sunacak olan üçüncü bir tarafın katılımını içerir. Klasik bir Stonewall işleminde, işbirlikçi rolü gönderen tarafından üstlenilir.



Fırındaki Alice örneğimize geri dönelim. Eğer harcama çılgınlığında ona eşlik edecek Bob gibi birini bulamamış olsaydı, kendi başına bir Taş Duvarı yapabilirdi. Bu şekilde, içeri girerken iki UTXO onun olurdu ve çıkarken de 3 tane alırdı.



![image](assets/fr/02.webp)




Dışarıdan bakan birinin bakış açısına göre, işlem aynı kalacaktı.



![image](assets/fr/05.webp)



Bu nedenle, bir Ashigaru harcama aracı kullanmak istediğinizde mantık aşağıdaki gibi olmalıdır:




- Satıcı Payjoin Stowaway'i desteklemiyorsa, Stonewall x2 sayesinde ödeme dışında başka bir kişiyle ortak bir işlem yapabilirsiniz;
- Stonewall x2 işlemi yapacak kimseyi bulamazsanız, Stonewall x2 işleminin davranışını taklit edecek bir Stonewall only işlemi yapabilirsiniz.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Stonewall x2 işleminin amacı nedir?



Stonewall x2 yapısı işleme muazzam miktarda entropi ekleyerek zincir analizini karıştırır. Dışarıdan bakıldığında, böyle bir işlem iki kişi arasında küçük bir Coinjoin olarak yorumlanabilir. Ancak gerçekte bu bir ödemedir. Dolayısıyla bu yöntem zincir analizinde belirsizlikler yaratır, hatta yanlış ipuçlarına yol açar.



Alice, Bob ve Boulanger örneğini ele alalım. Blok zincirindeki işlem şu şekilde görünecektir:



![image](assets/fr/03.webp)



Genel zincir analizi sezgiselliğine güvenen dışarıdan bir gözlemci yanlış bir şekilde "*Alice ve Bob, her biri bir UTXO ve her biri iki UTXO ile küçük bir coinjoin yaptı*" sonucuna varabilir.



![image](assets/fr/04.webp)



Bu yorum yanlıştır, çünkü bildiğiniz gibi Boulanger'e bir UTXO gönderilmiştir, Alice'nin sadece bir değişim çıkışı vardır ve Bob'nin iki çıkışı vardır.



![image](assets/fr/01.webp)



Dışarıdan bir gözlemci Stonewall x2 işleminin muhatabını tespit etmeyi başarsa bile, tüm bilgilere sahip olmayacaktır. Aynı tutardaki iki UTXO'dan hangisinin ödemeye karşılık geldiğini belirleyemeyecektir. Ödemeyi Alice'ün mü yoksa Bob'ün mü yaptığını da belirleyemeyecektir. Son olarak, girilen iki UTXO'nun iki farklı kişiye mi ait olduğunu yoksa bunları birleştiren tek bir kişiye mi ait olduğunu belirleyemeyecektir. Bu son nokta, yukarıda tartışılan klasik Stonewall işlemlerinin Stonewall x2 işlemleriyle tamamen aynı paterne uyması gerçeğinden kaynaklanmaktadır. Dışarıdan bakıldığında ve ek bağlamsal bilgi olmadan, bir Stonewall işlemini bir Stonewall x2 işleminden ayırt etmek imkansızdır. Birincisi işbirliğine dayalı işlemler değilken, ikincisi öyledir. Bu da harcamalara daha da fazla şüphe katmaktadır.



![image](assets/fr/05.webp)




## Paynym'ler arasında nasıl bağlantı kurabilirim?



Ashigaru'daki (*Cahoots*) diğer işbirlikçi işlemlerde olduğu gibi, Stonewall x2, gönderen ve işbirlikçi arasında kısmen imzalanmış işlemlerin değişimini içerir. Bu değişim, işbirlikçinizin yanında fiziksel olarak bulunuyorsanız manuel olarak veya Soroban iletişim protokolü kullanılarak otomatik olarak gerçekleştirilebilir.



İkinci seçeneği seçerseniz, bir Stonewall x2 gerçekleştirmeden önce Paynym'ler arasında bir bağlantı kurmanız gerekir. Bunu yapmak için, Paynym'iniz işbirlikçinizin Paynym'ini "*takip*" etmelidir ve bunun tersi de geçerlidir. Bunu nasıl yapacağınızı öğrenmek için bu diğer eğitimin başlangıcını takip edebilirsiniz:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Ashigaru'da nasıl Stonewall x2 işlemi yapabilirim?



Bir Stonewall x2 işlemi gerçekleştirmek için, ekranın sol üst köşesindeki Paynym'inizin resmine tıklayın, ardından `İşbirliği Yap` menüsünü açın. QR kodlarını şahsen değiştirmediğiniz sürece, işlemde sizinle birlikte yer alan kişi de aynısını yapmalıdır.



![Image](assets/fr/06.webp)



İki seçeneğiniz vardır: ödemeyi gönderen sizseniz `Başlat` seçeneğini veya işlemde işbirliği yapan ancak ne ödeme yapan ne de gerçek alıcı olan kişi sizseniz `Katıl` seçeneğini seçin.



![Image](assets/fr/07.webp)



Eğer işbirlikçi rolüne sahipseniz, prosedür çok basittir. Soroban ağı üzerinden uzaktan işbirliği için, `Katıl` seçeneğine tıklayın, kullanmak istediğiniz hesabı seçin, ardından mükellef tarafından gönderilen talebi beklemek için `KAHOOT TALEPLERİNİ BEKLE` düğmesine basın.



![Image](assets/fr/08.webp)



Öte yandan, QR kodu tarama yoluyla yüz yüze işbirliği için, wallet'inizin ana sayfasına gidin, ekranın üst kısmındaki QR kodu simgesine basın, ardından işlemi başlatan ödeyici tarafından sağlanan QR kodunu tarayın.



![Image](assets/fr/09.webp)



Ödeyen rolündeyseniz, yani işlemi başlatan kişi iseniz, `İşbirliği Yap` menüsüne gidin ve ardından `Başlat` seçeneğini seçin.



![Image](assets/fr/10.webp)



İşlem türü için, bir Stonewall x2 gerçekleştirmek istediğimizden, bu seçeneği seçin.



![Image](assets/fr/11.webp)



Daha sonra çevrimiçi işbirliği (*Soroban* aracılığıyla *Cahoots*) veya QR kodu alışverişi ile yüz yüze işbirliği arasında seçim yapabilirsiniz.



![Image](assets/fr/12.webp)



### Cahoots çevrimiçi



Eğer `Online` seçeneğini seçtiyseniz, takip ettiğiniz Paynym'lerden işbirlikçinizi seçin.



![Image](assets/fr/13.webp)



İşlemi ayarla'ya tıklayın, ardından harcamayı yapmak istediğiniz hesabı seçin.



![Image](assets/fr/14.webp)



Bir sonraki sayfada, işlem ayrıntılarını girin: ödemenin gerçek alıcısının adresi, gönderilecek tutar ve ücret oranı. Ardından `İşlem kurulumunu gözden geçir` seçeneğine tıklayın.



![Image](assets/fr/15.webp)



Bilgileri dikkatlice kontrol edin, işbirlikçinizin *Cahoots* isteklerini dinlediğinden emin olun, ardından Soroban aracılığıyla PSBT alışverişini başlatmak için yeşil `İŞLEMİ BAŞLAT` düğmesine tıklayın.



![Image](assets/fr/16.webp)



Her iki katılımcı da işlemi imzalayana kadar bekleyin, ardından Bitcoin ağında yayınlayın.



![Image](assets/fr/17.webp)



### Yüz yüze görüşmeler



Değişimi şahsen yapmak istiyorsanız, `STONEWALL X2` işlem türünü seçin, ardından `Şahsen / Manuel` seçeneğini seçin.



![Image](assets/fr/18.webp)



İşlemi ayarla'ya tıklayın, ardından harcamayı yapmak istediğiniz hesabı seçin.



![Image](assets/fr/19.webp)



Bir sonraki sayfada, işlem ayrıntılarını girin: ödemenin gerçek alıcısının adresi, gönderilecek tutar ve ücret oranı. Ardından `İşlem kurulumunu gözden geçir` seçeneğine tıklayın.



![Image](assets/fr/20.webp)



Ayrıntıları kontrol edin, ardından QR kod tarama yoluyla PSBT alışverişine başlamak için yeşil renkli `İŞLEM BAŞLAT` düğmesine basın.



![Image](assets/fr/21.webp)



Değişim, işbirlikçi ile dönüşümlü olarak tarama yapılarak gerçekleştirilir: QR kodunuzu işbirlikçinize göstermek için `SHOW QR CODE` üzerine tıklayın, o da QR kodunuzu tarayacaktır. Ardından o da kendi QR kodunu görüntülemek için `SHOW QR CODE` seçeneğine tıklayacak ve siz de `LAUNCH QR Scanner` ile tarayacaksınız. Beş değişim adımı da tamamlanana kadar bu işlemi tekrarlayın.



![Image](assets/fr/22.webp)



Tüm değişimler tamamlandıktan sonra, işlem ayrıntılarını kontrol edin ve ardından ekranın altındaki yeşil oku sürükleyerek bırakın.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Yapısı aşağıdaki gibidir:



![Image](assets/fr/24.webp)



*Kredi: [mempool.space](https://mempool.space/)*



Portföyümden sırasıyla `91,869 sats` ve `64,823 sats` olmak üzere iki girdi gözlemleyebiliriz, diğer iki girdi ise işbirlikçimin wallet'undan gelmektedir. Çıktı tarafında, `100,000 sats`lik bir UTXO gerçek alacaklıya gönderilir ve `100,000 sats` ve `159,578 sats`lik iki UTXO işbirlikçimin portföyüne geri döner. Girdiye yatırdığı fonların tamamını geri aldığı için (katkıda bulunduğu mining maliyetleri hariç) bu işlem onun için nötrdür. Son olarak, toplam girdilerim ile alıcıya gönderilen `100,000 sats` ödemesi arasındaki farka karşılık gelen `56,270 sats` tutarında bir UTXO değişimi alıyorum.



Açıkçası, bu yapıyı tanımlayabilirim çünkü işlemi kendim oluşturdum. Ancak dışarıdan bir gözlemci için, hangi UTXO'ların hangi katılımcıya ait olduğunu belirlemek genellikle imkansızdır.



Bitcoin'de zincir üzerinde gizlilik yönetimi hakkındaki bilgilerinizi derinleştirmek için Plan ₿ Academy'deki BTC 204 eğitimimi almanızı tavsiye ederim:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c