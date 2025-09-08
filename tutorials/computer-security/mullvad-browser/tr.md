---
name: Mullvad Tarayıcı
description: Gizlilik için Mullvad Tarayıcı nasıl kullanılır?
---

![cover](assets/cover.webp)



Dijital gözetimin her yerde yaygınlaştığı bir dünyada, çevrimiçi gizliliğinizi korumak hiç bu kadar önemli olmamıştı. Şirketler sizi takip etmek için sofistike teknikler kullanıyor:





- Üçüncü taraf çerezleri**: sizi bir siteden diğerine takip etmek için harici siteler tarafından bırakılan küçük dosyalar
- Parmak izi**: çerezler olmadan sizi tanımlamak için tarayıcınızın ve cihazınızın benzersiz özelliklerini (ekran çözünürlüğü, yüklü yazı tipleri, eklentiler vb.) toplar
- İzleme komut dosyaları**: tarama davranışınızı analiz eden görünmez JavaScript kodları (tıklamalar, kaydırma, harcanan zaman)
- IP Address analizi**: coğrafi konum ve İnternet servis sağlayıcınızın tanımlanması



Bu veriler daha sonra çevrimiçi davranışınızın ayrıntılı profillerini oluşturmak için birleştirilir ve genellikle sizin bilginiz olmadan paraya dönüştürülür. Bu gerçeklik temel bir soruyu gündeme getiriyor: Anonimliğinizi ve gizliliğinizi koruyarak internette nasıl gezinebilirsiniz?



