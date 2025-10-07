---
name: DietPi
description: Düşük performanslı makineler için optimize edilmiş hafif işletim sistemi. Kendi kendine barındırma tercihi ile
---

![cover](assets/cover.webp)



Teknik olmayan çevrelerde `Odroid`, `Raspberry Pi`, `Orange Pi` ya da `Radxa` gibi markalar pek bilinmez. Ancak tek bir anakart üzerine inşa edilmiş, yaygın olarak kullanılan bilgisayarlara kıyasla genellikle mikroskobik boyutta olan **SBC** bilgisayarların herhangi bir kişisel proje için destek olarak vazgeçilmez hale geldiğini görmek için teknoloji çevrelerine bakmak yeterlidir.



Bunlar çok çeşitli modellerde üretilen bilgisayarlardır. Tercihen, genellikle bu güçsüz makinelerde sorunsuz çalışacak şekilde uyarlanmış Linux dağıtımlarını barındırırlar.



**DietPi bir istisna değildir**: Debian tabanlı bir işletim sistemidir, mümkün olduğunca hafif olacak ve en düşük performanslı `SBC`yi bile çok hızlı hale getirecek şekilde optimize edilmiştir. Bu rehber yazılırken Debian12 Bookworm'dan Debian13 Trixie'ye geçildi, artık açık kaynaklı `RISC-V` işlemci tabanlı SBC'leri de destekliyor. DietPi daha fazla çalışmayı hak eden hoş bir keşif.



## Güçlü Yönler



Bu, küçük Raspberry tipi kartlar için Debian'ın "olağan kopyası" değildir. DietPi'dir:




- Hız ve hafiflik için optimize edilmiştir**: [SBC için diğer Debian dağıtımları ile karşılaştırma](https://dietpi.com/blog/?p=888), DietPi her şeyde daha hafiftir. DietPi ISO görüntüsü 1 GB'den daha hafiftir, Raspberry veya Orange PI'nin eski modellerine (örneğin) adanmış olanlar arasında açık ara en küçüğüdür. RAM ve CPU kaynaklarına olan talep çok düşüktür, böylece eski olanlar da dahil olmak üzere kartlardan her zaman en iyi şekilde yararlanır.
- Yerleşik otomasyonlar ve yükleyiciler**: Özel komutlardan oluşan bir paket, kullanıcıların sistem kaynaklarını izlemelerinin yanı sıra programları yüklemek ve başlatmak, sürümleri güncellemek, yedekleme yapmak ve tüm günlükleri kontrol etmek için görevleri otomatikleştirmelerine yardımcı olur.
- Güçlü, deney odaklı bir topluluk**: dietPi topluluğundan [tutorials](https://dietpi.com/forum/c/community-tutorials/8) ve projeler, DietPi sayesinde tek tıkla yükleyebileceğiniz yazılımlardan ilham almak için idealdir.



**SBC'nizden her bir parçayı sıkmak hiç bu kadar kolay olmamıştı**.



## Kendi kendine barındırma için otomasyonlar


Gelişmiş ağ çözümlerini çalıştırmak için kendi sunucunuzla denemeler yapmak veya Bitcoin uzmanlığınızı geliştirmek için araçlar mı istiyorsunuz? DietPi aradığınız çözüm olabilir. Birçok kişi kendi altyapısını nasıl yöneteceğini ve mükemmel yapılandırılmış ve korunan sunucuları nasıl çalıştıracağını bilse de, DietPi sıfırdan başlamak isteyenler için uygun bir adımdır.



DietPi, böyle bir görevin gerektirdiği tüm karmaşık görevleri manuel olarak gerçekleştirmek yerine, bunları bir `sihirbaz` ve kendi komut satırı ile oluşturmanıza olanak tanır. Burada kendi kişisel bulutunuz, _akıllı ev_ cihaz yönetimi, otomatik yedeklemeler ve crontab'ın yanı sıra daha gelişmiş çözümleri deneyebilirsiniz.



![img](assets/en/01.webp)



## Kurulum



### İndir



DietPi, işletim sistemini birçok farklı cihaza yazdırmak için sayısız ISO görüntüsü seti sunar. Bazıları yalnızca desteklenmektedir: örneğin Raspberry PI5 için ISO hala test aşamasındadır, ancak kartınız için uygun olanı kesinlikle bulabilirsiniz.



Bu kılavuz için ince bir istemciye kurmayı seçtim, bu yüzden seçim _PC/VM_ ve ardından _Native PC_'ye gitti. Bu cihazlar için önyükleyicinin oluşturulmasında farklılık gösteren iki ISO görüntüsü vardır. Eğitimde kullanılan makine oldukça eski, bu nedenle seçim _BIOS/CSM_ sürümüne gitti. Eğer daha yeni bir makineniz varsa, doğru sürüm `UEFI` olabilir.



![img](assets/en/02.webp)



Yükleyicinin `görüntüsünü`, `sha256` ve `İmzaları` içeren sayfaya ulaşacaksınız.



![img](assets/en/03.webp)



Günlük bilgisayarınızın `home` dizininde bir dizin hazırlayın, böylece gerekli dosyaları `wget` ile indirebilirsiniz.



![img](assets/en/04.webp)



Geliştiricinin açık anahtarı minimum araştırma gerektiriyordu, ancak bu bağlantıda bulabilirsiniz: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Dizinin içeriğini `ls -la` ile kontrol edin ve MichaIng anahtarını `gpg --import` ile anahtarlığınıza aktarın.



### Doğrulama ve flaş



Son olarak, en çok tavsiye ettiğim kısım: indirdiğiniz ve SBC'nize kurmak üzere olduğunuz işletim sisteminin orijinalliğini tespit edin.



![img](assets/en/06.webp)



Eğer sha256sum komutu ile de `Good signature` sonucunu ve aynı Hash kontrolünü aldıysanız, ISO'yu bir USB belleğe flaşlamaya devam edebilirsiniz. Bunu yapmak için Whale Etcher gibi uygulamaları kullanın.



![img](assets/en/07.webp)



## DietPi Kurulumu



![img](assets/en/09.webp)



Flash sürücüyü DietPi'yi barındıracak cihaza aktarın ve lime Green işletim sisteminin kurulumuna başlayın. Bu alıştırmada 16 GB RAM, işletim sistemi için 128 GB SSD ve ikinci bir 1 TB veri diski olan ince bir istemci kullanıyoruz. Kurulum 30 dakikadan az sürdü, ancak örneğin bir Raspberry kullanacaksanız, kaynaklar daha az olabilir ve daha uzun sürebilir. Kurulum sırasında ilerleme durumu size gösterilecektir.



![img](assets/en/08.webp)



Raspberry ve benzerleri için tasarlanmış olan DietPi'nin gerçek doğası, grafiksel bir ortam olmadan ve yerel `shsh' erişimi ile `headless' kurulum olarak adlandırılır. Kılavuzda bunun yerine grafiksel bir ortam göreceksiniz, tam olarak LXDE.



Bu adımda ayrıca Chromium ve Firefox arasında varsayılan olarak hangi web tarayıcısını kullanmak istediğinize karar vermeniz istenecektir. Her ikisi de iyi çalışır; kişisel tercihiniz dışında herhangi bir özel kontrendikasyon yoktur.



Sona doğru, yükleyici size herhangi bir program yüklemek isteyip istemediğinizi sorabilir, ancak burada **hiçbir şeyi önceden yüklememenizi tavsiye ederim**. Bu adımdan sonra, güvenlik nedeniyle iki kullanıcının varsayılan şifrelerini değiştirmeniz isteneceğini bilmelisiniz. En önemlisi, çeşitli yazılımlara kontrollü bir şekilde erişimi sağlayacak olan **Global Yazılım Parolasını (GSP)`** ayarlamanız gerekecektir. **İşletim sistemi kurulumu sırasında `GSP` ayarlanmadan herhangi bir yazılım indirirseniz, bunlar neredeyse erişilemez kalacaktır**. Global Yazılım Parolası`nı ayarladıktan sonra bunları kaldırmanız ve yeniden yüklemeniz gerekecektir: bu nedenle, **çifte çalışmayı önlemek için hiçbir şey koymayın**. (Rahatsızlık olasıdır, %100 kesin değildir).



Kurulum, işletim sisteminin geliştirilmesini desteklemek için kullanılan otomatik bir veri toplama hizmeti olan DietPi-Survey'in etkinleştirilmesi talebiyle sona erer. Web sitesine göre, DietPi tarafından sağlanan otomasyondan herhangi bir yazılımı indirdiğinizde veya bir sonraki sürüme yükselttiğinizde veri toplama etkinleştirilir. Herkesin katılma (_Opt IN_) veya katılmama (_Opt OUT_) seçeneği vardır.



![img](assets/en/23.webp)



Kurulumun tamamlanması ve ardından yeniden başlatmanın ardından, DietPi ekranda ayarladığınız gibi görünür. Eğitim için, belirtildiği gibi, `LXDE` grafik ortamını seçtim. Masaüstünde `htop` ve açık terminali başlatmak için bir kısayol buldum.



![img](assets/en/10.webp)



### i̇şletim sisteminden "Araçlar"



Linux dağıtımınızda kullandığınız programların çoğunu unutun-DietPi o kadar optimize edilmiştir ki, pek çoğunu dışarıda bırakmışsınızdır. Temelde birçok komutu manuel olarak yüklemeniz gerekir, ancak sadece deniyorsanız, cazibesine karşı koyun ve DietPi'nin otomasyonlarını test etmeyi deneyin.



Yeni işletim sisteminize başlamak için ilk kullanışlı araç kesinlikle terminaldir ve her açtığınızda otomatik olarak açılır.



![img](assets/en/11.webp)



Terminal ekranında, önünde `dietpi-` bulunan ve bu işletim sisteminin [tools](https://dietpi.com/docs/dietpi_tools/)'unu temsil eden bir dizi komutun listelendiğini göreceksiniz:




- `dietpi-launcher`: işletim sistemine, dosya yöneticisine vb. erişmek için
- `dietpi-Software`: pakette zaten mevcut olan tüm yazılımları yükleyebileceğiniz aracı temsil eder
- `dietpi-config`: en gelişmiş olanlar da dahil olmak üzere sistem yapılandırmalarına erişmek için.



![img](assets/en/14.webp)



### Yedekleme



Bir sunucunun yedeklenmesi, sistem yöneticisinin ilk çalıştırmadan itibaren öngörmesi gereken bir rutindir.



DietPi ile ideal çözümü bulmak için keşfetmenizi tavsiye ettiğim `dietpi-Backup` komutu vardır: kullanılan uygulamalara ve rutini özelleştirmek için tüm seçeneklere bağlı olarak düzenli bir yedekleme, artımlı veya değil ayarlamanıza olanak tanır.



![img](assets/en/22.webp)



Hedef sürücüyü bağlamak ve bu işlev için kullanmak üzere `dietpi-Drive_Manager`ı başlatarak yedeklemenin hedefini, örneğin başka bir diski seçin.



## Konfigürasyon



Kendi kendini barındırma, ister meraklı ister hevesli olsun herkes için tavsiye edilen bir deneyimdir. Ancak, bir sunucuyu kurmak ve yapılandırmak hiç de azımsanmayacak bazı teknolojik zorluklar içerir. DietPi'nin** basitliği burada devreye giriyor ve birkaç basit adımda ihtiyaçlarınıza uygun bir sistem yapılandırmanıza olanak tanıyor.



![img](assets/en/24.webp)



Temel ve gelişmiş ayarlar, hepsi komutla birlikte sunulan tek bir Interface'te parmaklarınızın ucunda:



```dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-yazılım


```