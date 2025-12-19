---
name: Bitcoin Core (Linux)
description: Linux üzerinde Bitcoin core ile kendi düğümünüzü çalıştırma
---

![cover](assets/cover.webp)


## Bitcoin core ile kendi düğümünüzü çalıştırma


Linux üzerinde kapsamlı bir kurulum kılavuzu ile tamamlanan Bitcoin'e ve düğüm kavramına giriş.


Bitcoin'ün en heyecan verici yönlerinden biri, programı kendi başına çalıştırabilme ve böylece ağa ve Ledger kamu işleminin doğrulanmasına ayrıntılı bir düzeyde katılabilme yeteneğidir.


Açık kaynaklı bir proje olan Bitcoin, 2009 yılından bu yana ücretsiz olarak erişilebilir ve herkese açık olarak dağıtılmaktadır. Kuruluşundan yaklaşık 17 yıl sonra, Bitcoin artık güçlü bir organik ağ etkisinden yararlanan sağlam ve durdurulamaz bir dijital para ağıdır. Çabaları ve vizyonları için Satoshi Nakamoto minnettarlığımızı hak ediyor. Bu arada, Bitcoin whitepaper'ını Agora 256'da (not: üniversitede de) barındırıyoruz.


### Kendi bankanız olmak


Kendi node'unuzu çalıştırmak Bitcoin ethos'una bağlı olanlar için elzem hale gelmiştir. Kimseden izin almadan Blockchain'i en baştan indirmek ve böylece A'dan Z'ye tüm işlemleri Bitcoin protokolüne göre doğrulamak mümkündür.


Program ayrıca kendi Wallet'unu da içeriyor. Böylece, herhangi bir aracı veya üçüncü taraf olmadan ağın geri kalanına gönderdiğimiz işlemler üzerinde kontrol sahibi oluruz. Siz kendi bankanızsınız.


Bu nedenle bu makalenin geri kalanı, özellikle Ubuntu ve Pop!OS gibi Debian uyumlu Linux dağıtımlarında en yaygın kullanılan Bitcoin yazılım sürümü olan Bitcoin core'in kurulumuna ilişkin bir rehberdir. Bireysel egemenliğinize bir adım daha yaklaşmak için bu kılavuzu izleyin.


## Debian/Ubuntu için Bitcoin core Kurulum Kılavuzu


**Önkoşullar**


- Minimum 6GB veri depolama alanı (pruned düğümü) - 1TB veri depolama alanı (Full node)
- İlk Blok İndirme* (IBD) işleminin en az 24 saat sürmesini bekleyin. Bu işlem bir pruned düğümü için bile zorunludur.
- Bir pruned düğümü için bile IBD için ~600GB bant genişliğine izin verin.


**Not: 💡** aşağıdaki komutlar Bitcoin core sürüm 24.1 için önceden tanımlanmıştır.


### Dosyaları İndirme ve Doğrulama



