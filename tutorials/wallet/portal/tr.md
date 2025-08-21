---
name: Portal
description: TwentyTwo-Devices Hardware Wallet Portalını yapılandırma ve kullanma
---
![cover](assets/cover.webp)


Portal, bitcoin kullanıcıları için açık kaynaklı donanım cüzdanları oluşturma konusunda uzmanlaşmış bir şirket olan TwentyTwo Devices tarafından tasarlanmış bir Bitcoin Hardware Wallet'dir. Magical Bitcoin projesinin ([bundan böyle BDK olarak adlandırılacaktır](https://github.com/bitcoindevkit)) yaratıcısı ve Blockstream ve BHB Network için çalışmış olan Alekos Filini tarafından kurulan TwentyTwo Devices, kullanıcı özerkliği, basitlik ve güvenliğe odaklanmayı amaçlamaktadır.


Portal'ı piyasadaki diğer donanım cüzdanlarından ayıran şey, akıllı telefonlarla yerel entegrasyonudur. Kablo veya pil olmadan çalışır. Kendisine güç sağlamak ve uyumlu herhangi bir mobil Wallet ile iletişim kurmak için NFC teknolojisini kullanır. İlgi çekici tasarımı ergonomik kullanım için tasarlanmıştır. Yuvarlak kısım akıllı telefonun arkasına yerleştirilerek, özel düğme ile imzalamadan önce işlemlerinizin ayrıntılarını kontrol edebileceğiniz bir ekran ortaya çıkar.


![Image](assets/fr/01.webp)


Tamamen açık kaynaklı olan Portal, Rust'de yazılmış aygıt yazılımına dayanmakta ve anahtar ve işlem yönetimi için BDK (Bitcoin Dev Kit) kullanmaktadır. Resmi web sitesinde] 89 €'ya satılmaktadır (https://store.twenty-two.xyz/products/portal-hardware-Wallet).


Bu yazının yazıldığı sırada Portal, Nunchuk ve Bitcoin Keeper uygulamaları ile uyumludur. Bu eğitimde, Nunchuk ile yapılandıracağız.


## Kutudan Çıkarma


Portalınızı aldığınızda, kutunun ve kutuyu kapatan etiketin iyi durumda olup olmadığını kontrol edin. İçinde, Portalınızı mühürlü bir poşet içinde bulacaksınız.


Poşetin açılmadığını doğrulamak için Seal'un sağlam olduğundan emin olun. Torbanın üzerinde büyük harflerle gösterilen benzersiz numara, mavi Seal'un altında siyah renkte yazılı olana, kutu etiketinde yazılı olana ve ilk başlattığınızda ekranınızda görünecek olana karşılık gelmelidir.


![Image](assets/fr/02.webp)


## Nunchuk kurulumu


Portal üzerinde barındırılan Wallet'yi yönetmek için Nunchuk uygulamasını kullanacağız. Uygulamayı [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) veya doğrudan [dosya `.apk`](https://github.com/nunchuk-io/nunchuk-android/releases) üzerinden indirin.


![Image](assets/fr/03.webp)


Nunchuk'u ilk kez kullanıyorsanız, uygulama sizden bir hesap oluşturmanızı isteyecektir. Bu eğitimin amaçları doğrultusunda, bir hesap oluşturmanız gerekli değildir. Hesap oluşturmadan devam etmek için "*Misafir olarak devam et*" seçeneğini seçin.


![Image](assets/fr/04.webp)


## Portal yapılandırması


Nunchuk ana ekranında, ekranın üst kısmındaki "*NFC*" logosuna tıklayın.


![Image](assets/fr/05.webp)


Etkinleştirmek için Portal'ınızı akıllı telefonunuzun arkasına yerleştirin.


![Image](assets/fr/06.webp)


Nunchuk Portalınızı tanıyacaktır. Ardından "*Devam*" üzerine tıklayın.


![Image](assets/fr/07.webp)


Yeni bir Wallet oluşturmak için "*generate Portalda seed*" öğesini seçin ve ardından "*Devam*" öğesine tıklayın.


![Image](assets/fr/08.webp)


12 veya 24 kelimelik Mnemonic cümlesi arasında seçim yapabilirsiniz. Her iki seçeneğin sunduğu güvenlik benzerdir, bu nedenle kaydetmesi en kolay olanı, yani 12 kelimeyi tercih edebilirsiniz.


![Image](assets/fr/09.webp)


Daha sonra bir şifre seçmeniz istenecektir. Şifre Portalınızın kilidini açar. Bu nedenle yetkisiz fiziksel erişime karşı koruma sağlar. Bu parola Wallet'inizin kriptografik anahtarlarının türetilmesinde yer almaz. Dolayısıyla, bu şifreye erişiminiz olmasa bile, 12 veya 24 kelimelik Mnemonic ifadenize sahip olmanız bitcoinlerinize yeniden erişmenizi sağlayacaktır. Mümkün olduğunca rastgele ve yeterince uzun bir parola seçmeniz tavsiye edilir. Bu şifreyi Portalınızın saklandığı yerden ayrı bir yere (örneğin bir şifre yöneticisine) kaydettiğinizden emin olun.


![Image](assets/fr/10.webp)


Portalınızda 12 kelimelik Mnemonic ifadeniz görüntülenecektir. Bu Mnemonic size tüm bitcoinlerinize tam ve sınırsız erişim sağlar. Bu ifadeye sahip olan herhangi biri, Portalınıza fiziksel erişimi olmasa bile paranızı çalabilir.


12 kelimelik ifade, Portalınızın kaybolması, çalınması veya kırılması durumunda bitcoinlerinize erişimi geri kazandırır. Bu nedenle dikkatlice kaydetmeniz ve güvenli bir yerde saklamanız çok önemlidir.


Bunu bir kağıda yazabilirsiniz veya daha fazla güvenlik için, yangından, selden veya çökmeden korumak için paslanmaz çelik bir tabana kazımanızı öneririm.


Mnemonic ifadenizi kaydetmenin ve yönetmenin doğru yolu hakkında daha fazla bilgi için, özellikle de yeni başlayan biriyseniz, bu diğer öğreticiyi izlemenizi şiddetle tavsiye ederim:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

_**Tabii ki, benim bu eğitimde yaptığım gibi, bu kelimeleri asla internette paylaşmamalısınız. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir.**_


Bir sonraki kelimeye geçmek için Portalınızdaki düğmeye sıkıca basın. Etkileşimin düzgün bir şekilde algılanması için parmağınızın tamamını düğmenin üzerine koyduğunuzdan ve birkaç saniye boyunca baskıyı sürdürdüğünüzden emin olun.


![Image](assets/fr/11.webp)


Portalınız daha sonra Nunchuk'ta girdiğiniz şifreyi onaylayacaktır.


![Image](assets/fr/12.webp)


Artık Portalınızı yapılandırmayı ve Mnemonic ifadenizi oluşturmayı tamamladınız!


![Image](assets/fr/13.webp)


## Bitcoin Wallet yapılandırması


Nunchuk üzerinde, Portalınızı telefonunuzun arkasında tutmaya devam ederek "*Devam*" üzerine tıklayın.


![Image](assets/fr/14.webp)


Bu eğitimde, bir single-sig Wallet kuracağım, bu yüzden bu seçeneği seçiyorum.


![Image](assets/fr/15.webp)


Varsayılan hesabı, yani Wallet'deki ilk hesabı (0 numara) kullanın. Nunchuk daha sonra kilidi açmak için Portal şifrenizi onaylamanızı isteyecektir.


![Image](assets/fr/16.webp)


Portalda, xpub'ınızın Nunchuk'a aktarılmasını onaylayın. Bu, Portal olmadan bitcoin harcayamadan Wallet'i akıllı telefonunuzdan yönetmenizi sağlar. Onaylamak için düğmeye basın.


Bu eğitim Testnet üzerinde gerçekleştirildiğinden, sizin durumunuzda belirtilen türetme yolunun benimkinden farklı olacağını unutmayın.


![Image](assets/fr/17.webp)


Wallet'unuza bir ad verin, örneğin "*Portal*", ardından "*Devam*" düğmesine tıklayın.


![Image](assets/fr/18.webp)


Nunchuk daha sonra size Descriptor'inizi sunar. Bir yedekleme yapmak iyi bir fikirdir. Descriptor bitcoin harcamanıza izin vermese de, Wallet'ün kurtarılması durumunda Mnemonic ifadenizden anahtarlarınızın türetme yollarını izlemenize olanak tanır. Güvenli bir yerde saklayın, çünkü sızması bir güvenlik sorunu oluşturmasa da bir gizlilik sorunu teşkil eder.


"*Bitti*" üzerine tıklayın.


![Image](assets/fr/19.webp)


Şimdi generate Bitcoin Wallet'nız için açık anahtarları Wallet yapmanız gerekecektir. Bunu yapmak için "*Yeni Wallet* oluştur" düğmesine tıklayın.


![Image](assets/fr/20.webp)


"*Yeni Wallet oluştur*" üzerine tekrar tıklayın. Ardından "*Mevcut anahtarları kullanarak yeni bir Wallet oluştur*" seçeneğini seçin.


![Image](assets/fr/21.webp)


Wallet'iniz için bir isim seçin ve "*Devam*" düğmesine tıklayın.


![Image](assets/fr/22.webp)


Bu yeni anahtar seti için imzalama cihazı olarak Portalınızı seçin ve ardından "*Devam*" düğmesine tıklayın.


![Image](assets/fr/23.webp)


Her şey sizi tatmin ediyorsa, yaratımı onaylayın.


![Image](assets/fr/24.webp)


Daha sonra Wallet yapılandırma dosyanızı kaydedebilirsiniz. Bu dosya yalnızca açık anahtarlarınızı içerir, yani birisi bu dosyaya erişse bile bitcoinlerinizi çalamaz. Ancak, tüm işlemlerinizi takip edebileceklerdir. Bu nedenle bu dosya yalnızca gizliliğiniz için bir risk teşkil eder. Bazı durumlarda, Wallet'unuzu kurtarmak için vazgeçilmez olabilir.


![Image](assets/fr/25.webp)


Ve hepsi bu kadar!


![Image](assets/fr/26.webp)


## Portal ile nasıl bitcoin alabilirim?


Bitcoin almak için Wallet'ınızı seçin.


![Image](assets/fr/27.webp)


Oluşturulan Address'i kullanmadan önce Portal ekranında kontrol edin. Bunu yapmak için "*Receive*" seçeneğine tıklayın.


![Image](assets/fr/28.webp)


Üç noktaya tıklayın, ardından "*PORTAL üzerinden Address'yi doğrulayın*" seçeneğini seçin. Ardından şifrenizi girin.


![Image](assets/fr/29.webp)


Portalınızı telefonunuzun arkasına yerleştirin, ardından düğmeye basarak onaylayın.


![Image](assets/fr/30.webp)


Portalda görüntülenen Address'ün Nunchuk'unuzdakiyle eşleştiğinden emin olun, ardından düğmeye tekrar basarak onaylayın. Adresler aynıysa, bu Address'ü mükellefe verebilirsiniz.


![Image](assets/fr/31.webp)


Ödeyenin işlemi yayınlandıktan sonra, Wallet'ünüzde göründüğünü göreceksiniz.


![Image](assets/fr/32.webp)


"*Köşeleri görüntüle*" üzerine tıklayın.


![Image](assets/fr/33.webp)


Yeni UTXO'inizi seçin.


![Image](assets/fr/34.webp)


UTXO'nıza bir etiket eklemek için "*Etiketler*"in yanındaki "*+*" işaretine tıklayın. Bu iyi bir uygulamadır, çünkü madeni paralarınızın nereden geldiğini hatırlamanıza yardımcı olur ve gelecekte harcama yaparken gizliliğinizi optimize eder.


![Image](assets/fr/35.webp)


Mevcut bir etiketi seçin veya yeni bir etiket oluşturun, ardından "*Kaydet*" düğmesine tıklayın. Parçalarınızı daha yapılandırılmış bir şekilde düzenlemek için "*koleksiyonlar*" da oluşturabilirsiniz.


![Image](assets/fr/36.webp)


## Portal kullanarak nasıl bitcoin gönderebilirim?


Artık Wallet'nizde bitcoinler olduğuna göre, onları da gönderebilirsiniz. Bunu yapmak için, seçtiğiniz Wallet'ye tıklayın.


![Image](assets/fr/37.webp)


"*Gönder*" düğmesine tıklayın.


![Image](assets/fr/38.webp)


Gönderilecek tutarı seçin ve ardından "*Devam*" düğmesine tıklayın.


![Image](assets/fr/39.webp)


Amacını hatırlatmak için gelecekteki işleminize bir "*not*" ekleyin.


![Image](assets/fr/40.webp)


Ardından sağlanan alana alıcının Address numarasını girin. QR kodu olarak kodlanmış bir Address'i ekranın sağ üst köşesindeki simgeye tıklayarak da tarayabilirsiniz. Ardından "*İşlem Oluştur*" düğmesine tıklayın.


![Image](assets/fr/41.webp)


İşlem ayrıntılarınızı kontrol edin, ardından Portalınızın yanındaki "*İmzala*" düğmesine tıklayın ve şifrenizi girin.


![Image](assets/fr/42.webp)


Portalınızı telefonunuzun arkasına yerleştirin. Alıcının Address numarasının ve tutarın doğru olup olmadığını kontrol edin. Doğruysa, devam etmek için düğmeye basın.


![Image](assets/fr/43.webp)


İşlem ücretinin doğru olup olmadığını kontrol edin, ardından işleminizi imzalamak için düğmeye tekrar basın.


![Image](assets/fr/44.webp)


İşleminiz imzalanmıştır. Ayrıntılarını Nunchuk'ta son bir kez kontrol edebilir, ardından Bitcoin ağında yayınlamak için "*İşlemi yayınla*" düğmesine tıklayabilirsiniz.


![Image](assets/fr/45.webp)


İşleminiz şimdi onay bekliyor.


![Image](assets/fr/46.webp)


Tebrikler, artık Portal'ı kullanmayı öğrendiniz! Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Daha fazla bilgi edinmek için HD cüzdanların nasıl çalıştığına dair eksiksiz eğitim kursumuza göz atın:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f