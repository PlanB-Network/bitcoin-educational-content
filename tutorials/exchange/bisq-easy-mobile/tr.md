---
name: Bisq Easy Mobile
description: Yeni bitcoin kullanıcıları için eşler arası bir ticaret protokolü - aracı yok, KYC yok.
---
![cover](assets/cover.webp)


## Giriş


Bisq Easy](https://bisq.network/bisq-easy/) ticaret protokolü, [Bisq v1](https://github.com/bisq-network/bisq)'in halefi olan [Bisq 2](https://github.com/bisq-network/bisq2) için tasarlanmıştır. Bisq 2 çoklu ticaret protokollerini, gizlilik ağlarını ve kimlikleri destekleyecektir. Bitcoin'in sıfır işlem ücreti ve depozito gereksinimi olmadan satın alınmasını kolaylaştırır. Bisq platformuna aşina olan deneyimli ve bilgili satıcılar tarafından verimli bir şekilde işe alınmak isteyen ve KYC olmayan bir seçenek arayan yeni Bitcoin alıcıları için tasarlanmıştır.


Şu anda Bisq Easy, Bisq 2 için tek ticaret protokolüdür. Gelecek için daha fazla ticaret protokolü planlanmaktadır. Bu eğitimde Bisq 2 hakkında daha fazla bilgi edinin:


https://planb.academy/tutorials/exchange/peer-to-peer/bisq-v2-c1c6a702-6c16-4101-8b90-62c424017b80

Bu kısa kılavuz, [Bisq Easy Mobile] (https://github.com/bisq-network/bisq-mobile) uygulamasını ve Lightning'i kullanarak Bitcoin satın alma hakkında yukarıdaki öğreticiyi tamamlayıcı niteliktedir.


## 1️⃣ Başlarken


Başlamak için, [indirme sayfası] (https://bisq.network/downloads/) adresinden Bisq Easy Mobile'ı indirin. İndirme işlemini doğrulamanız önerilir. Doğrulama talimatları [indirme sayfası](https://bisq.network/downloads/) adresinde de mevcuttur. Kurulumdan sonra, `Kullanıcı Sözleşmesi`ni kabul etmeniz gerekir. Ardından, bir `nickname` ve avatardan (bir `bot simgesi` ile temsil edilir) oluşan genel bir profil oluşturun. Bisq Easy ile bir istemci içinde birden fazla kullanıcı profili de oluşturabilirsiniz. Kısa bir başlatma işleminden sonra `Ana Ekran`a geleceksiniz. Uygulama, eğitim materyallerini doğrudan ana sayfada vurgular. En son bilgilere aşina olmak için `Ticaret Rehberini Aç` seçeneğine dokunun.


![image](assets/en/01.webp)


Ticaret rehberi, ilgili her şeyi kolay adımlarla açıklıyor:



- Bisq Easy'de nasıl işlem yapılır
- Ticaret süreci nasıl işler?
- Ticaret kuralları hakkında bilmem gerekenler.


Bir diğer önemli bölüm ise **"Bisq Easy'de işlem yapmak ne kadar güvenli? "**


![image](assets/en/08.webp)


"Okudum ve anladım" etiketli kutuyu işaretleyin ve "Bitir" düğmesine dokunun.


![image](assets/en/02.webp)


## 2️⃣ Verilerinizi yedekleyin


Başlamadan önce, bazı temizlik işlerini halledelim ve veri depolama dosyanızın bir `yedeklemesini` oluşturalım. Profilinizi ve işlem geçmişinizi kaydetmek için `Diğer` > `Yedekle ve Geri Yükle` seçeneğine gidin. Yedekleme yapmadan cihazınızı kaybederseniz, itibarınız ve devam eden işlemleriniz kurtarılamaz. Yedeğinizi şifrelemek için bir `Şifre` girin.


![image](assets/en/11.webp)


## 3️⃣ Teklifler


Ana ekrandan tekliflere gitmenin iki yolu vardır. Ekranın ortasındaki `Teklifleri keşfet` seçeneğine veya alt menüdeki `Teklifler` seçeneğine dokunun. Buradan, işlem yapmak istediğiniz "para birimini" seçin.


![image](assets/en/03.webp)


Teminat gerektiren [Bisq 1]'in (https://planb.academy/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04) aksine, Bisq Easy güvenlik için yalnızca satıcının itibarına güvenir. Bu yaklaşım, alıcıların önceden sahip olmadan ilk kez Bitcoin satın almalarını sağlarken, satıcının fiat ödemelerini aldıktan sonra Bitcoin'yi teslim etme yeteneğine yüksek derecede güvenmektedir. Bu nedenle, Bisq Kolay menkul kıymet modeli yalnızca küçük işlem tutarları için optimize edilmiştir ve riski en aza indirmek için işlemler işlem başına 600 USD eşdeğeri ile sınırlandırılmıştır. Teklif Defteri bölümünde, Lightning veya Bitcoin (on-chain) ile ödeme yöntemleri ve mutabakat için filtreleri seçin.


![image](assets/en/04.webp)


Filtreleri uyguladıktan sonra, saygın bir ticaret ortağından uygun bir teklif seçin. Satıcının önceden seçtiği ödeme yöntemi ve ödeme türü (`Lightning` veya `on-chain`) görüntülenecektir. Devam etmeden önce bunların tercihlerinizle eşleştiğinden emin olun. Burada Lightning ⚡ seçeneğini seçiyoruz.


![image](assets/en/05.webp)


İşlem ayrıntılarını gözden geçirin ve `Teklifi almayı onayla` seçeneğine dokunarak onaylayın. Ardından bir Açılır Ekran teklifi başarıyla aldığınızı onaylar. Açık İşlemler`de İşlemi göster`e dokunun. Açık İşlemler bölümünde, `Lightning faturanızı` yapıştırın ve paylaşmak için `Satıcıya gönder` seçeneğine dokunun. Şimdi satıcının ödeme hesabı verilerini bekleyin. Satıcıların yanıt vermesi zaman alabilir. Sohbet penceresindeki güncellemeler için periyodik olarak tekrar kontrol edin.


![image](assets/en/06.webp)


Sohbette kısa bir selamlama gönderin. Satıcı çevrimiçi olduklarında ödeme ayrıntılarını paylaşacaktır


![image](assets/en/09.webp)


Satıcıdan gerekli ödeme bilgilerini aldıktan sonra, ödemeyi tamamlamaya devam edin. Daha sonra, `Ödemeyi yaptığınızı onaylayın` düğmesine dokunun, ardından sabırla makbuzun onaylanmasını bekleyin. ️ ⌛️


Son olarak, satıcı ödeme makbuzunu onayladığında, siz de Bitcoin'in alındığını onaylamalısınız. Böylece Bisq'yı Kolay Modda kullanarak satın alma işlemi tamamlanmış olur. Tebrikler! Şimdi `ticareti kapat` düğmesine dokunabilirsiniz.


![image](assets/en/10.webp)


## 4️⃣ Bisq'de Uyuşmazlık Çözümü Kolay


Ticaretinizde herhangi bir sorun çıkarsa, hem alıcılar hem de satıcılar arabuluculuk desteği talep edebilir.


**Arabulucular Ne Yapabilir:**

- Ticaretin başarıyla tamamlanmasına yardımcı olun

- Fiat, altcoin ve Bitcoin ödemelerini doğrulayın

- Gerektiğinde işlemleri iptal edin

- Ciddi kural ihlallerini olası kullanıcı yasaklamaları için moderatörlere bildirin


**Hileli Satıcılar için Sonuçlar:**

İtibar türlerine bağlı olarak:



- BSQ Tahvil İtibarı**: DAO, tahvil edilmiş BSQ'larına el koyabilir
- Soğan Address İtibar**: Bisq 1 soğan adresleri yasaklanabilir


**Önemli Not:** Tüm itibar kullanıcı profilinize bağlı olduğundan, bir yasaklama itibarınızı tamamen devre dışı bırakır.


## 5️⃣ Kendi teklifinizi oluşturun


Mevcut teklifleri almak yerine, kendi satın alma teklifinizi oluşturabilir ve satıcıların size gelmesini sağlayabilirsiniz. İşlem yapmak istediğiniz pazarda doğru prim veya ödeme yöntemlerine sahip herhangi bir teklif bulamazsanız bu doğru seçenektir, ancak bir satıcının kabul etmesini beklemeniz gerekecektir.


Teklifler ekranından sağ alt köşedeki yeşil `+` simgesine dokunun. Ardından `Bitcoin Satın Al` seçeneğini seçin ve fiat para biriminizi seçin.


İşlem parametrelerinizi ayarlayın:



- Sabit tutar veya Aralık tutarı**: Ne kadar harcamak istediğinizi seçin.
- Ödeme yöntemi**: Mevcut seçeneklerden birini seçin
- Yerleşim**: Yıldırım ⚡ veya ₿ on-chain'yi seçin


Bilgilerinizi gözden geçirin ve `Teklif oluştur`a dokunun. Teklifiniz şimdi `Teklif Defteri`nde görünür.


![image](assets/en/07.webp)


*Not: Bisq Easy'de bir alıcı olarak itibara ihtiyacınız yoktur - bu en önemli avantajdır. Satıcılar itibar gereksinimini ve riskini üstlenirler, bu yüzden prim alırlar. Teklifinizin, itibarlı satıcıların dikkate alması için yeterince cazip fiyatlandırılması yeterlidir.*


Yayınlandıktan sonra `Teklif Defteri` bölümünde bekleyin. Bir satıcı teklifinizi kabul ettiğinde, bir bildirim alacaksınız. Satıcı ve sizin ödeme bilgilerinizi değiş tokuş edebileceğiniz `Açık İşlemler` bölümünde işlemi açın. Satıcıya Bitcoin adresinizi veya Lightning faturanızı gönderin. Fiat gönderdikten sonra ödemeyi onaylayın. Satıcı ödemeyi aldığını onayladığında, takası tamamlamak için Bitcoin'leri serbest bırakacaktır.


## 🎯 Sonuç


Bisq Easy, teminatsız Bitcoin alımlarına olanak tanıyarak yeni alıcılar için klasik tavuk-yumurta sorununu çözer. Değiş tokuş açıktır: güvenlik için kilitli fonlar yerine satıcı itibarına güvenirsiniz. Bu güvene dayalı yaklaşım, saygın satıcıların güven oluşturma ve destek sağlama yatırımlarını telafi eden tipik %5-15 primi açıklamaktadır. Sistem olası kayıpları önlemek için alım satımları küçük miktarlarla sınırlasa da, her zaman itibar puanı yüksek satıcılara bağlı kalın. Bu koşulları kabul etmeye istekli yeni gelenler için Bisq Easy, Bitcoin'e kolay bir giriş noktası sunar.


## 📚 Bisq Kolay Mobil Kaynaklar


[Github](https://github.com/bisq-network/bisq-mobile) | [Web Sitesi ](https://bisq.network/bisq-easy/)| [Wiki](https://bisq.wiki/Bisq_Easy)