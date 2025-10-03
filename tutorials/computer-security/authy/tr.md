---
name: Authy 2FA
description: 2FA uygulaması nasıl kullanılır?
---
![cover](assets/cover.webp)


Günümüzde iki faktörlü kimlik doğrulama (2FA), çevrimiçi hesapların yetkisiz erişime karşı güvenliğini artırmak için gerekli hale gelmiştir. Siber saldırıların artmasıyla birlikte, hesaplarınızı güvence altına almak için yalnızca bir parolaya güvenmek bazen yetersiz kalmaktadır. 2FA, parolaya ek olarak ikinci bir kimlik doğrulama biçimi gerektirerek ek bir Layer güvenlik sağlar. Bu doğrulama, SMS yoluyla gönderilen bir kod, özel bir uygulama tarafından oluşturulan dinamik bir kod veya fiziksel bir güvenlik anahtarı kullanımı gibi çeşitli şekillerde olabilir. 2FA kullanımı, parolanızın çalınması durumunda bile hesaplarınızın ele geçirilme riskini büyük ölçüde azaltır.


## kimlik Doğrulama Uygulamaları aracılığıyla 2FA


Fiziksel güvenlik anahtarları gibi diğer çözümleri diğer eğitimlerde inceleyeceğiz, ancak bu eğitimde özellikle 2FA uygulamalarını tartışmayı öneriyorum. Bu uygulamaların çalışması oldukça basittir: 2FA bir hesapta etkinleştirildiğinde, her girişte sizden yalnızca normal şifreniz değil, aynı zamanda 6 basamaklı bir kod da istenecektir. Bu kod 2FA uygulamanız tarafından oluşturulur. Bu 6 haneli kodun önemli bir özelliği statik olmamasıdır; uygulama tarafından her 30 saniyede bir yeni bir kod oluşturulur.

![AUTHY 2FA](assets/notext/01.webp)

Kodun her 30 saniyede bir yenilenmesi, bir saldırganın hesabınıza erişmesini çok zorlaştırır. Bu sistem saldırganların çalınan veya ele geçirilen bir kodu tekrar kullanmasını engeller, çünkü kodun süresi hızla dolar. Bu nedenle, bir saldırgan kodu ele geçirmeyi başarsa bile, yeni bir kod gerekmeden önce yalnızca çok kısa bir süre boyunca kullanabilecektir. Dahası, kodun bu kadar sık değişmesi, kaba kuvvet yoluyla kodu tahmin etmeye çalışan bir bilgisayar korsanı için mevcut süreyi önemli ölçüde azaltır.


kimlik doğrulama uygulamaları aracılığıyla 2FA, çevrimiçi hesaplarınızın güvenliğini önemli ölçüde artırmak için kullanımı kolay ve ücretsiz bir yöntemdir.


Google Authenticator ve Microsoft Authenticator'ın en bilinenleri olduğu 2FA kurmak için çok sayıda uygulama vardır. Ancak, bu eğitimde size Authy adında daha az bilinen başka bir çözümü tanıtmak istiyorum. Tüm bu uygulamalar aynı TOTP (*Zaman Tabanlı Tek Kullanımlık Şifre*) protokolünü kullanarak çalışır, bu da kullanımlarını oldukça benzer hale getirir.

Authy, büyük teknoloji şirketlerinin diğer çözümlerine göre çeşitli avantajlar sunar. Her şeyden önce, 2FA belirteçlerinizi birden fazla cihaz arasında senkronize etmenize olanak tanır; bu, telefon kaybı veya değişikliği durumunda yararlı olabilir. Authy ayrıca generate şifreli bir yedekleme yapmanızı ve çevrimiçi olarak saklamanızı sağlayarak, birincil cihazınızı kaybetseniz bile belirteçlerinize erişiminizi asla kaybetmemenizi sağlar. Kullanıcı Interface perspektifinden bakıldığında, şahsen Authy'nin alternatiflerinden daha hoş ve sezgisel bir deneyim sunduğunu düşünüyorum.


## Authy nasıl kurulur?


Akıllı telefonunuzda, uygulama mağazasına (Google Play Store veya Apple Store) gidin ve "*Twilio Authy Authenticator*" için arama yapın.



- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)

![AUTHY 2FA](assets/notext/02.webp)

Uygulamayı ilk kez başlattığınızda bir hesap oluşturmanız gerekecektir. Ülkenizin arama kodunu ve telefon numaranızı seçin, ardından "*Gönder*" düğmesine tıklayın.

![AUTHY 2FA](assets/notext/03.webp)

Kod kurtarma için e-posta adresinizi Address girin.

![AUTHY 2FA](assets/notext/04.webp)

Address'ünüzü doğrulamak için size bir e-posta gönderilecektir. Onaylamak için alınan 6 rakamı girin.

![AUTHY 2FA](assets/notext/05.webp)

Telefon numaranızı doğrulamak için mevcut iki yöntemden birini seçin. SMS almayı tercih ederseniz, numaranızı onaylamak için mesajla gelen 6 haneli kodu girin.

![AUTHY 2FA](assets/notext/06.webp)

Tebrikler, Authy hesabınız oluşturuldu!

![AUTHY 2FA](assets/notext/07.webp)

