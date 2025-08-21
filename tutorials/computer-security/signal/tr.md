---
name: Sinyal
description: Kendinizi özgürce ifade edin
---
![cover](assets/cover.webp)



Signal, varsayılan olarak iyi bir gizlilik sunmak üzere tasarlanmış, uçtan uca şifrelenmiş bir mesajlaşma uygulamasıdır. Her mesaj, arama ve dosya, en sağlam mesajlaşma protokollerinden biri olarak kabul edilen Signal protokolü ile korunmaktadır. RCS iletişimleri için WathsApp, Facebook Messenger, Skype ve Google Messages dahil olmak üzere birçok başka uygulama tarafından yeniden kullanılır.



Signal, 2014 yılında Moxie Marlinspike (takma ad) tarafından başlatıldı ve 2018'den beri Brian Acton'ın (WhatsApp'ın kurucu ortağı) desteğiyle oluşturulan ve kar amacı gütmeyen bir kuruluş olan Signal Vakfı tarafından geliştirildi.



![Image](assets/fr/01.webp)



WhatsApp ile karşılaştırıldığında Signal şeffaflığıyla öne çıkıyor: Uygulamanın hem istemci hem de sunucu tarafındaki kodu tamamen açık kaynak kodlu. Bu, herkesin onu denetlemesine ve özellikle şifrelemenin ilan edildiği gibi uygulanıp uygulanmadığını kontrol etmesine olanak tanır.



Ancak Signal, diğer çözümlerle karşılaştırıldığında anonimlik söz konusu olduğunda ana zayıflığı olan bir telefon numarasının kullanımına dayanır. Buna rağmen, uygulama, tamamen açık mimarisi ve yaygın olarak benimsenen bir şifreleme protokolü sayesinde güvenlik ve gizlilik açısından bence en güvenilir olanlardan biridir ve bu nedenle diğer daha marjinal uygulamaların aksine test edilmiş ve denetlenmiştir.



| Application          | E2EE 1:1       | E2EE groups    | Anonymous registration | Open-source client license | Open-source server license | Decentralized server | Year of creation  |
| -------------------- | -------------- | -------------- | ---------------------- | -------------------------- | -------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                      | ❌                          | ❌                          | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                      | ❌                          | ❌                          | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optional) | ❌                      | ❌                          | ❌                          | ❌                    | 2011              |
| Telegram             | 🟡 (optional) | ❌              | 🟡                     | ✅                          | ❌                          | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                      | ❌                          | ❌                          | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                      | ✅                          | ✅                          | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                      | ✅                          | ❌                          | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                      | ✅                          | ✅                          | 🟡 (federated)      | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                      | ✅                          | N/A                        | 🟡 (via email)      | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                      | ✅                          | ✅                          | 🟡 (federated)      | 2014              |
| Session              | ✅              | ✅              | ✅                      | ✅                          | ✅                          | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                      | ✅                          | ✅                          | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                      | ✅                          | ❌                          | 🟡(no directory)     | 2019              |
| Keet                 | ✅              | ✅              | ✅                      | ❌                          | N/A                        | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                      | ✅                          | N/A                        | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                      | ✅                          | N/A                        | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                      | ✅                          | N/A                        | ✅                    | 2013              |

*E2EE = Uçtan uca şifreleme*




## Signal uygulamasını yükleyin



Signal tüm platformlarda kullanılabilir. Uygulamayı doğrudan telefonunuzun uygulama mağazasından indirebilirsiniz:




- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669);



Android'de [APK ile yüklemek](https://github.com/signalapp/Signal-Android/releases) de mümkündür.



