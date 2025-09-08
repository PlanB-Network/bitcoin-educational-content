---
name: Tapsigner
description: Nunchuk ile bir Tapsigner kurma ve kullanma
---
![cover](assets/cover.webp)


Hardware Wallet, bir Bitcoin Wallet'nin özel anahtarlarının yönetimine ve güvenliğine adanmış elektronik bir cihazdır. Genellikle internete bağlı genel amaçlı makinelere kurulan yazılım cüzdanlarının (veya Hot cüzdanlarının) aksine, donanım cüzdanları özel anahtarların fiziksel olarak izole edilmesini sağlayarak bilgisayar korsanlığı ve hırsızlık risklerini azaltır.


Bir Hardware Wallet'ün ana hedefi, saldırı yüzeyini azaltmak için cihazın işlevlerini en aza indirmektir. Daha küçük bir saldırı yüzeyi aynı zamanda daha az potansiyel saldırı vektörü, yani saldırganların bitcoinlere erişmek için sistemde yararlanabileceği daha az zayıf nokta anlamına gelir.


Özellikle mutlak değer olarak veya toplam varlıklarınızın bir oranı olarak önemli miktarlara sahipseniz, bitcoinlerinizi güvence altına almak için bir Hardware Wallet kullanmanız önerilir.


Donanım cüzdanları, bir bilgisayar veya akıllı telefondaki Wallet yönetim yazılımı ile birlikte kullanılır. Bu yazılım işlemlerin oluşturulmasını yönetir, ancak bu işlemleri doğrulamak için gerekli kriptografik imza yalnızca Hardware Wallet içinde yapılır. Bu, özel anahtarların hiçbir zaman potansiyel olarak savunmasız bir ortama maruz kalmadığı anlamına gelir.


Donanım cüzdanları kullanıcı için ikili koruma sunar: bir yandan özel anahtarları çevrimdışı tutarak bitcoinlerinizi uzaktan saldırılara karşı korurlar, diğer yandan da genellikle anahtarları çıkarma girişimlerine karşı daha iyi fiziksel direnç sunarlar. İşte tam da bu 2 güvenlik kriterine göre piyasada bulunan farklı modeller değerlendirilebilir ve sıralanabilir.


Bu eğitimde, bu çözümlerden birini keşfetmeyi öneriyorum: Coinkite tarafından geliştirilen Tapsigner.


## Tapsigner'a Giriş


Tapsigner, Coldcard'ları üretmesiyle de bilinen Coinkite şirketi tarafından NFC kartı şeklinde tasarlanmış bir Hardware Wallet'dir.


![TAPSIGNER NUNCHUK](assets/notext/01.webp)


Tapsigner, kriptografik anahtarlardan oluşan bir ağaç türetmek için BIP32'ye uygun olarak bir ana özel anahtar ve bir chain code'dan oluşan bir çiftin depolanmasına izin verir. Bu anahtarlar, Tapsigner'ı bir telefona veya bir NFC kart okuyucusuna karşı konumlandırarak işlemleri imzalamak için kullanılabilir.

Bu NFC kartı 19.99$'a satılmaktadır ve piyasadaki diğer donanım cüzdanlarına kıyasla oldukça uygun fiyatlıdır. Bununla birlikte, formatı nedeniyle Tapsigner diğer cihazlar kadar çok seçenek sunmuyor. Açıkçası bir kart olduğu için bataryası, kamerası ya da mikro SD kart okuyucusu yok. Bence en büyük dezavantajı Hardware Wallet'da ekran olmaması, bu da onu bazı uzaktan saldırı türlerine karşı daha savunmasız hale getiriyor. Gerçekten de bu durum kullanıcıyı körü körüne imza atmaya ve bilgisayar ekranında gördüklerine güvenmeye zorluyor.


Sınırlamalarına rağmen, Tapsigner düşük fiyatı nedeniyle ilgi çekici olabilir. Bu Wallet, özellikle ekranlı bir Hardware Wallet ile korunan bir tasarruf Wallet'e ek olarak bir harcama Wallet'ün güvenliğini artırmak için kullanılabilir. Ayrıca küçük miktarlarda bitcoin tutan ve daha sofistike bir cihaza yüz avro yatırmak istemeyenler için de iyi bir çözümdür. Dahası, Tapsigner'ın Multisig konfigürasyonlarında veya potansiyel olarak gelecekte zaman kilitli Wallet sistemlerinde kullanılması ilginç avantajlar sunabilir.


## Tapsigner nasıl satın alınır?


Tapsigner [resmi Coinkite web sitesinden] (https://store.coinkite.com/store/category/tapsigner) satın alınabilir. Fiziksel bir mağazadan satın almak için sitede [sertifikalı satıcıların listesini] (https://coinkite.com/resellers) de bulabilirsiniz.


Ayrıca NFC iletişimiyle uyumlu bir telefona veya NFC kartlarını standart frekans olan 13,56 MHz'de okumak için bir USB cihazına ihtiyacınız olacaktır.


## Nunchuk ile bir Tapsigner nasıl başlatılır?


Tapsigner'ınızı aldıktan sonra ilk adım, açılmadığından emin olmak için ambalajı incelemektir. Paket hasar görmüşse, bu kartın ele geçirildiğini ve orijinal olmayabileceğini gösterebilir. CoinKite, Tapsigner'ınızı radyo dalgalarını engelleyen bir kılıfla birlikte teslim edecektir. Paketinizde bulunduğundan emin olun.


![TAPSIGNER NUNCHUK](assets/notext/02.webp)


Wallet'i yönetmek için **Nunchuk Wallet** mobil uygulamasını kullanacağız. Akıllı telefonunuzun NFC uyumlu olduğundan emin olun, ardından Nunchuk'u [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) veya doğrudan [`.apk` dosyası](https://github.com/nunchuk-io/nunchuk-android/releases) üzerinden indirin.


![TAPSIGNER NUNCHUK](assets/notext/03.webp)

Nunchuk'u ilk kez kullanıyorsanız, uygulama sizden bir hesap oluşturmanızı isteyecektir. Bu eğitimin amaçları doğrultusunda, bir hesap oluşturmanız gerekli değildir. Bu nedenle, hesap oluşturmadan devam etmek için "*Misafir olarak devam et*" seçeneğini seçin.

![TAPSIGNER NUNCHUK](assets/notext/04.webp)


Ardından "*Yardımsız Wallet*" üzerine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/05.webp)


Ardından, "*Kendi başıma keşfedeceğim*" düğmesine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/06.webp)


Nunchuk'a girdikten sonra, "*Tuşlar*" sekmesinin yanındaki "*+*" düğmesine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/07.webp)


"*NFC anahtarı ekle*" öğesini seçin.


![TAPSIGNER NUNCHUK](assets/notext/08.webp)


Ardından "*TAPSIGNER* Ekle" üzerine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/09.webp)


"*Devam*" üzerine tıklayın ve ardından Tapsigner NFC kartınızı akıllı telefonunuza yerleştirin.


![TAPSIGNER NUNCHUK](assets/notext/10.webp)


Tapsigner'ınız yeniyse, Nunchuk onu başlatmayı teklif edecektir. "*Evet*" üzerine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/11.webp)


Şimdi ana chain code'nizi nasıl generate yapacağınızı seçmeniz gerekecektir.


Tapsigner BIP32 standardını kullanır. Bu, bitcoinlerinizi güvence altına alan kriptografik anahtarlarınızın türetilmesinin BIP39 cüzdanları gibi bir Mnemonic ifadesine değil, doğrudan ana özel anahtara ve ana chain code'a dayandığı anlamına gelir. Bu 2 Elements, Wallet'nizin geri kalanını deterministik ve hiyerarşik olarak türetmek için HMAC işlevinden geçirilir.


