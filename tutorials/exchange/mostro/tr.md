---
name: Mostro
description: Lightning ve Nostr aracılığıyla KYC içermeyen Bitcoin P2P değişim platformu
---

![cover](assets/cover.webp)



Finansal egemenliğinizden ödün vermeden nasıl bitcoin alır veya satarsınız? Merkezi platformlar, keyfi hesap dondurma veya devlet gözetimi olasılığı ile kişisel verilerinizi açığa çıkaran invaziv KYC prosedürleri uygular.



**Mostro P2P**, Lightning Network, Nostr protokolü ve fatura tutmayı birleştiren merkezi olmayan bir alternatif sunar. En önemli yeniliği: bitcoinlerinizin borsa boyunca kontrolünüz altında kaldığı, hırsızlık, borsa iflası veya keyfi el koyma riskini ortadan kaldıran otomatik bir emanet sistemi.



## Mostro P2P nedir?



Mostro P2P, 2021 yılında piyasaya sürülen popüler Telegram botu **lnp2pbot**'un geliştiricisi **grunch** tarafından oluşturulan açık kaynaklı bir Bitcoin değişim protokolüdür. Lnp2pbot, Lightning aracılığıyla KYC içermeyen P2P borsalarını zaten etkinleştirmiş olsa da, büyük bir güvenlik açığı sundu: **Telegram, hükümetler tarafından sansüre açık merkezi bir arıza noktası** oluşturmaktadır.



Mostro, bu konseptin **merkezsizleştirilmiş evrimini** temsil etmektedir: Telegram'ı **Nostr** protokolü (dağıtılmış rölelerden oluşan ölçülemez bir ağ) ile değiştirerek Mostro, bu sistemik riski ortadan kaldırmaktadır. Protokol, anlık işlemler için Lightning Network'yi, sansüre dayanıklı iletişim için Nostr'u ve gerçekten gözetim dışı otomatik bir emanet oluşturmak için **fatura tutma** özelliğini birleştirir.



### Teknik mimari



Mostro üç bileşen üzerinden çalışır:




- Daemon Mostrod**: kullanıcılar ve Lightning Network arasındaki alışverişleri koordine eder
- Lightning** düğümü: bekletilen faturaları oluşturur (~24 saat kriptografik emanet)
- Mostro** müşterileri: kullanıcı arayüzleri (CLI, Mobil, Web)



Emirler Nostr'da herkese açık etkinlikler (tip 38383) olarak yayınlanırken, özel işlemler uçtan uca şifrelenmiş mesajlar (NIP-59, NIP-44) aracılığıyla iletilir. Her Mostro örneği kendi ücretlerini (genellikle %0,3 ile %1 arasında) ve işlem limitlerini (örneğe bağlı olarak birkaç bin ile birkaç yüz bin sats arasında değişir) tanımlar.



### Belirleyici avantajlar



**Sansüre dayanıklı**: Nostr röleleri dünyanın herhangi bir yerinde var olduğu sürece hiçbir hükümet Mostro'yu kapatamaz. Telegram aracılığıyla savunmasız lnp2pbot'un aksine Mostro, **sansüre dayanıklı** alışverişlere izin verir.



**Emanet dışı**: Lightning hold faturaları bitcoinlerinizi kalıcı olarak transfer etmeden kilitler. Paralarınız kontrolünüz altında kalır ve bir sorun olması durumunda (~24 saat) otomatik olarak size iade edilir.



**Tasarım gereği gizlilik**: İhtiyaçlarınıza uygun iki mod mevcuttur. İtibar Modu** kalıcı güven oluşturmak için itibarınızı Nostr anahtarınıza bağlar. Tam Özel Mod** tek kullanımlık geçici anahtarlarla mutlak anonimliği tercih eder.



## Ana Özellikler



**Merkezi olmayan iletişim**: Tüm siparişler kriptografik olarak imzalanmış etkinlikler aracılığıyla Nostr'da yayınlanır. Özel müzakereler, mutlak gizliliği garanti eden uçtan uca şifrelenmiş mesajlar aracılığıyla iletilir.



