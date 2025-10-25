---
name: Proton Authenticator
description: Hesaplarımı 2FA ile güvence altına almak için Proton Authenticator'ı nasıl kullanabilirim?
---
![cover](assets/cover.webp)



İki faktörlü kimlik doğrulama (2FA), şifrenize ek olarak sadece sizde olduğuna dair ek bir kanıt gerektirerek hesaplarınıza ekstra bir güvenlik bariyeri ekler. 2FA'yı etkinleştirmek, şifreniz kimlik avı veya veri sızıntısı yoluyla ele geçirilse bile bilgisayar korsanlığı riskini büyük ölçüde azaltır. 2FA olmadan, bir saldırganın hesaplarınıza erişmek için yalnızca şifrenize ihtiyacı olacaktır; 2FA ile, ikinci faktörünüze de ihtiyaç duyacak ve çoğu hesap hırsızlığı girişimini engelleyecektir.



Çeşitli 2FA türleri mevcuttur. SMS kodları hiç yoktan iyidir, ancak SIM değiştirme saldırılarına ve müdahaleye karşı savunmasız kalır. SMS'i birincil 2FA olarak önermiyoruz. Kimlik doğrulama uygulamaları (TOTP) generate geçici kodları yerel olarak cihazınıza yükler ve bu kodların ele geçirilmesini çok daha zor hale getirir. Fiziksel güvenlik anahtarları en iyi güvenliği sunar, ancak özel donanım gerektirir.



Proton Authenticator bir TOTP kimlik doğrulayıcısıdır. Proton'un mevcut uygulamaların sınırlamalarına yanıtıdır: çoğu özel mülktür, reklam izleyicileri içerir ve şifreli yedekleme sunmaz. Proton Authenticator, reklam ve izleyici içermeyen, uçtan uca şifrelenmiş yedeklemeye sahip açık kaynaklı bir uygulama sunarak kendini diğerlerinden ayırır.



## Proton Authenticator ile tanışın



Proton Authenticator, gizlilik odaklı hizmetleriyle tanınan Proton tarafından geliştirilen bir mobil ve masaüstü TOTP kimlik doğrulama uygulamasıdır. Tüm Proton ürünleri gibi, uygulama açık kaynak kodludur ve bağımsız güvenlik denetimlerinden geçmiştir. Tüm platformlarda (Android, iOS, Windows, macOS, Linux) ücretsiz olarak kullanılabilir.



Proton Authenticator aşağıdaki temel özellikleri sunar:





- Google Authenticator, Authy vb. kullanan çoğu siteyle uyumlu 2FA hesaplarınız için **TOTP** kodları oluşturma.





- **İsteğe bağlı şifreli bulut yedekleme**: Kodlarınızı uçtan uca şifreleme ile yedeklemek ve senkronize etmek için uygulamayı Proton hesabınıza bağlayabilirsiniz. Cihazınızı kaybederseniz, tüm kodlarınızı geri yüklemek için yeni bir tane bağlamanız yeterlidir.





- **Çoklu cihaz senkronizasyonu**: Uygulamada Proton'a giriş yaparak, 2FA kodlarınız uçtan uca şifreleme yoluyla birden fazla cihaz arasında otomatik olarak senkronize edilir. IOS'ta, iCloud aracılığıyla senkronizasyon bir alternatiftir.





- **Parola veya biyometri ile yerel kilitleme**: uygulama PIN ve / veya parmak izi / Yüz Kimliği kilitleme sunar. Yani birisi kilidi açık telefonunuza fiziksel olarak erişse bile Proton Authenticator'ı açamaz.





- **Veri toplama veya izleyici yok**: Proton, uygulama aracılığıyla hiçbir kişisel veri toplamamayı taahhüt eder. Gizli reklam veya davranışsal analiz yoktur.





- **Kolay içe / dışa aktarma**: Proton Authenticator'ın güçlü noktalarından biri, diğer uygulamalarla (Google Authenticator, Authy, Aegis, vb.) Uyumlu mevcut hesaplar için içe aktarma sihirbazıdır. Gerekirse kodlarınızı bir dosyaya da aktarabilirsiniz.



Kısacası, Proton Authenticator ödün vermeyen bir 2FA çözümü olmayı hedefliyor: güvenli, özel, esnek.



## Kurulum



Proton Authenticator tüm platformlarda ücretsiz olarak kullanılabilir. Başvuruyu indirmek için resmi sayfaya gidin: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Uygulamanın ana özelliklerini ve Interface*'i gösteren resmi Proton Authenticator sayfası



Bu sayfada, tüm işletim sistemleri için indirme bağlantıları bulacaksınız: Android, iOS, Windows, macOS ve Linux. Seçtiğiniz işletim sistemine tıklamanız ve standart kurulum adımlarını takip etmeniz yeterlidir.



Bu eğitimde, macOS'a nasıl yükleyeceğinizi ve yapılandıracağınızı göstereceğiz ve ardından uygulamayı iOS'a nasıl yükleyeceğinize ve kodlarınızı iki cihaz arasında nasıl senkronize edeceğinize bakacağız.



### MacOS üzerinde kurulum



Uygulamayı indirip kurduktan sonra Proton Authenticator'ı başlatın. İlk açılışta, uygulama sizi birkaç ilk yapılandırma ekranında yönlendirir:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*"Her kodda güvenlik" mesajı ve "Başlayın "* düğmesi içeren Proton Authenticator karşılama ekranı



### İlk ithalat



Proton Authenticator daha önce başka bir 2FA uygulaması kullandığınızı tespit ederse, bir içe aktarma sihirbazı görünebilir. Belirli uygulamalardan (Google Authenticator, 2FAS, Authy, Aegis, vb.) Doğrudan içe aktarmayı destekler. Alternatif olarak, bu adımı atlayabilir ve hesaplarınızı daha sonra manuel olarak ekleyebilirsiniz.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Diğer kimlik doğrulama uygulamalarından kod aktarmak için içe aktarma sihirbazı*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Uyumlu içe aktarma uygulamaları: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth ve Google Authenticator*



### Yerel uygulama koruması



Bir kilit açma PIN'i ayarlayın veya varsa biyometrik kilit açmayı (Touch ID) etkinleştirin. Bu adım, Mac'inizi kullanan herhangi birinin 2FA kodlarınıza ücretsiz erişim elde etmesini önlemek için çok önemlidir.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*"Verilerinizi koruyun" mesajı ve "Touch ID'yi Etkinleştir "* düğmesi bulunan Touch ID yapılandırma ekranı



### Senkronizasyon seçenekleri



Uygulama ayrıca verilerinizi Apple aygıtlarınız arasında güvenli bir şekilde yedeklemek için iCloud senkronizasyonunu etkinleştirmenizi sağlar.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*"Şifrelenmiş iCloud senkronizasyonu ile verilerinizi güvenli bir şekilde yedekleyin "* mesajını içeren iCloud senkronizasyon seçeneği



Bu adımlar tamamlandıktan sonra, Proton Authenticator kullanıma hazırdır.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*"Yeni bir kod oluştur" ve "Kodları içe aktar "* seçenekleriyle Interface ana boş Proton Authenticator



## ProtonMail ile bir 2FA hesabı ekleyin



Şimdi örnek olarak ProtonMail'i kullanarak ilk 2FA kodunuzu nasıl ekleyeceğinize bakacağız. Bu yöntem, iki faktörlü kimlik doğrulamayı destekleyen tüm hizmetler için aynı şekilde çalışır.



### ProtonMail'de 2FA'yı etkinleştirin



Öncelikle, daha fazla bilgi için ProtonMail rehberimize başvurabilirsiniz:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

ProtonMail hesabınıza giriş yapın ve güvenlik ayarlarına gidin. "İki faktörlü kimlik doğrulama" seçeneğini arayın ve etkinleştirin.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*"İki faktörlü kimlik doğrulama "* bölümünde "Kimlik doğrulayıcı uygulaması" seçeneği bulunan ProtonMail ayarları sayfası



Kimlik doğrulayıcıyı etkinleştirmek için düğmeye tıklayın ve ProtonMail sizden bir kimlik doğrulama uygulaması seçmenizi isteyecektir.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*"İptal" ve "Sonraki "* düğmeleriyle ProtonMail 2FA yapılandırma penceresi



ProtonMail daha sonra kimlik doğrulama uygulamanızla taramanız için bir QR kodu görüntüleyecektir.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*Kimlik doğrulama uygulamanızla taramak için ProtonMail QR kodu, "Bunun yerine anahtarı manuel olarak girin" seçeneği mevcuttur*



Anahtarı manuel olarak girmeyi tercih ederseniz, gizli anahtarı görmek için "Bunun yerine anahtarı manuel olarak girin" seçeneğine tıklayın.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*2FA bilgilerinin manuel girişi: Anahtar, Aralık (30) ve Rakamlar (6)*



