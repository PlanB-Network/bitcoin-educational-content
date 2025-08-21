---
name: Linux Mint

description: Bitcoin işlemleri için bir bilgisayar ayarlayın
---

![image](assets/cover.webp)


## Normal bir bilgisayar kullanıyorsanız sorun nedir?


Bitcoin işlemleri yaparken, bilgisayarınızda kötü amaçlı yazılım olmaması idealdir. Açıkçası.


Bitcoin seed ifadenizi (genellikle 12 veya 24 kelime) bir imzalama cihazıyla (örneğin bir Hardware Wallet - asıl amacı) bilgisayardan uzak tutarsanız, "temiz" bir bilgisayara sahip olmanın o kadar da önemli olmadığını düşünebilirsiniz - doğru değil.


Kötü amaçlı yazılım bulaşmış bir bilgisayar Bitcoin adreslerinizi okuyarak bakiyenizi bir saldırgana ifşa edebilir - sadece Address'i bilerek Bitcoin'yı alamazlar, ancak ne kadar paranız olduğunu görebilir ve buradan değerli bir hedef olup olmadığınızı hesaplayabilirler. Ayrıca, örneğin nerede yaşadığınızı bir şekilde öğrenebilir ve fidye ödemenizi sağlamak için sizden tırnaklarınızı ya da çocuklarınızı alabilirler.


## Çözüm nedir?


Çoğu Bitcoin kullanıcısını Bitcoin işlemleri yapmak için kötü amaçlı yazılım içermeyen (internet erişimi olan) özel bir bilgisayar kullanmaya teşvik ediyorum. İnsanlara Linux Mint gibi açık kaynaklı bir işletim sistemi kullanmalarını öneririm, ancak mecbursanız Windows veya Mac kullanın - bu, her zaman içinde kötü amaçlı yazılım gizlenmiş olan normal, iyi kullanılmış bir bilgisayar kullanmaktan daha iyidir.


İnsanların karşılaştığı engellerden biri, bu tür bilgisayarlara yeni bir işletim sistemi yüklemektir. Bu kılavuz bu konuda yardımcı olacaktır.


Birçok Linux çeşidi var ve ben birkaçını denedim. Bitcoin kullanıcıları için tavsiyem Linux Mint, çünkü kurulumu kolay, çok hızlı (özellikle açılış ve kapanışta), şişirilmemiş (her ekstra yazılım bir risktir) ve nadiren çöktü ya da garip davrandı (Ubuntu ve Debian gibi diğer sürümlerle karşılaştırıldığında).


Bazıları Windows veya Mac OS'u tercih ederek yeni bir işletim sistemine karşı çok dirençli olabilir. Anlıyorum, ancak Windows ve Apple işletim sistemleri kapalı kaynak kodlu, bu nedenle yaptıklarına güvenmek zorundayız; bunun iyi bir politika olduğunu düşünmüyorum, ancak ya hep ya hiç değil. İnsanların iyi kullanılmış (kim bilir üzerinde hangi kötü amaçlı yazılımlar birikmiş) bir bilgisayar yerine yeni yüklenmiş özel bir Windows veya Mac OS bilgisayar kullanmasını tercih ederim. Bir adım daha iyisi, yeni kurulmuş bir Linux bilgisayar kullanmaktır ki ben de bunu göstereceğim.


Bilinmeyenler nedeniyle Linux kullanma konusunda gerginseniz, bu doğaldır, ancak öğrenmek için biraz zaman harcamak da öyle. İnternette çok fazla bilgi mevcut. Burada komut satırının temellerini tanıtan mükemmel bir kısa video var, şiddetle tavsiye ederim.

Bir bilgisayar seçin


En iyi seçenek olduğunu düşündüğüm şeyle başlayacağım. Daha sonra alternatifler hakkında görüşlerimi bildireceğim.


İdeal seçenek:


Benim tavsiyem, eğer paranız yetiyorsa ve Bitcoin yığınınızın boyutu bunu haklı çıkarıyorsa, yepyeni bir giriş seviyesi dizüstü bilgisayar almanızdır. Bugünlerde üretilen en temel model, kullanılacağı işi halletmek için yeterince iyidir. İşlemci ve RAM özellikleri önemli değildir, çünkü hepsi yeterince iyi olacaktır.


Kaçın:



