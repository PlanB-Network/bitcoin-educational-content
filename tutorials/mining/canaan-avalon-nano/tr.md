---
name: Canaan Avalon Nano 3S
description: ASIC Avalon'unuzu solomining veya Miner havuzlama için yapılandırma
---

![cover](assets/cover.webp)



Bu eğitimde, Miner'nin evde kolay kullanımı için Canaan Avalon Nano 3S'in nasıl kurulacağına bir göz atacağız.



Şimdiye kadar, belirli bir görevi yerine getirmek için özel olarak tasarlanmış ASIC (*Uygulamaya Özel Entegre Devre*) makineleri - bu durumda, Bitcoin'ün Miner'ü için Hash hesaplaması (SHA-256) - özellikle ev kullanımı için uygun değildi. Gürültü rahatsızlığı, üretilen ısı ve elektrik tesisatınızı bu cihazların muazzam gücünü destekleyecek şekilde uyarlama ihtiyacı, çoğumuzun katılmasını engelledi.



Bugün, ASIC makinelerinin önde gelen üreticilerinden biri olan Canaan, nispeten sessiz ve kurulumu çok kolay (tak ve çalıştır) bir dizi ürün sunarak evde Miner isteyen özel şahısların pazarını ele almaya karar verdi.



Bu cihazlar, **Avalon Nano 3S (140W)** örneğinde olduğu gibi yardımcı ısıtıcı olarak veya **Avalon Mini 3** örneğinde olduğu gibi **800W** çıkışlı mini radyatör olarak pazarlanmaktadır.



https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Lütfen eşdeğer güce sahip geleneksel ısıtıcılarla aradaki fiyat farkının, çoğu durumda finansal bir kâr elde etmenize izin vermediğini unutmayın. Bedava (ihtiyaç fazlası) veya çok ucuz elektriğe erişiminiz olmadığı sürece, Mining'un faaliyeti ile üretilen satoshiler bu fiyat farkını asla telafi etmeyecektir.



Bence bu cihazlar daha çok kişisel nedenlerle bunu yapmak isteyenler için evde Miner yapmanın basit bir yolu olarak görülmelidir: *kYC olmayan Satss almak / solominasyon yaparak "piyango" oynamak / Hashrate ademi merkeziyetçiliğine katılmak vb...*, kışın odasını ısıtmak için üretilen ısıdan ** bonus olarak** yararlanırken. Ancak en azından çoğu durumda (Batı ülkeleri) para tasarrufu yapmanın bir yolu olarak değil.



## Kutudan Çıkarma ve Özellikler



İlk olarak, Avalon Nano 3S kutusunun içinde ne olduğuna bakalım.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



Kutuyu açtığınızda, daha sonra göreceğimiz gibi, yerel ağınıza bağlanmasını sağlamak için cihazın USB portuna takmanız gereken bir WIFI alıcısı içeren bir karton kılıf bulacaksınız. Ayrıca kullanım kılavuzu ve gerektiğinde cihazı fabrika ayarlarına sıfırlamak için metal bir pim de kutu içeriğinde yer almaktadır.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



Her şey kutudan çıktığında, işte elinizde bulunanlar: elbette makinenin kendisi, kullanım kılavuzu, WIFI alıcısı, yukarıda bahsedilen metal uç ve cihazın Supply gücü. Verilen kredi kartı bize göre bahsetmeye değmez.



![image](assets/fr/05.webp)



Aşağıda Nano 3S'in genel teknik özelliklerini özetleyen bir tablo yer almaktadır:



| Caractéristique                                      | Valeur                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Taux de hachage                                      | 6 Th/s +- 5%                                            |
| Consommation d'énergie                               | 140 W                                                   |
| Bruit                                                | 30 - 40 dB                                              |
| Plage de température de sortie d'air                 | 60-70°C (sous température ambiante 25°C)                |
| Exigences de température ambiante pour l'utilisation | de -5 à 30°C                                            |
| Plage d'entrée de l'appareil                         | 28V 5A continu                                          |
| Plage d'entrée de l'adaptateur                       | 110-240V AC 50/60Hz                                     |
| Taille de la machine                                 | Longueur: 205 mm /  Largeur: 115 mm / Hauteur:  58.5 mm |
| Poids de la machine                                  | 0.86 kg                                                 |

## Gücü açma ve yerel ağa bağlanma



