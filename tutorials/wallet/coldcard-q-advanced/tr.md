---
name: COLDCARD Q - Gelişmiş
description: COLDCARD Q'nun gelişmiş seçeneklerini kullanma
---
![cover](assets/cover.webp)


![video](https://youtu.be/6L2hhT0J27s)


Bir önceki eğitimde, COLDCARD Q'nun ilk yapılandırmasını ve yeni başlayanlar için temel işlevlerini ele almıştık. COLDCARD Q'nuzu yeni aldıysanız ve henüz kurmadıysanız, buraya devam etmeden önce o eğitimle başlamanızı tavsiye ederim:


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Bu yeni eğitim, ileri düzey ve paranoyak kullanıcılar için tasarlanmış COLDCARD Q'nun gelişmiş seçeneklerine adanmıştır. Aslında, COLDCARD'lar birçok gelişmiş güvenlik özelliği ile diğer donanım cüzdanlarından ayrılır. Elbette, tüm bu seçenekleri kullanmak zorunda değilsiniz. Sadece güvenlik stratejinize uygun olanları seçin.


**Uyarı**, bu gelişmiş seçeneklerden bazılarının yanlış kullanımı bitcoinlerinizin kaybına veya Hardware Wallet'ınızın yok olmasına neden olabilir. Bu nedenle her bir seçeneğe ilişkin tavsiye ve açıklamaları dikkatlice okumanızı şiddetle tavsiye ederim.


Başlamadan önce, 12 veya 24 kelimelik Mnemonic ifadenizin fiziksel bir yedeğine erişiminiz olduğundan emin olun ve aşağıdaki menü aracılığıyla geçerliliğini kontrol edin: gelişmiş/Araçlar > Tehlike Bölgesi > seed İşlevleri > seed Sözcüklerini Görüntüle.


![CCQ](assets/fr/01.webp)


## BIP39 passphrase


BIP39 passphrase'ün ne olduğunu bilmiyorsanız veya nasıl çalıştığını tam olarak bilmiyorsanız, passphrase kullanımıyla ilgili riskleri anlamak için gereken teorik temelleri kapsayan bu eğitime önceden bir göz atmanızı şiddetle tavsiye ederim:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase'i Wallet'nize kurduktan sonra, Mnemonic'nızın bitcoinlerinize yeniden erişim sağlamak için tek başına yeterli olmayacağını unutmayın. Hem Mnemonic'ya hem de passphrase'e ihtiyacınız olacak. Dahası, COLDCARD Q'nuzun kilidini her açtığınızda passphrase'i girmeniz gerekecektir. Bu, COLDCARD'a fiziksel erişimi ve PIN bilgisini passphrase olmadan yetersiz hale getirerek güvenliği artırır.


COLDCARD'larda, passphrase'inizi yönetmek için iki seçeneğiniz vardır:


1. **Klasik giriş:** Diğer donanım cüzdanlarında yaptığınız gibi Hardware Wallet'unuzu her kullandığınızda passphrase'u manuel olarak girersiniz. COLDCARD Q, tam klavyesi ile bu görevi basitleştirir.


2. **passphrase'inizi şifrelemeyi ve bir microSD kartta saklamayı seçebilirsiniz. Bu durumda, microSD'yi her kullandığınızda COLDCARD Q'ya takmanız gerekecektir. Bu microSD'nin yalnızca COLDCARD Q'nuzda çalışacağını ve bir yedek olmadığını unutmayın. Bu nedenle, passphrase'inizin bir kopyasını kağıt veya metal gibi fiziksel bir ortamda da saklamanız çok önemlidir.


BIP39 passphrase'nizi ayarlamak için "*passphrase*" menüsüne erişin.


![CCQ](assets/fr/02.webp)


Klavyeyi kullanarak passphrase'ünüzü girin. Güçlü bir passphrase (uzun ve rastgele) seçtiğinizden ve fiziksel bir yedekleme yaptığınızdan emin olun.


![CCQ](assets/fr/03.webp)


passphrase'ünüzü ayarladıktan sonra, COLDCARD Q size bu passphrase ile ilişkili yeni Wallet'in ana anahtar parmak izini gösterecektir. Bu parmak izini kaydettiğinizden emin olun. Gelecekte cihazınızı kullanırken passphrase'ünüzü yeniden girdiğinizde, görüntülenen parmak izinin kaydettiğinizle eşleşip eşleşmediğini kontrol edebileceksiniz. Bu kontrol, passphrase'ünüzü girerken bir hata yapmadığınızdan emin olmanızı sağlar.


![CCQ](assets/fr/04.webp)


Şimdi bu passphrase'yı Mnemonic ifadenize uygulamak ve yeni Wallet'i etkinleştirmek için "*ENTER*" tuşuna basabilirsiniz. Bu passphrase'yı bir microSD'ye kaydetmeyi tercih ederseniz, kartı uygun yuvaya takın ve "*1*" tuşuna basın.


![CCQ](assets/fr/05.webp)


passphrase'unuz şimdi uygulanmıştır. Anahtar baskısı ana ekranda ve ekranın üst kısmında görünür.


![CCQ](assets/fr/06.webp)


COLDCARD Q'nuzun kilidini her açtığınızda, "*passphrase*" menüsüne erişmeniz ve cihazda kayıtlı Mnemonic'e uygulamak ve doğru Bitcoin Wallet'e erişmek için passphrase'nizi yukarıdaki gibi girmeniz gerekecektir.


![CCQ](assets/fr/07.webp)


passphrase'ü bir microSD karta kaydettiyseniz, her kullandığınızda kartı COLDCARD'a takın ve "*passphrase*" menüsüne erişin. COLDCARD'ınız passphrase'ü doğrudan microSD'den yükleyecektir, böylece manuel olarak girmenize gerek kalmayacaktır. "*Kaydedilenleri Geri Yükle*" üzerine tıklayın.


![CCQ](assets/fr/08.webp)


Yüklenen passphrase'in uzunluğunun ve ilk harfinin doğru olduğunu kontrol edin.


![CCQ](assets/fr/09.webp)


Görüntülenen parmak izinin Wallet'nızın parmak iziyle eşleştiğini onaylayın ve "*Geri Yükle*"ye tıklayın.


![CCQ](assets/fr/10.webp)


Bir passphrase kullanmanın, Mnemonic ifadeniz ve passphrase kombinasyonundan türetilen yeni bir anahtar setini Wallet yönetim yazılımınıza (Sparrow wallet gibi) aktarmanız gerektiği anlamına geldiğini unutmayın. Bunu yapmak için, bu diğer eğitimdeki "*Sparrow üzerinde yeni bir Wallet yapılandırın*" adımını izleyin:


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

## Kilit açma seçenekleri


COLDCARD'lar ayrıca cihaz kilidi açma işlemi için bir dizi seçenekten yararlanır. Bu gelişmiş seçenekler hakkında daha fazla bilgi edinelim.


### Hileli PIN'ler


Trick PIN, ilk cihaz yapılandırması sırasında tanımlanandan farklı ikincil bir PIN kodudur. Bu kod, COLDCARD açıldığında girilir girilmez önceden yapılandırılmış belirli eylemleri tetiklemek için kullanılır. Her biri farklı bir eylemle bağlantılı olan birkaç Trick PIN kodu yapılandırabilirsiniz. Bu özellikler COLDCARD'ınızı kişisel güvenlik stratejinize göre uyarlamanızı sağlar. Özellikle soygun (Bitcoin topluluğunda yaygın olarak "*$5 İngiliz anahtarı saldırısı*" olarak adlandırılır) gibi fiziksel baskı durumlarında kullanışlıdırlar.


Bir Hile PIN'ini etkinleştirmek ve bir eylemle ilişkilendirmek için `Ayarlar > Giriş Ayarları > Hile PIN'leri` menüsüne erişin.


![CCQ](assets/fr/11.webp)


"*Yeni Hile Ekle*" öğesini seçin.


![CCQ](assets/fr/12.webp)


Eylemle ilişkilendirilecek PIN kodunu ayarlayın ve kaydetmeyi unutmayın.


![CCQ](assets/fr/13.webp)


Ardından bu Trick PIN'i her girdiğinizde otomatik olarak gerçekleştirilecek eylemi seçin. İşte bir PIN için kullanılabilecek eylemlerin listesi:




- "*Brick Self*: Bu eylem, Hile PIN kodunun girilmesi halinde her iki COLDCARD Q çipini de yok ederek cihazı tamamen kullanılamaz hale getirir. Bu durumda cihazı yeniden satmak, yeniden kullanmak ve hatta Coinkite'a iade etmek mümkün olmayacaktır. Cihaz geri dönüşü olmayan bir şekilde kullanılmaz hale gelecektir. Bu özellik, bir soygun durumunda saldırganı bitcoinlerinize asla erişemeyeceğine ikna etmek için kullanılabilir. **Lütfen dikkat**: Mnemonic ifadenizin ve herhangi bir passphrase'ün fiziksel bir yedeği olmadan, bitcoinleriniz kalıcı olarak kaybolacaktır.


![CCQ](assets/fr/14.webp)




- "*Wipe seed*": Bu menü seed'yı silmek, yani COLDCARD'ı yok etmeden sıfırlamak için çeşitli eylemler sunar. "*Brick Self*" seçeneğinden farklı olarak, Mnemonic ifadenizin bir yedeğini kullanarak cihazı yeniden yapılandırmak mümkün olacaktır. Ancak, bu yedekleme olmadan bitcoinleriniz kaybolacaktır. İşte mevcut seçenekler:
 - "*Sil ve Yeniden Başlat* : seed'yi kaldırır ve ekranda herhangi bir bilgi görüntülemeden COLDCARD'ı yeniden başlatır.
 - "*Sessiz Silme*": seed'u sessizce siler ve hiçbir şey olmamış gibi rastgele sahte bir Wallet'deki COLDCARD'ın kilidini açar.
 - "*Sil -> Wallet*": seed'yi gizlice kaldırır ve yem olarak tasarlanmış önceden yapılandırılmış ikincil bir Wallet'deki COLDCARD'ın kilidini açar. Bu Wallet, bir saldırganı tatmin etmek için Bitcoin birikimlerinizin küçük bir kısmını içerebilir.
 - "*Silindi, Dur* Deyin": seed'ü siler ve ekranda `seed silindi, Durdur` mesajını görüntüler.


![CCQ](assets/fr/15.webp)




- "*Duress Wallet*": Bu eylemle, Hile PIN kodu BIP85 kullanarak seed'ten türetilen bir Wallet'ün kilidini açar. Bu ikincil Wallet bir saldırganı tatmin etmek için yem olarak kullanılabilir. COLDCARD gerçek Wallet'müş gibi davranır, ancak ana PIN kodu (Hile PIN kodundan farklı) olmadan saldırgan asla gerçek Wallet'e erişemez. Bu strateji, insanları Hile PIN'ine bağlı Wallet'ün var olan tek Wallet olduğuna inandırmak için tasarlanmıştır.


![CCQ](assets/fr/16.webp)




- "*Giriş Geri Sayımı*": Bu menü, gerçekleştirilmeden önce geri sayımı olan eylemleri gruplandırır. **Uyarı**, bunlardan bazıları cihazınızı yok edebilir veya bitcoinlerinizin kaybına neden olabilir. İşte mevcut alt eylemler:
 - "*Sil ve Geri Sayım* : seed'i COLDCARD'ın belleğinden siler, ardından bir saatlik geri sayım başlatır. Mnemonic veya passphrase'nızı kaydetmeden bitcoinleriniz kaybolacaktır. Bu seçenek, bir saldırganı geri sayımın sonunda cihazın kilidinin açılacağını düşünmesi için kandırmak üzere tasarlanmıştır, ancak aslında fabrika ayarlarına sıfırlanacaktır.
 - "*Geri Sayım ve Tuğla*": Bir saatlik bir geri sayım başlatır ve sonunda COLDCARD iki güvenli çipini yok ederek kalıcı olarak kullanılamaz hale getirir. Yedekleme olmadan bitcoinleriniz kaybolacaktır. Bu eylem, aslında cihaz kendini imha edecekken bir kilit açma beklediğini düşünen bir saldırganı kandırmak için tasarlanmıştır.
 - "*Sadece Geri Sayım* : Basit bir saatlik geri sayımı tetikler, ardından COLDCARD başka bir işlem yapmadan yeniden başlar. seed silinmez ve cihaz bozulmadan kalır. Bu eylemi, aşağıdaki bölümlerde tartışılan ve gerçek Wallet'a erişim sağlarken ana PIN'e bir geri sayım ekleyen "*Login Countdown*" seçeneği ile karıştırmamaya dikkat edin.


![CCQ](assets/fr/17.webp)




- "*Boş Görün*": Bu eylem COLDCARD'ın boş görünmesini sağlayarak seed'in silindiği izlenimini verir. Gerçekte hiçbir şey olmaz ve seed bozulmadan kalır. Bu, kullanılmayan veya sıfırlanmış bir COLDCARD'ı simüle eder.


![CCQ](assets/fr/18.webp)




- "*Sadece Yeniden Başlat* : Trick PIN kullanıldığında, COLDCARD basitçe yeniden başlatılır. Başka hiçbir işlem yapılmaz.


![CCQ](assets/fr/19.webp)




- "*Delta Modu*": Deneyimli kullanıcılar için ayrılmış olan bu karmaşık eylem, ister bir devletten ister ayrıcalıklı bilgilere sahip bir akrabadan gelsin, son derece karmaşık baskı saldırılarına karşı koymak için tasarlanmıştır. Delta Modu etkinleştirildiğinde, COLDCARD gerçek Wallet'e erişim sağlayarak bir saldırganın gezinmesine ve doğru Wallet olduğunu doğrulamasına olanak tanır. Ancak, işlem imzaları engellenir, böylece herhangi bir Bitcoin aktarımı önlenir. Buna ek olarak, Mnemonic ifadesine erişim devre dışı bırakılır ve herhangi bir geri alma girişimi silinmesine neden olur. Güvenilirliği artırmak için Delta Modu ile kullanılan Kandırmaca PIN'i gerçek PIN ile aynı ön eki paylaşmalıdır (aynı kimlik avı karşıtı kelimeleri görüntülemek için), ancak son ek farklı olmalıdır.


![CCQ](assets/fr/20.webp)


Bir eylem seçtikten sonra seçiminizi onaylayın.


![CCQ](assets/fr/21.webp)


Daha sonra yapılandırılmış tüm Trick PIN'lerini özel menüde görüntüleyebilirsiniz.


![CCQ](assets/fr/22.webp)


Mevcut bir Hile PIN'ini seçerek, ilişkili eylemi kontrol edebilirsiniz. Ayrıca "*Hile Gizle*" ile gizleyebilir ve Hile PIN'i menüsünde görünmez hale getirebilirsiniz. "*Hileyi Sil*" seçeneğine tıklayarak silebilir veya "*Hileyi Değiştir*" seçeneğiyle ilişkili eylemi koruyarak PIN kodunu değiştirebilirsiniz.


![CCQ](assets/fr/23.webp)


"*Trick PIN*" menüsünde bulunan "*Add If Wrong*" seçeneği, ana PIN kodunu girmek için belirli sayıda yanlış denemeden sonra otomatik olarak tetiklenen belirli bir eylemi yapılandırmanıza olanak tanır. İzin verilen deneme sayısı yapılandırma sırasında ayarlanabilir.


### Scramble Tuşları


Tuşları Karıştır seçeneği, PIN kodunuzu girerken tuş takımı düğmelerinizde görüntülenen rakamları karıştırmanıza olanak tanır. Bu özellik, insanlar veya kameralar tarafından izlenme durumunda bile PIN kodunuzun gizliliğini korur.


Bu seçeneği etkinleştirmek için `Ayarlar > Giriş Ayarları > Karıştırma Tuşları` menüsüne erişin.


![CCQ](assets/fr/24.webp)


"*Scramble Keys*" seçeneğini seçin.


![CCQ](assets/fr/25.webp)


Şu andan itibaren, COLDCARD Q'nuzun kilidini açtığınızda, tuş takımındaki tuşlara her kullandığınızda rastgele yeni numaralar atanacaktır.


![CCQ](assets/fr/26.webp)


### Giriş Geri Sayımı


Bu seçenek, COLDCARD'ınızın kilidini her açmaya çalıştığınızda sistematik bir geri sayım uygulamanızı sağlar. Hırsızlık durumunda cihaza erişimi geciktirerek veya örneğin bir soygun durumunda kendinizi korumak için bir işlemi imzalamadan önce bir gecikme uygulayarak güvenlik stratejinize entegre edilebilir. Ancak bu geri sayım, COLDCARD'ınızı yasal olarak kullandığınız zamanlar da dahil olmak üzere tüm kullanımlarınız için geçerlidir ve bu da sizi sabırlı olmaya zorlar. Bu seçeneği, yalnızca belirli bir Trick PIN kullanıldığında etkinleştirilen "*Sadece Geri Sayım*" eylemiyle karıştırmamaya dikkat edin.


Bu seçeneği yapılandırmak için `Ayarlar > Oturum Açma Ayarları > Oturum Açma Geri Sayımı` menüsüne erişin.


![CCQ](assets/fr/27.webp)


Geri sayım süresini seçin. Örneğin, 1 saat seçerseniz, COLDCARD Q'nun kilidini açmak için her denemede 1 saat beklemeniz gerekecektir.


![CCQ](assets/fr/28.webp)


Kilidi her açtığınızda PIN kodunuzu girmeniz istenecektir.


![CCQ](assets/fr/29.webp)


Ardından geri sayım tarafından belirlenen süreyi bekleyin.


![CCQ](assets/fr/30.webp)


Geri sayımın sonunda, cihaza erişmek için PIN kodunuzu tekrar girmeniz gerekecektir.


![CCQ](assets/fr/31.webp)


### Hesap Makinesi Girişi


Bu seçenek, kilidi açarken COLDCARD'ınızı bir hesap makinesi olarak gizlemenizi sağlar. Bu özelliği etkinleştirmek için `Ayarlar > Giriş Ayarları > Hesap Makinesi Girişi` menüsüne erişin.


![CCQ](assets/fr/32.webp)


Seçerek seçeneği etkinleştirin.


![CCQ](assets/fr/33.webp)


Şu andan itibaren, cihaz her açıldığında, temel komutları içeren çalışan bir hesap makinesi görüntülenecektir.


![CCQ](assets/fr/34.webp)


Örneğin, "*Plan B Network*" öğesinin SHA256 Hash değerini hesaplayabilirsiniz.


![CCQ](assets/fr/35.webp)


COLDCARD'ın kilidini hesap makinesi modundan açmak için, PIN kodu önekinizi ve ardından bir tire girerek başlayın. Örneğin, PIN kodunuz `00-00` ise (bu kod zayıftır ve yalnızca bir örnektir, bu nedenle güçlü bir PIN kodu seçin), `00-` yazın. COLDCARD daha sonra iki kimlik avı karşıtı kelimenizi görüntüleyecektir.


![CCQ](assets/fr/36.webp)


Ardından, bir boşluk veya tire ile ayırarak PIN kodunuzun tamamını girin, örneğin: `00 00`.


![CCQ](assets/fr/37.webp)


COLDCARD daha sonra hesap makinesi modundan çıkacak ve kilidi normal şekilde açacaktır.


## COLDCARD'ınızı temiz bir şekilde imha etme


COLDCARD Q cihazınızı, örneğin artık başka bir Hardware Wallet kullandığınız için elden çıkarmayı planlıyorsanız, cihazı doğru şekilde imha etmeniz önemlidir. Bu, Wallet'nizle ilgili hiçbir bilginin üçüncü bir tarafça kurtarılamamasını sağlar.


İhtiyaçlarınıza bağlı olarak üç bilgi imha seviyesi vardır. Başlamadan önce, Wallet'inizin başka bir Hardware Wallet'e aktarıldığından, tüm fonlarınıza erişiminiz olduğundan ve hepsinden önemlisi, her ikisi de işlevsel olan Mnemonic ifadenizin ve herhangi bir passphrase'unuzun olduğundan emin olun. Bir Wallet yedeği olmadan, COLDCARD'ınızın imhası bitcoinlerinizin kaybıyla sonuçlanacaktır.


İlk imha seviyesi sadece seed'ün silinmesinden oluşur. Bu seçenek, Mnemonic cümlenizi COLDCARD'ın belleğinden silerken cihazı çalışır durumda bırakır. COLDCARD Q'yu daha sonraki bir tarihte tekrar kullanmak istiyorsanız idealdir. seed'ü bellekten silmek için `Gelişmiş/Araçlar > Tehlike Bölgesi > seed İşlevleri > seed'ü Yok Et` menüsüne erişin.


![CCQ](assets/fr/38.webp)


İkinci imha seviyesi, COLDCARD'ın iki güvenli çipinin yazılım aracılığıyla kalıcı olarak devre dışı bırakılmasından oluşur. Bu işlem cihazı tamamen kullanılamaz hale getirir. Yeniden satamaz, yeniden kullanamaz veya Coinkite'a iade edemezsiniz: kalıcı olarak imha edilecektir. Devam etmek için, "*Brick Me*" ile ilgili önceki bölümde açıklanan adımları izleyin PIN kodunu girin, ardından COLDCARD'ın kilidini açarken bu PIN kodunu kasıtlı olarak girin.


Üçüncü seviye, COLDCARD Q'nuzun güvenli bileşenlerinin fiziksel olarak imha edilmesini içerir. Daha önce olduğu gibi, bu da cihazı geri dönülemez bir şekilde kullanılamaz hale getirecektir. Bunu yapmak için, bir matkap kullanarak cihazın sağ üst tarafındaki iki çipte (ters çevrildiğinde), "*SHOOT HERE*" yazısına yakın bir yerde bir delik açın.


**Önemli önlemler** :




- Elektrik çarpması riskini önlemek için, kullanmadan önce pilleri cihazdan çıkarın ve fişini prizden çekin.
- Delme işlemine başlamadan önce üniteyi kapattıktan sonra birkaç dakika bekleyin.
- Güvenliğinizi sağlamak için yalıtımlı eldiven ve koruyucu gözlük kullanın.


![CCQ](assets/fr/39.webp)


Çipler delindikten sonra, COLDCARD Q'yu yeniden bağlamaya çalışmayın.


Tebrikler, artık COLDCARD Q'nun gelişmiş seçenekleri hakkında bilgi sahibisiniz!


Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmak bırakırsanız çok minnettar olurum. Bu öğreticiyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


CCQ'nun doğrudan rakibi olan Ledger Flex'in kullanımını tartıştığımız bu diğer öğreticiyi de tavsiye ederim:


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a