- Surface Pro dahil herhangi bir tablet kombinasyonu
- Chromebook'lar - genellikle depolama kapasitesi çok düşüktür
- EMMC sürücüsü olan herhangi bir bilgisayar; SSD sürücüsü varsa, bu mükemmeldir
- Mac'ler - pahalıdırlar ve benim deneyimlerime göre donanımları Linux işletim sistemleriyle iyi uyum sağlamıyor
- Yenilenmiş veya 2. el herhangi bir şey (yine de mutlak bir anlaşma kırıcı değil)


Bunun yerine, bir Windows 11 dizüstü bilgisayar arayın (Şu anda Windows 11 en son sürümdür. Bu yazılımdan kurtulacağız, merak etmeyin). Amazon.com'da "Windows 11 Laptop" diye arattım ve bu güzel örneği buldum:


![image](assets/1.webp)


Yukarıdaki bu ürünün fiyatı iyi. Özellikleri yeterince iyi. QR kodlu PSBT işlemleri için kullanabileceğimiz dahili bir kamerası var (aksi takdirde bunu yapmak için bir USB kamera satın almanız gerekir). Tanınmış bir marka olmaması konusunda endişelenmeyin (ucuz). Daha iyi bir marka istiyorsanız, size pahalıya mal olacaktır, örn:


![image](assets/2.webp)


Daha ucuz olanların bazılarında yalnızca 64 Gb sürücü alanı var; bu kadar küçük sürücülü dizüstü bilgisayarları test etmedim - 64 Gb olması muhtemelen sorun değil, ancak zorluyor olabilir.


## Diğer seçenekler - Kuyruklar


Tails, bir USB flash sürücüden önyükleme yapan ve herhangi bir bilgisayarın donanımını geçici olarak devralan bir işletim sistemidir. Yalnızca Tor bağlantılarını kullanır, bu nedenle Tor kullanırken rahat olmanız gerekir. Ayarları değiştirmediğiniz ve bir parola ile kilitlediğiniz kalıcı bir depolama seçeneği (USB başparmak sürücüsünde) oluşturmadığınız sürece, oturumunuz sırasında belleğe yazdığınız hiçbir veri sürücüye kaydedilmez (her seferinde yeni başlar).


Kötü bir seçenek değil ve ücretsiz, ancak bizim amacımız için biraz hantal. Üzerine yeni yazılım yüklemek hiç de kolay değil. Electrum ile birlikte gelmesi iyi bir özellik, ancak bunun dezavantajı, kendiniz yüklememiş olmanızdır. Kullandığınız USB sürücünün en az 8Gb olduğundan emin olun.


Tails kullanırsanız esnekliğiniz azalır. İhtiyacınız olanı kurmak ve düzgün çalışmasını sağlamak için çeşitli kılavuzları takip edemeyebilirsiniz. Örneğin, Bitcoin core'u kurmak için benim kılavuzumu takip ederseniz, çalışması için gerekli değişiklikler vardır. Tails'e özel bir rehber hazırlayacağımı sanmıyorum, bu nedenle becerilerinizi geliştirmeniz ve bunu tek başınıza yapmanız gerekir.


Ayrıca donanım cüzdanlarının bu işletim sistemi ile ne kadar iyi etkileşime gireceğinden emin değilim.


Tüm bunları söyledikten sonra, Bitcoin işlemleri için bir Tails bilgisayarı güzel bir ek seçenektir ve Tails kullanmayı öğrenmek için genel gizlilik becerilerinize kesinlikle yardımcı olacaktır.


## Diğer seçenekler - Canlı İşletim Sistemi Önyüklemesi


Bu, işletim sisteminin gizliliğe adanmamış olması dışında Tails'e çok benzer. Bunu kullanmanın temel yolu, seçtiğiniz Linux işletim sistemiyle bir USB sürücüsünü flaşlamak ve bilgisayarın dahili sürücü yerine bundan önyükleme yapmasını sağlamaktır. Bunun nasıl yapılacağı daha sonra açıklanmaktadır.


Avantajı, daha az kısıtlanmış olmanız ve işlerin gelişmiş ince ayarlar olmadan çalışacak olmasıdır.