Bu eğitimde mobil versiyona odaklanacağız, ancak [masaüstü versiyonlarının da mevcut olduğunu] (https://signal.org/fr/download/) (MacOS, Linux ve Windows) lütfen unutmayın. Ancak hesabınızı masaüstü sürümüyle senkronize etmeden önce mobil uygulamayı kurmanız gerekecektir.



## Signal'de bir hesap oluşturun



Uygulamayı ilk kez başlattığınızda, "*Devam*" düğmesine tıklayın.



![Image](assets/fr/02.webp)



Telefon numaranızı girin ve ardından "*Sonraki*" düğmesine tıklayın.



![Image](assets/fr/03.webp)



Size SMS ile bir doğrulama kodu gönderilecektir. Bu kodu Signal uygulamasına girin.



![Image](assets/fr/04.webp)



Signal hesabınızın güvenliğini sağlamak için bir PIN kodu seçin. Bu kod verilerinizi şifreler ve cihazınız kaybolursa hesabınıza erişimi geri yüklemek için kullanılabilir. Bu nedenle, mümkün olduğunca uzun ve rastgele olan sağlam bir PIN kodu seçmek ve güvenilir bir kaydını tutmak önemlidir.



![Image](assets/fr/05.webp)



Bu PIN kodunu ikinci kez onaylayın.



![Image](assets/fr/06.webp)



Artık kullanıcı profilinizi kişiselleştirebilirsiniz. Bir fotoğraf seçin, adınızı veya bir takma ad girin. Bu aşamada, sizi Signal'de numaranız üzerinden kimlerin bulabileceğini de tanımlayabilirsiniz. Görünür olmak istiyorsanız "*Herkes*" seçeneğini ya da telefon numaranız üzerinden takip edilememek için "*Hiç kimse*" seçeneğini seçin (bu durumda yalnızca "*Kullanıcı adınız*" ile eklenirsiniz). Seçimlerinizi yaptıktan sonra "*Sonraki*" üzerine tıklayın.



![Image](assets/fr/07.webp)



Artık Signal'e bağlısınız ve Exchange mesajlarına hazırsınız.



![Image](assets/fr/08.webp)



## Signal hesabınızı kurma



Uygulama ayarlarına erişmek için sol üst köşedeki profil fotoğrafınıza tıklayın.



![Image](assets/fr/09.webp)



"*Hesap*" menüsü profil ayarlarınızı yönetmenizi sağlar. Varsayılan ayarları korumanızı tavsiye ederim. Hesabınızı belirli saldırı türlerine karşı koruyan "*Kayıt Kilidi*" seçeneğini de etkinleştirebilirsiniz. Bu menü aynı zamanda hesabınızı yeni bir cihaza aktarmak için ihtiyacınız olan seçenekleri de içerir.



![Image](assets/fr/10.webp)



Ayarlarda profil resminize tekrar tıkladığınızda profilinizi kişiselleştirme seçeneklerine ulaşacaksınız. Bir "*Kullanıcı Adı*" belirlemenizi tavsiye ederim: bu, telefon numaranızı ifşa etmeden diğer insanlarla iletişime geçmenizi sağlayacaktır.



![Image](assets/fr/11.webp)



"*QR kodu veya bağlantı*" seçeneğini seçerek, sizi Signal'e eklemek isteyen biriyle paylaşmanız gereken bilgileri alırsınız.



![Image](assets/fr/12.webp)



"*Gizlilik*" menüsü özellikle önemlidir. Burada numaranızın görünürlüğünü, kişilerinizle mesajlarınızın yönetimini ve uygulama üzerinde verilen çeşitli yetkileri kontrol etmek için seçenekler bulacaksınız.



![Image](assets/fr/13.webp)



Interface'i ve uygulamanın çalışmasını kişisel ihtiyaçlarınıza göre uyarlamak için "*Görünüm*", "*Sohbetler*" ve "*Bildirimler*" menülerini keşfetmekten çekinmeyin.



## Masaüstü uygulamasını bağlayın



Masaüstü uygulamasını bağlamak için, yazılımı bilgisayarınıza yükleyerek başlayın (bu eğitimin ilk bölümüne bakın). Ardından, telefonunuzda Ayarlar'a gidin ve "*Bağlı cihazlar*" bölümünü açın.



![Image](assets/fr/14.webp)



"*Yeni bir cihaz bağla*" düğmesine tıklayın.



![Image](assets/fr/15.webp)



Bilgisayarınızda yazılımı başlatın, ardından telefonunuzu kullanarak ekranda görüntülenen QR kodunu tarayın. Konuşmalarınızı içe aktarmak istiyorsanız, "*Mesaj geçmişini aktar*" seçeneğini seçin.



![Image](assets/fr/16.webp)



Cihazlarınız artık tamamen senkronize edilmiştir.



![Image](assets/fr/17.webp)



## Signal ile mesaj gönderme



Signal'de biriyle iletişim kurmak için önce onu kişi olarak eklemeniz gerekir. Birkaç seçenek vardır: onları telefon numaraları aracılığıyla ekleyebilir (kişi bu yolla bulunma seçeneğini etkinleştirmişse) veya Signal ID'lerini kullanabilirsiniz.



Interface'nin sağ alt köşesindeki kalem simgesine tıklayın.



![Image](assets/fr/18.webp)



Benim durumumda, kişiyi kullanıcı adına göre eklemek istiyorum. Bu yüzden "*Kullanıcı adına göre bul*" seçeneğine tıklıyorum.



![Image](assets/fr/19.webp)



Daha sonra giriş bilgilerini yapıştırabilir veya QR kodunu tarayabilirsiniz.



![Image](assets/fr/20.webp)



İletişim kurmak için ona bir mesaj gönderin.



![Image](assets/fr/21.webp)



Görüşme daha sonra ana sayfada görünecektir. Kişi iletişim isteğinizi kabul ederse, adını ve profil fotoğrafını görürsünüz.



![Image](assets/fr/22.webp)



Tebrikler, artık WathsApp'a harika bir alternatif olan Signal mesajlaşmayı kullanmaya başladınız! Bu eğitimi faydalı bulduysanız, aşağıya bir Green başparmak bırakırsanız çok minnettar olurum. Bu öğreticiyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!



Size Gmail'e çok daha gizlilik dostu bir alternatif olan Proton Mail'i tanıttığım bu diğer eğitimi de tavsiye ederim:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2