---
name: Aegis Authenticator
description: Hesaplarınızı ikili kimlik doğrulama ile güvence altına almak için Aegis Authenticator'ı nasıl kullanabilirsiniz?
---

![cover](assets/cover.webp)



Günümüzde, iki faktörlü kimlik doğrulama (2FA) çevrimiçi hesapların güvenliğini sağlamak için çok önemlidir. Parolaya ek olarak, 30 saniye sonra sona eren ikinci bir faktör (genellikle 6 haneli bir kod) ekler ve bilgisayar korsanları için önemli ölçüde daha zor hale getirir. Özel bir TOTP (*Zaman Tabanlı Tek Kullanımlık Şifre*) uygulaması kullanmak, SIM değiştirme saldırıları ile ele geçirilebilen SMS'ten daha güvenlidir.



Ancak, tüm kimlik doğrulama uygulamaları eşit yaratılmamıştır. Birçok tescilli çözüm (Google Authenticator, Authy, vb.) sorun teşkil eder: tescilli ve kapalı kaynaklıdırlar (güvenliklerini denetlemek imkansızdır), bazen reklam izleyicileri entegre ederler, kodlarınızın şifreli yedeklemesini sunmazlar ve sizi kendi ekosistemlerine kilitlemek için hesaplarınızın dışa aktarılmasını bile engelleyebilirler.



Aegis Authenticator ise kendisini bu uygulamalara ücretsiz ve etik bir alternatif olarak sunuyor. Aegis, Android'de iki aşamalı doğrulama jetonlarınızı yönetmek için ücretsiz, güvenli, açık kaynaklı bir uygulamadır. Geliştirilmesi, yerel verilerin sağlam şifrelenmesi ve güvenli yedekleme olasılığı dahil olmak üzere diğer uygulamaların sunmadığı temel özelliklere odaklanmaktadır. Sonuç olarak Aegis, 2FA kodları üzerinde tam kontrol sahibi olmak isteyen herkes için ideal olan yerel, denetlenebilir bir çift kimlik doğrulama çözümü sunuyor.



## Aegis Authenticator ile tanışın



Aegis Authenticator, GPL v3 lisansı altında yayınlanan Android için açık kaynaklı bir 2FA uygulamasıdır. "Tasarım gereği gizlilik" felsefesiyle öne çıkar: uygulama tamamen çevrimdışı çalışır ve uzak bir hizmete bağlantı gerektirmez. Sonuç olarak, belirteçleriniz cihazınızda yerel olarak, anahtarı yalnızca sizde olan güvenli bir kasada saklanır.



### Temel özellikler



**Şifreli kasa:** tüm OTP kodlarınız, kullanıcı tanımlı bir ana parola ile korunan AES-256 şifreli bir kasada (GCM modu) saklanır. Daha fazla kolaylık için bu kasanın kilidini parola veya biyometrik verilerle (parmak izi, yüz tanıma) açabilirsiniz. Parola olmaması durumunda veriler şifrelenmemiş olacaktır - bu nedenle bir parola belirlemenizi şiddetle tavsiye ederiz.



**Gelişmiş organizasyon:** Aegis, birçok 2FA hesabınızı iyi organize eder. Girişlerinizi alfabetik olarak veya istediğiniz sıraya göre sıralayabilir, kolay erişim için kategorilere göre gruplandırabilir (ör. Kişisel, İş, Sosyal) ve her girişe kişiselleştirilmiş bir simge atayabilirsiniz. Bir hizmeti veya hesabı adına göre anında bulmak için bir arama çubuğu dahildir.