Böyle bir sistemin mevcut bilgisayardaki kötü amaçlı yazılımları yeni işletim sistemini barındıran USB önyükleme sürücüsünden ne kadar iyi izole ettiğinden emin değilim. Muhtemelen iyi bir iş çıkarır ama muhtemelen Tails kadar iyi değildir. Bilmediğim için benim tercihim özel dizüstü bilgisayar.

Diğer seçenekler - Kendi kullanılmış dizüstü veya masaüstü bilgisayarınız


Kullanılmış bir bilgisayar kullanmak ideal değil, çünkü sofistike kötü amaçlı yazılımların iç işleyişini ve bir sürücüyü silmenin ondan kurtulmak için yeterli olup olmadığını bilmiyorum. Muhtemelen öyledir ama hain bilgisayar korsanlarının ne kadar zeki olabileceğini hafife almak istemiyorum. Siz karar verebilirsiniz, ben taahhütte bulunmak istemiyorum.


Eski bir dizüstü bilgisayar yerine eski bir masaüstü bilgisayar kullanmayı tercih ederseniz, muhtemelen nadir bulunan Bitcoin işlemleriniz için kalıcı olarak yer kaplaması dışında bu iyi olacaktır; başka bir şey için kullanmamalısınız. Oysa bir dizüstü bilgisayarla, onu bir kenara koyabilir ve hatta ekstra güvenlik için saklayabilirsiniz.


## Linux Mint'i herhangi bir bilgisayara yükleme


Bunlar yeni dizüstü bilgisayarınızdan herhangi bir işletim sistemini silmek ve Linux Mint yüklemek için talimatlardır, ancak hemen hemen her bilgisayara hemen hemen her Linux sürümünü yüklemek için uyarlayabilirsiniz.


İşletim sistemini bir çeşit bellek çubuğuna yüklemek için herhangi bir bilgisayar kullanacağız. USB portu ile uyumlu olduğu sürece hangi bellek olduğu önemli değildir ve en az 16 Gb olmasını öneririm.


Şunlardan bir tane al:


![image](assets/3.webp)


Ya da bunun gibi bir şey kullanabilirsiniz:


![image](assets/4.webp)


Ardından, linuxmint.com adresine gidin


![image](assets/5.webp)


Fareyi en üstteki İndir menüsünün üzerine getirin ve ardından "Linux Mint 20.3" bağlantısına veya bunu yaptığınız sırada önerilen en son sürüm neyse ona tıklayın.


![image](assets/6.webp)


Aralarından seçim yapabileceğiniz birkaç "tat" olacaktır. Bu kılavuzu takip etmek için "Cinnamon" ile devam edin. İndir düğmesine tıklayın.


![image](assets/7.webp)


Bir sonraki sayfada, aynaları görmek için aşağı kaydırabilirsiniz (Aynalar, istediğimiz dosyanın bir kopyasını tutan çeşitli sunuculardır). SHA256 ve gpg (önerilir) kullanarak indirmeyi doğrulayabilirsiniz, ancak bu konuda zaten kılavuzlar yazdığım için burada açıklamayı atlayacağım.


![image](assets/8.webp)


Size en yakın aynayı seçin ve bağlantısına tıklayın (ayna sütunundaki Green metni). Dosya indirilmeye başlayacaktır - benim indirdiğim sürüm 2.1 gigabayt.


İndirildikten sonra, dosyayı taşınabilir bir bellek aygıtına flaşlayabilir ve önyüklenebilir hale getirebilirsiniz. Bunu yapmak için en kolay yol Balena Etcher kullanmaktır. Eğer sahip değilseniz indirin ve kurun.


Sonra çalıştırın:


![image](assets/9.webp)


Dosyadan flash'a tıklayın ve indirdiğiniz LinuxMint dosyasını seçin.


Ardından Hedef seç'e tıklayın. Bellek aygıtının takılı olduğundan ve doğru sürücüyü seçtiğinizden emin olun, aksi takdirde yanlış sürücünün içeriğini yok edebilirsiniz!


Bundan sonra, Flash'ı seçin! Şifrenizi girmeniz gerekebilir. İşlem tamamlandığında, sürücü bir Linux aygıtına dönüştürüldüğü için muhtemelen Windows veya Mac bilgisayarınız tarafından okunamayacaktır. Sadece çekip çıkarın.

Hedef bilgisayarı hazırlama


