---
name: 1ML
description: Bitcoin'ın Lightning ağını anlamak ve analiz etmek için 1ML gezginini nasıl kullanacağınızı öğrenin.
---
![cover](assets/cover.webp)



## Giriş



Lightning Network, Bitcoin'nin üzerine inşa edilmiş hızlı, düşük maliyetli bir ödeme çözümüdür ve anında, güvenli işlemlere olanak sağlar. Bu ağı gözlemlemek, nasıl çalıştığını, topolojisini ve onu oluşturan düğümlerin durumunu anlamak için çok önemlidir. 1ML gibi bir Lightning gezgini, aktif düğümler, açık kanallar ve mevcut kapasite dahil olmak üzere ağın genel verilerini görselleştirmek için kullanılır ve kullanıcılar, geliştiriciler ve düğüm operatörleri için değerli bir genel bakış sağlar.



## 1ML'ye erişin ve ana sayfayı anlayın



1ML'ye erişmek için web tarayıcınızı açın ve [https://1ml.com](https://1ml.com) yazın. Bu sizi Lightning Network'ün küresel kontrol paneli olarak hizmet veren ana sayfaya götürür.



![capture](assets/fr/03.webp)



Bu sayfa, ekranın üst kısmında aşağıdakiler de dahil olmak üzere birkaç önemli istatistik görüntüler:





- Ağdaki **toplam aktif düğüm sayısı**, yani Lightning ödemelerini gönderip alan bilgisayarlar.
- Bu düğümler arasında fon transferlerine olanak sağlayan bağlantılara karşılık gelen **açık kanal sayısı**.
- Bitcoin (BTC) cinsinden ifade edilen ve tüm genel kanalların kapasitelerinin toplamını gösteren **toplam ağ kapasitesi**.



Bu rakamlar ağın mevcut durumunu yansıtacak şekilde düzenli olarak güncellenmektedir. Ağın büyüklüğü, büyümesi ve sağlamlığı hakkında bir fikir vermektedir.



![capture](assets/fr/04.webp)



Sayfanın hemen altında, sıralamaları içeren listeler bulunmaktadır:





- Diğer düğümlere en fazla açık kanala sahip olan **en bağlantılı düğümler**.
- Düğümlerdeki **en yüksek kapasiteler**, hangi düğümlerin en büyük miktarları aktarabileceğini gösterir.
- Kapasite açısından en önemli kanallar.



Bu listeleri coğrafi konum veya diğer kriterlere göre daraltmak için filtreler de kullanılabilir.



Bu sayfa, Lightning Network'ü keşfetmek ve genel topolojisini anlamak için ideal bir başlangıç noktasıdır.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Lightning düğümlerini keşfetme



1ML'de bir düğümü keşfetmek için, sayfanın üst kısmındaki arama çubuğunu kullanarak başlayın. Düğümün benzersiz tanımlayıcısı olan **Node ID** veya hatırlanması daha kolay bir isim olan **alias** girebilirsiniz.



Arama tamamlandıktan sonra, ayrıntılı sayfasına erişmek için ilgili düğüme tıklayın.



![capture](assets/fr/07.webp)



Bu sayfada birkaç önemli bilgi görüntülenir:





- Düğüm Kimliği**: Bu benzersiz tanımlayıcı, düğümün ağ boyunca tam olarak tanımlanmasını sağlayan uzun bir karakter dizisidir.



![capture](assets/fr/08.webp)





- Takma ad**: Bu, düğüm sahibi tarafından düğümü herkese açık olarak temsil etmesi için seçilen addır.



![capture](assets/fr/09.webp)





- Kanal sayısı** düğümün diğer düğümlerle kaç tane açık bağlantısı olduğunu gösterirken, **toplam kapasite** bu kanallarda bulunan bitcoinlerin toplamını temsil eder. Çok sayıda kanala ve yüksek kapasiteye sahip bir node genellikle iyi bağlantılara sahiptir ve ağ üzerinden büyük miktarlarda parayı hızlı bir şekilde aktarabilir.



![capture](assets/fr/10.webp)





