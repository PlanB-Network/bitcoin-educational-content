---
name: Ledger U2F & FIDO2
description: Ledger ile çevrimiçi güvenliğinizi artırın
---
![cover](assets/cover.webp)



Ledger cihazları, orijinal olarak bir Bitcoin Wallet'ü güvence altına almak için tasarlanmış donanım cüzdanlarıdır, ancak aynı zamanda web üzerinde güçlü kimlik doğrulama için gelişmiş seçeneklere sahiptirler. U2F** ve **FIDO2** protokolleriyle uyumlulukları sayesinde, ikinci bir kimlik doğrulama faktörü oluşturarak çevrimiçi hesaplarınıza erişimi güvence altına almanızı sağlarlar.



U2F (Evrensel 2. Faktör) protokolü 2014 yılında Google ve Yubico tarafından tanıtılmış, ardından FIDO Alliance tarafından standartlaştırılmıştır. Oturum açarken ikinci bir fiziksel kimlik doğrulama faktörünün (2FA) eklenmesini sağlar. Etkinleştirildikten sonra, klasik şifreye ek olarak, kullanıcılar Ledger'lerindeki bir düğmeye basarak hesaplarına bağlanmak için her girişimi onaylamalıdır. Bu bağlamda Ledger, Yubikey'e benzer bir şekilde çalışmaktadır. U2F aslında FIDO2 standardının bir alt bileşenidir ve modern tarayıcılar için yerel destek ve kimlik doğrulama anahtarı yönetiminde daha fazla esneklik dahil olmak üzere önemli iyileştirmeler getirirken onu kapsar.



Bu yöntemler asimetrik kriptografiye dayanmaktadır: hiçbir gizli veri iletilmez, bu da kimlik avı veya ele geçirme saldırılarını etkisiz hale getirir. U2F ve FIDO2 artık birçok çevrimiçi hizmet tarafından desteklenmektedir.



Bu eğitimde, Ledger'nızla iki faktörlü kimlik doğrulama için U2F ve FIDO2'yi nasıl etkinleştireceğinizi göstereceğiz.



**Not:** U2F ve FIDO2, Nano X ve Nano S classic için 2.1.0 sürümünden ve Nano S Plus için 1.1.0 sürümünden itibaren yeni ürün yazılımı ile donatılmış tüm Ledger cihazlarında desteklenmektedir. Stax ve Flex modelleri yerel olarak uyumludur.



## Ledger Güvenlik Anahtarı uygulamasını yükleyin



Bir Ledger cihazı kullanıyorsanız, muhtemelen aygıt yazılımının tek başına kripto cüzdanlarını yönetmek için gereken tüm özellikleri içermediğini biliyorsunuzdur. Örneğin, bir Bitcoin Wallet kullanmak için "*Bitcoin*" uygulamasını yüklemeniz gerekir. Benzer şekilde, MFA anahtarlarını yönetmek için "*Security Key*" uygulamasını yüklemeniz gerekir.



Başlamadan önce, Bitcoin Wallet'inizi Ledger'ünüze kurduğunuzdan emin olun. 2FA için kullanılan anahtarlar bu Mnemonic'den türetildiği için Mnemonic'nizi doğru şekilde kaydetmeniz önemlidir. Ledger'ünüz kaybolur veya hasar görürse, Mnemonic ifadenizi başka bir Ledger cihazına girerek anahtarlarınıza erişimi kurtarabilirsiniz (şu an için "*parolasız*" moddaki FIDO2 tanımlayıcıları Ledger'larda henüz desteklenmemektedir, bu nedenle yerleşik tanımlayıcılar yoktur).



Ledger'nızı bilgisayarınıza bağlayın ve kilidini açın.



![Image](assets/fr/01.webp)



