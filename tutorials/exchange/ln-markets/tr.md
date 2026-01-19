---
name: LN Markets
description: Lightning Network üzerinde Bitcoin ticaret platformu
---

![cover](assets/cover.webp)



LN Markets, kaldıraçlı Bitcoin türevlerini KYC olmadan, anında ödeme ve minimum saklama ile doğrudan wallet Lightning'inizden alıp satmanıza olanak tanıyan, gerçek anlamda Lightning'e özgü ilk Bitcoin ticaret platformudur. 2020 yılında piyasaya sürülen bu platform, geleneksel borsaların sürtüşmelerini ortadan kaldırıyor: kimlik doğrulama yok, bloke mevduat yok, blok zinciri onaylarını beklemek yok. wallet Lightning'iniz ticaret hesabınız haline gelir.



## LN Markets nedir?



LN Markets **Futures** (100 kata kadar kaldıraçlı sürekli sözleşmeler) ve **Options** (ödenen primle sınırlı riske sahip Alım/Satım) sunmaktadır. Platform, optimum sıfır kayma uygulaması için birden fazla ticaret merkezini birleştiren bir likidite toplama katmanı olarak işlev görür. Fonlarınız, geleneksel bir saklama hesabında olduğu gibi günler veya haftalar boyunca değil, yalnızca aktif pozisyonlarınızın tam süresi boyunca kilitlenir.



### Mevcut ticari ürünler



**Futures (Sürekli Sözleşmeler)**



Sürekli sözleşmeler, vade tarihi olmayan vadeli işlemlerdir ve kaldıraçla Bitcoin fiyat eğilimi üzerine spekülasyon yapmanızı sağlar. LN Markets iki marj yönetimi modu sunar:



**Yalıtılmış mod**: Her pozisyonun kendi özel marjı vardır. Yalnızca bu belirli pozisyona tahsis edilen fonlar risk altındadır. Pozisyon likidasyon fiyatına ulaşırsa, **sadece bu pozisyon likide edilir**, diğer pozisyonlarınız ve kalan bakiyeniz etkilenmez. İşlem başına riski kesin olarak sınırlamak için idealdir.



**Çapraz Mod (Çapraz Marj)** : Teminat tüm açık pozisyonlarınız arasında paylaşılır. Toplam hesap bakiyeniz tüm pozisyonlarınız için teminat görevi görür. Bir pozisyon kötü giderse, sistem likidasyonu önlemek için mevcut bakiyenizin tamamını kullanır. **Risk**: Toplam bakiyeniz biterse, tüm pozisyonlarınız aynı anda tasfiye edilebilir. Yalnızca sermaye verimliliğini en üst düzeye çıkarmak isteyen deneyimli yatırımcılar için önerilir.



**Pozisyon yönetimi** :





- Uzun pozisyon**: BTC/USD'nin yükselişi üzerine bahis oynarsınız. Fiyat yükselirse kazanırsınız; düşerse kaybedersiniz. **Örnek**: Bitcoin 100.000$'da, 10.000 sats ve 10× kaldıraç ile bir Uzun pozisyon açarsınız. Bitcoin 105.000$'a (+%5) yükselirse, pozisyonunuz %50 (%5 × 10), yani ~5.000 sats kar kazanır. Bitcoin 95.000 $'a (-%5) düşerse, %50 kaybedersiniz, yani ~5.000 sats zarar edersiniz.





- Kısa pozisyon**: BTC/USD'nin düşmesi üzerine bahis oynarsınız. Fiyat düşerse kazanırsınız; yükselirse kaybedersiniz. **Örnek**: Bitcoin 100.000$'da, 10.000 sats ve 10× kaldıraç ile kısa pozisyon açarsınız. Eğer Bitcoin 95.000$'a düşerse (-%5), %50 kazanırsınız, yani ~5.000 sats. Bitcoin 105.000$'a (+%5) yükselirse, %50 kaybedersiniz.



Kaldıraç (100 kata kadar) kazanç ve kayıpları orantılı olarak artırır. Bir **fonlama oranı** mekanizması (her 8 saatte bir periyodik ücretlendirme) uzun ve kısa pozisyonları dengeler. Aynı anda 100 adede kadar vadeli işlem pozisyonunu yönetebilirsiniz.



**Seçenekler**



Opsiyon, son kullanma tarihi olan bir **piyango bileti** gibidir. Bitcoin fiyatının yönü üzerine bahis oynamak için bir prim ödersiniz. **En büyük avantajı**: asla ödenen primden daha fazlasını kaybedemezsiniz, likidasyon mümkün değildir.





- Alım Opsiyonu (yükseliş bahsi)**: Bitcoin'in vade bitiminden önce kullanım fiyatının üzerine çıkacağına dair bahse girersiniz. Fiyat yükselirse kazanırsınız, fiyat düşerse kayıp primle sınırlıdır.





- Satım Opsiyonu (düşüş bahsi)**: Bitcoin'nın kullanım fiyatının altına düşeceğine dair bahse girersiniz. Fiyat düşerse kazanırsınız, fiyat yükselirse kaybınız primle sınırlıdır.





- Straddle (volatilite bahsi)**: Aynı anda bir Call VE bir Put satın alırsınız. Bitcoin herhangi bir yönde büyük bir hareket yaparsa kazanırsınız, fiyat sabit kalırsa her iki primi de kaybedersiniz.



Limit: 50 eşzamanlı pozisyon. Likidasyon korkusu olmadan kaldıraçlı ticarete başlamak için idealdir.



**sats ↔ sUSD**: Kendinizi volatiliteden korumak için satoshilerinizi anında sentetik dolara (sUSD) dönüştürün veya Bitcoin maruziyetini yeniden kazanmak için tam tersini yapın.



## Platform erişimi ve hesap oluşturma



### LN Markets'ye git



