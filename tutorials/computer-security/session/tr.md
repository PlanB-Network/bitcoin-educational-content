---
name: Oturum
description: Meta verileri değil, şifrelenmiş mesajları gönderin
---
![cover](assets/cover.webp)



Session, 2020 yılında oluşturulan ve geleneksel mesajlaşmadan daha yüksek düzeyde gizlilik sunmak üzere tasarlanmış şifreli bir mesajlaşma uygulamasıdır. İlk olarak *Oxen Privacy Tech Foundation*, ardından *Session Technology Foundation* tarafından geliştirilmiştir.



Session bazı ilginç teknik özelliklere sahiptir: mesajların uçtan uca şifrelenmesi, kullanılabilirliği ve yedekliliği garanti etmek için organize edilmiş merkezi olmayan bir ağ ve Tor'dan esinlenen onion yönlendirme. Ayrıca, kayıt için telefon numarası gerektiren WathsApp veya Signal'in aksine, Session hiçbir kişisel bilgi istemiyor (numara yok, e-posta yok, sadece bir çift kriptografik anahtar).



Session, meta veri sızıntılarını en aza indirirken mesajlar, dosyalar, sesli mesajlar, sesli aramaların yanı sıra 100 üyeye kadar gruplar (ve bunun ötesinde topluluklar) göndermenizi sağlar.



![Image](assets/fr/01.webp)



Session her şeyden önce gizliliği önceliklerinin merkezine koyan kullanıcılara yöneliktir. Bu mesajlaşma hizmeti, modern gözetim modellerine dayanacak şekilde tasarlanmış mimarisiyle WhatsApp'a ciddi bir alternatif oluşturuyor.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Uçtan uca şifreleme*



## Oturum uygulamasını yükleyin



Oturum tüm platformlarda kullanılabilir. Uygulamayı doğrudan telefonunuzun uygulama mağazasından indirebilirsiniz:




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).



Android'de [APK ile yüklemek](https://github.com/session-foundation/session-android/releases) de mümkündür.