Uygulamayı yüklemek için [Ledger Live] yazılımını açın (https://www.Ledger.com/Ledger-live), ardından "*My Ledger*" sekmesine gidin. "*Güvenlik Anahtarı*" uygulamasını bulun ve cihazınıza yükleyin.



![Image](assets/fr/02.webp)



"*Güvenlik Anahtarı*" uygulaması artık Ledger'inizde yüklü olan diğer uygulamalarla birlikte görünmelidir.



![Image](assets/fr/03.webp)



Öğreticideki sonraki adımlar için uygulamayı açık bırakmak üzere üzerine tıklayın.



![Image](assets/fr/04.webp)



## Ledger ile 2FA için U2F/FIDO2 kullanın



İki faktörlü kimlik doğrulama ile güvence altına almak istediğiniz hesaba erişin. Örneğin, ben bir Bitwarden hesabı kullanacağım. 2FA seçeneğini genellikle hizmet ayarlarında, "*authentication*", "*security*", "*login*" veya "*password*" sekmelerinin altında bulabilirsiniz.



![Image](assets/fr/05.webp)



İki faktörlü kimlik doğrulamaya ayrılmış bölümde "*Passkey*" seçeneğini seçin (bu terim kullandığınız siteye göre değişebilir).



![Image](assets/fr/06.webp)



Sık sık mevcut şifrenizi onaylamanız istenecektir.



![Image](assets/fr/07.webp)



Kolay tanınması için güvenlik anahtarınıza bir isim verin ve ardından "*Anahtarı Oku*" seçeneğine tıklayın.



![Image](assets/fr/08.webp)



Hesap bilgileriniz Ledger ekranında görünecektir. Onaylamak için "*Kayıt*" düğmesine (veya kullandığınız modele bağlı olarak her iki düğmeye aynı anda) basın.



![Image](assets/fr/09.webp)



Erişim anahtarı başarıyla kaydedildi.



![Image](assets/fr/10.webp)



Bu güvenlik anahtarını kaydedin.



![Image](assets/fr/11.webp)



Şu andan itibaren, hesabınıza giriş yaptığınızda, normal şifrenize ek olarak, Ledger'inizi bağlamanız istenecektir.



![Image](assets/fr/12.webp)



Ardından kimlik doğrulamasını onaylamak için Ledger ekranınızdaki "*Log in*" düğmesine (veya kullandığınız modele bağlı olarak her iki düğmeye aynı anda) basabilirsiniz.



![Image](assets/fr/13.webp)



İki faktörlü kimlik doğrulama için bir Hardware Wallet Ledger kullanmanın avantajı, Mnemonic ifadesi sayesinde anahtarlarınızı kolayca kurtarabilmenizdir. Bu temel yedeklemeye ek olarak, 2FA'yı etkinleştirdiğiniz her hizmet tarafından sağlanan bir acil durum kodunu da kullanabilirsiniz. Bu acil durum kodu, güvenlik anahtarınızı kaybetmeniz durumunda hesabınıza bağlanmanızı sağlar. Bu nedenle, gerektiğinde bağlantı için 2FA'nın yerini alır.



Örneğin Bitwarden'da bu koda "*Kurtarma kodunu görüntüle*" seçeneğine tıklayarak erişebilirsiniz.



![Image](assets/fr/14.webp)



Birlikte çalınmalarını önlemek için bu kodu ana parolanızı sakladığınız yerden farklı bir yerde saklamanızı öneririm. Örneğin, parolanız bir parola yöneticisinde kayıtlıysa, 2FA acil durum kodunuzu kağıt üzerinde ayrı bir yerde saklayın.



Bu yaklaşım, 2FA kimlik doğrulaması için Ledger'nizin kaybolması durumunda size iki düzeyde yedekleme sunar: tüm hesaplarınız için Mnemonic ifadesini kullanan bir ilk yedekleme ve acil durum kodlarını kullanan ikinci bir hesaba özel yedekleme. Ancak, **Mnemonic'nın rolünü acil durum kodunun rolü ile karıştırmamak önemlidir**:




- 12 veya 24 kelimelik Mnemonic ifadesi, yalnızca tüm hesaplarınızda 2FA için kullanılan anahtarlara değil, aynı zamanda Ledger ile güvence altına alınan bitcoinlerinize de erişmenizi sağlar;
- Acil durum kodu, 2FA talebini yalnızca ilgili hesapta (bu örnekte yalnızca Bitwarden'da) geçici olarak atlamanıza olanak tanır.



Tebrikler, artık Ledger'unuzu MFA için kullanmaya başladınız! Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız çok minnettar olurum. Lütfen bu öğreticiyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!



Ayrıca U2F ve FIDO2 kimlik doğrulaması için başka bir çözümü incelediğimiz bu diğer öğreticiyi de tavsiye ederim:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e