---
name: BIP-85
description: BIP-85'i bir ana seed'den birden fazla seedphrase'i generate yapmak için nasıl kullanabilirim?
---
![cover](assets/cover.webp)



## 1. BIP-85'i Anlamak



### 1.1 BIP-85 nedir?



BIP-85, bir **seed ana cümlesinden** birkaç **seed ikincil cümlesi** oluşturmanızı sağlayan gelişmiş bir işlevdir.



Her bir seed ikincil cümlesi tamamen bağımsız bir Bitcoin portföyü oluşturmak için kullanılabilir. Bu portföyler çeşitli amaçlar için kullanılabilir: mobil cihazlarda bir KİS-6 KİS-4, bir akraba için portföy, ayrı bir tasarruf portföyü, vb.



Tüm seed alt ifadeleri **matematiksel olarak türetilmiştir**, ancak bir alt ifadeden seed ana ifadesine** geri dönmek **imkansızdır. Bu, her portföy arasında tam bir ayrım sağlar.



seed ana ifadenize (ve eğer kullanıyorsanız ilişkili passphrase'e) erişiminiz olduğu sürece, herhangi bir seed ikincil ifadesini ayrı olarak kaydetmek zorunda kalmadan **aynı şekilde** yeniden oluşturabilirsiniz.



### 1.2 Neden BIP-85 kullanılmalı?



BIP-85 aşağıdakileri yapmak istiyorsanız kullanışlıdır:





- Birden fazla yedekleme olmadan birkaç bağımsız Bitcoin portföyü oluşturun
- Fonlarınızı farklı kullanımlara göre yönetin (tasarruflar, harcamalar, aile, projeler)
- Akrabalar için güvence sağlanması ("Jim Amca" işlevi)
- Fonlarınıza erişiminizi kaybetmeden bir portföyü silin
- Güvenliğinizi basitleştirin: korumak için sadece bir seed anahtar cümlesi



### 1.3 BIP-32'ye göre avantajları



BIP-32 ile tek bir seed cümlesi, türetme yolları (örneğin: `m/44'/0'/0'/0/0`) kullanılarak Bitcoin hesaplarının ve adreslerinin tam bir hiyerarşisini generate için kullanılabilir. Her yol ayrı bir hesabı temsil edebilir, ancak **hepsi aynı seed cümlesine bağlı kalır**. Dolayısıyla, bu seed cümlesi tehlikeye atılırsa, **tüm türetilmiş hesaplar erişilebilir hale gelir**.



BIP-85 ile bir seed ana cümlesi, tamamen bağımsız birkaç seed ikincil cümlesini generate yapmak için kullanılabilir: **Bu ikincil tohumlardan biri ele geçirilirse, saldırgan asla ana seed'ya geri dönemez veya diğer portföylere erişemez**.


Bu, risklerin bölümlere ayrılmasını mümkün kılar:





- Hot Wallet veya geçici kullanım için daha yüksek bir pozlamayı kabul ederek ikincil bir seed kullanabilirsiniz.
- Bu Hot Wallet tehlikeye girse bile, diğer ikincil tohumlar tarafından korunan veya çevrimdışı tutulan diğer fonlarınız **güvende kalır**.



Öte yandan, hem BIP-32 hem de BIP-85 için, ana seed tehlikeye girerse, **tüm fonlar savunmasızdır**. Bu nedenle en üst düzeyde güvenlikle korunması çok önemlidir.



![image](assets/fr/02.webp)


## 2. BIP-85 için pratik kullanım örnekleri



BIP-85, her biri kendi seed ikincil ifadesine sahip tek bir seed çekirdek ifadesinden birden fazla Bitcoin portföyü oluşturmanıza olanak tanır. İşte Bitcoin fonlarınızı düzenlemek ve güvence altına almak için beş pratik kullanım örneği. Her vaka, BIP-85 kullanmanın neden BIP-32 aracılığıyla tek bir seed ifadesiyle birden fazla hesabı yönetmekten daha pratik olduğunu açıklamaktadır.



### 2.1 Daha az güvenli bir portföyün riskinin sınırlandırılması





- Senaryo**: Günlük işlemler için bir "Hot Wallet" Wallet (İnternet bağlantılı bir cihaza yüklenmiş) kullanıyorsunuz.
- Çözüm BIP-85**: Bu portföye adanmış bir seed ikincil ifade oluşturursunuz.
- BIP-32**'ye göre avantaj: seed birincil ifadesini telefonunuza aktarmanız gerekmez, bu da bilgisayar korsanlığı riskini azaltır. Yalnızca seed ikincil ifade tehlikeye atılır ve diğer cüzdanlarınızı korur. BIP-32 ile, tüm fonlarınızı açığa çıkaran seed ana ifadesini ve bir bypass yolunu kullanmanız gerekir.



### 2.2 Bir aile üyesi için portföy oluşturun





- Senaryo**: Size yakın biri (örneğin anneniz) için bir Bitcoin Wallet kurdunuz ve kaybetmeleri halinde geri alabiliyorsunuz.
- Çözüm BIP-85**: Özel bir seed ikincil cümlesi oluşturursunuz ve sadece bunu paylaşırsınız.
- BIP-32'ye göre avantaj**: BIP-32 ile sevdiğiniz biri için bir hesap oluşturmak için ya ana seed ifadenizi paylaşmanız, tüm fonlarınızı riske atmanız ve sevdiğiniz kişi için yönetimi karmaşıklaştırmanız (dallanma yollarını yönetmek) ya da ana seed ifadenize ek olarak kaydetmek için yeni bir seed ifadesi oluşturmanız gerekir.



### 2.3 Ayrı portföylerin yönetiminin kolaylaştırılması





- Senaryo**: Bitcoinlerinizi farklı amaçlar için ayırıyorsunuz (örn. uzun vadeli tasarruflar, KYC dışı fonlar).
- Çözüm BIP-85**: Her bir hedef için seed ikincil ifadeler oluşturursunuz.
- BIP-32**'ye göre avantaj: BIP-32 ile tüm hesaplar aynı seed ifadesini paylaşır, bu da `m/44'/0'/0'` gibi türetme yollarının yönetilmesini gerektirerek üçüncü taraf portföylerinde yönetimi zorlaştırır. Buna ek olarak, her cihaz için ayrı bir hesap atamak mümkün değildir (örneğin, "Coldcard'da tasarruf", "cep telefonunda günlük", "Trezor'da tatil"). BIP-85, hedef başına benzersiz bir seed ikincil ifade atar, bu da her cihazda ayrı ayrı tanımlanması ve içe aktarılması kolaydır.



### 2.4 İşlemler için geçici bir Wallet kullanma





- Senaryo**: Tek seferlik bir işlem için veya gizliliği korumak için geçici bir portföye ihtiyacınız var (örneğin: fonların karıştırılması, Exchange KYC ile etkileşim, vb.)
- Çözüm BIP-85**: Bir seed ikincil cümlesi oluşturursunuz, işlem için kullanırsınız, ardından yeniden oluşturulabileceğini bilerek gerekirse imha edersiniz.
- BIP-32'ye göre avantaj**: BIP-32 ile geçici bir hesap seed ana cümlesine bağlıdır ve ele geçirilmesi halinde tüm fonlarınız açığa çıkar.





## 3. Başlamadan önce





- Donanım** (isteğe bağlı)
 - Coldcard Mk4 veya Q1
 - MicroSD kart





- Temel bilgi
 - Mnemonic cümlelerini anlama (BIP-39): portföy kaydetmek için 12 ila 24 kelimelik bir liste.
 - Bitcoin Wallet'nin ne olduğunu bilin: bitcoinlerinizi yönetmek için bir yazılım veya cihaz ve bunu bir Mnemonic ifadesiyle nasıl geri yükleyeceğinizi.
 - Eklerde daha fazla kaynak bulunmaktadır.





- Uyumlu** yazılım
 - Sparrow wallet (bilgisayar, yalnızca izleme veya gelişmiş yönetim için)
 - Nunchuck (mobil, çoklu imzalar için)
 - BlueWallet (mobil)
 - ...





- 3.4 Soğuk kart** yapılandırması
 - Coldcard üzerinde 24 kelimelik bir seed cümlesini başlatın.
 - İsteğe bağlı: BIP-85 şubelerine erişimi güvence altına almak için bir passphrase ekleyin.
 - Yararlı seçenekleri etkinleştirin: NFC (dışa aktarma için), pilde USB'yi devre dışı bırakma (güvenlik).




## 4. Adım adım öğretici



Coldcard'ınızda BIP-85 ile ikincil bir Mnemonic oluşturmak, kullanmak ve almak için aşağıdaki adımları izleyin.



### 4.1 generate a seed ikincil cümle



seed ana cümlenizden bir seed ikincil cümlesi oluşturacaksınız.


Coldcard'ınızı açın, PIN kodunuzu girin.





- 1. Ana seed'inize bir passphrase uyguladıysanız:**
 - Ana ekrandan `passphrase` seçeneğine gidin.
    - Kelime Ekle'yi seçin ve şifrenizi girin.
    - "Uygula" düğmesine basın.
    - Wallet'ün kimliğini kontrol edin: Wallet'ün parmak izini not etmek için `Gelişmiş > Kimliği Görüntüle'ye gidin.





- 2. BIP-85** menüsüne gidin
 - Ana ekrandan `Gelişmiş > seed B85 Türet` seçeneğine gidin
 - Uyarıyı okuyun ve onaylayın.



ColdCard, üretilen tohumların matematiksel olarak ana seed'inizden türetildiğini, ancak kriptografik olarak tamamen bağımsız olduğunu bildirir.


![image](assets/fr/03.webp)





- 3. Bir format seçin


seed cümle biçimini seçin: 12, 18 veya 24 kelime. Wallet cümlenizi aktarmak istediğiniz seed tarafından kabul edilen kelime sayısını kontrol edin.


![image](assets/fr/04.webp)





- 4. Dizin seçin
 - 0 ile 9999 arasında bir dizin girin.
 - Bu indeks, ikincil seed'un daha sonraki bir tarihte yeniden üretilmesi için çok önemlidir. Aşağıdaki gibi bir etiketle dikkatlice saklayın: "Dizin 1 = Wallet mobil", "Dizin 2 = aile projesi", "Dizin 4 = test karışımı", ...
 - Kaybederseniz, paranıza erişiminizi kaybetmezsiniz, ancak onları bulmak için 0'dan 9999'a kadar kombinasyonları test etmeniz gerekir.


![image](assets/fr/05.webp)





- 5. seed ikincil cümlesini not edin veya dışa aktarın**


ColdCard artık yeni bir seed ikincil cümlesi görüntülüyor. Yapabilirsin :




 - Manuel olarak **not alın**.
 - Basın :
     - 1` SD karta kaydetmek için
     - coldCard'da **"bu seed'yi kullan "** moduna girmek için `2` (bir işlemi dışa aktarmak veya imzalamak için kullanışlıdır)
     - 3` bir **QR kodu** görüntülemek için (BlueWallet veya Nunchuck gibi bir mobil uygulama ile taranmak üzere)
     - 4` **NFC** ile göndermek için



💡 Bu noktada, herhangi bir Wallet BIP39'da (Trezor, Ledger, BlueWallet, Nunchuck...) kullanılabilen bağımsız bir seed ifadesine sahip olursunuz.


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 İkincil seed'nın kullanılması



'de yeni bir portföy oluşturmak için artık bu türetilmiş seed'yi kullanabilirsiniz:




- bir mobil uygulama
- başka bir Hardware Wallet
- bir Multisig portföyü



### 4.3 Kayıp bir seed ikincil ifadesinin kurtarılması



Herhangi bir zamanda ikincil bir seed almak için işlemi tekrarlayın:


1. ColdCard'ınızı yeniden başlatın


2. PIN kodunuzu girin


3. Tanımlanmışsa passphrase'nizi girin


4. Gelişmiş > seed B85 Türet` seçeneğine gidin


5. Format seçin (12/18/24 kelime)


6. Aynı indeksi girin (örneğin `1`)


7. Tam olarak aynı ikincil seed'ü alacaksınız




## 5. Sınırlar, riskler ve en iyi uygulamalar



### 5.1 seed ana cümlesine bağımlılık + passphrase



BIP85'in kullanımı tamamen 24 kelimelik seed ana cümlesine ve eğer uyguladıysanız passphrase'ye dayanır.




- Bu iki Elements'dan, tüm seed ikincil ifadeleri yeniden üretilebilir.
- Bu 2 Elements'den biri olmadan, tüm türev portföylerine erişiminizi kaybedersiniz.



### 5.2 Çoklu imza yapılandırmasındaki riskler



Bir multi-sig yapılandırmasında aynı birincil seed ifadesinden oluşturulan ikincil seed ifadelerinin kullanılmamasını şiddetle tavsiye ederiz: cihazın veya birincil seed ifadesinin ele geçirilmesi durumunda, tüm multi-sig anahtarları bir saldırgan tarafından yeniden oluşturulabilir.



### 5.3 Yazılım uyumluluğu



Tüm uygulamalar BIP85 türetimini doğrudan desteklememektedir. Ancak, BIP85 ile üretilen tohumlar standart BIP39 tohumlarıdır (12, 18 veya 24 kelime) ve bu nedenle herhangi bir BIP39 uyumlu portföyde kullanılabilir.



### 5.4 BIP85 hesap kaydı



seed ikincil ifadelerinin güncel bir kişisel kaydının tutulması tavsiye edilir.




- seed ikincil ifadeleri tutmak zorunda kalmadan hangi BIP85 endeksinin hangi portföye karşılık geldiğini hızlı bir şekilde bulmanızı sağlar.
- Bu kayıt, Bitcoin'dan açıkça bahsetmeden minimalist kalmalı ve ana seed'den ayrı olarak saklanmalıdır. Miras planınızda bundan bahsetmeyi unutmayın.



Kayıt şunları içerebilir :




- bIP85 indeksi kullanıldı (0 ila 9999 arası sayı)
- bir kullanım veya referans adı (örn. Hot Wallet, kişisel tasarruflar, Annemden Wallet)
- gerekirse, ColdCard'da doğrulama için Wallet parmak izi



### 5.5 Yedekleme



Yedeklemeler şunları içermelidir :




- ana seed
- gW-76 (eğer kullanılıyorsa)



Asla birlikte saklamayın:




- ana seed ve passphrase
- ana seed ve BIP85 hesap kaydı



Eklerde daha fazla kaynak bulunmaktadır.




## EKLER



## A.1 Sözlük





- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [seed ifade](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 Kurtarma ifadenizi kaydedin



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 passphrase BIP'yi Anlamak39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Bitcoin portföyleri nasıl çalışır?



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f