Ana özel anahtar doğrudan Tapsigner'ınıza entegre TRNG (*True Random Number Generator*) tarafından oluşturulur. Öte yandan, ana chain code dışarıdan sağlanmalıdır. Bu adımda bir seçeneğiniz vardır: "*Otomatik*" seçeneğine tıklayarak Nunchuk'un otomatik olarak generate oluşturmasına izin verin veya "*Gelişmiş*" seçeneğini seçip verilen alana girerek kendiniz generate oluşturun.


![TAPSIGNER NUNCHUK](assets/notext/12.webp)


Ardından, bir PIN kodu seçmeniz gerekir. "*Başlangıç PIN kodu*" alanına, Tapsigner'ınızın arkasında yazılı olan PIN kodunu girin.


![TAPSIGNER NUNCHUK](assets/notext/13.webp)


Tapsigner'ınıza fiziksel erişimi güvence altına almak için bir PIN kodu seçin. Bu PIN kodu Wallet kurtarma işleminde hiçbir rol oynamaz. Tek işlevi, işlemleri imzalamak için Tapsigner'ınızın kilidini açmaktır. Unutmamak için bu PIN kodunu kaydettiğinizden emin olun. Devam etmek için "*Devam*" üzerine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/14.webp)

Başlatmak için Tapsigner kartınızı şimdi telefonunuzun arkasına yerleştirin.

![TAPSIGNER NUNCHUK](assets/notext/15.webp)


Nunchuk daha sonra Wallet'niz için generate kurtarma dosyasını oluşturacak ve NFC kartınızı kaybetmeniz durumunda bitcoinlerinize yeniden erişmenizi sağlayacaktır. Bu dosya, Tapsigner'ınızın arkasında yazılı olan yedekleme kodu ile şifrelenmiştir. Bitcoinlerinizi kurtarmak için bu dosyaya ve şifresini çözmek için koda kesinlikle ihtiyacınız olacaktır. Bu nedenle, bu kodun kağıt üzerinde bir kopyasını oluşturmanız önemlidir, çünkü NFC kartınızı kaybederseniz, şimdilik yalnızca kartta yazılı olduğu için bu koda erişim de kaybolacaktır. Ayrıca şifrelenmiş kurtarma dosyanızın birkaç yedeğini oluşturduğunuzdan emin olun.


![TAPSIGNER NUNCHUK](assets/notext/16.webp)


Wallet'iniz için bir isim seçin.


![TAPSIGNER NUNCHUK](assets/notext/17.webp)


Wallet'unuzun temeli şimdi kurulmuştur. Tapsigner'ınızın gerçekliğini doğrulamak için istediğiniz zaman "*Sağlık kontrolünü çalıştır*" düğmesine tıklayabilirsiniz.


![TAPSIGNER NUNCHUK](assets/notext/18.webp)


PIN kodunuzu girin.


![TAPSIGNER NUNCHUK](assets/notext/19.webp)


Ardından kartınızı telefonunuzun arkasına yerleştirin.


![TAPSIGNER NUNCHUK](assets/notext/20.webp)


## Tapsigner üzerinde bir Wallet nasıl oluşturulur?


Nunchuk ana sayfasına geri döndüğünüzde, Tapsigner'ınızın mevcut imzalama cihazlarında kayıtlı olduğunu görebilirsiniz.


![TAPSIGNER NUNCHUK](assets/notext/21.webp)


Şimdi Bitcoin Wallet için anahtarları generate yapmanız gerekecektir. Bunu yapmak için, "*Cüzdanlar*" sekmesinin sağındaki "*+*" düğmesine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/22.webp)


"*Yeni Wallet* oluştur" üzerine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/23.webp)


Ardından "*Mevcut anahtarları kullanarak yeni bir Wallet oluştur*" seçeneğini seçin.


![TAPSIGNER NUNCHUK](assets/notext/24.webp)


Wallet'nız için bir isim seçin ve ardından "*Devam*" düğmesine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/25.webp)


Bu yeni anahtar seti için imzalama cihazı olarak Tapsigner'ınızı seçin ve ardından "*Devam*" düğmesine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/26.webp)


