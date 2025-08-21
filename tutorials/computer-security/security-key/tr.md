---
name: YubiKey 2FA
description: Fiziksel güvenlik anahtarı nasıl kullanılır?
---
![cover](assets/cover.webp)


Günümüzde iki faktörlü kimlik doğrulama (2FA), çevrimiçi hesapların yetkisiz erişime karşı güvenliğini artırmak için gerekli hale gelmiştir. Siber saldırılardaki artışla birlikte, hesaplarınızı güvence altına almak için yalnızca bir parolaya güvenmek bazen yetersiz kalmaktadır.


2FA, geleneksel parolaya ek olarak ikinci bir kimlik doğrulama biçimi gerektirerek ek bir Layer güvenlik sunar. Bu doğrulama, SMS yoluyla gönderilen bir kod, özel bir uygulama tarafından oluşturulan dinamik bir kod veya fiziksel bir güvenlik anahtarının kullanılması gibi çeşitli şekillerde olabilir. 2FA kullanımı, şifrenizin çalınması durumunda bile hesaplarınızın ele geçirilme riskini önemli ölçüde azaltır.


Başka bir eğitimde TOTP 2FA uygulamasının nasıl kurulacağını ve kullanılacağını anlatmıştım:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Burada, tüm hesaplarınız için ikinci bir kimlik doğrulama faktörü olarak fiziksel bir güvenlik anahtarının nasıl kullanılacağını göreceğiz.


## Fiziksel güvenlik anahtarı nedir?


Fiziksel güvenlik anahtarı, iki faktörlü kimlik doğrulama (2FA) yoluyla çevrimiçi hesaplarınızın güvenliğini artırmak için kullanılan bir cihazdır. Bu cihazlar genellikle, bağlanmaya çalışanın gerçekten meşru kullanıcı olduğunu doğrulamak için bir bilgisayarın bağlantı noktasına takılması gereken küçük USB anahtarlarına benzer.

![SECURITY KEY 2FA](assets/notext/01.webp)

2FA ile korunan bir hesapta oturum açtığınızda ve fiziksel bir güvenlik anahtarı kullandığınızda, yalnızca normal parolanızı girmeniz değil, aynı zamanda fiziksel güvenlik anahtarını bilgisayarınıza takmanız ve kimlik doğrulamasını doğrulamak için bir düğmeye basmanız gerekir. Bu yöntem ek bir Layer güvenlik sağlar, çünkü birisi şifrenizi ele geçirmeyi başarsa bile, anahtara fiziksel olarak sahip olmadan hesabınıza erişemez.


Fiziksel güvenlik anahtarı özellikle etkilidir çünkü iki farklı kimlik doğrulama faktörünü birleştirir: bilgi kanıtı (şifre) ve sahip olma kanıtı (fiziksel anahtar).


Ancak bu 2FA yönteminin dezavantajları da vardır. İlk olarak, hesaplarınıza erişmek istiyorsanız güvenlik anahtarını her zaman hazır bulundurmanız gerekir. Anahtarı anahtarlığınıza eklemeniz gerekebilir. İkinci olarak, diğer 2FA yöntemlerinden farklı olarak, fiziksel bir güvenlik anahtarı kullanmak, küçük cihazı satın almanız gerektiğinden bir başlangıç maliyeti içerir. Güvenlik anahtarlarının fiyatı, seçilen özelliklere bağlı olarak genellikle 30 ila 100 € arasında değişir.


## Hangi fiziksel güvenlik anahtarı seçilmeli?


Güvenlik anahtarınızı seçmek için çeşitli kriterler göz önünde bulundurulmalıdır.

İlk ve en önemlisi, cihaz tarafından desteklenen protokolleri kontrol etmeniz gerekir. En azından OTP, FIDO2 ve U2F'yi destekleyen bir anahtar seçmenizi öneririm. Bu ayrıntılar genellikle üreticiler tarafından ürün açıklamalarında vurgulanır. Her bir anahtarın uyumluluğunu doğrulamak için [dongleauth.com](https://www.dongleauth.com/dongles/) adresini de ziyaret edebilirsiniz.

