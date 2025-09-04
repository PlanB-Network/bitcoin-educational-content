---
name: RaspiBlitz
description: RaspiBlitz'inizi kurmak için kılavuz
---

![image](assets/0.webp)


RaspiBlitz, RaspberryPi (1TB SSD) üzerinde bir Bitcoin-Fullnode ile birlikte çalışan bir kendin yap Lightning Node (LND ve/veya Core Lightning) ve kolay kurulum ve izleme için güzel bir ekrandır.


RaspiBlitz temel olarak evden merkezi olmayan kendi düğümünüzü nasıl çalıştıracağınızı öğrenmeyi hedefliyor - çünkü: Sizin Düğümünüz Değil, Sizin Kurallarınız Değil. Lightning Network'nin büyüyen ekosistemini tam bir parçası haline gelerek keşfedin ve geliştirin. Bir atölyenin parçası olarak veya bir hafta sonu projesi olarak kendiniz inşa edin.


![video](https://youtu.be/DTHlSPMz3ns)

RASPIBLITZ - Yıldırım ve Bitcoin Full node BTC oturumu ile Nasıl Çalıştırılır


# Parman'ın Raspiblitz Kurulum Kılavuzu


Raspiblitz, bir Bitcoin Node ve ilgili uygulamaları çalıştırmak için mükemmel bir sistemdir. Bunu ve My Node düğümünü çoğu kullanıcıya tavsiye ederim (İdeal olarak yedeklilik için iki düğüme sahip olun.) En büyük avantajı, Raspiblitz düğümünün MyNode veya Umbrel'den farklı olarak "Ücretsiz Açık Kaynak Yazılımı" olmasıdır. Bu neden önemli? Vlad Costa açıklıyor. RaspbiBlitz'i ethernet yerine WiFi bağlantısı ile de çalıştırabilirsiniz - işte bunun için ek bir kılavuz. (Bunu MyNode ile yapmanın bir yolunu bulamadım).


Ekli bir mini ekrana sahip hazır bir düğüm satın alabilir veya kendiniz inşa edebilirsiniz (ekrana ihtiyacınız yoktur).


Github sayfasındaki kılavuz mükemmel, ancak muhtemelen orta derecede deneyimli bir kullanıcı için fazla ayrıntılı. Benim talimatlarım daha kısa ve öz olacak ve umarım takip etmeniz daha kolay olur.


Esasen, süreç Raspberry Pi 4 ile bir MyNode düğümü kurma sürecine çok benzer. Raspiblitz kılavuzu bir monitör almanızı öneriyor, ancak gerçekten bir monitöre ihtiyacınız yok ve ben de tavsiye etmem. Ekstra bir klavye ya da fareye bile ihtiyacınız yok. Sadece aynı ev ağındaki bir bilgisayar üzerinden cihazın terminal menüsüne erişin ve terminal kullanarak ssh komutunu kullanın. Bu Linux/Mac ile mümkün (kolay) ve Windows ile biraz daha zor.


## Adım 1: Ekipmanı satın alın.


Bir MyNode düğümünü çalıştırmak için ihtiyacınız olan ekipmanla tamamen aynı ekipmana ihtiyacınız var. Birini ya da diğerini deneyebilirsiniz, tek fark mikro SD karttaki verilerdir.



- Raspberry Pi 4, 4Gb bellek veya 8Gb (4Gb yeterlidir)
- Resmi Raspberry Pi Gücü (Çok Önemli! Jenerik almayın, cidden)
- Pi için bir kılıf. (FLIRC kasası harika. Tüm kasa bir ısı emicidir ve gürültülü olabilen bir fana ihtiyacınız yoktur)
- 32 Gb microSD kart (bir taneye ihtiyacınız var, ancak birkaç tane kullanışlı.)
- Bir bellek kartı okuyucusu (çoğu bilgisayarda microSD kart için yuva bulunmaz).
- Harici SSD 1Tb Hard sürücü.
- Bir ethernet kablosu (ev yönlendiricinize bağlanmak için).


Bir monitöre (veya klavye ya da fareye) ihtiyacınız yok


Not: Bu yanlış Hard sürücüsüdür: Bu taşınabilir bir harici Hard sürücüsüdür. Bu bir SSD değildir. SSD çok önemlidir. Bu yüzden ucuz (AUD cinsinden fiyat)


![image](assets/1.webp)


Bu, alınması gereken doğru tiptir:


![image](assets/2.webp)


Bu daha hızlıdır, ancak gereksiz yere pahalıdır:


![image](assets/3.webp)


## Adım 2: Raspiblitz Görüntüsünü İndirin


Raspiblitz github web sitesine gidin ve "resmi indir" bağlantısını bulun:


![image](assets/4.webp)


İndirilen dosyanın sha-256 Hash değeri web sitesinde verilmiştir. Her güncelleme ile değişecektir. Bunun ne hakkında olduğunu anlamıyorsanız, anlamalısınız, bu yüzden buradan okuyabileceğiniz bir rehber yazdım.


![image](assets/5.webp)


## Adım 3: Görüntüyü Doğrulayın


Devam etmeden önce, komut satırında dosya sistemini bilmiyorsanız, öğrenmesi kolaydır ve öğrenmelisiniz.


İşte Linux için faydalı bir video, ancak Mac için de geçerli.


Windows için, işte basit bir öğretici.


Mac/Linux


Dosyanın indirilmesinin bitmesini bekleyin (önemli!), ardından terminal açıkken dosyayı indirdiğiniz yere gidin ve aşağıdaki komutu yazın:

```bash
shasum -a 256 xxxxxxxxxxxxxx
```


burada `xxxxxxxxxxxxxx` yeni indirdiğiniz dosyanın adıdır. Eğer o dosyanın bulunduğu dizinde değilseniz, tam yolu yazmanız gerekir.


Bilgisayar 20 saniye kadar düşünür. Çıkan hash dosyasının bir önceki adımda web sitesinden indirilenle eşleşip eşleşmediğini kontrol edin. Eğer aynıysa devam edebilirsiniz.

Pencereler


Komut istemini açın ve dosyanın indirildiği yere gidin ve bu komutu yazın:


```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```


burada `xxxxxxxxxxxxxx` yeni indirdiğiniz dosyanın adıdır. Eğer o dosyanın bulunduğu direktörde değilseniz, tam yolu yazmanız gerekir.


Bilgisayar 20 saniye kadar düşünür. Çıkan hash dosyasının bir önceki adımda web sitesinden indirilenle eşleşip eşleşmediğini kontrol edin. Eğer aynıysa devam edebilirsiniz.


## Adım 4: SD kartı flaşlayın


Bunu yapmak için Balena Etcher'ı kullanabilirsiniz. Buradan indirebilirsiniz.


Etcher'ın kullanımı kendi kendini açıklar. Mikro SD kartınızı takın ve Raspiblitz yazılımını (.img dosyası) SD karta flaşlayın.


![image](assets/6.webp)


![image](assets/7.webp)


![image](assets/8.webp)


![image](assets/9.webp)


Bu işlem tamamlandığında sürücü artık okunamaz. İşletim sisteminden bir hata alabilirsiniz ve sürücü masaüstünden kaybolmalıdır. Kartı dışarı çekin.


## Adım 5: Pi'yi kurun ve SD kartı takın


Parçalar (kasa gösterilmemiştir):


![image](assets/10.webp)


![image](assets/11.webp)


Ethernet kablosunu ve Hard sürücü USB konektörünü bağlayın (henüz güç vermeyin). Ortadaki mavi renkli USB bağlantı noktalarına bağlanmaktan kaçının. Bunlar USB 3'tür. Sürücü USB 3 özellikli (daha güvenilir) olsa bile USB 2 bağlantı noktasını kullanın.


![image](assets/12.webp)


Mikro SD kart buraya takılır:


![image](assets/13.webp)


Son olarak, gücü bağlayın:


![image](assets/14.webp)


## Adım 6: Pi'nin IP Address'unu bulun


Raspiblitz ile asla bir monitöre ihtiyacınız olmaz. Ancak ev ağında başka bir bilgisayara ihtiyacınız var. Pi'niz ethernet ile bağlı değilse ve WiFi'ye güvenmek istiyorsanız, IP'yi bulmak bazı bilgisayar becerileri gerektirir. Size yardımcı olamam, üzgünüm. Bir ethernet bağlantısına ihtiyacınız var. (Sorun, WiFi'ye bağlanmak ve bir şifre girmek için bir monitöre ve işletim sistemine erişime ihtiyaç duymanızdan kaynaklanıyor)


