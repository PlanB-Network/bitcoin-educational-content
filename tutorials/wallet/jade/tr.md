---
name: Yeşim

description: JADE cihazınızı nasıl kurarsınız
---

![image](assets/cover.webp)


## Eğitici video


![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)

Blockstream Jade - BTCsession tarafından Mobil Bitcoin Hardware Wallet TAM TUTORIAL


## Tam yazım kılavuzu


![image](assets/cover2.webp)


### Ön Koşullar


1. Blockstream Green'nin en son sürümünü indirin.


2. Jade'in bilgisayarınız tarafından tanındığından emin olmak için bu sürücüyü yükleyin.


### Masaüstü Kurulumu


![full guide](https://youtu.be/0fPVzsyL360)


Blockstream Green'ü açın, ardından Aygıtlar altındaki Blockstream logosuna tıklayın.


![image](assets/1.webp)


Birlikte verilen USB kablosunu kullanarak Jade'i masaüstünüze takın.


**Not:** Jade bilgisayarınız tarafından tanınmıyorsa, gerekli sürücülerin yüklü olduğundan emin olun ve bunun bir USB izinleri sorunundan kaynaklanıp kaynaklanmadığını kontrol edin.


Jade cihazınız Green'te göründüğünde, Güncellemeleri kontrol et seçeneğine tıklayarak Jade cihazınızı güncelleyin ve en son ürün yazılımı sürümünü seçin. Onaylamak ve güncellemeye devam etmek için kaydırma tekerleğini kullanın veya Jade üzerinde geçiş yapın. Jade'inizin hala "Başlat" düğmesini gösterdiğinden emin olun, aksi takdirde Jade'i yükseltmek için ayarladıktan sonraya kadar beklemeniz gerekecektir. Gerekirse bu ekrana geri dönmek için geri düğmesini kullanın.


![image](assets/2.webp)


Jade'in aygıt yazılımını güncelledikten sonra, kullanmak istediğiniz ağ ve güvenlik politikasında Jade'i Kur'u seçin.


**İpucu:** Güvenlik politikası, aşağıda gösterilen giriş ekranında Tür altında listelenmiştir. Singlesig'i mi yoksa Multisig Shield'i mi seçeceğinizden emin değilseniz, lütfen kılavuzumuzu inceleyin [burada](https://help.blockstream.com/hc/en-us/articles/4403642609433)


![image](assets/3.webp)


Ardından, Yeni bir Wallet oluşturmayı seçin ve kurtarma ifadeniz için generate'ya 12 kelime seçin. Gelişmiş seçeneğine tıkladığınızda 12 ve 24 kelimelik kurtarma cümlesi seçenekleri sunulur.


![image](assets/4.webp)


Kurtarma ifadesini çevrimdışı olarak kağıda kaydedin (veya ekstra güvenlik için özel bir kurtarma ifadesi yedekleme cihazı kullanarak). Ardından, kurtarma ifadenizi doğrulamak için Jade cihazınızın üst kısmındaki tekerleği veya geçişi kullanın. Bu adım, doğru şekilde yazdığınızdan emin olmanızı sağlar.


![image](assets/5.webp)


Altı haneli PIN kodunuzu ayarlayın ve onaylayın. Bu, Wallet'inize her giriş yaptığınızda Blockstream Jade'in kilidini açmak için kullanılır.


![image](assets/6.webp)


Şimdi, Green masaüstü uygulamasında Wallet'e Git'i seçin ve Wallet'inizin Blockstream Green'da açıldığını göreceksiniz. Blockstream Jade de Hazır olduğunu gösterecektir! Artık Jade'inizi Bitcoin işlemlerini göndermek ve almak için kullanabilirsiniz.


![image](assets/7.webp)


Wallet'ünüzü kullanmayı bitirdikten sonra Blockstream Jade cihazınızın bağlantısını kesin. Wallet'ü Blockstream Jade üzerinde bir dahaki sefere kullanmak istediğinizde, cihazınızı yeniden bağlayın ve istemleri izleyin.


kaynak: https://help.blockstream.com/hc/en-us/articles/17478506300825


### Ek A - Green Wallet indirme dosyasının doğrulanması


İndirme işlemini doğrulamak, indirdiğiniz dosyanın geliştirici tarafından yayınlandıktan sonra değiştirilmediğini kontrol etmek anlamına gelir.


Bunu, indirilen dosya ve geliştiricinin açık anahtarı ile birlikte imzanın (geliştiricinin özel anahtarı tarafından üretilen) gpg -verify fonksiyonundan geçerken TRUE sonucunu döndürdüğünü kontrol ederek yaparız. Bunu nasıl yapacağınızı daha sonra göstereceğim.


İlk olarak, imzalama anahtarını alıyoruz:


Linux için, terminali açın ve bu komutu çalıştırın (metni kopyalayıp yapıştırmanız ve tırnak işaretlerini eklemeniz yeterlidir):


```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```


Mac için de aynı şeyi yaparsınız, ancak önce GPG Suite'i indirip yüklemeniz gerekir.


Windows için de aynı şeyi yaparsınız, ancak önce GPG4Win'i indirip yüklemeniz gerekir.


Açık anahtarın içe aktarıldığını söyleyen bir çıktı alacaksınız.


![image](assets/9.webp)


Bu resmin boş bir alt niteliği vardır; dosya adı resim-3-1024x162.webp'dir


Daha sonra, yazılımın Hash'sını içeren dosyayı almamız gerekiyor. Blockstream'in GitHub sayfasında saklanıyor. Önce buradaki bilgi sayfalarına gidin ve "masaüstü" bağlantısına tıklayın. GitHub'daki en son sürüm sayfasına götürecek ve orada Blockstream'in indirdiğimiz programın yayınlanmış Hash'sını içeren bir metin belgesi olan SHA256SUMS.asc dosyasına bir bağlantı göreceksiniz.


![image](assets/10.webp)


GitHub:


![image](assets/11.webp)


Gerekli değil, ancak diske kaydettikten sonra, dosyayı Mac'te metin düzenleyicisini kullanarak daha kolay açmak için "SHA256SUMS.asc" dosyasını "SHA256.txt" olarak yeniden adlandırdım. Dosyanın içeriği buydu:


![image](assets/12.webp)


Peşinde olduğumuz metin en üstte. Hangi dosyayı indirdiğimize bağlı olarak, daha sonra karşılaştıracağımız karşılık gelen bir Hash çıktısı vardır.


Belgenin alt kısmı yukarıdaki mesaja atılan imzayı içeriyor - bu ikisi bir arada bir dosya.


Sıra önemli değil, ancak Hash'i kontrol etmeden önce Hash mesajının gerçek olup olmadığını (yani tahrif edilmediğini) kontrol edeceğiz.


Terminali açın. SHA256SUMS.asc dosyasının indirildiği doğru dizinde olmanız gerekir. Linux ve Mac için "İndirilenler" dizinine indirdiğinizi varsayarsak, aşağıdaki gibi dizine geçin (büyük/küçük harfe duyarlı):


```bash
cd Downloads
```


Tabii ki, bu komutlardan sonra <enter> tuşuna basmanız gerekir. Windows için CMD'yi (komut istemi) açın ve aynı şeyi yazın (büyük/küçük harfe duyarlı olmasa da).


Windows ve Mac için, daha önce belirtildiği gibi sırasıyla GPG4Win ve GPG Suite'i indirmiş olmanız gerekir. Linux için, gpg İşletim Sistemi ile birlikte gelir. Terminal'den (veya Windows için CMD'den) şu komutu yazın:


```bash
gpg --verify SHA256SUMS.asc
```


Dosya adının tam yazılışı (kırmızı renkte) dosyayı aldığınız gün farklı olabilir, bu nedenle komutun indirilen dosya adıyla eşleştiğinden emin olun. Bu çıktıyı almalısınız ve güvenilir imza ile ilgili uyarıyı görmezden gelmelisiniz - bu sadece bilgisayara daha önce içe aktardığımız ortak anahtara güvendiğinizi manuel olarak söylemediğiniz anlamına gelir.


![image](assets/13.webp)


Bu görüntünün boş bir alt niteliği vardır; dosya adı image-4-1024x165.webp'dir


Bu çıktı imzanın iyi olduğunu doğrular ve "info@greenaddress.it" özel anahtarının verileri (Hash raporu) imzaladığından eminiz.


Şimdi indirdiğimiz zip dosyasını Hash ile taramalı ve çıktıyı yayınlandığı gibi karşılaştırmalıyız. SHA256SUMS.asc dosyasında "Hash. SHA512" yazan bir metin olduğuna dikkat edin: SHA512" yazan bir metin var, bu da kafamı karıştırıyor, çünkü dosyanın içinde açıkça SHA256 çıktıları var, bu yüzden bunu görmezden geleceğim.


Mac ve Linux için, terminali açın, zip dosyasının indirildiği yere gidin (terminali o zamandan beri kapatmadıysanız muhtemelen tekrar "cd Downloads" yazmanız gerekecektir). Bu arada, PWD ("çalışma dizinini yazdır") yazarak hangi dizinde olduğunuzu her zaman kontrol edebilirsiniz ve bunların hepsi yabancıysa, "Linux/Mac/Windows dosya sisteminde nasıl gezinilir" şeklinde arama yaparak hızlı bir YouTube videosu izlemek yararlı olacaktır.


Dosyaya sahip olmak için şunu yazın:


```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```


Dosyanızın adının tam olarak ne olduğunu kontrol etmeli ve gerekirse yukarıdaki mavi metni değiştirmelisiniz.


Şuna benzer bir çıktı alacaksınız (dosya benimkinden farklıysa sizinki de farklı olacaktır):


![image](assets/14.webp)


Ardından, Hash çıktısını SHA256SUMS.asc dosyasındakiyle görsel olarak karşılaştırın. Eğer eşleşiyorlarsa, o zaman -> BAŞARI! Tebrikler.


kaynak: https://armantheparman.com/jade/


### Sparrow üzerinde kullanma


Sparrow'ü nasıl kullanacağınızı zaten biliyorsanız, o zaman her zamanki gibi:


**Not:** örneğin Spectre için de aynı süreç söz konusudur


Burada verilen bağlantıyı kullanarak Sparrow'ü indirin.


![image](assets/14.5.webp)


Farklı bağlantı seçenekleri hakkında bilgi edinmek üzere kurulum kılavuzunu takip etmek için İleri'ye tıklayın.


![image](assets/15.webp)


İstediğiniz sunucuyu seçin ve ardından Yeni Wallet Oluştur'u seçin.


![image](assets/16.webp)


Wallet'nız için bir ad girin ve Wallet Oluştur'a tıklayın.


![image](assets/17.webp)


İstediğiniz politika ve komut dosyası türlerini seçin ve ardından Bağlı Hardware Wallet'yi seçin.


**Not:** Daha önce Blockstream Jade'i Blockstream Green ile Singlesig Wallet olarak kullandıysanız ve işlemlerinizi Sparrow'da görüntülemek istiyorsanız, komut dosyası türünün Green'de fonlarınızı içeren hesap türüyle eşleştiğinden emin olun. Ayrıca eşleşmesi için türetme yoluna da ihtiyacınız olacaktır.


![image](assets/18.webp)


Blockstream Jade cihazınızı takın ve Tara'ya tıklayın. Daha sonra Jade'e PIN kodunuzu girmeniz istenecektir.


**İpucu:** Jade'inizi bağlamadan önce Blockstream Green uygulamasının açık olmadığından emin olun. Green açıksa, bu Jade'inizin Sparrow içinde algılanmasıyla ilgili sorunlara neden olabilir.


![image](assets/19.webp)


Varsayılan hesabın ortak anahtarını içe aktarmak için Anahtar Deposunu İçe Aktar'ı seçin veya kullanmak istediğiniz türetme yolunu manuel olarak seçmek için oku seçin.


![image](assets/20.webp)


İstediğiniz anahtar içe aktarıldıktan sonra Uygula'ya tıklayın.


![image](assets/21.webp)


Artık Wallet'nizi başarıyla kurdunuz ve Bitcoin'inizi Sparrow ve Blockstream Jade kullanarak almaya, depolamaya ve harcamaya başlayabilirsiniz.


**Not:** Daha önce Jade'i Blockstream Green ile Multisig Shield Wallet olarak kullanıyorsanız, yeni Sparrow wallet'unuzun aynı bakiyeyi göstermesini beklememelisiniz - bunlar farklı cüzdanlardır. Multisig Shield Wallet'inize tekrar erişmek için Jade'inizi Blockstream Green'e geri bağlamanız yeterlidir.


![image](assets/22.webp)


kaynak: https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-


### Green uygulaması


daha çok mobil bir rehber iseniz, Blockstream Green ile kullanabilirsiniz



- Blockstream Jade Green ile nasıl kurulur | Blockstream Jade - https://youtu.be/7aacxnc6DHg
- Bitcoin bir Jade Wallet'ye nasıl alınır | Blockstream Jade - https://youtu.be/CVtcDdiPqLA