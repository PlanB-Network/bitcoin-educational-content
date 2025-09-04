---
name: Ntopng
description: Ağınızı ntopng ile izleyin
---
![cover](assets/cover.webp)



___



*Bu eğitim Florian Duchemin tarafından [IT-Connect](https://www.it-connect.fr/) adresinde yayınlanan orijinal içeriğe dayanmaktadır. Lisans [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Orijinal metinde değişiklikler yapılmış olabilir.*



___



## I. Sunum



**Ağ akışkanlığını kontrol etmek, kullanımın net bir resmini elde etmek veya performans istatistikleri için olsun, ağ akışı izleme kurumsal bir ağın önemli bir parçasıdır**. Altyapıdaki değişiklikleri öngörmeye yardımcı olur ve kullanıcılar için kullanım kalitesinin sağlanmasına yardımcı olur (QoS'un aksine *Deneyim Kalitesi* için QoE olarak da bilinir).



Bunu yapmak için birçok teknik ve yazılım/protokol mevcuttur. Örneğin Cisco tarafından geliştirilen Netflow, bir Interface'dan IP akış istatistiklerini almak için kullanılabilir, ancak kullanımı uyumlu ekipmanla sınırlıdır.



Bu nedenle bu eğitimde **Ntop**'u tanıtacağım ve ağ kullanımınızı takip etmek için altyapınızda nasıl kullanacağınızı göstereceğim.



Ntop, herhangi bir Linux makinesine kurulabilen açık kaynaklı bir yazılımdır. Ücretsizdir ve aşağıdaki verileri toplayabilir:





- Bant genişliği kullanımı
- Ana müşteriler
- Ana varış noktaları
- Kullanılan Protokoller
- Kullanılan uygulamalar
- Kullanılan bağlantı noktaları
- Vb.



Şimdi **Ntopng (Yeni Nesil)** olarak yeniden adlandırılan bu ürün, birçok temel işlevi ücretsiz olarak sunmaktadır. Yapılandırılmış uyarıların SIEM tipi yazılıma aktarılmasına veya trafiğin doğrudan probdan tanımlanan kurallarla filtrelenmesine olanak tanıyan ticari bir sürümü de mevcuttur.



## II. Ön Koşullar



Bir Ntop probunun kurulumu ekipmana ve ortama göre farklılık gösterir. Bu yüzden burada size adım adım bir kılavuz vermeyeceğim, ancak çeşitli olasılıkları özetleyeceğim.



### A. Yerleşik mod



Üretimde bir pfSense, OPNSense veya Endian güvenlik duvarınız varsa, hatta NFTables ile bir Linux iş istasyonunuz varsa, iyi haber! Ntopng'yi doğrudan yükleyebilir ve arayüzlerinizi izlemeye başlayabilirsiniz.



Bu tekniğin avantajı ek donanım gerektirmemesidir. Öte yandan, kaynak kullanımını artırır, bu nedenle yeterli donanıma veya yeterli boyutta bir sanal makineye (en az 2 çekirdek ve 2BG RAM) sahip olduğunuzdan emin olun.



### B. TAP / SPAN modu



Bir **tap**, içinden geçen trafiği kopyalayan ve başka bir cihaza gönderen bir ağ cihazıdır.** Bu cihazın avantajı, mevcut altyapıda herhangi bir değişiklik gerektirmemesi ve belirli ağ bölümlerini izlemek için herhangi bir yere veya İnternet'e giden / gelen trafiği analiz etmek için çekirdek anahtar ile kenar yönlendirici arasına yerleştirilebilmesidir.



Bu tür ekipmanın en büyük dezavantajı maliyetidir. Günümüzün Gigabit ağlarında, pasif bir musluk ağ trafiğini düzgün bir şekilde yakalayamaz, bu nedenle yaklaşık 200 € (minimum) maliyetli aktif bir cihaza ihtiyacınız vardır.



Port yansıtma** olarak da bilinen **SPAN** modu, trafiği bir porttan diğerine iletmek için bir anahtar tarafından kullanılır. Bu benim açık ara tercih ettiğim yöntemdir, çünkü kurulumu kolaydır ve tap gibi, ağın bir bölümünü veya tüm ağı istediğiniz zaman izlemenize olanak tanır. Bununla birlikte, iki dezavantajı vardır: anahtarın bu işlevi entegre etmesi gerekir ve kullanımı anahtar üzerindeki işlemci yükünü artırabilir.



### C. Yönlendirici modu



Linux altında bir yönlendirici monte etmek ve üzerine ntopng yüklemek tamamen mümkündür. Bu yöntemin tek dezavantajı, ağınızın dahili adreslemesini ya da "gerçek" yönlendiriciniz ile eklediğiniz yönlendirici arasındaki adreslemeyi değiştirecek olmasıdır.



Not: [Raspberry Pi ve RaspAP ile bir Wifi yönlendirici oluşturun] (https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) makalesini okuyanlar için, doğru istatistikler elde etmek için Rpi'nize ntopng yüklemek tamamen mümkündür!



### D. Köprü modu



İlginç bir alternatif de **köprü modunda bir Linux makinesi kullanmaktır.** İki ekipman arasına yerleştirilen bu makine, altyapının veya ekipmanının yapılandırmasına müdahale etmek zorunda kalmadan tüm trafiğin yakalanmasını sağlar. Eski bir makine bu işi yapabileceğinden, bu yöntemin maliyeti de cazip olabilir. Optimal olması için cihazda ikisi köprü modunda, biri Interface ve SSH'ye erişim için olmak üzere üç ağ kartı olması gerektiğini unutmayın. Sadece iki kart kullanmak mümkündür, ancak bu durumda cihaz yönetim trafiği de yakalanacaktır...



Yani benim kullanacağım **bu son mod**. Pratik nedenlerden dolayı, tanıtım için sanal makineler kullanacağım, ancak yöntem fiziksel makinelerde kullanım için aynı kalıyor.



## III. Interface köprüsü ile prob hazırlama



Sonda için, minimal kurulumda bir **Debian 11** makinesi seçiyorum.



İlk adım, her zaman aynı,:



```
apt-get update && apt-get upgrade
```



Ardından köprümüzü oluşturmamızı sağlayacak **bridge-utils** paketini yükleyin:



```
apt-get install bridge-utils
```



Kurulduktan sonra, dikkat edilmesi gereken ilk şey ağ kartlarımızın mevcut adıdır. Debian altında bu isim çeşitli şekillerde olabilir ve yapılandırma için buna ihtiyacımız olacak.



Basit bir **ip add** komutu bu bilgileri içeren bir çıktı döndürecektir:



![Image](assets/fr/016.webp)



Burada 3 arayüz görüyorum:





- Lo**: bu geri döngü Interface'üdür; ekipman üzerinde "döngü" yapan sanal bir Interface'tür. Temel olarak, Address'ü 127.0.0.1 olan bu Interface (bu aralık bu amaç için ayrıldığından 127.0.0.0/8'deki herhangi bir Address işe yarayacaktır) ekipmanın kendisiyle iletişim kurmak için kullanılır. Eğer iş istasyonunuza bir web sitesi kurduysanız (örneğin WAMPP kullanarak), muhtemelen "*localhost*" Kendi makinenizde barındırılan siteyi görüntülemek için bir seferde Address. Bu ana bilgisayar adı Address 127.0.0.1 ve dolayısıyla Interface loopback ile ilişkilidir.
- ens33**: bu benim ilk Interface'im, burada DHCP'den bir Address aldı
- ens36**: ikinci Interface'm



Artık tüm bilgilere sahip olduğuma göre, köprümü oluşturmak için */etc/network/interfaces* dosyasını değiştirebilirim. İşte şu anda nasıl göründüğü (değişebilir):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



İlk bölüm, dokunmayacağım geri döngü Interface'im ve ardından Interface ens33 ile ilgilidir. Değişiklikler ikinci Interface'imi (ens36) eklemeyi ve köprüyü bu iki arayüzle yapılandırmayı içeriyor:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



İşte bu ilk değişikliklere ilişkin bazı açıklamalar:





- auto *Interface***: sistem başlangıcında Interface'u otomatik olarak "başlatır"
- iface *Interface* inet manual**: Interface'u herhangi bir IP Address olmadan kullanmak için. Statik bir IP Address tanımlamak için "static" veya dinamik adresleme kullanmak için "dhcp" anahtar kelimesi gibi



Değişiklikler devam ediyor:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



İşte yine birkaç açıklama:





- iface br0 inet static**: burada Interface köprümü (*br0*) statik bir Address ile tanımladım.
- Address, netmask, gateway**: kart adresleme bilgileri
- bridge_ports**: köprüye dahil edilecek arayüzler
- bridge_stp**: Yayılan Ağaç protokolü, yedek bağlantıları tespit etmek ve döngülerden kaçınmak için anahtarları birbirine bağlarken kullanılır. Bir köprü iki ağ yolu arasına yerleştirilebildiğinden, bir döngünün kaynağı olabilir, dolayısıyla bu protokolü etkinleştirme olasılığı vardır. Burada buna ihtiyacım yok, bu yüzden devre dışı bırakıyorum.



Değişiklikleri kaydedin ve ağı yeniden başlatın:



```
systemctl restart networking
```



Değişiklikleri kontrol etmek için **ip** add komutunun sonucunu tekrar görüntüleyin:



![Image](assets/fr/021.webp)


Yeni Interface "*br0*" ile ona atadığım IP Address'yı açıkça görebilirsiniz.** Bu arada, iki fiziksel arayüzümün gerçekten "UP" olduğunu, ancak IP Address'ya sahip olmadığını da görebilirsiniz.



## IV. NtopNG'nin Kurulumu



Artık probumuz ağım ve yönlendirici arasındaki trafiği koklayabildiğine göre, geriye kalan tek şey ntopng'yi kurmak. Bunu yapmak için önce */etc/apt/sources.list* dosyasını değiştirin ve **deb** veya **deb-src** ile başlayan her satırın sonuna **contrib** ekleyin.



Varsayılan olarak, paket kaynakları yalnızca **main** anahtar sözcüğü ile tanımlanan DFSG (*Debian Free Sotftware Guidelines*) uyumlu paketleri içerir. Bu kaynakları siz de ekleyebilirsiniz:





- contrib**: DFSG uyumlu yazılım içeren, ancak **ana** dalın parçası olmayan bağımlılıkları kullanan paketler
- non-free**: DFSG uyumlu olmayan paketler içerir



Etc/apt/sources.list içinde bir satır örneği:



```
deb http://deb.debian.org/debian/ bullseye main
```



Bu yüzden bu gibi satırlara sadece **contrib** kelimesini ekleyeceğim.



Adımların geri kalanı [NtopNG] sitesinde (https://packages.ntop.org/apt/) listelenmiştir, burada Debian 11 için gelecekteki kurulum için Ntop kaynaklarını eklemeniz gerekir. Bu ekleme otomatik olarak bir:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Ardından asıl kurulum aşaması gelir:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



İlk komut apt paket yöneticisinin önbelleğini siler. İkincisi paket listesini güncelleyecek ve üçüncüsü NtopNG'yi yükleyecektir.



Kurulumdan sonra, **NtopNG yazılımı doğrudan Debian makinesinin 3000 numaralı portundan kullanılabilir**. Yani benim için `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



NtopNG ana sayfası



Varsayılan kullanıcı adı ve şifre gösterilir, böylece tek yapmanız gereken bunları girmektir!



## V. NtopNG Kullanımı



İlk oturum açtığınızda, yapmanız istenen ilk şey varsayılan yönetici şifresini ve dilini değiştirmektir. Ne yazık ki Fransızca bunlardan biri değil.



Sonra kontrol paneline ulaşırsınız:



![Image](assets/fr/023.webp)



NtopNG gösterge tablosu



Buna alışmayın! Ekranın üst kısmındaki sarı kutuya dikkat ederseniz, şu cümleyi göreceksiniz: "*Lisans 04:57'de sona eriyor*". Varsayılan olarak, kurulum NtopNG'nin tam sürümünün deneme sürümünü başlatır, ancak (çok) sınırlı bir süre için. Bu "geri sayıma" ulaşıldığında, *topluluk* sürümü etkinleştirilir ve gösterge tablosu değişir:



![Image](assets/fr/024.webp)



Yeni NtopNG topluluk panosu



Yapılacak ilk şey **doğru Interface'nin dinlendiğini kontrol etmektir**. Sol üst köşede, mevcut arayüzlerin açılır bir listesi, burada ilgilendiğimiz Interface'yi seçmenize olanak tanır: br0



![Image](assets/fr/025.webp)



Interface seçimi



Yeni pencere "Top Flaw Talkers "ı, yani en çok iletişim kuran cihazları gösterir. Burada sadece iki istasyon görünüyor:



![Image](assets/fr/026.webp)



**Kaynak ana bilgisayarlar solda, hedefler sağda görünür ** Bu, her bir ana bilgisayar tarafından toplam bant genişliğinin kullanımını görselleştirmenize ve ağ trafiğinin genel bir görünümünü elde etmenize olanak tanır. Bu fena değil, ama daha da ileri gidebiliriz...



Örneğin "*Hosts*" üzerine tıklarsam, ağımdaki her bir hostun gönderme ve alma güç tüketimini gösteren bir grafik elde ediyorum. Örneğin burada 192.168.1.37'nin tek başına trafiğimin %80'ini oluşturduğunu görebiliyorum:



![Image](assets/fr/027.webp)



Söz konusu ana bilgisayarın IP Address'una tıklarsam, bir özet sayfasına yönlendiriliyorum:



![Image](assets/fr/028.webp)



Örneğin, bunun bir VMWare makinesi olduğunu (MAC Address'min YES'ini tanıyarak), DESKTOP-GHEBGV1 olarak adlandırıldığını (yani kesinlikle bir Windows ana bilgisayarı) VE **alınan ve gönderilen paketlerin yanı sıra veri miktarı** istatistiklerine sahip olduğumu görebiliyorum.



Ayrıca bu özetin üst kısmında yeni bir menü göreceksiniz. Bu kadar çok trafiği neyin çektiğini görmek için "**Uygulamalar**" seçeneğine tıklamanızı öneririm:



![Image](assets/fr/017.webp)


Ha, görünüşe göre bir cevabımız var! Soldaki grafikte, ** trafiğinin %76,6'sının ...'dan geldiğini görüyoruz. Windows Update**, yani bu sunucu güncellemeleri indiriyor!



NtopNG, *Deep Packet Inspection* için DPI adı verilen bir teknoloji kullanarak her ağ akışını kategorize etmesini ve arkasındaki uygulamayı (veya uygulama ailesini) tanımlamasını sağlar.



Göstermek için ana bilgisayarımda bir YouTube videosu başlatıyorum:



![Image](assets/fr/018.webp)



**Trafik hemen fark edildi ve kategorize edildi!



Not: Açık nedenlerden dolayı, bu tür bir yazılım gizlilik sorunlarına yol açabilir, bu nedenle doğru koşullar altında kullanmaya dikkat edin. Ayrıca **sonuçları anonimleştirmenin** mümkün olduğunu unutmayın, seçenek **Ayarlar > Tercihler > Çeşitli** bölümünde bulunabilir ve "**Ana Bilgisayar IP Address**'i Maskele" olarak adlandırılır.



## VI. Tespitler ve uyarılar



NtopNG ayrıca belirli yayınlar için güvenlik uyarıları yayınlama kapasitesine sahiptir. Bunlar sol taraftaki başlıkta yer alan **Uyarılar** menüsünde bulunabilir. Burada, örneğin, farklı önem derecelerine bölünmüş toplam 2851 uyarı var: Bildirim, Uyarı ve Hata.



![Image](assets/fr/019.webp)



Yüksek kritiklikteki uyarılara bir göz atalım, 17 tane var!



Bu şekle tıklandığında uyarıların ayrıntıları görüntülenir. Burada endişe verici bir şey yok, bu bir yanlış pozitif, güncellemelerin indirilmesi bir HTTP akışında ikili dosya aktarımı olarak kategorize ediliyor, bu da gerçekten bir saldırı anlamına gelebilir.



![Image](assets/fr/020.webp)



Bununla birlikte, ücretsiz sürümü kullandığım için, uyarıların kaynağı olan alan adlarını veya ana bilgisayarları hariç tutamıyorum, bu nedenle çok daha endişe verici bir şeyi kaçırmamak için onlara göz kulak olmanız gerekecek. NtopNG,:





- HTTP üzerinden ikili dosya indirme
- Şüpheli DNS trafiği
- Standart olmayan bir bağlantı noktası kullanma
- SQL enjeksiyonu tespiti
- Siteler Arası Komut Dosyası Oluşturma (XSS)
- Vb.



## VII. Sonuç



Bu eğitimde, protokol kullanımını ve her bir ana bilgisayarın doluluğunu görselleştirmek ve aynı zamanda şüpheli trafiği tespit etmek için **ağ trafiğimizi analiz etmemize** olanak tanıyan **NtopNG ile bir probun nasıl kurulacağını** gördük.



Ne yazık ki, bu makalede tüm özellikleri ve olasılıkları ele alamıyorum, ancak keşfetmekten çekinmeyin!



Bu çözüm, kurumsal bir altyapı içinde kalıcı olarak uygulanabilir. NtopNG ayrıca sonuçları bir InfluxDB veritabanına aktarabilir ve Graphana gibi üçüncü taraf bir araçla kendi gösterge tablolarınızı oluşturmanıza olanak tanır.