- Kullanılabilirlik ya da **uptime**, bir düğümün ne kadar süre aktif ve erişilebilir kaldığını ölçerek güvenilirliğini yansıtır. Öte yandan düğümün **yaş** değeri, ağda ne kadar süredir bulunduğunu gösterir ve Lightning Network içindeki istikrarını ve deneyimini yansıtır.



![capture](assets/fr/11.webp)



Bu veriler, Lightning Network'daki bir düğümün önemini ve güvenilirliğini anlamanıza yardımcı olur. Örneğin, çok sayıda kanala, yüksek kapasiteye ve yüksek çalışma süresine sahip bir düğüm genellikle ağda önemli bir oyuncudur.



## Yıldırım kanallarını keşfetme



### Lightning kanalı nedir?



Lightning kanalı, iki ağ düğümü arasında doğrudan bir bağlantıdır. Bu iki düğümün, her işlem için Bitcoin ana zincirinden geçmeden anında, düşük maliyetli ödemeler yapmasını sağlar. Kanallar, Lightning Network'yi hızlı ve ölçeklenebilir kılan temel unsurlardır.



### 1ML ile ilgili kanal bilgilerini okuyun



1ML'de, her kanalın bir dizi önemli veri içeren kendi sayfası veya açıklama sayfası vardır:



Bir düğümün sayfasından, kanallarının bir listesine erişebilirsiniz. Bir kanala tıkladığınızda, 1ML birkaç önemli bilgi içeren özel bir sayfa görüntüler.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



Görünen ana veriler aşağıdaki gibidir:





- Ortak düğümler**: her kanal iki düğümü birbirine bağlar. 1ML hem tanımlayıcıları hem de ilgili takma adlarını görüntüler.



![capture](assets/fr/14.webp)





- Kanal kapasitesi**: Bu, bu kanalda kilitli olan toplam bitcoin miktarıdır. Bu kapasite, bu kanaldan geçebilecek maksimum ödeme limitini temsil eder.



![capture](assets/fr/15.webp)





- Kanal yaşı**: kanalın ne kadar süredir açık olduğunu gösterir. Eski bir kanal genellikle iki düğüm arasındaki istikrarlı bir ilişkinin işaretidir.



![capture](assets/fr/16.webp)



### Kanal görünürlük sınırları



1ML'nin Lightning Network'un sadece **bir kısmını** gösterdiğini anlamak önemlidir. Gezgin yalnızca **genel kanalları**, yani ağda duyurulmuş olanları gösterir. Genellikle gizlilik veya strateji nedenleriyle kullanılan özel kanallar görünmez. Ayrıca, 1ML bir kanalın her bir tarafındaki fonların tam dağılımını, yapılan ödemeleri veya belirli bir anda gerçekte mevcut olan likiditeyi göstermez. Bu nedenle, görüntülenen bilgiler ağın **genel yapısını** analiz etmek için kullanılabilir, ancak gerçek finansal faaliyetini veya ayrıntılı likidite durumunu analiz etmek için kullanılamaz.



## Lightning Network'u konuma göre keşfedin



### Ülke ve bölgelere göre düğümler



1ML, Lightning Network'i **coğrafi dağılıma** göre keşfetmenize olanak tanır. Ana sayfadan veya özel bölümler aracılığıyla düğümleri ülke veya bölgeye göre görüntülemek mümkündür. Bu özellik, düğüm operatörleri tarafından beyan edilen konum bilgilerine dayanmaktadır.


Gezinti çubuğunda **Lokasyon** bağlantısını göreceksiniz. Sayfada düğümler kıta, ülke ve şehre göre gruplandırılmıştır.



![capture](assets/fr/17.webp)



Bir ülke seçildiğinde, 1ML ilgili düğümlerin bir listesini ve söz konusu coğrafi alan için düğüm sayısı ve toplam görünür kapasite gibi toplu istatistikleri görüntüler.



#### Bu durum yerel evlat edinme hakkında ne söylüyor?





