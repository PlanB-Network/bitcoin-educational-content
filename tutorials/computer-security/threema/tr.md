---
name: Threema
description: Güvenli, anonim anlık mesajlaşma
---
![cover](assets/cover.webp)



2012 yılında İsviçre'de kurulan Threema, gizlilik ve güvenliği garanti etmek için tasarlanmış bir anlık mesajlaşma uygulamasıdır. WhatsApp, Telegram veya Signal'in aksine, Threema bir hesap oluşturmak için telefon numarası veya e-posta Address gerektirmez. Her kullanıcının tamamen anonim kayıt sağlayan benzersiz bir tanımlayıcısı vardır.



Teknik açıdan, Threema üzerinden yapılan iletişimler uçtan uca şifrelenmektedir. Mobil uygulama kodu 2020'den beri açık kaynak kodludur, ancak sunucu altyapısı tescilli ve merkezi olmaya devam etmektedir. Sunucular yalnızca İsviçre'de (verilerin korunmasına yönelik yasal çerçevesiyle tanınan bir ülke) barındırılmaktadır.



![Image](assets/fr/01.webp)



Threema'nın Android ve iOS için temel istemcileri vardır. Ayrıca bir web uygulamasının yanı sıra Windows, Linux ve macOS için yazılım da mevcuttur. Ancak, bunları kullanmak için önce bir mobil cihaza kaydolmanız gerekir.



Threema uygulaması ücretsiz değildir. Tek seferlik satın alma modeliyle çalışır: uygulamayı ömür boyu kullanmak için 5,99 € (veya doğrudan satın alırsanız 4,99 €). Threema'yı gerçekten anonim olarak kullanmak için ödemenin de anonim olması gerekir. Bu nedenle Android sürümünü etkinleştirmek için "*Threema Shop*" üzerinden bitcoin veya nakit olarak bir etkinleştirme anahtarı satın alabilirsiniz. Öte yandan iOS'ta, Apple'ın uygulamadan para kazanma konusundaki kısıtlamaları nedeniyle satın alma işleminin App Store üzerinden yapılması gerekiyor.



Ayrıca "*Threema Work*" adında özel bir iş sürümü de var. Bu eğitimde, ev sürümüne odaklanacağız.



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



## Threema uygulamasını yükleyin



Threema tüm platformlarda mevcuttur. Uygulamayı doğrudan telefonunuzun uygulama mağazasından indirebilirsiniz:




- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



Android'de [APK ile yüklemek](https://shop.threema.ch/en/download) de mümkündür.



