---
name: Blixt Wallet
description: Cep telefonunuzda güçlü bir LN düğümünü kullanmaya nasıl başlayabilirsiniz?
---
![cover](cover.webp)


Bu kılavuz, Bitcoin Lightning Network (LN)'ü ÜCRETSİZ AÇIK KAYNAK, TAM MÜŞTEREK OLMAYAN bir şekilde kullanmaya başlamak isteyen tüm yeni kullanıcılara adanmıştır.


Blixt Wallet](https://blixtwallet.com/) kullanarak, nerede olursanız olun cep telefonunuzda tam bir LN düğümü.


Bitcoin Lightning Network'yi hiç kullanmadıysanız, başlamadan önce [lütfen Lightning Network (LN) hakkındaki bu basit açıklama analojisini okuyun] (https://darth-Coin.github.io/beginner/LN-airport-analogy-en.html).


## ÖNEMLI HUSUSLAR:



- Blixt özel bir düğümdür, yönlendirme düğümü DEĞİLDİR! Bunu aklınızda bulundurun: Bu, Blixt'teki tüm LN kanallarının LN grafiğine (özel kanallar olarak adlandırılır) bildirilmeyeceği anlamına gelir. Bu, BU DÜĞÜMÜN Blixt düğümü aracılığıyla diğer ödemelerin YÖNLENDİRMESİNİ YAPMAYACAĞI anlamına gelir. Bu Blixt düğümü yönlendirme için DEĞİLDİR, tekrar ediyorum. Esas olarak kendi LN kanallarınızı yönetebilmek ve ihtiyaç duyduğunuzda LN ödemelerinizi özel olarak yapabilmek içindir. Bu Blixt düğümü, SADECE işlemlerinizi yapmadan ÖNCE çevrimiçi ve senkronize olmak için gereklidir. Bu yüzden üstte senkronizasyon durumunu gösteren bir simge göreceksiniz. Ne kadar süre çevrimdışı tuttuğunuza bağlı olarak sadece birkaç dakika sürer.



- Blixt, Wallet arka ucu olarak LND (aezeed) kullanıyor, bu nedenle diğer Bitcoin cüzdan türlerini içine aktarmaya çalışmayın. [Burada Wallet Mnemonic tohum türlerini açıkladınız] (https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Ve işte [tüm cüzdan türlerinin daha kapsamlı bir listesi](https://walletsrecovery.org/). Dolayısıyla, daha önce bir LND düğümünüz varsa, seed ve backup.channels'ı Blixt'e aktarabilirsiniz, [bu kılavuzda açıklandığı gibi](https://darth-Coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Bu kılavuzun sonunda ["ipuçları ve püf noktaları"] içeren özel bir bölüm bulacaksınız (https://darth-Coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Blixt önemli bağlantılar - bu kılavuzun sonunda görebilirsiniz, lütfen yer imlerine ekleyin.


---

## Blixt - İlk Temas


Darth'ın annesi Blixt ile LN kullanmaya karar verdi. Hard kararı, ama akıllıca. Blixt sadece zeki insanlar ve LN'in derin kullanımını gerçekten öğrenmek isteyenler içindir.


![blixt](assets/en/01.webp)


Darth annesini uyardı:


"*Anne, eğer Blixt LN Node kullanmaya başlarsan, öncelikle Lightning Network'nin ne olduğunu ve nasıl çalıştığını en azından temel düzeyde bilmen gerekecek. [Burada Lightning Network hakkında basit bir kaynak listesi hazırladım] (https://blixtwallet.github.io/faq#what-is-LN). Lütfen önce bunları okuyun.*"


Darth'ın annesi kaynakları okudu ve ilk adımını attı: Blixt'i yepyeni Android cihazına yükledi. Blixt ayrıca iOS ve macOS (masaüstü) için de kullanılabilir. Ancak bunlar Darth'ın Annesi için değil... Yine de daha iyi uyumluluk ve deneyim için Android'in daha yeni bir sürümünün, en az 9 veya 10'un kullanılması önerilir. Bir mobil cihazda tam bir LN düğümü çalıştırmak kolay bir iş değildir ve biraz yer (en az 600MB) ve bellek alabilir.


Blixt'i açtığınızda, "Hoş Geldiniz" ekranı size bazı seçenekler sunacaktır:


![blixt](assets/en/02.webp)


Sağ üst köşede, bir menüyü etkinleştiren 3 nokta göreceksiniz:



- "Tor'u etkinleştir" - kullanıcı Tor ağı ile başlayabilir, özellikle sadece Tor eşleri ile çalışan eski bir LND düğümünü geri yüklemek istiyorsa.
- "Bitcoin düğümünü ayarla" - kullanıcı blokları Neutrino aracılığıyla senkronize etmek için doğrudan kendi düğümüne bağlanmak isterse, bunu karşılama ekranından hemen yapabilir. Bu seçenek, internet bağlantınızın veya Tor'unuzun varsayılan Bitcoin düğümüne (node.blixtwallet.com) bağlanmak için çok kararlı olmaması durumunda da iyidir.
- Yakında oraya dil eklenecek, böylece kullanıcı rahat bir dille doğrudan başlayabilir. Bu açık kaynak projesine diğer dillerdeki çevirilerle katkıda bulunmak istiyorsanız, [lütfen buraya katılın] (https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### SEÇENEK A - Yeni Wallet oluşturun


"Yeni bir Wallet oluştur" seçeneğini seçerseniz, doğrudan Blixt Wallet'un ana ekranına yönlendirileceksiniz.


Bu sizin "kokpitiniz" ve aynı zamanda "Ana LN Wallet "dur, bu nedenle size yalnızca LN Wallet'unuzun dengesini göstereceğini unutmayın. Zincir üzerindeki Wallet ayrı olarak görüntülenir (bkz. C).


![blixt](assets/en/03.webp)


A - Blixt blokları senkronizasyon göstergesi simgesi. Bu, bir LN düğümü için en önemli şeydir: ağ ile senkronize olmak. Eğer bu simge hala orada çalışıyorsa, düğümünüz HAZIR DEĞİL demektir! Bu yüzden özellikle ilk senkronizasyon için sabırlı olun. Cihazınıza ve internet bağlantınıza bağlı olarak 6-8 dakika kadar sürebilir.


Tıklayabilir ve senkronizasyonun durumunu görebilirsiniz:


![blixt](assets/en/04.webp)


Ayrıca, LND günlüğünün daha teknik ayrıntılarını gerçek zamanlı olarak görmek ve okumak istiyorsanız "LND Günlüğünü Göster" (A) düğmesine tıklayabilirsiniz. Hata ayıklama ve LN'ün nasıl çalıştığını daha fazla öğrenmek için çok yararlıdır.


B - Burada tüm Blixt Ayarlarına erişebilirsiniz ve çok fazladır! Blixt, LN düğümünüzü bir profesyonel gibi yönetmeniz için birçok zengin özellik ve seçenek sunuyor. Tüm bu seçenekler "[Blixt Özellikler Sayfası] (https://blixtwallet.github.io/features#blixt-options) - Seçenekler Menüsü "nde ayrıntılı olarak açıklanmıştır.


C - Burada "Sihirli Çekmece" menüsüne sahipsiniz, [ayrıca burada ayrıntılı olarak açıklanmıştır] (https://blixtwallet.github.io/features#blixt-drawer). İşte "Onchain Wallet" (B), Yıldırım Kanalları (C), Kişiler, Kanallar durum simgesi (A), Keysend (D).


![blixt](assets/en/05.webp)


D - SSS / Kılavuzlar sayfası, geliştiriciyle iletişim, Github sayfası ve Telegram destek grubuna bağlantılar içeren yardım menüsüdür.


E - İlk BTC Address'inizi, ilk test Sats'ınızı yatırabileceğiniz yeri belirtin. BU İSTEĞE BAĞLIDIR! Doğrudan bu Address'e para yatırırsanız, Blixt Node'a doğru bir LN kanalı açılır. Bu, yatırdığınız Sats'ın, bu LN kanalını açmak için başka bir zincir içi işleme (tx) girdiğini göreceğiniz anlamına gelir. Sağ üstteki TX menüsüne tıklayarak bunu Blixt onchain Wallet'da kontrol edebilirsiniz (bkz. C noktası).


![blixt](assets/en/06.webp)


Onchain İşlem Günlüğünde görebileceğiniz gibi, Sats'nin nereye gittiğini gösteren adımlar çok ayrıntılıdır (para yatırma, açma, kanalı kapatma).


TAVSIYE:


Çeşitli durumları test ettikten sonra, 1 ila 5 M Sats arasında kanallar açmanın çok daha verimli olduğu sonucuna vardık. Daha küçük kanallar hızla tükenme eğilimindedir ve daha büyük kanallara kıyasla daha yüksek bir ücret yüzdesi ödemektedir.


F - Ana Lightning Wallet bakiyenizi gösterir. Bu, toplam Blixt Wallet bakiyeniz DEĞİLDİR, yalnızca Lightning Kanallarında sahip olduğunuz ve gönderilebilecek Sats'i temsil eder. Daha önce de belirtildiği gibi, Onchain Wallet ayrıdır. Bu hususu aklınızda bulundurun. Zincirleme Wallet önemli bir nedenden dolayı ayrıdır: esas olarak LN kanallarını açmak/kapatmak için kullanılır.


Tamam, şimdi Darth'ın Annesi ana ekranda görüntülenen zincir üzerindeki Address'ye bir miktar Sats yatırdı. Bunu yaptığınızda, BTC tx madenciler tarafından ilk bloğa alınana kadar Blixt uygulamanızı bir süre çevrimiçi ve aktif tutmanız önerilir.


Bundan sonra, tamamen onaylanana ve kanal açılana kadar 20-30 dakika kadar sürebilir ve Sihirli Çekmece - Yıldırım Kanalları'nda aktif olarak göreceksiniz. Ayrıca çekmecenin üstündeki küçük renkli nokta, eğer Green ise, LN kanalınızın çevrimiçi olduğunu ve LN üzerinden Sats göndermek için kullanılmaya hazır olduğunu gösterecektir.


Address ve görüntülenen karşılama mesajı kaybolacaktır. Artık otomatik bir kanal açmaya gerek yoktur. Bu seçeneği Ayarlar menüsünden de devre dışı bırakabilirsiniz.


LN kanallarını açmak için diğer özellikleri ve seçenekleri test ederek devam etme zamanı.


Şimdi, başka bir node eşiyle başka bir kanal açalım. Blixt topluluğu [Blixt ile kullanmaya başlamak için iyi düğümlerin bir listesini] bir araya getirdi (https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Blixt**'te bir LN kanalı açma prosedürü


Bu çok basittir, sadece birkaç adım ve biraz sabır gerektirir:



- Blixt Topluluğu](https://github.com/hsjoberg/blixt-Wallet/issues/1033) eşler listesine girdim
- Bir düğüm seçin ve isim başlığı bağlantısına tıklayın, Amboss sayfası açılacaktır
- URI Address düğümünün QR kodunu görüntülemek için tıklayın


![blixt](assets/en/07.webp)


Blixt'i açın ve üst çekmeceye gidin - Lightning Channels ve "+" düğmesine tıklayın


![blixt](assets/en/08.webp)


Şimdi, Amboss sayfasından QR kodunu taramak için (A) kamerasına tıklayın ve düğüm ayrıntıları doldurulacaktır. İstediğiniz kanal için Sats miktarını ekleyin ve ardından tx için ücret oranını seçin. Daha hızlı bir onay için otomatik (B) bırakabilir veya düğmeyi kaydırarak manuel olarak ayarlayabilirsiniz. Ayrıca numaraya uzun basabilir ve istediğiniz gibi düzenleyebilirsiniz.


1 sat/vbyte'tan daha az koymayın! Genellikle bir kanal açmadan önce [Mempool ücretleri](https://Mempool.space/)'ne başvurmak ve uygun bir ücret seçmek daha iyidir.


Bitti, şimdi sadece "kanal aç" düğmesine tıklayın ve 3 onay bekleyin, bu genellikle 30 dakika sürer (yaklaşık her 10 dakikada bir 1 blok).


Onaylandıktan sonra, kanalı "Lightning Kanalları" bölümünüzde aktif olarak göreceksiniz.


---

## Blixt - İkinci Temas


Tamam, şimdi sadece OUTBOUND likiditesi olan bir LN kanalımız var. Bu da sadece GÖNDERİM yapabileceğimiz, LN üzerinden Sats ALAMAYACAĞIMIZ anlamına geliyor.


![blixt](assets/en/09.webp)


Neden? Başlangıçta belirtilen kılavuzları okudunuz mu? Okumadınız mı? Geri dönün ve okuyun. LN kanallarının nasıl çalıştığını anlamak çok önemlidir.


![blixt](assets/en/10.webp)


Bu örnekte görebileceğiniz gibi, ilk para yatırma ile açılan kanalda çok fazla INBOUND likiditesi ("Alabilir") yoktur, ancak çok fazla OUTBOUND likiditesi ("Gönderebilir") vardır.


Peki LN yerine daha fazla Sats almak istiyorsanız ne gibi seçenekleriniz var?



- Mevcut kanaldan biraz Sats harcayın. Evet, LN, Bitcoin'in bir ödeme ağıdır ve esas olarak Sats'nizi daha hızlı, daha ucuz, özel ve kolay harcamak için kullanılır. LN bir hodling yolu DEĞİLDİR, bunun için zincir üzerinde Wallet'ya sahipsiniz.



- Bir denizaltı takas hizmeti kullanarak bir miktar Sats'i kendi zincirinizdeki Wallet ile takas edin. Bu şekilde Sats'inizi harcamamış, kendi zincirinizdeki Wallet'a geri vermiş olursunuz. Burada, [Blixt Kılavuzları Sayfasında] (https://blixtwallet.github.io/guides) bazı yöntemleri ayrıntılı olarak görebilirsiniz.



- Herhangi bir LSP sağlayıcısından bir INBOUND kanalı açın. İşte gelen bir kanal açmak için LNBig LSP'nin nasıl kullanılacağına dair bir video demosu. Bu, BOŞ bir kanal için (sizin tarafınızda) küçük bir ücret ödeyeceğiniz ve bu kanala daha fazla Sats alabileceğiniz anlamına gelir. Harcadığından daha fazlasını alan bir tüccarsanız, bu iyi bir seçenektir. Ayrıca Robosats veya başka bir LN Exchange kullanarak LN üzerinden Sats satın alıyorsanız.



- Blixt düğümü veya başka bir Dunder LSP sağlayıcısı ile bir Dunder kanalı açın. Bir Dunder kanalı, bir miktar INBOUND likiditesi elde etmenin basit bir yoludur, ancak aynı zamanda bu kanala bir miktar Sats yatırırsınız. Ayrıca iyidir çünkü kanalı Blixt Wallet'inizden olmayan bir [UTXO] (https://en.Bitcoin.it/wiki/UTXO) ile açacaktır. Bu biraz gizlilik katar. Ayrıca, normal bir LN kanalı açmak için zincir üzerindeki bir Wallet'te Sats'nız yoksa, ancak başka bir LN Wallet'te varsa, bu Dunder kanalının açılışını ve depozitosunu (sizin tarafınızdan) LN aracılığıyla başka bir Wallet'ten ödeyebilirsiniz. [Dunder'ın nasıl çalıştığı ve kendi sunucunuzu nasıl çalıştıracağınızla ilgili daha fazla ayrıntı burada](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


İşte bir Dunder kanalı açmayı etkinleştirmek için adımlar:



- Ayarlar'a gidin, "Deneyler" bölümünde "Dunder LSP'yi Etkinleştir" kutusunu etkinleştirin.
- Bunu yaptıktan sonra, "Lightning Network" bölümüne geri dönün ve "Dunder LSP Sunucusunu Ayarla" seçeneğinin göründüğünü göreceksiniz. Orada, varsayılan olarak "https://dunder.blixtwallet.com" ayarlanmıştır, ancak bunu başka bir Dunder LSP sağlayıcısı Address ile değiştirebilirsiniz. [İşte Blixt'iniz için Dudner LSP kanalları sağlayabilecek düğümleri içeren bir Blixt topluluk listesi](https://github.com/hsjoberg/blixt-Wallet/issues/1033).
- Şimdi ana ekrana gidebilir ve "Al" düğmesine tıklayabilirsiniz. Ardından [bu kılavuzda açıklanan] bu prosedürü izleyin (https://blixtwallet.github.io/guides#guide-lsp).


Tamam, Dunder kanalı onaylandıktan sonra (birkaç dakika sürecektir) 2 LN kanalına sahip olacaksınız: biri başlangıçta otomatik pilotla açılmış (kanal A) ve diğeri Dunder ile açılmış daha fazla gelen likiditeye sahip (kanal B).


![blixt](assets/en/12.webp)


Güzel, artık LN üzerinden yeterince Sats göndermek ve almak için hazırsınız!


MUTLU Bitcoin YILDIRIMLARI!


---

## Blixt - Üçüncü Kişi


Hatırlayın, birinci bölüm "İlk Temas "ta Karşılama ekranında 2 seçenek vardı:


- [Seçenek A](https://darth-Coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Yeni Wallet oluşturun
- Seçenek B - Wallet'i Geri Yükleyin


Şimdi Blixt Wallet veya başka bir LND çökmüş düğümün nasıl geri yükleneceğini tartışalım. Bu biraz daha teknik bir konu ama lütfen dikkat edin. O Hard değil.


### SEÇENEK B - Wallet'yi Geri Yükleyin


Geçmişte [çökmüş bir Umbrel düğümü nasıl geri yüklenir] (https://darth-Coin.github.io/nodes/shtf-restore-LND-node-en.html) hakkında özel bir rehber yazdım ve burada Umbrel'den seed + channel.backup dosyasını kullanarak Blixt'i hızlı geri yükleme işlemi olarak kullanma yönteminden de bahsettim.


Ayrıca Blixt düğümünüzü nasıl geri yükleyeceğiniz veya Blixt'inizi başka bir cihaza nasıl taşıyacağınız konusunda bir kılavuz yazdım, [burada](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Ancak bu süreci basit adımlarla açıklayalım. Yukarıdaki resimde de görebileceğiniz gibi, önceki Blixt/LND düğümünüzü geri yüklemek için yapmanız gereken 2 şey var:



- üst kutu, seed'nizdeki (eski / ölü düğüm) 24 kelimenin tümünü doldurmanız gereken yerdir
- altta, daha önce eski Blixt/LND düğümünüzden kaydedilen channel.backup dosyasını eklemek / yüklemek için iki düğme seçeneği vardır. Yerel bir dosyadan (daha önce cihazınıza yüklediğiniz) veya bir Google sürücüsünden / iCloud uzak konumundan olabilir. Blixt, kanal yedeklemenizi doğrudan bir Google / iCloud sürücüsüne kaydetmek için bu seçeneğe sahiptir. Daha fazla ayrıntı için [Blixt Özellikler Sayfası] (https://blixtwallet.github.io/features#blixt-options) adresine bakın.


Bununla birlikte, daha önce açık LN kanalınız yoksa, herhangi bir channels.backup dosyası yüklemenize gerek yoktur. Sadece 24 kelimelik seed'u yerleştirin ve geri yükle düğmesine basın.


Seçenek A bölümünde açıkladığımız gibi, üstteki 3 nokta menüsünden Tor'u etkinleştirmeyi unutmayın. Bu, SADECE Tor eşleriniz olduğunda ve clearnet (domain/IP) üzerinden iletişim kurulamadığında geçerlidir. Aksi takdirde gerekli değildir.


Bir başka kullanışlı özellik de bu üst menüden belirli bir Bitcoin düğümü ayarlamaktır. Varsayılan olarak blokları node.blixtwallet.com'dan (nötrino modu) senkronize eder, ancak nötrino senkronizasyonu sağlayan başka herhangi bir Bitcoin düğümünü ayarlayabilirsiniz.


Bu seçenekleri doldurup geri yükle düğmesine bastığınızda, İlk Temas bölümünde açıkladığımız gibi Blixt ilk olarak blokları Neutrino aracılığıyla senkronize etmeye başlayacaktır. Bu yüzden sabırlı olun ve ana ekranda senkronizasyon simgesine tıklayarak geri yükleme işlemini izleyin.


![blixt](assets/en/14.webp)


Bu örnekte görebileceğiniz gibi, Bitcoin bloklarının %100 senkronize olduğunu (A) ve kurtarma işleminin devam ettiğini (B) göstermektedir. Bu, daha önce sahip olduğunuz LN kanallarının kapatılacağı ve fonların Blixt onchain Wallet'e geri yükleneceği anlamına gelir.


Bu süreç zaman almaktadır! Bu nedenle lütfen sabırlı olun ve Blixt'inizi aktif ve çevrimiçi tutmaya çalışın. İlk senkronizasyon 6-8 dakika kadar sürebilir ve kanalların kapanması 10-15 dakika kadar sürebilir. Bu yüzden cihazınızı iyi şarj etseniz iyi olur.


Bu işlem başladıktan sonra, Sihirli Çekmece - Yıldırım Kanalları'nda, önceki kanallarınızın her birinin durumunu kontrol edebilir, "kapanmayı bekliyor" durumunda olduklarını gösterebilirsiniz. Her kanal kapatıldığında, kapanış tx'ini onchain Wallet'te görebilirsiniz (bkz. Sihirli Çekmece - Onchain) ve tx menü günlüğünü açabilirsiniz.


![blixt](assets/en/15.webp)


Ayrıca, eski LN düğümünüzde daha önce sahip olduğunuz eşlerinizin orada olup olmadığını kontrol etmek ve eklemek iyi olacaktır. Bu yüzden Ayarlar menüsüne gidin, "Lightning Network "ya inin ve "Yıldırım Eşlerini Göster" seçeneğine girin.


![blixt](assets/en/16.webp)


Bölümün içinde o anda bağlı olduğunuz eşleri göreceksiniz ve daha fazlasını ekleyebilirsiniz, daha önce kanallarınız olanları eklemek daha iyidir. Sadece [Amboss page] (https://amboss.space/) adresine gidin, eş düğümlerinizin takma adlarını veya nodeID'sini arayın ve düğüm URI'lerini tarayın.


![blixt](assets/en/17.webp)


Yukarıdaki resimde görebileceğiniz gibi, 3 yön vardır:


A - clearnet düğümünü temsil eder Address URI (etki alanı/IP)


B - Tor onion düğümü Address URI'sini (.onion) temsil eder


C - Blixt kameranızla veya kopyalama düğmesiyle taranacak QR kodudur.


Bu Address URI düğümünü eşler listenize eklemeniz gerekir. Bu yüzden sadece düğüm takma adı veya nodeID'nin yeterli olmadığını unutmayın.


Şimdi Magic Drawer (sol üst menü) - Lightning Channels'a gidebilir ve fonların hangi vade bloğu yüksekliğinde Address zincirinize iade edileceğini görebilirsiniz.


![blixt](assets/en/18.webp)


Bu blok numarası 764272, fonların Address zincirindeki Bitcoin'ünüzde kullanılabilir olacağı zamandır. Ve 1. onay bloğundan serbest bırakılana kadar 144 blok kadar sürebilir. [Bunu Mempool'te kontrol edin] (https://Mempool.space/).


Ve işte bu kadar. Tüm kanallar kapanana ve fonlar zincir üzerindeki Wallet'inize geri dönene kadar sabırla bekleyin.


👉 **Gizli geri yükleme yöntemi :**


Blixt LND düğümünüzü kanalları bile kapatmadan geri yüklemek için başka bir yöntem daha var. Ancak normal noob kullanıcılardan gizlenmiştir, çünkü bu yöntem SADECE ne yaptığını bilenler içindir.


Mevcut (çalışan) Blixt düğümünüzü, mevcut LN kanallarını kapatmadan başka bir yeni cihaza taşımanız gerekiyorsa, aşağıdaki adımları uygulamanız gerekecektir:



- Blixt Wallet seed'u zaten kaydettiğinizi varsayıyoruz (24 kelime aezeed)
- Eski cihazda, "Ayarlar" - hata ayıklama bölümü - "LND veritabanını sıkıştır" seçeneğine gidin. Bu adım isteğe bağlıdır ancak channel.db dosyasının boyutunun daha küçük olmasını istiyorsanız önerilir. Düğüm etkinliğinize bağlı olarak genellikle oldukça büyüktür. Bu, Blixt'i yeniden başlatacak ve db dosya boyutunu sıkıştıracaktır.
- Yeniden başlattıktan sonra, "Ayarlar "a gidin ve normal takma adınızı "Hampus" olarak değiştirin. Bu, yalnızca ileri düzey kullanıcılar için gizli seçenekleri etkinleştirecektir.
- "Hata Ayıklama" bölümüne gidin ve yeni bir "channel.db dosyasını dışa aktar" seçeneği göreceksiniz. UYARI! Bu dışa aktarma işlemini yaptığınızda, mevcut Blixt LN düğümü bu eski cihazda devre dışı bırakılacak ve yeni bir cihaza aktarılmaya hazır tüm düğüm veritabanını (channel.db) dışa aktaracaktır.
- Bu db dosyası eski cihazınızda (Belgeler veya İndirilenler) belirlenmiş bir klasöre kaydedilecek ve oradan olduğu gibi yeni cihazınıza taşımanız gerekecektir. Dosyayı doğrudan cihazlar arasında aktarmak için örneğin [LocalSend FOSS uygulamasını] (https://github.com/localsend/localsend) kullanabilirsiniz.
- Bu anda eski Blixt'iniz kapalı kalmalıdır. TEKRAR AÇMAYIN!
- Channel.db dosyasını yeni cihaza aktardıktan sonra, Blixt'in yeni kurulumunu başlatın ve ilk ekranda "Wallet'yi Geri Yükle "yi seçin.
- "SCB dosyası seç" yazan düğmeye uzun basın (basit tıklama DEĞİL!) ve ardından yeni cihazda yerel olarak kaydettiğiniz bir channel.db dosyası seçme seçeneğini göreceksiniz. Bu düğmeye basitçe basarsanız, varsayılan olarak bir SCB dosyası (kanalları kapatarak) kullanacaktır, tam yedek canlı kanallar için çalışmaz.
- 24 seed kelimesini girin ve ardından "Geri Yükle "ye tıklayın
- Blixt'in Neutrino ile senkronize olmaya başlayacağını göreceksiniz. Senkronizasyon günlüklerini de izleyebilirsiniz.
- AKLINIZDA BULUNDURUN! Bu aşamada Blixt'i her zaman açık tutmaya çalışın! Uykuya geçmesine veya uygulama ekranını kapatmasına izin vermeyin. Bu ilk senkronizasyonu bozabilir ve tekrar yapmanız gerekir. Sabırla bekleyin, birkaç dakikadan fazla sürmez.
- İlk blok senkronizasyonu tamamlandığında, önceki Wallet adreslerinizi hızlı bir şekilde tarayacak ve ardından kanallarınız canlı ve iyi bir şekilde tekrar çevrimiçi olacaktır.
- Ne yazık ki önceki ödeme geçmişini ve kişileri geri yüklemek (henüz) mümkün değil. Ancak bu zaten o kadar da önemli değil.


Ve BİTTİ! Artık tamamen geri yüklenmiş bir Blixt LN düğümünüz var. Daha önce channel.db dosyasını doğru bir şekilde kaydettiyseniz, diğer LND yedekleriyle (Umbrel, Raspiblitz vb.) de çalışabilir. Böylece Blixt herhangi bir LND ölü düğümünü tam anlamıyla kurtarabilir.


---

## Blixt - Dördüncü Temas


Bu bölüm özelleştirme ve Blixt Node'u daha iyi tanımakla ilgilidir. Mevcut tüm özellikleri açıklamayacağım, çok fazla ve [Blixt Özellikleri Sayfası](https://blixtwallet.github.io/features)'da zaten açıklanmıştı.


Ancak Blixt'inizi kullanarak ilerlemek ve harika bir deneyim yaşamak için gerekli olanlardan bazılarına işaret edeceğim.


### A - İsim (NameDesc)


![blixt](assets/en/19.webp)


[NamDesc] (https://github.com/lightning/blips/blob/master/blip-0011.md), BOLT11 faturalarında "alıcı adını" iletmek için bir standarttır.


Bu herhangi bir isim olabilir ve istenildiği zaman değiştirilebilir.


Bu seçenek, Invoice açıklaması ile birlikte bir isim göndermek istediğiniz çeşitli durumlarda gerçekten yararlıdır, böylece alıcı bu Sats'i kimin aldığına dair bir ipucuna sahip olabilir. Bu tamamen isteğe bağlıdır ve ayrıca ödeme ekranında kullanıcının takma adın gönderilmesini belirten kutuyu işaretlemesi gerekir.


İşte [chat.blixtwallet.com](https://chat.blixtwallet.com/) adresini kullandığınızda nasıl görüneceğine dair bir örnek


![blixt](assets/en/20.webp)


Bu, NameDesc'i destekleyen başka bir Wallet uygulamasına gönderilen başka bir örnektir:


![blixt](assets/en/21.webp)


### B - Yıldırım Kutusu


Yeni v0.6.9-420 [yakın zamanda duyuruldu] (https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420) ile başlayarak, Blixt Lightning Address için Blixt'te yeni ve güçlü bir özellik sundu.


Bu yeni özellik isteğe bağlı olarak etkinleştirilir, varsayılan olarak AÇIK değildir!


Şu an için varsayılan LN Kutusu Blixt sunucusu tarafından çalıştırılıyor ve @blixtwallet.com LN Address sunuyor. Ancak LND genel düğümü olan HERKES Lightning Box sunucusunu çalıştırabilir ve kendi etki alanı için LN Address sunabilir, kendi kendini koruyabilir.


Şu anda, Blixt sunucusu yalnızca @blixtwallet.com LN adreslerine gönderilen ödemeleri LN Address'lerini ayarlayan Blixt kullanıcılarına iletiyor. Kullanıcıların bu ödemeleri @blixtwallet.com LN adreslerine alabilmeleri için Blixt düğüm Wallet'larını "kalıcı moda" geçirmeleri gerekmektedir.


Sürüm notlarında LN Address'inizi Blixt'te nasıl kuracağınızla ilgili video demosuna bakın.


Blixt Wallet uygulamasına uygulanan bu LN Address, LN üzerinden bir sohbet gibidir, anında ve eğlencelidir, ayrıca [LUD-18] (https://github.com/lnurl/luds/blob/luds/18.md) (bir ödemeye takma ad ekleme) destekler. Sıklıkla kullandığınız tüm normal LN adreslerinizi kişi listesine ekleyebilir ve sohbet için elinizin altında bulundurabilirsiniz. Artık Blixt tam bir LN sohbet uygulaması olarak kabul edilebilir 😂😂.


Bir diğer kullanışlı özellik ise LUD-18'e tam destek vermesidir (ayrıca [Stacker.News](https://stacker.news/r/DarthCoin) ve diğerleri de desteklemektedir).


![blixt](assets/en/22.webp)


Yukarıdaki ekran görüntüsünde görebileceğiniz gibi, bir Stacker News hesabından gönderirken, logo + LN Address + mesajı güzel bir şekilde görüntüledi. Blixt'ten gönderirken de aynı şekilde çalışır, Blixt LN Address'ünüzü ekleyebilir veya sadece takma adınızı (önceden Blixt ayarlarında ayarlanmış) veya hatta her ikisini de ekleyebilirsiniz.


LUD-18'deki bu seçenek, kullanıcının belirli bir takma ad gönderebileceği (düğüm takma adınız veya gerçek adınız DEĞİLDİR!) ve buna dayanarak kaydedilebileceğiniz veya belirli bir mesajı geri alabileceğiniz veya başka bir şey yapabileceğiniz abonelik hizmetleri için de yararlı olabilir. Bir LN ödemesine bir takma ad ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ yorum ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) eklemek birden fazla kullanım alanına sahip olabilir!


Kendiniz, aileniz ve arkadaşlarınız için kendi düğümünüzde çalıştırırsanız [Lightning Box] (https://github.com/hsjoberg/lightning-box) için kod burada.


Burada ayrıca Blixt mobil düğümleri için [LSP Dunder sunucusu] (https://github.com/hsjoberg/dunder-lsp) çalıştırabilir ve iyi bir genel LN düğümünüz varsa (yalnızca LND ile çalışır) Blixt kullanıcıları için likidite sunabilirsiniz.


### C - Yedek LN Kanalları ve seed kelimeleri


Bu çok önemli bir özellik!


Bir LN kanalını açtıktan veya kapattıktan sonra bir yedekleme yapmalısınız. Küçük bir dosyayı yerel cihaza (genellikle indirme klasörü) kaydederek veya bir Google Drive veya iCloud hesabı kullanarak manuel olarak yapılabilir.


![blixt](assets/en/23.webp)


Blixt Ayarları - Wallet bölümüne gidin. Orada Blixt Wallet cihazınız için tüm önemli verileri kaydetme seçeneklerine sahipsiniz:



- "Mnemonic'yi Göster" - 24 kelimeyi yazmanız için seed'ü gösterecektir
- "Mnemonic'ü cihazdan kaldır" - bu isteğe bağlıdır ve yalnızca seed kelimelerini cihazınızdan gerçekten kaldırmak istiyorsanız kullanın. Bu işlem Wallet'inizi SİLMEZ, sadece seed'yı siler. Ancak dikkatli olun! İlk önce yazmadıysanız onları kurtarmanın bir yolu yoktur.
- "Kanal yedeğini dışa aktar" - bu seçenek yerel cihazınıza, genellikle "indirilenler" klasörüne küçük bir dosya kaydeder, buradan alıp güvenli bir şekilde saklamak için cihazınızın dışına taşıyabilirsiniz.
- "Kanal yedeklemesini doğrula" - Google drive veya iCloud kullanıyorsanız, uzaktan yapılan yedeklemenin bütünlüğünü kontrol etmek için bu iyi bir seçenektir.
- " Google sürücü kanalı yedeklemesi" - yedekleme dosyasını kişisel Google sürücünüze kaydeder. Dosya şifrelenir ve normal google dosyalarınızdan ayrı bir depoda saklanır. Yani herhangi biri tarafından okunabileceğine dair hiçbir endişe yoktur. Her neyse, bu dosya seed kelimeleri olmadan tamamen işe yaramaz, bu nedenle kimse paranızı yalnızca bu dosyadan alamaz.


Bu bölüm için aşağıdakileri tavsiye ederim:



- gW-158 ve yedekleme dosyanızı güvenli bir şekilde saklamak için bir şifre yöneticisi kullanın. KeePass veya Bitwarden bunun için çok iyidir ve çoklu platformda ve kendi kendine barındırılan veya çevrimdışı olarak kullanılabilir.
- Bir kanalı her açtığınızda veya kapattığınızda YEDEKLEME YAPIN. Bu dosya kanal bilgileri ile güncellenir. LN üzerinde yaptığınız her işlemden sonra bunu yapmanıza gerek yoktur. Kanal yedeği bu bilgiyi depolamaz, sadece kanalın durumunu depolar.


![blixt](assets/en/24.webp)


---

## Blixt - İpuçları ve Püf Noktaları


### VAKA 1 - SENKRONİZASYON SORUNLARI


"_Blixt'im senkronize olmuyor... Blixt'im bakiyeyi göstermiyor... Blixt cihazım kanalları açamıyor... Başka bir cihazda geri yüklemeyi denedim... vb_"


Tüm bu sorunlar, CİHAZINIZIN DÜZGÜN SENKRONİZE OLMAMASI nedeniyle başlar. Lütfen bu önemli hususu anlayın: Blixt, blokları senkronize etmek / okumak için Neutrino kullanan mobil bir LND düğümüdür.



- İşte [Bitcoin Magazine]'den daha az teknik bir açıklama (https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- İşte [Bitcoin Optech] (https://bitcoinops.org/en/topics/compact-block-filters/) adresinden daha fazla teknik kaynak
- Neutrino'yu kendi ev düğümünüzde nasıl etkinleştirebileceğinizi ve mobil düğümünüz için blok filtreleri nasıl sunabileceğinizi [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) adresinden öğrenebilirsiniz


HATIRLATMA: Neutrino'yu clearnet üzerinden kullanmak tamamen güvenlidir, IP'niz veya xpub'ınız sızdırılmaz. Siz sadece neutrino ile uzak bir düğümden blokları okuyorsunuz. Hepsi bu kadar. Geri kalan her şey yerel cihazınızda yapılır.


Bu yüzden Tor ile kullanmaya GEREK YOKTUR. Tor, senkronizasyon sürecinize büyük bir gecikme ekleyecek ve Blixt'inizi çok kararsız hale getirecektir. Eğer gerçekten Tor üzerinden kullanmak istiyorsanız, ne yaptığınızdan emin olun ve iyi bir bağlantıya ve sabra sahip olun. VPN kullanmak için de aynı durum geçerlidir. VPN'den size verilen gecikme süresine dikkat edin.


Bir neutrino sunucusunun gecikme süresini, bir PC'den veya cep telefonunuzdan ping atarak test edebilirsiniz.


![blixt](assets/en/25.webp)


Bu, neutrino sunucusu europe.blixtwallet.com'a yapılan olağan bir pingdir, bu, bağlantının ortalama 50 ms yanıt süresi ve 51 TTL ile çok iyi olduğunu gösterir. Yanıt süresi değişebilir ama çok fazla değil. TTL sabit olmalıdır.


Bu değerler 100-150 ms'den yüksekse, senkronizasyon işleminiz bayatlayacak veya daha da kötüsü, eşler tarafından kapalı kanallara neden olabilir! Bu hususu göz ardı etmeyin.


Düzgün bir senkronizasyon olmadan, doğru dengeyi de göremezsiniz veya LN kanallarınız çevrimiçi ve çalışır durumda olmaz. İndirme hızınız kaç giga ultra terra mbps olursa olsun ÖNEMLİ DEĞİLDİR. Önemli olan zaman tepkisi ve TTL (yaşam süresi).


Bu LATAM kullanıcıları için genel bir durum gibi. Orada ne olduğunu bilmiyorum ama 200 ms'nin üzerinde pinglerle herhangi bir senkronizasyonu bozabilecek korkunç bir bağlantınız var.


Peki bu çaresiz kullanıcılar için çözüm nedir?



- tor ile Blixt kullanmayı bırakın. Tamamen işe yaramaz
- bir VPN kullanabilirsiniz ancak akıllıca seçin ve ping'i her zaman izleyin. Coğrafi konumunuza daha yakın bir VPN kullanın. Mesafe, daha fazla ms yanıt süresi anlamına gelir, unutmayın.
- neutrino eşlerinizi akıllıca seçin, burada iyi bilinen halka açık neutrino sunucularının bir listesi bulunmaktadır:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Başka bir yol da "kompakt filtreler" (BIP157 / neutrino) - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS) duyuran bu düğüm listesinden birini seçmektir. Coğrafi konumunuza daha yakın olanı seçin.


Başka bir yol (en iyi yol), tanıdığınız bir arkadaşınız veya grup tarafından yönetilen ve nötrino bağlantısı sunan yerel bir topluluk düğümüne bağlanmaktır. [İşte nasıl yapılacağına dair talimatlar](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Düğümleri hiçbir şekilde etkilenmeyecektir, sadece istikrarlı ve herkese açık bir bağlantıya ihtiyaçları vardır.


Daha iyi ve hızlı bir senkronizasyon için LATAM bölgesinde daha fazla neutrino sunucusuna ihtiyaç var. Bu nedenle, lütfen yerel Bitcoin topluluğunuzla kendinizi organize edin ve kendi kullanımınız için kimin ve nerede bir Bitcoin core + Neutrino çalıştırdığına karar verin. Sadece genel bir IP ile yeterlidir. Genel bir IP'ye erişiminiz yoksa, bir VPS IP kullanabilir ve ev düğümünüze wireguard tüneli yapabilirsiniz. Bu şekilde, ev düğümünüz hakkında herhangi bir özel bilgiyi açığa çıkarmadan tüm trafiği yerel VPS IP'nize yönlendirirsiniz.


### DURUM 2 - SENKRONIZASYONU ASLA TAMAMLAMAYIN


"_Blixt'imin neutrino sunucusuyla iyi bir bağlantısı var ama senkronizasyonda takılıyor._"


#### Zaman Sunucusu


Bazen insanlar çeşitli eski cihazlar kullanıyor veya bir zaman sunucusuna düzgün bir şekilde bağlı değiller. Neutrino, gerçek yerel zamana karşılık gelmeyen gerçek bloklara ulaşana kadar senkronizasyonu tamamlıyor. Blixt LND günlüklerinde "blok zaman damgası gelecekten uzak" veya "başlık sağlık kontrolünü geçemiyor" ile ilgili bir hata göreceksiniz.


Hızlı düzeltme: cihazınız için doğru saat ve tarihi ayarlayın ve Blixt'i yeniden başlatın.


#### Cihazda az yer var


Bazen düşük alana sahip eski bir cihaz kullanıldığında, bir eşik sınırına ulaşabilir ve takılabilir. Gerçekten de bu mobil LND düğümünü ne kadar çok kullanırsanız, nötrino dosyaları ve ayrıca channel.db dosyası o kadar büyür.


Hızlı düzeltme: Blixt Seçenekleri - Hata Ayıklama bölümüne gidin - "LND'ü durdur ve nötrino dosyalarını sil" seçeneğini seçin. Uygulamayı yeniden başlatacak ve yeni bir senkronizasyon başlatacaktır. Bazen bu hızlı düzeltme bozuk verileri de onarabilir. Tamamen yeniden senkronize etmenin 1 ila 3 dakika arasında biraz zaman alacağını unutmayın. Mevcut fonları veya kanalları SİLMEZ, ancak evet, yeniden senkronizasyondan sonra Bitcoin adreslerinizin yeniden taranmasını tetikleyebilir ve bu daha fazla zaman alabilir.


Bir sonraki adım, hala ne kadar veri kullanıldığını kontrol etmektir. Bunu Android Uygulama bilgisi - veri bölümünde görebilirsiniz. Eğer hala 400-500MB'den büyükse, LND dosyalarını sıkıştırabilirsiniz. Bu yüzden Blixt Seçenekleri - Hata Ayıklama bölümüne gidin - "DB LND'ü Sıkıştır" seçeneğini seçin. Otomatik olarak yapılmıyorsa Blixt uygulamasını yeniden başlatın. Sıkıştırma işlemi başlangıçta gerçekleşir ve yalnızca bir kez yapılır. Şimdi Blixt verilerinin daha az dolu olduğunu göreceksiniz.


#### Kalıcı mod


Bazen insanlar Blixt'i uzun süre açmazlar, bu yüzden senkronizasyon çok eskidir. Ancak açtıklarında anında senkronize edilmeyi bekliyorlar.


Lütfen sabırlı olun ve en üstteki dönen tekerleğe bakın. İsteğe bağlı olarak Seçenekler - Düğüm Bilgilerini Gör'e gidebilir ve zincirle senkronize edilip edilmediğini ve grafikle senkronize edilip edilmediğini "doğru" olarak işaretlenmiş olarak görebilirsiniz. Bu "true" ibaresi olmadan Blixt'i düzgün kullanamazsınız, bakiyeyi doğru göremezsiniz, LN kanallarını çevrimiçi göremezsiniz, ödeme yapamazsınız.


Hızlı düzeltme: Blixt düğümünüzü "canlı tutmak" için güçlü bir seçenek var. Seçenekler - Denemeler'e gidin - "Kalıcı Modu Etkinleştir "i seçin. Bu, Blixt'inizi yeniden başlatacak ve LND hizmetini kalıcı moda geçirecektir, yani başka bir uygulamaya geçseniz veya Blixt'i kapatsanız bile (kapatmaya zorlamayın veya görevi öldürmeyin) her zaman aktif olacak ve senkronizasyonunuzu çevrimiçi tutacaktır. Sabit bir bağlantınız varsa ve Blixt'i birkaç kez kullanmanız gerekiyorsa tüm gün bu şekilde tutabilirsiniz. Pili çok fazla tüketmeyecektir.


### DURUM 3 - BAŞKA BİR CİHAZA GEÇMEK İSTİYORUM


Tamam bu senaryo hakkında [SSS sayfasında] (https://blixtwallet.github.io/faq#blixt-restore) kapsamlı bir kılavuz yazdım: 2 seçenekle, hızlı (geçişten önce kanalların kooperatif olarak kapatılması) ve yavaş (eski cihaz öldüğü için kanalları kapatmaya zorlayın).


Ancak burada bazı önemli hususları tekrarlamak ve yeni bir "gizli" prosedür eklemek istiyorum.


HATIRLATMA:



- Bir kanalı her açtığınızda veya kapattığınızda her zaman kanal durumunuzun (SCB) yedeğini alın. Bunu yapmak sadece birkaç saniye sürer.
- Eski SCB dosyalarını saklamayın, kafanız karışmasın ve geri yüklemeyin. Tamamen işe yaramazlar ve onları ele geçirirseniz bir ceza prosedürünü tetikleyebilirler. Geri yüklemeye devam ederseniz her zaman SCB dosyasının son sürümünü kullanın.
- SCB dosyasını (.bin uzantılı şifreli bir metindir) cihazınızın dışında güvenli bir yere kaydedin. Bu dosyayı bir PC'ye veya başka bir cihaza taşımak için [LocalSend] (https://github.com/localsend/localsend) kullanabilirsiniz.
- Blixt Wallet'nizin seed'ini de güvenli bir yere, örneğin çevrimdışı bir şifre yöneticisine / şifreli USB'ye kaydedin.


Gizli yöntem: Mevcut kanalları kapatmadan Blixt düğümü nasıl taşınır. Bunun için bu kılavuzdaki "Wallet'u Geri Yükle" ile ilgili önceki "Üçüncü Kişi" bölümünü dikkatlice okumanız gerekecektir.


Bu prosedür NOOBS İÇİN DEĞİLDİR, sadece ileri düzey kullanıcılar içindir! Bu yüzden yaygın olarak açık değildir ve bunu yalnızca Blixt geliştiricilerinden veya desteğimden yardım alarak yapmanızı öneririm. Lütfen bu tavsiyeyi göz ardı etmeyin.


### VAKA 4 - KANAL AÇMAK İÇİN HANGİ EŞLER KULLANILIR?


Blixt kılavuzları sayfasında] (https://blixtwallet.github.io/guides) yazdığım gibi, bu mobil LND düğümü ile kanal açmanın birçok yolu var. Ancak burada size hatırlatmak istediğim bazı önemli hususlar var:



- iyi bilinen LSP düğümleri ve topluluk onaylı eşler ile açık. [Burada bir listeye bakın](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- sadece rastgele Tor düğümleri ile açmayın. Bunlar değersizdir ve yalnızca ödeme yapamama sorunları yaşarsınız. Arkadaşınız "düğüm koşucusu" ormanda ne kadar iyi bir Tor düğümüne sahip olursa olsun, size asla mobil bir özel düğüm için en iyi rotaları vermeyecektir. Arkadaşınız olduğu için biriyle kanal açmazsınız. Burası Facebook değil! Bir kanalı şunun için açarsınız: iyi rotalar, küçük ücretler, uygunluk.
- bir ton küçük kanal açmaya gerek yok, 2-3 veya en fazla 4, ancak iyi miktarda Sats ile. Küçük kanallar açmayın, tamamen işe yaramazlar. Bir mobil cihaz için 200k'dan daha küçük kanalların pek bir faydası yoktur.
- gelen kanallar ve JIT (tam zamanında) kanalları sunan LSP'leri aklınızda bulundurun. Bunlar çok kullanışlıdır çünkü UTXO'larınızdan herhangi birini kullanmanıza gerek yoktur, açılış kanalını diğer LN cüzdanlarında zaten sahip olduğunuz fonlarla ödeyebilir, bunları istifleyebilir ve daha büyük bir kanalın açılması için hazırlayabilirsiniz. Bu JIT kanallarını kendi lehinize kullanmalısınız. [Bu kılavuzda açıkladım] (https://darth-Coin.github.io/nodes/managing-lightning-node-liquidity-en.html) Blixt gibi özel düğümler için eşler için daha fazla seçenek. Ayrıca [burada SN'de yayınlanan bu kılavuzda](https://stacker.news/items/679242/r/DarthCoin) özel mobil düğümlerin likiditesinin nasıl yönetileceğini açıkladım.


---

## Sonuç


Tamam, Blixt'in sunduğu daha birçok harika özellik var, bunları tek tek keşfetmenize ve eğlenmenize izin vereceğim.


Bu uygulama gerçekten hafife alınıyor, çünkü herhangi bir VC finansmanı tarafından desteklenmiyor, topluluk odaklı, Bitcoin ve Lightning Network için sevgi ve tutku ile inşa edildi.


Bu mobil LN düğümü, Blixt, nasıl kullanılacağını iyi bilirlerse, birçok kullanıcının elinde çok güçlü bir araçtır. Düşünün, cebinizde bir LN düğümü ile dünyayı dolaşıyorsunuz ve kimse bunu bilmeyecek.


Ve diğer Wallet uygulamalarının çok azının veya hiçbirinin sunamayacağı, birlikte gelen diğer tüm zengin özelliklerden bahsetmiyorum.


Bu arada, bu muhteşem Bitcoin Lightning Node ile ilgili tüm bağlantılar burada:



- [Blixt Resmi Web Sayfası](https://blixtwallet.com/)
- [Blixt Github sayfası](https://github.com/hsjoberg/blixt-Wallet/)
- [Blixt Özellikleri sayfası](https://blixtwallet.github.io/features) - her bir özelliği ve işlevselliği tek tek açıklar.
- [Blixt SSS sayfası](https://blixtwallet.github.io/faq) - Blixt'in Soru-Cevap ve sorun giderme listesi
- [Blixt Kılavuzları sayfası](https://blixtwallet.github.io/guides) - Blixt için demolar, video eğitimleri, ekstra kılavuzlar ve kullanım örnekleri
- İndirin: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK doğrudan indir](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Doğrudan destek için Telegram grubu](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Geyser kitlesel fonlama sayfası] (https://geyser.fund/project/blixt) - projeyi desteklemek için istediğiniz gibi Sats bağışında bulunun
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - anonim LN sohbeti
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - tanıtım videosu (LN'ü ilk kullanımınızı test edebilirsiniz)
- [Çeşitli dillerde Blixt'i kullanarak ilk adımları içeren yazdırılabilir A4 broşür](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt ayrıca gerçek dünyada kullanmaya başlamadan önce tam bir deneyim testine sahip olmak için web sitesinde veya özel bir sürüm web'de tam işlevsel bir demo] (https://blixt-Wallet-git-master-hsjoberg.vercel.app/) sunar.


---
**İDDİANAME:**


*Bu uygulamanın geliştiricileri tarafından herhangi bir şekilde ödeme almıyorum veya desteklenmiyorum. Bu kılavuzu yazdım çünkü bu Wallet uygulamasına olan ilginin arttığını ve yeni kullanıcıların hala nasıl başlayacaklarını anlamadıklarını gördüm. Ayrıca Hampus'a (ana geliştirici) bu Wallet düğümünün kullanımıyla ilgili belgelerde yardımcı olmak için.*


*Bu LN uygulamasının tanıtımında, Bitcoin ve LN'in benimsenmesini ilerletmekten başka bir çıkarım yok. Tek yol bu!*


---