- [Download](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz` dosyasının yanı sıra `SHA256SUMS` ve `SHA256SUMS.asc` dosyaları (tabii ki yazılımın en son sürümünü indirmeniz gerekiyor).



- İndirilen dosyaların bulunduğu dizinde bir terminal açın. Örnek: `cd ~/Downloads/`.



- Sürüm dosyasının sağlama toplamının `sha256sum --ignore-missing --check SHA256SUMS` komutunu kullanarak sağlama toplamı dosyasında listelendiğini doğrulayın.



- Bu komutun çıktısı, indirilen sürüm dosyasının adını ve ardından `Tamam` ifadesini içermelidir. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Git`i `sudo apt install git` komutunu kullanarak yükleyin. Ardından, `git clone https://github.com/Bitcoin-core/guix.sigs` komutunu kullanarak Bitcoin core imzalayıcılarının PGP anahtarlarını içeren depoyu klonlayın.



- Tüm imzalayanların PGP anahtarlarını `gpg --import guix.sigs/builder-keys/*` komutunu kullanarak içe aktarın



- Sağlama toplamı dosyasının imzalayanların PGP anahtarlarıyla imzalandığını `gpg --verify SHA256SUMS.asc` komutunu kullanarak doğrulayın.



Her geçerli imza ile başlayan bir satır görüntülenecektir: `gpg: İyi imza` ve ile biten başka bir satır: `Birincil anahtar parmak izi: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (Pieter Wuille'in PGP anahtar parmak izi örneği).


**Not💡:** tüm imzalayıcı anahtarlarının "OK" döndürmesi gerekli değildir. Aslında, sadece bir tanesi gerekli olabilir. PGP doğrulaması için kendi doğrulama eşiğini belirlemek kullanıcıya bağlıdır.


Uyarıları görmezden gelebilirsiniz:



- 'Bu anahtar güvenilir bir imza ile onaylanmamıştır!



- "İmzanın sahibine ait olduğuna dair hiçbir belirti yok


### Bitcoin core grafiksel Interface'ün kurulumu



- Terminalde, hala Bitcoin core sürüm dosyasının bulunduğu dizinde, arşivde bulunan dosyaları çıkarmak için `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` komutunu kullanın.



- Önceden ayıklanmış dosyaları `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*` komutunu kullanarak yükleyin



- Gerekli bağımlılıkları `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev` komutunu kullanarak yükleyin



- Bitcoin-qt` komutunu kullanarak _bitcoin-qt_ (Bitcoin core grafiksel Interface) başlatın.



- Bir pruned düğümü seçmek için _Limit Blockchain storage_ seçeneğini işaretleyin ve depolanacak veri sınırını yapılandırın:


![welcome](assets/fr/02.webp)


### Bölüm 1'in Sonucu: Kurulum Kılavuzu


Bitcoin core kurulduktan sonra, işlemleri doğrulayarak ve diğer eşlere yeni bloklar ileterek Bitcoin ağına katkıda bulunmak için mümkün olduğunca çalışır durumda tutulması önerilir.


Bununla birlikte, sadece alınan ve gönderilen işlemleri doğrulamak için bile düğümünüzü aralıklı olarak çalıştırmak ve senkronize etmek iyi bir uygulama olmaya devam etmektedir.


![Creation wallet](assets/fr/03.webp)


## Bir Bitcoin core Düğümü için Tor Yapılandırma


**Not💡:** Bu kılavuz Ubuntu/Debian uyumlu Linux dağıtımlarında Bitcoin core 24.0.1 için tasarlanmıştır.


### Bitcoin core için Tor'un yüklenmesi ve yapılandırılması


İlk olarak, anonim iletişim için kullanılan bir ağ olan Tor hizmetini (The Onion Router) yüklememiz gerekiyor, bu da Bitcoin ağıyla etkileşimlerimizi anonimleştirmemizi sağlayacak. Tor da dahil olmak üzere çevrimiçi gizlilik koruma araçlarına giriş için bu konudaki makalemize bakın.


Tor'u yüklemek için bir terminal açın ve `sudo apt -y install tor` yazın. Kurulum tamamlandığında, hizmet normalde arka planda otomatik olarak başlatılacaktır. Doğru çalışıp çalışmadığını `sudo systemctl status tor` komutuyla kontrol edin. Yanıt `Active: active (exited)` göstermelidir. Bu işlevden çıkmak için `Ctrl+C` tuşlarına basın.


**İpucu:** Her durumda, Tor'u başlatmak, durdurmak veya yeniden başlatmak için terminalde aşağıdaki komutları kullanabilirsiniz:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Daha sonra, `Bitcoin-qt` komutuyla Bitcoin core grafiksel Interface'ı başlatalım. Ardından, bağlantılarımızı bir Tor proxy üzerinden yönlendirmek için yazılımın otomatik özelliğini etkinleştirin: ayarlar > Ağ_ ve buradan _SOCKS5 proxy (varsayılan proxy)_ üzerinden bağlan ve _Tor onion hizmetleri üzerinden eşlere ulaşmak için ayrı bir SOCKS5 proxy kullan_ seçeneklerini işaretleyin.


![option](assets/fr/04.webp)


Bitcoin core Tor'un kurulu olup olmadığını otomatik olarak algılar ve kurulu ise varsayılan olarak IPv4/IPv6 ağlarını (clearnet) kullanan düğümlere bağlantılara ek olarak Tor kullanan diğer düğümlere de giden bağlantılar oluşturur.


**Not💡:** Ekran dilini Fransızca olarak değiştirmek için Ayarlar'daki Ekran sekmesine gidin.


### Gelişmiş Tor Yapılandırması (isteğe bağlı)


Bitcoin core'ü eşlerle bağlantı kurmak için yalnızca Tor ağını kullanacak şekilde yapılandırmak mümkündür, böylece düğümümüz aracılığıyla anonimliğimizi optimize ederiz. Grafiksel Interface'te bunun için yerleşik bir işlev olmadığından, manuel olarak bir yapılandırma dosyası oluşturmamız gerekecektir. Ayarlar'a ve ardından Seçenekler'e gidin.


![option 2](assets/fr/05.webp)


Burada, _Yapılandırma dosyasını aç_ seçeneğine tıklayın. Bitcoin.conf` metin dosyasına girdikten sonra, sadece `onlynet=onion` satırını ekleyin ve dosyayı kaydedin. Bu komutun etkili olması için Bitcoin core'i yeniden başlatmanız gerekir.


Daha sonra Tor hizmetini, Bitcoin core'nin bir proxy aracılığıyla gelen bağlantıları alabileceği şekilde yapılandıracağız, böylece ağdaki diğer düğümlerin makinemizin güvenliğinden ödün vermeden Blockchain verilerini indirmek için düğümümüzü kullanmasına izin vereceğiz.


Terminalde, Tor hizmeti yapılandırma dosyasına erişmek için `sudo nano /etc/tor/torrc` yazın. Bu dosyada `#ControlPort 9051` satırını bulun ve etkinleştirmek için `#` işaretini kaldırın. Şimdi dosyaya iki yeni satır ekleyin:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Dosyayı kaydederken çıkmak için `Ctrl+X > Y > Enter` tuşlarına basın. Terminale döndüğünüzde, `sudo systemctl restart tor` komutunu girerek Tor'u yeniden başlatın.


Bu yapılandırmayla, Bitcoin core ağdaki diğer düğümlerle yalnızca Tor ağı (Onion) üzerinden gelen ve giden bağlantılar kurabilecektir. Bunu onaylamak için _Window_ sekmesine ve ardından _Peers_ öğesine tıklayın.


![Nodes Window](assets/fr/06.webp)


### Ek Kaynaklar


Sonuç olarak, yalnızca Tor ağını (`onlynet=onion`) kullanmak sizi bir Sybil Attack'ye karşı savunmasız hale getirebilir. Bu nedenle bazıları bu tür riskleri azaltmak için çoklu ağ yapılandırmasını önermektedir. Ayrıca, daha önce belirtildiği gibi, yapılandırıldıktan sonra tüm IPv4/IPv6 bağlantıları Tor proxy üzerinden yönlendirilecektir.


Alternatif olarak, yalnızca Tor ağında kalmak ve bir Sybil Attack riskini azaltmak için, `addnode=trusted_address.onion` satırını ekleyerek `Bitcoin.conf` dosyanıza başka bir güvenilir düğümün Address'sini ekleyebilirsiniz. Birden fazla güvenilir düğüme bağlanmak istiyorsanız bu satırı birden fazla kez ekleyebilirsiniz.


Bitcoin düğümünüzün özellikle Tor ile etkileşimiyle ilgili günlüklerini görüntülemek için, `Bitcoin.conf` dosyanıza `debug=tor` ekleyin. Artık hata ayıklama günlüğünüzde, _Bilgi_ penceresinde _Ayıklama Dosyası_ düğmesiyle görüntüleyebileceğiniz ilgili Tor bilgilerine sahip olacaksınız. Bu günlükleri `bitcoind -debug=tor` komutuyla doğrudan terminalde görüntülemek de mümkündür.


**İpucu💡:** burada bazı ilginç bağlantılar var:


- [Tor ve Bitcoin ile ilişkisini açıklayan Wiki sayfası](https://en.Bitcoin.it/wiki/Tor)
- [Jameson Lopp tarafından Bitcoin core yapılandırma dosyası oluşturucu](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Jon Atack tarafından hazırlanan Tor yapılandırma kılavuzu](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Her zaman olduğu gibi, herhangi bir sorunuz varsa, bunları Agora256 topluluğu ile paylaşmaktan çekinmeyin. Yarın bugün olduğumuzdan daha iyi olmak için birlikte öğreniyoruz!