### Proton Authenticator ile QR kodunu tarayın



MacOS'taki Proton Authenticator'da "Yeni bir kod oluştur" a tıklayın. Uygulama size birkaç seçenek sunar: **Bir QR kodunu tarayın** veya **Anahtarı manuel olarak girin**.



ProtonMail ekranında görüntülenen QR kodunu taramak için Mac'inizin kamerasını kullanın. QR kodunu taradıktan sonra, yeni kod yapılandırma ekranına yönlendirileceksiniz.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Başlık (ProtonMail), Gizli, Gönderen (Proton), rakam parametreleri ve aralık alanları ile yeni giriş oluşturma penceresi*



Proton Authenticator bilgileri otomatik olarak dolduracaktır. İsterseniz adı özelleştirebilir, ardından "Kaydet" e tıklayabilirsiniz.



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*ProtonMail için oluşturulan TOTP kodu (848 812) ve kalan süre görüntülenir*



### Yapılandırmayı doğrulama



ProtonMail, 2FA'nın doğru çalıştığını onaylamak için Proton Authenticator tarafından oluşturulan 6 basamaklı bir kod girmenizi isteyecektir.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*ProtonMail doğrulama ekranı sizden 6 haneli kodu (848812)* girmenizi ister



Kodu uygulamadan kopyalayın (üzerine tıklayarak) ve aktivasyonu tamamlamak için ProtonMail'e yapıştırın.



Doğrulandıktan sonra, ProtonMail sizden kurtarma kodlarınızı indirmenizi isteyecektir. Bunları dikkatlice kaydetmeniz çok önemlidir.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*Kurtarma kodlarının listesini ve "İndir "* düğmesini içeren ProtonMail kurtarma kodları ekranı



### Acil durum kodları



Bir hesap eklerken, hizmet tarafından sağlanan kurtarma kodlarını saklayın. Çoğu site, güvenli bir yerde saklamak için statik, tek kullanımlık kurtarma kodları sunar. Bu yedek kodları Proton Authenticator dışında tutun, böylece 2FA uygulamasına erişiminizi kaybederseniz hesabınıza erişebilirsiniz.



## IOS kurulumu ve kod aktarımı



Proton Authenticator'ı macOS'ta kurduğunuza göre, iPhone veya iPad'inizde de kullanmak isteyebilirsiniz. 2FA kodlarınızı birden fazla cihazda nasıl alacağınız aşağıda açıklanmıştır.



### Uygulamayı iOS üzerinden indirin



App Store'a gidin ve "Proton Authenticator" için arama yapın. Uygulamayı iOS cihazınıza indirin ve yükleyin.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*IOS'ta kurulum süreci: karşılama ekranı, içe aktarma sihirbazı, uyumlu uygulamaların seçimi ve son "Proton Authenticator'dan kodları içe aktar "* ekranı



### Yöntem 1: JSON dosyası aracılığıyla Dışa/İçe Aktarma



Otomatik senkronizasyon (iCloud veya Proton hesabı) kullanmıyorsanız, kodlarınızı Mac'inizden iPhone'unuza manuel olarak aktarmanız gerekir:



**Adım 1 - macOS'tan dışa aktar** :



Mac'inizde Proton Authenticator'ı açın ve Ayarlar'a gidin (dişli simgesi). Menüde "Dışa Aktar "a tıklayın.



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*MacOS üzerinde Proton Authenticator ayarlar menüsü ve "Dışa Aktar" seçeneği görünür*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*"Proton_Authenticator_backup_2025" dosya adı ve "Kaydet "* düğmesi ile dışa aktarma penceresi



JSON dosyasını Mac'inize kaydedin. Güvenli bir e-posta ile gönderebilir veya iPhone'unuzdan erişmek için iCloud Drive'a kaydedebilirsiniz.



**Adım 2 - iOS'a İçe Aktar** :



IPhone'unuza Proton Authenticator'ı yükleyin ve yapılandırma sırasında kodları içe aktarmayı seçin. Listeden "Proton Authenticator "ı seçin ve JSON dosyasını içe aktarın.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*IOS'ta içe aktarma işlemi: JSON dosyası yerelleştirme, içe aktarma onayı ve Face ID ve iCloud seçenekleriyle yapılandırma ekranları*



### Yöntem 2: Otomatik senkronizasyon



**Proton hesabı üzerinden (çoklu platform senkronizasyonu için)** :



Henüz bir Proton hesabı oluşturmadıysanız ve farklı işletim sistemleri arasında senkronizasyon yapmak istiyorsanız, uygulama sizden bir Proton hesabı oluşturmanızı veya bağlamanızı isteyecektir.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Ücretsiz bir Proton hesabı oluşturmanızı veya mevcut bir hesaba bağlanmanızı isteyen cihaz senkronizasyon ekranı*



**Via iCloud (yalnızca Apple ekosistemi için)** :


Yalnızca Apple cihazları kullanıyorsanız, uygulama ayarlarında iCloud senkronizasyonunu seçebilirsiniz. Bu yöntem, Proton hesabına ihtiyaç duymadan kodlarınızı tüm Apple cihazlarınız arasında otomatik ve güvenli bir şekilde senkronize edecektir.



## Şifreli yedekleme ve geri yükleme



Proton Authenticator'ın en önemli özelliklerinden biri, 2FA kodlarının uçtan uca yedeklenmesidir, böylece cihaz kaybı veya değişikliği her şeye yeniden başlamanız gerekmez.



### Uçtan uca şifreleme



Proton Authenticator ile şifrelenmiş bulut yedekleme söz konusu olduğunda, TOTP sırlarınız Proton sunucusuna gönderilmeden önce cihazınızda yerel olarak şifrelenir. Şifre çözme işlemi yalnızca Proton hesabınıza bağlı cihazlarınızda sizin tarafınızdan mümkündür. Proton AG, kayıtlı kodlarınızı okumak için anahtara sahip değildir.



IOS'ta Proton hesabı yerine iCloud'u tercih ederseniz verileriniz Apple standartlarına göre şifrelenir. Android'de yerel yedekleme, yedekleme dosyasını seçtiğiniz bir parola ile şifrelemenize olanak tanır.



### Kayıp durumunda restorasyon



Telefonunuz kaybolursa, çalınırsa veya ahizeyi değiştirirseniz :



**Proton yedekleme etkinken**: Proton Authenticator'ı yeni cihaza yükleyin. İlk kurulum sırasında aynı Proton hesabına giriş yapın. Uygulama hemen tüm 2FA kodlarınızı şifrelenmiş yedeklemeden senkronize edecek ve indirecektir.



**iCloud yedeklemesi ile (iOS)**: Yeni iPhone/iPad'i aynı Apple Kimliği ile bağlayın ve iCloud Anahtar Zinciri'ni etkinleştirdiğinizden emin olun. Proton Authenticator'ı yükledikten sonra iCloud'a bağlanın. Kodlarınız iCloud üzerinden senkronize edilmeli ve görünmelidir.



**Bulut yedeklemesi yok**: Hesaplarınızı manuel olarak içe aktarmanız gerekir. Bir yedekleme dosyasını dışa aktardıysanız, Proton Authenticator'daki İçe Aktar işlevini kullanın. En kötü senaryoda, yedeklemeniz yoksa, her hizmet için yedekleme kodlarını kullanmanız veya desteğe başvurmanız gerekir.



Proton Authenticator, hesaplarınızı istediğiniz zaman şifreli bir dosya veya çok hesaplı bir QR kodu olarak dışa aktarmanıza olanak tanır. Bu seçenekler size ek güvence sağlar.



## En iyi uygulamalar



Bir 2FA kimlik doğrulayıcı kullanmak güvenliğinizi büyük ölçüde artırır, ancak bazı en iyi uygulamalara uyulmalıdır:



### Acil durum kodlarınızı kaydedin



Bir hizmette 2FA'yı etkinleştirdiğinizde, genellikle size bir kurtarma kodları listesi verilir. Bunları telefonunuzdan uzak tutun (kağıt üzerinde, şifreli bir parola yöneticisinde vb.). Kimlik doğrulayıcınızın tamamen kaybolması durumunda, bu statik kodlar sizi kurtaracaktır.



### Parolalarınızı ve 2FA kodlarınızı karıştırmayın



TOTP'leri de depolayan bir parola yöneticisi kullanmak caziptir. Ancak, parola ve 2FA kodunu aynı yerde tutmak tek bir hata noktası oluşturur ve ikili kimlik doğrulamayı zayıflatır. Maksimum güvenlik için, birçok uzman iki faktörü ayırmayı önerir: güvenli bir yöneticide parolalar ve Proton Authenticator gibi ayrı bir uygulamada 2FA kodları. Bununla birlikte, entegre bir yönetici kullanmak, hiç 2FA'ya sahip olmamaktan daha iyidir.