Bağlı tüm cihazların IP'lerinin bir listesi için yönlendiricinizi kontrol edin.


Tarayıcıya 192.168.0.1 yazdım (yönlendiricimle birlikte gelen talimatlar), oturum açtım ve cihazımı 192.168.0.191 IP adresiyle görebildim. Bu IP adreslerinin internete açık olmadığını unutmayın (önce yönlendiriciden geçerler), bunlar sadece ev ağınızdaki cihazlar için tanımlayıcılardır.


IP'yi bulmak çok önemlidir.


**Not:** "arp -a" komutunu kullanarak ev ağındaki tüm Ethernet bağlantılı cihazların IP Address'ini bulmak için bir Mac veya Linux makinesinde terminali kullanabilirsiniz. Çıktı, yönlendiricinin göstereceği kadar güzel değildir, ancak ihtiyacınız olan tüm bilgiler oradadır. Eğer Pi'nin hangisi olduğu belli değilse, deneme yanılma yöntemini kullanın.


## Adım 7: Pi'ye SSH ile bağlanın


Açmadan önce SD kartı Pi'ye takmayı unutmayın. Birkaç dakika bekleyin ve ardından başka bir Linux/Mac'te terminali açın.


Mac/Linux için, terminalde şunu yazın:


```bash
ssh admin@You_Pi's_IP_address
```


