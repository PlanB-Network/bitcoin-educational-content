---
name: Trezor Safe 3
description: Hardware Wallet Safe 3'ü yapılandırma ve kullanma
---
![cover](assets/cover.webp)



*Resim kredisi: [Trezor.io](https://trezor.io/)*



Trezor Safe 3, SatoshiLabs tarafından tasarlanan ve 2023 yılında üretilen bir Hardware Wallet'dir. Hem yeni başlayanlar hem de orta düzey kullanıcılar için tasarlanmış çok kompakt ve hafif bir modeldir (14 gram). Ünlü Model One'ın önemli eklemelerle halefidir ve markanın onu ana rakibi Ledger'den ayıran açık kaynak yaklaşımını korur. Safe 3'ün fiyatı 79 €'dur. Bu nedenle orta sınıf Hardware Wallet segmentinde, Ledger Nano S Plus ile doğrudan rekabet içinde konumlandırılmıştır.



Safe 3'ün pili yoktur ve yalnızca hem güç hem de iletişim için kullanılan bir USB-C bağlantısı üzerinden çalışır. Küçük bir 0,96 inç monokrom OLED ekrana ve iki fiziksel düğmeye sahiptir.



![Image](assets/fr/01.webp)



Safe 3, passphrase BIP39'un mükemmel entegrasyonu da dahil olmak üzere iyi bir Hardware Wallet'ten beklenen tüm temel özellikleri sunar. Ancak, henüz Miniscript'i desteklemiyor.



Bu model özellikle yeni başlayanlar için uygundur ve hatta yeni bir kullanıcıya tavsiye edeceğim Hardware Wallet olabilir. Ayrıca orta düzey kullanıcılar için de çok uygun. Öte yandan, Coldcard gibi cihazlarda bulunan daha spesifik özellikler arayan ileri düzey kullanıcıların tüm beklentilerini karşılamayabilir. Yine de, bu gelişmiş seçeneklere ihtiyacınız yoksa, Trezor Safe 3 mükemmel bir seçim olabilir.



## Trezor Safe 3 güvenlik modeli



Trezor Safe 3 artık Model One ve Model T gibi önceki modellere göre önemli bir gelişme olan EAL6+ sertifikalı **secure element** ile donatılmıştır. Bu, seed'yi doğrudan depolamayan, ancak ona erişimi güvence altına almak için kriptografik bir bileşen görevi gören OPTIGA Trust M V3 çipidir. secure element, yalnızca kullanıcı PIN kodunu doğru girdiğinde erişilebilen bir sırrı saklar. Bu sır daha sonra cihazın ana belleğinde şifreli olarak saklanan seed'nin şifresini çözmek için kullanılır.



Bu hibrit güvenlik sistemi, özellikle Model One'ın özellikle PIN yönetiminde eğilimli olduğu ekstraksiyon saldırılarına veya istilacı analizlere karşı gelişmiş fiziksel koruma sunar. secure element kullanımı sayesinde bu güvenlik açıkları artık ortadan kaldırılmıştır. Bu model aynı zamanda açık kaynaklı bir yazılım mimarisine sahiptir: özel anahtarların üretimini ve kullanımını yöneten kod tamamen erişilebilir ve doğrulanabilir olmaya devam etmektedir. OPTIGA çipi yalnızca Bitcoin Wallet anahtar yönetimine harici bir unsur olan PIN kodunu yönetir. Yalnızca seed'in şifresini çözmek için kullanılabilecek bir sırrı serbest bırakır. Ayrıca, OPTIGA Trust M V3 çipi, SatoshiLabs'a potansiyel güvenlik açıklarını serbestçe yayınlama yetkisi veren nispeten ücretsiz bir lisanstan yararlanmaktadır.



Bu güvenlik modeli, bence bugün piyasada bulunan en iyi uzlaşmalardan birini temsil ediyor. Bir secure element'nin avantajlarını açık kaynaklı yazılım yönetimiyle birleştiriyor. Daha önce kullanıcılar bir çip ile gelişmiş fiziksel güvenlik ve açık kaynak ile şeffaflık arasında seçim yapmak zorundaydı; Trezor Safe 3 ile her ikisinden de faydalanmak mümkün.



Bu eğitimde, Trezor Safe 3'ünüzü nasıl güvenli bir şekilde kuracağınızı ve kullanacağınızı göstereceğiz.



## Trezor Safe 3'ün kutu açılışı



Safe 3'ünüzü teslim aldığınızda, paketin açılmadığını doğrulamak için kutunun ve Seal'ün sağlam olduğundan emin olun. Cihazın orijinalliği ve bütünlüğüne ilişkin bir yazılım doğrulaması da daha sonra kurulduğunda gerçekleştirilecektir.



Kutu içeriği şunları içerir :




- Trezor Safe 3;
- Mnemonic ifadenizi kaydetmek için kart stoğu, çıkartmalar ve talimatlar içeren bir kese;
- USB-C - USB-C kablosu.



![Image](assets/fr/02.webp)



Trezor Safe 3'ünüz açıldığında koruyucu bir plastik ile korunmalı ve USB-C bağlantı noktası holografik bir Seal ile sabitlenmelidir. Orada olduğundan emin olun.



![Image](assets/fr/03.webp)



Cihazda gezinme basittir: sağa kaydırmak için sağ düğmeyi, sola kaydırmak için sol düğmeyi kullanın. Bir eylemi onaylamak için her iki düğmeye aynı anda basın.



![Image](assets/fr/04.webp)



## Ön Koşullar



Bu eğitimde, Trezor Safe 3'ü [Sparrow wallet Wallet yönetim yazılımı] (https://sparrowwallet.com/download/) ile nasıl kullanacağınızı göstereceğim. Bu yazılımı henüz yüklemediyseniz, lütfen şimdi yükleyin. Yardıma ihtiyacınız olursa, Sparrow wallet'nın yapılandırılması hakkında ayrıntılı bir eğitimimiz de var:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Safe 3'ü yapılandırmak, orijinalliğini kontrol etmek ve aygıt yazılımını yüklemek için Trezor Suite yazılımına da ihtiyacınız olacak. Bu yazılımı yalnızca bunun için kullanacağız ve daha sonra yalnızca aygıt yazılımı güncellemeleri için gerekli olacak. Wallet'in günlük yönetimi için yalnızca Sparrow wallet'i kullanacağız, çünkü Bitcoin için optimize edilmiştir ve yeni başlayanlar için bile kullanımı kolaydır (Sparrow yalnızca Bitcoin'u destekler, altcoinleri desteklemez).



