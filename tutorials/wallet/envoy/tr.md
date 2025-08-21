---
name: Elçi
description: Envoy uygulaması ile bir Pasaportun kurulması ve kullanılması
---
![cover](assets/cover.webp)


Envoy, Foundation tarafından geliştirilen bir Bitcoin Wallet yönetim uygulamasıdır. Passport Hardware Wallet ile kullanılmak üzere özel olarak tasarlanmıştır.


Bu eğitimde Envoy uygulamasıyla birlikte sunulan Passport "*Batch 2*", "*Founder's Edition*"ın halefidir. Üstün tasarımı, yüksek çözünürlüklü renkli ekranı ve ergonomik fiziksel klavyesi ile öne çıkmaktadır. "*Air-Gap*" modunda çalışarak Wallet'ünüzün özel anahtarlarının tamamen izole kalmasını sağlar ve bir MicroSD kart veya QR kodları aracılığıyla iletişim mümkündür. Cihaz, 1200 mAh kapasiteli çıkarılabilir, şarj edilebilir bir Nokia BL-5C batarya ile donatılmıştır. BL-5C modeli mağazalarda yaygın olarak bulunduğundan, tescilli olmayan bu pil kolayca değiştirilebilir.


Bağlanabilirlik açısından Passport bir MicroSD portu, şarj için bir USB-C portu ve QR kodlarını taramak için bir arka kamera ile donatılmıştır.


Güvenlik açısından Passport bir secure element içerir ve cihazın kaynak kodu tamamen açık kaynaklıdır. İyi bir Bitcoin Hardware Wallet'ten beklenen tüm özellikleri sunmaktadır. Passport'un henüz miniscript'i desteklemediğini, ancak bu özelliğin 2025'in ikinci çeyreği için planlandığını unutmayın.


199 $ fiyatla satılan Passport, Coldcard Q, Jade Plus, Tezor Safe 5 ve Ledger'in en üst düzey modelleriyle rekabet eden üst düzey bir Hardware Wallet olarak konumlandırılmıştır.


![Image](assets/fr/01.webp)


Güvenli Wallet'inizi bir Passport üzerinde yönetmek için birkaç seçeneğiniz vardır. Bu Hardware Wallet, diğerlerinin yanı sıra Sparrow wallet, Spectre Desktop, Nunchuk, Keeper dahil olmak üzere piyasadaki Wallet yönetim yazılımlarının çoğuyla uyumludur.


Yeni başlayanlara ve orta düzey kullanıcılara yönelik olan bu eğitimde, Envoy uygulamasını Passport'unuzla nasıl kullanacağınızı keşfedeceğiz. Bu, Hardware Wallet'nizden en iyi şekilde yararlanmanın en kolay yoludur.


İleri düzey bir kullanıcıysanız ve daha karmaşık özellikleri keşfetmek istiyorsanız, Passport'u Sparrow wallet ile yapılandırdığımız bu diğer eğitime göz atmanızı tavsiye ederim:


https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

## Pasaportun Kutusundan Çıkarılması


Passport'unuzu teslim aldığınızda, paketin açılmadığını teyit etmek için kutunun ve karton üzerindeki Seal'ün sağlam olduğundan emin olun. Cihazın orijinalliği ve bütünlüğüne ilişkin bir yazılım doğrulaması da cihaz kurulduğunda gerçekleştirilecektir.


![Image](assets/fr/02.webp)


Kutu içeriği şunları içerir :




- Pasaport;
- Mnemonic cümlenizi yazmak için bir karton parçası;
- Şarj için bir USB-C kablosu ;
- MicroSD kart ;
- İki MicroSD - Lightning veya USB-C adaptörü ;
- Çıkartmalar.


Cihaz üzerinde, :




- Bir klavye (1) ;
- USB-C bağlantı noktası (2);
- Bir silme düğmesi (3);
- Bir geri dönüş düğmesi (4) ;
- Bir onay düğmesi (5);
- Yön pedi (6);
- Açma/kapama düğmesi (7);
- Bir durum göstergesi (8);
- MicroSD bağlantı noktası (9) ;
- AA1 modunu değiştirmek için bir düğme (10);
- Bir arka kamera.


