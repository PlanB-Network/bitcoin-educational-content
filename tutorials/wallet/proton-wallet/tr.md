---
name: Proton Wallet
description: Proton Bitcoin Wallet'nin kurulumu ve kullanımı
---
![cover](assets/cover.webp)


Proton, 2014 yılında CERN bilim insanları tarafından kurulmuş, dijital gizlilik konusunda uzmanlaşmış bir İsviçre şirketidir. Açık kaynak çözümleriyle tanınan Proton, Proton Mail, Proton VPN ve Proton Drive dahil olmak üzere bir dizi hizmet sunmaktadır.


Proton kısa bir süre önce, Proton hesabınıza bağlı bir mobil uygulama veya web istemcisi olarak kullanılabilen açık kaynaklı, kendi kendini koruyan bir Bitcoin Wallet olan Proton Wallet'yı tanıttı. Wallet'nın işlevleri şu an için nispeten klasik, RBF (*Replace-by-fee*), etiketleme veya BIP39 passphrase ekleme yeteneği gibi iyi bir Bitcoin Wallet'dan beklenen temel araçlara sahip.


Bu Wallet'in özelliği, alıcının e-posta Address'unu kullanarak bitcoin gönderme yeteneğidir; bunun için Proton otomatik olarak kullanıcının Wallet'ine bağlı boş bir Bitcoin Address oluşturur. Proton gelecekte Lightning ve coinjoins dahil olmak üzere yeni özellikler eklemeyi planlıyor (muhtemelen GitHub depolarındaki etkinlik tarafından önerildiği gibi Whirlpool kullanarak).


## Bir Proton hesabı oluşturun


Proton Wallet'yi kullanmak için bir Proton hesabına ihtiyacınız var. Proton posta kutusu oluşturmaya adanmış bu eğitimin ilk adımlarını izleyerek ücretsiz olarak bir tane oluşturabilirsiniz (yalnızca "*Proton hesabı oluşturma*" bölümü). Hesabınız kurulduktan sonra, bu eğitimin geri kalanıyla devam edebilirsiniz.


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Proton Wallet'e bağlanın


