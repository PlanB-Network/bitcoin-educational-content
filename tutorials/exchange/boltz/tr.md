---
name: Boltz
description: Kontrolü korurken farklı Bitcoin katmanları arasında geçiş yapın.
---


![cover](assets/cover.webp)



Bitcoin'nin eşler arası elektronik nakit sistemi, 2009'daki dağıtımından bu yana katlanarak büyüdü ve bugün özellikle Lightning Network aracılığıyla günlük eylemlerimizde anında kullanabileceğimiz bir sistem olmasını sağlayan çözümlere hayat verdi.



Ancak, Bitcoin protokol katmanları arasında büyük bir sorun devam ediyordu: akışkan birlikte çalışabilirliği. Bitcoin'ün tüm potansiyelinden faydalanmak için, protokolün farklı katmanları arasında işlem yapılmasını sağlayacak bir çözüm bulmak zorunluydu. Bu ihtiyaç, 2019 yılında birkaç Bitcoin katmanını birbirine bağlayan bir köprü olan Boltz'un ortaya çıkmasına neden oldu.



## Boltz nedir?



[Boltz] (https://boltz.Exchange), Bitcoin protokolünün farklı katmanları arasında işlem yapmak isteyen herkes için ideal, gözetim dışı bir platformdur:




- on chain**: İşlemlerin ortalama her 10 dakikada bir onaylandığı Bitcoin'nin ana zincirinde işlem ücretleri genellikle yüksektir ve bu da kullanıcıların ihtiyaçlarını karşılamamaktadır;
- Lightning Network**: Düşük ücretlerle anında ödemeler için Bitcoin kaplaması, Bitcoin'un günlük ödemeler için kullanılmasına olanak tanır;
- Liquid Network**: Blockstream tarafından oluşturulan, hızlı, Confidential Transactions ve diğer Bitcoin tabanlı finansal araçların kullanımını sağlayan Bitcoin için bir kaplama;
- RootStock**: Bitcoin protokolüne dayalı akıllı sözleşmeler geliştirmek için bir çözüm.



![layers](assets/fr/01.webp)



Bu farklı katmanlar arasındaki birlikte çalışabilirlik, kullanıcılara Bitcoin ekosisteminin sunduğu her şeyden tam olarak yararlanmaları için ihtiyaç duydukları esnekliği sağladığından büyük önem taşımaktadır.



Boltz atomik takas kullanır. Bu teknoloji, bitcoinlerin 2 katman arasında (örneğin Exchange'teki BTC onchain ile Lightning'deki BTC) doğrudan iki taraf arasında, güvene ve bir aracıya ihtiyaç duymadan takas edilmesini sağlar. Bu değiş tokuşlar "atomik" olarak adlandırılır çünkü yalnızca iki sonuç üretebilirler:




- Ya Exchange başarılı olur ve iki katılımcı BTC'lerini etkin bir şekilde takas etmiş olur;
- Ya Exchange başarısız olur ve her iki katılımcı da orijinal BTC'leriyle ayrılır.



Bu şekilde, bitcoinlerinizin kalıcı öz emanetini elinizde tutarsınız ve Exchange karşı tarafa herhangi bir güvene dayanmaz: Exchange başarılı olur ya da başarısız olur, ancak taraflardan hiçbiri diğerinin fonlarını çalamaz.



Atomik bir Exchange akıllı sözleşmelerle çalışır [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). Bu tür bir Contract'da, miktar iki yönlü bir kanalda "kilitlenir" ve bir zaman kısıtlaması getirilir, böylece işlem belirli bir süre içinde tamamlanmazsa, bakiye yatırana geri döner. Boltz platformu tarafından kullanılan mekanizma budur.



## Boltz ile ilk alışverişleriniz



Boltz, sizden hiçbir kişisel bilgi istemeyen, depozitosuz bir web platformudur. Boltz, bir dakikadan daha kısa sürede işlem yapmaya başlamanızı sağlayan minimalist, akıcı bir Interface'ye sahiptir.



![boltz](assets/fr/02.webp)



Platforma girdikten sonra, Bitcoin ekosisteminin farklı katmanları arasında atomik alışverişler oluşturabilirsiniz.



![home](assets/fr/03.webp)



Ağ ücretleri ve Boltz tarafından alınan %0,1 ile %0,5 arasındaki bir yüzde dahil olmak üzere Boltz aracılığıyla ticaret yapabileceğiniz minimum ve maksimum satoshi (en küçük Bitcoin birimi) sayısını göreceksiniz.



![fees](assets/fr/04.webp)



Ardından, atomik bir Exchange yapmak istediğiniz Layer'yı seçin ve bitcoinleri almak istediğiniz Layer'yı seçin.



![couches](assets/fr/05.webp)



Bu eğitimde, ana Layer'dan Lightning Network'ye atomik Exchange'e odaklanacağız.



Seçenekler arasından seçim yaparak baz üniteyi borsalarınız için yapılandırabilirsiniz:




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Temel yapılandırmalarınızı tamamladıktan sonra, atomik Exchange miktarınızı girin, ardından eşdeğer miktar için bir Lightning Invoice oluşturun veya sadece LNURL'nizi girin.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



Güvenli tarafta olmak için, lütfen Exchange'ünüze bağlı yedek anahtarları dışa aktarmak üzere atomik Exchange'ünüzün parametrelerini kontrol edin.



Ayarlar** simgesinde, yedekleme anahtarını indirin ve dosyayı uygun şekilde kaydedin.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



Bu dosya, atomik borsalarınızla ilişkili portföyün 12 anahtar kelimesini içerir.



Ardından **Create atomic Exchange** düğmesine tıklayın ve belirtilen tutarın ödemesine devam edin.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Ödemeniz yapıldıktan ve onaylandıktan sonra, eşdeğer tutarı otomatik olarak Lightning Wallet'inize alacaksınız.



Geri Ödeme** menüsünde, geri ödeme yapmak istediğiniz Exchange'yı belirlemek için atomik Exchange geçmişinizi bulun. Ayrıca, örneğin bu değişimlerle ilişkili yedek anahtar dosyasını kullanarak başka bir cihazda yaptığınız değişimlerin geçmişini de içe aktarabilirsiniz.



![refund](assets/fr/11.webp)



Geçmiş** menüsünde, **Yedekle** düğmesine tıklayarak kurtarma anahtarınızla ilişkili değişimlerin daha ayrıntılı bir geçmişini indirebilirsiniz.



![backup](assets/fr/12.webp)



⚠️ İşlemlerinizle ilgili tüm bilgileri ve bu işlemlere bağlı yedekleme anahtarını içerdiğinden lütfen bu dosyayı da ifşa etmeyin.



Boltz, Tor ağındaki bir `.onion` bağlantısı üzerinden erişimi sayesinde size yüksek düzeyde gizlilik sunar. Tarayıcınızda Tor taramasını etkinleştirdikten sonra **Onion** menüsünü seçerek atomik alışverişleri tamamen anonim hale getirin.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Şimdiye kadar Exchange ekosisteminin farklı katmanları arasında birlikte çalışabilirliği sağlayan benzersiz bir Bitcoin platformu olan Boltz'a aşina olmuşsunuzdur.