Ayrıca [bilgisayar sürümleri] (https://threema.ch/download) (MacOS, Linux ve Windows) de vardır. Bu eğitim size bunları nasıl senkronize edeceğinizi gösterecektir.



## Threema lisansı satın alın



Uygulamayı yükledikten sonra, doğrudan bir uygulama mağazası üzerinden gittiyseniz, lisans için zaten ödeme yapmışsınızdır ve uygulamaya hemen erişebilmeniz gerekir. Eğer F-Droid ya da APK'yı kullandıysanız, şimdi resmi web sitesinden bir lisans satın almanız gerekmektedir.



["*Threema Shop*" (https://shop.threema.ch/) adresine gidin ve "*Buy Threema for Android*" düğmesine tıklayın.



![Image](assets/fr/02.webp)



Satın almak istediğiniz lisans sayısını seçin (sadece sizin içinse sadece bir tane), para birimini seçin ve lisans teslim yöntemini seçin. Lisansı e-posta ile veya anonim kalmak istiyorsanız doğrudan site üzerinden almayı seçebilirsiniz. Ardından "*Ödemeye devam et*" seçeneğine tıklayın.



![Image](assets/fr/03.webp)



Ödeme yönteminizi seçin. Benim durumumda, bitcoin ile ödeme yapacağım, bunu yapmanızı da tavsiye ederim, çünkü anonim kalmanıza izin verir (Bitcoin'yi uygun şekilde kullanmanız koşuluyla) ve uzaktan nakit ödemeden çok daha kullanışlıdır. Ardından "*Sonraki*" seçeneğine tıklayın.



![Image](assets/fr/04.webp)



Invoice'e ihtiyacınız yoksa, herhangi bir kişisel bilgi girmeden tekrar "*Sonraki*" düğmesine tıklayın.



Ardından "*Ödemeyi onayla*" seçeneğine tıklayarak satın alma işleminizi onaylayın.



![Image](assets/fr/05.webp)



Daha sonra belirtilen tutarı sağlanan Bitcoin Address'e göndermeniz gerekecektir (ne yazık ki Lightning henüz desteklenmemektedir). İşlem Blockchain'te onaylandıktan sonra, Invoice'nin yanındaki "*Kapat*" düğmesine tıklayın.



Daha sonra lisans anahtarınıza erişebileceksiniz. Lütfen dikkat: eğer bir e-posta Address girmediyseniz, bu anahtar sadece burada görüntülenecektir. Gerekirse daha sonra erişebilmek için sayfanın URL'sini kaydetmeyi unutmayın.



![Image](assets/fr/06.webp)



## Threema'da bir hesap oluşturun



Artık lisans anahtarınız olduğuna göre, nihayet uygulamayı başlatabilirsiniz. İlk açılışta, Threema'yı bir uygulama mağazası aracılığıyla satın almadıysanız, siteden satın aldığınız lisans anahtarınızı girmeniz istenecektir.



![Image](assets/fr/07.webp)



Ardından "*Şimdi kur*" düğmesine tıklayın.



![Image](assets/fr/08.webp)



"*Threema ID*"nizi oluşturmak için gereken entropi kaynağını generate'a getirmek için parmağınızı ekranda gezdirin.



![Image](assets/fr/09.webp)



Daha sonra "*Threema ID*"niz görüntülenecektir. Bu, diğer kullanıcılarla iletişime geçmenizi sağlayacaktır. "*Sonraki*" üzerine tıklayın.



![Image](assets/fr/10.webp)



Bir şifre seçin. İhtiyaç halinde hesabınıza yeniden erişim sağlamanıza olanak tanıyacaktır. Parolanızı mümkün olduğunca uzun ve rastgele yapın ve güvenli bir kopyasını, örneğin bir parola yöneticisinde saklayın.



![Image](assets/fr/11.webp)



Ardından, gerçek adınız veya takma adınız olabilecek bir kullanıcı adı seçin.



![Image](assets/fr/12.webp)



Daha sonra Threema kimliğinizi telefon numaranıza bağlayabilirsiniz. Bu, kişileriniz arasında arama yapmanızı kolaylaştırır, ancak Threema kullanıyorsanız, anonimliğinizi de korumak içindir: bu yüzden bağlamamak en iyisidir. "*Sonraki*" üzerine tıklayın.



![Image](assets/fr/13.webp)



Bu adımı tamamladıktan sonra "*Bitir*" düğmesine tıklayın.



![Image](assets/fr/14.webp)



Artık Threema'ya bağlısınız ve iletişim kurmaya başlayabilirsiniz.



![Image](assets/fr/15.webp)



## Threema'yı kurun



Öncelikle, sağ üst köşedeki üç küçük noktaya tıklayarak ayarlara erişin, ardından "*Ayarlar*"ı seçin.



![Image](assets/fr/16.webp)



"*Gizlilik*" sekmesinde, ihtiyaçlarınıza göre ayarlayabileceğiniz çeşitli seçenekler bulacaksınız:




- Telefonunuzdaki kişileri senkronize etme ;
- Bilinmeyen kişilerden gelen mesajları kabul etmek;
- Veri girişi sırasında gösterge yazma ;
- Mesajların alındığına dair bildirim..



![Image](assets/fr/17.webp)



"*Güvenlik*" sekmesinde, uygulamaya erişimi korumak için "*Kilitleme mekanizması*" seçeneğini etkinleştirmenizi öneririm. Yerel yedeklemelerinizi güvence altına almak için passphrase'u etkinleştirmeniz de tavsiye edilir.



![Image](assets/fr/18.webp)



Uygulamayı tercihlerinize göre özelleştirmek için ayarların diğer bölümlerini keşfetmekten çekinmeyin.



![Image](assets/fr/19.webp)



## Threema hesabınızı yedekleme



Mesaj alışverişine başlamadan önce, özellikle telefonunuzun değiştirilmesi veya kaybolması durumunda hesabınızı kurtarmanın bir yolunu planlamanız önemlidir. Bunu yapmak için, Interface'in sağ üst köşesindeki üç noktaya tıklayın ve ardından "*Yedeklemeler*" menüsüne erişin.



![Image](assets/fr/20.webp)



Burada verilerinizi yedeklemek için iki seçenek bulacaksınız:




- "*Threema Safe*";
- "*Veri Yedekleme*".



"Threema Safe*, konuşmalarınız hariç tüm hesap bilgilerinizi Threema'nın sunucularında kaydeder. Bu veriler, hesabınızı oluştururken seçtiğiniz parola ile şifrelenir ve Threema'nın bunlara erişememesini sağlar. Yedeklemeler otomatik ve düzenli olarak yapılır.



"*Threema Safe*" ile hesabınızı yeni bir cihazda kurtarmak için tek yapmanız gereken "*Threema ID*" ve şifrenizi girmektir. Bu iki bilgiden herhangi biri eksikse, hesabınızı geri yüklemek imkansız olacaktır.



Bu seçenek yalnızca kimliğinizi, profilinizi, kişilerinizi, gruplarınızı ve belirli ayarlarınızı almanıza izin verir, ancak **konuşma geçmişinizi** almanıza izin vermez.



"*Threema Safe*"i etkinleştirmek için "*Yedeklemeler*" menüsündeki seçeneği işaretlemeniz yeterlidir.



![Image](assets/fr/21.webp)



Konuşma geçmişinizi de yedeklemek ve geri yüklemek istiyorsanız, "*Veri Yedekleme*" seçeneğini kullanmanız gerekir. Bu, hesabınızın telefonunuzda yerel olarak depolanan tam bir yedeğini oluşturur. Bu yedeği yeni cihazınıza aktarmanız ve tüm hesabınızı geri yüklemek için şifrenizi (ve muhtemelen passphrase'nizi) kullanmanız gerekir.



Bu yedekleme yalnızca yerel olduğundan, düzenli olarak harici ortama kopyalanması gerekir. Aksi takdirde, cihazınız kaybolursa, kurtarma imkansız olacaktır. Bu nedenle bu yöntem, acil durumlardan ziyade bir cihazdan diğerine planlı bir aktarım için en uygun yöntemdir.



Lütfen dikkat: "*Veri Yedekleme*" yalnızca aynı işletim sistemini kullanıyorsanız çalışır. Örneğin bir Samsung'dan iPhone'a geçiş yapmak için kullanamazsınız.



## Threema profilinizi özelleştirin



Interface'ün sol üst köşesinde profil resminize tıklayın ve ardından "*Profilim*"i seçin.



![Image](assets/fr/22.webp)



Burada profilinizi özelleştirebilirsiniz: bir fotoğraf ekleyebilir, kimlerin görebileceğini seçebilir veya Threema giriş bilgilerinizi görüntüleyebilirsiniz.



![Image](assets/fr/23.webp)



## PC yazılımını senkronize edin



Konuşmalarınıza bilgisayarınızdan erişmek istiyorsanız, Threema hesabınızı özel yazılımla senkronize edebilirsiniz. İşletim sisteminiz için yazılımı [resmi web sitesinden] indirin (https://threema.ch/en/download).



![Image](assets/fr/24.webp)



Telefonunuzda, sağ üstteki üç noktaya tıklayın, ardından "*Threema 2.0 for Desktop*" menüsünü açın.



![Image](assets/fr/25.webp)



"*Cihaz ekle*" üzerine tıklayın, ardından bilgisayarınızdaki yazılım tarafından görüntülenen QR kodunu taramak için telefonunuzu kullanın.



![Image](assets/fr/26.webp)



Senkronizasyonu onaylamak için yazılımda görüntülenen emoji grubuna tıklayın.



![Image](assets/fr/27.webp)



Bilgisayarınızda şifrenizi kullanarak oturum açın.



![Image](assets/fr/28.webp)



Mobil uygulamaya ek olarak, artık Threema hesabınıza doğrudan bilgisayarınızdan da erişebilirsiniz.



![Image](assets/fr/29.webp)



## Threema ile mesaj gönderme



Artık her şey doğru şekilde ayarlandığına göre, iletişim kurmaya başlayabilirsiniz. "*Sohbeti başlat*" düğmesine tıklayın.



![Image](assets/fr/30.webp)



"*Yeni kişi*" öğesini seçin.



![Image](assets/fr/31.webp)



Muhatabınızın "*Threema ID*"sini girin veya tarayın.



![Image](assets/fr/32.webp)



Mesaj simgesine tıklayın.



![Image](assets/fr/33.webp)



Muhatabınıza bir ilk mesaj gönderin.



![Image](assets/fr/34.webp)



Muhatabınız cevap verdiğinde bağlantı kurulacak ve onun adını ve profil fotoğrafını görebileceksiniz. Ardından Exchange mesajları, multimedya dosyaları gönderebilir ve hatta arama yapabilirsiniz.



![Image](assets/fr/35.webp)



Tebrikler, artık WathsApp'a harika bir alternatif olan Threema mesajlaşmasını kullanmaya başladınız! Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmak bırakırsanız çok minnettar olurum. Bu öğreticiyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!



Size Gmail'e çok daha gizlilik dostu bir alternatif olan Proton Mail'i tanıttığım bu diğer eğitimi de tavsiye ederim:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2