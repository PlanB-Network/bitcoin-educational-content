---
name: IbexPay
description: Ödemeleri bitcoin olarak kabul edin ve yerel para birimine dönüştürün.
---
![cover](assets/cover.webp)



Bitcoin'ı herkes için kullanılabilir hale getirmek, aynı zamanda kullanışlılığını ve işinize nasıl mükemmel bir şekilde uyduğunu göstermek anlamına gelir.  Bitcoin'ın gücünü göstermek için dünyanın her yerinden ödeme toplamanıza izin vermekten daha iyi bir yol olabilir mi?  Bu eğitimde, bitcoin'i hem fiziksel mağazanızda hem de e-ticaret platformunuzda bir ödeme aracı olarak entegre etmenizi sağlayan basit bir platform olan IbexPay'e göz atacağız.



## IbexPay ile çalışmaya başlama



IbexPay, Lightning altyapı hizmetlerinde öncü olan IBEX tarafından geliştirilen bir platformdur. Bir hesap edinmek için IbexPay [resmi platform](https://www.ibexpay.io/) adresine gidin ve "**Başlat**" düğmesine tıklayın.



![start](assets/fr/01.webp)



İşletmenizle ilgili çeşitli bilgileri doldurun, ardından mağaza kurduğunuz ülkeyi seçin: bu adım, ödemeleri toplamak için kullanılacak para birimi için önemlidir.



![register](assets/fr/02.webp)



Ne yazık ki, IbexPay çoğu Afrika ülkesi için mevcut değildir, ancak Avrupa, Asya ve Amerika'da birçok seçenek vardır.



Kaydınızı onayladığınızda, hesabınız için bir şifre belirleyebilmeniz amacıyla size bir e-posta gönderilecektir. Hassas ticari bilgilerinizi korumak için lütfen güçlü bir şifre belirleyin.



![passe](assets/fr/03.webp)



## Hesabınızı yapılandırın



IbexPay, Bitcoin (onchain ve Lightning) aracılığıyla ödemeleri çok hızlı bir şekilde kurmanıza ve toplamaya başlamanıza olanak tanıyan minimalist, akıcı bir platformdur.



Giriş yaptıktan sonra, gösterge paneli size işletmenizin nakit makbuz verilerine ilişkin özelleştirilebilir bir genel bakış sunar.



Bu gösterge tablosundan şunları yapabilirsiniz





- Günlük, aylık, yıllık veya özelleştirilmiş bir dönem boyunca işlem geçmişini görüntüleyin;
- Muhasebe amaçları için geçmişi Excel formatında (CSV) dışa aktarın;
- Kişisel adresinize gönderilecek toplam satoshis miktarına bakın;
- Hesabınızda bulunan yerel para birimi karşılığını kontrol edin.




![dashboard](assets/fr/04.webp)




Ayarlar** menüsünde, işletmeniz için gerekli tüm bilgileri yapılandırın: kişisel adresleriniz, şirket belgeleriniz vb.



Bu bölümde, bitcoin onchain alıcı adresinizi ve Lightning adresinizi yapılandırabilirsiniz. Bu iki bilgi yararlıdır, çünkü IbexPay her 24 saatte bir o günkü işlemlerinizin toplam tutarını doğrudan yapılandırılmış bitcoin onchain adresinize aktaracaktır.



![addresses](assets/fr/05.webp)



Bu bilgiler IbexPay ekibi tarafından doğrulanacaktır. Bu doğrulama tamamlandıktan sonra, işlem başına nakde çevirmek istediğiniz bitcoin yüzdesini tanımlama seçeneğiniz de vardır. Örneğin, Lightning aracılığıyla 20 avroluk bir ödeme için, Bitcoin yüzdeniz %30 olarak ayarlanmışsa, IbexPay bu tutarı 6 avro eşdeğeri bitcoin olarak gönderecek, ardından FIAT bakiyenizde 14 avro mevcut olacaktır.



![percent](assets/fr/06.webp)



IbexPay, bakiyenizi yerel para biriminde ödemek için banka bilgilerinize de ihtiyaç duyacaktır. Ödemelerinizi almak için banka hesap bilgilerinizi ayarlayın.



![bank](assets/fr/07.webp)



Birden fazla mağazanız varsa, her mağazanız için bir hesap oluşturabilir ve işlemleri aynı IbexPay arayüzünden ayrı ayrı takip edebilirsiniz.



![accounts](assets/fr/08.webp)



Ayrıca her bir hesabınıza (mağazanıza) farklı bir yönetici atayabilirsiniz. Bunu yapmak için **Yöneticiler** menüsünde mağaza sorumlusunun adını ve e-posta adresini girerek bir mağaza yöneticisi oluşturun. Bu yönetici, kendisine atanan mağazayı yönetmesi için otomatik olarak bir e-posta daveti alacaktır.



![manager](assets/fr/09.webp)



Hesaplar** menüsünde, **Süpervizör ata** düğmesine tıklayarak bir süpervizörü bir mağazaya bağlayabilirsiniz.



![assign](assets/fr/10.webp)



Ardından mağazayı (hesabı) ve belirlenen amiri seçin ve bağlantı düğmesine tıklayın.



![link](assets/fr/11.webp)



## Bitcoin ödeme terminalleri



BTP'ler** (*Bitcoin Ödeme Terminalleri*) sekmesinde, mağazanızın kasasında kullanmak üzere bir satış noktası sayfası oluşturabilirsiniz. BTP Ekle** düğmesine tıklayın, ardından :




- Terminal adı ;
- bu terminalle ilişkili mağaza;
- kullanılacak yerel para birimi.



Ödeme terminaliniz oluşturulduktan sonra, sizi ödeme arayüzüne yönlendirecek bağlantıya tıklayın.



![btps](assets/fr/12.webp)



![interface](assets/fr/13.webp)



Artık müşterilerinizin ve ortaklarınızın ödeyebileceği Lightning faturaları oluşturmaya başlayabilirsiniz. Arayüzdeki IbexPay logosuna tıkladığınızda, herhangi bir cihazda IbexPay POS'u almak için akıllı telefonunuzda tarayabileceğiniz bir QR kodu alırsınız.



![smartphone](assets/fr/14.webp)



![phone](assets/fr/15.webp)



![invoices](assets/fr/16.webp)




![integrations](assets/fr/17.webp)



## Çevrimiçi mağazalara entegrasyon



IbexPay fiziksel mağaza konumlarınızla sınırlı değildir. Entegrasyonlar** menüsünde, IbexPay ile ilişkili tüm e-ticaret platformlarını ve ödeme çözümlerini bulabilirsiniz. Özellikle, IbexPay hesabınızı :





- Özelleştirilmiş e-ticaret siteniz için API;
- WooCommerce ;
- Shopify;
- Zaprite;
- TiloPay;
- ve IbexPay bağış sayfaları.



![integrations](assets/fr/18.webp)



Artık işletmenizde Bitcoin'yı sadece birkaç dakika içinde kabul etmenizi sağlayan bir araca sahipsiniz. Kendi kendine saklama çözümlerini tercih ediyorsanız, Breez POS gibi araçlar için eğitimlerimize bir göz atın:



https://planb.academy/tutorials/business/point-of-sale/breez-pos-76d6bf36-f4b5-422e-8579-edf149021525

Ayrıca, bitcoin ödemeleriyle ilgili en iyi uygulamaları öğrenmek ve Bitcoin'yi işletmenize entegre ederken nakit akışınızı nasıl etkili bir şekilde yöneteceğinizi anlamak için işletmeler için kapsamlı BIZ 101 kursumuza göz atın:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a