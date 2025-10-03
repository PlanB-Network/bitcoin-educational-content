---
name: Sentinel
description: Watch-only wallet nedir ve nasıl kullanılır?
---

![cover](assets/cover.webp)


---

**\*UYARI:** Samourai Wallet kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından Sentinel uygulaması çalışmaya devam etmektedir, ancak **Blockchain bilgilerine erişmek ve işlemleri yayınlamak için kendi Dojo'nuzu** kullanmanız zorunludur.\*


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

> Özel anahtarlarınızı gizli tutun.

Bu makalede, yalnızca saat cüzdanları hakkında bilmeniz gereken her şeyi keşfediyoruz. Nasıl çalıştıklarını tartışıyor ve piyasada bulunan farklı uygulamaları inceliyoruz. Son olarak, en popüler Watch-only wallet uygulamalarından biri hakkında ayrıntılı bir eğitim sunuyoruz: Sentinel.


## Watch-only wallet nedir?


Bir Watch-only wallet veya salt okunur bir Wallet, kullanıcının ilgili özel anahtarlara erişimi olmadan bir veya daha fazla belirli Bitcoin açık anahtarıyla ilişkili işlemleri gözlemlemesine izin vermek için tasarlanmış bir yazılım türüdür.


Bu tür bir uygulama yalnızca bakiyesini ve işlem geçmişini görüntülemek de dahil olmak üzere bir Bitcoin Wallet'u izlemek için gerekli verileri tutar, ancak özel anahtarlara erişimi yoktur. Bu nedenle, Wallet'da tutulan bitcoinlerin yalnızca izleme uygulamasında harcanması mümkün değildir.

![watch-only](assets/en/1.webp)

Watch-only genellikle bir Hardware Wallet ile birlikte kullanılır. Bu, Wallet'ün özel anahtarlarının "Cold," internete bağlı olmayan bir cihazda saklanmasına olanak tanır, bu da özel anahtarları potansiyel olarak savunmasız ortamlardan izole ederek minimum saldırı yüzeyine sahiptir. Öte yandan sadece izle uygulaması sadece Bitcoin Wallet'ün genişletilmiş açık anahtarını (`xpub`, `zpub`, vb.) saklar. Bu ana anahtar, ilişkili özel anahtarların keşfedilmesine izin vermez ve sonuç olarak bitcoinlerin harcanmasına izin vermez. Ancak, alt açık anahtarların ve alıcı adreslerinin türetilmesine izin verir. Hardware Wallet tarafından güvence altına alınan Wallet adreslerinin bilinmesiyle, sadece izle uygulaması Bitcoin ağındaki bu işlemleri izleyebilir ve kullanıcıya her seferinde Hardware Wallet'larını bağlamak zorunda kalmadan bakiyelerini ve generate yeni alıcı adreslerini izleme olanağı sunar.


## Hangi Watch-only wallet kullanılmalı?


Şu anda en kapsamlı izleme uygulaması Samourai Wallet ekipleri tarafından geliştirilen [Sentinel](https://sentinel.watch/)'dir. İyi bir Watch-only wallet için gerekli tüm özellikleri kapsamaktadır:



- Genişletilmiş anahtarlar, genel anahtarlar ve adresler için destek;
- Birden fazla hesabı veya cüzdanı koleksiyonlar halinde düzenleme yeteneği;
- Doğrudan kullanım gerektirmeden kişinin Hardware Wallet'inde bitcoin almak için adreslerin oluşturulması;
- İşlemleri çevrimdışı olarak oluşturma ve yayınlama yeteneği;
- Kişinin kendi Bitcoin düğümüne bağlanma seçeneği;
- Gelişmiş gizlilik için Tor entegrasyonu.

Sentinel'in benzersiz dezavantajları, uygulamanın yalnızca Android için mevcut olması ve çoklu imza cüzdanlarını desteklememesidir. Bu nedenle, bir Android cihazınız varsa ve Wallet'niz klasik bir tek imza ise, Sentinel'i öneririm.

Çok imzalı bir Wallet'i takip etmek isteyenler için Blue Wallet, bu tür cüzdanlar için yalnızca izleme modu sunan bildiğim tek uygulamadır ve hem Android hem de iOS'tan erişilebilir.


Sentinel'e alternatif arayan iOS kullanıcıları için [Green Wallet](https://blockstream.com/Green/) veya [Blue Wallet](https://bluewallet.io/watch-only/) seçenek olabilir, ancak yalnızca saat işlevleri Sentinel'inki kadar kapsamlı değildir.

![watch-only](assets/notext/2.webp)


## Sentinel Watch-only wallet Nasıl Kullanılır?


### Kurulum ve Ayarlama


Sentinel uygulamasını yükleyerek başlayın. Bunu Google Play Store'dan veya [APK resmi web sitesinden indirilebilir] (https://sentinel.watch/download/) kullanarak yapabilirsiniz.


![watch-only](assets/notext/3.webp)


Uygulamayı ilk açtığınızda, size aşağıdakiler arasında bir seçim sunulur:



- "Dojo'ya Bağlan";
- "Samourai'nin sunucusuna bağlan".


Samourai ekibi tarafından geliştirilen Dojo, bağımsız olarak kurulabilen veya [Umbrel](https://umbrel.com/) ve [RoninDojo](https://ronindojo.io/) gibi kutu içinde düğüm çözümlerine tek bir tıklamayla eklenebilen tam bir Bitcoin düğüm sürümüdür.


[**-> RoninDojo v2'nin Raspberry Pi'ye nasıl kurulacağını keşfedin.**](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)


Kendi Dojo'nuz varsa, bu aşamada onu bağlayabilirsiniz. Bunu yaparak, Bitcoin ağ işlem bilgilerinizi kontrol ederken en üst düzeyde gizlilikten yararlanacaksınız.


![watch-only](assets/notext/4.webp)


Aksi takdirde, Samourai'nin varsayılan sunucusunu tercih etmek mümkündür. Ayrıca Tor üzerinden bağlanıp bağlanmayacağınızı da seçebilirsiniz.


![watch-only](assets/notext/5.webp)


Daha sonra Sentinel'in ana sayfasına ulaşacaksınız.


![watch-only](assets/notext/6.webp)


Başlamak için uygulamayı ayarlayabilirsiniz. Sağ üst köşedeki üç küçük noktaya ve ardından `Ayarlar` seçeneğine tıklayın.


![watch-only](assets/notext/7.webp)

Kullanıcı PIN kodu`nu seçerek, Watch-only wallet'inize güvenli erişim için bir şifre belirleme seçeneğine sahip olursunuz. Ayrıca, bakiyelerinizi fiat para birimine dönüştürmek için referans para birimini değiştirme ve hatta `Fiat değerlerini gizle` seçeneğini etkinleştirerek fiat değerlerini gizleme olanağına da sahipsiniz. Daha fazla güvenlik için, Sentinel uygulamanızın ekran görüntülerini engelleyen ve böylece harici bir ekranda herhangi bir bilginin ifşa edilmesini önleyen `Ekran Görüntülerini Devre Dışı Bırak` seçeneğini etkinleştirebilirsiniz.

![watch-only](assets/notext/8.webp)


Bu ayarlar menüsünde, Sentinel'inizi yedekleme seçeneğiniz de vardır.


### Watch-only wallet'un Kullanımı


Takip edilecek yeni bir genişletilmiş açık anahtar eklemek için ana sayfadan mavi `YENİ` düğmesine basın. Daha sonra anahtarınızın QR kodunu tarama veya `Paste Pubkey` seçeneğini seçerek anahtarı doğrudan yapıştırma (`xpub`, `zpub`...) seçeneğiniz vardır.


![watch-only](assets/notext/9.webp)


Genel olarak, Wallet'nizin `xpub` bilgisine kullandığınız Wallet yönetim yazılımı aracılığıyla doğrudan erişebilirsiniz. Örneğin, Hardware Wallet'unuzu Sparrow ile yönetiyorsanız, bu bilgi `Ayarlar` sekmesinde, `Anahtar Deposu` bölümü altında bulunur.


![watch-only](assets/notext/10.webp)


Sentinel'de genişletilmiş açık anahtarı girdikten sonra, uygulama size yeni bir koleksiyon oluşturmanızı önerir. Bir koleksiyon, birlikte organize edilmiş bir dizi genişletilmiş açık anahtarı temsil eder. Bu seçenek size sadece tüm `xpub`larınızı listeleme değil, aynı zamanda onları düzenli bir şekilde sınıflandırma imkanı da verir. Örneğin, birden fazla hesaba sahip bir Samourai Wallet'ünüz varsa (depozito, premix, postmix...), tüm bu hesapları `Samourai` koleksiyonu altında toplayabilirsiniz. Aileniz için yönetilen cüzdanlar için `Aile` adında bir koleksiyon oluşturabilirsiniz.


Yeni koleksiyon oluştur`u seçin. Ardından yeni entegre ettiğiniz genişletilmiş anahtar için bir isim girin. Örneğin, Samourai Wallet'ümün mevduat hesabını tararsam, bu anahtara `Deposit` adını veririm. Sonlandırmak için `KAYDET`e tıklayın.


![watch-only](assets/notext/11.webp)


Ardından, bu koleksiyona bir ad verin ve koleksiyonu kaydetmek için ekranın sağ üst köşesinde bulunan doğrulama simgesine basın. Koleksiyonunuz artık Sentinel ana ekranında görülebilir.


![watch-only](assets/notext/12.webp)


Başka bir genişletilmiş ortak anahtar eklemek isterseniz, tekrar `YENİ` üzerine tıklayın ve anahtarınızı girin.


![watch-only](assets/notext/13.webp)

Daha sonra bu anahtarı entegre etmek istediğiniz koleksiyonu seçmeniz veya yeni bir koleksiyon oluşturmanız istenecektir. Örneğin, benim durumumda, özellikle Ledger Wallet için bir koleksiyon oluşturdum.

![watch-only](assets/notext/14.webp)


Bir koleksiyonun genişletilmiş anahtarlarını ayrıntılı olarak görmek için üzerine tıklamanız yeterlidir. Daha sonra işlem geçmişini görüntülemek için farklı sekmeler arasında gezinebilirsiniz.


![watch-only](assets/notext/15.webp)


Bir koleksiyondan, sağ üstteki üç küçük noktaya ve ardından `Harcanan Çıktıları Görüntüle` seçeneğine dokunarak, izlenen Wallet tarafından tutulan UTXO'ların bir listesine erişebilirsiniz.


![watch-only](assets/notext/16.webp)


### Sentinel'den Bitcoin Gönderme ve Alma


Her iyi Watch-only wallet'da olduğu gibi Sentinel, takip edilen Wallet'de bitcoin almak için generate alıcı adreslerine izin verir. Ancak Sentinel bir başka gelişmiş özellik daha sunar: bir Partially Signed Bitcoin Transaction (PSBT) oluşturulması ve yayınlanması. Böylece, özel anahtarları tutan Wallet bu işlemi imzalayabilir ve bu işlem imzalandıktan sonra Sentinel tarafından Bitcoin ağında yayınlanabilir. Tüm bunların nasıl yapılacağını görelim.


**Dikkat, Wallet'nin kendisi tarafından doğrulanmamış bir alıcı Address'dan bitcoin alınması önerilmez.** Özel anahtarları tutan Wallet, örneğin bir Hardware Wallet, belirli bir Address'nın kendisine bağlı olduğunu açıkça onaylamamışsa, bu Address'ya bitcoin göndermek riskli bir uygulamadır. Gerçekten de, bu onay olmadan, Address'nın gerçekten Wallet'nize ait olduğuna dair hiçbir garanti yoktur. Bu nedenle, bir Watch-only wallet'ün alıcı işlevi, gönderilen fonların potansiyel olarak kaybedilebileceği akılda tutularak dikkatli kullanılmalıdır.


Sentinel aracılığıyla bitcoin almak için, ilgilendiğiniz koleksiyonu seçin, ardından para aktarmak istediğiniz genişletilmiş açık anahtara karşılık gelen sekmeye tıklayın.


![watch-only](assets/notext/17.webp)


Son olarak, ekranın sol alt tarafındaki ok simgesine tıklayın. Sentinel daha sonra sizin için boş bir alıcı Address oluşturur. Bunu kopyalayabilir veya QR kodunu kullanarak tarayabilirsiniz.


![watch-only](assets/notext/18.webp)


Sentinel'den bir PSBT'i generate yapmak ve böylece bir harcama işlemi başlatmak için, ödemeyi yapmak istediğiniz Wallet'nin genişletilmiş anahtarına gidin. Örneğin, Samourai Wallet'mdeki mevduat hesabımı ele alalım. Ardından ekranın sağ alt kısmında bulunan ok simgesine tıklayın.


![watch-only](assets/notext/19.webp)


İşleminizle ilgili tüm parametreleri girin:



- Alıcının Address'sini girin (QR kodu simgesine tıklayarak bu Address'yi tarama seçeneğiniz vardır);
- Bu Address'e gönderilecek tutarı belirtin;
- İşlem ücretlerini belirleyin.


İşleminiz için gerekli tüm alanları doldurduktan sonra, `İMZASIZ İŞLEMİ TAMAMLA` düğmesine basın.


![watch-only](assets/notext/20.webp)


Daha sonra, Sentinel'in özel anahtarlarınıza erişimi olmadığından, oluşturulmuş ancak imzalanmamış bir Bitcoin işlemini temsil eden PSBT'e erişeceksiniz. Bu işlemi kopyalama, bir `.PSBT` dosyası olarak dışa aktarma veya animasyonlu QR kodu aracılığıyla tarama seçeneğiniz vardır.


![watch-only](assets/notext/21.webp)


Ardından, işlemi imzalamak için özel anahtarlara sahip olan Wallet'nize gidin (Samourai, Hardware Wallet...).


![watch-only](assets/notext/22.webp)


İşlem imzalandıktan sonra, yayınlamak için Sentinel'e geri dönebilirsiniz. Bunu yapmak için, ana menüden sağ üstteki üç küçük noktaya ve ardından `İşlemi yayınla` seçeneğine tıklayın.


![watch-only](assets/notext/23.webp)


İmzalı PSBT'inizi üç farklı şekilde girme seçeneğiniz vardır:



- Doğrudan panonuzdan yapıştırarak;
- Bir `.PSBT` dosyasından içe aktararak;
- Bir QR kodu aracılığıyla tarayarak.


![watch-only](assets/notext/24.webp)


İmzalanan işlem gri çerçeveye girildikten sonra, Bitcoin ağında yayınlamak için Green `BROADCAST TRANSACTION` düğmesine tıklayabilirsiniz. Sentinel size txid'yi verecektir.


![watch-only](assets/notext/25.webp)