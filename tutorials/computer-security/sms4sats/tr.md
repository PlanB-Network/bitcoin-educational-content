---
name: SMS4Sats
description: Bitcoin Lightning ile ödeme yaparak anonim olarak SMS alın ve gönderin
---

![cover](assets/cover.webp)



SMS doğrulaması birçok çevrimiçi hizmet için bir zorunluluk haline gelmiştir. İster bir platformda hesap oluşturmak, ister bir kaydı doğrulamak ya da bir kimliği onaylamak için olsun, web siteleri neredeyse sistematik olarak bir telefon numarası talep etmektedir. Bu yaygın uygulama, gizliliğini korumak isteyen herkes için büyük bir sorun teşkil ediyor: kişisel numaranız kalıcı bir tanımlayıcı haline geliyor, çeşitli dijital faaliyetlerinizi gerçek kimliğinizle ilişkilendiriyor ve istenmeyen ticari taleplere kapı açıyor.



**SMS4Sats** bu soruna SMS mesajları almak ve göndermek için geçici telefon numaraları sunarak yanıt vermektedir. Hizmet, kayıt gerektirmeyen modeli ve Lightning Network üzerinden özel Bitcoin ödemesiyle öne çıkıyor. Birkaç satoshi karşılığında, kişisel numaranızı asla açıklamadan bir kaydı doğrulamanıza olanak tanıyan tek kullanımlık bir numara alırsınız.



Bu eğitim size üç SMS4Sats özelliği hakkında rehberlik edecektir: doğrulama SMS'i alma, anonim SMS gönderme ve birkaç saatliğine geçici bir numara kiralama.



## SMS4Sats nedir?



