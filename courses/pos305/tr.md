---
name: Bitcoin ve BTC Ödeme Sunucusu
goal: İşletmeniz için BTC Pay Sunucusu kurun
objectives: 

  - Btcpayserver'ın ne olduğunu anlayın.
  - BTC Pay Server'ı kendiniz barındırın ve yapılandırın.
  - Günlük işlerinizde btcpayserver kullanın.

---

# Bitcoin ve BTCPay Sunucusu


Bu, Alekos ve Bas tarafından yazılan ve melontwist ve asi0 tarafından Plan ₿ Kurs Formatı için uyarlanan BTCPay Sunucu Operatörü üzerine bir giriş kursudur.


BITMEMIŞ BIR HIKAYE


"Bu Yalan, Sana Olan Güvenim Kırıldı, Seni Modası Geçmiş Yapacağım".


BTCPay Server Foundation tarafından üretilmiştir


+++

# Giriş


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Kursa Genel Bakış


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


BTCPay Server'daki POS 305 kursuna hoş geldiniz!


Bu eğitimin amacı, BTCPay Server'ı işletmenizde veya kuruluşunuzda nasıl kuracağınızı, yapılandıracağınızı ve kullanacağınızı öğretmektir. BTCPay Server, Bitcoin ödemelerini otonom, güvenli ve uygun maliyetli bir şekilde işlemenizi sağlayan açık kaynaklı bir çözümdür. Bu eğitim öncelikle günlük operasyonlarına tam entegrasyon için BTCPay Server'ı kendi kendine barındırma konusunda uzmanlaşmak isteyen ileri düzey kullanıcılara yöneliktir.


**Bölüm 1: BTCPay Sunucusuna Giriş**

Giriş ekranı, kullanıcı hesabı yönetimi ve yeni bir mağaza oluşturma dahil olmak üzere BTCPay Server'ın genel bir sunumuyla başlayacağız. Bu giriş, BTCPay Server Interface'ü anlamanıza ve bu aracı kullanmaya başlamak için gereken temel özellikleri kavramanıza yardımcı olacaktır.


**Bölüm 2: Bitcoin Anahtarlarının Güvenliğini Sağlamaya Giriş**

Bitcoin fonlarınızın güvenliği çok önemlidir. Bu bölümde, kriptografik anahtarların oluşturulmasını, bu anahtarları güvence altına almak için donanım cüzdanlarının kullanımını ve BTCPay Server aracılığıyla anahtarlarınızla nasıl etkileşimde bulunacağınızı inceleyeceğiz. Ayrıca, işlemlerinizi optimize etmek için bir BTCPay Server Lightning Wallet'yı nasıl yapılandıracağınızı da öğreneceksiniz.


**Bölüm 3: BTCPay Sunucusu Interface**

Bu bölüm size BTCPay Server kullanıcı Interface'de rehberlik edecektir. Kontrol panelinde nasıl gezineceğinizi, mağaza ve sunucu ayarlarını nasıl yapılandıracağınızı, ödemeleri nasıl yöneteceğinizi ve entegre eklentilerden nasıl yararlanacağınızı öğreneceksiniz. Amaç, kurulumunuzu özel ihtiyaçlarınıza göre özelleştirmek için gerekli araçları size sağlamaktır.


**Bölüm 4: BTCPay Sunucusunun Yapılandırılması**

Son olarak, BTCPay Server'ın çeşitli ortamlarda pratik kurulumuna odaklanacağız. LunaNode, Voltage veya Umbrel node kullanıyor olsanız da, her ortamın özelliklerini dikkate alarak BTCPay Sunucunuzu dağıtmak ve yapılandırmak için gerekli adımları öğreneceksiniz.


BTCPay Server'da ustalaşmaya ve işinizi büyütmeye hazır mısınız? Hadi başlayalım!


## Yazarın Bitcoin ve BTCPay Sunucusu için eleştirel beğeni


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


BTCPay Server'ın ne olduğunu ve kökenlerini anlayarak başlayalım. Bitcoin alanında güven oluşturmak için şeffaflığa ve belirli standartlara değer veriyoruz.

Alandaki bir proje bu değerleri çiğnedi. BTCPay Server'ın baş geliştiricisi Nicolas Dorier bunu kişisel olarak ele aldı ve bu değerleri ortadan kaldırmaya söz verdi. İşte yıllar sonra buradayız ve her gün tamamen açık kaynaklı olarak bu geleceğe doğru çalışıyoruz.


> Bu yalan, sana olan güvenim kırıldı, seni kullanılmaz hale getireceğim.
> Nicolas Dorier

Nicolas tarafından söylenen sözlerden sonra, inşa etmeye başlama zamanı gelmişti. Şimdi BTCPay Sunucusu olarak adlandırdığımız şey için önemli miktarda çalışma yapıldı. Daha fazla insan bu çabaya katkıda bulunmak istedi. En tanınmışları r0ckstardev, MrKukks, Pavlenex ve yazılımı kullanan ilk tüccar astupidmoose'dur.


Açık kaynak ne anlama geliyor ve böyle bir projeye neler giriyor?


FOSS, Özgür ve Açık Kaynak Yazılım anlamına gelmektedir. İlki, herkesin yazılımın sürümlerini kopyalamasına, değiştirmesine ve hatta dağıtmasına (kar amaçlı bile olsa) izin veren terimleri ifade eder. İkincisi ise kaynak kodunun açıkça paylaşılması, halkın katkıda bulunmaya ve geliştirmeye teşvik edilmesi anlamına gelir.

Bu, halihazırda kullandıkları ve değer elde ettikleri yazılıma katkıda bulunma konusunda hevesli olan deneyimli kullanıcıları çeker ve sonuçta benimsemede tescilli yazılımdan daha başarılı olduğunu kanıtlar. "Bilgi özgür olmak ister" şeklindeki Bitcoin ethosuyla tutarlıdır Bir topluluk oluşturan tutkulu insanları bir araya getirir ve tek kelimeyle daha eğlencelidir. Bitcoin gibi, FOSS da kaçınılmazdır.


### Başlamadan önce


Bu kurs birden fazla bölümden oluşmaktadır. Birçoğu sınıf öğretmeniniz tarafından halledilecek, erişebileceğiniz Demo ortamları, kendiniz için barındırılan bir sunucu ve muhtemelen bir alan adı. Bu kursu bağımsız olarak tamamlarsanız, lütfen DEMO olarak etiketlenen ortamların sizin için mevcut olmayacağını unutmayın.

NB. Bu kursu bir sınıfta takip ediyorsanız, sunucu adları sınıf kurulumunuza bağlı olarak farklılık gösterebilir. Sunucu adlarındaki değişkenler bu nedenle farklı olabilir.


### Kurs Yapısı


Her bölümün hedefleri ve bilgi değerlendirmeleri vardır. Bu kursta, bunların her birini ele alacağız ve her ders bloğunun (yani bölümün) sonunda temel özelliklerin bir özetini sunacağız. Görsel geri bildirim sağlamak ve temel kavramları görsel açıdan pekiştirmek için resimlere yer verilmiştir. Her ders bloğunun başında hedefler belirlenmiştir. Bu hedefler bir kontrol listesinin ötesine geçmektedir. Bunlar size yeni bir beceri seti için bir rehber sağlar. BTCPay Sunucunuzun kurulumu tamamlandıkça, Bilgi Değerlendirmeleri giderek daha zorlu hale gelir.


### Öğrenciler kursla birlikte ne alıyor?


BTCPay Sunucu Kursu ile bir öğrenci Bitcoin'nin teknik ve teknik olmayan temel ilkelerini anlayabilir. BTCPay Server aracılığıyla Bitcoin kullanımına ilişkin kapsamlı eğitim, öğrencilerin kendi Bitcoin altyapılarını işletmelerine olanak sağlayacaktır.


### Önemli Web adresleri veya İletişim olanakları


Alekos ve Bas'ın bu dersi yazmasına olanak sağlayan BTCPay Sunucu Vakfı Tokyo, Japonya'da bulunmaktadır. BTCPay Sunucu vakfına listelenen web sitesi üzerinden ulaşılabilir.



- https://foundation.btcpayserver.org
- Resmi sohbet kanallarına katılın: https://chat.btcpayserver.org


## Bitcoin'e Giriş


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Bitcoin'ün sınıf alıştırması yoluyla anlaşılması


Bu bir sınıf alıştırmasıdır, bu nedenle bu dersi kendiniz alırsanız, bunu gerçekleştiremezsiniz, ancak yine de bu alıştırmadan geçebilirsiniz. Bu görevi tamamlamak için en az 9 ila 11 kişi gereklidir.


BBC'nin "Bitcoin ve Blockchain nasıl çalışır?" başlıklı giriş bölümünü izledikten sonra alıştırmaya başlayın.


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


Bu alıştırma en az dokuz katılımcı gerektirmektedir. Bu alıştırma, Bitcoin'in nasıl çalıştığına dair fiziksel bir anlayış sağlamayı amaçlamaktadır. Ağdaki her bir rolü oynayarak, interaktif ve eğlenceli bir öğrenme yöntemine sahip olacaksınız. Bu alıştırma Lightning Network'yi içermez.


### Örnek: 9 / 11 kişi gerektirir


Roller şunlar:



- 1 Müşteri
- 1 Tüccar
- 7 ila 9 Bitcoin düğümü


**Kurulum aşağıdaki gibidir:**


Müşteriler mağazadan Bitcoin ile bir ürün satın alır.


**Senaryo 1 - Geleneksel Bankacılık Sistemi**



- Hazırlan:
  - Ekteki Figjam - [Etkinlik Şeması] (https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0) içindeki diyagramlara/açıklayıcıya bakınız.
  - Müşteri (Alice), Tüccar (Bob) ve Banka rollerini oynayacak üç gönüllü öğrenci bulun.
- Olayların sırasını canlandırın:
  - Müşteri - mağazayı online olarak gezer ve istediği 25$'lık bir ürünü bulur ve satın almak istediğini satıcıya bildirir
  - Tüccar- ödeme ister.
  - Müşteri - kart bilgilerini Satıcıya gönderir
  - Satıcı - Bankaya bilgi iletir (hem kendi hem de kimliği/bilgileri tanımlayarak), aşağıdakilerin ödenmesini talep eder
  - Banka, Müşteri ve Üye İşyeri hakkında bilgi toplar (Alice ve Bob) ve müşterinin bakiyesinin yeterli olup olmadığını kontrol eder.
  - Alice'in hesabından \$25 keser, Bob'nın hesabına \$24 ekler, hizmet için \$1 alır
  - Satıcı, Banka'dan onay alır ve ürünü müşteriye gönderir.
- Yorumlar:
  - Bob ve Alice'nin bir banka ile ilişkisi olmalıdır.
  - Banka hem Bob hem de Alice hakkında tanımlayıcı bilgiler toplar.
  - Bank bir kesik aldı.
  - Bankanın her katılımcının parasını her zaman saklayacağına güvenilmelidir.


**Senaryo 2 - Bitcoin Sistemi**



- Hazırlan:
  - Ekteki Figjam - [Etkinlik Şeması] (https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0) içindeki diyagramlara/açıklayıcıya bakınız.
  - Bankanın yerine geçecek bir ağda Bilgisayar (Bitcoin Düğümler/Minerler) rolünü oynayacak dokuz öğrenci ile Bankayı değiştirin.
- 9 Bilgisayarın her biri, şimdiye kadar yapılmış tüm geçmiş işlemlerin eksiksiz bir tarihsel kaydına (böylece sahtecilik olmadan doğru bakiyeler) ve bir dizi kurala sahiptir:
  - İşlemin düzgün imzalandığını doğrulayın (thekeyfitsthelock)
  - Ağdaki eşlere geçerli işlemleri yayınlayın ve alın, geçersiz olanları atın (aynı fonları iki kez harcamaya çalışanlar dahil)
- Tüm içeriklerin geçerli olması koşuluyla "rastgele" bilgisayardan alınan yeni işlemlerle kayıtları periyodik olarak güncelleyin/ekleyin (not: basitlik açısından şimdilik Proof of Work bileşenini göz ardı ediyoruz), aksi takdirde bunları reddedin ve bir sonraki "rastgele" bilgisayar bir güncelleme gönderene kadar önceki gibi devam edin
  - İçeriğin geçerli olması halinde uygun miktar ödüllendirilmiştir.
- Olayların sırasını canlandırın:
  - Müşteri - mağazayı online olarak gezer ve istediği 25$'lık bir ürünü bulur ve satın almak istediğini satıcıya bildirir
  - Satıcı - müşteriye Wallet'larından bir Invoice/Address göndererek ödeme ister.
  - Müşteri- bir işlem oluşturur (Satıcı tarafından sağlanan bir Address'ye 25 $ değerinde BTC gönderir) ve bunu Bitcoin Ağına yayınlar.
- Bilgisayarlar- işlemi alır ve doğrular:
  - Address'dan gönderilen en az 25 dolarlık BTC var
  - İşlem düzgün bir şekilde imzalanmıştır (müşteri tarafından "kilidi açılmıştır")
  - Durum böyle değilse, işlem ağ üzerinden yayılmaz ve eğer öyleyse, yayılır ve bekletilir.
  - Satıcılar işlemin beklemede olduğunu ve beklediğini kontrol edebilir.
- Bir bilgisayar, önerilen işlemi içeren "bir blok" yayınlayarak sonuçlandırmayı önermek üzere "rastgele" seçilir; eğer işlem başarılı olursa, bir BTC ödülü alırlar.
  - OPSİYONEL/ GELİŞTİRİLMİŞ - rastgele bir Bilgisayar seçmek yerine, önceden belirlenmiş bir sonuç ortaya çıkana kadar Bilgisayarların zar atmasını sağlayarak Mining'ı simüle edin (örneğin, çift altılı atan ilk kişi seçilir)
  - Ayrıca, iki Bilgisayarın yaklaşık olarak aynı anda kazanması ve zincirleme bir bölünmeyle sonuçlanması durumunda ne olacağını da oynayabilir.
  - Bilgisayarlar geçerliliği kontrol eder, kurallar karşılanırsa kayıtları defterlerine günceller/ekler ve işlem bloğunu eşlere yayınlar.
  - Rastgele seçilen bilgisayar geçerli bir blok önerdiği için bir ödül alır.
  - Satıcı çekleri işlemi sonuçlandırıldı; böylece para alındı ve ürün müşteriye gönderildi.
- Yorumlar:
  - Önceden var olan bir bankacılık ilişkisine gerek olmadığına dikkat edin.
  - Kolaylaştırmak için üçüncü bir tarafa ihtiyaç yoktur; bunun yerini kodlar/teşvikler alır.
  - Doğrudan Exchange dışında hiç kimse tarafından veri toplanmamalı ve katılımcılar arasında sadece gerekli miktarda veri alışverişi yapılmalıdır (örn. nakliye Address).
  - İnsanlar arasında (ürünü gönderen Satıcı dışında) güvene gerek yoktur, birçok yönden nakit satın alma gibi.
  - Paranın sahibi doğrudan bireylerdir.
  - Bitcoin Ledger basitlik açısından dolar cinsinden gösterilmiştir, ancak gerçekte BTC'dir.
  - Tek bir işlemin yayınlandığını simüle ediyoruz, ancak gerçekte ağda birden fazla işlem beklemede ve bloklar aynı anda binlerce işlem içeriyor. Düğümler ayrıca çift harcama işlemlerinin beklemede olmadığını da doğrular (bu durumda biri hariç hepsini atardım).
- Hile senaryoları:
  - Ya müşterinin 25 BTC'si olmasaydı?
    - İşlemi oluşturamazlar çünkü "kilit açma" ve "Ownership" aynı şeydir ve bilgisayarlar işlemin uygun şekilde imzalanıp imzalanmadığını kontrol eder; aksi takdirde reddederler
  - Ya rastgele seçilen bilgisayar "Ledger'yı değiştirmeye" çalışırsa?
    - Diğer tüm bilgisayarlar eksiksiz bir geçmişe sahip olduğundan ve kurallarından birini ihlal eden değişikliği fark edeceğinden blok reddedilecektir.
    - Rastgele Bilgisayar bir ödül almayacak ve bloklarından hiçbir işlem sonuçlandırılmayacaktır.


## Bilgi değerlendirmesi


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### KA Sınıf tartışması


İkinci senaryo kapsamında sınıf alıştırmasında yapılan bazı aşırı basitleştirmeleri tartışın ve gerçek Bitcoin sisteminin ne yaptığını daha ayrıntılı olarak açıklayın.


### KA Kelime dağarcığı incelemesi


Önceki bölümde tanıtılan aşağıdaki anahtar terimleri tanımlayın:



- Düğüm
- Mempool
- Zorluk Hedefi
- Blok


**Grup olarak bazı ek terimlerin anlamlarını tartışınız:**


Blockchain, İşlem, Çift Harcama, Bizans Generalleri Problemi, Mining, Proof of Work (PoW), Hash Fonksiyon, Block reward, Blockchain, En Uzun Zincir, %51 Saldırı, Çıkış, Çıkış Kilidi, Değişim, Satoshis, Açık/Özel Anahtar, Address, Açık Anahtar Kriptografi, Dijital İmza, Wallet


# BTCPay Sunucusu ile tanışın


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## BTCPay Sunucu giriş ekranını anlama


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### BTCPay Sunucusu ile Çalışma


Bu kurs bloğunun amacı BTCPay Server yazılımı hakkında genel bir anlayış kazanmaktır. Paylaşılan bir ortamda, eğitmenin gösterimini takip etmeniz ve öğretmenle birlikte takip etmek için BTCPay Server Kurs Kitabına başvurmanız önerilir. Birden fazla yöntemle nasıl Wallet oluşturacağınızı öğreneceksiniz. Örnekler arasında Hot Wallet kurulumları ve BTCPay Server Vault aracılığıyla bağlanan donanım cüzdanları bulunmaktadır. Bu hedefler, kurs eğitmeniniz tarafından görüntülenen ve erişim izni verilen Demo ortamında gerçekleşir.


Bu kursu kendi başınıza takip ederseniz, https://directory.btcpayserver.org/filter/hosts adresinde Demo amaçlı üçüncü taraf ana bilgisayarların bir listesini bulabilirsiniz. Bu üçüncü taraf seçeneklerinin üretim ortamları olarak kullanılmamasını şiddetle tavsiye ediyoruz; ancak, Bitcoin ve BTCPay Server'ın kullanımını tanıtmak için doğru amaca hizmet ediyorlar.


Bir BTCPay Server rockstar stajyeri olarak, daha önce bir Bitcoin düğümü kurma deneyiminiz olabilir. Bu eğitim özellikle BTCPay Server Yazılım yığınına göre uyarlanmıştır.


BTCPay Server'daki seçeneklerin çoğu, Bitcoin Wallet ile ilgili diğer yazılımlarda bir şekilde veya başka bir şekilde mevcuttur.


### BTCPay Sunucu Giriş ekranı


Demo ortamına hoş geldiniz derken, sizden 'Oturum açmanız' veya 'Hesabınızı oluşturmanız' istenir Sunucu yöneticileri güvenlik nedeniyle yeni hesap oluşturma özelliğini devre dışı bırakabilir. BTCPay Server Açık Kaynak Yazılımı olduğu için BTCPay Server logoları ve düğme renkleri değiştirilebilir. Üçüncü taraf bir sunucu yazılımı beyaz etiketleyebilir ve tüm görünümü değiştirebilir.


![image](assets/en/001.webp)


### Hesap Oluştur penceresi


BTCPay Sunucusunda hesap oluşturmak için geçerli E-posta Address dizeleri gerekir; example@email.com E-posta için geçerli bir dize olacaktır.


Parolanın harfler, sayılar ve karakterler dahil olmak üzere en az 8 karakter uzunluğunda olması gerekir. Parolayı bir kez belirledikten sonra, parolanın ilk parola alanına yazılanla aynı olduğunu doğrulamanız gerekecektir.


E-posta ve Şifre alanlarının her ikisi de doğru şekilde doldurulduğunda, 'Hesap Oluştur' düğmesine tıklayın. Bu, E-posta ve şifreyi eğitmenin BTCPay Sunucu örneğine kaydedecektir.


![image](assets/en/002.webp)


**!Not!**


Bu kursu bağımsız olarak takip ederseniz, bu hesabı oluşturmak muhtemelen üçüncü taraf bir ana bilgisayarda yapılacaktır; bu nedenle, bunların üretim ortamları olarak değil, yalnızca eğitim amacıyla kullanılması gerektiğini tekrar vurguluyoruz.


### BTCPay Sunucu Yöneticisi Tarafından Hesap Oluşturma


BTCPay Sunucu Örneğinin Yöneticisi de BTCPay Sunucusu için hesaplar oluşturabilir. BTCPay Sunucu örneğinin Yöneticisi 'Sunucu Ayarları'na (1) tıklayabilir, 'Kullanıcılar' sekmesine (2) tıklayabilir ve Kullanıcılar sekmesinin sağ üst köşesindeki "+ Kullanıcı Ekle" düğmesine (3) tıklayabilir. Amaç (4.3) bölümünde, Hesapların yönetici kontrolü hakkında daha fazla bilgi edineceksiniz.


![image](assets/en/003.webp)


Yönetici olarak, kullanıcının Address e-posta adresine ihtiyacınız olacak ve standart bir parola belirleyeceksiniz. Yöneticinin güvenlik nedeniyle hesabı kullanmadan önce kullanıcıyı bu parolayı değiştirmesi konusunda bilgilendirmesi önerilir. Yönetici bir Parola belirlemezse ve sunucuda SMTP yapılandırılmışsa, kullanıcı kendi hesabını oluşturması ve bir parola belirlemesi için bir davet bağlantısı içeren bir e-posta alacaktır.


### Örnek


Kursu bir eğitmenle birlikte takip ederken, eğitmen tarafından sağlanan bağlantıyı takip edin ve Demo ortamında hesabınızı oluşturun. E-posta Address ve şifrenizin güvenli bir şekilde kaydedildiğinden emin olun; bu kurstaki demo hedeflerinin geri kalanı için bu oturum açma kimlik bilgilerine ihtiyacınız olacak.


Eğitmeniniz Address e-postasını önceden toplamış ve bu alıştırmadan önce bir davet bağlantısı göndermiş olabilir. Talimat verildiyse, E-postanızı kontrol edin.


Eğitmen olmadan kursa katılırken, BTCPay Server demo ortamını kullanarak hesabınızı oluşturun; şu adrese gidin


https://Mainnet.demo.btcpayserver.org/login.


Bu hesap yalnızca tanıtım/eğitim amacıyla kullanılmalı ve asla iş için kullanılmamalıdır.


### Beceri Özeti


Bu bölümde aşağıdakileri öğrendiniz:



- Interface aracılığıyla barındırılan bir sunucuda nasıl hesap oluşturulur.
- Bir sunucu yöneticisinin sunucu ayarlarına manuel olarak nasıl kullanıcı ekleyebileceği.


### Bilgi değerlendirmesi


#### KA Kavramsal İnceleme


Demo Sunucu kullanmanın üretim amaçları için neden kötü bir fikir olduğuna dair nedenler belirtin.


## Kullanıcı hesaplarını yönetme


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### BTCPay Sunucusunda Hesap Yönetimi


Bir mağaza sahibi hesabını oluşturduktan sonra, BTCPay Sunucu Kullanıcı Arayüzünün Sol Alt kısmından yönetebilir. Hesap düğmesinin altında, birden fazla üst düzey ayar vardır.



- Karanlık/Aydınlık modu.
- Hassas Bilgileri Gizle geçişi.
- Hesabı Yönet.


![image](assets/en/004.webp)


### Koyu ve Açık mod


BTCPay Server kullanıcıları, kullanıcı arayüzünün Açık veya Koyu mod versiyonu arasında seçim yapabilirler. Müşteriye yönelik sayfalar değişmeyecektir. Koyu veya açık modla ilgili müşterinin tercih ettiği ayarları kullanırlar.


### Hassas Bilgileri Gizle Değiştir


Hassas Bilgileri Gizle düğmesi hızlı ve basit bir Layer güvenliği sağlar. BTCPay Sunucunuzu çalıştırmanız gerektiğinde, ancak halka açık bir alanda omzunuzun üzerinden gizlenen insanlar olabileceğinde, Hassas Bilgileri Gizle'yi açın ve BTCPay Sunucusundaki tüm değerler gizlenecektir. Birisi omzunuzun üzerinden bakabilir, ancak artık uğraştığınız değerleri göremez.


### Hesabı Yönet


Kullanıcı hesabı oluşturulduktan sonra, parolaların, 2FA'nın veya API anahtarlarının yönetileceği yer burasıdır.


### Hesabı Yönet - Hesap


İsteğe bağlı olarak hesabınızı farklı bir E-posta Address ile güncelleyin. Address e-postanızın doğru olduğundan emin olmak için BTCPay Server bir doğrulama e-postası göndermenize izin verir. Kullanıcı yeni bir e-posta Address ayarlarsa ve doğrulamanın işe yaradığını onaylarsa kaydet'i tıklayın. Kullanıcı adı önceki E-posta ile aynı kalır.


Bir kullanıcı tüm hesabını silmeye karar verebilir. Bu, Hesap sekmesindeki sil düğmesine tıklanarak yapılabilir.


![image](assets/en/005.webp)


**!Not!**


E-posta değiştirildikten sonra, hesabın kullanıcı adı değişmeyecektir. Daha önce verilen E-posta Address Giriş adı olarak kalacaktır.


### Hesabı Yönet - Şifre


Bir öğrenci şifresini değiştirmek isteyebilir. Bunu Parola sekmesine giderek yapabilir. Burada, eski şifresini yazması gerekir ve bunu yeni bir şifreyle değiştirebilir.


![image](assets/en/006.webp)


### İki Faktörlü Kimlik Doğrulama (2fa)


Çalınan bir parolanın sonuçlarını sınırlamak için, nispeten yeni bir güvenlik yöntemi olan iki faktörlü kimlik doğrulamayı (2FA) kullanabilirsiniz. İki faktörlü kimlik doğrulamayı Hesabı yönet ve iki faktörlü kimlik doğrulama sekmesi aracılığıyla etkinleştirebilirsiniz. Kullanıcı adınız ve parolanızla oturum açtıktan sonra ikinci bir adımı tamamlamanız gerekir.


BTCPay Server, 2FA'yı etkinleştirmek için iki yöntemi destekler: uygulama tabanlı 2FA (Authy, Google, Microsoft Authenticators) veya Güvenlik cihazları (FIDO2 veya LNURL Auth) aracılığıyla.


### İki Faktörlü Kimlik Doğrulama - Uygulama tabanlı


Cep telefonunuzun İşletim Sistemine (Android veya iOS) bağlı olarak, kullanıcılar aşağıdaki uygulamalar arasından seçim yapabilirler;


1. İki faktörlü bir kimlik doğrulayıcı indirin.


   - Android](https://play.google.com/store/apps/details?id=com.authy.authy) veya [iOS](https://apps.apple.com/us/app/authy/id494168017) için Authy
   - Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) veya [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458) için Microsoft Authenticator
   - Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) veya [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605) için Google Authenticator

2. Authenticator Uygulamasını indirip yükledikten sonra.


   - BTCPay Sunucusu tarafından sağlanan QR Kodunu tarayın
   - Veya BTCPay Server tarafından oluşturulan anahtarı Authenticator uygulamanıza manuel olarak girin.

3. Authenticator uygulaması size benzersiz bir kod sağlayacaktır. Kurulumu doğrulamak için benzersiz kodu BTCPay Server'a girin ve işlemi tamamlamak için doğrula'ya tıklayın.


![image](assets/en/007.webp)


### Beceri Özeti


Bu bölümde aşağıdakileri öğrendiniz:



- Hesap yönetimi seçenekleri ve BTCPay Sunucu örneğindeki bir hesabı yönetmenin çeşitli yolları.
- Uygulama tabanlı 2FA nasıl kurulur?


### Bilgi değerlendirmesi


#### KA Kavramsal İnceleme


Uygulama tabanlı 2FA'nın hesabınızın güvenliğini sağlamaya nasıl yardımcı olduğunu açıklayın.


## Yeni bir mağaza oluşturma


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Mağaza sihirbazınızı oluşturun


Yeni bir kullanıcı BTCPay Server'a giriş yaptığında, ortam boştur ve ilk mağazaya ihtiyaç duyar. BTCPay Server'ın giriş sihirbazı kullanıcıya 'Mağazanızı oluşturun' seçeneğini sunacaktır (1). Bir Mağaza, Bitcoin ihtiyaçlarınız için bir Ev olarak görülebilir. Yeni bir BTCPay Sunucu Düğümü, Bitcoin Blockchain'i senkronize ederek başlayacaktır (2). BTCPay Server'ı hangi altyapıda çalıştırdığınıza bağlı olarak, bu birkaç saat ile birkaç gün arasında değişebilir. Örneğin geçerli sürümü BTCPay Server kullanıcı arayüzünüzün sağ alt köşesinde gösterilir. Bu, sorun giderme sırasında referans için kullanışlıdır.


![image](assets/en/008.webp)


### Mağaza sihirbazınızı oluşturun


Bu kursu takip etmeye bir önceki sayfadan biraz farklı bir ekranla başlayacaksınız. Eğitmeniniz Demo ortamını hazırladığı için Bitcoin Blockchain önceden senkronize edilmiştir ve bu nedenle düğümlerin senkronizasyon durumunu görmeyeceksiniz.


Bir kullanıcı tüm hesabını silmeye karar verebilir. Bu, Hesap sekmesindeki sil düğmesine tıklanarak yapılabilir.


![image](assets/en/009.webp)


**!Not!**


BTCPay Server hesapları sınırsız sayıda mağaza oluşturabilir. Her mağaza bir Wallet veya "ev" dir.


### Örnek


"Mağazanızı oluşturun" seçeneğine tıklayarak başlayın.


![image](assets/en/010.webp)


Bu, BTCPay Sunucusunu kullanmak için ilk Evinizi ve gösterge tablonuzu oluşturacaktır.


(1) "Mağazanızı oluşturun" seçeneğine tıkladıktan sonra, BTCPay Sunucusu mağazayı adlandırmanızı isteyecektir; bu sizin için yararlı herhangi bir şey olabilir.


![image](assets/en/011.webp)


(2) Daha sonra varsayılan bir mağaza para birimi ayarlanmalıdır, ya fiat para birimi ya da Bitcoin veya Sats cinsinden bir para birimi. Demo ortamı için bunu USD olarak ayarlayacağız.


![image](assets/en/012.webp)


(3) Mağaza kurulumunda son bir parametre olarak BTCPay Server, Bitcoin'un fiyatını mevcut fiat fiyatıyla karşılaştırmak için bir "Tercih edilen fiyat kaynağı" ayarlamanızı gerektirir, böylece mağazanız Bitcoin ile mağaza tarafından belirlenen fiat para birimi arasında doğru Exchange oranını görüntüler. Demo örneğinde varsayılana bağlı kalacağız ve bunu Kraken Exchange olarak ayarlayacağız. BTCPay Server, Exchange oranlarını kontrol etmek için Kraken API'sini kullanır.


![image](assets/en/013.webp)


(4) Artık bu mağaza parametreleri ayarlandığına göre, Oluştur düğmesine tıklayın ve BTCPay Server, sihirbazın devam edeceği ilk mağazanızın kontrol panelini oluşturacaktır.


![image](assets/en/014.webp)


Tebrikler, ilk mağazanızı oluşturdunuz ve bu alıştırmayı tamamladınız.


![image](assets/en/015.webp)


### Beceri Özeti


Bu bölümde şunları öğrendiniz:



- Mağaza oluşturma ve fiyat kaynağı tercihleriyle birlikte varsayılan para birimini yapılandırma.
- Her "Mağaza", BTCPay Server'ın bu kurulumunda diğer mağazalardan ayrılmış yeni bir evdir.


# Bitcoin Anahtarlarının Güvenliğini Sağlamaya Giriş


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Bitcoin Anahtar Üretimini Anlama


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### Bitcoin anahtarlarının oluşturulmasında neler yer alır?


Bitcoin cüzdanları oluşturulduklarında "seed" olarak adlandırılan bir cüzdan oluştururlar. Son hedefte, bir "seed" oluşturdunuz, Daha önce oluşturulan kelime dizileri Mnemonic cümleleri olarak da bilinir. seed, bireysel Bitcoin Anahtarlarını türetmek için kullanılır ve Bitcoin göndermek veya almak için kullanılır. seed cümleleri asla üçüncü taraflarla veya güvenilmeyen eşlerle paylaşılmamalıdır.


seed üretimi "Hiyerarşik Deterministik" (HD) çerçevesi olarak bilinen endüstri standardına göre gerçekleştirilir.


![image](assets/en/016.webp)


### Adresler


BTCPay Sunucusu generate yeni bir Address için oluşturulmuştur. Bu, ortak anahtar veya Address'in yeniden kullanılması sorununu hafifletir. Aynı Genel anahtarı kullanmak, tüm ödeme geçmişinizi izlemeyi çok kolaylaştırır. Anahtarları tek kullanımlık kuponlar olarak düşünmek gizliliğinizi önemli ölçüde artıracaktır. Ayrıca Bitcoin Adresleri de kullanıyoruz, bunları Açık anahtarlarla karıştırmayın.


Bir Address, bir "hashing algoritması" aracılığıyla Açık anahtardan türetilir Ancak çoğu cüzdan ve işlem, bu açık anahtarlar yerine Adresleri görüntüler. Adresler genel olarak açık anahtarlardan daha kısadır ve genellikle `1`, `3` veya `bc1` ile başlarken, açık anahtarlar `02`, `03` veya `04` ile başlar.



- 1.....` ile başlayan adresler hala çok yaygın adreslerdir. "Yeni bir mağaza oluşturma" bölümünde belirtildiği gibi, bunlar eski adreslerdir. Bu Address tipi P2PKH işlemleri içindir. P2Pkh Base58 kodlamasını kullanır, bu da Address'i büyük/küçük harfe duyarlı hale getirir. Yapısı, tanımlayıcı olarak ek bir rakam içeren açık anahtara dayanır.



- Bc1...` ile başlayan adresler yavaş yavaş çok yaygın adresler arasına girmektedir. Bunlar (doğal) SegWit Adresleri olarak bilinmektedir. Bunlar, bahsedilen diğer Adreslere göre daha iyi bir ücret yapısı sunar. Yerel SegWit Adresleri Bech32 kodlamasını kullanır ve yalnızca küçük harflere izin verir.



- 3...` ile başlayan adresler genellikle hala borsalar tarafından depozito adresleri için kullanılmaktadır. Bu adreslerden "Yeni bir mağaza oluşturma" bölümünde bahsedilmiştir, sarılmış veya iç içe geçmiş SegWit adresleri. Ancak, "Multisig Address" olarak da işlev görebilirler. SegWit Address olarak kullanıldığında, işlem ücretlerinde yine Yerel SegWit'e göre daha az olmak üzere bazı tasarruflar söz konusudur. P2SH Adresleri Base58 kodlamasını kullanır. Bu da onu eski Address gibi büyük/küçük harfe duyarlı hale getirir.



- 2...` ile başlayan adresler Testnet adresleridir. Bunlar Testnet Bitcoin (tBTC) almak içindir. Bunu asla karıştırmamalı ve bu adreslere Bitcoin göndermemelisiniz. Geliştirme amacıyla, bir generate Testnet Wallet gönderebilirsiniz. Testnet Bitcoin almak için çevrimiçi birden fazla musluk vardır. Asla Testnet Bitcoin satın almayın. Testnet Bitcoin mayınlıdır. Bu, bir geliştiricinin bunun yerine Regtest kullanması için bir neden olabilir. Bu, geliştiriciler için belirli ağ bileşenlerinin eksik olduğu bir oyun alanı ortamıdır. Bununla birlikte, Bitcoin geliştirme amaçları için çok kullanışlıdır.


### Genel Anahtarlar


Açık anahtarlar günümüzde pratikte daha az kullanılmaktadır. Zaman içinde Bitcoin kullanıcıları bunları Adresler ile değiştirmeye başladılar. Hala varlar ve hala ara sıra kullanılıyorlar. Açık anahtarlar, genel olarak, adreslerden çok daha uzun dizelerdir. Tıpkı adreslerde olduğu gibi, belirli bir tanımlayıcı ile başlarlar.



- İlk olarak, `02...` ve `03...` SEC formatında kodlanmış çok standart açık anahtar tanımlayıcılarıdır. Bunlar işlenebilir ve alım için adreslere dönüştürülebilir, multi-sig adresleri oluşturmak veya bir imzayı doğrulamak için kullanılabilir. İlk günlerin Bitcoin işlemleri, P2PK işlemlerinin bir parçası olarak açık anahtarları kullanmıştır.



- Ancak HD cüzdanlar farklı bir yapı kullanır. xpub...`, `ypub...` veya `zpub...` genişletilmiş genel anahtarlar veya xpubs olarak adlandırılır. Bu anahtarlar HD Wallet'ün bir parçası olarak birçok genel anahtarı türetmek için kullanılır. Xpub'ınız tüm geçmişinizin, yani geçmiş ve gelecekteki işlemlerin kayıtlarını tuttuğundan, bunları asla güvenilmeyen taraflarla paylaşmayın.


### Beceri Özeti


Bu bölümde aşağıdakileri öğrendiniz:



- Adresler ve açık anahtar veri türleri arasındaki farklar ve açık anahtarlar yerine adres kullanmanın faydaları.


### Bilgi değerlendirmesi


Address'in yeniden kullanımı veya açık anahtar yöntemlerine kıyasla her işlem için yeni adresler kullanmanın faydasını açıklayın.


## Hardware Wallet ile anahtarların güvenliğini sağlama


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Bitcoin Anahtarlarının Saklanması


Bir seed ifadesi oluşturduktan sonra, bu kitapta oluşturulan 12-24 kelimelik liste uygun yedekleme ve güvenlik gerektirir, çünkü bu kelimeler bir Wallet'a erişimi kurtarmanın tek yoludur. HD cüzdanlarının yapısı ve tek bir seed kullanarak adresleri deterministik olarak üretmesi, oluşturduğunuz tüm adreslerin Mnemonic veya kurtarma ifadenizi temsil eden bu tek seed kelime listesi kullanılarak yedekleneceği anlamına gelir.


Kurtarma cümlenizi güvende tutun. Özellikle kötü niyetli biri tarafından erişilirse, fonlarınızı taşıyabilirler. seed'ü güvenli ve emniyetli tutarken, aynı zamanda aralarında karşılıklı olduğunu da unutmayın. Bitcoin özel anahtarlarını saklamak için her biri güvenlik, gizlilik, kolaylık ve fiziksel depolama açısından kendi avantaj ve dezavantajlarına sahip çeşitli yöntemler vardır. Özel anahtarların önemi nedeniyle, Bitcoin kullanıcıları bu anahtarları bankalar gibi "saklama" hizmetlerini kullanmak yerine "kendi kendine saklama" yöntemiyle saklama ve güvenli bir şekilde saklama eğilimindedir. Kullanıcıya bağlı olarak ya bir Cold depolama çözümü ya da bir Hot Wallet kullanmalıdırlar.


### Hot ve Cold Bitcoin anahtarlarının depolanması


Genellikle, Bitcoin cüzdanları Hot Wallet veya Cold Wallet cinsindendir. Çoğu değiş tokuş, kolaylık, kullanım kolaylığı ve güvenlik risklerinde yatmaktadır. Bu yöntemlerin her biri bir saklama çözümünde de görülebilir. Ancak, buradaki ödünleşimler çoğunlukla güvenlik ve gizlilik tabanlıdır ve bu dersin kapsamı dışındadır.


### Hot Wallet


Hot cüzdanları, mobil, web veya masaüstü yazılımı aracılığıyla Bitcoin ile etkileşim kurmanın en uygun yoludur. Wallet her zaman internete bağlıdır ve kullanıcıların Bitcoin göndermesini veya almasını sağlar. Bununla birlikte, bu aynı zamanda zayıf yönüdür; Wallet, her zaman çevrimiçi olduğundan, artık bilgisayar korsanlarının veya cihazınızdaki kötü amaçlı yazılımların saldırılarına karşı daha savunmasızdır. BTCPay Server'da, Hot cüzdanları özel anahtarları örnek üzerinde saklar. BTCPay Server mağazanıza erişen herhangi biri, kötü niyetli olması durumunda bu Address'ten para çalabilir. BTCPay Server barındırılan bir ortamda çalıştığında, bunu güvenlik profilinizde her zaman göz önünde bulundurmalı ve böyle bir durumda tercihen bir Hot Wallet kullanmamalısınız. BTCPay Server sizin sahip olduğunuz ve güvenliğini sağladığınız donanım üzerine kurulduğunda, risk profili önemli ölçüde azalır, ancak asla tamamen ortadan kalkmaz.


### Cold Wallet


Bireyler Bitcoin'lerini bir Cold Wallet'ye taşırlar çünkü özel anahtarları internetten izole edebilir ve böylece onları potansiyel çevrimiçi tehditlerden koruyabilir. İnternet bağlantısının denklemden çıkarılması kötü amaçlı yazılım, casus yazılım ve SIM değiştirme riskini azaltır. Cold depolamanın, Bitcoin özel anahtarlarının kaybedilmesini önlemek için yeterli önlemlerin alınması koşuluyla, güvenlik ve özerklik açısından Hot depolamadan daha üstün olduğuna inanılmaktadır. Cold depolama, Wallet kurulumunun karmaşıklığı nedeniyle sık sık harcanması amaçlanmayan büyük miktarlardaki Bitcoin için en uygun olanıdır.


Bitcoin anahtarlarını Cold deposunda saklamak için kağıt cüzdanlardan beyin cüzdanlarına, donanım cüzdanlarına veya başlangıçtan itibaren bir Wallet dosyasına kadar çeşitli yöntemler vardır. Çoğu cüzdan generate ifadesini seed için BIP 39 kullanır. Bununla birlikte, Bitcoin core yazılımı içinde, kullanımı konusunda henüz bir fikir birliğine varılmamıştır. Bitcoin core yazılımı yine de güvenli bir çevrimdışı konumda saklamanız gereken bir Wallet.dat dosyasını generate yapacaktır.


### Beceri Özeti


Bu bölümde şunları öğrendiniz:



- İşlevsellik açısından Hot ve Cold cüzdanları arasındaki farklar ve bunların değiş tokuşları.


### Bilgi Değerlendirmesi Kavramsal İnceleme



- Wallet nedir?



- Hot ve Cold cüzdanları arasındaki fark nedir?



- "Bir Wallet oluşturmak" ile ne kastedildiğini açıklayınız?


## Bitcoin tuşlarınızı kullanma


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### BTCPay Sunucusu Wallet


BTCPay Sunucusu aşağıdaki standart Wallet özelliklerinden oluşur:



- İşlemler
- Gönder
- Almak
- Yeniden tara
- Çekme Ödemeleri
- Ödemeler
- PSBT
- Genel ayarlar


### İşlemler


Yöneticiler, işlemler görünümünde bu belirli mağazaya bağlı On-Chain Wallet için gelen ve giden işlemleri görebilir. Her işlemde alınan ve gönderilen tutarlar arasında bir ayrım vardır. Alınan Green ve giden işlemler kırmızı olacaktır. BTCPay Server işlem görünümünde, yöneticiler bir dizi standart etiket de göreceklerdir.


| Transaction Type | Description                                          |
| ---------------- | ---------------------------------------------------- |
| App              | Payment was received through an app-created invoice  |
| invoice          | Payment was received through an invoice              |
| payjoin          | Not paid, invoice timer still has not expired        |
| payjoin-exposed  | UTXO was exposed through an invoice payjoin proposal |
| payment-request  | Payment was received through a payment request       |
| payout           | Payment was sent through a payout or refund          |

### Nasıl Gönderilir


BTCPay sunucusunun gönderme işlevi, BTCPay Sunucunuzdan On-Chain Wallet işlemlerini gönderir. BTCPay Sunucusu, para harcamak için işlemlerinizi imzalamanın birden fazla yoluna izin verir. Bir işlem ile imzalanabilir;



- Hardware Wallet
- PSBT'yi destekleyen cüzdanlar
- HD özel anahtarı veya kurtarma tohumları.
- Hot Wallet


#### Hardware Wallet


BTCPay Server, Hardware Wallet'inizi BTCPay Vault ile üçüncü taraf uygulamalara veya sunuculara bilgi sızdırmadan kullanmanıza olanak tanıyan yerleşik Hardware Wallet desteğine sahiptir. BTCPay Server'daki Hardware Wallet entegrasyonu, Hardware Wallet'inizi içe aktarmanıza ve cihazınızda basit bir onay ile gelen fonları harcamanıza olanak tanır. Özel anahtarlarınız asla cihazdan çıkmaz ve tüm fonlar Full node'nize göre doğrulanır, böylece veri sızıntısı olmaz.


#### PSBT'ü destekleyen bir Wallet ile imzalama


PSBT (Kısmen İmzalanmış Bitcoin İşlemleri), hala tam olarak imzalanması gereken Bitcoin işlemleri için bir değişim formatıdır. PSBT BTCPay Server'da desteklenir ve uyumlu donanım ve yazılım cüzdanları ile imzalanabilir.


Tamamen imzalanmış bir Bitcoin işleminin oluşturulması aşağıdaki adımlardan geçer:



- Bir PSBT belirli giriş ve çıkışlarla inşa edilir, ancak imza yoktur
- Dışa aktarılan PSBT, bu formatı destekleyen bir Wallet tarafından içe aktarılabilir
- İşlem verileri Wallet kullanılarak incelenebilir ve imzalanabilir
- İmzalı PSBT dosyası Wallet'den dışa aktarılır ve BTCPay Sunucusu ile içe aktarılır
- BTCPay Sunucusu son Bitcoin işlemini üretir
- Sonucu doğrular ve ağa yayınlarsınız


#### HD Özel Anahtarı veya Mnemonic seed ile İmzalama


BTCPay Sunucusunu kullanmadan önce bir Wallet oluşturduysanız, özel anahtarınızı uygun bir alana girerek fonları harcayabilirsiniz. Wallet> Ayarlar'da uygun bir "AccountKeyPath" ayarlayın; aksi takdirde harcama yapamazsınız.


#### Bir Hot Wallet ile imzalama


Mağazanızı kurarken yeni bir Wallet oluşturduysanız ve bunu bir Hot Wallet olarak etkinleştirdiyseniz, imzalamak için otomatik olarak bir sunucuda depolanan seed'i kullanacaktır.


### RBF (Replace-by-fee)


Replace-by-fee (RBF), daha önce yayınlanmış bir işlemi (hala onaylanmamışken) değiştirmenize olanak tanıyan bir Bitcoin protokol özelliğidir. Bu, Wallet'inizin işlem parmak izini rastgele hale getirmenize veya işlemi onay (Mining) önceliği kuyruğunda daha yükseğe taşımak için daha yüksek bir ücret oranıyla değiştirmenize olanak tanır. Bu, daha yüksek ücret oranına öncelik verileceğinden orijinal işlemin yerini alacak ve onaylandıktan sonra orijinal işlemi geçersiz kılacaktır (çifte harcama yok).


RBF seçeneklerini görüntülemek için "Gelişmiş Ayarlar" düğmesine basın.


![image](assets/en/017.webp)



- Daha yüksek gizlilik için Randomize, işlem parmak izinin rastgele hale getirilmesi için işlemin otomatik olarak değiştirilmesini sağlar.
- Evet, RBF için işlemi işaretleyin ve açıkça değiştirin (Varsayılan olarak değiştirilmez, yalnızca girişle değiştirilir)
- Hayır, işlemin değiştirilmesine izin vermeyin.


### Coin Seçimi


Coin seçimi, bir işlem oluştururken harcamak istediğiniz madeni paraları seçmenize olanak tanıyan gelişmiş bir gizlilik artırıcı özelliktir. Örneğin, bir birleştirme karışımından yeni çıkan madeni paralarla ödeme yapmak.


Coin seçimi, Wallet etiketler özelliği ile yerel olarak çalışır. Bu, daha sorunsuz UTXO yönetimi ve harcaması için gelen fonları etiketlemenizi sağlar.


BTCPay Server etiket yönetimi için BIP-329'u destekler. BIP-329'u destekleyen bir Wallet'den aktarım yaparsanız ve etiketleri ayarladıysanız, BTCPay Server bunları otomatik olarak tanıyacak ve içe aktaracaktır. Sunucuları taşırken, bu bilgiler de dışa aktarılabilir ve yeni ortama aktarılabilir.


### Nasıl Teslim Alınır


BTCPay Server'da al düğmesine tıklandığında, ödemeleri almak için kullanılabilecek kullanılmayan bir Address oluşturur. Yöneticiler ayrıca yeni bir "Invoice" oluşturarak yeni bir Address generate oluşturabilirler


BTCPay Sunucusu, Address'nin yeniden kullanılmasını önlemek için her zaman sizden bir sonraki mevcut Address'yi generate yapmanızı isteyecektir. "generate sonraki mevcut BTC Address" seçeneğine tıkladıktan sonra BTCPay Server yeni bir Address ve QR oluşturur. Ayrıca, adreslerinizin daha iyi yönetimi için Address'ye doğrudan bir Etiket ayarlamanıza olanak tanır.


![image](assets/en/018.webp)


![image](assets/en/019.webp)


#### Yeniden tarama


Yeniden Tarama özelliği, yapılandırılmış türetme şemasına ait madeni paralar için Blockchain'ün (UTXO Seti olarak adlandırılır) mevcut durumunu taramak için Bitcoin core 0.17.0'ın "Scantxoutset" özelliğine dayanır. Wallet yeniden taraması, BTCPay Server kullanıcılarının sıklıkla karşılaştığı iki yaygın sorunu ele alır.


1. Boşluk sınırı sorunu - Üçüncü taraf cüzdanların çoğu, bir düğümü birçok kullanıcı arasında paylaşan hafif cüzdanlardır. Hafif ve Full node'e bağımlı cüzdanlar, performans sorunlarını önlemek için Blockchain'de izledikleri bakiyesi olmayan adres sayısını (genellikle 20) sınırlar. BTCPay Sunucusu her Invoice için yeni bir Address oluşturur. Yukarıdakileri göz önünde bulundurarak, BTCPay Sunucusu art arda 20 ödenmemiş fatura oluşturduktan sonra, harici Wallet yeni işlem gerçekleşmediğini varsayarak işlemleri almayı durdurur. Harici Wallet'iniz, faturalar 21'inde, 22'sinde vb. ödendiğinde bunları göstermeyecektir. Öte yandan, dahili olarak BTCPay Sunucusu Wallet, önemli ölçüde daha yüksek bir boşluk limiti ile birlikte ürettiği herhangi bir Address'u izler. Üçüncü bir tarafa güvenmez ve her zaman doğru bir bakiye gösterebilir.

2. Boşluk limiti çözümü - [Harici/mevcut Wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) boşluk limiti yapılandırmasına izin veriyorsa, kolay çözüm bunu artırmaktır. Ancak, cüzdanların çoğu buna izin vermez. Bildiğimiz kadarıyla şu anda boşluk sınırı yapılandırmasını destekleyen tek cüzdanlar Electrum, Wasabi ve Sparrow wallet'dir. Ne yazık ki, diğer birçok cüzdanla ilgili bir sorunla karşılaşmanız muhtemeldir. En iyi kullanıcı deneyimi ve gizlilik için, harici cüzdanlar yerine BTCPay Sunucusunun dahili Wallet'ünü kullanmayı düşünün.


#### BTCPay Sunucusu "mempoolfullrbf=1" kullanır


BTCPay Server "mempoolfullrbf=1" kullanır; bunu BTCPay Server kurulumunuza varsayılan olarak ekledik. Bununla birlikte, bunu kendiniz devre dışı bırakabileceğiniz bir özellik haline getirdik. "mempoolfullrbf=1" olmadan, bir müşteri RBF sinyali vermeyen bir işlemle bir ödemeyi iki kez harcarsa, Satıcı bunu ancak onaydan sonra öğrenebilir.


Bir yönetici bu ayarı devre dışı bırakmak isteyebilir. Aşağıdaki dize ile varsayılan ayarı değiştirebilirsiniz.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i
```


### BTCPay Sunucusu Wallet ayarları


BTCPay Server içindeki Wallet ayarları, Wallet'nızın genel ayarlarına açık ve özlü bir genel bakış sağlar. Wallet BTCPay Server ile oluşturulmuşsa, tüm bu ayarlar önceden doldurulmuştur.


![image](assets/en/020.webp)


BTCPay Server'daki Wallet ayarları, Wallet'inizin genel ayarlarına açık ve özlü bir genel bakış sağlar. Wallet BTCPay Server ile oluşturulmuşsa, tüm bu ayarlar önceden doldurulmuştur. BTCPay Server'ın Wallet ayarları Wallet durumu ile başlar. Yalnızca İzle mi yoksa Hot Wallet mi? Wallet türüne bağlı olarak, Wallet'in eksik işlemler için yeniden taranması, geçmişten eski işlemlerin budanması, ödeme bağlantıları için Wallet'in kaydedilmesi veya mağazaya bağlı mevcut Wallet'in değiştirilmesi ve silinmesi gibi eylemler değişebilir. BTCPay Server'ın Wallet ayarlarında, yöneticiler daha iyi Wallet yönetimi için Wallet için bir Etiket ayarlayabilirler. Burada, Yönetici ayrıca Türetme Şemasını, hesap anahtarını (xpub), Parmak İzini ve Anahtar Yolunu görebilecektir. Wallet ayarlarındaki ödemelerin yalnızca iki ana ayarı vardır. İşlem, Invoice'nin sona ermesinden sonra (ayarlanan dakika) içinde onaylanmazsa ödeme geçersizdir. Ödeme işlemi X miktarda onay aldığında Invoice'nin onaylandığını kabul edin. Yöneticiler ayrıca ödeme ekranında önerilen ücretleri görüntülemek için bir geçiş ayarlayabilir veya blok sayısında manuel bir onay hedefi belirleyebilir.


![image](assets/en/021.webp)


**!Not!**


Bu kursu bağımsız olarak takip ederseniz, bu hesabı oluşturmak muhtemelen üçüncü taraf bir ana bilgisayarda yapılacaktır. Bu nedenle, bunların üretim ortamı olarak değil, yalnızca eğitim amacıyla kullanılmasını öneriyoruz.


### Örnek


#### BTCPay Sunucusunda bir Bitcoin Wallet kurun


BTCPay Server, bir Wallet kurmak için iki yöntem sunar. Bir yol, mevcut bir Bitcoin Wallet'ü içe aktarmaktır. İçe aktarma, bir Hardware Wallet bağlayarak, bir Wallet dosyasını içe aktararak, Genişletilmiş bir genel anahtar girerek, bir Wallet'ün QR kodunu tarayarak veya en az tercih edilen şekilde, önceden oluşturulmuş bir Wallet kurtarma seed'i elle girerek yapılabilir. BTCPay Server'da yeni bir Wallet oluşturmak da mümkündür. Yeni bir Wallet oluştururken BTCPay Server'ı yapılandırmanın iki olası yolu vardır.


BTCPay Server'daki Hot Wallet seçeneği 'PayJoin' veya 'Liquid' gibi özellikleri etkinleştirir. Bununla birlikte, bir dezavantajı vardır: bu Wallet için oluşturulan kurtarma seed, yönetici kontrolüne sahip herhangi birinin onu alabileceği sunucuda saklanacaktır. Özel anahtarınız kurtarma seed'unuzdan türetildiğinden, kötü niyetli bir aktör mevcut ve gelecekteki fonlarınıza erişim sağlayabilir!


BTCPay Server'da bu riski azaltmak için, bir Yönetici Sunucu Ayarları > Politikalar > "Yönetici olmayanların mağazaları için Hot cüzdanları oluşturmasına izin ver" seçeneğindeki değeri varsayılan değer olduğu için "hayır" olarak ayarlayabilir. Bu Hot cüzdanlarının güvenliğini artırmak için sunucu yöneticisi, Hot cüzdanlarına sahip olmasına izin verilen hesaplarda 2FA kimlik doğrulamasını etkinleştirmelidir. Özel anahtarları genel bir sunucuda saklamak tehlikeli bir uygulamadır ve önemli riskler taşır. Bazıları Lightning Network risklerine benzerdir (Lightning Network riskleri için bir sonraki bölüme bakın).


BTCPay Server'ın yeni bir Wallet oluşturmada sunduğu ikinci seçenek bir Watch-only wallet oluşturmaktır. BTCPay Sunucusu özel anahtarlarınızı bir kez generate yapacaktır. Kullanıcı seed İfadesini yazdığını onayladıktan sonra, BTCPay Sunucusu özel anahtarları sunucudan silecektir. Sonuç olarak, mağazanızın artık kendisine bağlı bir Watch-only wallet'ü vardır. Watch-only wallet'ünüze gelen fonları harcamak için, BTCPay Server Vault, PSBT (Partially Signed Bitcoin Transaction) kullanarak veya en az önerilen şekilde seed cümlenizi manuel olarak sağlayarak Nasıl Gönderilir bölümüne bakın.


Son bölümde yeni bir 'Mağaza' oluşturdunuz. Kurulum sihirbazı "Bir Wallet kurun" veya "Bir Lightning düğümü kurun" diye sorarak devam edecektir. Bu örnekte, "Bir Wallet kur" sihirbaz sürecini takip edeceksiniz (1).


![image](assets/en/022.webp)


"Bir Wallet kur" seçeneğine tıkladıktan sonra, sihirbaz nasıl devam etmek istediğinizi sorarak devam edecektir; BTCPay Server şimdi mevcut bir Bitcoin Wallet'i yeni mağazanıza bağlama seçeneği sunuyor. Eğer bir Wallet'iniz yoksa, BTCPay Server yeni bir tane oluşturmanızı önerir. Bu örnekte "yeni bir Wallet oluşturma" (2) adımları izlenecektir. "Mevcut bir Wallet'i nasıl bağlayacağınızı öğrenmek için adımları izleyin (1).


![image](assets/en/023.webp)


**!Not!**


Bu kursu bir sınıfta alıyorsanız, oluşturduğumuz mevcut örneğin ve seed'nin yalnızca eğitim amaçlı olduğunu lütfen unutmayın. Bu adreslerdeki alıştırmalarda hiçbir zaman gerekenin dışında önemli bir miktar olmamalıdır.


(1) "Yeni bir Wallet oluştur" düğmesine tıklayarak "Yeni Wallet" sihirbazına devam edin.


![image](assets/en/024.webp)


(2) "Yeni bir Wallet oluştur" seçeneğine tıkladıktan sonra, sihirbazdaki bir sonraki pencerede "Hot Wallet" ve "Watch-only wallet" seçenekleri sunulacaktır Bir eğitmenle birlikte takip ediyorsanız, ortamınız paylaşılan bir Demo'dur ve yalnızca bir Watch-only wallet oluşturabilirsiniz. Aşağıdaki iki şekil arasındaki farka dikkat edin. Demo ortamındayken, eğitmenle birlikte takip ederken, bir "Watch-only wallet" oluşturun ve "Yeni Wallet" sihirbazıyla devam edin.


![image](assets/en/025.webp)


![image](assets/en/026.webp)


(3) Yeni Wallet sihirbazına devam ederken, şu anda BTC Watch-only wallet Oluşturma bölümündesiniz. Burada, Wallet'un "Address türünü" ayarlayacağız BTCPay Server tercih ettiğiniz Address türünü seçmenize olanak tanır; bu dersin yazıldığı tarih itibariyle, hala bech32 adreslerinin kullanılması önerilmektedir. Bu bölümün ilk kısmında adresler hakkında daha ayrıntılı bilgi edinebilirsiniz.



- SegWit (bech32)
  - Yerel SegWit adresleri `bc1q` ile başlar.
  - Örnek: `bc1qXXXXXXXXXXXXXXXXXXXXXXXX`
- Miras
  - Eski adresler `1` sayısı ile başlayan adreslerdir.
  - Örnek: `15e15hXXXXXXXXXXXXXXXXXXXXXX`
- Taproot (İleri düzey kullanıcılar için)
  - Taproot adresleri `bc1p` ile başlar.
  - Örnek: `bc1pXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- SegWit sarılmış
  - SegWit ile sarılmış adresler `3` ile başlar.
  - Örnek: `37BBXXXXXXXXXXXXXXX`


Tercih ettiğiniz Wallet Address tipi olarak SegWit'yi (önerilen) seçin.


![image](assets/en/027.webp)


(4) Wallet için parametre ayarlarken, BTCPay Sunucusu kullanıcıların BIP39 aracılığıyla isteğe bağlı bir passphrase ayarlamasına izin verir; şifrenizi onayladığınızdan emin olun.


![image](assets/en/028.webp)


(5) Wallet'ün Address türünü ve muhtemelen bazı gelişmiş seçenekleri ayarladıktan sonra Oluştur'a tıklayın ve BTCPay Sunucusu yeni Wallet'ünüzü generate yapacaktır. Bunun seed ifadenizi oluşturmadan önceki son adım olduğunu unutmayın. Bunu yalnızca birisinin ekranınıza bakarak seed ifadesini çalamayacağı bir ortamda yaptığınızdan emin olun.


![image](assets/en/029.webp)


(6) Sihirbazın aşağıdaki ekranında, BTCPay Server size yeni oluşturduğunuz Wallet için Kurtarma seed ifadesini gösterir; bunlar Wallet'nızı kurtarmanın ve işlemleri imzalamanın anahtarlarıdır. BTCPay Server 12 kelimeden oluşan bir seed cümlesi oluşturur. Bu kelimeler, bu kurulum ekranından sonra sunucudan silinecektir. Bu Wallet özellikle bir Watch-only wallet'tir. Bu seed ifadesinin dijital olarak veya fotoğrafik görüntü ile saklanmaması tavsiye edilir. Kullanıcılar ancak seed cümlesini yazdıklarını aktif olarak onayladıkları takdirde sihirbazda daha ileri gidebilirler.


![image](assets/en/030.webp)


(7) Bitti'ye tıkladıktan ve yeni oluşturulan Bitcoin seed ifadesini güvence altına aldıktan sonra, BTCPay Sunucusu mağazanızı ekli yeni Wallet ile güncelleyecek ve ödeme almaya hazır olacaktır. Kullanıcı Interface'de, sol gezinti menüsünde, Bitcoin'un artık Wallet altında nasıl vurgulandığına ve etkinleştirildiğine dikkat edin.


![image](assets/en/031.webp)


### Örnek: Bir seed cümlesinin yazılması


Bu, Bitcoin'ü kullanmak için özellikle güvenli bir andır. Daha önce de belirtildiği gibi, seed ifadenize yalnızca sizin erişiminiz veya bilginiz olmalıdır. Bir eğitmen ve sınıfla birlikte takip ederken, oluşturulan seed yalnızca bu kursta kullanılmalıdır. Sınıf arkadaşlarının meraklı bakışları, güvensiz sistemler ve diğerleri gibi çok sayıda faktör bu anahtarları yalnızca eğitim amaçlı ve güvenilmez kılmaktadır. Ancak, üretilen anahtarlar yine de kurs örnekleri için saklanmalıdır.


Bu durumda kullanacağımız ilk yöntem, ki bu aynı zamanda en az güvenli olanıdır, seed ifadesini doğru sırayla yazmaktır. Öğrenciye verilen kurs materyalinde bir seed cümle kartı yer almaktadır veya BTCPay Sunucusu GitHub'da bulunabilir. Bu kartı bir önceki adımda oluşturulan kelimeleri yazmak için kullanacağız. Bunları doğru sırada yazdığınızdan emin olun. Bunları yazdıktan sonra, doğru sırada yazdığınızdan emin olmak için yazılım tarafından verilenlerle karşılaştırın. Yazdıktan sonra, seed cümlenizi doğru yazdığınızı belirten onay kutusunu tıklayın.


### Örnek: Bir seed ifadesinin bir Hardware Wallet üzerinde saklanması


Bu kursta, bir seed ifadesinin bir Hardware Wallet üzerinde saklanmasına değiniyoruz. Bu kursu bir eğitmenle birlikte takip etmek bazen böyle bir cihazı da içerebilir. Kursta, rehber materyaller bu alıştırma için uygun olabilecek donanım cüzdanlarının bir listesini derlemiştir.


Bu örnekte BTCPay Server kasası ve bir Blockstream Jade Hardware Wallet kullanacağız.


Ayrıca Hardware Wallet'in bağlanmasıyla ilgili bir video kılavuzunu da takip edebilirsiniz.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


BTCPay Sunucu Kasasını İndirin: https://github.com/btcpayserver/BTCPayServer.Vault/releases


Sisteminiz için doğru dosyaları indirdiğinizden emin olun. Windows kullanıcıları [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe) paketini, Mac kullanıcıları [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg) paketini ve Linux kullanıcıları [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz) paketini indirmelidir


BTCPay Server Vault'u kurduktan sonra, Masaüstünüzdeki simgeye tıklayarak yazılımı başlatın. BTCPay Server Vault düzgün bir şekilde kurulduğunda ve ilk kez başlatıldığında, Web Uygulamaları ile kullanılmak üzere izin isteyecektir. Birlikte çalıştığınız belirli BTCPay Sunucusuna erişim izni vermenizi isteyecektir. Bu koşulları kabul edin. BTCPay Server Vault şimdi Donanım cihazını arayacaktır. Cihaz bulunduğunda, BTCPay Server Vault'un çalıştığını ve cihazınızı getirdiğini tanıyacaktır.


**!Not!**


Hot Wallet kullanırken SSH anahtarlarınızı veya sunucu yönetici hesabınızı yöneticiler dışında kimseye vermeyin. Bu hesaplara erişimi olan herkes Hot Wallet'deki fonlara erişebilir.


### Beceri Özeti


Bu bölümde aşağıdakileri öğrendiniz:



- Bitcoin Wallet'in işlem görünümü ve çeşitli kategorizasyonları.
- Bir Bitcoin Wallet'den gönderirken donanımdan Hot cüzdanlarına kadar çeşitli seçenekler mevcuttur.
- Çoğu cüzdanı kullanırken karşılaşılan boşluk sınırı sorunu ve bunun nasıl düzeltileceği.
- Anahtarların bir Hardware Wallet'da saklanması ve kurtarma ifadesinin yedeklenmesi dahil olmak üzere BTCPay Sunucusu içinde yeni bir generate Bitcoin Wallet nasıl yapılır.


Bu hedefte, BTCPay Sunucusu içinde yeni bir generate Bitcoin Wallet'in nasıl yapılacağını öğrendiniz. Henüz bu anahtarların nasıl güvence altına alınacağı veya kullanılacağı konusuna girmedik. Bu hedefe hızlı bir genel bakışta, ilk mağazanın nasıl kurulacağını öğrendiniz. generate bir Bitcoin Kurtarma seed ifadesinin nasıl oluşturulacağını öğrendiniz.


### Bilgi Değerlendirmesi Pratik İnceleme


Anahtar üretmek için bir yöntem ve bunları güvence altına almak için bir şemayı, güvenlik şemasının ödünleşimleri/riskleri ile birlikte tanımlayın.


## BTCPay Sunucu Yıldırım Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


Bir sunucu yöneticisi yeni bir BTCPay Server örneği hazırladığında, LND, Core Lightning veya Eclair gibi bir Lightning Network uygulaması kurabilir; daha ayrıntılı kurulum talimatları için BTCPay Server'ın Yapılandırılması bölümüne bakın.


Bir sınıf tarafından takip edilirse, bir Lightning düğümünü BTCPay Sunucunuza bağlamak bir Özel düğüm aracılığıyla çalışır. BTCPay Server'da sunucu yöneticisi olmayan bir kullanıcı varsayılan olarak dahili Lightning düğümünü kullanamaz. Bu, sunucu sahibini fonlarını kaybetmekten korumak içindir. Sunucu yöneticileri, Lightning düğümlerine LNBank aracılığıyla erişim izni vermek için bir eklenti yükleyebilir; bu, bu kitabın kapsamı dışındadır. LNBank hakkında daha fazla bilgi için resmi eklenti sayfasına bakın.


### Dahili düğümü bağlayın (sunucu yöneticisi)


Sunucu Yöneticisi BTCPay Sunucusunun dahili Lightning Düğümünü kullanabilir. Lightning uygulaması ne olursa olsun, dahili Lightning düğümüne bağlanmak aynıdır.


Önceki bir kurulum mağazasına gidin ve sol menüdeki "Lightning" Wallet'e tıklayın. BTCPay Server iki kurulum olanağı sunar: Dahili düğümü (varsayılan olarak yalnızca Sunucu yöneticisi) veya özel bir düğümü (harici bağlantı) kullanma. Sunucu yöneticileri "Dahili düğümü kullan" seçeneğine tıklayabilirler. Başka bir yapılandırmaya gerek yoktur. "Kaydet" düğmesine tıklayın ve "BTC Lightning düğümü güncellendi" bildirimine dikkat edin. Mağaza artık başarılı bir şekilde Lightning Network özelliklerine sahip olmuştur.


### Harici düğümü bağlayın (sunucu kullanıcısı/mağaza sahibi)


Varsayılan olarak, mağaza sahiplerinin sunucu yöneticisi Lightning Node'u kullanmasına izin verilmez. Bağlantının, BTCPay Sunucusu kurmadan önce mağaza sahibinin sahip olduğu bir düğüm, sunucu yöneticisi tarafından kullanılabiliyorsa bir LNBank eklentisi veya Alby gibi bir saklama çözümü gibi harici bir düğüme yapılması gerekir.


Önceden kurulmuş bir mağazaya gidin ve sol menüdeki cüzdanların altında yer alan "Lightning" seçeneğine tıklayın. Varsayılan olarak mağaza sahiplerinin dahili düğümü kullanmasına izin verilmediğinden bu seçenek gri renktedir. Özel bir düğüm kullanmak, mağaza sahipleri için varsayılan olarak kullanılabilen tek seçenektir.


BTCPay Sunucusu bağlantı bilgileri gerektirir; önceden hazırlanmış (veya saklama çözümü) bu bilgileri özellikle bir Lightning uygulamasına göre uyarlanmış olarak sunacaktır. BTCPay Sunucusu içinde, Mağaza sahipleri aşağıdaki bağlantıları kullanabilir;



- TCPveyaUnixdomainsocketconnection aracılığıyla C-lightning.
- HTTPS üzerinden Lightning Charge
- HTTPS üzerinden Eclair
- REST proxy aracılığıyla LND
- REST API aracılığıyla LNDhub


![image](assets/en/032.webp)


Bağlantı ayrıntılarını doğru girdiğinizden emin olmak için "bağlantıyı test et" seçeneğine tıklayın. Bağlantının iyi olduğu onaylandıktan sonra, 'Kaydet'e tıklayın ve BTCPay Server mağazanın bir Lightning Node ile güncellendiğini gösterir.


### Dahili Lightning düğümü LND'ü yönetme (Sunucu yöneticisi)


Dahili Lightning Node'u bağladıktan sonra, sunucu yöneticileri Dashboard'da özellikle Lightning bilgileri için yeni kutucuklar fark edeceklerdir.



- Yıldırım Dengesi
- Kanallardaki BTC
  - BTC açılış kanalları
  - BTC yerel Bakiyesi
  - BTC uzak bakiye
  - BTC kapanış kanalları
- BTC On-Chain
  - BTC onaylandı
  - BTC onaylanmadı
  - BTC ayrılmıştır
- Yıldırım Hizmetleri
  - Ride the Lightning (RTL).


Sunucu yöneticileri, "Lightning hizmetleri" kutucuğundaki Lightning Logosuna veya sol menüdeki cüzdanların altındaki "Lightning" seçeneğine tıklayarak Lightning düğümü yönetimi için RTL'ye ulaşabilirler.


**Not!**


Dahili Lightning Node bağlantısı başarısız - Dahili bağlantı başarısız olursa, onaylayın:


1. Bitcoin On-Chain düğümü tamamen senkronize edilmiştir

2. Dahili yıldırım düğümü "Lightning" > "Ayarlar" > "BTC Lightning Ayarları" altında "Etkin "dir


Lightning düğümünüze bağlanamıyorsanız, sunucunuzu yeniden başlatmayı deneyebilir veya BTCPay Server resmi belgelerinde daha fazla ayrıntı okuyabilirsiniz; https://docs.btcpayserver.org/Troubleshooting/. Lightning düğümünüz "Çevrimiçi" görünene kadar mağazanızda lightning ödemelerini kabul edemezsiniz. "Public Node Info" bağlantısına tıklayarak Lightning bağlantınızı test etmeyi deneyin.


### Yıldırım Wallet


Sol menü çubuğundaki Lightning Wallet seçeneğinde, sunucu yöneticileri RTL'ye, Genel düğüm Bilgilerine ve BTCPay Sunucu mağazalarına özgü Lightning ayarlarına kolay erişim bulacaklar.


#### Dahili düğüm bilgisi


Sunucu yöneticileri, sunucu durumlarını (Çevrimiçi/Çevrimdışı) ve Clearnet veya Tor için bağlantı dizesini görüntülemek için dahili düğüm bilgilerine tıklayabilirler.


![image](assets/en/033.webp)


#### Bağlantıyı değiştir


Harici Lightning düğümünü değiştirmek için "Lightning Ayarları "na gidin ve "Bağlantıyı değiştir "e ("Genel Düğüm bilgisi "nin yanında) tıklayın. Bu, mevcut kurulumu sıfırlar. Yeni düğüm ayrıntılarını girin, Kaydet'e tıklayın ve mağaza buna göre güncellenecektir.


![image](assets/en/034.webp)


#### Hizmetler


Sunucu yöneticisi Lightning uygulaması için birden fazla hizmet kurmaya karar verirse, bunlar burada listelenecektir. Standart bir LND uygulamasıyla, yöneticiler düğüm yönetimi için standart bir araç olarak Ride The Lightning'e (RTL) sahip olacaklardır.


#### BTC Lightning Wallet ayarları


Önceki adımda Lightning düğümünü mağazaya ekledikten sonra mağaza sahipleri, Lightning ayarlarının üst kısmındaki Geçiş özelliğini kullanarak mağazaları için bu düğümü devre dışı bırakmayı seçebilirler.


![image](assets/en/035.webp)


#### Lightning Ödeme seçenekleri


Mağaza sahipleri, müşterilerinin Lightning deneyimini geliştirmek için aşağıdaki parametreleri ayarlayabilir.



- Yıldırım ödeme tutarlarını Satoshis cinsinden görüntüleyin.
- Lightning Invoice'e özel kanallar için atlama ipuçları ekleyin.
- Ödeme sırasında On-Chain ve Lightning ödeme URL/QR kodlarını birleştirin.
- Yıldırım faturaları için bir açıklama şablonu ayarlayın.


#### LNURL


Mağaza sahipleri LNURL kullanmayı ya da kullanmamayı seçebilir. Lightning Network URL veya LNURL, Lightning Payer ve alacaklı arasındaki etkileşimler için önerilen bir standarttır. Kısacası, LNURL, LNURL ile ön eklenmiş bech32 kodlu bir URL'dir. Lightning Wallet'ün URL'nin kodunu çözmesi, URL ile iletişime geçmesi ve daha fazla talimat içeren bir JSON nesnesi, özellikle de LNURL'ün davranışını tanımlayan bir etiket beklemesi beklenir.



- LNURL'ü Etkinleştir
- LNURL Klasik Mod
  - Wallet uyumluluğu için, Bech32 kodlu (klasik) ve açık metin URL (gelecek)
- Alacaklının bir yorum iletmesine izin verin.


### Örnek 1


#### Dahili düğüm ile Lightning'e bağlanın (Yönetici)


Bu seçenek yalnızca bu örneğin Yöneticisi iseniz veya Yönetici, kullanıcıların dahili yıldırım düğümünü kullanabilmesi için varsayılan ayarları değiştirmişse kullanılabilir.


Yönetici olarak, sol menü çubuğundaki Lightning Wallet'ya tıklayın. BTCPay Server sizden bir Lightning Node bağlamak için iki seçenekten birini seçmenizi isteyecektir: Dahili bir düğüm veya özel bir harici düğüm. "Dahili düğüm kullan" seçeneğine tıklayın ve ardından "Kaydet" seçeneğine tıklayın


#### Lightning düğümünüzü yönetme (RTL)


Dahili Lightning düğümüne bağlandıktan sonra, BTCPay Server güncellenecek ve Lightning'i mağazanıza bağladığınızı onaylayan "BTC Lightning düğümü güncellendi" bildirimini gösterecektir.


Yıldırım düğümünü yönetmek sunucu yöneticisinin görevidir. Bu, aşağıdakileri içerir:


- İşlem yönetme
- Likiditenin yönetilmesi
  - Gelen likidite
  - Giden likidite
- Akranları ve kanalları yönetme
  - Bağlı eşler
  - Kanal ücretleri
  - Kanal durumu
- Kanal durumlarının sık sık yedeklenmesi.
- Yönlendirme raporlarını kontrol etme
- Alternatif olarak, Loop gibi hizmetleri kullanın.


Tüm lightning düğüm yönetimi RTL ile standart olarak yapılır (bir LND uygulaması üzerinde çalıştığınızı varsayarsak). Yöneticiler BTCPay Server'da Lightning Wallet'lerine tıklayabilir ve RTL'yi açmak için bir düğme bulabilirler. BTCPay Server'ın ana Gösterge Tablosu artık RTL'ye hızlı erişim de dahil olmak üzere Lightning Network Kutucukları ile güncellenmiştir.


### Örnek 2


#### Alby ile Yıldırım'a bağlanın


Alby gibi bir emanetçiyle bağlantı kurarken, mağaza sahipleri önce bir hesap oluşturmalı ve https://getalby.com/ adresini ziyaret etmelidir


![image](assets/en/036.webp)


Alby hesabını oluşturduktan sonra BTCPay Sunucu mağazanıza gidin.


Adım 1: Gösterge Panosunda 'Lightning düğümü kur' veya cüzdanların altındaki 'Lightning' seçeneğine tıklayın.


![image](assets/en/037.webp)


Adım 2: Alby tarafından sağlanan Wallet bağlantı kimlik bilgilerinizi girin. Alby'nin Kontrol Panelinde, Wallet'ye tıklayın. Burada "Wallet Bağlantı Kimlik Bilgileri "ni bulacaksınız. Bu kimlik bilgilerini kopyalayın. Alby'den gelen kimlik bilgilerini BTCPay Server'daki Bağlantı yapılandırma alanına yapıştırın.


![image](assets/en/038.webp)


Adım 3: BTCPay Sunucusuna Bağlantı ayrıntılarını verdikten sonra, bağlantının düzgün çalıştığından emin olmak için "Bağlantıyı Test Et" düğmesine tıklayın. Ekranınızın üst kısmındaki "Yıldırım düğümüne bağlantı başarılı" mesajına dikkat edin. Bu, her şeyin beklendiği gibi çalıştığını onaylar.


![image](assets/en/039.webp)


4. Adım: "Kaydet "e tıkladığınızda mağazanız artık Alby tarafından bir Lightning düğümüne bağlanır.


![image](assets/en/040.webp)


**!Not!**


Bir saklama kuruluşu Lightning çözümüne asla kaybetmek isteyeceğinizden daha fazla değerle güvenmeyin.


### Beceri Özeti


Bu bölümde şunları öğrendiniz:



- Dahili veya harici bir Lightning düğümü nasıl bağlanır
- Gösterge Tablosundaki Lightning ile ilgili çeşitli kutucukların içeriği ve işlevi
- Gerilim Dalgalanması veya Alby kullanarak Lightning Wallet nasıl yapılandırılır


### Bilgi değerlendirmesi Pratik İnceleme


Lightning Wallet'yi mağazanıza bağlamak için çeşitli seçeneklerden bazılarını açıklayın.


# BTCPay Sunucusu Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Gösterge tablosuna genel bakış


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay Server modüler bir yazılım paketidir. Bununla birlikte, her BTCPay Sunucusunun uyması gereken standartlar vardır ve bu standartlar Yönetici ile kullanıcılar arasındaki etkileşimi yönetecektir. Gösterge Tablosu ile başlamak. Giriş yaptıktan sonra her BTCPay Sunucusunun ana giriş noktası. Gösterge Tablosu, mağazanızın performansına, Wallet'ün mevcut bakiyesine ve son 7 gündeki işlemlere genel bir bakış sağlar. Modüler bir görünüm olduğundan, Eklentiler bu görünümü kendi yararları için kullanabilir ve Gösterge Tablosunda kendi kutucuklarını oluşturabilir. Bu kursta, BTCPay Server'da yalnızca standart eklentileri ve uygulamaları, ilgili görünümleriyle birlikte ele alacağız.


### Gösterge Paneli Döşemeleri


BTCPay Sunucu panosunun ana görünümünde birkaç standart kutucuk mevcuttur. Bu kutucuklar, Mağaza sahibinin veya Yöneticinin mağazasını tek bir genel bakışta hızlı bir şekilde yönetmesi için tasarlanmıştır.



- Wallet denge
- İşlem faaliyeti
- Lightning Balance (mağazada Lightning etkinleştirilmişse)
- Lightning Hizmetleri (Lightning mağazada etkinleştirilmişse)
- Son işlemler.
- Son Faturalar
- Mevcut aktif Kitle Fonları
- Mağaza performansı / en çok satan ürünler.


### Wallet denge


Wallet Bakiye kutucuğu, Wallet'nizin fonlarına ve performansına hızlı bir genel bakış sağlar. Haftalık, aylık veya yıllık bir grafikte BTC veya Fiat para birimi cinsinden görüntülenebilir.


![image](assets/en/041.webp)


### İşlem faaliyeti


BTCPay Server, Wallet Bakiye kutucuğunun yanında bekleyen Ödemeler, son 7 gündeki İşlemlerin sayısı ve mağazanızın herhangi bir geri ödeme yapıp yapmadığına dair hızlı bir genel bakış gösterir. Yönet düğmesine tıklamak sizi bekleyen ödemelerin yönetimine götürür (BTCPay Server - Ödemeler bölümünde ödemeler hakkında daha fazla bilgi edinin).


![image](assets/en/042.webp)


### Yıldırım Dengesi


Bu yalnızca Lightning etkinleştirildiğinde görünür.


Yönetici Lightning Network erişimine izin verdiğinde, BTCPay Sunucu panosunda artık Lightning düğümü bilgilerinizi içeren yeni bir kutucuk vardır. Kanallarda ne kadar BTC olduğu, bunun yerel veya uzaktan nasıl dengelendiği (gelen veya giden likidite), kanalların kapanıp kapanmadığı ve yıldırım düğümünde ne kadar Bitcoin On-Chain tutulduğu.


![image](assets/en/043.webp)


### Yıldırım Hizmetleri


Bu yalnızca yıldırım aktif olduğunda görünür.


BTCPay Server panosunda Lightning bakiyenizi görmenin yanı sıra, yöneticiler Lightning Hizmetleri kutucuğunu da göreceklerdir. Burada, yöneticiler Lightning düğümlerini yönetmek için kullandıkları araçlar için hızlı düğmeler bulabilirler; örneğin, Ride the Lightning, Lightning düğümü yönetimi için BTCPay Server ile standart araçlardan biridir.


![image](assets/en/044.webp)


### Son İşlemler


Son İşlemler kutucuğu mağazanızın en son işlemlerini görüntüler. BTCPay Sunucu örneğinin Yöneticisi artık tek bir tıklamayla en son işlemi görebilir ve buna dikkat edilmesi gerekip gerekmediğini görebilir.


![image](assets/en/045.webp)


### Son faturalar


Son Faturalar kutucuğu, Durum ve Invoice tutarı dahil olmak üzere BTCPay Sunucunuz tarafından oluşturulan en son 6 faturayı görüntüler. Kutucukta ayrıca Invoice genel görünümünün tamamına kolayca erişmek için bir "Tümünü görüntüle" düğmesi bulunur.


![image](assets/en/046.webp)


### Satış Noktası ve Kitle Fonları


BTCPay Server bir dizi standart eklenti veya uygulama sunduğundan, Satış Noktası ve Kitle Fonlaması BTCPay Server'ın iki ana eklentisidir. Her mağaza ve Wallet ile, bir BTCPay Server kullanıcısı uygun gördüğü sayıda Satış Noktası veya Kitle Fonlaması generate yapabilir. Her biri, eklentilerin performansını gösteren yeni bir gösterge tablosu kutucuğu oluşturacaktır.


![image](assets/en/047.webp)


Satış Noktası ve Kitle Fonlaması kutucukları arasındaki küçük farka dikkat edin. Yönetici, Satış Noktası kutucuğunda en çok satılan öğeleri görür. Kitle Fonlaması kutucuğunda bu, En İyi Avantajlar olur. Her iki kutucukta da ilgili uygulamayı yönetmek ve en iyi ürünler veya en iyi avantajlar tarafından oluşturulan son faturaları görüntülemek için hızlı düğmeler bulunur.


![image](assets/en/048.webp)


**!Not!**


Bakiye grafikleri ve son işlemler yalnızca On-Chain ödeme yöntemleri için mevcuttur. Lightning Network bakiyeleri ve işlemleri hakkında bilgi yapılacaklar listesindedir. BTCPay Server Sürüm 1.6.0 itibariyle, temel Lightning Network bakiyeleri mevcuttur.


### Beceri Özeti


Bu bölümde aşağıdakileri öğrendiniz:



- Ana açılış sayfasındaki kutucukların temel düzeni Gösterge Tablosu olarak bilinir.
- Her bir karonun içeriği hakkında temel bir anlayış.


### Bilgi Değerlendirme İncelemesi


Gösterge Tablosundan hafızanızdan listeleyebildiğiniz kadar çok kutucuğu listeleyin.


## BTCPay Sunucusu - Mağaza ayarları


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


BTCPay Server yazılımı içinde iki tür ayar olduğunu biliyoruz. BTCPay Server Mağazasına özel ayarlar, Gösterge Tablosunun altındaki sol menü çubuğunda bulunan ayarlar düğmesi ve menü çubuğunun altında, Hesabın hemen üstünde bulunan BTCPay Server ayarları. BTCPay Server Sunucusuna özel ayarlar yalnızca Sunucu yöneticileri tarafından görüntülenebilir.


Mağaza ayarları, her bir ayar setini kategorize etmek için birçok sekmeden oluşur.



- Genel
- Oranlar
- Ödeme Görünümü
- Erişim Belirteçleri
- Kullanıcılar
- Roller
- Webhooks
- Ödeme İşlemcileri
- E-postalar
- Formlar


### Genel


Genel Ayarlar sekmesinde, mağaza sahipleri markalarını ve ödeme varsayılanlarını ayarlar. Mağazanın ilk kurulumunda bir mağaza adı verilmiştir; bu, Mağaza Adı altındaki Genel ayarlara yansıtılacaktır. Mağaza sahibi burada ayrıca web sitesini markayla eşleşecek şekilde ayarlayabilir ve Yöneticinin veritabanında tanıması için bir Mağaza Kimliği belirleyebilir.


#### Markalaşma


BTCPay Sunucusu FOSS olduğundan, bir mağaza sahibi mağazasına uyacak şekilde özel markalama yapabilir. Marka rengini ayarlayın, markanızın logolarını saklayın ve genel/müşteriye dönük sayfalar (Faturalar, Ödeme Talepleri, Çekme ödemeleri) için özel CSS ekleyin


#### Ödeme


Ödemeler ayarlarında, mağaza sahipleri mağazalarının varsayılan para birimini (Bitcoin veya herhangi bir fiat para birimi) ayarlayabilirler.


#### Herkesin fatura oluşturmasına izin verin


Bu ayar, BTCPay Server üzerindeki geliştiriciler veya kurucular içindir. Mağazanız için bu ayar etkinleştirildiğinde, dış dünyanın BTCPay Sunucu örneğinizde fatura oluşturmasına izin verir.


#### Faturalara ek Ücret (ağ ücreti) ekleyin


BTCPay'de, tüccarları Dust saldırılarından veya müşterileri, tüccarın bir kerede büyük miktarda Bitcoin taşıması gerektiğinde daha sonra ücretlerde yüksek bir maliyete maruz kalmaktan korumak için bir özellik. Örneğin, müşteri 20$ karşılığında bir Invoice oluşturdu ve bunu kısmen ödedi, Invoice tamamen ödenene kadar 20 kez 1$ ödedi. Satıcı artık daha büyük bir işleme sahiptir ve bu da satıcı bu fonları daha sonra taşımaya karar verirse Mining maliyetini artırır. Varsayılan olarak BTCPay, Invoice birden fazla işlemde ödendiğinde tüccar için bu masrafı karşılamak üzere toplam Invoice tutarına ek bir ağ maliyeti uygular. BTCPay, bu koruma özelliğini özelleştirmek için çeşitli seçenekler sunar. Bir ağ ücreti uygulayabilirsiniz:



- Yalnızca müşteri Invoice için birden fazla ödeme yaparsa (Yukarıdaki örnekte, müşteri 20\$ için bir Invoice oluşturduysa ve 1\$ ödediyse, ödenmesi gereken toplam Invoice artık 19\$ + ağ ücreti olur. Şebeke ücreti ilk ödemeden sonra uygulanır)
- Her ödemede (ilk ödeme dahil, örneğimizde, ilk ödemede bile toplam hemen 20\$ + ağ ücreti olacaktır)
- Asla ağ ücreti eklemeyin (ağ ücretini tamamen devre dışı bırakır)


Dust işlemlerinden korurken, doğru şekilde iletilmediği takdirde işletmelere de olumsuz yansıyabilir. Müşterilerin ek soruları olabilir ve onlardan fazla ücret aldığınızı düşünebilirler.


#### Invoice, tutarın tamamı ödenmediği takdirde sona erer mi?


Invoice zamanlayıcısı varsayılan olarak 15 dakikaya ayarlanmıştır. Zamanlayıcı, Bitcoin tutarını Bitcoin-to-fiat Exchange oranlarına göre kilitlediği için dalgalanmaya karşı bir koruma mekanizması görevi görür. Müşteri tanımlanan süre içinde Invoice'i ödemezse, Invoice'in süresinin dolduğu kabul edilir. Invoice, işlem Blockchain üzerinde görünür olduğu anda (sıfır onay ile) "ödenmiş" olarak kabul edilir ve satıcının tanımladığı onay sayısına (genellikle 1-6) ulaştığında "tamamlanmış" olur. Zamanlayıcı dakikalara göre özelleştirilebilir.


#### Ödenen tutar beklenenden %X daha az olsa bile Invoice ödenmiş sayılır mı?


Bir müşteri Exchange Wallet'yi doğrudan bir Invoice için ödeme yapmak için kullandığında, Exchange küçük bir ücret alır. Bu, böyle bir Invoice'in tamamen tamamlanmış olarak kabul edilmediği anlamına gelir. Invoice "kısmen ödendi" olarak işaretlenir. Bir satıcı eksik ödenmiş faturaları kabul etmek istiyorsa, yüzde oranını burada ayarlayabilirsiniz.


### Oranlar


BTCPay Server'da, bir Invoice oluşturulduğunda, her zaman en güncel ve doğru Bitcoin-to-fiat fiyatına ihtiyaç duyar. BTCPay Server'da yeni bir mağaza oluştururken, yöneticilerden tercih ettikleri fiyat kaynağını belirlemeleri istenir. Mağaza kurulduktan sonra, mağaza sahipleri fiyat kaynaklarını istedikleri zaman bu sekmeden değiştirebilirler.


#### Gelişmiş oran kuralı komut dosyası oluşturma


Genelde uzman kullanıcılar tarafından kullanılır. Açılırsa, mağaza sahipleri fiyat davranışı ve müşterilerini nasıl ücretlendirecekleri konusunda komut dosyaları oluşturabilir.


#### Test


Tercih ettiğiniz döviz çiftleri için hızlı bir test yeri. Bu özellik ayrıca bir REST sorgusu aracılığıyla varsayılan döviz çiftlerini kontrol etme özelliğini de içerir.


### Ödeme Görünümü


Ödeme Görünümü sekmesi Invoice'e özgü ayarlar ve varsayılan bir ödeme yöntemiyle başlar ve belirlenen gereksinimler karşılandığında belirli ödeme yöntemlerini etkinleştirir.


#### Invoice ayarları


Varsayılan ödeme yöntemleri. BTCPay Sunucusu, standart yapılandırmasında üç seçenek sunar.



- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain & Lightning)


Mağazamız için, bir müşterinin yalnızca fiyat X tutarından az olduğunda Lightning ile etkileşime gireceği parametreleri ayarlayabiliriz ve On-Chain işlemleri için tam tersi, X Y'den büyük olduğunda her zaman On-Chain ödeme seçeneğini sunabiliriz.


![image](assets/en/049.webp)


#### Ödeme


BTCPay Server 1.7 sürümünden itibaren, yeni bir Checkout Interface, Checkout V2 tanıtıldı. Sürüm 1.9 standartlaştırıldığından, yöneticiler ve mağaza sahipleri kasayı hala önceki sürüme ayarlayabilirler. Bir mağaza sahibi, "Klasik kasayı kullan" geçişini kullanarak mağazayı önceki ödeme deneyimine geri döndürebilir. BTCPay Server ayrıca Çevrimiçi ticaret veya mağaza içi deneyim için belirli bir dizi ön ayara sahiptir.


![image](assets/en/050.webp)


Bir müşteri mağaza ile etkileşime girdiğinde ve bir Invoice oluşturduğunda, Invoice için bir sona erme süresi vardır. Varsayılan olarak, BTCPay Server bunu 5 dakikaya ayarlar ve yöneticiler bunu tercihlerine göre ayarlayabilir. Ödeme sayfası, aşağıdaki parametreler kontrol edilerek daha da özelleştirilebilir:



- Konfeti göstererek ödemeyi kutlayın
- Mağaza üstbilgisini göster (İsim ve logo)
- "Wallet ile Öde" düğmesini gösterin
- On-Chain ve off-chain ödemeleri URL/QR'lerini birleştirin
- Yıldırım ödeme tutarlarını Satoshis cinsinden görüntüleme
- Ödeme sırasında dili otomatik algılama


![image](assets/en/051.webp)


Otomatik algılama dili ayarlanmadığında, BTCPay Sunucusu varsayılan olarak İngilizce görüntüleyecektir. Bir mağaza sahibi bu varsayılanı tercih ettiği dile değiştirebilir.


![image](assets/en/052.webp)


Açılır menüye tıkladığınızda Mağaza sahipleri, ödeme sayfasında görüntülenecek bir Özel HTML başlığı ayarlayabilir.


![image](assets/en/053.webp)


Müşterilerin ödeme yöntemlerini bilmelerini sağlamak için, bir mağaza sahibi ödeme işlemlerini her zaman kullanıcıların tercih ettikleri ödeme yöntemini seçmelerini gerektirecek şekilde açıkça ayarlayabilir. Invoice ödendikten sonra, BTCPay Server müşterinin web mağazasına geri dönmesine izin verir. Mağaza sahipleri bu yönlendirmeyi müşteri ödeme yaptıktan sonra otomatik olarak uygulanacak şekilde ayarlayabilir.


![image](assets/en/054.webp)


#### Kamu makbuzu


Genel makbuz ayarlarında, bir mağaza sahibi makbuz sayfalarını herkese açık olacak şekilde ayarlayabilir, makbuz sayfasında ödeme listesini ve müşterinin kolayca erişebilmesi için QR kodunu görüntüleyebilir.


![image](assets/en/055.webp)


### Erişim Belirteçleri


Erişim belirteçleri, belirli e-ticaret entegrasyonları veya özel olarak oluşturulmuş entegrasyonlarla eşleştirmek için kullanılır.


![image](assets/en/056.webp)


### Kullanıcılar


Mağaza kullanıcıları, mağaza sahibinin personel üyelerini, hesaplarını ve mağazaya erişimlerini yönetebildiği yerdir. Personel üyeleri hesaplarını oluşturduktan sonra, mağaza sahibi belirli kullanıcıları Misafir kullanıcılar veya sahipler olarak mağazaya ekleyebilir. Personelin rolünü daha fazla tanımlamak için "BTCPay Server Mağaza ayarları - Roller" başlıklı bir sonraki bölüme bakın


![image](assets/en/057.webp)


### Roller


Bir mağaza sahibi, kullanıcının standart rollerini yeterince önemli bulmayabilir. Özel roller ayarlarında, bir mağaza sahibi işletmesindeki her rol için tam ihtiyaçları tanımlayabilir.


(1) Yeni bir rol oluşturmak için "+ Rol ekle" düğmesine tıklayın.


![image](assets/en/058.webp)


(2) Bir Rol adı girin, örneğin "Kasiyer".


![image](assets/en/059.webp)


(3) Rol için bireysel izinleri yapılandırın.



- Mağazalarınızı değiştirin.
- Mağazalarınıza bağlı Exchange hesaplarını yönetin.
  - Mağazalarınıza bağlı Exchange hesaplarını görüntüleyin.
- Çekme ödemelerinizi yönetin.
- Çekme ödemeleri oluşturun.
  - Onaylanmamış çekme ödemeleri oluşturun.
- Faturaları değiştirin.
  - Faturaları görüntüleyin.
  - Bir Invoice oluşturun.
  - Mağazalarınızla ilişkili yıldırım düğümlerinden faturalar oluşturun.
- Mağazalarınızı görüntüleyin.
  - Faturaları görüntüleyin.
  - Ödeme taleplerinizi görüntüleyin.
  - Mağazaların web kancalarını değiştirin.
- Ödeme taleplerinizi değiştirin.
  - Ödeme taleplerinizi görüntüleyin.
- Mağazalarınızla ilişkili yıldırım düğümlerini kullanın.
  - Mağazalarınızla ilişkili yıldırım faturalarını görüntüleyin.
  - Mağazalarınızla ilişkili yıldırım düğümlerinden faturalar oluşturun.
- Mağazalarınıza bağlı Exchange hesaplarına para yatırın.
- Exchange hesaplarından mağazanıza para çekin.
- Mağazanızın Exchange hesaplarında fon ticareti yapın.


Rol oluşturulduğunda adı sabitlenir ve düzenleme moduna geçtikten sonra değiştirilemez.


![image](assets/en/060.webp)


### Webhooks


BTCPay Server'da yeni bir "Webhook" oluşturmak oldukça kolaydır. BTCPay Server Mağaza ayarları - Webhooks sekmesinde, bir mağaza sahibi "+ Webhook Oluştur" seçeneğine tıklayarak kolayca yeni bir webhook oluşturabilir. Webhooks, BTCPay Server'ın mağazanızla ilgili HTTP olaylarını diğer sunuculara veya e-ticaret entegrasyonlarına göndermesini sağlar.


![image](assets/en/061.webp)


Şimdi bir Webhook oluşturma görünümündesiniz. Yük URL'nizi bildiğinizden emin olun ve bunu BTCPay Sunucunuza yapıştırın. Yük URL'sini yapıştırdığınızda, altında web kancası sırrı gösterilir. Webhook sırrını kopyalayın ve uç noktada sağlayın. Her şey ayarlandığında, BTCPay Server'da "Otomatik yeniden teslimat" seçeneğine geçebilirsiniz BTCPay Server, başarısız olan herhangi bir teslimatı 10 saniye, 1 dakika ve 10 dakika sonra en fazla 6 kez yeniden teslim etmeye çalışacaktır. Her olay arasında geçiş yapabilir veya ihtiyaçlarınıza göre olayları belirleyebilirsiniz. Web kancasını etkinleştirdiğinizden emin olun ve kaydetmek için "Web kancası ekle" düğmesine basın.


![image](assets/en/062.webp)


Web kancalarının Bitpay API ile uyumlu olması amaçlanmamıştır. BTCPay Server'da iki ayrı IPN (BitPay terimleriyle: "Anında Ödeme Bildirimleri") vardır.



- Webhookp
- Bildirimler


Bildirim URL'sini yalnızca Bitpay API aracılığıyla fatura oluşturduğunuzda kullanın.


### Ödeme İşlemcileri


Ödeme işlemcileri BTCPay Server'daki Payouts konsepti ile birlikte çalışır. Birden fazla işlemi toplu hale getirmek ve bir kerede göndermek için bir ödeme toplayıcı. Ödeme işlemcileri ile bir mağaza sahibi toplu ödemeleri otomatikleştirebilir. BTCPay Server iki otomatik ödeme yöntemi sunar: On-Chain ve off-chain (LN).


Mağaza sahibi her iki ödeme işlemcisini ayrı ayrı tıklayıp yapılandırabilir. Bir mağaza sahibi On-Chain işlemcisini yalnızca her X saatte bir çalıştırmak isteyebilirken off-chain işlemcisi birkaç dakikada bir çalışabilir. On-Chain için hangi bloğun dahil edilmesi gerektiğine dair bir hedef de belirleyebilirsiniz. Varsayılan olarak, bu 1 (veya mevcut bir sonraki blok) olarak ayarlanmıştır. off-chain ödeme işlemcisinin ayarlanmasında yalnızca aralık zamanlayıcısının bulunduğuna ve blok hedefinin bulunmadığına dikkat edin. Lightning Network ödemeleri anlıktır.


![image](assets/en/063.webp)

![image](assets/en/064.webp)


Mağaza sahipleri On-Chain işlemcisini yalnızca mağazalarına bağlı bir Hot Wallet varsa yapılandırabilir.


![image](assets/en/065.webp)


Bir Ödeme işlemcisi kurduktan sonra, BTCPay Sunucu Mağazası ayarlarındaki Ödeme işlemcisi sekmesine geri dönerek bunu hızlı bir şekilde kaldırabilir veya değiştirebilirsiniz.


**Not**


Ödeme işlemcisi On-Chain - On-Chain ödeme işlemcisi yalnızca Hot Wallet bağlı olarak yapılandırılmış bir mağazada çalışabilir. Hot Wallet bağlı değilse, BTCPay Sunucusu Wallet anahtarlarını tutmaz ve ödemeleri otomatik olarak işleyemez.


### E-postalar


BTCPay Server, Bildirimler için veya doğru ayarlandığında, örnekte oluşturulan hesapları kurtarmak için E-postaları kullanabilir. Standart olarak, BTCPay Server, örneğin şifre kaybolduğunda bir e-posta göndermez.


![image](assets/en/066.webp)


Bir mağaza sahibi, mağazasındaki belirli olayları tetiklemek için E-posta kuralları belirlemeden önce, bazı temel e-posta ayarlarını yapmalıdır. BTCPay Server, mağazanızla ilgili olaylar veya şifre sıfırlamaları için e-posta göndermek üzere bu ayarlara ihtiyaç duyar.


BTCPay Sunucusu, "Hızlı Doldurma" Seçeneğini kullanarak bu bilgileri doldurmayı kolaylaştırdı:



- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid


BTCPay Server, hızlı doldurma seçeneğini kullanarak SMTP sunucusu ve bağlantı noktası için alanları önceden dolduracaktır. Şimdi, mağaza sahibinin yalnızca E-posta Address, Oturum Açma (genellikle e-posta Address'ünüze eşittir) ve şifresi dahil olmak üzere kimlik bilgilerini doldurması gerekir. BTCPay Sunucusu e-posta ayarlarındaki gelişmiş seçenek, TLS Sertifikası güvenlik kontrollerini Devre Dışı Bırakmaktır; varsayılan olarak bu etkindir.


![image](assets/en/067.webp)


E-posta kuralları ile bir mağaza sahibi, belirli e-posta adreslerine e-postaları tetiklemek için belirli olayları ayarlayabilir.



- Invoice Oluşturuldu
- Invoice Ödeme Alındı
- Invoice İşleme
- Invoice Süresi doldu
- Invoice Anlaşıldı
- Invoice Geçersiz
- Invoice Ödeme Gerçekleştirildi


Müşteri bir E-posta Address sağlamışsa, bu tetikleyiciler bilgileri müşteriye de gönderebilir. Mağaza sahipleri, bu E-postanın neden oluştuğunu ve neyin tetiklediğini netleştirmek için Konu satırını önceden doldurabilir.


![image](assets/en/068.webp)


### Formlar


BTCPay Server herhangi bir veri toplamadığından, bir mağaza sahibi ödeme deneyimine özel bir form eklemek isteyebilir; bu şekilde mağaza sahibi müşterilerinden ek bilgi toplayabilir. BTCPay Server Form oluşturucu iki bölümden oluşur: formların görsel ve daha gelişmiş kod görünümü.


Yeni bir form oluştururken, BTCPay Server yeni formunuzun ne sormasını istediğinize ilişkin temel bilgileri talep eden yeni bir pencere açar. İlk olarak, mağaza sahibinin yeni formu için net bir isim vermesi gerekir; bu isim belirlendikten sonra değiştirilemez.


![image](assets/en/069.webp)


Mağaza sahibi forma bir ad verdikten sonra, "Formun genel kullanımına izin ver" anahtarını AÇIK konuma getirebilirsiniz; böylece form Green'e dönüşecektir. Bu, formun müşteriye dönük her konumda kullanılmasını sağlar. Örneğin, bir mağaza sahibi Satış Noktası üzerinden değil de ayrı bir Invoice oluşturursa, yine de müşteriden bilgi toplamak isteyebilir. Bu geçiş, bu bilgilerin toplanmasını sağlar.


![image](assets/en/070.webp)


Her form en az 1 Yeni form alanı ile başlar. Bir mağaza sahibi bunun ne tür bir alan olması gerektiğini seçebilir.



- Metin
- Sayı
- Şifre
- E-posta
- URL
- Telefon numaraları
- Tarih
- Gizli alanlar
- Fieldset
- Açık yorumlar için bir metin alanı.
- Seçenek seçici


Her tür, doldurulması gereken parametreleriyle birlikte gelir. Mağaza sahibi bunu kendi isteğine göre ayarlayabilir. İlk oluşturulan alanın altında, mağaza sahipleri bu forma yeni alanlar ekleyebilir.


![image](assets/en/071.webp)


#### Gelişmiş özel formlar


BTCPay Server ayrıca kod içinde Formlar oluşturmanıza da olanak tanır. Özellikle JSON. Mağaza sahipleri editöre bakmak yerine, editörün hemen yanındaki KOD düğmesine tıklayabilir ve Formlarının koduna girebilirler. Bir alan tanımında yalnızca aşağıdaki alanlar ayarlanabilir; alanların değerleri Invoice'in meta verilerinde saklanır:


| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | If true, the .value must be set in the form definition, and the user will not be able to change the field's value. ( example: the form definition's version)                                                                                                                                                                                                                                                                                                       |
| .fields.type          | The HTML input type text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                |
| .fields.options       | If .fields.type is select, the list of selectable values                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.options.text  | The text displayed for this option                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.value | The value of the field if this option is selected                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.type=fieldset | Create a HTML fieldset around the children .fields.fields (see below)                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.name          | The JSON property name of the field as it will appear in the invoice's metadata                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.value         | The default value of the field                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.required      | if true, the field will be required                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.label         | The label of the field                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.helpText      | Additional text to provide an explanation for the field.                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.fields        | You can organize your fields in a hierarchy, allowing child fields to be nested within the invoice’s metadata. This structure can help you better organize and manage the collected information, making it easier to access and interpret. For example, if you have a form that collects customer information, you can group the fields under a parent field called customer. Within this parent field, you might have child fields like name, Email, and address. |

Alan adı, kullanıcı tarafından sağlanan değeri Invoice'nın meta verilerinde saklayan JSON özellik adını temsil eder. Bazı iyi bilinen isimler yorumlanabilir ve Invoice'nın ayarlarını yapmak için değiştirilebilir.


| Field name       | Description            |
| ---------------- | ---------------------- |
| invoice_amount   | The invoice's amount   |
| invoice_currency | The invoice's currency |

Formun URL'sine "?your_field=value" gibi sorgu dizeleri ekleyerek bir Invoice'nin alanlarını otomatik olarak önceden doldurabilirsiniz.


İşte bu özellik için bazı kullanım durumları:



- Kullanıcı girişine yardımcı olmak: Formu doldurmalarını kolaylaştırmak için alanları bilinen müşteri bilgileriyle önceden doldurun. Örneğin, bir müşterinin Address e-postasını zaten biliyorsanız, onlara zaman kazandırmak için e-posta alanını önceden doldurabilirsiniz.
- Kişiselleştirme: Formu müşteri tercihlerine veya segmentasyonuna göre özelleştirin. Örneğin, farklı müşteri katmanlarınız varsa, formu üyelik seviyeleri veya belirli teklifler gibi ilgili verilerle önceden doldurabilirsiniz.
- İzleme: Gizli alanları ve önceden doldurulmuş değerleri kullanarak müşteri ziyaretlerinin kaynağını izleyin. Örneğin, her pazarlama kanalı için önceden doldurulmuş utm_media değerlerine sahip bağlantılar oluşturabilirsiniz (ör. Twitter, Facebook, E-posta). Bu, pazarlama çabalarınızın etkinliğini analiz etmenize yardımcı olur.
- A/B testi: Farklı form sürümlerini test etmek için alanları farklı değerlerle önceden doldurarak kullanıcı deneyimini ve dönüşüm oranlarını optimize etmenizi sağlar.


### Beceri Özeti


Bu bölümde aşağıdakileri öğrendiniz:



- Mağaza Ayarları'ndaki sekmelerin düzeni ve işlevleri
- Temel Exchange oranlarının, kısmi ödemelerin, hafif eksik ödemelerin ve daha fazlasının işlenmesinde ince ayar yapmak için çok sayıda seçenek.
- Faturalarda fiyata bağlı ana zincir ve Lightning etkinleştirmesi dahil olmak üzere ödeme görünümünü özelleştirin.
- Roller arasında mağaza erişim düzeylerini ve izinleri yönetin.
- Otomatik e-postaları ve tetikleyicilerini yapılandırma
- Ödeme sırasında ek müşteri bilgileri toplamak için özel formlar oluşturun.


### Bilgi Değerlendirmeleri


#### KA İnceleme


Mağaza Ayarları ile Sunucu Ayarları arasındaki fark nedir?


#### KA Varsayımsal


Ödeme Görünümü > Invoice Ayarları bölümünde seçebileceğiniz bazı seçenekleri ve nedenlerini açıklayın.


## BTCPay Sunucusu - Sunucu ayarları


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


BTCPay Server iki farklı ayar görünümünden oluşur. Biri Mağaza ayarlarına, diğeri ise Sunucu ayarlarına ayrılmıştır. İkincisi yalnızca sunucu yöneticileri tarafından kullanılabilir, mağaza sahipleri tarafından kullanılamaz. Sunucu yöneticileri kullanıcı ekleyebilir, özel roller oluşturabilir, e-posta sunucusunu yapılandırabilir, politikalar belirleyebilir, bakım görevlerini çalıştırabilir, BTCPay Server'a bağlı tüm hizmetleri kontrol edebilir, sunucuya dosya yükleyebilir veya Günlükleri kontrol edebilir.


### Kullanıcılar


Önceki bölümde belirtildiği gibi, Sunucu Yöneticileri kullanıcıları Kullanıcılar sekmesine ekleyerek sunucularına davet edebilirler.


### Sunucu genelinde özel Roller


BTCPay Server iki tür özel role sahiptir: BTCPay Server ayarlarında mağazaya özgü özel roller ve sunucu genelinde Özel roller. Her ikisi de benzer izinlere sahiptir; ancak, BTCpay Sunucu Ayarları - Roller sekmesi aracılığıyla ayarlanırsa, uygulanan rol sunucu genelinde olacak ve birden fazla mağaza için geçerli olacaktır. Sunucu ayarlarındaki özel roller için "Sunucu çapında" etiketine dikkat edin.


![image](assets/en/072.webp)


### Sunucu genelinde özel Roller


Sunucu genelinde özel roller izin kümesi;



- Mağazalarınızı değiştirin.
- Mağazalarınıza bağlı Exchange hesaplarını yönetin.
  - Mağazalarınıza bağlı Exchange hesaplarını görüntüleyin.
- Çekme ödemelerinizi yönetin.
- Çekme ödemeleri oluşturun.
  - Onaylanmamış çekme ödemeleri oluşturun.
- Faturaları değiştirin.
  - Faturaları görüntüleyin.
  - Bir Invoice oluşturun.
  - Mağazalarınızla ilişkili yıldırım düğümlerinden faturalar oluşturun.
- Mağazalarınızı görüntüleyin.
  - Faturaları görüntüleyin.
  - Ödeme taleplerinizi görüntüleyin.
  - Mağazaların web kancalarını değiştirin.
- Ödeme taleplerinizi değiştirin.
  - Ödeme taleplerinizi görüntüleyin.
- Mağazalarınızla ilişkili yıldırım düğümlerini kullanın.
  - Mağazalarınızla ilişkili yıldırım faturalarını görüntüleyin.
  - Mağazalarınızla ilişkili yıldırım düğümlerinden faturalar oluşturun.
- Mağazalarınıza bağlı Exchange hesaplarına para yatırın.
- Exchange hesaplarından mağazanıza para çekin.
- Mağazanızın Exchange hesaplarında fon ticareti yapın.


**!Not!**


Rol oluşturulduğunda adı sabitlenir ve düzenleme moduna geçtikten sonra değiştirilemez.


### E-posta


Sunucu genelinde E-posta ayarları, Mağazaya özel e-posta ayarlarındakilere benzer. Bununla birlikte, bu kurulum yalnızca mağazalar veya yönetici günlükleri için tetikleyicileri değil, aynı zamanda diğer olaylar için tetikleyicileri de işler. Bu E-posta kurulumu ayrıca BTCPay Sunucusunda Oturum Açma sırasında parola kurtarmayı da mümkün kılar. Mağazaya özel ayarlara benzer şekilde çalışır; yöneticiler E-posta parametrelerini hızlı bir şekilde doldurabilir ve e-posta kimlik bilgilerini girerek sunucunun e-posta göndermesine izin verebilir.


![image](assets/en/073.webp)


### Politikalar


BTCPay Server politika yöneticileri, Mevcut Kullanıcı ayarları, Yeni Kullanıcı ayarları, Bildirim ayarları ve Bakım ayarları gibi konularda çeşitli ayarlar yapabilirler. Bunlar, yeni kullanıcıları yönetici veya normal kullanıcı olarak kaydetmek veya BTCPay Sunucusunu sunucu başlığınıza ekleyerek arama motorlarından gizlemek için tasarlanmıştır.


![image](assets/en/074.webp)


#### Mevcut kullanıcı Ayarları


Burada bulunan seçenekler özel rollerden ayrıdır. Bu ek izinler, bir mağazayı veya sahibini saldırılara karşı savunmasız hale getirebilir. Mevcut kullanıcılara eklenebilecek politikalar:



- Yönetici olmayanların mağazalarında dahili Lightning düğümünü kullanmasına izin verin.
  - Bu, mağaza sahiplerinin sunucu Yöneticisinin Lightning düğümünü ve dolayısıyla fonlarını kullanmasına olanak tanıyacaktır! Dikkat edin, bu Lightning'e erişim sağlamak için bir çözüm değildir.
- Yönetici olmayanların mağazaları için Hot cüzdanları oluşturmasına izin verin.
  - Bu, BTCPay Sunucu örneğinizde hesabı olan herkesin Hot-cüzdanları oluşturmasına ve kurtarma seed'lerini Yöneticinin sunucusunda saklamasına olanak tanır. Bu, Yöneticiyi üçüncü taraf fonlarını tutmaktan sorumlu hale getirebilir!
- Yönetici olmayanların mağazaları için Hot cüzdanlarını içe aktarmalarına izin verin.
  - Önceki Hot cüzdanları oluşturma konusuna benzer şekilde, bu ilke Hot cüzdanları oluşturma bölümünde belirtilen aynı tehlikelerle birlikte bir Hot Wallet'in içe aktarılmasına izin verir.


![image](assets/en/075.webp)


#### Yeni kullanıcı ayarları


Sunucuya gelen yeni kullanıcıları yönetmek için bazı önemli ayarlar yapabiliriz. Yeni kayıtlar için bir onay e-postası ayarlayabilir, giriş ekranı üzerinden yeni kullanıcı oluşturmayı devre dışı bırakabilir ve yönetici olmayanların API üzerinden kullanıcı oluşturma erişimini kısıtlayabiliriz.



- Kayıt için bir onay e-postası isteyin.
  - Sunucu yöneticisi bir E-posta sunucusu kurmuş olmalıdır.
- Sunucuda yeni kullanıcı kaydını devre dışı bırakın
- Yönetici olmayanların kullanıcı oluşturma API uç noktasına erişimini devre dışı bırakın.


Varsayılan olarak, BTCPay Server "Sunucuda yeni kullanıcı kaydını devre dışı bırak" seçeneğini işaretlemiş ve yönetici olmayanların kullanıcı oluşturma API uç noktasına erişimini kapatmıştır. Bu güvenlik içindir, böylece BTCPay giriş bilgilerinize rastlayan rastgele kişiler hesap oluşturamaz.


![image](assets/en/076.webp)


#### Bildirim Ayarları


![image](assets/en/077.webp)


#### Bakım Ayarları


BTCPay Server, GitHub'da yaşayan bir Açık Kaynak projesidir. BTCPay Server yazılımın yeni bir sürümünü yayınladığında, Yöneticiler yeni bir sürümün mevcut olduğu konusunda bilgilendirilebilir. Yöneticiler ayrıca arama motorlarının (Google, Yahoo ve DuckDuckGo gibi) BTCPay Server etki alanını dizine eklemesini önlemek isteyebilir. BTCPay Server FOSS olduğundan, dünya çapındaki geliştiriciler yeni özellikler oluşturmak isteyebilir. BTCPay Server, açıldığında yöneticilerin üretim için değil, test amaçlı özellikleri kullanmasına olanak tanıyan deneysel bir özelliğe sahiptir.



- GitHub'daki sürümleri kontrol edin ve yeni bir BTCPay Server sürümü mevcut olduğunda haberdar olun.
- Arama motorlarının bu siteyi indekslemesini engelleyin
- Deneysel özellikleri etkinleştirin.


![image](assets/en/078.webp)


#### Eklentiler


BTCPay Server Eklentiler ekleyebilir ve özellik setini genişletebilir. Eklentiler varsayılan olarak BTCPay Server eklenti oluşturucu deposundan yüklenir. Bununla birlikte, bir yönetici eklentileri Yayın Öncesi durumunda görmeyi seçebilir ve eklenti geliştiricisi izin verirse, sunucu yöneticisi artık eklentilerin beta sürümlerini yükleyebilir.


![image](assets/en/079.webp)


##### Özelleştirme Ayarları


Standart bir BTCPay Server dağıtımına kurulum sırasında ayarlanan etki alanı üzerinden erişilebilir. Ancak, bir sunucu yöneticisi kök etki alanını yeniden eşleyebilir ve belirli bir mağazadan oluşturulan uygulamalardan birini görüntüleyebilir. Sunucu Yöneticisi ayrıca belirli etki alanlarını belirli uygulamalarla eşleştirebilir.



- Uygulamayı web sitesinin kök dizininde görüntüleme
  - Kök etki alanında gösterilecek olası uygulamaların bir listesini görüntüler.


![image](assets/en/080.webp)



- Belirli etki alanlarını belirli uygulamalarla eşleştirin.
  - Belirli uygulamalar için belirli bir etki alanı ayarlamak üzere tıkladığınızda, Yönetici belirli uygulamalara işaret eden gerektiği kadar etki alanı ayarlayabilir.


![image](assets/en/081.webp)


#### Blok kaşifleri


BTCPay Server, standart olarak, işlemler için Mempool olarak Block explorer.space ile birlikte gelir. BTCPay Server yeni bir Invoice oluşturduğunda ve buna bir işlem bağlandığında, mağaza sahibi işlemi açmak için tıklayabilir. BTCPay Server varsayılan olarak Mempool.space'i Block explorer olarak işaret edecektir; ancak, bir sunucu Yöneticisi bunu tercih ettiği seçeneğe değiştirebilir.


![image](assets/en/082.webp)


### Hizmetler


"BTCPay Sunucu ayarları: Hizmetler" sekmesi BTCPay Sunucunuzun kullandığı bileşenlere genel bir bakıştır. BTCPay Sunucunuzun sunduğu hizmetler dağıtım yöntemine bağlı olarak değişebilir.


Bir BTCPay Sunucu Yöneticisi, her bir hizmetin arkasındaki "Bilgileri gör "e tıklayarak hizmeti açabilir ve belirli ayarları yapabilir.


![image](assets/en/083.webp)


#### LND (gRPC)


BTCPay, LND'in GRPC hizmetini dış tüketim için sunar; bağlantı bilgilerini bu özel ayarlar menüsünde bulacaksınız; uyumlu cüzdanlar burada listelenmiştir. BTCPay Sunucusu ayrıca bağlantı için taranabilen ve mobil bir Wallet'de uygulanabilen bir QR kodu sağlar.


Sunucu yöneticileri daha fazla ayrıntı görmek için açabilir.



- Ev sahibi detayları
- SSL Kullanımı
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- GRPC SSL Şifre takımı (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


BTCPay, LND'in REST hizmetini dış tüketim için sunar; bağlantı bilgilerini burada bulacaksınız; uyumlu cüzdanlar burada listelenmiştir. Uyumlu cüzdanlar arasında Joule, Alby ve ZeusLN bulunmaktadır. BTCPay Sunucusu, bağlantı için uyumlu bir Wallet'de taranabilen ve uygulanabilen bir QR kodu sağlar.



- REST URI
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon


#### LND seed Yedekleme


LND seed yedeklemesi, sunucu bozulması durumunda LND Wallet'ünüzdeki fonları kurtarmak için kullanışlıdır. Lightning düğümü bir Hot-Wallet olduğundan, gizli seed bilgilerini bu sayfada bulabilirsiniz.


LND kurtarma sürecini belgeler. Belgeler için https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md adresine bakın.


#### Yıldırıma Bin


Ride the Lightning, Açık Kaynak yazılımı olarak oluşturulmuş bir Lightning düğüm yönetim aracıdır. BTCPay Server, yığınında Lightning düğüm yönetimi bileşeni olarak RTL kullanır. BTCPay Server yöneticileri RTL'ye Sunucu ayarları - Hizmetler sekmesinden veya Lightning Wallet'a tıklayarak ulaşabilirler.


#### Full node P2P


Sunucu yöneticileri Bitcoin düğümlerini mobil bir Wallet'e bağlamak isteyebilir. Bu sayfa, Full node protokolü aracılığıyla P2P'nıza uzaktan nasıl bağlanacağınız hakkında bilgi sağlar. Bu dersin yazımı itibariyle BTCPay Server, Blockstream Green ve Wasabi cüzdanlarını uyumlu cüzdanlar olarak listelemektedir. BTCPay Server, bağlantı için uyumlu bir Wallet'te taranabilen ve uygulanabilen bir QR kodu sağlar.


#### Full node RPC


Bu sayfa, RPC protokolü aracılığıyla Full node'unuza uzaktan bağlanmak için gerekli bilgileri gösterir.


#### SSH


SSH bakım amacıyla kullanılır. BTCPay Server, Sunucunuza ulaşmak için ilk bağlantı komutunu ve Sunucunuza bağlanmak için yetkilendirilmiş SSH genel anahtarlarını gösterir. Sunucu yöneticileri BTCPay Server kullanıcı arayüzü üzerinden SSH değişikliklerini devre dışı bırakmak isteyebilir.


#### Dinamik DNS


Dinamik DNS, IP Address'iniz düzenli olarak değişse bile, Sunucunuzu işaret eden sabit bir DNS adına sahip olmanızı sağlar. BTCPay Sunucusunu evde barındırıyorsanız ve Sunucunuza erişmek için temiz bir alan adına sahip olmak istiyorsanız bu önerilir.


HTTPS sertifikasını almak için NAT ve BTCPay Server kurulumunuzu doğru şekilde yapılandırmanız gerektiğini unutmayın.


### Tema


BTCPay Server, standart olarak iki tema ile birlikte gelir: Açık ve Koyu modlar. Bunlar, sol alt kısımdaki Hesap'a tıklanarak ve Koyu tema ile Açık tema arasında geçiş yapılarak değiştirilebilir. BTCPay Server yöneticileri, özel bir CSS teması sağlayarak kendi temalarını ekleyebilirler.


Yöneticiler kendi özel CSS'lerini ekleyerek veya özel temalarını tam özel olarak ayarlayarak Açık/Koyu temasını genişletebilirler.


![image](assets/en/084.webp)


#### Sunucu Markası


Sunucu yöneticileri, şirketinizin Sunucu çapında bir markasını belirleyerek BTCPay Sunucu markasını değiştirebilir. BTCPay Server FOSS olduğundan, sunucu yöneticileri yazılımı beyaz etiketleyebilir ve görünümü kendi işlerine uyacak şekilde özelleştirebilir.


![image](assets/en/085.webp)


### Bakım


Bir sunucu yöneticisi olarak, kullanıcılarınız sizden Sunucuya iyi bakmanızı bekler. BTCPay Server'ın Bakım sekmesinde, yönetici bazı temel bakımları yapabilir. Alan adını BTCPay Sunucu örneğine ayarlayın, Sunucuyu yeniden başlatın veya temizleyin. Muhtemelen en önemlisi, güncellemeleri çalıştırın.


BTCPay Server bir Açık Kaynak projesidir ve sık sık güncellenir. Her yeni sürüm, BTCPay Server Bildirimleriniz veya BTCPay Server'ın iletişim kurduğu resmi Kanallar aracılığıyla duyurulur.


![image](assets/en/086.webp)


#### Alan adı


BTCPay Sunucusu kurulduktan sonra, bir yönetici orijinal Etki Alanından uzaklaşmak isteyebilir. Bakım sekmesinde, yönetici Etki Alanını değiştirebilir. Onayla'ya tıkladıktan ve Etki Alanında uygun DNS kayıtlarını ayarladıktan sonra, BTCPay Server yeni Etki Alanına dönmek için güncellenir ve yeniden başlatılır.


![image](assets/en/087.webp)


#### Yeniden Başlat


BTCPay Sunucusunu ve ilgili hizmetleri yeniden başlatın.


![image](assets/en/088.webp)


#### Temiz


BTCPay Server Docker bileşenleri ile çalışır; güncellemelerle birlikte Docker imajları, geçici dosyalar vb. kalıntılar olabilir. Sunucu yöneticileri Clean betiğini çalıştırarak yer açabilirler.


![image](assets/en/089.webp)


#### Güncelleme


Bakım sekmesindeki en önemli seçenektir. BTCPay Server topluluk tarafından oluşturulmuştur ve bu nedenle güncelleme döngüleri çoğu yazılım ürününden daha sıktır. BTCPay Server yeni bir sürüme sahip olduğunda, yöneticiler bildirim merkezlerinde bilgilendirilecektir. Güncelleme düğmesine tıklandığında, BTCPay Server en son sürüm için GitHub'ı kontrol edecek, Sunucuyu güncelleyecek ve yeniden başlatacaktır. Güncellemeden önce, sunucu yöneticilerine her zaman BTCPay Server'ın resmi kanalları aracılığıyla dağıtılan sürüm notlarını okumaları tavsiye edilir.


![image](assets/en/090.webp)


### Günlükler


Bir sorunla karşılaşmak asla eğlenceli değildir. Bu belge, sorununuzu kendi başınıza veya topluluk yardımı ile etkili bir şekilde tanımlamak ve çözmek için en yaygın iş akışını ve adımları özetlemektedir.


Sorunun tanımlanması çok önemlidir.


#### Sorunun tekrarlanması


İlk ve en önemlisi, sorunun ne zaman meydana geldiğini belirlemeye çalışın. Sorunu tekrarlamaya çalışın. Sorunu yeniden oluşturabildiğinizi doğrulamak için Sunucunuzu güncellemeyi ve yeniden başlatmayı deneyin. Sorununuzu daha iyi açıklıyorsa, bir ekran görüntüsü alın.


##### Sunucunun güncellenmesi


BTCPay Server sürümünüzün BTCPay Server'ın [en son sürümünden] (https://github.com/btcpayserver/btcpayserver/releases) çok daha eski olup olmadığını kontrol edin. Sunucunuzu güncellemek sorunu çözebilir.


##### Sunucuyu yeniden başlatma


Sunucunuzu yeniden başlatmak, en yaygın BTCPay Sunucu sorunlarının çoğunu çözmenin kolay bir yoludur. Yeniden başlatabilmek için Sunucunuza SSH ile bağlanmanız gerekebilir.


##### Bir hizmeti yeniden başlatma


SSL sertifikasını yenilemek için letsencrypt konteynerini yeniden başlatmak gibi bazı sorunlar için BTCPay Server dağıtımınızda yalnızca belirli bir hizmeti yeniden başlatmanız gerekebilir.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Yeniden başlatmak istediğiniz farklı bir hizmetin adını bulmak için docker ps kullanın.


#### Kayıtları incelemek


Günlükler önemli bir bilgi parçası sağlayabilir. Aşağıdaki paragraflarda, BTCPay'in çeşitli bölümleri için günlük bilgilerinin nasıl alınacağını açıklayacağız.


##### BTCPay Günlükleri


V1.0.3.8'den bu yana, BTCPay Sunucu günlüklerine ön uçtan kolayca erişebilirsiniz. Sunucu yöneticisiyseniz, Sunucu Ayarları > Günlükler'e gidin ve günlük dosyasını açın. Günlüklerdeki belirli bir hatanın ne anlama geldiğini bilmiyorsanız, sorun giderme sırasında bundan bahsedin.


Daha ayrıntılı günlükler istiyorsanız ve bir Docker dağıtımı kullanıyorsanız, komut satırını kullanarak belirli Docker kapsayıcılarının günlüklerini görüntüleyebilirsiniz. Bir VPS üzerinde çalışan bir BTCPay örneğine ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) için bu [talimatlara] bakın.


Bir sonraki sayfada, BTCPay Sunucusu için kullanılan konteyner adlarının genel bir listesi yer almaktadır.


Günlükleri konteyner adına göre yazdırmak için aşağıdaki komutları çalıştırın. Diğer konteyner günlüklerini görüntülemek için konteyner adını değiştirin.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```


