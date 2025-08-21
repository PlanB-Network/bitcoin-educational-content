---
name: Blockstream Green - Masaüstü
description: Bilgisayarınızda Green Wallet'i kullanma
---
![cover](assets/cover.webp)


Bu eğitimde, bir Hardware Wallet üzerindeki güvenli bir Wallet'yi yönetmek için bilgisayarınızdaki Blockstream Green yazılımını nasıl kullanacağınızı inceleyeceğiz. Bir Hardware Wallet kullanırken, Wallet'yi yönetmek için bilgisayarınızda bir yazılım kullanmanız çok önemlidir. Bu yönetim yazılımının özel anahtarlara erişimi yoktur; yalnızca Wallet bakiyenize, generate alıcı adreslerine danışmak ve Hardware Wallet tarafından imzalanacak işlemleri oluşturmak ve dağıtmak için kullanılır. Green, Bitcoin Hardware Wallet'ünüzü yönetmek için mevcut birçok çözümden sadece biridir.


2024 yılında Blockstream Green yalnızca Ledger Nano S (eski sürüm), Ledger Nano X, Trezor One, Trezor T ve Blockstream Jade cihazlarıyla uyumludur.


## Blockstream Green ile tanışın


Blockstream Green mobil ve masaüstünde kullanılabilen bir yazılım uygulamasıdır. Eskiden Green Address olarak bilinen bu Wallet, 2016 yılında satın alınmasının ardından bir Blockstream projesi haline geldi.


Green kullanımı çok kolay bir uygulamadır, bu da onu özellikle yeni başlayanlar için uygun hale getirir. Hot cüzdanlarının, donanım cüzdanlarının ve Liquid Sidechain'deki cüzdanların yönetimi gibi çeşitli işlevler sunar. Ayrıca bir Watch-only wallet kurmak için de kullanabilirsiniz.


![GREEN-DESKTOP](assets/fr/01.webp)


Bu eğitimde, yalnızca yazılımı bilgisayarda kullanmaya odaklanacağız. Green'in diğer kullanımlarını keşfetmek için lütfen diğer özel eğitimlerimize bakın:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

## Blockstream Green yazılımının yüklenmesi ve yapılandırılması


