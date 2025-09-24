---
name: Passport Core
description: Passport Hardware Wallet'ı manuel modda yapılandırma ve kullanma
---
![cover](assets/cover.webp)


Passport, Nisan 2020'de Boston'da kurulan bir Amerikan şirketi olan Foundation Devices tarafından tasarlanan, yalnızca Bitcoin'ye özel bir Hardware Wallet'dir.


Bu eğitimde sunulan Passport "*Batch 2*", "*Founder's Edition*"ın halefidir. Üstün tasarımı, yüksek çözünürlüklü renkli ekranı ve ergonomik fiziksel klavyesi ile öne çıkmaktadır. "*Air-Gap*" modunda çalışarak Wallet'ünüzün özel anahtarlarının tamamen izole kalmasını sağlar ve bir MicroSD kart veya QR kodları aracılığıyla iletişim mümkündür. Cihaz, 1200 mAh kapasiteli çıkarılabilir, şarj edilebilir bir Nokia BL-5C batarya ile donatılmıştır. BL-5C modeli mağazalarda yaygın olarak bulunduğundan, tescilli olmayan bu pil kolayca değiştirilebilir.


💡 **Güncelleme:** Mart 2025'ten bu yana, bu Hardware Wallet'ün adı artık "Passport" veya "Passport V2" değil, "Passport Core".


Bağlanabilirlik açısından Passport bir MicroSD portu, şarj için bir USB-C portu ve QR kodlarını taramak için bir arka kamera ile donatılmıştır.


Güvenlik açısından Passport bir secure element içermektedir ve cihazın kaynak kodu tamamen açık kaynaklıdır. İyi bir Bitcoin Hardware Wallet'ten beklenen tüm özellikleri sunmaktadır. Passport'un henüz miniscript'i desteklemediğini, ancak bu özelliğin 2025'in ikinci çeyreği için planlandığını unutmayın.


199 $ fiyatla satılan Passport, Coldcard Q, Jade Plus, Tezor Safe 5 ve Ledger'un en üst düzey modelleriyle rekabet eden üst düzey bir Hardware Wallet olarak konumlandırılmıştır.


![Image](assets/fr/01.webp)


Güvenli Wallet'nizi bir Passport üzerinde yönetmek için birkaç seçeneğiniz vardır. Bu Hardware Wallet, Sparrow wallet, Specter Desktop, Nunchuk, Keeper ve diğerleri dahil olmak üzere piyasadaki Wallet yönetim yazılımlarının çoğuyla uyumludur. Bu eğitimde, Sparrow wallet ile nasıl kullanılacağını öğreneceğiz.


Eğer yeni başlayan biriyseniz, en kolay seçenek Passport'unuzu Foundation tarafından geliştirilen yerel Envoy uygulaması ile kullanmaktır. Envoy'u Passport'unuzla nasıl kullanacağınızı öğrenmek için bu diğer eğitime göz atın:


https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

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


## Başlangıç Pasaportu


Çalıştırmak için ünitenin yan tarafındaki açma/kapama düğmesine basın.


![Image](assets/fr/04.webp)


Bir sonraki menüye erişmek için onay düğmesine basın.


![Image](assets/fr/05.webp)


Bu eğitimde, Pasaport güvenlikli Wallet'yı yönetmek için Sparrow wallet'i kullanacağız. "*Manuel Kurulum*" öğesini seçin.


![Image](assets/fr/06.webp)


Ardından kullanım koşullarını kabul edin.


![Image](assets/fr/07.webp)


Bir sonraki adım cihazınızı kontrol etmektir. Bu, Pasaportunuzun gerçekliğini teyit eder ve taşıma sırasında tahrif edilmediğinden emin olunmasını sağlar. Sizden bir QR kodu taramanız istenecektir.


![Image](assets/fr/08.webp)


