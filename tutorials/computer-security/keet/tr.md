---
name: Keet
description: Eşler arası sohbet
---
![cover](assets/cover.webp)



Keet, herhangi bir sunucu olmadan çalışmak üzere tasarlanmış bir anlık mesajlaşma uygulamasıdır. Holepunch (Tether ve Bitfinex tarafından finanse edilen bir şirket) tarafından 2022 yılında başlatılan uygulama, tamamen eşler arası bir ağa dayanmaktadır ve radikal bir şekilde merkezi olmayan bir yaklaşıma sahiptir: mesajlar, aramalar ve dosyalar, aracılar olmadan doğrudan kullanıcılar arasında değiş tokuş edilir.



Keet, tüm iletişimleri uçtan uca şifreler ve hiçbir kişisel veri istemez. Kayıt anonimdir, telefon numarası veya e-posta gerekmez. Kısa mesaj alışverişine ek olarak Keet, çok yüksek kaliteli görüntülü görüşmelerin yanı sıra sınırsız dosya paylaşımı da sunar. Bu nedenle uygulama hem kişisel hem de profesyonel kullanım için hibrit bir şekilde kullanılabilir.



![Image](assets/fr/01.webp)



Şu anda (Nisan 2025), Keet tamamen açık kaynaklı değildir. Kaynak kodunun bir kısmı, özellikle kriptografik ve ağ bileşenleri olmak üzere [Holepunch'ın GitHub deposunda] (https://github.com/holepunchto) mevcuttur, ancak istemci Interface henüz mevcut değildir. Ancak Holepunch, eninde sonunda tüm uygulamayı açık kaynaklı hale getirme niyetini açıkladı. Bu öğreticiyi ne zaman keşfettiğinize bağlı olarak, bu çoktan yapılmış olabilir.




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



## Keet'i kurun



Keet tüm platformlarda mevcuttur. Uygulamayı doğrudan telefonunuzun uygulama mağazasından indirebilirsiniz:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



Android'de [APK ile yüklemek](https://github.com/holepunchto/keet-mobile-releases/releases) de mümkündür.



Bu eğitimde mobil versiyona odaklanacağız, ancak [bilgisayar versiyonlarının da mevcut olduğunu] (https://keet.io/) (MacOS, Linux ve Windows) lütfen unutmayın. Hesabınızı birden fazla cihazda senkronize etmeniz de mümkündür.



## Keet'te bir hesap oluşturun



İlk açılışta sunum ekranlarını görmezden gelebilirsiniz.



![Image](assets/fr/02.webp)



"*Ben yeni bir kullanıcıyım*" düğmesine tıklayın.



![Image](assets/fr/03.webp)



Kullanım koşullarını kabul edin, ardından "*Hızlı kurulum*" seçeneğine tıklayın.



![Image](assets/fr/04.webp)



Bir ad veya takma ad seçin, ardından "*Kurulumu bitir*" seçeneğine tıklayın.



![Image](assets/fr/05.webp)



Profiliniz artık oluşturulmuştur. Sonlandırmak için tekrar "*Kurulumu tamamla*" düğmesine tıklayın.



![Image](assets/fr/06.webp)



Profilinizi istediğiniz zaman "*Profil*" sekmesinden özelleştirebilirsiniz.



## Keet hesabınızı kaydedin



Yeni Keet hesabınızla yapılacak ilk şey, kurtarma cümlenizi kaydetmektir. Bu, kayıp veya cihaz değişikliği durumunda hesabınıza erişimi geri yüklemenizi sağlayacak 24 kelimeden oluşan bir dizidir. Bu ifade, onu bilen herkese hesabınıza tam erişim sağlar, bu nedenle güvenilir bir yedekleme yapmak ve asla ifşa etmemek önemlidir.



Bunu yapmak için Interface'in sağ alt tarafındaki "*Profil*" sekmesine tıklayın.



![Image](assets/fr/07.webp)



Ardından "*Ayarlar*" menüsüne erişin.



![Image](assets/fr/08.webp)



"*Gizlilik ve Güvenlik*" öğesini seçin.



![Image](assets/fr/09.webp)



Ardından "*Kurtarma ifadesi*" üzerine tıklayın.



![Image](assets/fr/10.webp)



Kurtarma ifadenizi görüntülemek için "*İfadeyi görüntüle*" düğmesine basın. Dikkatlice kopyalayın ve güvenli bir yerde saklayın.



![Image](assets/fr/11.webp)



## Keet ile mesaj gönderme



Keet'te iletişim kurmak için "*Odalar*" oluşturmanız gerekir. Bunu yapmak için, Interface'nin sağ üst köşesindeki kalem simgesine tıklayın.



![Image](assets/fr/12.webp)



"*Yeni grup sohbeti*" öğesini seçin.



![Image](assets/fr/13.webp)



"*Oda*" için bir ad ve açıklama seçin, ardından "*Grup sohbeti oluştur*" seçeneğine tıklayın.



![Image](assets/fr/14.webp)



"*Oda*"nız artık oluşturulmuştur. Katılımcıları davet etmek için sağ üstteki "*+*" simgesine tıklayın.



![Image](assets/fr/15.webp)



Davet bağlantısı aracılığıyla yeni üyelere verdiğiniz hakları ve bağlantının geçerlilik süresini tanımlayın. Ardından "*generate davet*" üzerine tıklayın.



![Image](assets/fr/16.webp)



Keet, "*Odanıza*" katılmak için bir bağlantı generate verecektir. Bu bağlantıyı kopyalayıp paylaşabilir ya da QR kodunu davet etmek istediğiniz kişilere okutabilirsiniz.



![Image](assets/fr/17.webp)



Artık mesaj ve multimedya dosyaları alışverişine başlayabilirsiniz. Bir arama başlatmak için sağ üst köşedeki telefon simgesine tıklayın.



![Image](assets/fr/18.webp)



Bu gruptan belirli bir üyeye özel mesaj da gönderebilirsiniz. Grubun profil resmine tıklayın, ardından "*Üyeler*" bölümünden istediğiniz üyeyi seçin.



![Image](assets/fr/19.webp)



"*DM isteği gönder*" düğmesine tıklayın ve mesajınızı girin.



![Image](assets/fr/20.webp)



DM isteği kabul edildikten sonra, bu kişiyi ana sayfada bulacak ve onunla özel olarak konuşabileceksiniz.



![Image](assets/fr/21.webp)



## Hesabınızı birden fazla cihazda senkronize edin



Artık Keet'i nasıl kullanacağınızı bildiğinize ve bir hesabınız olduğuna göre, onu bilgisayar gibi başka bir cihazda da senkronize edebilirsiniz. Bunu yapmak için, cep telefonunuzdaki uygulamayı açın, ardından "*Profil*" e tıklayın ve "*Ayarlar*" a erişin.



![Image](assets/fr/22.webp)



Ardından "*Cihazlarım*" menüsüne gidin.



![Image](assets/fr/23.webp)



"*Cihaz ekle*" üzerine tıklayın. Keet, yeni bir cihazı senkronize etmek için bir bağlantı generate verecektir. Bu bağlantıyı kopyalayın.



![Image](assets/fr/24.webp)



İkinci cihazınızda Keet'i yükleyin. Ana ekranda "*Mevcut kullanıcıyım*" seçeneğini seçin.



![Image](assets/fr/25.webp)



Ardından "*Cihazı bağla*" üzerine tıklayın.



![Image](assets/fr/26.webp)



İlk cihazınız tarafından sağlanan bağlantıyı yapıştırın ve ardından "*Senkronizasyonu başlat*" seçeneğine tıklayın.



![Image](assets/fr/27.webp)



İlk cihazınızda, bağlantıyı yetkilendirmek için "*Bağlantı cihazlarını onayla*" seçeneğine tıklayın.



![Image](assets/fr/28.webp)



İkinci cihazda, "*Cihazları bağla*" seçeneğine tıklayarak işlemi tamamlayın.



![Image](assets/fr/29.webp)



Artık tüm "*Oda*" ve konuşmalarınıza bu yeni cihazdan erişebilirsiniz.



![Image](assets/fr/30.webp)



Tebrikler, artık WathsApp'a harika bir alternatif olan Keet mesajlaşmasını kullanmaya başladınız! Bu öğreticiyi yararlı bulduysanız, aşağıya bir Green başparmak bırakırsanız çok minnettar olurum. Bu öğreticiyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!



Size Gmail'e çok daha gizlilik dostu bir alternatif olan Proton Mail'i tanıttığım bu diğer eğitimi de tavsiye ederim:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2