- Teknolojinin benimsenmesi**: Bir bölgedeki çok sayıda düğüm, Bitcoin kullanıcılarının, şirketlerinin veya hizmetlerinin Lightning Network'yi aktif olarak benimsediğini gösterir. Bu, teknolojik olgunluğu ve Lightning'in avantajlarından (hızlı işlemler, daha düşük maliyetler) yararlanma isteğini gösterir.
- Ekonomik ekosistem** : Düğümlerin yoğun varlığı, Bitcoin etrafında yerel bir ekonomik dokuya da işaret edebilir: Lightning kabul eden tüccarlar, araç geliştiren girişimler, topluluk etkinlikleri vb.
- Güvenlik ve esneklik**: Farklı coğrafi dağılım, yerel kesintiler veya kısıtlamalar karşısında ağın dayanıklılığını artırır. Düğümler ne kadar dağınık olursa, ağ o kadar merkezsizleşir ve sansürlenmesi zorlaşır.
- Politikalar ve düzenlemeler**: Bazı ülkelerde elverişli bir düzenleyici çerçeve veya proaktif bir topluluk sayesinde daha hızlı benimsenme görülebilir. Tersine, düzenlemelerin katı veya düşmanca olduğu bölgelerde düğüm sayısı daha düşük olacaktır.



#### Coğrafi verilerin sınırları



Bununla birlikte, Lightning düğümlerinin coğrafi konumunun sınırları ve önyargıları olduğunu unutmayın:





- Yaklaşık IP konumu**: 1ML, konumlarını tahmin etmek için genellikle düğümlerin genel IP adresini kullanır. Ancak bu yöntem VPN'lerin, bulut sunucularının (AWS, Google Cloud) kullanılması veya düğüm sahibinin gerçek ikametgahından farklı ülkelerde barındırılması nedeniyle bozulabilir.
- Sanal düğümler**: Bazı operatörler, güvenilirlik ve kullanılabilirlik nedenleriyle düğümlerini uzak sunucularda barındırır ve bu da yanlış bir fiziksel konum hissi verebilir.
- Kullanıcı hareketliliği**: Bir düğüm operatörü konum değiştirebilir, altyapısını taşıyabilir veya farklı bölgelerde birkaç düğüm açabilir, bu da veri okumayı daha karmaşık hale getirir.
- Özel düğümlerin görünmezliği**: Bazı düğümler IP adreslerini yayınlamaz veya konumlarını gizlemek için yöntemler kullanır, bu da coğrafi konumu imkansız hale getirir.



## 1ML somut kullanım örnekleri



### Ağ topolojisini anlama



1ML, Lightning Network'in **genel yapısını** görselleştirmenizi sağlar. Düğümler arasındaki bağlantıları, kanal sayısını ve toplam kapasiteyi gözlemleyerek, ağın nasıl organize edildiğini, hangi düğümlerin merkezi bir rol oynadığını ve ödeme akışlarının teorik olarak nasıl dolaşabileceğini anlamak mümkündür.



Bu anlayış, sadece portföy kullanımı için değil, Lightning Network'nın nasıl çalıştığını anlamak için de gereklidir.



### Önemli düğümleri belirleyin



1ML tarafından sunulan sıralamalar (en çok bağlı düğüm, en yüksek kapasite, yaş) sayesinde, ağda önemli bir yer tutan düğümleri tespit etmek mümkündür. Bu düğümler genellikle Lightning ödemeleri için büyük ağ geçitleri olarak hizmet vermektedir.



![capture](assets/fr/18.webp)



### Bir düğümün genel görünürlüğünü kontrol edin



Bir düğüm operatörü için 1ML, düğümünüzün Lightning Network'de **genel olarak ilan edilip edilmediğini** kontrol etmenizi sağlar. Eğer bir düğüm 1ML'de görünüyorsa, bu onun görünür olduğu ve diğer düğümler tarafından genel kanallar açmak için erişilebilir olduğu anlamına gelir.


Bu, görünürlük veya bağlantı sorunlarını teşhis etmek için yararlı olabilir.



### Lightning Network'in zaman içinde gelişimini izlemek



Farklı dönemlerdeki küresel istatistikleri karşılaştırarak 1ML, Lightning Network'un evrimini gözlemlememizi sağlar: düğüm sayısındaki artış veya azalış, toplam kapasitedeki değişimler veya coğrafi dağılımdaki değişiklikler.


Bu gözlemler Lightning Network'nin büyümesi, olgunlaşması ve eğilimleri hakkında ilginç bir bakış açısı sunmaktadır.



## 1ML en iyi uygulamaları ve sınırlamaları



### Kamuya açık veri ≠ tam gerçeklik



1ML yalnızca Lightning Network ile ilgili **kamuya açıklanan** verilere dayanmaktadır. Bu, aracın gerçeğin yalnızca bir kısmını gösterdiği anlamına gelir. Birçok kanal özel olabilir, bazı düğümler ilan edilmemiş olabilir ve kanallarda mevcut olan gerçek likidite görünmez. Bu nedenle 1ML'yi ağın kapsamlı bir temsili olarak değil, küresel bir analiz aracı olarak kullanmak önemlidir.



### Gizlilik ve Yıldırım



Lightning Network, **ödeme gizliliğine** güçlü bir şekilde odaklanılarak tasarlanmıştır. Bireysel işlemler 1ML'de görünmez ve tam kanal bakiyeleri herkese açık değildir. Bu sınırlama gezginin bir hatası değil, kullanıcıların gizliliğini korumak için tasarlanmış Lightning Network'nin temel bir özelliğidir.



### Hemen sonuca varmayın



Yüksek kapasiteli ya da çok kanallı bir düğümün her durumda daha "güvenilir" ya da "verimli" olması gerekmez. Benzer şekilde, genel ağ kapasitesindeki geçici bir düşüş, mutlaka yapısal bir sorun olduğu anlamına gelmez. Rakamlar her zaman geriye dönük olarak yorumlanmalı ve bir bağlama oturtulmalıdır.



### Diğer araçlarla tamamlayıcılık



1ML, Lightning Network'ü keşfetmek için mükemmel bir başlangıç noktasıdır, ancak en iyi şekilde Lightning portföyleri, düğüm yönetimi arayüzleri ve diğer kaşifler gibi diğer araçlarla birlikte kullanılır. Bu yaklaşım, ağın daha eksiksiz ve incelikli bir görünümünü sağlar.



## 1ML bağlantı seçeneği (gelişmiş işlevsellik)



1ML, sitede görülebilen bir **log-in / create account** seçeneği sunar, ancak Lightning Network verilerini görüntülemek için bu **gerekli değildir**. Bu eğitimde şimdiye kadar tartışılan tüm özellikler **hesap olmadan** kullanılabilir.



Bağlantı öncelikle **Lightning düğüm operatörlerine** yöneliktir. Özellikle, düğümün sunumu, iletişim bağlantıları ve diğer meta veriler gibi belirli genel bilgileri yönetmek için bir düğümün bir 1ML hesabıyla ilişkilendirilmesini sağlar. Bu özellik, gezgin içinde bir düğümün görünürlüğünü ve tanımlanmasını iyileştirmek için tasarlanmıştır.



1ML'nin **bir saklama hizmeti** olmadığını unutmamak önemlidir. Bir hesabın oluşturulması, bir düğümün fonlarına, kanallarına veya ödemelerine erişim sağlamaz. Yalnızca bildirimsel ve bilgilendirici bir bakış açısıyla gezginle etkileşime girmeye yarar.



Lightning Network'i öğrenme veya keşfetme bağlamında, bu seçenek bu nedenle **isteğe bağlı** olarak kabul edilebilir ve daha ileri düzey kullanım için ayrılmıştır.



## Sonuç



1ML, Lightning Network'yı kamuya açık verilerinden gözlemlemek ve anlamak için değerli bir araçtır. Ağın yapısını keşfetmenize, düğümleri ve kanalları analiz etmenize ve zaman içinde Lightning Network'nın benimsenmesinin genel gelişimini izlemenize olanak tanır. Bir hesaba veya fon kullanımına ihtiyaç duymadan 1ML, Lightning'in nasıl çalıştığına dair anlayışlarını derinleştirmek isteyen herkes için erişilebilir bir ağ geçidi sunar.


Lightning Network ile daha ileri gitmek istiyorsanız, Lightning Network'ye Giriş kursunun tamamını tavsiye ederim:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb