---
name: WireGuard
description: Debian ve Windows üzerinde WireGuard VPN kurulumu
---
![cover](assets/cover.webp)



___



*Bu eğitim Florian BURNEL tarafından [IT-Connect](https://www.it-connect.fr/) adresinde yayınlanan orijinal içeriğe dayanmaktadır. Lisans [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Orijinal metinde değişiklikler yapılmış olabilir.*



___



## I. Sunum



Bu eğitimde, güvenliği ihmal etmeden performansı artıran ücretsiz, açık kaynaklı bir VPN çözümü olan WireGuard'ı temel alan bir VPN'i nasıl yapılandıracağımızı öğreneceğiz.



WireGuard, Mart 2020'den bu yana kararlı bir sürüm olarak mevcut olan nispeten yeni bir çözümdür ve 5.6** sürümünden bu yana doğrudan **Linux çekirdeğine entegre olma onuruna sahiptir. Bu, çekirdeğin farklı bir sürümünü kullanan eski Linux dağıtımlarından erişilebilir olmasını engellemez. OpenVPN ve IPSec gibi çözümlerle karşılaştırıldığında, WireGuard'ın kullanımı daha basit ve bu makalenin sonunda göreceğimiz gibi çok daha hızlıdır.



WireGuard hakkında bazı önemli noktalar:





- Basit, hafif ve ultra verimli!
- Yalnızca UDP çalışması (belirli güvenlik duvarlarını aşarken dezavantaj olabilir)
- İstemci-sunucu modeli yerine eşler arası modelde çalışır
- Exchange anahtarıyla kimlik doğrulama, özel/genel anahtarlarla SSH ile aynı prensipte
- Çeşitli algoritmaların kullanımı: ChaCha20 ile simetrik şifreleme, Poly1305 ile mesaj doğrulama ve Curve25519, BLAKE2 ve SipHash24 gibi diğerleri
- Hem IPv4 hem de IPv6'yı destekler
- Çoklu platform: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (ve ProtonVPN'de uygulanmaktadır)
- Diğer çözümlerdeki yüz binlerce satırlık koda kıyasla yalnızca 4.000 satırlık kod



Kriptografik kısım için, kullanılan çeşitli algoritmalar özenle seçilmiş, çeşitli şekillerde denetlenmiş ve alanında uzman güvenlik araştırmacıları tarafından incelenmiştir.



Resmi proje web sitesi: [wireguard.com](https://www.wireguard.com/)



Bu girişi okuduktan sonra bu çözüme ikna oldunuz mu? Geriye kalan tek şey okumaya devam etmek!



## II. Lab WireGuard şeması



WireGuard'ın kurulumuna ilişkin laboratuvarımı sunmadan önce, WireGuard'ı **iki uzak altyapıyı birbirine bağlamak için**, aynı zamanda **uzak bir istemciyi kurumsal ağ veya ev ağınız gibi bir altyapıya bağlamak için** kullanabileceğinizi bilmelisiniz. Bu, yakın zamanda "[Synology üzerinde OpenVPN] (https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)" eğitiminde gördüğümüz gibi OpenVPN ile aynı ruha sahiptir.



WireGuard, OpenWRT'de olduğu gibi doğrudan yönlendirici veya güvenlik duvarı üzerinde kurulmamışsa, akışın WireGuard çiftine ulaşması için bağlantı noktası yönlendirmeyi ayarlamanız gerekecektir.



![Image](assets/fr/034.webp)



Şimdi size laboratuvarımdan ve bugün ne kuracağımızdan bahsedeceğim.



WireGuard sunucusu olarak bir Debian 11 makinesi ve WireGuard VPN istemcisi olarak da bir Windows istemcisi kullanacağım. İstemci-sunucu ilişkisinden bahsetmek biraz yanıltıcı olsa da, **WireGuard "eşler arası "** bir model üzerinde çalışır. "İstemciden siteye" bir bağlantı kurmaya çalıştığınızda bu biraz yanlış bir isimlendirmedir. Bunun yerine diyelim ki iki çift ya da **iki WireGuard bağlantı noktam** olacak: biri Debian 11 altında ve diğeri Windows altında.



Bu iki çift birbirleriyle her iki yönde de iletişim kurabilir, yani Windows makinemden Debian 11 makinesinin uzak LAN'ına erişebilirim veya tam tersi: hepsi tünelin yapılandırmasına ve WireGuard eşinin güvenlik duvarına bağlıdır.



Bu örnekte, aşağıdaki duruma odaklanacağım: **Ev ağıma bağlı Windows Peer 1 cihazımdan, WireGuard VPN tüneli aracılığıyla şirket sunucularına erişmek için şirket ağıma erişmek istiyorum**. Bu aşağıdaki diyagramı verir:



![Image](assets/fr/035.webp)



IP adresleri açısından bu,:





- Ev ağı**: 192.168.1.0/24
- Kurumsal ağ**: 192.168.100.0/24
- WireGuard tünel ağı**: 192.168.110.0/24


+ Tüneldeki Eş 1'in (Windows) IP Address'i: 192.168.110.2/24


+ Tüneldeki Eş 2'nin (Debian) IP Address'si: 192.168.110.121/24



Hepsi bu kadar! Hadi yapılandırmaya geçelim!



**Not: WireGuard varsayılan olarak **port 51820** üzerinde UDP modunda çalışır.



## III WireGuard sunucu kurulumu ve yapılandırması



Bu eğitimde Windows makinesi için "istemci" ve Debian makinesi için "sunucu" terimlerini kullanacağım, çünkü eşler arası olsa da bu daha anlamlı görünüyor.



### A. Debian 11 üzerinde WireGuard Kurulumu



WireGuard kurulum paketi resmi Debian 11 depolarında mevcuttur, bu nedenle tek yapmamız gereken paket önbelleğini güncellemek ve kurmaktır:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



WireGuard sunucu kısmı, yapılandırmayı yönetmek için yararlı komutlara erişim sağlayan çeşitli araçlarla birlikte kurulacaktır.



### B. Interface WireGuard'ın Kurulumu



"wg "** komutunu kullanarak generate'e bir özel anahtar ve bir açık anahtar eklememiz gerekir: iki çift, yani sunucu ve bir istemci (aynı zamanda bir anahtar çiftine ihtiyaç duyacak olan) arasında kimlik doğrulama için gereklidir.



Bu komut dizisi ile özel anahtar "**/etc/wireguard/wg-private.key**" ve genel anahtar "**/etc/wireguard/wg-public.key**" oluşturacağız:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



Açık anahtarın değeri konsolda döndürülecektir. WireGuard yapılandırma dosyasına **özel anahtarımızın değerini** eklememiz gerekir. Bu değeri almak için aşağıdaki komutu girin ve değeri kopyalayın:



```
sudo cat /etc/wireguard/wg-private.key
```



Şimdi sıra "**/etc/wireguard/**" içinde bir yapılandırma dosyası oluşturmaya geldi. Örneğin, WireGuard ile ilişkili Interface ağının "eth0" ile aynı prensipte "wg0" olacağını düşünürsek, bu dosyayı "**wg0.conf**" olarak adlandırabiliriz.



```
sudo nano /etc/wireguard/wg0.conf
```



Bu dosyaya öncelikle aşağıdaki içeriği eklemeliyiz (daha sonra tamamlamak için geri döneceğiz):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



Bölüm `[Interface]` sunucu kısmını bildirmek için kullanılır. İşte bazı bilgiler:





- Address**: VPN tüneli içindeki Interface WireGuard'ın IP Address'i (uzak LAN'dan farklı alt ağ)
- SaveConfig**: yapılandırma Interface etkin olduğu sürece saklanır (ve korunur)
- ListenPort**: WireGuard'ın dinleme portu. Bu durumda, 51820 varsayılan bağlantı noktasıdır, ancak bunu özelleştirebilirsiniz
- PrivateKey**: sunucumuzun özel anahtarının değeri (*wg-private.key*)



Dosyayı kaydedin ve kapatın. "**wg-quick**" komutuyla, bu Interface'u adını belirterek başlatabiliriz (dosya wg0.conf olarak adlandırıldığı için wg0):



```
sudo wg-quick up wg0
```



Debian 11 sunucunuzun IP adreslerini listelerseniz, yapılandırma dosyasında tanımlanan IP Address ile "wg0" adlı yeni bir Interface göreceksiniz:



```
ip a
```



![Image](assets/fr/027.webp)



Aynı şekilde, Interface "wg0" yapılandırmasını "wg show" komutu aracılığıyla görüntüleyebiliriz:



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Son olarak, Interface wg0 WireGuard'ımızın otomatik olarak başlatılmasını etkinleştirmemiz gerekiyor:



```
sudo systemctl enable wg-quick@wg0.service
```



Şimdilik, WireGuard'ın sunucu tarafının yapılandırmasını bir kenara bırakacağız.



### C. IP Yönlendirmeyi Etkinleştir



Debian 11 makinemizin **paketleri farklı ağlar arasında (bir yönlendirici gibi)**, yani VPN ağı ile yerel ağ arasında yönlendirebilmesi için [IP Yönlendirme] (https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/) özelliğini etkinleştirmemiz gerekir. Varsayılan olarak bu özellik devre dışıdır.



Bu yapılandırma dosyasını değiştirin:



```
sudo nano /etc/sysctl.conf
```



Aşağıdaki yönergeyi dosyanın sonuna ekleyin ve kaydedin:



```
net.ipv4.ip_forward = 1
```



Hepsi bu kadar.



### D. IP Maskeli Baloyu Etkinleştir



Sunucumuzun paketleri doğru bir şekilde yönlendirmesi ve uzak LAN'ın Windows makinesine erişebilmesi için Debian sunucumuzda IP Masquerade'i etkinleştirmemiz gerekir. Bu bir çeşit NAT aktivasyonudur. Bu yapılandırmayı Linux güvenlik duvarı üzerinde, kullanmaya alışık olduğum UFW üzerinden gerçekleştireceğim ([ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Eğer UFW'ye sahip değilseniz ve kurmak istiyorsanız (Nftables'ı da kullanabilirsiniz),:



```
sudo apt install ufw
```



Öncelikle, uzak sunucunun kontrolünü kaybetmemek için SSH'yi etkinleştirmeniz gerekir (bağlantı noktası numarasını uyarlayın):



```
sudo ufw allow 22/tcp
```



WireGuard için kullandığımız için UDP'deki 51820 numaralı bağlantı noktası da yetkilendirilmelidir (yine bağlantı noktası numarasını uyarlayın):



```
sudo ufw allow 51820/udp
```



Daha sonra, IP maskelemeyi etkinleştirmek için yapılandırmaya devam edeceğiz. Bunu yapmak için, yerel ağa bağlı Interface'in adını almamız gerekiyor. Eğer adını bilmiyorsanız, kartın adını görmek için "ip a" komutunu çalıştırın. Benim durumumda, bu "**ens192**" kartıdır.



![Image](assets/fr/036.webp)



Bu bilgiyi kullanacağız. Aşağıdaki dosyayı düzenleyin:



```
sudo nano /etc/ufw/before.rules
```



Yerel güvenlik duvarımızın NAT tablosunun POSTROUTING dizesi içinde **Interface ens192** (Interface adını uyarlayın) üzerinde IP masquerade'i etkinleştirmek için dosyanın sonuna bu satırları ekleyin:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



Resim gösteriyor:



![Image](assets/fr/037.webp)



Bu yapılandırma dosyasını açık tutun ve bir sonraki adıma geçin. 😉



### E. WireGuard için Linux güvenlik duvarı yapılandırması



Yine aynı yapılandırma dosyasında, şirket ağını "192.168.100.0/24" olarak bildireceğiz, böylece onunla iletişim kurabileceğiz. İşte eklenecek iki kural (ideal olarak kuralları birlikte gruplamak için "*# ok icmp code for FORWARD*" bölümünden sonra):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Yalnızca bir ana bilgisayarı, örneğin "192.168.100.11" yetkilendirmek istiyorsanız, bu kolaydır:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Şimdi dosyayı kaydedebilir ve kapatabilirsiniz. Geriye kalan tek şey UFW'yi etkinleştirmek ve değişikliklerimizi uygulamak için hizmeti yeniden başlatmaktır:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Debian sunucu yapılandırmasının ilk bölümü artık tamamlanmıştır.



## IV. Windows için WireGuard istemcisi



WireGuard istemcisi Windows, macOS, Android vb. için kullanılabilir. Bu harika bir haber. Tüm indirmeler bu sayfada mevcuttur: [WireGuard İstemcisi](https://www.wireguard.com/install/). Bu örnekte, istemciyi Windows üzerinde kuracağım. WireGuard istemcisini Linux'ta kurmak için, Debian makinesinde wg0.conf dosyasını oluşturmakla aynı prensibi izleyin (tüm NAT vb. olmadan).



### A. WireGuard Windows istemcisinin yüklenmesi



Yürütülebilir dosyayı veya MSI paketini indirdikten sonra, kurulum basittir: sadece yükleyiciyi başlatın ve... işte, tamam! 🙂



![Image](assets/fr/038.webp)



### B. WireGuard profili oluşturma



Yeni bir tünel oluşturmak için yazılımı açarak başlayın. Bunu yapmak için, "**Tünel ekle**" düğmesinin sağındaki oka tıklayın ve "**Boş tünel ekle**" düğmesine tıklayın.



![Image](assets/fr/028.webp)



Bir yapılandırma penceresi açılacaktır. Her yeni tünel yapılandırması oluşturulduğunda, WireGuard bu yapılandırmaya özgü bir özel/genel anahtar çifti oluşturur. **Bu yapılandırmada, "eş", yani uzak sunucuyu bildirmemiz gerekir:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Bu yapılandırmayı tamamlamamız, özellikle IP Address'i bu Interface (*Address*) üzerinde bildirmemiz ve aynı zamanda uzak WireGuard sunucusunu bir [Peer] bloğu aracılığıyla bildirmemiz gerekiyor. Aşağıdaki resim size Linux sunucu tarafında oluşturduğumuz yapılandırma dosyasını hatırlatacaktır.



Address "**192.168.110.2**" IP'sini ekleyerek `[Interface]` bloğu ile başlayalım; sunucunun bu ağ segmentinde Address "**192.168.110.121**" IP'sine sahip olduğunu unutmayın. Bu şunu verir:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Ardından, "Peer" bloğunu üç özellik ile bildirmemiz gerekir, bu da bu yapılandırma ile sonuçlanır:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



Resimlerde:



![Image](assets/fr/029.webp)



**Peer] bloğu hakkında birkaç açıklama:





- PublicKey**: WireGuard Debian 11 sunucusunun genel anahtarıdır ("*sudo wg*" komutu ile değerini elde edebilirsiniz)
- AllowedIPs**: bunlar bu WireGuard VPN ağı üzerinden erişilebilen IP adresleri / alt ağlardır, bu durumda WireGuard VPN'ime (*192.168.110.0/24*) ve uzak LAN'ıma (*192.168.100.0/24*) özel alt ağ
- Uç Nokta**: Bu, Debian 11 ana bilgisayarının IP Address'idir, çünkü bu bizim WireGuard bağlantı noktamızdır (genel IP Address'i belirtmeniz gerekir)



Son olarak, "**Name**" alanına bir isim girin (boşluk bırakmadan) ve istemcinin açık anahtarını kopyalayıp yapıştırın, çünkü bunu sunucuda beyan etmemiz gerekecek. "**Kayıt**" üzerine tıklayın.



### C. WireGuard sunucusunda istemci bildirme



WireGuard yapılandırmasında "**Peer**"ı, yani Windows bilgisayarımızı bildirmek için Debian sunucusuna dönme zamanı geldi. Her şeyden önce, yapılandırmasını değiştirmek için **Interface "wg0"**'ı durdurmamız gerekiyor:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Ardından, önceden oluşturulmuş yapılandırma dosyasını değiştirin:



```
sudo nano /etc/wireguard/wg0.conf
```



Bu dosyada, `[Interface]` bloğunun ardından, bir `[Peer]` bloğu bildirmemiz gerekir:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Bu [Peer] bloğu Windows 10 PC'nin açık anahtarını (**PublicKey**) ve PC'nin Address'inin IP Interface'ünü (**AllowedIPs**) içerir: sunucu bu WireGuard tünelinde yalnızca Windows istemcisiyle iletişim kurmak için iletişim kuracaktır, dolayısıyla "**192.168.110.2/32**" değeri.



Geriye kalan tek şey dosyayı kaydetmektir (*CTRL+O sonra Enter sonra Nano üzerinden CTRL+X*). Interface "wg0 "ı yeniden başlatın:



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Eş bildiriminin çalışıp çalışmadığını kontrol etmek için bu komutu kullanabilirsiniz:



```
sudo wg show
```



Uzak ana bilgisayar WireGuard bağlantısını kurduktan sonra, IP Address "uç nokta" değerine taşınacaktır.



![Image](assets/fr/033.webp)



Son olarak, kök erişimini sınırlamak için yapılandırma dosyalarını güvence altına alacağız:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. İlk WireGuard bağlantısı



Artık yapılandırma hazır olduğuna göre, Windows PC'den başlatabiliriz. Bunu yapmak için, "**WireGuard**" istemcisinde, "**Activate**" düğmesine tıklayın: bağlantı **"Off "dan "On "a** değişecektir, ancak bu çalışacağı anlamına gelmez. Her şey yapılandırmanızın doğru olup olmadığına bağlıdır. **Bağlantı kurulduğunda, iki makinemiz her iki tarafta yapılandırılmış Interface WireGuard aracılığıyla iletişim kurar!



![Image](assets/fr/030.webp)



Bir sorun olması durumunda, bu durum "**Logbook**" sekmesinde görülebilecektir. İki ana bilgisayar, bağlantının durumunu kontrol etmek için düzenli olarak Exchange paketleri gönderecektir, dolayısıyla "*Receiving keepalive packet from peer 1*" mesajları.



![Image](assets/fr/031.webp)



WireGuard'ın "**Journal**" sekmesinde aşağıdaki gibi bir mesaj görüntüleniyorsa, her iki tarafta da beyan edilen açık anahtarların doğru olup olmadığını kontrol etmeniz gerekir.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Uzak bilgisayarımdan, sunucu tarafındaki Interface WireGuard'ımın IP Address'ine ve uzak LAN'ımdaki bir ana bilgisayara ping atabiliyorum.



![Image](assets/fr/032.webp)



### E. Performans: OpenVPN vs WireGuard



WireGuard VPN'ime bağlı uzak bilgisayarımdan bir dosya sunucusuna erişip [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/) üzerinden bir dosya aktarabildim ve aktarım hızını görebildim. **WireGuard ile en fazla 45 Mb/s hızına çıkabiliyorum ki bu da WiFi kullandığım için harika



![Image](assets/fr/025.webp)



Aynı koşullar altında, ancak bu kez bir OpenVPN bağlantısı (UDP'de) aracılığıyla, aynı işlemle, verim tamamen farklıdır: yaklaşık 3 MB / s. Aradaki fark çok açık!



![Image](assets/fr/026.webp)



Bu ilginçtir, çünkü örneğin bir WiFi bağlantısından 4G/5G bağlantısına geçerseniz, yeniden bağlantı o kadar hızlı olacaktır ki kesinti görünmeyecektir.



### F. Bonus: tam tünel WireGuard



Mevcut yapılandırmayla, trafiğin bir kısmı VPN üzerinden, geri kalanı ise İnternet'te gezinme dahil olmak üzere müşterinin İnternet bağlantısı üzerinden akar. WireGuard **tam tünel moduna** geçmek istiyorsak, böylece her şey VPN tünelinden geçecekse, yapılandırmamızda birkaç değişiklik yapmamız gerekir....



İlk olarak, "resolvconf" paketini:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Bu yapıldıktan sonra, Debian makinesindeki "wg0.conf" profilini değiştirmeniz gerekir: Interface'yi durdurun, değiştirin ve yeniden başlatın.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Ardından, **[Interface]` bloğunda, kullanılacak DNS sunucusunu ekliyoruz**. Benim durumumda, laboratuvarımın etki alanı denetleyicisi, ancak yerel bir çözümleyiciye sahip olmak için Debian makinesine Bind9 da yükleyebiliriz.



```
DNS = 192.168.100.11
```



Dosyayı kaydedin, ardından Interface'ü yeniden başlatın:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Son olarak, Windows 10 iş istasyonundaki tünel yapılandırmasında, her şeyin tünelden geçmesi gerektiğini belirtmek için "AllowedIPs" bölümünü değiştirmeniz gerekir. Değiştirin:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Tarafından:



```
AllowedIPs = 0.0.0.0/0
```



Bunun aynı zamanda "**Öldürme anahtarı*" seçeneğini de etkinleştirdiğini görebilirsiniz.



![Image](assets/fr/040.webp)



Son olarak, bu dolu tünelden yararlanarak, sonuçları aşağıda gösterilen küçük bir akış testi gerçekleştirdim:



![Image](assets/fr/039.webp)



WireGuard'ın konfigürasyonu oldukça basit ve anlaşılması kolaydır ve her şeyden önce bakımı kolaydır. **WireGuard VPN'lerin geleceği olarak görülüyor**, bu yüzden onu yakından takip etsek iyi olur! OpenVPN ile karşılaştırıldığında WireGuard için büyük bir avantaj olan performans açısından da önemli bir fayda olduğunu görebiliyoruz.



Ek belgeler:





- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - Command wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**WireGuard VPN'iniz hazır ve çalışıyor! Tebrikler!