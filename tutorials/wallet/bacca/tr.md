---
name: Bacca
description: Ledger Live yazılımı olmadan bir Ledger yapılandırma
---
![cover](assets/cover.webp)


Bir Ledger kullanıyorsanız, muhtemelen en azından ilk cihaz yapılandırması için, orijinalliğini kontrol etmek ve üzerine Bitcoin uygulamasını yüklemek için Ledger Live yazılımından geçmeniz gerektiğini fark etmişsinizdir. Ancak, bu yapılandırmadan sonra, birçok bitcoin kullanıcısı Ledger Live yerine Sparrow veya Liana gibi özel Bitcoin Wallet yönetim yazılımlarını kullanmayı tercih etmektedir. Ledger, en son Bitcoin özelliklerini hızlı bir şekilde içeren mükemmel donanım cüzdanları üretmesine rağmen, yazılımları bitcoin kullanıcılarının özel ihtiyaçlarına göre uyarlanmış değildir. Gerçekten de, Ledger Live altcoinler için tasarlanmış birçok özellik içerirken, Bitcoin Wallet yönetimine adanmış seçenekler sınırlıdır. Ancak Sparrow ve Liana ile ilgili sorun (şimdilik), Bitcoin uygulamasını Ledger'e yüklemenize izin vermemeleridir.