Yeni dizüstü bilgisayarı açın ve açılırken BIOS tuşunu basılı tutun. Bu genellikle F2'dir, ancak F1, F8, F10, F11, F12 veya Delete olabilir. Anlayana kadar her birini deneyin ya da bilgisayarınızın modeli için internette arama yapın ve doğru soruyu sorun.


Örneğin "BIOS anahtarı Dell dizüstü bilgisayarlar".


Her bilgisayarın farklı bir BIOS menüsü olacaktır. Hangi menünün önyükleme sırasını yapılandırmanıza izin verdiğini araştırın ve bulun. Bizim amaçlarımız doğrultusunda, bilgisayarın dahili Hard sürücüsünden önyükleme yapmaya çalışmadan önce USB bağlantılı bir aygıttan (bağlı bir aygıt varsa) önyükleme yapmayı denemesini istiyoruz (aksi takdirde Windows yüklenecektir). Bunu ayarladıktan sonra, çıkmadan önce kaydetmeniz gerekebilir veya otomatik olarak kaydedebilir.


Bilgisayarı yeniden başlatın ve USB bellek aygıtından yüklenmesi gerekir. Linux'u dahili sürücüye yükleyemeyiz ve Windows temelli olarak kaldırılacaktır.


Aşağıdaki ekrana geldiğinizde, "OEM kurulumu (üreticiler için)" seçeneğini seçin. Bunun yerine "Linux Mint'i Başlat "ı seçerseniz, bellek aygıtından yüklenen bir Linux Mint oturumu elde edersiniz, ancak bilgisayarı kapattığınızda, bilgilerinizin hiçbiri kaydedilmez - bu temelde deneyebilmeniz için geçici bir oturumdur.


![image](assets/10.webp)


Size basit olması gereken bir dizi soru soracak olan grafiksel bir sihirbaz aracılığıyla yönlendirileceksiniz. Bunlardan biri Languange ayarları, diğeri ise ev internet ağ bağlantınız ve şifreniz olacaktır. Ek yazılım yüklemeniz istenirse, bunu reddedin. Kurulum türü ile ilgili soruya geldiğinizde, bazı insanlar tereddüt edebilir - "Diski sil ve Linux Mint'i kur" seçeneğini seçmeniz gerekir. Ayrıca, sürücüyü şifrelemeyin ve LVM'yi seçmeyin.


Sonunda masaüstüne ulaşacaksınız. Bu noktada, işiniz tam olarak bitmemiştir. Aslında üretici olarak hareket ediyorsunuz (yani bir bilgisayar üreten ve müşteri için Linux kuran biri). Sonlandırmak için masaüstü simgesi olan "Linux Mint Yükle "ye çift tıklamanız gerekiyor.


![image](assets/11.webp)


Bellek çubuğunu çıkarmayı ve ardından yeniden başlatmayı unutmayın. Yeniden başlatmanın ardından, işletim sistemini yeni bir kullanıcı olarak ilk kez kullanacaksınız. Tebrikler.


Yapılması gereken ilk şeylerden biri (ve düzenli olarak yapılması gereken), sistemi güncel tutmaktır.


Terminal uygulamasını açın ve aşağıdakileri yazın:


```bash
sudo apt-get update
```


<enter> tuşuna basın, seçiminizi onaylayın ve ardından bu komutu verin:


```bash
sudo apt-get upgrade
```


<enter> tuşuna basın ve seçiminizi onaylayın.


Bırakın işini yapsın, birkaç dakika sürebilir.


Ardından, Tor'u (büyük/küçük harfe duyarlı) yüklemek istiyorum:


```bash
sudo apt-get install tor
```


**Pro İpucu:** Linux Mint önyüklemesini "OEM yüklemesinden" de çalıştırabilirsiniz (İnternete bağlı olduğunuzdan emin olun, aksi takdirde hata alabilirsiniz). Bunu yaparsanız, daha sonra masaüstünde olması gereken "son kullanıcıya gönder" simgesine tıklamanız gerekir. Daha sonra bilgisayarı ilk kez açıyormuş gibi yeniden başlatır ve işletim sistemini başlatırsınız.


Bu kılavuzda, Bitcoin işlemleri için neden özel bir bilgisayara ihtiyaç duyabileceğiniz ve bu bilgisayara yeni bir Linux Mint işletim sisteminin nasıl kurulacağı açıklanmaktadır.