Blockstream Green yazılımını bilgisayarınıza yükleyerek başlayın. Resmi web sitesine] (https://blockstream.com/Green/) gidin ve "*Şimdi İndir*" düğmesine tıklayın. Ardından işletim sisteminize göre kurulum sürecini takip edin.


![GREEN-DESKTOP](assets/fr/02.webp)


Uygulamayı başlatın, ardından "Koşulları kabul ediyorum...*" kutusunu işaretleyin.


![GREEN-DESKTOP](assets/fr/03.webp)


Green'yi ilk kez açtığınızda, ana ekran yapılandırılmış bir Wallet olmadan görünür. Daha sonra, cüzdanlar oluşturur veya içe aktarırsanız, bu Interface'te görüneceklerdir. Bir Wallet oluşturmaya devam etmeden önce, uygulamanın ayarlarını ihtiyaçlarınıza göre düzenlemenizi tavsiye ederim. Sol alt köşedeki Ayarlar simgesine tıklayın.


![GREEN-DESKTOP](assets/fr/04.webp)


"*Genel*" menüsünde yazılım dilini değiştirebilir ve dilerseniz deneysel işlevleri etkinleştirebilirsiniz.


![GREEN-DESKTOP](assets/fr/05.webp)


"*Ağ*" menüsünde, tüm bağlantılarınızı şifreleyen ve faaliyetlerinizin izlenmesini zorlaştıran bir ağ olan Tor üzerinden bağlantıyı etkinleştirebilirsiniz. Bu seçenek uygulamanın çalışmasını biraz yavaşlatsa da, özellikle kendi tam düğümünüzü kullanmıyorsanız, gizliliğinizi korumak için şiddetle tavsiye edilir.


![GREEN-DESKTOP](assets/fr/06.webp)


Kendi tam düğümüne sahip kullanıcılar için Green, bir Electrum sunucusu aracılığıyla bağlanma seçeneği sunarak Bitcoin ağ bilgileri ve işlem yayılımı üzerinde tam kontrolü garanti eder. Bunu yapmak için, "*Özel sunucular ve doğrulama*" menüsüne tıklayın, ardından Electrum sunucu bilgilerinizi girin.


![GREEN-DESKTOP](assets/fr/07.webp)


Diğer bir alternatif özellik ise, belirli Blockchain verilerini doğrudan doğrulamanıza ve böylece Blockstream'in varsayılan düğümüne güvenme ihtiyacını azaltmanıza olanak tanıyan "*SPV Doğrulama*" seçeneğidir, ancak bu yöntem bir Full node'in tüm garantilerini sağlamaz. Bu seçenek ayrıca "*Özel sunucular ve doğrulama*" menüsünde de bulunabilir.


![GREEN-DESKTOP](assets/fr/08.webp)


Bu parametreleri ihtiyaçlarınıza göre ayarladıktan sonra, bu Interface'den çıkabilirsiniz.


## Blockstream Green üzerinde bir Bitcoin Wallet içe aktarın


Artık Bitcoin Wallet'nizi içe aktarmaya hazırsınız. "**Get Started**" düğmesine tıklayın.


![GREEN-DESKTOP](assets/fr/09.webp)


Yerel bir Software Wallet oluşturmak veya bir Hardware Wallet üzerinden bir Cold Wallet yönetmek arasında seçim yapabilirsiniz. Bu eğitim için, bir Hardware Wallet'i yönetmeye odaklanacağız, bu nedenle "*Hardware Wallet'de*" seçeneğini seçmeniz gerekecek.


"*Sadece izle*" seçeneği, ilgili fonları harcayamadan Wallet işlemlerini görüntülemek için genişletilmiş bir genel anahtarı (`xpub`) içe aktarmanıza olanak tanır.


![GREEN-DESKTOP](assets/fr/10.webp)


Eğer bir Jade kullanıyorsanız, ilgili düğmeye tıklayın. Aksi takdirde, "*Farklı bir Donanım Aygıtı Bağlayın*" seçeneğini seçin. Benim durumumda, bir Ledger Nano S kullanıyorum. Ledger kullanıcıları için, Green yalnızca bu sürümü desteklediğinden, Hardware Wallet'ünüze "*Bitcoin Legacy*" uygulamasını yüklediğinizden emin olun.


![GREEN-DESKTOP](assets/fr/11.webp)


Hardware Wallet'nizi bilgisayara bağlayın ve Green'i seçin.


![GREEN-DESKTOP](assets/fr/12.webp)


Green'nin Wallet bilgilerinizi içe aktarmasını bekleyin, ardından bu bilgilere erişebilirsiniz.


![GREEN-DESKTOP](assets/fr/13.webp)


Bu noktada iki olası senaryo vardır. Eğer Hardware Wallet'inizi daha önce kullandıysanız, hesabınızın yazılımda göründüğünü göreceksiniz. Ancak, benim gibi, Hardware Wallet'inizi henüz kullanmadan bir Mnemonic cümlesi oluşturarak yeni başlattıysanız, bir hesap oluşturmanız gerekecektir. "*Hesap Oluştur*" üzerine tıklayın.


![GREEN-DESKTOP](assets/fr/14.webp)


Klasik bir Wallet kullanmak istiyorsanız "*Standart*" seçeneğini seçin.


![GREEN-DESKTOP](assets/fr/15.webp)


Artık hesabınıza erişiminiz var.


![GREEN-DESKTOP](assets/fr/16.webp)


## Hardware Wallet'i Blockstream Green ile kullanma


Artık Bitcoin Wallet'niz ayarlandığına göre, ilk Sats'inizi almaya hazırsınız! "*Al*" düğmesine tıklamanız yeterlidir.


![GREEN-DESKTOP](assets/fr/17.webp)


Address'u kopyalamak için "*Address'u Kopyala*" düğmesine tıklayın veya QR kodunu tarayın.


![GREEN-DESKTOP](assets/fr/18.webp)


İşlem ağda yayınlandıktan sonra Wallet'ınızda görünecektir. İşlemin değiştirilemez olduğunu düşünmek için yeterli sayıda onay alana kadar bekleyin.


![GREEN-DESKTOP](assets/fr/19.webp)


Wallet'inizde bitcoinler varken, artık onları göndermeye hazırsınız. "*Gönder*" düğmesine tıklayın.


![GREEN-DESKTOP](assets/fr/20.webp)


Sonraki sayfada, alıcının Address numarasını girin. Manuel olarak girebilir veya web kameranızla bir QR kodu tarayabilirsiniz.


![GREEN-DESKTOP](assets/fr/21.webp)


Ödeme tutarını seçin.


![GREEN-DESKTOP](assets/fr/22.webp)


Ekranın alt kısmında, bu işlem için ücret oranını seçebilirsiniz. Uygulamanın önerilerini takip etme veya ücretlerinizi özelleştirme seçeneğiniz vardır. Bekleyen diğer işlemlere göre ücret ne kadar yüksekse, işleminiz o kadar hızlı işlenecektir. Ücret piyasası bilgileri için lütfen [Mempool.space] (https://Mempool.space/) adresindeki "*İşlem Ücretleri*" bölümünü ziyaret edin.


![GREEN-DESKTOP](assets/fr/23.webp)


İşleminizde hangi UTXO'ların kullanılacağını özellikle seçmek isterseniz, "*Manuel Coin seçimi*" düğmesine tıklayın.


![GREEN-DESKTOP](assets/fr/24.webp)


İşlem parametrelerinizi kontrol edin ve her şey beklediğiniz gibiyse "*Sonraki*" düğmesine tıklayın.


![GREEN-DESKTOP](assets/fr/25.webp)


Address, tutar ve ücretlerin doğru olduğunu iki kez kontrol edin, ardından "*İşlemi onayla*" seçeneğine tıklayın.


![GREEN-DESKTOP](assets/fr/26.webp)


Hardware Wallet ekranınızda tüm işlem parametrelerinin doğru olduğundan emin olun, ardından işlemi bu ekranı kullanarak imzalayın.


![GREEN-DESKTOP](assets/fr/27.webp)


İşlem Hardware Wallet'den imzalandıktan sonra, Green bunu otomatik olarak Bitcoin ağına yayınlar. İşleminiz daha sonra Bitcoin Wallet kontrol panelinizde görünecek ve onaylanmayı bekleyecektir.


![GREEN-DESKTOP](assets/fr/28.webp)


Artık Blockstream Green'i bir Hardware Wallet üzerinde Bitcoin Wallet'ünüzü yönetmek için nasıl kolayca yapılandıracağınızı biliyorsunuz.


Bu eğitimi faydalı bulduysanız, aşağıya bir Green başparmak bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Ayrıca Blockstream Green Hot Wallet kurulumu için Hot mobil uygulaması hakkındaki bu diğer kapsamlı eğitime de göz atmanızı tavsiye ederim:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143