### Birkaç 2FA yöntemini etkinleştirin



İdeal olarak, kritik hesaplarınızda birden fazla ikinci faktör kullanın. Hizmet izin veriyorsa fiziksel bir güvenlik anahtarı eklemekten çekinmeyin. Daha fazla bilgi için Yubikey fiziksel anahtarları hakkındaki eğitimimize bakın:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Aynı şekilde, basılı acil durum kodlarını da el altında bulundurun.



### Dikkat çekmeyin ve cihazınızı koruyun



Kilitli olmayan telefonunuzu kimsenin aramasına izin vermeyin. Proton Authenticator ile kodlarınız PIN/biyometri ile korunur - bu PIN'i ifşa etmeyin. Benzer şekilde, kimlik avına karşı dikkatli olun: 2FA ile bile, gerçek zamanlı olarak sahte bir siteye bir kod verirseniz, bir saldırgan tarafından kullanılabilir.



### Güncellemeler ve denetimler



Proton Authenticator'ı güncel tutun (güncellemeler olası kusurları düzeltir). Kod açık olduğundan, topluluk gayri resmi denetimler gerçekleştirir ve Proton resmi denetimlerin sonuçlarını yayınlar.



## Diğer uygulamalarla karşılaştırma



Proton Authenticator diğer kimlik doğrulama uygulamalarına karşı nasıl bir performans sergiliyor? İşte karşılaştırmalı bir özet:



**Proton Authenticator**: Açık kaynak, isteğe bağlı E2EE şifreli bulut yedekleme, çoklu cihaz senkronizasyonu, yerel kilitleme, izleme yok, mobil ve masaüstünde kullanılabilir.



**Google Authenticator**: Tescilli, 2023'ten beri Google hesabı üzerinden yedekleme, ancak uçtan uca şifreleme yok (anahtarlar Google tarafından görülebilir), 2023'te çoklu cihaz senkronizasyonu eklendi, varsayılan olarak uygulama kilidi yok, Google izleyicileri içeriyor.



**Aegis Authenticator**: Açık kaynak, yalnızca yerel yedekleme, bulut senkronizasyonu yok, kod/biyometrik kilit, izleme yok, yalnızca Android.



**Gerçek**: Tescilli, parola şifreli bulut yedekleme ancak kapalı kod, çoklu cihaz senkronizasyonu, PIN kilidi / parmak izi, telefon numarasını toplar, masaüstü uygulaması Mart 2024'te durdurulmuştur.



Authy ile ilgili rehberimizi aşağıda bulabilirsiniz:



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator, mevcut en kapsamlı ve güvenli çözümlerden biridir: açık kaynak, çok cihazlı şifreli senkronizasyon, ticari takip yok.



## Kaynaklar ve destek



### Resmi belgeler




- **Resmi web sitesi**: [proton.me/authenticator](https://proton.me/authenticator) - Ürün tanıtımı ve indirmeler
- **İndirme sayfası**: [proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - Tüm işletim sistemleri için bağlantılar
- **Proton desteği**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Resmi 2FA aktivasyon kılavuzu
- **Proton blog**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Duyuru ve ayrıntılı özellikler



### Kaynak kodu ve şeffaflık




- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Açık kaynak kodu
- **Güvenlik denetimleri**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Bağımsız denetim raporları



### Önerilen güvenlik testleri


Yapılandırmadan sonra kurulumunuzu test edin:




- [Have I Been Pwned](https://haveibeenpwned.com/) - Hesaplarınızın ele geçirilip geçirilmediğini kontrol edin
- [2FA Dizini](https://2fa.directory/) - 2FA'yı destekleyen hizmetlerin listesi



### Topluluklar ve tartışmalar




- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Resmi Proton topluluğu
- **Gizlilik Kılavuzları Forumu**: [discuss.privacyguides.net](https://discuss.privacyguides.net) - Gizlilik konularında teknik tartışmalar
- **Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Genel gizlilik ipuçları



### Diğer




- [Have I Been Pwned](https://haveibeenpwned.com/) - Hesaplarınızın ele geçirilip geçirilmediğini kontrol edin
- [2FA Dizini](https://2fa.directory/) - 2FA'yı destekleyen hizmetlerin listesi