Windows için, Pi'ye ssh yapmak için putty yüklemeniz gerekir. Yukarıdaki komutun aynısını yazın.


Bunu ilk kez yaptığınızda veya SD kartı değiştirerek Pi'nin işletim sistemini her değiştirdiğinizde, bu hatayı alabilir veya almayabilirsiniz..


![image](assets/15.webp)


Bunu düzeltmenin yolu "known_hosts" dosyasının olduğu yere gitmek (hata mesajında size söyler) ve onu silmektir. Komut "rm known_hosts"


Ardından, oturum açmak için ssh komutunu tekrarlayın. Bu gerçekleşecek..


![image](assets/16.webp)


Devam etmek için evet (tam kelime) yazın.


Başarılı olursa, sizden bir şifre istenecektir. Bu bilgisayarınız için değil, raspiblitz içindir. Genel şifre "raspiblitz" dir ve bunu daha sonra değiştireceksiniz. Terminal penceresi maviye dönecek ve eski DOS menüleri gibi menü seçeneklerine sahip olacaksınız. Ok tuşları ya da fare ile gezinin.


![image](assets/17.webp)


Komutları izleyin, şifrelerinizi ayarlayın ve ardından Hard sürücünüzü algılayacak ve gerekirse biçimlendirme seçeneği sunacaktır.


Ardından Blockchain verilerini başka bir kaynaktan kopyalamak mı yoksa yeniden indirmek mi istediğiniz sorulacaktır. Kopyalamak bir öğrenme sürecidir ve talimatlar oldukça iyidir ve el altında tutulması iyidir....


![image](assets/18.webp)


Basit ama daha yavaş bir yol ise tüm zinciri sıfırdan indirmektir..


![image](assets/19.webp)


Terminal ekranında bir sürü metin yanıp sönecektir. Bunu Blockchain indirme işlemi sanabilirsiniz, ancak bana göre iletişim için özel bir anahtar oluşturuyor gibi görünüyor.


Ardından şimşek seçenekleri görünür.


![image](assets/20.webp)


Aydınlatma Wallet'inizi kilitlemek için yeni bir şifre oluşturun, ardından yeni bir Wallet oluşturulacak ve size yazmanız için 24 kelime verilecektir..


![image](assets/21.webp)


Yazdığınızdan ve güvenli bir yerde sakladığınızdan emin olun. Yıldırım kullanmayı planlamadığı için bunu yapmayan, ancak bir yıl sonra kullanmaya karar veren ve kanalları açan bir kişi duydum. Daha sonra kelimelerinin yedeklenmediğini fark etmiş ve hatırladığım kadarıyla kelimeleri cihazdan tekrar çıkarmanın mümkün olmadığını fark edince tüm kanallarını kapatıp yeniden başlamak zorunda kalmış. O paçayı kurtardı ama diğerleri bu kadar şanslı olmayabilir.


Bunu takiben, terminal penceresinde birkaç dakikalık bir metin kayar. Sonra..


![image](assets/22.webp)


Ssh oturumundan çıkış yapacaksınız. Tekrar giriş yapın, bu sefer yeni şifrenizle, şifre A. Giriş yaptıktan sonra lightning Wallet'nızın kilidini açmak için şifre C sorulacaktır.


Şimdi bekleyeceğiz. 2 hafta sonra görüşürüz. Terminali kapatabilirsiniz, Pi'ye hiçbir şey yapmaz, sadece bir iletişim penceresidir.


![image](assets/23.webp)


Herhangi bir nedenle, Blockchain indirmeyi bitirmeden önce Pi'yi kapatmak isterseniz, bunu düzgün bir şekilde yaptığınız sürece sorun olmaz. Yeniden bağlandığınızda Blockchain kaldığı yerden indirmeye devam edecektir.


Mavi ekrandan çıkmak için CTRL+c tuşlarına basın. Pi'nin Linux terminaline erişiyor olacaksınız. Burada "menu" yazarak aşağıdaki ekranı yükleyebilir ve buradan Pi'yi kapatabilirsiniz.


![image](assets/24.webp)


Rehberin sonu


Artık node si'niz kullanıma hazır. Hala daha fazla seçenekte gezinmeye yardımcı oluyorsanız, daha fazla öğretici ve rehber için github'a bakın https://github.com/raspiblitz/raspiblitz#feature-documentation