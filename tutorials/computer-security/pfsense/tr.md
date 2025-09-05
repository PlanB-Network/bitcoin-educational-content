---
name: pfSense
description: Pfsense'i Yükleme
---
![cover](assets/cover.webp)



___



*Bu eğitim Florian BURNEL tarafından [IT-Connect](https://www.it-connect.fr/) adresinde yayınlanan orijinal içeriğe dayanmaktadır. Lisans [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Öğreticiyi güncel hale getirmek için yazarın orijinal metninde büyük değişiklikler yapılmıştır.*



___



![Image](assets/fr/027.webp)



## I. Sunum



pfSense, herhangi bir bilgisayarı, özel sunucuyu veya donanım cihazını yüksek performanslı, son derece yapılandırılabilir bir yönlendirici ve güvenlik duvarına dönüştüren ücretsiz, açık kaynaklı bir işletim sistemidir. FreeBSD'ye dayanan ve istikrarlı, sağlam ağ mimarisiyle tanınan pfSense, on beş yılı aşkın süredir işletmeler, yerel yönetimler ve talepkar ev kullanıcıları için açık kaynaklı güvenlik duvarlarının standardını belirlemektedir.



Ana işlevleri yıllar içinde önemli ölçüde gelişti ve her yeni sürümde geliştirildi. Bugüne kadar, pfSense:





- Modern, sezgisel ve güvenli bir Interface web Interface aracılığıyla eksiksiz, merkezi yönetim.
- Gelişmiş NAT desteği (NAT-T dahil) ve granüler kural yönetimi ile yüksek performanslı durum bilgisi güvenlik duvarı.
- İnternet bağlantılarının toplanmasını veya yedeklenmesini sağlayan yerel çoklu WAN desteği.
- Entegre DHCP sunucusu ve aktarıcısı.
- Yük devretme için CARP protokolü ve pfSense kümelerini yapılandırma imkanı sayesinde yüksek kullanılabilirlik.
- Birkaç bağlantı veya sunucu arasında yük dengeleme.
- Tam VPN desteği: IPsec, OpenVPN ve WireGuard (artık kullanılmayan L2TP'nin yerine).
- Özellikle halka açık veya otel ortamlarında misafir erişim kontrolü için yapılandırılabilir esir portalı.



pfSense ayrıca şeffaf proxy (Squid), URL filtreleme veya IDS/IPS (Snort veya Suricata) gibi gelişmiş özelliklerin doğrudan Interface web'den eklenmesini kolaylaştıran genişletilebilir bir paket sistemine sahiptir.



pfSense, mevcut FreeBSD önerileri doğrultusunda yalnızca 64 bit platformlar için dağıtılmaktadır. Standart donanımlara (PC'ler, raf sunucuları) veya Netgate cihazları veya eski Alix kutularından çok daha güçlü olan bazı düşük profilli x86 kutuları gibi düşük güçlü gömülü platformlara kurulabilir.



Son olarak, pfSense'in en az iki fiziksel ağ arayüzü gerektirdiğini hatırlamakta fayda var: biri harici bölgeye (WAN) ve diğeri dahili ağa (LAN) ayrılmış. Altyapınızın karmaşıklığına bağlı olarak (DMZ, VLAN, çoklu WAN'lar), yeteneklerinden tam olarak yararlanmak için birkaç ek arayüz gerekebilir.



## II. Resmi indir



Bu eğitimin yazıldığı sırada pfSense'in en son kararlı sürümü 2.8'dir (Haziran 2025'te yayınlanmıştır). ISO imajını veya donanım ortamınıza uyarlanmış kurulum dosyasını doğrudan resmi web sitesinden indirebilirsiniz:





- [Download pfSense](https://www.pfsense.org/download/)



İndirme portalı seçim yapmanıza olanak tanır:





- Mimari (genellikle tüm modern donanımlar için **AMD64**).
- Görüntü türü (USB bellek üzerinden kurulum için **Installer USB Memstick**, yakma veya sanal düzenleme için **ISO Installer**).
- Aktarım hızını optimize etmek için en yakın indirme aynası.



PfSense'i sanallaştırılmış bir ortamda (Proxmox, VMware ESXi, VirtualBox...) dağıtmak isteyenler için bir **OVA** görüntüsü de mevcuttur. Bu kullanıma hazır sanal makine, kurulumu ve ilk yapılandırmayı büyük ölçüde basitleştirir. Tahsis edilen kaynakları (CPU, RAM, ağ arayüzleri) beklenen yüke ve ağ topolojinize göre ayarladığınızdan emin olun.



Kurulumdan önce, resmi indirme sayfasında sağlanan **SHA256**'yı doğrulayarak indirilen dosyanın bütünlüğünü kontrol etmenizi öneririz. Bu, görüntünün değiştirilmediğinden veya bozulmadığından emin olmanızı sağlar.



## III. Kurulum



Bu örnekte, kurulum VirtualBox çalıştıran bir sanal makine üzerinde gerçekleştirilmektedir. Prosedür, sanal cihaz yönetimi dışında, fiziksel bir makinede veya başka bir hipervizörde kesinlikle aynı kalır.



### 1. Minimum donanım gereksinimleri



Standart bir dağıtım için:





- minimum 1 GB RAM** (ek paketleri veya ZFS desteğini etkinleştirmek için 2 GB veya daha fazlası önerilir).
- 8 GB disk alanı** (özellikle bir proxy önbelleği, IDS/IPS veya ayrıntılı günlükler yüklüyorsanız, daha gelişmiş yapılandırmalar için 20 GB veya daha fazlası tercih edilir).
- En az iki sanal ağ arayüzü** (biri WAN için, diğeri LAN için). VirtualBox'ta, başlatmadan önce bunları VM ayarlarına ekleyin.



### 2. Yükleyici başlatma



İndirilen ISO görüntüsünü VirtualBox'ta sanal bir optik sürücü olarak monte edin veya fiziksel bir makineye kuruyorsanız USB anahtarını takın. Başlangıçta bir önyükleme menüsü görünür:



Herhangi bir seçenek seçmezseniz, pfSense birkaç saniye sonra varsayılan seçeneklerle otomatik olarak başlayacaktır. Normal başlatmayı başlatmak için "**Enter**" tuşuna basın.



![Image](assets/fr/027.webp)



Ana menü göründüğünde, kurulumu başlatmak için hızlıca "**I**" düğmesine basın.



![Image](assets/fr/001.webp)



### 3. İlk yükleyici ayarları



İlk ekran, ekran yazı tipi ve karakter kodlaması gibi birkaç bölgesel parametre ayarlamanızı sağlar. Bu ayarlar belirli durumlarda (standart olmayan klavyeler, seri ekranlar, doğu dilleri) kullanışlıdır. Çoğu kurulum için varsayılan değerleri koruyun ve "**Bu Ayarları Kabul Et**" seçeneğini seçin.



![Image](assets/fr/002.webp)



### 4. Kurulum modu seçimi



Önerilen seçeneklerle otomatik bir yükleme çalıştırmak için "**Hızlı/Kolay Yükleme**" seçeneğini belirleyin. Bu yöntem seçilen diski siler ve pfSense'i varsayılan bölümleme ile yapılandırır.



![Image](assets/fr/003.webp)



Diskteki tüm verilerin silineceğini belirten bir uyarı görüntülenir. "**OK**" ile onaylayın.



Yükleyici daha sonra gerekli dosyaları diske kopyalar. Donanımınıza bağlı olarak bu işlem birkaç saniye ile birkaç dakika arasında sürebilir.



### 5. Çekirdek seçimi



Yükleyici sizden çekirdek türünü seçmenizi istediğinde, "**Standart Çekirdek**" seçeneğini seçili bırakın. Bu genel çekirdek, ister PC, ister sunucu veya VM üzerinde olsun, standart dağıtımlar için mükemmel şekilde uygundur.



### 6. Kurulum sonu ve yeniden başlatma



Kurulum tamamlandığında, makinenizi yeni pfSense örneğinizde yeniden başlatmak için "**Reboot**" öğesini seçin.



**Önemli not**: bir sonraki açılışta kurulum programının yeniden başlatılmasını önlemek için yeniden başlatmadan önce ISO görüntüsünü kaldırın veya kurulum USB anahtarının bağlantısını kesin.



## IV. PfSense'i ilk kez başlatma



İlk başlangıçta, pfSense ağ arayüzlerini (WAN, LAN, DMZ, VLAN'lar, vb.) tanıyacak ve doğru şekilde atayacak şekilde yapılandırılmalıdır. Ağ kartlarınızın dikkatli bir şekilde tanımlanması, sizi Interface web'e erişimden mahrum bırakabilecek veya güvenlik duvarınızı çalışmaz hale getirebilecek herhangi bir yapılandırma hatasından kaçınmak için çok önemlidir.



Başlatıldığında, pfSense mevcut tüm ağ arayüzlerini otomatik olarak algılar ve listeler ve her biri için MAC Address'ü gösterir. Bu, aralarında ayrım yapmayı kolaylaştırır.



### 1. VLAN'lar



İlk soru VLAN'ların yapılandırılmasıyla ilgilidir. Bu aşamada, temel bir yapılandırma için, herhangi bir VLAN'ı etkinleştirmeyeceğiz. Bu yüzden bu adımı atlamak için "**N**" tuşuna basın.



![Image](assets/fr/004.webp)



### 2. WAN ve LAN Interface Assignment



pfSense daha sonra WAN (İnternet erişimi) için hangi Interface'nın kullanılacağını tanımlamanızı ister. Arasında seçim yapabilirsiniz:





- Interface adını manuel olarak girin (sanal ortamlar için önerilir).
- "**A**" düğmesine basarak otomatik algılamayı kullanın. Bu seçenek, ağ kablolarınızın bağlı ve bağlantıların etkin olması koşuluyla fiziksel bir ana bilgisayarda kullanışlıdır.



![Image](assets/fr/005.webp)



Bu örnekte, WAN'ı manuel olarak yapılandırıyoruz. Interface'in tam adını girin. Bir Intel kartı için bu isim FreeBSD altında genellikle "**em0**" olacaktır, ancak donanıma bağlı olarak değişebilir. Örneğin, bir Realtek kartı genellikle "**re0**" olarak görüntülenecektir.



![Image](assets/fr/006.webp)



Interface LAN'ı tanımlamak için aynı işlemi tekrarlayın. Burada "**em1**" kullanıyoruz.



pfSense, Interface LAN'ın dahili ağınızı korumak ve Address çevirisini yönetmek için hem güvenlik duvarını hem de NAT'ı etkinleştirdiğini onaylar.



Başka fiziksel arayüzleriniz varsa, bu aşamada ek arayüzler (DMZ, Wi-Fi, belirli VLAN'lar) yapılandırabilirsiniz. Her mantıksal Interface, karşılık gelen bir ağ kartı veya sanal Interface gerektirir. İlk yapılandırma için kendimizi WAN ve LAN ile sınırlayacağız.



Atamalar tamamlandıktan sonra, pfSense fiziksel arayüzler ve atanan roller arasındaki yazışmaların açık bir özetini görüntüler. "**Y**" ile onaylayın.



### 3. PfSense konsolu



Bu adım tamamlandığında, pfSense konsolu ana menüsü görünür. Doğrudan yönetim için web parolasını sıfırlama, yeniden başlatma, yapılandırmayı yeniden yükleme veya arabirimleri yeniden atama gibi çeşitli yararlı seçenekler sunar.



![Image](assets/fr/007.webp)



Ayrıca, Interface LAN'ın varsayılan IP'si Address, genellikle **192.168.1.1** dahil olmak üzere mevcut ağ ayarlarının bir özetini de göreceksiniz. Bu, Interface yönetim web'ine erişmek için tarayıcınıza girmeniz gereken Address'tür.



**Not**: Dahili ağınız farklı bir Address aralığı kullanıyorsa, ortamınıza uygun bir IP Address atamak için menüden "**2)** Set Interface(s) IP Address" öğesini seçin.



Varsayılan olarak, Interface WAN'ınız DHCP ile yapılandırılmış bir kutuya veya modeme bağlıysa, pfSense otomatik olarak bir genel IP Address alacaktır. Bu nedenle, pfSense Interface LAN'a bir istemci bağlayarak anında İnternet erişiminden yararlanabilirsiniz.



## V. Interface web'e ilk erişim



İlk başlatma tamamlandıktan ve ağ arayüzleri yapılandırıldıktan sonra, yapılandırmanızı sonlandırmak ve ince ayar yapmak için pfSense'in Interface web'ine erişebilirsiniz.



### 1. İlk bağlantı



LAN bağlantı noktasına (veya hipervizörünüzdeki sanal Interface LAN'a) bir bilgisayar bağlayın ve gerekirse aynı aralıkta bir IP Address atayın (varsayılan olarak, pfSense LAN'da DHCP aracılığıyla otomatik olarak bir Address dağıtır).



Tarayıcınızda, konsol tarafından belirtilen Address'e gidin (varsayılan olarak `https://192.168.1.1`). PfSense'in ilk bağlantı için bile HTTPS gerektirdiğini unutmayın - bu nedenle, bir istisna ekleyerek göz ardı edebileceğiniz kendinden imzalı bir sertifika uyarısı bekleyin.



Oturum açma ekranı görünür. Varsayılan kimlik bilgileri:




- Kullanıcı adı:** `admin`
- Şifre:** `pfsense`



Bu tanımlayıcılar ilk yapılandırma sihirbazı sırasında değiştirilecektir.



## VI. Kurulum Sihirbazı



İlk bağlantıda, pfSense sizden **Kurulum Sihirbazını** takip etmenizi ister. Tüm temel parametrelerin doğru tanımlandığından emin olmak için bunu kullanmanızı şiddetle tavsiye ederiz.



### 1. Genel parametreler



Yapabilirsin:




- Bir ana bilgisayar adı ve yerel etki alanı belirtin (örnek: `pfsense` ve `lan.local`).
- DNS sunucularını tanımlayın ve pfSense'in ISP'nizin DNS'sini mi yoksa harici bir hizmeti mi (Cloudflare, OpenDNS, Quad9...) kullanacağını seçin.



### 2. Saat dilimi



Günlüklerin ve programların tutarlı olması için sitenizin saat dilimini belirtin (örn. `Avrupa/Paris`).



### 3. WAN yapılandırması



WAN bağlantısını yapılandırma:




- Varsayılan olarak **DHCP** (bir kutunun arkasındaysanız yeterlidir).
- Sabit bir IP'niz varsa, parametreleri (statik IP, maske, ağ geçidi, DNS) manuel olarak girin.
- Gerekirse, bir VLAN veya PPPoE kimlik doğrulaması tanımlayın (bazı İSS'lerde yaygındır).



### 4. LAN yapılandırması



Sihirbaz, varsayılan LAN alt ağını değiştirmenizi önerir. Belirli bir adresleme planınız varsa, şimdi bunu uyarlamanın tam zamanı.



### 5. Yönetici şifresini değiştirme



Hemen `admin` kullanıcısı için güçlü bir parola belirleyerek pfSense'inizin güvenliğini sağlayın.



## VII. Doğrulama ve güncellemeler



Güvenlik duvarınızı dağıtmadan önce, en son:





- Sistem > Güncelle** öğesine gidin.
- Güncelleme kanalını seçin (genellikle **Stable**).
- Güncellemeleri kontrol edin ve uygulayın.



Güvenlik yamaları hakkında bilgi sahibi olmanızı sağlamak için güncelleme bildirimlerini etkinleştirmek iyi bir fikirdir.



## VIII. Yapılandırmayı kaydetme



Herhangi bir büyük değişiklik yapmadan önce bir yedekleme politikası uygulayın:





- Diyagnostikler > Yedekleme ve Geri Yükleme** bölümüne gidin.
- Geçerli yapılandırmanın bir kopyasını indirin (`config.xml`).
- Güvenli bir yerde saklayın (şifrelenmiş harici medya).



Görev açısından kritik ortamlar için, harici bir sunucuda veya programlanmış bir komut dosyası aracılığıyla otomatik yapılandırma yedeklemesini düşünün.



## IX. Kurulum sonrası en iyi uygulamalar



Görevinizi gönül rahatlığıyla sonlandırmak için:





- Güvenlik duvarı kurallarını değiştirin**: pfSense varsayılan olarak LAN'da tüm giden trafiğe izin verir ve WAN'da gelen trafiği engeller. Bu kuralları gerektiği gibi ayarlayın.
- Güvenli uzaktan erişimi yapılandırın**: Gerekirse, Interface web'e WAN'dan yalnızca VPN aracılığıyla veya IP kısıtlamalarıyla erişimi etkinleştirin.
- Bildirimleri etkinleştir**: uyarıları (arızalar, güncellemeler, hatalar) almak için bir SMTP sunucusu yapılandırın.
- Yararlı uzantıları yükleyin**: örneğin, IDS/IPS (Snort, Suricata), proxy (Squid), DNS filtreleme (pfBlockerNG).



PfSense güvenlik duvarınız artık çalışır durumda ve ağınızı korumaya hazır. Esnekliği ve aktif topluluğu sayesinde, gelecekteki ihtiyaçlarınıza (çoklu WAN, VLAN, siteden siteye VPN, captive portal vb.) uyum sağlayabilecek güçlü, ölçeklenebilir bir araca sahipsiniz.



Yeni özellikleri keşfetmek ve yapılandırmanızın güncel ve güvenli olduğundan emin olmak için düzenli olarak resmi belgelere ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) başvurun.