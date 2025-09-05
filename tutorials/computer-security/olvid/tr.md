---
name: Olvid
description: Herkes için özel mesajlaşma
---
![cover](assets/cover.webp)



Olvid, gizlilikten ödün vermeden yüksek düzeyde güvenlik sunmak için tasarlanmış, 2019 yılında piyasaya sürülen bir Fransız anlık mesajlaşma uygulamasıdır. WhatsApp veya Signal'in aksine, Olvid kayıt sırasında hiçbir kişisel veri istemiyor: telefon numarası yok, e-posta yok, hiçbir şey yok. Kullanıcılar arasındaki tanımlama, dizin sunucusu veya paylaşılan Address kitabı olmadan bir Exchange anahtarına dayanmaktadır.



Tüm mesajlar, meta verileri de korumak için tasarlanmış orijinal bir kriptografik protokol kullanılarak uçtan uca şifrelenir: kimse kiminle veya ne zaman konuştuğunuzu bilemez. İstemci kodu açık kaynak kodludur, ancak şifrelenmiş mesajları yönlendirmek için kullanılan merkezi sunucu AWS'de barındırılmaktadır.


Olvid'in güvenlik modeli temel bir ilkeye dayanır: dijital kimliklerin oluşturulmasında güvenilir üçüncü tarafların tamamen yokluğu. Kullanıcı kimliklerini yönetmek için merkezi bir dizine dayanan çoğu şifreli mesajlaşma aracının aksine Olvid, iletişimin bütünlüğünü sağlamak için herhangi bir merkezi altyapıya bağlı değildir. Bu mimari, dizinin tehlikeye atılmasıyla ilişkili riskleri ortadan kaldırır.


Bununla birlikte, Olvid kesinlikle lojistik bir rolle sınırlı olan merkezi bir mesaj dağıtım sunucusu kullanır: şifrelenmiş mesajların eşzamansız iletimini gerçekleştirir. Bu sunucu şifreleme sürecinde hiçbir rol oynamaz, ne kullanıcıların gerçek kimliklerini ne de mesajların içeriğini veya meta verilerini bilir (yönlendirme için gerekli olan alıcının açık anahtarı hariç). Bu nedenle, sistemin genel güvenliğini tehlikeye atmadan varsayılan olarak düşmanca kabul edilebilir. Ele geçirilse bile mesaj içeriklerine erişim izni vermeyecektir. Bu nedenle Olvid, mesaj iletimi için merkezileştirmeyi (verimlilik ve hizmet kalitesi için) varsayarken, bu altyapıdan bağımsız bir güvenliği garanti eder.



Olvid, ücretsiz bir sürüm ve aylık 4,99 € 'luk bir abonelik sürümü sunuyor. Ücretsiz sürüm, sesli ve görüntülü arama yapmak dışında (bunları almak mümkün olsa da) tam işlevsellik sunar ve birden fazla cihaz arasında hesap senkronizasyonuna izin vermez. Dolayısıyla, akıllı telefonunuzu yalnızca kullanmayı planlıyorsanız ve arama yapmanız gerekmiyorsa, Olvid mükemmel bir çözümdür.



Olvid, ANSSI (Fransız siber güvenlik otoritesi) tarafından onaylanmıştır. Bu uygulama, kullanım kolaylığını korurken gizlilik arayanlar için geleneksel mesajlaşma hizmetlerine (WhatsApp, Facebook Messenger, WeChat...) mükemmel bir alternatiftir.


| Application          | E2EE 1:1      | E2EE groups   | Anonymous registration | Open-source client license | Open-source server license | Decentralized server | Year of creation |
| -------------------- | ------------- | ------------- | ---------------------- | -------------------------- | -------------------------- | -------------------- | ---------------- |
| WhatsApp             | ✅             | ✅             | ❌                      | ❌                          | ❌                          | ❌                    | 2009             |
| WeChat               | ❌             | ❌             | ❌                      | ❌                          | ❌                          | ❌                    | 2011             |
| Facebook Messenger   | ✅             | 🟡 (optional) | ❌                      | ❌                          | ❌                          | ❌                    | 2011             |
| Telegram             | 🟡 (optional) | ❌             | 🟡                     | ✅                          | ❌                          | ❌                    | 2013             |
| LINE                 | ✅             | ✅             | ❌                      | ❌                          | ❌                          | ❌                    | 2011             |
| Signal               | ✅             | ✅             | ❌                      | ✅                          | ✅                          | ❌                    | 2014             |
| Threema              | ✅             | ✅             | ✅                      | ✅                          | ❌                          | ❌                    | 2012             |
| Element (Matrix)     | ✅             | ✅             | ✅                      | ✅                          | ✅                          | 🟡 (federated)       | 2016             |
| Delta Chat           | ✅             | ✅             | ✅                      | ✅                          | N/A                        | 🟡 (via email)       | 2017             |
| Conversations (XMPP) | ✅             | ✅             | ✅                      | ✅                          | ✅                          | 🟡 (federated)       | 2014             |
| Session              | ✅             | ✅             | ✅                      | ✅                          | ✅                          | ✅                    | 2020             |
| SimpleX              | ✅             | ✅             | ✅                      | ✅                          | ✅                          | ✅                    | 2021             |
| **Olvid**            | **✅**         | **✅**         | **✅**                  | **✅**                      | **❌**                      | 🟡(no directory)     | **2019**         |
| Keet                 | ✅             | ✅             | ✅                      | ❌                          | N/A                        | ✅                    | 2022             |
| Jami                 | ✅             | ✅             | ✅                      | ✅                          | N/A                        | ✅                    | 2005             |
| Briar                | ✅             | ✅             | ✅                      | ✅                          | N/A                        | ✅                    | 2018             |
| Tox                  | ✅             | ✅             | ✅                      | ✅                          | N/A                        | ✅                    | 2013             |

*E2EE = Uçtan uca şifreleme*



## Olvid uygulamasını yükleyin



Olvid tüm platformlarda kullanılabilir. Uygulamayı doğrudan telefonunuzun uygulama mağazasından indirebilirsiniz:




- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store](https://apps.apple.com/app/olvid/id1414865219);



Android'de [APK ile yüklemek](https://www.olvid.io/download/) de mümkündür.



Bu eğitimde mobil versiyona odaklanacağız, ancak [bilgisayar versiyonlarının da mevcut olduğunu] (https://www.olvid.io/download/) (MacOS, Linux ve Windows) lütfen unutmayın. Ücretli sürümü seçerseniz, hesabınızı birden fazla cihazda senkronize edebileceksiniz.



![Image](assets/fr/01.webp)



## Olvid'de bir hesap oluşturun



Uygulamayı ilk kez başlattığınızda, "*Ben yeni bir kullanıcıyım*" düğmesine tıklayın.



![Image](assets/fr/02.webp)



Bir takma ad seçin veya adınızı ve soyadınızı girin.



![Image](assets/fr/03.webp)



Bir profil fotoğrafı ekleyin.



![Image](assets/fr/04.webp)



Hesabınız şimdi oluşturuldu.



![Image](assets/fr/05.webp)



Olvid hesabınıza herhangi bir erişim kaybını önlemek için otomatik yedeklemeler ayarlamanızı öneririz. Bunu yapmak için, Interface'nin sağ üstündeki üç noktaya tıklayarak ayarları açın, ardından "*Ayarlar*" ı seçin.


⚠️ **Uyarı**: Olvid 3.7 sürümünden bu yana, profillerinizi ve kişilerinizi yedekleme prosedürü yeni bir prosedürle değiştirildi. Bu eğitim hala eski sürümü sunmaktadır. Yeni sürümü SSS bölümünden keşfedebilirsiniz: [💾 Profillerinizi yedekleme](https://www.olvid.io/faq/sauvegarder-vos-profils/)


![Image](assets/fr/06.webp)



"*Tuşları ve kişileri kaydet*" menüsüne gidin.



![Image](assets/fr/07.webp)



Ardından "*generate bir yedekleme anahtarı*" üzerine tıklayın. Bu anahtar yedeklerinizi şifreleyecektir. Hesabınızı başka bir cihazda kurtarmanız gerekiyorsa ve artık hesabınıza erişiminiz yoksa, şifresini çözmek için hem bir yedeğe hem de bu anahtara ihtiyacınız olacaktır.



![Image](assets/fr/08.webp)



Bu anahtarı güvenli bir yerde saklayın. Ayrıca bir kağıt kopyasını da alabilirsiniz.



![Image](assets/fr/09.webp)



Daha sonra yerel bir yedekleme veya bir bulut hizmetinde otomatik bir yedekleme oluşturmayı seçebilirsiniz. Bu ikinci seçenek, telefonunuzu kaybetseniz bile her koşulda Olvid hesabınıza erişimi garanti etmek için şiddetle tavsiye edilir.



![Image](assets/fr/10.webp)



"*Otomatik yedeklemeyi etkinleştir*" seçeneğinin işaretli olduğundan emin olun.



![Image](assets/fr/11.webp)



Uygulamayı ihtiyaçlarınıza göre özelleştirmek için mevcut diğer ayarları da keşfedebilirsiniz.



![Image](assets/fr/12.webp)



## Olvid ile mesaj gönderme



Mesaj gönderebilmek için önce kişi eklemeniz gerekir. Ana sayfadan mavi "*+*" düğmesine tıklayın.



![Image](assets/fr/13.webp)



Olvid daha sonra kullanıcı kimliğinizi görüntüler. Daha sonra bunu iletişim kurmak istediğiniz kişilere iletebilirsiniz, böylece sizi bir kişi olarak ekleyebilirler.



Bir kişiyi eklemek için kimliğini kameranızla tarayın veya sağ üst köşedeki üç küçük noktaya tıklayarak manuel olarak yapıştırın.



![Image](assets/fr/14.webp)



Kimlik tarandıktan sonra, kişinizin görüntülenen QR kodunu taramasını sağlayabilir veya "*Uzak kişi*" seçeneğine tıklayarak ona bir uzaktan bağlantı isteği gönderebilirsiniz.



![Image](assets/fr/15.webp)



Bağlantı şimdi kurulmuştur.



![Image](assets/fr/16.webp)



Artık muhabirinizle mesaj ve diğer içerik alışverişine başlayabilirsiniz!



![Image](assets/fr/17.webp)



Ana sayfadan tüm konuşmalarınızı bulabilirsiniz.



![Image](assets/fr/18.webp)



İkinci sekme tüm kişilerinizi içerir.



![Image](assets/fr/19.webp)



Ayrıca grup tartışmaları da oluşturabilirsiniz.



![Image](assets/fr/20.webp)



Tebrikler, artık WathsApp'a harika bir alternatif olan Olvid mesajlaşmayı kullanmaya başladınız! Bu öğreticiyi yararlı bulduysanız, aşağıya bir Green başparmak bırakırsanız çok minnettar olurum. Lütfen bu öğreticiyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!



Size Gmail'e çok daha gizlilik dostu bir alternatif olan Proton Mail'i tanıttığım bu diğer eğitimi de tavsiye ederim:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2