---
name: Blockstream Green - 2FA
description: Green Wallet üzerinde 2/2 Multisig kurulumu
---
![cover](assets/cover.webp)


___


***Not:** Mayıs 2025 itibariyle, iki faktörlü kimlik doğrulama (2FA) ile korunan yeni hesapları etkinleştirmek artık mümkün olmayacaktır. Bu özellik yalnızca daha önce bu tür bir hesabı etkinleştirmiş olan kullanıcılar tarafından kullanılabilir.*


___


Software Wallet, bir bilgisayara, akıllı telefona veya internete bağlı başka bir cihaza yüklenen ve Bitcoin Wallet anahtarlarınızı yönetmenizi ve güvence altına almanızı sağlayan bir uygulamadır. Özel anahtarları izole eden donanım cüzdanlarının aksine, "Hot" cüzdanları bu nedenle potansiyel olarak siber saldırılara maruz kalan bir ortamda çalışır ve korsanlık ve hırsızlık riskini artırır.


Yazılım cüzdanları, özellikle günlük işlemler için makul miktarlarda bitcoin yönetmek için kullanılmalıdır. Bitcoin'a yatırım yapmanın orantısız görünebileceği sınırlı Hardware Wallet varlığına sahip kişiler için de ilginç bir seçenek olabilirler. Ancak, sürekli internete maruz kalmaları, uzun vadeli tasarruflarınızı veya büyük fonlarınızı saklamak için daha az güvenli olmalarına neden olur. İkincisi için, donanım cüzdanları gibi daha güvenli çözümleri tercih etmek en iyisidir.


Bu eğitimde, Blockstream Green'daki "*2FA*" seçeneğini kullanarak bir Hot Wallet'in güvenliğini nasıl artıracağınızı göstereceğim.


![GREEN 2FA MULTISIG](assets/fr/01.webp)


## Blockstream Green ile tanışın


Blockstream Green, mobil ve masaüstünde kullanılabilen bir Software Wallet'tir. Eskiden *Green Address* olarak bilinen bu Wallet, 2016 yılında satın alınmasının ardından bir Blockstream projesi haline geldi.


Green özellikle kullanımı kolay bir uygulamadır, bu da onu yeni başlayanlar için ilginç kılar. RBF (*Replace-by-fee*), Tor bağlantı seçeneği, kendi düğümünüzü bağlama yeteneği, SPV (*Basit Ödeme Doğrulaması*), Coin etiketleme ve kontrol dahil olmak üzere iyi bir Bitcoin Wallet'in tüm temel özelliklerini sunar.


Blockstream Green ayrıca Liquid Network, Blockstream tarafından hızlı için geliştirilen bir Bitcoin Sidechain, ana Confidential Transactions dışında Blockchain'i de destekler. Bu öğreticide, yalnızca Bitcoin'a odaklanıyoruz, ancak Liquid'in Green'de nasıl kullanılacağını öğrenmek için başka bir öğretici de hazırladım:


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## 2/2 Multisig seçeneği (2FA)


Green'da klasik bir "*singlesig*" oluşturabilirsiniz Hot Wallet. Ancak, günlük yönetimini aşırı karmaşıklaştırmadan Hot Wallet'inizin güvenliğini artıran "*2FA Multisig*" seçeneğine de sahipsiniz.


Böylece 2/2 Multisig Wallet kuracaksınız, bu da her işlemin iki anahtarın imzasını gerektireceği anlamına gelir. İlk anahtar, 12 veya 24 kelimelik Mnemonic ifadenizden türetilir ve telefonunuzdaki bir PIN kodu ile yerel olarak güvence altına alınır. Bu anahtar üzerinde tam kontrole sahipsiniz. İkinci anahtar Blockstream'in sunucuları tarafından tutulur ve imzalamak için kullanımı, e-posta, SMS, telefon görüşmesi veya bu eğitimde göreceğimiz gibi bir kimlik doğrulama uygulaması (Authy, Google Authenticator, vb.) aracılığıyla alınan bir kodla elde edilebilen kimlik doğrulaması gerektirir.


