---
name: SimpleX Sohbet
description: Kullanıcı kimliği olmayan ilk posta kutusu
---
![cover](assets/cover.webp)



2021 yılında piyasaya sürülen SimpleX, gizlilik konusunda radikal bir şekilde farklı bir yaklaşıma sahip ücretsiz bir anlık mesajlaşma uygulamasıdır. WhatsApp, Signal ve diğer merkezi mesajlaşma hizmetlerinin aksine, SimpleX kullanıcı yönetimiyle öne çıkmaktadır: kullanıcı tanımlayıcıları, takma adlar, numaralar veya görünür ortak anahtarlar yoktur. Tanımlayıcıların tamamen yokluğu, kullanıcıları ilişkilendirmeyi neredeyse imkansız hale getirerek yüksek düzeyde gizliliği garanti eder.



Bir hesap veya telefon numarası gerektiren çoğu uygulamanın aksine SimpleX, bir bağlantı veya geçici QR kodu paylaşarak görüşmeleri başlatmanıza olanak tanır. Her bağlantı benzersiz bir şifreli kanal oluşturur ve kişiler açık bir Exchange olmadan göndereni bulamaz veya yeniden iletişime geçemez. Mesajlar uçtan uca şifrelenir ve gönderildikten sonra onları silen ve ne göndereni ne alıcıyı ne de anahtarlarını gören aktarma sunucularından geçer.



![Image](assets/fr/01.webp)



Ağ mimarisi tamamen merkezsiz ve federasyonsuzdur: sunucular birbirlerini tanımazlar, global bir dizin tutmazlar ve herhangi bir kullanıcı profili barındırmazlar. Daha da iyisi, her kullanıcı kendi aktarıcı sunucusunu kurabilir ve kullanabilirken, genel ağdakilerle birlikte çalışabilir.



SimpleX tamamen açık kaynaklıdır (istemciler, protokoller ve sunucular), Android, iOS, Linux, Windows ve macOS'ta kullanılabilir. Yerel depolama alanı şifrelenmiş ve taşınabilirdir, böylece merkezi bir sunucuya güvenmeden bir profili bir cihazdan diğerine aktarabilirsiniz.



SimpleX, mesajlaşma uygulamalarının tüm klasik özelliklerini bir araya getiriyor. Bununla birlikte, ergonomisi WhatsApp veya Signal'inkinden daha az akıcı kalıyor. Ayrıca, özellikle kişi eklerken kullanımı daha kısıtlayıcı olabiliyor. Bu nedenle, bana göre, gizliliği önceliklerinin merkezine koyan ve bu nedenle günlük kullanıcı konforundan birkaç taviz vermeye hazır olan kullanıcılar için WhatsApp veya Signal'e uygun bir alternatif.



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



## SimpleX Chat uygulamasını yükleyin



SimpleX Chat tüm platformlarda kullanılabilir. Uygulamayı doğrudan telefonunuzun uygulama mağazasından indirebilirsiniz:




- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store](https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid](https://simplex.chat/fdroid/).



Android'de [APK ile yüklemek](https://github.com/simplex-chat/simplex-chat/releases) de mümkündür.



Bu eğitimde mobil versiyona odaklanacağız, ancak [masaüstü versiyonlarının da mevcut olduğunu] (https://simplex.chat/downloads/) (MacOS, Linux ve Windows) lütfen unutmayın. Masaüstü sürümünü mevcut bir mobil kullanıcı profiline bağlamak mümkündür, ancak bu senkronizasyonun çalışması için her iki cihazın da aynı yerel ağa bağlı olması gerekir.



![Image](assets/fr/02.webp)



## SimpleX Chat'te bir hesap oluşturun



Uygulamayı ilk başlattığınızda, "*Profilinizi oluşturun*" düğmesine tıklayın.



![Image](assets/fr/03.webp)



Gerçek adınız veya takma adınız olabilecek bir kullanıcı adı seçin ve ardından "*Oluştur*" düğmesine tıklayın.



![Image](assets/fr/04.webp)



Ardından, uygulamanın yeni mesajları kontrol edeceği sıklığı ayarlayın. Telefonunuzun pil ömrü bir sorun teşkil etmiyorsa, mesajları gerçek zamanlı olarak almak için "*Anında*" seçeneğini seçin. Pilinizden tasarruf etmeyi ve uygulamanın arka planda çalışmasını engellemeyi tercih ediyorsanız, "*Uygulama çalışırken*" seçeneğini seçin: bu durumda yalnızca uygulama açıkken mesaj alırsınız. Her 10 dakikada bir periyodik kontrolü tercih etmek olası bir uzlaşmadır.



Seçiminizi yaptıktan sonra "*Sohbeti kullan*" seçeneğine tıklayın.



![Image](assets/fr/05.webp)



Artık SimpleX Chat'e bağlısınız ve sohbete başlamaya hazırsınız.



![Image](assets/fr/06.webp)



## SimpleX Chat'in Kurulumu



Öncelikle, sağ alt köşedeki profil fotoğrafınıza ve ardından "*Ayarlar*" seçeneğine tıklayarak ayarlara erişin.



![Image](assets/fr/07.webp)



Varsayılan ayarlar genellikle çoğu kullanıcı için uygundur. Ancak, "*Veritabanı passphrase & dışa aktar*" menüsüne gitmenizi tavsiye ederim. Burada SimpleX hesap veritabanınızı yedekleme amacıyla dışa aktarabilirsiniz.



Bu veritabanını şifrelemek için kullanılan passphrase'yi de değiştirebilirsiniz. Varsayılan olarak rastgele oluşturulur ve cihazınızda yerel olarak saklanır. İsterseniz kendi passphrase'nizi tanımlayabilir ve yerel passphrase yedeğini silebilirsiniz: bu durumda uygulamayı her açtığınızda ve başka bir cihaza geçtiğinizde bunu manuel olarak girmeniz gerekecektir.



**Lütfen dikkat**: bu seçeneği seçerseniz, passphrase'ün kaybı tüm SimpleX profillerinizin ve mesajlarınızın kalıcı olarak kaybolmasına neden olacaktır.



![Image](assets/fr/08.webp)



Ayrıca "*Gizlilik ve güvenlik*" menüsüne gitmenizi ve burada "*SimpleX Lock*" seçeneğini etkinleştirmenizi tavsiye ederim. Bu, uygulamaya erişimi bir kilit kodu ile korur.



![Image](assets/fr/09.webp)



Son olarak, "*Bildirimler*" ve "*Görünüm*" menüleri SimpleX Chat'i tercihlerinize uyacak şekilde özelleştirmenizi sağlar.



![Image](assets/fr/10.webp)



## SimpleX Chat ile mesaj gönderin



SimpleX'te başka bir kişiyle bağlantı kurmak için iki seçeneğiniz vardır:




- Tek kullanımlık bir bağlantı kullanın;
- Yeniden kullanılabilir bir statik Address kullanın.



Statik bir Address, onu bilen herkesin SimpleX'te sizinle iletişim kurmasını sağlar. Kalıcı bir Address, zaman sınırı olmaksızın farklı kişiler tarafından birkaç kez kullanılabilir. Bu kalıcılık onu spam'e karşı daha savunmasız hale getirir. Bununla birlikte, diğer mesajlaşma uygulamalarının aksine, SimpleX Address'nızı silmek, mevcut konuşmaları etkilemeden tüm spam'leri durdurmak için yeterlidir. Aslında, bu Address yalnızca ilk bağlantıyı kurmak için kullanılır ve Exchange başladıktan sonra artık gerekli değildir.



Öte yandan, tek kullanımlık bağlantılar herhangi bir kullanıcı tarafından yalnızca bir kez kullanılabilir. Bir kişi bağlantıyı kullandıktan sonra bağlantı geçersiz hale gelir. Her yeni bağlantı için generate ile yeni bir bağlantı oluşturmanız gerekir.



### Statik Address ile



Address'u kullanmak istiyorsanız, Interface'un sol alt kısmındaki profil resminize tıklayın, ardından "*SimpleX Address* Oluştur "u seçin. Ardından "*SimpleX Address* Oluştur" seçeneğine tekrar tıklayın.



![Image](assets/fr/11.webp)



Yeniden kullanılabilir Address'iniz artık oluşturuldu. QR kodunu göstererek ya da bağlantıyı göndererek sizinle iletişime geçmek isteyen kişilerle paylaşabilirsiniz.



![Image](assets/fr/12.webp)



"*Address ayarları*" düğmesine tıklayın. Burada Address'niz ile ilişkili izinleri yapılandırabilirsiniz. "*Kişilerle paylaş*" seçeneği Address'nizi SimpleX profilinizde görünür hale getirir. Kişileriniz daha sonra ona danışabilecek ve sizinle iletişim kurmak isteyen diğer kişilere iletebilecektir.



"*Otomatik kabul*" seçeneği, Address'ünüz üzerinden gelen bağlantıları otomatik olarak kabul eder. Bu, "*Gizli kabul et*" seçeneğini etkinleştirmediğiniz sürece Address'ünüze sahip herkesin profilinizi görebileceği ve size mesaj gönderebileceği anlamına gelir. Bu, yeni bir bağlantı kurulduğunda adınızı ve profil fotoğrafınızı gizler ve bunları her muhatap için farklı olan rastgele bir takma adla değiştirir.



![Image](assets/fr/13.webp)



### Yeniden kullanılabilir bağlantı ile



Bir kişiyle bağlantı kurmanın ikinci yolu tek seferlik bir bağlantı oluşturmaktır. Bunu yapmak için, Interface'ün sağ alt köşesindeki kalem simgesine tıklayın, ardından "*Bir kerelik bağlantı oluştur*" seçeneğini seçin.



Kişiniz size bir bağlantı gönderdiyse, taramak veya yapıştırmak için "*Bağlantıyı Tara/Yapıştır*" seçeneğine tıklayın.



![Image](assets/fr/14.webp)



SimpleX daha sonra tek kullanımlık bir bağlantı oluşturur. Bunu herhangi bir yolla kişinize iletebilirsiniz: fiziksel Exchange, diğer mesajlaşma vb.



![Image](assets/fr/15.webp)



Bu davet bağlantısının hangi profille ilişkilendirileceğini de seçebilirsiniz. Bunu yapmak için QR kodunun hemen altındaki profilinize tıklayın. Daha sonra şunları yapabileceksiniz:




- mevcut profillerinizden birini seçin (bir sonraki bölümde nasıl birden fazla profil oluşturacağımızı göreceğiz);
- veya "*Incognito*" modunu seçerek adınızı ve profil fotoğrafınızı gizleyebilir, muhabiriniz için rastgele oluşturulmuş bir takma ad kullanabilirsiniz.



Burada "*Incognito*" modunu seçiyorum.



![Image](assets/fr/16.webp)



Bağlantım bağlantıyı kullandı. Kendi adına, "*Incognito*" modunu etkinleştirmedi, bu yüzden profil adını görüyorum, "*Bob*". Öte yandan, Bob benim gerçek ismim olan "*Loïc Morel*"i değil, rastgele bir takma ismi, bu durumda "*RealSynergy*"yi görüyor.



![Image](assets/fr/17.webp)



Hemen sohbete başlayabilirim ama önce bağlantıyı ele geçirmiş ya da MITM saldırısı gerçekleştirmiş olabilecek kötü niyetli biriyle değil, Bob ile konuştuğumu kontrol etmek istiyorum.



Bunu yapmak için, güvenlik bağlantımızı **uygulamanın dışında** kontrol edeceğiz. Bu önemlidir, çünkü bir MITM saldırısı durumunda dahili doğrulama tehlikeye girecektir. Bu yüzden başka bir güvenli mesajlaşma sistemi kullanın veya daha da iyisi kodları şahsen kontrol edin.



Sohbette Bob'in fotoğrafına ve ardından "*Güvenlik kodunu doğrula*" seçeneğine tıklayın. Bob'in de aynı şeyi kendi tarafında yapması gerekiyor.



![Image](assets/fr/18.webp)



Uzaktan çalışıyorsanız, kodları başka bir güvenli mesajlaşma sisteminde karşılaştırın (aynı olmalıdırlar). Daha da iyisi, yüz yüze görüşebiliyorsanız, "*Kodu tara*" seçeneğine tıklayarak kişinizin QR kodunu tarayın.



![Image](assets/fr/19.webp)



Doğrulama başarılı olursa, kişinizin adının yanında onay işaretli bir kalkan simgesi görünecektir. Bu, Bob ile alışveriş yaptığınıza dair güvencenizdir. Doğrulama başarısız olursa, "*Yanlış güvenlik kodu!*" uyarısı görünecektir.



![Image](assets/fr/20.webp)



Bu konuşma için ayarladığınız izinlere bağlı olarak artık Exchange mesajlarını, aramalarını ve dosyalarını Bob ile serbestçe yapabilirsiniz.



## SimpleX Chat profillerinizi özelleştirin



SimpleX'in en güçlü özelliklerinden biri, hepsine aynı yerel hesaptan erişilebilen tamamen ayrı birkaç kullanıcı profilini yönetme yeteneğidir. Bu, mesaj yönetimini karmaşıklaştırmadan farklı kimliklerinizi düzgün bir şekilde ayırmanıza olanak tanır.



Örneğin,:




- Gerçek adınızı ve profesyonel paylaşımlarınız için gerçek bir fotoğrafınızı içeren bir profil;
- Gerçek adınızı ve aile alışverişleriniz için komik bir fotoğrafınızı içeren bir profil;
- Sahte bir fotoğraf ve kişisel konuşmalarınız için bir takma ad içeren bir profil;
- Yabancılarla sohbet etmek için başka bir takma ad profili.



Burada yapacağımız şey de bu. Gerçek kimliğimle bağlantılı olan ana profilimi yapılandırarak başlıyorum. Bunu yapmak için sağ alt köşedeki profil fotoğrafıma ve ardından kullanıcı adıma tıklıyorum.



![Image](assets/fr/21.webp)



Daha sonra değiştirmek ve yeni bir fotoğraf eklemek için profil fotoğrafıma tıklıyorum.



![Image](assets/fr/22.webp)



Başka profiller eklemek için "*Sohbet profilleriniz*" menüsüne tıklayın.



![Image](assets/fr/23.webp)



Burada tüm profillerinizi göreceksiniz. Yeni bir profil oluşturmak için "*Profil ekle*" seçeneğine tıklayın.



![Image](assets/fr/24.webp)



Ardından yeni profiliniz için bilgileri seçin: isim, fotoğraf vb. Burada, belirli alışverişlerde gerçek kimliğimi gizlemek için bir takma ad ve farklı bir resim kullanıyorum.



![Image](assets/fr/25.webp)



Parmağınızı bir profilin üzerinde basılı tutarak onu gizleyebilirsiniz. Bu, ilgili tüm konuşmalarla birlikte uygulamada görünmez hale getirecektir. Bildirim almayı durdurmak için "*Sessiz*" yapmayı da seçebilirsiniz.



![Image](assets/fr/26.webp)



Profillerinizi oluşturduktan sonra, onları bağımsız olarak yönetebilirsiniz. Ana sayfadan, görüntülenecek aktif profili seçmeniz yeterlidir.



![Image](assets/fr/27.webp)



Bir davet bağlantısı veya statik Address oluşturduğunuzda, artık hangi profilin onunla ilişkilendirileceğini seçebilirsiniz. Örneğin, generate'ye bir bağlantı vermek için "*Satoshi Nakamoto*" profilini seçer ve bunu Alice'e gönderirsem, gerçek kimliğim "*Loïc Morel*"i hiç bilmeden yalnızca takma kimliğim "*Satoshi Nakamoto*"yu görecektir. Tersine, eğer ona gerçek profilimden bir bağlantı verirsem, takma isimli profilime bağlantı vermesinin hiçbir yolu olmayacaktır.



![Image](assets/fr/28.webp)



Tebrikler, artık WathsApp'a mükemmel bir alternatif olan SimpleX mesajlaşma ile hız kazanmış durumdasınız!



Ayrıca, mesajlaşma uygulamanız için ilginç bir alternatif olan Threema'yı sunduğum bu diğer öğreticiyi de tavsiye ederim:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74