Lnmarkets.com] (https://lnmarkets.com) adresine gidin ve "Uygulamayı Aç" seçeneğine tıklayın.



![Page d'accueil LN Markets](assets/fr/01.webp)



### Hesabınızı oluşturun



Karşılama ekranı çeşitli bağlantı yöntemleri sunar:



![Méthodes de connexion](assets/fr/02.webp)



**Seçenekler mevcut** :


1. **Lightning wallet** ile kayıt olun (önerilir) : Phoenix, Breez, Zeus veya BlueWallet ile LNURL-auth


2. **E-posta ile kaydolun**: klasik hesap (Lightning deneyimini sınırlar)


3. **Alby** veya **Ledger**: tarayıcı uzantıları



### Lightning üzerinden bağlantı (LNURL-auth)



"wallet Lightning ile Kayıt Ol" üzerine tıklayın. wallet Lightning'iniz ile QR kodunu tarayın:



![QR code LNURL-auth](assets/fr/03.webp)



wallet'niz otomatik olarak kriptografik bir talebi imzalar ve hesabınız e-posta veya şifre olmadan anında oluşturulur. Güçlü güvenlik ve tam anonimlik.



### İlk yapılandırma



![Configuration post-connexion](assets/fr/04.webp)



**Mevcut parametreler** :




- Kullanıcı adı**: kullanıcı adınızı kişiselleştirin
- Otomatik para çekme**: işlem kapandıktan sonra wallet'inize otomatik para çekme işlemlerini etkinleştirin
- İki Faktörlü Kimlik Doğrulama**: 2FA ile gelişmiş güvenlik
- Dokümantasyon**: resmi kaynaklara erişim



## Interface turu



LN Markets arayüzü, yan menüden erişilebilen çeşitli bölümler halinde düzenlenmiştir:



### Gösterge Tablosu



![Dashboard](assets/fr/06.webp)



Performansınızı ürün türüne göre (Çapraz Vadeli İşlemler, İzole Vadeli İşlemler, Opsiyonlar) P&L, işlem hacimleri ve kişisel Address Lightning (örn. `pivi@lnmarkets.com`) ile görüntüler.



### Profil



![Profil trader](assets/fr/07.webp)



Ayrıntılı istatistikler: işlem sayısı, tüccar türü (SCALPER, vb.), medyan pozisyon süresi, Uzun/Kısa dağılımı, kazanma oranı, ortalamalar (miktar, marj, kaldıraç) ve hacme göre kademeli ücret yapısı.



### Ticaret



![Historique des trades](assets/fr/08.webp)



İşlemler sekmesi, tüm önemli ölçütlerle birlikte pozisyonlarınızın eksiksiz bir geçmişini görüntüler: oluşturma tarihi, yön (Uzun/Kısa), pozisyon boyutu (miktar), taahhüt edilen marj, giriş ve çıkış fiyatı, gerçekleşen kar/zarar (P&L) ve işlem ücretleri. Ürün türüne (vadeli işlemler/opsiyonlar) göre filtreleyebilir ve verilerinizi harici analiz veya muhasebe için dışa aktarabilirsiniz.



### Ayarlar



![Paramètres de la plateforme](assets/fr/05.webp)



Ayarlar sekmesi iki sekme sunar: **Hesap** ve **Interface**.



**Hesap** sekmesi:



Düzenlenebilir alanlarla hesap yönetimi :




- Kullanıcı adı**: "Güncelle" düğmesi ile kullanıcı adınızı (örneğin "pivi") değiştirin
- E-posta**: e-posta adresinizi ekleyin/düzenleyin
- Para yatırma bitcoin adresi**: on-chain fonlarını yatırmak için kullanabileceğiniz bitcoin adresi.



**Üç yapılandırma geçişi** :




- Liderlik tablolarında görün**: herkese açık liderlik tablolarında görünüp görünmeyeceğinizi seçin
- Taproot adreslerini kullanın**: on-chain para yatırma/çekme işlemleri için Bitcoin Taproot adreslerini kullanın
- Otomatik para çekme işlemlerini etkinleştir**: işlem kapatıldıktan sonra wallet Lightning'inize otomatik para çekme işlemlerini etkinleştirin



**Hesap geçişi**: Lightning hesabınızı klasik e-posta/parola kimlik doğrulamasına geçirmenizi sağlayan bölüm.



**Session yönetimi**: yerel tarayıcı verilerinin bağlantısını kesmek ve temizlemek için "Oturumu ve yerel verileri temizle" düğmesi.



**Interface** sekmesi:



Yedi geçiş ile kullanıcı deneyimini özelleştirin:




- Emir onayını atla**: işlem gerçekleştirilmeden önce onay modalini devre dışı bırak (hızlı işlem)
- Araç ipuçlarını göster**: öğelerin üzerine gelindiğinde araç ipuçlarını görüntüle
- Özel Mod (hassas verileri maskeler)**: arayüzdeki miktarları ve hassas verileri maskeler (gizlilik modu)
- Profilde net PL'yi göster**: herkese açık profilinizde net kar/zararı gösterin
- Birim simgelerini kullan**: para birimleri için simgeleri görüntüle (sats, $)
- Sesli bildirimleri etkinleştir**: alım satım olayları için sesli bildirimleri etkinleştirin
- Masaüstü bildirimlerini etkinleştir**: işletim sistemi masaüstü bildirimlerini etkinleştirin



### Wallet



![Wallet](assets/fr/09.webp)



Bitcoin ve Sentetik USD bakiyeleri ile para yatırma, çekme, çapraz transferler, takaslar, fonlama ve on chain adres yönetimi geçmişi.



### API



![API V3](assets/fr/10.webp)



LN Markets, işlemlerinizi komut dosyaları veya botlar aracılığıyla tamamen otomatikleştirmek için eksiksiz bir API REST (V2 ve V3) sunar. Doğrudan arayüzden özelleştirilebilir izinlere (salt okunur, alım satım, para çekme) sahip API anahtarları oluşturabilirsiniz. Kolay entegrasyon için resmi TypeScript ve Python SDK'ları mevcuttur. Tam API V3 belgeleri [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3) adresinde mevcuttur.



## İlk para yatırma işlemi



"Para Yatırma" üzerine tıklayın. Üç yöntem mevcuttur:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: QR kodunu wallet Lightning cihazınızla tarayın


2. **Invoice**: bir tutar girin ve ardından Lightning faturasını tarayın


3. **On-Chain**: depo Bitcoin on chain



## Uygulamada ticaret



### Vadeli İşlemlerde Uzun İşlem: yukarı yönde bahis



Gösterge Tablosundan "Vadeli İşlemler" ve ardından "İzole" üzerine tıklayın. Uzun pozisyon açmak için **"Satın Al "** üzerine tıklayın.



![Interface Futures Long](assets/fr/12.webp)



Pozisyon hesaplayıcısını görüntülemek için "Satın Al" düğmesinin yanındaki **hesaplayıcı** simgesine tıklayın:



![Calculateur de position Long](assets/fr/13.webp)



**Somut örnek** :




- Miktar**: $100 (pozisyon büyüklüğü)
- Ticaret Marjı**: 12.336 sats (taahhüt edilen marj)
- Kaldıraç**: 7.73× (her %1 BTC değişimi = sermayeniz üzerinden %7,73)
- Giriş fiyatı** : $104,863.5
- Tasfiye**: $92,852 (kritik otomatik tasfiye fiyatı)
- Çıkış fiyatı**: 110.000 $ (kar hesaplaması için)
- PL** : 4.492 sats (110.000 $'dan çıkış yapılırsa kar)



**Senaryolar** :




- Artış +%4,9** (110.000 $) : +4.492 sats kâr (+%36,4)
- Nötr** (104.863 $) : -185 sats (sadece ücretler)
- Aşağı -%11,5** (92.852 $): toplam tasfiye (-%100)



İşlemi onaylamak için "Satın Al" düğmesine tıklayın. **İki olası durum** :





- Hesabınızda yeterli likidite** varsa: doğrudan bir onay modu görüntülenir (aşağıdaki resim). İşlemi anında gerçekleştirmek için "Evet" üzerine tıklayın.



![Confirmation trade Long](assets/fr/14.webp)





- Yeterli nakit paranız yoksa**: bunun yerine bir Lightning QR kodu görüntülenir. Gerekli marjı ödemek için wallet Lightning'iniz ile tarayın. Ödeme alındığında işlem otomatik olarak açılır



### Vadeli İşlemlerde Kısa İşlem: Aşağı yönlü bahis



Kısa pozisyon açmak için **"Sat "** seçeneğine tıklayın (fiyat düşerse kazanırsınız). Pozisyonunuzu ayarlamak için hesap makinesi simgesini kullanarak hesap makinesini açın:



![Calculateur de position Short](assets/fr/15.webp)



Onaylamak için "Sat" üzerine tıklayın. Uzun'a gelince, **iki olası durum**:





- Yeterli paranız varsa**: doğrudan onay modu, "Evet" üzerine tıklayın
- Yeterli nakit paranız yoksa**: bir Lightning QR kodu görüntülenir (aşağıdaki resim). Gerekli marjı ödemek için wallet Lightning'inizle bu kodu tarayın:



![Paiement Lightning pour Short](assets/fr/16.webp)



Lightning ödemesi alındıktan sonra, Kısa pozisyonunuz otomatik olarak açılır. Daha sonra bunu işlem arayüzünden yönetebilirsiniz.



#### Pozisyon kapatma



Pozisyonunuzu (Uzun veya Kısa) kapatmak için, yönetim arayüzünün sağ alt köşesindeki **küçük çarpı işaretine** tıklayın:



![Interface de clôture](assets/fr/17.webp)



İşlem kapanışını onaylamak için bir onay iletişim kutusu görüntülenir:



![Confirmation clôture](assets/fr/18.webp)



Modal, mevcut P&L'nizi (kar veya zarar) görüntüler. Kapatmak için "Evet "e tıklayın. Bakiye, Lightning aracılığıyla Wallet'inize anında eklenir (kâr) veya düşülür (zarar).



### Opsiyon Alım Satımı: koşullu satın alma hakkı



Opsiyonlar, ödenen primle sınırlı **risk** sunar ve likidasyon mümkün değildir. Alım opsiyonu size vade bitiminden önce kullanım fiyatından Bitcoin satın alma hakkı (yükümlülüğü değil) verir. Vadeli işlemlerin aksine, yatırdığınız primden daha fazlasını asla kaybedemezsiniz.



Gösterge Tablosundan "Seçenekler "e tıklayın, ardından "Çağrı" sekmesini seçin.



![Interface Options Call](assets/fr/19.webp)



İşleminizi aşağıdaki parametrelerle yapılandırın:




- Miktar**: $100 (sözleşmenizin boyutu)
- Son kullanma tarihi** : 2025-11-15 (son kullanma tarihi)
- Strike**: $96,000 (hedef fiyat)



Diğer alanlar otomatik olarak hesaplanır:




- Marj**: 1.045 sats (ödenecek prim, yatırımınız)
- Başabaş**: $96,923 (hissenizi geri kazanma fiyatı)
- Delta**: 40 (Bitcoin fiyat duyarlılığı)



**Kazancınızı nasıl hesaplarsınız?



Kârınız, vade sonundaki Bitcoin fiyatına bağlıdır. Formül: **(BTC fiyatı - Strike) × Contract boyutu - Ödenen prim**.



**Somut örnekler** :





- Bitcoin $96,000** (mevcut fiyat) : İçsel değer = $0. **Kayıp: -1.045 sats** (primi kaybedersiniz)





- Bitcoin 97.000$**: İçsel değer = (97.000 - 96.000) × 0,00105 BTC = 1,05 $. sats ≈ 2,175 sats'ye dönüştürüldü. **Kâr: 2,175 - 1,045 = +1,130 sats** (+%108 kazanç)





- 98.000$'dan Bitcoin**: içsel değer = 2.000$ ≈ 3.224 sats. **Kâr: +2.179 sats** (+%208 kazanç)





- 100.000$** değerinde Bitcoin: içsel değer = 4.000$ ≈ 5.263 sats. **Kâr: +4.218 sats** (+%403 kazanç)





- Bitcoin $96,000** altında: Opsiyon değersiz olarak sona erer. **Sınırlı kayıp: -1,045 sats**, tasfiye mümkün değil



"Çağrı Satın Al" üzerine tıklayın. Bir onay iletişim kutusu görüntülenir:



![Confirmation Call option](assets/fr/20.webp)



Onaylamak için tekrar "Çağrı Satın Al "a tıklayın. Opsiyon "Çalışan Opsiyonlar" bölümünde görünür. Vade bitiminde, LN Markets otomatik olarak içsel değeri hesaplar ve kar/zararınızı ayarlar.



**Satım Opsiyonları Hakkında Not** : İşlem çağrı ile aynıdır, ancak tersidir. Satım Opsiyonu ile Bitcoin fiyatının **düşeceğine** bahis oynarsınız. Eğer Bitcoin sizin belirlediğiniz fiyatın altına düşerse kazanırsınız; üstünde kalırsa sadece ödediğiniz primi kaybedersiniz. Kazançların hesaplanması da aynı mantığı izler: **(Kullanım - BTC fiyatı) × Contract büyüklüğü - Ödenen prim**.



### Yıldırım fonunun çekilmesi



"Para Çek" üzerine tıklayın:



![Modal de retrait](assets/fr/21.webp)



**Yöntemler** : LNURL, Invoice, Yıldırım Address, On-Chain.



**Invoice prosedürü** :


1. wallet'inizden bir Lightning faturası oluşturun


2. Faturayı kopyalayın (`lnbc...` ile başlar)


3. LN Markets alanına yapıştırın


4. Çekilmeyi onaylayın


5. wallet'ünüz 1-3 saniye içinde kredilendirilir



Lightning para çekme ücreti yok, sadece minimum yönlendirme maliyeti (pratikte <%0,1).



## Riskler ve en iyi uygulamalar



**Ana riskler** :




- Tam likidasyon**: yüksek kaldıraç marjın %100'ünü dakikalar içinde silebilir
- Deneysel hizmet**: alfa aşaması, teknolojik belirsizlikler
- Karşı taraf riski**: platform tek karşı taraf olarak kalır



**En iyi uygulamalar** :



1. **Sermaye yönetimi**: profilinize uygun bir risk yönetimi stratejisi benimseyin. Örneğin: toplam varlığınızın %5'ini kaldıraçlı alım satıma ayırın, ardından işlem başına bu sermayenin maksimum %1'ini riske atın (örneğin: 1 BTC varlık → 5M sats işlem → 50k sats pozisyon başına maksimum risk)



2. **Sistematik stop-loss**: işlem başına kayıplarınızı sınırlamak için stop-loss'ları yapılandırın. Örneğin, %1 risk kuralı ile, art arda kaybedilen 10 işlem bile ticari sermayenizin yalnızca %10'unu temsil eder



3. **Küçük başlayın**: sermaye yönetimi stratejinizi uygulamadan önce mekanizmaları anlamak için önce birkaç bin sats ile test edin



4. **Kârınızı düzenli olarak çekin**: kârınızı ana wallet'inizde güvence altına alın ve platformda yalnızca aktif ticaret sermayesi bırakın



5. **Kaldıraç oranına dikkat edin**: tasfiye risklerinin tam olarak farkında değilseniz >20× kaldıraç oranından kaçının



**Maliyetler**: Lightning para yatırma/çekme ücreti yok, işlem başına ~%0,1 spread (hacme bağlı olarak %0,06'ya düşer).



## Avantajlar ve sınırlamalar



**Avantajlar** :




- Gözetim dışı (işlem dönemleri hariç toplam kontrol)
- KYC'siz (Lightning/Nostr aracılığıyla anonimlik)
- Anında ödemeler (saniyeler içinde para yatırma/çekme)
- Likidite toplama ile sıfır kayma uygulaması
- API kamu ve Nostr desteği



**Sınırlamalar** :




- Hizmet alfası (olası evrimler)
- Binance/Deribit'ten daha düşük likidite
- ABD'de ikamet edenlere yasak



## Sonuç



LN Markets, kontrolü kullanıcılara geri vermek için Lightning Network'u yerel olarak entegre ederek Bitcoin ticaretinin büyük bir evrimini temsil etmektedir. Egemenliklerinden ödün vermeden spekülasyon yapmak isteyen bilgili bitcoin kullanıcıları için bu, geleneksel merkezi borsalara benzersiz bir alternatiftir.



Platform, USDT lineer vadeli işlemler ve geliştirilmekte olan Discreet Log Contracts (DLC) aracılığıyla gözetim dışı ticaret ile gelişmeye devam ediyor. İyi risk yönetimi uygulamaları (küçük miktarlar, zararı durdurma, düzenli para çekme) uygulayarak LN Markets, Bitcoin kaldıracını sorumlu bir şekilde keşfetmek için güçlü bir araç haline gelir.



Küçük başlayın, birkaç bin sats ile test edin ve bu yeni Lightning Network sınırını yavaş yavaş keşfedin. Mutlu egemen ticaret ⚡️!



## Kaynaklar





- [LN Markets resmi web sitesi](https://lnmarkets.com)
- [Dokümantasyon](https://docs.lnmarkets.com)