## Authy nasıl yapılandırılır?


Başlamak için, ekranın sağ üst kısmında bulunan üç küçük noktaya tıklayarak uygulamanın ayarlarına gidin.

![AUTHY 2FA](assets/notext/08.webp)

Ardından "*Ayarlar*" üzerine tıklayın.

![AUTHY 2FA](assets/notext/09.webp)

"*Hesabım*" sekmesinde, hesabınızı değiştirme seçeneğiniz vardır. "*Uygulama Koruması*" seçeneğini seçerek uygulamaya bir PIN kodu eklemenizi öneririm. Bu, uygulamanıza erişmek için ekstra bir Layer güvenlik ekler.

![AUTHY 2FA](assets/notext/10.webp)

"*Hesaplar*" sekmesinde, jetonlarınız için bir yedekleme ayarlayabilirsiniz. Bu yedekleme, bir sorun olması durumunda kodlarınızın kurtarılmasını sağlar. Tanımlamanız gereken bir parola kullanılarak şifrelenir. Bu parolanın güçlü olması ve güvenli bir yerde saklanması önemlidir. Örneğin aynı Authy hesabına sahip ikinci bir cihaz gibi başka kurtarma yöntemleriniz varsa bu yedeği ayarlamak zorunlu değildir.

![AUTHY 2FA](assets/notext/11.webp)In the "*Devices*" tab, you can see all the devices synchronized with your Authy account. You have the option to disable the use of multiple devices, which restricts access to your account to that device only. If you use only one device, this can increase the security of your account, but make sure you have another backup method in case you lose that device.


Başka cihazların eklenmesine izin vermeyi tercih ediyorsanız, yeni bir cihaz eklemeden önce Authy hesabınızdaki mevcut yetkili cihazlardan onay alınmasını gerektiren seçeneği etkinleştirmenizi tavsiye ederim.

![AUTHY 2FA](assets/notext/12.webp)

Yeni bir cihaz eklemek için, aynı kimlik bilgilerini kullanarak önceki bölümde sunulan kurulum işlemini tekrarlamanız yeterlidir. Daha sonra ana cihazınızdan bu yeni erişimi onaylamanız istenecektir.


## Bir hesapta 2FA nasıl kurulur?


Bir hesapta Authy gibi bir uygulama aracılığıyla 2FA kimlik doğrulama kodu ayarlamak için hesabın bu özelliği desteklemesi gerekir. Günümüzde, çevrimiçi hizmetlerin çoğu bu 2FA seçeneğini sunmaktadır, ancak durum her zaman böyle değildir. Başka bir eğitimde sunduğum Proton posta hesabı örneğini ele alalım:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

![AUTHY 2FA](assets/notext/13.webp)

Bu 2FA seçeneğini genellikle hesabınızın ayarlarında, genellikle "*Password*" veya "*Security*" bölümünün altında bulabilirsiniz.

![AUTHY 2FA](assets/notext/14.webp)

Proton posta hesabınızda bu seçeneği etkinleştirdiğinizde, size bir QR kodu sunulur. Daha sonra bu QR kodunu Authy uygulamanızla taramanız gerekir.

![AUTHY 2FA](assets/notext/15.webp)

Authy'de "*+*" düğmesine tıklayın.

![AUTHY 2FA](assets/notext/16.webp)

"*Karekod Tarama*" üzerine tıklayın. Ardından web sitesindeki QR kodunu tarayın.

![AUTHY 2FA](assets/notext/17.webp)

Gerekirse kullanıcı adınızı ayarlama seçeneğiniz de vardır. Değişiklikleri yaptıktan sonra "*KAYDET*" düğmesine tıklayın.

![AUTHY 2FA](assets/notext/18.webp)

Authy daha sonra her 30 saniyede bir yenilenen, söz konusu hesaba özel 6 haneli dinamik kodunuzu görüntüleyecektir.

![AUTHY 2FA](assets/notext/19.webp)

2FA kurulumunu tamamlamak için bu kodu web sitesine girin.

![AUTHY 2FA](assets/notext/20.webp)

Bazı siteler 2FA'yı etkinleştirdikten sonra size kurtarma kodları da sağlayacaktır. Bu kodlar, Authy uygulamanıza erişiminizi kaybetmeniz durumunda hesabınıza erişmenizi sağlar. Bunları güvenli bir yere kaydetmenizi öneririm.

![AUTHY 2FA](assets/notext/21.webp)Your account is now secured with two-factor authentication via the Authy app.

![AUTHY 2FA](assets/notext/22.webp)

Hesaba her giriş yaptığınızda, Authy tarafından oluşturulan dinamik kodu sağlamanız gerekecektir. Artık bu 2FA yöntemiyle uyumlu tüm hesaplarınızı güvence altına alabilirsiniz. Authy'de yeni bir hesap eklemek için uygulamanın sağ üst köşesindeki üç küçük noktaya tıklayın.

![AUTHY 2FA](assets/notext/23.webp)

Ardından "*Hesap Ekle*" seçeneğine tıklayın.

![AUTHY 2FA](assets/notext/24.webp)

İlk hesap için kullanılanlarla aynı adımları izleyin. Çeşitli dinamik kodlarınız Authy ana sayfasında görünür olacaktır.