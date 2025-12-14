---
name: Ashigaru - Stowaway
description: Ashigaru'da nasıl Payjoin işlemi yapabilirim?
---
![cover](assets/cover.webp)



> *Blok zinciri casuslarını bildiklerini düşündükleri her şeyi yeniden düşünmeye zorlayın.*

Payjoin, ödeme alıcısı ile doğrudan işbirliğini içererek kullanıcı gizliliğini artırmak için tasarlanmış bir Bitcoin işlem yapısıdır. Uygulanmasını kolaylaştırmak ve süreci otomatikleştirmek için çeşitli uygulamalar mevcuttur. Bunlardan en iyi bilineni şüphesiz başlangıçta Samurai Wallet ekibi tarafından geliştirilen ve şimdi fork Ashigaru'ya entegre edilen Stowaway'dir.



## Stowaway nasıl çalışır?



Daha önce de belirtildiği gibi Ashigaru, `Stowaway` adlı bir PayJoin aracını entegre etmektedir. Bu, Android'deki Ashigaru uygulamasında mevcuttur. Bir Payjoin'in gerçekleştirilebilmesi için alıcının (aynı zamanda işbirlikçi rolünü de üstlenen) Stowaway ile uyumlu bir yazılım kullanıyor olması gerekir, yani şu an için yalnızca Ashigaru.



Stowaway, Samurai'nin "Cahoots" olarak adlandırdığı bir işlem kategorisine dayanmaktadır. Bir Cahoot, Bitcoin blok zinciri dışında bilgi alışverişini içeren, birkaç kullanıcı arasındaki işbirliğine dayalı bir işlemdir. Ashigaru şu anda iki Cahoots aracı sunmaktadır: Stowaway (Payjoins) ve StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Cahoots işlemleri, kullanıcılar arasında kısmen imzalanmış işlemlerin değiş tokuş edilmesini gerektirir. Bu süreç, özellikle uzaktan gerçekleştirildiğinde uzun ve sıkıcı olabilir. Bununla birlikte, ortak çalışanlar aynı konumdaysa bunu manuel olarak yapmak hala mümkündür. Somut olarak bu, iki katılımcı arasında değiş tokuş edilen beş QR kodunun art arda taranmasını içerir.



Uzak mesafelerde bu yöntem çok karmaşık hale gelmektedir. Samourai bunu düzeltmek için "*Soroban*" adında Tor tabanlı şifreli bir iletişim protokolü geliştirdi. Soroban sayesinde, Payjoin için gerekli alışverişler otomatikleştirilir ve arka planda gerçekleşir.



Bu şifreli iletişimler, Cahoot katılımcıları arasında bir bağlantı ve kimlik doğrulaması gerektirir. Soroban'ın kullanıcıların Paynym'lerine güvenmesinin nedeni budur. Paynym'lerin nasıl çalıştığını henüz bilmiyorsanız, daha fazla bilgi edinmek için bu özel eğitime bir göz atın:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

Özetle Paynym, wallet'nızla ilişkilendirilen ve şifreli alışverişler de dahil olmak üzere çeşitli işlevleri etkinleştirmenizi sağlayan benzersiz bir tanımlayıcıdır. Bir resimle birlikte bir tanımlayıcı şeklini alır. Burada, örneğin, Testnet'te kullandığım bir tanımlayıcı var:



![Image](assets/fr/01.webp)



**Özetlemek gerekirse:**





- payjoin" = Spesifik işbirliğine dayalı işlem yapısı;





- `Stowaway` = Ashigaru'da mevcut Payjoin uygulaması;





- `Cahoots` = Samourai tarafından tüm işbirlikçi işlem türlerine verilen isim, özellikle de bugün Ashigaru'da devralınan Payjoin `Stowaway`;





- soroban = Tor üzerinde kurulan ve `Cahoots` işleminde diğer kullanıcılarla işbirliğine izin veren şifreli iletişim protokolü;





- paynym" = Bir "Chahoots" işlemi gerçekleştirmek amacıyla "Soroban" üzerinde başka bir kullanıcıyla iletişim kurmak için kullanılan benzersiz wallet tanımlayıcısı.



Payjoins'in nasıl çalıştığına ve onchain gizliliğindeki kullanışlılığına daha derinlemesine bakmak için bu diğer öğreticiyi tavsiye ederim:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Paynym'ler arasında nasıl bağlantı kurabilirim?



Başlamak için elbette Ashigaru'yu yüklemeniz ve bir :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Ashigaru aracılığıyla PayJoin (*Stowaway*) dahil olmak üzere uzaktan bir Cahoots işlemi gerçekleştirmek için, önce Paynym'lerini kullanarak işbirliği yapmak istediğiniz kullanıcıyı "takip etmeniz" gerekir. Kaçak yolcu söz konusu olduğunda bu, bitcoin göndermek istediğiniz kişiyi takip etmek anlamına gelir. Başka bir Paynym'i nasıl takip edeceğinizi henüz bilmiyorsanız, ayrıntılı prosedürü bu eğitimde bulabilirsiniz:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Ashigaru'da nasıl Payjoin yapabilirim?



Bir Stowaway işlemi gerçekleştirmek için, ekranın sol üst köşesindeki Paynym'inizin resmine tıklayın ve ardından `İşbirliği Yap` menüsünü açın. QR kodlarını şahsen değiştirmediğiniz sürece, işlemde sizinle birlikte yer alan kişi de aynısını yapmalıdır.



![Image](assets/fr/02.webp)



İki seçeneğiniz vardır: ödemeyi gönderen sizseniz `Başlat` seçeneğini veya bu ödemenin alıcısı sizseniz `Katıl` seçeneğini seçin.



