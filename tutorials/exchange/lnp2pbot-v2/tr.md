---
name: LNP2PBot
description: LNP2PBot ve P2P Bitcoin ticareti için eksiksiz kılavuz
---
![cover](assets/cover.webp)


## Giriş


KYC içermeyen eşler arası (P2P) borsalar, kullanıcıların gizliliğini ve finansal özerkliğini korumak için çok önemlidir. Kimlik doğrulamasına ihtiyaç duymadan bireyler arasında doğrudan işlem yapılmasını sağlarlar ki bu da gizliliğe önem verenler için çok önemlidir. Teorik kavramları daha derinlemesine anlamak için BTC204 kursuna bir göz atın:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Bitcoin eşler arası (P2P) alım satımı, bitcoin edinmenin veya elden çıkarmanın en özel yöntemlerinden biridir. LNP2PBot, P2P'te Lightning Network değişimlerini kolaylaştıran, hızlı, düşük maliyetli, KYC içermeyen işlemler sağlayan açık kaynaklı bir Telegram botudur.


### Neden Lnp2pbot kullanılmalı?




- KYC gerekmez
- Lightning Network'da hızlı işlemler
- Düşük maliyetler
- Dünyanın her yerinden erişilebilen popüler bir mesajlaşma uygulaması olan Telegram aracılığıyla basit Interface
- Entegre itibar sistemi
- Güvenli ticaret için otomatik emanet
- Çoklu para birimi desteği
- Aktif ve büyüyen topluluk


### Ön Koşullar


Lnp2pbot'u kullanmak için ihtiyacınız olacak :


1. Lightning Network Wallet (Breez, Phoenix veya Blixt önerilir)


2. Telegram uygulaması yüklü (https://telegram.org/)


3. Tanımlanmış bir kullanıcı adına sahip bir Telegram hesabı


## Kurulum ve yapılandırma


### 1. Lightning Wallet'unuzu yapılandırma


Uyumlu bir Lightning Wallet kurarak başlayın. İşte ayrıntılı önerilerimiz:


**Önerilen cüzdanlar**




- [Breez](https://breez.technology)**:
  - Yeni başlayanlar için mükemmel
  - Sezgisel, modern Interface
  - Velayetsiz (fonlarınızın kontrolü sizde kalır)
  - Lnp2pbot ile mükemmel uyumlu
  - IOS ve Android'de kullanılabilir


Aşağıda bu Wallet için öğretici bağlantı bulunmaktadır:


https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06


- [Phoenix](https://phoenix.acinq.co)** :
  - Basit ve güvenilir
  - Otomatik kanal yapılandırması
  - BOLT11 faturaları için yerel destek
  - Günlük işlemler için mükemmel
  - IOS ve Android'de kullanılabilir


Aşağıda bu Wallet için eğitim linki bulunmaktadır:


https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


- [Blixt](https://blixtwallet.github.io)** :
  - Daha teknik ama çok eksiksiz
  - Gelişmiş yapılandırma seçenekleri
  - Deneyimli kullanıcılar için mükemmel
  - Açık kaynak
  - Android'de mevcut


Aşağıda bu Wallet için eğitim linki bulunmaktadır:


https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

**Diğer cüzdanlar hakkında önemli notlar**


⚠️ **Önemli**: Sats'yi satmadan önce, Wallet'nızın bot tarafından bir emanet sistemi olarak kullanılan "hold" faturalarını desteklediğinden emin olun.




- Satoshi'in Wallet'u**: Sats'yi almak için iyi çalışır, ancak bir satış iptal edilirse bakiyenin güncellenmesinde gecikmeler olabilir.
- Muun**: Bot yönlendirme ücreti limitleri (maksimum %0,2) nedeniyle ödemeler başarısız olabileceğinden önerilmez.
- Aqua**: Sats'yi almak için çalışır, ancak bir satış iptali durumunda bakiye güncellemeleri için uzun gecikmeler (48 saate kadar) olabilir.


💡 **İpucu**: Optimum deneyim için önerilen cüzdanları (Breez, Phoenix veya Blixt) tercih edin.


⚠️ **Önemli**: Kurtarma cümlelerinizi güvenli bir yere kaydetmeyi unutmayın.


### 2. Lnp2pbot ile çalışmaya başlama


1. Bota erişmek için bu bağlantıya tıklayın: [@lnp2pBot](https://t.me/lnp2pbot)


2. Telegram otomatik olarak açılacaktır


3. "Başlat" üzerine tıklayın veya "/başlat" komutunu gönderin


4. Henüz bir kullanıcı adınız yoksa bot sizden bir kullanıcı adı oluşturmanızı isteyecektir


5. Bot, ilk yapılandırma boyunca size rehberlik edecektir


### 3. Topluluğa katılın




- Ana kanala katılın: [@p2plightning](https://t.me/p2plightning)
- Destek: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)


## Bitcoin Alımı ve Satımı


Lnp2pbot'ta Exchange bitcoinleri kullanmanın iki ana yolu vardır:


1. Pazardaki mevcut tekliflere göz atın ve yanıt verin


2. Kendi alım veya satım teklifinizi oluşturun


Bu kılavuzda, :




- Mevcut bir tekliften bitcoin satın alın
- Kendi teklifinizi oluşturarak bitcoin satın


### Bitcoin nasıl satın alınır


**1. Bir teklif bulun ve seçin**


![Sélection d'une offre de vente](assets/fr/01.webp)


P2plightning](https://t.me/p2plightning) adresindeki tekliflere göz atın ve ilgilendiğiniz ilanın altındaki "Satoshis satın al" düğmesine tıklayın.


**2. Teklifi ve tutarı doğrulayın**


![Validation de l'offre](assets/fr/02.webp)


1. Bot sohbetine geri dönün


2. Teklif seçiminizi onaylayın


3. Satın almak istediğiniz fiat para birimi cinsinden tutarı girin


4. Bot sizden satoshis cinsinden tutar için bir Lightning Invoice sağlamanızı isteyecektir


**3. Satıcı ile iletişime geçin**


![Mise en relation](assets/fr/03.webp)


Invoice gönderildikten sonra, bot sizi satıcıyla iletişime geçirir.


**4. Satıcı ile iletişim**


![Chat privé](assets/fr/04.webp)


Exchange fiat ödeme ayrıntılarını girebileceğiniz özel bir sohbet kanalı açmak için satıcının takma adına tıklayın.


**5. Ödeme onayı


![Confirmation du paiement](assets/fr/05.webp)


Fiat ödemesini yaptıktan sonra, bot sohbetinde `/fiatsent` komutunu kullanın. İşlem tamamlandığında, satıcıyı derecelendirebileceksiniz ve işlem kapanacaktır.


### Bitcoin nasıl satılır


**1. Bir satış teklifi oluşturun**


![Création d'une offre de vente](assets/fr/06.webp)


Bir satış teklifi oluşturmak için komutu kullanmanız yeterlidir:


`/sat`


Bot daha sonra sizi adım adım yönlendirecektir:


1. Para biriminizi seçin


2. Satılacak satoshis miktarını belirtin


3. Fiyat için iki seçeneğiniz var:




   - Satoshis miktarı için sabit bir fiyat belirleyin
   - Prim (pozitif veya negatif) uygulama seçeneğiyle birlikte piyasa fiyatını kullanın


💡 **İpucu**: Prim, fiyatınızı piyasa fiyatına göre ayarlamanıza olanak tanır. Örneğin, %1'lik bir prim, piyasa fiyatından %1 daha düşük bir fiyata sattığınız anlamına gelir.


**2. Sipariş oluşturma onayı**


![Confirmation de l'ordre de vente](assets/fr/07.webp)


Sipariş oluşturulduktan sonra, `/cancel` komutunu kullanarak siparişi iptal etme seçeneğini içeren bir onay göreceksiniz.


**3. Satışları yönetmek**


![Prise de l'ordre par un acheteur](assets/fr/08.webp)




- Bir alıcı teklifinize yanıt verdiğinde, QR kodu ve ödeme için bir Invoice içeren bir bildirim alırsınız.
- Alıcının profilini ve itibarını kontrol edin.


![Mise en relation avec l'acheteur](assets/fr/09.webp)




- Özel bir tartışma kanalı açmak için alıcının takma adına tıklayın.
- Fiat ödeme detaylarını alıcıya iletin.
- Alıcıdan fiat ödemesinin onaylanmasını bekleyin.
- Hesabınıza ödeme yapılıp yapılmadığını kontrol edin.


![Confirmation de la fin de l'ordre](assets/fr/10.webp)




- İşlemi `/release` ile onaylayın ve siparişi tamamlayın. Alıcıyı değerlendirme fırsatınız olacak.


## İyi Uygulamalar ve Güvenlik


### Güvenlik ipuçları




- Küçük miktarlarla başlayın
- Her zaman kullanıcıların itibarını kontrol edin
- Yalnızca önerilen ödeme yöntemlerini kullanın
- Tüm iletişimleri bot sohbetinde tutun
- Hassas bilgileri asla paylaşmayın


### İtibar sistemi




- Her kullanıcının bir itibar puanı vardır
- Başarılı işlemler puanınızı artırır
- İyi bir üne sahip kullanıcıları seçin
- Şüpheli davranışları moderatörlere bildirin


### Uyuşmazlık çözümü


1. Sorunlar ortaya çıktığında sakin ve profesyonel kalın


2. Bilet açmak için `/dispute` komutunu kullanın


3. Gerekli tüm kanıtları sağlayın


4. Bir moderatör bekleyin


## Diğer çözümlerle karşılaştırma


Lnp2pbot, Peach, Bisq, HodlHodl ve Robosat gibi diğer P2P Exchange çözümlerine göre çeşitli avantaj ve dezavantajlara sahiptir:


### Lnp2pbot'un Avantajları




- KYC gerekmez ** : Bazı platformların aksine, Lnp2pbot kimlik doğrulaması gerektirmez, böylece kullanıcı gizliliğini korur.
- Hızlı işlemler**: Lightning Network sayesinde işlemler neredeyse anında gerçekleşir.
- Düşük ücretler** : İşlem maliyetleri geleneksel borsalara göre daha düşüktür.
- Mobil kullanılabilirlik**: LNP2PBot'a Telegram üzerinden erişilebilir, bu da mobil cihazlarda kullanımı kolaylaştırır.
- Kolay kullanım** : Lnp2pbot'un sezgisel Interface'i, daha az deneyimli kullanıcılar için bile kullanımı kolaylaştırır.


### Lnp2pbot'un Dezavantajları




- Telegram bağımlılığı**: Lnp2pbot'u kullanmak, tüm kullanıcılar için uygun olmayabilecek bir Telegram hesabı gerektirir.
- Daha az likidite**: Bisq gibi daha köklü platformlarla karşılaştırıldığında, likidite daha sınırlı olabilir.


Buna karşılık, Bisq gibi çözümler daha fazla likidite ve masaüstü Interface sunar, ancak daha yüksek ücretler ve daha uzun işlem süreleri içerebilir. Bu arada HodlHodl ve Robosat da KYC'siz alım satım imkanı sunuyor, ancak farklı ücret yapıları ve arayüzleri var.


## Yararlı kaynaklar




- Resmi web sitesi: https://lnp2pbot.com/
- Dokümantasyon: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Destek: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)