Ledger'inizin ilk yapılandırması sırasında Ledger Live'ı kullanma ihtiyacını atlamak için Bacca aracını (veya "Ledger Installer") kullanabilirsiniz. Bu yazılım, Bitcoin uygulamasını yüklemenize ve güncellemenize, Ledger'inizin orijinalliğini doğrulamanıza ve hatta daha sonra cihazın aygıt yazılımını güncellemenize olanak tanır. Bacca, Chaincode Labs'de Bitcoin core geliştiricisi, [Revault ve Liana'un] kurucu ortağı (https://wizardsardine.com/) ve Pythcoiner olan Antoine Poinsot (Darosior) tarafından oluşturulmuştur.


Bu eğitimde size bu aracı nasıl kullanacağınızı göstereceğim, böylece Ledger Live yazılımı olmadan da Ledger cihazlarının keyfini çıkarabilirsiniz. Tüm cihazlarda çalışır: Nano S Classic, Nano S Plus, Nano X, Flex ve Stax.


---
*Lütfen bu aracın oldukça yeni olduğunu ve geliştiricilerinin hala **test aşamasında** olduğunu belirttiklerini unutmayın. Gerçek bir Bitcoin Wallet barındırması amaçlanan bir cihaz için değil, yalnızca test amacıyla kullanılmasını önermektedirler, ancak bunu yapmak mümkündür. Bu bağlamda, bu aracın geliştiricilerinin [GitHub depolarının README'sinde] belirtilen tavsiyelerine uymanızı tavsiye ederim (https://github.com/darosior/ledger_installer).*


---
## Ön Koşullar


Bilgisayarınızda Bacca'yı kullanmak için iki araca ihtiyacınız olacak:




- Git;
- Rust.


Bunları zaten yüklediyseniz, bu adımı atlayabilirsiniz.


**Linux:**


Bir Linux dağıtımında Git genellikle önceden yüklenmiştir. Git'in sisteminizde kurulu olup olmadığını kontrol etmek için terminalde aşağıdaki komutu yazabilirsiniz :


```bash
git --version
```


Sisteminizde Git yüklü değilse, Debian'a yüklemek için gereken komut aşağıda verilmiştir:


```bash
sudo apt install git
```


Son olarak, Rust geliştirme ortamınızı kurmak için şu komutu kullanın :


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


**Windows:**


Git'i yüklemek için [projenin resmi web sitesine] (https://git-scm.com/) gidin. Yazılımı indirin ve kurulum talimatlarını izleyin.


![BACCA](assets/fr/01.webp)


Rust'i [resmi web sitesinden] (https://www.Rust-lang.org/tools/install) yüklemek için aynı şekilde devam edin.


![BACCA](assets/fr/02.webp)


**MacOS:**


Git sisteminizde henüz kurulu değilse, bir terminal açın ve yüklemek için aşağıdaki komutu çalıştırın:


```bash
git --version
```


Git sisteminizde yüklü değilse, Git'i içeren Xcode'u yüklemenizi öneren bir pencere açılacaktır. Kuruluma devam etmek için ekrandaki talimatları izlemeniz yeterlidir.


Rust'yı kurmak için aşağıdaki komutu çalıştırın:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


## Bacca kurulumu


Bir terminal açın ve yazılımı kaydetmek istediğiniz klasöre gidin, ardından aşağıdaki komutu çalıştırın:


```bash
git clone https://github.com/darosior/ledger_installer.git
```


Yazılım dizinine gidin:


```bash
cd ledger_installer
```


Ardından projeyi derlemek ve Bacca GUI'yi çalıştırmak için Cargo'yu kullanın:


```bash
cargo run -p ledger_manager_gui
```


Artık Interface yazılımına erişiminiz var.


![BACCA](assets/fr/03.webp)


## Ledger'in Yapılandırılması


Başlamadan önce, Ledger'unuz yeniyse PIN kodunu ayarladığınızdan ve kurtarma cümlesini kaydettiğinizden emin olun. Bu ilk adımlar için Ledger Live'a ihtiyacınız yoktur. Ledger'unuza güç vermek için USB kablosuyla bağlamanız yeterlidir. Bu iki adımda nasıl ilerleyeceğinizden emin değilseniz, modelinize özgü eğitimin başına bakabilirsiniz:


https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Bacca'yı Kullanmak


Ledger'nizi bilgisayarınıza bağlayın ve ayarladığınız PIN kodunu kullanarak kilidini açın. Bacca, Ledger'nizi otomatik olarak algılamalıdır.


![BACCA](assets/fr/04.webp)


Ledger cihazınızın gerçekliğini onaylamak için "*Check*" düğmesine tıklayın. Devam etmek için Ledger cihazınızdaki bağlantıyı yetkilendirmeniz gerekecektir.


![BACCA](assets/fr/05.webp)


Bacca daha sonra Ledger'nizin orijinal olup olmadığını size bildirecektir. Eğer değilse, bu ya cihazın ele geçirildiğini ya da sahte olduğunu gösterir. Bu durumda, cihazı kullanmayı derhal bırakın.


![BACCA](assets/fr/06.webp)


"*Apps*" menüsünde, Ledger'ünüzde halihazırda yüklü olan uygulamaların listesine bakabilirsiniz.


![BACCA](assets/fr/07.webp)


Bitcoin uygulamasını yüklemek için "*Yükle*" seçeneğine tıklayın, ardından Ledger'inize yükleme yetkisi verin.


![BACCA](assets/fr/08.webp)


Uygulama iyi bir şekilde kurulmuştur.


![BACCA](assets/fr/09.webp)


Bitcoin uygulamasının en son sürümü yüklü değilse, Bacca "*En Son*" göstergesi yerine bir "*Güncelle*" düğmesi görüntüleyecektir. Uygulamayı güncellemek için bu düğmeye tıklamanız yeterlidir.


![BACCA](assets/fr/10.webp)


Artık Ledger'unuz Bitcoin uygulamasının en son sürümüyle doğru şekilde yapılandırıldığına göre, Ledger Live'dan geçmek zorunda kalmadan Wallet'unuzu Sparrow veya Liana gibi yönetim yazılımlarına aktarmaya ve kullanmaya hazırsınız!


Bu eğitimi faydalı bulduysanız, aşağıya bir Green başparmak bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Ayrıca, yazılımınızı yüklemeden önce bütünlüğünü ve gerçekliğini nasıl kontrol edeceğinizi açıklayan GnuPG hakkındaki bu eğitime de göz atmanızı tavsiye ederim. Bu, özellikle Wallet veya Liana gibi Sparrow yönetim yazılımlarını kurarken önemli bir uygulamadır:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc