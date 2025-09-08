---
name: OPNsense
description: OPNsense güvenlik duvarını nasıl kurabilir ve yapılandırabilirim?
---
![cover](assets/cover.webp)



___



*Bu eğitim Florian BURNEL tarafından [IT-Connect](https://www.it-connect.fr/) adresinde yayınlanan orijinal içeriğe dayanmaktadır. Lisans [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Orijinal metinde değişiklikler yapılmış olabilir.*



___



## I. Sunum



Bu eğitimde OPNsense açık kaynak güvenlik duvarına bir göz atacağız. Ana özelliklerine, önkoşullarına ve FreeBSD tabanlı bu çözümün nasıl kurulacağına bakacağız.



Başlamadan önce, **OPNsense ve pfSense'in her ikisinin de FreeBSD tabanlı açık kaynaklı güvenlik duvarları** olduğunu bilmelisiniz. PfSense'in OPNsense'in bir tür ağabeyi olduğunu söyleyebiliriz, çünkü ikincisi 2015'te oluşturulan bir Fork'dır. Son olarak, 2017'den bu yana **OPNsense'in FreeBSD** yerine HardenedBSD'ye geçtiğini belirtmek önemlidir. HardenedBSD, FreeBSD'nin gelişmiş güvenlik özelliklerine sahip geliştirilmiş bir sürümüdür



OPNsense, daha modern kullanıcı Interface ve **daha sık güncelleme temposu** ile öne çıkmaktadır. Gerçekten de, OPNsense'in güncelleme programı yılda iki büyük sürüm içeriyor ve bunlar iki haftada bir güncelleniyor (küçük sürümlerle sonuçlanıyor). Bu çözümlerin topluluk sürümlerine bakarsak, bu takip pfSense ile karşılaştırıldığında çok ilginçtir.



![Image](assets/fr/050.webp)



## II. OPNsense özellikleri



OPNsense, özellikleri çok sayıda olmasına ve ek paketler yüklenerek genişletilebilmesine rağmen, güvenlik duvarı ve yönlendirici olarak hareket etmek üzere tasarlanmış bir işletim sistemidir. Üretim kullanımı için uygundur, esas olarak ağ güvenliği ve akış yönetimi için kullanılır.



### A. Ana özellikler



OPNsense'in temel özelliklerinden bazıları şunlardır:





- Güvenlik Duvarı ve NAT**: OPNsense, durum bilgisi filtrelemeli gelişmiş durum bilgisi güvenlik duvarı işlevselliğinin yanı sıra ağ Address çevirisi (NAT) yetenekleri sağlar.





- DNS/DHCP**: OPNsense, ağdaki DNS ve DHCP hizmetlerini yönetmek için yapılandırılabilir. Bir DHCP sunucusu olarak hareket edebilir, ancak yerel ağdaki makineler için bir DNS çözümleyicisi olarak da kullanılabilir. Dnsmasq da varsayılan olarak entegre edilmiştir.





- VPN**: OPNsense, IPsec, OpenVPN ve WireGuard dahil olmak üzere çeşitli VPN protokollerini destekleyerek mobil iş istasyonlarına uzaktan erişim veya site ara bağlantısı için güvenli bağlantılar sağlar.





- Web proxy**: OPNsense, İnternet erişimini kontrol etmek ve filtrelemek için bir web proxy'si içerir. Ayrıca içeriği filtrelemek ve ağ erişimini yönetmek için de kullanılabilir.





- Bant genişliği yönetimi (QoS)**: OPNsense, ağ trafiğine öncelik vermek ve ağ bant genişliğini daha iyi yönetmek için Hizmet Kalitesi (QoS) yönetim özellikleri sunar.





- Captive portal**: Bu özellik, bir kimlik doğrulama sayfası (yerel taban, kuponlar vb.) aracılığıyla ağa kullanıcı erişimini yönetmenizi sağlar. Genel Wi-Fi ağları için yaygın olarak kullanılan bir özelliktir.





- IDS/IPS**: OPNsense, ağı saldırılara karşı korumak için saldırı tespit ve önleme (IDS/IPS) işlevleri sunmak üzere Suricata'yı entegre eder.





- Yüksek kullanılabilirlik (CARP)**: OPNsense, birden fazla OPNsense güvenlik duvarı arasında yüksek kullanılabilirlik için CARP'yi (*Common Address Redundancy Protocol*) destekler ve donanım arızası durumunda bile hizmetin etkin kalmasını sağlar.





- Raporlama ve İzleme**: OPNsense, günlüklerin oluşturulması sayesinde ağ performansını (NetFlow ile) izlemek ve olası sorunları tespit etmek için gerçek zamanlı raporlama ve izleme araçları sağlar. Buna grafikler de dahildir. Monit aracı OPNsense'e entegre edilmiştir ve güvenlik duvarının kendisinin denetlenmesini sağlar.



### B. Ek paketler



Bu sadece OPNsense tarafından sunulan özelliklere genel bir bakıştır. Buna ek olarak, OPNsense yönetim Interface'ten erişilebilen **paket kataloğu**, güvenlik duvarını **ek işlevlerle zenginleştirmenize** olanak tanır. Bunlar arasında bir ACME istemcisi, bir Wazuh aracısı, NTP Chrony hizmeti ve bir ters proxy olarak Caddy bulunur.



![Image](assets/fr/051.webp)



## III. OPNsense önkoşulları



Her şeyden önce, OPNsense'i nereye kuracağınıza karar vermeniz gerekir. . üzerine kurulum da dahil olmak üzere birkaç olası çözüm vardır:





- Hyper-V, Proxmox, VMware ESXi vb. sanal makine olarak bir hipervizör.
- Çıplak metal* sistem olarak bir makine. Bu, güvenlik duvarı görevi gören mini bir bilgisayar olabilir.



Ayrıca çevrimiçi mağazamızdan **bir OPNsense rafa monte edilebilir cihaz** satın alabilirsiniz.



OPNsense'i çalıştırmak için gereken donanım kaynaklarını hesaba katmanız gerekir. Bu konu [bu dokümantasyon sayfası] (https://docs.opnsense.org/manual/hardware.html) adresinde ayrıntılı olarak açıklanmıştır.



**Üretim için minimum ve önerilen kaynaklar:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Son olarak, **kaynak gereksinimleriniz her şeyden önce yönetilecek bağlantı sayısına** ve dolayısıyla **bant genişliği gereksinimlerinize** bağlıdır. Ayrıca, CPU ve/veya RAM'e ihtiyaç duyabilecekleri için **etkinleştirilecek ve kullanılacak hizmetleri** (proxy, saldırı tespiti, vb...) aklınızda bulundurmanız gerekir.



Ayrıca [resmi web sitesinden] (https://opnsense.org/download/) indirebileceğiniz OPNsense kurulum ISO görüntüsüne de ihtiyacınız olacak. Bir sanal makineye kurulum için, bir ISO görüntüsü elde etmek üzere görüntü türü olarak "**dvd**" seçeneğini seçin (ve bununla istediğinizi yapın...). Önyüklenebilir bir USB anahtarı aracılığıyla kurulum için, bir "**.img**" dosyası elde etmek üzere "**vga**" seçeneğini seçin.



![Image](assets/fr/048.webp)



OPNsense yönetimi ve testi için bir bilgisayara da ihtiyacınız olacak.



## IV. Hedef yapılandırması



Bizim hedefimiz





- OPNsense güvenlik duvarı üzerinden İnternet'e erişebilen dahili bir sanal ağ (192.168.10.0/24 - LAN)** oluşturun. Üretim kullanımı için bu, yerel ağınız, kablo ve/veya Wi-Fi olabilir.
- Dahili sanal ağdaki VM'lerin İnternet'e erişebilmesi için NAT'ı** etkinleştirin ve yapılandırın
- Dahili sanal ağa bağlı gelecekteki makinelere bir IP yapılandırması dağıtmak için OPNsense** üzerindeki DHCP sunucusunu etkinleştirin ve yapılandırın
- Güvenlik duvarını** HTTP (80) ve HTTPS (443) ile yalnızca LAN'dan WAN'a giden akışlara izin verecek şekilde yapılandırın.
- Sanal LAN'ın OPNsense'i DNS çözümleyicisi olarak kullanmasına izin vermek için güvenlik duvarını** yapılandırın (53).



Hyper-V platformunu kullanıyorsanız, bu size aşağıdaki gösterimi verecektir:



![Image](assets/fr/033.webp)



## V. OPNsense güvenlik duvarının kurulması



### A. Önyüklenebilir USB anahtarını hazırlama



İlk adım kurulum ortamını hazırlamaktır: **OPNsense ile önyüklenebilir USB anahtarı**. Sanal bir ortamda çalışıyorsanız bu elbette isteğe bağlıdır, ancak her durumda OPNsense kurulum ISO görüntüsünü indirmeniz gerekir.



İndirdikten sonra, ".img "** biçiminde bir görüntü içeren bir **arşiv elde edersiniz. Kullanımı son derece basit olan **balenaEtcher** dahil olmak üzere çeşitli uygulamalarla **önyüklenebilir bir USB bellek** oluşturabilirsiniz. Dahası, uygulama arşivdeki görüntüyü tanıyacaktır, bu nedenle önceden sıkıştırmayı açmanız gerekmez.





- [Download balenaEtcher](https://etcher.balena.io/)



Uygulama yüklendikten sonra, resminizi ve USB anahtarınızı seçin ve ardından "Flash! Bir dakika bekleyin.



![Image](assets/fr/049.webp)



Şimdi yüklemeye hazırsınız.



### B. OPNsense Sisteminin Kurulması



OPNsense'i barındıran makineyi başlatın. Aşağıdakine benzer bir karşılama sayfası görmelisiniz. Birkaç saniye boyunca, gösterilen ekran pencerede görünür olacaktır. İşlemin devam etmesine izin verin...



![Image](assets/fr/019.webp)



OPNsense görüntüsü makineye yüklenir, böylece sisteme "**canlı**" modda erişilebilir, yani geçici olarak bellekte saklanır.



![Image](assets/fr/025.webp)



Ardından aşağıdakine benzer bir Interface'e geleceksiniz. Giriş "**installer**" ve şifre "**opnsense**" ile giriş yapın. Lütfen klavyenin şu anda **QWERTY** olduğunu unutmayın. Bu noktada, **OPNsense kurulum sürecini** başlatacağız.



![Image](assets/fr/026.webp)



Ekranda yeni bir sihirbaz belirir. İlk adım, yapılandırmanıza karşılık gelen klavye düzenini seçmektir. AZERTY klavye için listeden "**Fransızca (aksan tuşları)**" seçeneğini seçin ve ardından çift tıklayın**.



![Image](assets/fr/027.webp)



İkinci adım, gerçekleştirilecek görevi seçmektir. Burada, **ZFS dosya sistemini** kullanarak bir kurulum gerçekleştireceğiz. Kendinizi "**Kurulum (ZFS)**" satırında konumlandırın ve **Enter** ile onaylayın.



![Image](assets/fr/028.webp)



Üçüncü adımda, makinemiz **sadece bir disk** ile donatıldığından "**şerit**" seçeneğini seçin: güvenlik duvarı depolamasını ve verilerini güvence altına almak için yedekleme mümkün değildir. Bu, özellikle RAID prensibi aracılığıyla bir diskin donanım arızasına karşı koruma sağlamak için fiziksel bir makineye kurulum yaparken önemlidir.



![Image](assets/fr/029.webp)



Dördüncü adımda, onaylamak için **Enter** tuşuna basmanız yeterlidir.



![Image](assets/fr/030.webp)



Son olarak, "**Evet**" seçeneğini seçerek ve ardından **Enter** tuşuna basarak onaylayın.



![Image](assets/fr/031.webp)



Şimdi OPNsense yüklenirken beklemeniz gerekecek... Bu işlem yaklaşık 5 dakika sürer.



![Image](assets/fr/032.webp)



Kurulum tamamlandıktan sonra, yeniden başlatmadan önce "**root**" parolasını değiştirebiliriz. "**Root Password**" öğesini seçin, **Enter** tuşuna basın ve "**root**" parolasını iki kez girin.



![Image](assets/fr/020.webp)



Son olarak, "**Kurulumu Tamamla**" seçeneğini seçin ve **Enter** tuşuna basın. Bu fırsattan yararlanarak diski VM'nin DVD sürücüsünden çıkarın**. VM ayarlarında, diske ilk önyüklemeyi de ayarlayabilirsiniz.



![Image](assets/fr/021.webp)



Sanal makine yeniden başlatılacak ve OPNsense sistemini yeni yüklediğimiz için diskten yükleyecektir. Konsolda "root" hesabıyla ve yeni parolanızla oturum açın (aksi takdirde varsayılan parola "**opnsense**" olur).



### D. Ağ arayüzlerini bağlama



Aşağıda gösterilen ekran görünecektir. Makinenin ağ kartlarını OPNsense arayüzleriyle ilişkilendirmek için "**1**" öğesini seçin ve **Enter** tuşuna basın.



![Image](assets/fr/022.webp)



İlk olarak, sihirbaz sizden bağlantı birleştirme ve VLAN'ları yapılandırmanızı ister. Reddetmek için "**n**" belirtin ve her seferinde **Enter** ile yanıtınızı doğrulayın. Ardından, iki arayüzü "**hn0**" ve "**hn1**" **WAN** ve **LAN**'a atamanız gerekir. Prensip olarak, "**hn0**" WAN'a ve diğer Interface LAN'a karşılık gelir.



Şöyle çalışıyor:



![Image](assets/fr/023.webp)



Artık elimizde:





- Interface **LAN** "**hn1**" ağ kartıyla ve OPNsense varsayılan IP Address ile ilişkilidir, yani **192.168.1.1/24**.
- Interface **WAN**, "**hn0**" ağ kartıyla ve yerel ağdaki **DHCP** aracılığıyla alınan bir IP Address ile ilişkilendirilmiştir (harici sanal anahtarımız sayesinde).



Varsayılan olarak, OPNsense yönetimi Interface'e bariz güvenlik nedenleriyle yalnızca LAN Interface'den erişilebilir. Bu nedenle, yönetimi gerçekleştirmek için güvenlik duvarının Interface LAN'ına bağlanmanız gerekir. Bu mümkün değilse, OPNsense'i geçici olarak WAN'dan yönetebilirsiniz. Bu, güvenlik duvarı işlevinin devre dışı bırakılmasını içerir.



Bunu yapmak için, "**8**" seçeneğini kullanarak kabuk moduna geçin ve aşağıdaki komutu çalıştırın:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. OPNsense Interface yönetim sistemine erişim



OPNsense Administration Interface'e, LAN** Interface'ün (veya WAN'ın) IP Address'ü kullanılarak HTTPS üzerinden erişilebilir. Tarayıcınız sizi bir oturum açma sayfasına götürecektir. Daha önce seçtiğiniz "root" hesabı ve parolası ile oturum açın.



![Image](assets/fr/034.webp)



Birkaç saniye bekleyin... Temel yapılandırmayı gerçekleştirmek için bir sihirbazı takip etmeniz istenecektir. Devam etmek için "**Sonraki**" seçeneğine tıklayın.



![Image](assets/fr/036.webp)



İlk adım, ana bilgisayar adını, alan adını tanımlamak, dili seçmek ve ad çözümlemesi için kullanılacak DNS sunucusunu/sunucularını tanımlamaktır. "**Enable Resolver**" seçeneğini tutmak, güvenlik duvarının bir DNS çözümleyici olarak kullanılmasına izin verecek ve bu da sanal LAN'ımızdaki makineler için yararlı olacaktır.



![Image](assets/fr/037.webp)



Bir sonraki adıma geçin. Varsayılan olarak yapılandırılmış sunucular olmasına rağmen sihirbaz size **tarih ve saat senkronizasyonu için bir NTP sunucusu tanımlama** seçeneği sunar. Buna ek olarak, coğrafi konumunuza karşılık gelen saat dilimini seçmeniz önemlidir (özel gereksinimleriniz yoksa).



![Image](assets/fr/038.webp)



Ardından önemli bir adım gelir: **Interface WAN'ın yapılandırılması**. Şu anda DHCP'de yapılandırılmıştır ve statik bir IP Address ayarlamak istemediğiniz sürece bu yapılandırma modunda kalacaktır.



![Image](assets/fr/039.webp)



Yine Interface WAN yapılandırma sayfasında, WAN tarafındaki ağ özel adresleme kullanıyorsa "**WAN üzerinden özel ağlara erişimi engelle**" seçeneğinin işaretini kaldırmanız gerekir. Bir Laboratuvar çalıştırıyorsanız muhtemelen bu durum söz konusu olacaktır ve bu nedenle İnternet'e erişmenizi engelleyebilir.



![Image](assets/fr/040.webp)



Daha sonra, bir "root "** parolası tanımlayabilirsiniz, ancak bu isteğe bağlıdır çünkü bunu zaten yaptık.



![Image](assets/fr/041.webp)



Yapılandırmanın yeniden yüklenmesini başlatmak için sonuna kadar devam edin. WAN üzerinden kontrol almaya devam etmeniz gerekiyorsa, bu işlem tamamlandıktan sonra yukarıdaki komutu yeniden başlatın.



![Image](assets/fr/042.webp)



Hepsi bu kadar!



![Image](assets/fr/035.webp)



### E. DHCP yapılandırması



Amacımız sanal LAN üzerinde IP adreslerini dağıtmak için OPNsense DHCP sunucusunu kullanmaktır. Bunu yapmak için bu menü konumuna erişmemiz gerekiyor:



```
Services > ISC DHCPv4 > [LAN]
```



**Gördüğünüz gibi, DHCP LAN'da varsayılan olarak zaten etkin ** Bu hizmetle ilgilenmiyorsanız, devre dışı bırakmalısınız. Zaten etkin olmasına ve onu kullanmak istememize rağmen, yapılandırmasını gözden geçirmek önemlidir.



Gerekirse, dağıtılacak IP adresi aralığını değiştirebilirsiniz: *mevcut ayarlara bağlı olarak *192.168.10.10** ila **192.168.10.245**.



![Image](assets/fr/046.webp)



Ayrıca "**DNS sunucuları**", "**Ağ geçidi**", "**Alan adı**" vb. alanların varsayılan olarak boş olduğunu görebiliriz. Aslında, bu çeşitli alanlar için belirli seçeneklerin ve varsayılan değerlerin otomatik bir kalıtımı vardır. Örneğin, DNS sunucusu için, Interface LAN'ın IP Address'u dağıtılacak ve OPNsense güvenlik duvarının bir DNS çözümleyici olarak kullanılması sağlanacaktır.



Gerekirse herhangi bir değişiklik yaptıktan sonra yapılandırmayı kaydedin.



![Image](assets/fr/047.webp)



DHCP sunucusunu test etmek için, güvenlik duvarınızın LAN ağına bir makine bağlamanız gerekir.



Bu makine OPNsense DHCP sunucusundan bir IP Address almalı ve makinemizin ağa erişimi olmalıdır. İnternet erişimi çalışmalıdır. OPNsense'e WAN'dan erişmek için güvenlik duvarı işlevini devre dışı bıraktıysanız, bunun NAT'ı devre dışı bırakarak Web'e erişmenizi engelleyeceğini lütfen unutmayın.



**Not**: Şu anda yayınlanan DHCP kiralamaları OPNsense yönetim Interface'den görülebilir. Bunu yapmak için aşağıdaki konuma gidin: **Services > ISC DHCPv4 > Leases**.



![Image](assets/fr/045.webp)



### F. NAT ve güvenlik duvarı kurallarını yapılandırma



İyi haber şu ki artık LAN'dan OPNsense yönetim Interface'ye erişebiliyoruz.



```
https://192.168.1.10
```



OPNsense'e giriş yaptıktan sonra NAT yapılandırmasını keşfedelim. Bu konuma gidin: **Güvenlik Duvarı > NAT > Giden**. Burada giden NAT kurallarının otomatik (varsayılan) ve manuel oluşturulması arasında seçim yapabilirsiniz.



"**Giden NAT kurallarının otomatik oluşturulması**" seçeneği üzerinden otomatik modu seçin ve "**Kaydet**" seçeneğine tıklayın (prensip olarak, bu yapılandırma zaten etkin olandır). Otomatik modda, OPNsense'in kendisi her ağınız için bir NAT kuralı oluşturur.



![Image](assets/fr/043.webp)



Şimdilik, "**192.168.10.0/24**" sanal LAN'ına bağlı tüm bilgisayarlar kısıtlama olmaksızın İnternet'e erişebilir. Ancak, amacımız WAN'a erişimi HTTP ve HTTPS protokollerinin yanı sıra güvenlik duvarının Interface LAN'ındaki DNS ile kısıtlamaktır.



Bu yüzden güvenlik duvarı kuralları oluşturmamız gerekiyor... Menüye aşağıdaki gibi göz atın: **Güvenlik Duvarı > Kurallar > LAN**.



**Varsayılan olarak, IPv4 ve IPv6'da** tüm giden LAN trafiğini yetkilendirmek için iki kural vardır. Her satırın başında, en soldaki Green okuna tıklayarak bu iki kuralı devre dışı bırakın.



Ardından **LAN ağını** (yani "**LAN net**") yetkilendirmek için üç yeni kural oluşturun:





- tüm hedeflere **HTTP** kullanarak erişin.
- tüm hedeflere **HTTPS** ile erişin.
- gW-25 LAN'ında** (yani "**LAN Address**") **DNS protokolü** aracılığıyla **OPNsense** talep edin (bu, güvenlik duvarını DNS olarak kullanmak anlamına gelir), aksi takdirde DNS çözümleyicinizi IP Address aracılığıyla yetkilendirin.



Bu da aşağıdaki sonucu verir:



![Image](assets/fr/044.webp)



Geriye kalan tek şey, yeni güvenlik duvarı kurallarını üretime geçirmek için "**Değişiklikleri uygula**" seçeneğine tıklamaktır. **Açıkça yetkilendirilmemiş tüm akışların varsayılan olarak engelleneceğini lütfen unutmayın



LAN makinesi HTTP ve HTTPS kullanarak İnternet'e erişebilir. Diğer tüm protokoller engellenecektir.



![Image](assets/fr/018.webp)



## IV. Sonuç



Bu kılavuzu takip ederek OPNsense'i kurabilir ve hemen kullanmaya başlayabilirsiniz. OPNsense, ağ trafiğinizi verimli bir şekilde güvence altına almak ve yönetmek için çok çeşitli özellikler sunar ve profesyonel ortamlarda kullanıma uygundur.



Bu kurulum sadece bir başlangıçtır: OPNsense'i ihtiyaçlarınıza göre uyarlamak için menüleri keşfetmekten ve diğer özellikleri yapılandırmaktan çekinmeyin.