Blockstream'in başarısız olması durumunda (örneğin, şirketin iflası veya ikinci anahtarı tutan sunucuların yok edilmesi durumunda) özerkliğinizi sağlamak için Multisig'inize bir zaman kilidi mekanizması uygulanır. Bu mekanizma, 2/2 Multisig'i yaklaşık bir yıl sonra 1/2 Multisig'e dönüştürür (veya tam olarak 51.840 blok, ancak bu değer değiştirilebilir), bundan sonra Wallet'niz bitcoin harcamak için yalnızca yerel anahtarınıza ihtiyaç duyacaktır. Dolayısıyla, Blockstream sunucularına veya 2FA kimlik doğrulamasına erişiminizi kaybederseniz, Blockstream'e bağlı kalmadan uygulamanızla bitcoinlerinizi özgürce kullanabilmek için en fazla bir yıl beklemeniz yeterlidir.


![GREEN 2FA MULTISIG](assets/fr/02.webp)


Bu yöntem Hot Wallet'ünüzün güvenliğini önemli ölçüde artırırken, bitcoinlerinizin kontrolünü size bırakır ve günlük kullanımını kolaylaştırır. Bununla birlikte, 2FA'nın güvenliğini korumak için düzenli zaman kilidi yenilemeleri gerektirir. Fonlarınızın 2FA tarafından korunduğu 360 günlük geri sayım, bitcoinleri aldığınız anda başlar. Bu makbuzdan 360 gün sonra, bu fonları harcayan bir işlem gerçekleştirmediyseniz, bitcoinleriniz 2FA olmadan yalnızca yerel anahtarınız tarafından korunacaktır.


Bu kısıtlama, 2FA seçeneğini, düzenli işlemlerin zaman kilitlerini otomatik olarak yenilediği bir harcama Wallet için daha uygun hale getirir. Uzun vadeli bir tasarruf Wallet için bu sorunlu olabilir, çünkü zaman kilidi sona ermeden önce her yıl kendinize bir süpürme işlemi yapmayı düşünmeniz gerekecektir.


Bu güvenlik yönteminin bir diğer dezavantajı da azınlık komut dosyası şablonları kullanmak zorunda olmanızdır. Bu, gizlilik açısından işlerin daha karmaşık hale geldiği anlamına gelir: çok az kişi sizinle aynı türde komut dosyası kullanır, bu da dışarıdan bir gözlemcinin Wallet parmak izinizi tespit etmesini kolaylaştırır. Dahası, bu komut dosyaları daha büyük boyutları nedeniyle daha yüksek işlem maliyetlerine maruz kalacaktır.


2FA seçeneğini kullanmamayı tercih ediyorsanız ve sadece bir "*singlesig*" kurmak istiyorsanız Wallet üzerinde Green, sizi bu diğer eğitime başvurmaya davet ediyorum:


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Blockstream Green yazılımının yüklenmesi ve yapılandırılması


İlk adım elbette Green uygulamasını indirmektir. Uygulama mağazanıza gidin:



- [Android için](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN 2FA MULTISIG](assets/fr/03.webp)