SMS4Sats, [sms4sats.com](https://sms4sats.com) adresinden erişilebilen ve Bitcoin Lightning ile ödeme yaparak anonim SMS yönetimi sağlayan çevrimiçi bir hizmettir. Hizmet üç farklı işlev sunmaktadır: tek kullanımlık doğrulama kodlarının alınması, herhangi bir numaraya SMS gönderilmesi ve birkaç saatliğine geçici numaraların kiralanması.



### Felsefe ve işletme modeli



Proje, maksimum gizlilik ve finansal egemenlik sağlamak üzere tasarlanmıştır. Hesap oluşturmayı gerektirmeyen ve yalnızca Bitcoin Lightning ödemelerini kabul eden SMS4Sats, kişisel veri sağlama ihtiyacını tamamen ortadan kaldırıyor. E-posta adresi, kredi kartı, kişisel bilgi gerekmez. Hizmetlere erişmek için sadece Lightning ödemesi gereklidir.



Hizmet, yaklaşık 120 ülkede 400'den fazla site ve uygulamayı destekleyerek yaygın doğrulama ihtiyaçlarının çoğunu karşılamaktadır. Bu geniş coğrafi kapsam, sosyal ağlardan mesajlaşma hizmetlerine kadar çeşitli platformlarda kayıtların doğrulanmasını sağlar.



### Şartlı ödeme modeli



SMS4Sats, SMS alım işlevi için koşullu Yıldırım faturaları (hodl faturaları) kullanır. Bu mekanizma, yalnızca SMS gerçekten alındığında ücretlendirilmenizi sağlar. Tahsis edilen süre içinde (maksimum 20 dakika) hiçbir mesaj gelmezse, ödeme otomatik olarak iptal edilir ve satoshiler wallet'inize iade edilir. Bu garanti, iade edilmeyen gönderme ve kiralama özellikleri için geçerli değildir.



## Üç SMS4Sat'ın özellikleri



SMS4Sats arayüzü, üç farklı kullanıma karşılık gelen üç sekme etrafında düzenlenmiştir: *doğrulama kodlarını almak için *RECEIVE**, anonim SMS göndermek için **SEND** ve geçici bir numara kiralamak için **RENT**.



### SMS alma



Ana özellik, benzersiz bir doğrulama kodu almak için geçici bir numara almanızı sağlar. Kod alındıktan ve kullanıldıktan sonra numara kalıcı olarak devre dışı bırakılır.



### SMS Gönderin



Bu özellik, kimliğinizi açıklamadan herhangi bir telefon numarasına SMS göndermenizi sağlar. Alıcı mesajı anonim bir numaradan alacaktır.



### Bir oyun kiralayın



SMS4Sats, tek bir numara üzerinden birden fazla SMS mesajı almak isteyen kullanıcılar için geçici kiralama seçeneği sunar. Bu seçenek, kiralama süresi boyunca birkaç mesaj almanıza ve göndermenize olanak tanır.



**Fiyatlar hakkında not** : Bu eğitimde gösterilen fiyatlar gösterge niteliğindedir. Numaranın ülkesine, hedef servise ve mevcut talebe göre değişir. Örneğin, Telegram Fransa'ya bir SMS, koşullara bağlı olarak 1.500 ila 5.000 satoshiye mal olabilir. Ödeme yapmadan önce daima Lightning faturasının tam tutarını kontrol edin.



## Bir doğrulama SMS'i alın



Bir doğrulama kodu almak için SMS4Sats'ın nasıl kullanılacağına, bir Telegram hesabı oluşturarak ayrıntılı bir şekilde bakalım.



### Adım 1: Ülke ve hizmet seçin



Sms4sats.com](https://sms4sats.com) adresine gidin ve **RECEIVE** sekmesinde kalın. Açılır menüden istediğiniz numaranın ülkesini seçin. Aboneliğinizin hedef hizmeti listeleniyorsa, alım şansını optimize etmek için onu seçin.



![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)



Bu örnekte, ülke olarak Fransa'yı ve hedef hizmet olarak Telegram'i seçiyoruz. Bir sonraki adıma geçmek için **NEXT** düğmesine tıklayın.



### Adım 2: Lightning faturasını ödeyin



Yıldırım faturası bir QR kodu şeklinde görüntülenir. Tutar, ülkeye ve seçilen hizmete göre değişir. Lightning wallet'unuzla QR kodunu tarayın veya manuel olarak ödemek için faturayı kopyalayın.



![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)



Önemli mesaja dikkat edin: "SMS Kodu Yok = Ödeme Yok". SMS almazsanız, ödemeniz otomatik olarak iptal edilecek ve en fazla 20 dakika içinde iade edilecektir.



### Adım 3: Geçici numarayı alın



Ödeme onaylandıktan sonra, geçici telefon numarası hemen görüntülenir. Bir sayaç SMS'in alınması için kalan süreyi gösterir.



![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)



Kayıt olmak istediğiniz hizmette kullanmak için bu numarayı kopyalayın (burada +33 7 74 70 09 66).



### Adım 4: Hedef hizmetteki numarayı kullanın



Hesabınızı oluşturduğunuz uygulama veya web sitesindeki geçici numarayı girin. Telegram örneğimizde numarayı girin, onaylayın ve doğrulama kodunu bekleyin.



![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)



Süreç geleneksel kayıt ile aynıdır: numarayı girersiniz, Telegram SMS ile bir doğrulama kodu gönderir ve ardından hesap oluşturmayı tamamlarsınız.



### Adım 5: Doğrulama kodunu alın



SMS4Sats arayüzüne geri dönün. SMS alınır alınmaz, aktivasyon kodu otomatik olarak görüntülenir. Kolayca kopyalamak için **KODU KOPYALA** üzerine tıklayın.



![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)



Kaydınızı tamamlamak için bu kodu hedef servise girin. Geçici numara daha sonra kalıcı olarak devre dışı bırakılır.



## Anonim bir SMS gönderin



SMS4Sats ayrıca kimliğinizi açıklamadan herhangi bir numaraya SMS mesajı göndermenizi sağlar.



### Adım 1: Mesajın yazılması



GÖNDER** sekmesine tıklayın. Hedef telefon numarasını uluslararası arama koduyla birlikte girin ve mesajınızı yazın (maksimum 1600 karakter).



![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)



Ödemeye geçmek için **NEXT** butonuna tıklayınız.



### Adım 2: Öde ve gönder



Görüntülenen Lightning faturasını ödeyin. Ödeme onaylandıktan sonra SMS hemen alıcıya gönderilir.



![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)



Mesajın gönderildiğini onaylamak için bir onay kodu görüntülenir. Alıcı SMS'i anonim bir numaradan alacaktır.



## Geçici bir numara kiralayın



Aynı numara üzerinden birden fazla SMS mesajı gerektiren kullanımlar için KİRALA özelliği bir numarayı birkaç saatliğine kiralamanızı sağlar.



### Kiralama yapılandırması



KİRALA** sekmesine tıklayın. Ülke ve süre seçin.



![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)



**Dikkat edilmesi gereken önemli noktalar:**




- Fiyatlar ülkeye ve kalış süresine göre değişir
- Tek kullanımlık SMS mesajlarının aksine kiralamalar iade edilmez**
- Kiralık numaralar genellikle Telegram ile çalışmaz
- Bu seçenek, art arda birkaç hizmete abone olmak için uygundur



SONRAKİ** seçeneğine tıkladıktan ve Lightning faturasını ödedikten sonra, SMS mesajları almak ve göndermek için kiralama süresi boyunca kullanabileceğiniz bir numara alacaksınız.



## Avantajlar ve sınırlamalar



### Önemli Noktalar



**Kişisel veri gerekmez**: Kayıt gerektirmeyen model, hiçbir kişisel bilginin toplanmamasını garanti eder.



**Üç ek fonksiyon**: Alma, gönderme ve kiralama çoğu ihtiyacı karşılar.



**Sadece Bitcoin ile ödeme** : Lightning Network anlık ve takma isimli işlemlere izin verir.



**Otomatik geri ödeme**: SMS mesajları alırken, hodl fatura sistemi yalnızca SMS geldiğinde ödeme yapmanızı garanti eder.



### Dikkate alınması gereken kısıtlamalar



**Göreceli SMS kanalı güvenliği**: SMS kodları sağlam bir kimlik doğrulama yöntemi değildir ve hassas hesaplar için kullanılmamalıdır.



**Değişken uyumluluk**: Birçok site sanal numaraları algılar ve engeller. Birkaç deneme gerekli olabilir.



**Tekrar kullanılamayan numaralar**: Tek kullanımdan sonra numara geri dönüştürülür ve geri kazanılamaz.



**Para iadesi olmayan kiralamalar**: Tek seferlik SMS mesajlarının aksine, kiralamalarda para iade garantisi yoktur.



## En iyi uygulamalar



### Daha fazla gizlilik için Tor kullanın



SMS4Sats'a [Tor](sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion) üzerinden erişilebilir. Bu yapılandırma, hizmete erişirken IP adresinizi maskeler.



### Kritik hesaplardan kaçının



Önemli hesaplarınız (banka, ana e-posta) için asla tek kullanımlık bir numara kullanmayın. Bu platformlar daha sonraki bir tarihte numaranızı yeniden doğrulamanızı gerektirirse, hesaba erişiminizi kaybedersiniz.



### Dijital kimliklerinizi ayırın



Sahte hesaplar için, geçici numarayı tek kullanımlık bir e-posta adresi ve normal kullanımınızdan izole edilmiş bir tarayıcı ile birleştirin.



### Sağlam bir 2FA seçin



Hesabınız oluşturulduktan sonra, daha güçlü kimlik doğrulama çözümlerini etkinleştirin: TOTP uygulaması (Aegis, Ente Auth) veya FIDO2 fiziksel güvenlik anahtarı.



## Sonuç



SMS4Sats, gizli SMS yönetimi için eksiksiz bir çözümdür. İster bir doğrulama kodu almak, ister anonim bir mesaj göndermek veya geçici bir numara kiralamak isteyin, hizmet Bitcoin Lightning ile ödeme sayesinde çok çeşitli gizlilik ihtiyaçlarını karşılar.



Bununla birlikte, sınırlamalarını aklınızda bulundurun: hizmet mutlak anonimliği garanti etmez ve hassas veya uzun vadeli hesaplar için uygun değildir. Akıllıca ve sınırlamalarının farkında olarak kullanıldığında SMS4Sats, telefon iletişiminiz üzerindeki kontrolü yeniden kazanmak için pratik bir araçtır.



## Kaynaklar





- [SMS4Sats resmi web sitesi](https://sms4sats.com)
- [Hizmet SSS](https://sms4sats.com/faq)
- [Tor adresi](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)