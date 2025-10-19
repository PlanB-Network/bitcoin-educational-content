---
name: Ginger Wallet
description: Açık kaynaklı, kendi kendini muhafaza eden Bitcoin Wallet yazılımı, Wasabi Wallet'den Fork, Coinjoins entegrasyonu
---
![cover](assets/cover.webp)



Ginger Wallet, gizlilik ve mahremiyete odaklanan açık kaynaklı, gözetim dışı bir Bitcoin portföyüdür. Wasabi Wallet'ten Fork olarak hayata başladı (2.0.7.2 sürümünden sonra - MIT lisansı).



Ginger Wallet, Wasabi'nin teknik mimarisini korurken birkaç spesifik özellik ekler. Ginger Wallet belgelerine] (https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet) göre, Wasabi **otonomi ve kontrolü** vurgularken, Ginger **kullanım kolaylığı, güvenlik ve basitleştirilmiş bir deneyime** odaklanarak teknik konulara daha az aşina olanlar için erişilebilir hale getiriyor.



Ginger Wallet sadece bilgisayarlar için Wallet yazılımıdır (mobil uygulama yoktur).



## CoinJoin nedir?



CoinJoin**, birkaç katılımcıyı tek bir ortak işlemde bir araya getiren özel bir Bitcoin işlem yapısı türüdür. Bu mekanizma, farklı kullanıcıların girdilerini ortak bir işlemde karıştırarak fonların izini sürmeyi son derece zorlaştırır - hatta düzgün yapıldığında çoğu zaman imkansız hale getirir. Sonuç olarak, geleneksel Bitcoin işlemlerinin aksine, dışarıdan bir gözlemcinin ilgili bitcoinlerin kaynağını ve hedefini kesin olarak belirlemesi neredeyse imkansız hale gelir.



Siz kullanıcılar için CoinJoin gizliliğinizi korumanıza yardımcı olur. Örneğin, bir Bitcoin Address'te 10.000 Sats'lik bir bağış alırsanız, gönderen bu fonları izleyebilir ve bazı durumlarda daha büyük miktarda bitcoin tuttuğunuz sonucuna varabilir veya faaliyetlerinizi gözlemleyebilir. Bu 10.000 Sats'lik bağışın ardından bir CoinJoin yaparak, izlenebilirliği bozarsınız: gönderen artık bu ödemeden sizin hakkınızda herhangi bir bilgi elde edemez.



Chaumian CoinJoin, fonlar her zaman kullanıcının münhasır kontrolü altında kaldığı için yüksek düzeyde güvenlik sunar. Koordinasyon sunucularının operatörleri bile katılımcıların bitcoinlerini hiçbir koşulda yönlendiremez. Ne kullanıcıların ne de koordinatörlerin birbirlerine güvenmeleri gerekir: her biri kendi özel anahtarlarının kontrolünü elinde tutar ve işlemleri doğrulama yetkisi yalnızca kendilerinde kalır. Dolayısıyla hiçbir üçüncü taraf bir CoinJoin sırasında bitcoinlerinize el koyamaz ya da girdileriniz ve çıktılarınız arasında doğrudan bir bağlantı kuramaz.



CoinJoin hakkında daha fazla bilgi edinmek için Plan ₿ Academy'nin BTC 204 kursuna göz atın:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ginger Wallet'i kurun



Ginger Wallet'u yüklemek için [Ginger Wallet] (https://gingerwallet.io) web sitesini ziyaret edin.



Bilgisayarınız için doğru sürümü (Windows / MacOs / Linux) indirmek için **Download** tuşuna basın.



![screen](assets/fr/03.webp)



Diğer bir seçenek de projeyi indirmek için [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) adresine gitmektir.



![screen](assets/fr/04.webp)



Ardından kurulum programını çalıştırın.



![screen](assets/fr/05.webp)




## Parametre ayarları



### Ön konfigürasyonlar