Android kullanıcıları için, uygulamayı [Blockstream'in GitHub'ında bulunan] `.apk' dosyası aracılığıyla da yükleyebilirsiniz (https://github.com/Blockstream/green_android/releases).


![GREEN 2FA MULTISIG](assets/fr/04.webp)


Uygulamayı başlatın, ardından "Koşulları kabul ediyorum...*" kutusunu işaretleyin.


![GREEN 2FA MULTISIG](assets/fr/05.webp)


Green'yı ilk kez açtığınızda, ana ekran yapılandırılmış bir Wallet olmadan görünür. Daha sonra, cüzdanlar oluşturur veya içe aktarırsanız, bu Interface'te görüneceklerdir. Bir Wallet oluşturmaya devam etmeden önce, uygulama ayarlarını ihtiyaçlarınıza göre ayarlamanızı tavsiye ederim. "Uygulama ayarları" üzerine tıklayın.


![GREEN 2FA MULTISIG](assets/fr/06.webp)


Yalnızca Android'de kullanılabilen "*Gelişmiş Gizlilik*" seçeneği, ekran görüntülerini devre dışı bırakarak ve uygulama önizlemelerini gizleyerek gizliliği artırır. Ayrıca telefonunuz kilitlenir kilitlenmez uygulama erişimini otomatik olarak kilitleyerek verilerinizin açığa çıkmasını daha zor hale getirir.


![GREEN 2FA MULTISIG](assets/fr/07.webp)


Gizliliğini artırmak isteyenler için uygulama, tüm bağlantılarınızı şifreleyen ve faaliyetlerinizin izlenmesini zorlaştıran bir ağ olan Tor üzerinden trafiğinizi köklendirme seçeneği sunar. Bu seçenek uygulamanın çalışmasını biraz yavaşlatsa da, özellikle kendi tam düğümünüzü kullanmıyorsanız, gizliliğinizi korumak için şiddetle tavsiye edilir.


![GREEN 2FA MULTISIG](assets/fr/08.webp)


Kendi tam düğümüne sahip kullanıcılar için Green Wallet, bir Electrum sunucusu aracılığıyla bağlanma imkanı sunarak Bitcoin ağ bilgileri ve işlemlerin dağıtımı üzerinde tam kontrolü garanti eder.


![GREEN 2FA MULTISIG](assets/fr/09.webp)


Bir başka alternatif özellik de, belirli Blockchain verilerini doğrudan doğrulamanıza ve böylece Blockstream'in varsayılan düğümüne güvenme ihtiyacını azaltmanıza olanak tanıyan "*SPV Doğrulama*" seçeneğidir, ancak bu yöntem bir Full node'in tüm garantilerini sağlamaz.


![GREEN 2FA MULTISIG](assets/fr/10.webp)


Bu ayarları ihtiyaçlarınıza göre yaptıktan sonra "*Kaydet*" düğmesine tıklayın ve uygulamayı yeniden başlatın.


![GREEN 2FA MULTISIG](assets/fr/11.webp)


## Blockstream Green üzerinde bir Bitcoin Wallet oluşturun


Artık bir Bitcoin Wallet oluşturmaya hazırsınız. "*Get Started*" düğmesine tıklayın.


![GREEN 2FA MULTISIG](assets/fr/12.webp)


Yerel bir Software Wallet oluşturmak veya bir Hardware Wallet aracılığıyla bir Cold Wallet yönetmek arasında seçim yapabilirsiniz. Bu eğitim için, bir Hot Wallet oluşturmaya odaklanacağız, bu nedenle "*Bu Cihazda*" seçeneğini seçmeniz gerekecek.


![GREEN 2FA MULTISIG](assets/fr/13.webp)


Daha sonra mevcut bir Bitcoin Wallet'ü geri yüklemeyi veya yeni bir tane oluşturmayı seçebilirsiniz. Bu eğitimin amaçları doğrultusunda, yeni bir Wallet oluşturacağız. Ancak, mevcut bir Bitcoin Wallet'ü Mnemonic ifadesinden yeniden oluşturmanız gerekiyorsa, örneğin eski telefonunuzu kaybettikten sonra, ikinci seçeneği seçmeniz gerekecektir.


![GREEN 2FA MULTISIG](assets/fr/14.webp)


Daha sonra 12 veya 24 kelimelik bir Mnemonic cümlesi arasında seçim yapabilirsiniz. Bu ifade, telefonunuzda bir sorun olması durumunda herhangi bir uyumlu yazılımdan Wallet'nıza erişimi kurtarmanızı sağlayacaktır. Şu anda, 24 kelimelik bir ifade seçmek 12 kelimelik bir ifadeden daha fazla güvenlik sunmamaktadır. Bu nedenle 12 kelimelik bir Mnemonic cümlesi seçmenizi tavsiye ederim.


Green daha sonra size Mnemonic ifadenizi verecektir. Devam etmeden önce izlenmediğinizden emin olun. Ekranda görüntülemek için "*Kurtarma cümlesini göster*" üzerine tıklayın.


![GREEN 2FA MULTISIG](assets/fr/15.webp)


**Bu Mnemonic size tüm bitcoinlerinize tam ve sınırsız erişim sağlar**. Bu ifadeye sahip olan herkes, telefonunuza fiziksel erişimi olmasa bile paranızı çalabilir (Green'de 2/2 Wallet olması durumunda süresi dolmuş zaman kilidine veya 2FA'ya tabidir).


Telefonunuzun kaybolması, çalınması veya kırılması durumunda yerel anahtarlarınıza erişimi geri yüklemenizi sağlar. Bu nedenle **fiziksel bir ortamda (dijital değil)** dikkatlice yedeklemeniz ve güvenli bir yerde saklamanız çok önemlidir. Bunu bir kağıda yazabilir veya daha fazla güvenlik için, eğer büyük bir Wallet ise, yangın, sel veya çökme riskinden korumak için paslanmaz çelik bir destek üzerine kazımanızı tavsiye ederim (az miktarda bitcoini korumak için tasarlanmış bir Hot Wallet için, basit bir kağıt yedekleme muhtemelen yeterlidir).


*Açıkçası, bu öğreticide yaptığım gibi, bu kelimeleri asla internette paylaşmamalısınız. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir.*


![GREEN 2FA MULTISIG](assets/fr/16.webp)


Mnemonic cümlenizi fiziksel bir ortama doğru bir şekilde kaydettikten sonra "*Devam*" düğmesine tıklayın. Green Wallet daha sonra doğru kaydettiğinizden emin olmak için Mnemonic cümlenizdeki bazı kelimeleri onaylamanızı isteyecektir. Boşlukları eksik kelimelerle doldurun.


![GREEN 2FA MULTISIG](assets/fr/17.webp)


Green Wallet cihazınızın kilidini açmak için kullanılacak olan cihazınızın PIN kodunu seçin. Bu, yetkisiz fiziksel erişime karşı korumanızdır. Bu PIN kodu, Wallet'ınızın kriptografik anahtarlarının türetilmesinde yer almaz. Dolayısıyla, bu PIN koduna erişiminiz olmasa bile, 12 veya 24 kelimelik Mnemonic ifadenize sahip olmanız yerel anahtarlarınıza yeniden erişmenizi sağlayacaktır.


Mümkün olduğunca rastgele 6 haneli bir PIN kodu seçmenizi öneririz. Unutmamak için bu kodu kaydettiğinizden emin olun, aksi takdirde Wallet'ünüzü Mnemonic'den almak zorunda kalırsınız. Daha sonra, her kullandığınızda PIN girmek zorunda kalmamak için bir biyometrik engelleme seçeneği ekleyebilirsiniz. Genel olarak konuşursak, biyometrikler PIN'in kendisinden çok daha az güvenlidir. Bu nedenle, varsayılan olarak bu kilit açma seçeneğini ayarlamamanızı tavsiye ederim.


![GREEN 2FA MULTISIG](assets/fr/18.webp)


Onaylamak için PIN kodunuzu ikinci kez girin.


![GREEN 2FA MULTISIG](assets/fr/19.webp)


Wallet'ünüzün oluşturulmasını bekleyin, ardından "*Hesap oluştur*" düğmesine tıklayın.


![GREEN 2FA MULTISIG](assets/fr/20.webp)


Daha sonra standart tek imzalı bir Wallet veya iki faktörlü kimlik doğrulama (2FA) ile korunan bir Wallet arasında seçim yapabilirsiniz. Bu eğitimde ikinci seçeneği seçeceğiz.


![GREEN 2FA MULTISIG](assets/fr/21.webp)


Bitcoin Multisig Wallet'iniz şimdi Green uygulaması kullanılarak oluşturuldu!


![GREEN 2FA MULTISIG](assets/fr/22.webp)


## 2FA'nın ayarlanması


Hesabınıza tıklayın.


![GREEN 2FA MULTISIG](assets/fr/23.webp)


"*2FA ekleyerek hesabınızın güvenliğini artırın*" Green düğmesine tıklayın.


![GREEN 2FA MULTISIG](assets/fr/24.webp)


Daha sonra 2/2 Multisig'inizin ikinci anahtarına erişmek için kimlik doğrulama yöntemini seçebileceksiniz. Bu eğitim için bir kimlik doğrulama uygulaması kullanacağız. Bu tür bir uygulamaya aşina değilseniz, Authy hakkındaki eğitimimize başvurmanızı tavsiye ederim:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

"*Authenticator Application*" öğesini seçin.


![GREEN 2FA MULTISIG](assets/fr/25.webp)


Green daha sonra bir QR kodu ve bir kurtarma anahtarı görüntüleyecektir. Bu anahtar, Authy uygulamanızın kaybolması durumunda 2FA'nıza erişimi geri yüklemenizi sağlar. Bu anahtarın güvenli bir yedeğini almanız tavsiye edilir, ancak yukarıda açıklandığı gibi zaman kilidi sona erdikten sonra da bitcoinlerinize erişimi kurtarabilirsiniz.


Kimlik doğrulama uygulamanızda yeni bir kod ekleyin, ardından Green tarafından sağlanan QR kodunu tarayın.


![GREEN 2FA MULTISIG](assets/fr/26.webp)


*Açıkçası, benim bu eğitimde yaptığım gibi, bu anahtarı ve QR kodunu asla internette paylaşmamalısınız. Bu Wallet örneği yalnızca Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir.*


"*Devam*" düğmesine tıklayın.


![GREEN 2FA MULTISIG](assets/fr/27.webp)


Kimlik doğrulama uygulamanızda bulunan 6 basamaklı dinamik kodu girin.


![GREEN 2FA MULTISIG](assets/fr/28.webp)


2 faktörlü kimlik doğrulama artık etkin.


![GREEN 2FA MULTISIG](assets/fr/29.webp)


Bu menüye göz atarak zaman kilidi süresini de ayarlayabilirsiniz. Bu geri sayım, bitcoinler alınır alınmaz başlar ve zaman kilidi sona erdiğinde, paranız 2FA'ya gerek kalmadan yalnızca yerel anahtarınızla harcanabilir. Varsayılan süre 12 ay olarak ayarlanmıştır, ancak bir tasarruf Wallet için, zaman kilidi yenileme sıklığını en aza indirmek için 15 ay seçmek mantıklı olabilir. Tersine, bir harcama Wallet'sı için 6 aylık bir zaman kilidi tercih edilebilir, çünkü günlük işlemlerinizle sık sık yenilenecektir ve daha kısa bir zaman kilidi, 2FA ile ilgili bir sorun olması durumunda beklemeyi azaltır. Size en uygun zaman kilidi süresini belirlemek size kalmıştır.


![GREEN 2FA MULTISIG](assets/fr/30.webp)


Artık bu menüden çıkabilirsiniz. Multisig Wallet'iniz hazır!


![GREEN 2FA MULTISIG](assets/fr/31.webp)


## Wallet'unuzu Blockstream Green üzerinde kurma


Wallet'inizi kişiselleştirmek isterseniz, sağ üst köşedeki üç küçük noktaya tıklayın.


![GREEN 2FA MULTISIG](assets/fr/32.webp)


"*Rename*" seçeneği Wallet'nizin adını özelleştirmenizi sağlar, bu da özellikle aynı uygulama üzerinde birkaç cüzdan yönetiyorsanız kullanışlıdır.


![GREEN 2FA MULTISIG](assets/fr/33.webp)


"*Birim*" menüsü Wallet'ünüzün temel birimini değiştirmenizi sağlar. Örneğin, bitcoin yerine satoshi cinsinden görüntülemeyi seçebilirsiniz.


![GREEN 2FA MULTISIG](assets/fr/34.webp)


"*Ayarlar*" menüsü Bitcoin Wallet cihazınızın çeşitli seçeneklerine erişim sağlar.


![GREEN 2FA MULTISIG](assets/fr/35.webp)


Burada, örneğin, genişletilmiş genel anahtarınızı ve *Descriptor*'yı bulacaksınız; bu Wallet'den yalnızca izleme modunda bir Wallet kurmayı planlıyorsanız kullanışlıdır.


![GREEN 2FA MULTISIG](assets/fr/36.webp)


Ayrıca Wallet PIN kodunuzu değiştirebilir ve bir biyometrik bağlantıyı etkinleştirebilirsiniz.


![GREEN 2FA MULTISIG](assets/fr/37.webp)


## Blockstream Green Kullanımı


Artık Bitcoin Wallet'iniz ayarlandığına göre, ilk Sats'nizi almaya hazırsınız! "*Al*" düğmesine tıklamanız yeterlidir.


![GREEN 2FA MULTISIG](assets/fr/38.webp)


Green daha sonra Wallet'inizde ilk boş alıcı Address'ü görüntüleyecektir. Bitcoin göndermek için ilgili QR kodunu tarayabilir ya da Address'ü doğrudan kopyalayabilirsiniz. Bu tür bir Address, ödeme yapan tarafından gönderilecek miktarı belirtmez. Bununla birlikte, sağ üst köşedeki üç küçük noktaya ve ardından "*Talep miktarı*" seçeneğine tıklayıp istediğiniz miktarı girerek belirli bir miktar talep eden bir generate Address oluşturabilirsiniz.


![GREEN 2FA MULTISIG](assets/fr/39.webp)


İşlem ağ üzerinde yayınlandığında, Wallet'nizde görünecektir.


![GREEN 2FA MULTISIG](assets/fr/40.webp)


İşlemi kesin olarak değerlendirmek için yeterli sayıda onay alana kadar bekleyin.


![GREEN 2FA MULTISIG](assets/fr/41.webp)


Wallet'inizdeki bitcoinler ile artık bitcoin de gönderebilirsiniz. "*Gönder*" üzerine tıklayın.


![GREEN 2FA MULTISIG](assets/fr/42.webp)


Sonraki sayfada, alıcının Address numarasını girin. Manuel olarak girebilir veya bir QR kodu tarayabilirsiniz.


![GREEN 2FA MULTISIG](assets/fr/43.webp)


Ödeme tutarını seçin.


![GREEN 2FA MULTISIG](assets/fr/44.webp)


Ekranın alt kısmında, bu işlem için ücret oranını seçebilirsiniz. Uygulamanın önerilerini takip etme veya ücretlerinizi özelleştirme seçeneğiniz vardır. Bekleyen diğer işlemlere göre ücret ne kadar yüksekse, işleminiz o kadar hızlı işlenecektir. Ücret piyasası bilgileri için lütfen [Mempool.space] (https://Mempool.space/) adresindeki "*İşlem Ücretleri*" bölümünü ziyaret edin.


![GREEN 2FA MULTISIG](assets/fr/45.webp)


İşlem özeti ekranına erişmek için "*Sonraki*" üzerine tıklayın. Address, tutar ve masrafların doğru olup olmadığını kontrol edin.


![GREEN 2FA MULTISIG](assets/fr/46.webp)


Her şey yolunda giderse, işlemi imzalamak ve Bitcoin ağında yayınlamak için ekranın altındaki Green düğmesini sağa kaydırın.


![GREEN 2FA MULTISIG](assets/fr/47.webp)


Bu, Blockstream tarafından tutulan ikinci Multisig anahtarının kilidini açmak için kimlik doğrulama kodunuzu girmeniz gereken zamandır. Kimlik doğrulama uygulamanızda görüntülenen 6 basamaklı kodu girin.


![GREEN 2FA MULTISIG](assets/fr/48.webp)


İşleminiz şimdi Bitcoin Wallet kontrol panelinizde görünecek ve onaylanmayı bekleyecektir.


![GREEN 2FA MULTISIG](assets/fr/49.webp)


Artık Blockstream Green'nin 2FA seçeneğini kullanarak 2/2 Multisig Wallet'u nasıl kolayca kuracağınızı biliyorsunuz!


Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Ayrıca bir Liquid Wallet kurmak için Blockstream Green mobil uygulaması hakkındaki bu diğer kapsamlı eğitime de göz atmanızı tavsiye ederim:


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a