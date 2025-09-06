---
name: Firefox
description: Gizliliğinizi korumak için Firefox nasıl yapılandırılır?
---

![cover](assets/cover.webp)



## Giriş



Hepimiz internette saatler geçiriyoruz ve çoğu zaman tarayıcımızın hakkımızda neler ifşa ettiğini fark etmiyoruz. Her tıklama, her arama, ziyaret ettiğimiz her site devasa bir kişisel veri toplama endüstrisini besliyor.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Web tarayıcısı pazar payı: Chrome pazarın %65'ine hakimken onu Safari ve Edge takip ediyor. Kaynak: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Bu grafikte de görüldüğü gibi, Google Chrome dünya çapındaki kullanımın %65'inden fazlasıyla büyük bir hakimiyete sahip. Bu hegemonya, İnternet kullanıcılarının çoğunluğunun tarama verilerini, iş modeli hedefli reklamcılığa dayanan bir şirket olan Google'a emanet ettiği anlamına geliyor. Pazarın sadece %3'üne sahip olan Firefox, verilerinizi sömürmek gibi bir ticari çıkarı olmayan ve kar amacı gütmeyen bir kuruluş olan Mozilla tarafından geliştirilen bir alternatifi temsil etmektedir.



Ancak Firefox'u seçmek yalnızca ilk adımdır. Varsayılan olarak, Firefox bile korumanızı en üst düzeye çıkarmak için ayarlamalar gerektirir. Bu kılavuz sizi en basitinden en gelişmişine kadar adım adım yönlendirerek Firefox'u izlemeye karşı gerçek bir kalkana dönüştürürken keyifli bir tarama deneyimi yaşamanızı sağlar.



### Neden Firefox?





- Ücretsiz ve açık kaynak** (Gecko motoru): denetlenebilir, şeffaf kod
- Kâr amacı gütmeyen kuruluş**: Mozilla Vakfı, genel çıkar misyonu
- Yerleşik yerel korumalar**: Gelişmiş İzleme Koruması (ETP), Toplam Çerez Koruması (TCP), Durum Bölümleme, Yalnızca HTTPS modu, HTTPS üzerinden DNS (DoH)
- Gelişmiş özelleştirme**: Chrome'un aksine Firefox, davranışını derinlemesine değiştirmenize izin verir



### Başlamadan önce önemli ilkeler





- Evrensel bir reçete yok**: ne kadar çok değişiklik yaparsanız, o kadar çok göze çarpma riski (parmak izi) alırsınız. Amaç, kalabalığın arasından sıyrılmadan daha iyi korunmaktır.
- Adım adım ilerleme**: Bir ayarı değiştirin, her zamanki sitelerinizi test edin, sonra devam edin. Her şeyi bir kerede değiştirmenize gerek yok.
- Kişisel denge**: Gizlilik ve kullanım kolaylığı arasındaki uzlaşmanızı bulun.



## Hızlı kurulum



![Téléchargement Firefox](assets/fr/02.webp)



