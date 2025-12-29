---
name: Coin Wallet
description: Coin Wallet ve gizlilik ve güvenliği artırma yolları hakkında eğitim
---

![cover](assets/cover.webp)


Bu eğitimde, mobil cihazlar için kendi kendini denetleyen bir kripto wallet olan [Coin Wallet] (https://coin.space/) ve mobil wallet uygulamalarını kullanırken güvenlik ve gizliliğin nasıl artırılacağı anlatılmaktadır.



## Coin Wallet Hakkında


**Coin Wallet**, 2015 yılında Bitcoin meraklılarından oluşan bir ekip tarafından oluşturulan kendi kendine gözetim / gözetim dışı, açık kaynaklı bir wallet'dir. Bir web uygulaması olarak başladı, ardından 2017'de iOS uygulaması ve 2020'de Android uygulaması - Google Play, Samsung Galaxy Store ve Huawei AppGallery'de mevcut.


Önemli avantajlar:


- Gözetim dışı mimari
- Tamamen [açık kaynak kodu](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Basit ve temiz tasarım
- Gereksiz özellikler olmadan kripto para birimini güvenli bir şekilde saklamak olan temel amaca odaklanmıştır
- Platformlar arası destek: mobil (iOS ve Android), masaüstü, web
- RBF (Ücretle Değiştir) desteği - takılan işlemleri istediğiniz zaman hızlandırın
- YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2 anahtarı ile donanım 2FA
- Dahili Tor desteği - maksimum gizlilik için tüm trafiği Tor ağı üzerinden yönlendirin



## 1️⃣ Coin'nin Kurulması Wallet

Coin Wallet tüm büyük platformlarda mevcuttur.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Tüm yayın bağlantıları](https://github.com/CoinSpace/CoinSpace/releases)


Masaüstü (Windows, Linux, macOS), web uygulaması olarak ve Tor üzerinden de kullanılabilir.


![image](assets/en/01.webp)


## 2️⃣ Bir Wallet Oluşturma ve PIN Ayarlama


Bir wallet, [2048 kelimelik bir listeden] (https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts) oluşturulan, boşluklarla ayrılmış 12 kelimelik rastgele bir dizi olan bir passphrase kullanılarak oluşturulur.

Coin Wallet, diğer cüzdanlardan içe aktarılan 12, 15, 18, 21 veya 24 kelimelik parolaları destekler.


passphrase, ana özel anahtarın insan tarafından okunabilir formudur. Güvenli bir şekilde kaydedilmelidir. passphrase, wallet'a erişmek veya geri yüklemek için gereken tek şeydir. passphrase kaybedilirse, wallet ve tüm fonlar kalıcı olarak kaybedilir. passphrase asla paylaşılmamalıdır. Coin Wallet anahtarları herhangi bir sunucuda veya veritabanında saklamaz.


**12 kelimelik bir passphrase güvenli mi?

Pozisyon başına 2048 olası kelime ile 2048¹² ≈ 10³⁹ kombinasyon vardır - Bitcoin özel anahtarlarıyla karşılaştırılabilir ~128 bit güvenlik sağlar. Bu seviye yaygın olarak yeterli kabul edilmektedir.


![image](assets/en/02.webp)


passphrase yazıldıktan ve onaylandıktan sonra, uygulama günlük erişim için **4 basamaklı bir PIN** ayarlamanızı ister. Daha fazla kolaylık için, PIN kullanmak yerine biyometrik kimlik doğrulamayı (parmak izi veya yüz tanıma) etkinleştirebilirsiniz.


![image](assets/en/03.webp)



Hesap yok, anahtar kurtarma yok, passphrase sıfırlama yok ve işlem tersine çevirme yok. Güvenlik tamamen kullanıcının sorumluluğundadır.


Anımsatıcı ifadenin kaydedilmesine ilişkin ayrıntılı en iyi uygulamalar için:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Parola + PIN. Ne Zaman ve Nasıl Kullanılırlar


**passphrase ne zaman gereklidir?

Sadece bu nadir durumlarda:


- wallet'yı yeni bir cihaza kurma
- Coin Wallet uygulamasını yeniden yükleme
- Uygulama/tarayıcı verilerini temizleme (Yerel Depolama)
- Bir donanım anahtarını hesaptan kaldırma
- Üç kez yanlış PIN girmek (uygulama güvenlik için kilitlenir)


Günlük kullanımda, wallet'un kilidini açmak için 4 haneli PIN yeterlidir.


**Parola + PIN: Nasıl Çalışır**

passphrase gerçek ana özel anahtardır ve tüm cihazlarda çalışır.

Her seferinde 12-24 kelime yazmak zahmetli olacağından, Coin Wallet mevcut cihazda hızlı, günlük erişim için 4 haneli bir PIN kullanır.

Basit bir PIN tek başına ana anahtarı doğrudan korumak için yeterince güvenli değildir, bu nedenle şifreleme için asla kullanılmaz. Bunun yerine:



- PIN sunucuya gönderilir ve uzun bir kriptografik token ile değiştirilir.
- Bu token, yalnızca cihazda depolanan şifrelenmiş ana anahtarın şifresini çözer.


PIN üç kez yanlış girilirse, sunucu token'yi kalıcı olarak siler. Yerel olarak saklanan anahtar kullanılamaz hale gelir ve wallet'yı kurtarmanın tek yolu orijinal passphrase'i girmektir.

Bu tasarım hem kolaylık hem de güçlü geri dönüş koruması sağlar.



## 4️⃣ ₿itcoin Alma - Address Türleri ve Gizlilik


Coin Wallet, üç Bitcoin adres formatının tümünü destekler:



- Yerel SegWit (Bech32)** - **bc1q** ile başlar - en düşük ücretler, önerilir
- İç içe geçmiş SegWit (P2SH)** - **3** ile başlar
- Eski (P2PKH)** - **1** ile başlar


![image](assets/en/04.webp)


**Her para yatırma işleminden sonra adres neden değişiyor?

Bu kasıtlıdır ve gizliliği korur. Her coin alındığında, Coin Wallet otomatik olarak yeni bir kullanılmayan adres oluşturur. Aynı adres tekrar kullanılırsa (örneğin aylık maaş için), herhangi biri bir blok zinciri gezgininde gelen tüm işlemleri kolayca toplayabilir ve toplam geliri öğrenebilir.


Eski adresler sonsuza kadar geçerli kalır - onlara hala alıcı gönderebilirsiniz - ancak her seferinde yeni bir adres kullanmak önerilen en iyi gizlilik uygulamasıdır.


**Bitcoin nasıl alınır:**

1. Madeni parayı açın

2. Al** öğesine dokunun

3. İstediğiniz adres türünü seçin (tercihen **bc1q** - `Native SegWit`)

4. QR kodunu gösterin veya adresi kopyalayın ve ödeyene gönderin


**Opsiyonel - Mecto (şahsen ödemeler için):**

Aynı Alım ekranında bir `Mecto` düğmesi vardır.

Açtığın zaman:


- Sizden bir **nickname** (gravatar) girmeniz istenecektir
- Geçerli konumunuz + alma adresiniz, Mecto'yu etkinleştirmiş olan diğer Coin Wallet kullanıcılarıyla geçici olarak paylaşılır
- Sizi küçük bir harita üzerinde keşfedebilir ve yazmadan veya taramadan para gönderebilirler


Veriler yalnızca diğer Mecto kullanıcıları tarafından görülebilir ve 1 saat sonra (veya kapattığınızda hemen) otomatik olarak silinir.

Mecto tamamen isteğe bağlıdır - maksimum gizlilik tercih ediyorsanız kapalı bırakın.


![image](assets/en/05.webp)


## 5️⃣ ₿itcoin Gönderme


Bitcoin'i göndermek için:


1. Madeni parayı açın → **Gönder** üzerine dokunun

2. Adresi yapıştırın veya QR kodunu tarayın

3. Tutarı girin (veya **Maks** öğesine dokunun)

4. İşlem hızını seçin:


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5. 4 haneli PIN kodunuzla onaylayın → işlem yayınlanır


### Bekleyen bir ₿itcoin işlemi nasıl hızlandırılır (RBF)


Yavaş bir ücret seçtiyseniz ve işlem takıldıysa:


1. Tarihçe** sekmesine gidin

2. Bekleyen işleme dokunun

3. Tap **Accelerate** (Ücret Karşılığı Değiştirme)

4. Onayla → işlem daha yüksek bir ücretle yeniden yayınlanacak


RBF hızlandırma şu anda aşağıdakiler için desteklenmektedir:

Bitcoin - Avalanche - Binance Akıllı Zincir - Ethereum - Ethereum Classic - Polygon


Replace-by-fee (RBF) hakkında daha fazla bilgi: https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Özel Anahtarları Dışa Aktarma


**Özel anahtara gerçekten ne zaman ihtiyaç duyarsınız?

(Kullanıcıların %99'u bunu asla yapmaz - 12 kelimelik passphrase yeterlidir)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Coin Wallet'de özel anahtarlar nasıl dışa aktarılır


1. Açık **Bitcoin (BTC)**

2. Sayfanın en altına kaydırın - **Özel anahtarları dışa aktar** öğesine dokunun

3. Uygulama, bakiyesi olan her adresi + özel anahtarını **WIF** formatında (5, K veya L ile başlar) ve bir QR kodu ile gösterir.


Yalnızca boş olmayan adresler görünür.


**Örnek WIF anahtarı**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Sonra ne yapmalı (tavsiye edilir)**


- Electrum, Sparrow, BlueWallet veya herhangi bir donanım wallet'ü açın
- Özel anahtarı içe aktarma/süpürme
- Tüm fonlar anında mevcut seed'ünüz altında yeni bir güvenli adrese taşınır


Özel anahtarı asla dijital olarak düz metin halinde saklamayın. Süpürme işleminden sonra güvenli bir şekilde silinebilir.


Özel anahtarlar ve türetme yolları hakkında eksiksiz bir kılavuz için: [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Teknik Ayrıntılar - BIP39, BIP32 ve Türetme Yolları


Coin Wallet, neredeyse tüm ciddi cüzdanlar tarafından kullanılan resmi Bitcoin standartlarını sıkı sıkıya takip eder.


`BIP39` - passphrase nasıl ana özel anahtar haline gelir


- Varsayılan kelime sayısı: 12
- İsteğe bağlı passphrase/parola: yok ("")
- Başlangıç entropisi: 128 bit (12 kelime) → 256 bit (24 kelime)
- Açık kaynak uygulaması: https://github.com/paulmillr/scure-bip39
- Kelime listesi: 2048 kelimeden oluşan standart İngilizce listesi
- Başka herhangi bir BIP39 wallet'den 12, 15, 18, 21 ve 24 kelimelik cümlelerin içe aktarılmasını destekler


`BIP32 + BIP44/BIP49/BIP84` - tüm adreslerin deterministik üretimi

Tek bir ana anahtardan wallet, kesin olarak tanımlanmış bir sırayla milyarlarca adresi generate yapabilir. Bu nedenle Electrum, Sparrow, Trezor, Ledger, BlueWallet vb. programlara girilen aynı 12 kelime tamamen aynı adresleri ve bakiyeleri gösterecektir.


**Bitcoin** için Coin Wallet'de kullanılan sapma yolları


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

Her yolun içinde:


- `/0` - harici zincir (ödemeleri almak için gösterdiğiniz adresler)
- `/1` - dahili zincir (wallet'un kendi kullandığı adresleri değiştirin)


Coin Wallet bu kamu standartlarını herhangi bir değişiklik yapmadan takip ettiğinden, fonlarınız 10-20-30 yıl sonra bile uyumlu herhangi bir wallet'de geri kazanılabilir kalacaktır.


## 8️⃣ Tor ile Anonimliği Artırma


**Neden Coin Wallet**'te Tor kullanılmalı?

Tor gerçek IP adresinizi Bitcoin düğümlerinden, borsalardan ve gözlemcilerden gizler.

Tüm trafik (bakiyeler, işlemler, takaslar) Tor ağı üzerinden geçer - doğrudan bağlantı yok, IP sızıntısı yok.

Bu, doğrudan uygulamanın kaynak kodunda uygulanır (bkz. [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet gizli bir .onion adresine ve v6.6.3'ten (Aralık 2024) bu yana **doğrudan mobil uygulamada yerleşik Tor desteğine** sahiptir.


### Android ve iOS'ta Tor nasıl etkinleştirilir


1. **Orbot** yükleyin - resmi Tor Projesi uygulaması (ücretsiz)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Orbot'u açın → Başlat** üzerine dokunun

Listeden **Coin Wallet** öğesini seçin, böylece yalnızca wallet Tor kullanır (isteğe bağlı ancak önerilir)

"Bağlandı "** yazana kadar bekleyin (10-30 saniye)


3. **Coin Wallet → Ayarlar → Ağ** öğesini açın

Aç **Tor Kullan**


4. **Durumu kontrol edin**

Üst çubukta bir **mor Tor soğan simgesi** görünür → tüm trafik artık Tor üzerinden yönlendirilir


![image](assets/en/06.webp)


İşte bu kadar - cep telefonunuz Coin Wallet tamamen anonimdir.


Özel kripto yönetiminin keyfini çıkarın!


## 📝 Sonuç


[Coin Wallet](https://coin.space/) - 10 yıllık bir geliştirme geçmişine sahip gerçek Bitcoin wallet öncülerinden biri.

Kasıtlı olarak basittir ve temel misyonuna lazer odaklı kalır: kripto para biriminizi güvenli bir şekilde saklamak.

Reklam yok, haber akışı yok, abonelik yok, sosyal özellikler yok, dikkat dağıtıcı şeyler yok - sadece temiz, hızlı, kendi kendine yetebilen ve tam olarak yapması gerekeni yapan bir wallet var.

Coin Wallet basitliği ve güvenliği ilk sıraya koyar - her zaman koymuştur, her zaman koyacaktır.


## 📖 Kaynaklar


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39