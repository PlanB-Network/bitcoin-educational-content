---
name: LibreWolf
description: LibreWolf gizlilik tarayıcısı nasıl kullanılır?
---

![cover](assets/cover.webp)



Her tıklama, her arama, ziyaret edilen her site: web tarayıcınız küresel bir ticari gözetim sistemini besleyen sofistike bir muhbir haline geldi. Üç milyardan fazla kişi tarafından kullanılan Google Chrome, günlük gezintilerinizi reklam devleri için kazançlı verilere dönüştürüyor. Firefox bile, "etik" bir tarayıcı olarak tanınmasına rağmen, varsayılan olarak tarama alışkanlıklarınızı Mozilla'ya ileten telemetri mekanizmalarını etkinleştirir.



Bu gerçeklik önemli bir soruyu gündeme getiriyor: Sürekli gözetlenmeden ve fişlenmeden internette özgürce gezinmek hala mümkün mü? Neyse ki, kullanıcıyı endişelerinin merkezine geri koyan topluluk projeleri sayesinde cevap evet.



LibreWolf bu dijital direniş felsefesini somutlaştırıyor. Bağımsız geliştiricilerden oluşan bir topluluğun buluşu olan bu tarayıcı, Firefox'u çevrimiçi gözetime karşı gerçek bir kalkana dönüştürüyor. Ticari tarayıcıların dikkatinizden para kazanmaya çalıştığı yerde, LibreWolf tam tersini yapıyor: akıcı, modern bir tarama deneyimini korurken sizi izleyiciler için görünmez kılıyor.



Bu eğitimde, LibreWolf'un performans veya web uyumluluğundan ödün vermeden izlemeye karşı güçlü koruma sunarak web'de gezinme şeklinizi nasıl değiştirebileceğini keşfedeceğiz.



![LIBREWOLF](assets/fr/01.webp)


*Web tarayıcısı pazar payı: Chrome pazarın %65'ine hakimken, onu Safari ve Edge takip ediyor. Bu hakimiyet, web çeşitliliği ve gizlilikle ilgili soruları gündeme getiriyor*



## Karşınızda LibreWolf



**FreeWolf**, Mozilla Firefox'tan türetilmiş, özgür yazılım meraklılarından oluşan bağımsız bir topluluk tarafından geliştirilen ve sürdürülen açık kaynaklı bir web tarayıcısıdır. Temel amacı, kullanıcının gizliliğine, güvenliğine ve özgürlüğüne odaklanan bir tarama sunmaktır.



Somut olarak LibreWolf, Firefox'un Gecko motorunu kullanır, ancak tamamen farklı bir felsefeye sahiptir: Firefox'un gizlilik ve kullanım kolaylığı arasında denge kurması gerekirken, LibreWolf varsayılan olarak gizliliği tercih eder. Proje, gelişmiş güvenlik ayarlarını entegre ederken gizliliğinizi ihlal edebilecek her şeyi (telemetri, veri toplama, sponsorlu modüller) kaldırır.



### Hedefler: mahremiyet ve özgürlük



LibreWolf, tarayıcı güvenliğini artırırken izleme ve parmak izine karşı korumayı en üst düzeye çıkarmayı amaçlamaktadır. Ana hedefleri şunlardır:





- Firefox'ta tüm telemetri ve veri toplama işlemlerini ortadan kaldırın**
- Tescilli DRM modülleri gibi kullanıcı özgürlüğüne** aykırı işlevleri devre dışı bırakın
- Gizlilik/güvenlik ayarlarını** ve belirli yamaları en başından itibaren uygulayın
- Toplumsal kalkınma şeffaflığı ve ticari çıkarlardan bağımsızlığı** garanti eder



Kısacası, LibreWolf kendisini "gizlilik en önemli öncelik olsaydı Firefox nasıl olurdu" olarak sunuyor - ek yapılandırma gerektirmeden varsayılan olarak size saygı duyan bir tarayıcı.



### Ana Özellikler



LibreWolf en başından itibaren gizlilik odaklı bir dizi özellik sunuyor:



**Telemetri veya veri toplama yok:** Belirli kullanım istatistiklerini gönderen Chrome veya Firefox'un aksine, LibreWolf gezintinizden kesinlikle hiçbir şey toplamaz. Ne çökme raporları, ne kullanıcı araştırmaları, ne de sponsorlu öneriler.



**LibreWolf, piyasadaki en iyi reklam engelleyicilerden ve izleyicilerden biri olan uBlock Origin uzantısını yerel olarak entegre eder. Varsayılan olarak, LibreWolf sizi çevrimiçi olarak izleyebilecek her şeyi agresif bir şekilde filtreler (müdahaleci reklamlar, izleme komut dosyaları, kripto para birimi Mining).



**Varsayılan olarak özel arama motoru:** LibreWolf varsayılan olarak ilk arama motoru olarak DuckDuckGo'yu kullanır ve sorgularınızın geçmişini tutmaz. Diğer gizlilik odaklı alternatifler de (Searx, Qwant, Whoogle) mevcuttur.



**Güçlendirilmiş parmak izi koruması:** Parmak izi, bir tarayıcının çerezler olmadan bile yapılandırması aracılığıyla benzersiz bir şekilde tanımlanmasını sağlar. Buna karşı koymak için LibreWolf, tarayıcınızı mümkün olduğunca genel hale getirmek için Tor projesinden RFP (Resist Fingerprinting) teknolojisini etkinleştirir. Testler, standart bir Firefox'un coveryourtracks.eff.org gibi araçlarda ~%90 benzersiz olduğunu, buna karşılık LibreWolf için sadece ~%10-20 benzersiz olduğunu göstermektedir (bu rakamlar gösterge niteliğindedir ve yazılım ve donanım yapılandırmasına ve yüklü uzantılara göre değişebilir).



![LIBREWOLF](assets/fr/07.webp)


*TEST YOUR BROWSER düğmesi ile EFF test sayfası [Cover Your Tracks] (https://coveryourtracks.eff.org/). Bu sayfa, izleyicilere ve parmak izine karşı korumayı değerlendirmek için kullanılır



![LIBREWOLF](assets/fr/08.webp)


*İzlerinizi Örtün test sonucu. LibreWolf.* korumasının etkinliğini gösteren "Web takibine karşı güçlü bir korumanız var" mesajı görüntülenir



**LibreWolf varsayılan olarak sıkı güvenlik ayarlarını etkinleştirir. Firefox'un Gelişmiş İzleme Koruması, binlerce izleyiciyi, üçüncü taraf çerezlerini ve kötü amaçlı içeriği engellemek için Sıkı seviyeye getirilmiştir. Ayrıca her etki alanı için verileri bölümlere ayırmak üzere site ve çerez izolasyonunu (*Total Cookie Protection*) etkinleştirir ve IP Address sızıntısı riskini azaltmak için WebRTC'yi kısıtlar (*ICE adaylarını* sınırlandırır ve bir proxy mevcut olduğunda proxy üzerinden yönlendirme yapar).



**Hızlı motor güncellemeleri:** Proje Firefox gelişmelerini çok yakından takip etmektedir: LibreWolf her zaman Firefox'un en son kararlı sürümünü temel alır ve geliştiriciler her resmi Firefox sürümünden sonra 24 ila 72 saat içinde yeni bir sürüm yayınlamaya çalışırlar.



## Avantajlar ve dezavantajlar



### Avantajlar





- Telemetri veya istenmeyen bağlantılar yok:** LibreWolf hiçbir kullanım verisi iletmez, gizliliğinize tam saygı sağlar.





- Açık kaynaklı ve topluluk tabanlı:** Proje %100 açık kaynaklıdır ve gönüllüler tarafından sürdürülmektedir. Bu bağımsızlık, hiçbir reklam modelinin gelişimi etkilemeyeceğini garanti eder.





- Gizlilik için önceden yapılandırılmış:** LibreWolf size değerli zaman kazandırır: Firefox ayarlarını sertleştirmek için saatler harcamanıza gerek yok, her şey zaten yapıldı.





- Yerel reklam engelleyici/izleyici:** uBlock Origin standart olarak entegre edilmiştir, böylece kendinizi reklamlara ve hatalara karşı korumak için hiçbir şey yapmanıza gerek kalmaz.





- Mükemmel parmak izi koruması:** RFP ve çok sayıda gizlilik ayarı sayesinde LibreWolf, web üzerindeki benzersiz dijital ayak izinizi büyük ölçüde azaltır.





- Geliştirilmiş performans ve hafiflik:** Telemetri ve bazı gerekli olmayan özellikleri kaldırarak, LibreWolf standart Firefox'tan biraz daha hızlı ve daha az güç tüketebilir.



### Dezavantajlar ve sınırlamalar





- Yerleşik otomatik güncelleme yok:** LibreWolf kendini güncellemez. Güvende kalmak için yeni sürümleri yayınlanır yayınlanmaz yüklemek size bağlıdır.





- Belirli hizmetlerle daha az uyumluluk:** Çok katı ayarları nedeniyle, LibreWolf belirli web sitelerinde sorunlarla karşılaşabilir. LibreWolf varsayılan olarak Widevine DRM'yi devre dışı bıraktığı için Netflix ve Disney+ yayın platformları çalışmayacaktır.





- Yerleşik anonim ağ yok:** Tor Browser'ın aksine, LibreWolf trafiği Tor veya bir VPN üzerinden kendi başına yönlendirmez. Ağ anonimliğine ihtiyacınız varsa, bir proxy/VPN'i manuel olarak yapılandırmanız gerekir.





- Kalıcı olmayan çerezler ve oturumlar (varsayılan):** Gizlilik nedeniyle LibreWolf, tarayıcınızı her kapattığınızda çerezleri, geçmişi ve site verilerini siler. Her giriş yaptığınızda hesaplarınıza tekrar giriş yapmanız gerekecektir.





- Mobil sürüm veya bulut senkronizasyonu yok:** LibreWolf yalnızca masaüstünde (Windows, Linux, macOS) kullanılabilir. Mobil uygulama yoktur ve bu nedenle hesapların veya yer imlerinin bir bulut aracılığıyla senkronizasyonu yoktur.



## LibreWolf'u Yükleme



**Resmi web sitesi:** [librewolf.net](https://librewolf.net)



LibreWolf tüm büyük masaüstü işletim sistemleri için kullanılabilir: Linux, Windows ve macOS. LibreWolf'u indirmek için resmi web sitesini ziyaret edin:



![LIBREWOLF](assets/fr/02.webp)


*LibreWolf ana sayfası (librewolf.net) tarayıcı logosunu, mavi Yükle düğmesini, Kaynak Kodu ve Dokümantasyon bağlantılarını gösterir. Büyük mavi bir ok Yükle düğmesini işaret etmektedir*



İşletim sisteminizle ilgili ayrıntılı talimatlara erişmek için "Kurulum" düğmesine tıklayın:



![LIBREWOLF](assets/fr/03.webp)


*LibreWolf.* indirme için işletim sistemi seçim sayfası



Kurulum, işletim sisteminize bağlı olarak farklılık gösterir:



### Linux üzerinde


LibreWolf birçok dağıtım için derlemeler sunar. Debian/Ubuntu ve türevlerinde resmi bir APT deposu mevcuttur. Alternatif olarak, LibreWolf Flathub üzerinde Flatpak olarak yayınlanmaktadır:


```
flatpak install flathub io.gitlab.librewolf-community
```



### Windows üzerinde


Yükleyiciyi (.exe) resmi web sitesinden indirin veya:




- Chocolatey:** `choco install librewolf`
- WinGet:** `winget install librewolf`



### MacOS üzerinde


LibreWolf, Mac için bir .dmg paketi olarak mevcuttur. Disk görüntüsünü resmi web sitesinden indirin ve LibreWolf uygulamasını Uygulamalar klasörünüze sürükleyip bırakın. Alternatif olarak, Homebrew aracılığıyla da yükleyebilirsiniz.




## Yapılandırma ve ilk kullanım



İlk açılışta tanıdık Firefox Interface'yi fark edeceksiniz, ancak daha sadeleştirilmiş: ana sayfada yalnızca arama çubuğu var ve sponsorlu öneriler yok. Araç çubuğunda uBlock Origin simgesini göreceksiniz - engelleyicinin aktif olduğunu gösteren bir işaret.



![LIBREWOLF](assets/fr/04.webp)


*Uzantıları ve menüsüyle LibreWolf ana sayfası. Sağ üst köşedeki mavi ok menü simgesini gösterir (üç yatay çubuk)



LibreWolf sayfalarınızı otomatik olarak "katı" (izleme karşıtı) modda yükler ve varsayılan arama motoru DuckDuckGo olacaktır. Açığa çıkan ayak izini gözlemlemek için bir izleme test sitesini (örneğin amiunique.org) ziyaret etmeyi deneyebilirsiniz - standart bir tarayıcıdan çok daha genel olmalıdır.



### Gizlilik ayarları



LibreWolf zaten gizlilik için en iyi şekilde yapılandırılmıştır. Menü → Seçenekler → Gizlilik ve Güvenlik bölümünde LibreWolf'un Gelişmiş İzleme Koruması moduna ayarlandığını göreceksiniz: Sıkı. Bu mod engeller:




- Siteler arası izleyiciler
- Üçüncü taraf çerezleri
- Bilinen izleme içeriği
- Kriptomadencilik
- Dijital parmak izi dedektörleri



![LIBREWOLF](assets/fr/05.webp)


*LibreWolf.* güvenlik ayarlarını gösteren güvenlik ve gizlilik sekmesi sayfası



WebRTC devre dışıdır (IP sızıntılarını önler) ve Toplam Çerez Koruması yürürlüktedir. Telemetri ve Firefox anketleri tamamen devre dışı bırakılmıştır.



### Çerez ve geçmiş yönetimi



Varsayılan olarak, LibreWolf her kapandığında çerezleri ve yerel depolamayı siler. Bu davranış sizi rahatsız ediyorsa, Gizlilik ve Güvenlik → Çerezler ve site verileri bölümünde "LibreWolf'u kapatırken çerezleri ve site verilerini sil" seçeneğinin işaretini kaldırarak ayarlayabilirsiniz.



![LIBREWOLF](assets/fr/06.webp)


*Aynı sayfa biraz daha aşağıda, tarayıcı kapatıldığında çerezleri silme seçeneğini gösteriyor*



### Yararlı uzantılar ekleme



Prensip olarak, LibreWolf gereksiz uzantıların eklenmesini önermez, çünkü her uzantı bir izleme vektörü olabilir. Bununla birlikte, bazı saygın uzantılar deneyiminizi geliştirebilir:




- Bölümlere ayrılmış tarama için Firefox Multi-Account Containers** (Mozilla tarafından)
- Ortak kütüphanelere yerel olarak hizmet vermek için Decentraleyes** veya **LocalCDN**



Özellikle "ücretsiz VPN" uzantılarından veya şüpheli proxy'lerden kaçının - uBlock Origin zaten ihtiyaçlarınızın %99'unu karşılıyor.



## Günlük kullanım



### Günlük web taraması


Günlük İnternet aktiviteleriniz için LibreWolf kullanın. Diğer tarayıcılarla aranızdaki en büyük fark, çok daha az reklam izi bırakmanızdır. UBlock'un filtreleme listeleri sayesinde birçok sitede "çerez kabul et" banner'ları kaybolur.



### Bölümlere ayırmak için özel sekmeleri kullanın


LibreWolf oturumun sonunda her şeyi silse de, oturum sırasında belirli görevler için özel bir tarayıcı penceresi (Ctrl+Shift+P) açmak, belirli bir kimliği ayırmak için yararlı olabilir.



### Çoklu hesap konteynerlerinden yararlanın


Multi-Account Containers uzantısını yüklemek, faaliyetlerinizi su geçirmez silolara ayırmanıza büyük ölçüde yardımcı olabilir. Örneğin, bankacılık siteleriniz için bir "Bankacılık" konteyneri, Facebook/Twitter için bir "Sosyal Ağlar" konteyneri vb. tanımlayabilirsiniz. Her konteynerin kendi çerezleri, oturumları ve izole edilmiş depolama alanı vardır. Her konteynerin kendi çerezleri, oturumları ve izole edilmiş depolama alanı vardır.



### Siteye göre ince ayarlı izin yönetimi


LibreWolf, sitelere verdiğiniz izinleri (Konum, Kamera, Mikrofon, Bildirimler) duruma göre kontrol etmenizi sağlar. İzinleri yalnızca güvendiğiniz ve gerekli olan sitelere verin.



## LibreWolf ile en iyi uygulamalar



1. **LibreWolf'u güncel tutun:** Özellikle kararlı bir Firefox sürümünden sonra yeni sürümler için siteyi düzenli olarak kontrol edin.



2. **Kişisel kimlik ve özel taramayı karıştırmaktan kaçının:** İdeal olarak, hassas araştırma yaptığınız aynı oturumda kişisel hesaplarınızla oturum açmamalısınız.



3. **LibreWolf'u gereksiz uzantılarla aşırı yüklemeyin:** Yüklediğiniz her uzantı güvenlik veya parmak izi riskleri doğurabilir.



4. **Ek olarak bir VPN veya Tor proxy kullanın:** LibreWolf sizi İSS'nize karşı anonim yapmaz. Ağ anonimliği için LibreWolf'u güvenilir bir VPN'in arkasında kullanabilirsiniz.



5. **Önemli verilerinizi kaydedin:** Yer imleri, yerel olarak saklanıyorsa şifreler. Tarayıcının temel parola yöneticisi yerine harici bir parola yöneticisi (KeePassXC, Bitwarden) düşünün.



## Diğer tarayıcılarla karşılaştırma



LibreWolf, gizlilik odaklı tarayıcıların "araç kutusunun" bir parçasıdır:



**LibreWolf vs Firefox:** LibreWolf zaten güçlendirilmiş ve herhangi bir telemetri olmadan gelir. Firefox çoklu cihaz senkronizasyonu ve çok geniş bir kullanıcı tabanı avantajını korur, ancak LibreWolf'un gizlilik seviyesine ulaşmak için manuel yapılandırma gerektirir.



**Brave, Chrome/Chromium kodunu kullanır ve isteğe bağlı reklam programı aracılığıyla bir iş modelini entegre eder. Firefox için bir topluluk Fork olan LibreWolf, Mozilla'nın özgür ekosistemini korur ve Google ile hiçbir bağı yoktur.



**LibreWolf vs Tor Browser:** Tor Browser güçlü gözetim karşısında anonimlik için vazgeçilmezdir, ancak günlük kullanımda yavaş ve rahatsız edicidir. LibreWolf, klasik web'de günlük gezinme için çok daha hızlı ve pratiktir.



**LibreWolf vs Mullvad Browser:** Mullvad Browser standardizasyonda daha da ileri gidiyor, ancak kullanılabilirliğin azalması pahasına (giriş çerezini saklamak imkansız). LibreWolf bir denge kuruyor: çok özel, ancak günlük olarak kullanılabilir.



## Sonuç



LibreWolf, Tor'un aşırı anonimliğine kadar gitmeden ultra özel bir "günlük" tarayıcı arayanlar için mükemmel bir çözümü temsil ediyor. Aktivistler, gazeteciler, geliştiriciler veya reklam takibi ve Big Tech'ten kaçarken klasik web taraması (hızlı, modern sitelerle uyumlu) isteyen uzman kullanıcılar için ideal bir seçimdir.



Belirli sınırlamaları olmasına rağmen (otomatik güncelleme yok, belirli hizmetlerle uyumluluğu azalmış), LibreWolf dijital gizliliklerinin kontrolünü yeniden kazanmak isteyen herkesin cephaneliğinde değerli bir araçtır. Kullanım kolaylığı ve varsayılan yapılandırması onu gizlilik bilincine sahip kullanıcılar için akıllıca bir seçim haline getiriyor.



## Kaynaklar



### Resmi belgeler




- [LibreWolf resmi web sitesi](https://librewolf.net)
- [Codeberg'deki kaynak kodu](https://codeberg.org/librewolf)
- [Resmi SSS](https://librewolf.net/docs/faq)



### Kılavuzlar ve karşılaştırmalar




- [Gizlilik Kılavuzları](https://www.privacyguides.org/en/desktop-browsers/)
- [Karşılaştırmalı gizlilik testleri](https://privacytests.org)



### Toplum desteği




- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)