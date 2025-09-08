---
name: Nmap
description: Ağ haritalama ve güvenlik açığı taraması için Master Nmap
---

![cover](assets/cover.webp)



*Bu eğitim Mickael Dorigny tarafından [IT-Connect](https://www.it-connect.fr/) adresinde yayınlanan orijinal içeriğe dayanmaktadır. Lisans [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Orijinal metinde değişiklikler yapılmıştır.*



___



Bu güçlü ağ tarama aracında uzmanlaşmak isteyen herkes için tasarlanmış Nmap'e giriş niteliğindeki bu eğitime hoş geldiniz. Amaç, Nmap'i günlük olarak etkili bir şekilde kullanmanız için gereken temel bilgileri size sağlamaktır.



Nmap, BT, ağ ve siber güvenlik uzmanları tarafından tanılama, ağ keşfi ve güvenlik denetimi için yaygın olarak kullanılan çok yönlü bir araçtır. Bu eğitim, bu alanlarda yeni olan ve Nmap'in temellerini öğrenmek isteyenlere yöneliktir. Temel bir sistem ve ağ yönetimi bilgisi tavsiye edilir.



Nmap'in temellerini, port taramalarını nasıl yapacağınızı, bir ağdaki aktif ana bilgisayarları nasıl belirleyeceğinizi, hizmet sürümlerini ve işletim sistemlerini nasıl tespit edeceğinizi, güvenlik açığı taramalarını nasıl gerçekleştireceğinizi ve çok daha fazlasını öğreneceksiniz. Her bölüm, çeşitli bağlamlarda Nmap kullanımında ustalaşmanıza yardımcı olacak ayrıntılı açıklamalar ve pratik örnekler içerir.



Bu eğitimin sonunda, Nmap hakkında sağlam bir anlayışa sahip olacak ve ağlarınızın güvenliğini ve yönetimini iyileştirmek için etkili bir şekilde kullanabileceksiniz. Keyifli okumalar.



## 1 - Nmap'e Giriş: Nmap nedir?



### I. Sunum



Bu ilk bölümde, Nmap ağ tarama aracına bir göz atacağız. Bu araç hakkında bilmeniz gereken temel Elements'a ve genel olarak nasıl çalıştığına bakacağız. Bu, eğitimin geri kalanını daha iyi anlamamıza yardımcı olacaktır.



### II. Nmap aracının tanıtılması



Nmap, _Network Mapper_ için, **ağ keşfi, haritalama ve güvenlik denetimi** için kullanılan ücretsiz, açık kaynaklı bir araçtır. Ayrıca **ağ envanteri, tanılama veya denetim** gibi diğer görevler için de kullanılabilir.



Hedeflenen bir ağdaki ana bilgisayarların aktif ve erişilebilir olup olmadığını, hangi ağ hizmetlerinin açıkta olduğunu, hangi sürümlerin ve teknolojilerin kullanıldığını ve diğer yararlı analiz bilgilerini belirleyebilir. Nmap, belirli bir makinedeki tek bir hizmeti veya tüm İnternet'e kadar ağın geniş alanlarını taramak için kullanılabilir.



Nmap'in güçlü yönleri çoktur:





- Güçlü ve esnek**: Nmap büyük ağları tarayabilir ve gelişmiş algılama teknikleri kullanabilir. UDP, TCP, ICMP, IPv4 ve IPv6'yı destekler ve sürüm tespiti, güvenlik açığı taramaları veya protokole özgü etkileşimler gerçekleştirebilir. Mimarisi modülerdir, özellikle bu eğitimin ilerleyen bölümlerinde inceleyeceğimiz NSE (Nmap Scripting Engine) komut dosyaları sayesinde.
- Kullanım kolaylığı**: resmi belgeler bol miktarda ve en yüksek kalitede. Başlamanıza yardımcı olacak çok sayıda topluluk kaynağı da mevcuttur.
- Popülerlik ve uzun ömürlülük**: Nmap 1998'den beri kendi alanında bir referans olmuştur. Bu güncelleme sırasında geçerli sürüm 7.95'tir. Belirli görevler için başka araçlar mevcut olsa da, Nmap ağ haritalama ve analizi için sahip olunması gereken bir araç olmaya devam etmektedir.



**Sinemada Nmap**



Nmap, halk arasında belli bir şöhrete sahip olan birkaç güvenlik aracından biridir. Matrix Reloaded_ filminde Trinity'nin bir sistemi hacklemek için kullandığı sembolik bir sahnede yer almaktadır:



![nmap-image](assets/fr/01.webp)



matrix: Nmap içeren Reloaded sahnesi



Ayrıca başka sinematografik çalışmalarda da yer alır.



**Geri bildirim



Bir sistem yöneticisi ve daha sonra siber güvenlik denetçisi ve pentester olarak **Nmap'i neredeyse her gün kullanıyorum** ve ağlara hakimiyetlerini güçlendirmek ve teşhis yeteneklerini geliştirmek isteyen sistem yöneticilerine **düzenli olarak tavsiye ediyorum**.



### III. Üst düzey operasyon



Nmap Linux, Windows ve macOS için kullanılabilir. Esas olarak C, C++ ve Lua (NSE komut dosyaları için) dillerinde yazılmıştır. Zenmap gibi grafik arayüzler de mevcut olmasına rağmen, esas olarak komut satırında kullanılır. Ancak, nasıl çalıştığını daha iyi anlamak için komut satırıyla başlamanızı şiddetle tavsiye ederiz.



Basit bir örnek:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Bu komut daha sonra ayrıntılı olarak açıklanacaktır. Bu eğitimde, Nmap'i Linux'ta kullanacağız, ancak diğer sistemlerde de benzer şekilde kullanılmaktadır. Windows altında, Nmap ağ paketlerini yakalamak ve enjekte etmek için **Npcap** kütüphanesine (artık kullanılmayan WinPcap'in yerine) dayanır.



Nmap, `ls` veya `ip` gibi geleneksel bir ikili gibi kullanılır. Araç bazen hedef sistemlerde belirli tepkileri kışkırtmak için paketleri alışılmadık şekillerde manipüle ettiğinden (özellikle hizmet veya güvenlik açığı tespiti için) bazı gelişmiş özellikler yükseltilmiş haklar gerektirebilir.



### IV. Nmap kullanmanın etkileri



Nmap'i kullanmadan önce, ağlar ve sistemler üzerindeki potansiyel etkisinin farkında olmak çok önemlidir:





- Kısa bir süre içinde **binlerce hatta milyonlarca paket** gönderebilir ve bu da belirli ağ altyapılarını doyurabilir.
- generate **yanlış biçimlendirilmiş veya standart olmayan** paketler oluşturabilir, bu da belirli ekipmanları (özellikle endüstriyel sistemleri) bozabilir.
- Güvenlik sistemlerinde (güvenlik duvarları, IDS/IPS, vb.) uyarıları tetikleyebilecek **saldırı benzeri davranışlar** üretebilir.



Genel olarak konuşmak gerekirse, **Nmap çok konuşkan bir araçtır**, çünkü mümkün olduğunca fazla bilgi elde etmek için çok fazla trafik oluşturur. Bu nedenle, hassas veya üretim ortamlarında kullanmadan önce nasıl çalıştığını tam olarak anlamanız tavsiye edilir.



### V. Sonuç



Bu bölümde Nmap ve ana özellikleri tanıtılmaktadır. Temel, güçlü ve esnek bir ağ haritalama aracı olduğunu gördük. Ayrıca nasıl çalıştığını ve onu kullanırken almanız gereken önlemleri tartıştık ve eğitimin sonraki bölümleri için sahneyi hazırladık.



## 2 - Neden Nmap kullanılmalı?



### I. Sunum



Bu bölümde, Nmap ağ tarama aracının ana kullanım alanlarına bir göz atacağız. Birçok bağlamda ve meslekte yaygın olarak kullanılan bir araç olduğunu ve alet çantanızda bulundurmanın ve nasıl ustalaşacağınızı bilmenin kesinlikle yararlı bir beceri olduğunu göreceğiz.



### II. Teşhis ve denetim için Nmap kullanımı



Nmap ağ tanılama ve daha geniş anlamda izleme için kullanılabilir. İki ana bilgisayarın iletişim kurup kurmadığını belirlemek için bir ping'in kullanılabilmesi gibi, Nmap de bir ana bilgisayarın aktif olup olmadığını veya belirli bir hizmetin çalışıp çalışmadığını hızlı bir şekilde belirlemek için kullanılabilir. Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap") sayesinde, bir ana bilgisayarın yanıt süresi, paketlerin izlediği yol, belirli bir hizmet tarafından verilen yanıt vb. ile ilgili kesin veriler elde edebiliriz.



Örneğin, **192.168.1.18** ana bilgisayarındaki bir web sunucusunun etkin olup olmadığını ve doğru yanıt verip vermediğini hızlı bir şekilde öğrenmek için aşağıdaki komut ve sonuç kullanılabilir:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Uzak bir sunucudan web hizmeti durumunu almak için Nmap kullanın.*



Dolayısıyla, Nmap'i kullanmak, hata ayıklama veya teşhis aşamaları sırasında ünlü "ping testi "nden daha ileri gider. Daha sonra göreceğimiz gibi, Nmap tarafından belirli bir bağlantı noktasında hangi hizmetin dinlendiğini belirlemek için kullanılan çeşitli yöntemler vardır.



### III. Ağ haritalama için Nmap kullanımı



Bir _Network Mapper_ olarak, ağ haritalama bu aracın ana hedefidir. Tüm erişilebilir ana bilgisayarları ve hizmetleri listelemek için yerel bir ağ içinde veya birden fazla ağ, alt ağ ve VLAN arasında kullanılabilir. Nmap bu görevi herhangi bir manuel yöntemden çok daha hızlı ve verimli hale getirir.



Örneğin, **192.168.1.0/24** ağındaki etkin ana bilgisayarları hızlı bir şekilde tanımlamak için aşağıdaki komut kullanılabilir:



```
nmap -sn 192.168.1.0/24
```



*Not: `-sP` seçeneği artık kullanılmamaktadır ve yerini `-sn` almıştır.*



![nmap-image](assets/fr/03.webp)



*Bir ağdaki erişilebilir ana bilgisayarları keşfetmek için Nmap kullanma*



Daha sonra göreceğimiz gibi, Nmap tarafından bir ana bilgisayarın "aktif" olarak kabul edilip edilemeyeceğini belirlemek için kullanılan birkaç yöntem vardır, önsel olarak herhangi bir hizmet göstermese bile.



### IV. Bir filtreleme politikasını değerlendirmek için Nmap kullanma



Nmap'in gerçeklere dayalı olma avantajı vardır: sonuçları, herhangi bir mimari belge veya filtreleme politikasından farklı olarak somut bulgular oluşturmayı mümkün kılar. Filtreleme politikasının gerçekten uygulanıp uygulanmadığını **doğrulamanıza** izin verdiği için bilgi sistemi bölümlendirmesinin etkinliğini değerlendirmek için önemli bir araçtır.



Kurumsal bir ağda en iyi uygulama, sistemlerin rollerine, kritikliklerine veya konumlarına göre bölümlere ayrılmasını gerektirir. Filtreleme kuralları (genellikle güvenlik duvarları aracılığıyla uygulanır) bölgeler arasındaki iletişimi kısıtlamalıdır. Ancak bu yapılandırmalar genellikle karmaşıktır ve hatalara açıktır.



Dolayısıyla, politikaya uyulduğunu doğrulamak için hiçbir şey somut bir testten daha iyi olamaz. Örneğin, hassas yönetim hizmetlerine (SSH, WinRM, MSSQL, MySQL, vb.) bir kullanıcı bölgesinden erişilemediğini kontrol edebilirsiniz.



Filtreleme politikasını** test etmek için **Nmap kullanımı, böyle bir politika üretime alınmadan önce sistematik olmalıdır. Ne yazık ki, bu kontrol genellikle ihmal edilmektedir.



Deneyimlerime göre, doğrulama testleri olmadığında birçok yapılandırma hatası fark edilmiyor. Bir IP aralığındaki basit bir hata ya da bir kuralın gözden kaçması, izole olduğu varsayılan bir bölgeyi savunmasız bırakabilir.



### V. Güvenlik denetimi ve sızma testi için Nmap kullanımı



Nmap, güvenlik değerlendirmesi**, sızma testleri (pentestler) ve ne yazık ki saldırganlar için de **birçok yararlı özelliğe sahiptir.



Ağ keşif işlevleri, ilk tehlikeden sonra ağ topolojisini anlaması gereken bir saldırgan için çok önemlidir. Ancak Nmap bundan çok daha fazlasını sunar: **çoğu güvenlik açığı tespitine** adanmış bir komut dosyası motorunu entegre eder.



Örneğin, bu komut bir FTP hizmetinin elle bağlanmaya gerek kalmadan anonim bağlantıya izin verip vermediğini kontrol etmek için kullanılabilir:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Nmap.* aracılığıyla anonim FTP kimlik doğrulamasını kontrol etmek için bir NSE betiği kullanma



Nmap güvenlik açığı tespiti, bir denetim veya sızma testinin ilk adımlarından biridir. Belirli zayıf noktaları hızlı bir şekilde belirlemenizi ve analiz çabalarınızı optimize etmenizi sağlar.



Ancak dikkatli olun: **Güvenlik açığı tarama araçlarının sınırları vardır**. Nmap tehditlerin yalnızca bir kısmını kapsar ve herhangi bir sorun tespit edilmediğinde sistemin güvende olduğunu garanti etmez. Bu nedenle **kullanılan komut dosyalarının nasıl çalıştığını anlamak** ve yalnızca onların kararlarına güvenmemek çok önemlidir.



### VI. Sonuç



Nmap'te uzmanlaşmanın tanılama ve izlemeden haritalamaya, güvenlik politikası değerlendirmesine ve güvenlik açığı taramasına kadar çok çeşitli kullanım durumlarını kapsayabileceğini gördük. Bir sonraki bölümde, işin özüne inecek ve Nmap'i kuracağız.




## 3 - Nmap'in yüklenmesi ve yapılandırılması



### I. Sunum



Bu bölümde, Nmap ağ tarama aracının Linux ve Windows işletim sistemlerine nasıl kurulacağını öğreneceğiz. Bu bölümün sonunda, gelecekteki modüller için Nmap'i kullanmaya başlamak için ihtiyacımız olan her şeye sahip olacağız. Son olarak, kullanıldığında hangi ayrıcalıkları ve neden gerektirebileceğini göreceğiz.



### II. Linux altında Nmap Kurulumu



Nmap başlangıçta GNU/Linux işletim sistemlerinde çalışmak üzere tasarlanmıştır. Sonuç olarak, uzun ömürlülüğü ve popülerliği sayesinde, onu büyük Unix dağıtımlarının tüm resmi depolarında bulabilirsiniz. Bu eğitimde Debian tabanlı bir işletim sistemi [Kali Linux] (https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux") kullanacağım. Ancak klasik bir Debian, CentOS, Red Hat ya da her neyse aynı şekilde kullanabilirsiniz!



Debian altında, Nmap'in mevcut depolarınızda bulunup bulunmadığını kontrol etmek için aşağıdaki komutu kullanabilirsiniz:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Buradaki cevap açıkça "nmap" paketinin depolarda (burada, Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")) var olduğunu gösteriyor. Şu andan itibaren, Nmap'i normal kurulum komutları ile kurabilirsiniz, şu an için silahsızlandıran bir şey yok 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Nmap'in doğru kurulup kurulmadığını kontrol etmek için sürümünü görüntüleyeceğiz:



```
nmap --version
```



İşte beklenen sonuç:



![nmap-image](assets/fr/05.webp)



nmap'in geçerli sürümünü görüntülemenin sonucu._



Bu ekranda "libpcap" (_Paket Yakalama Kütüphanesi_) kütüphanesinin ve sürümünün varlığına dikkat edin. Wireshark tarafından da kullanılan "libpcap", Nmap tarafından paket oluşturmak ve işlemek ve ağ trafiğini dinlemek için kullanılır.



### III Windows'ta Nmap Kurulumu



Bir Windows işletim sistemine yüklemek için, ikili dosyayı resmi siteden indirerek başlayın (başka hiçbir yerden değil!):





- Resmi web sitesindeki Nmap indirme sayfası: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Daha sonra `nmap-<VERSION>-setup.exe` adlı ikili dosyayı indirmeniz gerekecektir:



![nmap-image](assets/fr/06.webp)



windows için nmap kurulum ikili dosyası indirme sayfası



Bu ikili dosyayı sisteminize yükledikten sonra, Nmap'i yüklemek için çalıştırmanız yeterlidir. Bu basit bir kurulumdur ve tüm seçenekleri varsayılan olarak bırakabilirsiniz.



Benim refleksim "zenmap (GUI Frontend)" kutusunun işaretini kaldırmaktır. Bu, benim kullanmadığım ve bu eğitimde ele alınmayacak olan Nmap için bir grafik Interface'dir, ancak Nmap komut satırı aracında ustalaştıktan sonra denemekten çekinmeyin!



![nmap-image](assets/fr/07.webp)



windows'a Nmap yüklerken Zenmap'in isteğe bağlı olarak seçilmemesi



Nmap kurulumunun sonunda, ikinci bir kurulum önerilmektedir: "Npcap" kütüphanesi:



![nmap-image](assets/fr/08.webp)



windows altında Nmap yüklenirken "Npcap" kütüphanesinin yüklenmesi



Bu, Nmap'in ağ iletişimlerini yönetmek, yani ağ paketleri oluşturmak, göndermek ve almak için dayandığı kütüphanedir. Windows'ta Wireshark kullanıyorsanız muhtemelen bu kütüphaneyle zaten karşılaşmışsınızdır, çünkü o da bunu kullanır ve kurulum gerektirir.



Linux'ta olduğu gibi, bir Komut İstemi veya [Powershell] terminali (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") açıp aşağıdaki komutu yazarak Nmap'in kurulu olduğunu doğrulayabilirsiniz:



```
nmap --version
```



İşte beklenen sonuç:



![nmap-image](assets/fr/09.webp)



nmap'in geçerli sürümünü görüntülemenin sonucu._



Nmap artık Windows'ta yüklü. Bu öğreticiyi takip ederek Linux'ta olduğu gibi kullanabilirsiniz.



### IV. Nmap'i kullanmak için gereken yerel ayrıcalıklar



Ancak bu arada, Nmap kullanırken, **sistem üzerinde yükseltilmiş yerel ayrıcalıklara sahip olmak gerekli midir? **Duruma göre değişir**.



En temel haliyle, yani seçeneklerini kullanmada çok ileri gitmeden, Nmap mutlaka ayrıcalıklı haklar gerektirmez. Ancak, kısa süre içinde Nmap'i tam potansiyeliyle kullanabilmek için ayrıcalıklı bir bağlamda (Linux altında "root", Windows altında "administrator" veya eşdeğeri) kullanmanın daha iyi olduğunu fark edeceksiniz, bunun gibi bir hata mesajı alma riskini göze alarak:



![nmap-image](assets/fr/10.webp)



nmap seçenekleri kök hakları gerektirdiğinde Linux altında hata mesajı._



İster Linux ister Windows üzerinde olsun, Nmap'in sizden ayrıcalıklı erişim isteyeceği birçok durum vardır. Ana nedenler aşağıdaki gibidir (kapsamlı olmayan liste):





- "Ham" ağ paketleri oluşturma**: Nmap, gelişmiş paket manipülasyonu ve yapımı da dahil olmak üzere çok çeşitli tarama yöntemlerine sahiptir. Örneğin, TCP alışverişlerinin klasik _Üç yönlü el sıkışması_ kuralına uymayan TCP SYN taramaları gerçekleştirmek istediğimizde durum böyledir. Bunu yapmak için, Nmap'in sadece ağ iletişiminde iyi uygulamalara nasıl saygı gösterileceğini bilen işletim sistemlerinin yerel işlevlerinden başka işlevler kullanması gerekir (yukarıda görülen "Npcap" ve "libcap" kütüphanelerini çağırır). Nmap işleri "standart" şekilde yapmadığı için işletim sistemleri, hizmetler ve belirli güvenlik açıkları hakkında belirli bilgileri çıkarabilmektedir.





- Ağ trafiğini dinle**: Nmap'in bazı seçenekleri, belirli bilgileri almak için ağı dinlemesini gerektirir. Bu eylem işletim sistemlerinde hassas olarak kabul edilir, çünkü sistemdeki diğer uygulamaların iletişimini dinlemenize de izin verir. Tıpkı Wireshark gibi, Nmap'in de bunu yapmak için belirli ayrıcalıklara ihtiyacı vardır ve bu ayrıcalıkları doğrudan ayrıcalıklı bir oturumda bulunarak elde etmek daha kolaydır.





- Ayrıcalıklı bağlantı noktalarında dinleme**: işletim sistemlerinde, 0'dan 1024'e kadar olan bağlantı noktalarının (TCP'nin yanı sıra UDP) ayrıcalıklı olduğu söylenir, yani bir şekilde çok özel kullanımlar için ayrılmışlardır ve bu nedenle korunurlar. Her ne kadar günümüzde bu biraz geçersiz bir neden olsa da, bu bağlantı noktalarını dinlemek için hala belirli ayrıcalıklara sahip olmak gerekir; Nmap'in nasıl kullanılacağına bağlı olarak bunu yapması gerekebilir.





- UDP paketleri gönderme:** Benzer şekilde, UDP bağlantı noktalarında (durum bilgisi olmayan bir protokol) bir ağ uygulamasını dinlemek, işletim sistemlerinde ayrıcalıklı haklar gerektirir. Bu nedenle, Nmap'in taramalarına verilen yanıtları analiz etmek için bir yanıt dinlemek zorunda kalacağı bir UDP taraması gerçekleştirmek istiyorsanız ayrıcalıklı bir oturum gerekecektir.




Daha açık olmak gerekirse, en azından Linux altında, Nmap'i tüm işlevleri ve seçenekleriyle root olmadan çalıştırmak mümkündür. Bu, ikiliye doğru _yetenekleri_ vererek elde edilir. Bununla birlikte, bu gelişmiş manipülasyon gerektirir ve Nmap'i doğrudan ayrıcalıklarla çalıştırmak kadar pratik olmayabilir. Ayrıca, bu yaklaşım daha az yaygındır ve yanlış yapılandırılırsa güvenlik sorunları oluşturabilir.



Ancak, bu Nmap dersimizden biraz farklıdır, bu yüzden şimdilik bundan vazgeçeceğiz.



Bu eğitimin geri kalanında, belirtilmemiş olsa bile Nmap'in her zaman "root" olarak ("root" olarak bir kabuktan veya "sudo" komutu aracılığıyla) veya Windows altında bir yönetici terminalinde çalıştırıldığını varsayın. Aksi takdirde, öğreticiden ince ama fark edilebilir farklılıklar yaşayabilirsiniz.



### V. Sonuç



İşte bu kadar! Nmap artık işletim sistemimize yüklendi ve başka bir yapılandırma gerektirmeden kullanıma hazır. Bu bölüm Nmap'in tanıtımı ve sunumunu tamamlamaktadır. Umarım ağzınızı sulandırmıştır ve pratik yapmaya başlamak için isteklisinizdir.



Daha ciddi bir not olarak, artık Nmap haritalama aracının ne olduğu ve en yaygın kullanımlarının yanı sıra sınırlamaları hakkında daha iyi bir fikrimiz var. Şimdi devam edelim!




## 4 - Nmap ile TCP ve UDP port taramaları



### I. Sunum



Bu bölümde, Nmap ağ tarama aracını kullanarak ilk port taramalarımızı nasıl gerçekleştireceğimizi öğreneceğiz. TCP veya UDP protokollerini kullanarak bir ana bilgisayarda açık olan ağ hizmetlerinin bir listesini derlemek için nasıl kullanacağımızı göreceğiz.



Şu andan itibaren, yalnızca açık yetkiye sahip olduğunuz kontrollü bir ortamdaki ana bilgisayarları taramayı unutmayın.





- Bir hatırlatma olarak: [Ceza Kanunu: Bölüm III: Otomatik bilgi işlem sistemlerine saldırılar] (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Elinizde bir tane yoksa**, aşağıdaki ücretsiz çözümleri öneririm, bunlar tam size göre!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Hacking eğitim platformu Hack The Box, uygun gördüğünüz şekilde saldırmanız için sürekli olarak savunmasız sistemler sağlar. Birkaç yüz sistem mevcuttur, ancak 20 makineden oluşan yenilenmiş bir havuz, bir OpenVPN VPN aracılığıyla erişim ile tüm yıl boyunca ücretsiz olarak sunulmaktadır.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Bu platform, VirtualBox (aynı zamanda ücretsiz bir çözüm) veya diğer yollarla kullanılabilen, indirilmek üzere çok sayıda kasıtlı olarak savunmasız sistem sunmaktadır. İndirildikten sonra VPN'e gerek yoktur - her şey yereldir.




Ayrıca, favori işletim sisteminizde **bir sanal makine** oluşturmakta ve test hedefi olarak çeşitli hizmetleri yüklemekte özgürsünüz. Buradaki avantaj, özellikle Wireshark ile bir tarama sırasında sunucu tarafında neler olduğunu görebilmeniz ve daha gelişmiş testler yaptığımızda yerel güvenlik duvarına da el atabilmeniz olacaktır.



Pratik olalım!



### II. Nmap aracılığıyla bir ana bilgisayarın TCP bağlantı noktalarını tarama



#### A. Nmap ile ilk TCP bağlantı noktası taraması



Şimdi Nmap aracılığıyla ilk taramalarımızı gerçekleştireceğiz. Buradaki amacımız basit: yeni dağıttığımız web sunucusu tarafından hangi hizmetlerin açığa çıkarıldığını bulmak, erişilememesi gereken bir yönetim hizmeti veya devre dışı bırakıldığını düşündüğümüz bir uygulamanın bir portunun açığa çıkarılması gibi beklenmedik bir şey olup olmadığını görmek istiyoruz.



Benim örneğimde, taranacak ana bilgisayarın IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



İşte olası bir sonuç. Çok fazla bilgi içeren klasik bir Nmap dönüşü görüyoruz:



![nmap-image](assets/fr/11.webp)



nmap ile gerçekleştirilen basit bir TCP taramasının sonuçları._



Bu sonuca hızlıca baktığımızda, TCP/22 ve TCP/80 portlarının bu ana bilgisayarda erişilebilir olduğunu anlıyoruz.



Varsayılan olarak ve eğer söylemezseniz, Nmap sadece TCP portlarını tarayacaktır.



#### B. Basit bir Nmap taramasının sonuçlarını anlama



Ancak bu çıktıyı anlamak için bir adım daha ileri gidelim: her satır, ilk olarak ne yapıldığını bilmek ve ikinci olarak tarama sonuçlarını doğru bir şekilde yorumlamak için önemlidir.



İlk satır esasen tarama sürümünü ve tarihini hatırlatır (sonuçta günlük kaydı ve arşivleme için yararlıdır!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



İkinci satır "debian.home (192.168.1.19)" ana bilgisayarı için tarama sonuçlarının başlangıcını gösterir. Bu bilgi, aynı anda birkaç ana bilgisayarı taramaya başladığımızda faydalı olacaktır:



```
Nmap scan report for debian.home (192.168.1.19)
```



Üçüncü satır bize söz konusu ana bilgisayarın "Up", yani aktif olduğunu söyler:



```
Host is up (0.00022s latency).
```



Son olarak, Nmap bize kapalı olarak tanımlanan 998 TCP portunun 'de görüntülenmediğini bildirmektedir:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Bu, bizi . gibi görünen yaklaşık 1.000 satır çıktıdan kurtarır:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Bizi bundan kurtardığı için ona teşekkürler!



Neden 998 "kapalı" port? 2 açık portu eklediğimizde 1000 yapar ve bu Nmap'in varsayılan yapılandırmasında tarayacağı port sayısıdır, mevcut 65535 TCP portu değil! Bunun tamamen ve kolayca özelleştirilebilir olduğunu daha sonra göreceğiz. Ancak hedeflenen ana bilgisayarın oldukça egzotik bir bağlantı noktasını dinleyen bir hizmeti varsa, bu "varsayılan" tarama onu ortaya çıkarmayacaktır.



Bu bilgilerin ardından, en ilginç olanı buluyoruz: "PORT - STATE - SERVICE" üç sütununa göre düzenlenmiş bir tablo:





- İlk "PORT" sütunu basitçe hedeflenen portu/protokolü gösterir ve burada bunun bir TCP portu (`<port>/tcp`) mu yoksa UDP (`<port>/udp`) mi olduğuna bakmak önemlidir.





- "DURUM" sütunu, bu bağlantı noktasında keşfedilen ve elde edilen yanıt temelinde Nmap tarafından belirlenen ağ hizmetinin durumunu gösterir. Bu "açık", "kapalı", "filtrelenmiş" veya "bilinmeyen" olabilir. Nmap'in bu farklı durumlar arasında nasıl ayrım yaptığını daha sonra göreceğiz.





- "SERVİS" sütunu, söz konusu bağlantı noktasında maruz kalınan hizmeti gösterir. Ancak burada aktif hizmet keşif seçeneklerini kullanmadığımızı lütfen unutmayın. Nmap bir port/protokol ile sözde atanmış hizmet arasındaki yerel referansa dayanır: "/etc/services" dosyası




Bir Linux sistemindeki "/etc/services" dosyasına bakarsanız, Nmap tarafından görüntülenene benzer bir "port/protocol - service" bağlantısı bulacaksınız:



![nmap-image](assets/fr/12.webp)



linux altında "/etc/services" dosyasının içeriğini çıkarır._



Şu an için Nmap'in herhangi bir aktif hizmet keşfi gerçekleştirmediğini anlamak önemlidir. Örneğin, böyle bir durum söz konusu olsaydı, bir TCP/80 portunun arkasındaki SSH hizmetini tanımlayamazdı. Bu nedenle, doğru seçeneklerin nasıl kullanılacağını bilmenin önemi - yakında geliyor!



Nmap'in çıktısını nasıl yorumlayacağınızı bilmek, araçta ustalaşmanın önemli bir parçasıdır. İyi haber şu ki, kullandığınız seçenekler ne olursa olsun bu çıktı büyük ölçüde aynı olacaktır.



#### C. Kaputun altında: Wireshark aracılığıyla ağ analizi



Sunucuyu tarayan ana bilgisayarın ağ Interface'ünde veya sunucunun kendisinde neler olduğuna yakından bakarsanız, Nmap'in eylemleri çok daha net olacaktır. Burada yapacağımız şey de bu.



Burada size gösterebileceklerim Wireshark'ta görünenlerin sadece bir kısmı. Daha ileri gitmek istiyorsanız, bir tarama sırasında kendiniz bir ağ yakalama işlemi yapmaktan çekinmeyin ve ardından yakalananlara göz atın.



Bu testte, tarama ana bilgisayarım (192.168.1.18) ve hedef ana bilgisayarım (192.168.1.19) aynı yerel ağ üzerindedir.



Nmap, bir ARP isteği göndererek hedef ana bilgisayarın yerel ağda etkin olup olmadığını öğrenerek başlar. Bir yanıt alırsa, ana bilgisayarın aktif olduğunu bilir ve ağ taramasına başlar:



![nmap-image](assets/fr/13.webp)



yerel ağda bir hedef ana bilgisayarın bulunup bulunmadığını belirlemek için Nmap tarafından yayınlanan _ARP isteği._



Taranacak ana bilgisayar uzak bir ağ üzerindeyse, Nmap bir ping isteği göndererek başlar ve en sık maruz kalınan bağlantı noktalarından bazılarına (TCP/80, TCP/443) ulaşmaya çalışır:



![nmap-image](assets/fr/14.webp)



bir hedef ana bilgisayarın uzak bir ağda erişilebilir olup olmadığını belirlemek için Nmap tarafından yayınlanan ping isteği



Bu testlerden herhangi birine yanıt alırsa, hedefi aktif olarak kabul eder.



Nmap hedefinin aktif olduğunu belirledikten sonra, alan adını ağ kartında yapılandırılmış DNS sunucusu ile çözmeye çalışacaktır:



![nmap-image](assets/fr/15.webp)



nmap tarama hedefinde dNS çözünürlüğü



Artık Nmap hedefini belirlediğine ve aktif olduğunu bildiğine göre, TCP port taramasına başlar:



![nmap-image](assets/fr/16.webp)



nmap taraması sırasında tCP SYN paketi iletimi ve RST/ACK alımı



Bunu yapmak için, varsayılan aralığındaki her TCP bağlantı noktasında **TCP SYN paketleri gönderecek ve bir yanıt bekleyecektir**. Yukarıdaki ekran görüntüsünde, taranan sunucudan TCP RST/ACK paketleri alıyor, yani "devam edin, burada görülecek bir şey yok" - başka bir deyişle, bu portlar kapalı. Sonuçlarda gördüğümüz gibi, bu durum taranan portların çoğu için geçerli olacaktır. İki istisna dışında:



![nmap-image](assets/fr/17.webp)



tarama hedefinde etkin olan 22 numaralı bağlantı noktasına gönderilen bir TCP SYN paketine yanıt



Yukarıdaki ekran görüntüsünde, hedef ana bilgisayar** tarafından gönderilen bir TCP SYN/ACK paketi görüyoruz. Bağlantı noktası aktiftir ve bir hizmet sunar. Nmap yanıtın alındığını onaylar, ardından bağlantıyı sonlandırır (TCP RST/ACK). **TCP/22 portunun aktif olduğunu bu şekilde biliyordu**.



Burada Nmap'in bir TCP ağını tararken "Üç Yollu El Sıkışma "ya saygı gösterdiğini gördük. Performans nedenleriyle, sunucunun geri dönüşüne yanıt vermemesini istemek mümkündür, böylece büyük bir ağı tararken birkaç bin paket tasarruf edilir. Ancak bu seçeneklere ve optimizasyonlara eğitimin ilerleyen bölümlerinde bakacağız.



Artık bir TCP taramasının nasıl yapılacağı ve yapıldığında gerçekte ne olduğu hakkında daha iyi bir fikrimiz var. Ayrıca Nmap'in varsayılan olarak sınırlı sayıda port üzerinde TCP port taraması gerçekleştirdiğini gördük.



### III. Nmap ile UDP portlarını tarama



#### A. Nmap ile ilk UDP port taraması



Şimdi bir ana bilgisayarın UDP portlarını nasıl tarayacağımızı görelim. Gördüğümüz gibi, Nmap varsayılan olarak her zaman TCP portlarını tarayacaktır. Bu, eğer farkında değilsek birçok bilgiyi kaçırmamız anlamına gelebilir.



Bir hatırlatma olarak, bu testin amaçları doğrultusunda, tarama ana bilgisayarım (192.168.1.18) ve hedef ana bilgisayarım (192.168.1.19) aynı yerel ağ üzerindedir.



```
nmap -sU 192.168.1.19
```



Burada, elde edilen dönüş TCP taramasıyla aynı biçime sahiptir, ancak görüntülenen etkin hizmetler istendiği gibi `<port>/UDP` şeklindedir!



![nmap-image](assets/fr/18.webp)



nmap ile gerçekleştirilen basit bir UDP taramasının sonucu._



"-sU" seçeneği, Nmap'e varsayılan olarak TCP yerine UDP üzerinde çalışmak istediğinizi söylemek için kullanılır.



Bu arada, eğitimde daha önce de belirtildiği gibi, Nmap'in UDP taramaları için "root" hakları gerektirdiğini muhtemelen fark edeceksiniz.



not: Nmap'in en son sürümlerinden bu yana, bazı özellikler ağ soketlerine ham erişim gerektirdiğinden, güvenilir sonuçlar elde etmek için UDP taramalarını her zaman yönetici ayrıcalıklarıyla çalıştırmanız önerilir._



UDP taramaları çok uzun sürebilir (benim örneğimde 1000 portu taramak için 1100 saniye), çünkü UDP'de "Üç Yollu El Sıkışma" yoktur, bu da Nmap'in gönderilen her UDP paketi için bir geri dönüş bekleyeceği ve yalnızca belirli bir süre sonra (zaman aşımı) geri dönüş olmazsa portu "kapalı" olarak belirleyeceği anlamına gelir. Taranan ana bilgisayarlardan gelen bu yanıt sistematik değildir ve belirli amplifikasyon saldırılarından kaçınmak için genellikle saniyedeki yanıt sayısı açısından sınırlıdır. Bu, port açık ya da kapalı olsun, taranan ana bilgisayardan anında yanıt alınan TCP'nin aksine bir durumdur. Bunu nasıl optimize edeceğimizi daha sonra göreceğiz.



UDP ile ilgili ikinci bir zorluk **hizmetlerin gelen paketlere her zaman yanıt vermemesidir**, çünkü bu her zaman gerekli değildir ve UDP'nin prensibidir. Durum böyle olduğunda ve hiçbir ICMP "port unreachable" alınmadığında, hizmet yukarıdaki ekran görüntüsünde gösterildiği gibi Nmap tarafından "open|filtered" olarak işaretlenir.



#### B. Kaputun altında: Wireshark ile ağ analizi



TCP taramamızda olduğu gibi, bir Wireshark analizi kullanarak UDP taraması sırasında ağ düzeyinde neler olduğuna daha yakından bakalım. Nmap'in bir ana bilgisayarın aktif olup olmadığını belirleme davranışı aynıdır.



UDP'yi tararken tek gerçek fark, Nmap'in "Üç Yollu El Sıkışma" beklemeyecek olmasıdır, çünkü bu mekanizma UDP'de (durumsuz protokol) mevcut değildir:



![nmap-image](assets/fr/19.webp)



nmap taraması sırasında uDP paket iletimi ve ICMP alımı (bağlantı noktasına ulaşılamıyor)



Yukarıdaki ekran görüntüsünde Nmap'in çok sayıda UDP paketi göndereceğini ve bunların çoğu için yanıt olarak bir ICMP "Hedefe ulaşılamıyor (Port ulaşılamıyor)" paketi alacağını görebiliriz. Bu normaldir, çünkü bir UDP portuna ulaşılamadığında [RFC 1122] (https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") tarafından tanımlanan uygun yanıttır:



![nmap-image](assets/fr/20.webp)



rFC 1122'den alıntıdır._



UDP'deki **üç olası senaryoyu** gösteren bu Wireshark yakalamasına daha yakından bakalım:



![nmap-image](assets/fr/21.webp)



nmap ile farklı portlarda UDP taraması sırasında ağ yakalama._



Üç vaka aşağıdaki gibidir:





- İlk Exchange, 3, 4 ve 8, 9 numaralı paketlerden oluşmaktadır. 3, 4 ve 8, 9 numaralı paketlerden oluşur. Nmap klasik SNMP portu üzerinden UDP paketleri gönderir ve bu nedenle **protokol uyumlu paketleri önceden oluşturur**. Daha sonra sunucudan bir yanıt alır (8 ve 9 numaralı paketler). Sonuç: Nmap bir yanıt aldı, hizmet "açık".





- İkinci Exchange, 6. ve 7. paketlerden oluşur. Nmap, UDP/165 portuna "boş" bir UDP paketi (protokol yapısı olmayan) gönderir ve yanıt olarak bir ICMP paketi alır: "Hedefe ulaşılamıyor (Bağlantı noktasına ulaşılamıyor)". Sonuç: Nmap (olumsuz) bir yanıt aldı, ana bilgisayar çalışıyor, ancak ulaşmaya çalıştığı hizmet bu bağlantı noktasında çalışmıyor ve bu bağlantı noktası "kapalı" olarak işaretlenecek.





- Son Exchange 12 numaralı paketten oluşur: Nmap UDP/1235 portuna "boş" bir UDP paketi gönderir. Taranan ana bilgisayardan herhangi bir yanıt, hatta açık bir ret bile gelmez. Sonuç: Nmap portu "açık|filtreli" olarak işaretler, çünkü bunun yanıt vermeyecek şekilde yapılandırılmış bir güvenlik duvarının varlığından mı yoksa yine de yanıt vermeyen aktif bir UDP hizmetinden mi kaynaklandığını anlayamaz (UDP'de zorunlu değildir).




İşte bu üç durumun ardından Nmap tarafından görüntülenen sonuç:



![nmap-image](assets/fr/22.webp)



nmap._ aracılığıyla gerçekleştirilen bir UDP taramasının olası sonuçları



Artık bir UDP taramasının nasıl yapılacağı ve yapıldığında gerçekte ne olacağı hakkında daha iyi bir fikrimiz var. Şimdiye kadar Nmap'i çok basit bir şekilde, hangi portları tarayacağımıza karar vermeden kullanıyorduk, ancak bu değişmek üzere!



### IV. Nmap ile port taramasında ince ayar



#### A. Nmap'in varsayılan davranışını hatırlatma



Gördüğümüz gibi, herhangi bir seçenek belirtmezseniz taranacak numara ve portları Nmap kendisi seçer. Bu, tam olarak ne yapacağını söylemediğinizde Nmap tarafından kullanılan "varsayılan" yapılandırmadır. Bu varsayılan seçenekler, maruz kalınan ana bağlantı noktaları hakkında bir fikir vermek için tasarlanmıştır, bunlar sayısal sırayla (bağlantı noktası 1, 2, 3, vb.) değil, maruz kalma sıklığına göre (en yaygın veya sık bağlantı noktaları) seçilir ve ayrıca uygun seçenekleri belirtmezseniz 65535 olası bağlantı noktasının taranmasını başlatmaktan kaçınmak için tasarlanmıştır, bu da "varsayılan" bir kullanım durumu için çok uzun ve kelimeli olacaktır.



**Bu limanlar nasıl seçiliyor?



Varsayılan modda taranan 1000 port, görülme sıklıklarına göre seçilir. Bu istatistikler Nmap tarafından tutulur ve ikili dosyanın kendisi ve komut dosyaları (modüller) ile aynı şekilde güncellenir. Bu istatistikleri "/usr/shares/nmap/nmap-services" dosyasında kendiniz görüntüleyebilirsiniz:



![nmap-image](assets/fr/23.webp)



"/usr/shares/nmap/nmap-services"._ dosyasından çıkarılmıştır



Burada, üçüncü sütunda, olasılıklara (0 ile 1 arasında) veya yüzde dağılımına benzeyen bir şey görüyoruz. Bu, her bir port/protokol çiftinin görülme sıklığıdır. En iyi bilinen portların (bu özette FTP, SSH, TELNET ve SMTP) diğerlerinden çok daha yüksek bir değere sahip olduğunu görebiliriz.



#### B. Nmap taraması için hedef portları kesin olarak belirtin



Ancak gerçek dünyada sadece belirli bir portu, birkaç portu ya da belirli bir port aralığını taramamız gerekebilir. Nmap, hem UDP hem de TCP taramaları için tek tip bir şekilde bunu yapmayı kolaylaştırır.



**Nmap aracılığıyla belirli bir bağlantı noktasını tarayın**



Eğer 1000 değil de tek bir portu taramak istersek, bu portu Nmap'in "-p" veya "--port" seçeneği ile belirtebiliriz:



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Sonuç olarak, tarama doğal olarak çok daha hızlı olacak ve Nmap yalnızca ana bilgisayarın aktif olup olmadığını ve ardından belirtilen bağlantı noktasına erişilip erişilemeyeceğini tespit etmek için gereken paketleri yayacaktır. Bu, vitrin sitenizdeki web hizmetinin hala açık olup olmadığını görmek için hızlı bir test yapmak istediğinizde zaman kazandırır.



**Nmap aracılığıyla birden fazla bağlantı noktasını tarayın**



Aynı şekilde, aynı seçeneği kullanarak ve belirtilen portları virgülle birleştirerek Nmap'e birkaç port belirtebiliriz:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Sırası ne olursa olsun, Nmap tüm bu bağlantı noktalarını ve yalnızca hedeflenen ana bilgisayardakileri kontrol edecektir. Nmap'in çıktısında, "kapalı" olsalar bile **tüm portları ve durumlarını** bize açıkça söylediğini fark edeceksiniz. Bu tam çıktının çok fazla yer kaplayacağı varsayılan davranışın aksine:



![nmap-image](assets/fr/24.webp)



*Belirtilen bağlantı noktalarında bir Nmap TCP taramasının sonucu.*



**Bir dizi bağlantı noktasını tarayın



Taramak istediğiniz bağlantı noktası sayısı çok fazlaysa, bunları aralığa göre belirtebilirsiniz, örneğin:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Elbette, uygun gördüğünüz şekilde karıştırabilir ve eşleştirebilirsiniz, örneğin:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**TCP ve UDP port taraması



Seçilen bağlantı noktalarında aynı anda UDP ve TCP taramaları da gerçekleştirebilirsiniz:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



Bu son örnekte bir UDP portunu belirtmek için "U:" ve bir TCP portunu belirtmek için "T:" bulunduğunu fark edeceksiniz. İşte bu tür bir taramanın olası bir çıktısı:



![nmap-image](assets/fr/25.webp)



*Nmap.* ile TCP ve UDP bağlantı noktası taramasının sonucu



İşte taramalarınızı kişiselleştirmenin ilginç bir yolu!



**Tüm bağlantı noktalarını tara



Son olarak, Nmap'e çok daha büyük veya daha küçük aralıklar belirtmek mümkündür. Nmap tarafından seçilen varsayılan listenin 1000 port içerdiğini gördük. "--top-ports" seçeneğini kullanarak en sık kullanılan ilk 100 portu veya ilk 200 portu da isteyebiliriz:



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Son olarak, "-p-" gösterimini kullanarak tüm olası portları (65535'in tümü) taramasını isteyebiliriz:



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



İkincisi, özellikle UDP ile daha uzun sürecektir, ancak herhangi bir açık bağlantı noktasını kaçırmayacağınızdan emin olacaksınız.



*Not: "-p-" seçeneği tüm TCP portlarını taramak için önerilen yöntemdir. UDP taramaları için, tüm UDP portlarının tam olarak taranması çok uzun sürebileceğinden, performans nedenleriyle port sayısını sınırlamanız önerilir.*



Eğitimin ilerleyen bölümlerinde, Nmap taramalarının hızını ihtiyaçlarımıza göre nasıl optimize edeceğimizi göreceğiz, bu özellikle tüm TCP ve UDP bağlantı noktalarındaki taramalar için yararlı olacaktır.



### V. Sonuç



Bu bölümde, nihayet biraz uygulamalı pratik yaptık, böylece artık **bir ana bilgisayarın TCP ve UDP bağlantı noktalarını taramak için Nmap'i temel bir şekilde nasıl kullanacağımızı** biliyoruz. Ayrıca ağ seviyesinde neler olduğunu ve **Nmap'in bir TCP veya UDP portunun aktif olup olmadığını nasıl belirlediğini** ayrıntılı olarak inceledik. Son olarak, taramak istediğimiz portları nasıl hassas bir şekilde seçeceğimizi ve **Nmap'in varsayılan seçeneklerinin gerçekte ne yaptığını** biliyoruz. Aşağıda, bu bilgileri tekrar kullanacağız ve küresel haritalama ve ağ keşfi de dahil olmak üzere tüm bir ağı taramak için uygulayacağız.




## 5 - Nmap ile ağ haritalama ve keşif



### I. Sunum



Bu bölümde, ağınızın haritasını çıkarmak için Nmap ağ tarama aracını nasıl kullanacağımızı öğreneceğiz. Çeşitli seçenekleriyle bu görevde ne kadar etkili olabileceğini göreceğiz. Son olarak, taramalarımızın hedeflerini Nmap'e belirtmenin farklı yollarına bakacağız.



Özellikle, Nmap'in bir ana bilgisayarın aktif ve erişilebilir olup olmadığını nasıl belirlediği hakkında önceki bölümde öğrendiklerimizi kullanacağız.



Nmap'in giriş bölümünde de belirtildiği gibi, bu bir Ağ Eşleyicisidir. Bu nedenle, ister yerel ister uzak olsun, bir ağdaki erişilebilir ana bilgisayarların bir listesini hazırlamak için mükemmel bir araçtır.



**Yazarın dönüşü:**



Aslında, bir siber güvenlik denetçisi ve pentester olarak, nerede olduğumu, yerel ağdaki komşularımın kim olduğunu ve diğer hangi ağların erişilebilir olduğunu ve üzerlerinde bulunan sistemleri bulmak için dahili sızma testleri gerçekleştirirken sistematik olarak Nmap kullanıyorum. Amacım basit: ağın haritasını çıkarmak, bilgi sisteminin boyutunu belirlemek ve özellikle de saldırı yüzeyinin taslağını çıkarmak.



Ağ haritalama, ağ tanılama, denetleme, varlık haritalama bağlamında da yararlı olabilir (IS'nizin yalnızca Active Directory'de veya GLPI/OCS Envanterinizde bulunanlardan oluştuğundan gerçekten emin misiniz? Bilgi sisteminizde Gölge BT'nin varlığını tespit etmek için de kullanılabilir.



### II. Bir ağ aralığını taramak için Nmap kullanma



#### A. Nmap taraması ile bir ağı keşfetme



Şimdi bir vites yükseltmek ve tüm yerel ağımızı analiz etmek istiyoruz. Hiçbir şey daha basit olamazdı: tek yapmamız gereken önceki bölümde gördüğümüz komutları tekrar kullanmak, ancak basit bir IP Address yerine bir CIDR belirtmek.



CIDR (**Classless Inter Domain Routing**), bir ağ aralığını ve kapsamını (maske kullanarak) belirtmek için kullanılan "klasik" gösterimdir. Örneğin, "192.168.0.0/24", "255.255.255.0" ondalık maske gösteriminin bir "çevirisidir".



Nmap'i bir CIDR belirterek kullanmak için aşağıdaki gibi kullanabiliriz:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Önceki bölümde bağlantı noktalarında olduğu gibi, birden fazla ana bilgisayar, birden fazla ağ veya aralık belirtmek de mümkündür:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



İşte bir ağ üzerinde tarama yaparken alabileceğimiz sonuçlara bir örnek:



![nmap-image](assets/fr/26.webp)



birkaç ağın haritasını çıkarmak için bir Nmap taramasının sonuçları



Özellikle, birkaç aktif ana bilgisayar görüyoruz ve her ana bilgisayar bölümü aşağıdaki gibi bir satırla başlıyor:



```
Nmap scan report for <name> (<IP>)
```



Bu, aşağıdaki sonuçların hangi ana bilgisayara atıfta bulunduğunu açıkça görmemizi sağlar. En son satır da önemlidir:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Taranan ağlarda Nmap'in 5 aktif ana bilgisayar keşfettiğini biliyoruz.



#### B. Kaputun altında: Wireshark ile ağ analizi



Şimdi Nmap aracılığıyla gerçekleştirilen bir ağ keşfi sırasında ağ düzeyinde neler olduğuna daha yakından bakacağız.



Önceki bölümde gördüğümüz gibi, Nmap varsayılan olarak yerel ağdaki ana bilgisayarların varlığını tespit etmek için ARP protokolünü kullanacaktır:



![nmap-image](assets/fr/27.webp)



nmap ve varsayılan seçenekleri kullanılarak yerel bir ağ taranırken yakalanan aRP paketleri



Böylece yerel ağdaki neredeyse tüm ana bilgisayarları tespit edebilir, çünkü bir ARP isteğine verilen yanıt genellikle ağda aktif olan tüm ana bilgisayarlar tarafından sağlanır ve herhangi bir şekilde şüpheli görünmez.



Uzak ağlar için, Nmap tekniklerin bir kombinasyonunu kullanır:



![nmap-image](assets/fr/28.webp)



nmap ve varsayılan seçenekleri kullanılarak uzak bir ağ taranırken yakalanan iCMP ve TCP paketleri



Daha kesin olmak gerekirse, Nmap bir ICMP yankı paketi (klasik pingleme durumu) ve genellikle paket geçiş sürelerini hesaplamak için kullanılan bir ICMP Timestamp paketi kullanır. Uzak ağlardaki ana bilgisayarlardan bir yanıt almayı umar.



Ama bundan daha fazlası var. Yukarıdaki Wireshark yakalamasında, taranacak ağlardaki her potansiyel ana bilgisayarın TCP/443 portlarına sistematik olarak **TCP SYN** paketlerinin ve TCP/80 portuna **TCP ACK** paketlerinin gönderildiğini görebilirsiniz.



**Ağ keşfinin bir parçası olarak neden portlara TCP paketleri gönderilir?



Belirli bir porta SYN paketi göndermek, Nmap'in **bir servisin o portta dinlenip dinlenmediğini** belirlemesini sağlar. Bir ana bilgisayar SYN paketine bir SYN/ACK paketi ile yanıt verirse, bu aktif olduğunu ve bir hizmetin o bağlantı noktasını dinlediğini gösterir. Bu nedenle Nmap, **ping'e yanıt alınmamış olsa bile** bu hizmet üzerinde şansını dener.



Belirli bir bağlantı noktasına bir ACK paketi göndermek, Nmap'in **o ana bilgisayarda bir güvenlik duvarı olup olmadığını belirlemesini sağlar**. Bir ana bilgisayar ACK paketine bir RST (Reset) paketi ile yanıt verirse, bu, o ana bilgisayarda muhtemelen bir güvenlik duvarı bulunduğunu ve istenmeyen trafiği engellediğini gösterir. Böylece ana bilgisayar, diğer isteklere yanıt vermemiş olsa bile ağdaki varlığını ele verir.



Bununla birlikte, bu tekniği kullanan güvenlik duvarı algılamasının her durumda tamamen güvenilir olmayabileceğini unutmamak önemlidir. Bazı ana bilgisayarlar, belirli bir hizmet veya işletim sistemi yapılandırması gibi bir güvenlik duvarının varlığından başka nedenlerle generate RST yanıtları verebilir. Ayrıca, modern güvenlik duvarları bu tür keşif girişimlerine yanıt vermeyecek şekilde yapılandırılabilir.



Artık uzun bir yol kat ettik ve temel ağ keşfi gerçekleştirebiliyoruz. Şimdi Nmap'in davranışı üzerinde bize daha fazla kontrol sağlayacak birkaç seçeneğe daha bakacağız.



### III. Nmap ile port taraması yapmadan ağ keşfi



Fark etmiş olabileceğiniz gibi, varsayılan olarak Nmap **aktif bir ana bilgisayar bulduktan sonra bir port taraması gerçekleştirir**, bu da taramamıza büyük miktarda paket ve yanıt bekleme ekler. Ağınızda 5 ana bilgisayar varsa, Nmap yaklaşık 5.000 portun durumunu kontrol etmeye çalışacak ve bu da daha uzun sürecektir.



Bununla birlikte, Nmap'in seçeneklerini, hizmetlerini keşfetmeden bir ağ üzerinde **sadece aktif ana bilgisayarların keşfini** gerçekleştirmek için kullanmak mümkündür.



Açtıkları hizmetler ve bağlantı noktaları hakkında herhangi bir bilgi olmadan yalnızca hangi ana bilgisayarların erişilebilir olduğunu bilmek istiyorsak, "-sn" seçeneğini kullanarak **sadece ICMP Echo (ping) ve ARP isteklerini kullanarak bir tarama** gerçekleştirebiliriz. Başka bir deyişle, port taramasını tamamen devre dışı bırakın:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



İşte port taraması olmadan gerçekleştirilen bir Nmap ağ keşfinin sonucu:



![nmap-image](assets/fr/29.webp)



Nmap ile bağlantı noktası taraması olmadan bir ağ keşfinin sonucu.



Ana bilgisayar keşfi için tek başına ICMP kullanmanın olası sınırlamalarından daha önce bahsetmiştik (uzak ağlar için). Bu nedenle Nmap, ana bilgisayarlarda bir güvenlik duvarının veya belirli bir hizmetin varlığına ihanet edebilecek birkaç numara da kullanır. Seçeneklerin yardımıyla, keşfedilen her ana bilgisayarın tam bir port taramasıyla yeniden başlamak zorunda kalmadan bu hileleri yeniden kullanabilir ve hatta genişletebiliriz.



Bunu yapmak için, ana bilgisayar keşfimizin bir parçası olarak katılmak istediğimiz bağlantı noktalarını belirtmemize olanak tanıyan "-PS" (TCP SYN) ve "-PA" (TCP ACK) seçeneklerinin yanı sıra "-PP" seçeneğini de kullanacağız:



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Bu tarama zaten ana bilgisayar keşfinin varsayılan seçeneklere göre biraz daha eksiksiz olmasını sağlar.



Birden fazla seçenek kullanarak oldukça kapsamlı komutlar almaya başlıyoruz. Bunun nedeni, Nmap'in nasıl çalıştığını ve bazen zaman kaybetmemize veya önemli Elements'i kaçırmamıza neden olabilecek "varsayılan" seçeneklerinin sınırlamalarını bilmemizdir. Ustalaşmak için zaman ayırmanın tüm amacı bu!



Son siparişimizin seçeneklerini detaylandırmak için:





- "`-sn`: Nmap tarafından keşfedilen her aktif ana bilgisayar için bağlantı noktası taramasını devre dışı bırakır.





- "`-PP`: ana bilgisayar keşfi için ICMP yankısını (ping taraması) etkinleştirir.





- "`-PS <PORT>`": ping'e yanıt vermeyen bir ana bilgisayarın varlığına ihanet eden herhangi bir etkin hizmeti tespit etmek için belirtilen port(lar)a bir TCP SYN paketi gönderin.





- "`-PA <PORT>`": ping'e yanıt vermeyen bir ana bilgisayarın varlığına ihanet eden herhangi bir aktif güvenlik duvarını tespit etmek için belirtilen port(lar)a bir TCP ACK paketi gönderin.




Yukarıdaki örnekte, "-PS" seçeneği için Nmap bağlamlarımda en sık maruz kaldığını düşündüğüm bağlantı noktalarını belirtiyorum. Bu farklı portlar daha sonra her bir ana bilgisayarda test edilecek, barındırdıkları hizmetin gerçekten aktif olup olmadığını görmek için değil, bunun hala aktif olduğu halde ICMP Echo'muza yanıt vermeyen bir ana bilgisayarı keşfetmemize izin verip vermediğini görmek için (hizmetten veya ana bilgisayarın güvenlik duvarından gelen bir yanıt yoluyla).



İşte böyle bir tarama sırasında alınan bir ağ yakalamasında görülebilecekler, bu durumda tek bir hedef ana bilgisayarda bir özüt:



![nmap-image](assets/fr/30.webp)



gelişmiş ağ keşfi sırasında Nmap tarafından gönderilen paketler, port taraması olmadan



TCP SYN paketlerimizi, TCP/80 portundaki TCP ACK'mizi ve ICMP yankımızı buluyoruz. Nmap, ağ keşif taramamız tarafından hedeflenen her ana bilgisayar için tüm bu testleri gerçekleştirecektir.



### IV. Nmap ile hedeflemek için bir varlık dosyası kullanma



Bazen düzinelerce veya yüzlerce ağ, alt ağ ve VLAN'dan oluşabilen gerçek hayattaki bilgi sistemlerinde hedefleri belirlemek hızlı bir şekilde karmaşık hale gelebilir. Bu nedenle Nmap için bir dosyayı kaynak olarak kullanmak, komut satırında tek tek belirtmekten daha kolaydır.



Başlangıç olarak, her satırda bir girdi içeren basit bir dosya oluşturun:



![nmap-image](assets/fr/31.webp)



satır başına bir hedef (ana bilgisayar veya ağ) içeren dosya



Daha sonra, şimdiye kadar görülen tüm Nmap seçeneklerini kullanabilir ve "-iL <path/file>" seçeneğini belirtebiliriz:



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap daha sonra dosyamızda bulunan tüm hedefleri taramasına dahil edecektir.



Tüm hedeflerinizin dikkate alınacağından emin olmak istiyorsanız, "-sL -n" seçeneğini kullanabilirsiniz. Nmap daha sonra ağ üzerinden herhangi bir paket göndermeden sadece dosyadaki CIDR'leri ve ana bilgisayarları yorumlayacak ve bunları size gösterecektir:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Bu, taranacak ana bilgisayar listesinin doğru olmasını sağlar.



Sizinle paylaşmak istediğim son bir önemli ipucu da **taramanın bir parçası olarak ana bilgisayar veya ağın hariç tutulması** ile ilgilidir. Bir ana bilgisayarı hariç tutma ihtiyacı, özellikle **bilgi sisteminin hassas bir bileşeninin taramalarımız tarafından rahatsız edilmediğinden veya bozulmadığından** emin olmak istiyorsak, bazı durumlarda gerekli olabilir.



Bir şirketin endüstriyel (PLC) veya sağlık ekipmanına sahip olması bu tür ihtiyaçların sık görülen örnekleridir. Bu tür ekipmanlar bazen kötü tasarlanmıştır ve kötü biçimlendirilmiş paketleri ya da çok fazla sayıda paketi almak için tasarlanmamıştır. Kullanılabilirlik veya iş/insan riski gibi bariz nedenlerden dolayı, bu ekipmanların test dışında bırakılması tercih edilir.



IP adreslerini veya ağları taramamızın dışında tutmak için Nmap'in "--exclude" seçeneğini kullanabiliriz, örneğin:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



Bu örnekte, "192.168.1.0/24" ağını tarıyorum ancak burada bulunan "192.168.1.140" ana bilgisayarını hariç tutuyorum. Nmap tarafından bu ana bilgisayara hiçbir paket gönderilmeyecektir. Alt ağ dışlama ile başka bir örnek:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



Benzer şekilde, "10.0.0.0/16" büyük ağını tararım, ancak "10.0.100.0/24" ağı taranmayacaktır. Yine, özellikle hassas bir bağlamda çalışıyorsanız, hangi ana bilgisayarların taranacağını ve hangilerinin tarama dışında bırakılacağını çok net bir şekilde görmek için "-sL -n" seçeneğini kullanmanızı öneririm.



### V. Ağ keşfi ve bağlantı noktası taraması



Şimdi bu bölümde öğrendiklerimizi bir önceki bölümde port tarama seçenekleri hakkında öğrendiklerimizle birleştirebiliriz. Varsayılan olarak, Nmap'in keşfettiği her aktif ana bilgisayarda en sık kullanılan 1000 bağlantı noktasını tarayacağını gördük. İstemediğimiz takdirde bu davranışı nasıl önleyebileceğimizi gördük, ancak bunu tamamen kontrol edebilir ve hatta ihtiyaçlarımıza uygunsa genişletebiliriz.



Örneğin, aşağıdaki komut taranan her ana bilgisayarda TCP/22 bağlantı noktasında bir dinleme hizmetinin varlığını kontrol edecektir:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap ilk olarak aktif ana bilgisayarları listelemek için bir ağ keşfi gerçekleştirecek ve her biri için TCP/22 bağlantı noktasında bir hizmetin mevcut olup olmadığını kontrol edecektir.



Aynı şekilde, örneğin "192.168.0.4" ana bilgisayarı hariç olmak üzere, "192.168.0.0/24" ağında keşfedilen her ana bilgisayardaki tüm TCP bağlantı noktalarının tam taramasını gerçekleştirebiliriz:



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Şimdiye kadar öğrendiğimiz tüm seçenekleri kendi ihtiyaçlarınıza uyacak şekilde birleştirmekte özgürsünüz.



### VI. Sonuç



Bu bölümde, çeşitli seçenekleri kullanarak ağı haritalamak için Nmap'i nasıl kullanacağımızı gördük. Artık taramalarımızın hedeflerinin yanı sıra Nmap'in bağlantı noktası tarama davranışı ve ana bilgisayar bulma yöntemi hakkında ince ayarlı bir anlayışa sahibiz. Ve en önemlisi, Nmap'in varsayılan davranışının ve sınırlamalarının ne olduğunu ve daha ileri gitmek için ana seçeneklerini nasıl kullanacağımızı biliyoruz.



Bir sonraki bölümde, Nmap tarafından taranan hizmetlerin ve işletim sistemlerinin sürümlerini keşfetmek için mekanizmalara ve seçeneklere bakacağız.




## 6 - Nmap ile hizmet ve işletim sistemi sürümlerini tespit etme



### I. Sunum



Bu bölümde, taranan ana bilgisayarlar tarafından kullanılan hizmetlerin ve işletim sistemlerinin sürümlerini keşfetmek ve doğru bir şekilde tespit etmek için Nmap'i nasıl kullanacağımızı öğreneceğiz. Nmap'in bu görevi nasıl yerine getirdiğinin yanı sıra sonuçlarını daha iyi anlamak ve yorumlamak için aracın sınırlamalarına ayrıntılı bir şekilde bakacağız.



Bu eğitimin önceki bölümlerinde gördüğümüz gibi, Nmap varsayılan olarak taradığı ve açık olarak kabul ettiği portlarda hangi servisin açık olduğuna bakmaz. Dolayısıyla, TCP/22 bağlantı noktasındaki bir web hizmetini dinliyorsanız, Nmap bunu açık olarak rapor etmeye devam edecektir, ancak bir `SSH` hizmeti olarak. Bunun nedeni, bir port/protokol ile bir hizmetin adı (`/etc/services/` dosyası) arasında bir ilişki aramak için sisteminizde yerel olarak bulunan bir [veritabanı] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) kullanmasıdır.



Çoğu durumda, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) size doğru bilgiyi sağlayacaktır, çünkü üretim ortamında bu tür durumlarla karşılaşmak nadirdir. Bununla birlikte, geri kalan durumlar klasik bir hizmetin ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, vb.) klasik olmayan bir bağlantı noktasında (örneğin bir SSH hizmeti için 2022) açık olduğu durumlar olacaktır, bu durumda Nmap yerel veritabanında bir eşleşme bulamaz veya gerçekle eşleşmeyen bir eşleşme bulamaz ve önemli bilgileri kaçırırsınız.



Neyse ki Nmap, açık bir portun arkasında tam olarak hangi hizmetin saklanıyor olabileceğini keşfetmek için çok hassas seçenekler ve mekanizmalar sunar. Hatta tam teknolojileri ve sürümleri tanımlamak için bir sorgu ve imza veritabanına sahiptir. Hizmetlere ek olarak, Nmap kullanılan teknolojiyi ve sürümünü de belirleyebilir.



Bu bölümde bu konuya bakacağız.



### II. Bir teknoloji veya sürüm nasıl tespit edilir



#### A. Bir teknoloji veya sürümün nasıl tanımlanacağına dair hatırlatma



Bir teknolojinin ve sürümün tanımlanması, hedeflenen bağlantı noktasını dinleyen hizmetin, CMS'nin, uygulamanın veya yazılımın adının alınmasını içerir. Örneğin, bir web sayfası bir CMS (`WordPress`) tarafından yönetilir, bir web hizmeti (`Apache`, IIS, Nginx) tarafından çalıştırılır ve bir sunucu (Linux veya Windows) tarafından barındırılır. Ancak hangi web hizmetinin çalıştığını nasıl anlarsınız?



Bu bilgiyi bulmak için kullanılan klasik yöntem, söz konusu hizmetin bu bilgiyi nerede görüntülediğini bulmak ve veriyi okumaktan ibaret olan _banner grabbing_ yöntemidir. Çoğu zaman, varsayılan yapılandırmalarında veya işlemlerinde, hizmetler bir bağlantıdan sonra ilk yanıt olarak adlarını ve hatta sürümlerini görüntüler.



![nmap-image](assets/fr/32.webp)



fTP hizmeti tarafından bir TCP bağlantısı kurulur kurulmaz bir sürüm görüntüleme



Burada, `telnet` üzerinden bu hizmete yapılan basit bir TCP bağlantısının, teknolojisini ve sürümünü içeren bir TCP paketiyle sonuçlandığını görüyoruz.



Uğraştığınız hizmetin türü hakkında bir fikir edindikten sonra, bu hizmetten bilgi almak için belirli komutlar veya istekler de gönderebilirsiniz. Bu istekler/komutlar, içlerinden birinin söz konusu hizmetten bir yanıt almasını sağlamak umuduyla (doğru hizmet türü olduklarından emin olmadan) körü körüne de gönderilebilir.



Diğer, daha gelişmiş durumlarda, kullanılan sürüm veya teknoloji hakkında ayrıntılı bilgi sağlayacak bir hata gibi bir tepkiye neden olmak için belirli paketlerin gönderilmesi gerekir.



Tahmin edebileceğiniz gibi, Nmap tüm bu teknikleri kullanarak bir bağlantı noktasında barındırılan hizmetin tam türünü, teknolojisinin adını ve sürümünü belirlemeye çalışacaktır.



#### B. Nmap Problarını ve Eşleşmelerini Anlama



Taranan her bağlantı noktasında tüm bu kontrolleri gerçekleştirmek için Nmap, sık sık güncellenen yerel bir veritabanı kullanır (tıpkı ikili veya modülleri gibi). Bu birkaç bin satırlık bir metin dosyasıdır: `/usr/share/nmap/nmap-service-probes`.



Bu dosya, tümü iki ana kılavuz etrafında düzenlenmiş çok sayıda girdiden oluşur:





- Prob: Bu, Nmap'in tanımlanacak hizmetten bir tepki almak için göndereceği paketin tanımıdır. Bunu kör bir girişim gibi düşünün _Hello? Guten Tag? Merhaba mı? Um... Buenos Dias belki? Hedeflenen hizmet, anladığı (yani doğru protokolü konuşan) bir sonda alır almaz, Nmap'e yanıt verecek ve bu da hizmetin türünü onaylayacaktır.





- Match": bunlar Nmap'in elde edilen yanıta uyguladığı düzenli ifadelerdir. Bir HTTP GET isteği göndermek hizmetten bir yanıt alınmasına neden olduysa, örneğin `Apache`, `Nginx`, `Microsoft IIS` vb. kelimelerin varlığını belirlemek için bu yanıta düzinelerce düzenli ifade uygulayacaktır.




Belirli durumlar için birkaç başka yönerge daha vardır, ancak Nmap'in nasıl çalıştığını anlamak ve kullanımını özelleştirmek için ana yönergeler bunlardır. Bu teori kısmını daha somut hale getirmek için, işte bir örnek:



![nmap-image](assets/fr/33.webp)



nmap'in `/usr/share/nmap/nmap-service-probes` dosyasındaki bir Prob örneği



Bu örneğin ilk satırında `GetRequest` adında anlaşılması kolay bir Prob görüyoruz. Bu, HTTP/1.0 kullanarak web hizmeti köküne boş bir HTTP GET isteği içeren bir TCP paketidir, ardından bir satır beslemesi ve boş bir satır gelir.



Port` satırı Nmap'e bu Probu hangi port için göndereceğini söyler. Bu, testlere öncelik vermenizi ve zaman kazanmanızı sağlar.



Son olarak, iki `match` örneğimiz var. Örneğin ilki, bu satırda yer alan düzenli ifade alınan hizmet yanıtıyla eşleşirse, taranan web hizmetini `ajp13` olarak kategorize edecektir.



Sondaların neye benzeyebileceğini anlamanıza yardımcı olmak için, bu dosyada bulacağınız bazı Sondaların bir listesini aşağıda bulabilirsiniz (bu eğitim yazılırken toplam 188 adet vardı).



![nmap-image](assets/fr/34.webp)



nmap tarafından kullanılan ve `/usr/share/nmap/nmap-service-probes`._ dosyasında bulunan birkaç Prob örneği



İlk ikisi (`NULL` ve `GenericLines` olarak adlandırılır) burada özellikle ilgi çekicidir, çünkü sadece boş bir TCP paketi veya satır sonu içeren bir paket gönderirler. Sunucu hizmetleri genellikle bir bağlantı alınır alınmaz, istemciden herhangi bir özel eylem, komut veya talep olmaksızın kendilerini tam olarak duyururlar.



Burada biraz daha karmaşık bir _match_ durumu söz konusudur:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



Tam düzenli ifade burada `m|` ve `|` arasında yer alır ve bu dosyadaki herhangi bir düzenli ifadeyi sınırlandırır. Lütfen bu örneğin tamamını okumak için zaman ayırın. Düzenli ifadede bir seçim fark edeceksiniz: `([\d.]+)`, bir sürümü izole etmek için kullanılır. Bu örnek ayrıca `p/nginx/` ürün adı, `v/$1/` alınan sürüm ve `cpe:/a:igor_sysoev:nginx:$1/` sürümlü CPE gibi diğer Elements'leri de tanımlar.



CPE (Common Platform Enumeration), yazılım ve donanımı tanımlamak ve açıklamak için kullanılan standartlaştırılmış bir gösterim sistemidir. Bu format, güvenlik açıklarının ve güvenlik yapılandırmalarının daha verimli bir şekilde yönetilmesini ve her şeyden önce söz konusu ürün ne olursa olsun bunların birleşik bir şekilde temsil edilmesini sağlar. İşte iki CPE örneği: `cpe:/o:microsoft:windows_8.1:r1` ve `cpe:/a:apache:http_server:2.4.35`



Burada işletim sistemi için `o`, uygulama, satıcı, ürün ve sürümler için `a` türlerini açıkça tanımlıyoruz.



Dolayısıyla, bu düzenli ifadelerden biriyle _match_ olması durumunda, yalnızca hizmetin adını değil, aynı zamanda sürümünü ve tam CPE'sini de alacağız, böylece bu sürümü etkileyen CVE'leri bulmayı kolaylaştıracağız. Bu bilgileri Nmap'in standart çıktısında bulacaksınız ve birkaç bölümde ele alacağımız diğer amaçlar için çok yararlı olduğunu göreceksiniz.



_matches_ ve daha genel olarak `/usr/share/nmap/nmap-service-probes' dosyasındaki yönergelerin tam sözdizimi burada bitmez ve Nmap'i ve sonuçlarını manipüle etmeye alışkın değilseniz oldukça karmaşık görünebilir. Bununla birlikte, en azından varlığını ve genel işleyişini aklınızda tutmalısınız; bu, daha sonra bir sonucu anlamak veya hata ayıklamak, bir taramayı özelleştirmek veya hatta Nmap geliştirmeye katkıda bulunmak istediğinizde kullanışlı olacaktır.



### III. Sürümleri tespit etmek için Nmap kullanma



Şimdi tüm bu karmaşık _Probe_ ve _Match_ mekaniğini basit bir seçenek aracılığıyla kullanacağız: `-sV`. Bu basitçe Nmap'e şunu söyler: açık olarak ayarladığınız portların tam olarak hangi servisleri ve sürümleri olduğunu bulmaya çalışın.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



İşte böyle bir komutun sonucunun tam bir örneği:



![nmap-image](assets/fr/35.webp)



nmap'in ağda maruz kalan uygulamaların sürüm tespitinin sonuçları



Burada Nmap'in bu hedef tarafından maruz bırakılan ağ hizmetlerinin tüm sürümlerini tanımlamayı başardığını ve bu bilgileri yeni bir `VERSION` sütununda gösterdiğini görebiliriz. Bu bilgi kurtarılan imzanın bir parçasıysa, işletim sistemine kadar oldukça kesin bilgiler görmek mümkündür.



Bir güvenlik açığı taraması sırasında neler olduğunu ayrıntılı olarak anlamak için `--version-trace` seçeneğini kullanabiliriz. Bu, algılamaya yol açan _Probe_'u görüntüleyen bir hata ayıklama modu görünümü sağlayacaktır:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Sonuç olarak, sıralamamız gereken çok fazla bilgi olacak. `Service scan Hard match` ile başlayan satırları belirlemeye çalışın. Daha sonra bunun gibi satırlar göreceksiniz:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Teknolojiyi ve sürümü tespit etmek için hangi _Probes_ kullanıldığını (bu durumda `NULL` ve `GetRequest` _Probes_) ve alınan bilgileri açıkça görebiliriz.



### IV. Mastering testleri ve tespit doğruluğu



Şimdi `/usr/share/nmap/nmap-service-probes' dosyasında daha önce bakmadığımız bir yönergeye geri döneceğiz:



![nmap-image](assets/fr/36.webp)



probes `rarity` yönergesi `/usr/share/nmap/nmap-service-probes`._ dosyasında



Bu yönerge bir _Probe_ ile ilişkili nadirliği (yani öncelik/olasılık) belirtmek için kullanılır. 1'den 9'a kadar olan bu gösterim, _Probe_ gönderirken Nmap tarafından gerçekleştirilen analizin bütünlüğünü kontrol etmenizi sağlar. Nmap'in "notasyon" sisteminde, 1'lik bir nadirlik vakaların büyük çoğunluğunda bilgi sağlarken, 8 veya 9'luk bir nadirlik, nadiren mevcut olan bir yapılandırma veya hizmete özgü çok özel bir durumu temsil eder.



Daha açık olmak gerekirse, varsayılan bir durumda, Nmap tanımlanacak her hizmete 1 ila 7 arasında bir nadirliğe sahip _Probes_ gönderecektir. Nadirliğe göre _Probes_ dağılımı hakkında daha iyi bir fikir vermek için, işte sayıları:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Mantığa aykırı gibi görünse de, 8 ve 9 numaralı Problar diğerlerinden daha fazladır. Bunun nedeni, nadirlik 1 Problarının genel olması ve hizmetten bağımsız olarak çoğu durumda çalışmasıdır (sadece boş bir TCP paketi gönderen `NULL` Probunu hatırlayın). Daha karmaşık Problar ise her hizmet için neredeyse benzersizdir.



Sürüm taramamızda kullanmak istediğimiz Probları manuel olarak yönetmek istersek, `--version-intensity` seçeneğini kullanabiliriz. İşte iki örnek:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Bu konuyu bitirmek için, işte _Probe_ 9 ve 8'in bir örneği:



![nmap-image](assets/fr/37.webp)



`/usr/share/nmap/nmap-service-probes`._ dosyasındaki 8 ve 9 nadirlikteki Prob örnekleri



Bu iki _Probes_ Quake1 ve Quake2 sunucularını (video oyunu) tespit eder. Nostaljik açıdan ilginç, ancak günlük hayatta pek işe yarayacak gibi görünmüyor.



Hassasiyet veya hız ihtiyaçlarınıza bağlı olarak, bu `nadirlik' ilkesinin var olduğunu ve sonucu etkileyebileceğini unutmayın.



### V. İşletim sistemlerini tespit etmek için Nmap kullanma



Şimdi Nmap'in bir ağ üzerinde taranan ve tespit edilen ana bilgisayarların işletim sistemlerini tespit etmemize nasıl yardımcı olabileceğine bakacağız. Bunu yapmak için, Nmap'in `-O` (`OS Scan` için) seçeneğini kullanın.



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



İşte sonuçların bir örneği. Burada, Nmap bize bunun muhtemelen bir Linux işletim sistemi olduğunu söylüyor ve bize tam sürümüyle ilgili çeşitli istatistikler sunuyor.



![nmap-image](assets/fr/38.webp)



nmap tarafından bir işletim sisteminin tanımlanma olasılığının tespiti



Bunu başarmak için Nmap, teknoloji ve sürüm tespiti için _Probes_ ve _Matches_ ile çok benzer bir şekilde çalışan çok sayıda teknik kullanacaktır. Temel fark, Nmap'in ICMP, TCP, UDP ve diğer protokollerin oldukça "düşük seviyeli" parametrelerini kullanacak olmasıdır. İşte Microsoft Windows 11 işletim sistemini tespit etmek için iki test örneği:



![nmap-image](assets/fr/39.webp)



windows 11 işletim sistemini tespit etmek için Nmap tarafından gerçekleştirilen test örnekleri



Kabul edelim ki, bu testleri yorumlamak çok zordur ve Nmap'e giriş dersi bağlamında bunları derinlemesine anlamaya çalışmayacağız. Konuyu daha derinlemesine incelemek isterseniz, bu bilgileri içeren dosya `/usr/share/nmap/nmap-os-db`dir.



Ancak, işletim sistemi tespitinin bir kesinlikten ziyade Nmap tarafından belirlenen bir olasılık olduğunun farkında olmanız gerekir.



### VI. Sonuç



Bu bölümde, taranan ana bilgisayarların ve hizmetlerin teknolojilerini, sürümlerini ve işletim sistemlerini tespit etmek için Nmap'in seçeneklerini nasıl kullanacağımızı öğrendik. Artık Nmap'in bu bilgileri uzaktan nasıl elde ettiğini iyi bir şekilde anlıyoruz. Ayrıca verbosity ve test doğruluğunu yönetme seçeneklerinin yanı sıra aracın bu konulardaki sınırlamalarını da gözden geçirdik.



Bir sonraki bölümde, bilgi sistemimizin güvenlik analizini gerçekleştirmek için Nmap'in NSE komut dosyalarını nasıl kullanacağımızı öğreneceğiz. Gerekirse son bölümleri tekrar okumak için zaman ayırın ve şimdiye kadar öğrendiklerimizde daha iyi ustalaşmak için pratik yapmaktan ve aracın bağırsaklarına girmekten çekinmeyin.




## 7 - Güvenlik analizi: güvenlik açıklarını tespit etme



### I. Sunum



Bu bölümde, taramalarımızın hedeflerindeki güvenlik açıklarını tespit etmek ve analiz etmek için Nmap ağ tarama aracını nasıl kullanacağımızı öğreneceğiz. Özellikle, bu görevi yerine getirmek için mevcut olan çeşitli seçeneklere bakacağız ve sonuçlarını daha iyi anlamak ve yorumlamak için aracın yeteneklerinin sınırlarını inceleyeceğiz.



Bu ilk bölümde, Nmap'in güvenlik açığı tarayıcısına bir göz atacağız ve temel güvenlik açığı algılama seçeneklerinin nasıl kullanılacağını göreceğiz. İlerleyen bölümlerde, bu özelliğin nasıl çalıştığına ve nasıl özelleştirilebileceğine daha yakından bakacağız.



### II. Güvenlik açıklarını tespit etmek için Nmap kullanma



Şimdi bilgi sistemimizin hizmet ve sistemlerindeki güvenlik açıklarını tespit etmek için Nmap ağ tarayıcısını kullanmak istiyoruz. Bu, aktif ana bilgisayarları keşfetmenin, maruz kalan hizmetleri numaralandırmanın ve sürümleri ve teknolojileri tespit etmenin yanı sıra, Nmap'in güvenlik açıklarını arayacağı anlamına gelir.



Bunu başarmak için Nmap, test için ayrıntılı bir yaklaşım sağlayan modüller olarak görülebilecek NSE (_Nmap Scripting Engine_) komut dosyalarına dayanır.



Doğru seçeneklerle, Nmap'ten keşfedilen her hizmette çeşitli NSE komut dosyalarını kullanmasını isteyeceğiz, böylece:





- Yapılandırma hataları ;





- Ek ve daha gelişmiş sürüm ve işletim sistemi keşifleri ;





- Bilinen güvenlik açıkları (CVE'ler) ;





- Zayıf tanımlayıcılar ;





- Kötü amaçlı yazılım bulaşmasının karakteristik Elements'ü ;





- Hizmet reddi olasılıkları ;





- Vb.




Gördüğünüz gibi, NSE komut dosyaları, gerçekleştirebileceği ağ işlemleri açısından Nmap'in yeteneklerini önemli ölçüde genişletmektedir. Ve bu, her zamankinden çok daha gelişmiş görevleri gerçekleştirmek için. İyi haber şu ki, her zamanki gibi, bu özellikler sadece bir seçenek aracılığıyla ve varsayılan bir bağlamda kullanılabilir. Bundan sonra göreceğimiz şey bu.



### III. Güvenlik açığı taraması örneği



NSE komut dosyaları, Nmap'i bir ana bilgisayardaki tek bir bağlantı noktasını, o ana bilgisayardaki tüm hizmetleri veya birkaç ağda algılanan tüm hizmetleri taramak için kullanırken kullanılabilir. Bu nedenle, göreceğimiz seçenekleri şimdiye kadar incelediğimiz tüm bağlamlarda kullanabiliriz.



Bir Nmap taraması yoluyla güvenlik açığı taramasını etkinleştirmek için `-sC` seçeneğini kullanmamız gerekir:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Varsayılan olarak, herhangi bir şey belirtmezseniz, Nmap'in yalnızca en yaygın 1000 bağlantı noktasını tarayacağını unutmayın. Hedeflerinizin açığa çıkarabileceği daha egzotik bağlantı noktalarındaki güvenlik açıklarını tespit etmeyecektir.



Bu işlevi bir üretim bilgi sisteminde kullanmadan önce, sizi öğreticiyi okumaya devam etmeye davet ediyorum. İlerleyen bölümlerde, çalıştırılacak testlerin etkisini ve türlerini nasıl daha iyi kontrol edebileceğimize bakacağız.



Daha önce öğrendiklerimizi yeniden kullanarak, örneğin daha kapsamlı olabilir ve bir hedefin tüm TCP bağlantı noktalarını tarayabiliriz:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



İşte NSE komut dosyaları kullanılarak yapılan bir Nmap taramasının sonucu:



![nmap-image](assets/fr/40.webp)



nmap._ aracılığıyla bir ana bilgisayarda yapılan güvenlik açığı taramasının sonuçlarına örnek



Burada, bir güvenlik açığı analizi bağlamında ilgi çekici ek bilgilerin görüntülendiğini görüyoruz:





- FTP hizmetine anonim olarak erişilebilir ve kimlik doğrulama ile korunmaz. Bu doğrulamadan sorumlu NSE betiği bize bunu söyler ve hatta FTP hizmetinin ağaç yapısının bir kısmını görüntüler. Burada Windows sisteminin `C` dizinine erişimimiz olduğunu görüyoruz!





- Gelişmiş web hizmeti alımından sorumlu NSE komut dosyası, sayfa başlığını görüntüleyerek web hizmetinin ne barındırdığı konusunda bize daha iyi bir fikir verir.





- Ayrıca SMB hizmet yapılandırmasının mini bir analizini de yapıyoruz (`smb2-time`, `smb-security-mode` ve `smb2-security-mode` komut dosyaları). Bilgiler, okumayı kolaylaştırmak için ağ tarama sonucundan sonra biraz farklı bir şekilde görüntülenir. Özellikle, bu bilgi SMB Exchange imzalarının olmadığını gösterir. Bu yapılandırma zayıflığı, hedefin, izinsiz giriş/siber saldırı testlerinde sıklıkla kullanılan önemli bir güvenlik açığı olan SMB Relay saldırısında kullanılmasına olanak tanır.




Elbette bu sadece bir örnek. Nmap, çok çeşitli güvenlik açıklarını hedefleyen birçok hizmet için NSE komut dosyalarına sahiptir. Bir sonraki bölümde bu olasılıklara daha yakından bakacağız.



Güvenlik açığı taramasına giriş niteliğindeki bu çalışmayı tamamlamak üzere, ağ keşfi, TCP bağlantı noktası taraması, sürüm ve güvenlik açığı tespiti için eksiksiz bir komut sunuyoruz:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



İşte daha gerçekçi Nmap kullanım durumları gibi görünmeye başlayan bir komut!



### IV. Güvenlik açığı taramasında Nmap'in sınırlamalarını anlama



Açık olalım: Nmap, bilgi sisteminizin tam bir sızma testini gerçekleştirme veya bir Red Team operasyonunu simüle etme yeteneğine sahip değildir. Yanlış bir güvenlik hissine kapılmamanız için farkında olmanız gereken çeşitli sınırlamaları vardır:





- Sınırlı kapsam**: Nmap'in NSE komut dosyaları güçlü olmasına rağmen, test kapsamları diğer özel güvenlik açığı keşif araçlarına kıyasla sınırlı olabilir. Active Directory güvenlik açıkları, hassas verilerin açığa çıkması veya daha gelişmiş güvenlik açığı olan web uygulamaları gibi bazı güvenlik açıkları mevcut NSE komut dosyaları tarafından kapsanmayabilir.





- Güvenlik açığı karmaşıklığı**: belirli güvenlik açığı türlerinin karmaşıklıkları nedeniyle NSE komut dosyaları kullanılarak tespit edilmesi zor olabilir. Örneğin, uzak bir hizmetle karmaşık etkileşim gerektiren güvenlik açıkları Nmap tarafından etkili bir şekilde tespit edilemeyebilir (bir dosya paylaşımındaki aşırı izinler veya bir web uygulamasındaki izin kontrolü açığı gibi).





- Pasif algılama**: Nmap, güvenlik açıklarını tespit etmek için öncelikle aktif taramalara odaklanır, bu da hedef ana bilgisayarlarla aktif bir bağlantı kurmadan potansiyel güvenlik açıklarını etkili bir şekilde tespit edemeyebileceği anlamına gelir. Bu nedenle, aktif bir tarama sırasında kendini göstermeyen güvenlik açıkları gözden kaçabilir (bir web uygulamasında kod enjeksiyonu durumunda olduğu gibi).





- Güncellemelere bağımlılık**: Nmap'in NSE komut dosyalarının [veritabanı] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) sürekli olarak gelişmektedir, ancak yeni bir güvenlik açığının keşfedilmesi ile ilgili bir komut dosyasının Nmap'e eklenmesi arasında bir gecikme olabilir. Sonuç olarak, Nmap her zaman en son güvenlik açıkları ile güncel olmayabilir.





- Yanlış pozitifler ve yanlış negatifler**: Her güvenlik aracında olduğu gibi, Nmap'in NSE komut dosyaları yanlış pozitifler (yanlış güvenlik açığı uyarıları) veya yanlış negatifler (tespit edilmeyen gerçek güvenlik açıkları) üretebilir. Bu, Nmap sonuçlarını analiz ederken akılda tutulması gereken bir konudur.




Bu nedenle Nmap'in ne yapıp ne yapmadığını anlamak ve aynı şekilde sonuçlarını nasıl yorumlayacağınızı bilmek önemlidir. Özellikle, bu eğitim boyunca varsayılan seçeneklerin dikkatli kullanımla ortaya çıkarılabilecek önemli Elements'yı kaçırmamıza neden olabileceğini gördük.



İster bir ağ sistemi yöneticisi, ister bir güvenlik mühendisi veya hatta bir CISO olun, Nmap kullanmak size bir bilgi sisteminin güvenlik durumu hakkında genel bir bakış sağlar. Bu, bir sistemin güvenliğini sağlamada BT ekibi tarafından düzenli olarak gerçekleştirilebilecek önemli bir ilk adımdır. Ancak, zayıflıkları Nmap'ten çok daha kapsamlı bir şekilde ortaya çıkarabilecek olan [siber güvenlik] uzmanlarının (https://www.it-connect.fr/cours-tutoriels/securite-informatique/) müdahalesinin ve tavsiyelerinin yerini almamalıdır.



### V. Sonuç



Modül 3'ün bu ilk bölümünde, Nmap aracılığıyla güvenlik açığı taramasını tanıttık. Artık bu görevi gerçekleştirmek için ana seçeneği nasıl kullanacağımızı biliyoruz, ancak alıştırmanın sınırlarını da biliyoruz. Bir sonraki bölümde, Nmap'in gücünü on kat artırmak için NSE komut dosyalarını kullanarak bu işlevselliğe daha yakından bakacağız.



## 8 - Nmap'in NSE komut dosyalarını kullanma



### I. Sunum



Bu bölümde, NSE (_Nmap Scripting Engine_) komut dosyalarına derinlemesine bir göz atacağız. Özellikle, neden bu aracın en güçlü yönlerinden biri olduklarına, nasıl çalıştıklarına ve mevcut birçok komut dosyasına nasıl göz atılacağına ve kullanılacağına bakacağız.



Bu bölüm, Nmap'in güvenlik açığı tarama özelliklerini temel bir şekilde nasıl kullanacağımızı öğrendiğimiz bir önceki eğitimin devamı niteliğindedir. Şimdi [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/)'in bu açıdan nasıl çalıştığına daha yakından bakacağız, böylece bir kez daha daha hassas ve kontrollü taramalar yapabiliriz.



### II. Nmap NSE komut dosyaları kavramı



Nmap'in NSE komut dosyaları, yeteneklerini son derece esnek bir şekilde genişletmenize olanak tanır. Bunlar, Nmap tarafından kullanılan C veya C#'a göre kullanımı ve erişimi daha kolay olan bir betik dili olan LUA ile yazılmıştır. Tek başına bir araç yerine Nmap ile bir LUA betiği kullanmanın avantajı, Nmap'in yürütme hızından ve standart özelliklerinden (ana bilgisayar, bağlantı noktası ve sürüm keşfi vb.) yararlanmamıza olanak sağlamasıdır.



Bu senaryolar kategorilere göre düzenlenmiştir ve tek bir senaryo birden fazla kategoriye ait olabilir:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Teknik olarak, bir komut dosyasının ait olduğu kategoriler doğrudan kodunda belirtilir.



![nmap-image](assets/fr/41.webp)



nSE komut dosyası kategorileri `ftp-anon`._



Bu örnek, bir önceki bölümde çalıştırılmasını gördüğümüz NSE betiği `ftp-anon.nse` kodunun bir kısmını göstermektedir.



### III. Mevcut NSE senaryolarını listeleyin



Nmap'in NSE komut dosyaları varsayılan olarak `/usr/share/nmap/scripts/' dizininde bulunur ve belirli bir ağaç yapısı veya hiyerarşisi yoktur. İşte bu dizinin içeriğine genel bir bakış:



![nmap-image](assets/fr/42.webp)



nSE komut dosyalarını içeren `/usr/share/nmap/scripts/` dizininin içeriğini çıkarır._



Bu dizinde 5.000'den fazla NSE komut dosyası bulunmaktadır. Çoğu durumda, betik adının ilk kısmı ait olduğu protokolü veya kategoriyi içerir. Bu, örneğin FTP hizmetini hedefleyen tüm komut dosyalarını listelemek istediğimizde listeyi sıralamamızı sağlar:



![nmap-image](assets/fr/43.webp)



ftp-`._ ile başlayan adlara sahip NSE Nmap komut dosyalarının listesi



Nmap, NSE komut dosyalarına göz atmak ve listelemek için gerçekten bir seçenek sunmaz; `--script-help' komutunu ve ardından bir kategori adını veya bir kelimeyi kullanabilirsiniz:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Ancak, çıktı her bir komut dosyasının adı ve açıklaması olacaktır, bu da arama birkaç düzine komut dosyası getiriyorsa uygun değildir:



![nmap-image](assets/fr/44.webp)



nmap'in `--script-help' komutunu kullanmanın sonucu



Bence en etkili yöntem `/usr/share/nmap/scripts/` dizinindeki klasik Linux komutlarını kullanmaktır:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Bir NSE komut dosyasının nasıl çalıştığını daha iyi anlamak için size hitap eden modüllerin kodlarına göz atmaktan çekinmeyin.



### IV. Nmap'in NSE komut dosyalarını kullanma



Şimdi ilgilendiğimiz NSE betiklerini dikkatlice seçerek güvenlik açığı taramalarını nasıl gerçekleştireceğimizi öğreneceğiz.



#### A. Senaryoları kategoriye göre seçin



Başlangıç olarak, belirli bir kategoriye ait tüm betikleri çalıştırmayı seçebiliriz. Bu kategoriyi veya bu kategorileri Nmap'e `--script <category>` argümanı ile belirtmemiz gerekir:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Bu ilk komut `nmap -sC` komutunun eşdeğeridir. Varsayılan olarak, Nmap `default` kategorisindeki komut dosyalarını seçecektir, ancak bu sadece tartışma içindir. Bir sonraki komut, örneğin, `discovery` kategorisindeki tüm komut dosyalarını kullanacaktır:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Gördüğümüz gibi, bazı kategoriler ilgili NSE betiklerinin ne yaptığını hızlı bir şekilde tanımlamamızı sağlarken (`discovery`, `vuln`, `exploit`), diğerleri gerçekleştirilen testin risk, tespit veya kararlılık seviyesini tanımlar. Hassas bir bağlamdaysak ve komut dosyası seçimimiz tarafından gerçekleştirilen farklı eylemleri iyi bir şekilde kavramadıysak, yalnızca `discovery` ve `safe` kategorilerinde bulunan komut dosyalarını seçmek için seçimleri birleştirmeyi seçebiliriz:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Komut dosyalarını kesinlikle ve açıkça `dos` ve `intrusive` kategorilerinden hariç tutmak istiyorsanız, aşağıdaki gösterimi kullanabilirsiniz:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Yukarıdaki gibi hariç tutma koşullarının belirtilmesinin, açıkça hariç tutulmayan diğer tüm kategorilerin kullanılmasıyla sonuçlanacağını lütfen unutmayın. Daha adil olmak için, örneğin şunları belirtebiliriz:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Burada, özellikle gerçek yaşam bağlamlarında güvenlik açığı analizi için Nmap kullanırken, NSE komut dosyalarının kategoriye göre nasıl ele alınacağına dair bazı örnekler verilmiştir.



#### B. Senaryoları bir birim olarak seçin



Bir analiz sırasında, bir NSE komut dosyasına karşılık gelen tek bir özel test gerçekleştirmeyi de seçebiliriz. Bunu yapmak için, `-script <name>` parametresinde betiğin adını belirtmemiz gerekir. Örnek olarak `ftp-anon.nse` betiğini ele alalım:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



O zaman çok kesin bir sonuç elde ederiz:



![nmap-image](assets/fr/45.webp)



nmap aracılığıyla bir FTP bağlantı noktasında NSE `ftp-anon` komut dosyasını kullanmanın sonucu._



P 21` seçeneğini belirttiğimiz için `ftp-anon` betiğinin 21 numaralı bağlantı noktasında çalıştırıldığını ve başka bir bağlantı noktasında çalıştırılmadığını görüyoruz. Ayrıca, `ftp-anon` NSE betiğini yalnızca keşfedilen FTP hizmetlerinde çalıştırarak temel bir bağlantı noktası taraması da gerçekleştirebilirdik:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Bu nedenle, Nmap başka bir bağlantı noktasında bir FTP hizmeti bulmuş olsaydı bu anonim bağlantı testini de gerçekleştirirdi.



Bir NSE betiğinin ne yaptığına dair kısa bir açıklama için yukarıda bahsedilen `--script-help` seçeneğini kullanabilirsiniz:



![nmap-image](assets/fr/46.webp)



help NSE betiği `sshv1`._ için sonuç görüntüleme



Kısacası, şimdiye kadar kullandığımız tüm ağ keşif seçeneklerini, hizmetlerini, sürümlerini ve teknolojilerini bir kez daha yeniden kullanabiliriz!



#### C. Kod argümanlarını yönetme



Nmap'i kullanırken, düzgün çalışması için girdi argümanları gerektiren bazı NSE komut dosyalarıyla karşılaşacaksınız. Şimdi Nmap'in seçenekleri aracılığıyla bu komut dosyalarına nasıl argüman aktarılacağına bakacağız.



Örnek olarak, SSH hizmetine kaba kuvvet saldırısı yapmanızı sağlayan `ssh-brute` betiğini ele alalım.



Klasik bir kaba kuvvet saldırısı, belirli bir hesapta kimlik doğrulama girişiminde birkaç parolanın (bazen milyonlarca) test edilmesinden oluşur. Saldırgan çok sayıda parola deneyerek, kullanıcının saldırı için kullanılan parola sözlüğünde zayıf bir parola kullanmış olma olasılığı üzerine bahse girer.



Bu betik, bağlamımıza uyacak şekilde özelleştirebileceğimiz "varsayılan" seçeneklere sahiptir. Bu saldırı bağlamında, örneğin, Nmap'e kullanıcı listesini ve kullanılacak parola sözlüğünü sağlayabiliriz. Bildiğim kadarıyla, bir betik için gerekli argümanları kolayca listelemek mümkün değil, bu nedenle en güvenilir yol resmi Nmap web sitesini ziyaret etmektir. Bir NSE betiğinin belgelerine doğrudan bir bağlantı `--script-help` seçeneğine yanıt olarak elde edilebilir:



![nmap-image](assets/fr/47.webp)



nSE `ssh-brute` betiği için yardımın nmap.org._ bağlantısıyla görüntülenmesinin sonucu



Belirtilen bağlantıya tıklayarak [https://nmap.org](https://nmap.org/) sitesinin bu web sayfasına ulaşırız:



![nmap-image](assets/fr/48.webp)



nmap'in `ssh-brute` NSE betiğine aktarılabilecek argümanların listesi



Burada kullanılabilecek argümanların net bir görünümüne sahibiz, bizim bağlamımızdaki ana argümanlar `passdb` (şifrelerin bir listesini içeren dosya) ve `userdb` (kullanıcıların bir listesini içeren dosya). Buradaki dokümantasyon dahili Nmap kütüphanelerine atıfta bulunur, çünkü bu kaba kuvvet mekanizmaları ve ilgili seçenekler çeşitli komut dosyalarında (`ssh-brute`, `mysql-brute`, `mssql-brute`, vb.) aynı şekilde kullanılmak üzere karşılıklı hale getirilmiştir ve bu nedenle aşağı yukarı aynı argümanlara sahip olacaktır:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Bu son komutta görebileceğiniz gibi, `--scripts-args key=value,key=value` seçeneğini kullanarak bir Nmap betiğine gerekli argümanları belirtebiliriz. İşte `ssh-brute` NSE betiği aracılığıyla bir SSH kaba kuvveti gerçekleştirirken Nmap çıktısının olası bir sonucu:



![nmap-image](assets/fr/49.webp)



nmap._ aracılığıyla SSH bruteforce yürütmesinin sonucu



Gördüğünüz gibi, NSE betikleri tarafından üretilen bilgilerin önüne etkileşimli çıktıda (terminal çıktısı) `NSE: [betik adı]` eklenir, böylece bulması daha kolay olur. Nmap sonuçlarının olağan görüntüsü içinde, zayıf tanımlayıcıların keşfedilip keşfedilmediğini gösteren bir özetimiz var (şifreler dahil, unutmayın).



İşleri bir adım daha ileri götürmek ve tüm bunların daha önce incelediğimiz tüm seçeneklere ek olarak kullanılabileceğini hatırlatmak için, işte `10.10.10.0/24` ağını keşfedecek, en sık kullanılan 2000 TCP bağlantı noktasını tarayacak ve FTP hizmetlerinde anonim erişim araması ve SSH hizmetlerinde kaba kuvvet kampanyası yürütecek bir komut:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Bu, mevcut birçok komut dosyasının ve seçeneklerinin sadece bir örneğidir. Ancak artık NSE komut dosyalarıyla nasıl başa çıkılacağı, argüman gerektirip gerektirmedikleri ve bu argümanların Nmap'e nasıl aktarılacağı konusunda daha iyi bir fikrimiz var.



### V. Sonuç



Bu bölümde, çeşitli görevleri gerçekleştirmek için Nmap'in NSE komut dosyalarını nasıl kullanacağımızı öğrendik. Sizi farklı komut dosyası kategorilerini ve komut dosyalarının kendilerini keşfetmeye ve kaç tane testi otomatikleştirebileceklerini görmeye davet ediyorum.



Birkaç bölümdür, az ya da çok gelişmiş keşif, tarama ve numaralandırma seçeneklerini biriktiriyoruz. Şimdiye kadar, Nmap'in çıktı ve sonuç ekranının oldukça kapsamlı olmaya başladığının, hatta bazen terminalimiz için çok ayrıntılı olduğunun farkında olmalısınız. Bir sonraki bölümde, özellikle çeşitli formatlardaki dosyalarda saklayarak bu çıktıya nasıl hakim olacağımızı öğreneceğiz.






## 9 - Nmap çıktı verilerini yönetme




### I. Sunum



Bu bölümde, Nmap tarafından üretilen çıktıya ve özellikle de bu çıktıyı biçimlendirmek için çeşitli seçeneklere bir göz atacağız. Nmap'in farklı ihtiyaçlara uygun çeşitli çıktı formatları üretebildiğini ve bunun da bu aracın en güçlü yanlarından biri olduğunu göreceğiz.



Varsayılan olarak, Nmap gerçekleştirdiği taramaların ve testlerin sonuçlarının ayrıntılı bir görünümünü sunar. Bu, taranan ana bilgisayarları ve hizmetleri, erişilebilir olarak algılananları, açık bağlantı noktalarının özelliklerini, durumlarını ve sürümlerini içerir. Ayrıca, NSE komut dosyalarının ayrıntıları da terminal çıktısında mevcuttur. Bununla birlikte, bu çıktı, bilgilerin net bir şekilde biçimlendirilmesiyle bile hızlı bir şekilde hacimli hale gelebilir ve bu da sonuçlarda kesin bilgi bulmayı zorlaştırabilir.



### II. Nmap çıktı formatlarında uzmanlaşma



#### A. Tarama sonuçlarını bir metin dosyasına kaydetme



İşleri kolaylaştırmak için, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) çıktısını bir metin dosyasına kaydetmeyi çok kolaylaştırır. Bu, arşivleme, diğer testlerle karşılaştırma ve aynı zamanda Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed, vb. gibi özel kelime işlem araçları veya komut dosyası dilleri ile bu çıktıya göz atmak için yararlı olabilir. Nmap'in standart çıktısını bir metin dosyasında saklamak için `-oN <dosya adı>` seçeneğini kullanabiliriz ("normal "deki "N"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Nmap her zamanki standart çıktısını terminalimizde ve aynı zamanda belirtilen dosyada görüntüleyeceği için bu durum şaşırtıcı değildir.



#### B. Yoğunlaştırılmış formatta generate Nmap çıktısı



Ayrıca bir insan tarafından kolayca yorumlanabilen "metin" tarzında ikinci bir çıktı biçimi daha vardır: "greppable" biçimi.



Bu format, `grep` gibi araçlar tarafından işlenmesini kolaylaştıracak şekilde yapılandırılmış Nmap çıktısının "yoğunlaştırılmış" bir görünümünü sağlamak için oluşturulmuştur. Şimdi bu tür bir çıktı örneğine bakalım:



![nmap-image](assets/fr/50.webp)



nmap ağ taraması ve "greppable" formatında çıktı._



Burada, bir ağ keşfinin yanı sıra bir port taraması ve /24 ağındaki teknolojilerin ve sürümlerin bir analizini gerçekleştirdim, ardından çıktıyı "greppable" formatında bir dosyada sakladım. Sonunda aktif ana bilgisayar başına 2 satır içeren bir dosya elde ettim:





- İlk satır bana falanca sunucunun _Up_ olduğunu söylüyor;





- İkinci bir satır bana hangi portların tarandığını, durumlarını ve çok özel bir formatta alınan teknoloji ve sürüm bilgilerini söyler: `<port>/<status/<protocol>//<service>//<version>/,`




Sabit bir sınırlayıcı ile bu biçimlendirme, `grep` gibi kelime işlem araçları veya komut dosyası ve programlama dilleri tarafından hızlı bir şekilde işlenmesini sağlar. Örneğin aşağıdaki komut, Nmap tarafından gerçekleştirilen ve çıktısına göz atmanın zor olacağı büyük bir tarama durumunda `10.10.10.5` ana bilgisayarı hakkındaki bilgileri kolayca almamı sağlıyor:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Tersine, portlar ve IP aynı satırda olduğu için 21 numaralı portu açık olan tüm ana bilgisayarları da kolayca listeleyebilirim:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Böyle bir çıktıyı generate yapmak için `-oG <dosya adı>.gnmap` seçeneğini ("grep "teki "G") kullanmamız gerekir. Alışkanlık olarak, böyle bir dosya için burada `.gnmap` uzantısını kullanıyorum, ancak hangisini isterseniz onu kullanmaktan çekinmeyin:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Bu format çeşitli amaçlar için kullanılabilir ve özellikle hızlı kodlama/sıralama için kullanışlıdır. Bununla birlikte, daha sonra inceleyeceğimiz format lehine terk edilme eğilimindedir.



not: `-oG` greppable formatı Nmap 7.90'dan beri resmi olarak kullanımdan kaldırılmıştır. Uyumluluk için hala kullanılabilir. Uyumluluk amacıyla hala kullanılabilir, ancak herhangi bir geliştirme veya otomatik ayrıştırma için XML veya normal biçimi kullanmanız önerilir._



#### C. Nmap çıktısı için XML formatı



Bu eğitimde bahsetmeye değer son format XML'dir. Önceki iki formatın aksine, bu format insanlar tarafından değil, diğer araçlar veya komut dosyaları tarafından okunmak üzere tasarlanmıştır.



XML (_eXtensible Markup Language_), verileri depolamak ve taşımak için kullanılan, özel etiketler aracılığıyla hiyerarşik bir yapı sunan bir biçimlendirme dilidir.



Nmap içinde XML formatı, ana bilgisayarlar, bağlantı noktaları ve tespit edilen güvenlik açıkları hakkında bilgilerin yanı sıra standart Nmap çıktısında görüntülenmeyen ek bilgiler de dahil olmak üzere gerçekleştirilen taramalar hakkında generate ayrıntılı raporlar için kullanılır.



XML formatında bir çıktı dosyası generate için `-oX` seçeneğini ("XML" den "O") kullanmamız gerekir:



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Sonuç, terminalinizde Nmap'in standart çıktısının yanı sıra geçerli dizininizde XML biçiminde bir dosyadır.



Elbette XML formatı insanlar tarafından okunmak ve yorumlanmak üzere tasarlanmamıştır. Bununla birlikte, Nmap çıktısının bu biçimi üzerinde komut dosyası veya otomatik analiz yapmak istiyorsanız, kullanılan etiketler ve yapı hakkında bir fikriniz olması gerekir. Örneğin, burada Nmap tarafından oluşturulan ve 1 ana bilgisayar için tarama sonuçlarını gösteren XML dosyasının içeriğinin bir kısmı yer almaktadır:



![nmap-image](assets/fr/51.webp)



nmap taraması sırasında 1 ana bilgisayar için XML kaydı örneği



Burada pek çok bilgi var ve biz özellikle iki açık portla ilgileniyoruz:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Bu formatın sonuçların otomatik olarak ayrıştırılmasını kolaylaştıracağını anlıyoruz, çünkü her bilgi parçası özel, adlandırılmış bir etiket veya nitelikte düzgün bir şekilde düzenlenmiştir. Özellikle, daha önce karşılaşmadığımız bir bilgi parçası buluyoruz: CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



CPE'den modül 2'nin 2. bölümünde kısaca bahsetmiştik ve bu bilgi sürüm tespiti sırasında eşleşmelerde belirlenir. Nmap, ilişkili CPE'yi bulmak için hizmet, teknoloji ve sürüm algılama mekanizmalarını kullanır.



Bu, bu bilgileri kullanan veritabanları ve uygulamalarla yeniden kullanmamızı sağlar. Özellikle CVE'lere atıfta bulunan NVD veritabanını düşünüyorum. Her CVE için, güvenlik açığından etkilenen CPE'leri içerir. İşte NVD veritabanından `a:microsoft:internet_information_services:7.5` ile ilgili bir CVE örneği:



![nmap-image](assets/fr/52.webp)



nVD veri tabanındaki bir CVE'nin ayrıntılarında bir CPE'nin varlığı



Çok net bir bilgi yapısı sunan ve Nmap tarafından toplanan veya işlenen tüm verileri içeren bu formatın faydalarını artık daha iyi anlıyoruz.



Bir refleks olarak, Nmap taramalarımı sistematik olarak aynı anda üç formatta da kaydediyorum. Bu, bir `<name>.nmap` dosyası, bir `<name>.xml` dosyası ve bir `<name>.gnmap` dosyası oluşturacak olan `-oA <name>` seçeneği ("All" için "A") ile mümkün olmaktadır. Bu şekilde, sonuçlara geri dönmem gerektiğinde hiçbir şeyin tükenmeyeceğinden eminim.



Bu üç formatla, Nmap sonuçlarını kaydetmek ve sonunda otomatik bir şekilde işlemek için ihtiyacınız olan her şeye sahip olmalısınız. Nmap'i diğer güvenlik araçlarıyla birlikte kullanmayı incelediğimiz bir sonraki bölümde XML formatını tekrar kullanacağız.



#### III. Nmap taramasından bir HTML raporu oluşturma



XML formatı pek çok olanak sunmaktadır, özellikle de HTML formatında bir rapor oluşturmak için temel oluşturması açısından, görsel olarak daha hoş bir görünüm sağlayacaktır.



XML formatındaki bir Nmap dosyasını bir web sayfasına dönüştürmek için, öncelikle kurmamız gereken `xsltproc' aracını kullanacağız:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Bu araç kurulduktan sonra, dönüştürülecek XML dosyasını ve oluşturulacak HTML raporunun adını vermeniz yeterlidir:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Sonuç olarak, tüm taramamız güzel bir şekilde yapılandırılmış olacak, hatta birkaç renk ve içindekiler tablosunda tıklanabilir bağlantılar bile olacak!



![nmap-image](assets/fr/53.webp)



xsltproc._ tarafından oluşturulan HTML biçimindeki bir Nmap tarama raporundan alıntı



Genel olarak, Nmap tarafından kaydedilen XML dosyası XSL formatında başka bir dosyaya referans içerir:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Bu nedenle HTML'ye dönüştürme Nmap tarafından sağlanan ve kolaylaştırılan bir işlevdir, `xsltproc' bu görevi yerine getirmek için yaygın ve tanınmış bir araçtır (Nmap araç paketinden gelmez).



XSLT (_Extensible Stylesheet Language Transformations_), XML verilerinin bir web sayfasında görüntülenmesine ve XSL stillerine paralel olarak HTML biçiminde okunabilir, biçimlendirilmiş bilgilere "dönüştürülmesine" olanak tanıyan bir XSL alt kümesidir.



kaynak: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Rapordaki bilgi seviyesi Nmap'in XML formatına eşdeğerdir ve standart terminal çıktısından (_interactive output_) daha yüksektir.



### IV. Nmap'in ayrıntı düzeyini yönetme



Şimdi Debugger Nmap için veya ilerlemesini izlemek için birkaç seçeneğe göz atacağız.



Bahsetmemiz gereken ilk seçenek, Nmap'in ayrıntı düzeyini artıran `-v` seçeneğidir. İşte bir örnek:



![nmap-image](assets/fr/54.webp)



v`._ seçeneğini kullanarak nmap'in ayrıntılı çıktısı



Çok sayıda ana bilgisayar ve bağlantı noktasını hedefleyen bir taramada, görüntülenen bilgi miktarı nedeniyle terminal çıktısından yararlanmak zorlaşacaktır. Bu nedenle, bu seçenek Nmap'in standart çıktısını bir dosyada saklamanıza izin veren daha önce görülen seçeneklerle birlikte kullanılmalıdır. Verbosity kullanımı ile ilgili bilgiler bu çıktı dosyasına dahil edilmeyecektir. Yukarıdaki örnekten de görebileceğiniz gibi, bu ayrıntı Nmap'in eylemlerini ve keşiflerini net ve doğrudan izlemenizi sağlar. Veri gösteriminin yavaş olabileceği daha uzun taramalar için bu, Nmap'in mevcut etkinliğine kör olmayı ve işlerin hangi hızda ilerlediğini bilmeyi önler. Ayrıntı düzeyini bir seviye daha artırmak için `-vv` seçeneğini kullanabilirsiniz.



Nmap'in tarama sırasındaki etkinliğini daha fazla izlemek için `--packet-trace` seçeneğini kullanabilirsiniz. V` seçeneği ile, Nmap tarafından keşfedilen tüm açık portların canlı bir günlüğünü alırken, bu seçenekle, bir porta gönderilen her paket için bir günlük satırı alırız. Bu doğal olarak çok ayrıntılı bir çıktı üretir, ancak Nmap'in etkinliğinin ayrıntılı olarak izlenmesine izin verir, işte bir örnek:



![nmap-image](assets/fr/55.webp)



nmap etkinliğinin `--packet-trace`._ aracılığıyla ayrıntılı izlenmesi



Yine, `-oN`, `-oG`, `-oX` veya `-oA` seçenekleri kullanılırsa bu bilgi Nmap tarafından üretilen çıktı dosyasına kaydedilmeyecektir.



Son olarak, Nmap ayrıca iki hata ayıklama seçeneği sunar: `-d` ve `-dd`. Bu seçenekler `-v` verbosity seçeneğine benzer şekilde davranır, ancak taramanın başlangıcında teknik parametrelerin bir özeti gibi ek teknik bilgiler ekler:



![nmap-image](assets/fr/56.webp)



zamanlama seçenekleri Nmap'in hata ayıklama görünümünde görüntülenir



Önümüzdeki birkaç bölümde, "Zamanlama" seçeneklerinin neler olduğuna ve neden bunları bilmeye değer olduğuna bir göz atacağız.



Son olarak, Nmap taramasının ilerleyişine ilişkin yalnızca temel, sentetik bir genel bakış elde etmek istiyorsanız, `--stats-every 5s` seçeneğini kullanabilirsiniz. Buradaki "5s" 5 saniye anlamına gelir ve ihtiyaçlarınıza göre değiştirilebilir. Bu, Nmap'ten ilerlemesi hakkında geri bildirim alacağımız sıklıktır:



![nmap-image](assets/fr/57.webp)



nmap'in `--stats-every` seçeneği tarafından görüntülenen bilgiler



Özellikle, ilerleme yüzdesinin yanı sıra içinde bulunduğu aşamanın bir göstergesini de alabiliriz: [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/) aracılığıyla ana bilgisayar keşif aşaması, açık TCP bağlantı noktalarının keşif aşaması, vb. Bu bilgiler, tarama sırasında "Enter" tuşuna basarak terminal çıktısından da elde edilebilir.



Bununla birlikte, Nmap bir görevin ne kadar süreceğini tahmin etmede çok iyi değildir, çünkü kaç ana bilgisayar ve hizmeti taraması gerektiğini önceden bilmez.



### V. Sonuç



Bu bölümde, Nmap tarama sonuçlarını farklı dosya formatlarında kaydetmek için bir dizi seçeneği inceledik. Bu çok kullanışlı olacaktır, çünkü gerçekçi bağlamlarda tarama sonuçları yüzlerce hatta binlerce satır alabilir! Ayrıca hata ayıklama amacıyla ya da tarama ilerleme raporu almak için Nmap'in verbosity seviyesini nasıl artıracağımızı da gördük.



XML formatı, Nmap sonuçlarıyla çalışabilen birkaç aracı inceleyeceğimiz bir sonraki bölümde özellikle yararlı olacaktır.




## 10 - Nmap'i diğer güvenlik araçlarıyla birlikte kullanma



### I. Sunum



Bu bölümde, Nmap'in diğer ücretsiz ve açık kaynaklı güvenlik araçlarıyla birlikte klasik kullanımlarından bazılarına göz atacağız. Özellikle, Nmap'in gücünü ve verimliliğini daha da artırmak için önceki bölümlerde öğrendiklerimizi kullanacağız.



Nmap tarama sonuçlarını XML olarak kaydedebilme özelliği, verileri bir dizi başka araçla uyumlu hale getirir. Günümüzde neredeyse tüm programlama ve komut dosyası dilleri XML'i ayrıştırabilen kütüphanelere sahip olduğundan, bu verilerin işlenmesini çok daha kolay hale getirmektedir. Özellikle saldırgan güvenliğe yönelik olan bir dizi araç, Nmap tarafından oluşturulan XML formatını işlemek için işlevlere sahiptir. Şimdi daha yakından bakalım.



Nasıl kullanıldıklarını ya da nasıl çalıştıklarını detaylandırmadan birkaç saldırı aracından bahsedeceğim. Okuyucunun bunların temel kullanımlarına aşina olduğunu ve halihazırda çalışır durumda olduklarını varsayacağım. Bu bölüm özellikle [siber güvenlik] profesyonellerinin (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), eğitim alanların ya da konuyu derinlemesine incelemeye karar verenlerin ilgisini çekecektir.



### II. Nmap sonuçlarını Metasploit'e aktarma



Saldırgan güvenlik ve güvenlik açığı araştırmalarında Nmap verilerini yeniden kullanmak için bakacağımız ilk araç Metasploit'tir.



Metasploit bir istismar ve saldırı çerçevesidir. Ücretsiz bir çözümdür ve Ruby veya Python ile yazılmış çok sayıda modül içeren tanınmış bir araçtır. Bunlar, güvenlik açıklarından yararlanılmasını, saldırıların gerçekleştirilmesini, arka kapıların oluşturulmasını, geri aramaların yönetilmesini (C&C veya İletişim ve Kontrol işlevleri) ve her şeyin tek tip olarak kullanılmasını sağlar.



Özellikle, bu iyi bilinen ve yaygın olarak kullanılan işletim çerçevesi, ana bilgisayarların, bağlantı noktalarının, hizmetlerin, kimlik doğrulama bilgilerinin ve daha fazlasının depolandığı bir postgreSQL [veritabanı] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) ile çalışabilir.





- Resmi Metasploit belgeleri: [https://docs.metasploit.com/](https://docs.metasploit.com/)




İşte bu noktada Nmap ve çıktısı devreye girer, çünkü Nmap çıktısının XML formatı Metasploit'in veritabanına kolayca aktarılabilir ve böylece ana bilgisayarlar ve hizmetler veritabanı doldurulabilir ve bunlar daha sonra hızlı bir şekilde şu veya bu saldırı için hedef olarak belirlenebilir.



Metasploit etkileşimli kabuğuma girdikten sonra, o günkü ortamıma özgü bir tür alan olan bir çalışma alanı oluşturarak başlıyorum:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Çalışma alanım oluşturulduktan sonra, veritabanı ile iletişimin çalışır durumda olduğunu doğrulamamız gerekir:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Son olarak, Nmap taramamızı XML formatında içe aktarmak için Metasploit `db_import` komutunu kullanabiliriz:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



İşte tüm bu komutların çalıştırılmasının sonucu:



![nmap-image](assets/fr/58.webp)



xML biçimindeki bir Nmap taramasını Metasploit veritabanına aktarma



Burada her bir ana bilgisayarın hizmetleriyle birlikte içe aktarıldığını görebilirsiniz. Bu veriler daha sonra belirli bir hizmet için `services` veya `services -p <port>` komutuyla görüntülenebilir:



![nmap-image](assets/fr/59.webp)



xML dosyasından Metasploit veritabanına aktarılan hizmetlerin listesi



Son olarak, gerçekleştirilecek saldırının hedeflerini belirtmek için kullanılan `RHOSTS` yönergesi için girdi olarak elde edilen hizmetlerin listesini "dönüştürecek" olan `-R` seçeneği sayesinde bu verileri bir modülde hızlı ve kolay bir şekilde yeniden kullanabiliriz. İşte [SSH] hizmetlerine kaba kuvvet saldırısı yapmanızı sağlayan `ssh_login` modülü ile bir örnek (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



saldırının hedefi olarak belirtilen hizmetleri içe aktarmak için `services -R` seçeneğini kullanın



Bu, Metasploit'te Nmap verileriyle neler yapılabileceğinin sadece küçük bir örneğidir, ancak bu bilgilerin bir sızma testi, güvenlik açığı taraması veya siber saldırının bir parçası olarak ne kadar hızlı ve kolay bir şekilde yeniden kullanılabileceği konusunda size küçük bir fikir verir. Ayrıca, Nmap'in sonuçları veritabanına aktarmak için doğrudan Metasploit'ten çalıştırılabileceğini de belirtmek gerekir (komut `db_nmap`), bu da ele alınması gereken bir başka ilginç konu!



### III. Aquatone web tarayıcısı ile Nmap kullanımı



Nmap sonuçlarının saldırgan güvenlik ve güvenlik açığı analizi için yeniden kullanılmasına ilişkin bu bölümde tanıtmak istediğim ikinci araç Aquatone'dur.



Aquatone, bir ağ üzerindeki web uygulamalarını verimli bir şekilde keşfetmek için tasarlanmış bir web tarayıcısıdır. Web hizmetleri keşfi, alt alan adı tanımlama, bağlantı noktası analizi ve web uygulaması parmak izi için gelişmiş özellikler sunar. Hepsi kolay web güvenlik analizi için HTML, JSON ve metin raporlarında açık ve net bir şekilde sunulmuştur.



Metasploit'te olduğu gibi Aquatone da Nmap'in XML formatını doğrudan işleyebilir ve tarama için bir hedef olarak kullanabilir. Özellikle, bir Nmap raporunun içerebileceği tüm verilerden yalnızca ilgilenilen ana bilgisayarları ve hizmetleri (web hizmetleri) çıkarabilir.





- Araç bağlantısı: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Nmap'in XML çıktısını Aquatone ile kullanmak için, XML dosyasını Aquatone tarafından tüketilecek bir boruya göndermeniz yeterlidir. İşte bir örnek:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Aquatone normalde web hizmetlerini bulmak için ana bilgisayarlarda bağlantı noktası keşfi gerçekleştirirken, bu bağlamda yalnızca bu işlemi zaten gerçekleştirmiş olan Nmap'in sonuçlarına güvenecek ve böylece zaman kazanacaktır:



![nmap-image](assets/fr/61.webp)



nmap sonuçlarını XML formatında `aquatone`._ ile kullanmak



Bilginiz için, Aquatone tarafından hazırlanan rapordan bir alıntı aşağıda yer almaktadır:



![nmap-image](assets/fr/62.webp)



bir `aquatone` raporu örneği



Şahsen ben Aquatone'u, özellikle ekran görüntüsü alma işlevi sayesinde ağda bulunan web sitesi türlerine hızlı bir genel bakış elde etmek için sık sık kullanıyorum.



Burada da, XML formatında eksiksiz bir Nmap raporuna sahip olmak zaman kazandırır ve başka bir araçta yeniden kullanılmasını kolaylaştırır.



### IV. Sonuç



Bu iki örnek, Nmap'in XML formatının, yapılandırılmış, kullanımı kolay bir veri formatı olduğu için diğer araçların sonuçlarını kullanmasını kolaylaştırdığını açıkça göstermektedir. Otomatik raporlama araçları, grafiksel gösterimler veya daha karmaşık, tescilli güvenlik açığı tarayıcıları gibi bu sonuçları işleyebilen birçok başka araç vardır.



Elbette, Nmap sonuç verilerini uygun gördüğünüz şekilde işlemek ve yeniden kullanmak için Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) veya XML ayrıştırma kitaplığına sahip başka bir dilde kendi komut dosyalarınızı ve araçlarınızı da geliştirebilirsiniz.



Bu bölüm bizi, özellikle NSE komut dosyaları aracılığıyla güvenlik açığı taraması için Nmap'in daha gelişmiş kullanımı hakkındaki eğitim modülünün sonuna getiriyor.



Eğitimin bir sonraki bölümü, diğer şeylerin yanı sıra, Nmap'in gerçekleştirebileceği belirli taramalarla ilgili bazı ek, daha teknik en iyi uygulamalara ve ipuçlarına odaklanacaktır. Ayrıca, büyük ağları tararken özellikle yararlı olan tarama performansı optimizasyon seçeneklerine de göz atacağız.




## 11 - Ağ tarama performansını iyileştirme



### I. Sunum



Bu bölümde, çeşitli özel seçenekleri kullanarak Nmap ile gerçekleştirilen ağ taramalarının hızını nasıl optimize edeceğimizi öğreneceğiz. Özellikle, _timeout_ yönetiminden aracın önceden kaydedilmiş yapılandırmalarına kadar Nmap'in iç işleyişi hakkında daha fazla bilgi edineceğiz.



Nmap'in özelliklerine iyice göz attığımıza göre, şimdi bu canavar ve onun gücü ile başa çıkalım. Bu aracı daha önce büyük ağlarda kullandıysanız, muhtemelen aracın gücüne rağmen bazı taramaların uzun zaman alabildiğini fark etmişsinizdir. Ve bunun iyi bir nedeni var: birkaç seçenekli basit bir `nmap' komutu yüz binlerce potansiyel sistem ve hizmeti hedefleyen milyonlarca paketi generate yapabilir.



Dahası, bazı ağ ekipmanı yapılandırmaları, paketlerinizi reddetme veya IP Address'ünüzü güvenlik nedenleriyle yasaklama riskini alarak kasıtlı olarak daha yavaş bir hız (saniyedeki paket sayısı) uygulayabilir.



Bağlama bağlı olarak, bu bölümde göreceğimiz gibi, tüm bunları optimize etmeye çalışmak faydalı olabilir.



Her durumda, bakacağımız parametrelerin varsayılan değerlerini ve kullanacağınız seçeneklerin doğru bir şekilde dikkate alınıp alınmadığını Nmap debug (önceki bölümde görülen `-d` seçeneği) aracılığıyla kontrol edebilirsiniz:



![nmap-image](assets/fr/63.webp)



nmap'in `-d` seçeneği aracılığıyla Zamanlama seçeneklerini görüntüleyin._



### II. Nmap taramalarının hızını yönetme



#### A. Paralelleştirmeyi yönetme



Varsayılan olarak, Nmap taramalarını optimize etmek için paralelleştirme kullanır ve kullandığı tüm parametreler çeşitli seçenekler aracılığıyla değiştirilebilir. Ancak, bu parametreleri değiştirmenin gerçekten gerekli olduğu durumlar oldukça nadirdir, bu nedenle bu eğitimde ayrıntılı olarak ele almayacağız:





- `--min-hostgroup/max-hostgroup <size>`: paralel ana bilgisayar tarama gruplarının boyutu.





- `--min-parallelism/max-parallelism <numprobes>`: Probların paralelleştirilmesi.





- `--scan-delay/--max-scan-delay <time>`: Problar arasındaki gecikmeyi ayarlar.




Sadece var olduklarını ve kullanılabileceklerini bilin.



#### B. Saniye başına paket sayısını yönetme



Varsayılan olarak, Nmap saniyede gönderdiği paket sayısını ağ yanıtına göre kendisi ayarlar. Ancak, saniyedeki paket sayısı açısından takip edilecek en yüksek ve/veya en düşük değeri tanımlayarak bu ayarı zorlamak mümkündür. Bu ayar `--min-rate <number>` ve `--max-rate <number>` seçenekleri kullanılarak yapılır, burada `number` saniyedeki paket sayısını temsil eder. Örnek:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Bu seçenekler, süreci hızlandırmak ya da kullanılan bant genişliğini sınırlamak için taramaların hızını özel ihtiyaçlarınıza göre ayarlamanıza olanak tanır. İkinci durum (tarama hızının sınırlandırılması), özellikle Nmap kullanırken ağ gecikmesi yaşıyorsanız (ki bu oldukça nadirdir), sizi bu seçeneklere yönlendirecek en olası durumdur.



### III. Bağlantı hatalarını ve zaman aşımlarını yönetme



Nmap taramalarının hızını optimize etmek (veya daha fazla doğruluk sağlamak) için oynayabileceğimiz bir başka parametre _timeout_ ve _retry_ ile ilgilidir.



Timeouts_ için bu, Nmap'in bir yanıt beklemeyi bırakacağı ve hizmeti veya ana bilgisayarı ulaşılamaz olarak kabul edeceği **yanıt yok zaman aşımıdır**. _retry_ için bu, Nmap'in devam etmeden önce gerçekleştireceği **bir işlemdeki ardışık deneme sayısıdır**.



Paralelleştirmede olduğu gibi, _timeout_ ve _retry_ yönetimi ana bilgisayar veya hizmet keşif aşamalarına uygulanabilir:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: bir Exchange'ün gidiş-dönüş süresini belirtir. Yine, bu parametre aslında tarama sırasında anında hesaplanır ve uyarlanır. Nmap bu süreyi ağ tepkisine göre anında hesapladığı için kullanmanız gerekmeyecektir.





- `--max-retries <number>`: port taraması sırasında bir paketin yeniden iletim sayısını sınırlar. Varsayılan olarak, Nmap, özellikle ağ düzeyinde gecikmeler veya kayıplar bulursa, tek bir hizmet için 10 yeniden denemeye kadar gidebilir, ancak çoğu durumda yalnızca bir tane gerçekleştirilir.





- `--host-timeout <time>`: Nmap'in port tarama, hizmet algılama ve bu ana bilgisayarla ilgili diğer işlemler de dahil olmak üzere tüm işlemleri için bir ana bilgisayarda geçireceği maksimum süreyi belirtir. Bu zaman aralığı herhangi bir yanıt veya **işlemlerin tamamlanması** olmadan aşılırsa, Nmap bu ana bilgisayarla ilgili herhangi bir sonuç görüntülemeden terk edecek ve listesindeki bir sonrakine geçecektir. Bu, Nmap'in belirli bir ana bilgisayarda geçirdiği maksimum süreyi kontrol etmenize, inatçı ana bilgisayarlarda takılıp kalmaktan kaçınmanıza ve genel tarama süresini optimize etmenize olanak tanır.




Günlük çalışmalarımda, taramalarımı optimize etmek için `--max-retries` ve `--host-timeout` seçeneklerini kullanıyorum:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Bu parametreler, tarama davranışını özel ihtiyaçlara ve ağ koşullarına göre ayarlamak için ek esneklik sunar. Ancak, taranan ana bilgisayarlar üzerindeki yük ve potansiyel doğruluk kaybı açısından etkilerinin farkında olmanız gerekir.



### IV. Hazır konfigürasyonların kullanımı



Bu bölümde gördüğümüz çeşitli seçenekler tek tek ya da Nmap tarafından sunulan hazır yapılandırmaların bir parçası olarak kullanılabilir. Bu _templates_ (yapılandırma şablonları) kullanılmasını sağlayan seçenek `-T <number>` veya `-T <name>` dir. Kullanılabilir 5 _templates_ seviyesi vardır:



```
-T<0-5>: Set timing template (higher is faster)
```



Nmap varsayılan olarak _template_ 3 (_normal_) kullanır ve bu genellikle yeterlidir.



Kendi adıma, genellikle oldukça hızlı olmam gereken bağlamlarda çalışıyorum (mümkün olduğunca eksiksiz kalırken) ve sık sık `-T4` seçeneğini kullanıyorum.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Bu tarama için hata ayıklama bilgilerinin bize gösterdiği şey şudur:



![nmap-image](assets/fr/64.webp)



nmap taraması sırasında `-T4` kurulumunun kullanılması



### V. Sonuç



Bu bölümde, Nmap'in gücünü, saldırganlığını ve performansını yönetmek için kullanabileceğiniz çeşitli tekniklere ve seçeneklere baktık. Bu seçenekler özellikle büyük ağları tararken ve daha nadiren gizli amaçlar için kullanışlıdır.



Bir sonraki bölümde, Nmap'i kullanmak ve güvenliğini sağlamak için birkaç en iyi uygulamaya göz atacağız.




## 12 - Nmap kullanırken veri güvenliği ve gizliliği



### I. Sunum



Bu bölümde, Nmap tarafından üretilen, işlenen ve depolanan verilerin güvenliği ve her şeyden önce gizliliği ile ilgili olarak benimsenmesi gereken bir dizi iyi uygulamaya bakacağız.



Nmap'in bir bilgi sistemi içinde kullanımı hızlı bir şekilde saldırgan bir eylem olarak kategorize edilebilir. Sonuç olarak, amaçlanan hedeflerin, toplanan verilerin ve tarama için kullanılan sistemin güvenliğini garanti ederken yasal bir çerçeve içinde hareket etmek için bir dizi önlem alınması gerekir.



### II. Uygun izinlerin alınması



Bir ağı veya sistemi taramadan önce, uygun yetkileri aldığınızdan emin olun. Yetki almadan sistemleri güvenlik açıkları için taramak (`NSE komut dosyaları`) yasa dışı olabilir ve özellikle bilgi sistemi güvenliği resmi görev alanınızın bir parçası değilse yasal sonuçları olabilir.





- Bir hatırlatma olarak: [Ceza Kanunu: Bölüm III: Otomatik bilgi işlem sistemlerine saldırılar] (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Hassas verilerin korunması



Nmap tarafından üretilen sonuçlar, özellikle bir saldırgan tarafından istismar edilebilecek bilgi sistemindeki zayıflıklar hakkında bilgi içerdiklerinde hassas olarak kabul edilebilir. Ancak aynı zamanda herkesin erişimine açık olmayan sistemlerle ilgili olduklarında da (örneğin hassas, endüstriyel, sağlık veya [yedek] bilgi sistemleri (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Ayrıca, kullanılan NSE komut dosyalarına bağlı olarak, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) NSE tarama sonuçlarının da tanımlayıcılar içerebileceğini gördük.



Böylece, bu tarama sonuçlarına erişmeyi başaran kötü niyetli bir kişi, bu eylemleri kendisi gerçekleştirmeden, tespit edilme riski altında, bilgi sisteminin bir haritasına ve çok sayıda teknik bilgiye sahip olacaktır.



Bu nedenle, Nmap kullanırken aşağıdakiler dahil ancak bunlarla sınırlı olmamak üzere hassas bilgileri uygunsuz bir şekilde toplamamaya veya saklamamaya dikkat etmek önemlidir:





- Çıktı verilerinin şifrelenmesi: Nmap taramalarınızın sonuçlarını saklamanız veya iletmeniz gerekiyorsa, veri gizliliğini korumak için bunları şifrelediğinizden emin olun. Bu, hassas bilgilerin yetkisiz kişilerce ele geçirilmesini önleyecektir. İdeal olarak, veriler taramayı gerçekleştirmek için kullanılan sistemi terk eder etmez şifrelenmelidir (güçlü bir parola ile şifrelenmiş bir ZIP arşivi çok iyi bir başlangıçtır).





- Erişim kontrollerini ayarlayın: Nmap taramalarınızın sonuçlarına depolanacakları yerde yalnızca yetkili kişilerin erişebildiğinden emin olun. Hassas bilgileri yetkisiz erişimden korumak için uygun erişim kontrolleri kurun.





- Verileri kullanırken dikkatli olun: tarama verilerini aktarırken, kopyalarken veya işlerken, veri güvenliğini sıkı kontrol altında tuttuğunuzdan emin olun. Bu şu anlama gelir: İnternete bağlı bir iş istasyonunun `Download' dizininde ortalıkta bırakmayın, dahili HTTP dosya Exchange uygulamanızdan geçmelerine izin vermeyin, öğle tatiliniz sırasında iş istasyonunu kilitlemeden Not Defterinizi açık bırakmayın, vb.




### IV. Agresif taramaların yönetilmesi



Bu eğitim boyunca gördüğümüz gibi, Nmap ağ düzeyinde çok ayrıntılı olabilir. Ayrıca düzgün biçimlendirilmemiş paketler gönderebilir ve ürettiği ağ çerçevelerinde ve paketlerinde protokol yapısına kesinlikle uymayabilir. Tüm bu eylemler, belirli sistemler ve hizmetler üzerinde, bazen sistem ve ağ kaynaklarının arızalanmasına veya doygunluğuna neden olacak kadar etkili olabilir.



Herhangi bir olaydan kaçınmak için, Nmap'in davranışına hakim olmanız ve bu eğitimde tartışılan çeşitli seçenekler aracılığıyla onu kullanıldığı bağlama nasıl uyarlayacağınızı bilmeniz gerekir. Nmap'i endüstriyel [donanım] (https://www.it-connect.fr/actualites/actu-materiel/) içeren bir bilgi sisteminde, yerel bir güvenlik duvarı tarafından korunan Windows sistemlerinden oluşan bir kullanıcı ağında veya bir ağ çekirdeğinde aynı şekilde kullanmamız gerekmeyecektir.



Umarım, bu eğitimdeki çeşitli dersler size Nmap'in davranışını nasıl yöneteceğinizi ve analiz edeceğinizi öğretmiştir, ancak öğrenmenin en iyi yolu yaparak öğrenmektir. Bu yüzden kullanacağınız Nmap seçeneklerine aşina olduğunuzdan emin olun.



### V. Tarama sisteminin korunması



İlk bölümde, çoğu durumda Nmap'in `root' veya yerel yönetici olarak çalıştırılması gerektiğini gördük. Bunun nedeni, sistem kararlılığı veya diğer uygulamaların gizliliği açısından yüksek ve riskli izinler gerektiren ağ kütüphaneleri aracılığıyla bazen oldukça düşük düzeyde ağ işlemleri gerçekleştirmesidir.



Sonuç olarak, Nmap kurulu olduğu sistemin hassas bir bileşeni olarak görülebilir. Eski sürümler bilinen güvenlik açıkları içerebileceğinden, Nmap'in en son sürümünü kullandığınızdan emin olun. Güncel bir sürüm kullanarak, aracın kullanımıyla ilgili riskleri en aza indirebilirsiniz.



Nmap'i `root` olarak bir oturum aracılığıyla değil, ayrıcalıklı bir kullanıcıya belirli ayrıcalıklar vererek kullanmayı tercih ettiyseniz, böylece Nmap'i kullanmak için ihtiyaç duyduğu her şeye sahip olur (`sudo` veya _capabilities_), Nmap'in tam bir ayrıcalık yükseltmesinin bir parçası olarak kullanılabileceğini unutmayın:



![nmap-image](assets/fr/65.webp)



nmap ayrıcalıklarının `sudo`._ aracılığıyla yükseltilmesi



Burada, Nmap komutunu `sudo` aracılığıyla kullanıyorum, ancak bu, sistemde `root` olarak etkileşimli bir kabuk elde etmemi sağlıyor, ki asıl amaç bu değildi.



Nmap'i ağ taraması yapmak için tasarlanmamış sistemlere kurmak da son derece sakıncalıdır. Özellikle sunucuları ya da iş istasyonlarını düşünüyorum. Bir yandan, bu ayrıcalık yükseltme için potansiyel bir vektör ekleyecektir, ancak her şeyden önce saldırgana bir saldırı aracına zahmetsiz erişim sağlayacaktır.



Son olarak, tarama için kullanılan sistemin güvenliği daha geniş kapsamlı olarak sağlanmalıdır, böylece kendisi izinsiz giriş veya bilgi sızıntısı için bir vektör haline gelmez. Bir sistem yöneticisi olarak, kendi iş istasyonunuz yerine, ideal olarak sınırlı bir kullanım ömrüne sahip özel bir sistem kullanmak daha iyidir.



### VI. Sonuç



Sonuç olarak, Nmap'i gerçek hayatta veya üretim koşullarında kullanmadan önce düzgün bir şekilde ustalaştığınızdan emin olun ve sonuçlarını işlerken ve yönetirken dikkatli olun. İlk yaklaşım şirketinizin güvenliğini artırmaya yönelikken, hasara neden olmak, veri sızdırmak veya bir tehlikeyi kolaylaştırmak üzücü olacaktır.



## 13 - TCP aracılığıyla port taramaları: SYN, Connect ve FIN



### I. Sunum



Bu bölümde ve bir sonraki bölümde, en yaygın kullanılanlardan başlayarak Nmap'te bulunan farklı TCP tarama türlerine daha yakından bakacağız: SYN, Connect ve FIN taramaları.



Fark etmiş olabileceğiniz gibi, Nmap TCP taramaları için çeşitli seçenekler sunar:



![nmap-image](assets/fr/66.webp)



nmap'te mevcut tarama teknikleri._



Buradaki fikir, bu yöntemlerden bazılarını açıklamak, farklılıklarını, avantajlarını ve sınırlamalarını anlamanıza yardımcı olmaktır. Bağlama veya ne bilmek istediğinize bağlı olarak, bir seçeneği veya diğerini tercih etmenin daha iyi olduğunu göreceksiniz.



### II. TCP SYN taraması veya "Yarı Açık tarama



İnceleyeceğimiz ilk TCP tarama türü `Yarı Açık Tarama` olarak da bilinen `TCP SYN Taraması`dır. İlk port taramalarımızdan sonra yaptığımız ağ taramalarını hatırlarsanız, bu, root haklarıyla çalıştırıldığında [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) tarafından varsayılan olarak kullanılan tarama türüdür.



Çeviri, bu taramanın nasıl çalıştığını anlamanıza yardımcı olacaktır. Aslında, bir TCP SYN taraması, hedeflenen her bağlantı noktasına bir TCP SYN paketi gönderir; bu, ünlü _Üç yönlü el sıkışma_ TCP'nin bir parçası olarak bir istemci (bağlantı kurmak isteyen) tarafından gönderilen ilk pakettir. Normalde, port hedef sunucuda açıksa ve arkasında bir hizmet çalışıyorsa, sunucu istemcinin SYN'sini doğrulamak ve TCP bağlantısını başlatmak için bir TCP SYN/ACK paketi geri gönderir. Bu yanıt, SYN ve ACK bayrakları 1 olarak ayarlanmış bir TCP paketi biçimini alır ve bağlantı noktasının açık olduğunu ve bir hizmete yönlendirildiğini doğrulamamızı sağlar.



Öte yandan, eğer port kapalıysa, sunucu bize bağlantı isteğini sonlandırmak için RST ve ACK bayrakları 1 olarak ayarlanmış bir `TCP` paketi gönderecektir, böylece bu portun arkasında hiçbir hizmetin aktif görünmediğini bileceğiz:



![nmap-image](assets/fr/67.webp)



açık ve kapalı portlar için tCP SYN Tarama davranış diyagramı



TCP SYN Taraması`nın daha somut bir görünümünü elde etmek için, TCP/80 portunu, bu portta aktif bir web sunucusu olan bir ana bilgisayara taradım. Wireshark ile bir ağ taraması çalıştırdığımızda aşağıdaki akışı görebiliriz (tarama kaynağı: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



açık bir bağlantı noktası için TCP SYN taraması sırasında ağ yakalama



İlk satırda, tarama kaynağının TCP/80 portu üzerinden `10.10.10.203` ana bilgisayarına bir TCP paketi gönderdiğini görüyoruz. Bu TCP paketinde, bunun bir TCP bağlantı başlatma isteği olduğunu belirtmek için SYN bayrağı 1 olarak ayarlanmıştır.



Ardından, ikinci satırda, hedefin bir `TCP SYN/ACK` ile yanıt verdiğini görüyoruz, yani bir bağlantı başlatmayı ve dolayısıyla TCP/80 portundan akış almayı kabul ediyor. Bu nedenle TCP/80 portunun açık olduğu ve taranan sunucuda bir web sunucusunun mevcut olduğu sonucuna varabiliriz.



Ana bilgisayarımız daha sonra bağlantıyı kapatmak için bir RST paketi göndererek taranan ana bilgisayarın yanıt bekleyen açık bir TCP bağlantısını sürdürmemesini sağlar. Birçok bağlantı noktasında tarama yapılması durumunda, TCP bağlantılarının kapatılmaması, sunucunun sürdürebileceği yanıt bekleyen bağlantı sayısını doygunluğa ulaştırarak hizmet reddine yol açabilir (bkz. [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



Wireshark'ta, gerçekleştirdiğimiz her test için TCP bayraklarının durumunu görebileceksiniz. Bu, paketin SYN, SYN/ACK, ACK vb. bir paket olup olmadığını gösterecektir:



![nmap-image](assets/fr/69.webp)



wireshark'ta bir paketin TCP bayraklarını görüntüleme (TCP SYN burada)



Tersine, aynı testi iki makine arasında çalıştırdım, ancak bu kez hiçbir hizmetin etkin olmadığı bir TCP/81 bağlantı noktasını taradım (tarama kaynağı: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



kapalı bir bağlantı noktası için TCP SYN taraması sırasında ağ yakalama



Taranan ana bilgisayar, bağlantı noktası açık olmadığında benim `TCP SYN`ime yanıt olarak bir `TCP RST/ACK` döndürür.



Belirtildiği gibi, Nmap'i ayrıcalıklı bir terminalden çalıştırırken, TCP SYN Taraması varsayılan moddur ve `-sS` (`scan SYN`) seçeneği ile zorlanabilir:



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




TCP SYN Taraması hız nedeniyle en sık kullanılan taramadır. Öte yandan, bir istemcinin _Three Way Handshake_'i tamamlayamaması (yani sunucu SYN/ACK'inden sonra ACK'yi göndermemesi), bir sunucuda veya ağdaki aynı kaynaktan çok fazla kez gözlemlenirse şüpheli görünebilir. Aslında, bir TCP SYN'e yanıt olarak bir TCP SYN/ACK paketi aldıktan sonra bir istemcinin normal davranışı bir "onay" (ACK) göndermek ve ardından Exchange'yı başlatmaktır.



Bununla birlikte, her pozitif yanıt için bir ACK gönderme zahmetine girmediği için biraz daha hızlı bir tarama sağlar. SYN Scan'in avantajı, taranacak bağlantı noktası başına yalnızca bir paket gönderildiğinden, tespit edilme şansının daha yüksek olması pahasına hızıdır.



Buna ek olarak, TCP SYN taraması bir portun bir güvenlik duvarı tarafından filtrelenip filtrelenmediğini (korunup korunmadığını) tespit edebilir. Aslında, hedef ana bilgisayarın önündeki bir güvenlik duvarı, koruması gereken bir bağlantı noktasında bir TCP SYN paketi aldığında nasıl davrandığı ile tespit edilebilir. Basitçe yanıt vermeyecektir. Ancak, gördüğümüz gibi, her iki durumda da (açık veya kapalı port), ana bilgisayardan bir yanıt gelir. Bu üçüncü davranış, taranan ana bilgisayar ile taramayı çalıştıran makine arasında bir güvenlik duvarının varlığını ortaya çıkaracaktır. İşte taranan bir port bir güvenlik duvarı tarafından filtrelendiğinde Nmap'in döndürebileceği sonuç:



![nmap-image](assets/fr/71.webp)



filtrelenmiş bir bağlantı noktasını tararken nmap ekranı



Tarama zamanında bir ağ yakalama gerçekleştirdiğimizde, aslında hiçbir yanıt verilmediğini görebiliriz:



![nmap-image](assets/fr/72.webp)



güvenlik duvarı tarafından filtrelenen bir bağlantı noktası için TCP SYN taraması sırasında ağ yakalama



Kapalı bir port ile filtrelenmiş bir port arasındaki fark şudur: filtrelenmiş bir port bir güvenlik duvarı tarafından korunan bir porttur, kapalı bir port ise üzerinde hiçbir hizmetin çalışmadığı ve bu nedenle TCP paketlerimizi işleyemeyen bir porttur. TCP SYN taraması gibi bazı TCP tarama türleri bir portun filtrelenip filtrelenmediğini tespit edebilirken, diğer tarama türleri bunu yapamaz.



### III. TCP Bağlantısı taraması veya Tam Açık tarama



İkinci TCP tarama türü, _Tam Açık Tarama_ olarak da bilinen `TCP Bağlantı taraması`dır. TCP SYN taramasıyla aynı şekilde çalışır, ancak bu kez sunucudan gelen olumlu bir yanıttan (bir SYN/ACK) sonra bir `TCP ACK` döndürür. Bu nedenle `Tam Açık' olarak adlandırılır, çünkü bağlantı tamamen açılır ve tarama sırasında açılan her bağlantı noktasında başlatılır, böylece TCP _Three Way Handshake_'e saygı duyulur:



![nmap-image](assets/fr/73.webp)



tCP Connect Açık ve kapalı portlar için tarama davranış diyagramı



Açık bir portu hedefleyen bir `TCP Connect taraması` sırasında ağdan geçenler burada görülebilir:



![nmap-image](assets/fr/74.webp)



açık bir bağlantı noktası için TCP Connect taraması sırasında ağ koklama



Gönderilen ilk TCP paketinin istemci tarafından gönderilen bir `TCP SYN` olduğunu görebiliriz ve sunucu daha sonra portun açık olduğunu ve aktif bir hizmet barındırdığını belirten bir `TCP SYN/ACK` ile yanıt verecektir. Meşru bir istemciyi tamamen simüle etmek için, Nmap daha sonra sunucuya bir `TCP ACK` gönderecektir. Tersine, kapalı bir portu tararken:



![nmap-image](assets/fr/75.webp)



kapalı bir bağlantı noktası için TCP Connect taraması sırasında ağ yakalama



Sunucunun `SYN` paketimize verdiği yanıtın yine bir `TCP RST/ACK` paketi olduğuna dikkat edin, böylece portun kapalı olduğunu ve üzerinde hiçbir servisin çalışmadığını anlayabiliriz.



Nmap kullanırken, bir TCP Bağlantı Taraması gerçekleştirmek için `-sT` (`scan Connect`) seçeneği kullanılır. Nmap ayrıcalıksız bir oturumdan kullanıldığında, bunun varsayılan TCP tarama modu olduğunu lütfen unutmayın:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



TCP Bağlantı Taraması, bir lambda istemcisine en çok benzeyen davranışla daha meşru bir bağlantı isteğini simüle eder, bu nedenle daha az sayıda bağlantı noktasında bir taramayı tespit etmek daha zordur. Bununla birlikte, taranan makinenin açık portlarındaki her TCP bağlantısını tamamen başlattığı için daha yavaştır.



Ağ saldırı tespit ve koruma hizmetleri (IDS, IPS, EDR) kuruluysa, 10.000 portluk bir Nmap taraması yine de kolayca tespit edilebilir. Bir saldırgan dikkat çekmemek istediğinde 445 (SMB) veya 80 (HTTP) gibi sunucularda sıklıkla açık olan ve yaygın güvenlik açıkları sunan az sayıda stratejik olarak seçilmiş bağlantı noktasına odaklanma eğiliminde olacaktır.



TCP Connect Scan her iki durumda da bir yanıt beklediğinden, hedef ana bilgisayarda bağlantı noktalarını filtreliyor olabilecek bir güvenlik duvarının varlığını da tespit edebilir.



### IV. TCP FIN taraması veya "Gizli Tarama



Gizli Tarama olarak da bilinen `TCP FIN Taraması`, açık bir bağlantı noktasını tespit etmek için bir TCP bağlantısını sonlandıran bir istemcinin davranışını kullanır.



TCP'de oturum sonu, FIN bayrağı 1 olarak ayarlanmış bir TCP paketi göndermek anlamına gelir. Normal bir Exchange'de, sunucu istemciyle tüm iletişimi keser (yanıt yok). Sunucunun istemciyle aktif bir TCP bağlantısı yoksa, bir `RST/ACK` gönderecektir. Bu nedenle, bir dizi porta `TCP FIN` paketleri göndererek açık ve kapalı portlar arasında ayrım yapabiliriz:



![nmap-image](assets/fr/76.webp)



açık ve kapalı portlar için tCP FIN tarama davranış diyagramı



Bir _Stealth taraması_ sırasında ağı tekrar yakaladım ve taranan bağlantı noktası açık olduğunda gördüğünüz şey bu:



![nmap-image](assets/fr/77.webp)



açık bir bağlantı noktası için TCP FIN taraması sırasında ağ yakalama



İstemcinin bir TCP bağlantısını sonlandırmak için bir veya iki paket gönderdiğini ve sunucunun yanıt vermediğini görebiliriz. Sadece bağlantının sona erdiğini kabul eder ve iletişimi durdurur.



Kapalı bir portu taradığımızda şimdi gördüğümüz şey şu:



![nmap-image](assets/fr/78.webp)



kapalı bir port için TCP FIN taraması sırasında ağ yakalama



Sunucunun bir `TCP RST/ACK` paketi gönderdiğini görüyoruz, bu nedenle açık ve kapalı bir port arasında bir davranış farkı var ve bir TCP FIN paketi göndererek bir sunucudaki açık portları listeleyebiliyoruz. Nmap kullanarak, TCP FIN Taraması yapmak için `-sF` (`scan FIN`) seçeneği kullanılır:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Taraması Windows ana bilgisayarlarında çalışmaz, çünkü işletim sistemi açık olmayan bağlantı noktalarına gönderildiklerinde TCP FIN paketlerini yok sayma eğilimindedir. Dolayısıyla, bir Windows ana bilgisayarında TCP FIN Taraması çalıştırırsanız, tüm bağlantı noktalarının kapalı olduğu izlenimini edinirsiniz.



Bu nedenle çeşitli tarama yöntemlerine aşina olmak ve aralarındaki farkı anlamak önemlidir.



Her iki durumda da TCP FIN bir yanıt beklemeyeceğinden, hedef ana bilgisayar ile tarama kaynağı arasında bir güvenlik duvarının varlığını tespit edemeyecektir.



İşte Nmap'in TCP FIN tarama sonucuna bir örnek:



![nmap-image](assets/fr/79.webp)



nmap tarafından yapılan bir TCP FIN taramasının sonuçları._



Aslında, belirli bir bağlantı noktasındaki ana bilgisayardan yanıt alınamaması, bağlantı noktasının filtrelendiği anlamına gelebilir, ancak aynı zamanda açık ve aktif olduğu anlamına da gelebilir.



Bu tarama "gizli" olarak adlandırılır, çünkü generate fazla trafik oluşturmaz ve genellikle hedeflenen sistemlerde günlüğe kaydetmeye neden olmaz. Herhangi bir alarm vermeden bir ağ üzerindeki bağlantı noktalarını gizlice keşfetmek için kullanılabilir. Bununla birlikte, yukarıda belirtildiği gibi, etkinliği hedef sisteme bağlı olarak değişebilir, güvenlik ekipmanının yapılandırmasına bağlı olarak takdir edilebilir.



### V. Sonuç



Nmap tarafından sunulan farklı TCP tarama türleri hakkındaki iki bölümden ilki için bu kadar! Bir sonraki bölümde, bir ana bilgisayardaki açık portları tespit etmek için farklı şekillerde çalışan XMAS, Null ve ACK TCP tarama türlerine bakacağız.





## 14 - TCP üzerinden port taramaları: XMAS, Null ve ACK



### I. Sunum



Bu bölümde, Nmap tarafından sunulan çeşitli TCP tarama yöntemlerini keşfetmeye devam edeceğiz. Burada, belirli bir hedefte açık olan portlar ve hizmetler hakkında bilgi almak için TCP'ye özgü özellikleri kullanan `XMAS`, `Null` ve `ACK` yöntemlerine bakacağız.



### II. TCP XMAS taraması



XMAS Scan TCP, bir ağ üzerindeki normal kullanıcı veya makine davranışını hiç taklit etmediği için biraz sıra dışıdır. Aslında, XMAS Scan, belirli güvenlik duvarlarını veya filtreleme mekanizmalarını atlamak için `URG` (Acil), `PSH` (İt) ve `FIN` (Bitir) bayrakları 1 olarak ayarlanmış TCP paketleri gönderecektir.



XMAS adı, bu bayrakları açık görmenin olağandışı olduğu gerçeğinden gelir. Bir TCP paketinde üç bayrak da aynı anda ayarlandığında, yanan bir Noel ağacı gibi görünür:



![nmap-image](assets/fr/80.webp)



xMAS taramasında kullanılan tCP bayrakları



Burada bu bayrakların rolü hakkında ayrıntıya girmeden, bu üç bayrak etkinken bir paket gönderirken, hedef portun arkasındaki aktif bir servisin herhangi bir paket döndürmeyeceğini bilmek önemlidir. Öte yandan, eğer port kapalıysa, bir TCP RST/ACK paketi alacağız. Artık bir makinedeki portları listelerken açık ve kapalı bir portun davranışını ayırt edebileceğiz:



![nmap-image](assets/fr/81.webp)



tCP XMAS Açık ve kapalı portlar için tarama davranış diyagramı



Yine aynı mantığı izleyerek, aktif bir web sunucusuna sahip bir ana bilgisayarın TCP/80 bağlantı noktasındaki bir ağ taraması, açık bir bağlantı noktası tespit ederken aşağıdaki davranışı gösterir (tarama kaynağı `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



açık bir bağlantı noktası için TCP XMAS taraması sırasında ağ yakalama



Tarama kaynağının `10.10.10.203` ana bilgisayarına iki TCP XMAS paketi (`FIN`, `PSH` ve `URG` bayrakları 1 olarak ayarlanmış olarak) gönderdiğini ve hedeften herhangi bir geri dönüş olmadığını görebiliriz, bu da portun açık olduğunu gösterir. Tersine, kapalı bir bağlantı noktasında bir `TCP XMAS Taraması` gerçekleştirirken, aşağıdaki sonuç gözlemlenir:



![nmap-image](assets/fr/83.webp)



kapalı bir bağlantı noktası için TCP XMAS taraması sırasında ağ yakalama



TCP paketimizin yanıtı, portun kapalı olduğunu belirten bir `TCP RST/ACK` olur. Bu tekniği Nmap ile kullanmak için, `-sX` (`scan XMAS`) seçeneği bir TCP XMAS Taraması gerçekleştirmenizi sağlar:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



TCP XMAS taramasının, TCP SYN veya Connect gibi diğer bazı tarama türlerinin aksine, hedef ile tarama makinesi arasında olabilecek güvenlik duvarlarını tespit edemediğini belirtmek önemlidir. Aslında, iki ana bilgisayar arasındaki aktif bir güvenlik duvarı, hedeflenen bağlantı noktası filtrelenmişse (yani güvenlik duvarı tarafından korunuyorsa) hiçbir TCP dönüşünün yapılmamasını sağlayacaktır. Bu nedenle, yanıt alınamaması durumunda, bağlantı noktasının güvenlik duvarı tarafından korunup korunmadığını veya açık ve etkin olup olmadığını bilmek imkansızdır. TCP FIN taramasında olduğu gibi, Windows gibi belirli uygulamaların veya işletim sistemlerinin bu tür taramanın sonuçlarını bozabileceğini de bilmelisiniz.



not: Windows'un son sürümlerinde XMAS/FIN/NULL taramaları için destek sınırlıdır ve bu tür hedeflerde sonuçlar tutarsız olabilir. (Güncelleme 2025)_



### III. TCP Null taraması



TCP XMAS taramasının aksine, TCP Null taraması tüm bayrakları 0 olarak ayarlanmış TCP tarama paketleri gönderir. Bu da makineler arasındaki normal bir Exchange'da asla bulunmayacak bir davranıştır, çünkü bayraksız bir TCP paketi göndermek TCP protokolünü tanımlayan RFC'de belirtilmemiştir. Bu yüzden daha kolay tespit edilebilir.



TCP XMAS taraması gibi, bu tarama da belirli güvenlik duvarları veya filtreleme modülleri ile etkileşime girerek paketlerin geçmesine izin verebilir:



![nmap-image](assets/fr/84.webp)



açık ve kapalı portlar için tCP Null Scan davranış diyagramı



İşte açık bir bağlantı noktasında TCP Null taraması sırasında ağda görülebilecekler:



![nmap-image](assets/fr/85.webp)



açık bir bağlantı noktası için TCP Null taraması sırasında ağ yakalama



Tarama makinesi, sunucudan herhangi bir yanıt almadan bayraksız bir paket (Wireshark'ta `[<None>]`) gönderir. Tersine, hedef port kapalı olduğunda:



![nmap-image](assets/fr/86.webp)



kapalı bir bağlantı noktası için TCP Null taraması sırasında ağ yakalama



Nmap ile TCP Null taraması yapmak için `-sN` (`scan Null`) seçeneğini kullanmanız yeterlidir:



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Bir bağlantı noktası açık olduğunda ve bir güvenlik duvarı etkin olduğunda (her iki durumda da sunucu geri bildirimi yok) yanıt aynı olduğundan, TCP Null taraması bir güvenlik duvarının varlığını tespit edemez. Dahası, güvenlik duvarı, port filtrelenmiş olsa bile bayraksız TCP paketlerine yanıt vermediğinden, bir portun açık olduğunu öne sürerek sonucu tahrif edebilir. Bu, `TCP Null`, `XMAS` veya `FIN` taramaları gibi açık ve filtrelenmiş (güvenlik duvarı korumalı) bir bağlantı noktası arasında ayrım yapamayan taramaları kullanırken, elde edilen sonuçların yorumlanmasında tutarlı kalmak için bilinmesi gereken önemli bir bilgidir.



### IV. TCP ACK taraması



TCP ACK taraması, hedef ana bilgisayarda veya hedef ile tarama kaynağı arasında bir güvenlik duvarının varlığını tespit etmek için kullanılır.



Diğer taramaların aksine, TCP ACK taraması ana bilgisayarda hangi portların açık olduğunu belirlemeye çalışmaz, bunun yerine bir filtreleme sisteminin aktif olup olmadığını belirler ve her port için `filtered` veya `unfiltered` ile yanıt verir. TCP SYN` veya `TCP Connect` gibi bazı TCP taramaları her ikisini de aynı anda yapabilirken, `TCP FIN` veya `TCP XMAS` gibi diğerleri filtrelemenin varlığını belirleyemez. Bu nedenle TCP ACK taraması yararlı olabilir:



![nmap-image](assets/fr/87.webp)



filtrelenmiş ve filtrelenmemiş bağlantı noktaları için tCP ACK Tarama davranış diyagramı



Bu tür bir tarama gerçekleştirmek için Nmap'in `-sA' seçeneğini kullanacağız. İşte port filtrelenmişse, yani engellenmişse ve bir güvenlik duvarı tarafından korunuyorsa TCP ACK taramasının sonucu:



![nmap-image](assets/fr/88.webp)



tCP ACK Taraması sırasında nmap ekranı._



Güvenlik duvarı olan ve olmayan bir ana bilgisayar için örnek sonuç. Nmap, `10.10.10.203` ana bilgisayarının TCP/80 ve TCP/81 bağlantı noktalarında `filtered` sonucunu döndürür. Wireshark aracılığıyla yapılan bir ağ analizinde davranış aşağıdaki gibidir:



![nmap-image](assets/fr/89.webp)



güvenlik duvarı tarafından filtrelenmeyen bir bağlantı noktası için TCP ACK taraması sırasında ağ yakalama



Bir güvenlik duvarı mevcutsa hedef makine hiçbir şey döndürmez.



Bu taramayı Nmap ile başlatmak için `-sA` (`scan ACK`) seçeneğini kullanın:



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Sonuç



Daha önce sunulanlara ek olarak TCP üzerinden taramanın üç farklı yöntemini inceledik. Bu farklı yöntemler çok özel koşullarda ve bağlamlarda, özellikle de gizlilik kavramlarının mevcut olduğu sızma testleri veya Kırmızı Ekip operasyonları bağlamında kullanılmalıdır.



## 15 - Nmap CheatSheet - Öğretici komutların özeti



### I. Sunum



İşte Nmap'in birçok komutunun ve kullanım durumunun kısa bir özeti, böylece bunları günlük kullanımda hızlı bir şekilde bulabilir ve yeniden kullanabilirsiniz.



### II. Nmap: CheatSheet IT-Connect



İşte sunulan komutların bir hile sayfası. Bu sayfa Nmap'in en yaygın kullanımlarını bulmayı kolaylaştırır.





- Liman taraması




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Aktif ana bilgisayarları keşfetme




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



not: `-sP` seçeneği birkaç yıldır kullanılmamaktadır ve `-sn` ile değiştirilmelidir. (Güncelleme 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Sürüm algılama




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- NSE komut dosyaları: güvenlik açıkları aranıyor




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Nmap çıktı yönetimi




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Performans optimizasyonu




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- TCP tarama türleri




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Umarım bu komutları faydalı bulursunuz. Taramalarınızın hedefini bağlamınıza göre uyarlamayı ve gerçekleştirilen testlere tam olarak hakim olmak için resmi belgelere başvurmayı unutmayın.



### III. Sonuç



Nmap eğitimi şimdi tamamlandı. Artık bu kapsamlı ve güçlü aracı kullanmak için ihtiyacınız olan temel bilgilere sahipsiniz. Üretimde kullanmadan önce kontrollü ortamlarda (Hack The Box, VulnHub, sanal makineler) pratik yapmanızı şiddetle tavsiye ederiz.



Aracın iç işleyişi ve gelişmiş özellikleri hakkında keşfedilecek çok şey var. Bununla birlikte, burada sunulan komutlara ve kavramlara hakim olmak, Nmap'i güvenle ve uygun bir şekilde kullanmanızı sağlayacaktır.