| Logs for     | Container Name                    |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker


Docker kullanırken LND günlüklerinize erişmenin birkaç yolu vardır. İlk olarak, root olarak oturum açın:


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Alternatif olarak, konteyner kimliğini kullanarak günlükleri hızlı bir şekilde yazdırabilirsiniz (yalnızca en soldaki iki karakter gibi ilk benzersiz kimlik karakterleri gereklidir):


```bash
docker logs 'add your container ID'
```


Herhangi bir nedenle daha fazla günlüğe ihtiyacınız olursa


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


Şöyle bir şey göreceksiniz


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


Bu günlüklerin sıkıştırılmamış günlüklerine erişmek için `cat LND.log` yapın veya başka bir tane istiyorsanız `cat LND.log.15` kullanın.


.gzip` sıkıştırılmış günlüklere erişmek için `gzip -d LND.log.16.gz` kullanın (bu durumda, `LND.log.16.gz` dosyasına erişiyoruz). Bu size `cat LND.log.16` yapabileceğiniz yeni bir dosya vermelidir. Yukarıdakilerin işe yaramaması durumunda, önce `sudo apt-get install gzip` ile gzip yüklemeniz gerekebilir.


###### Lightning Network c-lightning - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


Alternatif olarak, bunu kullanın:


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Günlük bilgilerini c-lightning CLI komutu ile de alabilirsiniz.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Bitcoin Düğüm Günlükleri


bitcoind konteynerinizin [günlüklerine bakmanın](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) yanı sıra, [bitcoin-cli komutlarından](https://developer.Bitcoin.org/reference/RPC/index.html) herhangi birini de kullanabilirsiniz


gW-454 düğümünüzden bilgi almak için [(yeni pencere açar)](https://developer.Bitcoin.org/reference/RPC/index.html). BTCPay, Bitcoin düğümünüzle kolayca iletişim kurmanızı sağlayacak bir komut dosyası içerir.


Btcpayserver-docker klasörünün içinde, düğümünüzü kullanarak Blockchain bilgilerini alın:


```bash
bitcoin-cli.sh getblockchaininfo
```


### Dosyalar


BTCPay Sunucusu, mağaza (ürün) varlıklarını, Logoları ve markaları doğrudan Sunucuya yüklemesine olanak tanıyan yerel bir dosya sistemine sahiptir. Sunucunun dosya sistemine yalnızca Sunucu Yöneticileri erişebilir; mağaza sahipleri logolarını veya markalarını mağaza düzeyinde yükleyebilirler.


Sunucu yöneticisi Dosya Depolama sekmesindeyken, doğrudan Sunucunuza yüklemek veya dosya depolama sağlayıcısını bir Yerel dosya sistemi veya Azure Blob Depolama olarak değiştirmek mümkündür.


![image](assets/en/091.webp)


![image](assets/en/092.webp)


### Beceri Özeti


Bu bölümde aşağıdakileri öğrendiniz:



- Mağaza ve Sunucu ayarları arasındaki fark, özellikle Kullanıcılar, Roller ve E-postalar ile ilgili olanlar
- Lightning veya Bitcoin Hot Wallet kullanımı ve oluşturulması, yeni kullanıcı kaydı ve e-posta bildirimleri için sunucu genelinde ilkeler ayarlayın.
- Özel temaların nasıl ekleneceği (sağlanan basit açık/koyu seçenekler yerine) ve özel logoların nasıl oluşturulacağı
- Sağlanan GUI aracılığıyla basit sunucu bakım görevlerini gerçekleştirin
- Docker konteynerlerinden herhangi biri veya düğümünüz için ayrıntıların alınması da dahil olmak üzere sorunları giderme
- Dosya depolamayı yönetin


### Bilgi değerlendirmesi


#### KA Kavramsal İnceleme


Sunucu ve Mağaza Ayarları aracılığıyla atanan Roller arasındaki fark nedir ve birinin diğerine göre potansiyel kullanımını ne açıklar?


#### KA Pratik İnceleme


İlkeler sekmesinde etkinleştirilen bazı olası kullanım durumlarını açıklayın.


#### KA Pratik İnceleme


Bir yöneticinin Bakım sekmesinde rutin olarak yapabileceği bazı eylemleri açıklayın.


## BTCPay Sunucusu - Ödemeler


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


Invoice, satıcının ödemeyi tahsil etmek için alıcıya verdiği bir belgedir.


BTCPay Server'da bir Invoice, sabit bir Exchange oranı üzerinden tanımlanmış bir zaman aralığında ödenmesi gereken bir belgeyi temsil eder. Faturaların son kullanma tarihleri vardır, çünkü Exchange oranını belirli bir zaman dilimi içinde kilitleyerek alıcıyı fiyat dalgalanmalarından korurlar.


BTCPay Server'ın özü, bir Bitcoin Invoice yönetim sistemi olarak hareket etme yeteneğidir. Bir Invoice, alınan ödemeleri izlemek ve yönetmek için önemli bir araçtır.


Ödemeleri manuel olarak almak için yerleşik bir [Wallet](https://docs.btcpayserver.org/Wallet/) kullanmadığınız sürece, bir mağazadaki tüm ödemeler Faturalar sayfasında gösterilecektir. Bu sayfa ödemeleri tarihe göre kümülatif olarak sıralar ve Invoice yönetimi ve ödeme sorunlarının giderilmesi için merkezi bir kaynak görevi görür.


![image](assets/en/093.webp)


### Genel


#### Invoice durumları


Aşağıdaki tabloda BTCPay'deki standart Invoice durumları, önerilen ortak eylemlerle birlikte listelenmekte ve açıklanmaktadır. Eylemler sadece tavsiyedir. Kendi kullanım durumları ve işleri için en iyi eylem planını tanımlamak kullanıcılara bağlıdır.


| Invoice Status             | Description                                                                                                                             | Action                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New                        | Not paid, invoice timer still has not expired                                                                                           | None                                                                                                                        |
| New (paidPartial)          | Paid, not in full, invoice timer still has not expired                                                                                  | None                                                                                                                        |
| Expired                    | Not paid, invoice timer expired                                                                                                         | None                                                                                                                        |
| Expired (paidPartial) \*\* | Paid, not in full amount, and expired                                                                                                   | Contact buyer to arrange a refund or ask for them to pay their due. Optionally mark the invoice as settled or invalid           |
| Expired (paidLate)         | Paid, in full amount, after the invoice timer has expired                                                                               | Contact buyer to arrange a refund or process order if late confirmations are acceptable.                                    |
| Settled (paidOver)         | Paid more than the invoice amount, settled, received sufficient amount of confirmations                                                 | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing                 | Paid in full, but has not received sufficient amount of confirmations specified in the store settings                                   | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing (paidOver)      | Paid more than the invoice amount, not received sufficient amount of confirmations                                                      | Wait to be settled, then contact the  buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Settled                    | Paid, in full, received sufficient amount of confirmations in store                                                                     | Fulfil the order                                                                                                            |
| Settled (marked)           | Status was manually changed to settled from a processing or invalid status                                                             | Store admin has marked the payment as settled                                                                               |
| Invalid\*                  | Paid, but failed to receive sufficient amount of confirmations within the time specified in store settings                              | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |
| Invalid (marked)           | Status was manually changed to invalid from a settled or expired status                                                                 | Store admin has marked the payment as invalid                                                                               |
| Invalid (paidOver)         | Paid more than the invoice amount, but failed to receive sufficient amount of confirmations within the time specified in store settings | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |

#### Invoice ayrıntıları


Invoice ayrıntıları sayfası bir Invoice ile ilgili tüm bilgileri içerir.


Invoice bilgileri, Invoice durumu, Exchange oranı vb. temel alınarak otomatik olarak oluşturulur. Invoice, Satış Noktası uygulamasında olduğu gibi ürün bilgileriyle oluşturulmuşsa ürün bilgileri otomatik olarak oluşturulur.


#### Invoice filtreleme


Faturalar, arama düğmesinin yanında bulunan hızlı filtreler veya üstteki (Yardım) bağlantısına tıklanarak değiştirilebilen gelişmiş filtreler aracılığıyla filtrelenebilir. Kullanıcılar faturaları mağaza, sipariş kimliği, ürün kimliği, durum veya tarihe göre filtreleyebilir.


#### Invoice ihracat


BTCPay Sunucu Faturaları CSV veya JSON formatında dışa aktarılabilir. Invoice dışa aktarma ve muhasebe hakkında daha fazla bilgi için.


#### Bir Invoice'nın İadesi


Herhangi bir nedenle geri ödeme yapmak isterseniz, Invoice görünümünden kolayca bir geri ödeme oluşturabilirsiniz.


#### Faturaların arşivlenmesi


BTCPay Server'ın Address yeniden kullanım özelliğinin bir sonucu olarak, mağazanızın Invoice sayfasında süresi dolmuş birçok fatura görmek yaygındır. Bunları görünümünüzden gizlemek için listeden seçin ve arşivlendi olarak işaretleyin. Arşivlendi olarak işaretlenen faturalar silinmez. Arşivlenmiş bir Invoice'a yapılan ödeme BTCPay Sunucunuz tarafından algılanmaya devam edecektir (paidLate durumu). Arama filtresi açılır menüsünden arşivlenmiş faturaları seçerek mağazanın arşivlenmiş faturalarını istediğiniz zaman görüntüleyebilirsiniz.


#### Varsayılan Para Birimi


Mağaza oluşturma sihirbazında ayarlanan mağaza varsayılan para birimi.


#### Herkesin bir Invoice oluşturmasına izin verin


Dış dünyanın mağazanızda fatura oluşturmasına izin vermek istiyorsanız bu seçeneği etkinleştirmelisiniz. Bu seçenek yalnızca ödeme düğmesini kullanıyorsanız veya API ya da üçüncü taraf bir HTML web sitesi aracılığıyla fatura düzenliyorsanız kullanışlıdır. PoS uygulaması önceden yetkilendirilmiştir ve rastgele bir ziyaretçinin POS mağazanızı açıp bir Invoice oluşturması için bu ayarın etkinleştirilmesini gerektirmez.


#### Invoice'ye Ek bir ücret (şebeke ücreti) ekleyin



- Yalnızca müşteri Invoice için birden fazla ödeme yaparsa
- Her ödemede
- Asla ağ ücreti eklemeyin


#### Invoice, tutarın tamamının ... tutanaktan sonra ödenmemesi durumunda sona erer.


Invoice zamanlayıcı varsayılan olarak 15 dakikaya ayarlanmıştır. Zamanlayıcı, kripto para miktarını kripto-fiat oranlarına göre kilitlediği için dalgalanmaya karşı bir koruma mekanizması görevi görür. Müşteri tanımlanan süre içinde Invoice'yı ödemezse, Invoice'nın süresinin dolduğu kabul edilir. Invoice, işlem Blockchain'te görünür hale gelir gelmez (sıfır onay ile) "ödendi" olarak kabul edilir ve satıcının tanımladığı onay sayısına (genellikle 1-6) ulaştığında "tamamlandı" olarak kabul edilir. Zamanlayıcı özelleştirilebilir.


#### Ödenen tutar beklenenden % ..oranında daha az olsa bile Invoice'nin ödendiğini kabul edin.


Bir müşterinin doğrudan bir Invoice için ödeme yapmak üzere bir Exchange Wallet kullandığı bir durumda, Exchange küçük bir ücret alır. Bu, böyle bir Invoice'un tamamen tamamlanmış olarak kabul edilmediği anlamına gelir. Invoice "kısmen ödendi" olarak işaretlenmiştir Bir satıcı eksik ödenmiş faturaları kabul etmek isterse, yüzde oranını buradan ayarlayabilirsiniz


### Talepler


Ödeme Talepleri, BTCPay mağaza sahiplerinin uzun ömürlü faturalar oluşturmasına olanak tanıyan bir özelliktir. Fonlar, ödeme sırasında yürürlükte olan Exchange oranı kullanılarak ödeme talebine göre ödenir. Bu, kullanıcıların ödeme sırasında mağaza sahibiyle Exchange oranlarını müzakere etmelerine veya doğrulamalarına gerek kalmadan istedikleri zaman ödeme yapmalarına olanak tanır.


Kullanıcılar kısmi ödemelerde talepler için ödeme yapabilirler. Ödeme talebi, tamamı ödenene kadar veya mağaza sahibi bir sona erme süresi talep ederse geçerli kalacaktır. Adresler asla tekrar kullanılmaz. Kullanıcı ödeme talebine yönelik bir Invoice oluşturmak için her ödeme düğmesine tıkladığında yeni bir Address oluşturulur.


Mağaza sahipleri, kayıt tutma ve muhasebe için ödeme taleplerini yazdırabilir (veya Invoice verilerini dışa aktarabilir). BTCPay, mağazanızın Invoice listesinde faturaları otomatik olarak Ödeme Talepleri olarak etiketler.


#### Ödeme Taleplerinizi Özelleştirin



- Invoice Tutar - Talep Edilen Ödeme Tutarını Ayarlayın
- Denomination - Talep Edilen Tutarı Fiat veya Kripto Para Olarak Göster
- Ödeme Miktarı - Yalnızca tek ödemelere veya kısmi ödemelere izin verin
- Sona Erme Süresi - Ödemelerin bir tarihe kadar veya sona ermeden yapılmasına izin verin
- Açıklama - Metin Düzenleyici, Veri Tabloları, Fotoğraf ve Video Ekleme
- Görünüm - CSS Temaları ile Renk ve Stil


![image](assets/en/094.webp)


#### Ödeme Talebi Oluşturun


Sol menüden Ödeme Talebi'ne gidin ve "Ödeme Talebi Oluştur "a tıklayın.


![image](assets/en/095.webp)


Talep Adı, Tutar, Gösterge Değeri, İlişkili Mağaza, Son Kullanma Süresi ve Açıklama (İsteğe Bağlı)


Kısmi ödemelere izin vermek istiyorsanız Alacaklının kendi mezhebinde fatura oluşturmasına izin ver seçeneğini belirleyin.


Ödeme talebinizi incelemek için Kaydet ve Görüntüle'ye tıklayın.


BTCPay ödeme talebi için bir URL oluşturur. Ödeme talebinizi görüntülemek için bu URL'yi paylaşın. Aynı talepten birden fazlasına mı ihtiyacınız var? Ana menüdeki Klonla seçeneğini kullanarak ödeme taleplerini çoğaltabilirsiniz.


![image](assets/en/096.webp)


**UYARI**


Ödeme talepleri mağazaya bağlıdır, yani her ödeme talebi oluşturma sırasında bir mağaza ile ilişkilendirilir. Ödeme talebinin ait olduğu mağazanıza bağlı bir Wallet olduğundan emin olun.


#### Ücretli Talep


Alacaklı ve talep eden, ödeme gönderildikten sonra ödeme talebinin durumunu görüntüleyebilir. Ödeme tam olarak alınmışsa durum Anlaşıldı olarak görünecektir. Yalnızca kısmi ödemeler yapılmışsa, Ödenmesi Gereken Tutar kalan bakiyeyi gösterecektir.


![image](assets/en/097.webp)


#### Ödeme Taleplerini Özelleştirin


Açıklama içeriği, ödeme talebinin metin düzenleyicisi kullanılarak düzenlenebilir. Ek renk temaları veya özel CSS stilleri kullanmak istiyorsanız her iki seçenek de mevcuttur.


Teknik olmayan kullanıcılar bir [bootstrap teması] (https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes) kullanabilir. Aşağıda gösterildiği gibi ek CSS kodu sağlayarak daha fazla özelleştirme yapılabilir.


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### Ödemeleri çekin


Geleneksel olarak, bir alıcı Bitcoin ödemesi yapmak için Bitcoin Address'sini paylaşır ve gönderici daha sonra bu Address'ye para gönderir. Alıcı müsait olmayabilirken gönderici ödemeyi başlattığı ve ödemeyi alıcıya ittiği için böyle bir sistem İtmeli ödeme olarak adlandırılır.


Ancak, rolü tersine çevirmeye ne dersiniz?


Peki ya gönderici ödemeyi itmek yerine, alıcının uygun gördüğü bir zamanda ödemeyi çekmesine izin verirse? Bu bir Çekme ödemesi kavramıdır. Bu, aşağıdakiler gibi birçok yeni uygulamaya izin verir:



- Bir abonelik hizmeti (abonenin hizmetin her x miktarda para çekmesine izin verdiği)
- Para iadeleri (satıcının, müşterinin uygun gördüğü zaman iade parasını Wallet'una çekmesine izin verdiği durumlarda)
- Serbest çalışanlar için zamana dayalı faturalandırma (işe alan kişinin, zaman raporlandıkça serbest çalışanın Wallet'üne para çekmesine izin vermesi)
- Patronaj (patronun, alıcının çalışmalarını desteklemeye devam etmesi için her ay para çekmesine izin vermesi)
- Otomatik satış (bir Exchange müşterisinin, Exchange'in Wallet'sinden her ay otomatik olarak satış yapmak için para çekmesine izin vermesi)
- Bakiyeden para çekme sistemi (yüksek hacimli bir hizmetin kullanıcıların bakiyelerinden para çekme talebinde bulunmalarına izin verdiği durumlarda, hizmet daha sonra tüm ödemeleri sabit aralıklarla birçok kullanıcıya kolayca toplu olarak yapabilir)


### Ödemeler


Ödeme işlevi [Pull Payments] (https://docs.btcpayserver.org/PullPayments/) özelliğine bağlıdır. Bu özellik, BTCPay'inizde ödeme oluşturmanıza olanak tanır. Bu özellik, çekme ödemelerini (geri ödemeler, maaş ödemeleri veya para çekme işlemleri) işleme koymanıza olanak tanır.


#### Örnek 1: Para İadesi


Para iadesi örneğiyle başlayalım. Müşteri mağazanızdan bir ürün satın aldı, ancak ne yazık ki iade etmek zorunda. Para iadesi istiyorlar. BTCPay'de bir [Refund] (https://docs.btcpayserver.org/Refund/) oluşturabilir ve müşteriye fonlarını talep etmesi için bağlantı sağlayabilirsiniz. Müşteri Address'ünü girdikten ve parayı talep ettikten sonra, Ödemeler bölümünde görüntülenecektir.


Sahip olduğu ilk durum Onay Bekliyor'dur. Mağaza görevlileri birden fazla bekleyen olup olmadığını kontrol edebilir ve seçimi yaptıktan sonra Eylemler düğmesini kullanırsınız.


Eylem düğmesindeki seçenekler



- Seçilen ödemeleri onaylayın
- Seçilen ödemeleri onaylayın ve gönderin
- Seçili ödemeleri iptal et


Bir sonraki adım, müşteriye para iadesi yapmak istediğimiz için seçilen ödemeleri onaylamak ve göndermektir. Tutarı ve ücretlerin iadeden çıkarılmasını isteyip istemediğimizi gösteren Müşterinin Address'ünü kontrol edin. Kontrolleri tamamladıktan sonra geriye kalan tek adım işlemi imzalamaktır.


Müşteri artık Talep sayfasında güncellenir. Kendisine bir Block explorer bağlantısı ve işlemi sağlandığı için işlemi takip edebilir. İşlem onaylandıktan sonra durumu 'Tamamlandı' olarak değişir.


#### Örnek 2: Maaş


Şimdi Maaş ödemesine geçelim, çünkü bu Müşterinin talebine göre değil, mağazanın içinden yönlendirilir. Temel konsept aynıdır; çekme ödemelerini kullanır. Ancak bir geri ödeme oluşturmak yerine, bir [Çekme Ödemesi] (https://docs.btcpayserver.org/PullPayments/) yapacağız.


BTCPay sunucunuzdaki Çekme Ödemeleri sekmesine gidin. Sağ üstte, Çekme Ödemesi Oluştur Düğmesine tıklayın.


Şimdi Ödemeyi oluşturuyoruz, ona bir isim ve seçilen para biriminde istenen miktarı verin. Açıklamayı doldurun, böylece çalışan bunun ne hakkında olduğunu bilir. Sonraki kısım geri ödemelere benzer. Çalışan Hedef Address'yı ve bu Ödemeden talep etmek istediği tutarı doldurur. Bunu 2 ayrı talep haline getirmeye, farklı adreslere göndermeye veya hatta yıldırım üzerinden kısmen talep etmeye karar verebilir.


Bekleyen birden fazla Ödeme varsa, bunları toplu olarak imzalayıp gönderebilirsiniz. İmzalandıktan sonra ödemeler Devam Ediyor sekmesine taşınır ve İşlemi gösterir. Ağ tarafından kabul edildiğinde, ödeme Tamamlandı sekmesine taşınır. Tamamlanan sekmesi tamamen tarihsel amaçlar içindir. İşlenmiş Ödemeleri ve ona ait işlemleri tutar


### Ödemeleri çekin


#### Konsept


Gönderen bir Çekme ödemesini yapılandırdığında, bir dizi özelliği yapılandırabilir:



- Çekme isteği Adı
- Bir limit tutarı
- Bir Birim (BTC, SAT, USD gibi)
- Ödeme Yöntemleri
  - BTC On-Chain
  - BTC off-chain
- Açıklama
- Özel CSS
- Bitiş tarihi (Lightning Network BOLT11 için isteğe bağlı)


Bundan sonra, gönderici alıcı ile bir bağlantı kullanarak çekme ödemesini paylaşabilir ve alıcının bir ödeme oluşturmasına izin verebilir. Alıcı kendi ödemesini seçecektir:



- Hangi ödeme yönteminin kullanılacağı
- Paranın nereye gönderileceği


Bir ödeme oluşturulduktan sonra, mevcut dönem için çekme ödemesi limitine sayılacaktır. Gönderen daha sonra ödemenin gönderileceği oranı ayarlayarak ödemeyi onaylayacak ve ödemeye devam edecektir.


Gönderen için, [BTCPay Internal Wallet] (https://docs.btcpayserver.org/Wallet/) üzerinden birden fazla ödemeyi toplu hale getirmek için kullanımı kolay bir yöntem sunuyoruz.


#### Greenfield API


BTCPay Server, hem gönderici hem de alıcı için örneğinizin `/docs` sayfasında belgelenen tam bir API sağlar. (veya dokümantasyon web sitesinde https://docs.btcpayserver.org)


API'miz çekme ödemelerinin tüm kapasitesini ortaya çıkardığından, bir gönderici ödemeleri kendi ihtiyaçlarına göre otomatikleştirebilir.


### Beceri Özeti


Bu bölümde aşağıdakileri öğrendiniz:



- BTCPay Server'ın Invoice durumlarının yanı sıra bunlar üzerinde gerçekleştirilebilecek eylemlerin derinlemesine anlaşılması
- İstekler olarak bilinen uzun ömürlü Invoice mekanizmalarını özelleştirin ve yönetin.
- BTCPay Server'ın benzersiz Çekerek Ödeme özelliği ile özellikle geri ödemeler ve maaş ödemelerinde ek esnek ödeme olanakları sağlanmıştır.


### Bilgi değerlendirmesi


#### KA Kavramsal İnceleme


Faturalar ve ödeme talepleri arasındaki bazı farklar nelerdir ve ikincisini kullanmak için iyi bir neden ne olabilir?


#### KA Kavramsal İnceleme


Çekme ödemeleri tipik olarak On-Chain ile yapılabilenleri nasıl genişletiyor? Sağladıkları bazı kullanım durumlarını açıklayın.


## BTCPay Sunucu Varsayılan Eklentileri


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Varsayılan Eklentiler ve Uygulamalar


BTCPay sunucusu, BTCPay Sunucusunu bir e-ticaret ödeme ağ geçidine dönüştürebilen standart bir Eklenti (Uygulama) seti ile birlikte gelir. Satış Noktası, Kitle Fonlaması platformu ve kolay Ödeme düğmesinin eklenmesiyle BTCPay Sunucusu, kurulumu kolay bir çözüm haline gelir.


### Satış Noktası


BTCPay Server'ın standart eklentilerinden biri de Satış Noktası'dır (PoS). PoS eklentisi ile bir mağaza sahibi doğrudan BTCPay Server'dan bir Webshop oluşturabilir; mağaza sahibinin bir Webshop çalıştırmak için üçüncü taraf e-ticaret çözümlerine ihtiyacı yoktur. Web tabanlı PoS uygulaması, tuğla ve harç mağazaları olan kullanıcıların Bitcoin'ü ücret veya üçüncü bir taraf olmadan doğrudan Wallet'lerine kolayca kabul etmelerini sağlar. PoS, tabletlerde veya web taramasını destekleyen diğer cihazlarda kolayca görüntülenebilir. Kullanıcılar web uygulamasına hızla erişmek için kolayca bir ana ekran kısayolu oluşturabilir.


#### Yeni bir Satış Noktası nasıl oluşturulur


BTCPay Server, mağaza sahiplerinin birden fazla düzende hızlı bir şekilde Satış Noktası oluşturmasını sağlar. BTCPay Server, her mağazanın e-ticaret olmadığını ve her mağazanın bir bar veya restoran olmadığını kabul eder ve PoS'unuz için birden fazla standart kurulumla birlikte gelir.


Mağaza sahibi sol menü çubuğunda "Satış Noktası" üzerine tıkladığında, BTCPay Sunucusu şimdi bir isim isteyecektir; bu isim sol menü çubuğunda görünecektir. PoS'u oluşturmak için Oluştur'a tıklayın.


![image](assets/en/098.webp)


#### Yeni oluşturulan Satış Noktasını güncelleyin


Yeni bir PoS oluşturduktan sonra, aşağıdaki ekran Satış Noktanızı güncellemenize ve mağazanız için ürün eklemenize olanak tanıyacaktır.


##### Uygulama adı


Burada Satış Noktanıza verilen isim BTCPay Sunucusunun ana menüsünde görülecektir.


##### Ekran Başlığı


Halk ziyaret ederken mağazanızın başlığını veya adını görecektir. BTCPay Server, varsayılan olarak mağazanızı "Çay dükkanı" olarak adlandırır Bunu mağazanızın adı ile değiştirin.


![image](assets/en/099.webp)


#### Satış Noktası Stilini Seçin


BTCPay Sunucusu, Satış Noktasını birden fazla şekilde görüntüleyebilir.



- Ürün listesi
  - Müşterilerin aynı anda yalnızca 1 ürün satın alabildiği bir mağaza görünümü.
- Sepetli ürün listesi.
  - Müşterilerin aynı anda birden fazla ürün satın alabilecekleri ve ekranlarının sağ tarafında alışveriş sepetine genel bakış görebilecekleri bir mağaza görünümü.
- Yalnızca tuş takımı
  - Ürün listesi yok, sadece doğrudan faturalama için bir tuş takımı.
- Print display (QR ile yazdırılabilir ürün listesi)
  - Ürün listenizi her zaman dijital olarak görüntüleyemiyorsanız, ürünler için "çevrimdışı" bir çözüme ihtiyacınız var; BTCPay Server, Çevrimdışı mağaza olarak işlev görmek için bir baskı ekranına sahiptir.


![image](assets/en/100.webp)


#### Satış Noktası Stili - Ürün listesi


![image](assets/en/101.webp)


#### Satış Noktası Stili - Ürün listesi + Sepet


![image](assets/en/102.webp)


#### Satış Noktası Stili - Sadece Tuş Takımı


![image](assets/en/103.webp)


#### Satış Noktası Stili - Baskı ekranı


![image](assets/en/104.webp)


#### Para Birimi


Mağaza sahibi, Satış Noktası için genel olarak ayarlanmış varsayılan para biriminden farklı bir para birimi belirleyebilir. Mağazanın varsayılan para birimi bu alanı otomatik olarak dolduracaktır.


#### Açıklama


Dünyaya dükkanınızdan bahsedin; ne satıyorsunuz ve ne kadara satıyorsunuz? Dükkanınızı anlatan her şey burada.


![image](assets/en/105.webp)


#### Ürünler


Bir Satış Noktası oluşturulduğunda, standart bir BTCPay Sunucusu referans için mağazaya birkaç öğe ekler. Bir öğe için olası her seçeneği daha iyi anlamak için standart öğelerden herhangi birinin üzerindeki Düzenle düğmesine tıklayın.


Mağazanızda yeni bir ürün oluşturmak aşağıdaki alanlardan oluşur;



- Başlık
- Fiyat (sabit, minimum veya özel)
- Resim URL'si
- Açıklama
- Envanter
- KIMLIK
- Düğme Metni Satın Alın.
- Etkinleştir/Devre Dışı Bırak


Mağaza sahibi tüm yeni ürün alanlarını doldurduktan sonra kaydet'e tıklayın ve Satış Noktasındaki Ürünler bölümünün artık doldurulduğunu göreceksiniz. Mağaza sahiplerinin ürün eklerken ilerlemelerini kaybetme olasılığını önlemek için her zaman ekranınızın sağ üst köşesine kaydedin.


Mağaza sahipleri ürünlerini yapılandırmak için "Ham Düzenleyici "yi de kullanabilir. Ham düzenleyici, JSON yapılarının temel düzeyde anlaşılmasını gerektirir.


![image](assets/en/106.webp)


#### Ödeme


BTCPay Server, küçük PoS'a özgü ödeme özelleştirmesine izin verir. Mağaza sahibi "x için satın al" metnini ayarlayabilir veya formlara ekleyerek belirli müşteri verilerini talep edebilir.


#### İpuçları


Yalnızca bazı mağazaların satışlarıyla ilgili İpuçları seçeneğine ihtiyacı vardır. Mağaza sahipleri bunu mağazaları için uygun gördükleri şekilde açabilir veya kapatabilir. Mağaza bahşişleri açık olarak kullanıyorsa, mağaza sahibi istediği bahşişler için alandaki metni ayarlayabilir. BTCPay Sunucu bahşişleri bir yüzde miktarına göre çalışır. Mağaza sahipleri virgülle ayırarak birden fazla yüzde ekleyebilir.


#### İndirimler


Bir mağaza sahibi olarak, müşteriye ödeme sırasında özel bir indirim vermek isteyebilirsiniz; İndirimler için geçiş mağazanızın ödeme sayfasında kullanılabilir hale gelir. Ancak, self-checkout sistemlerinin kullanılmaması şiddetle tavsiye edilir.


#### Özel Ödemeler


Özel Ödemeler seçeneği açıldığında, müşteri mağaza tarafından oluşturulan orijinal Invoice'ya eşit veya daha yüksek bir fiyat girebilir.


#### Ek Seçenekler


Satış Noktanız için her şeyi ayarladıktan sonra geriye bazı ekstra seçenekler kalıyor. Mağaza sahipleri PoS'larını bir Iframe aracılığıyla kolayca yerleştirebilir veya belirli bir mağaza öğesine bağlanan bir ödeme düğmesi yerleştirebilir. Yeni oluşturulan PoS mağazasını stilize etmek için, mağaza sahipleri ek seçeneklerin altına özel CSS ekleyebilir.


#### Bu uygulamayı sil


Mağaza sahibi Satış Noktasını BTCPay Sunucusundan tamamen silmek isterse, PoS'u güncellemenin alt kısmında, mağaza sahipleri PoS uygulamalarını tamamen yok etmek için Bu uygulamayı sil düğmesine tıklayabilirler. "Bu uygulamayı sil" düğmesine tıklandığında, BTCPay Sunucusu `DELETE` yazarak onay isteyecek ve Sil düğmesine tıklayarak onaylayacaktır. Silme işleminden sonra, mağaza sahibi BTCPay Server kontrol paneline geri döner.


### BTCPay Sunucusu - Kitle Fonlaması


Satış Noktası eklentisinin yanında, BTCPay Server bir kitle fonlaması oluşturma seçeneğine sahiptir. Tıpkı diğer Crowdfund platformlarında olduğu gibi, mağaza sahipleri bir hedef belirleyebilir, katkılar için avantajlar oluşturabilir ve bunu ihtiyaçlarına göre özelleştirebilir.


#### Yeni bir kitle fonlaması nasıl kurulur?


BTCPay Sunucunuzun solundaki ana menüden, Eklenti bölümünün altındaki Crowdfund eklentisine tıklayın. BTCPay Sunucusu şimdi Kitle Fonlaması için bir ad isteyecektir; bu ad Sol menü çubuğunda da görüntülenecektir.


![image](assets/en/107.webp)


#### Yeni oluşturulan Satış Noktasını güncelleyin


Uygulamaya bir isim verildikten sonra, bir sonraki ekran Uygulamayı içeriğe sahip olacak şekilde güncellemek olacaktır.


#### Uygulama Adı


Kitle Fonunuza verilen ad BTCPay Sunucusunun ana menüsünde görünecektir.


#### Ekran Başlığı


Kitle Fonuna halk için unvan verilmiştir.


#### Tagline


Kitle fonuna, bağış kampanyasının ne hakkında olduğunu belirten tek satırlık bir açıklama ekleyin.


![image](assets/en/108.webp)


#### Öne Çıkan Görsel URL'si


Her kitle fonunun ana görseli, doğrudan tanıdığınız bir afiş vardır. Yönetici haklarınız varsa bu görüntü sunucunuzda saklanabilir. Yöneticiler BTCPay Sunucu ayarları - Dosyalar altında yükleme yapabilir. Bir Mağaza sahibi olduğunuzda, görsel üçüncü taraf bir ana bilgisayar (örneğin, Imgur) aracılığıyla web'e yüklenmelidir.


#### Kitle Fonunu Halka Açın


Bu geçiş, Kitle Fonunuzu halka açık hale getirir ve böylece dış dünya tarafından görülebilir. Test amacıyla veya temanızın doğru uygulanıp uygulanmadığını görmek için, kitle fonunu oluşturma süresi boyunca bu ayarı KAPALI olarak tutun.


#### Açıklama


Dünyaya Kitle Fonunuzdan bahsedin. Ne için fon topluyorsunuz? Kitle fonunuzu açıklayan her şey burada.


![image](assets/en/109.webp)


#### Kitlesel Fon Hedefi


Bağış toplayan kişinin proje için ne kadar kazanması gerektiğine ve hedefin hangi para birimi cinsinden olması gerektiğine dair bir hedef belirleyin. Hedefleriniz tarihler arasında belirleniyorsa, bu hedef ve bitiş tarihlerini Kitle Fonlamasında Hedefler bölümüne ekleyin.


![image](assets/en/110.webp)


#### Avantajlar


Avantajlar kitlesel fonlama çalışmalarınızı önemli ölçüde geliştirebilir. Bunun nedeni, avantajların insanlara kampanyanıza katılmaları için bir yol sunmasıdır. Hem bencil hem de yardımsever motivasyonlardan yararlanırlar. Ayrıca destekçilerinizin yalnızca hayırseverlik cüzdanlarına değil, harcamalarına da erişmenizi sağlarlar - hangisinin daha önemli olduğunu tahmin edebilirsiniz.


Yeni bir avantaj oluşturmak aşağıdaki alanlardan oluşur.



- Başlık
- Fiyat (sabit, minimum veya özel)
- Resim URL'si
- Açıklama
- Envanter
- KIMLIK
- Düğme Metni Satın Alın.
- Etkinleştir/Devre Dışı Bırak


Mağaza sahibi yeni avantajın tüm alanlarını doldurduktan sonra kaydet'e tıklayın ve Kitle Fonları'ndaki Avantajlar bölümünün artık doldurulduğunu göreceksiniz.


![image](assets/en/111.webp)


### BTCPay Sunucusu - Satış Noktası


#### Katkılar


Mağaza sahipleri Avantajların nasıl görüntüleneceğini, nasıl sıralanacağını ve hatta diğer avantajlara göre nasıl sıralanacağını seçebilir. Bununla birlikte, Kitle Fonları hedeflerine ulaşıldığında, mağaza sahipleri bu bağış toplama etkinliğine akan bağışları durdurmak isteyebilir. Bu nedenle, "Hedefe ulaştıktan sonra ek katkılara izin verme" seçeneğini açabilir. Bu, Kitle Fonunun bağış kabul etmesini engelleyecektir.


##### Kitle fonlaması davranışı


Crowdfund'un standardı yalnızca Crowdfund ile oluşturulan faturaları hedefe doğru sayar. Ancak, Mağaza sahibinin bu mağazada oluşturulan tüm faturaların Kitle Fonuna sayılmasını istediği durumlar olabilir.


#### Özelleştirme için Ek Seçenekler


BTCpay Server birkaç ekstra özelleştirme sunar. Kitle Fonuna sesler, animasyonlar ve hatta tartışma konuları ekleyin. Mağaza sahipleri ayrıca kendi özel CSS'lerini girerek Kitle Fonunun görünümünü ve hissini değiştirebilirler.


#### Bu uygulamayı sil


Mağaza sahibi Kitle Fonunu BTCPay Sunucusundan tamamen silmek isterse, Kitle Fonunu güncellemenin alt kısmında, Kitle Fonu uygulamasını tamamen kaldırmak için "Bu uygulamayı sil" düğmesine tıklayabilir. "Bu uygulamayı sil" düğmesine tıklandığında, BTCPay Sunucusu `DELETE` yazarak onay isteyecek ve Sil düğmesine tıklayarak onaylayacaktır. Silme işleminden sonra, mağaza sahibi BTCPay Server kontrol paneline geri döner.


### BTCPay Sunucusu - Ödeme Düğmesi


Kolayca yerleştirilebilen HTML ve son derece özelleştirilebilir ödeme düğmeleri, mağaza sahiplerinin bahşiş ve bağış almasına olanak tanır. BTCPay Server'ın sol menü çubuğunda, Eklentiler bölümünün altında, mağaza sahipleri "Ödeme Düğmesi" ni tıklayabilir ve bir Ödeme düğmesi oluşturmak için Etkinleştir'i tıklayabilir.


#### Genel Ayarlar


Ödeme Düğmesi için Genel Ayarlar'da mağaza sahipleri şunları ayarlayabilir



- Standart fiyat
- Varsayılan Para Birimi
- Varsayılan Ödeme Yöntemi
  - Mağaza varsayılanını kullan
  - BTC On-Chain
  - BTC off-chain (Yıldırım)
  - BTC off-chain (LNURL-pay)
- Ödeme açıklaması
- Sipariş Kimliği


#### Görüntüleme seçenekleri


BTCPay Server'ın Ödeme düğmesi farklı stillere uyacak şekilde yapılandırılabilir. Düğmeler, kaydırıcı veya artı ve eksi geçişleriyle görüntülenen sabit veya özel bir tutara sahip olabilir.


#### Modal Kullan


Mağaza sahipleri ödeme düğmesini oluştururken, müşteri düğmeye tıkladığında davranışını seçebilir ve düğmeyi bir modalde veya yeni bir sayfa olarak gösterebilir.


**!Not!**


Uyarı Ödeme düğmesi yalnızca bahşiş ve bağışlar için kullanılmalıdır


Kullanıcı siparişle ilgili bilgileri değiştirebileceğinden, e-ticaret entegrasyonları için ödeme düğmesinin kullanılması önerilmez. E-ticaret için Greenfield API'mizi kullanmalısınız. Bu mağaza ticari işlemler gerçekleştiriyorsa ödeme düğmesini kullanmadan önce ayrı bir mağaza oluşturmanızı öneririz.


#### Ödeme düğmesi Metnini Özelleştir


Varsayılan olarak, BTCPay Server'ın ödeme düğmesinde "BTCPay ile Öde" yazar. Mağaza sahipleri bu metni istedikleri gibi ayarlayabilir ve BTCPay Server logosunu kendi logolarıyla değiştirebilirler. Metni "Ödeme Düğmesi Metni "ni kullanarak ayarlayın ve resim URL'sini "Ödeme Düğmesi Resim URL'si "nin altına yapıştırın.


##### Resim boyutu


Düğmedeki görüntünün boyutu yalnızca üç varsayılan değere ayarlanabilir.



- 146x40px
- 168x46px
- 209x57px


#### Düğme Tipi


BTCPay Sunucusu, Ödeme Düğmesi için üç durumu bilir.



- Sabit Tutar
  - Önceki ayarlanan fiyat düğmenin genel ayarlarındadır.
- Özel Tutar
  - BTCPay Sunucusunun Ödeme düğmesi, özel bir fiyat belirlemek için + ve - geçişlerine sahiptir.
  - Özel tutarı kullanırken, BTCPay Sunucusu bir Min, Maks ve ne kadar kademeli olarak artması gerektiğini talep edecektir.
  - Düğmeler "Basit giriş stilini kullan" olarak ayarlanabilir, bu +/- Geçişlerini ortadan kaldırır.
  - Düğme ve geçişlerin satır içinde göründüğü yere düğmeyi satır içine sığdırın.
- Kaydırıcı
  - Özel miktara benzer, ancak +/- geçişleri yerine bir kaydırıcıya sahip olduğu için görsel olarak farklıdır.
  - Kaydırıcıyı kullanırken, BTCPay Sunucusu bir Min, Maks ve ne kadar kademeli olarak artması gerektiğini talep edecektir.


**!Not!**


Uyarı açıklamasının üst kısmındaki Ödeme düğmesi silinebilir.


#### Ödeme Bildirimleri


Sunucu IPN (Anında Ödeme Bildirimi) web kancaları için tasarlanmıştır ve satın alma sonrası veriler için bir URL ile yapılandırılabilir.


#### E-posta Bildirimleri


Bir ödeme yapıldığında, BTCPay Sunucusu mağaza sahibini bilgilendirebilir.


#### Tarayıcı yönlendirmesi


Müşteri satın alma işlemini tamamladığında, mağaza sahibi tarafından ayarlanmışsa bu bağlantıya yönlendirilecektir.


#### Gelişmiş Ödeme Düğmesi Seçenekleri


Invoice oluşturulduktan sonra ödeme sayfasına eklenmesi gereken ek sorgu dizesi parametrelerini belirtin. Örneğin, `lang=da-DK` ödeme sayfasını varsayılan olarak Danca dilinde yükleyecektir.


#### Uygulamayı Uç Nokta Olarak Kullanın


Ödeme düğmesini daha önce kullandığınız PoS veya Kitle Fonlaması uygulamalarından birindeki bir öğeye doğrudan bağlayabilirsiniz.


Mağaza sahipleri açılır menüye tıklayıp istedikleri Uygulamayı seçebilir; Uygulama seçildikten sonra mağaza sahibi bağlanması gereken öğeyi ekleyebilir.


#### Oluşturulan Kod


BTCPay Server'ın Ödeme düğmesi kolayca gömülebilir bir HTML olduğundan, BTCPay Server Ödeme düğmesini yapılandırdıktan sonra alt kısımda bir web sitesine kopyalamak için oluşturulan kodu gösterir.


Mağaza sahipleri oluşturulan kodu web sitelerine kopyalayabilir ve BTCPay Sunucusundan Ödeme düğmesi doğrudan web sitelerinde aktif olur.


#### Ödeme Bildirimleri


Sunucu IPN (Anında Ödeme Bildirimi) web kancaları için tasarlanmıştır ve satın alma verilerini göndermek için bir URL ile yapılandırılabilir.


#### E-posta Bildirimleri


Bir ödeme yapıldığında, BTCPay Sunucusu mağaza sahibini bilgilendirebilir.


#### Tarayıcı yönlendirmesi


Müşteri satın alma işlemini tamamladığında, mağaza sahibi tarafından ayarlanmışsa bu bağlantıya yönlendirilecektir.


#### Gelişmiş Ödeme Düğmesi Seçenekleri


Invoice oluşturulduktan sonra ödeme sayfasına eklenmesi gereken ek sorgu dizesi parametrelerini belirtin. Örneğin, `lang=da-DK` ödeme sayfasını varsayılan olarak Danca dilinde yükleyecektir.


#### Uygulamayı Uç Nokta Olarak Kullanın


Ödeme düğmesini, daha önce kullandığınız PoS veya Kitle Fonlaması uygulamalarından birindeki bir öğeye doğrudan bağlayabilirsiniz. Mağaza sahipleri açılır menüye tıklayabilir ve istedikleri uygulamayı seçebilir. Uygulama seçildikten sonra mağaza sahibi bağlanması gereken öğeyi ekleyebilir.


#### Oluşturulan Kod


BTCPay Server'ın Ödeme düğmesi kolayca gömülebilir bir HTML olduğundan, BTCPay Server, Ödeme düğmesini yapılandırdıktan sonra altta bir web sitesine kopyalamak için oluşturulan kodu gösterir. Mağaza sahipleri oluşturulan kodu web sitelerine kopyalayabilir ve BTCPay Server'dan Ödeme düğmesi doğrudan web sitelerinde aktif olur.


### Beceri Özeti


Bu bölümde şunları öğrendiniz:



- Kolayca özel bir mağaza oluşturmak için BTCPay Server'ın entegre PoS eklentisi nasıl kullanılır?
- Kolayca özel bir kitle fonlaması uygulaması oluşturmak için BTCPay Server'ın entegre Crowdfund eklentisi nasıl kullanılır?
- Pay Button eklentisini kullanarak özel bir ödeme düğmesi için kod oluşturma


### Bilgi değerlendirmesi


#### KA İnceleme


BTCPay Server ile standart olarak gelen üç yerleşik eklenti nedir? Birkaç kelimeyle, her birinin nasıl kullanılabileceğini açıklayın.


# BTCPay Sunucusunu Yapılandırma


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## LunaNode ortamına BTCPay Server kurulumu hakkında temel bilgi


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### BTCPay Sunucusunu Barındırılan Env. üzerine Kurma (LunaNode)


Bu adımlar, LunaNode üzerinde BTCPay Sunucusunu kullanmaya başlamak için gerekli tüm bilgileri sağlayacaktır. Yazılımı dağıtmak için birçok seçenek vardır.

BTCPay Sunucusu ile ilgili tüm detayları https://docs.btcpayserver.org adresinde bulabilirsiniz.


#### Nereden başlayacağız?


Bu bölümde, barındırma sağlayıcısı olarak LunaNode'u tanıyacak, BTCPay Sunucunuzu kullanmanın ilk adımlarını öğrenecek ve Lightning Network ile nasıl kullanılacağını öğreneceksiniz. Tüm adımları geçtikten sonra, Bitcoin kabul eden bir web mağazası veya kitle fonlaması platformu çalıştırabilirsiniz!


Bu, BTCPay Server'ı dağıtmanın birçok yolundan biridir. Daha fazla ayrıntı için belgelerimizi okuyun.


https://docs.btcpayserver.org.


### BTCPay Sunucusu - LunaNode dağıtımı


#### LunaNode dağıtımı


İlk olarak, yeni bir hesap oluşturacağımız LunaNode.com web sitesine gidin. Sağ üstteki Kaydol'a tıklayın veya ana sayfalarındaki Başlayın sihirbazını kullanın.


![image](assets/en/112.webp)


Yeni hesabınızı oluşturduktan sonra, LunaNode bir doğrulama e-postası gönderir. Hesabı doğruladıktan sonra, Voltage ile karşılaştırıldığında, hemen hesap bakiyenizi yükleme seçeneği sunulur. Bu bakiye, sunucu alanı ve barındırma maliyetlerini karşılamak için gereklidir.


![image](assets/en/113.webp)


#### LunaNode hesabınıza kredi ekleyin


"Kredi yatır" seçeneğine tıkladıktan sonra, hesabınıza ne kadar para yüklemek istediğinizi ve bunun için nasıl ödeme yapmak istediğinizi ayarlayabilirsiniz. LunaNode ve BTCPay Sunucusu aylık 10 ila 20 $ arasında bir ücrete mal olacaktır.

Voltage.cloud ile karşılaştırıldığında, Sanal Özel Sunucunuza (VPS) tam erişim elde edersiniz ve sunucunuz üzerinde daha fazla kontrole sahip olursunuz. Yeni hesabınızı oluşturduktan sonra LunaNode bir doğrulama e-postası gönderir.

Hesabı doğruladıktan sonra, Voltage ile karşılaştırıldığında, hemen hesap bakiyenizi yükleme seçeneği sunulur. Bu bakiye, sunucu alanı ve barındırma maliyetlerini karşılamak için gereklidir.


#### Yeni bir sunucu nasıl dağıtılır?


Bu kılavuzda, bir dizi API anahtarı oluşturarak ve LunaNode tarafından geliştirilen BTCPay Server başlatıcısını kullanarak kurulum sürecinde size yol göstereceğiz.


LunaNode kontrol panelinizde, sağ üstteki API'ye tıklayın. Bu yeni bir sayfa açar. API anahtarı için yalnızca bir Ad belirlememiz gerekiyor. Geri kalanı LunaNode tarafından halledilecek ve bu kılavuzda ele alınmayacaktır. API Kimlik Bilgisi Oluştur düğmesine tıklayın.

API kimlik bilgilerini oluşturduktan sonra, uzun bir harf ve karakter dizisi elde edersiniz. Bu sizin API anahtarınızdır.


![image](assets/en/114.webp)


#### Yeni bir sunucu nasıl dağıtılır?


Bu kimlik bilgilerinin API anahtarı ve API ID olmak üzere iki bölümü vardır; her ikisine de ihtiyacımız olacak. Bir sonraki adıma geçmeden önce, tarayıcıda ikinci bir sekme açalım ve https://launchbtcpay.lunanode.com/ adresine gidelim


Burada sizden API anahtarınızı ve API kimliğinizi girmeniz istenecektir. Bu, bu yeni sunucuyu sağlayan kişinin siz olduğunuzu bildirmek içindir. API anahtarı önceki sekmenizde hala açık olmalıdır; aşağıdaki tabloda aşağı kaydırırsanız API kimliğini bulacaksınız.


Başlatıcı'nın bulunduğu sayfaya geri dönebilir, API anahtarınız ve ID'niz ile alanları doldurabilir ve devam et'e tıklayabilirsiniz.


![image](assets/en/115.webp)


Bir sonraki adımda, bir alan adı sağlayabilirsiniz. Zaten bir alan adınız varsa ve bunu BTCPay Sunucusu için kullanmak istiyorsanız, alan adınıza DNS kaydını (`A` kaydı olarak adlandırılır) da eklediğinizden emin olun. Bir alan adınız yoksa, bunun yerine LunaNode tarafından sağlanan alan adını kullanın (bunu daha sonra BTCPay Server ayarlarından değiştirebilirsiniz) ve Devam'a tıklayın.


BTCPay Sunucusu için bir DNS kaydı ayarlama veya değiştirme hakkında daha fazla bilgi edinin; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### LunaNode üzerinde BTCPay Sunucusunu Başlatın


Önceki adımları uyguladıktan sonra, yeni sunucumuz için tüm seçenekleri ayarlayabiliriz. Burada, desteklenen para birimimiz olarak Bitcoin'ü (BTC) seçeceğiz. Ayrıca, isteğe bağlı olarak, yenileme amacıyla şifreleme sertifikaları hakkında bildirim almak için bir e-posta ayarlayabiliriz.


Bu kılavuz bir Mainnet ortamı (gerçek dünya Bitcoin) kurmayı amaçlamaktadır; ancak LunaNode, geliştirme amacıyla Testnet veya Regtest olarak ayarlamanıza da izin verir. Bu kılavuz için Mainnet seçeneğinde bırakacağız.


Lightning uygulamanızı seçebilirsiniz. LunaNode, LND ve Core Lightning olmak üzere iki farklı uygulama sunar. Bu kılavuz için LND'i ele alacağız. Her iki uygulamada da az ama gerçek farklılıklar vardır; bu konuda daha fazla bilgi için kapsamlı belgeleri okumanızı öneririz: https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/116.webp)


LunaNode birden fazla Sanal Makine (VM) planı sunar. Bunlar fiyat aralığı ve sunucu özellikleri açısından farklılık gösterir. Bu kılavuz için m2 planı yeterli olacaktır; ancak para birimi olarak Bitcoin'dan daha fazlasını seçtiyseniz en az m4 kullanmayı düşünün.


İlk Blockchain senkronizasyonunu hızlandırın; bu isteğe bağlıdır ve ihtiyaçlarınıza bağlıdır. Lightning Takma Adı belirleme, belirli bir GitHub sürümüne işaret etme veya SSH anahtarlarını ayarlama gibi gelişmiş seçenekler vardır; bunların hiçbiri bu kılavuzda ele alınmayacaktır.


Formu doldurduktan sonra Launch VM'ye tıklamanız gerekir ve Lunanode, üzerinde BTCPay Server kurulu olan yeni VM'nizi oluşturmaya başlayacaktır. Bu işlem birkaç dakika sürer; sunucunuz hazır olduğunda, LunaNode size yeni BTCPay Sunucunuzun bağlantısını verir.


Oluşturma işleminden sonra, BTCPay Sunucunuzun bağlantısına tıklayın; burada bir Yönetici hesabı oluşturmanız istenecektir.


![image](assets/en/117.webp)


### Beceri Özeti


Bu bölümde şunları öğrendiniz:



- LunaNode'da bir hesap oluşturma ve finanse etme
- Kendi sunucunuzu oluşturmak için BTCPay Sunucu Başlatıcısını kullanma


### Bilgi değerlendirmesi


#### KA Kavramsal İnceleme


BTCPay Server'ın bir örneğini VPS üzerinde çalıştırmak ile barındırılan bir örnek üzerinde hesap oluşturmak arasındaki bazı farkları açıklayın.


## BTCPay Sunucusunu bir Voltaj ortamına yükleme


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


Hosting sağlayıcısı olarak Voltage.cloud'u tanıyacak, BTCPay Sunucunuzu kullanmanın ilk adımlarını öğrenecek ve Lightning Network'i nasıl kullanacağınızı öğreneceksiniz. Tüm adımları geçtikten sonra, Bitcoin kabul eden bir web mağazası veya kitle fonlaması platformu çalıştırabilirsiniz!


Bu, BTCPay Server'ı dağıtmanın birçok yolundan biridir. Daha fazla ayrıntı için belgelerimizi okuyun.

https://docs.btcpayserver.org.


### BTCPay Sunucusu - Voltage.cloud dağıtımı


İlk olarak, Voltage.cloud web sitesine gidin ve yeni bir hesap için kaydolun. Bir hesap oluştururken, 7 günlük ücretsiz deneme için kaydolabilirsiniz. Ya sağ üstteki Kaydol'a tıklayın ya da ana sayfadaki "7 günlük ücretsiz deneme sürümünü deneyin" seçeneğini kullanın.


![image](assets/en/118.webp)


Bir hesap oluşturduktan sonra, kontrol panelinizdeki `NODES` düğmesine tıklayın. Düğümler'i seçtikten ve yeni bir düğüm oluşturduktan sonra, olası düğümlerin Voltage teklifleri bize sunulur. Bu kılavuz Lightning Network'ü de kapsayacağından, Voltage'da bir BTCPay Sunucusu oluşturmadan önce Lightning uygulamamızı seçmemiz gerekiyor. LightningNode üzerine tıklayın.


![image](assets/en/119.webp)


Burada, ne tür bir Yıldırım düğümü istediğinizi seçmeniz gerekecektir. Voltage, aydınlatma kurulumunuz için çeşitli seçeneklere sahiptir. Bu, örneğin LunaNode ile dağıtım yaparken farklıdır. Bu kılavuzun amacı için bir Lite Node yeterli olacaktır. Voltage.cloud'daki farklılıklar hakkında daha fazla bilgi edinin.


![image](assets/en/120.webp)


Düğümünüze bir Ad verin, bir parola belirleyin ve bu parolayı güvence altına alın. Bu parola kaybolursa, yedeklerinize erişiminizi kaybedersiniz ve Voltage bunu kurtaramaz. Düğümü oluşturun ve Voltage size ilerlemeyi gösterir. Voltage Lightning Node'unuzu oluşturdu. Artık BTCPay Sunucu örneğini oluşturabilir ve Lightning Network'e doğrudan erişebiliriz.


Kontrol panelinizin sol üst köşesindeki Düğümler'e tıklayın. Burada BTCPay Sunucu örneğinizin bir sonraki bölümünü ayarlayabilirsiniz. Düğümlere genel bakışa geldiğinizde "yeni oluştur" seçeneğine tıklayın. Daha önce olduğu gibi benzer bir ekran elde edersiniz. Şimdi, Lightning Node yerine BTCPay Server'ı seçiyoruz.


Voltaj size ABD Batı bölgesinde barındırılan BTCPay Sunucunuzun coğrafi konumunu gösterir. Burada ayrıca sunucuyu barındırmanın maliyetini de göreceksiniz. Oluştur'a tıklayın ve BTCPay Sunucunuza bir ad verin. Lightning'i etkinleştirin ve Voltage size önceki adımda oluşturulan Lightning düğümünü gösterir. Oluştur'a tıklayın ve Voltage bir BTCPay Sunucu örneği oluşturacaktır.


![image](assets/en/121.webp)


Oluştur düğmesine bastıktan sonra, Voltage size varsayılan kullanıcı adı ve şifreyi sunar. Bunlar, Voltage'da daha önce belirlediğiniz parolaya benzer. Sizi BTCPay Sunucunuza yönlendirmek için Hesaba Giriş düğmesine tıklayın.


Yeni BTCPay Sunucu örneğinize hoş geldiniz. Oluşturma sürecinde Lightning'i zaten kurduğumuz için, Lightning'in zaten etkin olduğunu gösteriyor!


### Beceri Özeti


Bu bölümde şunları öğrendiniz:



- Voltage.cloud'da bir hesap oluşturma
- BTCPay Sunucusunu hesapta bir Lightning düğümü ile birlikte çalıştırmak için adımlar


### Bilgi değerlendirmesi


#### KA Kavramsal İnceleme


Voltage ve LunaNode kurulumları arasındaki bazı temel farklar nelerdir?


## BTCPay Sunucusunu bir Umbrel düğümüne yükleme


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


Bu adımların sonunda, yerel ağınızdaki BTCPay mağazanıza yıldırım ödemelerini kabul edebilirsiniz. Bu işlem, bir restoran veya işletmede bir umbrel düğümü çalıştırıyorsanız da geçerli olacaktır. Bu mağazayı herkese açık bir web sitesine bağlamak istiyorsanız, umbrel düğümünüzü herkese açık hale getirmek için Gelişmiş alıştırmayı izleyin.


https://umbrel.com/


![image](assets/en/122.webp)


### BTCPay Sunucusu - Umbrel dağıtımı


Umbrel düğümünüz Bitcoin Blockchain ile tamamen senkronize olduktan sonra, Umbrel Uygulama Mağazasına gidin ve Uygulamalar altında BTCPay Sunucusunu arayın.


![image](assets/en/123.webp)


Uygulama ayrıntılarını görmek için BTCPay Server'a tıklayın. BTCPay Sunucusunun ayrıntıları açıkken, sağ alt köşede Uygulamanın düzgün çalışması için gerekenler gösterilir. Bir Bitcoin ve Lightning düğümü gerektirdiğini gösterir. Lightning Node'u Umbrel'inize yüklemediyseniz, Yükle'ye tıklayın. Bu işlem birkaç dakika sürebilir.


![image](assets/en/124.webp)


Lightning Node'unuzu yükledikten sonra:


1. Uygulama ayrıntılarında veya Umbrels kontrol panelindeki Uygulamada aç'a tıklayın.

2. Yeni bir düğüm kur seçeneğine tıklayın; yıldırım düğümünüzün kurtarılması için 24 kelime gösterilecektir.

3. Bunları yaz.


![image](assets/en/125.webp)


Umbrel, az önce yazılan kelimelerin doğrulanmasını isteyecektir. Lightning düğümü kurulduktan sonra Umbrel App Store'a dönün ve BTCPay Server'ı bulun. Yükle düğmesine tıklayın ve Umbrel gerekli bileşenlerin yüklü olup olmadığını ve BTCPay Server'ın bu bileşenlere erişim gerektirdiğini gösterecektir. Kurulumdan sonra, Uygulama ayrıntılarının sağ üst kısmındaki Aç'a tıklayın veya Umbrels kontrol paneliniz aracılığıyla BTCPay Server'ı açın.


Umbrel, az önce yazılan kelimelerin doğrulanmasını isteyecektir.


![image](assets/en/126.webp)


**!Not!**


Anahtarları saklarken daha önce öğrendiğiniz gibi bunları da güvenli bir yerde sakladığınızdan emin olun.


Lightning düğümü kurulduktan sonra Umbrel App Store'a dönün ve BTCPay Server'ı bulun. Yükle düğmesine tıklayın ve Umbrel, gerekli bileşenlerin yüklü olup olmadığını ve BTCPay Server'ın bu bileşenlere erişim gerektirdiğini gösterecektir.


![image](assets/en/127.webp)


Kurulumdan sonra, Uygulama ayrıntılarının sağ üst köşesindeki Aç'a tıklayın veya Umbrels kontrol panelinizden BTCPay Sunucusunu açın.


![image](assets/en/128.webp)


### Beceri Özeti


Bu bölümde şunları öğrendiniz:



- Bir Umbrel düğümüne Lightning işlevselliğine sahip BTCPay Sunucusunu yükleme adımları


### Bilgi değerlendirmesi


#### KA Kavramsal İnceleme


Umbrel'deki kurulumun önceki iki barındırma seçeneğinden farkı nedir?


# Son Bölüm


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Yorumlar & Derecelendirmeler

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Kurs Sonucu


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>