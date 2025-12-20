---
name: BitBanana
description: Lightning düğümünüz için mobil yönetici
---

![cover](assets/cover.webp)



Bu eğitimde, Lightning node'unuzu akıllı telefonunuzdan kontrol etmek için Android'de BitBanana'yı nasıl kuracağınızı ve yapılandıracağınızı öğreneceksiniz. Uygulamayı mevcut altyapınıza (Umbrel, RaspiBlitz, myNode veya herhangi bir LND/Core Lightning node) nasıl bağlayacağınızı, Lightning ödemelerini nasıl yapacağınızı, kanallarınızı uzaktan nasıl yöneteceğinizi, yönlendirme gelirinizi nasıl görüntüleyeceğinizi ve yapılandırmalarınızı nasıl yedekleyeceğinizi göreceğiz. Ayrıca düğümünüze erişimi korumak için en iyi güvenlik uygulamalarını ve popüler bir alternatif olan Zeus ile nasıl karşılaştırıldığını öğreneceksiniz.



## Karşınızda BitBanana



BitBanana, akıllı telefonunuzu Lightning düğümünüzün uzaktan kontrolü için eksiksiz bir kontrol paneline dönüştüren açık kaynaklı bir Android mobil uygulamasıdır. Telefona yerel bir düğüm yerleştiren Lightning cüzdanlarının aksine, BitBanana %100 uzaktan kontrol felsefesini benimser: uygulama hiçbir satoshi tutmaz ve yalnızca mevcut altyapınıza bağlanır.



Michael Wünsch tarafından MIT lisansı altında geliştirilen uygulama, sıfır kişisel veri toplama ve doğrulanmış tekrarlanabilir yapılarla tam şeffaflığı garanti eder. BitBanana, standart URI'ler (`lndconnect://` ve `clngrpc://`) aracılığıyla LND ve Core Lightning'i yerel olarak destekleyerek ilk yapılandırmayı büyük ölçüde basitleştirir. Uygulama ayrıca, kişisel bir düğümü olmayan kullanıcılar için LndHub ve Nostr Wallet Connect'i de tanır, ancak bu modlar sınırlı işlevsellikle gözetim altında çalışır.



Arayüz, node'unuzun tüm kritik işlevlerine tam erişim sunar: ödeme gönderme ve alma (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), Lightning kanal yönetimi (açma, kapatma, ücret ayarlama, yeniden dengeleme), gelişmiş coin kontrolü ve gözetleme kulesi yönetimi. BitBanana ayrıca birkaç sağlam güvenlik katmanı uygular: biyometrik kilitleme, gizli mod, Acil PIN ve bağlantıları anonimleştirmek için yerel Tor desteği.



## Desteklenen platformlar ve kurulum



### Kurulum



BitBanana yalnızca Android 8.0 veya üstü için kullanılabilir. Uygulama iOS'ta mevcut değildir ve herhangi bir sürüm planlanmamaktadır. Bu sınırlama projenin geçmişi ile açıklanmaktadır: BitBanana, çalışmalarına kendi markası altında devam etmeye karar veren Michael Wünsch tarafından geliştirilen Zap Android'in doğrudan halefidir. Zap, farklı katılımcılar tarafından ayrı kod tabanlarına sahip olarak geliştirilen ayrı uygulamalardan (Zap Android, Zap iOS, Zap Desktop) oluşan bir aileydi. BitBanana sadece Android şubesini takip ediyor.



Buna ek olarak, iOS ekosistemi, gözetim altında olmayan Lightning uygulamaları için önemli düzenleyici ve teknik kısıtlamalar sunmaktadır. Apple, 2023 yılında bir Zeus güncellemesini "lisans ihlalleri" nedeniyle reddetti ve 2024 yılında Phoenix Wallet, Lightning hizmet sağlayıcılarına ilişkin düzenleyici belirsizlikler karşısında ABD App Store'dan ayrıldı. Bu engeller, birçok Lightning geliştiricisinin neden gözetim dışı uygulamalar için daha açık bir politika sunan Android'i tercih ettiğini açıklıyor.



Android için üç yükleme yöntemi mevcuttur: Google Play Store (5000+ kurulum, otomatik güncellemeler), F-Droid (tekrarlanabilir yapılar, kaynak kodu doğrulama) veya GitHub'dan manuel APK.



![BitBanana](assets/fr/01.webp)



Resmi bitbanana.app web sitesi (solda) "SIFIR veri toplama ile %100 Kendi Kendine Gözetim" ile övünüyor. Orta ekran üç indirme seçeneğini gösteriyor: F-Droid (önerilen), Google Play ve APK. Sağdaki ekran ödeme uyarıları için bildirim iznini göstermektedir.



Uygulama şu izinleri ister: ağ (düğüm bağlantısı), kamera (QR kodları), NFC (LNURL), arka plan hizmetleri (bildirimler), biyometri (güvenlik) ve WireGuard VPN. İzleyici yok, sıfır veri toplama. Güvenli erişim için parola veya biyometrik kilitlemeyi etkinleştirin.



## İlk yapılandırma



### Bir LND düğümüne bağlanma



BitBanana'yı LND düğümünüze (Umbrel, RaspiBlitz, myNode) bağlamak için adres, TLS sertifikası ve kimlik doğrulama makaronunu içeren bir `lndconnect` URI veya QR kodu alın.



Bu eğitim için, umbrel aracılığıyla bir LND düğümü kullanıyoruz. Daha fazla ayrıntı için lütfen özel eğitimimize bakın:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Lightning Node uygulamasında, sağ üstteki menüye erişin ve "Connect wallet "i seçin.



![BitBanana](assets/fr/04.webp)



Tor üzerinden bağlanmak için **gRPC (Tor)** öğesini seçin (önerilir). QR kodu ve ayrıntılar (Host .onion, Port 10009, Macaroon) görüntülenir.



![BitBanana](assets/fr/02.webp)



BitBanana'da "BAĞLAN NODE" düğmesine basın, QR kodunu tarayın veya URI'yi yapıştırın. Kamera erişimini yetkilendirin, ardından onaylamadan önce görüntülenen .onion adresini kontrol edin.



**Core Lightning** bağlantısı



LND yerine Core Lightning (CLN) kullanıyorsanız, karşılıklı TLS sertifikalarını içeren URI `clngrpc://` ile işlem aynı kalır. Core Lightning, BOLT12'yi (teklifler) yerel olarak destekleyerek LND'de bulunmayan yeniden kullanılabilir faturaları ve yinelenen ödemeleri mümkün kılar.



**Kişisel düğüm olmadan bağlantı (LNbits/hosted)**



Lightning düğümünüz yoksa BitBanana, LndHub (BlueWallet ve LNbits tarafından kullanılan protokol) veya Nostr Wallet Connect (NWC) aracılığıyla barındırılan hizmetlere bağlanabilir. Lütfen dikkat: bu modlar sınırlı işlevsellik ile saklama modunda (hizmet fonlarınızı barındırır) çalışır. Kanalları yönetemez veya yönlendirme ücretlerini yapılandıramazsınız ve yalnızca Lightning ödemeleri gönderip alabilirsiniz.



LNbits veya Nostr Wallet Connect hakkında daha fazla bilgi için lütfen çeşitli eğitimlerimize başvurun:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Günlük kullanım



### Interface ana



Ana ekran Lightning bakiyenizi gösterir ve sol üstteki menü aşağıdaki bölümlere erişim sağlar: Kanallar, Yönlendirme, İmzala/Doğrula, Düğümler, Kişiler, Ayarlar, Yedekleme. Saat simgesi (sağ üstte) işlem geçmişini açar. Alttaki "Gönder" ve "Al" düğmeleri satoshilerinizi göndermenizi ve almanızı sağlar.



![BitBanana](assets/fr/05.webp)



### Yıldırım ve on-chain ödemeleri



![BitBanana](assets/fr/10.webp)



**Bir ödeme gönderin:** Ana ekrandan "Gönder" düğmesine basın. Ödeme ekranı (solda), kodları taramak için sağ üstte bir QR tarayıcı ile "Address veya ödeme verileri" alanına bir adres veya ödeme verileri yapıştırmanızı sağlar. Her seferinde tarama yapmak zorunda kalmamak için Kişiler bölümünde kayıtlı bir kişiyi de seçebilirsiniz.



BitBanana tüm ödeme formatlarını akıllıca tanır: klasik Lightning faturaları (`lnbc` ile başlayan karakter dizileri), Lightning Address (`utilisateur@domaine.com` gibi e-posta formatı), dinamik ödemeler için LNURL-pay kodları, para çekmek için LNURL-withdraw ve hatta önceden fatura olmadan doğrudan bir Lightning genel anahtarına Keysend ödemeleri. Uygulama, gerekli LNURL çözümlemelerini arka planda otomatik olarak gerçekleştirir.



