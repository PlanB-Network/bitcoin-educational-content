---
name: Canaan Avalon Mini 3
description: ASIC Avalon'unuzu solomining veya Miner havuzlama için yapılandırma
---

![cover](assets/cover.webp)



Bu eğitimde, Miner'nin evde kolay kullanımı için Canaan Avalon Mini 3'ün nasıl kurulacağına bir göz atacağız.



Şimdiye kadar, belirli bir görevi yerine getirmek için özel olarak tasarlanmış ASIC (*Uygulamaya Özel Entegre Devre*) makineleri - bu durumda, Bitcoin'ün Miner'ü için Hash hesaplaması (SHA-256) - özellikle ev kullanımı için uygun değildi. Gürültü rahatsızlığı, üretilen ısı ve elektrik tesisatınızı bu cihazların muazzam gücünü destekleyecek şekilde uyarlama ihtiyacı, çoğumuzun katılmasını engelledi.



Bugün, ASIC makinelerinin önde gelen üreticilerinden biri olan Canaan, nispeten sessiz ve kurulumu çok kolay (tak ve çalıştır) bir dizi ürün sunarak evde Miner isteyen özel şahısların pazarını ele almaya karar verdi.



Bu cihazlar, **Avalon Nano 3S (140W)** örneğinde olduğu gibi yardımcı ısıtıcı olarak veya **Avalon Mini 3** örneğinde olduğu gibi **800W** çıkışlı mini radyatör olarak pazarlanmaktadır.



https://planb.network/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Lütfen eşdeğer güce sahip geleneksel ısıtıcılarla aradaki fiyat farkının, çoğu durumda finansal bir kâr elde etmenize izin vermediğini unutmayın. Bedava (ihtiyaç fazlası) veya çok ucuz elektriğe erişiminiz olmadığı sürece, Mining'un faaliyeti ile üretilen satoshiler bu fiyat farkını asla telafi etmeyecektir.



Bence bu cihazlar daha çok kişisel nedenlerle bunu yapmak isteyenler için evde Miner yapmanın basit bir yolu olarak görülmelidir: *kYC olmayan Sats'lar almak / solominasyon yaparak "piyango" oynamak / Hashrate ademi merkeziyetçiliğine katılmak vb...*, kışın odasını ısıtmak için üretilen ısıdan ** bonus olarak** yararlanırken. Ancak en azından çoğu durumda (Batı ülkeleri) para tasarrufu yapmanın bir yolu olarak değil.



## Kutudan Çıkarma ve Özellikler



### Avalon Nano 3S



İlk olarak, Avalon Mini 3 kutusunun içinde ne olduğuna bakalım.



![image](assets/fr/24.webp)



Kutuyu açtığınızda, kullanım talimatları doğrudan önünüzdedir, ancak daha da önemlisi, WIFI alıcı modülü kullanım talimatlarının solundaki yuvarlak beyaz etiketin altında gizlenmiştir. Ona daha sonra ihtiyacınız olacak.



![image](assets/fr/25.webp)



Köpük bloğun altında cihaz, ardından kutudan çıkarıldığında güç Supply ünitesi bulunur.



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## Gücü açma ve yerel ağa bağlanma



Ambalajından çıkardıktan sonra, ısının düzgün bir şekilde dolaşmasını sağlamak için Avalon Mini 3'ünüzü mümkünse nispeten açık bir alana yerleştirin. Ardından, küçük WIFI alıcı modülünü cihazın alt tarafındaki USB bağlantı noktasına takarak, Supply'ü prize takarak ve güç düğmesinin "1" konumunda olduğundan emin olarak başlayın.



![image](assets/fr/28.webp)



Bu adımlar tamamlandıktan sonra, cihazın LED ekranı yanar ve "Bluetooth" sembolünü göstererek Avalon Family uygulaması aracılığıyla yerel ağınıza bağlanmaya hazır olduğunu belirtir.



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Bunu yapmak için mobil uygulama mağazanıza gidin, **Avalon Family** uygulamasını arayın ve indirin.



![image](assets/fr/11.webp)


Kurulduktan sonra, sağ üst köşedeki "Atla" düğmesine, ardından "Ekle" düğmesine ve son olarak "Ara" düğmesine tıklayarak açın. Akıllı telefonunuzda Bluetooth'un etkin olduğundan emin olun, böylece cihazın algılanması sorunsuz çalışır.



![image](assets/fr/12.webp)


Cihaz uygulama tarafından algılandıktan sonra üzerine tıklayın ve "Bağlan "ı seçin. Daha sonra WIFI bağlantı bilgilerinizi girebileceğiniz ekrana yönlendirileceksiniz.


![image](assets/fr/13.webp)


Yerel ağınıza bağlandıktan sonra Mini 3'ünüz IP Address, saat, Hashrate ve elektrik gücü gibi bilgileri görüntüleyecektir.



Aşağıda Mini 3'ün genel teknik özelliklerine ilişkin özet bir tablo yer almaktadır:



| Caractéristique                                      | Valeur                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consommation électrique                              | 800 W                                                     |
| Bruit                                                | 35-55 dB                                                  |
| Température de l'air en sortie                       | 60-70°C (sous température ambiante 25°C)                  |
| Exigences de température ambiante pour l'utilisation | -5° C - 40°C                                              |
| Plage d'entrée de l'appareil                         | 110V-240V AC 50/60Hz                                      |
| Taille de la machine                                 | Longueur: 760 mm / Profondeur: 104 mm / Hauteur: 214.5 mm |
| Poids de la machine                                  |  8.35 kg                                                  |

## Bir Mining pool'ya Bağlanma



**Bu kısım Nano 3s ve Mini 3 cihazları için ortaktır, çünkü işlemler kesinlikle aynıdır **



İster "solominate" ister Miner "pool" yapmak isteyelim, bir Mining pool'ye bağlanmamız gerekecek. Aslında, cihazımız Bitcoin ağının farkında olmayan bir Hash yapıcıdan başka bir şey değildir. Onu bir havuza bağlamak Bitcoin ağına erişimini sağlar ve üzerinde çalışmak için blok şablonları almasına olanak tanır.



### Bir Mining pool'e bağlanmak için uygulamayı kullanma



Avalon Family uygulamasında, aşağıda gösterildiği gibi cihazı seçin. Daha sonra otomatik olarak makinenin yönetici şifresini değiştirmeniz istenecektir. Bunu yapmak istiyorsanız "Tamam" üzerine tıklayın veya varsayılan erişim şifresi "admin" olarak bırakmak için iptal üzerine tıklayın.


![image](assets/fr/16.webp)


Ardından "Ayarlar" ve ardından "Havuz Yapılandırması "nı seçin ve istenen 3 havuz için parametreleri girin.


2. ve 3. havuzlar, bunlardan birinin arızalanması durumunda yedekleme görevi görecektir, böylece Miner'ünüz boşuna çalışmaz. Varsayılan olarak, Hashrate 1 numaralı havuza yönlendirilecektir



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





- gW-27 Address* cihazınız ve cihazınız için seçtiğiniz *sözde* cihazdan oluşan "çalışanın" adı, 2'si bir *nokta* ile ayrılır, örneğin:**bc1qxxxxxxxxxxxxx.MonAvalonNano3S**





- genellikle her zaman "**x**" olan parola



Havuz bilgileri girildikten sonra "Kaydet" düğmesine tıklayın.



![image](assets/fr/18.webp)


Cihazı talimatlara uygun şekilde yeniden başlatın ve Hashrate'iniz tercih ettiğiniz havuza (#1) yönlendirilene kadar birkaç dakika bekleyin.



### Bir Mining pool'a bağlanmak için tarayıcıyı kullanma



Ayrıca bir Mining pool'a bağlanabilir ve daha genel olarak cihazınızın Interface yönetim sistemine favori tarayıcınız üzerinden erişebilirsiniz.



Bunu yapmak için, tarayıcının arama çubuğuna aşağıdaki ekranda gösterilen cihazın IP Address'sini yazın, örneğimizde **192.168.144.6**



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



Şimdi evimizdeki Miner'ü yerel ağımıza bağladık ve Hashrate'ümüzü Minings havuzlarına yönlendirdik. Şimdi Avalon Family uygulaması aracılığıyla makinemizin temel özelliklerini keşfedelim.



Avalon ailesi uygulamasının ana menüsünde, Avalon Mini 3'e karşılık gelen simgeye tıklayın. Doğrudan çalışma modlarını yönetmek için menüye yönlendirileceksiniz.



3 seçenek mevcuttur: "Isıtıcı" modu, "Mining" modu veya "Gece" modu.





- "Isıtıcı" modunda "Eko" veya "Süper" olmak üzere 2 güç seviyesine sahipsiniz.


"Eco" seviyesi, yaklaşık 25 Th/s'lik bir Hashrate için 500W'lık bir ısıtma gücüne ve ses seviyesi için 40 dB'ye karşılık gelir.


"Süper" seviye yaklaşık 30Th/s ve 45 dB'de 650 W çıkış gücüne karşılık gelir. Bu mod, ünitenin çalışmayı durduracağı maksimum ortam sıcaklığını ayarlamanıza olanak tanır.



![image](assets/fr/36.webp)




- "Mining" modunda, ünite bir hedef sıcaklık belirleme seçeneği olmadan maksimum hızda çalışır (elbette dahili aşırı ısınma limiti dışında). Amaç, Miner'in performansından en iyi şekilde yararlanmaktır. Burada, çıkış gücü yaklaşık 37,5 Th/s ve 50-55 dB gürültü seviyesinde 800 W'a yaklaşır.



![image](assets/fr/37.webp)


Son olarak, "Gece" modunda Mini 3'ünüz minimum gürültü ile mümkün olan en düşük hızda çalışır. 400 W, 20 Th/s ve yaklaşık 33 dB.



Burada da ünitenin inaktif moda geçeceği ve Miner'u durduracağı bir hedef sıcaklık ayarlayabilirsiniz. Sıcaklık düşerse, ünite yeniden başlatılır ve ısıtmaya ve Miner'a devam eder. Bu modda, ekran LED'leri varsayılan olarak kapalıdır, ancak odayı karanlıkta bir gece lambası gibi aydınlatmak için gerekirse bunları açmayı seçebilirsiniz (aşağıdaki fotoğrafa bakın).



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



Son olarak, "Ekran" menüsü aracılığıyla Avalon'unuzun LED'leri ile oynayabilirsiniz. İlgili işletim bilgileri arasında gezinebilir, saati veya hatta özel (pikselli) bir görüntüyü göstermeyi seçebilirsiniz.



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



Avalon Nano 3S'de olduğu gibi, "Ayarlar" menüsü yönetici şifresini, havuz ayarlarını değiştirmenize, filtre tıkanıklığını kontrol etmenize (cihazın alt tarafında bulunur), destekle iletişime geçmenize veya cihaz günlüklerini görüntülemenize olanak tanır.



![image](assets/fr/42.webp)



Bir kez daha, ünitenin altındaki filtre elektrikli süpürge ile temizlenebilir, ne kadar düzenli olursa o kadar iyidir.



Avalon Mini 3'ümüzü yerel ağımıza nasıl bağlayacağımızı, Hashrate'ımızı Mining havuzlarına nasıl yönlendireceğimizi ve Avalon Family uygulamasını kullanarak seçenekler ve ayarlar arasında nasıl gezineceğimizi öğreten bu eğitimin sonuna geldik.



Daha fazla bilgi edinmek için Avalon'un daha küçük versiyonu olan Nano 3S hakkındaki eğitimimize göz atın.



https://planb.network/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6