Ayrıca, Yubikey gibi tanınmış markalar genellikle yaygın olarak kullanılan tüm sistemleri desteklese de, anahtarın işletim sisteminizle uyumlu olduğundan emin olun.


Ayrıca anahtarı bilgisayarınızda veya akıllı telefonunuzda bulunan bağlantı noktalarının türüne göre seçmelisiniz. Örneğin, bilgisayarınızda yalnızca USB-C bağlantı noktaları varsa, USB-C konektörlü bir anahtar seçin. Bazı tuşlar Bluetooth veya NFC üzerinden bağlantı seçenekleri de sunar.

![SECURITY KEY 2FA](assets/notext/02.webp)

Cihazları ayrıca suya ve Dust'ye dayanıklılık gibi ek özelliklerinin yanı sıra tuşun şekli ve boyutuna göre de karşılaştırabilirsiniz.


Güvenlik anahtarı markalarına gelince, Yubico, kişisel olarak kullandığım ve tavsiye ettiğim [YubiKey cihazları] (https://www.yubico.com/) ile en tanınmış olanıdır. Google da [Titan Security Key](https://store.google.com/fr/product/titan_security_key) ile bir cihaz sunuyor. Açık kaynaklı alternatifler için [SoloKeys](https://solokeys.com/) (OTP olmayan) ve [NitroKey](https://www.nitrokey.com/products/nitrokeys) ilginç seçenekler, ancak bunları test etme şansım hiç olmadı.


## Fiziksel güvenlik anahtarı nasıl kullanılır?


Güvenlik anahtarınızı aldıktan sonra özel bir kurulum gerekmez. Anahtar normalde teslim alındığında kullanıma hazırdır. Bu tür kimlik doğrulamayı destekleyen çevrimiçi hesaplarınızı güvence altına almak için hemen kullanabilirsiniz. Örneğin, Proton posta hesabımı bu fiziksel güvenlik anahtarıyla nasıl güvence altına alacağımı göstereceğim.

![SECURITY KEY 2FA](assets/notext/03.webp)

2FA'yı etkinleştirme seçeneğini hesap ayarlarınızda, genellikle "*Password*" veya "*Security*" bölümü altında bulabilirsiniz. Fiziksel bir anahtarla 2FA'yı etkinleştirmenizi sağlayan onay kutusuna veya düğmeye tıklayın.

![SECURITY KEY 2FA](assets/notext/04.webp)

Anahtarınızı bilgisayarınıza takın.

![SECURITY KEY 2FA](assets/notext/05.webp)

Doğrulamak için güvenlik anahtarınızın üzerindeki düğmeye dokunun.

![SECURITY KEY 2FA](assets/notext/06.webp)

Hangi tuşu kullandığınızı hatırlamak için bir ad girin.

![SECURITY KEY 2FA](assets/notext/07.webp)

İşte bu kadar, güvenlik anahtarınız hesabınızın 2FA kimlik doğrulaması için başarıyla eklendi.

![SECURITY KEY 2FA](assets/notext/08.webp)

Örneğimde, Proton posta hesabıma yeniden bağlanmaya çalışırsam, önce kullanıcı adımla birlikte parolamı girmem istenecek. Bu, kimlik doğrulamanın ilk faktörüdür.

![SECURITY KEY 2FA](assets/notext/09.webp)

Ardından, ikinci kimlik doğrulama faktörü için güvenlik anahtarımı girmem isteniyor.

![SECURITY KEY 2FA](assets/notext/10.webp)

Ardından, kimlik doğrulamasını doğrulamak için fiziksel anahtar üzerindeki düğmeye dokunmam gerekiyor ve Proton posta hesabıma yeniden bağlanıyorum.

![SECURITY KEY 2FA](assets/notext/11.webp)

Bu işlemi, özellikle e-posta hesaplarınız, parola yöneticileriniz, bulut ve çevrimiçi depolama hizmetleriniz veya finansal hesaplarınız gibi kritik hesaplar olmak üzere, bu şekilde güvenliğini sağlamak istediğiniz tüm çevrimiçi hesaplar için tekrarlayın.