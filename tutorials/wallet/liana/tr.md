---
name: Liana
description: Liana üzerinde bir Wallet'in kurulması ve kullanılması
---
![cover](assets/cover.webp)


![video](https://youtu.be/rTId6hfiRm0)


Bu eğitimde, Liana uygulamasının bir bilgisayarda nasıl kullanılacağını adım adım açıklayacağız. Diğer şeylerin yanı sıra, otomatik bir ardıl planın nasıl oluşturulacağını, normal durumlarda bitcoin almayı ve göndermeyi ve belirli bir süre sonra mevcut bir Wallet'ten fonları nasıl geri alacağınızı öğreneceksiniz.


Ocak 2025'te Liana ile uyumlu donanım cüzdanları şunlardı: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.


Mevcut bir Liana Wallet'den para kurtarmak istiyorsanız, aşağıdaki sunumu okuyun ve doğrudan "Bitcoinlerin kurtarılması" bölümüne gidin.


## Liana yazılımı ile tanışın


Liana, özellikle otomatik bir miras sisteminin veya sağlam bir yedekleme mekanizmasının bir parçası olarak gelişmiş cüzdanların oluşturulması ve yönetimi için tasarlanmış açık kaynaklı bir yazılım paketidir. Proje 2022 yılından bu yana Kévin Loaec ve Antoine Poinsot tarafından kurulan Wizardsardine şirketi tarafından geliştirilmektedir. Resmi web sitesinde Liana, "kurtarma ve miras alma işlevlerine sahip, kişisel kürasyon için basit bir Wallet" olarak sunuluyor. Yazılım bilgisayarlarda - Linux, MacOS, Windows - çalışmaktadır ve (açık) kaynak kodu [GitHub'da] mevcuttur (https://github.com/wizardsardine/Liana).


Liana, gelişmiş bir Wallet oluşturmak için Bitcoin'nin programlanabilirliği üzerine kurulmuştur. Özellikle, fonların yalnızca belirli bir süre geçtikten sonra harcanmasına izin veren ve Bitcoin'lerin geri kazanımında yer alan zaman kilitlerinden (*timelocks*) yararlanır. Bir Liana Wallet böylece birkaç harcama yolundan oluşur:




- Her zaman mevcut olan bir ana harcama yolu;
- Belirli bir süre sonra erişilebilir hale gelen en az bir kurtarma yolu.


Aşağıdaki şemada iki harcama yolu olan bir Wallet'in çalışması gösterilmektedir:


![Schéma explicatif](assets/fr/01.webp)


Bu işlem, aşağıdakiler de dahil olmak üzere çeşitli konfigürasyonları ayarlamanıza olanak tanır:




- Kullanıcının ölümü halinde varislerin fonları geri almasını sağlayan bir veraset (veya miras) planı. Bu konuda daha fazla bilgi için BTC102 kursunun [bölüm 4](https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f/233c88d3-2e8e-5eba-ac06-efe67a209038) bölümünü okumanızı tavsiye ederiz.
- Kurtarma süresine sahip güçlendirilmiş bir yedekleme, kullanıcıya ilgili gizli ifadeyi saklamak zorunda kalmadan ve örneğin bir hırsızlık sırasında çalınması riskini almadan Wallet'sını kullanma imkanı verir.
- Bitcoin ile başlayan insanlar için bir güvenlik ağı: kendi Wallet'lerini yönetecekler ve "vasileri" (örneğin bir akraba) belirli bir süre sonra fonlarını geri alma hakkını saklı tutacak.
- Bir şirketin ortakları gibi bir veya daha fazla katılımcının ortadan kaybolmasıyla başa çıkmak için zaman içinde azaltılmış gereksinimlere sahip çok taraflı bir imza şeması (*Multisig*).


Liana'ün en büyük gücü, cari harcamalar için kullanılan ana anahtarın kaybedilmesi durumunda fonların geri kazanılmasını garanti etmenin standart bir yolunu sunmasıdır. Bu, özellikle de konu hakkında yeterince bilgi sahibi değilseniz, risklerle dolu olan fonların temiz bir şekilde saklanması için büyük bir yeniliği temsil etmektedir. Bu nedenle Liana, en riskten kaçınan kullanıcıları bile fonlarını tutmak için bir saklama kuruluşu (Exchange platformu gibi) kullanmayı bırakmaya ve Bitcoin'ün Cypherpunk ethosuna uygun olarak paralarının Ownership'ini yeniden kazanmaya teşvik edebilir.


Elbette Liana'in dezavantajları vardır. Bunlardan ilki, Bitcoin Blockchain üzerinde bir işlem yaparak Wallet'nizi düzenli olarak güncellemeniz gerektiğidir. Bu (yazılımı ne sıklıkta kullandığınıza bağlı olarak) zahmetli ve maliyetli (o zamanki ücret seviyesine bağlı olarak) olabilir, ancak ekstra güvenlik için ödediğiniz bedeldir.


İkinci bir olumsuz nokta gizlilik olabilir. Yapılandırmaya başka bir kişiyi dahil ettiğinizde, o kişi tüm adreslerinizi öğrenebilir ve bu nedenle faaliyetlerinizi izleyebilir. Bununla birlikte, güçlendirilmiş bir yedeklemeyi veya varisinizin Wallet'un ayrıntılarını hemen bilmediği bir halefiyet planını tercih ederseniz, bu bir sorun olmayacaktır.


## Hazırlık


Bu eğitimde, bir halefiyet planı oluşturacağız. Kullanacağız :




- Günlük harcamalar için bir Ledger Nano S Plus;


https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4


- Fonları geri almak için kullanılan bir Blockstream Jade;


https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3


- Wallet Descriptor'i saklamak için iki depolama ortamı (USB bellekler);
- Fonların geri alınmasına ilişkin talimatları içeren bir halefiyet mektubu;
- Geri kazanım cihazının (Jade) kullanılmadığından emin olmak için numaralandırılmış mühürlü bir torba.


## Kurulum ve yapılandırma


Resmi Wizardsardine web sitesini ziyaret edin ve Liana'ü https://wizardsardine.com/Liana/ adresinden indirin. Ayrıca yazılımın orijinalliğini kontrol edebileceğiniz en son sürümü [GitHub deposundan] (https://github.com/wizardsardine/Liana/releases) indirebilirsiniz. Bu eğitimde kullanılan sürüm 0.9'dur.


![Télécharger Liana](assets/fr/02.webp)


Kurulumdan önce yazılımın orijinalliğini ve bütünlüğünü manuel olarak nasıl doğrulayacağınızı öğrenmek için bu eğitime başvurmanızı öneririz:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Yazılımı makinenize kurun ve başlatın. Wallet'ünüzü yapılandırmak için "*Yeni bir Liana Wallet* oluştur" seçeneğini seçin.


![Accueil Liana](assets/fr/03.webp)


Wallet türünüzü seçin. Kurtarma süresine sahip gelişmiş bir yedekleme kurmak istiyorsanız, "*Kendiniz oluşturun*" seçeneğini seçebilir ve varsayılan şemayı tercih edebilirsiniz. Bu, Hardware Wallet kurtarma ifadesini saklamanız gerekmemesi dışında hemen hemen aynı şekilde çalışacaktır.


Burada daha karmaşık bir konfigürasyon oluşturan *Genişleyen Multisig* durumunu göz ardı ediyoruz.


Bu eğitimin amaçları doğrultusunda, basit kalıtım kullanacağız.


![Choisir type de portefeuille](assets/fr/04.webp)


Aşağıda kısa bir açıklama yer almaktadır.


![Rapide explication](assets/fr/05.webp)


Açıklamayı okuduktan sonra, Liana Wallet'unuzun anahtarlarını ayarlayabileceksiniz. Bu, hesabınızın harcama özelliklerini belirlediği için çok önemli bir adımdır.


![Configurer clés](assets/fr/06.webp)


Öncelikle, "Gelişmiş Ayarlar" menüsünde "Descriptor tipine", yani Contract'nin zincire nasıl yazılacağına karar verebilirsiniz. İki tip arasında seçim yapabilirsiniz: P2WSH (SegWit) veya Taproot. Her iki durumda da harcama koşullarının semantiği aynı olacaktır. P2WSH Contract'nin anlaşılmasını kolaylaştırırken, Taproot kullanılmayan koşulları gizlemesi ve geri alma sırasında maliyet tasarrufu sağlaması açısından daha üstündür.


Bu seçim isteğe bağlıdır: şüpheniz varsa, varsayılan seçeneği bırakın (0.9 sürümü durumunda P2WSH, ancak bu değişebilir).


![Choisir le type de descripteur](assets/fr/07.webp)


Ardından, birincil anahtarınızı (*primary key*) yapılandırın. Bu anahtar (ya da daha doğrusu bu anahtarlar kümesi), herhangi bir zamanlama koşuluna tabi olmayan mevcut fon harcamaları için kullanılacaktır. "*Set*" üzerine tıklayarak, ilgili *imzalama cihazını* seçebilirsiniz. Bizim durumumuzda, Ledger Nano S Plus Hardware Wallet'i seçtik.


Genişletilmiş genel anahtarın cihazdan paylaşılmasına izin verin. Bu anahtara anlamlı bir ad verin (bu durumda "Nano S+"). Cihazda yüklü olan tüm uygulamaların normal şekilde çalışmaya devam edeceğini unutmayın.


![Configurer clé principale](assets/fr/08.webp)


Ardından, geri ödeme gecikmesini, yani fonların *miras anahtarı* tarafından harcanabileceği süreyi ayarlayın. Bu gecikme, her blok ortalama 10 dakika ile ayrılacak şekilde blok cinsinden tanımlanır. Bu süre 10 dakika (1 blok) ile yaklaşık 15 ay (65.535 blok) arasında değişebilir. Bu üst sınır, kilitleme süresi 16 bit olarak kodlandığından Bitcoin protokolünün bir sınırlamasıdır.


Özel durumlar dışında, en uzun teslim süresini tercih edin: 15 ay veya 65.535 blok. Bu size maliyet tasarrufu sağlayacaktır. Bununla birlikte, bu uygulamayı "ritüelleştirmek" ve unutmaktan kaçınmak için güncelleme prosedürünü ("Wallet'in Güncellenmesi" bölümünde açıklanmıştır) yılda bir kez, her zaman yılın aynı zamanında gerçekleştirmenizi öneririz.


Burada, testlerimizi gerçekleştirmek için bir saatlik (6 blok) bir kurtarma süresi ayarladık.


![Configurer temps de verrouillage](assets/fr/09.webp)


Son olarak, emlak anahtarınızı ayarlayın. Bu anahtar (ya da daha doğrusu anahtar seti) kaybolmanız durumunda fonları kurtarmak için kullanılacaktır. "*Ayarla*" üzerine tıklayın, imzalama cihazını seçin ve genişletilmiş ortak anahtarın paylaşımını doğrulayın.


Bu eğitim için Jade'i seçtik. Anahtara çağrıştırıcı bir isim verin (burada "Jade"). İlk cihazda olduğu gibi, geleneksel hesaplar çalışmaya devam edecektir.


![Configurer clé de succession](assets/fr/10.webp)


Tüm bu işlemler tamamlandıktan sonra, her şeyin yolunda olup olmadığını kontrol edin ve seçimlerinizi onaylamak için "*Devam*" düğmesine tıklayın.


![Confirmer clés](assets/fr/11.webp)


Bir sonraki adım Wallet Descriptor'unuzu kaydetmektir. Bu, hesabınızdaki fonları bulmak için ihtiyacınız olan bilgidir. Mnemonic ifadesinin aksine, Descriptor para harcamanıza izin vermez, bu nedenle bunu ifşa etmek yalnızca bir gizlilik sorunu yaratacaktır (kişi tüm işlemlerinizi bilecektir).


Descriptor'nin iki kopyasını USB bellek gibi elektronik ortamlara kaydedin. Elektronik ortamın hasar görmesi durumunda bunlara erişebilmek için iki kopyayı da kağıda yazdırdığınızdan emin olun. Her yedekleme bir imza cihazı ile ilişkilendirilmelidir.


![Sauvegarder descripteur](assets/fr/12.webp)


Descriptor'ümüz (eğitimin sonunda analiz edilmiştir) aşağıdaki gibidir:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


İlk Wallet yapılandırmasındaki son adım, imza cihazları olarak hizmet veren donanım cüzdanlarının her birinde Descriptor'ün doğrulanmasıdır.


![Enregistrer descripteur](assets/fr/13.webp)


Her imzalama cihazı için aynı işlemi yapın. Descriptor'nin her bir Hardware Wallet'ya eklendiğini kontrol etmeniz ve onaylamanız gerekecektir.


![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)


Wallet bilgileriniz artık kayıtlıdır ve geriye kalan tek şey Bitcoin ağına nasıl bağlanmak istediğinizi yapılandırmaktır. Kendi düğümünüzü (yerel veya uzak) kullanmayı veya WizardSardine'in altyapısını kullanmayı seçebilirsiniz. İkinci durumda, bir e-posta Address'u Wallet'inize bağlamanız gerekecek, bu da Descriptor'i almanızı sağlayacaktır. WizardSardine tüm işlemlerinize erişebilecektir. Bu nedenle ilk seçenek önerilmektedir.


![Sélectionner connexion réseau](assets/fr/15.webp)


Biz kendi node'umuzu kullanmayı seçtik. Mevcut bir düğümü kullanabilir veya makinenize bir *pruned düğümü* kurabilirsiniz. Başka bir node'a erişiminiz yoksa, makinenize kendi node'unuzu kurun, bu biraz zaman alacaktır (birkaç gün mertebesinde).


![Choisir type de nœud](assets/fr/16.webp)


Bu eğitim için mevcut (herkese açık) bir Electrum sunucusu kullandık. Ancak dikkatli olun! Liana Wallet ile yaptığımız tüm aktivitelere erişimi vardı. Bu yüzden gizliliğinizi korumak istiyorsanız kendi node'unuzu kullanın.


![Connexion serveur Electrum public](assets/fr/17.webp)


Düğüm yapılandırması tamamlandığında, yeni oluşturduğunuz Liana Wallet'i görüntüleyen ana ekran açılmalıdır.


Kurtarma ünitesini güvenli bir yerde saklama fırsatını değerlendirin. Ölümünüz halinde mirasçılarınız tarafından bulunabilmesi için stratejik bir yerde saklanmalıdır.


Daha fazla güvenlik için, kurtarma için kullanılan bileşenleri mühürlü bir torbaya (*kurcalamaya karşı korumalı torba*) koyabilir ve seri numarasını bir yere yazabilirsiniz. Bu, kimsenin ona erişmemesini ve cihazınızın geçerliliğini korumasını sağlar.


Örneğimizde, aşağıdaki Elements'yi bir araya getirdik:




- Blockstream Jade emlak için imza cihazı olarak;
- Cihazı bağlamak ve şarj etmek için bir USB kablosu;
- Cihazın arızalanması veya hasar görmesi durumunda cümlenin kağıt yedeği (ortamın metal olabileceğini ve bu nedenle örneğin Cryptosteel kapsüllerde olduğu gibi Elements'den korunabileceğini unutmayın);
- Wallet Descriptor içeren USB anahtarı;
- Arıza veya USB anahtarının hasar görmesi durumunda Descriptor'in kağıt yedeği (bu yedek burada fotoğraflanmamıştır);
- Fonların geri alınması için atılacak adımları açıklayan bir halefiyet mektubu.


![Éléments de récupération](assets/fr/18.webp)


Ve bu maddeleri Seal'nin altına koyduk!


![Sachet scellé récupération](assets/fr/19.webp)


## Fonların teslim alınması


Liana'ün ana ekranı bakiyenizi ve Wallet'ünüze bağlı işlemleri (geçmiş ve güncel) görüntüler. Bizim durumumuzda, bakiye sıfırdır ve bu normaldir.


![Écran principal](assets/fr/20.webp)


Fon almak için "*Alma*" sekmesine gidin ve "*generate Address*" üzerine tıklayın. Ekranınızda yeni bir Address görünmelidir. Geleneksel cüzdanlardan daha uzundur: bağımsız bir Contract'e (P2WSH veya Taproot) bağlı bir Address'dir.


![Générer nouvelle adresse](assets/fr/21.webp)


"*Donanım aygıtında doğrula*" seçeneğine tıklayarak bu Address'i Hardware Wallet'unuzda doğrulamanız gerekir.


![Vérifier adresse portefeuille matériel](assets/fr/22.webp)


Para gönderildikten sonra, işlem ana ekranda görünür (önce onaylanmamış, sonra onaylanmış olarak). Burada, bu test için 50.000 satoshis (transfer sırasında 50 doların biraz üzerinde) gönderdik. Sizin durumunuzda transfer edilen miktarın, işlem ücretleri nedeniyle bu değerden çok daha yüksek olması gerekeceğini söylemeye gerek yok.


![Vérifier solde](assets/fr/23.webp)


"*Coins*" sekmesine giderek fonlarınızın son kullanma durumunu kontrol edebilirsiniz. Bu sekme size Wallet'inizdeki farklı coinleri (UTXO) gösterir. Burada, işlemimiz tarafından oluşturulan 50.000 satoshis Coin'nin aynı gün (bir saatlik süre) sona erdiğini görebiliriz.


![Obtenir informations pièce](assets/fr/24.webp)


Bitcoin'te kullanılan UTXO temsil modelini daha iyi anlamak için Loïc Morel tarafından yazılan Bitcoin'te gizlilik konulu kursun ilk bölümüne başvurabilirsiniz:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Cari harcamalar


Mevcut harcama, Liana kullanımı için normal durumdur. Ana anahtar ile bitcoin göndermek, Electrum veya Sparrow gibi tüm klasik Bitcoin cüzdanlarında olduğu gibi çalışır.


Bir ücretlendirme yapmak için "*Gönder*" sekmesine gidin ve temel bilgileri girin: alıcının BTC Address'u, gönderilecek miktar ve istenen ücretlendirme oranı. Kişisel rahatlığınız için bir açıklama (yerel olarak kaydedilmiş) da eklenebilir. Örneğimizde, belirli bir Bob'a 4 sat/ov veya işlem sırasında 0,67 $ ücret oranı için 10.000 satoshis gönderdik.


Liana ayrıca "Coin kontrolü" sunar: hangi Coin'yi (UTXO) harcamak istediğinizi belirtirsiniz. Burada, Coin'nin daha önce yarattığı 50.000 satoshiyi seçtik.


![Envoyer fonds clé principale](assets/fr/25.webp)


Ardından "*İmzala*" düğmesine tıklayarak ana anahtara bağlı imza cihazınızla işlemi imzalayın. İşlemi Hardware Wallet cihazınızda doğrulamanız ve onaylamanız gerekecektir. Burada, işlemi imzalamak için Nano S Plus kullandık.


![Signer transaction clé principale](assets/fr/26.webp)


Son olarak, "*Broadcast*" seçeneğine tıklayarak işlemi ağ üzerinden yayınlayın. Para göndermenin kullanılmış coin'ler için kurtarma süresini sıfırlayacağını unutmayın.


![Diffuser transaction clé principale](assets/fr/27.webp)


İşlem ana ekranda görünecek ve bakiyeniz güncellenecektir.


![Solde après dépense](assets/fr/28.webp)


## Portföy güncellemesi


Yukarıda açıklandığı gibi, Liana Wallet, Blockchain üzerinde bir işlem gerçekleştirerek fonlarınızı düzenli olarak güncellemenizi gerektirir. Bunu yapmazsanız, fonlarınız mirasçınız (veya gelişmiş yedekleme durumunda ikinci cihazınız) tarafından geri alınabilir. Bu durum son derece tehlikeli değildir, ancak bu mekanizmanın kurulma amacını ortadan kaldırır: bir güvenlik ağından yararlanırken güvenilir bir üçüncü tarafa başvurmadan bitcoinlerinizin kontrolünü elinizde tutmak.


Fonlarınızın (veya bir kısmının) süresi dolmadan önce bir uyarı görüntülenir ve kurtarma anahtarı ile harcanabilir. "Kurtarma yolunuzun" (*kurtarma yolu*) yakında kullanılabilir olacağını belirtecektir. Kurtarma süremizin kısalığı (bir saat) göz önüne alındığında, bu mesaj bizim durumumuzda doğrudan görüntülenir.


![Avertissement chemin récupération](assets/fr/29.webp)


Son tarih yaklaştığında, ilgili fonları güncellemenizi isteyen bir düğme görünecektir.


![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)


Madeni paralarınızı güncellemek için "*Madeni Paralar*" sekmesine gidin ve ilgili Coin kutusundaki "*Coin'ü Yenile*" seçeneğine tıklayın. Birden fazla madeni paranız varsa, gizlilik nedeniyle bunları tek tek ve nispeten kısa aralıklarla yenilemelisiniz. Maliyetleri düşük tutmak için, tüm Wallet'u yeni bir alıcı Address'e göndererek fonlarınızı birleştirebilirsiniz, ancak bu gizliliğinizi etkileyecektir.


![Actualiser pièce](assets/fr/31.webp)


İşlem için istediğiniz ücret oranını belirtin. Bu kendinize yapacağınız bir transfer olduğu için, özellikle son kullanma tarihinden birkaç gün önce yaparsanız, oldukça düşük bir ücret oranı belirleyebilirsiniz.


![Transfert à soi-même](assets/fr/32.webp)


İşlem ("*self-transfer*" etiketli) yalnızca "*Transactions*" sekmesinde görünür olacaktır.


![Transactions après auto-transfert](assets/fr/33.webp)


Onaylandıktan sonra Coin'iniz güvende! Bir sonraki son kullanma tarihine kadar içiniz rahat olabilir.


## Bitcoin kurtarma


Liana Wallet'ten fonları kurtarırken iki durumdan biriyle karşı karşıya kalabilirsiniz. Yazılımın yüklü olduğu bilgisayara erişiminiz olabilir, bu durumda tek yapmanız gereken onu açmaktır (gelişmiş yedekleme modelinde bu gerçekleşecektir). Ancak, bu bilgisayara erişiminiz olmayabilir, bu nedenle burada sıfırdan başlayacağız. Kurtarma prosedürünün her iki durumda da aynı olduğunu unutmayın.


Başlamak için Liana'yı [resmi Wizardsardine web sitesinden] (https://wizardsardine.com/Liana/) veya yazılımın orijinalliğini kontrol edebileceğiniz [GitHub deposundan] (https://github.com/wizardsardine/Liana/releases) indirin. Yazılımı kurun ve çalıştırın. Bizim durumumuzda kullanılan sürüm 0.9'dur, bu nedenle görseller değişmiş olabilir. Karşılama ekranında "Mevcut bir Liana Wallet ekle" seçeneğini seçin.


![Ajouter portefeuille existant](assets/fr/34.webp)


Ağa nasıl bağlanmak istediğinizi yapılandırın. Kendi düğümünüzü (yerel veya uzak) kullanmayı veya WizardSardine'in altyapısını kullanmayı seçebilirsiniz. İkinci durumda, fonların otomatik olarak bulunabilmesi için Address oluşturucusu tarafından kullanılan Wallet e-postasına ihtiyacınız olacaktır. Eğer bu bilgiye sahip değilseniz, ilk seçeneği seçin.


![Sélectionner connexion réseau](assets/fr/35.webp)


Kendi düğümünüzü kullanıyorsanız, Wallet Descriptor'u içe aktarın. Bu, hesabın teknik bir açıklamasıdır ve içinde tutulan fonları almanızı sağlar. Bizim durumumuzda, aşağıdaki bilgilerdir:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


![Importer descripteur](assets/fr/36.webp)


Liana daha sonra sizden bir Mnemonic cümlesi girmenizi ister. Eğer çalışan bir imza cihazınız varsa (Hardware Wallet), bu kısmı atlayın. Cihazınız kayıp veya hasarlıysa, ancak ilgili 12 veya 24 kelimeye sahipseniz, yine de bu seçeneği kullanabilirsiniz. Güvenli tarafta olmak için (kurtarılacak miktar yüksekse), yine de yeni bir Hardware Wallet edinmenizi ve üzerindeki anahtarları geri yüklemek için Mnemonic'yi kullanmanızı öneririz.


Bizim durumumuzda, Blockstream Jade Hardware Wallet'ü bir kurtarma cihazı olarak kullanıyoruz ve bu adımı atlamayı ("*Skip*") seçiyoruz.


![Passer phrase mnémotechnique](assets/fr/37.webp)


Ekranda seçerek imza cihazınızdaki Descriptor'yı kontrol edin ve kaydedin. Hardware Wallet'iniz görünmüyorsa, bağlı ve kilidinin açık olduğunu kontrol edin. Bu bilgilerin cihazınıza eklendiğini kontrol edin ve onaylayın.


![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)


Düğümünüzü yapılandırın. Mevcut bir düğümü kullanabilir veya makinenize bir *pruned düğümü* kurabilirsiniz. Bizim durumumuzda, mevcut bir node kullandık.


![Choisir type de nœud](assets/fr/39.webp)


Bu eğitim için halka açık bir Electrum sunucusu kullandık. Ancak, Liana Wallet ile tüm faaliyetlerimize erişimi vardı. Gizliliğinizi korumak istiyorsanız, kendi node'unuzu kullanmanız daha iyi olacaktır.


![Connexion serveur Electrum public](assets/fr/17.webp)


Düğümünüzü kurduktan sonra, hesaba bağlı bakiyeyi ve geçmiş işlemleri görüntüleyebileceğiniz ana Wallet ekranına yönlendirilirsiniz. Ayrıca fonların alınıp alınamayacağını da görebilirsiniz. Burada, bir Coin'in alınabileceğini görüyoruz.


![Accueil Liana récupération](assets/fr/40.webp)


Wallet'deki fonları kurtarmak için sol alttaki Ayarlar'a ("*Ayarlar*") gidin ve "*Kurtarma*"ya tıklayın.


![Récupération dans paramètres](assets/fr/41.webp)


Uygun kutuyu işaretleyerek Coin'i Wallet'te harcayın. Parayı göndermek istediğiniz BTC Address'ü ve işlem ücreti oranını belirtin. Ardından "*Sonraki*" üzerine tıklayın.


![Récupération des pièces](assets/fr/42.webp)


"*İmzala*" düğmesine tıklayarak ve Hardware Wallet'nızda işlemi doğrulayarak işlemi imzalayın.


![Signer transaction clé de récupération](assets/fr/43.webp)


Ardından "*Yayın*" seçeneğine tıklayarak ağ üzerinden yayınlayın.


![Diffuser transaction clé de récupération](assets/fr/44.webp)


İşlem ana ekranda görünmelidir. Onaylandıktan sonra kurtarma işlemi tamamlanmıştır!


![Écran principal après récupération](assets/fr/45.webp)


## Bonus: Descriptor analizi


Descriptor, bir dizi adresi kapsamlı bir şekilde tanımlayan, insan tarafından okunabilir bir karakter dizisidir. Gelişmiş bir Wallet'un parçalarını (UTXO) almak için bir dizi temel bilgiyi birleştirir. Descriptor'in yazım şekli, Andrew Poelstra, Pieter Wuille ve Sanket Kanjalkar tarafından 2019 yılında geliştirilen komut dosyası dili olan [Miniscript syntax] (https://bitbox.swiss/blog/understanding-Bitcoin-miniscript-part-2/)'a dayanmaktadır.


Bu karakter dizisinin neden önemli olduğunu daha iyi anlamak için örneğimizdeki Descriptor'yi analiz edelim, yani :


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


Bu Descriptor'ten aşağıdaki bilgiler çıkarılabilir:




- wsh` (*witness script Hash*'in kısaltması): Bu, oluşturulan işlemsel çıktı türüdür. Eğer Taproot kullanmayı seçmiş olsaydık, tanımlayıcı `tr` olacaktı.
- veya_d`: Bu, masrafın kabul edilmesi için aşağıdaki iki* koşuldan birinin karşılanması gerektiğini belirten mantıksal bir işleçtir (`_d` belirli bir sözdizimini belirtir).
- pk` (*açık anahtarın* kısaltması): Bu işleç, verilen bir imzayı aşağıdaki açık anahtarla karşılaştırır ve cevabı Boolean (DOĞRU veya YANLIŞ) olarak verir.
- `[3689a8e7/48'/0'/0'/2']`: Bu öğe, ana Hardware Wallet (bu durumda Nano S Plus) için ana anahtarın *parmak izini* ve bağlantılı genişletilmiş özel anahtara (diğer tüm özel anahtarların türetildiği) giden türetme yolunu içerir.
- `xpub6FKY ... WQa`: Bu, ana Hardware Wallet'ye (burada Nano S Plus) bağlı genişletilmiş açık anahtardır
- `/<0;1>/*`: Bunlar basit anahtarlar ve adresler elde etmek için türetme yollarıdır: alım için `0`, dahili işlemler (*değiştir*) için `1`, klasik Wallet yazılımının "boşluk sınırı" yönetimine benzer şekilde yapılandırılabilir bir şekilde birkaç adresin sıralı olarak türetilmesine izin veren bir "joker karakter" (`*`) ile.
- ve_v`: Bu, harcamanın kabul edilmesi için *aşağıdaki iki* koşulun karşılanması gerektiğini belirten mantıksal bir işleçtir (`_v` belirli bir sözdizimini belirtir).
- `v:pkh` (*verify: public key Hash* için kısa): Bu işleç, verilen bir imzayı ve açık anahtarı takip eden Hash (*Hash*) açık anahtarına karşı doğrular. Bu aslında P2PKH ve P2WPKH betikleri için yapılan kontrolün aynısıdır.
- `[42e629dd/48'/0'/0'/2']`: Bu, donanım kurtarma Wallet'in ana anahtarının izinin (bu durumda Jade) belirtilmesi dışında, yukarıdaki ile aynı unsurdur (iz ve türetme yolundan oluşur).
- `xpub6DpQ ... WQd`: Bu, donanım kurtarma Wallet (burada Jade) ile bağlantılı genişletilmiş genel anahtardır.
- `older(6)` : Bu işleç, oluşturulan işlem çıktısının harcanabilmesi için kesinlikle 6 bloktan daha büyük bir yaşa sahip olması gerektiğini kontrol eder.


Son veri öğesi (`8alrve5h`) Descriptor sağlama toplamıdır ve Wallet tanımlayıcısına karşılık gelir.


Bu Wallet tarafından oluşturulan komut dosyaları aşağıdaki şekli alacaktır:


```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```


Bitcoin Wallet'inizin güvenliği de nasıl çalıştığını anlamanıza bağlı olduğundan, Plan ₿ Network hakkındaki bu ücretsiz eğitim kursunu alarak deterministik ve hiyerarşik cüzdanların mekanizmalarını derinlemesine incelemenizi öneririm:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f