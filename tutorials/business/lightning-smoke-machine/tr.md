---
name: Lightning Smoke Machine
description: ESP32 üzerinden Lightning ödemesi ile bir duman makinesini tetikleyin.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Giriş



Klasik bir duman makinesini Lightning Network aracılığıyla Bitcoin'de ödenebilen bir cihaza dönüştürür. Her ödeme otomatik olarak bir duman püskürmesini tetikler!





- Seviye: Orta seviye
- Tahmini süre: 2-3 saat
- Kullanım alanları: Bitcoin etkinlikleri, sanatsal performanslar, Lightning demoları, otomatik sahne efektleri



## Ön Koşullar



### Bilgi





 - Temel elektronik (kablolama, röleler)
 - Kaynak (veya Dupont konektörlerinin kullanımı)
 - Ağ yapılandırması (WiFi, WebSocket)



### Gerekli hesaplar





- BTCPay Sunucusu: İşlevsel örnek (kendi kendine barındırılan veya barındırılan)
- Blink Wallet : Hesap + erişim API



### Erişim





- BTCPay Sunucusuna yönetici erişimi
- ESP32 için WiFi bağlantısı



## Gerekli malzemeler



### Donanım - Elektronik bileşenler





- 1 Mikrodenetleyici - ESP32-WROOM-32


*ESP32-WROOM-32, elektronik cihazları internete bağlamak ve uzaktan kontrol etmek için kompakt, düşük maliyetli bir WiFi/Bluetooth mikrodenetleyicidir*



![ESP32](assets/fr/1.webp)





- 1 Röle modülü - optokuplörlü 5V


*Röle, ESP32'nin duman makinesini açmak veya kapatmak için çalıştırabileceği bir anahtar gibidir*



![relay](assets/fr/2.webp)





- ~10 Dupont kablo - Erkek/Erkek ve Erkek/Dişi



![dupont-cables](assets/fr/3.webp)





- 1 ESP32 için güç kaynağı - 5V USB veya Li-Po pil



![battery](assets/fr/4.webp)





- 1 mikro-USB kablosu - ESP32 ve güç kaynağı arasındaki bağlantı



![micro-usb-cables](assets/fr/5.webp)





- 1 adet 12V pilli uzaktan kumandalı 220V sis makinesi



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 şişe duman makinenizle uyumlu sıvı



### Donanım - Araçlar





- Havya + kalay (lehimleme yapılacaksa)
- Tornavida
- Multimetre (önerilir)



### Yazılım





- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- WebSerial uyumlu web tarayıcısı (Chrome/Edge/Brave)
- BTCPay Sunucusu yapılandırıldı. BTCPay Sunucu örneği oluşturma hakkında daha fazla bilgi için bu öğreticiyi ziyaret edin: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Sistem mimarisi



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **GÜVENLİK UYARISI - DEVAM ETMEDEN ÖNCE OKUYUN** **⚠️**



Bu proje **220V şebeke kaynağına** bağlı bir sis makinesi içermektedir. Yanlış kullanım **ölümcül elektrik çarpması** veya **yangın** ile sonuçlanabilir.



**Müzakere edilemez kurallar:**



1. **Uzaktan kumandayı açmadan veya kablo tesisatını kurcalamadan önce DAİMA duman makinesinin elektrik bağlantısını kesin**


2. **Kullanmadan önce pili uzaktan kumandadan çıkarın** (kısa devre ve bileşenlerde hasar riski)


3. **Herhangi bir şeyi yeniden bağlamadan önce tüm bağlantılarınızın izole edildiğini** kontrol edin


4. **Uzaktan kumanda kutusu kapatılmadan ve emniyete alınmadan 220V** bağlantısını asla tekrar yapmayın



Bu tür bir kullanım konusunda rahat değilseniz, yanınıza rahat olan birini alın.



---

## BÖLÜM 1: Donanım montajı



### Adım 1: Uzaktan kumandayı hazırlama



Amaç: Röleyi uzaktan kumanda üzerindeki AÇMA/KAPAMA düğmesine bağlayın


1. Uzaktan kumandayı açın




    - AÇMA/KAPAMA düğmesini tanımlama
    - Uzaktan kumandayı açmak için kılıfı sökün


2. Bağlantıları bulun




 - Cihazın + ve - terminallerini bulun
 - Bir multimetre ile sürekliliği test edin (isteğe bağlı)



![smoke-machine-remote](assets/fr/8.webp)



3. Düğme kabloları (lehim veya konektörler)




    - Düğmenin - terminaline siyah bir kablo lehimleyin
    - Ortak + terminaline kırmızı bir kablo lehimleyin



![smoke-machine-remote](assets/fr/9.webp)



### Adım 2: Röle modülüne bağlanma



**Hatırlatma: Röle terminolojisi



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**Uzaktan kumandadan röle modülüne kablolama:**




- AÇMA/KAPAMA düğmesinden gelen siyah kablo **→** NO (Normalde Açık)
- Kırmızı kablo (ortak) **→** COM (Ortak)



**Mantık:**


ESP32 röleyi etkinleştirdiğinde, COM ve NO'yu birbirine bağlar, bu da uzaktan kumanda düğmesine basmakla tamamen aynıdır.


ESP32 röleyi kestiğinde, COM ve NO ayrılır, bu da düğmeyi bırakmaya eşdeğerdir.



![remote-relay](assets/fr/10.webp)



### Adım 3: ESP32'nin röle modülüne bağlanması



**Kablo şeması:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**Doğrulama:**




- VCC ve GND iyi bağlanmış (polarite)
- Kontrol sinyali için kullanılan GPIO 21
- Görünür kısa devre yok



![relay-esp32](assets/fr/11.webp)



**Kontrol Noktası Donanımı**


Yazılıma geçmeden önce kontrol edin:




- Doğru kablolanmış uzaktan kumanda
- ESP32'ye bağlı röle modülü
- Diğer bileşenlere temas eden çıplak kablo yok
- 220V her zaman bağlantısı kesilmiş



![relay-esp32](assets/fr/12.webp)





---


## BÖLÜM 2: Yazılım yapılandırması



Örnek olarak *Blink* kullanacağız, ancak *BTCPay Server* başka bir seçeneği tercih ederseniz *Strike, Breez ve Boltz* de sunar.



### Adım 1: Eklentiler, Kurulum *BitcoinSwitch* + *Blink



1 - Bir yönetici hesabı ile *BTCPay Sunucu* örneğinize gidin



2 - İlk körünüzü oluşturun



3 - *BTCPay Server'ın* sol tarafında, aşağıya doğru kaydırın ve *"Eklentileri Yönet "e gidin



![btcpay-plugins](assets/fr/13.webp)



4 - *BitcoinSwitch* eklentilerinin yanı sıra *Blink* eklentilerini de yükleyeceğiz



![btcpay-plugins](assets/fr/14.webp)



5 - Eklentiler listesini aşağı kaydırın ve *"Yükle "* seçeneğine tıklayın: *BitcoinSwitch ve Blink* (veya seçtiğiniz mevcut wallet)



![btcpay-plugins](assets/fr/15.webp)



6 - Kurulum tamamlandıktan sonra *BTCPay Sunucusunu* yeniden başlatın ve örneğin yeniden başlaması için 1 dakika bekleyin



![btcpay-plugins](assets/fr/16.webp)



7 - *"Eklentileri yönet "e* döndüğünüzde, her iki eklentinin de yüklendiğini kontrol edin



![btcpay-plugins](assets/fr/17.webp)



### Adım 2: Arka Uç: *BTCPay Sunucusu + Blink* yapılandırması



**1 - Bir wallet oluşturun *Blink***




- Https://www.blink.sv adresini ziyaret edin
- Hesabınızı oluşturun. Lütfen öğreticiye bakın :



[https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd](https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Bir API anahtarı oluşturun *Blink***




- API arayüzüne erişin: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** ve wallet'nizi oluştururken kullandığınız hesapla oturum açın *Blink*



![blink-api](assets/fr/18.webp)





   - Bağlandıktan sonra *API Tuşları* sekmesine gidin



![blink-api](assets/fr/19.webp)





   - Üzerine tıklayın *" gW-24 Anahtar yapılandırmanıza erişmek için sağ üst köşedeki + "*



![blink-api](assets/fr/20.webp)





   - API Anahtarınıza bir isim verin ve varsayılan ayarları bırakın. Ardından, üçüncü adımda API Anahtarınızı not edin - yalnızca bir kez göreceksiniz: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Oluşturulduktan sonra, etkin API Anahtarı listenizde görünmelidir.



![blink-api](assets/fr/22.webp)



**3 - *Blink*'yi *BTCPay Sunucusuna*** bağlayın




- BTCPay Sunucunuzu* açın
- Şuraya git : *Wallet* **→** *Yıldırım*



![btcpay-server](assets/fr/23.webp)





- Özel bir düğüm kullan* seçeneğine tıklayın
- Aşağıdaki bağlantı dizesini yapıştırın:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Önemli** :




- İlk kısmı değiştirmeyin: `type=blink;server=https://api.blink.sv/graphql`;
- Sadece değiştirin :
    - api-key= *API Blink* anahtarınız ile
    - wallet-id= *wallet Blink* kimliğinize göre
- Ardından *Bağlantıyı test et* ve ardından *Kaydet* seçeneğine tıklayın



![btcpay-server](assets/fr/24.webp)





 - Bağlantının kurulduğunu kontrol edin (yeşil durum)



![btcpay-server](assets/fr/25.webp)



**4 - Bir Satış Noktası (PoS)** Oluşturun




- BTCPay Server'da *Eklentiler* sekmesine gidin ve *Satış noktası* seçeneğine tıklayın



![btcpay-server](assets/fr/26.webp)





- PoS'unuza bir isim verin ve *Oluştur* seçeneğine tıklayın



![btcpay-server](assets/fr/27.webp)





- PoS yapılandırması :
    - Bir satış noktası stili seçin = *Basılı ekran*
    - Para Birimi = *SATS*
    - KAYDET* üzerine tıklayın



![btcpay-server](assets/fr/28.webp)





- Ürün konfigürasyonu :
    - Tüm varsayılan ürünleri sil
    - Ardından *öğe ekle* seçeneğine tıklayın



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Ürünü yapılandırın:
    - Başlık : *duman maki̇nesi̇*
    - Fiyat : *10 sats*
    - Bitcoin GPIO anahtarı : 21
    - Bitcoin anahtar süresi (milisaniye cinsinden) : 5000
    - Yeni ürünü kaydetmek için *Kapat* ve ardından *Kaydet* üzerine tıklayın



![btcpay-server](assets/fr/31.webp)



### Adım 3: Firmware: ESP32'yi Yanıp Söndürme



**1 - Flash sitesine git




- Gitmek : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash BitcoinSwitch ürün yazılımı**




- ESP32'yi USB/Mikro-USB kablosu ile bilgisayarınıza bağlayın
- Ardından *Cihaza Bağlan* seçeneğine tıklayın
- Bir pencere açılır, ESP32'nizdeki USB bağlantı noktasını seçin, ardından *Bağlan* seçeneğine tıklayın



![bitcoinswitch-lnbits](assets/fr/33.webp)





- ESP32'niz bağlandıktan sonra, BitcoinSwitch aygıt yazılımını yükleyeceğiz. T-Display* bölümünde, mevcut en son sürüm için *Upload Firmware* seçeneğine tıklayın (şu anda: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Yükleme için bekleyin, günlükler *"Ayrılıyor..." gösterdiğinde işlem tamamlanmıştır. "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- ESP32'nin fişini çekin



**3 - BitcoinSwitch ürün yazılımı kurulumunu kontrol edin




- Sayfayı yeniden yükle: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- ESP32'yi USB/Mikro-USB kablosu ile bilgisayarınıza yeniden bağlayın
- Ardından *Cihaza bağlan'a tıklayın
- ESP32'nizdeki USB bağlantı noktasını seçin, ardından yukarıda açıklandığı gibi *Bağlan* seçeneğine tıklayın
- Bağlandıktan sonra ESP32 üzerindeki **RESET** düğmesine basın
- Günlüklerde son satırların gösterilip gösterilmediğini kontrol edin:



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Bu normaldir, henüz yapılandırma olmadığı, ancak aygıt yazılımının yüklendiği anlamına gelir)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - WebSocket LNURL** URL'si oluşturun



Beklenen nihai format :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Üretim adımları :




- BTCPay Sunucu örneğinizi açın, ardından daha sonra oluşturduğumuz PoS'a gidin.
- Ardından PoS'unuzu tarayıcıda açmak için "Görüntüle "ye tıklayın



![btcpay-server-https](assets/fr/37.webp)





- Sayfanın URL'sini kopyalayın, örneğin :



![btcpay-server-https](assets/fr/38.webp)



Bu URL'yi açalım:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → BTCPay Sunucu örneğinizin etki alanı
- `46XXXXXXXXXXXXXXXXXXwFB` → PoS benzersiz tanımlayıcınız
- `/pos` → bir Satış Noktasını gösterir



Dönüştürün:




- Https://` yerine `wss://` yazın
- Sonuna `/bitcoinswitch` ekleyin



Sonuç:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



ESP32'nizin BTCPay Sunucusu ile gerçek zamanlı olarak iletişim kurmasını sağlayacağından, bu URL'yi gelecekteki yapılandırma için saklayın. WebSocket protokolü (`wss://`) ikisi arasında kalıcı bir bağlantı kurar: PoS'unuzda bir Lightning ödemesi onaylanır onaylanmaz, BTCPay bilgileri anında ESP32'ye gönderir ve bu da duman makinenizi tetikleyebilir.



**5 - WiFi ve WebSocket'in Yapılandırılması




- Sayfaya geri dönün: eSP32'niz bağlıyken [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Cihazı Yapılandır* → *Wifi Ayarları* bölümüne gidin



Bilgilendir:




- WiFi SSID: WiFi ağınızın adı
- WiFi Şifresi: WiFi şifreniz



![bitcoinswitch-lnbits](assets/fr/39.webp)





- LNbits Cihaz URL'si* bölümüne, önceki adımda oluşturulan WebSocket URL'sini yapıştırın
- Yapılandırmayı yükle* seçeneğine tıklayın



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Yüklemenin tamamlanmasını bekleyin; günlükler az önce girdiğiniz parametreleri (SSID, şifre ve WebSocket URL'si) göstermelidir



![bitcoinswitch-lnbits](assets/fr/41.webp)





- ESP32 WebSocket bağlantısını kurarken bekleyin. Görmelisiniz :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Artık ESP32'nin bağlantısını kesebilirsiniz



---
## Checkpoint Yazılım



Son testten önce kontrol edin :





- Blink BTCPay'e bağlandı
- En az 1 öğe ile oluşturulmuş PoS
- ESP32 BitcoinSwitch ile flaşlandı
- ESP32 üzerinde yapılandırılmış WiFi
- WebSocket URL'si doğru
- Hatasız ESP32 günlükleri



---

## Test etme ve hata ayıklama



### Son testi tamamlayın



1. Duman makinesini fişe takın (220V) ve çalıştırın


2. ESP32'ye güç verin (pil veya USB)


3. Tarayıcınızda BTCPay PoS'unuzu açın


4. "Duman makinesi" öğesini tara


5. wallet Lightning ile ödeme yapın (Blink veya diğer wallet)


6. Gözlemleyin:




 - Röle tıklamaları (duyulabilir ses ve röle LED'i yanar)
 - Duman makinesi etkinleştirildi
 - Duman çıktı!



### Adalet sorunları ve çözümleri



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## Kaynaklar



### Faydalı bağlantılar





- BitcoinSwitch Ürün Yazılımı: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay Sunucu Belgeleri : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 Pin Çıkışı : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Topluluk ve Destek





- BTCPay Sunucusu** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Resmi Mattermost
- BTCPay Sunucusu Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Resmi Telegram, aktif topluluk
- BitcoinSwitch (ürün yazılımı hataları)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Kaynak kodu





- BitcoinSwitch ürün yazılımı kaynak kodu: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** sats'yı istifleyin, duman yapın, eğlenin, alçakgönüllü kalın! **⚡**