Her şey sizi tatmin ediyorsa, oluşturma işlemini onaylayın.


![TAPSIGNER NUNCHUK](assets/notext/27.webp)

Daha sonra Wallet'nizin yapılandırma dosyasını kaydedebilirsiniz. Bu dosya yalnızca açık anahtarlarınızı içerir, yani birisi bu dosyaya erişse bile bitcoinlerinizi çalamaz. Ancak, tüm işlemlerinizi takip edebilirler. Bu nedenle, bu dosya yalnızca gizliliğiniz için bir risk oluşturur. Bazı durumlarda, Wallet'nizi kurtarmak için gerekli olabilir.

![TAPSIGNER NUNCHUK](assets/notext/28.webp)


Ve işte, Wallet'iniz başarıyla oluşturuldu!


![TAPSIGNER NUNCHUK](assets/notext/29.webp)


Tapsigner'ınızı kullanmadığınız zamanlarda, yetkisiz okumalara karşı korumak için radyo dalgalarını engelleyen Coinkite tarafından sağlanan kılıfta saklamayı unutmayın.


## Tapsigner'da bitcoin nasıl alınır?


Bitcoin almak için Wallet'unuza tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/30.webp)


Ardından bitcoin almak için oluşturulan Address'i kullanın. Daha önce bu Wallet üzerinden bitcoin aldıysanız, yeni bir boş Address almak için "*Al*" düğmesine tıklamanız gerekecektir.


![TAPSIGNER NUNCHUK](assets/notext/31.webp)


Göndericinin işlemi yayınlandıktan sonra, Wallet'ünüzde göründüğünü göreceksiniz.


![TAPSIGNER NUNCHUK](assets/notext/32.webp)


"*Madeni paraları görüntüle*" üzerine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/33.webp)


Yeni UTXO'ünüzü seçin.


![TAPSIGNER NUNCHUK](assets/notext/34.webp)


UTXO'inize bir etiket eklemek için "*Etiketler*"in yanındaki "*+*" işaretine tıklayın. Bu, madeni paralarınızın kaynağını hatırlamanıza ve gelecekteki harcamalarınız için gizliliğinizi optimize etmenize yardımcı olduğu için iyi bir uygulamadır.


![TAPSIGNER NUNCHUK](assets/notext/35.webp)


Mevcut bir etiketi seçin veya yeni bir etiket oluşturun, ardından "*Kaydet*" düğmesine tıklayın. Madeni paralarınızı daha yapılandırılmış bir şekilde düzenlemek için "*koleksiyonlar*" oluşturma seçeneğiniz de vardır.


![TAPSIGNER NUNCHUK](assets/notext/36.webp)


## Tapsigner ile bitcoin nasıl gönderilir?


Artık Wallet'nızda bitcoinler olduğuna göre, onları da gönderebilirsiniz. Bunu yapmak için, seçtiğiniz Wallet'ya tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/37.webp)


"*Gönder*" düğmesine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/38.webp)


Gönderilecek tutarı seçin ve ardından "*Devam*" düğmesine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/39.webp)


Amacını hatırlamak için gelecekteki işleminize bir "*not*" ekleyin.


![TAPSIGNER NUNCHUK](assets/notext/40.webp)

Ardından, belirlenen alana alıcının Address'sini manuel olarak girin.

![TAPSIGNER NUNCHUK](assets/notext/41.webp)


Ayrıca ekranın sağ üst köşesinde bulunan simgeye tıklayarak Address kodlu bir QR kodunu tarayabilirsiniz.


![TAPSIGNER NUNCHUK](assets/notext/42.webp)


"*İşlem Oluştur*" düğmesine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/43.webp)


İşleminizin ayrıntılarını doğrulayın, ardından Tapsigner'ınızın yanındaki "*İmzala*" düğmesine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/44.webp)


Kilidi açmak için PIN kodunuzu girin.


![TAPSIGNER NUNCHUK](assets/notext/45.webp)


Ardından Tapsigner'ı akıllı telefonunuzun arkasına yerleştirin.


![TAPSIGNER NUNCHUK](assets/notext/46.webp)


İşleminiz artık imzalanmıştır. Her şeyin doğru olup olmadığını son bir kez kontrol edin, ardından Bitcoin ağında yayınlamak için "*İşlemi Yayınla*" seçeneğine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/47.webp)


İşleminiz şimdi onay bekliyor.


![TAPSIGNER NUNCHUK](assets/notext/48.webp)


## Tapsigner'ın kaybolması durumunda Wallet nasıl kurtarılır?


Tapsigner'ınızı kaybettiyseniz, kartın arkasında belirtilen kodu kullanarak Wallet'inizi kurtarabilirsiniz. Bu nedenle bu kodu Tapsigner'dan ayrı olarak kaydetmeniz önemlidir, çünkü kart kaybolursa bu koda erişim de kaybolacaktır. Ayrıca Wallet'in şifrelenmiş yedeğine de ihtiyacınız olacaktır.


Kurtarma için Nunchuk uygulamasını kullanacağız, ancak bunun fonlarınızı geçici olarak bir Hot Wallet'de güvence altına almak anlamına geldiğini unutmayın. Tapsigner'ınız önemli miktarları güvence altına alıyorsa, bunun yerine yeni bir Coldcard ile aynı kurtarma sürecini izlemeyi düşünün.


Nunchuk uygulamasını açın ve "*Tuşlar*" sekmesinin yanındaki "*+*" düğmesine tıklayın.


![TAPSIGNER NUNCHUK](assets/notext/49.webp)


"*NFC anahtarı ekle*" öğesini seçin.


![TAPSIGNER NUNCHUK](assets/notext/50.webp)


"*TAPSIGNER anahtarını yedekten kurtar*" seçeneğini seçin.


![TAPSIGNER NUNCHUK](assets/notext/51.webp)


Daha sonra cihazınızın dosya gezginine yönlendirilirsiniz. Wallet cihazınızın şifrelenmiş yedek dosyasını bulun ve seçin. Normalde bu dosyanın adı `backup...` ile başlar.


![TAPSIGNER NUNCHUK](assets/notext/52.webp)


Yedekleme dosyasının şifresini çözen parolayı girin. Bu parola, Tapsigner'ınızın arkasında başlangıçta belirtilen parolaya karşılık gelir.


![TAPSIGNER NUNCHUK](assets/notext/53.webp)

Ardından kurtarma Wallet'iniz için bir isim seçin.

![TAPSIGNER NUNCHUK](assets/notext/54.webp)


Artık bitcoinlerinize yeniden erişim kazandınız. Wallet'nız artık Nunchuk uygulamasının "*Anahtarlar*" sekmesinde görünen bir Hot Wallet olarak yönetilmektedir. Ardından, bu anahtarı onunla ilişkilendirerek "*Cüzdanlar*" bölümünde yeni bir kriptografik anahtar seti oluşturmanız gerekir. Bunu yapmak için, bu eğitimin "*Tapsigner'da Wallet nasıl oluşturulur? "* bölümündeki adımları tekrar takip edebilirsiniz.


![TAPSIGNER NUNCHUK](assets/notext/55.webp)


Tapsigner'ınızı kaybettiyseniz, bitcoinlerinizi derhal sahip olduğunuz ve ideal olarak bir Hardware Wallet tarafından korunan başka bir Wallet'a aktarmanızı şiddetle tavsiye ederim. Gerçekten de, kaybettiğiniz Tapsigner potansiyel olarak yanlış ellerde olabilir. Bu nedenle, yeni kurtardığınız Wallet'u boşaltmanız ve kullanmayı bırakmanız önemlidir.


Tebrikler, artık Tapsigner'ı kullanmaya başladınız! Bu eğitimi faydalı bulduysanız, aşağıya bir beğeni bırakırsanız çok memnun olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!