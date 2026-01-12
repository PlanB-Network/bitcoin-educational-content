---
name: Miras planı Bitcoin
description: Sevdiklerinize bitcoin nasıl transfer edilir
---

![cover](assets/cover.webp)



Bitcoinlerin iletimi, birçok sahibinin göz ardı ettiği büyük bir teknik zorluğu temsil etmektedir. Bir finans kurumunun fonları gerçek sahiplerine havale edebildiği geleneksel bankacılık varlıklarının aksine, Bitcoin aracılar olmadan çalışır. Sevdikleriniz, yasal meşruiyetleri ne olursa olsun, gerekli teknik bilgiler olmadan fonlarınıza asla erişemeyecektir.



Bu eğitim, teknik bir miras planının oluşturulmasında size rehberlik eder. Otomatik aktarım için on-chain mekanizmalarının nasıl çalıştığını, yapılandırmalarınızı nasıl belgeleyeceğinizi ve Bitcoin mirasınızın sevdikleriniz için erişilebilir kalmasını sağlamak için doğru çözümleri nasıl seçeceğinizi öğreneceksiniz.



## Teknik miras planı neden gereklidir?



Bitcoin temel bir kriptografik ilkeye dayanmaktadır: özel anahtarları elinde bulunduran kişi fonları kontrol eder. Bu egemenlik, sahibi gerekli bilgileri iletmeden ortadan kaybolduğunda büyük bir güvenlik açığı haline gelir.



Bir Bitcoin miras planı, görünüşte çelişkili olan iki hedefi karşılamalıdır: sevdiklerinizin zamanı geldiğinde fonlarınıza erişmesine izin verirken, başkalarının bunlara erken erişmesini önlemek. Bu hassas denge, Bitcoin'in yerel programlama yeteneklerine dayanır.



Teknik karmaşıklık ekstra bir zorluk katmanı ekler. Mirasçılarınızın kurtarma ifadeleri, portföy tanımlayıcıları veya türetme yolları gibi kavramları manipüle etmesi gerekecektir. Yeterli hazırlık yapılmazsa, iyi niyetli bir mirasçı bile geri dönüşü olmayan hatalar yapma riski taşır.



## on-chain kalıtımı nasıl çalışır?



Bitcoin, harcama koşullarını doğrudan işlemlerde kodlamak için komut dosyası dilini kullanır. on-chain kalıtımı, otomatik olarak etkinleşen alternatif kurtarma yolları oluşturmak için bu programlanabilirlikten yararlanır.



### Zaman Kilitleri



Zaman kilitleri Bitcoin kalıtımının temel mekanizmasıdır. Bir zaman koşulu karşılanana kadar fonların kilitlenmesini sağlarlar.



**CLTV (CheckLockTimeVerify)**: Bu mutlak zaman kilidi, harcamayı yetkilendirmeden önce belirli bir zamana (tarih veya blok yüksekliği) ulaşılıp ulaşılmadığını kontrol eder. Örneğin, "bu fonlar yalnızca blok 900000'den sonra harcanabilir" veya "1 Ocak 2026'dan sonra". CLTV'nin avantajı uzun gecikmelere (birkaç yıl) izin vermesidir, ancak tarih sabittir ve portföydeki tüm UTXO'lar için aynı şekilde geçerlidir. Fonlarınızın kontrolünü sürdürmek için, periyodik olarak uzatılmış bir son kullanma tarihine sahip yeni bir portföy oluşturmalı ve fonlarınızı buna aktarmalısınız.



**CSV (CheckSequenceVerify)**: Bu göreceli zaman kilidi, UTXO'un oluşturulmasından bu yana belirli sayıda blok geçtiğini doğrular. Örneğin, "bu fonlar alındıktan sonra sadece 52560 blok (~1 yıl) harcanabilir". CSV'nin avantajı, her UTXO'un kendi bağımsız sayacına sahip olmasıdır. Her işlem yaptığınızda, yeni oluşturulan UTXO'lar kendi zaman sınırlarını sıfırlar. Bununla birlikte, 65535 blokluk teknik sınır (~15 ay maksimum) olası zaman dilimlerini kısıtlar. Bu yaklaşım günlük kullanım için daha doğaldır, çünkü normal aktiviteniz otomatik olarak son tarihleri geri çeker.