Ambalajı açtıktan sonra, Avalon Nano 3 S'nizi mümkünse ısının dolaşmasına izin vermek için nispeten açık bir alana yerleştirin. Ardından, aşağıda gösterildiği gibi küçük WIFI alıcı modülünü takarak başlayın:



![image](assets/fr/06.webp)


Ardından Supply'ün USB-C fişini cihazın USB-C bağlantı noktasına takarak güç verin.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



Cihaz açılacak ve ekranda Avalon Nano logosu görünecek, ardından "Lütfen Ağı Avalon Family Uygulamasıyla Yapılandırın" yazan bir "cep telefonu" logosu belirecektir.



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



Bunu yapmak için mobil uygulama mağazanıza gidin, **Avalon Family** uygulamasını arayın ve indirin.



![image](assets/fr/11.webp)


Kurulduktan sonra, sağ üst köşedeki "Atla" düğmesine, ardından "Ekle" düğmesine ve son olarak "Ara" düğmesine tıklayarak açın. Akıllı telefonunuzda Bluetooth'un etkin olduğundan emin olun, böylece cihazın algılanması sorunsuz çalışır.



![image](assets/fr/12.webp)


Cihaz uygulama tarafından algılandıktan sonra üzerine tıklayın ve "Bağlan "ı seçin. Daha sonra WIFI bağlantı bilgilerinizi girebileceğiniz ekrana yönlendirileceksiniz.


![image](assets/fr/13.webp)


Cihaz yerel ağınıza bağlandığında, ekran şimdi aşağıdaki gibi görünecektir:



![image](assets/fr/14.webp)



Henüz bir havuz yapılandırılmadığı için "hayali" bir Hashrate ve cihazın saatini, tarihini, gücünü ve IP Address'sını gösterir - cihazın Interface'üne bir PC ve tarayıcı aracılığıyla erişmek istiyorsanız çok kullanışlıdır (bu konuda daha sonra daha fazla bilgi verilecektir).



![image](assets/fr/15.webp)




## Bir Mining pool'ye Bağlanma



**Bu kısım Nano 3s ve Mini 3 için ortaktır, çünkü süreçler kesinlikle aynıdır**.



İster "solominate" ister Miner "pool" yapmak isteyelim, bir Mining pool'e bağlanmamız gerekecek. Aslında, cihazımız Bitcoin ağının farkında olmayan bir Hash yapıcıdan başka bir şey değildir. Onu bir havuza bağlamak Bitcoin ağına erişimini ve üzerinde çalışabileceği blok şablonları almasını sağlar.



### Bir Mining pool'ye bağlanmak için uygulamayı kullanma



Avalon Family uygulamasında, aşağıda gösterildiği gibi cihazı seçin. Daha sonra otomatik olarak makinenin yönetici şifresini değiştirmeniz istenecektir. Bunu yapmak istiyorsanız "Tamam" üzerine tıklayın veya varsayılan erişim şifresi "admin" olarak bırakmak için iptal üzerine tıklayın.


![image](assets/fr/16.webp)


Ardından "Ayarlar" ve ardından "Havuz Yapılandırması "nı seçin ve istenen 3 havuz için parametreleri girin.


2. ve 3. havuzlar, bunlardan birinin arızalanması durumunda yedek olarak işlev görecektir, böylece Miner'ünüz boşuna çalışmaz. Varsayılan olarak, Hashrate 1 numaralı havuza yönlendirilecektir



Bizim durumumuzda biz seçiyoruz:




- 1 - Halka Açık Havuz,
- 2 - CkPool,
- 3 - Okyanus.



![image](assets/fr/17.webp)



Bir Mining pool'e nasıl bağlanılacağı hakkında daha fazla ayrıntı için lütfen bu eğitimlere bakın:



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.network/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Özetlemek gerekirse, şunlara ihtiyacımız var





- havuz Address, genellikle **stratum+tcp://xxxxxx:port**.





- gW-28 Address* cihazınız ve cihazınız için seçtiğiniz *sözde* cihazdan oluşan "çalışanın" adı, 2'si bir *nokta* ile ayrılır, örneğin:**bc1qxxxxxxxxxxxxx.MonAvalonNano3S**





- genellikle her zaman "**x**" olan parola



Havuz bilgileri girildikten sonra "Kaydet" düğmesine tıklayın.



![image](assets/fr/18.webp)


Cihazı talimatlara uygun şekilde yeniden başlatın ve Hashrate tercih ettiğiniz havuza (#1) gelene kadar birkaç dakika bekleyin.



### Bir Mining pool'a bağlanmak için tarayıcıyı kullanma



Ayrıca bir Mining pool'e bağlanabilir ve daha genel olarak cihazınızın Interface yönetim sistemine favori tarayıcınız üzerinden erişebilirsiniz.



Bunu yapmak için, tarayıcının arama çubuğuna aşağıdaki ekranda gösterilen cihazın IP Address'ünü yazın, örneğimizde **192.168.144.6**



![image](assets/fr/15.webp)



Avalon Family uygulamasını açmanızı ve uygulamayla birlikte görüntülenen QR kodunu taramanızı isteyen aşağıdaki sayfa görünecektir.



![image](assets/fr/20.webp)



Uygulamayı açın ve sağ üstteki 3 tire işaretine, ardından taramaya tıklayın. Tarayıcının QR kodunu tarayın, ardından uygulamanın yönetici şifresini girin ve Tamam'a tıklayın.



![image](assets/fr/21.webp)



Burada Avalon'unuzla etkileşime geçmenizi sağlayan web sayfasındasınız. Bu, makineyi yapılandırmaktan ziyade makinenin ölçümlerini görüntülemek için bir gösterge tablosudur.



Ancak havuz ayarlarına yine de bu şekilde, sağ alt köşedeki **"Pool Config "** seçeneğine tıklayarak erişilebilir.



![image](assets/fr/22.webp)



Mobil uygulamada olduğu gibi havuz parametrelerinizi buradan girebilirsiniz.



![image](assets/fr/23.webp)



## Cihazınızı Avalon Family uygulaması üzerinden kontrol edin



Şimdi evimizdeki Miner'i yerel ağımıza bağladık ve Hashrate'ümüzü Minings havuzlarına yönlendirdik. Şimdi Avalon Family uygulaması aracılığıyla makinemizin temel özelliklerini keşfedelim.



Avalon ailesi uygulamasında, Avalon Nano 3S'e karşılık gelen simgeye tıklayın.


ardından size 3 menü sunulur: "Çalışma Modu", "Işık kontrolü" ve "Ayarlar". İlk olarak, "Çalışma Modu" üzerine tıklayın. Daha sonra makineniz için 3 güç modu sunulacaktır.



**Düşük**: 70W güç tüketimi için yaklaşık 3 Th/s Hashrate sağlar


**Orta**: 100 W güç tüketimi için yaklaşık 4,5 Th/s Hashrate sağlar


**Yüksek**: maksimum 140W tüketimde yaklaşık 6 Th/s Hashrate verecektir



![image](assets/fr/31.webp)


Bir adım geri atalım ve "Işık Kontrolü" menüsünü inceleyelim. Bu tamamen kozmetiktir. Rengi, yoğunluğu, ısıyı değiştirmek, geceleri cihazın LED'lerini kapatmak vb. için bir dizi seçenek mevcuttur. Kendiniz bulmak çok kolay.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



Son olarak, kullanabileceğimiz son menü, Mining havuzlarımıza bağlanmak için daha önce gördüğümüz "Ayarlar" menüsüdür. Burada havuzlarınızı yönetebilir, cihazın yönetici şifresini değiştirebilir ve garanti bitiş tarihi, filtre temizliği veya arıza durumunda destekle nasıl iletişime geçileceği gibi çeşitli ölçümleri gözlemleyebilirsiniz.



![image](assets/fr/35.webp)


Bakım ve filtreyi mümkün olduğunca temiz tutmak için elektrikli süpürge kullanmanızı ve tıkanmayı önlemek için hava girişlerini ve çıkışlarını düzenli olarak vakumlamanızı öneririz.



Avalon Nano 3 S'imizi yerel ağımıza nasıl bağlayacağımızı, Hashrate'ımızı Mining havuzlarına nasıl yönlendireceğimizi ve Avalon Family uygulamasını kullanarak seçenekler ve ayarlar arasında nasıl gezineceğimizi öğreten bu eğitimin sonuna geldik.



Daha fazla bilgi edinmek için Avalon'un bir üst versiyonu olan Mini 3 hakkındaki eğitimimize göz atın.



https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7