**Şifreli yerel yedeklemeler:** Hesaplarınıza erişiminizi asla kaybetmemenizi sağlamak için Aegis, kasanızın otomatik yedeklerini sunar. Bunlar şifrelenir (bir parola aracılığıyla) ve seçtiğiniz konuma (dahili depolama, bulut klasörü vb.) kaydedilebilir. Uygulama ayrıca hesap veritabanınızı manuel olarak, gerektiği gibi şifreli veya şifresiz biçimde dışa aktarabilir. Diğer 2FA uygulamalarından hesapları içe aktarmak da aynı derecede kolaydır (Aegis Authy, Google Authenticator, FreeOTP, andOTP vb. uygulamalardan içe aktarımı destekler).



**Güvenlik ve gizlilik:** uygulama varsayılan olarak tamamen çevrimdışıdır. Hiçbir ağ izni gerektirmez - yani dış dünyaya hiçbir veri aktarmaz ve hiçbir reklam izleyici veya davranışsal analiz modülü içermez. Aegis reklam göstermez ve bir kullanıcı hesabı gerektirmez: kurulur kurulmaz kayıt olmadan çalışmaya başlar. Kaynak kodu GitHub'da herkese açık olduğundan, topluluk onu özgürce denetleyebilir ve kötü amaçlı veya gizli işlevlerin bulunmadığını garanti eder.



**Modern Interface:** Aegis, koyu tema desteği (AMOLED modu dahil) ve hatta kodlarınızı ızgara olarak görüntülemek için isteğe bağlı bir döşeme görünümü ile zarif bir Materyal Tasarımı benimser. Interface düzenli ve gösterişsizdir ve güvenlik önlemi olarak kodların ekran görüntüsünün alınmasını engeller.



## Kurulum



Aegis Authenticator açık kaynak kodlu olduğundan, geliştiricileri gizlilik dostu dağıtım kanallarını tercih etmektedir. Yüklemenin iki ana yolu vardır:



### F-Droid aracılığıyla (önerilir)



En güvenli ve en kolay yol, ücretsiz alternatif mağaza olan F-Droid'dir. F-Droid henüz telefonunuzda yüklü değilse, resmi web sitesinden [F-Droid.org] (https://f-droid.org) indirerek başlayın. Sonra :





- F-Droid'i açın ve en son uygulama listesini almak için depolarınızı güncellediğinizden emin olun
- F-Droid'de "Aegis Authenticator" için arama yapın. Resmi uygulama görünmelidir (yayıncı: Beem Development)
- Yükle'ye basarak yüklemeyi başlatın. Aegis, F-Droid tarafından doğrulanan uygulamalardan biri olduğundan, güvenilir ve güvenli bir indirmeden yararlanırsınız



F-Droid aracılığıyla yükleme, uygulama güncellemelerini yayınlanır yayınlanmaz otomatik olarak alma avantajı sunar. Dahası, F-Droid uygulamanın istenmeyen tescilli bileşenler içermediğini garanti eder.



### GitHub aracılığıyla (imzalı APK)



Uygulamayı bir mağazadan geçmeden yüklemeyi tercih ederseniz, resmi APK'yı doğrudan projenin GitHub sayfasından indirebilirsiniz. Aegis deposunda ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), kararlı sürümlerin yayınlandığı Sürümler bölümüne gidin.





- En son APK sürümünü indirin
- APK'yı yüklemeden önce, cihazınızda bilinmeyen kaynaklardan uygulamaların yüklenmesine izin verdiğinizden emin olun (Android Ayarları'nda)
- GitHub'da sağlanan APK, geliştirici tarafından F-Droid'dekiyle aynı anahtarla imzalanmıştır



Manuel kurulumdan sonra uygulama aynı şekilde çalışacaktır. Güncellemelerin otomatik olmayacağını lütfen unutmayın: yeni sürümler için GitHub'ı periyodik olarak kontrol etmeniz gerekecektir.



### Google Play Store vs F-Droid



Aegis Authenticator hem Google Play Store'da hem de F-Droid'de mevcuttur ve size yükleme yöntemi seçeneği sunar:



**Google Play Store:**




- ✅ Android sistemine entegre otomatik güncellemeler
- ✅ Basit, tanıdık kurulum
- ✅ Diğer kanallarda olduğu gibi aynı imzalı APK