Bu eğitimde mobil versiyona odaklanacağız, ancak [bilgisayar versiyonlarının da mevcut olduğunu] (https://getsession.org/download) (MacOS, Linux ve Windows) lütfen unutmayın. Daha sonra, bir hesabı birden fazla cihaz arasında nasıl senkronize edeceğimize bakacağız.



## Oturum'da bir hesap oluşturun



İlk açılışta "*Hesap oluştur*" seçeneğine tıklayın.



![Image](assets/fr/02.webp)



Profiliniz için bir görünen ad seçin. Bu bir takma ad veya gerçek adınız olabilir.



![Image](assets/fr/03.webp)



Daha sonra iki bildirim yönetimi modu arasında seçim yapmanız gerekecektir:





- Hızlı mod ("*Firebase Cloud Messaging/Apple Push Notification Service*")**: Google veya Apple tarafından sağlanan bildirim hizmetleri sayesinde (sisteminize bağlı olarak) mesaj bildirimlerini neredeyse gerçek zamanlı olarak almanızı sağlar. Bunun çalışması için, IP Address ve benzersiz bir bildirim kimliğiniz Google veya Apple'a iletilir ve Oturum hesap kimliği de bir STF sunucusuna (Tor aracılığıyla) kaydedilir. Bu mod, meta verilerin (kuşkusuz minimum düzeyde) açığa çıkmasını içerir, ancak mesaj içeriğini veya kişileri tehlikeye atmaz ve gerçek etkinliğinizin izlenmesine izin vermez. Bu nedenle bu mod yanıt verme açısından daha verimlidir, ancak merkezi bir altyapıya dayanır ve gizlilik açısından biraz daha az etkilidir.





- Yavaş mod (*arka planda yoklama*)**: Oturum uygulaması arka planda aktif kalır ve yeni mesajlar için ağı periyodik olarak yoklar. Bu yaklaşım, üçüncü taraf sunuculara hiçbir veri iletilmediği için ilkine göre daha fazla gizliliği garanti eder; ne Google, Apple ne de STF sunucuları herhangi bir bilgi almaz. Öte yandan, bu modun iki dezavantajı vardır: bildirimler gecikebilir (birkaç dakikaya kadar) ve arka plandaki uygulama etkinliği nedeniyle enerji tüketimi genellikle daha yüksektir.



![Image](assets/fr/04.webp)



Artık Oturum uygulamasına bağlısınız ve mesaj alışverişine başlayabilirsiniz.



![Image](assets/fr/05.webp)



## Oturum hesabınızı kaydedin



Session'ı kullanmaya başlamadan önce yapmanız gereken ilk şey, cihazınızı kaybetmeniz durumunda geri yükleyebilmek için hesabınızı kaydetmektir. Bunu yapmak için, "*Kurtarma şifrenizi kaydedin*" seçeneğinin yanındaki "*Devam*" düğmesine tıklayın.



![Image](assets/fr/06.webp)



Oturum daha sonra bir Mnemonic cümlesi görüntüleyecektir. Bunu dikkatlice kopyalayın ve güvenli bir yerde saklayın. Bu ifade Session hesabınıza tam erişim sağlar, bu nedenle ifşa edilmemesi önemlidir. Özellikle mevcut telefonunuz kaybolur veya değiştirilirse, hesabınıza başka bir cihazdan erişmek için buna ihtiyacınız olacaktır.



![Image](assets/fr/07.webp)



Bu ifade, Bitcoin cüzdanlarında kullanılan Mnemonic ifadelerine benzer şekilde çalışır. Bu nedenle, bir Mnemonic ifadesini kaydetmek için en iyi uygulamaları açıkladığım bu diğer eğitime başvurmanızı tavsiye ederim:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Lütfen dikkat**: Mnemonic cüzdanlarında kullanılan Bitcoin ifadelerinden farklı olarak, Oturum'da **her kelimeyi kesinlikle bütün olarak kaydetmelisiniz**. İlk 4 harf yeterli değildir!



## Oturum uygulamasının ayarlanması



Uygulama ayarlarına erişmek için Interface'nın sol üst köşesindeki profil fotoğrafınıza tıklayın. Burası bir profil fotoğrafı ekleyebileceğiniz yerdir.



![Image](assets/fr/08.webp)



"*Gizlilik*" menüsünde çeşitli özellikleri etkinleştirebilir veya devre dışı bırakabilirsiniz (dikkat edin, bazıları IP Address'nizi açığa çıkarabilir). Ayrıca uygulamaya erişmek için kimlik doğrulaması gerektiren "*Uygulamayı Kilitle*" seçeneğini etkinleştirmenizi öneririm.



![Image](assets/fr/09.webp)



"*Bildirim*" menüsünde, "*Hızlı Mod*" ve "*Yavaş Mod*" arasında bir seçim bulacaksınız (eğitimin önceki bölümlerine bakın). Ayrıca bildirimleri tercihlerinize uyacak şekilde özelleştirebilirsiniz.



![Image](assets/fr/10.webp)



Son olarak, Interface'i zevkinize göre uyarlamak için "*Görünüm*" menüsüne gidin. "*Kurtarma Şifresi*" menüsü, yeni bir yedekleme yapmak isterseniz Mnemonic ifadenizi geri almanızı sağlar.



![Image](assets/fr/11.webp)



## Oturum ile mesaj gönderme



Diğer kişilerle iletişime geçmek için ana sayfadaki "*+*" düğmesine tıklayın.



![Image](assets/fr/12.webp)



Çeşitli seçenekler mevcuttur. Bir grup oluşturmak veya gruba katılmak istiyorsanız, "*Grup Oluştur*" veya "*Topluluğa Katıl*" seçeneğini seçin.



![Image](assets/fr/13.webp)



Birinin sizi kişi olarak eklemesini istiyorsanız, Oturum Kimliğinizi QR kodu olarak taramasını sağlayabilirsiniz.



![Image](assets/fr/14.webp)



Oturum açma bilgilerinizi uzaktan göndermek için "*Bir Arkadaşınızı Davet Edin*" seçeneğine tıklayın. Daha sonra Oturum Kimliğinizi kopyalayabilir ve başka bir iletişim kanalı üzerinden gönderebilirsiniz. Bu bilgileri ana sayfadan profil fotoğrafınıza tıklayarak da alabilirsiniz.



![Image](assets/fr/15.webp)



Başka bir kişinin Oturum Kimliğine sahipseniz ve bunu eklemek istiyorsanız, "*Yeni Mesaj*" üzerine tıklayın.



![Image](assets/fr/16.webp)



Daha sonra tanımlayıcısını metne yapıştırabilir veya QR kodu olarak varsa doğrudan tarayabilirsiniz.



![Image](assets/fr/17.webp)



Ardından bu kişiye bir ilk mesaj gönderin.



![Image](assets/fr/18.webp)



Kişi isteğinizi kabul eder etmez, kullanıcı adının göründüğünü göreceksiniz ve onunla özgürce sohbet edebileceksiniz.



![Image](assets/fr/19.webp)



## Masaüstü yazılımını senkronize edin



Hesabınızı bilgisayarınızda senkronize etmek için yazılımı yüklemeniz gerekir. [Resmi web sitesinden indirin] (https://getsession.org/download). Yüklemeden önce orijinalliğini ve bütünlüğünü kontrol etmenizi tavsiye ederim.



![Image](assets/fr/20.webp)



İlk açılışta "*Bir hesabım var*" seçeneğine tıklayın.



![Image](assets/fr/21.webp)



Mnemonic ifadenizi girin ve her kelime arasında bir boşluk bıraktığınızdan emin olun.



![Image](assets/fr/22.webp)



Artık konuşmalarınıza bilgisayarınızdan erişebilirsiniz.



![Image](assets/fr/23.webp)



Tebrikler, artık WathsApp'a mükemmel bir alternatif olan Oturum mesajlaşmasını kullanmayı öğrendiniz!



Ayrıca, mesajlaşma uygulamanız için ilginç bir alternatif olan Threema'yı sunduğum bu diğer öğreticiyi de tavsiye ederim:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74