---
name: Dana Wallet
description: Sessiz Ödemeler için Minimalist Portföy (BIP-352)
---

![cover](assets/cover.webp)



Bitcoin adreslerinin yeniden kullanımı, kullanıcı gizliliğine yönelik en doğrudan tehditlerden biridir. Bir alıcı birden fazla ödeme almak için tek bir adresi paylaştığında, herhangi bir gözlemci tüm ilişkili işlemleri izleyebilir ve finansal geçmişlerini yeniden yapılandırabilir. Bu sorun özellikle, kendilerinin veya bağışçılarının gizliliğini tehlikeye atmadan bağış adreslerini kamuya açık bir şekilde göstermek isteyen içerik oluşturucuları, hayır kurumlarını veya aktivistleri etkilemektedir.



Dana Wallet bu soruna zarif bir çözümle yanıt veriyor: Sessiz Ödemeler. 2024'te piyasaya sürülen bu minimalist, açık kaynaklı wallet, yeniden kullanılabilir bir statik adres oluştururken, alınan her ödemenin blok zincirinde ayrı bir adreste sonlanmasını garanti eder. Göndericinin alıcıyla önceden etkileşime girmesine gerek yoktur ve hiçbir dış gözlemci bireysel işlemleri birbirine bağlayamaz. Blok zincirinde bu ödemeler tamamen sıradan Taproot işlemleri gibi görünür.



Dana Wallet, Mainnet ve Signet'te mevcuttur, ancak geliştiriciler hala deneysel olduğunu düşünüyor ve kaybetmeye hazır olmadığınız fonları yatırmamanızı tavsiye ediyor. Bu eğitimde, herhangi bir gerçek parayı riske atmadan Silent Payments'ı keşfetmek için Signet sürümünü kullanacağız.



## Dana Wallet nedir?



### Felsefe ve hedefler



Dana Wallet "SP öncelikli" bir yaklaşım benimser: wallet yalnızca Sessiz Ödeme adresleri oluşturur ve yalnızca bu tür ödemeleri kabul eder. Bu uygulama ile klasik bir Bitcoin adresi (eski, SegWit veya Taproot standardı) oluşturamazsınız. Bu kasıtlı kısıtlama, diğer özellikler tarafından dikkatiniz dağıtılmadan tamamen BIP-352 protokolünü öğrenmeye konsantre olmanızı sağlar. Düzenli arayüz, kasıtlı olarak çok sayıda seçenek yerine kullanım kolaylığını tercih eder ve aracı on-chain gizlilik kavramlarına yeni başlayan kullanıcılar için bile erişilebilir hale getirir.



Proje tamamen açık kaynaklıdır, mobil arayüz için Flutter ve dahili kriptografik mantık için Rust ile geliştirilmiştir. Bu mimari, yoğun tarama işlemleri için akıcı bir kullanıcı deneyimini optimum performansla birleştiriyor.



### Sessiz Ödemeler nasıl çalışır?



Sessiz Ödemeler (BIP-352) Eliptik Eğri Diffie-Hellman Anahtarı Exchange (ECDH) kullanan sofistike bir kriptografik mekanizmaya dayanmaktadır. Alıcı, iki farklı açık anahtardan oluşan statik bir adres (mainnet'de `sp1...` veya Signet'te `tsp1...` ile başlayan) oluşturur: gelen ödemeleri tespit etmek için bir tarama anahtarı ($B_{scan}$) ve alınan fonları harcamak için bir harcama anahtarı ($B_{spend}$). Bu ayrım, tarama anahtarını bağlı bir cihazda kullanırken harcama anahtarını wallet donanımında tutmayı mümkün kılar.



Bir gönderici ödeme yapmak istediğinde, wallet girdilerinin özel anahtarlarının toplamını alıcının genel tarama anahtarıyla birleştirerek paylaşılan bir ECDH sırrı hesaplar. Bu sır, alıcının harcama anahtarına eklenerek söz konusu işlem için benzersiz bir Taproot adresi oluşturan bir kriptografik "ince ayar" üretir.



Alıcı, özel tarama anahtarını ve işlemde görünen açık anahtarları kullanarak bu hesaplamayı yeniden üretebilir (Diffie-Hellman matematiksel özelliği). Bu, göndericiyle önceden herhangi bir etkileşime girmeden fonları tespit etmesini ve harcamasını sağlar.



Bu yaklaşım çeşitli avantajlar sunmaktadır:




