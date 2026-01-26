---
name: Heritage
description: Taproot komut dosyaları aracılığıyla entegre miras mekanizmasına sahip bir Bitcoin portföyü
---

![cover](assets/cover.webp)



Ölüm veya iş göremezlik durumunda bitcoinleri devretmek, herhangi bir kripto varlık sahibi için büyük bir zorluk teşkil eder. Uygun bir miras planı olmadan, bu varlıklar sevdikleriniz için kurtarılamaz hale gelir.



Heritage, doğrudan Bitcoin blok zinciri üzerinde bir ölü adam anahtarı mekanizması uygulayarak zarif bir yanıt sunmaktadır. Bu açık kaynaklı wallet, on-chain ardıllık koşullarının yapılandırılmasını sağlar: mal sahibi belirli bir süre boyunca başka işlem yapmazsa, önceden belirlenmiş alternatif anahtarlar fonları serbest bırakabilir.



## Miras nedir?



Heritage, Taproot komut dosyaları aracılığıyla bir miras mekanizmasını yerel olarak entegre eden bir Bitcoin portföyüdür. Jérémie Rodon tarafından MIT lisansı altında geliştirilen bu açık kaynaklı yazılım şeffaflık ve dayanıklılığı garanti eder.



Heritage, Bitcoin adreslerinde kodlanmış Taproot komut dosyalarını kullanır. Her bir UTXO iki tür harcama koşulunu entegre eder:





- Birincil yol** : Sahibi bitcoinlerini istediği zaman birincil anahtarı ile harcayabilir
- Alternatif yollar**: Belirlenen her varis için, bir komut dosyası açık anahtarını bir zaman kilidi ile birleştirir



Her malik işlemi, miras hükümlerinin etkinleşme tarihini otomatik olarak erteler. Uzun süreli hareketsizlik durumunda (ölüm, iş göremezlik), koşullar otomatik olarak tetiklenir.



## Miras hizmeti (isteğe bağlı)



Heritage iki kullanım seçeneği sunmaktadır:



**Kendiniz yapın (ücretsiz)**: Yalnızca açık kaynaklı uygulama. Her şeyi kendi düğümünüzle özerk olarak yönetirsiniz. Bu seçenek yerleşik yedekleme erişimi, yerleşik miras ve bitcoinlerinizin özel kontrolünü sunar. Ancak, zaman kilitlerinizi yenilemeyi unutmamak için kendi uyarılarınızı (takvim, hatırlatıcılar) oluşturmanız gerekir ve mirasçılarınız için otomatik bildirimler yoktur.



**Hizmeti kullanın (yıllık %0,05)** : Btc-heritage.com hizmeti, yönetimi basitleştirmek için özellikler ekler:




- Süreniz dolmadan önce otomatik hatırlatmalar
- Mirasçılara kurtarma süreci boyunca yol gösterecek otomatik bildirimler
- Öncelikli destek
- Basitleştirilmiş tanımlayıcı yönetimi



Ücret: Yıllık yönetilen miktarın %0,05'i, minimum 0,5 mBTC/yıl. İlk yıl ücretsiz.



Hizmet gözetim altında değildir: özel anahtarlarınız cihazınızdan asla çıkmaz. Heritage fonlarınıza erişemez.



## Miras CLI



Terminali tercih eden ileri düzey kullanıcılar için Heritage, granüler kontrol ve hava boşluklu makine çalışması için bir komut satırı aracı (CLI) sunar.



![Page Heritage CLI](assets/fr/03.webp)



CLI belgelerinin tamamına [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli) adresinden ulaşabilirsiniz. Burada indirme, hizmete bağlanma, cüzdan oluşturma (Ledger veya yerel anahtarlarla), varisleri ve işlemleri yönetme talimatlarını bulacaksınız.



Bu eğitim, çoğu kullanıcı için daha erişilebilir olan Masaüstü uygulamasına odaklanmaktadır.



## Miras Masaüstü



Heritage Desktop, kullanıcıyı yapılandırma sürecinin her adımında yönlendiren sezgisel bir arayüze sahip grafiksel bir uygulamadır.



### İndir