**Resmi indirme:** [firefox.com/browsers/desktop] (https://www.firefox.com/en-US/browsers/desktop/) adresine gidin. Bu sayfada, özel kurulum talimatlarını içeren uygun indirme sayfasına erişmek için işletim sisteminizi (Windows, macOS, Linux) seçin.





- Windows**: `.exe` yükleyicisini indirin, çift tıklayın ve kurulum sihirbazını izleyin
- macOS**: `.dmg` dosyasını indirin, açın ve Firefox'u Uygulamalar klasörüne sürükleyin
- Linux**: çeşitli seçenekler mevcuttur - paket `.deb`/`.rpm`, Flatpak (Flathub), Snap veya paket yöneticisi (apt, dnf, pacman) aracılığıyla. Resmi Mozilla kaynaklarını tercih edin.



**İpucu:** Yüklendikten sonra, Yardım → **Firefox Hakkında** aracılığıyla güncellemeleri kontrol edin (güvenlik yamaları için önemlidir).



![Configuration initiale Firefox](assets/fr/03.webp)


*Firefox'u başlatırken ilk ekran: Firefox'u varsayılan tarayıcınız olarak ayarlayın, kısayollarınıza ekleyin ve ardından "Kaydet ve devam et "e tıklayın



![Création compte Firefox](assets/fr/04.webp)


*İsteğe bağlı adım: bir Firefox hesabı oluşturun veya oturum açın. Sağ alttaki "Şimdi değil" seçeneğine tıklayarak bu adımı atlayabilirsiniz*



![Page d'accueil Firefox](assets/fr/05.webp)


*Yapılandırma tamamlandıktan sonra Firefox ana ekranı. Firefox'u özelleştirmek için Ayarlar ve Uzantılar'a erişim sağlayan sağ üstteki ☰ menüsüne dikkat edin*



## Korumalar varsayılan olarak zaten etkinleştirilmiştir (güven verici)





- Site izolasyonu (Fission)**: aşamalı dağıtımda. Bu özellik, kötü amaçlı bir sekmenin diğerinin verilerine erişmesini önlemek için her siteyi ayrı bir işlemde çalıştırır. Durumunu `about:support` üzerinden kontrol edin ("Fission" için arama yapın). Etkinleştirilmemişse, `fission.autostart = true` ile `about:config` içinde manuel olarak etkinleştirebilirsiniz.
- Toplam Çerez Koruması (TCP)**: varsayılan olarak etkin. Çerezler ve diğer depolama alanları, siteler arası izlemeyi etkisiz hale getiren birinci taraf siteyle (site başına bir "kavanoz") sınırlandırılır. Gerektiğinde Depolama Erişim API'si aracılığıyla geçici istisnalar yapılır (entegre giriş düğmeleri).
- Hemen Çıkma/Yönlendirme İzleme Koruması**: Firefox, sıçrama sitelerinin (sizi hedeften önce bir izleyici aracılığıyla yönlendiren bağlantılar) geride bıraktığı çerezleri otomatik olarak algılar ve temizler, böylece sizin herhangi bir işlem yapmanıza gerek kalmadan bu izleme kanalını azaltır.



## Seviye 1 - Temel (≤ 10 dakika)



Amaç: Web'i bozmadan büyük gizlilik kazanımları. Kullanıcıların %90'ı için.



Ayarlara erişmek için sağ üstteki menüye ☰ ve ardından **"Ayarlar "** öğesine tıklayın:



![Paramètres généraux](assets/fr/07.webp)


*Firefox ayarlar sayfası - "Genel" sekmesi. Gizlilik seçeneklerinizin çoğunu burada yapılandırırsınız*



**İzleme koruması (ETP)**




- ETP**'yi **Strict** olarak değiştirin. Daha fazla izleyiciyi engellersiniz (siteler arası çerezler, parmak izi, kriptomining, sosyal widget'lar...).
- Bir site bozulursa (video, giriş düğmesi...), 🛡️ kalkanı aracılığıyla yalnızca o site için korumayı devre dışı bırakın, ardından sekmeyi yenileyin.



İşte farklı ETP güvenlik seviyeleri:




- Standart** (dengeli, maksimum uyumluluk)
  - Engeller: sosyal izleyiciler, siteler arası çerezler (tüm pencereler), gizli taramada içerik izleme, kripto para madencileri, parmak izi dedektörleri.
  - Toplam Çerez Koruması** (TCP) içerir: site başına bir kavanoz.
- Strict** (gizlilik için önerilir)
  - Ayrıca tüm pencerelerdeki izleme içeriğini + bilinen ve şüphelenilen parmak izini engeller.
  - Bazı siteleri bozabilir; yerel bir istisna için 🛡️ kalkanını kullanın.
- Özel** (gelişmiş)
  - İnce ayar: çerezler, izleme içeriği, küçükler, parmak izi (bilinen/şüphelenilen).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Çerezler ve site verileri




- Her yeniden başlattığınızda temiz bir şekilde yeniden başlatmak için **"Kapanışta çerezleri ve site verilerini sil "** seçeneğini etkinleştirin.
- İsterseniz 2-3 temel site için **İstisnalar** ekleyin (e-posta, banka).


**Otomatik veri girişi, öneriler ve ana sayfa**




- Otomatik doldurmayı** devre dışı bırakın (kimlikler, adresler, kartlar). Bunun yerine bir şifre yöneticisi kullanın.
- Arama**: **"Arama önerilerini göster "** seçeneğini devre dışı bırakın.
- Address çubuğu**: **"Sponsorlu öneriler "** ve **"Bağlamsal öneriler "** öğelerini kesin.
- Home**: **Pocket** ve **sponsorlu içeriği** devre dışı bırakın.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**Sadece HTTPS**




- "HTTPS modunu yalnızca tüm pencerelerde "** etkinleştirin.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Telemetri ve reklam ölçümü




- "Firefox tarafından veri toplama" bölümünde **tümünün** işaretini kaldırın.
- "Gizlilik dostu reklam önlemlerini "** (PPA) devre dışı bırakın.
- Güvenli Tarama**: etkin tutun (önerilir). Firefox, karma sorgular ve yerel kontroller aracılığıyla siteleri tehdit listelerine karşı denetler, kimlik avı ve kötü amaçlı yazılımlara karşı minimum gizlilik etkisiyle koruma sağlar.



**Global Gizlilik Kontrolü (isteğe bağlı)**




- Verileri satmayı/paylaşmayı reddettiğinizi belirtmek için **GPC**'yi etkinleştirin.



**Arama motoru




- DuckDuckGo**, **Startpage**, **Qwant** veya **Brave Search** (Ayarlar → Arama) seçeneklerine geçin.



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Özel navigasyon**




- Tek seferlik oturumlar (hediyeler, ikincil hesaplar...) için özel pencereler (Ctrl/Cmd+Shift+P). "Her zaman özel" modundan kaçının: uzantılar etkin olmayabilir ve çerez istisnaları daha az kullanışlı olabilir.



**Temel uzantılar** (resmi katalogdan yükleyin)




- uBlock Origin**: reklamları ve güncel takibi engeller, hafiftir.
- Privacy Badger**: sizi takip edenleri engellemeyi öğrenir; Do Not Track / GPC gönderir.
- ClearURLs** (isteğe bağlı): Firefox (ETP Strict) ve uBO zaten birçok şeyi temizliyor; hala "kirli" URL'ler (utm, fbclid) görüyorsanız bunu saklayın.
- Firefox Çoklu Hesap Konteynerleri**: **Kapsayıcı başına çerezleri/oturumları ve depolamayı izole eder; paralel çoklu hesaplar; daha az siteler arası izleme**. Resmi uzantı: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**Şifreler ve 2FA**




- Özel bir parola yöneticisi** (Bitwarden, KeePassXC) kullanın. **Parolaları tarayıcıda saklamaktan** kaçının. **Mümkün olan her yerde 2FA'yı** etkinleştirin.



## Seviye 2 - Güçlendirilmiş (Bölümlendirme ve Ağ)



Amaç: faaliyetleri bölümlere ayırmak ve ağ sızıntısını azaltmak.



**HTTPS üzerinden DNS (DoH)**




- Varsayılan durum**: Bazı bölgelerde otomatik olarak etkinleştirilir (ABD, Kanada, Rusya, Ukrayna). Diğer yerlerde manuel aktivasyon gereklidir.
- Yapılandırma**: Ayarlar → Genel → Ağ ayarları → ** DoH'u etkinleştir** → **Cloudflare** veya **Quad9** → **Maksimum koruma**.
- Maksimum koruma = Yalnızca TRR** (sistem DNS'sine geri dönüş yok). Bir şirket/otel ağı engellerse, **Standart** seçeneğine geri dönün veya DoH'yi devre dışı bırakın.
- Yedeklilik**: Zaten kendi güvenli DNS'sine sahip güvenilir bir VPN kullanıyorsanız, DoH gereksiz olabilir.
- Doğrulama testi**: `https://www.dnsleaktest.com/` yalnızca seçilen DoH sağlayıcısını görüntülemelidir.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Konteynerler ve profillerle bölümlere ayırma




- Çoklu Hesap Konteynerleri**: alanlar oluşturun (Kişisel, İş, Finans, Sosyal Ağlar, Alışveriş, Tek Kullanımlık). Yinelenen siteleriniz için **"Her zaman bu kapsayıcıda aç "** seçeneğini yapılandırın. Resmi uzantı: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Neden kullanıyorsunuz?
  - Çerezlerin/oturumların/depolamanın alana göre güçlü izolasyonu**.
  - Daha az siteler arası izleme**: devleri (Facebook, Google) sınırlandırın.
  - Aynı hizmet üzerinde eş zamanlı çoklu hesaplar**.
  - Bölümlere ayrılmış kimlikler arasında daha az CSRF/XSS** riski.
  - İpucu: En azından Sosyal Ağlar/Google, İş, Finans için özel konteynerler.
- Facebook Container** (isteğe bağlı): FB/Instagram'a adanmış basitleştirilmiş bir versiyon.
- Ayrı profiller**: `about:profiles` aracılığıyla (ana profil, minimal "ultra güvenli" profil, test profili). Toplam veri ve uzantı bölümlendirmesi.



**Gelişmiş uzantılar** (ayrılacak)




- Cookie AutoDelete**: sekme kapatılır kapatılmaz bir sitenin çerezlerini siler (Firefox uzun süre açık kaldığında kullanışlıdır).
- LocalCDN**: mevcut kütüphaneleri yerel olarak sunar (Google/Microsoft'a yapılan çağrıları azaltır). Kısmi uyumluluk.



**Mobil (Android)**




- Firefox Android + uBlock Origin**: hareket halindeyken benzer koruma.



## Seviye 3 - Uzman (about:config & Arkenfox)



Amaç: kabul edilen ödünlerle gelişmiş sertleştirme. Ayrı bir profilde** önerilir.



Aşağıdaki iki yaklaşımdan yalnızca birini seçin:



**Yaklaşım A - Manuel değişiklikler**: About:config` aracılığıyla birkaç hedefli ayarlama (daha basit, daha hassas kontrol)


**Yaklaşım B - Arkenfox user.js**: Tam otomatik yapılandırma (daha karmaşık, maksimum koruma)



➡️ **Arkenfox zaten aşağıda belirtilen TÜM about:config değişikliklerini** + yüzlerce daha fazlasını içerir. Eğer Arkenfox'u seçerseniz, about:config bölümünü görmezden gelin.



### Yaklaşım A: about:config aracılığıyla manuel değişiklikler



Address çubuğuna `about:config` yazın → Riski kabul edin.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Parmak izine karşı direnç (Tor Browser'dan miras alınmıştır)


```text
privacy.resistFingerprinting = true
```


Etkiler: UTC zaman dilimi, **letterboxing** (standart pencere boyutları), standartlaştırılmış User-Agent/politikalar, Canvas/WebGL/AudioContext kısıtlamaları. Daha fazla tekdüzelik, ancak birkaç "tuhaflık" (ofset zaman, bazen biraz İngilizce).





- WebRTC'yi devre dışı bırakın (IP sızıntılarını önler; Web visio'yu bozar)


```text
media.peerconnection.enabled = false
```





- Referer artı uyumlu (varsayılan)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Katı seçenek (ödemeleri/SSO'yu bozabilir):


```text
network.http.referer.XOriginPolicy = 2
```





- Geveze API'lerin ve spekülasyonların sınırlandırılması


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



Altın kural: Bir şey bozulursa, son değişikliğe geri dönün.



### Yaklaşım B: Arkenfox user.js (Tamamen otomatik yapılandırma)



Arkenfox** projesi, gizlilik ve güvenlik odaklı yüzlerce Firefox tercihini otomatik olarak uygulayan, topluluk tarafından tutulan bir `user.js` dosyası sağlar. Firefox yeniden başlatıldığında bu dosyayı profilinizden okur ve bu ayarları uygular.





- Amaç nedir? "Her yere tıklamadan" **tutarlı ve sağlamlaştırılmış bir temelden** başlayın; gözden kaçırmaları azaltın; zamandan tasarruf edin.
- Neleri değiştirir (örnekler): telemetri kesildi, çerezler/önbellek/referrer/HTTPS güçlendirildi, **RFP** + letterboxing, **WebRTC devre dışı bırakıldı**, DoH/TLS ayarlamaları, sohbet API'leri sınırlandırıldı.
- Ne zaman kullanılmalı: Firefox'un 10 dakika içinde sertleştirilmesini istiyorsanız ve birkaç istisnayı kabul ediyorsanız (DRM/streaming, Web visio, SSO/payments).
- Avantajları: hızlı, tutarlı, **güncellenmiş** (ESR uyumlu), çok iyi **belgelenmiş** (wiki + yorumlar), geçersiz kılmalar yoluyla **özelleştirilebilir**.
- Sınırlamalar: uyumluluk (bazı web uygulamaları), rahatlık (UTC, pencere boyutları) ve bir hatırlatma: **Bu Tor değil** (ağ anonimliği yok).



Kurulum (ideal olarak **özel bir profil** üzerinde)


1. Profili/favorileri kaydedin ve çerez istisnaları olan sitelerinizi listeleyin.


2. Kullanıcı.js` dosyasını `https://github.com/arkenfox/user.js` adresinden indirin (ESR/kararlı sürüm).


3. Profil klasörünüzü `about:profiles` üzerinden bulun:




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`


4. Firefox'u kapatın ve `user.js` dosyasını profil klasörünün kök dizinine taşıyın.


5. Yeniden başlatın; `about:config` veya bir geçersiz kılma dosyası aracılığıyla özelleştirin.



Güncellemeler




- Arkenfox sürümlerini (ESR uyumlu) takip edin, `user.js` dosyasını değiştirin, Firefox'u yeniden başlatın; sürüm notlarını okuyun.



**Geçersiz Kılmalarla Özelleştirme**



Arkenfox varsayılan olarak kasıtlı olarak kısıtlayıcıdır. Belirli ayarları ihtiyaçlarınıza göre uyarlamak için (akış, visio, belirli siteler), `user.js` ile aynı klasörde bir `user-overrides.js` dosyası oluşturabilirsiniz. Bu dosya, ana dosyayı değiştirmeden belirli Arkenfox tercihlerini "geçersiz kılmanıza" olanak tanır.



User-overrides.js` dosyasını oluşturun ve özelleştirmelerinizi ekleyin:


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



En iyi uygulamalar




- Ayrı bir **"Arkenfox" profili** kullanın ve rahatlık için "normal" bir profil bulundurun.
- Saldırı yüzeyini ve benzersizliği sınırlamak için uzantıları en aza indirin (uBlock Origin OK).
- Gerektiğinde site bazında istisnalar ekleyin (kalkan 🛡️, uBO, kullanılıyorsa NoScript).
- Her değişiklikten sonra test edin: WebRTC/DNS sızıntıları, İzlerinizi Örtün, CreepJS.



## En iyi uygulamalar





- Güncellemeler**: Firefox ve uzantıları güncel.
- Uzatmalar**: makul ve güvenilir; "şüpheli" itfalara dikkat edin.
- İndirmeler**: Dikkat; hassas dosyaları VirusTotal'da test edin.
- Şifreler**: **özel yönetici** (Bitwarden, KeePassXC); **2FA** etkin; tarayıcıda saklamaktan kaçının.
- Hijyen**: Google/Facebook'u konteynerlerle sınırlandırın; bağlamı "sıfırlamak" için düzenli olarak kapatın/açın.



## Sınırlar ve Alternatifler





- Sertleştirilmiş bir tarayıcı ≠ ağ anonimliği: **VPN** olmadan IP'niz görünür kalır; onunla bile korelasyon mümkün olmaya devam eder.
- Çok fazla değişiklik yapmak sizi **eşsiz** kılabilir. **RFP** standartlaştırır; randomizasyon araçları (örneğin Chameleon) sizi farklı kılabilir. Test edin, karşılaştırın, ayarlayın.
- Alternatifler/tamamlayıcılar:
 - Tor Browser: Tor üzerinden ağ anonimliği; daha yavaş. Tam kurulum ve yapılandırma kılavuzumuza bakın**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Mullvad Tarayıcı: vPN ile birleştirilecek "Tor'suz Tor"; standartlaştırılmış ayak izi. Özel eğitimimizde nasıl kurulacağını öğrenin**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Önerilen kombinasyonlar: Günlük kullanım için Firefox (Seviye 2) + VPN; hassas faaliyetler için Tor/Mullvad; bölümlere ayırma için ayrı profiller.



## Sonuç



Bu adım adım kılavuzu takip ederek Firefox'u dijital gözetime karşı gerçek bir sipere dönüştürdünüz. Temel Seviye 1 ayarlarından gelişmiş Arkenfox yapılandırmalarına kadar her değişiklik, tarama deneyiminizden ödün vermeden gizliliğinizi güçlendirir.



**Gizliliğiniz artık daha iyi korunuyor**: reklam izleyiciler engellendi, çerezler bölümlere ayrıldı, IP Address sızıntıları etkisiz hale getirildi, telemetri devre dışı bırakıldı. Firefox artık sadece bir tarayıcı değil, ihtiyaçlarınıza göre uyarlanmış bir dijital direnç aracıdır.



**Unutmayın: gizlilik hiçbir zaman kesin değildir. Korumanızı düzenli olarak test edin, ayarlarınızı güncelleyin ve alışkanlıklarınız değiştikçe yapılandırmanızı ayarlamaktan çekinmeyin. Çevrimiçi anonimliğiniz, uygulamalarınız kadar araçlarınıza da bağlıdır.



## Kaynaklar



### Plan ₿ Network




- SCU 202 - Kişisel dijital güvenliğinizi artırma: Bu eğitimde ele alınan dijital güvenlik kavramları hakkında daha fazla bilgi edinmek için**



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Mozilla belgeleri




- [Gelişmiş Takip Koruması](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Gelişmiş izleme koruması için resmi kılavuz
- [Durum Bölümleme] (https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Durum bölümleme hakkında teknik dokümantasyon
- [MDN Web Güvenliği](https://developer.mozilla.org/docs/Web/Security): Web güvenliği hakkında eksiksiz referans



### Arkenfox




- [Wiki ve kurulum kılavuzu](https://github.com/arkenfox/user.js/wiki): Arkenfox proje belgelerinin tamamı
- [Depozito ve sürümler](https://github.com/arkenfox/user.js): User.js dosyasını indirin ve güncellemeleri takip edin



### Rehberler & Topluluklar




- [PrivacyGuides - Masaüstü tarayıcılar](https://www.privacyguides.org/en/desktop-browsers/): Tarayıcı önerileri ve karşılaştırmaları
- Reddit**: r/firefox, geri bildirim ve destek için r/privacy
- PrivacyGuides forumu**: derinlemesine teknik tartışmalar



### Test araçları




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/): Dijital parmak izi ve izleme karşıtı etkinlik
- [DNS Sızıntı Testi](https://www.dnsleaktest.com/): DNS sızıntı testi ve DoH verimliliği
- [BrowserLeaks](https://browserleaks.com/): Eksiksiz test paketi (WebRTC, Canvas, Yazı Tipleri, vb.)
- [BadSSL](https://badssl.com/): SSL/TLS sertifika doğrulama testleri
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): 50'den fazla parmak izi vektörünün gelişmiş analizi
- [Cloudflare DNS Testi](https://1.1.1.1/help): Cloudflare DoH'un düzgün çalışıp çalışmadığını kontrol etme