- Alıcı gizliliği**: her ödeme farklı bir adrese gider
- Gönderen gizliliği**: ödemeleri birbirine bağlayan kalıcı bir tanımlayıcı yok
- Üçüncü taraf sunucu yok**: protokol bağımsız olarak çalışır
- Ayırt edilemeyen işlemler**: Sessiz Ödemeler sıradan Taproot işlemleri gibi görünür



Ana dezavantaj tarama maliyetidir: alıcının kendisine yönelik olanları tespit etmek için her yeni Taproot işlemini analiz etmesi gerekir.



Sessiz Ödemelerin teknik işleyişi hakkında daha fazla bilgi edinmek isterseniz, Sessiz Ödemelere ayrılmış bir bölüm içeren Bitcoin'te gizlilik konulu BTC204 kursunu öneririz:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Desteklenen platformlar



Dana Wallet bir Android uygulaması olarak mevcuttur. APK, geliştiriciler tarafından sağlanan özel F-Droid deposu üzerinden, Obtainium aracılığıyla veya doğrudan GitHub'dan indirilebilir. Linux kullanıcıları için Flutter uygulamasını masaüstü için derlemek teknik olarak mümkündür.



Uygulama iOS'ta veya resmi mağazalarda (Google Play, App Store) mevcut değildir, bu da deneysel durumunu ve teknik bir kitleye odaklandığını yansıtmaktadır.



## Kurulum



### Temel ön koşullar



Dana Wallet'yi Android'e yüklemek için, güvenlik ayarlarında "Bilinmeyen kaynaklar" seçeneği etkinleştirilmiş bir Android cihaza ihtiyacınız olacaktır. Herhangi bir hesap veya kayıt gerekmez.



### F-Cold depozitosu ekleyin



Önerilen yöntem Dana Wallet'un özel F-Droid deposunu eklemektir. Depo bağlantısını ve taramak için bir QR kodu bulacağınız `fdroid.silentpayments.dev` adresine gidin. Depo şu anda 3 uygulama sunmaktadır: Mainnet sürümü, Geliştirme ve Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### F-Droid aracılığıyla kurulum



Android cihazınızda F-Droid uygulamasını açın, ardından sağ alttaki simge aracılığıyla Ayarlar'a erişin. Uygulama kaynaklarını yönetmek için "Depolar "ı seçin. Yeni bir depo eklemek için "+" düğmesine basın, ardından QR kodunu tarayın veya `https://fdroid.silentpayments.dev/fdroid/repo` bağlantısını yapıştırın. Depo eklendikten sonra, Dana Wallet'in mevcut üç sürümünü göreceksiniz. "Dana Wallet - Bookmark "ı seçin ve "Install "a basın.



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## İlk yapılandırma



### Portföy oluşturma



Dana Wallet ilk açılışında misyonunu tanıtan bir karşılama ekranı görüntüler: "Aracılar olmadan bağış gönderin ve alın". Devam etmek için "Başla" düğmesine basın. Bir sonraki ekranda uygulamanın üç temel faydası sunulmaktadır:




- Zahmetsiz bağışlar**: saniyeler içinde bağış almaya başlayın
- Varsayılan olarak gizlilik**: sunuculara veya karmaşık altyapıya gerek yok
- E-posta benzeri deneyim**: e-posta kadar basit bir şekilde bitcoin gönderme ve alma



Mevcut bir portföyü geri yüklemek için "Geri Yükle" veya yeni bir portföy oluşturmak için "Yeni wallet Oluştur" arasında seçim yapabilirsiniz. "Yeni wallet Oluştur "a basın.



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Uygulama daha sonra fiziksel bir ortama dikkatlice not etmeniz gereken bir kurtarma ifadesi oluşturur. Gerçek değeri olmayan test fonları için bile iyi yedekleme uygulamalarını benimseyin.



### Interface ve parametreler



Portföy oluşturulduktan sonra, iki sekmeye ayrılmış ana arayüze yönlendirilirsiniz: "İşlem" ve "Ayarlar".



İşlem** sekmesinde bitcoin bakiyeniz (ve bunun dolara dönüşümü), son işlemlerin bir listesi ve iki işlem düğmesi görüntülenir: para göndermek için "Öde" ve bir alma düğmesi (indirme simgesi).



Ayarlar** sekmesi dört seçenek sunar:




- seed ifadesini göster**: kurtarma ifadenizi saklamak için görüntüler
- Fiat para birimini değiştir**: ekran para birimini değiştir (varsayılan olarak USD)
- Arka uç URL'sini ayarla**: Blindbit sunucu URL'sini yapılandırın (sonraki bölüme bakın)
- wallet'yı Sil**: wallet'yı cihazdan tamamen siler



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Blindbit sunucusu