**İtibar sistemi**: nostr'da kalıcı olarak saklanan yinelemeli hesaplama ile 5 yıldızlı derecelendirme. Güvenilir bir tüccar olarak kademeli olarak itibar kazanmanızı sağlar.



**Merkezi olmayan tahkim**: Bir anlaşmazlık durumunda, tarafsız bir hakem kanıtları inceler ve şeffaf kriterlere göre bir karar verir. Her anlaşmazlık, izlenebilirlik için benzersiz bir token oluşturur.



**Ödeme esnekliği**: Yadio.io döviz kuru hizmeti aracılığıyla birçok fiat para birimi için destek. SEPA transferleri, PayPal, Revolut, nakit ve taraflar arasında kararlaştırılan herhangi bir yöntemi kabul eder.



## Mostro müşterileri mevcut



Mostro, P2P borsalarınız için iki ana operasyonel istemci sunar.



### Mostro CLI - Komut Satırı İstemcisi



Mostro CLI** en olgun ve işlevsel istemcidir. Rust'te yazılmış, bir komut satırı arayüzü aracılığıyla Mostro özelliklerinin tamamını sunar. MacOS, Linux ve Windows ile uyumludur.



**Ana kontroller** :




- `siparişleri listele`: Mevcut tüm siparişleri görüntüle
- `neworder` : Yeni bir alış veya satış emri oluşturun
- `takesell` / `takebuy`: Alış veya satış emri almak
- `fiatsent`: Fiat ödemesinin gönderilmesini onaylayın
- `release`: Emaneti serbest bırak ve değişimi tamamla
- `getdm`: Doğrudan mesajları görüntüle
- `rate` : Bir değişimden sonra karşı tarafınızı değerlendirin



Teknik kullanıcılar, otomasyon ve maksimum güvenlik gerektiren ortamlar için idealdir.



### Mostro Mobile - Akıllı telefon uygulaması



Alfa sürümündeki **mobil uygulama** doğrudan akıllı telefonunuzdan P2P ticareti yapmanızı sağlar. Sekmeli gezinme, emir görüntüleme, gelişmiş filtreler ve karşı taraflarınızla iletişim kurmak için entegre sohbet içeren sezgisel grafik Interface.



Android ** için kullanılabilir (GitHub'daki APK aracılığıyla), basitliği ve ara sıra mobil ticareti tercih eden kullanıcılar için en uygun seçimdir.



### Mostro-web - Interface web (geliştirme aşamasında)



Interface gelişmiş JavaScript web uygulaması aktif geliştirme aşamasındadır. Kapsamlı ticaret ve portföy yönetimi işlevleri ile eksiksiz bir kullanıcı deneyimi sunmak üzere tasarlanmıştır. Kurulum gerektirmeden tarayıcı üzerinden erişim.



## Kurulum ve yapılandırma



Bu eğitim, iki ana Mostro istemcisinin kurulumu ve kullanımı konusunda size rehberlik edecektir: CLI ve mobil uygulama.



### Temel ön koşullar



Başlamadan önce, ihtiyacınız olacak :





- Yeterli likiditeye sahip çalışan bir Lightning Network** wallet (veya Lightning uyumlu)
 - Tavsiye edilir: Phoenix, Breez, Wallet of Satoshi...
 - Test için minimum 1000 satoshis likidite



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Bir Nostr** özel anahtarı (format `nsec1...`)
 - Nostrkeygen.com](https://nostrkeygen.com/) adresinde özel bir ticaret anahtarı oluşturun
 - Önemli**: Ana kişisel Nostr anahtarınızı asla kullanmayın
 - Özel anahtarınızı güvenli bir yerde saklayın (şifre yöneticisi)





- İsteğe bağlı ama önerilir**: IP adresinizi maskelemek için VPN veya Tor bağlantısı



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Mostro CLI kurulumu



#### MacOS üzerinde



**1. Adım: Rust kontrolü**



Rust'in kurulu olup olmadığını kontrol edin (sürüm 1.64+ gereklidir):



```bash
rustc --version
```



Rust kurulu değilse :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Adım 2: Depoyu klonlama**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**3. Adım: Yapılandırma**



'yi kopyalayın ve düzenleyin:



```bash
cp .env-sample .env
```



.env` dosyasını açın ve ayarlarınızı yapılandırın:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**CLI/Mobil** senkronizasyonu için önemlidir: CLI ve mobil uygulamada aynı siparişlere erişmek için, her iki istemcide de **aynı Mostro Pubkey** ve **aynı Nostr rölelerini** kullanmanız gerekir. Bu ayarları mobil uygulamadaki Ayarlar'dan kontrol edin.



![Configuration .env](assets/fr/02.webp)



**Adım 4: Kurulum**



CLI'i derleyin ve kurun:



```bash
cargo install --path .
```



Derleme 1-2 dakika sürer. Mostro-cli` çalıştırılabilir dosyası `~/.cargo/bin/` dosyasına yüklenecektir.



![Installation du CLI](assets/fr/03.webp)



**Adım 5: Kontrol Et**



Her şeyin çalışıp çalışmadığını kontrol edin:



```bash
mostro-cli --help
```



Siparişlerin tam listesini görmelisiniz.



![Vérification avec --help](assets/fr/04.webp)



#### Linux üzerinde (Ubuntu/Debian)



'nin eklenmesiyle macOS ile aynı şekilde kurulur:



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Ardından macOS bölümündeki 3. ve 4. adımları izleyin.



#### Windows üzerinde



Önce [rustup.rs] (https://rustup.rs/) üzerinden Rust'yi yükleyin, ardından PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Aynı yapılandırma: `.env-sample` dosyasını `.env` dosyasına kopyalayın ve parametrelerinizi girin.



### Mostro Mobile'ı Yükleme



#### Android'de



**Adım 1**: GitHub sürümleri sayfasına] (https://github.com/MostroP2P/mobile/releases) gidin ve **app-release.apk** dosyasını indirin (yaklaşık 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**2. Adım: İndirdikten sonra, APK dosyasını indirilenler bölümünden açın. Android sizden bu kaynaktan yüklemeye izin vermenizi isteyecektir.



![Téléchargement et installation APK](assets/fr/11.webp)



**Adım 3**: İşlevleri sunan ilk katılım ekranlarını takip edin:




- Bitcoin ile serbestçe ticaret yapın - KYC yok** : Nostr sayesinde kimlik doğrulaması olmadan ticaret yapın
- Varsayılan olarak gizlilik**: İtibar modu ve Tam gizlilik modu arasında seçim yapın
- Her adımda güvenlik**: Gözetim dışı bekletme faturaları ile koruma



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Adım 4**: Keşfetmek için katılıma devam edin :




- Tamamen şifrelenmiş sohbet**: Uçtan uca şifrelenmiş iletişim
- Bir teklif alın**: Sipariş defterine göz atın ve bir teklif seçin
- İhtiyacınız olanı bulamıyor musunuz? Kendi özelleştirilmiş siparişinizi oluşturun



![Suite onboarding](assets/fr/13.webp)



**Adım 5: İlk katılım tamamlandığında, uygulama otomatik olarak bir çift Nostr anahtarı oluşturur. Menüye (☰) ve ardından **Secret Words** (kurtarma cümlesi) kaydetmek için **Account** seçeneğine gidin. Ayrıca bu ekranda daha önce bahsedilen gizlilik modunu değiştirme seçeneğiniz de vardır.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Önemli**: Kurtarma cümlenizi güvenli bir yere yazın (şifre yöneticisi, kağıt kasa).



### İlk güvenlik yapılandırması



Hangi platformu kullanırsanız kullanın :





- Özel anahtar**: Ticaret için ayrı bir Nostr kimliği kullanın
- Küçük miktarlar**: Başlamak için sats 10.000'den az bir miktarla başlayın
- Çoklu röleler**: Coğrafi olarak farklı 3-5 röle yapılandırın
- Ağ koruması**: IP adresinizi gizlemek için VPN veya Tor'u etkinleştirin
- Wallet güvenli**: wallet Lightning'inizin otomatik kilitlenmesini etkinleştirin



## CLI ile kullanın



Bu bölümde, Mostro CLI aracılığıyla bitcoin satın alma işlemi gerçek hayattaki bir kullanım örneğine göre gösterilmektedir.



### Adım 1: Mevcut siparişleri listeleyin



Listorders` komutu tüm aktif emirleri görüntüler:



```bash
mostro-cli listorders
```



Her siparişin ayrıntılarını içeren bir tablo göreceksiniz: Kimlik, tür (alış/satış), tutar, para birimi, ödeme yöntemi.



![Liste des ordres disponibles](assets/fr/05.webp)



Bu örnekte, Revolut üzerinden 5 EUR satmak için bir emir görülmektedir (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Adım 2: Siparişin alınması



Bu bitcoinleri satın almak için `takesell` ile sipariş alın:



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro, BTC'yi almak için sizden bir **Yıldırım faturası** sağlamanızı isteyecektir. Satoshi cinsinden tam miktar belirtilir (burada: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Adım 3: Lightning faturanızı sağlayın



wallet'inizden (Phoenix, Breez, vb.) tam tutar için bir Lightning faturası oluşturun ve ardından gönderin:



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Sistem gönderiyi onaylar ve emaneti etkinleştirmeden önce satıcının bekletme faturasını ödemesini beklemenizi söyler.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Adım 4: Satıcıyla iletişime geçin



Emanet etkinleştirildikten sonra, satıcıdan ödeme ayrıntılarını istemek için `dmtouser` kullanın:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Adım 5: Cevabı alın



Satıcının yanıtını görmek için doğrudan mesajları kontrol edin:



```bash
mostro-cli getdm
```



Satıcı size ödeme kimliğini verir (burada Revtag: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Adım 6: Fiat ödemesinin yapılması



Ödemeyi kararlaştırılan yöntemle (bu örnekte Revolut) verilen iletişim bilgilerine gönderin. **Tüm destekleyici belgeleri saklayın** (ekran görüntüleri, işlem referansları).



### Adım 7: Ödeme gönderimini onaylayın



Ödeme yapıldıktan sonra Mostro'yu bilgilendirin:



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Adım 8: Bitcoinlerin alınması



Satıcı fiatın alındığını onaylar onaylamaz ve `release` komutuyla emaneti serbest bırakır bırakmaz, verdiğiniz Lightning faturasındaki bitcoinlerinizi anında alırsınız.



### Adım 9: Değerlendirme



Merkezi olmayan itibara katkıda bulunmak için satıcıya puan verin:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Yararlı komutlar



**Bir siparişi iptal edin** (alınmadan önce) :


```bash
mostro-cli cancel -o <order-id>
```



**Yeni bir satış siparişi oluşturun** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**İhtilaf açın** :


```bash
mostro-cli dispute -o <order-id>
```



## Mobil uygulama ile kullanım



Bu bölümde, Mostro Mobile aracılığıyla bitcoin satışını gerçek hayattan bir kullanım örneğini takip ederek gösterilmektedir.



### Interface ana



Uygulama 3 ana sekmeye sahiptir:





- Sipariş Defteri**: Mevcut alış (BTC AL) ve satış (BTC SAT) emirlerine göz atın
- İşlemlerim**: Aktif ve geçmiş emirlerinizi görüntüleyin
- Sohbet**: Rakamları kullanarak karşı taraflarınızla iletişim kurun



![Interface principale](assets/fr/14.webp)



### Önerilen yapılandırma



İşlem yapmadan önce, menü (☰) > **Ayarlar** üzerinden birkaç ayarı yapılandırın:





- Lightning Address** (isteğe bağlı): Ödemeleri doğrudan almak için
- Röleler**: Esneklik için birkaç Nostr rölesi ekleyin (örneğin `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Kullandığınız Mostro örneğinin ortak anahtarını kontrol edin



![Paramètres de l'application](assets/fr/16.webp)



**CLI/Mobil senkronizasyonu için önemlidir**: Hem CLI hem de mobil uygulamayı kullanıyorsanız, her iki istemcide de **tam olarak aynı Nostr rölelerini ve Mostro Pubkey'i** yapılandırın. Bu özdeş yapılandırma olmadan, her iki arayüzde de aynı siparişleri göremezsiniz. Ayarlar'da (yukarıdaki ekran görüntüsü) görünen röleler ve Mostro Pubkey, CLI `.env' dosyanızdakilerle eşleşmelidir.



### Adım 1: Bir satış emri oluşturun



Sağ alttaki yeşil **"+"** düğmesine basın, ardından **SAT** (kırmızı düğme) öğesini seçin.



![Boutons de création d'ordre](assets/fr/17.webp)



Oluşturma formunu doldurun :



1. **Para Birimi**: Almak istediğiniz para birimini seçin (EUR, USD, vb.)


2. **Tutar** : Fiat cinsinden tutarı girin (örn. 1 ila 3 EUR)


3. **Ödeme yöntemleri** : Yöntemi seçin (örn. "Revolut")


4. **Fiyat türü**: "Piyasa Fiyatı "nı seçin


5. **Premium**: Primi ayarlayın (-%10 ile +%10 arasında kaydırıcı, önerilen: hızlı satmak için %0)



Siparişinizi yayınlamak için **Gönder** düğmesine basın.



### Adım 2: Yayın onayı



Siparişiniz şimdi yayınlandı! 24 saat boyunca kullanılabilir olacaktır. Bir alıcı almadan önce `cancel` komutunu çalıştırarak istediğiniz zaman iptal edebilirsiniz.



![Ordre publié](assets/fr/18.webp)



Emir, **İşlemlerim** sekmesinde "Beklemede" durumu ve "Sizin tarafınızdan oluşturuldu" rozeti ile görünür.



### 3. Adım: Bir alıcı siparişinizi alır



Bir alıcı siparişinizi aldığında, bir bildirim alırsınız. Ayrıntıları **Ticaretlerim** bölümünde görebilirsiniz.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Önemli talimat**: Bitcoin'lerinizi (burada 1-5 EUR için 4674 sats) emanete almak için şimdi **görüntülenen tutma faturasını** ödemelisiniz. En fazla **15 dakikanız** var, aksi takdirde değişim iptal edilecektir.



Bekletme faturasını kopyalayın ve wallet Lightning (Phoenix, Breez, vb.) cihazınızdan ödeyin.



### Adım 4: Alıcı ile iletişim kurun



Emanet etkinleştirildikten sonra, alıcıyla şifreli sohbeti açmak için **CONTACT** tuşuna basın.



Alıcı (burada "anonymous-gloriaZhao") ödeme bilgilerinizi istemek için sizinle iletişime geçecektir. Lütfen bilgilerinizle (Revtag, IBAN, vb.) yanıt verin.



![Chat avec l'acheteur](assets/fr/20.webp)



### Adım 5: Fiat ödemesinin alınması



Revolut hesabınıza (veya kararlaştırılan diğer yönteme) fiat ödemesi gelene kadar bekleyin. **Dikkatlice kontrol edin**:




- Kesin miktar
- Gönderen
- İstenirse referans



Alıcı, ödemeyi gönderdiğini sohbet yoluyla size bildirecektir. Mostro ayrıca fiatın size gönderildiğini onaylayan bir mesaj görüntüleyecektir.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Adım 6: Emaneti serbest bırakın



Fiat ödemesini hesabınıza aldığınızı **onayladıktan** sonra, yeşil **RELEASE** düğmesine basın ve satsları alıcıya göndermek için onaylayın.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoinler, Lightning faturası aracılığıyla alıcıya anında aktarılır.



### Adım 7: Değerlendirmeyi yapın



Serbest bıraktıktan sonra, alıcıyı derecelendirmek için **RATE** tuşuna basın. 1 ila 5 yıldız arasından seçim yapın (burada 5/5) ve **Değerlendirmeyi Gönder** düğmesine basın.



![Évaluation de la contrepartie](assets/fr/21.webp)



Takas sona erdi!



### Mobil uygulama ile bitcoin satın alın



Bitcoin **satın alma** süreci benzerdir ancak tersine çevrilmiştir:



1. Satış siparişlerini görüntülemek için **Sipariş Defteri** > **BUY BTC** sekmesine göz atın


2. Ayrıntıları görüntülemek için ilginç bir siparişin üzerine tıklayın


3. Sipariş Al** tuşuna basın


4. Lightning faturanızı sağlayın (wallet'unuzdan oluşturulmuş)


5. Satıcının emaneti etkinleştirmesini bekleyin


6. Ödeme detayları için **CONTACT** üzerinden satıcıyla iletişime geçin


7. Fiat ödemesi gönderin (kanıtı saklayın)


8. Satıcı doğrulamadan sonra emaneti serbest bırakır


9. Lightning faturanız üzerinden anında bitcoin alın


10. Satıcıyı değerlendirin (1-5 yıldız)



### Sorun yönetimi



**Bir emri iptal edin**: İşlemlerim** bölümünde, siparişinize ve ardından **İPTAL** düğmesine basın (yalnızca alınmadan önce kullanılabilir).



**Bir anlaşmazlık açın**: Bir anlaşmazlık ortaya çıkarsa, sipariş ayrıntılarında **ANLAŞMAZLIK** düğmesine basın. Tüm kanıtları ekleyin (sohbet ekran görüntüleri, banka işlem referansları).



## Avantajlar ve sınırlamalar



### Avantajlar



**Finansal egemenlik**: Fatura tutma mekanizması sayesinde bitcoinleriniz asla doğrudan kontrolünüzden çıkmaz ve borsa iflası veya korsanlık riskini ortadan kaldırır.



**Sansüre dayanıklıdır**: Hiçbir otorite ağı kapatamaz veya emirlerinizi sansürleyemez. Sistem Nostr röleleri çalışır durumda olduğu sürece çalışır.



**Varsayılan anonimlik**: KYC veya kişisel veriler olmadan yalnızca takma bir Nostr anahtarı sizi tanımlar. Uçtan uca şifrelenmiş iletişim.



**Ödeme esnekliği**: Karşılıklı olarak kabul edilen herhangi bir ödeme yöntemi mümkündür (transferler, mobil uygulamalar, nakit, takas).



### Sınırlamalar



**Erken geliştirme**: İlkel arayüzler ve teknik öğrenme eğrisi gereklidir.



**Sınırlı likidite**: Özellikle büyük miktarlar veya nadir para birimleri için sınırlı sayıda emir.



**Teknik gereksinimler**: Lightning ve Nostr hakkında temel bilgi gereklidir.



**Bireysel sorumluluk**: Sorun durumunda merkezi destek yok, dikkatli olunması gerekiyor.



## Sonuç



Mostro P2P, gerçekten merkezi olmayan ticaret için Lightning Network, Nostr ve otomatik emaneti birleştirerek merkezi borsalara umut verici bir alternatif sunuyor. Erken gelişimine ve sınırlı likiditesine rağmen, platform halihazırda finansal egemenlik, sansüre direnç ve varsayılan anonimlik sunuyor.



Özerklik ve gizliliği tercih eden bitcoin kullanıcıları için Mostro, ilerici keşiflere değer, uygulanabilir bir seçenektir. Merkezi olmayan mimarisi, ticari evrimden ziyade topluluğu garanti altına alarak gerçekten özgür Bitcoin borsalarının geleceğinin önünü açıyor.



## Kaynaklar



### Resmi belgeler




- [Mostro resmi web sitesi](https://mostro.network)
- [Teknik dokümantasyon](https://mostro.network/docs-english/index.html)
- [Mostro Vakfı](https://mostro.foundation)



### Kaynak kodu ve geliştirme




- [Ana GitHub deposu](https://github.com/MostroP2P/mostro)
- [Web istemcisi](https://github.com/MostroP2P/mostro-web)
- [Müşteri CLI](https://github.com/MostroP2P/mostro-cli)



### Topluluk




- [Nostr Protokolü](https://nostr.com)
- [Lightning Network Kılavuzları](https://lightning.network)