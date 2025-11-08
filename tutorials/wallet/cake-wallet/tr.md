---
name: Kek Wallet
description: Cake Wallet ve Sessiz Ödemeler hakkında eğitim
---

![cover](assets/cover.webp)


Bu kılavuz [**Cake Wallet**](https://cakewallet.com/)'i incelemektedir: Android, iOS, macOS, Linux ve Windows için mevcut olan açık kaynaklı, gözetimsiz, gizlilik odaklı çoklu para birimi wallet. Bitcoin'e özgü gizlilik özelliklerini inceleyecek, **Silent Payments** (geliştirilmiş bir on-chain gizlilik protokolü) aracılığıyla Bitcoin gönderme/alma işlemlerini gerçekleştirecek ve eşzamansız işlemler için PayJoin v2 uygulamasına göz atacağız.


## 🎉 Temel Özellikler



- [**Silent Payments (BIP-352)**](https://bips.dev/352/) önceki [BIP 47 ödeme kodları](https://silentpayments.xyz/docs/comparing-proposals/bip47/) yeniden kullanılabilir gizli adreslerle "PayNyms" olarak da adlandırılır. Bir gönderici Sessiz Ödeme adresinizi kullandığında, wallet farklı anahtarlar kullanarak tek seferlik benzersiz bir adres türetir ve bu adres tek seferlik benzersiz bir Taproot adresinde birleştirilir. Blok zinciri kayıtları ilgisiz işlemleri göstererek gelen ödemelerin birbirine bağlanmasını önler. Sessiz Ödemeler, aşağıdakiler de dahil olmak üzere bir dizi avantaj sunar:
    - Yeniden kullanılabilir adresler: Her işlem için yeni bir generate adresi gerekmez, daha iyi bir kullanıcı deneyimi ve daha fazla gizlilik sağlar
    - Sıfır maliyet artışı: Sessiz Ödemeler işlemlerin boyutunu veya maliyetini artırmaz.
    - Geliştirilmiş anonimlik: Dışarıdan gözlemciler işlemleri bir Sessiz Ödeme adresine bağlayamaz.
    - Gönderici-alıcı etkileşimi gerekmez: İşlemler taraflar arasında herhangi bir iletişim olmadan yapılabilir.
    - Her ödeme için benzersiz adresler: Adreslerin yanlışlıkla yeniden kullanılması riskini ortadan kaldırır.
    - Sunucu gerekmez: Sessiz Ödemeler özel bir sunucuya ihtiyaç duymadan yapılabilir.
- PayJoin v2**, göndericilerin ve alıcıların girdilerini tek bir işlemde birleştirerek işlem grafiği analizini hafifletir. Cake Wallet iki kritik gelişmeyi hayata geçirmektedir:
    - Asenkron İşlemler**: Özel bir işlemi tamamlamak için gönderici ve alıcının artık aynı anda çevrimiçi olması gerekmiyor.
    - Sunucusuz İletişim**: Hiçbir tarafın Payjoin sunucusu çalıştırmasına gerek yoktur, bu da büyük bir teknik engeli ortadan kaldırır.
- Coin Kontrolü** işlemler sırasında manuel UTXO seçimini mümkün kılar. Bu, farklı orijinlere sahip birden fazla UTXO harcarken adreslerin yanlışlıkla bağlanmasını önler.
- Kullanıcıların ağ trafiğini Tor ağı üzerinden yönlendirmelerine olanak tanıyan TOR** desteği
- RBF** (Replace-By.Fee) bir işlem gönderdikten sonra ücreti ayarlamanızı sağlar.


## 1️⃣ Wallet'nızın Kurulumu


Cake Wallet geniş bir platform desteği yelpazesi sunar. Android, iOS / macOS, Linux ve Windows arasında seçim yapabilirsiniz.  Başlamak için https://docs.cakewallet.com/get-started/ adresini ziyaret edin ve işletim sisteminizi seçin.


![image](assets/en/01.webp)


Kurulumdan sonra bir `PIN` (4 veya 6 haneli) ayarlayın. Daha sonra göreceksiniz:


1. `Yeni Wallet Oluştur` (yeni kullanıcılar için)

2. `Restore Wallet` (mevcut cüzdanlar için)


![image](assets/en/02.webp)


Bir sonraki ekranda çok çeşitli kripto para birimleri arasından seçim yapabilirsiniz. Bitcoin`yi seçin ve `Sonraki` üzerine dokunun ve wallet`yi tanımlamak için bir `Wallet adı` girin. Gelişmiş Ayarlar`a dokunduğunuzda bir dizi `Gizlilik Ayarları` görünür. Bu değişiklikleri yapın:



- Fiat API:** `Tor Only` seçeneğini seçin (fiyat taleplerini Tor üzerinden yönlendirir)
- Takas:** `Tor Only` seçin (takas trafiğini anonimleştirir)


BIP-39 seed tipi varsayılan olarak oluşturulur ve Electrum seed tipine değiştirme seçeneği vardır. Türetme Yolları aşağıdaki gibidir:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Ekstra bir güvenlik katmanı eklemek istiyorsanız, bir `passphrase` kurabilirsiniz.  passphrase'un temel amacı fiziksel saldırılara karşı ek koruma sağlamaktır. Bir saldırgan seed ifadesini bulsa bile, doğru passphrase olmadan wallet'unuza erişemez. Başka bir deyişle, seed ifadesi tek başına bir wallet'u temsil ederken, seed ifadesi artı passphrase orijinaliyle hiçbir bağlantısı olmayan tamamen farklı bir wallet oluşturur. Bu özellik aynı zamanda passphrase tarafından korunan "gizli cüzdanları" mümkün kılar ve size makul inkar edilebilirlik sağlar. Zorlayıcı bir durumda, daha büyük varlıkları passphrase korumalı wallet'da güvende tutarken seed ifadesini ortaya çıkarabilirsiniz.


Zaten kendi düğümünüzü çalıştırıyorsanız, `Yeni Özel Düğüm Ekle` seçeneğini işaretleyin ve kendi altyapınızdaki işlemleri ve blokları doğrulamak için `Düğüm Address`nizi sağlayın. İşiniz bittiğinde wallet'ünüzü oluşturmak için `Devam` ve `Sonraki` üzerine dokunun.


![image](assets/en/03.webp)


Bir sonraki ekranda bir feragatname alırsınız:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Anımsatıcı ifadenizi kaydetmeye yönelik en iyi uygulamaları öğrenmek için lütfen bu eğiticiye başvurun:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Anladım'a dokunun. Bana seed`imi gösterin ve bu kelimeleri güvenli bir yere kaydedin! Ardından `seed`i Doğrula`ya ve doğrulamadan sonra `Wallet`ü Aç`a dokunun.


## 2️⃣ Ayarlar


Daha derine inmeden önce, `Ana Ekran` ve `Ayarlar`a bir göz atalım.


Ana Ekranda farklı öğelerin görüntülendiğini görebiliriz:



- "Hamburger menüsü" bizi "ayarlar "a götürür
- Mevcut Bakiye
- Sessiz Ödeme adresinize gönderilen işlemleri taramaya başlamak için Sessiz Ödemeler Kartı
- Payjoin kartı, gizliliği koruyan ve ücret tasarrufu sağlayan bir özellik olarak Payjoin'i `Etkinleştirmek` için
- altta `Wallet Genel Bakış`, `Alma`, Bitcoin ve diğer para birimleri arasında `Takas`, `Gönder` ve `Satın Al` kısayolları bulunmaktadır


![image](assets/en/11.webp)


Hamburger menü` simgesine dokunulduğunda ayarlar menüsü açılır. Seçenekleri gözden geçirelim.


![image](assets/en/05.webp)


### A - Bağlantı ve senkronizasyon 🔗


Burada, wallet'i yeniden bağlayabilir, düğümleri yönetebilir ve kendi düğümümüze bağlanabiliriz (önerilir). Sessiz Ödemeler Taraması`, `Blok yüksekliğinden tara` veya `Tarihten tara` seçeneklerinden birini belirleyerek taramayı özelleştirmemizi sağlar.


![image](assets/en/06.webp)


Bir `Alpha` özelliği olarak, trafiği Tor ağı üzerinden yönlendirmek için `Yerleşik Tor`u Etkinleştir` seçeneği de bulunmaktadır.


### B - Sessiz Ödemeler ayarları 🔈


Bu özelliği görüntülemek için Ana ekrandaki Sessiz Ödemeler kartını açabiliriz. Her zaman tarama` özelliğinin etkinleştirilmesi, wallet'un gelen Sessiz Ödemeler için blok zincirini sürekli olarak izlemesini sağlar. Tarama sürecini yukarıda açıklandığı gibi ihtiyaçlarımıza göre özelleştirmek için tarama parametrelerini belirleyebiliriz.


![image](assets/en/07.webp)


### C - Güvenlik ve yedekleme 🗝️


wallet'ımızı güvence altına almak için uygulama içi talimatları izleyerek bir yedek oluşturabiliriz. Bu, özel anahtarlarımızın güvenli bir kopyasına sahip olmamızı sağlayacak ve kaybolması veya çalınması durumunda wallet'ımızı kurtarmamıza olanak tanıyacaktır. Ek olarak, seed cümlemizi ve özel anahtarlarımızı görüntüleyebilir, PIN kodumuzu değiştirebilir, biyometrik kimlik doğrulamayı etkinleştirebilir, İmzalayabilir / Doğrulayabilir ve ekstra bir koruma katmanı için 2FA'yı ayarlayabiliriz.


![image](assets/en/08.webp)


**Not**: Eylül 2025 itibariyle, Android cihazlarda parmak izi biyometrik kimlik doğrulamasının en az Sınıf 2 biyometrik uygulama ile çalışması gerekmektedir, daha fazla ayrıntı için [buraya] (https://source.android.com/docs/security/features/biometric/measure#biometric-classes) bakınız. Ancak bu gereklilik gelecekte değişebilir.


### D - Gizlilik Ayarları 🔒


Ayrıca internet bağlantımızı şifrelemek ve harici kaynaklara erişirken gizliliğimizi korumak için Tor kullanarak wallet'ümüzün güvenliğini artırabiliriz. Ek olarak, wallet bilgilerimizi gizli tutmak için ekran görüntülerini engelleyebilir, her işlem için yeni adresler oluşturmak üzere otomatik oluşturulan adresleri etkinleştirebilir ve yetkisiz işlemleri önlemek için alım/satım işlemlerini devre dışı bırakabiliriz. Ayrıca, daha sonra inceleyeceğimiz bir başka gizlilik özelliği olan `PayJoin`yi etkinleştirebiliriz.


![image](assets/en/09.webp)


### E - Diğer ayarlar 🔧


Diğer ayarlar, ücret önceliğini yönetmemize ve işlemlerimiz için varsayılan ücret düzeyini belirlememize olanak tanır. Bu, mevcut ağ kullanımını dikkate alarak Sessiz Ödemelerimizle ilişkili işlem ücretlerini kontrol etmemizi sağlar.


![image](assets/en/10.webp)


## 3️⃣ Sessiz Ödemeleri Kullanarak ₿itcoin Alma


Bitcoin'ü almak için çeşitli seçenekler ve adres türleri mevcuttur. `Segwit (P2WPKH)` *(bc1q.... ile başlayan)* varsayılan seçenektir.  Bu örnekte `Sessiz Ödemeler` seçeneğini seçelim.


Sessiz Ödeme almak için önce Cake Wallet'daki "Al" simgesine dokunun. Ardından, almayı beklediğiniz tutarı girin. Adres türünü belirlemek için ekranın üst kısmındaki `Al` simgesine tekrar dokunun ve ardından seçeneklerden `Sessiz Ödemeler`i seçin.


Ana ekranda, yeniden kullanılabilir Sessiz Ödeme QR kodunuz ve adresiniz görüntülenecektir. Beklendiği gibi, adres oldukça uzundur:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Şimdi, bu QR kodunu taramak ve ödemeyi göndermek için BIP-352 uyumlu bir wallet (Blue Wallet gibi) kullanın. wallet'in sessiz adresinizden benzersiz bir hedef adresi türettiğini göreceksiniz.


![image](assets/en/13.webp)


## 4️⃣ Sessiz Ödemeleri Kullanarak ₿itcoin Gönderme


Blue Wallet yalnızca Sessiz Ödeme gönderebildiğinden, alıcı taraf olarak başka bir BIP 352 uyumlu wallet kullanacağız. Bu işlem normal bir Bitcoin işlemi ile aynıdır.



- Ana Ekranda `Gönder` üzerine dokunun
- ya yeniden kullanılabilir `sp1qq...` adresimizi yapıştırarak ya da QR kodunu doğrudan uygulama içinde tarayarak.
- Mevcut bakiyenizden ne kadar harcamak istediğinizi seçin
- İşlemi onaylamak için ekranın alt kısmındaki `Gönder` seçeneğine dokunun


Sp1qq...` adresini girdikten sonra, wallet otomatik olarak arka planda Sessiz Ödeme için kullanılacak olan karşılık gelen bir `bc1p...` Taproot adresi (P2TR) türetir.


İsteğe bağlı olarak her işlem için dahili bir not yazabilir, ücret ayarlarını yapabilir veya `Coin Control` özelliğini kullanarak işlem için belirli UTXO'ları seçebiliriz.


![image](assets/en/14.webp)


i̇şlemi onaylamak için sağa kaydırın.


İşlemi gönderdikten sonra, bu kişiyi adres defterinize eklemek isteyip istemediğiniz sorulacaktır.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


PayJoin'un [ne hakkında] olduğunu gözden geçirelim (https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


_Payjoin v2, bir işlemin göndericisinin ve alıcısının tek bir işlem oluşturmak için birlikte çalışmasına olanak tanıyan, Bitcoin'ta gizliliği koruyan ve ücret tasarrufu sağlayan bir özelliktir. Bu işlem hem göndericiden hem de alıcıdan gelen girdilere sahiptir, bu da Bitcoin'a karşı en yaygın gözetim tekniklerini kırar ve bazı durumlarda daha iyi ölçeklendirme ve ücret tasarrufu sağlar._


PayJoin hakkında daha fazla bilgi edinmek için aşağıdaki öğreticiyi de ziyaret edebilirsiniz.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

PayJoin'yi kullanmak için her iki tarafın da PayJoin uyumlu bir wallet'e ihtiyacı vardır ve alıcının wallet'ünde en az bir bozuk para veya çıkış olması gerekir. Başlamak için lütfen aşağıdaki adımları izleyin:


1. Hamburger Menü`ye dokunun ve `Gizlilik` düğmesine dokunun

2. Payjoin Kullan` Seçeneğini Değiştirin

3.  Ana ekranda `Al` seçeneğine dokunduğunuzda size bir PayJoin QR Kodu ve kopyalama düğmesi sunulacaktır (Segwit seçildiğinde)


![image](assets/en/16.webp)


## 6️⃣ Diğer özellikler


Çoklu para birimi `Swap`, farklı satıcı bağlantılarıyla `Al ve Sat` seçenekleri ve ön ödemeli kartlar veya hediye kartları satın almanızı sağlayan `Cake Pay` gibi Cake'e özel programlar gibi birçok başka özellik vardır.


![image](assets/en/17.webp)


## 🎯 Sonuç


Bu, Sessiz Ödemeler (BIP-352) ve Payjoin v2 gibi özellikler sayesinde pratik Bitcoin gizliliği sunan Cake Wallet incelememizdir.


Sessiz Ödemeler, gelen işlemlerin on-chain bağlantısını önlemek için tek kullanımlık adresleri yeniden kullanılabilir gizli adreslerle değiştirir. Önceki sürümlerin senkronizasyon sorunları önemli ölçüde iyileştirilmiş olsa da, Sessiz Ödemelerin taranması ve tespit edilmesi için daha fazla kaynak ve bant genişliği gerektiren bazı artan hesaplama gereksinimleri vardır.


Payjoin v2, gönderici ve alıcı girdilerini ekstra ücret veya merkezi koordinasyon olmadan tek bir işlemde birleştirerek zincir analizini bozar. Bu, tüm girdilerin gönderene ait olduğunu varsayamayacağınız anlamına geldiği için önemli bir avantaj olan ortak girdi sahipliği sezgiselliğini kırar.


Finansal anonimliğe öncelik veren kullanıcılar için Cake Wallet uygun bir seçenektir. Gizlilik protokollerini doğrudan temel işlevselliğine dahil ederek herhangi bir teknik karmaşıklık olmadan erişilebilir hale getirir. Halka açık blok zincirleri üzerindeki gözetim arttıkça, bunun gibi araçlar işlem gizliliğinin en önemli olduğu yerde korunmasına yardımcı olur. Bu standartların wallet ortamında daha geniş bir şekilde uygulanması memnuniyetle karşılanacak bir gelişme olacaktır.


## 📚 Kaynaklar


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/