Ginger Wallet'yi açın, tercih ettiğiniz dili seçin.



![screen](assets/fr/06.webp)



Ginger, en başından itibaren size CoinJoin sürecindeki maliyetleri hatırlatıyor.



![screen](assets/fr/07.webp)



Ardından yeni bir portföy oluşturmak için **Başlat** ve ardından **Yeni** düğmesine basın.



![screen](assets/fr/08.webp)



Ardından, seedphrase'nizi kaydedin ve onaylayın.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Daha fazla güvenlik için Ginger Wallet size bir passphrase ekleme seçeneği sunar.



![screen](assets/fr/11.webp)



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Bu passphrase, eklendikten sonra, portföyünüze her erişmeye çalıştığınızda istenecektir.



![screen](assets/fr/12.webp)



Ginger, portföyünüzü oluşturduğunuzda varsayılan **CoinJoin**'yı otomatik olarak etkinleştirir. Bu konuda bilgilendirilirsiniz ve ardından ayarı ihtiyaçlarınıza uyacak şekilde özelleştirebilirsiniz.



![screen](assets/fr/13.webp)




### Genel ayarlar



İlk portföyünüzü oluşturduktan sonra, Ginger'ın Interface Wallet'ine yönlendirileceksiniz.



![screen](assets/fr/14.webp)



Cüzdanlarınızdaki bakiyeleri gizlemek istiyorsanız **Gizli modu** etkinleştirin.



![screen](assets/fr/15.webp)



Ginger Wallet'da birden fazla portföy oluşturabilirsiniz. Sadece **Portföy ekle** seçeneğine tıklayın.



![screen](assets/fr/16.webp)



Ginger, Bitcoin core standardı Interface aracılığıyla donanım portföylerinin kullanımını destekler, ancak bir donanım portföyünden veya bir donanım portföyüne doğrudan entegrasyon henüz mevcut değildir.



Uyumlu donanım portföyleri şunları içerir (ancak bunlarla sınırlı değildir) :




- BLOCKSTREAM Yeşim
- Coldcard MK4
- Soğuk Kart Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Model T
- Trezor Safe 3
- vs.



Şimdi **Ayarlar** üzerine tıklayın.



![screen](assets/fr/17.webp)



Bu ayarlar genel olarak uygulamanın ayarlarıdır ve burada yaptığınız yapılandırmalar tüm portföyler için geçerli olacaktır.



Ayarlar** içinde sekmeleriniz vardır:





- Genel**



![screen](assets/fr/18.webp)





- Görünüş



Bu sekmede, diğerlerinin yanı sıra dili, para birimini ve ücret görüntüleme birimini (BTC/Satoshi) değiştirebilirsiniz.



![screen](assets/fr/19.webp)





- Bitcoin**



Bu sekme, uygulama başladığında Bitcoin Knots'nin çalışmasını etkinleştirmenizi, ağınızı (Main/RegTest) ve ücretlendirme oranı sağlayıcınızı (Mempool Space/BLOCKSTREAM info/Full node) vb. seçmenizi sağlar.



![screen](assets/fr/20.webp)





- Güvenlik özellikleri**



Güvenlik sekmesinde, iki faktörlü kimlik doğrulamayı etkinleştirebilir, Tor'u etkinleştirebilir veya devre dışı bırakabilir ve hatta Ginger uygulaması kapatıldığında devre dışı bırakabilirsiniz.



![screen](assets/fr/21.webp)



**NB** :




- İki faktörlü kimlik doğrulama için kimlik doğrulama uygulamanızın SHA256 protokolünü ve 8 basamaklı kodları desteklediğinden emin olun. Ginger Wallet, gelişmiş güvenlik için 8 basamaklı bir 2FA kodu gerektirir. Bu uzun format, kodun tahmin edilmesini veya ele geçirilmesini çok daha zor hale getirerek yetkisiz erişime karşı daha fazla koruma sağlar.
- Varsayılan olarak, tüm Ginger ağ trafiği Tor üzerinden geçerek manuel yapılandırma ihtiyacını ortadan kaldırır. Tor sisteminizde zaten etkinse, Ginger otomatik olarak ona öncelik verecektir.



Ancak ayarlardan Tor'u devre dışı bıraktığınızda, iki durum dışında gizliliğiniz genellikle korunur:




- bir CoinJoin sırasında koordinatör giriş ve çıkışlarınızı IP Address'ünüze bağlayabilir;
- bir işlemi yayınlarken, bağlandığınız kötü niyetli bir düğüm işleminizi IP'nizle ilişkilendirebilir.



Ayarlarınızı kaydetmek için her seferinde **Bitti** (sağ alt Coin'te) düğmesine basmayı unutmayın. Bazı ayarların etkili olması için Ginger Wallet'ün yeniden başlatılması gerekir.



Buna ek olarak, portföylerin üst kısmındaki arama çubuğu, herhangi bir parametreyi vb. aramanıza ve bunlara erişmenize olanak tanır.



![screen](assets/fr/22.webp)




### Portföy yapılandırması



Uygulamada birden fazla portföy oluşturulabilir, böylece her portföy ihtiyaçlarınıza göre yapılandırılabilir. Bunu yapmak için, portföy adının önündeki **üç noktaya** ve ardından **Portföy ayarları** seçeneğine tıklayın.



![screen](assets/fr/23.webp)



Gördüğünüz gibi, Wallet parametresinin yanı sıra UTXO'larınızı (sahip olduğunuz jetonların listesi), istatistiklerinizi ve Wallet bilgilerini (örneğin genişletilmiş genel anahtar) görebileceksiniz.



Portföy yapılandırmamıza geri dönmek için, portföy parametrelerine tıkladığınızda, aşağıdaki sekmelere yönlendirileceksiniz:




- Genel** (portföy adını değiştirebileceğiniz yer) ;



![screen](assets/fr/24.webp)





- CoinJoin** (bu portföyün CoinJoin ayarlarını özelleştirebileceğiniz yer) ;



![screen](assets/fr/25.webp)





- Araçlar** (seedphrase'inizi kontrol edebileceğiniz, portföyünüzü tekrar senkronize edebileceğiniz veya silebileceğiniz yer).



![screen](assets/fr/26.webp)




## Bitcoin alma



Ginger Wallet'da Wallet'unuzdaki bitcoinleri almak için:




- al** tuşuna basın;



![screen](assets/fr/27.webp)





- Address'i ilişkilendirmek istediğiniz kaynağın adını girin. Bu, ödemelerinizi takip etmek için etiketlemedir. Bunun hiçbir On-Chain etkisi yoktur; sadece uygulamanızda yerel olarak depolanan izlenebilirlik bilgisidir;



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- gW-53 formatınızı (**SegWit** /**Taproot**) seçmek için **generate**'nin solundaki küçük oka tıklayın, ardından generate'ye bir Address ve QR kodu için **generate**'ye tıklayın.



![screen](assets/fr/29.webp)



Bu Address veya QR kodu, göndericiniz tarafından size bitcoin göndermek için kullanılacaktır.



![screen](assets/fr/30.webp)




## Bitcoin gönder



Ginger Wallet ile nasıl gönderim yapılacağına dair video eğitimi.



![Vidéo](https://youtu.be/2nf5aAimfhg)



Bunu yapmak için :




- Gönder** düğmesine basın;
- alıcının Address numarasını, gönderilecek tutarı ve bir etiket girin;
- işlem genel görünümünü kontrol edin ve göndermek için onaylayın.



![screen](assets/fr/31.webp)




## Bitcoin harcayın



Ginger Wallet ile Bitcoin almak ve satmak çok kolay. Sadece birkaç adımda bitcoinlerinizi harcayabilirsiniz.



### Bitcoin satın alın



Ginger Wallet kullanıcıları bitcoin satın alabilir.





- Satın Al** düğmesine basın. Bu düğme Wallet boş olsa bile görünür kalır.



![screen](assets/fr/32.webp)





- Bitcoin satın alma işlemine başlamadan önce ülkenizi ve hatta eyaletinizi (Kanada gibi bazı bölgelerde) seçin. Aslında, **Satın Al** işlevine ilk kez tıkladığınızda, bölgenizi de belirtmeniz gerekecektir.



![screen](assets/fr/33.webp)



Satın alma sürecinde ilerlemek için **Devam** düğmesine basın.





- Ardından, özel alana satın almak istediğiniz bitcoin miktarını girin. İşlem para birimini de seçebilirsiniz.



![screen](assets/fr/34.webp)



Her para biriminin minimum ve maksimum satın alma limiti vardır. Örneğin, ABD doları cinsinden maksimum limit 30.000 ABD dolarıdır.



Daha önce bir satın alma işlemi gerçekleştirdiyseniz, **Önceki siparişler** düğmesine tıklayarak işlem geçmişinizi görüntüleyebilirsiniz. Geçmiş işlemlerin bir listesi ve durumları görüntülenecektir.





- Sizin için doğru olan teklifi seçin.



Bu noktada, mevcut tüm tekliflerin bir listesini göreceksiniz. Her teklif için, sahip olduğunuz :




 - tedarikçi adı (1) ;
 - daha önce girilen tutara eşdeğer bitcoin sayısı, ödeme yöntemi ve satın alma ücreti (2);
 - kabul** düğmesine (3) basın.



![screen](assets/fr/35.webp)



Teklifte belirtilen ücretler ek bir maliyet teşkil etmez. Bunlar zaten teklifin toplam tutarına dahildir.



Ekranın sağ üst Coin kısmında yer alan **Tüm** etiketi, teklifleri ödeme yöntemine göre filtrelemenizi sağlar. Seçtiğiniz ödeme yöntemi varsayılan olarak ayarlanacaktır, ancak istediğiniz zaman değiştirilebilir.



![screen](assets/fr/36.webp)



Uygun bir teklif bulursanız, satın alma işlemine devam etmek için **Kabul Et** düğmesine tıklayın. Daha sonra işlemi tamamlayabileceğiniz satıcının sayfasına yönlendirileceksiniz.



### Bitcoin satmak



Ginger Wallet kullanıcıları Bitcoin'i satabilir. Sat** düğmesi yalnızca portföyde kullanılabilir fon olduğunda görünür.





- Sat** üzerine tıklayın.



![screen](assets/fr/37.webp)





- Satın Al** seçeneğinde olduğu gibi, Sat işlevini ilk kez kullandığınızda, bir Bitcoin satışına devam etmeden önce ülkenizi seçmeniz gerekir.





- Ardından, satmak istediğiniz Bitcoin miktarını girmeniz gerekir. Bu tutarı BTC veya ABD doları (USD) gibi bir fiat para birimi cinsinden girebilirsiniz.





- Bunu yaptıktan sonra, mevcut tekliflerin bir listesini göreceksiniz. Size uygun bir satış teklifi seçin, ardından devam etmek için **Kabul Et** seçeneğine tıklayın.





- Şimdi işlemi sonuçlandırmanız gerekiyor:
 - Bir teklifi kabul ettiğinizde, tedarikçinin sayfasına yönlendirileceksiniz;
 - Tedarikçi sayfasındaki talimatları izleyin;
 - Bir noktada, bir alıcı Address ve gönderilecek tam miktar alacaksınız;
 - Ardından işleme devam etmek için Ginger Wallet'a dönün;
 - Ginger Wallet'e geri döndüğünüzde, **Gönder** seçeneğine tıklayarak devam etmenizi sağlayan bir iletişim kutusu görünecektir.



Bu, alıcının Address'i ve önceden doldurulmuş tutar ile **Gönder** ekranını açacaktır. Ana ekrandaki **Gönder** düğmesini de kullanabilirsiniz. İşlemi manuel olarak gönderebilmenize rağmen, optimize edilmiş bir süreç için iletişim kutusu aracılığıyla tamamlamanızı öneririz.



## Ginger Wallet üzerinde bir CoinJoin yapın



![Vidéo](https://youtu.be/AJe67RDfB1A)



Doğrudan Ginger Wallet'ya entegre edilmiş **CoinJoin** ile bitcoinlerinizin gizliliğini koruyun. Wallet, daha erişilebilir ve verimli coin birleşmelerini kolaylaştırmak için tasarlanmış bir Chaumian CoinJoin protokolü olan **WABISABI** kullanır.



Size en uygun CoinJoin stratejisini (otomatik veya manuel) seçmek size kalmış.



Ginger CoinJoin, indirir indirmez kullanıma hazırdır (ek adım gerekmez). Ginger CoinJoin, her işlemde gizliliğinizi korumak için otomatik olarak arka planda çalışır. Uygulamada, anonimleştirilebilecek bir bakiyeniz olduğunda CoinJoin okuyucu görünecektir.



CoinJoin'in manuel olarak başlatılmasına gelince, bu tek tıklamalı bir işlemdir. Turu başlatın ve CoinJoin işleminin oluşturulmasını ve onaylanmasını bekleyin. Interface'da anonimleştirme skorunu göreceksiniz.



İstenilen anonimlik seviyesine ulaşılana kadar birkaç karışım gerçekleştirilebilir. Ayrıca belirli kısımları karışımın dışında bırakabilirsiniz.



Varsayılan olarak Ginger, önceden yapılandırılmış tüm parametreler ve garantili ücretlerle kendi koordinatörünü kullanır. Değeri 0,03 BTC'den fazla olan tokenların Coinjoin'leri, Mining ücretine ek olarak %0,3 koordinatör ücretine tabidir. 0,03 BTC veya daha düşük girişlerin yanı sıra remiksler, tek bir işlemden sonra bile koordinatör ücretlerinden muaftır. Bu nedenle, CoinJoin fonlarıyla yapılan bir ödeme, hem göndericinin hem de alıcının koordinatör ücretlerine tabi olmadan coinlerini yeniden karıştırmasına olanak tanır.



Ginger, daha küçük ve daha hızlı turlar yerine daha fazla katılımcının olduğu coinjoin'leri tercih etmektedir. Daha büyük coinjoin'ler daha fazla anonimlik, daha düşük maliyet ve BLOCK alanının daha verimli kullanılmasını sağlar.




## Güvenlik ve en iyi uygulamalar



Ademi merkeziyetçilik arzusu ve mahremiyetin korunması, çeşitli en iyi uygulamaların benimsenmesini gerektirir:




- seedphrase'ünüzü her zaman çevrim dışı olarak güvenli bir yerde saklayın;
- Bilgisayarınızı kaybederseniz veya yetkisiz erişimden şüphelenirseniz, hemen yeni bir Wallet oluşturun. Fonlarınızı bu yeni portföye aktarın ve eskisini silin;
- Adreslerin tekrar kullanılmasını önlemek için her alım için farklı bir Address kullanın;
- Portföy uygulamalarınızı her zaman yalnızca resmi GitHub hesabından veya resmi web sitesinden indirin.



Artık bitcoinlerinizi göndermek, almak ve harcamak için Ginger Wallet uygulamasını kullanmaya aşinasınız.



Bu eğitimi faydalı bulduysanız, lütfen aşağıya bir Green başparmak bırakın. Lütfen bu makaleyi sosyal medya platformlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!



Ayrıca, Liana bilgisayar uygulamasını bitcoin göndermek ve almak için nasıl kullanacağınızı ve otomatik bir emlak planını nasıl uygulayacağınızı anlatan bu eğitime de göz atmanızı öneririm.



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04