Fatura yüklendikten sonra, BitBanana tüm ayrıntıları görüntüler: tam tutar, tahmini yönlendirme ücretleri, ödeme açıklaması (alıcı tarafından sağlanmışsa) ve fatura son kullanma tarihi. Onaylandıktan sonra, ödeme Lightning kanallarınız üzerinden yönlendirilir. Daha sonra adım adım izlenen rotayı ve gerçekte ödenen ücretleri işlem ayrıntılarında görüntüleyebilirsiniz.



**Ödeme al:** "Al" düğmesine basın. Bir seçici (sağ ekran) Lightning (kanallarınız üzerinden anında ödeme) ve On-Chain arasında seçim yapmanızı sağlar. Lightning makbuzu için, istediğiniz tutarı satoshi cinsinden girin (veya ödeyenin tamamlaması için sabit tutarı olmayan bir fatura oluşturmak için 0'da bırakın) ve faturada görünmesi için isteğe bağlı bir açıklama ekleyin. BitBanana anında tarama için QR kodlu bir Lightning faturası oluşturur. Ayrıca faturayı metin olarak kopyalayabilir ve e-posta ile gönderebilirsiniz. Ödeme alınır alınmaz, bir anlık bildirim sizi uyarır ve işlem tüm ayrıntılarıyla birlikte hemen geçmişte görünür.



### Kanallar ve yönlendirme



![BitBanana](assets/fr/06.webp)



"Kanallar" bölümü gönderme/alma yeteneklerinizi gösterir ve kanallarınızı benzersiz avatarlarla listeler. Her kanal, likiditesinin yerel ve uzak bakiye arasındaki dağılımını gösterir. Tüm ayrıntılar ve eylemler (kapatma, yönlendirme ücretlerini değiştirme) için bir kanala dokunun. Sağ üstteki üç nokta, kanallarınızın likiditesini yeniden dengelemek için "Yeniden Dengeleme" seçeneğine erişim sağlar. "+" düğmesi yeni bir kanal açar.



Yönlendirme bölümü (merkezi ekran), stratejinizi optimize etmek için ayrıntılı yönlendirme geçmişiyle birlikte dönemlere göre (1D, 1W, 1M, 3M, 6M, 1Y) yönlendirme gelirlerini görüntüler.



İmzala/Doğrula (sağ ekran) düğüm kontrolünü kanıtlamak için mesajları kriptografik olarak imzalamanızı/doğrulamanızı sağlar.



### Çoklu düğümler ve parametreler



![BitBanana](assets/fr/07.webp)



**Düğümleri Yönet**: manuel olarak eklemek, QR taramak veya düğümler arasında geçiş yapmak için düğmelerle birlikte düğümlerinizi listeler. Özellikle, aynı düğüme farklı bağlantı türleri kurabilirsiniz: LAN, VPN veya Tor.



**Kişileri Yönet**: Hızlı ödemeler için Lightning kişilerinizi saklar.



**Ayarlar**: para birimini, dili, avatarları özelleştirin. Güvenlik ve Gizlilik bölümü: Uygulama Kilidi (PIN/biyometrik), Bakiyeyi gizle (gizli mod), Tor (IP anonimleştirme). Fiyat oracle'larının, blok kaşiflerinin, özel ücret tahmincilerinin yapılandırılması.



## Avantajlar ve sınırlamalar



**Öne Çıkanlar:**




- Tam mobilite: Lightning düğümünüzü her yerden kontrol edin
- Tam işlevsellik: ödemeler (LNURL, Lightning Address, BOLT 12), kanal yönetimi, jeton kontrolü, gözetleme kuleleri, çoklu düğümler
- Güvenlik PIN/biyometri, gizli mod, Acil PIN, yerel Tor, ekran görüntüsü engelleme
- Ücretsiz, açık kaynak (MIT), sıfır komisyon, sıfır veri toplama



**Sınırlamalar:**




- Aktif bir Lightning düğümü (veya gözetim modunda LNbits) gerektirir
- Planlanan iOS sürümü yok
- Telefona erişimin güvence altına alınması kritik önem taşır (makaron yöneticisi = düğüme tam erişim)



## En iyi uygulamalar



**Güvenlik:**




- PIN/biyometrik kilidi etkinleştirin (düğüme yetkisiz erişimi önler)
- Bir Acil Durum PIN'i ayarlayın (zorlama durumunda hassas verileri siler)
- Oturum açma URI'nizi veya makaronunuzu asla paylaşmayın
- Düşman ortamlarda gizli mod



**Giriş:**




- VPN ağı (Tailscale, ZeroTier): hız ve güvenlik arasında en iyi uzlaşma
- Tor: maksimum gizlilik, daha yüksek gecikme süresi
- Clearnet: gerekli olmadıkça kaçının (IP'ye maruz kalma, açık portlar)



### Yedekleme ve geri yükleme



Son olarak, telefon taşıma veya yeniden yükleme için yapılandırmalarınızı kaydetmenizi sağlayan "Yedekleme" menüsü vardır.



![BitBanana](assets/fr/08.webp)



**Önemli:** Yedekleme seed veya kanal yedeklemelerini İÇERMEZ (düğüm üzerinde yapılmalıdır). Şunları içerir: düğüm yapılandırmaları (adresler, sertifikalar, makaronlar), etiketler, kişiler, parametreler. Geri yükle düğmesi mevcut bir yedeği içe aktarmanızı sağlar. Kaydetmeden önce onaylama gereklidir.



![BitBanana](assets/fr/09.webp)



Bir şifreleme parolası girin (sağ ekran). Sistem `BitBananaBackup_2025-XX-XX.dat` dosyasını kaydetmek için dosya seçiciyi (sol ekran) açar. Onay "Yedekleme oluşturuldu".



**Güvenlik:** Yedeklemeyi şifreli olarak saklayın (kişisel bulut, USB, NAS). Dosyaları veya parolaları asla paylaşmayın. Geri yüklemeyi düzenli olarak test edin. Yedekleme bağlantıları kurtarır, fonları değil.



## BitBanana vs Zeus: Aralarındaki fark nedir?



Bir Lightning düğümünü yönetmek için mobil uygulamaları araştırıyorsanız, BitBanana'ya popüler bir alternatif olan Zeus ile karşılaşmanız muhtemeldir. Yalnızca mevcut bir düğümün uzaktan kontrolüne odaklanan BitBanana'nın aksine Zeus, iki çalışma modu sunarak daha kapsamlı bir yaklaşım benimsiyor: doğrudan uygulamaya gömülü bir Lightning düğümü (entegre LND ile gömülü mod) ve tıpkı BitBanana gibi harici bir düğüme uzaktan bağlantı.



Bu ikili işlevsellik, Zeus'u özellikle önceden herhangi bir altyapı olmadan Lightning'i denemek isteyen yeni başlayanlar için cazip kılmaktadır. Gömülü mod, eksiksiz bir mobil düğümle anında başlatma sağlarken, ileri düzey kullanıcılar kişisel düğümleri yapılandırıldıktan sonra uzaktan bağlantıya geçebilirler. Zeus ayrıca BitBanana gibi uzaktan bağlantı için LND ve Core Lightning'i de desteklemektedir.



Zeus'un bir diğer önemli avantajı da platformlar arası kullanılabilirliği (iOS ve Android), BitBanana ise sadece Android tabanlı. Zeus ayrıca Lightning ödemelerinin tam zamanında kanallar aracılığıyla alınmasını kolaylaştırmak için Olympus LSP altyapısını, tüccarlar için bir Satış Noktası sistemini ve likiditeyi yönetmek için entegre takas işlevselliğini de içeriyor.



Bununla birlikte, BitBanana kendine özgü güçlü yönlerini korumaktadır: daha basit, daha akıcı bir arayüz, uzaktan kumandaya özel odaklanması sayesinde daha iyi bir kullanıcı deneyimi (UX) ve bağlamsal açıklamalarla eğitici bir yaklaşım. Zeus daha fazla işlevsellik sunuyor, ancak daha karmaşık bir arayüz pahasına. Uygulama, gözetim işlevleri olmaksızın bir düğümü yalnızca uzaktan kontrol etmek isteyen kullanıcılar için özellikle uygun olmaya devam etmektedir.



Zeus hakkında daha fazla bilgi edinmek için aşağıdaki eğitimlere göz atın:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Sonuç



BitBanana, Android akıllı telefonunuzu eksiksiz bir Lightning kontrol paneline dönüştürerek düğüm operatörleri için benzeri görülmemiş bir mobilite sunar. Uygulama tüm işlevleri kapsar: ödemeler (tüm formatlar), kanal yönetimi, jeton kontrolü, gözetleme kuleleri, çoklu düğüm, gelişmiş güvenlik (PIN / biyometri, Tor, Acil PIN).



Tamamen egemen olan BitBanana hiçbir veri toplamaz ve fonlarınızın ne gizliliğinden ne de kontrolünden ödün verir. Açık kaynak kodu (MIT) şeffaflığı garanti eder.



## Kaynaklar



### Resmi belgeler




- [BitBanana web sitesi](https://bitbanana.app)
- [Belgelerin tamamı](https://docs.bitbanana.app)
- [GitHub kaynak kodu](https://github.com/michaelWuensch/BitBanana)



### Kurulum




- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)