Resmi doğrulama sitesine] (https://validate.foundationdevices.com/) gidin ve "*Pasaport*" seçeneğini seçin.


![Image](assets/fr/09.webp)


Sitede görüntülenen QR kodunu taramak için Passport'unuzun kamerasını kullanın.


![Image](assets/fr/10.webp)


Cihazınız daha sonra 4 kelime görüntüleyecektir.


![Image](assets/fr/11.webp)


Pasaportunuzun gerçekliğini onaylamak için web sitesine bu kelimeleri girin ve "*Validate*" seçeneğine tıklayın.


![Image](assets/fr/12.webp)


"*Geçti*" mesajı görünürse, Hardware Wallet'niz orijinaldir. Artık bunu bir Bitcoin Wallet'u güvence altına almak için kullanabilirsiniz.


![Image](assets/fr/13.webp)


Pasaportunuzdaki test sonucunu onaylayın.


![Image](assets/fr/14.webp)


## PIN kodunun ayarlanması


Ardından PIN kodu adımı gelir. PIN kodu Pasaportunuzun kilidini açar. Bu nedenle, yetkisiz fiziksel erişime karşı koruma sağlar. PIN kodu, Wallet'inizin kriptografik anahtarlarının türetilmesinde yer almaz. Dolayısıyla, PIN koduna erişiminiz olmasa bile, 12 veya 24 kelimelik Mnemonic cümlenize sahip olmanız bitcoinlerinize yeniden erişmenizi sağlayacaktır.


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


Hardware Wallet cihazınız aygıt yazılımını güncellemenizi öneriyor. En son sürümlerin getirdiği iyileştirmelerden ve düzeltmelerden yararlanmak için hemen güncelleme yapmanızı öneririm. Devam etmek için sağdaki onay düğmesine tıklayın.


![Image](assets/fr/19.webp)


Passport'unuz bir MicroSD kart aracılığıyla yeni aygıt yazılımını almaya hazırdır.


![Image](assets/fr/20.webp)


Bunu yapmak için Passport kutunuzda bulunan MicroSD kartı (veya başka bir kartı) kullanın ve bilgisayarınıza takın. En son aygıt yazılımı sürümünü [Vakıf dokümantasyon sitesi](https://docs.foundation.xyz/firmware-updates/passport/) veya [GitHub depoları](https://github.com/Foundation-Devices/passport2/releases) adresinden indirin.


![Image](assets/fr/21.webp)


Cihazınıza yüklemeden önce, indirilen ürün yazılımının gerçekliğini ve bütünlüğünü kontrol etmenizi şiddetle tavsiye ederiz. Bu konuda yardıma ihtiyacınız varsa, bu eğiticiye başvurun :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

.bin` dosyasını kontrol ettikten sonra MicroSD'nize yerleştirin ve ardından Passport'a takın. Passport dosya gezgini açılacaktır. VN.N.N-passport.bin` dosyasını seçin.


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


Pasaportunuz şimdi "*Yedekleme Kodunuzu*" generate'e girecektir. Bu, MicroSD'de saklanan Wallet yedeğinizin şifresini çözmek için kullanılabilecek bir dizi sayıdır. Foundation cihazlarına özgü bu yedekleme sistemi, Mnemonic ifadenize ek bir yedekleme oluşturur, ancak diğer Bitcoin yazılımlarıyla uyumlu değildir.


Bu "*Yedekleme Kodunu*" kullanmaya karar verirseniz, Wallet'inizin şifrelenmiş yedeğini içeren MicroSD'nizden farklı bir yerde sakladığınızdan emin olun. Bununla birlikte, Mnemonic ifadenizin iyi bir yedeğinin yeterli olduğunu düşünüyorsanız bu sistemi kullanmamayı tercih edebilirsiniz.


![Image](assets/fr/31.webp)


Doğru kaydettiğinizi onaylamak için "*Yedekleme Kodunuzu*" girin.


![Image](assets/fr/32.webp)


Bir MicroSD takılmışsa, Wallet'nızın şifrelenmiş yedeği buraya kaydedilmiştir.


![Image](assets/fr/33.webp)


Pasaportunuzda 12 kelimelik Mnemonic ifadeniz görüntülenecektir. Bu Mnemonic size tüm bitcoinlerinize tam ve sınırsız erişim sağlar. Bu ifadeye sahip olan herkes, Pasaportunuza fiziksel erişimi olmasa bile fonlarınızı çalabilir.


12 kelimelik ifade, Pasaportunuzun kaybolması, çalınması veya kırılması durumunda bitcoinlerinize erişimi geri kazandırır. Bu nedenle dikkatli bir şekilde saklamanız ve güvenli bir yerde muhafaza etmeniz çok önemlidir.


Kutuyla birlikte verilen kartona yazabilir veya daha fazla güvenlik için, yangından, selden veya çökmeden korumak için paslanmaz çelik bir tabana kazımanızı öneririm.


Mnemonic ifadenizi görmek için onay düğmesine tıklayın.


![Image](assets/fr/34.webp)


Mnemonic ifadenizi kaydetmenin ve yönetmenin doğru yolu hakkında daha fazla bilgi için, özellikle de yeni başlayan biriyseniz, bu diğer öğreticiyi izlemenizi şiddetle tavsiye ederim:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

tabii ki, benim bu eğitimde yaptığım gibi, bu kelimeleri asla internette paylaşmamalısınız. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir.


Bu cümlenin fiziksel bir yedeğini alın.


![Image](assets/fr/35.webp)


Pasaportunuz başarıyla yapılandırıldı. Devam etmek için onay düğmesine tıklayın.


![Image](assets/fr/36.webp)


## Menü keşfi


Passport Interface'nizin üç ana menüsü vardır:




- "*Hesap*";
- "*Daha*";
- "*Ayarlar*".


Bu menüler arasında gezinmek için yön tuşları üzerindeki sol ve sağ okları kullanın.


### *Hesap*" menüsü


"*Hesap*" menüsünde Bitcoin Wallet cihazınızın ana özelliklerini bulabilirsiniz. Bir işlemi kamera ya da MicroSD portu üzerinden imzalayabilirsiniz.


![Image](assets/fr/37.webp)


"*Hesap Araçları*" alt menüsü bir Address'i doğrulama, bir mesajı imzalama veya Wallet'nızdaki adreslere bakma gibi seçenekler sunar.


![Image](assets/fr/38.webp)


"*Hesabı Yönet*" alt menüsünde, Bitcoin Wallet'inizi bir Wallet yönetim yazılımına bağlayabilir (bu öğreticinin sonraki adımlarında ele alacağız) veya hesabınızı görüntüleyebilir ve yeniden adlandırabilirsiniz.


![Image](assets/fr/39.webp)


### Daha Fazla" menüsü


"*Diğer*" menüsünde, Wallet'nizde aynı Mnemonic ifadesine bağlı yeni bir hesap oluşturabilirsiniz.


![Image](assets/fr/40.webp)


Ayrıca bir BIP39 passphrase girebilir (sonraki bölüme bakın) veya geçici bir seed kullanabilirsiniz.


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


"*Bitcoin*" alt menüsü görüntülenen birimi (BTC veya satoshis) değiştirmenizi, olası bir Multisig Wallet'i yönetmenizi veya "*Testnet*" moduna geçmenizi sağlar.


![Image](assets/fr/46.webp)


"*Gelişmiş*" bölümünde, Mnemonic ifadenizin kelimelerini görüntüleyebilir, takılı MicroSD üzerinde işlemler gerçekleştirebilir, Passport'unuzu fabrika ayarlarına sıfırlayabilir veya daha önce gerçekleştirildiği gibi bir orijinallik kontrolü gerçekleştirebilirsiniz.


![Image](assets/fr/47.webp)


PIN kodunun ilk dört hanesini girdikten sonra cihazın kilidini açarken iki özel kelime görüntüleyerek bir Layer güvenlik ekleyen bir özellik olan "*Güvenlik Kelimeleri*" özelliğini etkinleştirebilirsiniz. Yapılandırma sırasında kaydedilecek olan bu kelimeler, Passport'un değiştirilmediğinden veya kurcalanmadığından emin olunmasını sağlar. Daha sonraki bir tarihte herhangi bir tutarsızlık olması durumunda, cihazı kullanmamanızı tavsiye ederiz. Cihazın fiziksel olarak ele geçirilmesi risklerinin çoğunu önlemek için bu seçeneği etkinleştirmenizi tavsiye ederim.


![Image](assets/fr/48.webp)


Son olarak, "*Extensions*" alt menüsü, Whirlpool CoinJoin protokolü gibi cihazın belirli kullanımlarına özgü işlevleri etkinleştirmenizi sağlar.


![Image](assets/fr/49.webp)


## Bir BIP39 passphrase ekleyin


Devam etmeden önce, dilerseniz bir BIP39 passphrase ekleyebilirsiniz. BIP39 passphrase, serbestçe seçebileceğiniz ve Wallet güvenliğini güçlendirmek için Mnemonic ifadenize eklenen isteğe bağlı bir paroladır. Bu özellik etkinleştirildiğinde, Bitcoin Wallet'nize erişim için hem Mnemonic hem de passphrase gerekir. İkisi de olmadan Wallet'yi kurtarmak imkansız olacaktır.


Bu seçeneği Passport'unuzda yapılandırmadan önce, passphrase'in teorik işleyişini tam olarak anlamak ve bitcoinlerinizin kaybına yol açabilecek hatalardan kaçınmak için bu makaleyi okumanız şiddetle tavsiye edilir:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Etkinleştirmek için "*Daha Fazla*" menüsüne gidin ve "*passphrase'a Gir*" seçeneğine tıklayın.


![Image](assets/fr/50.webp)


passphrase'inizi aA1 tuş takımını kullanarak girin ve fiziksel ortama (kağıt veya metal) bir veya daha fazla kez kaydettiğinizden emin olun. Örnek için çok zayıf bir passphrase kullanıyorum, ancak siz tüm karakter türlerini içeren ve yeterince uzun (güçlü bir parola gibi) güçlü, rastgele bir passphrase seçmelisiniz.


![Image](assets/fr/51.webp)


Lütfen BIP39 parolalarının büyük/küçük harfe ve yazım hatasına duyarlı olduğunu unutmayın. Başlangıçta yapılandırılmış olandan biraz farklı bir passphrase girerseniz, Passport bir hata bildirmeyecek, ancak ilk Wallet'nizde olmayan başka bir kriptografik anahtar seti türetecektir.


Bu nedenle, yapılandırma sırasında bir sonraki adımda size verilecek olan ana anahtar parmak izini bir yere not etmeniz önemlidir. Örneğin, benim passphrase `Plan B Ağım` ile ana anahtar parmak izim `745D526B`dir.


![Image](assets/fr/52.webp)


Pasaportunuzun kilidini her açtığınızda, passphrase'ünüzü girmek ve Wallet'inize uygulamak için bu menüye dönmeniz gerekecektir. Passport passphrase'ü kaydetmez.


passphrase'yı yazdıktan sonra kilidi her açtığınızda, bu onay ekranında verilen parmak izinin yapılandırma sırasında yazdığınızla aynı olup olmadığını kontrol edin. Eğer öyleyse, passphrase'nız doğrudur ve doğru Bitcoin Wallet'e erişiyorsunuz demektir. Değilse, yanlış Wallet'desinizdir ve herhangi bir giriş hatası yapmamaya dikkat ederek tekrar denemeniz gerekir.


Wallet'nizdeki ilk bitcoinlerinizi almadan önce, **Boş bir kurtarma testi** yapmanızı şiddetle tavsiye ederim. Xpub'ınız veya ilk aldığınız Address gibi bazı referans bilgilerini not edin, ardından Wallet'nizi hala boşken Passport'tan silin (`Ayarlar -> Gelişmiş -> Passport'u Sil`). Ardından Mnemonic ifadesinin ve herhangi bir passphrase'un kağıt yedeklerini kullanarak Wallet'nizi geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan çerez bilgilerinin başlangıçta yazdığınızla eşleşip eşleşmediğini kontrol edin. Eğer eşleşiyorsa, kağıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz. Test kurtarma işleminin nasıl gerçekleştirileceği hakkında daha fazla bilgi edinmek için lütfen bu diğer eğitime başvurun:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)


## Sparrow wallet üzerinde Wallet'ün Yapılandırılması


Bu eğitimde size Passport'un Sparrow wallet ile gelişmiş bir kullanımını göstereceğim. Ancak, bu Hardware Wallet aynı zamanda Envoy (Foundation uygulaması), Keeper, BlueWallet, Nunchuk, Spectre ve diğerleri ile de uyumludur...


Henüz yapmadıysanız, Sparrow wallet'yi [resmi web sitesinden] (https://sparrowwallet.com/) bilgisayarınıza indirip yükleyerek başlayın.


![Image](assets/fr/54.webp)


Kurulumdan önce yazılımın orijinalliğini ve bütünlüğünü kontrol ettiğinizden emin olun. Bunu nasıl yapacağınızı bilmiyorsanız, lütfen bu eğiticiye başvurun:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sparrow wallet açıldığında, "*Dosya*" sekmesine ve ardından "*Yeni Wallet*" seçeneğine tıklayın.


![Image](assets/fr/55.webp)


Wallet'ınıza bir isim verin ve ardından "*Wallet Oluştur*" seçeneğine tıklayın.


![Image](assets/fr/56.webp)


"*Havalandırılmış Hardware Wallet*" öğesini seçin.


![Image](assets/fr/57.webp)


"*Pasaport*" seçeneğinin yanındaki "*Tarama...*" seçeneğine tıklayın. Bu web kameranızı açacaktır.


![Image](assets/fr/58.webp)


Hardware Wallet'nizde "*Hesap*" menüsüne gidin, "*Hesabı Yönet*" alt menüsünü seçin ve "*Wallet'ü Bağla*" seçeneğine tıklayın.


![Image](assets/fr/59.webp)


Görüntülenen açılır listeden "*Sparrow*" öğesini seçin.


![Image](assets/fr/60.webp)


Ardından Multisig olmadan normal bir yapılandırma için "*Single-sig*" seçeneğini seçin.


![Image](assets/fr/61.webp)


"*QR Kodu*" seçeneğini seçin.


![Image](assets/fr/62.webp)


Pasaportunuz daha sonra generate dinamik QR kodlarını gösterecektir. Bunları Sparrow yazılımına taramak için bilgisayarınızın web kamerasını kullanın.


![Image](assets/fr/63.webp)


Şimdi xpub'ınızı ve ana anahtar parmak izinizi görmelisiniz; bu parmak izi, passphrase'inizi girdiğinizde Pasaportunuzda gösterilenle eşleşmelidir. "*Uygula*" düğmesine tıklayın.


![Image](assets/fr/64.webp)


Sparrow wallet'unuza erişimi güvence altına almak için güçlü bir parola belirleyin. Bu parola genel anahtarlarınızı, adreslerinizi, etiketlerinizi ve işlem geçmişinizi yetkisiz erişime karşı koruyacaktır. Bu parolayı bir parola yöneticisine kaydetmek iyi bir fikirdir, böylece unutmazsınız.


![Image](assets/fr/65.webp)


Daha sonra Pasaportunuz, ithalatın başarılı olduğunu onaylamak için ilk alım Address'ü taramanızı ister.


![Image](assets/fr/66.webp)


Sparrow'de "*Receive*" sekmesine gidin ve ilk Address'in QR kodunu tarayın.


![Image](assets/fr/67.webp)


İşlem başarılı olursa, Pasaportunuzda "*Verified*" ibaresi görüntülenecektir.


![Image](assets/fr/68.webp)


Bu, içe aktarmanın başarılı olduğunu onaylar.


![Image](assets/fr/69.webp)


## Bitcoin alma


Artık Pasaportunuz ayarlandığına göre, yeni Bitcoin Wallet'inizde ilk Sats'nızı almaya hazırsınız. Bunu yapmak için, Sparrow'te "*Al*" menüsüne tıklayın.


![Image](assets/fr/70.webp)


Sparrow, Wallet'unuzdaki ilk boş makbuz Address'yi görüntüleyecektir. Bir etiket ekleyebilirsiniz.


![Image](assets/fr/71.webp)


Kullanmadan önce, Address'un Bitcoin Wallet'e ait olduğundan emin olmak için Passport ekranında Address'u kontrol edeceğiz. Sparrow'de, gerekirse üzerine tıklayarak Address'un QR kodunu büyütebilirsiniz. Passport'unuzun "*Hesap*" menüsünden "*Hesap Araçları*"nı seçin.


![Image](assets/fr/72.webp)


"*Verify Address*" üzerine tıklayın, ardından Sparrow wallet üzerinde görüntülenen QR kodunu tarayın.


![Image](assets/fr/73.webp)


Pasaportta görüntülenen Address'nın Sparrow'de gösterilene tam olarak karşılık geldiğinden ve "*Verified*" ifadesinin göründüğünden emin olun.


![Image](assets/fr/74.webp)


Artık bitcoin almak için kullanabilirsiniz. İşlem ağda yayınlandığında, Sparrow'de görünecektir. İşlemi kesin olarak değerlendirmek için yeterli onay alana kadar bekleyin.


![Image](assets/fr/75.webp)


## Bitcoin gönder


Artık Wallet'unuzda birkaç Sats olduğuna göre, bazılarını da gönderebilirsiniz. Bunu yapmak için "*UTXOs*" menüsüne tıklayın.


![Image](assets/fr/76.webp)


Bu işlem için girdi olarak kullanmak istediğiniz UTXO'ları seçin ve ardından "*Seçilenleri Gönder*" seçeneğine tıklayın.


![Image](assets/fr/77.webp)


Alıcının Address numarasını, işlemin amacını size hatırlatacak bir etiket ve bu Address numarasına göndermek istediğiniz tutarı girin.


![Image](assets/fr/78.webp)


Ücret oranını mevcut piyasa koşullarına göre ayarlayın, ardından "*İşlem Oluştur*" seçeneğine tıklayın.


![Image](assets/fr/79.webp)


Tüm işlem parametrelerinin doğru olduğunu kontrol edin ve ardından "*İmzalama için İşlemi Sonlandır*" seçeneğine tıklayın.


![Image](assets/fr/80.webp)


PSBT'ü (*Partially Signed Bitcoin Transaction*) görüntülemek için "*Show QR*" üzerine tıklayın. Sparrow işlemi oluşturdu, ancak hala girişte kullanılan bitcoinlerin kilidini açacak imzalardan yoksundur. Bu imzalar yalnızca işlemi imzalamak için gereken özel anahtarlara erişim sağlayan seed'inizi barındıran Passport tarafından gerçekleştirilebilir.


![Image](assets/fr/81.webp)


Pasaportunuzda "*Hesap*" menüsüne erişin ve "*Karekod ile İmzala*" seçeneğine tıklayın.


![Image](assets/fr/82.webp)


Sparrow wallet üzerinde görüntülenen PSBT'i (*Partially Signed Bitcoin Transaction*) tarayın.


![Image](assets/fr/83.webp)


Alıcı Address'un ve gönderilen miktarın doğru olduğunu onaylayın, ardından onay düğmesine basın.


![Image](assets/fr/84.webp)


Exchange Address'i kontrol edin. Benim örneğimde, işlem tek bir çıktı içerdiğinden hiçbiri yoktur.


![Image](assets/fr/85.webp)


Ücretin seçtiğiniz ücret olduğundan emin olun.


![Image](assets/fr/86.webp)


Tüm bilgiler doğruysa, işlemi imzalamak için onay düğmesine tıklayın.


![Image](assets/fr/87.webp)


Sparrow wallet'de "*Scan QR*" seçeneğine tıklayın ve Pasaportunuzda görüntülenen QR kodunu tarayın.


![Image](assets/fr/88.webp)


İmzalı işleminiz artık Bitcoin ağında yayınlanmaya ve bir Miner tarafından bir bloğa dahil edilmeye hazırdır. Her şey doğruysa, "*İşlemi Yayınla*" düğmesine tıklayın.


![Image](assets/fr/89.webp)


İşleminiz yayınlandı ve onay bekliyor.


![Image](assets/fr/90.webp)


Tebrikler, artık Passport'u nasıl yapılandıracağınızı ve kullanacağınızı biliyorsunuz. Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Paylaştığınız için teşekkürler!


Daha fazla bilgi için Liana yazılımı hakkındaki eğitimimize bakın:


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04