---
name: Ente Auth
description: Açık kaynaklı, uçtan uca şifrelenmiş bir 2FA doğrulayıcısı
---
![cover](assets/cover.webp)



İki faktörlü kimlik doğrulama (2FA), çevrimiçi hesaplarımızı güvence altına almak için vazgeçilmez hale geldi. Normal şifrenize ek olarak, genellikle özel bir uygulama tarafından oluşturulan geçici bir kod gerektirir. TOTP (Time-Based One-Time Password) olarak bilinen bu mekanizma, şifreniz ele geçirilse bile, bir saldırganın her 30 saniyede bir yenilenen bu ikinci faktöre sahip olmadan hesabınıza erişemeyeceğini garanti eder.



Ancak, doğru kimlik doğrulama uygulamasını seçmek önemsiz değildir. Google Authenticator, popüler olmasına rağmen önemli sınırlamalara sahiptir: denetlenmesi imkansız özel kod, uçtan uca şifreleme olmadan senkronizasyon ve telefonunuzda bir sorun olması durumunda kodların tamamen kaybolma riski. Authy gibi diğer çözümler bir telefon numarası gerektirir ve tam gizliliği garanti etmez.



**Ente Auth** modern ve güvenli bir alternatif olarak öne çıkıyor. Ente Photos]'un (https://ente.io) arkasındaki ekip tarafından geliştirilen bu ücretsiz, açık kaynaklı, çapraz platform uygulaması, uçtan uca şifrelenmiş bulut yedeklemeleri ve tüm cihazlarınız arasında sorunsuz senkronizasyon sunar. Tescilli çözümlerin aksine Ente Auth, gizliliğinizden ödün vermeden kimlik doğrulama kodlarınız üzerinde tam kontrol sahibi olmanızı sağlar.



Bu eğitimde, Ente Auth'u nasıl kurup kullanacağınızı ve bu çözümün geleneksel kimlik doğrulayıcılardan neden farklı olduğunu adım adım göstereceğiz.



## Ente Auth ile tanışın



Ente Auth, uçtan uca şifrelenmiş ve gizlilik dostu bir fotoğraf depolama hizmeti olan Ente Photos'un arkasındaki ekip tarafından geliştirilmiştir. Ente felsefesine sadık kalarak ("Ente" Malayalam dilinde "benim" anlamına gelir ve verileriniz üzerindeki kontrolü simgeler), Ente Auth kullanıcılara iki faktörlü kimlik doğrulama kodları üzerinde tam kontrol sağlamak için tasarlanmıştır.



### Ana Özellikler



**Standart TOTP kodları**: Ente Auth, çoğu hizmetle (GitHub, Google, Binance, ProtonMail, vb.) uyumlu geçici kodlar oluşturur. İhtiyaç duyduğunuz kadar 2FA hesabı ekleyebilirsiniz ve uygulama kodları sağlanan sırlara göre hesaplar.



**Uçtan uca şifrelenmiş bulut yedekleme**: Kodlarınız çevrimiçi olarak güvenli bir şekilde saklanır. Şifrelerinizi yalnızca siz çözebilirsiniz - şifreleme anahtarı şifrenizden türetilir ve yalnızca sizin tarafınızdan bilinir. Her şey sıfır bilgi mimarisi kullanılarak istemci tarafında şifrelendiğinden, Ente (sunucu) sırlarınız ve hatta hesap başlıklarınız hakkında hiçbir bilgiye sahip değildir.



**Çoklu cihaz senkronizasyonu**: Ente Auth'u birden fazla cihaza (akıllı telefon, tablet, bilgisayar) yükleyebilir ve kodlarınıza hepsinden erişebilirsiniz. Herhangi bir değişiklik, şifrelenmiş bulut aracılığıyla otomatik olarak ve anında diğer cihazlarınıza yayılır ve günlük işlerinizde size büyük esneklik sağlar.



**Minimalist, sezgisel Interface**: Uygulama, teknik olmayan kullanıcılar için bile öğrenmesi kolay, kolaylaştırılmış bir Interface sunar. 2FA hesapları, gerçek zamanlı olarak güncellenen hizmet adı, giriş bilgileriniz ve 6 basamaklı kod ile görüntülenir. Ente Auth ayrıca, sürenin dolmasına kısa bir süre kalmasını önlemek için bir sonraki kodu birkaç saniye önceden görüntüler.