Dana Wallet, Sessiz Ödemelerinizi tespit etmek için **Blindbit** adlı bir indeksleme sunucusu kullanır. Nasıl çalıştığını anlamak, uygulamanın güven modelini değerlendirmek için önemlidir.



**Neden bir sunucuya ihtiyacımız var?



Bir Sessiz Ödemeyi tespit etmek için wallet'unuzun teorik olarak her bloktaki tüm Taproot işlemlerini taraması ve her biri için bir kriptografik hesaplama (ECDH) yapması gerekir. Bir cep telefonunda bu işlem hesaplama ve bant genişliği açısından çok yoğun olacaktır.



Blindbit sunucusu bu sorunu, tüm Taproot işlemleri için ara verileri ("tweaks" olarak adlandırılır) önceden hesaplayarak çözer. wallet'iniz daha sonra bu ince ayarları indirir (işlem başına 33 bayt) ve bir ödemenin size ait olup olmadığını kontrol etmek için son hesaplamayı **yerel olarak** gerçekleştirir.



**Gizlilik korunur**



Adreslerinizi açıkladığınız geleneksel bir Electrum sunucusunun aksine, Blindbit sunucusu hangi ödemelerin size ait olduğunu bilmez. Tüm kullanıcılara aynı verileri sağlar ve son doğrulamayı gerçekleştiren sizin telefonunuzdur. Bu nedenle gizliliğiniz sunucuya karşı korunur.



**Varsayılan sunucu



Dana Wallet, `silentpayments.dev/blindbit/signet` (Signet için) veya `silentpayments.dev/blindbit/mainnet` (Mainnet için) genel sunucusunu kullanır. Kendi sunucunuzu barındırıyorsanız bu URL'yi ayarlardan değiştirebilirsiniz.



**Kendi Blindbit sunucunuzu barındırın**



Tam egemenlik isteyen kullanıcılar için kendi Blindbit Oracle sunucularını barındırmak mümkündür. Bunun için :




- Tam bir Bitcoin Çekirdek düğümü **kılıfsız** (pruned olmayan)
- Blindbit Oracle'ı Yükleme (GitHub'da mevcuttur: `setavenger/blindbit-oracle`)
- Yaklaşık 10 GB ek disk alanı
- Teknik beceriler (Go derleme, sunucu yapılandırması)



Umbrel veya Start9 için henüz paketlenmiş bir uygulama mevcut değildir. Kurulum şimdilik manuel olarak yapılmaktadır. Bu, aktif evrim geçirmekte olan bir alandır ve gelecekte daha erişilebilir çözümler ortaya çıkabilir.



## Günlük kullanım



### Fonların alınması



Bitcoin almak için ana ekrandan alma düğmesine (indirme simgesi) basın. Dana Wallet daha sonra yer iminde `tsp1q...` formatında tam Sessiz Ödeme adresinizi görüntüler. Arayüz çeşitli seçenekler sunar:




- QR kodunu göster**: kolay tarama için adresinizin QR kodunu görüntüler
- Paylaş**: adresi telefonunuzun uygulamaları aracılığıyla paylaşın
- Kopyala**: adresi panoya kopyalar



Ekranda gösterildiği gibi, bu adresi gizliliğinizden ödün vermeden sosyal ağlarınızda herkese açık olarak paylaşabilirsiniz.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Signet'te ilk test fonlarınızı almak için `silentpayments.dev/faucet/signet` adresinden erişebileceğiniz özel Silent Payments musluğunu kullanın. Adresinizi `tsp1...` kopyalayın, muslukta verilen alana yapıştırın ve ardından talebi doğrulayın. Bir bloğun çıkarılmasını bekleyin (Signet'te yaklaşık 10 dakika).



### Ödeme gönderin



Para göndermek için ana ekrandan "Öde" düğmesine basın. Alıcıyı belirlemek için üç seçenek içeren "Alıcı(lar)ı seçin" ekranı görüntülenir:




- Ödeme bilgilerini manuel olarak girin
- Panodan yapıştır**: panodan bir adres yapıştırır
- QR Kodunu Tara**: adresi içeren bir QR kodunu tarayın



Alıcının adresi doğrulandıktan sonra, "Tutar girin" ekranı gönderilecek tutarı satoshis olarak girmenizi sağlar. Mevcut bakiyeniz referans için görüntülenir. Devam etmek için "Ücret seçimine ilerle" düğmesine basın.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Bir sonraki ekranda, gereken aciliyete bağlı olarak üç ücret seviyesi gösterilmektedir:




- Hızlı** (10-30 dakika): hızlı onay için daha yüksek ücretler
- Normal** (30-60 dakika): orta düzeyde maliyetler
- Yavaş** (1+ saat): acil olmayan işlemler için minimum ücret