**F-Droid (önerilir) :**




- ✅ Ücretsiz ve açık kaynaklı mağaza
- ✅ Tekrarlanabilir ve doğrulanabilir yapı
- ✅ Google hizmeti gerekmez
- ✅ Özgür yazılım felsefesine saygı



Bu iki seçenek arasındaki seçim, Google ekosistemine ilişkin tercihlerinize bağlıdır. Basitliği tercih ediyorsanız Play Store idealdir. Google hizmetlerinden bağımsız, daha gizlilik dostu bir yaklaşım istiyorsanız, F-Droid daha iyi bir seçimdir.



## İlk yapılandırma



Aegis ilk kez başlatıldığında, 2FA kodunuzun güvenliğini sağlamak için bir başlangıç yapılandırma prosedürü önerilir:



![Configuration initiale Aegis](assets/fr/01.webp)



*İlk Aegis yapılandırma süreci: karşılama ekranı, güvenlik seçenekleri, ana parola tanımı ve sonlandırma*



### Ana parola belirleme



Aegis ilk olarak sizden bir ana parola seçmenizi isteyecektir. Bu parola, kasada saklanan tüm kimlik doğrulama belirteçlerinizi şifrelemek için kullanılacaktır. Sadece sizin bileceğiniz güçlü ve benzersiz bir parola belirlemenizi şiddetle tavsiye ederiz.



**⚠️ Uyarı:** bu şifreyi unutmayın - kaybederseniz, şifrelenmiş 2FA kodlarınız erişilemez hale gelecektir (arka kapı yoktur). Aegis onay için şifreyi iki kez girmenizi isteyecektir.



### Biyometrik kilit açmayı etkinleştirin (isteğe bağlı)



Android cihazınızda parmak izi okuyucu veya başka bir biyometrik sensör varsa, Aegis sizden biyometrik kilit açmayı etkinleştirmenizi isteyecektir. Bu seçenek isteğe bağlıdır ancak çok pratiktir: her seferinde şifreyi yazmak yerine parmak iziniz veya yüzünüzle uygulamanın kilidini hızlı bir şekilde açmanızı sağlar.



Biyometrinin ek bir kolaylık olduğunu unutmayın: biyometri değiştirildiğinde veya cihaz yeniden başlatıldığında ana parolanız hala gereklidir.



### Uygulama ayarlarını keşfedin



Uygulamanın içine girdiğinizde (ana Interface başlangıçta boştur), mevcut yapılandırma seçeneklerine aşina olun. Ekranın sağ üst köşesindeki açılır menüden (üç dikey nokta) ayarlara erişin ve ardından "Ayarlar "ı seçin.



![Interface principale et paramètres](assets/fr/02.webp)



*Interface ana Aegis başlangıçta boş, parametreler menüsüne erişim ve mevcut seçeneklere genel bakış*



Aegis ayarları menüsü birkaç önemli bölümü bir araya getirir:





- **Görünüm**: Temayı (açık, koyu, AMOLED), dili ve diğer görsel ayarları özelleştirin
- **Davranış**: Giriş listesiyle etkileşime girerken uygulama davranışını yapılandırın
- **Simge paketleri**: hesaplarınızın görünümünü ve hissini özelleştirmek için simge paketlerini yönetin ve içe aktarın
- **Güvenlik**: Şifreleme, biyometrik kilit açma, otomatik kilitleme ve diğer güvenlik parametreleri için ayarlar
- **Yedeklemeler**: Seçtiğiniz bir konuma otomatik yedeklemeleri yapılandırın
- **İçe ve Dışa Aktar**: Diğer kimlik doğrulama uygulamalarından yedekleri içe aktarın ve Aegis kasanızı manuel olarak dışa aktarın
- **Denetim günlüğü**: Uygulamadaki tüm önemli olayların ayrıntılı günlüğü