![Image](assets/fr/03.webp)



Alıcı sizseniz, prosedür çok basittir. Soroban ağı üzerinden uzaktan işbirliği için, `Katıl` seçeneğine tıklayın, kullanmak istediğiniz hesabı seçin, ardından ödeyici tarafından gönderilen talebi beklemek için `KAHOOT TALEPLERİNİ BEKLE` düğmesine basın.



![Image](assets/fr/04.webp)



Öte yandan, QR kodu tarama yoluyla yüz yüze işbirliği için, wallet'unuzun ana sayfasına gidin, ekranın üst kısmındaki QR kodu simgesine basın ve ardından işlemi başlatan ödeyici tarafından sağlanan QR kodunu tarayın.



![Image](assets/fr/05.webp)



Ödeyen rolündeyseniz, yani işlemi başlatan kişi iseniz, `İşbirliği Yap` menüsüne gidin ve ardından `Başlat` seçeneğini seçin.



![Image](assets/fr/06.webp)



İşlem türü için, bir Payjoin Stowaway yapmak istediğimizden, bu seçeneği seçin.



![Image](assets/fr/07.webp)



Daha sonra çevrimiçi işbirliği (*Soroban* aracılığıyla *Cahoots*) veya QR kodu alışverişi ile yüz yüze işbirliği arasında seçim yapabilirsiniz.



![Image](assets/fr/08.webp)



### Cahoots çevrimiçi



Eğer `Online` seçeneğini seçtiyseniz, takip ettiğiniz Paynym'lerden alıcıyı seçin.



![Image](assets/fr/09.webp)



İşlemi ayarla'ya tıklayın, ardından harcamayı yapmak istediğiniz hesabı seçin.



![Image](assets/fr/10.webp)



Bir sonraki sayfada işlem ayrıntılarını girin: alıcıya gönderilecek tutar ve ücretlendirme oranı. Alıcı adresi girmenize gerek yoktur, çünkü alıcı PSBT alışverişleri sırasında bunu kendisi iletecektir.



Ardından `İşlem kurulumunu gözden geçir` seçeneğine tıklayın.



![Image](assets/fr/11.webp)



Bilgileri dikkatlice kontrol edin, işbirlikçinizin *Cahoots* isteklerini dinlediğinden emin olun, ardından Soroban aracılığıyla PSBT alışverişini başlatmak için yeşil `İŞLEMİ BAŞLAT` düğmesine tıklayın.



![Image](assets/fr/12.webp)



Her iki katılımcı da işlemi imzalayana kadar bekleyin, ardından Bitcoin ağında yayınlayın.



![Image](assets/fr/13.webp)



### Yüz yüze görüşmeler



Değişimi şahsen yapmak istiyorsanız, `STONEWALL X2` işlem türünü seçin, ardından `Şahsen / Manuel` seçeneğini seçin.



![Image](assets/fr/14.webp)



İşlemi ayarla'ya tıklayın, ardından harcamayı yapmak istediğiniz hesabı seçin.



![Image](assets/fr/15.webp)



Bir sonraki sayfada, işlem ayrıntılarını girin: alıcıya gönderilecek tutar ve ücret oranı. Alıcı adresi girmenize gerek yoktur, çünkü alıcı PSBT alışverişleri sırasında bunu kendisi iletecektir.



Ardından `İşlem kurulumunu gözden geçir` seçeneğine tıklayın.



![Image](assets/fr/16.webp)



Ayrıntıları kontrol edin, ardından QR kod tarama yoluyla PSBT alışverişine başlamak için yeşil renkli `İŞLEM BAŞLAT` düğmesine basın.



![Image](assets/fr/17.webp)



Değişim, işbirlikçi ile dönüşümlü olarak tarama yapılarak gerçekleştirilir: QR kodunuzu işbirlikçinize göstermek için `SHOW QR CODE` üzerine tıklayın, o da QR kodunuzu tarayacaktır. Ardından o da kendi QR kodunu görüntülemek için `SHOW QR CODE` seçeneğine tıklayacak ve siz de `LAUNCH QR Scanner` ile tarayacaksınız. Beş değişim adımı da tamamlanana kadar bu işlemi tekrarlayın.



![Image](assets/fr/18.webp)



Tüm değişimler tamamlandıktan sonra, işlem ayrıntılarını kontrol edin ve ardından ekranın altındaki yeşil oku sürükleyerek bırakın.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Yapısı aşağıdaki gibidir:



![Image](assets/fr/20.webp)



*Kredi: [mempool.space](https://mempool.space/)*



Bu işlemi analiz edersek, girdi tarafında benim 164,211 sats`lık UTXO`imi ve ödemenin gerçek alıcısına ait 190,002 sats`lık UTXO`i görürüz. Çıktı tarafında ise ben 63,995 sats`lık bir değişim UTXO'i alırken, alıcı 290,002 sats`lık bir UTXO alır. Girdi ve çıktıları karşılaştırdığımızda, alıcının gerçekten de benim gerçek ödeme miktarıma karşılık gelen `100,000 sats` kazandığını ve benim de mining maliyetlerini eklediğim `100,000 sats` kaybettiğimi görebiliriz.



Açıkçası, bu yapıyı tanımlayabilirim çünkü işlemi kendim oluşturdum. Ancak dışarıdan bir gözlemci için, hangi UTXO'ların hangi katılımcıya ait olduğunu belirlemek genellikle imkansızdır.



Bitcoin'de zincir üzerinde gizlilik yönetimi hakkındaki bilgilerinizi derinleştirmek için Plan ₿ Academy'deki BTC 204 eğitimimi almanızı tavsiye ederim:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c