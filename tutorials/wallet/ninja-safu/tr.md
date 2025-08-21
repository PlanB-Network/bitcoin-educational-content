---
name: SAFU Ninja
description: SAFU Ninja yöntemi ile seed'ınızı kaydedin
---

![cover](assets/cover.webp)


## 1. Giriş



Ninja SAFU** yöntemi, **seed ifadenizin** (**BIP-39** standardı tarafından tanımlanan 12 veya 24 kelimelik bir Mnemonic ifadesi) **sürdürülebilir, güvenli ve gizli** bir yedeğini oluşturmanızı sağlayan bir **DIY (Do It Yourself)** çözümüdür. Bu ifade, bir Bitcoin Wallet veya uyumlu başka bir Wallet'ü geri yüklemek için gereklidir.



Sözlerinizi kağıda yazmak yerine - basit ama savunmasız bir yöntem - **Bolt** üzerine monte edilmiş **paslanmaz çelik pullar** üzerine kazıyacaksınız. Sonuç, kompakt, yangına, korozyona, suya ve darbelere dayanıklı bir yedektir. Alev, nem veya zamanla tahrip olabilen kağıdın aksine paslanmaz çelik, aşırı koşullar altında bile (1300°C'ye veya 20 ton basınca kadar) uzun süreli korumayı garanti eder.



Ninja SAFU yaklaşımı çeşitli avantajlar sunmaktadır:





- Gizlilik**: Kripto para yedekleme amaçlı olduğu belirtilen bir ürün satın almıyorsunuz. Bileşenler standarttır (pullar, cıvatalar, metal kutu), donanım mağazalarında mevcuttur, bu da özel bir satıcıdan veri sızıntısı olması durumunda hedef alma riskini azaltır.





- Ekonomiklik** : Bu çözüm, sahip olduğunuz araçlara bağlı olarak **15 ila 140 EUR** arasında bir maliyete sahiptir.





- Güvenilirlik**: 2020 yılından bu yana test edilen yöntem, [Jameson Lopp] (https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/) gibi güvenlik uzmanları tarafından denenmiş ve test edilmiş, zorlu stres testlerine (aşırı ısı, korozyon, mekanik basınç) tabi tutulmuştur.



Bu adım adım kılavuz, bitcoinlerinizi kayıp veya tahribata karşı daha iyi korumak için kendi Ninja SAFU yedeklemenizi nasıl yapacağınızı gösterecektir. Bir seed ifadesini yedekleme ve koruma hakkında daha fazla bilgi edinmek isterseniz, lütfen eklere bakın.




## 2. Donanım



Bir Ninja SAFU yedeklemesi oluşturmak için, tümü donanım mağazalarından veya çevrimiçi olarak temin edilebilen aşağıdaki bileşenlere ihtiyacınız olacaktır.



### 2.1 Gerekli malzemeler





- Paslanmaz çelik pullar (M8 önerilir)** :
 - Malzeme**: Paslanmaz çelik (örn. korozyon direnci için 304 veya V4A)
    - Boyut**: M8 (iç çap 8 mm, dış çap ~24 mm). M6 pullar çok küçüktür ve kazınması zordur.
    - Miktar**: standart bir seed cümlesi için 12 veya 24 pul, artı isteğe bağlı pullar (bkz. bölüm 3.4) ve testler veya hatalar için on kadar pul.





- Paslanmaz çelik Bolt ve somun (M8)** :
 - Özellikler**: Bolt 2,5 ila 5 cm uzunluğunda, pulların sayısına ve kalınlığına bağlı olarak, çap 8 mm. Kanatlı somun aletsiz açmayı kolaylaştırır, ancak basit bir somun da kullanılabilir.



![image](assets/fr/03.webp)





- Harf ve rakam zımba seti (3 mm veya 6 mm)** :
    - Özellikler**: 6 mm yüksekliğindeki karakterler okunabilirliği kolaylaştırır ve yazının bir kısmı bozulmuşsa tercih edilebilir. Tekrarlanan kullanım için sağlam bir set seçin.



![image](assets/fr/04.webp)





- Çekiç veya balyoz** :
    - Yeterli ve hassas damgalama kuvveti için bir balyoz tercih edilir





- Örs veya sağlam yüzey** :
 - Şokları emmek için kalın, Hard bir yüzey (örn. 1 kg örs veya 10 cm kaldırım taşı).



Bir zımba setine yatırım yapmak istemiyorsanız, pullarınızı bir gravür kalemiyle de kazıyabilirsiniz. Bu çözüm genellikle daha ekonomiktir, ancak tatmin edici bir sonuç elde etmek için daha fazla özen gerektirir.



### 2.2 İsteğe bağlı araçlar





- Damgalama cihazı**: Pulu tutar ve zımbayı yönlendirerek hassas, temiz damgalama, daha iyi yönlendirme ve harflerin eşit aralıklarla yerleştirilmesini sağlar



![image](assets/fr/05.webp)





- Sızdırmazlık cihazları**: Mühürlü poşet veya mühürleme şeridi



![image](assets/fr/06.webp)





- Hermetik olarak kapatılmış kap**: Pul bloğunu saklamak için



![image](assets/fr/07.webp)


### 2.3 Güvenlik





- Eldiven** ve **Güvenlik gözlükleri** önerilir.
- Zımbayı içine sokacağınız boru anahtarı**, böylece zımbayı parmaklarınızla değil boru anahtarıyla tutarsınız.



### 2.4 Miktarlar ve tahmini maliyet





- 24 kelimelik bir yedekleme için miktar**: 24 pul (minimum), 1 Bolt, 1 kelebek somun, 1 zımba seti, 1 çekiç/kaset, 1 örs/destek.





- Toplam maliyet** :
 - Pullar ve cıvatalar/somunlar: ~ 15 EUR
 - Yumruk seti: ~ 45 EUR
 - Koruyucu kılıf: ~ 55 EUR
 - Tüm aksesuarlarla birlikte: ~ 140 EUR





- Örnek ekipman için eke bakınız.




## 3. Adım adım talimatlar



1. **Hazırlanıyorum:**




 - Özel konum, kamera yok (akıllı telefonlar dahil)
 - Sağlam, şok emici yüzey
 - Eldivenler ve koruyucu gözlükler
 - Yıkayıcılardaki tüm yağ ve kiri temizleyin
 - Test pulları üzerinde alıştırma


2. **Burn Mnemonic words** :




    - Kelimenin tamamını bir tarafa kazıyın. Dördüncü harfin hasar görmesi ihtimaline karşı kendinizi ilk 4 harfle sınırlamayın.
    - Çekiçle sıkıca vurun, zımbayı bir boru anahtarıyla tutun


3. **Pulları numaralandırın** :




    - Aynı tarafa, pulların gevşemesi durumunda gerekli olan pozisyon numarası kelimesini kazıyın.


4. **Kayıt bilgileri** (isteğe bağlı ve önerilir) :




    - Gereksiz kelimeyi pakın diğer tarafına kazıyın
    - Ek bir rondelanın üzerine Wallet tanımlayıcısını kazıyın
    - Kullandığınız hesabın türetme yolunu ek bir yıkayıcı üzerine kazıyın. Bu bilgiyi portföy yazılımınızın ayarlarında bulabilirsiniz. Örneğin, standart bir Taproot portföyü için varsayılan türetme yolu şöyle olacaktır: `m / 86' / 0' / 0' /`
    - Hardware Wallet'nızın kilidini açmak için PIN kodunu veya COLDCARD kullanıyorsanız kimlik avı önleme sözcüklerini yazın.


5. **passphrase'yi YAKMAYIN :**




 - Bir passphrase kullanıyorsanız, bunu Mnemonic'unuzla aynı karta yazmadığınızdan emin olun. passphrase, Mnemonic'un çalınması durumunda Wallet'nizi korumak için tasarlanmıştır. Ekte daha fazla bilgi bulabilirsiniz.


6. **Okunabilirliği kontrol edin** :




    - Her kelimenin ve sayının açık ve okunaklı olduğundan emin olun.


7. **Pulları monte edin** :




    - Pulları Bolt'e numara sırasına göre geçirin.
    - İsteğe bağlı: uçlara boş pullar ekleyin.
    - Aküyü sabitlemek için kelebek somunu vidalayın.
    - Suya, yangına ve mekanik gerilime karşı korumayı artırmak için sıkıca sıkın.


8. **Test yedeği** :




    - Yeni yedeğinizden portföyünüzü kurtarmayı deneyin
- Yedeğin mühürlenmesi** (isteğe bağlı ve önerilir) :
 - Şeritler halinde veya mühürlü poşetlerde.
 - Bir poşet kullanıyorsanız, benzersiz kimlik numarasını not edin, böylece bunun doğru poşet olduğunu ve orijinalinin yerini alan bir yem olmadığını kontrol edebilirsiniz.




## 4. Depolama



### 4.1 Uygun bir yer seçin



Yedeğinizi **gizli bir yerde**, gözden uzak ve periyodik kontroller için erişilebilir bir yerde saklayın. Evde veya **özel kontrolünüz** altındaki bir yerde yanmaz ve su geçirmez bir depolama alanı** seçin.



Üçüncü bir tarafa (banka kasası, noter) bağımlı olduğunuz yerlerden kaçının: fonlarınıza otonom erişiminizi kaybedersiniz, bu da Bitcoin'nin egemenlik ilkelerine aykırıdır.



Ninja SAFU gibi bir yöntem kullandığınızı asla açıklamayın. Gizlilik, başlı başına bir Layer güvenliğidir.



### 4.2 Yedeklilik



Gerekirse, **birkaç kopya** oluşturun ve bunları **farklı coğrafi konumlarda** saklayın.


Cihazınız için seçtiğiniz malzemeler suya ve yangına dayanıklı olsa bile, evinizde m3 molozun altına gömüldüğünde ona erişemezsiniz ve geri almak imkansız olmasa da çok zor olacaktır.




## 5. Takip ve bakım



İyi saklandığında bile, yedeklemenizin **düzenli olarak kontrol edilmesi** gerekir:





- Gözden uzakta, yedeklemeyi **yılda bir veya iki kez** kontrol edin.
- Gravürlerin **bozulması** durumunda, yeni bir yedek oluşturun, **test edin** ve ardından **eski kopyayı** dikkatlice imha edin.
- Yedek mühürlü bir poşet içindeyse :
 - Giriş bilgilerinizi kontrol edin
 - Bütünlüğünü kontrol edin
 - Gravürlerin durumunu kontrol etmek için zarfı düzenli olarak açın ve her şey yolundaysa yedeği yeni bir cebe yerleştirin




*SAFU KAL!


![image](assets/fr/08.webp)




## EKLER



### A.1 Kurtarma ifadenizi kaydedin



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### A.2 passphrase BIP'yi Anlamak39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

### A.3 Bitcoin portföyleri nasıl çalışır?



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


### A.4 Ninja SAFU yönteminin sınıflandırılması



Jameson Lopp'a göre:





- ninja SAFU yöntemi hakkında [Rapor](https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/)





- Karşılaştırma tablosu [tam](https://jlopp.github.io/metal-Bitcoin-storage-reviews/?ref=blog.lopp.net)





- Kısmi tablo :


![image](assets/fr/09.webp)



### A.5 Donanım örneği





- Yıkayıcılar** için
 - [Titan](https://pleb.style/fr-fr/products/disques-de-seed-supplementaires-titan-Wallet)
- Pullar + somun + koruyucu kılıf** (pullar için)
 - [Titan](https://pleb.style/fr-fr/products/titan-Wallet-premium-acier-steel-Wallet-backup?variant=50022696419664)
 - [TerraSteel](https://pleb.style/fr-fr/products/terrasteel-Wallet-plebstyle-acier-backup)
- Punch seti
 - [PlebStyle](https://pleb.style/fr/products/schlagstempelset-a-z-0-9-3mm)
- Yazım esasları**
 - [PlebStyle](https://pleb.style/fr/products/schlagunterlage-10cm-x-10cm-x-1-5cm)
- Kılavuz çekme cihazı** (kılavuz)
 - [TerraSteel](https://pleb.style/fr-fr/products/zubehor-einschlag-vorrichtung?_pos=1&_sid=2767fd66f&_ss=r)
- Sızdırmazlık cihazı
 - [Mühürlü poşet](https://pleb.style/fr/products/zubehor-5x-sicherheitstasche-tamper-evident)
 - [Sızdırmazlık şeritleri] (https://pleb.style/fr/products/zubehor-5x-siegel-streifen-fur-dein-seed-backup)
- Komple** kit
 - [Titan](https://pleb.style/fr-fr/products/titan-Wallet-diy-kit-premium-seed-backup-steelwallet-plebstyle?pr_prod_strat=e5_desc&pr_rec_id=aa9f36359&pr_rec_pid=8728733155664&pr_ref_pid=8730877788496&pr_seq=uniform)
 - [TerraSteel](https://pleb.style/fr-fr/products/kopie-von-terrasteel-Wallet-starter-kit)



Not: Çevrimiçi mağazalara bağlantılar yalnızca bilgi amaçlı verilmiştir.


Plan B ile yukarıda belirtilen satıcılar ve üreticiler arasında herhangi bir ticari ortaklık bulunmamaktadır.


Plan B, ürünlerin kalitesi veya teslimatı ile ilgili kusurlardan, fiyat değişikliklerinden veya sorunlardan sorumlu tutulamaz. **YOR**




### A.6 Fotoğraf kredileri



https://pleb.style/fr/


https://x.com/lopp/status/1463155802345193475


https://bitcointalk.org/index.php?topic=5389446.0


https://x.com/econoalchemist/status/1329271981712289797


https://www.waivio.com/@themarkymark/create-your-own-metal-seed-key-backup


https://github.com/minibolt-guide/minibolt/blob/main/bonus/Bitcoin/safu-ninja.md