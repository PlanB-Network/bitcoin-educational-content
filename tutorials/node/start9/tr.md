---
name: Start9

description: Start9 özel sunucu kurma hakkında öğretici

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*İşte size bir Start9 / StartOS kişisel sunucusunun nasıl kurulacağını ve kullanılacağını ve bir bitcoin düğümünün nasıl çalıştırılacağını gösteren bir video kılavuzu olan Southern Bitcoiner'dan bir video eğitimi.*


## 1️⃣ Giriş


### Start9 tam olarak nedir?


Start9, 2020 yılında kurulan ve en çok [**StartOS**,](https://github.com/Start9Labs/start-os) kişisel sunucular için tasarlanmış Linux tabanlı bir işletim sistemi geliştirmesiyle tanınan bir şirkettir. Kullanıcıların Bitcoin ve Lightning düğümleri, mesajlaşma uygulamaları veya parola yöneticileri gibi çok çeşitli yazılım hizmetlerini kolayca kendi kendilerine barındırmalarını sağlarken, verileri üzerinde tam kontrol sahibi olmalarını ve merkezi teknoloji platformlarına olan bağımlılığı ortadan kaldırmalarını sağlar. StartOS kullanıcı dostu, tarayıcı tabanlı bir arayüze, hizmetlerin yüklenmesi için seçilmiş bir Marketplace'e ve Tor entegrasyonu ve sistem genelinde HTTPS şifreleme gibi yerleşik gizlilik araçlarına sahiptir. Start9 ayrıca işletim sistemi ile önceden yüklenmiş donanım cihazları da sağlıyor, ancak yazılım uyumlu donanımlara veya sanal makinelere (VM'ler) kurulabiliyor.


### Hangi seçenekler mevcut?


Start9 hem önceden oluşturulmuş hem de kendin yap dağıtım seçenekleri sunmaktadır. Server One**](https://store.start9.com/collections/servers/products/server-one) ve [**Server Pure** ](https://store.start9.com/collections/servers/products/server-pure) yüksek performanslı bileşenlere sahip resmi donanım cihazlarıdır: Server One, yapılandırılabilir RAM (16GB-64GB) ve depolama (2TB-4TB NVMe SSD) özelliklerine sahip bir **AMD Ryzen 7 5825U** işlemci kullanırken, Server Pure, yine yapılandırılabilir RAM ve depolama seçenekleri sunan bir **Intel i7-10710U** ile donatılmıştır. Her ikisi de doğrudan Start9'dan satın alındığında **ömür boyu teknik destek** içerir. Esnekliği tercih eden kullanıcılar için StartOS, dizüstü bilgisayarlar, masaüstü bilgisayarlar, mini PC'ler ve tek kartlı bilgisayarlar dahil olmak üzere çok çeşitli mevcut donanıma veya VM'lere ücretsiz olarak kurulabilir.


![image](assets/en/01.webp)


### Umbrel ile arasındaki farklar nelerdir?


StartOS ve Umbrel'in her ikisi de kendi kendine barındırılan hizmet kurulumunu basitleştirir ancak mimari ve özellikler açısından farklılık gösterir. Umbrel, Debian/Ubuntu sistemlerinde veya VM'lerde bir uygulama katmanı olarak çalışırken, Start9 doğrudan donanım veya VM kurulumu gerektiren özel bir işletim sistemidir. Umbrel cilalı, macOS'tan ilham alan bir arayüze sahipken, Start9 işlevsel, minimal bir tasarıma öncelik veriyor. Umbrel daha geniş bir [uygulama seçimi](https://apps.umbrel.com/) sunarken, [Start9 Marketplace](https://marketplace.start9.com/) gelişmiş teknik yeteneklerle bunu telafi ediyor. Start9, onaylanmış kullanıcı arayüzü formları aracılığıyla gelişmiş ayarlara erişimi basitleştirerek komut satırı etkileşimi ihtiyacını azaltır. Ayrıca, Umbrel'in yerel olarak sahip olmadığı bir özellik olan tek tıklamayla şifrelenmiş sistem yedeklemeleriyle yedekleme yönetiminde de üstündür. StartOS yerleşik izleme araçları sağlar ve yerel ağ erişimi için HTTPS şifrelemesini zorlayarak güvenliği artırır. Umbrel yerel olarak şifrelenmemiş HTTP kullanır, ancak her iki platform da Tor üzerinden güvenli uzaktan erişimi destekler. Umbrel, zengin bir uygulama ekosistemine ve gösterişli bir kullanıcı arayüzüne öncelik veren kullanıcılar için uygundur. Start9, komut satırı uzmanlığı gerektirmeden güvenlik, yapılandırılabilirlik, yedekleme güvenilirliği ve gelişmiş hizmet yönetimine değer verenler için güçlü bir seçimdir. Umbrel ve Start9 ile arasındaki farklar hakkında daha fazla bilgi edinmek için lütfen bu kursu ziyaret edin:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ DIY Önkoşulları: Minimum ve Önerilen Özellikler


Minimum hizmetlerle temel kullanım için **minimum özellikler** şunlardır: **1 vCPU çekirdeği (2.0GHz+ boost), 4GB RAM, 64GB depolama** ve bir Ethernet portu. Bununla birlikte, özellikle bir Bitcoin Node çalıştırıyorsanız, bunun ötesine geçmenizi tavsiye ederim. Şahsen ben 1TB ile başladım ve kısa sürede alanım tükendi. En iyisi **dört çekirdekli CPU (2.5GHz+)** ve **8GB+ RAM** ile birlikte **en az 2TB depolama alanı** hedefleyin. Performans ve uzun ömürlülük açısından büyük bir fark yaratır. Derinlere dalmak istiyorsanız, [StartOS Çalıştırabilen Donanım] (https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229) hakkında güncel bir topluluk başlığı.


## 3️⃣ Ürün Yazılımının İndirilmesi ve Yanıp Söndürülmesi


Kuruluma başlamak için ayrı bir bilgisayar kullanarak [Start9 web sitesini] (https://start9.com/) ziyaret edin ve `DOCS` seçeneğine tıklayarak dokümantasyon bölümüne gidin. Buradan, StartOS'un uygun sürümünü bulmak için `Flashing Guides'a erişin. İki seçenek mevcuttur:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Bu eğitim `x86/ARM` seçeneğini kapsamaktadır.


En son işletim sistemi sürümü [Github sürüm sayfası](https://github.com/Start9Labs/start-os/releases/latest) adresinden indirilebilir. yeni özellikleri test etmek isteyen kullanıcılar için [Pre-release](https://github.com/Start9Labs/start-os/releases) sürümleri de mevcuttur. Sayfanın alt kısmında, `Assets` altında, `x86_64` veya `x86_64-nonfree.iso` dosyasını indirin.  X86_64-nonfree.iso` imajı, Server One ve çoğu DIY donanımı için, özellikle grafik ve ağ aygıtı desteği için gerekli olan ücretsiz olmayan (kapalı kaynaklı) yazılımı içerir.


SHA256 hash'ini GitHub'da listelenenle karşılaştırarak dosyanın bütünlüğünü doğrulamanız önerilir. Linux için `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso` komutu kullanılabilir, diğer işletim sistemleri belgelerde ele alınmıştır.


StartOS görüntüsünü indirip doğruladıktan sonra, bir USB sürücüye flaşlanmalıdır. bu görev için `BalenaEtcher` önerilen bir yazılımdır. İşletim sistemi imaj dosyalarını USB sürücülere ve SD kartlara yazmak için ücretsiz, açık kaynaklı bir araçtır ve Windows, macOS ve Linux için kullanılabilir. Resmi [Balena Etcher web sitesinden] (https://www.balena.io/etcher/) uygun sürümü indirin ve yükleyiciyi çalıştırın. Hedef USB sürücüsünü veya SD kartı bağlayın, Balena Etcher'ı açın ve indirilen işletim sistemi görüntüsünü seçmek için `Dosyadan Flash'a tıklayın. Etcher bağlı sürücüleri otomatik olarak algılayacaktır; birden fazla varsa doğru hedefi seçin. Görüntüyü yazmaya başlamak için `Flash!` seçeneğine tıklayın. Etcher tamamlandığında yazma işlemini otomatik olarak doğrular. Tamamlandığında, sürücüyü güvenli bir şekilde çıkarın ve cihazı önyüklemek için kullanın.


![image](assets/en/19.webp)


## 4️⃣ İlk Kurulum


İlk kurulum için, `KULLANICI KILAVUZU` altındaki Start9 [dokümantasyon] (https://docs.start9.com/0.3.5.x/) sayfasına ve ardından `Getting Started - Initial Setup` bölümüne bakın.  En güncel bilgiler için bu resmi kılavuza başvurulmalıdır.


İki seçenek sunulmuştur:



- Yeni Başlayın
- Kurtarma Seçenekleri


Yeni bir sunucu kurulumu için `Yeni Başla` seçeneğini seçin. İlk olarak, sunucuyu güce ve bir Ethernet kablosuna bağlayın. Kurulum için kullanılan bilgisayarın aynı yerel ağ üzerinde olduğundan emin olun. Yeni flaşlanmış USB sürücüsünü bilgisayardan çıkarın ve sunucuya takın.


Sunucuyu aynı ağ üzerindeki herhangi bir bilgisayardan uzaktan kontrol edebilirsiniz. Bir web tarayıcısı açın ve `http://start.local` adresine gidin.


**Not**: Bu adresle bağlantı sorunları yaşanırsa, bunun nedeni genellikle ev ağlarının `.local` alan adlarını çözümleyememesidir. Sorun, sunucuya doğrudan IP adresi üzerinden erişilerek çözülebilir. IP, yönlendiricinin yönetici arayüzünde (genellikle `192.168.1.1` veya benzer bir adreste) oturum açarak ve cihazı DHCP istemcileri veya ağ haritası listesinde bularak bulunabilir. Ardından, tarayıcıya tam IP adresini (örneğin `http://192.168.1.105`) girin. Bu, DNS çözümlemesini atlar. Sorunlar devam ederse, [Yaygın Sorunlar sayfasına](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) veya [destek birimlerine ulaşın](https://start9.com/contact/) başvurun


StartOS kurulum ekranı görünmelidir. Yeni sunucu kurulumuna başlamak için `Yeni Başla` seçeneğine tıklayın.


![image](assets/en/03.webp)


Bir sonraki adım StartOS verilerinin depolanacağı depolama sürücüsünü seçmektir.


![image](assets/en/04.webp)


Sunucu için güçlü bir `Şifre` belirleyin. Start9 tarafından tavsiye edildiği gibi kaydedin ve ardından `BİTİR`e tıklayın.


![image](assets/en/05.webp)


Bir ekran StartOS'un başlatıldığını ve sunucunun kurulduğunu gösterecektir. Bir sonraki adım, `start.local` adresi yalnızca kurulum amaçlı olduğundan ve daha sonra çalışmayacağından, `Adres bilgisini indirin`.


![image](assets/en/06.webp)


Yapılandırma dosyası iki kritik erişim adresi içerir: biri `yerel ağ (LAN)` için ve diğeri `Tor` üzerinden güvenli erişim için. Her iki adres de güvenli bir parola yöneticisine kaydedilmelidir. Bir sonraki adım `Root CA`nıza güvenmek`tir. Yeni bir tarayıcı sekmesi açın ve Kök CA'ya güvenmek ve oturum açmak için talimatları izleyin. Kök CA sertifikası, indirilen dosyadaki `Sertifikayı indir` seçeneğine tıklanarak da indirilebilir.


## 5️⃣ Kök CA'nıza güvenin


Sertifikayı indirdikten sonra, sunucunun `Root CA`sına işletim sistemi tarafından güvenilmelidir. Talimatları Görüntüle'ye tıklayın ve belirli işletim sistemi için yönergeleri bulun.


![image](assets/en/07.webp)


Bir Linux sistemi için aşağıdaki komutlar kullanılır. Öncelikle bir Terminal açın ve gerekli paketleri yükleyin:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Sertifikanın indirildiği dizine gidin, tipik olarak `~/Downloads` . Sertifikayı işletim sisteminin güven deposuna eklemek için bu komutları yürütün. İndirilenler klasörüne `cd ~/Downloads` ile geçin. Gerekli dizini `sudo mkdir -p /usr/share/ca-certificates/start9` ile oluşturun. Sertifika dosyasını `sudo cp "your-filename.crt" /usr/share/ca-certificates/start9/` kullanarak `your-filename.crt` yerine gerçek dosya adını yazarak kopyalayın. Yolunu sistem yapılandırmasına `sudo bash -c "echo 'start9/your-filename.crt' >> /etc/ca-certificates.conf"` ile ekleyerek sertifikayı kalıcı olarak kaydedin. Son olarak, `sudo update-ca-certificates` ile güven deposunu yeniden oluşturun. Bu komutları çalıştırmadan önce gerçek sertifika dosya adını kullanmak ve tüm yolları doğrulamak çok önemlidir. Bu işlem Start9 sunucusunun HTTPS bağlantıları için kalıcı güven oluşturur.


Başarılı bir kurulum `1 eklendi` şeklinde bir çıktı ile belirtilecektir. Çoğu uygulama daha sonra `https` üzerinden güvenli bir şekilde bağlanabilecektir. Firefox kullanıyorsanız, ek bir [son adım](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff) gereklidir. Chrome veya Brave için, tarayıcıyı Kök CA'ya saygı gösterecek şekilde yapılandırmak için farklı bir [son adım](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) gereklidir. Sayfayı yenileyerek bağlantıyı test edin. Sorun devam ederse, sayfayı tekrar ziyaret etmeden önce tarayıcıdan çıkın ve yeniden açın.


![image](assets/en/08.webp)


## 6️⃣ StartOS ile Başlarken


Şimdi güvenli bir HTTPS bağlantısı kullanarak oturum açmak mümkün olmalıdır. Hoş Geldiniz Ekranı`na erişmek için `Şifre`yi girin.


![image](assets/en/09.webp)


Bu ekran, başlangıç için faydalı kısayollar sağlar. Sol kenar çubuğu navigasyon için ana menü öğelerini içerir.


## 7️⃣ Sistem


StartOS'taki Sistemler sekmesi, kişisel sunucuyu yönetmek için temel sistem işlevlerine erişim sağlar. Komut satırı uzmanlığı gerektirmeden sistem bakımı, güvenlik, tanılama ve yapılandırma için araçlar sunar.


Yedeklemeler' bölümü, hizmetler, yapılandırmalar ve veriler dahil olmak üzere daha sonra geri yüklenebilecek tam sistem yedeklerinin oluşturulmasına olanak tanır. Bu, felaket kurtarma veya yeni donanıma geçiş için gereklidir. Yedekler harici sürücülerde saklanabilir ve ana parola kullanılarak şifrelenir.


Sistemler sekmesindeki `Yönet` bölümü, temel sistem işlevleri üzerinde kontrol sağlar. Kullanıcılar StartOS güncellemelerini manuel olarak kontrol edebilir ve uygulayabilir, böylece sistem güncelleme süreci üzerinde kontrol sağlayabilirler. Resmi pazarda bulunmayan özel veya üçüncü taraf hizmetleri yandan yüklemek mümkündür. Sunucu Ethernet üzerinden bağlı değilse, Wi-Fi ayarları bu bölümden yapılandırılabilir. İleri düzey kullanıcılar terminal düzeyinde sistem yönetimi için SSH erişimini etkinleştirebilir.


![image](assets/en/10.webp)


Analizler bölümü, sunucunun performansının ve sağlığının gerçek zamanlı olarak izlenmesini sağlayarak CPU, RAM ve disk kullanımını grafiklerle gösterir. Ayrıca Raspberry Pi gibi aktif soğutması olmayan cihazlar için faydalı olan sistem sıcaklığını da gösterir. Çalışma süresi ve yük ortalaması ölçümleri sistem kararlılığını değerlendirmeye yardımcı olur ve hizmet veya sistem sorunlarını gidermek için canlı günlükler mevcuttur.


Destek' bölümü yerleşik SSS'lere, resmi belgelere ve topluluk destek kanallarına erişim sunar. Hata ayıklama günlükleri, daha hızlı sorun çözümü için Start9 desteği ile paylaşmak üzere bu bölümden indirilebilir.


![image](assets/en/11.webp)


## 8️⃣ Marketplace


Pazar yeri, kişisel sunucu üzerindeki hizmetleri keşfetmek, kurmak ve yönetmek için kullanılır. Bitcoin Core, BTCPay Server ve electrs gibi yazılımlara erişim sağlar. StartOS, resmi Start9 Kayıt Defteri ve topluluk tarafından işletilen kayıt defterleri dahil olmak üzere birden fazla pazar yerini destekler. Bunlar, `DEĞİŞTİR` seçeneğine tıklanarak ve daha geniş bir hizmet yelpazesine erişim sağlayan `Topluluk Kayıt Defteri`ne geçilerek eklenebilir.


![image](assets/en/12.webp)


## 9️⃣ Bitcoin Tam Düğümün Kurulması


StartOS üzerine bir Bitcoin full node kurmak, Bitcoin deneyimi üzerinde tam egemenlik sağlar. İşlemlerin doğrulanmasını sağlar ve etkinliği günlüğe kaydedebilecek harici hizmetlere olan bağımlılığı ortadan kaldırarak gizliliği ve güvenliği artırır. İşlemler üzerinde tam kontrol elde edilir ve bunların doğrudan ağa yayınlanmasına izin verilir. Varsayılan seçenek, StartOS ile yerel olarak entegre olan ve kendi kendini saklama kurulumu için Spectre, Sparrow veya Electrum gibi cüzdanlarla bağlantıya izin veren `Bitcoin Core`dur. Alternatif bir seçenek olan `Bitcoin Knots`, Topluluk Kayıt Defteri aracılığıyla da kullanılabilir.


Bitcoin Core'u yüklemek için Marketplace'e gidin. Varsayılan kayıt defterinin altında Bitcoin Core hizmetini bulun ve yükleyin. Kurulumdan sonra, hizmetin çalışabilmesi için ayarların tamamlanmasını gerektiren bir `Needs Config` istemi görünecektir. Bu genellikle güncellemelerden veya yeni kurulumlardan sonra ortaya çıkar ve `RPC ayarlarının` gözden geçirilmesini ister. Varsayılan yapılandırma ile devam edin ve `Kaydet` seçeneğine tıklayın.


![image](assets/en/13.webp)


Tamamen senkronize edildikten sonra, node'unuz Sparrow gibi cüzdanlar için özel bir arka uç olarak hizmet verebilir ve gelişmiş gizlilik ve işlem doğrulaması sağlar. Ancak, önemli miktarlarda para depolayan kullanıcılar için bu doğrudan bağlantının güvenlik dengelerini anlamak çok önemlidir. Bir wallet doğrudan Bitcoin Core'a bağlandığında, Bitcoin Core açık anahtarları (xpubs) ve wallet bakiyelerini ana makinede şifrelenmemiş olarak sakladığından hassas verileri açığa çıkarabilir. Güvenliği ihlal edilmiş bir sistem, bir saldırganın varlıklarınızı keşfetmesine ve sizi hedef almasına izin verebilir.


Bu riski azaltmak ve daha sağlam bir güvenlik modeli elde etmek için bir Özel Electrum Server kurabilirsiniz. Bu sunucu, wallet'ye özgü herhangi bir bilgiyi depolamadan blok zincirini indeksleyen bir aracı görevi görür. wallet'nizi doğrudan Bitcoin Core yerine kendi Electrum sunucunuza bağlayarak, wallet'nin node'un hassas verilerine erişmesini engellemiş olursunuz.


![image](assets/en/14.webp)


## 🔟 Elektrikleri ayarlayın


electrs` (Electrum Rust Sunucusu), Bitcoin Çekirdek düğümünüze bağlanan ve Electrum uyumlu cüzdanların işlem geçmişini ve bakiyelerini gerçek zamanlı olarak sorgulamasını sağlayan hızlı, verimli bir dizinleyicidir. StartOS üzerinde electrs çalıştırarak, üçüncü taraf Electrum sunucularına olan bağımlılığı ortadan kaldırır, gizliliği ve güvenliği önemli ölçüde artırırsınız - wallet sorgularınız doğrudan kendi barındırdığınız düğüme gider.


Kurmak için önce StartOS Marketplace'ten electrs hizmetini yükleyin. Sistem, devam etmeden önce Bitcoin Core'un tamamen senkronize edilmesini gerektirecektir. Kurulumdan sonra, `Needs Config` ayarlarını önerilen varsayılanlarla onaylayın ve electrs, donanımınıza bağlı olarak bir güne kadar sürebilecek blok zincirini indekslemeye başlar.


![image](assets/en/15.webp)


Tamamlandığında, Sparrow veya Spectre gibi cüzdanları bağlayabilirsiniz. Başarılı bir bağlantı, wallet'inizin doğrudan node'unuzla senkronize olmasını sağlayarak güvenli, özel ve kendi kendine barındırılan bir Bitcoin deneyimi sunar.


## 1️⃣1️⃣ Connect Sparrow Wallet


Electrs uygulamasını kullanarak `Sparrow Wallet`i StartOS düğümünüze bağlamak için öncelikle Bitcoin Core'un tamamen senkronize olduğundan ve electrs'in kurulu ve çalışır durumda olduğundan emin olun. Cihazınızda Sparrow Wallet`i açın ve `Dosya` -> `Ayarlar` -> `Sunucu` bölümüne gidin. Ardından `Özel Electrum Server`i seçin. URL alanına, StartOS'ta `Services` -> `electrs` -> `Properties` (genellikle `.onion:50001` ile biten) altında bulabileceğiniz electrs için `Tor hostname` ve `Port` girin.


![image](assets/en/16.webp)


Ardından, `Proxy Kullan` seçeneğini işaretleyip proxy adresini `127.0.0.1` ve bağlantı noktasını `9050` olarak ayarlayarak Tor'u etkinleştirin. Bağlantıyı Test Et` seçeneğine tıklayın ve birkaç dakika bekleyin. Başarılı bir bağlantı `Connected to electrs` gibi bir onay mesajı gösterecektir. Doğrulandıktan sonra ayarları kapatın ve wallet'nizi oluşturmaya veya geri yüklemeye devam edin. Bu kurulum, wallet'nizin electrs aracılığıyla kendi düğümünüzü sorgulamasını sağlayarak tam gizlilik ve güvensiz çalışma sağlar.


![image](assets/en/17.webp)


## 🎯 Sonuç


StartOS by Start9, Bitcoin ve Lightning düğümleri, cüzdanlar ve kişisel uygulamalar gibi temel hizmetleri kendi kendine barındırmak için tasarlanmış kullanıcı dostu, gizlilik odaklı bir platformdur. Temiz bir grafik arayüz, otomatik yedeklemeler, sağlık izleme ve güvenli Tor erişimi sunarak komut satırı becerilerine olan ihtiyacı ortadan kaldırır, bu da onu teknik olmayan kullanıcılar için ideal hale getirir. Modüler mimarisi, electrs veya Sparrow gibi araçlarla sorunsuz entegrasyonu destekleyerek finansal ve dijital egemenliğiniz üzerinde tam kontrol sahibi olmanızı sağlar. Şeffaflık, yerel kontrol ve genişletilebilirliğe güçlü bir şekilde odaklanan StartOS, kullanıcılara merkezi platformlardan mülkiyeti geri alma ve kendi özel, esnek altyapılarını çalıştırma yetkisi verir.