### Çoklu harcama yolları



Bir miras portföyü, her bir adreste çeşitli harcama yollarını birleştirir:





- Ana yol** : Sahip, fonlarını istediği zaman ana anahtarıyla zaman kısıtlaması olmaksızın harcayabilir.
- Kurtarma yolu(ları)**: Bir veya daha fazla alternatif anahtar ancak belirli bir süre geçtikten sonra fon harcayabilir.



Sahip tarafından gerçekleştirilen her işlem UTXO'i "yeniler" ve sıfırlama zaman kilitleriyle yeni çıkışlar oluşturur. Bu mekanizma, sahip aktif kaldığı sürece kurtarma yollarının asla etkinleşmemesini sağlar.



### Miniscript ve Taproot



**Miniscript** Andrew Poelstra, Pieter Wuille ve Sanket Kanjalkar tarafından geliştirilen ve karmaşık Bitcoin komut dosyalarının yazılmasını ve analiz edilmesini kolaylaştıran yapılandırılmış bir dildir. Birden fazla anahtar ve zaman kilidi içeren miras yapılandırmaları için gerekli olan okunabilir ve doğrulanabilir harcama koşulları oluşturmanıza olanak tanır.



**Taproot** (Kasım 2021'de etkinleştirildi) on-chain mirasını önemli ölçüde geliştirir. Ağaç yapısı (MAST) sayesinde, blok zincirinde yalnızca kullanılan harcama koşulu ortaya çıkar. Mal sahibi fonlarını normal şekilde harcarsa, miras koşulları görünmez kalır. Bu gizlilik, karmaşık yollar için işlem maliyetlerini de azaltır.



## Tanımlayıcıların kritik önemi



Eski portföyler için, kurtarma ifadesi (seed) fonlara erişimi yeniden sağlamak için yeterli değildir. Tanımlayıcı** kritik unsur haline gelir.



Tanımlayıcı, bir portföyün yapısını kapsamlı bir şekilde açıklayan bir dizedir: ilgili açık anahtarlar, harcama koşulları, türetme yolları ve yapılandırılmış zaman kilitleri. İşte basitleştirilmiş bir örnek:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Bu tanımlayıcı şöyle der: "ya ana anahtar hemen harcanabilir ya da kurtarma anahtarı 52560 blok sonra harcanabilir".



Bu örneği biraz açalım:




- wsh()` : Witness Script Hash, adres türünü belirtir (P2WSH)
- or_d()`: varsayılan bir dal ile "veya" koşulu
- pk([fingerprint/path]xpub...)`: Parmak izi ve türetme yolu ile birlikte ana açık anahtar
- and_v()`: kurtarma anahtarını zaman kilidi ile birleştiren "and" koşulu
- `older(52560)`: 52560 bloğun göreli zaman kilidi



**Tanımlayıcı olmadan, tüm kurtarma ifadelerine rağmen mirasçılarınız portföyü yeniden oluşturamaz.** Standart bir portföy yalnızca seed'den geri yüklenebilir çünkü standartlaştırılmış türetme yollarını (BIP44, BIP84) izler. Öte yandan eski bir portföy, tahmin edilemeyen özelleştirilmiş komut dosyaları kullanır. Tanımlayıcı yedeği (veya yazılımınız tarafından dışa aktarılan yapılandırma dosyası) miras planınızdaki kurtarma ifadelerine eşlik etmelidir.



## Miras planının belgesel bileşenleri



Teknik mekanizmaların ötesinde, etkili bir miras planı üç temel dokümantasyona dayanır.



### Miras mektubu



Bu kişisel mektup planınıza giriş noktasıdır. Mirasçılarınız için yazılmış olan bu mektup, planınızın içeriğini ve alınacak önlemleri açıklar.



Mektubunuz açık güvenlik kurallarını içermelidir:




- Acele etmeyin, fonları taşımadan önce öğrenmek için zaman ayırın
- Asla tek bir kişiye tam bir kurtarma ifadesi iletmeyin
- Doğrulanmamış bir yazılım programına veya bilgisayara asla bir kurtarma ifadesi girmeyin
- Dolandırıcılıklara ve istenmeyen yardım teklif eden kişilere karşı dikkatli olun
- Herhangi bir karar vermeden önce güvendiğiniz en az iki kişinin tavsiyesini alın



Bu mektup aynı zamanda noterinizin iletişim bilgilerini ve vasiyetnamenizin yerini de içerir. Asla kurtarma cümleleri veya şifreler içermemelidir.



### Güvenilir kişiler rehberi



Hiçbir mirasçı bitcoin kurtarma işlemiyle tek başına yüzleşmemelidir. Bu dizin, teknik veya hukuki yardım sağlayabilecek kişileri listeler.



Her bir kişi için şunları belgeleyin: tam adı, sizinle olan ilişkisi, plandaki rolü, güven düzeyi, Bitcoin becerileri ve tam iletişim bilgileri. Temel kural: mirasçılarınız önemli bir karar vermeden önce her zaman en az iki farklı kişiye danışmalıdır.



### Bitcoin varlık envanteri



Bu bölüm, tüm bitcoinlerinizi kurtarmak için gereken teknik bilgilerle eşleştirir.



Her bir portföy için belge :




- Portföy türü**: donanım, yazılım, yapılandırma (single-sig, multisig, legacy)
- Cihaz konumu**: wallet donanımının fiziksel konumu
- Descriptor/konfigürasyon dosyası konumu**: gelişmiş portföyler için kritik
- Kurtarma ifadesinin yeri**: tanımlayıcıdan ayrı
- Erişim kodları**: PIN'lerin ve parolaların saklandığı yer
- Yapılandırılmış gecikmeler**: kurtarma yolları etkinleştirildiğinde



## Teknik çözümler mevcut



Çeşitli yazılım paketleri on-chain kalıtım mekanizmalarını uygulamaktadır. Her birinin kendine has teknik özellikleri vardır.



### Liana



Liana, zamanlanmış kurtarma yolları ile portföyler oluşturmak için Miniscript kullanan bir masaüstü yazılımıdır (Linux, macOS, Windows). Proje, Antoine Poinsot (Bitcoin Çekirdek katılımcısı) tarafından kurulan Wizardsardine tarafından geliştirilmiştir.



**Teknik mimari**: Liana varsayılan olarak P2WSH portföyleri (SegWit yerel) oluşturur, wallet donanımınızın uyumluluğuna bağlı olarak Taproot desteği mevcuttur. Mimari, bir ana yola ve bir veya daha fazla kurtarma yoluna dayanmaktadır. Oluşturulan tanımlayıcı tüm koşulları kodlar ve kaydedilmelidir.



**Kullanılan zaman kilitleri**: Liana, 65535 blok (~15 ay) ile sınırlı göreli zaman kilitleri (CSV) kullanır. Kontrolü sürdürmek için, zaman kilidinin süresi dolmadan önce bir yenileme işlemi gerçekleştirmelisiniz.



**Donanım wallet entegrasyonu**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY ve diğer cihazlar imzalama işlemleri için uyumludur.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper, "Geliştirilmiş Kasalar" aracılığıyla multisig ve zaman kilitlerini birleştiren bir mobil uygulamadır (iOS, Android). Entegre rehberlik ile mobil yaklaşım, daha az teknik kullanıcılar için erişilebilir olmasını sağlar.



**Teknik mimari**: Geliştirilmiş Kasalar, tanımlanan gecikmelerden sonra ek anahtarların etkinleştirildiği çoklu anahtar yapılandırmaları oluşturmak için Miniscript kullanır. Miras Anahtarı mevcut çekirdeğe eklenirken, Acil Durum Anahtarı multisig'i tamamen atlayabilir.



**Kullanılan zaman kilitleri**: Bitcoin Keeper, 15 ayı aşan teslim sürelerine izin veren mutlak zaman kilitleri (CLTV) kullanır. Aktivasyon tarihi wallet oluşturulurken belirlenir ve tüm UTXO'lar için geçerlidir. Uygulama, yenilemeyi otomatik olarak yöneten bir "yenileme" işlevi içerir: kullanıcı, manuel olarak yeni bir wallet oluşturmak zorunda kalmadan sadece yönlendirilen adımları izler.



**Ek özellikler**: Entegre miras belgeleri, anahtar tehlikesini tespit etmek için Kanarya Cüzdanları ve yenileme hatırlatıcıları.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Miras



Heritage, miras koşullarını kodlamak için Taproot komut dosyalarını kullanan bir masaüstü uygulamasıdır. Taproot kullanımı, kullanılmayan yollar blok zincirinde görünmez kaldığı için gelişmiş gizlilik sunar.



**Teknik mimari**: Her Miras adresi, aşamalı zaman dilimleri ile her mirasçı için bir ana yol ve alternatif yollar içerir. Hiyerarşik yapı, 6 ayda bir kişisel yedekleme ve 12-15 ayda bir aile mirasçıları tanımlamayı mümkün kılar.



**Kullanım şekilleri**: Kendi düğümünüzle bağımsız sürüm (ücretsiz) veya mirasçılara hatırlatıcılar ve bildirimler ekleyen yönetilen hizmet (%0,05/yıl).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Mirasçının iyileşme süreci



Kurtarma sürecinin anlaşılması etkili bir plan hazırlanmasına yardımcı olur. İşte bir mirasçının izlemesi gereken teknik adımlar.



### Kurtarma gereksinimleri



Varisin ihtiyacı var:


1. **Orijinal portföyün tanımlayıcısı veya yapılandırma dosyası** (yazılıma bağlı olarak JSON veya metin formatı)


2. **Kurtarma ifadesi** (miras anahtarı ile ilişkili olan, genellikle 12 veya 24 kelime)


3. **Uyumlu yazılım** (standart tanımlayıcılar için Liana, Bitcoin Keeper, Heritage veya Sparrow/Specter)


4. **Zaman kilidi durumunu kontrol etmek ve işlemi yayınlamak için bir Bitcoin** düğümüne bağlantı



### Kurtarma adımları



1. **Yazılımı** güvenli bir cihaza yükleyin ve Bitcoin ağına (kişisel düğüm veya Electrum sunucusu) bağlantıyı yapılandırın


2. *portföy yapısını yeniden oluşturmak için *Tanımlayıcıyı içe aktarın**. Yazılım otomatik olarak kullanılan tüm adresleri generate


3. *kurtarma ifadesinden *Devralma anahtarını** geri yükle. Yazılım, bu anahtarın tanımlayıcıda yetkilendirilen anahtarlardan birine karşılık gelip gelmediğini kontrol edecektir


4. *tüm UTXO'ları ve harcama koşullarını keşfetmek için *Portföyü senkronize edin**


5. **Zaman kilidi süresinin dolup dolmadığını kontrol edin**: yazılım her bir UTXO için kurtarma yolunun aktif olup olmadığını gösterecektir


6. **Kurtarma işlemini** yalnızca varis tarafından kontrol edilen bir adrese oluşturun (ideal olarak yeni bir tek wallet)


7. **Bitcoin ağında işlemi imzalayın ve yayınlayın**



Zaman kilidinin süresi henüz dolmamışsa varisin beklemesi gerekecektir. Yazılım, kurtarmanın mümkün olduğu tarihi veya bloğu gösterecektir. Bu bekleme süresi boyunca fonlar blok zincirinde güvende kalır.



### Varis için dikkat edilmesi gereken noktalar



Mirasçı aşağıdakilere özellikle dikkat etmelidir:




- İndirilen yazılımın orijinalliğini kontrol edin** (sağlama toplamları, imzalar)
- İyileşme ifadenizi** asla yardım teklif eden biriyle paylaşmayın
- Kurtarma işlemini gerçekleştirmeden önce güvendiğiniz en az iki kişiye** danışın
- Fonları iyileştikten sonra tamamen kendisinin kontrol edeceği basit bir portföye** aktarın



## En iyi uygulamalar



### Bilgi ayrımı



Asla tüm bilgileri tek bir yerde saklamayın. Tanımlayıcı, kurtarma ifadelerinden ayrılmalı ve bunlar da PIN kodlarından ayrılmalıdır. Bu dağılım bir saldırganın erişimini zorlaştırırken meşru varisleriniz tarafından yeniden oluşturulabilir.



### Kurtarma testleri



Önemli miktarda para yatırmadan önce, tüm kurtarma sürecini küçük bir miktarla test edin. Portföyü boş bir cihazdaki tanımlayıcıdan ve kurtarma ifadelerinden geri yükleyebildiğinizi doğrulayın. Mirasçılarınız için adımları belgeleyin.



### Zaman kilidi bakımı



Zaman kilitlerinizi süreleri dolmadan çok önce yenilemeyi planlayın. 12 aylık bir zaman kilidi için her 9-10 ayda bir işlem gerçekleştirin. Yazılım genellikle hatırlatıcılar veya otomatik yenileme işlevleri sunar.



### Plan güncellemesi



Bitcoin yapılandırmanız gelişir. Her önemli değişiklik (yeni portföy, son tarihlerin değiştirilmesi, varis eklenmesi) belgelerinize yansıtılmalıdır. Yıllık bir gözden geçirme rutini oluşturun.



## Yaklaşımınızı seçme



Farklı çözümler arasındaki seçim, teknik profilinize ve özel ihtiyaçlarınıza bağlıdır.



**Liana**, kendi düğümleri üzerinden tam kontrol ile açık kaynaklı yazılımı tercih eden masaüstü kullanıcıları için uygundur. Kılavuzlu arayüz sayesinde yapılandırma erişilebilir kalır. Göreceli zaman çizelgeleri (CSV), normal aktiviteniz son teslim tarihlerini otomatik olarak geri çektiğinden bakımı kolaylaştırır. Sınırlama: yaklaşık 15 aylık maksimum gecikme (65535 blok).



**Bitcoin Keeper**, entegre eşlik eden belgelerle sezgisel bir arayüz arayan mobil kullanıcıları hedeflemektedir. Uygulama iki tür özel anahtar sunmaktadır: Miras Anahtarı (nisaba eklenir) ve Acil Durum Anahtarı (nisabı tamamen atlar). Mutlak zaman kilitleri (CLTV), yenilemeyi basitleştiren entegre bir yeniden tonozlama işlevi ile 15 ayı aşan teslim sürelerine izin verir. Diamond Hands planı gelişmiş eski özelliklerin kilidini açar.



**Kalıtım**, Taproot gizliliğini ve aşamalı gecikmelerle hiyerarşik kalıtımı takdir eden teknik kullanıcılara yöneliktir. Taproot ağaç yapısı, normal işlemler sırasında kalıtım koşullarını gizler ve yalnızca kurtarma sırasında kullanılan koşulu ortaya çıkarır.



Her üç çözümün de ortak bir noktası vardır: kurtarma yollarının erken etkinleştirilmesini önlemek için periyodik yenileme gerektirirler. Bu kısıtlama, on-chain'nın güvenilmeyen mirasının hem bedeli hem de garantisidir. Düzenli hatırlatıcılar planlayın ve bu bakımı Bitcoin yönetim rutininizin bir parçası haline getirin.



## Sonuç



Teknik bir Bitcoin eski planı, kriptografik mekanizmaları (zaman kilitleri, Miniscript, Taproot) titiz dokümantasyonla birleştirir. Gelişmiş cüzdanlar, bitcoinlerinizi üçüncü taraf müdahalesi olmadan bir süre kullanılmadığında otomatik olarak iletmenizi sağlar.



Varislerinize aktarmanız gereken kritik unsurlar şunlardır: tanımlayıcı veya yapılandırma dosyası, kurtarma ifadeleri, ayrıntılı kurtarma talimatları ve onlara yardımcı olabilecek yetkili kişilerin iletişim bilgileri.



Profilinize uygun bir teknik çözüm seçerek başlayın, küçük bir miktarla test edin, ardından bütünü yapılandırılmış bir planla belgeleyin. Başlangıçtaki karmaşıklık, Bitcoin varlıklarınızın tam bir güven içinde aktarılacağını garanti eder.



## Kaynaklar



### Miras planı şablonu





- [Bitcoin Miras Planı Şablonu (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Plan ₿ Academy Dokümantasyon Şablonu



### Teknik referanslar





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Mutlak zaman saatlerinin belirlenmesi (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Göreceli zaman saatlerinin belirtilmesi (CSV)
- [Miniscript Reference](https://bitcoin.sipa.be/miniscript/) - Pieter Wuille tarafından hazırlanan resmi Miniscript dokümantasyonu



### Resmi çözüm web siteleri





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet](https://btc-heritage.com/) - Crypto7