Ücret seviyesini seçtikten sonra, "Göndermeye hazır mısınız?" onay ekranı tüm ayrıntıları özetler: hedef adres, tutar, tahmini süre ve işlem ücreti. Bu bilgileri dikkatlice kontrol edin, ardından işlemi göndermek için "Gönder" düğmesine basın.



Gönderildikten sonra, işlem bir bloğa dahil edilene kadar geçmişinizde "Onaylanmadı" durumuyla görünür. Bakiyeniz buna göre güncellenir.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Avantajlar ve sınırlamalar



### Önemli Noktalar





- Pedagojik**: Sessiz Ödemeleri öğrenmeye odaklanan basitleştirilmiş arayüz
- Çift yönlü**: diğer portföylerin aksine hem göndermeyi hem de almayı destekler
- Açık kaynak**: GitHub'da tamamen denetlenebilir kod
- Özel Faucet**: test fonu elde etmeyi kolaylaştırır
- Hesap olmadan**: kayıt veya kişisel veri gerekmez



### Dikkate alınması gereken kısıtlamalar





- Deneysel**: denetlenmemiş yazılım, Mainnet'de dikkatli kullanın
- Sınırlı platform**: çoğunlukla Android, iOS sürümü yok
- Azaltılmış işlevsellik**: jeton kontrolü yok, alt hesap yok, Lightning yok
- Yoğun tarama**: ödeme tespiti önemli miktarda kaynak tüketir



## En iyi uygulamalar



### seed güvenlik



Değersiz arka planlara sahip Signet testleri için bile kurtarma ifadenizi ciddiye alın. Ayarlarda "seed ifadesini göster" seçeneğini kullanarak dikkatlice not alın. İyi bir uygulama olarak, Signet ve Mainnet için tamamen ayrı cüzdanlar bulundurun: test için oluşturulmuş bir seed'ü asla gerçek para almak için tasarlanmış bir wallet'te kullanmayın.



### Deneysel durum hakkında uyarı



Dana Wallet, geliştiricileri tarafından hala deneysel olarak kabul edilmektedir. Açıkça belirttikleri gibi: "Kaybetmek istemediğiniz fonları kullanmayın". Öğrenme amacıyla Signet versiyonunu tercih edin. Mainnet versiyonunu kullanıyorsanız, kendinizi token miktarlarıyla sınırlayın.



### Yedekleme ve geri yükleme



Sessiz Ödemeler fon kurtarma işlemi için BIP-352 protokolü ile uyumlu bir wallet gerekir. Standart bir wallet, UTXO Sessiz Ödemelerinizi almak için blok zincirini tarayamaz. Dana Wallet'i kurulu tutun veya mevcut bir wallet'u kurtarmak için ilk açılışta "Geri Yükle" seçeneğini kullanın.



## BIP-47 ve PayJoin ile karşılaştırma



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Sessiz Ödemeler, daha pahalı bir tarama pahasına BIP-47 bildirim işlemini ortadan kaldırır. PayJoin farklı bir sorunu (giriş korelasyonu) çözer ve Sessiz Ödemeler ile birleştirilebilir.



## Sonuç



Dana Wallet, risksiz bir ortamda Sessiz Ödemeleri öğrenmek için değerli bir eğitim aracıdır. Minimalist yaklaşımı, ikincil özelliklerle dikkatiniz dağılmadan BIP-352 protokolünün temel mekanizmalarını anlamanızı sağlar. Signet ile deneyler yaparak, Bitcoin işlem gizliliği için bu umut verici teknoloji hakkında pratik bir anlayış geliştireceksiniz.



Sessiz Ödemeler, kullanım kolaylığı ve gizliliğe saygının uzlaştırılmasında önemli bir adımı temsil etmektedir. Topluluğun coşkusu ve çeşitli cüzdanlara (Cake Wallet, BitBox02, göndermek için BlueWallet) ilk entegrasyonlar, bir bağış adresinin yayınlanmasının artık sahibinin finansal gizliliğini tehlikeye atmayacağı bir geleceğe işaret ediyor.



## Kaynaklar



### Resmi belgeler




- Dana Wallet GitHub deposu: https://github.com/cygnet3/danawallet
- F-Cold depozito: https://fdroid.silentpayments.dev
- Silent Payments topluluk sitesi: https://silentpayments.xyz
- Spesifikasyon BIP-352: https://bips.dev/352



### Signet test araçları




- Faucet Sessiz Ödemeler: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Blindbit sunucusu (kendi kendine barındırılan)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle