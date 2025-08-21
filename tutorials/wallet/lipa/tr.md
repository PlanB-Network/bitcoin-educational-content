---
name: Lipa
description: Lipa lightning mobil Wallet'ın kurulumu ve kullanımı
---
![cover](assets/cover.webp)


Bitcoin Lightning Wallet, Bitcoin'ün Lightning Network'i üzerinde anında, düşük maliyetli işlemler yapılmasını sağlayan bir mobil uygulamadır. Ana Blockchain (On-Chain) üzerindeki işlemlerin aksine, Lightning ödemeleri neredeyse anlıktır ve minimum ücret gerektirir, bu da onları özellikle küçük, günlük ödemeler için uygun hale getirir.


Lightning cüzdanları, tüm mobil cüzdanlar gibi, internete bağlı oldukları için "Hot" cüzdanları olarak kabul edilir. Bu nedenle, öncelikle günlük harcamalarınız için küçük miktarlarda para yönetmek için tasarlanmıştır. Daha büyük miktarlar için donanım cüzdanları gibi daha güvenli depolama çözümlerinin kullanılması tercih edilir.


Lightning Network hakkında daha fazla bilgi edinmek ve teknik olarak nasıl çalıştığını anlamak istiyorsanız, bu kursa katılmanızı tavsiye ederim:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Bu eğitimde, İsviçre'de geliştirilen basit ve etkili bir Lightning Wallet olan **Lipa**'ya göz atacağız.


## Karşınızda Lipa


Lipa, kullanım kolaylığı ve düzenli Interface ile ayırt edilen, gözetim altında olmayan bir Lightning Wallet'dur. İsviçreli bir ekip tarafından geliştirilen bu ürün, yeni başlayanlar için gizliliği ve kullanım kolaylığını vurgular.


Temel özellikler şunlardır:




- Sezgisel kullanıcı Interface
- Otonom Lightning kanal yönetimi
- LNURL protokol desteği
- Doğrudan uygulama içinden bitcoin satın alma imkanı


## Lipa'nın yüklenmesi ve yapılandırılması


İlk adım Lipa uygulamasını indirmektir. Şu an için sadece iOS'ta mevcut:




- [Apple için](https://apps.apple.com/app/lipa-Bitcoin-lightning/id1602180066)


Android sürümü şu anda geliştirilme aşamasındadır ve yakında kullanıma sunulacaktır.


![Installation de Lipa](assets/fr/01.webp)


Uygulamayı başlattıktan sonra, size iki seçenek sunan ana ekrana ulaşacaksınız:




- Yeni bir Wallet oluşturun
- Mevcut bir Wallet'ü bir yedekten geri yükleme


Seçeneğinizi belirledikten sonra, uygulama sizden bildirimleri etkinleştirmenizi ister. Bu adım önemlidir, çünkü bildirimler :




- Uygulama kapalı olsa bile ödemeler alındığında uyarılar alın
- Entegre çözümleri aracılığıyla Bitcoin satın almanın içerdiği adımlar hakkında bilgi sahibi olun


Uygulama daha sonra bir dizi tanıtım ekranı aracılığıyla ana işlevlerini sunar:




- Sorunsuz ödeme makbuzu**: Kullanıcılar uygulama kapalıyken bile Bitcoin ödemelerini alabilir, böylece güvenilirlik ve kolaylık garanti edilir.
- Gözetim altında olmayan Lightning adresleri**: Lipa artık velayetsiz Lightning adreslerini destekliyor ve kullanıcılara bitcoinleri üzerinde tam kontrol sağlayarak gizliliği ve güvenliği artırıyor.
- Analitik veriler üzerinde kontrol** : Şeffaflık ve gizlilik her şeyden önemli olduğundan, kullanıcılar toplanan veri türlerini görüntüleyebilir ve paylaşım tercihlerini seçebilirler.
- Telefon numarasıyla gönderin**: Karmaşık adreslere gerek yok - sadece bir kişi seçin, miktarı girin ve bitcoinleri doğrudan telefon numaralarına gönderin.


Uygulama ayrıca, optimum kullanıcı deneyimini garanti etmek için kararlılık, güvenlik ve güvenilirlik açısından sürekli iyileştirmelerden yararlanmaktadır.


## Uygulama navigasyonu


Lipa's Interface, ekranın altındaki gezinme çubuğu aracılığıyla erişilebilen 4 ana sekme etrafında düzenlenmiştir:


![Navigation principale](assets/fr/02.webp)




- Ana Sayfa**: Mevcut bakiyenizi ve işlem geçmişinizi görüntüler
- Tarayıcı**: Ödeme yapmak için QR kodlarını taramanızı sağlar
- Harita**: Bölgenizdeki Bitcoin kabul eden işletmelerin interaktif bir haritasını görüntüler
- Ayarlar**: Uygulama ayarlarına, yedeklemeye ve tercihlere erişim


Ana ekranı aşağı çekerek ek bir menüye erişilebilir:


![Menu supplémentaire](assets/fr/03.webp)


Bu hareket, aşağıdaki gibi ek işlevleri ortaya çıkarır:




- Bitcoin satın almak
- On-Chain Bitcoin mevduat
- Bitcoin almak için Lightning faturaları oluşturma
- Yıldırım Invoice ödemesi


## Wallet'nizi kaydedin


Wallet'ünüzü yedeklemek için "Ayarlar" sekmesine gidin ve "Kurtarma ifadesi "ni seçin. Lipa, fiziksel bir ortama (kağıt, metal) dikkatlice yazılması gereken bir kurtarma ifadesi kullanır. Bu ifade, telefonunuzun kaybolması veya çalınması durumunda paranızı kurtarmanın tek yoludur. Yedeklemenizi doğrulamak için uygulama sizden ifadenizden rastgele 3 kelimeyi onaylamanızı isteyecektir.


![Backup](assets/fr/04.webp)


Kurtarma ifadenizi nasıl düzgün bir şekilde yedekleyeceğiniz ve yöneteceğiniz hakkında daha fazla bilgi için, özellikle de yeni başlayan biriyseniz, bu diğer öğreticiyi izlemenizi şiddetle tavsiye ederim:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Bitcoin alma


Bitcoin almak için iki seçeneğiniz vardır. Bu seçeneklere erişmek için ana ekrana dönün ve ekranı aşağı çekin. Sonra ya yapabilirsiniz :




- On-Chain bitcoinlerini almak için "BTC Transfer Et" seçeneğini seçin. Ardından QR kodunu diğer Wallet'inizle tarayın ve işlemi tamamlayın.
- Lightning Network aracılığıyla almak için "Talep Et" seçeneğini seçin ve almak istediğiniz tutarı girin.


Her iki durumda da, tutarın %0,4'üne eşdeğer bir ücret veya uygulamanın yeni bir ödeme kanalı açması gerekiyorsa (ilk ödeme için kaçınılmaz olarak böyle olacaktır) yaklaşık 2.500 Sats ödemeniz gerekecektir.


![Recevoir des bitcoins on chain](assets/fr/05.webp)


![Recevoir des bitcoins lightning](assets/fr/06.webp)


## Bitcoin gönder


Bitcoin göndermek için ana ekrana gidin, ekranı aşağı çekin ve "Öde "yi seçin. Sonra basitçe ya :




- bir yıldırım LNURL Address girin
- ödemeyi yapmak için bir yıldırım QR kodunu tarayın.


Bir QR kodunu doğrudan taramak için ekranın altındaki ikinci sekmeye de gidebilirsiniz.


![Envoi de bitcoins](assets/fr/07.webp)


## Bitcoin satın alın


Lipa, %1,5'lik bir ücret karşılığında doğrudan uygulama üzerinden bitcoin satın alma imkanı sunmaktadır. Bir satın alma işlemi yapmak için ana ekrana gidin ve menüyü görüntülemek için aşağı çekin. Ardından "BTC Satın Al "ı seçin. Üç tanıtım ekranı, satın alma işlemi boyunca size rehberlik edecektir.


![Menu d'achat](assets/fr/08.webp)


Ardından, satın alma işlemini gerçekleştirmek için kullanacağınız hesabın banka bilgilerini girmeniz yeterlidir. Para biriminizi seçin ve Address e-postanızı girin.


Yükleme ekranından sonra, yapmak üzere olduğunuz havaleye dahil edilecek referans numarasını ve Exchange için banka bilgilerini bulacaksınız.


![Sélection du montant](assets/fr/09.webp)


Tek yapmanız gereken, istediğiniz tutarı transfer etmek için bankanızı kullanmak, daha önce alınan RIB'yi belirterek transferi ayarlamak ve Lipa'nın bu banka hareketini Lipa Wallet'inizle ilişkilendirebilmesi için işlem sırasında referansı belirtmektir.


![Confirmation d'achat](assets/fr/10.webp)


## Avantajlar ve dezavantajlar


### Avantajlar




- Sezgisel Interface
- Doğru hizmet ücretleri
- Gözetim dışı
- Entegre Bitcoin satın alma çözümü
- BTCmap entegrasyonu
- NFC desteği


### Dezavantajlar




- on chain bitcoin göndermek mümkün değil
- Ortalama ödemeden biraz daha uzun


Lipa, Lightning Network'e başlamak için mükemmel bir seçimdir ve özellikle günlük ödemeler için basit bir çözüm arayan kullanıcılar için uygundur. Kullanım kolaylığı ve düzenli Interface, günlük Lightning kullanımı için temel özellikleri sunarken, yeni başlayanlar için ideal bir Wallet olmasını sağlar.


## Kaynaklar




- [Lipa'nın resmi web sitesi](https://lipa.swiss/)
- [Lipa desteği](https://getlipa.atlassian.net/servicedesk/customer/portal/1)