Bu açık organizasyon, Aegis'i tercihlerinize ve güvenlik ihtiyaçlarınıza göre yapılandırmanızı sağlar.



## Bir 2FA hesabı ekleyin



Aegis yapılandırıldıktan sonra, temel konulara geçelim: iki faktörlü hesaplarınızı eklemek. İşlem basittir ve Aegis kimlik doğrulama kodlarınızı entegre etmek için çeşitli yöntemler sunar.



### Mevcut üç ekleme yöntemi



Ana Aegis Interface'ten, ekleme seçeneklerine erişmek için sağ alttaki **+** düğmesine basın. Üç seçeneğiniz vardır:





- **QR kodunu tarayın**: Web hizmeti tarafından görüntülenen QR kodunu doğrudan tarayın
- **Görüntü tara**: Cihazınızda kayıtlı bir görüntüden QR kodunu tarayın
- **Manuel olarak girin**: 2FA hesap bilgilerini manuel olarak girin



### Pratik örnek: Bitwarden'ı yapılandırma



Süreci göstermek için Bitwarden'da 2FA aktivasyonunun somut örneğini ele alalım:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Bitwarden üzerinde 2FA aktivasyon örneği: Kimlik doğrulama seçenekleri ve Aegis önerisi ile Interface web*





- **Oturum açma ve ayarlara erişme**: Bitwarden hesabınıza giriş yapın ve ayarlara, "Güvenlik" sekmesine erişin
- **Sağlayıcılar bölümü**: "Sağlayıcılar" bölümüne gidin ve "Authenticator uygulaması" bölümündeki "Yönet" seçeneğine tıklayın



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Bir hesap eklemek için eksiksiz süreç: Hizmet tarafından görüntülenen QR kodu, gizli anahtar görünür ve doğrulama kodu girilir*





- **QR kodunu tarayın**: QR kodunu ve gizli anahtarı içeren bir açılır pencere açılır
- **Aegis'te**: Bilgileri otomatik olarak yakalamak için "QR kodu tara"yı kullanın
- **Doğrulama**: Aegis tarafından oluşturulan 6 haneli kodu "Doğrulama kodu" alanına girin
- **Etkinleştirme**: Etkinleştirmeyi tamamlamak için "Aç" üzerine tıklayın



### Ayrıntıları manuel olarak ekleyin



QR kodunu taramayı tercih ediyorsanız veya yapamıyorsanız, "Manuel olarak girin" seçeneğini kullanın. Form girmenize izin verir :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Yeni bir 2FA hesabı ekleme süreci: boş Interface, seçenek ekle, manuel giriş formu ve hesap başarıyla eklendi*





- **İsim** : Hizmet adı (örneğin Bitwarden, GitHub...)
- **İhraççı** : İhraççı (genellikle isimle aynıdır)
- **Grup**: Hesaplarınızı kategoriye göre düzenlemek için isteğe bağlı
- **Not**: Bu hesapla ilgili kişisel açıklamalar
- **Gizli** : Hizmet tarafından sağlanan gizli anahtar (varsayılan olarak maskelenmiştir)
- **Gelişmiş**: Gelişmiş parametreler (algoritma, periyot, basamak sayısı)



Hesap eklendikten sonra, mevcut kodu ve yenilemeye kalan süreyi gösteren bir zaman göstergesi ile listenizde görünür.



### Evrensel uyumluluk



Aegis, 2FA sunan neredeyse tüm siteler dahil olmak üzere TOTP ve HOTP standartlarını kullanan tüm hizmetlerle uyumludur: sosyal ağlar, bankalar, şifre yöneticileri, kripto platformları vb.



### Giriş organizasyonu



Birkaç hesap ekledikten sonra, Aegis'in organizasyonel araçlarını takdir edeceksiniz:





- **Özel sıralama:** Varsayılan olarak hesaplar alfabetik sırayla listelenir, ancak sıralamayı manuel olarak değiştirebilirsiniz
- **Gruplar ve kategoriler:** Kişisel hesaplarınızı iş hesaplarınızdan ayırmak için gruplar oluşturun veya bunları hizmet türüne göre gruplandırın (bankacılık, e-posta, sosyal ağlar vb.)
- **Özelleştirilmiş simgeler:** Aegis, mevcutsa otomatik olarak uygun bir simge atamaya çalışır, aksi takdirde birçok genel simge arasından seçim yapabilir veya bir resmi içe aktarabilirsiniz
- **Hızlı arama:** Üstteki arama çubuğu, eşleşen girişleri anında filtrelemek için birkaç harf yazmanıza olanak tanır



Bir girişe dokunduğunuzda, OTP kodu tam boyutlu olarak görüntülenir (gizliyse) ve uzun bir basışla panoya kopyalayabilirsiniz - bağlanmak istediğiniz uygulamaya yapıştırmak için kullanışlıdır.



## Güvenlik ve yedeklemeler



Aegis'in merkezinde güvenlik olduğundan, 2FA kodlarınızın nasıl korunduğunu ve bir sorun olması durumunda kalıcılığının nasıl sağlanacağını anlamak önemlidir.



### Güvenlik mimarisi



**Sağlam şifreleme**: Tüm kodlarınız, ana parolanızla birlikte GCM modunda **AES-256 algoritması** kullanılarak şifrelenmiş bir kasada saklanır. Anahtar türetme **scrypt** tabanlıdır ve kaba kuvvet saldırılarına karşı gelişmiş koruma sunar.



**Güvenli kilit açma** : Verilerinizin şifresini çözmek için ana parola gereklidir. Biyometri (isteğe bağlı), şifreleme anahtarını korumak için **Android Secure Keystore** ve TEE (Trusted Execution Environment) kullanır.



**Minimum izinler**: Aegis varsayılan olarak çevrimdışı çalışır ve yalnızca kameraya (QR taraması), biyometriye ve vibratöre erişim gerektirir. Hiçbir veri toplanmaz veya paylaşılmaz.



### Yedekleme seçenekleri



Aegis, farklı güvenlik ve rahatlık ihtiyaçlarına uygun çeşitli yedekleme stratejileri sunar:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface ek hesap, yedekleme uyarısı, otomatik yedekleme ayarları ve yedekleme stratejileri ile tamamlandı*



**1. Otomatik yerel yedeklemeler**




- Seçtiğiniz bir hedef klasörü yapılandırın
- Özelleştirilebilir sıklık (her değişiklikten sonra, günlük, vb.)
- Parola korumalı şifrelenmiş dosyalar (.aesvault)
- Senkronize klasörlerle uyumlu (Nextcloud, Dropbox, vb.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Yedekleme klasörü seçim süreci: dosya gezgini, hedef klasör ve erişim yetkisi*



**2. Android** bulut yedeklemeleri




- Android yedekleme sistemi ile isteğe bağlı entegrasyon
- Yalnızca şifreli kasalar için kullanılabilir (güvenlik korunur)
- Diğer Android verileriyle şeffaf yedekleme
- Cihaz değişiminde otomatik geri yükleme



**3. Manuel** ihracatlar




- Talep üzerine **Ayarlar > İçe ve Dışa Aktar** aracılığıyla dışa aktarın
- Şifreli (önerilen) veya açık format seçimi
- Geçişler veya ara sıra yapılan yedeklemeler için kullanışlıdır



### İyi güvenlik uygulamaları





- Bozulmayı önlemek için birkaç **yedek sürüm** bulundurun
- **Geri yükleme deneyerek yedeklerinizi düzenli olarak test edin**
- **Servis tarafından sağlanan kurtarma kodlarınızı ayrı olarak saklayın**
- Bulut yedeklemelerinde bile **ana parolanız** hala gereklidir
- **Ana parolanızı güvence altına alın**: bir parola yöneticisinde saklanan benzersiz, güçlü bir parola kullanın
- **Uygulamanızı en son güvenlik yamaları ile güncel tutun**
- Uygulamaya erişimi güvence altına almak için ayarlardan **otomatik kilidi** etkinleştirin
- **Kodlarınızın ele geçirilmesini önlemek için ekran görüntülerini devre dışı bırakın** (varsayılan seçenek)
- **Biyometriyi idareli kullanın**: kritik erişimler için parolaları tercih edin



## Diğer uygulamalarla karşılaştırma



Aegis diğer popüler kimlik doğrulama uygulamalarına karşı nasıl bir duruş sergiliyor?



### Aegis vs Google Authenticator



**Aegis :**




- ✅ Açık kaynak kodlu ve denetlenebilir
- ✅ Yerel şifreli yedekleme
- ✅ Gelişmiş organizasyon (gruplar, simgeler, arama)
- veri toplama yok
- ❌ Yalnızca Android



**Google Authenticator :**




- ✅ Android ve iOS'ta kullanılabilir
- ✅ Bulut senkronizasyonu (2023'ten beri)
- ❌ Kapalı kaynak kodu
- ❌ Sınırlı işlevsellik
- ❌ Potansiyel Google veri toplama



### Aegis vs Authy



**Aegis :**




- ✅ Açık kaynak
- ✅ Hesap gerekmez
- ✅ Kod dışa aktarımı mümkün
- ✅ Toplam veri kontrolü
- ❌ Yerel çoklu cihaz senkronizasyonu yok



**Authy :**




- ✅ Çoklu cihaz senkronizasyonu
- ✅ Android ve iOS'ta kullanılabilir
- ❌ Kapalı kaynak kodu
- ❌ Telefon numarası gerektirir
- ❌ Kodlar dışa aktarılamıyor
- ❌ Masaüstü uygulamaları Mart 2024'te kaldırıldı



Aegis, şeffaflığa, yerel güvenliğe ve verileri üzerinde tam kontrole değer veren Android kullanıcıları için mükemmeldir. Otomatik çoklu cihaz senkronizasyonuna kesinlikle ihtiyacınız varsa Authy gibi alternatifler daha uygundur.




## Sonuç



Aegis Authenticator, gizlilik dostu, güvenli ve şeffaf bir 2FA uygulaması arayanlar için mükemmel bir çözümdür. Açık kaynak yaklaşımı, sağlam şifreleme ve düzgün bir Interface ile birleştiğinde, çevrimiçi hesaplarınızı güvence altına almak için birinci sınıf bir seçim haline gelir.



Android ile sınırlı olmasına ve yerel bulut senkronizasyonundan yoksun olmasına rağmen Aegis, "tasarım gereği gizlilik" felsefesi ve tam veri kontrolü ile bu sınırlamaları fazlasıyla telafi ediyor. Dijital gizlilikleri konusunda endişe duyan kullanıcılar için Aegis, pazarın baskın tescilli çözümlerine güvenilir ve güçlü bir alternatif sunuyor.



Çevrimiçi hesaplarınızın güvenliği ticari şirketlerin iyi niyetine bağlı olmak zorunda değil. Aegis ile kimlik doğrulama kodlarınızın kontrolü, anahtarı yalnızca sizde olan dijital bir kasada sizde olur.



## Kaynaklar



### Resmi web siteleri




- **Resmi web sitesi**: [getaegis.app](https://getaegis.app/) - Başvuru sunumu ve indirme
- **Kaynak kodu**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Resmi GitHub deposu
- **F-Droid**: [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Ücretsiz mağaza üzerinden kurulum



### Teknik dokümantasyon




- **Kasa belgeleri**: [Kasa tasarımı](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Şifreleme ve güvenli mimarinin teknik açıklaması
- **Resmi SSS**: [getaegis.app/#faq](https://getaegis.app/#faq) - Sıkça sorulan soruların yanıtları
- **Proje wiki**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Tam kullanıcı belgeleri