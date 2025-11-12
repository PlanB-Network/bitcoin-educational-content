---
name: Pi-Hole
description: Tüm ağınız için bir reklam engelleyici
---
![cover](assets/cover.webp)



___



*Bu eğitim Florian Duchemin tarafından [IT-Connect](https://www.it-connect.fr/) adresinde yayınlanan orijinal içeriğe dayanmaktadır. Lisans [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Orijinal metinde değişiklikler yapılmış olabilir.*



___



## I. Sunum



Hepimiz favori tarayıcımızı başlatır başlatmaz bunu yapmışızdır: bir **adblocker** (reklam engelleyici) yükleyin. Ancak, TV tarayıcısı veya bir Android cihaz vb. kullanırken. İşe yarayan bir şey bulmak biraz daha zordur. Ve evde birden fazla cihaz varsa, her tarayıcı için işlemi tekrarlamanız gerekir!



Bu eğitimde basit bir sorunu çözeceğiz**: ağımızdaki tüm makinelere bir reklam engelleyici sağlamak ve bunu merkezi olarak yönetmek.**



Bunu yapmak için, bu amaç için geliştirilmiş bir araç kullanacağız: **Pi-Hole**



Pi-Hole bir DNS obruğudur. Trafiği doğrulamak veya reddetmek için cihazlarınız tarafından yapılan DNS isteklerini kullanır, böylece sizi reklam, kötü amaçlı yazılım vb. dağıttığı bilinen adreslerden ve alan adlarından korur.



DNS, Alan Adı Sistemi anlamına gelir. Peki alan adı nedir? "it-connect.fr" sadece bir örnektir. Bir alan adı, genellikle tek bir kuruluş tarafından yönetilen bir veya daha fazla kaynak için benzersiz bir tanımlayıcıdır.



Makine adı artı alan adı, *Tam Nitelikli Alan Adı* için FQDN olarak adlandırılır. Belirli bir makineye sadece onu "arayarak" ulaşmanızı sağlar. Örneğin, "www.trucmachin.com" yazdığınızda, aslında "trucmachin.com" etki alanına ait olan "www" makinesini aramış olursunuz.



Bilgisayarlarımızın insan dilini anlamaması dışında, tek anladıkları ikilidir, bu nedenle web sitesine ulaşmak için bir telefon numarasına eşdeğer olan bir IP Address'a ihtiyaçları vardır.



Dolayısıyla, tarayıcınıza bir web sitesinin adını her girdiğinizde veya bir bağlantıya tıkladığınızda, bilgisayarınız önce bir DNS sunucusundan bu ada karşılık gelen IP Address'i ister.



**Pi-Hole daha sonra bu talepleri inceleyecek (her gün yüzlerce talep geliyor!) ve reklam ve hatta zararlı dosya barındırdığı bilinenleri otomatik olarak engelleyecektir.**



## II. Pi-Hole Kurulumu



Pi-Hole gibi bir isimle, haklı olarak bir Raspberry-Pi'ye ihtiyacınız olduğunu düşünebilirsiniz... Ancak bu tam olarak doğru değil. **Pi-Hole herhangi bir Linux bilgisayara kurulabilir (Debian, Fedora, Rocky, Ubuntu, vb.).**



Öte yandan, **bu cihazın basit bir nedenden dolayı günde 24 saat çalışması gerekeceğini aklınızda bulundurmanız gerekir: DNS yoksa İnternet de yok!** Raspberry bu nedenle iyi bir fikirdir, çünkü neredeyse hiç enerji tüketmez.



Yüklemek için Linux makinenize SSH ile bağlanın ve aşağıdaki komutu "*root*" olarak girin:



```
curl -sSL https://install.pi-hole.net | bash
```



> **Not**: Normal şartlar altında, ne işe yaradığını bilmeden bir betiği "hacklemeniz" tavsiye edilmez. Emin değilseniz, sayfaya bir tarayıcı ile gidin veya içeriği bir dosya olarak indirin.
>


> **Not:** Debian 11'in minimal sürümlerinde Curl yüklü değildir, bu nedenle yukarıdaki komutu yazmadan önce **apt-get install curl** komutuyla manuel olarak yüklemeniz gerekir.

Komut dosyası çalıştıktan sonra, bir dizi test gerçekleştirilecek ve kurulum kendi kendine hallolacaktır:



![Image](assets/fr/019.webp)



Pi-Hole'un Kurulumu



Kurulum tamamlandığında, bu ekrana yönlendirileceksiniz:



![Image](assets/fr/020.webp)



Pi-Hole başlangıç ekranı



> **Not**: Makinenizde DHCP kullanıyorsanız, bununla ilgili bir uyarı mesajı alacaksınız. Elbette, doğru kullanım için makinenize sabit bir IP atamanızı şiddetle tavsiye ederiz.

Bu ekranın ardından, birkaç bilgi mesajı alacaksınız ve ardından ilk olarak Pi-Hole'un istekleri hangi DNS sunucusuna yönlendireceğini soran yapılandırma sihirbazına yönlendirileceksiniz. Ben kendi adıma, kullanıcı gizliliği sözleşmesi olan Quad9'u seçtim.



![Image](assets/fr/021.webp)



DNS seçimi - Pi-Hole



> **Not:** Bir şirkette çalışıyorsanız, mevcut DNS sunucunuzun Active Directory etki alanı denetleyicisi olma ihtimali yüksektir. Ancak endişelenmeyin, daha sonra istediğiniz bir etki alanı için koşullu bir yeniden yönlendirici belirleyebilirsiniz. Tipik olarak, yerel etki alanınızla ilgili herhangi bir isteği DNS sunucunuza yönlendirebileceksiniz.

Bazı seçeneklerin bir DNSSEC seçeneği içerdiğini fark edeceksiniz. Temel olarak, DNS protokolü güvenli değildir (o zamanlar bu düşünülerek tasarlanmamıştır). DNSSEC, ilgili makalede açıklandığı gibi, alışverişlerin şifrelenmesi ve imzalanması yoluyla bir Layer güvenlik ekleyerek bu sorunu çözer: [DNS Güvenliği](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Her reklam engelleyici işini yapmak için bir veya daha fazla listeye ihtiyaç duyar. Pi-Hole standart olarak tek bir liste ile gelir, bu yüzden onu seçin ve daha sonra daha fazlasını ekleyin.



![Image](assets/fr/022.webp)



Interface web ile ilgili soruya gelirsek, aracın yönetim ve görselleştirme için kendi komut satırı olduğundan kurulumu isteğe bağlıdır. Ancak bu Interface oldukça hoş ve iyi yapılmış, bu yüzden aynı zamanda yüklemenizi tavsiye ederim:



![Image](assets/fr/023.webp)



Eğer Pi-Hole'u zaten bir Web sunucusu olan bir makineye kuruyorsanız, aşağıdaki soruya "hayır" yanıtını verebilirsiniz. Ancak, bunun çalışması için PHP ve birkaç modülün gerekli olduğunu lütfen unutmayın. Aksi takdirde, **lighttpd gerekli tüm modüllerle birlikte kurulacaktır**.



![Image](assets/fr/024.webp)



Daha sonra DNS isteklerini kaydetmek isteyip istemediğiniz sorulur. **Bir geçmiş tutmak istiyorsanız, bunu evet olarak ayarlayın; aksi takdirde, bunu hayır olarak ayarlayın, ancak bazı işlevleri kaybedersiniz** (sonraki ekrana bakın).



![Image](assets/fr/025.webp)



Interface web için Pi-Hole, bir API sağlayan ve DNS isteklerinden istatistikler üreten FTLDNS adlı kendi işlevini kullanır. Bu işlev, talep edilen alan adlarını, talebin arkasındaki müşterileri veya her ikisini de maskeleyen bir "gizlilik" modu içerebilir. İnsanların gizliliğini ihlal etmeden izleme yapmak istiyorsanız ya da sadece bir kamu ağında kullanım durumunda ilgili düzenlemelere uymak istiyorsanız kullanışlıdır.



![Image](assets/fr/026.webp)



Özel yaşam tarzı seçimi



Bu son soru yanıtlandıktan sonra, komut dosyası yapması gerekeni yapacaktır: GitHub depolarını indirin ve Pi-Hole'u yapılandırın. Kurulumun sonunda, önemli bilgileri içeren bir özet ekranı görüntülenecektir:



![Image](assets/fr/027.webp)



Kurulum özet ekranı



Interface web şifresini ve ağ bilgilerini not edin. Şimdi sıra mevcut konumumuzdaki DHCP hizmetini yapılandırmaya geldi.



## III. DHCP yapılandırması



Pi-Hole'un çalışabilmesi için istemcilerden gelen DNS isteklerini "çözümlemesi" gerekir, böylece istemcilerin bu istekleri gönderecekleri kişinin kendisi olduğunu bilmeleri gerekir. Bunu yapmanın birkaç yolu vardır:





- DHCP sunucunuzdaki DNS ayarlarını değiştirin (örn. Kutunuz)
- Bu sunucuyu devre dışı bırakın ve Pi-Hole tarafından sağlananı kullanın
- Pi-Hole'u DNS olarak kullanmak için her cihazı manuel olarak değiştirin



Ben şahsen ilk çözümü seçiyorum. Muhtemelen **bulunduğunuz yerde bir DHCP sunucunuz vardır** (genellikle kutunuz). Yani uğraşmanıza gerek yok.



Farklı operatörlerin kutuları (hepsi hakkında bilgim yok) ve kendi yönlendiricisi olanlar arasında çok sayıda olasılık olduğundan, bu değişiklikler için bir ekran görüntüsü vermeyeceğim. Her durumda, DHCP ayarlarına gitmeniz ve "DNS" parametresini Pi-Hole'unuzun IP Address'sını içerecek şekilde değiştirmeniz gerekecektir.



Bu yapıldıktan sonra, herhangi bir cihaz daha önce açılmışsa, eski ayarları koruyacaklardır, bu nedenle yapılandırma isteğini yeniden başlatmanız gerekecektir.



Windows iş istasyonlarında, bir komut istemi ile:



```
ipconfig /renew
```



Bir Linux iş istasyonunda:



```
dhclient
```



Diğer tüm cihazlar için kapatılmalı ve tekrar açılmalıdır.



Bu yüzden kontrol etmek için doğru parametreleri almalıdırlar:



```
ipconfig /all
```



DNS alanında, Pi-Hole'unuzun Address'si olmalıdır, benim durumumda 192.168.1.42:



![Image](assets/fr/029.webp)



## IV. Interface web Pi-Hole kullanımı



Yönetimi kolaylaştırmak için **Pi-Hole** iyi tasarlanmış bir Interface web Interface'dan yararlanır. Kullanıcı dostu ve erişilebilir, size izin verir:





- Talep sayısını, engellenen talepleri vb. gerçek zamanlı olarak görüntüleyin.
- Beyaz listenizi ve Kara listenizi yönetin
- Statik girişler, takma adlar vb. ekleyin.
- Liste ekleme
- Ve daha birçok işlev!



Kendi adıma, bir engelleme listesi ekleyeceğim. Yukarıda belirtildiği gibi, Soft ile aynı anda yalnızca bir liste yüklendi. Reklam siteleri için birçok liste var, ancak yaşadığınız ülkeye özgü en az bir tane seçmek en iyisidir. En iyi bilinen listelerden biri **EasyList**'tir ve bunlardan biri Fransa'ya özgüdür: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Eklemek için önce Interface yöneticisine bağlanın: **http://<ip_du_PiHole>/admin**



Yönetici şifresi zaten oluşturulmuştur (kurulum sonu ekran görüntüsüne bakın), bu nedenle Interface'ye erişmek için tek yapmanız gereken şifreyi girmektir:



![Image](assets/fr/030.webp)



Pi-Hole'dan Interface



Örneğin, Pi-Hole'a bağlı iki müşteri olduğunu, 442 isteği işlediğini ve bunlardan 8'inin engellendiğini görebiliriz. Bu grafikler, özellikle profesyonel bağlamda iyi bir bilgi kaynağı olabilir.



Listemizi eklemek için "**Grup Yönetimi**" ve "**Listeler**" menülerine gidin:



![Image](assets/fr/031.webp)



İlk listemizi görebiliriz "**StevenBlack**", bizimkini eklemek için yukarıda size verdiğim bağlantıyı kopyalayın ve "**Address**" alanına ekleyin, açıklama için listenin adını koymayı seçiyorum:



![Image](assets/fr/032.webp)



Pi-Hole'da liste ekleme



Geriye kalan tek şey eklemek için "**Ekle**" düğmesine tıklamak. Etkinleştirmek için, Pi-Hole'u bu listeyi devralması için "uyarmak" için ek bir adım gerçekleştirmemiz gerekiyor. Bunu yapmak için:





- Ya yerleşik komut satırını kullanın
- Ya Interface web



Ben şahsen ikincisini seçtim, çünkü dikkatlice baktıysanız, güncellemeyi gerçekleştiren PHP betiğinin bağlantısı doğrudan bulunduğumuz sayfada ("çevrimiçi" kelimesi) yer alıyor. Yani tek yapmanız gereken üzerine tıklamak, bu da sizi tek seçenekli bir sayfaya götürecektir:



![Image](assets/fr/033.webp)



Sayfa tamamlandığında, listenin dikkate alındığı anlamına gelen komut dosyasının sonucunu görüntüleyecektir (elbette bir hata mesajı görüntülenmediği sürece).



Bu eğitimin başında duyurulduğu gibi, Pi-Hole ayrıca **kötü amaçlı yazılım dağıttığı bilinen alan adlarını engellemenizi sağlar. Bu özelliği güçlendirmek için, ağınızın güvenliğini önemli ölçüde güçlendirecek olan Abuse.ch** tarafından dağıtılan düzenli olarak güncellenen alan adı listesini de eklemenizi öneririm, [bu Address] (https://urlhaus.abuse.ch/downloads/hostfile/) adresinde mevcuttur.



Elbette ilgili olduğunu düşündüğünüz listeleri ekleyebilir veya kara liste menüsünden kara listenizi manuel olarak yönetebilirsiniz.



## V. Pi-Delik testleri



Artık her şey yerli yerinde olduğuna göre, tek yapmanız gereken düzgün çalıştığından emin olmak için çözümü test etmektir.



Örneğin, kötü amaçlı yazılım barındırdığı bilindiği için Abuse.ch listesinde bulunan *http://admin.gentbcn.org/* alan adına ulaşmaya çalışacağım:



![Image](assets/fr/034.webp)



Belli ki bir yerde engellenmişim. İşi yapanın Pi-Hole olduğundan emin olmak için, Interface web "Sorgu Günlüğü "ndeki sorgu günlüğünü kontrol ederek bunun bir liste girişinden gelen bir engelleme olduğunu görebiliriz:



![Image](assets/fr/035.webp)



## VI. Sonuç



Bu eğitimde, yalnızca gezinme konforunuz için reklamların çoğunu ortadan kaldırmakla kalmayan, aynı zamanda kimlik avı ve kötü amaçlı yazılım yayan alanları** engelleyerek **bir Layer güvenlik ekleyen bir DNS sunucusunu nasıl kuracağınızı gösterdik.



Hepsi ücretsizdir ve Raspberry-Pi'ye kurulursa ekonomiktir (güç tüketimi açısından).