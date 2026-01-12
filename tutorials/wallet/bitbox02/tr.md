---
name: BitBox02

description: BitBox02'nin kurulumu ve kullanımı
---

![cover](assets/cover.webp)


BitBox02 (https://bitbox.swiss/), Bitcoin'lerinizi güvence altına almak için özel olarak tasarlanmış İsviçre yapımı bir fiziksel Wallet'dir. Temel özelliklerinden bazıları microSD kart kullanarak kolay yedekleme ve geri yükleme, minimalist ve gizli bir tasarım ve Bitcoin için kapsamlı destektir.


![device](assets/1.webp)


Uzmanlar tarafından tasarlanmış, güvenli bir çip içeren çift çipli bir tasarıma sahip son teknoloji güvenlik sunar. Kaynak kodu güvenlik araştırmacıları tarafından tamamen denetlenmiştir ve tamamen açık kaynaklıdır. BitBox02, Bitcoin'lerinizin güvenli yönetimini sağlayan basit ama güçlü bir BitBoxApp ile birlikte gelir. Bitcoin için Full node'yi destekler ve uygulama ile cihaz arasında uçtan uca şifrelenmiş iletişim sağlar. İsviçre'de üretilen BitBox02, kullanıcıları arasında olumlu bir itibar kazanmıştır.


![video](https://youtu.be/sB4b2PbYaj0)


İşte Wallet teknik özellikleri:



- Bağlanabilirlik: USB-C
- Uyumluluk: Windows 7 ve sonrası, macOS 10.13 ve sonrası, Linux, Android
- Giriş: Kapasitif dokunmatik sensörler
- Mikrodenetleyici: ATSAMD51J20A; 120 Mhz 32-bit Cortex-M4F; Gerçek rastgele sayı üreteci
- Güvenli çip: ATECC608B; Gerçek rastgele sayı üreteci (NIST SP 800-90A/B/C)
- Ekran: 128 x 64 piksel beyaz OLED
- Malzeme Polikarbonat
- Boyut: USB-C fişi dahil 54,5 x 25,4 x 9,6 mm
- Ağırlık: Cihaz 12g; ambalaj ve aksesuarlarla birlikte 160g


Veri sayfalarını web sitelerinden indirin https://bitbox.swiss/bitbox02/


## BitBox02 Hardware Wallet nasıl kullanılır?


### BitBox02'nin Kurulumu


BitBox02'nin kabuğuna bağlı bir USB-C bağlantısı vardır. Bilgisayarınız normal USB bağlantı noktasını kullanıyorsa, cihazla birlikte gelen adaptörü kullanmanız gerekecektir.


Bilgisayarınıza bağlayın ve cihaz açılacaktır (henüz yapmayın).


Üstünde ve altında sensörler vardır ve ekranı istediğiniz şekilde yönlendirmek için üste veya alta dokunmanızı isteyecektir.


![image](assets/2.webp)


### BitBox02 Uygulamasını İndirin


Https://shiftcrypto.ch/ adresini ziyaret edin ve indirme sayfasına ulaşmak için en üstteki "Uygulama" bağlantısına tıklayın:


![image](assets/3.webp)


Mavi İndir düğmesine tıklayın:


![image](assets/4.webp)


İndirmeyi doğrulamak için (karmaşıklık yaratır, ancak özellikle çok sayıda Bitcoin depoluyorsanız önerilir), Ek A'ya bakın.


İndirdikten sonra dosyayı açabilirsiniz. Mac'te, indirilen dosyaya çift tıkladığınızda indirilenler dizininizde bir BitBox Uygulama simgesi görünecektir. Kolay erişim için masaüstünüze (veya herhangi bir yere) sürükleyebilirsiniz.


Çalıştırmak için Uygulamaya çift tıklayın ("yüklenmez").


Mac'te, bilgisayar dadınız size bir uyarı verecektir. Sadece görmezden gelin ve "aç "a tıklayın:


![image](assets/5.webp)


Daha sonra bunu göreceksiniz:


![image](assets/6.webp)


Devam edin ve cihazı bilgisayara bağlayın.


Size bir eşleştirme kodu gösterecektir. Eşleştiklerini kontrol edin ve ardından onay işaretini seçmek için sensöre dokunun. Ardından ekrana geri döndüğünüzde, devam düğmesi sizin için kullanılabilir hale gelecektir.


![image](assets/7.webp)


Ardından yeni bir seed oluşturma veya bir seed'u geri yükleme seçeneğiniz olacaktır. Yeni bir seed oluşturmayı göstereceğim (Wallet'e herhangi bir Bitcoin yüklemeden önce, yedeklemenizin kalitesini test etmek için oluşturduğunuz seed'u geri yüklemeniz de önemlidir).


![image](assets/8.webp)


Cihaz bir microSD kart ile birlikte gelir. Eğer yoksa devam edin ve takın.


![image](assets/9.webp)


Cihazınızı adlandırın ve devam et'e tıklayın, ardından cihaz üzerinde onaylayın.


![image](assets/10.webp)


Daha sonra cihaz için bir şifre belirlemeniz istenecektir. Bu, seed'inizin bir parçası değildir. passphrase da değildir (bu seed'in bir parçasıdır). Bu sadece cihazı kilitlemek için bir paroladır. Cihazı açtığınızda, her seferinde bu şifreyi girmeniz istenecektir. Cihaz kendini tüm hafızadan silmeden önce art arda 10 hata yapma hakkınız vardır, bu yüzden dikkatli olun. Ekrandaki animasyon size şifreyi ayarlamak için cihaz kontrollerini nasıl kullanacağınızı öğretecektir.


![image](assets/11.webp)


Bir sonraki ekranı okuyun ve her kutuyu işaretleyin, ardından devam edin.


![image](assets/12.webp)

![image](assets/13.webp)

![image](assets/14.webp)


Ve Wallet kullanıma hazır olduğunda böyle görünüyor.


![image](assets/15.webp)


### ÇOK HIZLI DEĞİL!!


Oldukça garip ama BitBox02 bize cihazı kullanmaya hazır olduğumuzu söylüyor, ancak seed kelimelerini yazmamızı istemedi! Elimizdeki TEK yedekleme microSD karta kaydedilen dosya. Bu da yetersiz. Bu depolama aygıtları sonsuza kadar dayanmaz ("bit çürümesi" nedeniyle). Bir kağıt yedeğe ve bir kasada saklanan kopyalara ihtiyacımız var (genel donanım-cüzdan nasıl kullanılır kılavuzunda açıklandığı gibi)


seed cümlemizi almak ve bir yere yazmak için soldaki "cihazı yönet" sekmesine gidin ve ardından "kurtarma kelimelerini göster" seçeneğine tıklayın


![image](assets/16.webp)


Daha sonra onaylama işleminden geçebilirsiniz ve cihaz size kelimeleri sunacaktır. Kelimeleri düzgünce yazın ve kimsenin görmesine izin vermeyin.


![image](assets/17.webp)


Bundan sonra, alıcı adreslerinizi almak için soldaki Bitcoin sekmesine tıklayabilirsiniz.


![image](assets/18.webp)


Her seferinde bir tane gösteriyor, ancak en azından ilk 20'den hangi Address'yı kullanacağınızı seçmenize izin veriyor:


![image](assets/19.webp)


Mavi düğmeye tıkladığınızda Address'nin tamamı gösterilecek ve Address'nin ekrandaki görüntüyle eşleşip eşleşmediğini kontrol etmeniz istenecektir. Bu, bilgisayarınızdaki hiçbir kötü amaçlı yazılımın sizi Bitcoin'i bir saldırganın Address'sine göndermek için kandırmadığını doğrulamak için iyi bir uygulamadır.


![image](assets/20.webp)


Bitcoin'i bu Wallet'ye göndermek için, Address'yi kopyalayabilir ve madeni paralarınızın bulunduğu Exchange'un para çekme sayfasına yapıştırabilirsiniz. Önce küçük bir test miktarı göndermenizi, ardından bunu ya Exchange'a ya da Wallet'nizdeki ikinci Address'ye harcama alıştırması yapmanızı öneririm.


Daha büyük miktarlar için bir passphrase oluşturmanızı öneririm (aşağıya bakın). Orijinal Wallet (passphrase yok) yem Wallet olarak kullanılabilir (inandırıcı bir yem olması için içinde makul bir miktar olması gerekecektir).


### Bir düğüme bağlanma


BitBox02 otomatik olarak bir düğüme bağlanacaktır. Nereye bağlandığını görelim. Soldaki ayarlar sekmesine ve ardından "kendi Full node'inizi bağlayın" seçeneğine tıklayın.


![image](assets/21.webp)


Ve burada shiftcrypto'nun düğümüne bağlandığını görebiliyoruz. Pek iyi değil. Onlara tüm Bitcoin adreslerimizi ve IP Address'mızı verdik (elbette seed'u değil; adreslerimizi/dengelerimizi görebilirler, ancak harcayamazlar). Bu sayfaya kendi düğüm bilgilerimizi girebiliriz (bu özel kılavuzun kapsamı dışındadır) veya Sparrow Bitcoin Wallet, Electrum Desktop Wallet veya Spectre Desktop gibi daha iyi yazılımlar kullanabiliriz. Rehberin ilerleyen bölümlerinde Sparrow Bitcoin Wallet'u göstereceğim.


![image](assets/22.webp)


Bir passphrase ekleyin


Artık BitBox02 Uygulaması ile cihazı kurduğumuza göre (ve bu özel Hardware Wallet ile kaçınılmaz olan adreslerimizi ortaya çıkardığımıza göre), seed cümlemize bir passphrase ekleyebiliriz. Bu, aynı seed'i kullanarak yeni bir Wallet oluşturmamıza izin verecek ve ShiftCrypto yeni adreslerimizi asla görmeyecektir. Bu Wallet'ü yalnızca kendi yazılımımıza bağlayacağız.


### passphrase'yı Etkinleştir


Şimdi devam edin ve passphrase özelliğini "etkinleştirin" (ancak henüz bir passphrase ayarlamıyoruz). "Cihazı yönet" sekmesine gidin ve "passphrase'yi etkinleştir" seçeneğine tıklayın (aşağıdaki kırmızı daire).


![image](assets/23.webp)


Adımları okuyun..


![image](assets/24.webp)

![image](assets/25.webp)

![image](assets/26.webp)


Şimdi cihazın bağlantısını kesin ve BitBox02 Uygulamasını kapatın


Parman tarafından bitbox02 bölümünün sonu.


Divice'ınız artık specter, Sparrow ve bitbox Interface gibi herhangi bir masaüstü çözümünde kullanılmak üzere tamamen çalışır durumdadır.