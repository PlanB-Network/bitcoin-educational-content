---
name: Angry IP Scanner
description: Ağınızı taramanın basit bir yolu
---
![cover](assets/cover.webp)



___



*Bu eğitim Florian BURNEL tarafından [IT-Connect](https://www.it-connect.fr/) adresinde yayınlanan orijinal içeriğe dayanmaktadır. Lisans [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Orijinal metinde değişiklikler yapılmış olabilir.*



___



## I. Sunum



Bir Windows ağını bağlı makineler için hızlı ve kolay bir şekilde nasıl tararsınız? Cevap Angry IP Scanner. Bu açık kaynaklı proje, kullanımı kolay bir grafik Interface kullanarak bir ağı kolayca taramanızı sağlar.



Bu araç bireyler tarafından **yerel ağlarını** taramak için kullanılabileceği gibi BT uzmanları tarafından da aynı amaçla kullanılabilir. Bu aracın **çok pratik** olduğunun kanıtı, **bazı siber suç grupları** tarafından kurumsal ağları taramak için zaten kullanılmış olmasıdır (Nmap ile aynı şekilde). İyi bir örnek [fidye yazılımı grubu RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Hala sağlam bir yazılım parçasıdır, ancak diğer ağ ve güvenlik odaklı araçlarda olduğu gibi, kullanımı kötüye kullanılabilir.



Burada, **Windows 11** üzerinde kullanacağız, ancak **Windows'un** diğer sürümlerinin yanı sıra **Linux** ve **macOS** üzerinde de kullanmak tamamen mümkündür.



Nmap'ten daha az kapsamlı olan **Angry IP Scanner**, hızlı, temel bir ağ analizi için hala ilginçtir, ancak aynı zamanda herkesin erişebileceği bir yerde olduğu için. Ağa bağlı ana bilgisayarları tespit edecek ve **ana bilgisayar adlarını** ve **açık bağlantı noktalarını** belirleyecektir.



Daha ileri gitmek isterseniz, Nmap hakkındaki eğitime bakın:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Angry IP Scanner ile çalışmaya başlama



### A. Angry IP Scanner'ı indirin ve yükleyin



Angry IP Scanner'ın en son sürümünü uygulamanın resmi web sitesinden veya GitHub'dan indirebilirsiniz. Biz ikinci seçeneği kullanacağız. Aşağıdaki bağlantıya tıklayın ve EXE sürümünü indirin: "**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Kuruluma devam etmek için yürütülebilir dosyayı çalıştırın. Kurulum sırasında yapılacak özel bir şey yoktur.



![Image](assets/fr/013.webp)



### B. İlk ağ taramasını çalıştırın



İlk çalıştırmada, aracın nasıl çalıştığı hakkında daha fazla bilgi edinmek için "**Getting Started**" penceresindeki talimatları okumak için zaman ayırın. Bu arada, dikkate alınması gereken birkaç terim var:





- **Besleyici**: rastgele bir IP aralığından veya IP adreslerinin listesini içeren bir dosyadan taranacak IP adreslerinin listesini oluşturmaktan sorumlu modül.
- **Getirici**: ağdaki ana bilgisayarlar hakkında bilgi almak için bir dizi modül. Örneğin, MAC adreslerini tespit etmek, portları taramak, ana bilgisayar adlarını tespit etmek veya HTTP istekleri göndermek için getiriciler vardır.



![Image](assets/fr/018.webp)



Bir IP alt ağını taramak için, "**IP aralığı**" alanına **başlangıç IP Address** ve **son IP Address** girin (aksi takdirde, sağdaki türü değiştirin). Ardından "**Başlat**" düğmesine tıklayın.



![Image](assets/fr/019.webp)



Birkaç on saniye sonra, sonuç yazılımın Interface'sinde görülebilecektir. **Analiz edilen aralıktaki her IP Address için Angry IP Scanner'ın bir ana bilgisayar tespit edip etmediğini göreceksiniz.** Ekranda ayrıca aktif ana bilgisayar sayısını (bu durumda 6) ve açık bağlantı noktalarına sahip ana bilgisayar sayısını gösteren bir özet görünecektir.



![Image](assets/fr/020.webp)



Burada, IP Address "**192.168.10.1**" ile ilişkili ve **port 80** ve **443** (HTTP ve HTTPS) üzerinden erişilebilen "**OPNsense.local.domain**" adlı bir ana bilgisayarın varlığını görebiliriz. Ana bilgisayara sağ tıklamak, bu IP Address üzerinden ping, trace route ve tarayıcı açma gibi ek komutlara erişim sağlar.



![Image](assets/fr/012.webp)



### C. Tarama bağlantı noktaları ekleyin



Varsayılan olarak, **Angry IP Scanner** 3 portu tarayacaktır: **80** (HTTP), **443** (HTTPS) ve **8080**. Uygulama tercihlerinden taranacak daha fazla bağlantı noktası ekleyebilirsiniz. "**Araçlar**" menüsüne ve ardından "**Portlar**" sekmesine tıklayın.



Burada, "**Port seçimi**" seçeneği aracılığıyla port listesini değiştirebilirsiniz. Virgülle ayrılmış belirli bağlantı noktası numaralarını veya bağlantı noktası aralıklarını belirtebilirsiniz. Aşağıdaki örnekte iki bağlantı noktası eklenmiştir: **445** (SMB) ve **389** (LDAP). 1'den 1000'e kadar olan bağlantı noktalarını taramak için "**1-1000**" girin. Bağlantı noktası taramalarının TCP, UDP veya her ikisinde de gerçekleştirilip gerçekleştirilmeyeceği belirtilmez.



![Image](assets/fr/021.webp)



Taramayı tekrar çalıştırırsanız, muhtemelen yeni bilgiler elde edersiniz. Aşağıdaki örnekte Angry IP Scanner, taranacak bağlantı noktalarının yeni yapılandırması sayesinde "**SRV-ADDS-01**" ve "**SRV-ADDS-02**" ana bilgisayarlarında 389 ve 445 numaralı bağlantı noktalarının açık olduğunu söylüyor.



![Image](assets/fr/022.webp)



**Not**: "**Tarayıcı**" menüsünden tarama sonuçlarını bir metin dosyasına aktarabilirsiniz.



Taramayı daha da ileri götürmek isterseniz, "**Araçlar**" menüsüne tıklayın, ardından "**Fetchers**" seçeneğine tıklayın. Bu, taramaya "yetenekler" ekler. Basitçe bir getirici seçin ve etkinleştirmek için sola taşıyın. Bu, tarama sonucuna ekstra bir sütun ekleyecektir.



![Image](assets/fr/014.webp)



Aşağıdaki örnekte "**NetBIOS info**" ve "**Web detection**" fonksiyonları gösterilmektedir. İlki, makinenin MAC Address ve alan adı gibi ek bilgiler sağlarken, ikincisi web sayfası başlığını (web sunucusu veya uygulama türü hakkında bazı bilgiler verebilir) görüntüler.



![Image](assets/fr/011.webp)



Son olarak, tercihlerden "**ping**" için kullanılan yöntemi de değiştirebilirsiniz, yani bir ana bilgisayarın aktif olup olmadığını değerlendirmek için. Bazı ana bilgisayarlar pinglere yanıt vermediğinden, bu diğer yöntemleri (UDP paketi, TCP port probu, ARP, UDP + TCP kombinasyonu, vb.)



## III. Sonuç



Basit ve etkili: Angry IP Scanner bir ağa bağlı ana bilgisayarları tespit eder ve port taramalarını yapılandırmanıza izin verir. Seçenekler açısından, Nmap kadar esnek değildir ve o kadar ileri gitmez, ancak hızlı tarama için iyi bir başlangıçtır.



Grafiksel bir Interface ile **Nmap** kullanmak isterseniz, **Zenmap uygulamasını** kullanabilirsiniz (aşağıdaki genel bakışa bakın).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d