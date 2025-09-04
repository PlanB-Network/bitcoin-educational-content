---
name: Bitcoin core (Linux)
description: Bitcoin core ile kendi düğümünüzü çalıştırma
---

![cover](assets/cover.webp)


# Bitcoin core ile kendi düğümünüzü çalıştırma


Linux üzerinde kapsamlı bir kurulum kılavuzu ile tamamlanan Bitcoin'e ve düğüm kavramına giriş.


Bitcoin'ün en heyecan verici önerilerinden biri, programı kendi başına çalıştırabilme ve böylece ağa ve Ledger kamu işleminin doğrulanmasına ayrıntılı bir düzeyde katılabilme yeteneğidir.


Açık kaynaklı bir proje olan Bitcoin, 2009 yılından bu yana halka açık ve ücretsiz olarak dağıtılmaktadır. Kuruluşundan yaklaşık 15 yıl sonra, Bitcoin şu anda güçlü bir organik ağ etkisinden yararlanan sağlam ve durdurulamaz bir dijital para ağıdır. Çabaları ve vizyonları için Satoshi Nakamoto minnettarlığımızı hak ediyor. Bu arada, Bitcoin whitepaper'ını Agora 256'da (not: üniversitede de) yayınlıyoruz.


## Kendi bankanız olmak


Kendi düğümünüzü çalıştırmak, Bitcoin aksiyomuna bağlı olanlar için elzem hale gelmiştir. Kimseden izin almadan Blockchain'i en baştan indirmek ve böylece A'dan Z'ye tüm işlemleri Bitcoin protokolüne göre doğrulamak mümkündür.


Program ayrıca kendi Wallet'unu da içeriyor. Böylece, herhangi bir aracı veya üçüncü taraf olmadan ağın geri kalanına gönderdiğimiz işlemler üzerinde kontrol sahibi oluruz. Siz kendi bankanızsınız.


Bu nedenle bu makalenin geri kalanı, özellikle Ubuntu ve Pop!/\_OS gibi Debian uyumlu Linux dağıtımlarında en yaygın kullanılan Bitcoin yazılım sürümü olan Bitcoin core'in kurulumuna ilişkin bir rehberdir. Bireysel egemenliğinize bir adım daha yaklaşmak için bu kılavuzu izleyin.


## Debian/Ubuntu için Bitcoin core Kurulum Kılavuzu


**Önkoşullar**


- Minimum 6GB veri depolama alanı (pruned düğümü) - 1TB veri depolama alanı (Full node)
- İlk Blok İndirmenin (IBD) tamamlanması için en az 24 saat bekleyin. Bu işlem bir pruned düğümü için bile zorunludur.
- Bir pruned düğümü için bile IBD için ~600GB bant genişliğine izin verin.


**Not: 💡** aşağıdaki komutlar Bitcoin core sürüm 24.1 için önceden tanımlanmıştır.


## Dosyaları İndirme ve Doğrulama


1. Bitcoin-24.1-x86_64-linux-gnu.tar.gz dosyasının yanı sıra SHA256SUMS ve SHA256SUMS.asc dosyalarını indirin. (https://bitcoincore.org/bin/Bitcoin-core-24.1/Bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. İndirilen dosyaların bulunduğu dizinde bir terminal açın. Örneğin, cd ~/Downloads/.

3. Sha256sum --ignore-missing --check SHA256SUMS komutunu kullanarak sürüm dosyasının sağlama toplamının sağlama toplamı dosyasında listelendiğini doğrulayın.

4. Bu komutun çıktısı, indirilen sürüm dosyasının adını ve ardından "OK" ibaresini içermelidir. Örnek: Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: TAMAM.

5. Sudo install git komutunu kullanarak git'i yükleyin. Ardından, git clone https://github.com/Bitcoin-core/guix.sigs komutunu kullanarak Bitcoin core imzalayıcılarının PGP anahtarlarını içeren depoyu klonlayın.

6. Gpg --import guix.sigs/builder-keys//\* komutunu kullanarak tüm imzalayıcıların PGP anahtarlarını içe aktarın

7. Gpg --verify SHA256SUMS.asc komutunu kullanarak sağlama toplamı dosyasının imzalayanların PGP anahtarlarıyla imzalandığını doğrulayın.


Her imza: gpg: Good signature ile başlayan bir satır ve Primary key fingerprint ile biten başka bir satır döndürecektir: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (Pieter Wuille'in PGP anahtar parmak izi örneği).


**Not💡:** tüm imzalayıcı anahtarlarının "OK" döndürmesi gerekli değildir. Aslında, sadece bir tanesi gerekli olabilir. PGP doğrulaması için kendi doğrulama eşiğini belirlemek kullanıcıya bağlıdır.


UYARI mesajlarını görmezden gelebilirsiniz:


- 'Bu anahtar güvenilir bir imza ile onaylanmamıştır!
- "İmzanın sahibine ait olduğuna dair hiçbir belirti yok


## Bitcoin core grafiksel Interface'ün kurulumu


1. Terminalde, hala Bitcoin core sürüm dosyasının bulunduğu dizinde, arşivde bulunan dosyaları çıkarmak için tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz komutunu kullanın.


2. Sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/\* komutunu kullanarak önceden ayıklanmış dosyaları yükleyin


3. Sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev komutunu kullanarak gerekli bağımlılıkları yükleyin


4. Bitcoin-qt komutunu kullanarak Bitcoin-qt'yi (Bitcoin core grafiksel Interface) başlatın.


5. Bir pruned düğümü seçmek için Blockchain depolamayı sınırla seçeneğini işaretleyin ve depolanacak veri sınırını yapılandırın:


![welcome](assets/1.webp)


## Bölüm 1'in Sonucu: Kurulum Kılavuzu


Bitcoin core kurulduktan sonra, işlemleri doğrulayarak ve diğer eşlere yeni bloklar ileterek Bitcoin ağına katkıda bulunmak için mümkün olduğunca çalışır durumda tutulması önerilir.


Bununla birlikte, sadece alınan ve gönderilen işlemleri doğrulamak için bile düğümünüzü aralıklı olarak çalıştırmak ve senkronize etmek iyi bir uygulama olmaya devam etmektedir.


![Creation wallet](assets/2.webp)


# Bir Bitcoin core Düğümü için Tor Yapılandırma


**Not💡:** Bu kılavuz Ubuntu/Debian uyumlu Linux dağıtımlarında Bitcoin core 24.0.1 için tasarlanmıştır.


## Bitcoin core için Tor'un yüklenmesi ve yapılandırılması


İlk olarak, anonim iletişim için kullanılan bir ağ olan Tor hizmetini (The Onion Router) yüklememiz gerekiyor, bu da Bitcoin ağıyla etkileşimlerimizi anonimleştirmemizi sağlayacak. Tor da dahil olmak üzere çevrimiçi gizlilik koruma araçlarına giriş için bu konudaki makalemize bakın.


Tor'u yüklemek için bir terminal açın ve sudo apt -y install tor komutunu girin. Kurulum tamamlandığında, hizmet normalde arka planda otomatik olarak başlatılacaktır. Sudo systemctl status tor komutu ile doğru çalışıp çalışmadığını kontrol edin. Yanıt Aktif: aktif (çıktı) göstermelidir. Bu işlevden çıkmak için Ctrl+C tuşlarına basın.


**İpucu:** Her durumda, Tor'u başlatmak, durdurmak veya yeniden başlatmak için terminalde aşağıdaki komutları kullanabilirsiniz:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Ardından, Bitcoin core grafiksel Interface'ı Bitcoin-qt komutuyla başlatalım. Ardından, bağlantılarımızı bir Tor proxy üzerinden yönlendirmek için yazılımın otomatik özelliğini etkinleştirin: Ayarlar > Ağ ve buradan SOCKS5 proxy üzerinden bağlan (varsayılan proxy) ve Tor onion hizmetleri üzerinden eşlere ulaşmak için ayrı bir SOCKS5 proxy kullan seçeneklerini işaretleyebiliriz.


![option](assets/3.webp)


Bitcoin core Tor'un kurulu olup olmadığını otomatik olarak algılar ve kurulu ise varsayılan olarak IPv4/IPv6 ağlarını (clearnet) kullanan düğümlere bağlantılara ek olarak Tor kullanan diğer düğümlere de giden bağlantılar oluşturur.


**Not💡:** Ekran dilini Fransızca olarak değiştirmek için Ayarlar'daki Ekran sekmesine gidin.


## Gelişmiş Tor Yapılandırması (isteğe bağlı)


Bitcoin core'ü eşlerle bağlantı kurmak için yalnızca Tor ağını kullanacak şekilde yapılandırmak mümkündür, böylece düğümümüz aracılığıyla anonimliğimizi optimize ederiz. Grafiksel Interface'te bunun için yerleşik bir işlev olmadığından, manuel olarak bir yapılandırma dosyası oluşturmamız gerekecektir. Ayarlar'a ve ardından Seçenekler'e gidin.


![option 2](assets/4.webp)


Burada, Yapılandırma dosyasını aç'a tıklayın. Bitcoin.conf metin dosyasına girdikten sonra, onlynet=onion satırını ekleyin ve dosyayı kaydedin. Bu komutun etkili olması için Bitcoin core'i yeniden başlatmanız gerekir.

Daha sonra Tor hizmetini, Bitcoin core'nin bir proxy aracılığıyla gelen bağlantıları alabileceği şekilde yapılandıracağız, böylece ağdaki diğer düğümlerin makinemizin güvenliğinden ödün vermeden Blockchain verilerini indirmek için düğümümüzü kullanmasına izin vereceğiz.


Tor hizmeti yapılandırma dosyasına erişmek için terminalde sudo nano /etc/tor/torrc komutunu girin. Bu dosyada #ControlPort 9051 satırını bulun ve etkinleştirmek için # işaretini kaldırın. Şimdi dosyaya iki yeni satır ekleyin: HiddenServiceDir /var/lib/tor/Bitcoin-service/ ve HiddenServicePort 8333 127.0.0.1:8334. Dosyayı kaydederken çıkmak için Ctrl+X > Y > Enter tuşlarına basın. Terminale döndüğünüzde sudo systemctl restart tor komutunu girerek Tor'u yeniden başlatın.


Bu yapılandırmayla, Bitcoin core ağdaki diğer düğümlerle yalnızca Tor ağı (Onion) üzerinden gelen ve giden bağlantılar kurabilecektir. Bunu onaylamak için Pencere sekmesine ve ardından Eşler'e tıklayın.


![Nodes Window](assets/5.webp)


## Ek Kaynaklar


Sonuç olarak, yalnızca Tor ağını kullanmak (onlynet=onion) sizi bir Sybil saldırısına karşı savunmasız hale getirebilir. Bu nedenle bazıları bu tür riskleri azaltmak için çoklu ağ yapılandırmasını önermektedir. Ayrıca, daha önce belirtildiği gibi, yapılandırıldıktan sonra tüm IPv4/IPv6 bağlantıları Tor proxy üzerinden yönlendirilecektir.


Alternatif olarak, yalnızca Tor ağında kalmak ve Sybil saldırısı riskini azaltmak için, addnode=trusted_address.onion satırını ekleyerek başka bir güvenilir düğümün Address'ini Bitcoin.conf dosyanıza ekleyebilirsiniz. Birden fazla güvenilir düğüme bağlanmak istiyorsanız bu satırı birden fazla kez ekleyebilirsiniz.


Bitcoin düğümünüzün özellikle Tor ile etkileşimiyle ilgili günlüklerini görüntülemek için Bitcoin.conf dosyanıza debug=tor ekleyin. Artık hata ayıklama günlüğünüzde, Bilgi penceresinde Hata Ayıklama Dosyası düğmesiyle görüntüleyebileceğiniz ilgili Tor bilgilerine sahip olacaksınız. Bu günlükleri bitcoind -debug=tor komutuyla doğrudan terminalde görüntülemek de mümkündür.


**İpucu💡:** burada bazı ilginç bağlantılar var:


- Tor'u ve Bitcoin ile ilişkisini açıklayan Wiki sayfası
- Jameson Lopp tarafından Bitcoin core yapılandırma dosyası oluşturucu
- Jon Atack tarafından hazırlanan Tor yapılandırma kılavuzu


Her zaman olduğu gibi, herhangi bir sorunuz varsa, bunları Agora256 topluluğu ile paylaşmaktan çekinmeyin. Yarın bugün olduğumuzdan daha iyi olmak için birlikte öğreniyoruz!