---
name: Lightning Network+
description: Lightning düğümünüzdeki kooperatif açıklıkları ile ücretsiz gelen likidite elde edin
---

![cover](assets/cover.webp)



## Giriş



[LN+ (Lightning Network Plus)](https://lightningnetwork.plus/), Lightning Network düğüm operatörleri arasındaki işbirliğini kolaylaştırmak için tasarlanmış bir topluluk platformudur. Temel amacı, merkezi aracılara ihtiyaç duymadan Lightning ağının bağlanabilirliğini, likiditesini ve merkezsizleştirilmesini geliştirmektir.



Bu eğitim, günümüzde LN+'ın en yaygın kullanılan ve yapılandırma özelliği olan **"Swaps "** hizmetine odaklanacaktır. Platform tarafından sunulan diğer hizmetler de sunulacaktır.



## LN+ genel bakış



### Lightning Network Plus nedir?



Lightning Network Plus (LN+), doğrudan ve gönüllü olarak işbirliği yapmak isteyen Lightning düğüm operatörleri için bir topluluk platformudur. Merkezi çözümlere veya dayatılan merkezlere olan ihtiyacı ortadan kaldırırken faydalı, dengeli ve sürdürülebilir Lightning kanallarının oluşturulmasını kolaylaştırmayı amaçlamaktadır.



LN+ temel bir ilkeye dayanmaktadır: şeffaflık, karşılıklılık ve itibar üzerine kurulu eşler arası işbirliği.



### Bir bakışta LN+ hizmetleri



LN+, Lightning ağının topolojisini ve likiditesini iyileştirmek için tasarlanmış çeşitli hizmetler sunar:





- Takas**: operatörler arasında kanalların karşılıklı olarak açılması (ana hizmet).
- Halkalar**: birkaç katılımcı arasında dairesel kanal açıklıkları.
- Güvene dayalı takaslar**: Katılımcıların güvenine ve geçmişine daha fazla dayanan varyantlar.
- Sosyal özellikler**: profiller, yorumlar ve itibar sistemi.



Bu eğitimin geri kalanında, yalnızca mevcut LN+ kullanımının merkezinde yer alan **Swaps** hizmetine odaklanacağız.



## LN+ "Takas" hizmeti



### LN+ takasının tanımı



Bir LN+ **takas**, iki Lightning düğümü operatörü arasında eşdeğer (veya önceden kararlaştırılmış) kapasitede Lightning kanallarını karşılıklı olarak açmak için yapılan gönüllü bir anlaşmadır. Geleneksel tek taraflı kanal açmanın aksine, takas **açık karşılıklılığa** dayanır.



Uygulamada :





- Ortağınızın düğümüne bir kanal açarsınız.
- Ortağınız düğümünüze bir kanal açar.
- Her iki taraf da benzer miktarda on-chain bitcoin bağlamaktadır.



### Düğüm operatörleri için takasların amacı nedir?



Swap hizmeti, Lightning operatörlerinin karşılaştığı birkaç temel sorunu ele almaktadır:





- Geliştirilmiş bağlantı**: açılır açılmaz faydalı çift yönlü kanalların oluşturulması.
- Daha iyi likidite yönetimi**: her bir tarafın hem gelen hem de giden kapasitesi vardır.
- Gereksiz kanal riskinin azaltılması**: Ortak, kanalı açık tutmaya teşvik edilir.
- Daha fazla ademi merkeziyet**: operatörler arasında, dayatılmış merkezler olmadan doğrudan bağlantılar.



### Takaslar hangi düğüm profilleri için yararlıdır?



Takaslar özellikle şunlar için yararlıdır :





- Yönlendirilebilirliklerini hızla geliştirmek isteyen yeni düğümler.
- Kanal grafiklerinin yoğunluğunu artırmak isteyen aracı operatörler.
- Topolojilerini optimize etmek isteyen yönlendirme odaklı düğümler.



## Lightning düğümünüzü LN+'ya bağlayın



### Teknik gereksinimler



Başlamadan önce, ihtiyacınız olacak :





- Çalışan bir Lightning düğümü (LND, Core Lightning veya Eclair).
- Düğümünüzün yönetim arayüzüne erişim.
- Kanalları açmak için yeterli on-chain kapasitesi.



Lightning Network](https://lightningnetwork.plus/) Plus web sitesine gidin ve arayüzün sağ üst köşesindeki `Login` düğmesine tıklayın.



![capture](assets/fr/03.webp)



### Mesaj imzası ile kimlik doğrulama



Kimliğinizi doğrulamak için, Lightning düğümünüzün özel anahtarını kullanarak sağlanan mesajı imzalamanız gerekir. ThunderHub ile bu işlem çok basittir.



LN+ tarafından görüntülenen mesajı kopyalayarak başlayın.



![capture](assets/fr/04.webp)



ThunderHub'de `Araçlar` sekmesine gidin, ardından `Mesajlar` bölümündeki `İmzala` düğmesine tıklayın.



![capture](assets/fr/05.webp)



LN+ tarafından sağlanan kimlik doğrulama mesajını yapıştırın ve ardından `İmzala` düğmesine tıklayın.



![capture](assets/fr/06.webp)



ThunderHub daha sonra düğümünüzün özel anahtarını kullanarak bu mesajı imzalar. Oluşturulan imzayı kopyalayın.



![capture](assets/fr/07.webp)



Bu imzayı LN+ sitesindeki ilgili alana yapıştırın ve ardından `Sign in` (Oturum aç) düğmesine tıklayın.



![capture](assets/fr/08.webp)



Artık Lightning düğümünüzle LN+'ya bağlısınız. Bu işlem, LN+'nın platformlarında talep ettiğiniz düğümün gerçek sahibi olduğunuzu doğrulamasını sağlar.



![capture](assets/fr/09.webp)



Dilerseniz LN+ profilinizi, örneğin kısa bir biyografi ekleyerek kişiselleştirebilirsiniz.



## Mevcut bir takasa katılın



### Takas tekliflerine erişim



İlk kanal açılışınıza katılmak için, arayüzün üst kısmındaki `Takaslar' menüsüne gidin. Burada, düğümünüzün özelliklerine bağlı olarak şu anda mevcut olan tüm takasları bulacaksınız.



![capture](assets/fr/10.webp)



### Uygunluk koşulları



Mevcut bir takas teklifine katılmak için ilgili reklamı seçip kaydolmanız yeterlidir. Bununla birlikte, LN+, takas oluşturucunun aşağıdakiler gibi belirli **uygunluk koşullarını** tanımlamasına izin verir:





- halihazırda açık olan minimum sayıda kanal;
- minimum toplam düğüm kapasitesi ;
- belirli bağlantı türleri kabul edilir.



### Son düğümler



Sonuç olarak, özellikle kullanımın ilk aşamalarında, düğümünüz için **çok az teklif mevcut olabilir veya hiç teklif olmayabilir**. Bu, yeni düğümler veya henüz bağlanmamış olanlar için yaygın bir durumdur.



Benim durumumda, birkaç açık kanal olmasına rağmen, tekliflerin hiçbiri gerekli kriterleri karşılamadı.



## Kendi takas teklifinizi oluşturun



### Kendi takasınızı ne zaman oluşturmalısınız?



Mevcut bir teklif bulunmadığında, kendi takasınızı oluşturmak genellikle en iyi çözümdür. Ayrıca takasın parametreleri üzerinde kontrol sahibi olmanızı sağlar.



### Takas yapılandırması



Liquidity Swap'ı Başlat** seçeneğine tıklayın, ardından teklif parametrelerinizi yapılandırın:





- toplam katılımcı sayısını seçin (3, 4 veya 5);
- açılacak kanalların kapasitesini gösterir;
- katılımcıların kanallarını kapatmamayı kabul ettikleri taahhüt süresini tanımlar;
- katılımcılar için geçerli olan kısıtlamaları belirtiniz (minimum kanal sayısı, minimum toplam kapasite, kabul edilen bağlantı türü).



![capture](assets/fr/11.webp)



### Yayın ve katılımcıların beklentileri



Tüm parametreler girildikten sonra, teklifinizi yayınlamak için **Liquidity Swap'ı Başlat** seçeneğine tıklayın. Şimdi tek yapmanız gereken diğer operatörlerin kaydolmasını beklemek.



![capture](assets/fr/12.webp)



## Takasın sonuçlandırılması



### Etkin kanal açıklığı



Artık tüm takas pozisyonları alındığına göre, her katılımcı LN+ arayüzünden hangi düğüme bir Lightning kanalı açması gerektiğini görebilir.



![capture](assets/fr/13.webp)



Kendi tarafınızda, LN+ tarafından sağlanan Node ID'yi kullanarak ve belirtilen miktara uyarak kanalı açın. Bu işlem ThunderHub, başka bir Lightning düğüm yöneticisi veya doğrudan düğümünüzün temel arayüzü üzerinden gerçekleştirilebilir.



![capture](assets/fr/14.webp)



Kanal açıldıktan sonra bekleyen kanallar bölümünde görünür.



![capture](assets/fr/15.webp)



### LN+'da Onaylama



Ardından LN+'a geri dönerek `Kanal Açma Başlatıldı` düğmesine tıklayarak kanal açmayı başlattığınızı onaylayın.



![capture](assets/fr/16.webp)



### Takasın sonu



Tüm katılımcılar taahhüt ettikleri kanalları açtıklarında takas tamamlanmış sayılır.



## İtibar ve iyi iletişim uygulamaları



### LN+ itibar sistemi



LN+, takasların sonunda katılımcılar tarafından bırakılan görüşlere dayanan bir itibar sistemi içermektedir. Bu görüşler kamuya açıktır ve bir operatörün gelecekteki takaslara katılma veya takas oluşturma yeteneğini doğrudan etkiler.



![capture](assets/fr/17.webp)



### Önerilen en iyi uygulamalar



İyi bir itibarı korumak ve takas işlemlerinin sorunsuz bir şekilde yürütülmesini sağlamak için, :





- kanal açma sürelerine saygı gösterin ;
- bir sorun veya gecikme durumunda hızlı bir şekilde iletişim kurun;
- diğer katılımcılarla görüş alışverişinde bulunmak için yorumlar bölümünü kullanın;
- taahhüt süresinin bitiminden önce bir kanalı kapatmamak.




![capture](assets/fr/18.webp)



### İtibar neden LN+'nın merkezinde yer alır?



LN+, güçlü teknik kısıtlamalar olmaksızın gönüllü işbirliği modeline dayanmaktadır. Bu nedenle itibar, katılımcıların güvenilirliğini ve güvenilirliğini sağlamak için ana teşviktir.



## Diğer LN+ hizmetleri



Takaslara ek olarak LN+, Lightning düğüm operatörleri arasındaki bağlantı ve koordinasyonu geliştirmek için tasarlanmış başka hizmetler de sunmaktadır. Halkalar** birkaç katılımcının kanal açıklıklarından oluşan bir döngü oluşturmasını sağlayarak yönlendirme yollarının fazlalığını ve Lightning grafiğinin yoğunluğunu güçlendirir. Güvene dayalı takaslar** klasik takaslara benzer ilkelere dayanır, ancak platformda zaten yerleşik bir itibara sahip olan katılımcılara daha fazla esneklik sunar.



LN+ ayrıca herkese açık düğüm profilleri, takas yorumları ve itibar sistemi gibi sosyal özellikleri de entegre etmektedir. Bu araçlar kendi başlarına teknik hizmetler değildir, ancak platformun sorunsuz çalışmasında merkezi bir rol oynar, operatörler arasındaki iletişimi, koordinasyonu ve güveni kolaylaştırır.



## Sonuç



LN+'ın Takas hizmeti, Lightning ağında bağlanabilirliği, likiditeyi ve merkezsizleşmeyi geliştirmek için etkili bir araçtır. LN+, karşılıklı, koordineli kanal açılışlarını teşvik ederek düğüm operatörlerinin topolojilerini güçlendirmelerini sağlarken aynı zamanda sorumlu, merkezi olmayan işbirliğini de teşvik eder.