Btc-heritage.com] (https://btc-heritage.com) adresine gidin ve "Uygulamayı indir" seçeneğine tıklayın.



![Page d'accueil Heritage](assets/fr/01.webp)



İşletim sisteminize karşılık gelen sürümü seçin (Linux 64bits veya Windows 64bits). İkili dosyalar dijital olarak imzalanmamıştır, bu da güvenlik uyarılarını tetikleyebilir.



![Page de téléchargement](assets/fr/02.webp)



### Linux üzerinde kurulum



Linux üzerinde, uygulama AppImage formatında dağıtılır. Çalıştırmadan önce `libfuse2` bağımlılığını yüklemeniz gerekir:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Ardından dosyayı çalıştırılabilir hale getirin ve çalıştırın:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### İlk fırlatma



İlk açılışta, işe alım sihirbazı size üç seçenek sunar:



![Onboarding initial](assets/fr/05.webp)





- Bir Miras Wallet** kurun: Miras planı ile yeni bir wallet oluşturun
- Bitcoinleri miras alın**: Varis olarak bitcoinleri kurtarın
- Kendi başıma keşfedin**: Yardım almadan fonksiyonları keşfedin



İlk wallet'nizi oluşturmak için "Bir Miras Wallet Kur" seçeneğini seçin.



### Bitcoin ağ bağlantısı



Bitcoin ağına nasıl bağlanılacağını seçin:



![Choix connexion](assets/fr/06.webp)





- Miras Hizmetini** kullanma: Yönetilen altyapı, varisler için daha basit
- Kendi düğümümü kullanıyorum**: Kendi Bitcoin Core veya Electrum düğümünüze bağlanın



Bu eğitim için kendi node'umuzu kullanacağız.



### Özel anahtar yönetimi



Özel anahtarlarınızı nasıl yöneteceğinizi seçin:



![Gestion des clés](assets/fr/07.webp)





- Bir Ledger Donanım Cihazı ile** : wallet donanımı ile maksimum güvenlik (önerilir)
- Şifre ile yerel depolama**: Parola korumalı yerel olarak depolanan anahtarlar
- Mevcut bir wallet'ü geri yükleyin** : Mevcut bir seed'ten geri yükleme



### Düğüm yapılandırması



Kendi düğümünüzü kullanıyorsanız, uygulama yapılandırma sırasında size rehberlik eder. Bitcoin veya Electrum düğümünüzün olduğundan emin olun:




- Kuruldu ve çalışıyor
- Bitcoin ağı ile senkronize
- RPC bağlantılarını kabul edecek şekilde yapılandırıldı (Bitcoin Çekirdek için)



![Configuration nœud](assets/fr/08.webp)



Düğümünüz hazır olduğunda "My Bitcoin node is up and running" (Bitcoin düğümüm hazır ve çalışıyor) üzerine tıklayın.



### Durum paneli



Bağlantı parametrelerine erişmek için sağ üst köşedeki "Durum "a ve ardından "Yapılandırmayı Aç "a tıklayın.



![Panneau Status](assets/fr/09.webp)



Electrum sunucunuzun URL'sini ayarlayın (örneğin, Umbrel kullanıyorsanız `umbrel.local:50001`).



![Configuration Electrum](assets/fr/10.webp)



### wallet'ün Oluşturulması



Bağlantı kurulduktan sonra, CÜZDANLAR sekmesindeki "Wallet Oluştur" seçeneğine tıklayın.



![Créer wallet](assets/fr/11.webp)



Bir açılır pencere Heritage'ın bölünmüş mimarisini açıklar:



![Architecture split](assets/fr/12.webp)



1. **Anahtar Sağlayıcı (Çevrimdışı)**: Özel anahtarlarınızı yönetir ve işlemleri imzalar. Bir Ledger veya bir wallet yazılımı olabilir.


2. **Çevrimiçi Wallet**: Bitcoin ağı ile senkronizasyonu, adres oluşturmayı ve işlem yayınını yönetir.



Oluşturma formunu doldurun :



![Formulaire création wallet](assets/fr/13.webp)





- Wallet Adı**: wallet'inizi tanımlamak için benzersiz bir ad
- Anahtar Sağlayıcı**: Bu eğitim için Yerel Anahtar Depolamayı seçin
- Yeni/Restore**: generate'yi yeni bir seed yapmak için "Yeni "yi seçin
- Kelime Sayısı**: maksimum güvenlik için 24 kelime önerilir



Güçlü bir parola girin ve Çevrimiçi Wallet için seçenekleri belirleyin:



![Options Online Wallet](assets/fr/14.webp)





- Yerel Düğüm**: Kendi Electrum veya Bitcoin Çekirdek düğümünüzü kullanır
- Miras Hizmeti**: Heritage hizmetini kullanır (bildirim işlevleri için önerilir)



Oluşturma işlemini tamamlamak için "Wallet Oluştur" düğmesine tıklayın.



### Interface'den wallet'a



wallet'niz şimdi oluşturulmuştur. Arayüz görüntülenir :



![Interface wallet](assets/fr/15.webp)





- Denge
- GÖNDER ve AL düğmeleri
- İşlem geçmişi
- Miras yapılandırma geçmişi
- wallet adresleri



### Mirasçıların oluşturulması



Varislerinizi oluşturmak için "VARİSLER" sekmesine gidin.



![Page Heirs](assets/fr/16.webp)



Bilgi açılır penceresi açıklar:




- Varisler, bireylerle ilişkili Bitcoin açık anahtarlarıdır
- Her varisin kendi anımsatıcı cümlesi vardır
- İlk varis kendiniz için bir "Yedek" olmalıdır (ana wallet'ünüzün kaybolması durumunda)



#### Yedekleme varisi oluşturma



"Varis Oluştur "a tıklayın ve "Yedekleme" adını verin.



![Création héritier Backup](assets/fr/17.webp)



Açılır pencere, passphrase içermeyen 12 kelimelik bir cümlenin mirasçılar için neden güvenli olduğunu açıklar:


1. **Anında erişim yok**: Varis anahtarları zaman kilidi sona erene kadar fonlara erişemez


2. **Uzlaşma tespiti**: Birisi ifadeye erişirse, Miras yapılandırmasını güncelleyebilirsiniz


3. **Uzun vadeli erişilebilirlik**: Bir passphrase yıllar sonra unutulabilir



Varisi yapılandırın :



![Configuration héritier](assets/fr/18.webp)





- Anahtar Sağlayıcı** : Yerel Anahtar Depolama
- Yeni**: Yeni bir seed oluşturun
- Kelime Sayısı**: 12 kelime



Oluşturma işlemini tamamlayın:



![Finalisation héritier](assets/fr/19.webp)





- Varis Türü**: Genişletilmiş Açık Anahtar
- Hizmete Aktar**: İsteğe bağlı, mirasçılara otomatik bildirim yapılmasını sağlar



Yedekleme varisi şimdi oluşturulmuştur:



![Héritier créé](assets/fr/20.webp)



#### Mirasçının anımsatıcı ifadesini kaydetme



Yedekleme varisine ve ardından "Mnemonic'yi Göster" seçeneğine tıklayın:



![Afficher mnemonic](assets/fr/21.webp)



**ÖNEMLİ: Bu 12 kelimeyi not edin ve güvenli bir yerde saklayın. Bu, fonları geri kazanmanın anahtarıdır.



![Phrase mnémotechnique](assets/fr/22.webp)



#### seed'in uygulamadan kaldırılması



İfadeyi yazdıktan sonra, varis parametrelerine erişin (dişli çark simgesi):



![Paramètres héritier](assets/fr/23.webp)



Özel anahtarı uygulamadan kaldırmak için "Strip Heir Seed" seçeneğini kullanın. İfadeyi kaydettiğinizi onaylayın.



![Strip Heir Seed](assets/fr/24.webp)



Bu bir güvenlik önlemidir: uygulamada yalnızca ortak anahtar kalır ve kalıtımı yapılandırmak için yeterlidir.



#### İkinci bir varisin yaratılması



İkinci bir varis oluşturmak için işlemi tekrarlayın (örneğin "Satoshi"). Artık iki mirasçınız olacak:



![Deux héritiers](assets/fr/25.webp)





- Yedekleme**: Kişisel acil durum anahtarınız
- Satoshi**: Atanmış bir varis



### Miras yapılandırması



wallet'inize dönün ve Ayarlar simgesine tıklayın:



![Paramètres wallet](assets/fr/26.webp)



"Miras Yapılandırması" bölümünde "Oluştur "a tıklayın:



![Heritage Configuration](assets/fr/27.webp)



Her varis için zaman sınırları belirleyin:



![Configuration délais](assets/fr/28.webp)





- Yedek**: 180 gün (6 ay) - Vade Tarihi: 2026-06-18
- Satoshi**: 455 gün (15 ay) - Vade Tarihi: 2027-03-20



**Önemli**: Her varis bir öncekinden daha uzun bir gecikmeye sahip olmalıdır. İlk varis (Yedekleme) fonlara ilk olarak erişebilecektir.



Ayrıca yapılandır :



![Configuration finale](assets/fr/29.webp)





- Referans Tarihi**: Teslim sürelerinin hesaplanması için başlangıç tarihi
- Minimum Vade Gecikmesi**: Bir işlemden sonra minimum gecikme (10 gün önerilir)



Yapılandırmayı doğrulamak için "Oluştur" üzerine tıklayın.



Miras yapılandırması artık etkindir:



![Configuration active](assets/fr/30.webp)



Her iki varisi de kendi son tarihleri ve son kullanma tarihleriyle birlikte görüntüler.



### Tanımlayıcıları kaydetme



**Önemli**: wallet tanımlayıcılarınızı saklayın. Bunlar olmadan, anımsatıcı ifadeyle bile, fon geri kazanımı imkansızdır.



"Yedekleme Tanımlayıcıları" üzerine tıklayın:



![Bouton Backup](assets/fr/31.webp)



Bitcoin tanımlayıcılarınızı içeren JSON dosyasını kaydedin:



![Backup descripteurs](assets/fr/32.webp)



Bu dosya, ilgili anımsatıcı ifadelerle birlikte varislerinize aktarılmalıdır.



### Bitcoin alma



Bir alım adresini generate yapmak için "RECEIVE" (AL) üzerine tıklayın:



![Recevoir bitcoins](assets/fr/33.webp)



Tebrikler! Heritage Wallet'nız bitcoin almaya hazır. Oluşturulan her adres otomatik olarak Heritage koşullarınızı içerir.



Bir işlem aldıktan sonra bakiyeniz güncellenir:



![Solde mis à jour](assets/fr/34.webp)



Geçmiş, işlemi ve ilişkili Miras yapılandırmasını görüntüler.



---

## Bir varis tarafından kurtarma



Belirlenen süre geçtikten sonra mirasçı fonları geri alabilir.



### Ön Koşullar



Varisin ihtiyacı var:


1. 12 kelimelik anımsatıcı cümlesi


2. Orijinal wallet tanımlayıcı yedek dosyası (JSON)



### Varis Oluşturma Wallet



"MİRASLAR" sekmesinde, bir açılır pencere size bu önkoşulları hatırlatır:



![Page Heir Wallets](assets/fr/35.webp)



**Lütfen dikkat**: Tanımlayıcı yedekleme dosyası olmadan, doğru anımsatıcı ifadeyle bile fonlara erişim İMKANSIZDIR.



"Varis Wallet Oluştur" üzerine tıklayın:



![Créer Heir Wallet](assets/fr/36.webp)



Lütfen formu doldurunuz:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Varis Wallet Adı**: Bu varisi tanımlamak için bir isim wallet
- Anahtar Sağlayıcı** : Yerel Anahtar Depolama
- Geri yükle**: Mevcut bir ifadeyi girmek için bu seçeneği seçin



Mirasçının anımsatıcı cümlesinin 12 kelimesini girin ve Miras Sağlayıcısını yapılandırın:



![Entrée mnemonic](assets/fr/38.webp)





- Miras Sağlayıcı**: yedekleme dosyası ile kendi düğümünüzü kullanmak için "Yerel"



JSON yedek dosyasını yükleyin ve "Varis Wallet Oluştur" seçeneğine tıklayın:



![Chargement backup](assets/fr/39.webp)



### Interface Varis Wallet



Varis Wallet oluşturulur. Başlangıçta, zaman kilidinin süresi henüz dolmamışsa, miras alınamaz:



![Pas d'héritage disponible](assets/fr/40.webp)



Gecikme sona erdiğinde ve fonlar Bitcoin ağı ile senkronize edildiğinde, miras listesinde görünürler:



![Héritage disponible](assets/fr/41.webp)



Arayüz görüntülenir :




- Anahtar tipi ve parmak izi
- Toplam miras bırakılabilir fonlar
- Mevcut harcanabilir miktar (zaman kilidi henüz sona ermemişse 0 sat)
- Vade ve son kullanma tarihleri



Vade tarihine ulaşıldığında, "Harca" düğmesi bitcoinleri kişisel bir wallet'ye aktarır.



---

## En iyi uygulamalar



### Tanımlayıcıları kaydetme



wallet tanımlayıcıları Miras adreslerinizi yeniden yapılandırmak için gereklidir. **Tanımlayıcılar olmadan, anımsatıcı ifadenizle bile, fonlarınızı bulamazsınız.



### Anahtar güvenliği





- Mümkünse ana anahtar için bir Ledger kullanın
- Mirasçıların cümlelerini asla kendi cümlelerinizle aynı yerde saklamayın
- Bilgiyi birden fazla medya ve konuma yayma



### Sevdikleriniz için dokümantasyon



Kurtarma sürecinin her adımını açıklayan net talimatlar yazın. Mirasçılarınız kritik anda Bitcoin hakkında bilgi sahibi olmayabilir.



## Alternatifler



Bitcoinlerinizin iletimini yönetmek için Liana ve Bitcoin Keeper dahil olmak üzere başka çözümler de mevcuttur. Eğitimlerimizi aşağıda bulabilirsiniz:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Sonuç



Heritage, Masaüstü uygulaması aracılığıyla Bitcoin halefiyetinizi egemen bir şekilde planlamanıza olanak tanır. Uygulama, uygun zaman dilimlerinin dikkatlice değerlendirilmesini ve sırların güvence altına alınmasını gerektirir. Varislerinize devretmeyi unutmayın:




- 12 kelimelik anımsatıcı cümleleri
- Tanımlayıcı yedekleme dosyası
- Kurtarma talimatları



## Kaynaklar





- [Heritage resmi web sitesi](https://btc-heritage.com)
- [Dokümantasyon CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)