![Image](assets/fr/03.webp)


## Envoy uygulamasını indirin


Envoy'u indirmek için uygulama mağazanıza gidin:




- Google Play Store]'da (https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- App Store]'da (https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- F-Cold](https://foundation.xyz/fdroid/) üzerinde.


![Image](assets/fr/50.webp)


APK dosyasını doğrudan [Foundation'ın GitHub deposundan] da indirebilirsiniz (https://github.com/Foundation-Devices/envoy/releases).


![Image](assets/fr/51.webp)


Uygulama açıldıktan sonra "*Pasaportu Yönet*" seçeneğini seçin.


![Image](assets/fr/52.webp)


Gizliliği güçlendirmek için Tor bağlantısını etkinleştirmek isteyip istemediğinizi seçin ve ardından "*Devam*" düğmesine basın.


![Image](assets/fr/53.webp)


Passport'unuz zaten yapılandırılmışsa "*Mevcut bir Passport'u bağla*" seçeneğini veya Hardware Wallet'nizi ilk kez başlatıyorsanız "*Yeni bir Passport kur*" seçeneğini seçin.


![Image](assets/fr/54.webp)


Kullanım koşullarını kabul edin.


![Image](assets/fr/55.webp)


Daha sonra sizden Pasaportun gerçekliğini doğrulamanız istenecektir. "*Sonraki*" üzerine tıklayın.


![Image](assets/fr/56.webp)


## Başlangıç Pasaportu


Çalıştırmak için ünitenin yan tarafındaki açma/kapama düğmesine basın.


![Image](assets/fr/04.webp)


Bir sonraki menüye erişmek için onay düğmesine basın.


![Image](assets/fr/05.webp)


Bu eğitimde, Pasaport korumalı Wallet'i yönetmek için Envoy'u kullanacağız. "*Envoy App*" öğesini seçin.


![Image](assets/fr/57.webp)


"*Elçiye Devam*" üzerine tıklayın.


![Image](assets/fr/58.webp)


Bir sonraki adım cihazınızı kontrol etmektir. Bu, Pasaportunuzun gerçekliğini teyit eder ve taşıma sırasında tahrif edilmediğinden emin olunmasını sağlar. Sizden bir QR kodu taramanız istenecektir.


![Image](assets/fr/08.webp)


Uygulamada görüntülenen dinamik QR kodlarını Pasaportunuzla tarayın. Tarama tamamlandığında "*Sonraki*" butonuna tıklayın.


![Image](assets/fr/59.webp)


Ardından, Pasaportunuzda görüntülenen QR kodunu taramak için telefonunuzu kullanın.


![Image](assets/fr/60.webp)


"*Pasaportunuz güvende*" mesajı görüntülenirse, bu Hardware Wallet'unuzun orijinal olduğunu onaylar. Artık bunu bir Bitcoin Wallet'i güvence altına almak için kullanabilirsiniz.


![Image](assets/fr/61.webp)


Pasaportunuzdaki test sonucunu onaylayın.


![Image](assets/fr/14.webp)


## PIN kodunun ayarlanması


Ardından PIN kodu adımı gelir. PIN kodu Pasaportunuzun kilidini açar. Bu nedenle yetkisiz fiziksel erişime karşı koruma sağlar. PIN kodu, Wallet'ünüzün kriptografik anahtarlarının türetilmesinde yer almaz. Dolayısıyla, PIN koduna erişiminiz olmasa bile, 12 veya 24 kelimelik Mnemonic cümlenize sahip olmanız bitcoinlerinize yeniden erişmenizi sağlayacaktır.


![Image](assets/fr/15.webp)


Mümkün olduğunca rastgele bir PIN kodu seçmenizi öneririz. Ayrıca, bu kodu Pasaportunuzun saklandığı yerden ayrı bir yere (örneğin bir şifre yöneticisine) kaydettiğinizden emin olun.


PIN kodunu 6 ile 12 hane arasında seçebilirsiniz. Mümkün olduğunca uzun yapmanızı tavsiye ederim.


PIN numaralarınızı girmek için tuş takımını kullanın. Bitirdiğinizde, onay düğmesine tıklayın.


![Image](assets/fr/16.webp)


PIN kodunuzu ikinci kez onaylayın.


![Image](assets/fr/17.webp)


PIN kodunuz kaydedildi.


![Image](assets/fr/18.webp)


## Passport ürün yazılımını güncelleme


Hardware Wallet cihazınız aygıt yazılımını güncellemenizi öneriyor. En son sürümlerin getirdiği iyileştirmelerden ve düzeltmelerden yararlanmak için hemen güncellemenizi tavsiye ederim. Devam etmek için sağdaki onay düğmesine tıklayın.


![Image](assets/fr/19.webp)


Passport'unuz bir MicroSD kart aracılığıyla yeni aygıt yazılımını almaya hazırdır.


![Image](assets/fr/20.webp)


### Envoy uygulaması olmadan


Bunu yapmak için Passport kutunuzda bulunan MicroSD kartı (veya başka bir kartı) kullanın ve bilgisayarınıza takın. En son aygıt yazılımı sürümünü [Vakıf dokümantasyon sitesi](https://docs.foundation.xyz/firmware-updates/passport/) veya [GitHub depoları](https://github.com/Foundation-Devices/passport2/releases) adresinden indirin.


![Image](assets/fr/21.webp)


Cihazınıza yüklemeden önce, indirilen ürün yazılımının gerçekliğini ve bütünlüğünü kontrol etmenizi şiddetle tavsiye ederiz. Bu konuda yardıma ihtiyacınız varsa, bu eğiticiye başvurun :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Envoy uygulaması ile


Diğer ve daha basit bir seçenek ise doğrudan Envoy uygulamasını kullanmaktır. "*Ürün Yazılımını İndir*" üzerine tıklayın.


![Image](assets/fr/62.webp)


MicroSD kartı telefonunuza bağlamak için Passport'unuzla birlikte verilen adaptörü kullanın.


![Image](assets/fr/63.webp)


Ürün yazılımını kaydetmek için dosya gezgininizde MicroSD kartı seçin.


![Image](assets/fr/64.webp)


Aygıt yazılımı artık kaydedilmiştir. MicroSD'yi akıllı telefonunuzdan çıkarın ve Passport'a takın.


![Image](assets/fr/65.webp)


Passport dosya gezgini açılacaktır. VN.N.N-passport.bin` dosyasını seçin.


![Image](assets/fr/22.webp)


"*Seç*" üzerine tıklayın.


![Image](assets/fr/23.webp)


Ardından ürün yazılımı yüklemesini onaylayın.


![Image](assets/fr/24.webp)


Lütfen güncellemenin tamamlanmasını bekleyin.


![Image](assets/fr/25.webp)


Güncelleme tamamlandığında, cihazın kilidini açmak ve yapılandırmaya devam etmek için PIN kodunuzu girin.


![Image](assets/fr/26.webp)


## Yeni bir Bitcoin Wallet oluşturun


Şimdi yeni bir Bitcoin Wallet oluşturma zamanı. Onay düğmesine tıklayın.


![Image](assets/fr/27.webp)


Yeni bir Wallet oluşturmak için "*Yeni seed Oluştur*" seçeneğine tıklayın.


![Image](assets/fr/28.webp)


12 veya 24 kelimelik Mnemonic cümlesi arasında seçim yapabilirsiniz. Her iki seçeneğin sunduğu güvenlik benzerdir, bu nedenle kaydetmesi en kolay olanı, yani 12 kelimeyi tercih edebilirsiniz.


![Image](assets/fr/29.webp)


"*Devam*" üzerine tıklayın.


![Image](assets/fr/30.webp)


Pasaportunuz şimdi generate "*Yedekleme Kodunuzu*" verecektir. Bu, MicroSD'de saklanan Wallet yedeğinizin şifresini çözmek için kullanılabilecek bir dizi sayıdır. Foundation cihazlarına özgü bu yedekleme sistemi, Mnemonic ifadenize ek bir yedekleme oluşturur, ancak diğer Bitcoin yazılımlarıyla uyumlu değildir.


Bu "*Yedekleme Kodunu*" kullanmaya karar verirseniz, Wallet'nizin şifrelenmiş yedeğini içeren MicroSD'nizden farklı bir yerde sakladığınızdan emin olun. Bununla birlikte, Mnemonic ifadenizin iyi bir yedeğinin yeterli olduğunu düşünüyorsanız bu sistemi kullanmamayı tercih edebilirsiniz.


![Image](assets/fr/31.webp)


Doğru kaydettiğinizi onaylamak için "*Yedekleme Kodunuzu*" girin.


![Image](assets/fr/32.webp)


Bir MicroSD takılmışsa, Wallet'inizin şifrelenmiş yedeği buraya kaydedilmiştir.


![Image](assets/fr/33.webp)


Pasaportunuzda 12 kelimelik Mnemonic ifadeniz görüntülenecektir. Bu Mnemonic size tüm bitcoinlerinize tam ve sınırsız erişim sağlar. Bu ifadeye sahip olan herhangi biri, Pasaportunuza fiziksel erişimi olmasa bile paranızı çalabilir.


12 kelimelik ifade, Pasaportunuzun kaybolması, çalınması veya kırılması durumunda bitcoinlerinize erişimi geri kazandırır. Bu nedenle dikkatli bir şekilde saklamanız ve güvenli bir yerde muhafaza etmeniz çok önemlidir.


Kutuyla birlikte verilen kartona yazabilir veya daha fazla güvenlik için, yangından, selden veya çökmeden korumak için paslanmaz çelik bir tabana kazımanızı öneririm.


Mnemonic ifadenizi görmek için onay düğmesine tıklayın.


![Image](assets/fr/34.webp)


Mnemonic ifadenizi kaydetmenin ve yönetmenin doğru yolu hakkında daha fazla bilgi için, özellikle yeni başlayan biriyseniz, bu diğer öğreticiyi izlemenizi şiddetle tavsiye ederim:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

tabii ki, benim bu eğitimde yaptığım gibi, bu kelimeleri asla internette paylaşmamalısınız. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir.**_


Bu cümlenin fiziksel bir yedeğini alın.


![Image](assets/fr/35.webp)


Pasaportunuz başarıyla yapılandırıldı. Devam etmek için onay düğmesine tıklayın.


![Image](assets/fr/36.webp)


## Envoy'da Wallet'ün Kurulumu


Bu eğitimde size Passport'u Envoy uygulaması ile nasıl kullanacağınızı göstereceğim. Ancak, bu Hardware Wallet aynı zamanda Sparrow wallet, Keeper, BlueWallet, Nunchuk, Spectre ve diğerleri ile de uyumludur...


![Image](assets/fr/66.webp)


Pasaportunuzda görüntülenen QR kodunu taramak için Envoy uygulamasını kullanın.


![Image](assets/fr/67.webp)


Açık anahtarlarınız artık uygulamaya aktarılmıştır. "*Validate receive Address*" üzerine tıklayın.


![Image](assets/fr/68.webp)


Envoy'da görüntülenen Address'i taramak için Pasaportunuzu kullanın.


![Image](assets/fr/69.webp)


Pasaportunuz, Envoy'da ithal edilen Wallet'un geçerli olup olmadığını teyit edecektir. Uygulamada bunu onaylayın.


![Image](assets/fr/70.webp)


Artık Envoy'da Wallet'nizin herkese açık bilgilerine erişebilirsiniz, ancak bitcoin harcamak için Pasaportunuzu kullanmanız gerekecektir.


![Image](assets/fr/71.webp)


## Pasaport menülerini keşfedin


Passport Interface cihazınızın üç ana menüsü vardır:




- "*Hesap*";
- "*Daha*";
- "*Ayarlar*".


Bu menüler arasında gezinmek için yön tuşları üzerindeki sol ve sağ okları kullanın.


### *Hesap*" menüsü


"*Hesap*" menüsünde Bitcoin Wallet cihazınızın ana özelliklerini bulabilirsiniz. Bir işlemi kamera ya da MicroSD portu üzerinden imzalayabilirsiniz.


![Image](assets/fr/37.webp)


"*Hesap Araçları*" alt menüsü bir Address'ü doğrulama, bir mesajı imzalama veya Wallet'inizdeki adreslere bakma gibi seçenekler sunar.


![Image](assets/fr/38.webp)


"*Hesabı Yönet*" alt menüsünde, Bitcoin Wallet'nizi bir Wallet yönetim yazılımına bağlayabilir (bu öğreticinin sonraki adımlarında ele alacağız) veya hesabınızı görüntüleyebilir ve yeniden adlandırabilirsiniz.


![Image](assets/fr/39.webp)


### Daha Fazla" menüsü


"*Diğer*" menüsünde, Wallet'unuzda aynı Mnemonic ifadesine bağlı yeni bir hesap oluşturabilirsiniz.


![Image](assets/fr/40.webp)


Ayrıca bir BIP39 passphrase girebilir veya geçici bir seed kullanabilirsiniz.


![Image](assets/fr/41.webp)


### Ayarlar" menüsü


"*Ayarlar*" menüsünde tüm Wallet ve cihaz ayarlarınızı bulabilirsiniz.


![Image](assets/fr/42.webp)


"*Cihaz*" alt menüsü size ekran parlaklığını özelleştirme, otomatik kilitlemeden önceki gecikmeyi ayarlama, PIN kodunu değiştirme veya cihazı yeniden adlandırma seçenekleri sunar.


![Image](assets/fr/43.webp)


"*Yedekleme*" alt menüsü şifrelenmiş Wallet yedeğinizi dışa aktarmanızı, mevcut bir yedeğin geçerliliğini kontrol etmenizi veya "*Yedekleme Kodu*"nuzu tekrar aramanızı sağlar.


![Image](assets/fr/44.webp)


"*Firmware*" alt menüsü Passport'unuzun aygıt yazılımını güncellemek içindir. En son düzeltmelerden ve özelliklerden yararlanmak için bu güncellemeleri düzenli olarak yapmanızı öneririz.


![Image](assets/fr/45.webp)


"*Bitcoin*" alt menüsü görüntülenen birimi (BTC veya satoshis) değiştirmenizi, olası bir Multisig Wallet'yi yönetmenizi veya "*Testnet*" moduna geçmenizi sağlar.


![Image](assets/fr/46.webp)


"*Gelişmiş*" bölümünde, Mnemonic ifadenizin kelimelerini görüntüleyebilir, takılı MicroSD üzerinde işlemler gerçekleştirebilir, Passport'unuzu fabrika ayarlarına sıfırlayabilir veya daha önce gerçekleştirildiği gibi bir orijinallik kontrolü gerçekleştirebilirsiniz.


![Image](assets/fr/47.webp)


PIN kodunun ilk dört hanesini girdikten sonra cihazın kilidini açarken iki özel kelime görüntüleyerek bir Layer güvenlik ekleyen bir özellik olan "*Güvenlik Kelimeleri*" özelliğini etkinleştirebilirsiniz. Yapılandırma sırasında kaydedilecek olan bu kelimeler, Passport'un değiştirilmediğini veya kurcalanmadığını garanti eder. Daha sonraki bir tarihte herhangi bir tutarsızlık olması durumunda, cihazı kullanmamanızı tavsiye ederiz. Cihazın fiziksel olarak ele geçirilmesi risklerinin çoğunu önlemek için bu seçeneği etkinleştirmenizi tavsiye ederim.


![Image](assets/fr/48.webp)


Son olarak, "*Extensions*" alt menüsü, Whirlpool CoinJoin protokolü gibi cihazın belirli kullanımlarına özgü işlevleri etkinleştirmenizi sağlar.


![Image](assets/fr/49.webp)


## Bitcoin alma


Artık Pasaportunuz ayarlandığına göre, yeni Bitcoin Wallet'ünüzdeki ilk Sats'ünüzü almaya hazırsınız. Bunu yapmak için Envoy'da "*Primary 0*" hesabınıza tıklayın.


![Image](assets/fr/72.webp)


"*Receive*" düğmesine tıklayın.


![Image](assets/fr/73.webp)


Envoy uygulamanız Wallet'nizde mevcut ilk boş Address'i görüntüler. Kullanmadan önce, gerçekten Bitcoin Wallet'ye ait olduğundan emin olmak için Passport ekranındaki Address'i kontrol edelim. Passport'unuzun "*Hesap*" menüsünden "*Hesap Araçları*"nı seçin.


![Image](assets/fr/74.webp)


"*Verify Address*" üzerine tıklayın, ardından Envoy üzerinde görüntülenen QR kodunu tarayın.


![Image](assets/fr/75.webp)


Pasaportta görüntülenen Address'un Sparrow'de gösterilene tam olarak karşılık geldiğinden ve "*Verified*" ifadesinin göründüğünden emin olun.


![Image](assets/fr/76.webp)


Artık bitcoin almak için kullanabilirsiniz. İşlem ağda yayınlandığında, Envoy'da görünecektir. İşlemi kesin olarak değerlendirmek için yeterli onay alana kadar bekleyin.


![Image](assets/fr/77.webp)


## Bitcoin gönder


Artık Wallet'inizde birkaç Sats olduğuna göre, bazılarını da gönderebilirsiniz. Bunu yapmak için "*Gönder*" düğmesine tıklayın.


![Image](assets/fr/78.webp)


Alıcının Address numarasını ya doğrudan yapıştırarak ya da akıllı telefonunuzun kamerasıyla QR kodunu tarayarak girin.


![Image](assets/fr/79.webp)


Göndermek istediğiniz tutarı belirleyin ve ardından "*Onayla*" düğmesine tıklayın.


![Image](assets/fr/80.webp)


Mevcut piyasa durumuna göre işlem ücretini seçin, ardından işlem bilgilerini kontrol edin. Her şey doğruysa, "*Pasaport ile İmzala*" seçeneğine tıklayın.


![Image](assets/fr/81.webp)


Amacını net bir şekilde kaydetmek için işleminize bir etiket ekleyin.


![Image](assets/fr/82.webp)


Envoy daha sonra bir PSBT (*Partially Signed Bitcoin Transaction*) görüntüler. Uygulama işlemi oluşturmuştur, ancak girdide kullanılan bitcoinlerin kilidini açacak imza(lar) hala eksiktir. Bu imzalar yalnızca işlemi imzalamak için gereken özel anahtarlara erişim sağlayan seed'nızı barındıran Passport tarafından gerçekleştirilebilir.


![Image](assets/fr/83.webp)


Pasaportunuzda "*Hesap*" menüsüne erişin ve "*Karekod ile İmzala*" seçeneğine tıklayın.


![Image](assets/fr/84.webp)


Envoy'da görüntülenen PSBT'i (*Partially Signed Bitcoin Transaction*) tarayın.


![Image](assets/fr/85.webp)


Alıcı Address'un ve gönderilen miktarın doğru olduğunu onaylayın, ardından onay düğmesine basın.


![Image](assets/fr/86.webp)


Exchange Address'i kontrol edin. Benim örneğimde, işlem tek bir çıktı içerdiğinden hiçbiri yoktur.


![Image](assets/fr/87.webp)


Ücretin seçtiğiniz ücret olduğundan emin olun.


![Image](assets/fr/88.webp)


Tüm bilgiler doğruysa, işlemi imzalamak için onay düğmesine tıklayın.


![Image](assets/fr/89.webp)


Pasaportunuz size imzalı işleminizi bir QR kodu şeklinde gösterir.


![Image](assets/fr/90.webp)


Envoy uygulamasında QR kodu simgesine tıklayın, ardından Pasaport ekranınızda görüntülenen PSBT'yi tarayın.


![Image](assets/fr/91.webp)


İşlem detaylarınızı son bir kez kontrol edin. Her şey doğruysa, Bitcoin ağında yayınlamak için "*İşlem Gönder*" düğmesine basın.


![Image](assets/fr/92.webp)


İşleminiz şimdi onay bekliyor. Durumunu doğrudan hesabınızdan takip edebilirsiniz.


![Image](assets/fr/93.webp)


Tebrikler, artık Passport'u Envoy uygulaması ile nasıl kuracağınızı ve kullanacağınızı biliyorsunuz. Bu eğitimi faydalı bulduysanız, aşağıya bir Green başparmak bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Paylaştığınız için teşekkürler!


Daha fazla bilgi için Liana yazılımı hakkındaki eğitimimize bakın:


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04