**Açık kaynak ve denetlenmiş**: Ente Auth'un kaynak kodu AGPL v3.0 lisansı altında [GitHub'da herkese açıktır] (https://github.com/ente-io/auth). Herhangi bir geliştirici, kusurları veya istenmeyen davranışları kontrol etmek için bunu denetleyebilir. Uygulanan kriptografi, uygulamanın güvenliğinin ciddiyetinin bir garantisi olan bir [bağımsız dış denetim](https://ente.io/blog/cryptography-audit/) konusu olmuştur.



### Avantajlar ve sınırlamalar



**Avantajlar:**




- Uçtan uca şifreleme ile tasarım gereği gizlilik
- Tüm cihazlarınız arasında güvenli senkronizasyon
- Denetlenebilir açık kaynak kodu
- Interface açık, sezgisel kullanıcı Interface
- Kod kaybını önlemek için otomatik yedekleme
- Tüm platformlarda kullanılabilir (mobil ve masaüstü)



**Sınırlar:**




- Senkronizasyon için internet bağlantısı gereklidir
- İleri düzey kullanıcılar Aegis gibi %100 çevrimdışı çözümleri tercih edebilir (yalnızca Android)
- Yerleşik çözümlere kıyasla nispeten yeni



## Kurulum



Ente Auth en popüler platformlarda mevcuttur. Uygulamayı [resmi web sitesinden] (https://ente.io/auth) veya resmi mağazalardan indirebilirsiniz.



![Installation d'Ente Auth](assets/fr/01.webp)



*Mevcut tüm platformları içeren Ente Auth indirme sayfası*



### Android


Birkaç seçeneğiniz var:




- Google Play Store**: Klasik kurulum için "Ente Auth" araması yapın
- F-Droid**: Android açık kaynak uygulama kataloğundan, doğrulanmış yapı garantisiyle ve tescilli içerik olmadan edinilebilir
- Manuel kurulum** : APK dosyaları, yeni sürümlerin entegre bildirimi ile [projenin GitHub sayfasından] (https://github.com/ente-io/auth/releases) indirilebilir



### iOS (iPhone/iPad)


Ente Auth'u doğrudan Apple App Store'dan uygulama adını arayarak yükleyin. IOS uygulaması, Mac App Store aracılığıyla Apple Silicon çipleri (M1/M2) ile donatılmış Mac'lerde de çalıştırılabilir.



### Bilgisayarlar (Windows, macOS, Linux)


Ente Auth yerel masaüstü uygulamaları sunar. Ente.io/download](https://ente.io/download) veya [GitHub'ın Sürümler bölümü](https://github.com/ente-io/auth/releases) adreslerini ziyaret edin:





- Windows**: Bir EXE yükleyici sağlanır
- macOS**: DMG disk görüntüsünü Uygulamalar'a sürükleyip bırakın
- Linux** : Çeşitli formatlar mevcuttur (AppImage portable, Debian/Ubuntu için .deb, Fedora/Red Hat için .rpm)



**Not:** Bu eğitim Ente Auth v4.4.4 ve sonraki sürümleri temel almaktadır. Daha önceki sürümlerde küçük Interface farklılıkları olabilir.



### Interface Web


Kurulum olmadan, kodlarınıza [auth.ente.io](https://auth.ente.io) üzerinden herhangi bir tarayıcıdan erişebilirsiniz. Interface web, kodları görüntülemekle sınırlıdır (sorun giderme için kullanışlıdır), çünkü hesap eklemek güvenlik nedeniyle mobil veya masaüstü uygulaması gerektirir.



## İlk yapılandırma



### Hesap oluşturma



Ente Auth'u ilk başlattığınızda iki seçeneğiniz vardır:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Hesap oluşturma seçeneklerini içeren Ente Auth ana ekranı*



**Hesap ile (önerilir)**: "Hesap Oluştur "u seçin ve Address e-posta adresinizi ve bir parola girin. **Önemli**: bu parola verilerinizi şifrelemek için ana parola görevi görür. Veri kaybı olmadan geleneksel sıfırlama prosedürü olmadığından, güçlü ve benzersiz bir parola seçin. Şifreyi yanlış yere koyarsanız, şifrelenmiş verileriniz geri alınamaz.



**Çevrimdışı mod**: Uygulamayı bulut olmadan yerel olarak kullanmak için "Yedekleme olmadan kullan" seçeneğini seçin. Bu modda, kodlarınız cihazda kalır, ancak kaybetmemek için bunları manuel olarak dışa aktarmanız gerekir.



![Vérification email et récupération de clé](assets/fr/03.webp)



*E-posta doğrulama süreci ve 24 kelimelik kurtarma anahtarının oluşturulması*



Hesap oluşturmayı doğrulamak ve yeni bir cihazda kurtarmayı etkinleştirmek için bir e-posta doğrulaması istenebilir. Ente Auth ayrıca size 24 kelimelik bir kurtarma anahtarı sağlayacaktır (BIP39 yöntemine dayalı olarak). **Bu anahtarı** güvenli bir yere kaydetmeniz zorunludur: şifrenizi unutmanız halinde verilerinizi kurtarmanın tek yolu budur.



### Yerel güvenlik



Kod veya biyometri ile yerel korumayı etkinleştirmenizi şiddetle tavsiye ederim. Ayarlar → Güvenlik → Kilit ekranı** bölümüne gidin ve yapılandırın:





- Biyometrik kilit açma**: Cihazınızın özelliklerine bağlı olarak Face ID, parmak izi
- Uygulamaya özel PIN/şifre**
- Otomatik Kilit gecikmesi**: örneğin "Hemen" veya 30 saniye hareketsizlikten sonra



Bu koruma, birisinin kilidi açık telefonunuza erişmesi durumunda kodlarınıza yetkisiz erişimi önler. Bu kilidin ek bir bariyer olduğunu unutmayın: verileriniz bu koruma olmadan da uçtan uca şifrelenmiş olarak kalır.



## 2FA hesapları ekleyin



### Standart prosedür



Yeni bir 2FA hesabı eklemek için, Bull Bitcoin'da 2FA'yı etkinleştirmenin somut örneğini ele alalım:



![Configuration du premier compte](assets/fr/04.webp)



*Ente Auth'un ana Interface'si ilk 2FA* hesabını eklemeye hazır



**Servis tarafı (Bull Bitcoin)**: Bull Bitcoin hesabınıza giriş yapın, güvenlik ayarlarına gidin ve iki faktörlü kimlik doğrulamayı etkinleştirin.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* güvenlik ayarları menüsü



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Bull Bitcoin'de iki faktörlü kimlik doğrulamayı etkinleştirme seçeneği*



Hizmet daha sonra kimlik doğrulama uygulamanızla taramanız için bir QR kodu görüntüleyecektir:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*Bull Bitcoin tarafından kimlik doğrulayıcınızla taranmak üzere oluşturulan QR kodu*



**Ente Auth** içinde: "Bir kurulum anahtarı girin" seçeneğine tıklayın ve ardından Bull Bitcoin tarafından görüntülenen QR kodunu tarayın. Ente Auth hesabı otomatik olarak tanıyacak ve alanları dolduracaktır.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Ente Auth*'da Bull Bitcoin hesap ayrıntılarını yapılandırma



Bulmayı kolaylaştırmak için hizmetin adını ve oturum açma bilgilerinizi özelleştirebilirsiniz. Gelişmiş ayarlar (SHA1 algoritması, 30s periyodu, 6 hane) genellikle varsayılan olarak doğrudur.



**Servis tarafında doğrulama**: Bull Bitcoin'e dönün ve aktivasyonu tamamlamak için Ente Auth tarafından oluşturulan 6 haneli kodu girin.



![Saisie du code 2FA](assets/fr/09.webp)



*2FA* aktivasyonunu doğrulamak için Ente Auth tarafından oluşturulan kodu girin



![2FA activée](assets/fr/10.webp)



*Bull Bitcoin* üzerinde başarılı 2FA aktivasyonunun onayı



**Yedekleme kodları**: Bull Bitcoin size kurtarma kodları sağlayacaktır. **Bunları kimlik doğrulayıcınızdan ayrı olarak güvenli bir yere kaydedin.



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Bull Bitcoin* üzerinde generate acil durum yedekleme kodları seçeneği



![Codes de récupération](assets/fr/12.webp)



*Güvenli bir yerde saklamak için kurtarma kodlarının listesi*



### Organizasyon ve yönetim



Ente Auth çeşitli pratik özellikler sunar:



**Hızlı Kopyalama**: Otomatik olarak panoya kopyalamak için koda basın.



**Bağlama duyarlı eylemler**: Bir girişi düzenlemek, silmek, paylaşmak veya sabitlemek için basılı tutun (veya masaüstünde sağ tıklayın).



**Etiketler ve arama**: Hesaplarınızı etiketlerle (kişisel/profesyonel, hizmet kategorisine göre) düzenleyin ve hızlı bir şekilde filtrelemek için arama çubuğunu kullanın.



![Création d'un tag](assets/fr/17.webp)



*Etiket oluşturma süreci: bağlamsal menü ve oluşturma iletişim kutusu*



![Tag appliqué](assets/fr/18.webp)



*"Bitcoin" etiketi Bull Bitcoin* hesabına başarıyla uygulandı



**Otomatik simgeler**: Simple Icons] simge paketinin entegrasyonu sayesinde her giriş hizmetin logosuyla gösterilebilir (https://simpleicons.org/).



**Geçici güvenli paylaşım**: Benzersiz bir Ente Auth özelliği olan güvenli paylaşım, temel sırrı ifşa etmeden bir iş arkadaşınıza 2FA kodu iletmenizi sağlar. Maksimum 2, 5 veya 10 dakika geçerli şifreli bir bağlantı generate - alıcı kodu gerçek zamanlı olarak görür, ancak dışa aktaramaz veya hesap verilerine erişemez. Bu yöntem teknik yardım veya geçici işbirliği için idealdir ve basit bir ekran görüntüsü veya kısa mesaj ile mümkün olmayan bir güvenlik seviyesi sunar.



![Partage sécurisé](assets/fr/19.webp)



*Interface geçici güvenli paylaşım: süreyi seçin (5 dakika)*



**Güvenli ihracat/ithalat**: Ente Auth, kodlarınızı diğer uygulamalara aktarmanıza veya Google Authenticator ve diğer çözümlerden içe aktarmanıza olanak tanır. Dışa aktarım, şifrelenmiş bir dosya veya QR kodu aracılığıyla gerçekleşir ve güvenlikten ödün vermeden verilerinizin taşınabilirliğini garanti eder.



**BIP39 kurtarma anahtarı**: Uygulama, kripto para cüzdanlarıyla aynı olan BIP39 (Bitcoin Improvement Proposal) standardına göre otomatik olarak 24 kelimelik bir kurtarma cümlesi oluşturur. Bu ifade, ana şifrenizi unutsanız bile tüm kodlarınızı geri yüklemenizi sağlayan nihai kurtarma anahtarınızdır.



## Yapılandırma ve ayarlar



Ente Auth, uygulama ayarları üzerinden erişilebilen çok sayıda özelleştirme seçeneği sunar:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Ente Auth*'da mevcut parametrelere genel bakış



### Hesap ve veri yönetimi



![Paramètres de sécurité](assets/fr/14.webp)



*Gelişmiş güvenlik seçenekleri: e-posta doğrulama, PIN kodu, aktif oturumlar*



Güvenlik ayarları şunları yapmanıza olanak tanır:




- Yeni bağlantılar için e-posta doğrulamayı etkinleştirin
- Geçiş Anahtarını Etkinleştir
- Çeşitli cihazlarınızdaki aktif oturumları görüntüleyin
- PIN kodu veya biyometrik ayarlama



### Interface ve kullanım seçenekleri



![Paramètres généraux](assets/fr/15.webp)



*Interface parametreleri ve uygulama özelleştirmesi*



Genel ayarlar şunları içerir :




- Dil**: Interface çok dilli
- Ekran**: Büyük simgeler, kompakt mod
- Gizlilik**: Kodları gizle, hızlı arama
- Telemetri**: Hata raporlama (devre dışı bırakılabilir)



## Yedekleme ve senkronizasyon



### Şifreleme nasıl çalışır?



Bağlı bir Ente hesabıyla bir hesap eklediğinizde, uygulama bu hassas verileri ana anahtarınızı (parolanızdan türetilen) kullanarak hemen yerel olarak şifreler. Şifrelenmiş veriler daha sonra depolanmak üzere Ente sunucusuna gönderilir.



Bu mekanizma sayesinde, kodlarınızın uçtan uca şifrelenmiş bir bulut yedeği her zaman kullanılabilir. Cihazınızı kaybederseniz, Ente Auth'u yeniden yükleyin ve yeniden bağlanın: uygulama otomatik olarak tüm kodlarınızı indirecek ve şifresini çözecektir.



### Çoklu cihaz senkronizasyonu



Ente Auth'u hem akıllı telefon hem de bilgisayarda kullanırsanız, bir cihazdaki herhangi bir ekleme veya değişiklik saniyeler içinde diğerinde görünür. Bu senkronizasyon Ente'nin bulutu üzerinden gerçekleşir, ancak veriler uçtan uca şifrelenmiş olduğundan, sunucu yalnızca okunamayan şifrelenmiş içeriği görür.



![Synchronisation mobile](assets/fr/16.webp)



*Senkronizasyon demosu: mobil ve masaüstünden erişilebilen aynı Bull Bitcoin hesabı*



Senkronizasyon sorunsuzdur: Ente Auth'u akıllı telefonunuza yükleyin, kimlik bilgilerinizle giriş yapın ve tüm 2FA kodlarınız (burada Bull Bitcoin) otomatik olarak görünür. Yukarıdaki örnek masaüstü ve mobil arasında mükemmel senkronizasyonu göstermektedir - aynı Bull Bitcoin koduna her iki cihazdan da erişilebilir.



Gizlilik açısından, ne Ente ne de herhangi bir üçüncü taraf 2FA sırlarınıza erişemez. Meta veriler (etiketler, notlar, hizmet adları) bile gönderilmeden önce şifrelenir. Bu sıfır bilgi mimarisi, kodlarınızı yalnızca sizin deşifre edebilmenizi sağlar.



### Çevrimdışı kullanım



Senkronizasyon için İnternet gerekir, ancak tüm veriler yerel olarak depolandığından Ente Auth her cihazda mükemmel bir şekilde çevrimdışı çalışır. Çevrimdışı değişiklikler sıraya alınır ve bağlantı yeniden kurulur kurulmaz senkronize edilir.



## Güvenlik ve gizlilik



### Kriptografik garantiler



Ente Auth, sıfır bilgi mimarisi ile sağlam uçtan uca şifrelemeye dayanmaktadır. Kodlarınız, gelişmiş anahtar türetme işlevleri kullanılarak ana parolanızdan türetilen ve yalnızca sizin sahip olduğunuz bir anahtarla şifrelenir.



**Sıfır bilgi mimarisi: Ente verilerinize fiziksel olarak erişemez. Meta veriler (hizmet adları, etiketler, notlar) bile iletilmeden önce istemci tarafında şifrelenir. Bu yaklaşım, sunucularınıza bir saldırı veya devlet talebi olması durumunda, Ente'nin yalnızca şifreniz olmadan okunamayan şifrelenmiş verileri ifşa edebilmesini sağlar.



**Yerel şifreleme**: Şifreleme işlemi, buluta gönderilmeden önce tamamen cihazınızda gerçekleşir. Ente'nin sunucuları yalnızca şifrelenmiş verileri alır ve depolar, bu da hizmet yöneticileri için bile yetkisiz erişimi imkansız hale getirir.



### Şeffaflık ve denetimler



Kod [açık kaynak](https://github.com/ente-io/auth) olduğundan, topluluk arka kapıların olmadığını doğrulayabilir. Ente, uygulamasının güvenliğini doğrulamak için [çoklu dış denetimler](https://ente.io/blog/cryptography-audit/) gerçekleştirmiştir:





- Cure53** (Almanya): Uygulama ve kriptografik güvenlik denetimi
- Sembolik Yazılım** (Fransa): Özel kriptografik uzmanlık
- Fallible** (Hindistan): Sızma testi ve güvenlik açığı analizi



Tanınmış firmalar tarafından gerçekleştirilen bu bağımsız denetimler, Ente Auth'un kriptografik uygulamasının en iyi güvenlik uygulamalarına uygun olduğunu ve kritik kusurlar içermediğini garanti eder.



### Gizlilik Politikası



Ente Auth, minimum veri toplamaya dayalı bir [örnek gizlilik politikası] (https://ente.io/privacy/) uygular. Yalnızca hizmetin çalışması için kesinlikle gerekli olan bilgiler saklanır: kimlik doğrulama ve hesap kurtarma için e-posta Address'unuz.



**İzleme veya telemetri yok**: Çoğu uygulamanın aksine, Ente Auth hiçbir kullanım ölçümü, tanımlayıcı çarpışma verisi ve davranışsal bilgi toplamaz. Uygulama, müdahaleci reklam veya analiz izleyicileri olmadan çalışır.



**GDPR uyumluluğu**: Ente, Avrupa Genel Veri Koruma Yönetmeliği'ne tamamen uymaktadır. Verilerinize istediğiniz zaman erişme, düzeltme veya silme hakkına sahipsiniz. Veri aktarımı] (https://ente.io/take-control/) sadece bir tık uzağınızda ve hesabınızı kalıcı olarak silmek tüm verilerinizi sunuculardan siler.



**Merkezi olmayan, güvenli depolama**: Şifrelenmiş verileriniz 3 farklı ülkede, 3 farklı sağlayıcıda çoğaltılır ve tek bir bulut sağlayıcısına bağımlılıktan kaçınırken optimum kullanılabilirliği garanti eder.



Ente'nin iş modeli, verilerinizi paraya çevirerek gizliliğinizden ödün vermeden Ente Auth **ücretsiz ve sınırsız** olarak sunmamızı sağlayan ücretli Ente Photos hizmetine dayanmaktadır. Bu yaklaşım, reklamlara veya kişisel verilerin yeniden satışına dayanmadan hizmetin sürdürülebilirliğini garanti eder.



## Diğer çözümlerle karşılaştırma



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth, tüm avantajları bir araya getiren birkaç çözümden biri olarak öne çıkıyor: kaynak kodu şeffaflığı, şifreli bulut yedekleme ve platformlar arası senkronizasyon.



## Önerilen kullanım durumları



### Bireysel kullanıcılar



Ente Auth, 2FA'yı sistematik olarak etkinleştiren güvenlik bilincine sahip kişiler için idealdir. Artık telefon değiştirirken kodlarınızı kaybetme veya rahatlık ile güvenlik arasında seçim yapma konusunda endişelenmenize gerek kalmayacak.



### Aile ve çoklu cihaz kullanımı



Birden fazla cihaz kullanıyorsanız, uygulama kendi kendine gelir. Kodlarınızı akıllı telefonlara ve tabletlere kaydedebilir veya belirli aile kodlarını (Netflix, aile bulutu) eşzamanlı ve güvenli bir şekilde paylaşabilirsiniz.



### Profesyonel kullanım



Hassas hesapları yöneten ekipler için Ente Auth, "Organizasyon ve yönetim" bölümüne entegre edilmiş gelişmiş paylaşım özellikleri sayesinde güvenliği korurken işbirliğini kolaylaştırır.



## En iyi uygulamalar





- Acil durum kodlarınızı** saklayın: Her servis tarafından sağlanan kurtarma kodlarını telefonunuzdan uzak tutun.





- Güçlü bir ana parola kullanın**: Ente Auth ana parolanız, tüm kodlarınızı koruduğu için benzersiz ve sağlam olmalıdır.





- Yerel korumayı etkinleştirin**: Yetkisiz fiziksel erişimi önlemek için PIN veya biyometri yapılandırın.





- Aşırı özelleştirme yapmayın**: Senkronizasyonu tehlikeye atabilecek gelişmiş değişikliklerden kaçının.





- Uygulamayı güncel tutun**: Güncellemeler güvenlik açıklarını düzeltir ve işlevselliği artırır.





- Geri yüklemeyi test edin**: Ara sıra kodlarınızı başka bir cihaza geri yükleyip yükleyemeyeceğinizi kontrol edin.



## Sonuç



Ente Auth, iki faktörlü kimlik doğrulama için modern ve kapsamlı bir çözümü temsil eder. Güvenlik, şeffaflık ve kullanım kolaylığını bir araya getiren bu açık kaynaklı uygulama, kolaylıktan ödün vermeden talepkar kullanıcıların ihtiyaçlarını karşılamaktadır.



Sizi opak bir ekosisteme kilitleyen tescilli çözümlerin aksine Ente Auth, kimlik doğrulama verilerinizin kontrolünü size geri verirken şifreli yedeklemeleri sayesinde sizi kazara kaybolmaya karşı korur.



İster kişisel hesaplarınızı güvence altına almak isteyen bir birey, ister işletme erişimini yöneten bir ekip olun, Ente Auth, gizlilikten ödün vermeden dijital güvenlik yaklaşımınızı modernize etmek için akıllı bir seçimdir.



## Kaynaklar ve destek



### Resmi belgeler




- Resmi web sitesi**: [ente.io/auth](https://ente.io/auth)
- Yardım merkezi**: [help.ente.io/auth](https://help.ente.io/auth)
- Teknik blog**: [ente.io/blog](https://ente.io/blog)



### Kaynak kodu ve şeffaflık




- GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- Kriptografi denetimi**: [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### Topluluk




- Discord**: [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- Reddit**: [r/enteio](https://reddit.com/r/enteio)