[Trezor Suite'i resmi web sitesinden indirin](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



Bu iki program için de, makinenize yüklemeden önce hem orijinalliklerini (GnuPG ile) hem de bütünlüklerini (Hash ile) kontrol etmenizi şiddetle tavsiye ederim. Bunu nasıl yapacağınızı bilmiyorsanız, bu diğer öğreticiyi takip edebilirsiniz:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezor Safe 3'ü başlatma



Safe 3'ünüzü Trezor Suite ve Sparrow wallet'ün zaten yüklü olduğu bilgisayarınıza bağlayın.



![Image](assets/fr/06.webp)



Trezor Suite'i açın, ardından "*Trezor'umu kur*" seçeneğine tıklayın.



![Image](assets/fr/07.webp)



"*Bitcoin-only firmware*" öğesini seçin, ardından "*Install Bitcoin-only*" öğesine tıklayın.



![Image](assets/fr/08.webp)



Trezor Suite daha sonra aygıt yazılımını Safe 3'ünüze yükleyecektir. Lütfen kurulum sırasında bekleyin.



![Image](assets/fr/09.webp)



"*Devam*" üzerine tıklayın.



![Image](assets/fr/10.webp)



Ardından Hardware Wallet'inizin sahte veya ele geçirilmiş olmadığından emin olmak için orijinallik testine geçin.



![Image](assets/fr/11.webp)



Safe 3 cihazınızda onaylamak için sağ düğmeye basın.



![Image](assets/fr/12.webp)



Trezor'unuz orijinalse, Trezor Suite'te bir onay mesajı görünecektir.



![Image](assets/fr/13.webp)



Daha sonra temel kullanım talimatlarını içeren pencereleri atlayabilirsiniz.



![Image](assets/fr/14.webp)



## Bitcoin Wallet Oluşturma



Trezor Suite'te "*Yeni Wallet* oluştur" düğmesine tıklayın.



![Image](assets/fr/15.webp)



Standart bir Wallet için varsayılan yedekleme türünü seçebilirsiniz. Bu, 12 kelimelik bir Mnemonic cümlesine sahip klasik bir single-sig Wallet oluşturur. "*Wallet* Oluştur" üzerine tıklayın.



Eğer *Çoklu Paylaşım Yedekleme* de dahil olmak üzere Trezor'da bulunan diğer yedekleme seçenekleri hakkında daha fazla bilgi edinmek isterseniz, bu eğitime de başvurmanızı tavsiye ederim:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Hardware Wallet kullanım koşullarını kabul edin.



![Image](assets/fr/17.webp)



Yeni bir Wallet oluşturmak için sağ düğmeye tekrar basın.



![Image](assets/fr/18.webp)



Trezor Suite'te "*Yedeklemeye devam et*" seçeneğine tıklayın.



![Image](assets/fr/19.webp)



Yazılım, Mnemonic ifadenizi nasıl yöneteceğinize ilişkin talimatlar sağlar.



Bu Mnemonic size tüm bitcoinlerinize tam ve sınırsız erişim sağlar. Bu ifadeye sahip olan herhangi biri, Trezor Safe 3'ünüze fiziksel erişimi olmasa bile paranızı çalabilir.



12 kelimelik ifade, Hardware Wallet'inizin kaybolması, çalınması veya kırılması durumunda bitcoinlerinize erişimi geri kazandırır. Bu nedenle dikkatlice kaydetmeniz ve güvenli bir yerde saklamanız çok önemlidir.



Kutuyla birlikte verilen kartona yazabilir veya daha fazla güvenlik için, yangından, selden veya çökmeden korumak için paslanmaz çelik bir tabana kazımanızı öneririm.



Talimatları onaylayın, ardından "*Wallet yedeği oluştur*" düğmesine tıklayın.



![Image](assets/fr/20.webp)



Safe 3, rastgele sayı üretecini kullanarak Mnemonic cümlenizi oluşturacaktır. Bu işlem sırasında izlenmediğinizden emin olun. Ekranda verilen kelimeleri seçtiğiniz fiziksel ortama yazın. Güvenlik stratejinize bağlı olarak, ifadenin birkaç tam fiziksel kopyasını çıkarmayı düşünebilirsiniz (ancak her şeyden önce, bölmeyin). Kelimelerin numaralandırılmış ve sıralı olması önemlidir.



***Açıkçası, bu eğitimde yaptığım gibi, bu kelimeleri asla internette paylaşmamalısınız. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir



Mnemonic ifadenizi kaydetmenin ve yönetmenin doğru yolu hakkında daha fazla bilgi için, özellikle de yeni başlayan biriyseniz, bu diğer öğreticiyi izlemenizi şiddetle tavsiye ederim:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



Sonraki kelimelere geçmek için sağ tıklayın. Sol düğmeye tıklayarak geriye doğru gidebilirsiniz. Tüm kelimeleri yazdıktan sonra, bir sonraki adıma geçmek için sağ düğmeyi basılı tutun.



![Image](assets/fr/22.webp)



Mnemonic cümlenizdeki kelimeleri doğru yazdığınızı teyit etmek için sıralarına göre seçin. Teklifler arasında gezinmek için sol ve sağ düğmeleri kullanın, ardından 2 düğmeye aynı anda tıklayarak doğru kelimeyi seçin.



![Image](assets/fr/23.webp)



Bu doğrulama prosedürü tamamlandıktan sonra, sağdaki düğmeye tıklayın.



![Image](assets/fr/24.webp)



## PIN kodunun ayarlanması



Ardından PIN kodu adımı gelir. PIN kodu Trezor'unuzun kilidini açar. Bu nedenle yetkisiz fiziksel erişime karşı koruma sağlar. Bu PIN kodu, Wallet'ünüzün kriptografik anahtarlarının türetilmesinde yer almaz. Dolayısıyla, PIN koduna erişiminiz olmasa bile, 12 kelimelik Mnemonic cümlenize sahip olmanız bitcoinlerinize yeniden erişmenizi sağlayacaktır.



Trezor Suite'te "*PIN'e Devam Et*" ve ardından "*PIN Ayarla*" düğmesine tıklayın.



![Image](assets/fr/25.webp)



Safe 3 ile onaylayın.



![Image](assets/fr/26.webp)



Mümkün olduğunca rastgele bir PIN kodu seçmenizi öneririz. Bu kodu Trezor'unuzun kayıtlı olduğu yerden ayrı bir yere kaydettiğinizden emin olun (örneğin bir parola yöneticisine). PIN kodunu 8 ila 50 basamak arasında tanımlayabilirsiniz. Güvenliği artırmak için mümkün olduğunca uzun bir PIN kodu seçmenizi öneririm.



Her bir rakamı seçmek için sol ve sağ düğmeleri kullanın. Seçiminizi onaylamak ve bir sonraki haneye geçmek için her iki düğmeye aynı anda basın.



![Image](assets/fr/27.webp)



Bitirdiğinizde, rakamların başındaki "*ENTER*" onay işaretine tıklayın, ardından PIN kodunuzu ikinci kez onaylayın.



![Image](assets/fr/28.webp)



PIN kodunuz kaydedildi.



![Image](assets/fr/29.webp)



Trezor Suite'te "*Kurulumu tamamla*" düğmesine tıklayın.



![Image](assets/fr/30.webp)



Safe 3'ünüzün yapılandırması artık tamamlanmıştır. Dilerseniz Hardware Wallet'ünüzün adını ve ana sayfasını değiştirebilirsiniz.



![Image](assets/fr/31.webp)



Hardware Wallet'inizde düzenli ürün yazılımı güncellemeleri yapmak ya da bir kurtarma testi gerçekleştirmek dışında Trezor Suite yazılımına artık ihtiyacımız olmayacak. Artık Sparrow'yi Wallet'i yönetmek için kullanacağız, çünkü bu yazılım yalnızca Bitcoin kullanımı için mükemmel bir şekilde uygundur.



## Wallet'nin Sparrow wallet üzerinde kurulması



Henüz yapmadıysanız, Sparrow wallet'i [resmi web sitesinden] (https://sparrowwallet.com/) bilgisayarınıza indirip yükleyerek başlayın.



Sparrow wallet'yi açtıktan sonra, yazılımın Bitcoin'ün sağ alt köşesindeki tik işaretiyle gösterilen bir Interface düğümüne bağlı olduğundan emin olun. Sparrow'i bağlamakta sorun yaşıyorsanız, bu eğitimin başını okumanızı tavsiye ederim:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

"*Dosya*" sekmesine ve ardından "*Yeni Wallet*" seçeneğine tıklayın.



![Image](assets/fr/32.webp)



Wallet'nize bir isim verin ve ardından "*Wallet* Oluştur "a tıklayın.



![Image](assets/fr/33.webp)



"*Script Type*" açılır menüsünde, bitcoinlerinizi güvence altına almak için kullanılacak script türünü seçin. Ben "*Taproot*" ya da bu mümkün değilse "*Native SegWit*" seçeneğini öneririm.



![Image](assets/fr/34.webp)



"*Bağlı Hardware Wallet*" düğmesine tıklayın. Safe 3 cihazınız elbette bilgisayara bağlı ve kilidi açık olmalıdır.



![Image](assets/fr/35.webp)



"*Tarama*" düğmesine tıklayın. Güvenli 3'ünüz görünmelidir. "*Anahtar Deposunu Aktar*" üzerine tıklayın.



![Image](assets/fr/36.webp)



Artık ilk hesabınızın genişletilmiş genel anahtarı da dahil olmak üzere Wallet'inizin ayrıntılarını görebilirsiniz. Wallet oluşturma işlemini tamamlamak için "*Uygula*" düğmesine tıklayın.



![Image](assets/fr/37.webp)



Sparrow wallet'ye erişimi güvence altına almak için güçlü bir parola seçin. Bu parola, Sparrow wallet verilerinize güvenli erişim sağlayarak genel anahtarlarınızı, adreslerinizi, etiketlerinizi ve işlem geçmişinizi yetkisiz erişime karşı koruyacaktır.



Unutmamak için bu şifreyi bir şifre yöneticisine kaydetmenizi tavsiye ederim.



![Image](assets/fr/38.webp)



Ve şimdi Wallet'ünüz Sparrow wallet'e aktarıldı!



![Image](assets/fr/39.webp)



Wallet'inize ilk bitcoinlerinizi almadan önce, **Boş bir kurtarma testi** yapmanızı şiddetle tavsiye ederim. Xpub'ınız gibi bazı referans bilgilerini yazın, ardından Wallet hala boşken Trezor Safe 3'ünüzü sıfırlayın. Ardından kağıt yedeklerinizi kullanarak Wallet'inizi Trezor'a geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan xpub'ın ilk yazdığınızla eşleşip eşleşmediğini kontrol edin. Eğer eşleşiyorsa, kağıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz.



Kurtarma testinin nasıl yapılacağı hakkında daha fazla bilgi edinmek için bu diğer eğitime başvurmanızı öneririm:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Trezor Safe 3 ile bitcoinleri nasıl alabilirim?



Sparrow'da "*Alma*" sekmesine tıklayın.



![Image](assets/fr/40.webp)



Sparrow wallet tarafından önerilen Address'u kullanmadan önce Trezor'unuzun ekranında kontrol edin. Bu uygulama, Sparrow'te görüntülenen Address'un sahte olmadığını ve Hardware Wallet'nin gerçekten de bu Address ile güvence altına alınan bitcoinleri harcamak için gereken özel anahtara sahip olduğunu doğrulamanızı sağlar. Bu, çeşitli saldırı türlerinden kaçınmanıza yardımcı olur.



Bu kontrolü gerçekleştirmek için "*Address'i Göster*" düğmesine tıklayın.



![Image](assets/fr/41.webp)



Trezor'unuzda görüntülenen Address'ün Sparrow wallet'deki ile eşleşip eşleşmediğini kontrol edin. Geçerliliğinden emin olmak için Address'ünüzü göndericiye iletmeden hemen önce bu kontrolü yapmanız da tavsiye edilir. Onaylamak için düğmeleri kullanabilirsiniz.



![Image](assets/fr/42.webp)



Daha sonra bu Address ile güvence altına alınacak bitcoinlerin kaynağını tanımlamak için bir "*Etiket*" ekleyebilirsiniz. Bu, UTXO'larınızı daha iyi yönetmenizi sağlayan iyi bir uygulamadır.



![Image](assets/fr/43.webp)



Daha sonra bu Address'i bitcoin almak için kullanabilirsiniz.



![Image](assets/fr/44.webp)



## Trezor Safe 3 ile nasıl bitcoin gönderebilirim?



Safe 3 güvenlikli Wallet'nizde ilk Sats'larınızı aldığınıza göre artık onları da harcayabilirsiniz! Trezor'unuzu bilgisayarınıza bağlayın, PIN kodunu kullanarak kilidini açın, Sparrow wallet'yı başlatın ve ardından yeni bir işlem oluşturmak için "*Gönder*" sekmesine gidin.



![Image](assets/fr/45.webp)



Eğer *Coin Kontrolü* yapmak istiyorsanız, yani işlemde hangi UTXO'ların kullanılacağını özellikle seçmek istiyorsanız, "*UTXO'lar*" sekmesine gidin. Harcamak istediğiniz UTXO'ları seçin ve ardından "*Seçilenleri Gönder*" seçeneğine tıklayın. "*Gönder*" sekmesindeki aynı ekrana yönlendirileceksiniz, ancak UTXO'larınız işlem için zaten seçilmiş olacak.



![Image](assets/fr/46.webp)



Hedef Address'u girin. "*+ Ekle*" düğmesine tıklayarak birden fazla adres de girebilirsiniz.



![Image](assets/fr/47.webp)



Bu masrafın amacını hatırlamak için bir "*Etiket*" yazın.



![Image](assets/fr/48.webp)



Bu Address'e gönderilecek tutarı seçin.



![Image](assets/fr/49.webp)



İşleminizin ücret oranını mevcut piyasaya göre ayarlayın. Örneğin, uygun bir ücret oranı seçmek için [Mempool.space](https://Mempool.space/) adresini kullanabilirsiniz.



Tüm işlem parametrelerinizin doğru olduğundan emin olun ve ardından "*İşlem Oluştur*" seçeneğine tıklayın.



![Image](assets/fr/50.webp)



Her şey sizi tatmin ediyorsa, "*İmzalama için İşlemi Sonlandır*" seçeneğine tıklayın.



![Image](assets/fr/51.webp)



"*İmzala*" üzerine tıklayın.



![Image](assets/fr/52.webp)



Trezor Safe 3'ünüzün yanındaki "*İmzala*" düğmesine tıklayın.



![Image](assets/fr/53.webp)



Alıcının alıcı Address'ü, gönderilen miktar ve ücret dahil olmak üzere Hardware Wallet ekranınızdaki işlem parametrelerini kontrol edin. İşlem Trezor'da doğrulandıktan sonra, imzalamak için her iki düğmeye aynı anda tıklayın.



![Image](assets/fr/54.webp)



İşleminiz artık imzalanmıştır. Her şeyin yolunda olup olmadığını son bir kez kontrol edin, ardından Bitcoin ağında yayınlamak için "*İşlemi Yayınla*" düğmesine tıklayın.



![Image](assets/fr/55.webp)



Bunu Sparrow wallet'in "*İşlemler*" sekmesinde bulabilirsiniz.



![Image](assets/fr/56.webp)



Tebrikler, artık Trezor Safe 3'ün Sparrow wallet ile temel kullanımını öğrenmiş bulunuyorsunuz! İşleri bir adım öteye taşımak için, güvenliğinizi artırmak amacıyla Hardware Wallet Trezor'u passphrase BIP39 ile kullanma hakkındaki bu kapsamlı öğreticiyi tavsiye ederim:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!