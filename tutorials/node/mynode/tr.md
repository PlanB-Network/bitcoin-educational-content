---
name: My Node
description: Bitcoin MyNode'unuzu ayarlayın
---

![image](assets/0.webp)


[My Node] (https://mynodebtc.com/) bir Bitcoin ve Lightning düğümü çalıştırmanın en kolay ve en güçlü yoludur! Bitcoin ve Lightning'i kolayca, özel ve güvenli bir şekilde kullanabilmeniz için en iyi açık kaynak yazılımını Interface, yönetim ve desteğimizle birleştiriyoruz.


## Düğüm kurulumu türleri


Çeşitli Node kurulumları vardır. MyNode mükemmeldir. Birlikte gelen birçok uygulama var ve premium sürüm için ödeme yaparsanız daha da fazlası var. Aksi takdirde tüm bu uygulamaları kendiniz indirmek çok sıkıcıdır. MyNode, göreceğiniz gibi bunu oldukça kolaylaştırıyor.


Alternatif ve benzer bir seçenek RaspiBlitz'dir. GUI o kadar güzel değil ve uygulamalar MyNode ile gelen uygulamalarla çok fazla örtüşüyor, ancak Raspiblitz ücretsiz açık kaynaklı yazılım (FOSS) ve MyNode tam olarak değil. Bir diğer fark ise MyNode'un bir Docker konteynerinde çalıştırılıyor olması. Docker'ı ürkütücü ve sorun gidermek için Hard buluyorum. Bu yalnızca hata ya da bug'larla karşılaştığınızda bir sorun teşkil ediyor. Geliştirici, premium kullanıcılar için yardım sunuyor ve bir Telegram sohbet grubu da var.


RaspiBlitz, Docker olmadan Linux'a yüklenmiş birden fazla programdan ibarettir. Harici Hard sürücüsü, Bitcoin core ile başka bir Linux makinesine kolayca takılabilir ve ihtiyaç duyduğunuzda gidebilirsiniz.


Diğer bir seçenek de Bitcoin core ve bir Electrum Server çeşidini (birkaç tane var) bir işletim sistemine kurmaktır. Linux (Raspberry Pi), Mac ve Windows için kılavuzlarım var.


## Alışveriş listesi



- Raspberry Pi 4, 4Gb bellek veya 8Gb (4Gb yeterlidir)
- Resmi Raspberry Pi Gücü (Çok Önemli! Jenerik almayın, cidden)
- Pi için bir kılıf. FLIRC kasası harika. Tüm kasa bir ısı emicidir ve gürültülü olabilen bir fana ihtiyacınız yoktur
- 16 Gb microSD kart (bir taneye ihtiyacınız var, ancak birkaç tane kullanışlı)
- Bir bellek kartı okuyucusu (çoğu bilgisayarda microSD kart için yuva bulunmaz).
- Harici SSD 1Tb Hard sürücü.

Not: SSD çok önemlidir. daha ucuz olsa bile taşınabilir harici Hard sürücü kullanmayın


- Bir ethernet kablosu (ev yönlendiricinize bağlanmak için)
- Monitöre ihtiyacınız yok


## MyNode Görüntüsünü İndirin


MyNode web sitesine gidin Bağlantı


![image](assets/1.webp)


Şimdi İndir`e tıklayın


Raspberry Pi 4 sürümünü indirin:


![image](assets/2.webp)


Büyük bir dosya:


![image](assets/3.webp)


SHA 256 karmalarını indirin


![image](assets/4.webp)


Mac veya Linux'ta terminali veya Windows için Komut İstemi'ni açın. Yazın:


```bash
shasum -a 256 DOWNLOADEDFILENAME # <--- Mac/Linux
certUtil -hashfile DOWNLOADEDFILENAME SHA256 # <--- Windows
```


Bilgisayar 20 saniye kadar düşünür. Ardından, çıktı hash dosyasının önceki adımda web sitesinden indirilenle eşleşip eşleşmediğini kontrol edin. Eğer aynıysa devam edebilirsiniz.

SD kartı flaşlayın


## Balena Etcher'ı indirin ve yükleyin. Bağlantı


Bunun için dijital imzayı bulamadım. Nasıl yapılacağını biliyorsanız lütfen bana bildirin, ben de bu makaleyi güncelleyeyim.


Etcher'ın kullanımı kendinden açıklamalıdır. Mikro SD kartınızı takın ve Raspberry Pi yazılımını (.img dosyası) SD karta flashlayın.


![image](assets/5.webp)

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

![image](assets/10.webp)

![image](assets/11.webp)


Bu işlem tamamlandığında sürücü artık okunamaz. İşletim sisteminden bir hata alabilirsiniz ve sürücü masaüstünden kaybolmalıdır. Kartı dışarı çekin.


## Pi'yi kurun ve SD kartı takın


Parçalar (kasa gösterilmemiştir):


![image](assets/12.webp)

![image](assets/13.webp)


Ethernet kablosunu ve Hard sürücü USB konektörünü bağlayın (henüz güç vermeyin). Ortadaki mavi renkli USB bağlantı noktalarına bağlanmaktan kaçının. Bunlar USB 3'tür. MyNode, sürücü USB 3 özellikli olsa bile USB 2 bağlantı noktasını kullanmanızı önerir.


![image](assets/14.webp)


Mikro SD kart buraya takılır:


![image](assets/15.webp)


Son olarak, gücü bağlayın:


![image](assets/16.webp)


## Pi'nin IP Address'unu bulun


MyNode ile asla bir monitöre ihtiyacınız olmaz. Ancak ev ağında başka bir bilgisayara ihtiyacınız var. Pi'niz ethernet ile bağlı değilse ve WiFi'ye güvenmek istiyorsanız, IP'yi bulmak üst düzey bilgisayar becerileri gerektirir. Size yardımcı olamam, üzgünüm. Bir ethernet bağlantısına ihtiyacınız var. (Sorun, WiFi'ye bağlanmak ve bir şifre girmek için bir monitöre ve işletim sistemine erişime ihtiyaç duymanızdan kaynaklanmaktadır).


Bağlı tüm cihazların IP'lerinin bir listesi için yönlendiricinizi kontrol edin.


Tarayıcıya 192.168.0.1 yazdım (yönlendiricimle birlikte gelen talimatlar), giriş yaptım ve 192.168.0.18 IP'li bir "MyNode" cihazı görebildim. Bu IP adreslerinin internete açık olmadığını unutmayın (önce yönlendiriciden geçerler), bunlar sadece ev ağınızdaki cihazlar için tanımlayıcılardır.


IP'yi bulmak çok önemlidir.


**Not:** "arp -a" komutunu kullanarak ev ağındaki tüm Ethernet bağlantılı cihazların IP Address'ini bulmak için bir Mac veya Linux makinesinde terminali kullanabilirsiniz. Çıktı, yönlendiricinin göstereceği kadar güzel değildir, ancak ihtiyacınız olan tüm bilgiler oradadır. Eğer Pi'nin hangisi olduğu belli değilse, deneme yanılma yöntemini kullanın.


## Pi'ye SSH ile bağlanma


SSH komutu ile cihaza uzaktan giriş yapma seçeneğiniz vardır, ancak bu gerekli değildir (RaspiBlitz Node ise). Yine de çok kullanışlı olduğu için size nasıl yapılacağını göstereceğim.


Bir Mac veya Linux bilgisayar açın (Windows için bir SSH aracı olan putty'yi indirin) ve yazın:


```bash
ssh admin@192.168.0.18
```


Kendi IP Address'nizi kullanın. MyNode cihazı için kullanıcı adı varsayılan olarak "admin "dir. Parola varsayılan olarak "Bolt "tür.


Pi'nizi daha önce kullandıysanız ve mikro SD kartı değiştirdiyseniz, bu hatayı alırsınız:


![image](assets/17.webp)


Yapmanız gereken "known_hosts" dosyasının bulunduğu yere gitmek ve onu silmektir. Bunu yapmak güvenli. Hata mesajı size yolu gösterir. Benim için /Users/MyUserName/.ssh/ idi


Ssh'den önceki "." işaretini unutmayın, bu onun gizli bir dizin olduğunu gösterir.


Ardından ssh komutunu tekrar deneyin.


Bu sefer bu çıktıyı göreceksiniz:


![image](assets/18.webp)


Sildiğiniz dosya silindi ve yeni bir parmak izi ekliyorsunuz. Evet ve <enter> yazın.


Şifreyi girmeniz istenecektir. "Bolt"


Artık bir monitör olmadan MyNode Pi'ye terminal erişiminiz var ve her şeyin sorunsuz bir şekilde yüklendiğini doğrulayabilirsiniz.


![image](assets/19.webp)


## Web Tarayıcısı üzerinden erişim


Bir tarayıcı açın. Ev ağınızdaki bir bilgisayar olması gerekiyor, bunu dışarıdan yapamazsınız. Bir yolu var ama Hard. Henüz test etmedim.


IP Address'yı tarayıcı Address penceresine yazın. Bu gerçekleşecektir:


![image](assets/20.webp)


"Bolt" şifresini girin - daha sonra değiştirin.


O zaman bu olacak:


![image](assets/21.webp)


Sürücüyü Biçimlendir'i seçin


![image](assets/22.webp)


Şimdi bekleyeceğiz.


Bir noktada size ürün anahtarınızı mı yoksa ücretsiz "topluluk sürümünü" mü kullanmak istediğiniz sorulacak - ben Premium sürümü göstereceğim. Ödeyebiliyorsanız premium sürüm için ödeme yapmanızı tavsiye ederim, buna çok değer.


![image](assets/23.webp)


Daha sonra indirilen blokların ilerlemesini göreceksiniz. Bu günler sürer:


![image](assets/24.webp)


Gerekirse indirme sırasında makineyi kapatmak güvenlidir. Ayarlara gidin ve makineyi kapatmak için düğmeyi bulun. Kabloyu öylece çekmeyin, kurulumu veya Hard sürücüsünü bozabilirsiniz.


En başta "Ayarlar "a gidip quicksync'i devre dışı bıraktığınızdan emin olun. İlk blok indirmeye en baştan başlayacaktır.


![image](assets/25.webp)


Kılavuzu oluşturmaya devam etmek istedim, işte daha önce hazırladığım başka bir MyNode. Blockchain senkronize edildiğinde ve birkaç "uygulama" etkinleştirilip senkronize edildiğinde sayfa böyle görünüyor:


![image](assets/26.webp)


Electrum Sunucusunun da senkronize edilmesi gerektiğini unutmayın, bu nedenle Bitcoin Blockchain senkronize edilir edilmez, bu işlemi başlatmak için düğmeye tıklayın - bir veya iki gün sürer. Etkinleştirmeyi seçtiğinizde diğer her şey birkaç dakika içinde etkinleştirilir. Bir şeylere tıklayabilir ve keşfedebilirsiniz. Hiçbir şeyi bozmayacaksınız. Bir şey bozulursa (bu benim başıma geldi, ama sanırım ucuz parçalarım olduğu için) yeniden flaşlamanız ve yeniden indirmeye başlamanız gerekecek. MyNode ile yaşadığım sorun, "yeniden flaşlama" yapmanız gerektiğinde Blockchain senkronizasyonunu sıfırdan tekrar başlatmanız gerekmesi. Bunu aşmanın teknik yolları var ama kolay değil.


RaspiBlitz gibi başka bir düğüm de denemek istiyorsanız, ek bir SSD harici Hard sürücüye ve flaş için başka bir mikro SD karta ihtiyacınız vardır. Aksi takdirde, aynı ekipmana sahip olursunuz, sadece MyNode ve RaspiBlitz'i aynı anda çalıştıramazsınız. Bunu yapmak istiyorsanız, başka bir Raspberry Pi için alışveriş yapma zamanı.


Artık çalışan bir düğümünüz olduğuna göre, onu kullanın, sizin için hiçbir şey yapmadan orada oturmasına izin vermeyin. Electrum Desktop Wallet'ünüzü Electrum Server ve Bitcoin core'e nasıl bağlayacağınıza dair makalemi (ve videomu) buradan takip edebilirsiniz.