Proton Wallet web sitesine] (https://proton.me/Wallet) gidin ve "*Get Proton Wallet*" düğmesine tıklayın.


![Image](assets/fr/01.webp)


"*Ücretsiz*" abonelik seçeneğini seçin, ardından "*Giriş Yap*" seçeneğine tıklayın.


![Image](assets/fr/02.webp)


Giriş yapmak için Proton hesabınızla ilişkili e-posta adresinizi ve şifrenizi girin.


![Image](assets/fr/03.webp)


Hesabınız şimdi görüntülenmelidir. "*Proton Wallet'i şimdi kullanmaya başlayın*" üzerine tıklayın.


![Image](assets/fr/04.webp)


## Bir Bitcoin Wallet oluşturun


Hesabınız için varsayılan fiat para birimini seçin, ardından "*Yeni Wallet oluştur*" seçeneğine tıklayın.


![Image](assets/fr/05.webp)


Bitcoin Wallet'niz artık oluşturulmuştur. Teorik olarak hemen kullanmaya başlayabilirsiniz, ancak önce Mnemonic'nizi kaydetmeniz çok önemlidir. Bunu yapmak için Interface'un sağ üst köşesindeki "*Wallet'nizi güvence altına alın*" seçeneğine tıklayın.


![Image](assets/fr/06.webp)


Proton'da henüz yapmadıysanız, hesabınız için bir yedekleme ayarlamanız ve bir 2FA yöntemi kullanarak güvenliğini sağlamanız istenecektir. Bu güvenlik önlemleri, tüm Proton hesabınız için geçerli olsa da, Bitcoin Wallet'ünüz buna entegre edildiğinde daha da önemlidir. Bunları uygulamanızı şiddetle tavsiye ederim.


![Image](assets/fr/07.webp)


Mnemonic cümlenizi kaydetmek için "*Bu Wallet'nın seed cümlesini yedekle*" seçeneğine tıklayın.


![Image](assets/fr/08.webp)


Proton şifrenizi girin.


![Image](assets/fr/09.webp)


Ardından Wallet'unuzun Mnemonic cümlesini görüntülemek için "*Wallet seed cümlesini görüntüle*" üzerine tıklayın.


![Image](assets/fr/10.webp)


Proton Wallet, 12 kelimelik Mnemonic ifadenizi görüntüler. **Bu Mnemonic size tüm bitcoinlerinize tam ve sınırsız erişim sağlar**. Bu ifadeye sahip olan herkes, Proton hesabınıza erişimi olmasa bile fonlarınızı çalabilir. Hesabınıza erişiminizi kaybederseniz, 12 kelimelik ifade bitcoinlerinize erişimi geri yüklemek için kullanılabilir. Bu nedenle dikkatlice kaydetmeniz ve güvenli bir yerde saklamanız çok önemlidir.


Bunu bir kağıda yazabilirsiniz ya da daha fazla güvenlik için, yangından, selden veya çökmeden korumak için paslanmaz çelik bir tabana kazımanızı tavsiye ederim.


![Image](assets/fr/11.webp)


Mnemonic ifadenizi kaydetmenin ve yönetmenin doğru yolu hakkında daha fazla bilgi için, özellikle de yeni başlayan biriyseniz, bu diğer öğreticiyi izlemenizi şiddetle tavsiye ederim:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

_**Tabii ki, bu eğitimde yaptığımın aksine, bu kelimelerin fotoğrafını asla çekmemelisiniz.**_


İfadenizi kaydettikten sonra "*Bitti*" düğmesine tıklayın.


![Image](assets/fr/12.webp)


## Interface'ü keşfedin


Proton Wallet'in Interface'i oldukça sezgiseldir. Sol tarafta, farklı cüzdanlarınızı ve bunlarla ilişkili hesapları bulacaksınız. "*Primary*" hesabı ana hesabınızdır. Gizlilik nedeniyle, Proton e-posta Address aracılığıyla alınan bitcoinler "*Bitcoin E-posta ile*" adlı ayrı bir hesaba yerleştirilir.


![Image](assets/fr/13.webp)


Yeni bir hesap eklemek için "*Hesap ekle*" seçeneğine tıklayın.


![Image](assets/fr/14.webp)


Yeni bir Wallet oluşturmak için "*Cüzdanlar*"ın yanındaki "*+*" sembolüne tıklayın.


![Image](assets/fr/15.webp)


Burası yeni bir Wallet'e bir BIP39 passphrase ekleyebileceğiniz yerdir.


![Image](assets/fr/16.webp)


passphrase hakkındaki bilgilerinizi derinleştirmek için bu eğitimi tavsiye ederim:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Bitcoin alma


Wallet'ünüze bitcoin almak için, Interface'ün sol tarafında istediğiniz hesabı seçin, ardından "*Al*" düğmesine tıklayın.


![Image](assets/fr/17.webp)


Proton Wallet daha sonra otomatik olarak yeni, boş bir Address oluşturur.


![Image](assets/fr/18.webp)


İşlem tamamlandığında, "*İşlemler*" bölümünde bulabilirsiniz. İşleme bir etiket atamak için "*+Ekle*" üzerine tıklayın.


![Image](assets/fr/19.webp)


## Bitcoin gönder


Artık Wallet'inizde bitcoinler olduğuna göre, onları gönderebilirsiniz. Interface'nin sol tarafında istediğiniz hesabı seçin ve ardından "*Gönder*" seçeneğine tıklayın.


![Image](assets/fr/20.webp)


Alıcının Bitcoin Address numarasını girin. Küçük logoya tıklayarak bir QR kodunu tarayabilirsiniz. Bir e-posta Address'a göndermek için, doğrudan bu alana girin. Bitcoin Address'u girdikten sonra, küçük oka ve ardından "*Onayla*" seçeneğine tıklayın.


![Image](assets/fr/21.webp)


Gönderilecek tutarı fiat para birimi veya bitcoin olarak girin, ardından "*İncele*" seçeneğine tıklayın.


![Image](assets/fr/22.webp)


İşlem ücretini mevcut piyasa durumuna göre seçin.


![Image](assets/fr/23.webp)


İşleminize bir etiket ekleyin, ardından tüm ayrıntıları iki kez kontrol edin. Her şey doğruysa, işlemi imzalamak ve göndermek için "*Onayla ve gönder*" seçeneğine tıklayın.


![Image](assets/fr/24.webp)


İşleminiz şimdi hesabınızın "*İşlemler*" bölümünde onay bekliyor olarak görünecektir.


![Image](assets/fr/25.webp)


## Uygulamaya giriş yapın


Web istemcisine ek olarak, Proton Wallet'e bir mobil uygulama aracılığıyla da erişilebilir. Wallet'i Proton hesabınıza bağlayarak, Wallet'inizi web istemcisi ve mobil uygulama arasında senkronize edebilirsiniz.


Proton Wallet'yi uygulama mağazanızdan indirin:




- [App Store'da](https://apps.apple.com/us/app/proton-Wallet-secure-btc/id6479609548);
- [Google Play Store'da](https://play.google.com/store/apps/details?id=me.proton.Wallet.android).


![Image](assets/fr/26.webp)


Kurulumdan sonra, "*Giriş yap*" seçeneğine tıklayın ve Address e-posta adresinizi ve Proton şifrenizi girin.


![Image](assets/fr/27.webp)


Daha sonra web istemcisindeki aynı özelliklerle Bitcoin Wallet'nize erişebileceksiniz.


![Image](assets/fr/28.webp)


Tebrikler, artık Proton Wallet'i nasıl kuracağınızı ve kullanacağınızı biliyorsunuz. Bu öğreticiyi yararlı bulduysanız, aşağıya bir Green başparmağı bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Paylaştığınız için teşekkürler!


Daha ileri gitmek için, Blockstream'in en yeni Hardware Wallet'ı Jade Plus hakkındaki bu öğreticiyi tavsiye ederim:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262