Cevap büyük ölçüde web tarayıcısı seçiminizde yatmaktadır. Her gün bilgiye erişmek, alışveriş yapmak veya iletişim kurmak için kullandığımız bu araç, kişisel verilerimizin korunmasında belirleyici bir rol oynamaktadır. Ne yazık ki, Google Chrome gibi popüler tarayıcılar (küresel pazarın yaklaşık %65'ini elinde tutan) kullanıcı verilerinin büyük ölçüde toplanmasına dayalı iş modelleri etrafında tasarlanmıştır.



![MULLVAD BROWSER](assets/fr/01.webp)


*Mullvad Browser, tüketici tarayıcılarını geride bırakan son derece etkili izleyici engelleme özelliğiyle öne çıkıyor*



Bu zorlukla karşı karşıya kalan yeni oyuncular farklı bir felsefeyle ortaya çıkıyor: gizliliği tasarımlarının merkezine yerleştirmek. Bunlar arasında Mullvad Browser, en iyi gizlilik korumalarını akıcı ve erişilebilir bir tarama deneyimi ile birleştiren yenilikçi bir çözüm olarak öne çıkıyor.



Verilerinizi toplayarak deneyiminizi kişiselleştirmeye çalışan geleneksel tarayıcıların aksine, Mullvad Browser tam tersi bir yaklaşım benimser: tüm kullanıcılarının web sitelerinde aynı görünmesini sağlayarak kişiselleştirilmiş izlemeyi neredeyse imkansız hale getirir.



Bu eğitimde, Mullvad Browser'ın internette gezinme şeklinizi nasıl değiştirebileceğini ve kullanım kolaylığından ödün vermeden gözetlemeye karşı nasıl güçlü bir koruma sağlayabileceğini birlikte keşfedeceğiz.




## Mullvad Browser ile tanışın



**Mullvad Browser**, Tor Projesi ile işbirliği içinde geliştirilen ve İsveçli Mullvad VPN şirketi tarafından ücretsiz olarak dağıtılan gizlilik odaklı bir web tarayıcısıdır. Nisan 2023'te piyasaya sürülen bu tarayıcı, kullanıcıların Tor ağı yerine güvenilir bir VPN üzerinden gezinmesine izin verirken çevrimiçi izleme ve parmak izini en aza indirmek için tasarlanmış bir **"Tor ağı olmayan Tor Tarayıcı "** olarak kendini tanıtıyor.



Mullvad Browser, Firefox ESR (Mozilla Firefox'un uzun ömürlü sürümü) tabanlı ve Tor Projesi uzmanları tarafından güçlendirilmiş ücretsiz, açık kaynaklı bir tarayıcıdır. Somut olarak, Tor Browser'ın **koruma özelliklerinin** çoğunu içerir, ancak **trafiği Tor ağı üzerinden yönlendirmez**. Bunun yerine, kullanıcılar IP Address'lerini anonimleştirmek için güvenilir bir şifreli VPN'e bağlayabilirler (ve bağlamalıdırlar).



Kullanıcı deneyimi açısından Mullvad Browser, akıcı gezinme sunan klasik bir tarayıcıya benziyor. Windows, macOS ve Linux'ta ücretsiz olarak kullanılabilir (mobil sürümü yoktur). Kullanmak için Mullvad VPN abonesi olmanıza gerek yoktur; ancak, **IP'nizi maskelemeden Mullvad Browser'ı kullanmak tam bir anonimlik sağlamaz** - bu nedenle güvenilir bir VPN ile birlikte kullanılması şiddetle tavsiye edilir.



### Hedefler: gizlilik ve izleme karşıtlığı



Mullvad tarayıcısı tek bir ana hedef göz önünde bulundurularak tasarlanmıştır: **Çevrimiçi kullanıcı gizliliğini** korumak ve yaygın izleme ve profil oluşturma tekniklerine karşı koymak. Ana hedefleri şunlardır:





- Web siteleri ve reklam ajansları tarafından reklam takibini ve izlemeyi** büyük ölçüde azaltın. Mullvad Browser varsayılan olarak üçüncü taraf izleyicileri, izleme çerezlerini ve kimliğinizi belirleyebilecek parmak izi komut dosyalarını engeller.





- "Kalabalığa karışmak "** için tarayıcınızın parmak izini** standartlaştırın. Parmak izi, tarayıcınızın tüm özelliklerinin bir araya getirilmesiyle oluşturulan benzersiz bir "kimlik kartı" gibidir. Mullvad Browser, tüm kullanıcılarının tamamen aynı "kimlik kartına" sahip olmasını sağlayarak onları bireysel olarak ayırt etmeyi imkansız hale getirir.





- Ek uzantılar olmadan anında koruma sunar**. Mullvad Browser "kullanıma hazır" bir konfigürasyonda gelir: kullanıcının korunmak için bir dizi uzantı yüklemesi veya herhangi bir ayarı değiştirmesi gerekmez.





- Performans veya ergonomiden** gereğinden fazla ödün vermeyin. Tor yönlendirmesinin olmadığı durumlarda Mullvad Browser, Tor Browser'dan çok daha hızlı gezinme sunar ve VPN ile birlikte standart bir tarayıcının performansına yaklaşır.



### Temel Mullvad Tarayıcı özellikleri



Mullvad Browser, doğrudan Tor Browser'dan esinlenen bir dizi **güvenlik ve gizlilik özelliği** içerir:





- Her zaman gizli tarama:** Gizli tarama modu varsayılan olarak etkinleştirilir ve devre dışı bırakılamaz. **Bir oturumdan diğerine hiçbir geçmiş, çerez veya önbellek saklanmaz**. Mullvad Browser'ı kapattığınız anda tüm tarama verileri silinir.





- Parmak izine karşı geliştirilmiş koruma:** Tarayıcı, dijital parmak izini engellemek için katı ayarlar uygular. Buna şunlar dahildir:
 - Kullanıcı aracısı** ve tarayıcı sürümü standardizasyonu
 - Tüm kullanıcılar için saat dilimi UTC** olarak ayarlandı
 - Letterboxing**: ekran boyutunu standartlaştırmak ve ekran boyutlarınıza göre tanımlamayı önlemek için web sayfalarının etrafına otomatik olarak gri kenar boşlukları ekleyen bir teknik
 - Parmak izi API'lerini** engelleyin: Canvas (2D çizim), WebGL (3D grafikler) ve AudioContext (ses işleme) teknolojileri, donanımınızla ilgili benzersiz ayrıntıları ortaya çıkarabilecekleri için devre dışı bırakılmıştır
 - Yüklü yazı tipleri tarafından tanımlanmayı önlemek için standartlaştırılmış sistem yazı tipleri**





- İzleyicileri ve reklamları engelleme:** Mullvad Browser, **üçüncü taraf izleyicileri, reklam komut dosyalarını ve diğer kötü amaçlı içerikleri** engellemek için **uBlock Origin** uzantısını (önceden yüklenmiş) ek koruma listeleriyle yerel olarak entegre eder. Bu korumaya **Birinci Taraf İzolasyonu** eşlik eder: çerezleri her web sitesi için ayrı "kaplarda" saklayan ve bir sitenin başka bir site tarafından bırakılan çerezleri okumasını önleyen bir teknik.





- Oturum sıfırlama düğmesi:** Tor Browser'ın "Yeni Kimlik" düğmesi gibi, Mullvad Browser da **tarayıcıyı yeni, boş bir oturumla hızlı bir şekilde yeniden başlatmak** için bir düğme sunar.





- Ayarlanabilir güvenlik düzeyleri:** Tor Browser'da olduğu gibi ayarlardan güvenlik düzeyini (*Normal*, *Safer*, *Safest*) ayarlayabilirsiniz.



## Varsayılan olarak yerleşik uzantılar



Mullvad Browser, izleme karşıtı korumasının çekirdeğini oluşturan **önceden yüklenmiş üç uzantı** içerir. **Bu uzantıları asla kaldırmamanız veya yapılandırmalarını değiştirmemeniz çok önemlidir**, çünkü bu sizi Mullvad Browser kullanıcıları arasında benzersiz kılacaktır:



### **uBlock Origin**


Bu reklam ve izleyici engelleyici uzantısı, engellemek için **optimize edilmiş filtre listeleri** ile önceden yapılandırılmış olarak gelir:




- Müdahaleci reklamcılık
- Verilerinizi toplayan üçüncü taraf izleyiciler
- Kötü amaçlı komut dosyaları
- Davranışsal izleme Elements



mullvad Browser'daki uBlock Origin, tüm kullanıcıların tam olarak aynı Elements'ü engellemesini sağlamak için standartlaştırılmış parametreler kullanır ve böylece dijital ayak izlerinin tekdüzeliğini korur.



### **NoScript**


NoScript, tarayıcının **güvenlik seviyelerini** yönetmek için arka planda çalışır. Bu:




- JavaScript** yürütmesini seçilen seviyeye göre kontrol eder (Normal/En Güvenli/En Güvenli)
- XSS** (Cross-Site Scripting) saldırılarını otomatik olarak filtreler
- HTTPS olmayan sitelerdeki tehlikeli** aktif içeriği engeller
- Simgesi varsayılan olarak gizlidir, ancak "Araç çubuğunu özelleştir" aracılığıyla görüntülenebilir



### **Mullvad Browser** uzantısı


Mullvad'a özgü bu uzantı, Mullvad VPN müşterisi olup olmadığınıza bağlı olarak farklı işlevler sunar:



#### **Mullvad VPN aboneliği olmadan:**




- Temel bağlantı kontrolü**: mevcut genel IP adresinizi ve bazı bağlantı bilgilerini görüntüler
- Gizlilik önerileri**: güvenlik ayarlarınızı iyileştirmek için ipuçları (DNS, yalnızca HTTPS, arama motoru)
- WebRTC** kontrolü: IP Address sızıntılarını önlemek için etkinleştirin/devre dışı bırakın
- Mullvad VPN kullanmıyorsanız dijital ayak izinizi etkilemeden** silinebilir



#### **Mullvad VPN aboneliği ile:**


Eklenti, gelişmiş özellikleriyle tam potansiyelini ortaya koyuyor:





- Entegre SOCKS5 proxy**: Mullvad VPN sunucu proxy'sine tek tıkla bağlantı
 - Sabit IP Address**: IP Address'ini değiştirebilen bir VPN'in aksine, bir proxy her zaman aynı Address çıkışını garanti eder
 - Otomatik kill switch**: VPN bağlantısı kesilirse, tarayıcı trafiği hemen engellenir
 - IPv6 desteği**: VPN bağlantınız etkin olmasa bile IPv6 bağlantısı





- Multihop (çift VPN)**: tünel içinde bir tünel oluşturmak için proxy konumunu değiştirme yeteneği
 - Trafiğiniz önce VPN sunucunuzdan geçer, ardından başka bir Mullvad sunucusuna "atlar"
 - Yalnızca tarayıcı için farklı bir yerelleştirme kullanın





- Gelişmiş bağlantı izleme**: VPN durumunuzun gerçek zamanlı izlenmesi, bağlı sunucu ve DNS sızıntı tespiti





- Mullvad Leta'ya** erişim: aboneler için ayrılmış özel arama motoru (hesabınızla korelasyon nedeniyle Mullvad tarafından önerilmemesine rağmen)



Bu üç uzantı, kolektif anonimliği tehlikeye atacak özelleştirme olasılığı olmaksızın her kullanıcının tamamen aynı savunmalardan yararlandığı tutarlı bir koruma ekosistemi oluşturmak için birlikte çalışır.



## Mullvad Browser'ın avantajları ve dezavantajları



### Avantajlar





- Varsayılan olarak mükemmel gizlilik koruması:** Mullvad Browser, manuel yapılandırmaya gerek kalmadan en başından itibaren çok katı gizlilik ayarları uygular.





- Tor Browser'dan daha iyi performans:** Onion yönlendirme olmadığında, Mullvad Browser klasik web taraması için Tor Browser'dan **önemli ölçüde daha hızlı ve daha duyarlı**.





- Tanıdık Interface basitliği:** Mullvad Browser, Firefox'un Interface'sını temel alır. Firefox'a veya hatta Tor Browser'a alışkınsanız, kendinizi yabancı hissetmeyeceksiniz.





- Güvenilir işbirliği ve denetlenen kod:** Mullvad Browser, Tor Projesi'nin uzmanlığından yararlanır ve tüm kaynak kodu dış denetime açıktır.



### Dezavantajlar





- VPN olmadan ağ anonimliği yok:** En önemli nokta, **Mullvad Browser'ın IP Address'nizi kendi başına gizlememesidir** (Tor Browser hariç diğer tüm tarayıcılar gibi). IP Address'niz internetteki "posta Address'niz" gibidir: konumunuzu ve İSS'nizi ortaya çıkarır. Bu nedenle, bu önemli bilgileri gizlemek için **büyük ölçüde bir VPN'e** (sanal özel ağ) ihtiyaç duyar.





- Mobil versiyon yok:** Mullvad Browser bugüne kadar sadece PC'de (Windows, Mac, Linux) mevcuttu.





- Belirli alışkanlıklarla uyumsuz:** **kalıcı özel mod** bir oturumu bir kullanımdan diğerine koruyamayacağınız anlamına gelir. Bir oturumdan diğerine bir web hesabına bağlı kalmak imkansızdır.





- Kısıtlı özellikler:** Parmak izi bütünlüğünü korumak için Mullvad Browser, Firefox'ta bulunan bazı özellikleri** devre dışı bırakmıştır ve özelleştirme için tasarlanmamıştır.



## Mullvad Tarayıcıyı Yükleme



Mullvad Browser Windows, macOS ve Linux için ücretsiz olarak kullanılabilir. Yüklemek için [resmi Mullvad web sitesine] (https://mullvad.net/browser) gidin.



![MULLVAD BROWSER](assets/fr/02.webp)



*İndirme düğmesi vurgulanmış resmi Mullvad Browser ana sayfası.*



![MULLVAD BROWSER](assets/fr/03.webp)



*Mullvad Browser.* indirme sayfasında işletim sisteminizi seçin



İşletim sisteminize karşılık gelen **"İndir "** düğmesine tıklayın.



Linux için, dağıtımınıza bağlı olarak farklı formatlar arasından seçim yapabilirsiniz. İndirme işlemi tamamlandıktan sonra:



### Windows üzerinde


İndirilen `.exe` dosyasını çalıştırın ve kurulum talimatlarını izleyin.



### MacOS üzerinde


İndirilen `.dmg` dosyasını açın ve Mullvad Browser uygulamasını Uygulamalar klasörünüze sürükleyin.



### Linux üzerinde


.tar.xz` arşivini istediğiniz dizine çıkarın ve `start-mullvad-browser.desktop` dosyasını çalıştırın.



## Yapılandırma ve ilk kullanım



Mullvad Browser'ı ilk başlattığınızda, Tor Browser'ınkine çok benzeyen bir Interface göreceksiniz. Tarayıcı gizlilik için önceden yapılandırılmıştır ve özel bir değişiklik gerektirmez.



![MULLVAD BROWSER](assets/fr/04.webp)



*Interface Mullvad Browser ana sayfası uzantıları, süpürge simgesi ile generate'a yeni bir kimlik ve sağ üstte uygulama menüsü.*



**Önemli:** Mullvad Browser varsayılan olarak IP Address'inizi maskelemez. Tam koruma için, paralel olarak bir VPN kullanmanızı şiddetle tavsiye ederiz. Mullvad VPN veya başka bir güvenilir VPN hizmeti kullanabilirsiniz.



Tarayıcı ayrıca Mullvad'ın DNS hizmetini kullanan **DNS-over-HTTPS (DoH)** içerir: bu teknoloji, İSS'nizin ziyaret ettiğiniz siteleri izlemesini önlemek için DNS isteklerinizi şifreler (site adlarını IP adreslerine çevirir).



### Güvenlik ayarları



Sağ üstteki **uygulama menüsüne** (üç yatay çubuk), ardından **"Ayarlar "** ve ardından **"Gizlilik ve Güvenlik "** sekmesine tıklayarak güvenlik düzeyini ayarlayabilirsiniz. Aşağı doğru **"Güvenlik "** bölümüne kaydırın:



![MULLVAD BROWSER](assets/fr/05.webp)



*Güvenlik seviyelerinin seçimi: oklar, uygulama menüsünden "Gizlilik ve Güvenlik" sekmesine ve güvenlik seçeneklerine giden yolu gösterir*



Mullvad Browser üç güvenlik seviyesi sunar:





- Normal** (mevcut varsayılan seviye): Tüm tarayıcı ve web sitesi işlevleri etkin





- Daha güvenli**: Bazı web sitelerinde işlevsellik kaybına yol açabilecek, genellikle tehlikeli web sitesi işlevlerini devre dışı bırakır:
 - HTTPS olmayan siteler için JavaScript devre dışı
 - Bazı yazı tipleri ve matematiksel semboller devre dışı bırakıldı
 - Ses ve video (HTML5 medya) ve WebGL "tıklayarak oynat" özelliğine sahiptir





- En güvenli**: Yalnızca statik siteler ve temel hizmetler için gereken web sitesi işlevlerine izin verir:
 - JavaScript tüm siteler için varsayılan olarak devre dışıdır
 - Bazı yazı tipleri, simgeler, resimler ve matematiksel semboller devre dışı bırakılmıştır
 - Ses ve video (HTML5 medya) ve WebGL "tıklayarak oynat" özelliğine sahiptir



### Yeni oturum düğmesi



Tarayıcıyı kapatmadan boş bir oturumla yeniden başlatmak için süpürge simgesine tıklayın veya uygulama menüsü > **"Yeni oturum "** seçeneğini kullanın.



![MULLVAD BROWSER](assets/fr/06.webp)



*Tarayıcıyı tamamen yeni bir oturumla yeniden başlatmak için "Kimliğinizi sıfırlayın" işlevi*



## Günlük kullanım



### Normal navigasyon



Mullvad Browser, günlük gezintiler için klasik bir tarayıcı gibi davranır. Tüm web sitelerine her zamanki gibi erişilebilir, ayrıca izlemeye karşı gelişmiş koruma avantajı da vardır.



### Çerez yönetimi ve giriş



Kalıcı özel mod nedeniyle, her oturum açtığınızda hesaplarınıza yeniden bağlanmanız gerekecektir. Bu, maksimum gizlilik için ödediğiniz bedeldir.



### Uzantılar



Mullvad Browser teknik olarak Firefox kataloğundan ek uzantılar yüklemenize izin verir, ancak **etkilerini anlamak önemlidir**. Eklenen her uzantı dijital ayak izinizi değiştirir ve sizi diğer Mullvad Browser kullanıcılarından ayırır, bu da tarayıcının temel ilkesine aykırıdır: tüm kullanıcıların aynı görünmesini sağlamak.



Mullvad'ın açıkladığı gibi: *"Bazen belirli bir savunmaya sahip olmamak, sahip olmaktan daha iyidir. Çevrimiçi gizliliği artırmak isteyerek, sonuçta sizi daha da görünür hale getiren uzantılar yüklersiniz. "*



Yine de uzantıları yüklemeyi tercih ederseniz, sizi siteden siteye izlemek için kullanılabilecek benzersiz bir parmak izi oluşturduğunuzu unutmayın. Maksimum koruma için, tüm kullanıcılar için aynı olan önceden yüklenmiş üç uzantıya bağlı kalmak en iyisidir.



## Mullvad Browser ile en iyi uygulamalar



1. **Her zaman bir VPN kullanın: Mullvad Browser IP'nizi maskelemez. Tam anonimlik için bir VPN gereklidir.



2. **Tarayıcıyı özelleştirmeyin**: Kimliğinizin tespit edilmesine neden olabileceğinden ayarları değiştirmekten veya uzantı eklemekten kaçının.



3. **Yeni oturum düğmesini kullanın**: Farklı etkinlikler arasında, oturumlarınızı bölmek için sıfırlama işlevini kullanın.



4. **İhtiyaçlarınıza en uygun güvenlik seviyesini seçin**:




   - Normal (önerilir)**: Günlük gezinme için. Web sitelerini işlevsel tutarken zaten mükemmel koruma sunar. Bu, kullanıcıların %95'i için en iyi dengedir.
   - Daha güvenli**: Bilinmeyen veya tehlikeli olabilecek siteleri ziyaret ediyorsanız veya halka açık Wi-Fi ağlarında ekstra koruma için. Bazı siteler hatalı çalışabilir.
   - En güvenli**: Yüksek riskli durumlar için ayrılmıştır (araştırmacı gazetecilik, hassas iletişim, düşmanca ortamlar). Çoğu modern site kırılacaktır, ancak maksimum güvenliğin bedeli budur.



5. **Güncellemeleri düzenli olarak kontrol edin**: Tarayıcınızı en son güvenlik yamaları ile güncel tutun.



6. **Gizlilik dostu arama motorları kullanın**: Google yerine DuckDuckGo, Startpage veya Searx'i seçin.



7. **Sadece HTTPS modunu etkinleştirin**: Ayarlarda, güvenli bağlantıları zorlamak için "Yalnızca HTTPS" modunun etkinleştirildiğinden emin olun.



8. **Hiçbir gelişmiş ayarı DEĞİŞTİRMEYİN**: Diğer tarayıcıların aksine, Mullvad Browser TÜM kullanıcıların tamamen aynı yapılandırmaya sahip olacağı şekilde tasarlanmıştır. About:config`deki ayarları değiştirmek veya uBlock Origin/NoScript ayarlarını değiştirmek sizi benzersiz kılar ve tarayıcı anonimliğini tamamen ortadan kaldırır.



## Önerilen DNS yapılandırması



Mullvad Browser, Mullvad DNS-over-HTTPS'yi otomatik olarak entegre eder. Mullvad VPN kullanıyorsanız, VPN sunucunuzun DNS sunucusunu kullanmak daha hızlı olduğu için uzantı **Mullvad DoH'u devre dışı bırakmanızı** önerecektir. Mullvad VPN kullanmıyorsanız, İSS'nizin DNS izlemesini önlemek için Mullvad DoH'u etkin tutun.



## Sonuç



Mullvad Browser, Tor ağının performans kısıtlamaları olmadan gizlilik dostu web taraması arayanlar için mükemmel bir çözümdür. Kaliteli bir VPN ile birleştirildiğinde, çevrimiçi izleme ve gözetlemeye karşı sağlam bir koruma sağlar.



Bazı sınırlamaları olmasına rağmen (mobil versiyonu yok, kalıcı olmayan oturumlar), Mullvad Browser dijital gizliliklerinin kontrolünü yeniden kazanmak isteyen herkesin cephaneliğinde değerli bir araçtır. Kullanım kolaylığı ve varsayılan yapılandırması, ister yeni başlayanlar ister deneyimli olsun, gizlilik bilincine sahip kullanıcılar için akıllıca bir seçimdir.



## Kaynaklar



### Resmi belgeler




- [Resmi Mullvad Tarayıcı web sitesi](https://mullvad.net/fr/browser)
- [Mullvad Browser indirme sayfası](https://mullvad.net/en/download/browser)
- [Detaylı teknik özellikler](https://mullvad.net/en/browser/Hard-facts)
- [Mullvad Tarayıcı Uzantısı](https://mullvad.net/en/help/mullvad-browser-extension)



### Kılavuzlar ve açıklamalar




- [Gizlilik neden önemlidir](https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor olmadan Tor: Mullvad Tarayıcı konsepti](https://mullvad.net/en/browser/tor-without-tor)
- [Gizlilik dostu bir tarayıcı nasıl seçilir](https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Tarayıcı parmak izini anlama](https://mullvad.net/en/browser/browser-fingerprinting)



### Destek ve yardım




- [Mullvad Tarayıcı Yardım Merkezi](https://mullvad.net/en/help/tag/mullvad-browser)
- [Çevrimiçi gizlilik için ilk adımlar](https://mullvad.net/en/help/first-steps-towards-online-privacy)



### Topluluk kaynakları




- [Mullvad Tarayıcı Kılavuzu - Gizlilik Kılavuzları](https://www.privacyguides.org/en/desktop-browsers/)
- [Topluluk tartışmaları](https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)