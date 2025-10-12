---
name: Modern kriptografinin temelleri
goal: Kriptografi bilimine ve uygulamasına derinlemesine bir giriş.
objectives:
- Kriptografinin temel ve tarihsel kavramlarını anlamak için Beale şifrelerini ve modern kriptografik yöntemleri keşfedin.
- Kriptografinin altında yatan temel matematiksel kavramlarda ustalaşmak için sayı teorisi, gruplar ve alanları inceleyin.
- Simetrik kriptografik algoritmalar hakkında bilgi edinmek için RC4 akış şifresini ve 128 bit anahtarlı AES'yi inceleyin.
- Asimetrik kriptografiyi keşfetmek için RSA kriptosistemini, anahtar dağıtımını ve Hash işlevlerini inceleyin.
---
# Modern Kriptografiye Derinlemesine Bakış

Bu kursta, modern kriptografinin temellerini ağır bir matematik geçmişi gerektirmeden açık ve anlaşılır bir şekilde ele alacağız. Bölümler boyunca, simetrik ve açık anahtarlı şifreleme, hash fonksiyonları, dijital imzalar, anahtar değişimi ve gerçek dünya protokolleri gibi temel fikirleri öğreneceksiniz. Bu süreçte, güvenli mesajlaşma, TLS, parola depolama ve kimlik doğrulama gibi pratik uygulamalarla noktaları birleştireceğiz.

Materyal, her seviyeden öğrenci için tasarlanmıştır ve sezgiyi merakı tatmin edecek kadar teknik derinlikle dengeler. Odaklanmış, ilgi çekici bir yolculuk bekleyin. Sonunda, modern kriptografinin nasıl ve neden çalıştığını ve onu sorumlu bir şekilde nasıl kullanacağınızı anlayacaksınız.
+++
# Giriş

<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>


## Kursa genel bakış

<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

CYP302 kursuna hoş geldiniz!


Bu kitap kriptografi bilimine ve uygulamasına derinlemesine bir giriş sunmaktadır. Mümkün olan yerlerde, materyalin biçimsel olarak açıklanmasından ziyade kavramsal olarak açıklanmasına odaklanmaktadır.


Bu eğitim içeriği [JWBurgers] (https://github.com/JWBurgers/An_Introduction_to_Cryptography) kitabından ve reposundan uyarlanmıştır. Yazar, eğitim amaçlı kullanımına nezaketen izin vermiş olsa da, tüm fikri mülkiyet hakları orijinal yaratıcıya aittir.


**Motivasyon ve hedefler**


Kriptografi eğitiminde iyi bir orta yol sunan çok sayıda materyal bulmak zordur.


Bir yanda, sadece matematik, mantık veya diğer bazı resmi disiplinlerde güçlü bir geçmişe sahip olanların gerçekten erişebileceği uzun, resmi incelemeler var. Öte yandan, en azından biraz meraklı olan herkes için gerçekten çok fazla ayrıntıyı gizleyen çok üst düzey tanıtımlar var.


Kriptografiye giriş niteliğindeki bu kitap orta yolu yakalamayı amaçlamaktadır. Kriptografiye yeni başlayanlar için nispeten zorlayıcı ve ayrıntılı olsa da, tipik bir temel incelemenin tavşan deliği değildir.



**Hedef kitle**


Geliştiricilerden entelektüel meraklılara kadar, bu kitap kriptografi hakkında yüzeysel bir anlayıştan daha fazlasını isteyen herkes için yararlıdır. Amacınız kriptografi alanında uzmanlaşmaksa, bu kitap aynı zamanda iyi bir başlangıç noktasıdır.



**Okuma yönergeleri**


Kitap şu anda yedi bölümden oluşmaktadır: "Kriptografi Nedir?" (Bölüm 1), "Kriptografinin Matematiksel Temelleri I" (Bölüm 2), "Kriptografinin Matematiksel Temelleri II" (Bölüm 3), "Simetrik Kriptografi" (Bölüm 4), "RC4 ve AES" (Bölüm 5), "Asimetrik Kriptografi" (Bölüm 6) ve "RSA Kriptosistemi" (Bölüm 7). "Uygulamada Kriptografi" başlıklı son bir bölüm daha eklenecektir. Bu bölüm, Layer taşıma güvenliği, soğan yönlendirme ve Bitcoin'nin değeri Exchange sistemi dahil olmak üzere çeşitli kriptografik uygulamalara odaklanmaktadır.


Matematikte güçlü bir geçmişiniz yoksa, sayı teorisi muhtemelen bu kitaptaki en zor konudur. Bölüm 3'te genel bir bakış sunuyorum ve ayrıca Bölüm 5'te AES'in ve Bölüm 7'de RSA kriptosisteminin açıklanmasında da yer alıyor.


Kitabın bu bölümlerindeki biçimsel ayrıntılarla gerçekten zorlanıyorsanız, ilk seferde üst düzey bir okumayla yetinmenizi tavsiye ederim.



**Teşekkür**


Bu kitabın şekillenmesinde en etkili kitap Jonathan Katz ve Yehuda Lindell'in _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL), 2015 adlı kitabı olmuştur. Bu kitaba eşlik eden bir kurs da Coursera'da "Cryptography" adıyla mevcuttur


Bu kitaptaki genel bakışın oluşturulmasında yardımcı olan başlıca ek kaynaklar Simon Singh, _The Code Book_, Fourth Estate (Londra, 1999); Christof Paar ve Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) ve [Paar'ın "Introduction to Cryptography" adlı kitabına dayanan bir kurs] (https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); ve Bruce Schneier, Applied Cryptography, 2nd edn, 2015 (Indianapolis, IN: John Wiley & Sons).


Bu kaynaklardan aldığım çok spesifik bilgi ve sonuçlara sadece atıfta bulunacağım, ancak burada onlara olan genel borçluluğumu kabul etmek istiyorum.


Bu girişten sonra kriptografi hakkında daha ileri düzeyde bilgi edinmek isteyen okuyucular için Katz ve Lindell'in kitabını şiddetle tavsiye ederim. Katz'ın Coursera'daki kursu kitaba göre biraz daha erişilebilir.



**Katkılar**


Projeyi nasıl destekleyeceğinize dair bazı yönergeler için lütfen [depodaki katkı dosyasına] (https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) bir göz atın.



**Not**


**Anahtar terimler:**


Primerlerdeki anahtar terimler kalın yazılarak tanıtılır. Örneğin, Rijndael şifresinin bir anahtar terim olarak tanıtımı aşağıdaki gibi olacaktır: **Rijndael şifresi**.


Özel isimler olmadıkça veya anlamları tartışmadan açıkça anlaşılmadıkça, anahtar terimler açıkça tanımlanmıştır.


Herhangi bir tanım genellikle anahtar bir terimin girişinde verilir, ancak bazen tanımı daha sonraki bir noktaya bırakmak daha uygun olabilir.



**Vurgulanan kelimeler ve ifadeler:**


Kelimeler ve ifadeler italik olarak vurgulanır. Örneğin, "Parolanızı hatırlayın" ifadesi aşağıdaki gibi görünecektir: *Şifrenizi hatırlayın*.



**Resmi notasyon:**


Resmi gösterim temel olarak değişkenler, rastgele değişkenler ve kümelerle ilgilidir.



- Değişkenler: Bunlar genellikle sadece küçük harfle gösterilir (örn. "x" veya "y"). Bazen anlaşılır olmaları için büyük harfle yazılırlar (örn. "M" veya "K").
- Rastgele değişkenler: Bunlar her zaman büyük harfle gösterilir (örneğin, "X" veya "Y")
- Setler: Bunlar her zaman kalın, büyük harflerle gösterilir (örneğin, **S**)


Kriptografinin büyüleyici dünyasını keşfetmeye hazır mısınız? Hadi başlayalım!


# Kriptografi Nedir?

<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>


## Beale şifreleri

<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>


Kriptografi alanındaki incelememize, tarihindeki en çekici ve eğlenceli bölümlerden biriyle başlayalım: Beale şifreleri. [1]


Beale şifrelerinin hikayesi bana göre gerçek olmaktan ziyade kurgu olma olasılığı daha yüksektir. Ancak sözde olay şu şekilde gerçekleşmiştir.


Thomas J. Beale adında bir adam 1820 ve 1822 kışlarında Lynchburg'da (Virginia) Robert Morriss'e ait bir handa kalmıştır. Beale ikinci kalışının sonunda Morriss'e saklaması için içinde değerli evraklar bulunan demir bir kutu verdi.


Birkaç ay sonra Morriss, Beale'den 9 Mayıs 1822 tarihli bir mektup aldı. Mektupta demir kutunun içindekilerin büyük değeri vurgulanıyor ve Morriss'e bazı talimatlar veriliyordu: Beale ya da ortaklarından herhangi biri kutuyu almaya gelmezse, mektubun tarihinden tam on yıl sonra (yani 9 Mayıs 1832'de) açacaktı. İçindeki kağıtlardan bazıları normal metinle yazılmış olacaktı. Ancak diğer bazıları "bir anahtarın yardımı olmadan anlaşılmaz" olacaktı Bu "anahtar", Beale'in adı belirtilmeyen bir arkadaşı tarafından 1832 yılının Haziran ayında Morriss'e teslim edilir.


Açık talimatlara rağmen Morriss 1832 yılının Mayıs ayında kutuyu açmadı ve Beale'in gizemli arkadaşı da aynı yılın Haziran ayında bir daha ortaya çıkmadı. Hancı nihayet 1845 yılına kadar kutuyu açmaya karar verdi. Morriss kutuda, Beale ve arkadaşlarının Batı'da nasıl altın ve gümüş bulduklarını ve bunları bazı mücevherlerle birlikte saklamak üzere gömdüklerini açıklayan bir not buldu. Kutuda ayrıca üç **şifre metni** vardı: yani, açılması için bir **kriptografik anahtar** ya da bir sır ve buna eşlik eden bir algoritma gerektiren kodla yazılmış metinler. Bir Ģifreli metnin kilidini açma iĢlemi **Ģifre çözme**, kilitleme iĢlemi ise **Ģifreleme** olarak bilinir. (Bölüm 3'te açıklandığı gibi, Ģifre terimi çeĢitli anlamlara gelebilir. "Beale şifreleri" adında, şifreli metinlerin kısaltmasıdır)


Morriss'in demir kutuda bulduğu üç şifre metninin her biri virgüllerle ayrılmış bir dizi rakamdan oluşmaktadır. Beale'in notuna göre, bu şifreli metinler ayrı ayrı hazinenin yerini, hazinenin içindekileri ve hazinenin yasal varisleri ile paylarını içeren bir isim listesi vermektedir (Beale ve ortaklarının kutuyu almaya hiç gelmemeleri durumunda ikinci bilgi önemlidir).


Morris yirmi yıl boyunca üç şifre metninin şifresini çözmeye çalıştı. Anahtar olsaydı bu çok kolay olurdu. Ancak Morriss anahtara sahip değildi ve orijinal metinleri ya da kriptografide tipik olarak adlandırıldıkları şekliyle **düz metinleri** kurtarma girişimlerinde başarısız oldu.


Hayatının sonuna yaklaşan Morriss, 1862 yılında kutuyu bir arkadaşına verdi. Bu arkadaşı daha sonra 1885 yılında J.B. Ward takma adıyla bir broşür yayınladı. Bu broşürde kutunun (sözde) tarihçesi, üç şifre metni ve ikinci şifre metni için bulduğu bir çözüm yer alıyordu. (Görünüşe göre, Beale'in Morriss'e yazdığı mektupta önerdiği gibi üç şifre metninde de çalışan tek bir anahtar değil, her şifre metni için bir anahtar vardır)


İkinci şifre metnini aşağıdaki *Şekil 2*'de görebilirsiniz. [2] Bu şifreli metnin anahtarı Birleşik Devletler Bağımsızlık Bildirgesi'dir. Şifre çözme prosedürü aşağıdaki iki kuralı uygulamaktan ibarettir:



- Şifreli metindeki herhangi bir n sayısı için, Birleşik Devletler Bağımsızlık Bildirgesi'ndeki n'inci kelimeyi bulun
- N rakamını bulduğunuz kelimenin ilk harfi ile değiştirin



*Şekil 1: Beale şifreleme no. 2*


![Figure 1: Beale cipher no 2.](assets/Figure1-1.webp "Figure 1: Beale cipher no. 2")



Örneğin, ikinci şifreli metnin ilk sayısı 115'tir. Bağımsızlık Bildirgesi'nin 115. kelimesi "instituted "dır, dolayısıyla düz metnin ilk harfi "i "dir Şifreli metin kelime aralıklarını ve büyük harf kullanımını doğrudan belirtmez. Ancak ilk birkaç kelimenin şifresini çözdükten sonra, mantıksal olarak düz metnin ilk kelimesinin basitçe "I" olduğu sonucuna varabilirsiniz (Düz metin "Bedford ilçesine yatırdım" ifadesiyle başlar.)


Şifre çözüldükten sonra, ikinci mesaj hazinenin ayrıntılı içeriğini (altın, gümüş ve mücevherler) verir ve Bedford County'de (Virginia) demir kaplara gömüldüğünü ve kayalarla örtüldüğünü öne sürer. İnsanlar iyi bir gizemi severler, bu nedenle diğer iki Beale şifresinin, özellikle de hazinenin yerini tarif edenin şifresini çözmek için büyük çaba sarf edilmiştir. Hatta çeşitli tanınmış kriptograflar bile bu şifreler üzerinde çalışmışlardır. Ancak henüz hiç kimse diğer iki şifre metninin şifresini çözmeyi başaramamıştır.



**Notlar:**


[1] Hikayenin iyi bir özeti için bakınız Simon Singh, *The Code Book*, Fourth Estate (Londra, 1999), s. 82-99. Hikayenin kısa bir filmi 2010 yılında Andrew Allen tarafından yapılmıştır. "The Thomas Beale Cipher" adlı filmi [web sitesinde] bulabilirsiniz (http://www.thomasbealecipher.com/).


[2] Bu resim Beale şifreleri için Wikipedia sayfasında mevcuttur.



## Modern kriptografi

<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>


Beale şifreleri gibi renkli hikayeler çoğumuzun kriptografi ile ilişkilendirdiği şeylerdir. Ancak modern kriptografi bu tür tarihi örneklerden en az dört önemli açıdan farklılık gösterir.


İlk olarak, tarihsel olarak kriptografi yalnızca **gizlilik** (veya gizlilik) ile ilgilenmiştir. [3] Şifre metinleri, Beale şifrelerinde olduğu gibi, düz metinlerdeki bilgilere yalnızca belirli tarafların erişebilmesini sağlamak için oluşturulur. Bir şifreleme şemasının bu amaca iyi bir şekilde hizmet edebilmesi için, şifreli metnin şifresini çözmek yalnızca anahtara sahipseniz mümkün olmalıdır.


Modern kriptografi, gizlilikten daha geniş bir yelpazedeki konularla ilgilenir. Bu temalar öncelikle (1) **mesaj bütünlüğü**, yani bir mesajın değiştirilmediğinden emin olunması; (2) **mesaj gerçekliği**, yani bir mesajın gerçekten belirli bir göndericiden geldiğinden emin olunması; ve (3) **inkar edilemezlik**, yani bir göndericinin daha sonra bir mesaj gönderdiğini yanlış bir şekilde inkar edemeyeceğinden emin olunması. [4]


Bu nedenle, akılda tutulması gereken önemli bir ayrım, bir **şifreleme şeması** ile bir **kriptografik şema** arasındadır. Bir şifreleme şeması sadece gizlilikle ilgilidir. Bir şifreleme şeması bir kriptografik şema olsa da, bunun tersi doğru değildir. Bir kriptografik şema, bütünlük, orijinallik ve inkar etmeme gibi kriptografinin diğer ana temalarına da hizmet edebilir.


Bütünlük ve orijinallik temaları gizlilik kadar önemlidir. Modern iletişim sistemlerimiz, iletişimin bütünlüğü ve gerçekliği ile ilgili garantiler olmadan çalışamazdı. Dijital sözleşmelerde olduğu gibi inkar etmeme de önemli bir konudur, ancak kriptografik uygulamalarda gizlilik, bütünlük ve özgünlükten daha az yaygın olarak ihtiyaç duyulmaktadır.


İkinci olarak, Beale şifreleri gibi klasik şifreleme şemaları her zaman ilgili tüm taraflar arasında paylaşılan tek bir anahtar içerir. Bununla birlikte, birçok modern şifreleme şeması sadece bir değil, iki anahtar içerir: bir **özel** ve bir **açık anahtar**. Birincisi herhangi bir uygulamada gizli kalması gerekirken, ikincisi tipik olarak kamuya açıktır (dolayısıyla, ilgili isimleri). Şifreleme alanında, açık anahtar mesajı şifrelemek için kullanılabilirken, özel anahtar şifre çözme için kullanılabilir.


Tüm tarafların tek bir anahtarı paylaştığı şemalarla ilgilenen kriptografi dalı **simetrik kriptografi** olarak bilinir. Böyle bir şemadaki tek anahtara genellikle **özel anahtar** (veya gizli anahtar) denir. Kriptografinin özel-açık anahtar çifti gerektiren şemalarla ilgilenen dalı **asimetrik kriptografi** olarak bilinir. Bu dallar bazen sırasıyla **özel anahtar kriptografisi** ve **açık anahtar kriptografisi** olarak da adlandırılır (ancak açık anahtarlı kriptografik şemaların da özel anahtarları olduğu için bu karışıklığa neden olabilir).


1970'lerin sonlarında asimetrik kriptografinin ortaya çıkışı kriptografi tarihindeki en önemli olaylardan biri olmuştur. Bu olmadan, Bitcoin de dahil olmak üzere modern iletişim sistemlerimizin çoğu mümkün olmazdı ya da en azından çok pratik olmazdı.


Daha da önemlisi, modern kriptografi yalnızca simetrik ve asimetrik anahtarlı kriptografik şemaların incelenmesi değildir (bu alanın büyük bir kısmını kapsasa da). Örneğin, kriptografi aynı zamanda Hash fonksiyonları ve sözde rastgele sayı üreteçleri ile de ilgilidir ve bu ilkeller üzerine simetrik veya asimetrik anahtar kriptografisi ile ilgili olmayan uygulamalar geliştirebilirsiniz.


Üçüncü olarak, Beale şifrelerinde kullanılanlar gibi klasik şifreleme şemaları bilimden çok sanattı. Algılanan güvenlikleri büyük ölçüde karmaşıklıklarına ilişkin sezgilere dayanıyordu. Genellikle yeni bir saldırı öğrenildiğinde yamalanırlar ya da saldırı özellikle şiddetliyse tamamen bırakılırlardı. Ancak modern kriptografi, kriptografik şemaların hem geliştirilmesi hem de analiz edilmesine yönelik resmi, matematiksel bir yaklaşıma sahip titiz bir bilimdir. [5]


Özellikle, modern kriptografi resmi **güvenlik kanıtları** üzerine odaklanır. Bir kriptografik şema için herhangi bir güvenlik kanıtı üç adımda ilerler:


1.	Bir **kriptografik güvenlik tanımı**, yani bir dizi güvenlik hedefi ve saldırganın oluşturduğu tehdidin ifadesi.

2.	Şemanın hesaplama karmaşıklığı ile ilgili matematiksel varsayımların beyanı. Örneğin, bir kriptografik şema bir sözde rastgele sayı üreteci içerebilir. Bunların var olduğunu kanıtlayamasak da var olduğunu varsayabiliriz.

3.	Formel güvenlik kavramı ve herhangi bir matematiksel varsayım temelinde şemanın matematiksel **güvenlik** kanıtının açıklanması.


Dördüncüsü, kriptografi tarihsel olarak öncelikle askeri ortamlarda kullanılmış olsa da, dijital çağda günlük faaliyetlerimize nüfuz etmeye başlamıştır. İster online bankacılık yapıyor, ister sosyal medyada paylaşımlarda bulunuyor, ister kredi kartınızla Amazon'dan bir ürün satın alıyor ya da bir arkadaşınıza Bitcoin bahşiş veriyor olun, kriptografi dijital çağımızın olmazsa olmazıdır.


Modern kriptografinin bu dört yönü göz önüne alındığında, modern **kriptografiyi** dijital bilgiyi düşman saldırılarına karşı güvence altına almak için kriptografik şemaların resmi gelişimi ve analizi ile ilgilenen bilim olarak nitelendirebiliriz. [6] Buradaki güvenlik, iletişimde gizliliğe, bütünlüğe, kimlik doğrulamaya ve/veya inkar edilemezliğe zarar veren saldırıların önlenmesi olarak geniş bir şekilde anlaşılmalıdır.


Kriptografi en iyi şekilde bilgisayar sistemlerinin çalınmasını, zarar görmesini ve kötüye kullanılmasını önlemekle ilgilenen **siber güvenliğin** bir alt disiplini olarak görülür. Birçok siber güvenlik sorununun kriptografi ile çok az ya da sadece kısmi bir bağlantısı olduğunu unutmayın.


Örneğin, bir şirket pahalı sunucuları yerel olarak barındırıyorsa, bu donanımın hırsızlığa ve hasara karşı güvenliğini sağlamakla ilgilenebilir. Bu bir siber güvenlik endişesi olsa da kriptografi ile pek ilgisi yoktur.


Başka bir örnek vermek gerekirse, **phishing saldırıları** modern çağımızda yaygın bir sorundur. Bu saldırılar insanları bir e-posta ya da başka bir mesaj aracılığı ile kandırarak parola ya da kredi kartı numarası gibi hassas bilgilerden vazgeçmelerini sağlamaya çalışır. Kriptografi Address oltalama saldırılarına belli bir dereceye kadar yardımcı olabilirken, kapsamlı bir yaklaşım sadece biraz kriptografi kullanmaktan daha fazlasını gerektirir.



**Notlar:**


[3] Tam olarak söylemek gerekirse, kriptografik şemaların önemli uygulamaları gizlilikle ilgilidir. Örneğin çocuklar basit kriptografik şemaları sıklıkla "eğlence" için kullanırlar. Bu gibi durumlarda gizlilik gerçekten bir endişe kaynağı değildir.


[4] Bruce Schneier, *Applied Cryptography*, 2nd edn, 2015 (Indianapolis, IN: John Wiley & Sons), s. 2.


[5] İyi bir açıklama için Jonathan Katz ve Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), özellikle s. 16-23'e bakınız.


[6] Katz ve Lindell, a.g.e., s. 3. Onların tanımlamasının bazı sorunları olduğunu düşünüyorum, bu nedenle burada ifadelerinin biraz farklı bir versiyonunu sunuyorum.



## Açık iletişim

<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>


Modern kriptografi **açık iletişim** ortamında güvenlik güvencesi sağlamak üzere tasarlanmıştır. Eğer iletişim kanalımız, dinleyicilerin mesajlarımızı manipüle etme ya da sadece gözlemleme şansının olmadığı kadar iyi korunuyorsa, o zaman kriptografi gereksizdir. Ancak iletişim kanallarımızın çoğunun bu kadar iyi korunduğu söylenemez.


Modern dünyada iletişimin belkemiğini fiber optik kablolardan oluşan devasa bir ağ oluşturmaktadır. Modern bir evde telefon görüşmeleri yapmak, televizyon izlemek ve internette gezinmek genellikle bu fiber optik kablo ağına dayanır (küçük bir yüzde tamamen uydulara dayanabilir). Evinizde koaksiyel kablo, (asimetrik) dijital abone hattı ve fiber optik kablo gibi farklı veri bağlantıları olabileceği doğrudur. Ancak, en azından gelişmiş dünyada, bu farklı veri ortamları evinizin dışında tüm dünyayı birbirine bağlayan devasa bir fiber optik kablo ağındaki bir düğüme hızlı bir şekilde bağlanır. Bunun istisnaları, veri trafiğinin hala geleneksel bakır telefon kabloları üzerinden önemli mesafeler kat edebildiği Amerika Birleşik Devletleri ve Avustralya gibi gelişmiş dünyanın bazı uzak bölgeleridir.


Potansiyel saldırganların bu kablo ağına ve onu destekleyen altyapıya fiziksel olarak erişmesini engellemek imkansız olacaktır. Aslında, verilerimizin çoğunun çeşitli ulusal istihbarat kurumları tarafından İnternet'in önemli kavşaklarında ele geçirildiğini zaten biliyoruz.[7] Buna Facebook mesajlarından ziyaret ettiğiniz web sitesi adreslerine kadar her şey dahildir.


Verileri büyük ölçekte gözetlemek için ulusal istihbarat teşkilatı gibi güçlü bir düşman gerekirken, yalnızca birkaç kaynağa sahip saldırganlar kolayca daha yerel ölçekte casusluk yapmaya çalışabilir. Bu, kabloları dinleme düzeyinde gerçekleşebilse de, kablosuz iletişimleri engellemek çok daha kolaydır.


İster evimizde, ister ofisimizde ya da bir kafede olsun, yerel ağ verilerimizin çoğu artık fiziksel kablolar yerine radyo dalgaları aracılığıyla hepsi bir arada yönlendiricilerdeki kablosuz erişim noktalarına ulaşıyor. Dolayısıyla bir saldırganın yerel trafiğinizi ele geçirmek için çok az kaynağa ihtiyacı vardır. Çoğu insan yerel ağlarında dolaşan verileri korumak için çok az şey yaptığı için bu durum özellikle endişe vericidir. Buna ek olarak, potansiyel saldırganlar 3G, 4G ve 5G gibi mobil geniş bant bağlantılarımızı da hedef alabilirler. Tüm bu kablosuz iletişimler saldırganlar için kolay bir hedeftir.


Bu nedenle, iletişim kanalını koruyarak iletişimi gizli tutma fikri, modern dünyanın büyük bir kısmı için umutsuzca hayalperest bir istektir. Bildiğimiz her şey ciddi bir paranoya gerektiriyor: her zaman birilerinin sizi dinlediğini varsaymalısınız. Ve kriptografi bu modern ortamda her türlü güvenliği elde etmek için sahip olduğumuz ana araçtır.



**Notlar:**


[7] Bkz. örneğin Olga Khazan, "The creepy, long-standing practice of undersea cable tapping", *The Atlantic*, 16 Temmuz 2013 ([The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/) adresinden erişilebilir).



# Kriptografinin Matematiksel Temelleri 1

<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>



## Rastgele değişkenler

<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>


Kriptografi matematiğe dayanır. Ve kriptografi hakkında yüzeysel bir anlayıştan daha fazlasını inşa etmek istiyorsanız, bu matematik konusunda rahat olmanız gerekir.


Bu bölüm kriptografi öğrenirken karşılaşacağınız temel matematiğin çoğunu tanıtır. Konular arasında rastgele değişkenler, modulo işlemleri, XOR işlemleri ve sözde rastgelelik yer almaktadır. Kriptografiyi yüzeysel olmayan bir şekilde anlamak için bu bölümlerdeki materyallere hakim olmalısınız.


Bir sonraki bölüm çok daha zorlu olan sayı teorisi ile ilgilidir.


### Rastgele değişkenler


Bir rastgele değişken tipik olarak kalın olmayan, büyük bir harfle gösterilir. Örneğin, $X$ rastgele değişkeninden, $Y$ rastgele değişkeninden veya $Z$ rastgele değişkeninden bahsedebiliriz. Ben de bundan sonra bu gösterimi kullanacağım.


Bir **rastgele değişken**, her biri belirli bir pozitif olasılığa sahip iki veya daha fazla olası değer alabilir. Olası değerler **sonuç kümesinde** listelenir.


Bir rastgele değişkeni her **örneklediğinizde**, tanımlanmış olasılıklara göre sonuç kümesinden belirli bir değer çekersiniz.


Basit bir örneğe dönelim. Aşağıdaki gibi tanımlanmış bir X değişkeni olduğunu varsayalım:



- X, $\{1,2\}$ sonuç kümesine sahiptir


$$
Pr[X = 1] = 0.5
$$


$$
Pr[X = 2] = 0.5
$$


X$'in bir rastgele değişken olduğunu görmek kolaydır. İlk olarak, $X$ 'in alabileceği iki veya daha fazla olası değer vardır, yani $1$ ve $2$. İkinci olarak, $X$ değerini örneklediğinizde her olası değerin pozitif bir olasılığı vardır, yani $0.5$.


Bir rastgele değişkenin gerektirdiği tek şey, iki veya daha fazla olasılığa sahip bir sonuç kümesidir; burada her olasılık, örnekleme sırasında pozitif bir olasılığa sahiptir. O halde, ilke olarak, bir rastgele değişken herhangi bir bağlamdan yoksun olarak soyut bir şekilde tanımlanabilir. Bu durumda, "örneklemeyi" rastgele değişkenin değerini belirlemek için doğal bir deney yapmak olarak düşünebilirsiniz.


Yukarıdaki $X$ değişkeni soyut olarak tanımlanmıştır. Bu nedenle, yukarıdaki $X$ değişkenini örneklemeyi, adil bir Coin'i çevirmek ve tura durumunda "2", yazı durumunda "1" atamak olarak düşünebilirsiniz. Her $X$ örneği için Coin'i tekrar çevirirsiniz.


Alternatif olarak, $X$ örneklemesini adil bir zar atıp zarın 1$, 3$ veya 4$ gelmesi durumunda "2", 2$, 5$ veya 6$ gelmesi durumunda ise "1" atamak olarak da düşünebilirsiniz. X$ değerini her örneklediğinizde, zarı tekrar atarsınız.


Gerçekten de, yukarıdaki $X$'in olası değerlerinin olasılıklarını tanımlamanıza izin verecek herhangi bir doğal deney, çizime göre hayal edilebilir.


Ancak çoğu zaman rastgele değişkenler sadece soyut olarak tanıtılmaz. Bunun yerine, olası sonuç değerleri kümesinin açık bir gerçek dünya anlamı vardır (sadece sayılar olarak değil). Buna ek olarak, bu sonuç değerleri belirli bir deney türüne göre tanımlanabilir (bu değerlere sahip herhangi bir doğal deney yerine).


Şimdi soyut olarak tanımlanmamış bir $X$ değişken örneğini ele alalım. X, iki takımdan hangisinin bir futbol maçına başlayacağını belirlemek için aşağıdaki gibi tanımlanır:



- x$ sonuç kümesine sahiptir {kırmızı başlar, mavi başlar}
- Belirli bir Coin $C$ çevirin: yazı = "kırmızı atar"; tura = "mavi atar"


$$
Pr [X = \text{red kicks off}] = 0.5
$$


$$
Pr [X = \text{blue kicks off}] = 0.5
$$


Bu durumda, X'in sonuç kümesine somut bir anlam yüklenir, yani bir futbol maçında hangi takımın başlayacağı. Buna ek olarak, olası sonuçlar ve bunlarla ilişkili olasılıklar somut bir deneyle, yani belirli bir Coin $C$'nin çevrilmesiyle belirlenir.


Kriptografi tartışmalarında, rastgele değişkenler genellikle gerçek dünyada anlamı olan bir sonuç kümesine karşı tanıtılır. Bu, mesaj uzayı olarak bilinen, şifrelenebilecek tüm mesajların kümesi veya anahtar uzayı olarak bilinen, şifrelemeyi kullanan tarafların seçebileceği tüm anahtarların kümesi olabilir.


Bununla birlikte, kriptografi tartışmalarındaki rastgele değişkenler genellikle belirli bir doğal deneye karşı değil, doğru olasılık dağılımlarını verebilecek herhangi bir deneye karşı tanımlanır.


Rastgele değişkenler kesikli veya sürekli olasılık dağılımlarına sahip olabilir. **Kesikli olasılık dağılımına** sahip rastgele değişkenler, yani kesikli rastgele değişkenler, sonlu sayıda olası sonuca sahiptir. Şimdiye kadar verilen her iki örnekte de $X$ rastgele değişkeni kesikli idi.


**Sürekli rastgele değişkenler** bunun yerine bir veya daha fazla aralıkta değerler alabilir. Örneğin, bir rastgele değişkenin örnekleme üzerine 0 ile 1 arasındaki herhangi bir gerçek değeri alacağını ve bu aralıktaki her gerçek sayının eşit olasılıkta olduğunu söyleyebilirsiniz. Bu aralık içinde sonsuz sayıda olası değer vardır.


Kriptografik tartışmalar için sadece ayrık rastgele değişkenleri anlamanız gerekecektir. Bu nedenle, bundan sonra rastgele değişkenlerle ilgili her türlü tartışma, aksi özellikle belirtilmedikçe, ayrık rastgele değişkenlere atıfta bulunulduğu şeklinde anlaşılmalıdır.



### Rastgele değişkenlerin grafiği


Bir rastgele değişken için olası değerler ve ilişkili olasılıklar bir grafik aracılığıyla kolayca görselleştirilebilir. Örneğin, önceki bölümdeki $X$ rastgele değişkenini $\{1, 2\}$ sonuç kümesi ve $Pr [X = 1] = 0.5$ ve $Pr [X = 2] = 0.5$ ile ele alalım. Böyle bir rastgele değişkeni tipik olarak *Şekil 1*'deki gibi bir çubuk grafik şeklinde gösteririz.


*Şekil 1: Rastgele değişken X*


![Figure 1: Random variable X.](assets/Figure2-1.webp)


Şekil 1'deki geniş çubuklar, $X$ rassal değişkeninin aslında sürekli olduğu anlamına gelmemektedir. Bunun yerine, çubuklar görsel olarak daha çekici olması için geniş tutulmuştur (sadece düz bir çizgi daha az sezgisel bir görselleştirme sağlar).



### Tek tip değişkenler


"Rastgele değişken" ifadesinde "rastgele" terimi sadece "olasılıklı" anlamına gelir. Başka bir deyişle, değişkenin iki veya daha fazla olası sonucunun belirli olasılıklarla ortaya çıktığı anlamına gelir. Ancak bu sonuçların eşit olasılıklı olması gerekmez ("rastgele" terimi başka bağlamlarda gerçekten de bu anlama gelebilir).


**Tekdüze değişken** rastgele değişkenin özel bir durumudur. Hepsi eşit olasılığa sahip iki veya daha fazla değer alabilir. **Şekil 1**'de gösterilen $X$ rastgele değişkeni, her iki olası sonuç da 0,5$ olasılıkla gerçekleştiği için açıkça tekdüze bir değişkendir. Bununla birlikte, tekdüze değişkenlerin örnekleri olmayan birçok rastgele değişken vardır.


Örneğin, $Y$ rastgele değişkenini ele alalım. Bu değişken {1, 2, 3, 8, 10} sonuç kümesine ve aşağıdaki olasılık dağılımına sahiptir:


$$
\Pr[Y = 1] = 0.25
$$


$$
\Pr[Y = 2] = 0.35
$$


$$
\Pr[Y = 3] = 0.1
$$


$$
\Pr[Y = 8] = 0.25
$$


$$
\Pr[Y = 10] = 0.05
$$



İki olası sonucun, yani $1$ ve $8$'in gerçekleşme olasılığı eşit olsa da, $Y$ örnekleme sonucunda $0.25$'den farklı olasılıklara sahip belirli değerler de alabilir. Dolayısıyla, $Y$ gerçekten bir rastgele değişken olsa da, tekdüze bir değişken değildir.


Y$'nin grafiksel bir tasviri *Şekil 2*'de verilmiştir.


*Şekil 2: Rastgele değişken Y*


![Figure 2: Random variable Y.](assets/Figure2-2.webp "Figure 2: Random variable Y")


Son bir örnek olarak, {1,3,7,11,12} sonuç kümesine ve aşağıdaki olasılık dağılımına sahip rastgele değişken Z'yi düşünün:


$$
\Pr[Z = 2] = 0.2
$$


$$
\Pr[Z = 3] = 0.2
$$


$$
\Pr[Z = 9] = 0.2
$$


$$
\Pr[Z = 11] = 0.2
$$


$$
\Pr[Z = 12] = 0.2
$$


Bunu *Şekil 3*'de görebilirsiniz. Z rastgele değişkeni, Y'nin aksine, tekdüze bir değişkendir, çünkü örnekleme üzerine olası değerler için tüm olasılıklar eşittir.



*Şekil 3: Rastgele değişken Z*


![Figure 3: Random variable Z.](assets/Figure2-3.webp "Figure 3: Random variable Z")



### Koşullu olasılık


Bob'in son takvim yılından tekdüze bir gün seçmeye niyetlendiğini varsayalım. Seçilen günün Yaz mevsiminde olma olasılığının ne olduğu sonucuna varmalıyız?


Bob'nin sürecinin gerçekten de tekdüze olacağını düşündüğümüz sürece, Bob'nin Yaz'da bir gün seçme olasılığının 1/4 olduğu sonucuna varmalıyız. Bu, rastgele seçilen günün Yaz mevsiminde olmasının **koşulsuz olasılığıdır**.


Şimdi Bob'ün bir takvim gününü tekdüze olarak çekmek yerine, yalnızca Crystal Lake'te (New Jersey) öğlen sıcaklığının 21 santigrat derece veya daha yüksek olduğu günler arasından tekdüze olarak seçim yaptığını varsayalım. Bu ek bilgi göz önüne alındığında, Bob'ün Yaz mevsiminde bir gün seçme olasılığı hakkında ne sonuca varabiliriz?


Daha fazla spesifik bilgi olmadan bile (örneğin, geçen takvim yılında her gün öğle saatlerindeki sıcaklık) gerçekten öncekinden farklı bir sonuca varmalıyız.


Crystal Lake'in New Jersey'de olduğunu bildiğimizden, kışın öğle vakti sıcaklığın 21 santigrat derece veya daha yüksek olmasını kesinlikle beklemeyiz. Bunun yerine, İlkbahar veya Sonbaharda sıcak bir gün veya Yaz mevsiminde bir gün olması çok daha muhtemeldir. Dolayısıyla, seçilen günde Kristal Göl'de öğlen sıcaklığının 21 santigrat derece veya daha yüksek olduğu bilindiğinde, Bob tarafından seçilen günün Yaz mevsiminde olma olasılığı çok daha yüksek olur. Bu, Kristal Göl'deki öğle sıcaklığının 21 santigrat derece veya daha yüksek olduğu göz önüne alındığında, rastgele seçilen günün Yaz mevsiminde olma **koşullu olasılığıdır**.


Önceki örnekten farklı olarak, iki olayın olasılıkları tamamen ilişkisiz de olabilir. Bu durumda, **bağımsız** olduklarını söyleriz.


Örneğin, belirli bir adil Coin'in başları yere indirdiğini varsayalım. Bu gerçek göz önüne alındığında, yarın yağmur yağma olasılığı nedir? Bu durumda koşullu olasılık, yarın yağmur yağacağına dair koşulsuz olasılıkla aynı olmalıdır, çünkü bir Coin çevirmenin genellikle hava durumu üzerinde herhangi bir etkisi yoktur.


Koşullu olasılık ifadelerini yazmak için "|" sembolünü kullanırız. Örneğin, $B$ olayının gerçekleşmesi durumunda $A$ olayının olasılığı aşağıdaki gibi yazılabilir:


$$
Pr[A|B]
$$


Yani, $A$ ve $B$ iki olay bağımsız olduğunda, o zaman:


$$
Pr[A|B] = Pr[A] \text{ and } Pr[B|A] = Pr[B]
$$


Bağımsızlık koşulu aşağıdaki şekilde basitleştirilebilir:


$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$



Olasılık teorisinde önemli bir sonuç **Bayes Teoremi** olarak bilinir. Temel olarak $Pr[A|B]$ 'nin aşağıdaki gibi yeniden yazılabileceğini belirtir:



$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$



Belirli olaylarla ilgili koşullu olasılıkları kullanmak yerine, bir dizi olası olay üzerinden iki veya daha fazla rastgele değişkenle ilgili koşullu olasılıklara da bakabiliriz. İki rastgele değişken varsayalım, $X$ ve $Y$. X$ için herhangi bir olası değeri $x$ ile ve $Y$ için herhangi bir olası değeri $y$ ile gösterebiliriz. O halde, aşağıdaki ifade geçerliyse iki rastgele değişkenin bağımsız olduğunu söyleyebiliriz:


$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$


tüm $x$ ve $y$ için.


Bu ifadenin ne anlama geldiği konusunda biraz daha açık olalım.


X$ ve Y$ için sonuç kümelerinin aşağıdaki gibi tanımlandığını varsayalım: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ ve **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (Değer kümelerini kalın ve büyük harflerle belirtmek tipiktir)


Şimdi $Y$ örneklediğinizi ve $y_1$ gözlemlediğinizi varsayalım. Yukarıdaki ifade bize $X$ örneklemesinden $x_1$ elde etme olasılığımızın $y_1$'i hiç gözlemlememiş olmamızla tamamen aynı olduğunu söyler. Bu, başlangıçtaki $Y$ örneklememizden çıkarabileceğimiz herhangi bir $y_i$ için de geçerlidir. Son olarak, bu sadece $x_1$ için geçerli değildir. Herhangi bir $x_i$ için, gerçekleşme olasılığı $Y$ örneklemesinin sonucundan etkilenmez. Tüm bunlar $X$'in ilk olarak örneklendiği durum için de geçerlidir.


Tartışmamızı biraz daha felsefi bir noktada sonlandıralım. Herhangi bir gerçek dünya durumunda, bir olayın olasılığı her zaman belirli bir bilgi kümesine göre değerlendirilir. Kelimenin tam anlamıyla "koşulsuz olasılık" diye bir şey yoktur.


Örneğin, size 2030 yılına kadar domuzların uçma olasılığını sorduğumu varsayalım. Size daha fazla bilgi vermesem de, dünya hakkında kararınızı etkileyebilecek çok şey bildiğiniz açık. Domuzların uçtuğunu hiç görmediniz. Çoğu insanın onların uçmasını beklemeyeceğini biliyorsunuz. Gerçekten uçmak için yapılmadıklarını biliyorsunuz. Ve bu böyle devam eder.


Dolayısıyla, gerçek dünya bağlamında bir olayın "koşulsuz olasılığından" bahsettiğimizde, bu terim ancak "daha fazla açık bilgi olmaksızın olasılık" gibi bir anlama gelirse bir anlam ifade edebilir. O halde, herhangi bir "koşullu olasılık" anlayışı, her zaman belirli bir bilgi parçasına karşı anlaşılmalıdır.


Örneğin, size Yeni Zelanda'da bazı keçilerin birkaç yıllık eğitimden sonra uçmayı öğrendiğine dair kanıt sunduktan sonra domuzların 2030 yılına kadar uçma olasılığını sorabilirim. Bu durumda, muhtemelen domuzların 2030 yılına kadar uçma olasılığına ilişkin yargınızı değiştireceksiniz. Yani domuzların 2030 yılına kadar uçma olasılığı, Yeni Zelanda'daki keçilerle ilgili bu kanıta bağlıdır.



## Modulo işlemi

<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>


### Modulo


Modulo işlemini içeren en temel ifade şu şekildedir: $x \mod y$.


X$ değişkeni bölen, $y$ değişkeni ise bölen olarak adlandırılır. Pozitif bir bölen ve pozitif bir bölen ile bir modulo işlemi gerçekleştirmek için, sadece bölümden kalanı belirlersiniz.


Örneğin, $25 \mod 4$ ifadesini düşünün. 4 sayısı 25 sayısının içine toplam 6 kez girer. Bu bölme işleminden kalan 1'dir. Dolayısıyla, 25 $ \mod 4$ 1'e eşittir. Benzer bir şekilde, aşağıdaki ifadeleri de değerlendirebiliriz:



- $29 \mod 30 = 29$ (30, 29'un içine toplam 0 kez girdiğinden ve kalan 29 olduğundan)
- 42 \mod 2 = 0$ (2, 42'ye toplam 21 kez girdiği ve kalan 0 olduğu için)
- 12 $ \mod 5 = 2$ (5, 12'ye toplam 2 kez girdiğinden ve kalan 2 olduğundan)
- 20 $ \mod 8 = 4$ (8, 20'ye toplam 2 kez girdiğinden ve kalan 4 olduğundan)


Bölen veya bölünen negatif olduğunda, modulo işlemleri programlama dilleri tarafından farklı şekilde ele alınabilir.


Kriptografide negatif kar payı olan durumlarla mutlaka karşılaşacaksınız. Bu durumlarda tipik yaklaşım aşağıdaki gibidir:



- İlk olarak, bölenin sıfır kalanla böldüğü, bölen değerden *daha düşük veya ona eşit* en yakın değeri belirleyin. Bu değere $p$ adını verin.
- Eğer kar payı $x$ ise, modulo işleminin sonucu $x - p$ değeridir.


Örneğin, kar payının $-20$ ve bölenin 3 olduğunu varsayalım. 3'ün eşit olarak bölündüğü $-20$'den küçük veya eşit en yakın değer $-21$'dir. Bu durumda $x - p$ değeri $-20 - (-21)$ olur. Bu 1'e eşittir ve dolayısıyla $-20 \mod 3$ 1'e eşittir. Benzer bir şekilde, aşağıdaki ifadeleri de değerlendirebiliriz:



- $-8 \mod 5 = 2$
- $-19 \mod 16 = 13$
- $-14 \mod 6 = 4$


Gösterimle ilgili olarak, genellikle şu tür ifadeler görürsünüz: $x = [y \mod z]$. Parantezler nedeniyle, bu durumda modulo işlemi yalnızca ifadenin sağ tarafı için geçerlidir. Örneğin, $y$ 25'e ve $z$ 4'e eşitse, $x$ 1 olarak değerlendirilir.


Parantezler olmadan, modulo işlemi bir ifadenin *her iki tarafına* etki eder. Örneğin, aşağıdaki ifadeyi varsayalım: $x = y \mod z$. Eğer $y$ 25'e ve $z$ 4'e eşitse, tüm bildiğimiz $x \mod 4$'ün 1 olarak değerlendirildiğidir. Bu, $\{\ldots,-7, -3, 1, 5, 9,\ldots\}$ kümesindeki herhangi bir $x$ değeri ile tutarlıdır.


Sayılar ve ifadeler üzerinde modulo işlemleri içeren matematik dalı **modüler aritmetik** olarak adlandırılır. Bu dalı, sayı doğrusunun sonsuz uzunlukta olmadığı durumlar için aritmetik olarak düşünebilirsiniz. Kriptografide genellikle (pozitif) tam sayılar için modulo işlemlerine rastlasak da, herhangi bir gerçek sayıyı kullanarak da modulo işlemleri gerçekleştirebilirsiniz.


### Kaydırmalı şifre


Modulo işlemi kriptografide sıklıkla karşılaşılan bir işlemdir. Örnek olarak, en ünlü tarihi şifreleme şemalarından birini ele alalım: shift şifresi.


Önce bunu tanımlayalım. İngiliz alfabesindeki tüm harfleri sırayla $\{0, 1, 2, \ldots, 25\}$ sayı kümesine eşitleyen bir *D* sözlüğü varsayalım. Bir **M** mesaj uzayı varsayalım. O halde **shift cipher** aşağıdaki gibi tanımlanan bir şifreleme şemasıdır:



- **K** anahtar uzayından düzgün bir $k$ anahtarı seçin, burada **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Bir $m \in \mathbf{M}$ mesajını aşağıdaki gibi şifreleyin:
    - M$'yi kendi içinde $m_0, m_1, \ldots, m_i, \ldots, m_l$ harflerine ayırın
    - Her $m_i$'yi *D*'ye göre bir sayıya dönüştürün
    - Her $m_i$ için, $c_i = [(m_i + k) \mod 26]$
    - Her $c_i$'yi *D*'ye göre bir harfe dönüştürün
    - Daha sonra $c_0, c_1, \ldots, c_l$ birleştirilerek $c$ şifreli metni elde edilir
- Bir $c$ şifreli metninin şifresini aşağıdaki gibi çözün:
    - Her $c_i$'yi *D*'ye göre bir sayıya dönüştürün
    - Her $c_i$ için, $m_i = [(c_i - k) \mod 26]$
    - Her $m_i$'yi *D*'ye göre bir harfe dönüştürün
    - Daha sonra $m_0, m_1, \ldots, m_l$ birleştirilerek orijinal mesaj $m$ elde edilir


Kaydırma şifresindeki modulo operatörü, harflerin etrafını sarmasını sağlar, böylece tüm şifreli metin harfleri tanımlanır. Örnek olarak, "DOG" kelimesi üzerinde kaydırma şifresinin uygulanmasını düşünün.


Bir anahtarı 17 değerine sahip olacak şekilde eşit olarak seçtiğinizi varsayalım. "O" harfi 15'e eşittir. Modulo işlemi olmadan, bu düz metin sayısının anahtarla toplanması 32'lik bir şifreli metin sayısına karşılık gelecektir. Ancak, İngiliz alfabesinde yalnızca 26 harf bulunduğundan, bu şifreli metin sayısı bir şifreli metin harfine dönüştürülemez. Modulo işlemi, şifreli metin sayısının aslında 6 olmasını sağlar ($32 \mod 26$ sonucu), bu da "G" şifreli metin harfine eşittir.


Anahtar değeri 17 olan "DOG" kelimesinin tüm şifrelemesi aşağıdaki gibidir:



- Mesaj = DOG = D,O,G = 3,15,6
- $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
- $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
- $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
- $c = UGX$


Herkes vardiya şifresinin nasıl çalıştığını sezgisel olarak anlayabilir ve muhtemelen kendisi de kullanabilir. Bununla birlikte, kriptografi bilginizi ilerletmek için, şemalar çok daha zor hale geleceğinden, formalizasyon konusunda daha rahat olmaya başlamak önemlidir. Bu nedenle, vardiya şifresi için adımlar resmileştirilmiştir.



**Notlar:**


[1] Önceki bölümdeki terminolojiyi kullanarak bu ifadeyi tam olarak tanımlayabiliriz. Bir $K$ tekdüze değişkeninin olası sonuçlar kümesi $K$ olsun. Yani:


$$
Pr[K = 0] = \frac{1}{26}
$$


$$
Pr[K = 1] = \frac{1}{26}
$$


...vb. Belirli bir anahtar elde etmek için $K$ tekdüze değişkenini bir kez örnekleyin.



## XOR işlemi

<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>


Tüm bilgisayar verileri bit seviyesinde işlenir, saklanır ve ağlar üzerinden gönderilir. Bilgisayar verilerine uygulanan tüm kriptografik şemalar da bit düzeyinde çalışır.


Örneğin, e-posta uygulamanıza bir e-posta yazdığınızı varsayalım. Uyguladığınız herhangi bir şifreleme doğrudan e-postanızın ASCII karakterleri üzerinde gerçekleşmez. Bunun yerine, e-postanızdaki harflerin ve diğer sembollerin bit temsillerine uygulanır.


Modulo işleminin yanı sıra modern kriptografi için anlaşılması gereken önemli bir matematiksel işlem **XOR işlemi** veya "exclusive or" işlemidir. Bu işlem iki biti girdi olarak alır ve başka bir biti çıktı olarak verir. XOR işlemi basitçe "XOR" olarak gösterilecektir. İki bit aynıysa 0, iki bit farklıysa 1 değerini verir. Aşağıda dört olasılığı görebilirsiniz. $\oplus$ sembolü "XOR" işlemini temsil eder:



- $0 \oplus 0 = 0$
- 0 $ \oplus 1 = 1$
- $1 \oplus 0 = 1$
- $1 \oplus 1 = 0$


Örnek olarak, bir $m_1$ (01111001) ve bir $m_2$ (01011001) mesajınız olduğunu varsayalım. Bu iki mesajın XOR işlemi aşağıda görülebilir.



- $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$


İşlem basittir. Önce $m_1$ ve $m_2$'nin en soldaki bitlerini XOR'larsınız. Bu durumda bu 0$ \oplus 0 = 0$ olur. Daha sonra soldan ikinci bit çiftini XOR'larsınız. Bu durumda $1 \oplus 1 = 0$ olur. En sağdaki bitler üzerinde XOR işlemini gerçekleştirene kadar bu işleme devam edersiniz.


XOR işleminin değişmeli olduğunu, yani $m_1 \oplus m_2 = m_2 \oplus m_1$ olduğunu görmek kolaydır. Buna ek olarak, XOR işlemi aynı zamanda birleşimseldir. Yani, $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.


Alternatif uzunluktaki iki dizge üzerinde yapılan bir XOR işlemi, bağlama bağlı olarak farklı yorumlara sahip olabilir. Biz burada farklı uzunluktaki dizgeler üzerindeki XOR işlemleriyle ilgilenmeyeceğiz.


Bir XOR işlemi, bölen 2 olduğunda bitlerin toplanması üzerinde bir modulo işlemi gerçekleştirmenin özel durumuna eşdeğerdir. Eşdeğerliği aşağıdaki sonuçlarda görebilirsiniz:



- $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
- $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
- $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
- $(1 + 1) \mod 2 = 1 \oplus 1 = 0$


## Sözde rastlantısallık

<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>


Rastgele ve tekdüze değişkenlere ilişkin tartışmamızda, "rastgele" ve "tekdüze" arasında belirli bir ayrım yaptık. Bu ayrım, uygulamada rastgele değişkenleri tanımlarken tipik olarak korunmaktadır. Ancak, mevcut bağlamımızda, bu ayrımın bırakılması ve "rastgele" ve "tekdüze" kelimelerinin eşanlamlı olarak kullanılması gerekmektedir. Nedenini bölümün sonunda açıklayacağım.


Başlangıç olarak, $n$ uzunluğundaki bir ikili dizgiye **rastgele** (veya **tekdüze**) diyebiliriz, eğer böyle bir $n$ uzunluğundaki her ikili dizgiye eşit seçilme olasılığı veren tekdüze bir $S$ değişkeninin örneklenmesinin sonucuysa.


Örneğin, uzunluğu 8 olan tüm ikili dizelerin kümesini varsayalım: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (8 bitlik bir dizgiyi, her biri **nibble** olarak adlandırılan iki dörtlü halinde yazmak tipiktir) Bu dizge kümesine **$S_8$** diyelim.


Yukarıdaki tanıma göre, 8 uzunluğundaki belirli bir ikili dizgiye rastgele (veya tekdüze) diyebiliriz, eğer **$S_8$** içindeki her dizgiye eşit seçilme olasılığı veren tekdüze bir $S$ değişkeninin örneklenmesinin sonucuysa. **$S_8$** kümesinin **$2^8$** Elements içerdiği göz önüne alındığında, örnekleme sonucu seçilme olasılığının kümedeki her bir dize için **$1/2^8$** olması gerekir.


Bir ikili dizginin rastgeleliğinin önemli bir yönü, seçildiği sürece referansla tanımlanmış olmasıdır. Bu nedenle, herhangi bir ikili dizginin biçimi kendi başına, seçimdeki rastgeleliği hakkında hiçbir şey ortaya koymaz.


Örneğin, birçok insan sezgisel olarak $1111\ 1111$ gibi bir dizenin rastgele seçilemeyeceği fikrine sahiptir. Ancak bu açıkça yanlıştır.


Uzunluğu 8 olan tüm ikili dizeler üzerinde tekdüze bir $S$ değişkeni tanımlandığında, **$S_8$** kümesinden $1111\ 1111$ seçme olasılığı, $0111\ 0100$ gibi bir dizeyle aynıdır. Dolayısıyla, sadece dizginin kendisini analiz ederek bir dizginin rastgeleliği hakkında hiçbir şey söyleyemezsiniz.


Özellikle ikili dizgileri kastetmeden de rastgele dizgilerden bahsedebiliriz. Örneğin, rastgele bir $AF\ 02\ 82$ hex dizisinden bahsedebiliriz. Bu durumda, dizge 6 uzunluğundaki tüm onaltılık dizgeler kümesinden rastgele seçilmiş olur. Bu, her onaltılık basamak 4 biti temsil ettiğinden, 24 uzunluğunda bir ikili dizgeyi rastgele seçmeye eşdeğerdir.


Tipik olarak "rastgele bir dize" ifadesi, herhangi bir niteleme olmaksızın, aynı uzunluktaki tüm dizelerin kümesinden rastgele seçilen bir dizeyi ifade eder. Yukarıda bu şekilde tanımlamıştım. Elbette $n$ uzunluğundaki bir dizge farklı bir kümeden de rastgele seçilebilir. Örneğin, yalnızca $n$ uzunluğundaki tüm dizgilerin bir alt kümesini oluşturan bir küme ya da belki de farklı uzunluktaki dizgileri içeren bir küme. Ancak bu gibi durumlarda, bu dizgiden "rastgele dizgi" olarak değil, "**S** kümesinden rastgele seçilmiş bir dizgi" olarak söz ederiz.


Kriptografide anahtar kavramlardan biri sözde rastlantısallıktır. Uzunluğu $n$ olan bir **sözde rastlantısal dize**, **$S_n$** içindeki her dizeye eşit seçilme olasılığı veren tekdüze bir $S$ değişkeninin örneklenmesinin sonucuymuş gibi görünür. Ancak aslında bu dize, **$S_n$** alt kümesi üzerinde yalnızca bir olasılık dağılımı tanımlayan (tüm olası sonuçlar için eşit olasılıklara sahip olması gerekmeyen) tekdüze bir $S'$ değişkeninin örneklenmesinin sonucudur. Buradaki en önemli nokta, çok sayıda örnek alsanız bile hiç kimsenin $S$ ve $S'$ örneklerini gerçekten ayırt edemeyeceğidir.


Örneğin, bir $S$ rastgele değişkenini varsayalım. Sonuç kümesi **$S_{256}$** olsun, bu küme 256 uzunluğundaki tüm ikili dizelerin kümesidir. Bu kümede $2^{256}$ Elements vardır. Her elemanın örnekleme sırasında eşit bir seçilme olasılığı vardır, $1/2^{256}$.


Buna ek olarak, $S'$ rastgele değişkenini varsayalım. Sonuç kümesi yalnızca 256 uzunluğunda $2^{128}$ ikili dizeleri içerir. Bu diziler üzerinde bir olasılık dağılımı vardır, ancak bu dağılımın tekdüze olması gerekmez.


Şimdi $S$'den 1000'lerce örnek ve $S'$'den 1000'lerce örnek aldığımı ve iki sonuç kümesini size verdiğimi varsayalım. Size hangi sonuç kümesinin hangi rastgele değişkenle ilişkili olduğunu söyleyeceğim. Daha sonra, iki rastgele değişkenden birinden bir örnek alıyorum. Ancak bu sefer size hangi rastgele değişkeni örneklediğimi söylemiyorum. Eğer $S'$ sözde rastgele olsaydı, o zaman hangi rastgele değişkeni örneklediğime dair doğru tahminde bulunma olasılığınız pratikte $1/2$'den daha iyi olmazdı.


Tipik olarak, $x$ pozitif bir tamsayı olmak üzere, $n$ - x$ boyutunda bir dizgenin rastgele seçilmesi ve bir genişletme algoritması için girdi olarak kullanılmasıyla $n$ uzunluğunda bir sözde rastgele dizge üretilir. Bu $n - x$ boyutundaki rastgele dizge **seed** olarak bilinir.


Sözde rastgele diziler kriptografiyi pratik hale getirmek için anahtar bir kavramdır. Örneğin, akış şifrelerini düşünün. Bir akış şifresi ile rastgele seçilen bir anahtar, çok daha büyük bir sözde rastgele dizge üretmek için genişletici bir algoritmaya takılır. Bu sözde rastgele dizge daha sonra bir XOR işlemi aracılığıyla düz metinle birleştirilerek bir şifreli metin üretilir.


Eğer bir akış şifresi için bu tür bir sözde rastgele dizge üretemiyor olsaydık, o zaman güvenlik için mesaj kadar uzun bir anahtara ihtiyacımız olurdu. Bu çoğu durumda çok pratik bir seçenek değildir.


Bu bölümde tartışılan sözde rastgelelik kavramı daha resmi olarak tanımlanabilir. Ayrıca diğer bağlamlara da genişletilebilir. Ancak burada bu tartışmaya girmemize gerek yok. Kriptografinin büyük bir kısmı için sezgisel olarak anlamanız gereken tek şey rastgele ve sözde rastgele dizge arasındaki farktır. [2]


Tartışmamızda "rastgele" ve "tekdüze" arasındaki ayrımı bırakmamızın nedeni de artık açık olmalıdır. Pratikte herkes sözde rastgele terimini, tekdüze bir $S$ değişkeninin örneklenmesi sonucu **olmuş gibi** görünen bir dizgiyi belirtmek için kullanır. Daha açık konuşmak gerekirse, böyle bir dizgiye "sözde tekdüze" demeliyiz, daha önceki dilimizi benimseyerek. "Pseudo-uniform" terimi hem hantal hem de kimse tarafından kullanılmadığından, açıklık getirmek için burada kullanmayacağız. Bunun yerine, mevcut bağlamda "rastgele" ve "tekdüze" arasındaki ayrımı kaldırıyoruz.



**Notlar**


[2] Bu konularda daha resmi bir açıklama ile ilgileniyorsanız, Katz ve Lindell'in *Introduction to Modern Cryptography* kitabına, özellikle 3. bölüme bakabilirsiniz.



# Kriptografinin Matematiksel Temelleri 2

<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>



## Sayı teorisi nedir?

<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>


Bu bölüm kriptografinin matematiksel temelleri üzerine daha ileri bir konuyu ele almaktadır: sayı teorisi. Sayı teorisi simetrik kriptografi için önemli olsa da (Rijndael Şifresi gibi), açık anahtar kriptografik ortamında özellikle önemlidir.


Eğer sayılar teorisinin detaylarını hantal buluyorsanız, ilk seferde üst düzey bir okuma yapmanızı tavsiye ederim. Daha sonra her zaman geri dönebilirsiniz.


___


**Sayılar teorisini** tamsayıların ve tamsayılarla çalışan matematiksel fonksiyonların özelliklerinin incelenmesi olarak tanımlayabilirsiniz.


Örneğin, herhangi iki $a$ ve $N$ sayısının, en büyük ortak bölenleri 1'e eşitse **ortak asal** (veya **göreceli asal**) olduğunu düşünün. Şimdi belirli bir $N$ tamsayısı varsayalım. N$'den küçük kaç tamsayı $N$ ile eş asaldır? Bu sorunun yanıtları hakkında genel ifadeler kullanabilir miyiz? Bunlar sayılar kuramının yanıtlamaya çalıştığı tipik soru türleridir.


Modern sayı teorisi soyut cebir araçlarına dayanır. **Soyut cebir** alanı, analizin ana nesnelerinin cebirsel yapılar olarak bilinen soyut nesneler olduğu matematiğin bir alt disiplinidir. Bir **cebirsel yapı**, belirli aksiyomları karşılayan bir veya daha fazla işlemle birleştirilmiş bir Elements kümesidir. Cebirsel yapılar aracılığıyla matematikçiler, ayrıntılarından soyutlanarak belirli matematiksel problemler hakkında içgörü kazanabilirler.


Soyut cebir alanı bazen modern cebir olarak da adlandırılır. Ayrıca **soyut matematik** (veya **saf matematik**) kavramıyla da karşılaşabilirsiniz. Bu son terim soyut cebire bir atıf değildir, daha ziyade matematiğin sadece potansiyel uygulamalar göz önünde bulundurularak değil, kendi iyiliği için incelenmesi anlamına gelir.


Soyut cebir kümeleri, eşkenar üçgen üzerindeki şekli koruyan dönüşümlerden duvar kağıdı desenlerine kadar pek çok nesne türüyle ilgilenebilir. Sayı teorisi için, yalnızca tamsayılar veya tamsayılarla çalışan fonksiyonlar içeren Elements kümelerini dikkate alıyoruz.



## Gruplar

<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>


Matematikteki temel kavramlardan biri Elements kümesidir. Bir küme genellikle virgülle ayrılmış Elements'li aksan işaretleriyle gösterilir.


Örneğin, tüm tam sayıların kümesi $\{..., -2, -1, 0, 1, 2, ...\}$ şeklindedir. Buradaki elipsler, belirli bir örüntünün belirli bir yönde devam ettiği anlamına gelir. Dolayısıyla, tüm tamsayılar kümesi 3, 4, 5, 6$ ve benzerlerinin yanı sıra $-3, -4, -5, -6$ ve benzerlerini de içerir. Tüm tamsayıların bu kümesi tipik olarak $\mathbb{Z}$ ile gösterilir.


Bir başka küme örneği ise $\mathbb{Z} \mod 11$ ya da tüm tamsayıların modulo 11 kümesi. Tüm $\mathbb{Z}$ kümesinin aksine, bu küme yalnızca sonlu sayıda Elements, yani $\{0, 1, \ldots, 9, 10\}$ içerir.


Yaygın bir hata, $\mathbb{Z} kümesinin \mod 11$ aslında $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$ şeklindedir. Ancak, daha önce modulo işlemini tanımlama şeklimiz göz önüne alındığında durum böyle değildir. Modulo 11 ile indirgenen tüm negatif tamsayılar $\{0, 1, \ldots, 9, 10\}$ üzerine sarılır. Örneğin, $-2 \mod 11$ ifadesi $9$'a sarılırken, $-27 \mod 11$ ifadesi $5$'a sarılır.


Matematikteki bir diğer temel kavram da ikili işlemdir. Bu, üçüncüyü üretmek için iki Elements alan herhangi bir işlemdir. Örneğin, temel aritmetik ve cebirden dört temel ikili işleme aşina olursunuz: toplama, çıkarma, çarpma ve bölme.


Bu iki temel matematiksel kavram, kümeler ve ikili işlemler, soyut cebirdeki en temel yapı olan grup kavramını tanımlamak için kullanılır.


Özellikle, bazı ikili işlemlerin $\circ$ olduğunu varsayalım. Buna ek olarak, bu işlemle donatılmış bazı Elements **S** kümelerini varsayalım. Burada "donanımlı" ifadesinin tek anlamı $\circ$ işleminin **S** kümesindeki herhangi iki Elements arasında gerçekleştirilebileceğidir.


O halde $\langle \mathbf{S}, \circ \rangle$ kombinasyonu, grup aksiyomları olarak bilinen dört özel koşulu karşılıyorsa bir **grup**tur.


1. Elements olan herhangi bir $a$ ve $b$ için $\mathbf{S}$, $a \circ b$ aynı zamanda $\mathbf{S}$'in bir elemanıdır. Bu **kapanma koşulu** olarak bilinir.

2. Elements olan herhangi bir $a$, $b$ ve $c$ için $\mathbf{S}$, $(a \circ b) \circ c = a \circ (b \circ c)$ durumudur. Bu **ilişkililik koşulu** olarak bilinir.

3. Mathbf{S}$ içinde tek bir $e$ elemanı vardır, öyle ki $\mathbf{S}$ içindeki her $a$ elemanı için aşağıdaki denklem geçerlidir: $e \circ a = a \circ e = a$. Böyle tek bir $e$ elemanı olduğundan, buna **özdeşlik elemanı** denir. Bu koşul **özdeşlik koşulu** olarak bilinir.

4. Mathbf{S}$ içindeki her $a$ elemanı için, $\mathbf{S}$ içinde öyle bir $b$ elemanı vardır ki aşağıdaki denklem geçerlidir: $a \circ b = b \circ a = e$, burada $e$ özdeşlik elemanıdır. Burada $b$ elemanı **ters eleman** olarak bilinir ve genellikle $a^{-1}$ olarak gösterilir. Bu koşul **ters koşul** veya **tersinmezlik koşulu** olarak bilinir.


Grupları biraz daha inceleyelim. Tüm tamsayıların kümesini $\mathbb{Z}$ ile gösterin. Bu küme standart toplama veya $\langle \mathbb{Z}, + \rangle$ ile birleştirildiğinde, yukarıdaki dört aksiyomu karşıladığı için bir grup tanımına açıkça uymaktadır.


1. Elements olan herhangi bir $x$ ve $y$ için $\mathbb{Z}$, $x + y$ aynı zamanda $\mathbb{Z}$'nin bir elemanıdır. Yani $\langle \mathbb{Z}, + \rangle$ kapanış koşulunu sağlamaktadır.

2. Elements olan herhangi bir $x$, $y$ ve $z$ için $\mathbb{Z}$, $(x + y) + z = x + (y + z)$ olur. Yani $\langle \mathbb{Z}, + \rangle$ ilişkisellik koşulunu sağlar.

3. Langle \mathbb{Z}, + \rangle$ içinde bir özdeşlik elemanı vardır, yani 0. $\mathbb{Z}$ içindeki herhangi bir $x$ için, yani şu geçerlidir: 0 + x = x + 0 = x$. Yani $\langle \mathbb{Z}, + \rangle$ özdeşlik koşulunu sağlamaktadır.

4. Son olarak, $\mathbb{Z}$ içindeki her $x$ elemanı için, $x + y = y + x = 0$ olacak şekilde bir $y$ vardır. Örneğin $x$ 10 olsaydı, $y$ de $-10$ olurdu ($x$'in 0 olması durumunda $y$ de 0 olur). Yani $\langle \mathbb{Z}, + \rangle$ ters koşulu sağlıyor.


Daha da önemlisi, tamsayılar kümesinin toplama ile bir grup oluşturması, çarpma ile bir grup oluşturduğu anlamına gelmez. Bunu $\langle \mathbb{Z}, \cdot \rangle$ dört grup aksiyomuna karşı test ederek doğrulayabilirsiniz (burada $\cdot$ standart çarpma anlamına gelir).


İlk iki aksiyom açıkça geçerlidir. Buna ek olarak, çarpma işlemi altında 1 elemanı özdeşlik elemanı olarak hizmet edebilir. Herhangi bir $x$ tamsayısının 1 ile çarpımı $x$ sonucunu verir. Ancak, $\langle \mathbb{Z}, \cdot \rangle$ ters koşulu sağlamaz. Yani, $\mathbb{Z}$ içindeki her $x$ için $\mathbb{Z}$ içinde tek bir $y$ elemanı yoktur, böylece $x \cdot y = 1$ olur.


Örneğin, $x = 22$ olduğunu varsayalım. X$ ile çarpıldığında $\mathbb{Z}$ kümesinden hangi $y$ değeri özdeşlik elemanı 1'i verir? 1$/22$ değeri işe yarayacaktır, ancak bu $\mathbb{Z}$ kümesinde yer almaz. Aslında, 1 ve -1 değerleri dışındaki herhangi bir $x$ tamsayısı için bu sorunla karşılaşırsınız (burada $y$ sırasıyla 1 ve -1 olmalıdır).


Kümemiz için gerçek sayılara izin verirsek, sorunlarımız büyük ölçüde ortadan kalkar. Kümedeki herhangi bir $x$ elemanı için $1/x$ ile çarpma işlemi 1 sonucunu verir. Kesirler reel sayılar kümesine dahil edildiğinden, her reel sayı için bir tersi bulunabilir. Bunun istisnası sıfırdır, çünkü sıfır ile herhangi bir çarpım asla özdeşlik elemanı 1'i vermeyecektir. Dolayısıyla, çarpma işlemiyle donatılmış sıfır olmayan reel sayılar kümesi gerçekten de bir gruptur.


Bazı gruplar **komütativite koşulu** olarak bilinen beşinci bir genel koşulu karşılar. Bu koşul aşağıdaki gibidir:



- Bir **S** kümesi ve bir $\circ$ ikili operatörü olan bir $G$ grubu varsayalım. A$ ve $b$ 'nin **S** 'nin Elements'u olduğunu varsayalım. Eğer **S** içinde herhangi iki Elements $a$ ve $b$ için $a \circ b = b \circ a$ ise, $G$ değişme koşulunu sağlıyor demektir.


Değişmeli olma koşulunu sağlayan herhangi bir grup **komütatif grup** veya **Abelian grup** (Niels Henrik Abel'den sonra) olarak bilinir. Toplama işlemi üzerindeki gerçek sayılar kümesinin ve toplama işlemi üzerindeki tamsayılar kümesinin Abelian gruplar olduğunu doğrulamak kolaydır. Çarpma işlemi üzerindeki tamsayılar kümesi bir grup değildir, bu nedenle de Abelyen grup olamaz. Buna karşın, çarpma işlemi üzerinden sıfır olmayan reel sayılar kümesi de bir Abelian gruptur.


Gösterimle ilgili iki önemli kurala dikkat etmelisiniz. Birincisi, "+" veya "×" işaretleri, Elements aslında sayı olmasa bile, grup işlemlerini sembolize etmek için sıklıkla kullanılacaktır. Bu durumlarda, bu işaretleri standart aritmetik toplama veya çarpma olarak yorumlamamalısınız. Bunun yerine, bu aritmetik işlemlere yalnızca soyut bir benzerliği olan işlemlerdir.


Özellikle aritmetik toplama veya çarpma işlemlerine atıfta bulunmadığınız sürece, grup işlemleri için $\circ$ ve $\diamond$ gibi sembolleri kullanmak daha kolaydır, çünkü bunların kültürel olarak kökleşmiş çağrışımları yoktur.


İkinci olarak, "+" ve "×" nin genellikle aritmetik olmayan işlemleri belirtmek için kullanılmasıyla aynı nedenden dolayı, grupların özdeşlik Elements'i, bu gruplardaki Elements sayı olmasa bile, sıklıkla "0" ve "1" ile sembolize edilir. Sayılar içeren bir grubun özdeşlik elemanına atıfta bulunmadığınız sürece, özdeşlik elemanını belirtmek için "$e$" gibi daha nötr bir sembol kullanmak daha kolaydır.


Matematikte belirli ikili işlemlerle donatılmış birçok farklı ve çok önemli değer kümesi gruplardır. Ancak kriptografik uygulamalar yalnızca tamsayı kümeleriyle ya da en azından tamsayılarla tanımlanan Elements ile, yani sayılar teorisinin alanı içinde çalışır. Dolayısıyla, tamsayılar dışındaki gerçek sayılara sahip kümeler kriptografik uygulamalarda kullanılmaz.


Tam sayı olmamalarına rağmen "tam sayılarla tanımlanabilen" Elements'e bir örnek vererek bitirelim. Eliptik eğrilerin noktaları buna iyi bir örnektir. Eliptik bir eğri üzerindeki herhangi bir nokta açıkça bir tamsayı olmasa da, böyle bir nokta gerçekten de iki tamsayı tarafından tanımlanır.


Örneğin eliptik eğriler Bitcoin için çok önemlidir. Herhangi bir standart Bitcoin özel ve açık anahtar çifti, aşağıdaki eliptik eğri tarafından tanımlanan noktalar kümesinden seçilir:


$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$


($2^{256}$'dan küçük en büyük asal sayı olan).


Bitcoin'teki işlemler tipik olarak çıktıların bir şekilde bir veya daha fazla açık anahtara kilitlenmesini içerir. Bu işlemlerden elde edilen değer daha sonra ilgili özel anahtarlarla dijital imzalar oluşturularak açılabilir.




## Döngüsel gruplar

<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>


Yapabileceğimiz önemli bir ayrım **sonlu** ve **sonsuz grup** arasındadır. İlki sonlu sayıda Elements'ya sahipken, ikincisi sonsuz sayıda Elements'ya sahiptir. Herhangi bir sonlu gruptaki Elements sayısı **grubun mertebesi** olarak bilinir. Grupların kullanımını içeren tüm pratik kriptografi sonlu (sayı-teorik) gruplara dayanır.


Açık anahtar kriptografisinde, döngüsel gruplar olarak bilinen sonlu Abelian gruplarının belirli bir sınıfı özellikle önemlidir. Devirli grupları anlamak için öncelikle grup elemanı üs alma kavramını anlamamız gerekir.


Bir $\circ$ grup işlemine sahip bir $G$ grubu ve $a$'nın $G$'nin bir elemanı olduğunu varsayalım. O halde $a^n$ ifadesi, $a$ elemanının kendisiyle toplam $n - 1$ kez birleştiği şeklinde yorumlanmalıdır. Örneğin, $a^2$ ifadesi $a \circ a$, $a^3$ ifadesi $a \circ a \circ a$, vb. anlamına gelir. (Buradaki üs alma işleminin standart aritmetik anlamda üs alma işlemi olmadığına dikkat edin)


Şimdi bir örneğe dönelim. Diyelim ki $G = \langle \mathbb{Z} \mod 7, + \rangle$ ve $a$ değerimizin 4'e eşit olduğunu varsayalım. Bu durumda, $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$ olur. Alternatif olarak, $a^4$, $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$ değerini temsil edecektir.


Bazı Abelian gruplarının bir veya daha fazla Elements'si vardır ve bu Elements'ler sürekli üs alma yoluyla diğer tüm grup Elements'lerini verebilir. Bu Elements'lere **jeneratörler** veya **ilkel Elements** denir.


Bu tür grupların önemli bir sınıfı $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ 'dır, burada $N$ bir asal sayıdır. Buradaki $\mathbb{Z}^*$ gösterimi, grubun $N$'den küçük tüm sıfır olmayan pozitif tam sayıları içerdiği anlamına gelir. Dolayısıyla böyle bir grup her zaman $N - 1$ Elements'e sahiptir.


Örneğin, $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$ olsun. Bu grup aşağıdaki Elements'a sahiptir: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Bu grubun mertebesi 10'dur (ki bu gerçekten de $11 - 1$'e eşittir).


Bu gruptan 2 elemanının üs alma işlemini inceleyelim. $2^{12}$'a kadar olan hesaplamalar aşağıda gösterilmiştir. Denklemin sol tarafındaki üssün grup elemanı üs alma işlemini ifade ettiğine dikkat edin. Bizim özel örneğimizde, bu gerçekten de denklemin sağ tarafında aritmetik üs alma işlemini içerir (ancak örneğin toplama işlemini de içerebilirdi). Açıklığa kavuşturmak için, sağ taraftaki üs formundan ziyade tekrarlanan işlemi yazdım.



- $2^1 = 2 \mod 11$
- $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
- $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$
- $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
- $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
- $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
- $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
- $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
- $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
- $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
- $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
- $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$


Eğer dikkatlice bakarsanız, 2. eleman üzerinde üs alma işleminin $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ 'ın tüm Elements'ları boyunca aşağıdaki sırada döndüğünü görebilirsiniz: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. $2^{10}$'dan sonra, 2 elemanının sürekli üstelleştirilmesi tüm Elements'ları tekrar ve aynı sırayla çevreler. Dolayısıyla, 2 elemanı $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ içinde bir üreteçtir.


Her ne kadar $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ çoklu üreteçlere sahip olsa da, bu grubun tüm Elements'leri üreteç değildir. Örneğin, 3 elemanını düşünün. Zahmetli hesaplamaları göstermeden ilk 10 üs alma işlemini yapmak aşağıdaki sonuçları verir:



- $3^1 = 3 \mod 11$
- $3^2 = 9 \mod 11$
- $3^3 = 5 \mod 11$
- $3^4 = 4 \mod 11$
- $3^5 = 1 \mod 11$
- $3^6 = 3 \mod 11$
- $3^7 = 9 \mod 11$
- $3^8 = 5 \mod 11$
- $3^9 = 4 \mod 11$
- $3^{10} = 1 \mod 11$


Tüm $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ değerleri arasında dolaşmak yerine, 3 elemanının üs alma işlemi yalnızca bu değerlerin bir alt kümesine yol açar: 3, 9, 5, 4 ve 1. Beşinci üs alma işleminden sonra bu değerler tekrarlanmaya başlar.


Şimdi bir **döngüsel grubu** en az bir üreteci olan herhangi bir grup olarak tanımlayabiliriz. Yani, üstelleştirme yoluyla diğer tüm Elements gruplarını üretebileceğiniz en az bir grup elemanı vardır.


Yukarıdaki örneğimizde hem $2^{10}$ hem de $3^{10}$'ın $1 \mod 11$'e eşit olduğunu fark etmişsinizdir. Aslında, hesaplamaları yapmayacak olsak da, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ grubundaki herhangi bir elemanın 10 ile üslendirilmesi $1 \mod 11$ sonucunu verecektir. Bu durum neden böyledir?


Bu önemli bir soru, ancak cevaplamak için biraz çalışmak gerekiyor.


Başlangıç olarak, $a$ ve $N$ olmak üzere iki pozitif tamsayı varsayalım. Sayılar teorisindeki önemli bir teorem, $a$ ve $N$ arasındaki en büyük ortak bölenin 1'e eşit olması durumunda $a$'nın $N$ modülünde çarpımsal bir tersinin (yani $a \cdot b = 1 \mod N$ olacak şekilde bir $b$ tamsayısının) olduğunu belirtir. Yani, $a$ ve $N$ eş asal sayılar ise.


Dolayısıyla, $N$ modulo çarpımına sahip herhangi bir tamsayı grubu için, yalnızca $N$ ile daha küçük eş asal sayılar kümeye dahil edilir. Bu kümeyi $\mathbb{Z}^c \mod N$ ile gösterebiliriz.


Örneğin, $N$ sayısının 10 olduğunu varsayalım. Sadece 1, 3, 7 ve 9 tamsayıları 10 ile eş asaldır. Yani $\mathbb{Z}^c \mod 10$ kümesi sadece $\{1, 3, 7, 9\}$ içerir. Modulo 10 tamsayı çarpımına sahip bir grubu 1 ile 10 arasındaki diğer tamsayıları kullanarak oluşturamazsınız. Bu özel grup için, tersler 1 ve 9 ve 3 ve 7 çiftleridir.


N$'nin kendisinin asal olduğu durumda, 1'den $N - 1$'e kadar olan tüm tamsayılar $N$ ile eş asaldır. Dolayısıyla böyle bir grup $N - 1$ mertebesine sahiptir. Daha önceki gösterimimizi kullanarak, $N$ asal olduğunda $\mathbb{Z}^c \mod N$ eşittir $\mathbb{Z}^* \mod N$. Daha önceki örneğimiz için seçtiğimiz grup, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, bu grup sınıfının özel bir örneğidir.


Daha sonra, $\phi(N)$ fonksiyonu bir $N$ sayısına kadar olan eş asalların sayısını hesaplar ve **Euler'in Phi fonksiyonu** olarak bilinir. [1] **Euler Teoremine** göre, $a$ ve $N$ iki tamsayı eş asal olduğunda, aşağıdaki geçerlidir:



- $a^{\phi(N)} \mod N = 1 \mod N$


Bunun, $N$'nin asal olduğu $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ grupları sınıfı için önemli bir anlamı vardır. Bu gruplar için, grup elemanı üs alma işlemi aritmetik üs alma işlemini temsil eder. Yani, $a^{\phi(N)} \mod N$, $a^{\phi(N)} \mod N$ aritmetik işlemini temsil eder. Bu çarpımsal gruplardaki herhangi bir $a$ elemanı $N$ ile asal olduğundan, $a^{\phi(N)} \mod N = a^{N - 1} \mod N = 1 \mod N$.


Euler teoremi gerçekten önemli bir sonuçtur. Başlangıç olarak, $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ içindeki tüm Elements'ün yalnızca $N - 1$'e bölünen üs alma yoluyla bir dizi değer arasında dönebileceğini ima eder. Bu, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ durumunda, her bir elemanın yalnızca 2, 5 veya 10 Elements arasında döngü yapabileceği anlamına gelir. Herhangi bir elemanın üs alma işleminden sonra çevrim yaptığı grup değerleri **elemanın mertebesi** olarak bilinir. Bir grubun mertebesine eşdeğer bir mertebeye sahip bir eleman bir üreteçtir.


Ayrıca, Euler teoremi $a^{N - 1} sonucunu her zaman bilebileceğimizi ima eder n$'nin asal olduğu herhangi bir $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ grubu için \mod N$. Bu, gerçek hesaplamaların ne kadar karmaşık olabileceğinden bağımsız olarak böyledir.


Örneğin, grubumuzun $\mathbb{Z}^* \mod 160,481,182$ olduğunu varsayalım (burada 160,481,182 gerçekten de bir asal sayıdır). 1'den 160,481,181'e kadar olan tüm tam sayıların bu grubun Elements'ü olması gerektiğini ve $\phi(n) = 160,481,181$ olduğunu biliyoruz. Hesaplamalardaki tüm adımları yapamasak da 514$^{160,481,181}$, 2,005$^{160,481,181}$ ve 256,212$^{160,481,181}$ gibi ifadelerin hepsinin $1 \mod 160,481,182$ olarak değerlendirilmesi gerektiğini biliyoruz.


**Notlar:**


[1] Fonksiyon aşağıdaki gibi çalışır. Herhangi bir $N$ tamsayısı asal sayıların çarpımına çarpanlarına ayrılabilir. Belirli bir $N$'nin aşağıdaki gibi çarpanlara ayrıldığını varsayalım: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$ burada tüm $p$'ler asal sayılardır ve tüm $e$'ler 1'e eşit veya 1'den büyük tam sayılardır:


$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$


N$'nin asal çarpanlarına ayrılması için Euler'in Phi fonksiyonu formülü.



## Alanlar

<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>


Grup, soyut cebirdeki temel cebirsel yapıdır, ancak çok daha fazlası vardır. Aşina olmanız gereken diğer tek cebirsel yapı bir **alan**, özellikle de bir **sonlu alan** yapısıdır. Bu cebirsel yapı türü, Gelişmiş Şifreleme Standardı gibi kriptografide sıklıkla kullanılır. İkincisi, pratikte karşılaşacağınız ana simetrik şifreleme şemasıdır.


Bir alan, bir grup kavramından türetilmiştir. Spesifik olarak, bir **alan** aşağıdaki koşulları sağlayan $\circ$ ve $\diamond$ ikili operatörleri ile donatılmış bir Elements **S** kümesidir:


1. $\circ$ ile donatılmış **S** kümesi bir Abelian gruptur.

2. $\diamond$ ile donatılmış **S** kümesi "sıfır olmayan" Elements için bir Abelian gruptur.

3. İki operatörle donatılmış **S** kümesi, dağılım koşulu olarak bilinen koşulu sağlamaktadır: A$, $b$ ve $c$'nin **S**'nin Elements'si olduğunu varsayalım. O zaman iki operatörle donatılmış **S**, $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$ olduğunda dağılım özelliğini karşılar.


Gruplarda olduğu gibi, alan tanımının da çok soyut olduğunu unutmayın. Bu tanım **S** içindeki Elements türleri veya $\circ$ ve $\diamond$ işlemleri hakkında hiçbir iddiada bulunmaz. Sadece bir alanın, yukarıdaki üç koşulun geçerli olduğu iki işlemli herhangi bir Elements kümesi olduğunu belirtir. (İkinci Abelian grubundaki "sıfır" elemanı soyut olarak yorumlanabilir)


Peki bir alan örneği ne olabilir? İyi bir örnek $\mathbb{Z} kümesidir \mod 7$ veya $\{0, 1, \ldots, 7\}$ standart toplama (yukarıdaki $\circ$ yerine) ve standart çarpma (yukarıdaki $\diamond$ yerine) üzerinden tanımlanır.


İlk olarak, $\mathbb{Z} \mod 7$ toplama üzerinde bir Abelian grup olma koşulunu karşılar ve yalnızca sıfır olmayan Elements'u dikkate alırsanız çarpma üzerinde bir Abelian grup olma koşulunu karşılar. İkinci olarak, kümenin iki operatörle birleşimi dağılım koşulunu karşılar.


Bu iddiaları bazı özel değerler kullanarak incelemek didaktik açıdan faydalı olacaktır. $\mathbb{Z} kümesinden rastgele seçilen bazı Elements deneysel değerleri olan 5, 2 ve 3'ü alalım \mod 7$, $\langle \mathbb{Z} alanını incelemek için \mod 7, +, \cdot \rangle$. Belirli koşulları keşfetmek için gerektiğinde bu üç değeri sırayla kullanacağız.


Önce $\mathbb{Z} olup olmadığını araştıralım \mod 7$ toplama işlemi ile donatılmış bir Abelian gruptur.


1. **Kapanış koşulu**: Değerlerimiz olarak 5 ve 2'yi alalım. Bu durumda, $[5 + 2] \mod 7 = 7 \mod 7 = 0$ olur. Bu gerçekten de $\mathbb{Z}'nin bir elemanıdır \mod 7$, dolayısıyla sonuç kapanış koşuluyla tutarlıdır.

2. **İlişkilendirme koşulu**: Değerlerimiz olarak 5, 2 ve 3'ü alalım. Bu durumda, $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$ olur. Bu, birliktelik koşulu ile tutarlıdır.

3. **Kimlik koşulu**: Değerimizi 5 olarak alalım. Bu durumda, $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$ olur. Yani 0 toplama işlemi için özdeşlik elemanı gibi görünüyor.

4. **Ters koşul**: 5'in tersini düşünün. Bazı $d$ değerleri için $[5 + d] \mod 7 = 0$ olması gerekir. Bu durumda, $\mathbb{Z}'deki tek değer bu koşulu sağlayan \mod 7$ değeri 2'dir.

5. **Bütünlük koşulu**: Değerlerimiz olarak 5 ve 3'ü alalım. Bu durumda, $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$ olur. Bu değişebilirlik koşulu ile tutarlıdır.


$\mathbb{Z} kümesi toplama ile donatılmış \mod 7$ açıkça bir Abelian grubu olarak görünür. Şimdi de $\mathbb{Z} çarpma ile donatılmış \mod 7$ sıfır olmayan tüm Elements için bir Abelian gruptur.


1. **Kapanış koşulu**: Değerlerimiz olarak 5 ve 2'yi alalım. Bu durumda, $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$ olur. Bu aynı zamanda $\mathbb{Z}'nin bir elemanıdır \mod 7$, dolayısıyla sonuç kapanış koşuluyla tutarlıdır.

2. **İlişkilendirme koşulu**: Değerlerimiz olarak 5, 2 ve 3'ü alalım. Bu durumda, $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$ olur. Bu, birliktelik koşulu ile tutarlıdır.

3. **Kimlik koşulu**: Değerimizi 5 olarak alalım. Bu durumda, $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$ olur. Yani 1 çarpma işlemi için özdeşlik elemanı gibi görünüyor.

4. **Ters koşul**: 5'in tersini düşünün. Bazı $d$ değerleri için $[5 \cdot d] \mod 7 = 1$ olması gerekir. Tek değer $\mathbb{Z} bu koşulu sağlayan \mod 7$ 3'tür. Bu, ters koşulla tutarlıdır.

5. **Bütünlük koşulu**: Değerlerimiz olarak 5 ve 3'ü alalım. Bu durumda, $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$ olur. Bu, değişebilirlik koşulu ile tutarlıdır.


$\mathbb{Z} kümesi \mod 7$, sıfır olmayan Elements üzerinde toplama veya çarpma ile birleştirildiğinde bir Abelian grubu olma kurallarını açıkça karşılıyor gibi görünüyor.


Son olarak, her iki operatörle birleştirilen bu küme dağılım koşulunu karşılıyor gibi görünmektedir. Değerlerimiz olarak 5, 2 ve 3'ü alalım. Görüyoruz ki $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.


Şimdi gördük ki $\mathbb{Z} toplama ve çarpma ile donatılmış \mod 7$ belirli değerlerle test edildiğinde sonlu bir cisim için aksiyomları karşılar. Elbette bunu genel olarak da gösterebiliriz, ancak burada bunu yapmayacağız.


İki tür alan arasında önemli bir ayrım vardır: sonlu ve sonsuz alanlar.


Bir **sonsuz alan**, **S** kümesinin sonsuz büyük olduğu bir alanı içerir. Toplama ve çarpma ile donatılmış $\mathbb{R}$ reel sayılar kümesi sonsuz bir alan örneğidir. Bir **Galois alanı** olarak da bilinen bir **sonlu alan**, **S** kümesinin sonlu olduğu bir alandır. Yukarıdaki $\langle \mathbb{Z} örneğimiz \mod 7, +, \cdot \rangle$ sonlu bir cisimdir.


Kriptografide, öncelikle sonlu alanlarla ilgileniriz. Genel olarak, sonlu bir alanın bazı Elements **S** kümeleri için ancak ve ancak $p^m$ Elements'e sahipse var olduğu gösterilebilir; burada $p$ bir asal sayı ve $m$ birden büyük veya eşit bir pozitif tamsayıdır. Başka bir deyişle, eğer **S** kümesinin mertebesi bir asal sayı ($m = 1$ ise $p^m$) veya bir asal kuvvet ($m > 1$ ise $p^m$) ise, o zaman $\circ$ ve $\diamond$ olmak üzere iki operatör bulabilirsiniz, böylece bir alan için koşullar sağlanmış olur.


Eğer bir sonlu cisim asal sayıda Elements'e sahipse, bu cisme **asal cisim** denir. Eğer sonlu cisimdeki Elements sayısı bir asal kuvvet ise, o zaman cisim **genişleme cismi** olarak adlandırılır. Kriptografide, hem asal hem de uzantı alanlarıyla ilgileniriz. [2]


Kriptografide ilgi çeken ana asal alanlar, tüm tamsayılar kümesinin bazı asal sayılar tarafından modüle edildiği ve operatörlerin standart toplama ve çarpma olduğu alanlardır. Bu sonlu cisimler sınıfı $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$, ve böyle devam eder. Herhangi bir asal cisim için $\mathbb{Z} \mod p$, alanının tamsayılar kümesi aşağıdaki gibidir: $\{0, 1, \ldots, p - 2, p - 1\}$.


Kriptografide, uzantı alanlarıyla, özellikle de $m > 1$ olan $2^m$ Elements alanlarıyla da ilgileniyoruz. Bu tür sonlu alanlar, örneğin, Gelişmiş Şifreleme Standardının temelini oluşturan Rijndael Şifresinde kullanılır. Asal alanlar nispeten sezgisel olsa da, bu taban 2 uzantılı alanlar muhtemelen soyut cebire aşina olmayanlar için uygun değildir.


Başlangıç olarak, $2^m$ Elements olan herhangi bir tamsayı kümesine, kombinasyonlarını bir alan yapacak iki operatör atanabileceği gerçekten doğrudur ($m$ pozitif bir tamsayı olduğu sürece). Ancak, bir alanın var olması, keşfedilmesinin kolay olduğu ya da belirli uygulamalar için özellikle pratik olduğu anlamına gelmez.


Anlaşıldığı üzere, kriptografide $2^m$ 'nin özellikle uygulanabilir uzantı alanları, bazı tamsayı kümeleri yerine belirli polinom ifadeleri kümeleri üzerinde tanımlananlardır.


Örneğin, kümesinde $2^3$ (yani 8) Elements olan bir uzantı alanı istediğimizi varsayalım. Bu büyüklükteki alanlar için kullanılabilecek birçok farklı küme olsa da, böyle bir küme $a_2x^2 + a_1x + a_0$ biçimindeki tüm benzersiz polinomları içerir, burada her bir $a_i$ katsayısı ya 0 ya da 1'dir. Dolayısıyla, bu küme **S** aşağıdaki Elements'yi içerir:


1. $0$: A_2 = 0$, $a_1 = 0$ ve $a_0 = 0$ olduğu durum.

2. $1$: A_2 = 0$, $a_1 = 0$ ve $a_0 = 1$ olduğu durum.

3. $x$: A_2 = 0$, $a_1 = 1$ ve $a_0 = 0$ olduğu durum.

4. $x + 1$: A_2 = 0$, $a_1 = 1$ ve $a_0 = 1$ olduğu durum.

5. $x^2$: A_2 = 1$, $a_1 = 0$ ve $a_0 = 0$ olduğu durum.

6. $x^2 + 1$: A_2 = 1$, $a_1 = 0$ ve $a_0 = 1$ olduğu durum.

7. x^2 + x$: A_2 = 1$, $a_1 = 1$ ve $a_0 = 0$ olduğu durum.

8. x^2 + x + 1$: A_2 = 1$, $a_1 = 1$ ve $a_0 = 1$ olduğu durum.


Yani **S** $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$ kümesi olacaktır. Kombinasyonlarının bir cisim olmasını sağlamak için bu Elements kümesi üzerinde hangi iki işlem tanımlanabilir?


**S** kümesi ($\circ$) üzerindeki ilk işlem standart polinom toplama modulo 2 olarak tanımlanabilir. Tek yapmanız gereken polinomları normalde yaptığınız gibi toplamak ve ardından elde edilen polinomun katsayılarının her birine modulo 2'yi uygulamaktır. İşte bazı örnekler:



- $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
- $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
- $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$


Alan oluşturmak için gerekli olan **S** ($\diamond$) kümesi üzerindeki ikinci işlem daha karmaşıktır. Bu bir tür çarpma işlemidir, ancak aritmetiğin standart çarpma işlemi değildir. Bunun yerine, her bir elemanı bir vektör olarak görmeli ve işlemi bu iki vektörün indirgenemez bir polinom modülünde çarpımı olarak anlamalısınız.


İlk olarak indirgenemez polinom fikrine dönelim. **İndirgenemez bir polinom** çarpanlarına ayrılamayan bir polinomdur (tıpkı bir asal sayının 1 ve asal sayının kendisi dışındaki bileşenlerine ayrılamaması gibi). Amaçlarımız doğrultusunda, tüm tam sayılar kümesine göre indirgenemeyen polinomlarla ilgileniyoruz. (Bazı polinomları tamsayılarla çarpanlarına ayıramasanız bile, örneğin reel veya karmaşık sayılarla çarpanlarına ayırabileceğinizi unutmayın)


Örneğin, $x^2 - 3x + 2$ polinomunu düşünün. Bu, $(x - 1)(x - 2)$ olarak yeniden yazılabilir. Dolayısıyla, bu indirgenemez değildir. Şimdi $x^2 + 1$ polinomunu ele alalım. Sadece tamsayıları kullanarak bu ifadeyi daha fazla çarpanlarına ayırmanın bir yolu yoktur. Dolayısıyla, bu tamsayılara göre indirgenemez bir polinomdur.


Daha sonra, vektör çarpımı kavramına dönelim. Bu konuyu derinlemesine incelemeyeceğiz, ancak sadece temel bir kuralı anlamanız gerekiyor: Herhangi bir vektör bölme işlemi, bölenin derecesi böleninkine eşit ya da daha yüksek olduğu sürece gerçekleşebilir. Eğer bölünen, bölenin derecesinden daha düşük bir dereceye sahipse, o zaman bölünen artık bölen tarafından bölünemez.


Örneğin, $x^6 + x + 1 \mod x^5 + x^2$ ifadesini düşünün. Bölen 6'nın derecesi bölen 5'in derecesinden yüksek olduğu için bu açıkça daha da azalır. Şimdi $x^5 + x + 1 \mod x^5 + x^2$ ifadesini düşünün. Bölen 5'in derecesi ile bölen 5'in derecesi eşit olduğu için bu da daha da azalır.


Ancak, şimdi $x^4 + x + 1 \mod x^5 + x^2$ ifadesini düşünün. Bölenin derecesi olan 4, bölenin derecesi olan 5'ten düşük olduğu için bu ifade daha fazla küçülmez.


Bu bilgilere dayanarak, artık $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$ kümesi için ikinci işlemimizi bulmaya hazırız.


İkinci işlemin bazı indirgenemez polinomların modulo vektör çarpımı olarak anlaşılması gerektiğini söylemiştim. Bu indirgenemez polinom, ikinci işlemin **S** üzerinde bir Abelian grubu tanımlamasını ve dağılım koşuluyla tutarlı olmasını sağlamalıdır. Peki bu indirgenemez polinom ne olmalıdır?


Kümedeki tüm vektörler 2 veya daha düşük dereceli olduğundan, indirgenemez polinom 3 dereceli olmalıdır. Kümedeki iki vektörün herhangi bir çarpımı 3 veya daha yüksek dereceli bir polinom veriyorsa, 3 dereceli bir polinomun modülünün her zaman 2 veya daha düşük dereceli bir polinom verdiğini biliyoruz. Bunun nedeni, 3. derece veya daha yüksek dereceli herhangi bir polinomun her zaman 3. dereceden bir polinoma bölünebilir olmasıdır. Ayrıca, bölen olarak işlev gören polinom indirgenemez olmalıdır.


Bölenimiz olarak kullanabileceğimiz 3. dereceden birkaç indirgenemez polinom olduğu ortaya çıktı. Bu polinomların her biri **S** kümemiz ve toplama modulo 2 ile birlikte farklı bir alan tanımlar. Bu, kriptografide $2^m$ uzantılı alanları kullanırken birden fazla seçeneğiniz olduğu anlamına gelir.


Örneğimiz için $x^3 + x + 1$ polinomunu seçtiğimizi varsayalım. Bu gerçekten de indirgenemezdir, çünkü tamsayıları kullanarak çarpanlarına ayıramazsınız. Buna ek olarak, iki Elements'un herhangi bir çarpımının 2 veya daha düşük dereceli bir polinom vermesini sağlayacaktır.


Nasıl çalıştığını göstermek için bölen olarak $x^3 + x + 1$ polinomunu kullanarak ikinci işlemin bir örneği üzerinde çalışalım. Kümemiz **S**'deki Elements $x^2 + 1$ ile $x^2 + x$'i çarptığınızı varsayalım. O zaman, $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$ ifadesini hesaplamamız gerekir. Bu aşağıdaki gibi basitleştirilebilir:



- $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
- $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
- $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$


Biliyoruz ki $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ bölenin derecesi (4) bölenin derecesinden (3) daha yüksek olduğu için indirgenebilir.


Başlangıç olarak, $x^3 + x + 1$ ifadesinin $x^4 + x^3 + x^2 + x$ ifadesine toplam $x$ kez girdiğini görebilirsiniz. Bunu $x^3 + x + 1$ ifadesini $x^4 + x^2 + x$ olan $x$ ile çarparak doğrulayabilirsiniz. Son terim kar payı ile aynı dereceden, yani 4 olduğundan, bunun işe yaradığını biliyoruz. Bu bölme işleminin $x$ ile kalanını aşağıdaki gibi hesaplayabilirsiniz:



- $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
- $[x^3] \mod x^3 + x + 1 =$
- $x^3$


Yani $x^4 + x^3 + x^2 + x$'i $x^3 + x + 1$'e toplam $x$ kez böldükten sonra $x^3$ kalanımız var. Bu $x^3 + x + 1$ ile daha fazla bölünebilir mi?


Sezgisel olarak, $x^3$'ün artık $x^3 + x + 1$'e bölünemeyeceğini söylemek cazip gelebilir, çünkü ikinci terim daha büyük görünmektedir. Ancak, daha önce vektör bölme üzerine yaptığımız tartışmayı hatırlayın. Bölenin derecesi bölenin derecesine eşit veya daha büyük olduğu sürece, ifade daha da küçültülebilir. Özellikle, $x^3 + x + 1$ ifadesi $x^3$ ifadesine tam olarak 1 kez girebilir. Kalan aşağıdaki gibi hesaplanır:


$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$


Neden $-x - 1$ değil de $(x^3) - (x^3 + x + 1)$ değerinin $x + 1$ olduğunu merak ediyor olabilirsiniz. Alanımızın ilk işleminin modulo 2 olarak tanımlandığını hatırlayın. Dolayısıyla, iki vektörün çıkarılması, iki vektörün toplanmasıyla tamamen aynı sonucu verir.


X^2 + 1$ ve $x^2 + x$ çarpımlarını özetlemek gerekirse: Bu iki terimi çarptığınızda 4. derece bir polinom elde edersiniz, $x^4 + x^3 + x^2 + x$, bu polinomun $x^3 + x + 1$ modülüne indirgenmesi gerekir. 4. derece polinom $x^3 + x + 1$ ile tam olarak $x + 1$ kez bölünebilir. X^4 + x^3 + x^2 + x$ 'in $x^3 + x + 1$ 'e tam olarak $x + 1$ kez bölünmesinden sonra kalan $x + 1$ 'dir. Bu gerçekten de $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$ kümemizin bir elemanıdır.


Yukarıdaki örnekte olduğu gibi polinom kümeleri üzerinde 2 tabanına sahip uzantı alanları kriptografi için neden yararlı olsun? Bunun nedeni, bu tür kümelerin polinomlarındaki katsayıları, 0 veya 1, belirli bir uzunluğa sahip ikili dizelerin Elements'i olarak görebilmenizdir. Örneğin yukarıdaki örneğimizdeki **S** kümesi, bunun yerine 3 uzunluğundaki (000 ile 111 arası) tüm ikili dizeleri içeren bir **S** kümesi olarak görülebilir. O halde **S** üzerindeki işlemler, bu ikili dizgeler üzerinde işlemler gerçekleştirmek ve aynı uzunlukta bir ikili dizge üretmek için de kullanılabilir.


**Notlar:**


[2] Uzantı alanları çok mantıksız hale gelir. Tam sayılardan oluşan Elements yerine, polinom kümelerine sahiptirler. Buna ek olarak, herhangi bir işlem indirgenemez bir polinomun modülasyonu ile gerçekleştirilir.



## Uygulamada soyut cebir

<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>


Tartışmanın resmi diline ve soyutluğuna rağmen, bir grup kavramını kavramak çok zor olmamalıdır. Bu sadece bir ikili işlemle birlikte bir Elements kümesidir ve bu ikili işlemin bu Elements üzerindeki performansı dört genel koşulu karşılar. Bir Abelian grubunun sadece değişebilirlik olarak bilinen ekstra bir koşulu vardır. Döngüsel bir grup ise Abelyen grubun özel bir türüdür, yani bir üreteci olan bir gruptur. Bir alan sadece temel grup kavramından daha karmaşık bir yapıdır.


Ancak pratik eğilimli biriyseniz, bu noktada merak edebilirsiniz: Kimin umurunda? Bir operatöre sahip bazı Elements kümelerinin bir grup, hatta bir Abelian veya döngüsel grup olduğunu bilmenin gerçek dünyayla bir ilgisi var mı? Bir şeyin bir alan olduğunu bilmenin?


Çok fazla ayrıntıya girmeden, cevap "evet". Gruplar ilk olarak 19. yüzyılda Fransız matematikçi Evariste Galois tarafından oluşturulmuştur. Galois bu grupları, derecesi beşten büyük olan polinom denklemlerinin çözümü hakkında sonuçlar çıkarmak için kullanmıştır.


O zamandan beri grup kavramı matematikte ve başka alanlarda bir dizi soruna ışık tutmaya yardımcı olmuştur. Örneğin fizikçi Murray-Gellman, grup teorisine dayanarak bir parçacığın varlığını deneylerde gözlemlenmeden önce tahmin edebilmiştir. [3] Bir başka örnek olarak, kimyagerler moleküllerin şekillerini sınıflandırmak için grup teorisini kullanmaktadır. Hatta matematikçiler duvar kağıdı gibi somut bir şey hakkında sonuç çıkarmak için grup kavramını kullanmışlardır!


Esasen, bazı operatörlerle bir Elements kümesinin bir grup olduğunu göstermek, tanımladığınız şeyin belirli bir simetriye sahip olduğu anlamına gelir. Kelimenin genel anlamıyla bir simetri değil, daha soyut bir biçimde. Bu da belirli sistemler ve problemler hakkında önemli bilgiler sağlayabilir. Soyut cebirden gelen daha karmaşık kavramlar bize sadece ek bilgi verir.


En önemlisi, sayı teorisi gruplarının ve alanlarının pratikteki önemini kriptografideki, özellikle de açık anahtar kriptografisindeki uygulamaları aracılığıyla göreceksiniz. Alanlarla ilgili tartışmamızda, örneğin, uzantı alanlarının Rijndael Şifresinde nasıl kullanıldığını zaten görmüştük. Bu örneği *Bölüm 5*'da inceleyeceğiz.


Soyut cebir üzerine daha fazla tartışma için Socratica'nın soyut cebir üzerine hazırladığı mükemmel video serisini tavsiye ederim. [4] Özellikle aşağıdaki videoları tavsiye ederim: "Soyut cebir nedir?", "Grup tanımı (genişletilmiş)", "Halka tanımı (genişletilmiş)" ve "Alan tanımı (genişletilmiş)." Bu dört video size yukarıdaki tartışmanın büyük bir kısmı hakkında ek fikir verecektir. (Halkaları tartışmadık, ancak bir alan halkanın sadece özel bir türüdür)


Modern sayı teorisi hakkında daha fazla tartışma için kriptografi üzerine birçok ileri düzey tartışmaya başvurabilirsiniz. Daha fazla tartışma için Jonathan Katz ve Yehuda Lindell'in Introduction to Modern Cryptography ya da Christof Paar ve Jan Pelzl'in Understanding Cryptography adlı kitaplarını öneriyorum. [5]


**Notlar:**


[3] Bkz [YouTube Video](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)


[4] Socratica, [Soyut Cebir](https://www.socratica.com/subject/abstract-algebra)


[5] Katz ve Lindell, *Introduction to Modern Cryptography*, 2nd edn, 2015 (CRC Press: Boca Raton, FL). Paar ve Pelzl, *Understanding Cryptography*, 2010 (Springer-Verlag: Berlin).




# Simetrik Kriptografi

<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>



## Alice ve Bob

<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>


Kriptografinin iki ana dalından biri simetrik kriptografidir. Şifreleme şemalarının yanı sıra kimlik doğrulama ve bütünlük ile ilgili şemaları da içerir. 1970'lere kadar kriptografinin tamamı simetrik şifreleme şemalarından oluşmaktaydı.


Ana tartışma simetrik şifreleme şemalarına bakarak ve akış şifreleri ile blok şifreler arasındaki önemli ayrımı yaparak başlamaktadır. Daha sonra, mesaj bütünlüğünü ve gerçekliğini sağlamaya yönelik şemalar olan mesaj kimlik doğrulama kodlarına dönüyoruz. Son olarak, simetrik şifreleme şemalarının ve mesaj kimlik doğrulama kodlarının güvenli iletişimi sağlamak için nasıl birleştirilebileceğini araştırıyoruz.


Bu bölümde uygulamadan çeşitli simetrik şifreleme şemaları ele alınmaktadır. Bir sonraki bölüm, sırasıyla RC4 ve AES olmak üzere uygulamadan bir akış şifreleme ve bir blok şifreleme ile şifrelemenin ayrıntılı bir açıklamasını sunmaktadır.


Simetrik kriptografi hakkındaki tartışmamıza başlamadan önce, bu ve sonraki bölümlerde yer alan Alice ve Bob örnekleriyle ilgili kısaca bazı açıklamalar yapmak istiyorum.


___


Kriptografi prensiplerini açıklarken insanlar genellikle Alice ve Bob ile ilgili örneklere başvururlar. Ben de öyle yapacağım.


Özellikle kriptografide yeniyseniz, bu Alice ve Bob örneklerinin yalnızca kriptografik ilke ve yapıların basitleştirilmiş bir ortamda gösterilmesi amacıyla verildiğinin farkında olmanız önemlidir. Ancak bu ilkeler ve yapılar çok daha geniş bir yelpazedeki gerçek yaşam bağlamlarına uygulanabilir.


Aşağıda, kriptografide Alice ve Bob'i içeren örnekler hakkında akılda tutulması gereken beş önemli nokta yer almaktadır:


1. Bunlar, şirketler veya kamu kuruluşları gibi diğer aktör türleriyle ilgili örneklere kolayca tercüme edilebilir.

2. Üç veya daha fazla aktörü içerecek şekilde kolayca genişletilebilirler.

3. Örneklerde, Bob ve Alice tipik olarak her bir mesajın oluşturulmasında ve bu mesaj üzerinde kriptografik şemaların uygulanmasında aktif katılımcılardır. Ancak gerçekte elektronik iletişim büyük ölçüde otomatiktir. Örneğin, Layer aktarım güvenliğini kullanan bir web sitesini ziyaret ettiğinizde, kriptografi genellikle bilgisayarınız ve web sunucusu tarafından gerçekleştirilir.

4. Elektronik iletişim bağlamında, bir iletişim kanalı üzerinden gönderilen "mesajlar" genellikle TCP/IP paketleridir. Bunlar bir e-postaya, bir Facebook mesajına, bir telefon görüşmesine, bir dosya aktarımına, bir web sitesine, bir yazılım yüklemesine vb. ait olabilir. Bunlar geleneksel anlamda mesaj değildir. Bununla birlikte, kriptograflar genellikle mesajın örneğin bir e-posta olduğunu belirterek bu gerçeği basitleştireceklerdir.

5. Örnekler genellikle elektronik iletişime odaklanır, ancak mektuplar gibi geleneksel iletişim biçimlerine de genişletilebilirler.



## Simetrik şifreleme şemaları

<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>


Bir **simetrik şifreleme şemasını** gevşek bir şekilde üç algoritmalı herhangi bir şifreleme şeması olarak tanımlayabiliriz:


1. Özel bir anahtar oluşturan bir **anahtar oluşturma algoritması**.

2. Özel anahtarı ve bir düz metni girdi olarak alan ve bir şifreli metin çıktısı veren bir **şifreleme algoritması**.

3. Özel anahtarı ve şifreli metni girdi olarak alan ve orijinal düz metni çıktı olarak veren bir **şifre çözme algoritması**.


Tipik olarak bir şifreleme şeması - ister simetrik ister asimetrik olsun - kesin bir spesifikasyondan ziyade temel bir algoritmaya dayalı şifreleme için bir şablon sunar.


Örneğin, simetrik bir şifreleme şeması olan Salsa20'yi düşünün. Hem 128 hem de 256 bit anahtar uzunlukları ile kullanılabilir. Anahtar uzunluğuna ilişkin seçim, algoritmanın bazı küçük ayrıntılarını etkiler (tam olarak algoritmadaki tur sayısı).


Ancak Salsa20'yi 128 bit anahtarla kullanmanın, Salsa20'yi 256 bit anahtarla kullanmaktan farklı bir şifreleme şeması olduğu söylenemez. Çekirdek algoritma aynı kalır. Sadece çekirdek algoritma değiştiğinde gerçekten iki farklı şifreleme şemasından bahsedebiliriz.


Simetrik şifreleme şemaları tipik olarak iki tür durumda kullanışlıdır: (1) İki veya daha fazla aracının uzaktan iletişim kurduğu ve iletişimlerinin içeriğini gizli tutmak istediği durumlar; ve (2) bir aracının bir mesajın içeriğini zaman içinde gizli tutmak istediği durumlar.


Durum (1)'in bir tasvirini aşağıdaki *Şekil 1*'de görebilirsiniz. Bob, Alice'a uzak mesafeden bir $M$ mesajı göndermek istiyor, ancak başkalarının bu mesajı okuyabilmesini istemiyor.


Bob ilk olarak $M$ mesajını $K$ özel anahtarı ile şifreler. Daha sonra $C$ şifreli metnini Alice'e gönderir. Alice şifreli metni aldıktan sonra $K$ anahtarını kullanarak şifresini çözebilir ve düz metni okuyabilir. İyi bir şifreleme şemasıyla, $C$ şifreli metnini ele geçiren herhangi bir saldırganın $M$ mesajı hakkında gerçek bir öneme sahip hiçbir şey öğrenememesi gerekir.


Aşağıdaki *Şekil 2*'de (2) numaralı durumun bir tasvirini görebilirsiniz. Bob başkalarının belirli bilgileri görüntülemesini engellemek istiyor. Tipik bir durum, Bob'ün bilgisayarında ne yabancıların ne de iş arkadaşlarının okumaması gereken hassas verileri depolayan bir çalışan olması olabilir.


Bob $M$ mesajını $T_0$ zamanında $K$ anahtarı ile şifreleyerek $C$ şifreli metnini üretir. T_1$ zamanında mesaja tekrar ihtiyaç duyar ve $K$ anahtarı ile $C$ şifreli metninin şifresini çözer. Bu sırada $C$ şifreli metnine rastlamış olabilecek herhangi bir saldırgan, bu metinden $M$ hakkında önemli bir şey çıkaramamış olmalıdır.



*Şekil 1: Uzayda gizlilik*


![Figure 1: Secrecy across space](assets/Figure4-1.webp "Figure 1: Secrecy across space")



*Şekil 2: Zaman içinde gizlilik*



![Figure 2: Secrecy across time](assets/Figure4-2.webp "Figure 2: Secrecy across time")




## Bir örnek: Kaydırma şifresi

<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>


Bölüm 2'de, çok basit bir simetrik şifreleme şeması örneği olan kaydırmalı şifreleme ile karşılaşmıştık. Burada tekrar bakalım.


İngiliz alfabesindeki tüm harfleri sırayla $\{0,1,2,\dots,25\}$ sayı kümesine eşitleyen bir *D* sözlüğü varsayalım. Bir dizi olası mesaj **M** olduğunu varsayalım. O halde kaydırmalı şifre aşağıdaki gibi tanımlanan bir şifreleme şemasıdır:



- Olası anahtarlar **K** kümesinden rastgele bir $k$ anahtarı seçin; burada **K** = $\{0,1,2,\dots,25\}$
- Bir $m \in$ **M** mesajını aşağıdaki gibi şifreleyin:
    - M$'yi kendi içinde $m_0, m_1,\dots, m_i, \dots, m_l$ harflerine ayırın
    - Her $m_i$'yi *D*'ye göre bir sayıya dönüştürün
    - Her $m_i$ için, $c_i = [(m_i + k) \mod 26]$
    - Her $c_i$'yi *D*'ye göre bir harfe dönüştürün
    - Daha sonra $c_0, c_1,\dots, c_l$ birleştirilerek $c$ şifreli metni elde edilir
- Bir $c$ şifreli metninin şifresini aşağıdaki gibi çözün:
    - Her $c_i$'yi *D*'ye göre bir sayıya dönüştürün
    - Her $c_i$ için, $m_i = [(c_i - k) \mod 26]$
    - Her $m_i$'yi *D*'ye göre bir harfe dönüştürün
    - Daha sonra $m_0, m_1,\dots, m_l$ birleştirilerek orijinal mesaj $m$ elde edilir


Kaydırmalı şifreyi simetrik bir şifreleme şeması yapan şey, hem şifreleme hem de şifre çözme işlemi için aynı anahtarın kullanılmasıdır. Örneğin, "DOG" mesajını kaydırmalı şifre kullanarak şifrelemek istediğinizi ve anahtar olarak rastgele "24" seçtiğinizi varsayalım. Mesajı bu anahtarla şifrelediğinizde "BME" ortaya çıkacaktır. Orijinal mesajı geri almanın tek yolu, şifre çözme işlemi için aynı anahtarı, "24", kullanmaktır.


Bu Shift şifresi bir **monoalfabetik ikame şifresi** örneğidir: şifreli metin alfabesinin sabit olduğu (yani yalnızca tek bir alfabenin kullanıldığı) bir şifreleme şeması. Şifre çözme algoritmasının deterministik olduğu varsayılırsa, ikame şifreli metindeki her bir sembol, düz metindeki en fazla bir sembole karşılık gelebilir.


1700'lere kadar birçok şifreleme uygulaması büyük ölçüde monoalfabetik ikame şifrelere dayanıyordu, ancak bunlar genellikle Shift şifresinden çok daha karmaşıktı. Örneğin, her harfin şifreli metin alfabesinde yalnızca bir kez geçmesi kısıtlaması altında her orijinal metin harfi için alfabeden rastgele bir harf seçebilirsiniz. Bu da faktöriyel 26 olası özel anahtara sahip olacağınız anlamına gelir ki bilgisayar öncesi çağda bu çok büyük bir rakamdı.


Kriptografide **şifreleme** terimiyle çok karşılaşacağınızı unutmayın. Bu terimin çeşitli anlamları olduğunu unutmayın. Aslında, kriptografi içinde bu terimin en az beş farklı anlamını biliyorum.


Bazı durumlarda, Shift cipher ve monoalphabetic substitution cipher'da olduğu gibi bir şifreleme şemasını ifade eder. Bununla birlikte, terim aynı zamanda şifreleme algoritmasına, özel anahtara veya bu tür bir şifreleme şemasının sadece şifreli metnine de atıfta bulunabilir.


Son olarak, şifre terimi, kriptografik şemalar oluşturabileceğiniz temel bir algoritmayı da ifade edebilir. Bunlar çeşitli şifreleme algoritmalarının yanı sıra diğer kriptografik şema türlerini de içerebilir. Terimin bu anlamı blok şifreler bağlamında önem kazanır (aşağıdaki "Blok Şifreler" bölümüne bakınız).


Ayrıca **şifreleme** veya **şifre çözme** terimleriyle de karşılaşabilirsiniz. Bu terimler yalnızca şifreleme ve şifre çözmenin eşanlamlılarıdır.



## Kaba kuvvet saldırıları ve Kerckhoff prensibi

<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>


Kaydırmalı şifre, en azından modern dünyada, çok güvensiz bir simetrik şifreleme şemasıdır. [1] Bir saldırgan, hangi sonucun mantıklı olduğunu görmek için 26 olası anahtarın tümüyle herhangi bir şifreli metnin şifresini çözmeyi deneyebilir. Saldırganın neyin işe yaradığını görmek için anahtarlar arasında dolaştığı bu saldırı türü **brute force attack** veya **exhaustive key search** olarak bilinir.


Herhangi bir şifreleme şemasının asgari bir güvenlik kavramını karşılaması için, kaba kuvvet saldırılarının mümkün olmadığı kadar büyük bir olası anahtarlar kümesine veya **anahtar uzayına** sahip olması gerekir. Tüm modern şifreleme şemaları bu standardı karşılar. Bu **yeterli anahtar alanı ilkesi** olarak bilinir. Benzer bir ilke tipik olarak farklı kriptografik şemalarda da geçerlidir.


Modern şifreleme şemalarındaki büyük anahtar alanı boyutu hakkında bir fikir edinmek için, bir dosyanın gelişmiş şifreleme standardı kullanılarak 128 bitlik bir anahtarla şifrelendiğini varsayalım. Bu, bir saldırganın kaba kuvvet saldırısı için içinden geçmesi gereken bir dizi $2^{128}$ anahtara sahip olduğu anlamına gelir. Bu strateji ile %0,78'lik bir başarı şansı, saldırganın kabaca 2,65 \times 10^{36}$ anahtar üzerinden döngü yapmasını gerektirecektir.


İyimser olarak bir saldırganın saniyede 10^{16}$ anahtar deneyebileceğini varsayalım (yani saniyede 10 katrilyon anahtar). Anahtar alanındaki tüm anahtarların %0,78'ini test etmek için saldırısının 2,65 \times 10^{20}$ saniye sürmesi gerekir. Bu da yaklaşık 8,4 trilyon yıl eder. Dolayısıyla, saçma derecede güçlü bir düşman tarafından yapılacak kaba kuvvet saldırısı bile 128 bitlik modern bir şifreleme şeması için gerçekçi değildir. Bu, yeterli anahtar alanı prensibidir.


Saldırgan şifreleme algoritmasını bilmiyorsa kaydırma şifresi daha mı güvenlidir? Belki, ama çok fazla değil.


Her durumda, modern kriptografi, her zaman herhangi bir simetrik şifreleme şemasının güvenliğinin yalnızca özel anahtarın gizli tutulmasına bağlı olduğunu varsayar. Saldırganın her zaman mesaj uzayı, anahtar uzayı, şifreli metin uzayı, anahtar seçim algoritması, şifreleme algoritması ve şifre çözme algoritması dahil olmak üzere diğer tüm ayrıntıları bildiği varsayılır.


Bir simetrik şifreleme şemasının güvenliğinin yalnızca özel anahtarın gizliliğine bağlı olabileceği fikri **Kerckhoffs ilkesi** olarak bilinir.


Kerckhoffs tarafından başlangıçta amaçlandığı gibi, ilke yalnızca simetrik şifreleme şemaları için geçerlidir. Ancak ilkenin daha genel bir versiyonu günümüzün diğer tüm kriptografik şemaları için de geçerlidir: Herhangi bir kriptografik şemanın güvenli olması için tasarımının gizli olması gerekmez; gizlilik yalnızca bazı bilgi dizilerine (dizilerine), tipik olarak özel bir anahtara kadar uzanabilir.


Kerckhoffs'un prensibi dört nedenden ötürü modern kriptografinin merkezinde yer almaktadır. [2] İlk olarak, belirli uygulama türleri için yalnızca sınırlı sayıda kriptografik şema vardır. Örneğin, çoğu modern simetrik şifreleme uygulaması Rijndael şifresini kullanır. Dolayısıyla bir şemanın tasarımına ilişkin gizliliğiniz çok sınırlıdır. Bununla birlikte, Rijndael şifresi için bazı özel anahtarları gizli tutma konusunda çok daha fazla esneklik vardır.


İkincisi, bazı bilgi dizilerini değiştirmek tüm bir şifreleme şemasını değiştirmekten daha kolaydır. Bir şirketin tüm çalışanlarının aynı şifreleme yazılımına sahip olduğunu ve her iki çalışanın da gizli iletişim kurmak için özel bir anahtara sahip olduğunu varsayalım. Bu senaryoda anahtarların ele geçirilmesi bir sorun teşkil eder, ancak en azından şirket bu tür güvenlik ihlallerine rağmen yazılımı elinde tutabilir. Eğer şirket planın gizliliğine güveniyor olsaydı, bu gizliliğin herhangi bir şekilde ihlal edilmesi tüm yazılımın değiştirilmesini gerektirirdi.


Üçüncü olarak, Kerckhoffs'un prensibi kriptografik şemaların kullanıcıları arasında standardizasyon ve uyumluluk sağlar. Bunun verimlilik açısından büyük faydaları vardır. Örneğin, bu güvenlik kriptografik şemaların gizli tutulmasını gerektirseydi, milyonlarca insanın her gün Google'ın web sunucularına nasıl güvenli bir şekilde bağlanabileceğini hayal etmek zordur.


Dördüncüsü, Kerckhoff'un ilkesi kriptografik şemaların kamuya açık bir şekilde incelenmesine olanak tanır. Bu tür bir inceleme, güvenli kriptografik şemalar elde etmek için kesinlikle gereklidir. Örnek olarak, simetrik kriptografinin ana çekirdek algoritması olan Rijndael şifresi, 1997 ve 2000 yılları arasında Ulusal Standartlar ve Teknoloji Enstitüsü tarafından düzenlenen bir yarışmanın sonucuydu.


Belirsizlik yoluyla **güvenlik** elde etmeye çalışan herhangi bir sistem, tasarımının ve/veya uygulamasının ayrıntılarını gizli tutmaya dayanan bir sistemdir. Kriptografide bu, özellikle kriptografik şemanın tasarım detaylarını gizli tutmaya dayanan bir sistem olacaktır. Dolayısıyla, gizlilik yoluyla güvenlik Kerckhoffs'un prensibine doğrudan zıttır.


Açıklığın kalite ve güvenliği destekleme kabiliyeti dijital dünyada kriptografiden daha geniş bir alana yayılmaktadır. Örneğin Debian gibi özgür ve açık kaynaklı Linux dağıtımları gizlilik, istikrar, güvenlik ve esneklik açısından Windows ve MacOS muadillerine göre genellikle çeşitli avantajlara sahiptir. Bunun birden fazla nedeni olsa da, en önemli ilke muhtemelen Eric Raymond'un ünlü makalesi "The Cathedral and the Bazaar "da ifade ettiği gibi, "yeterli gözbebeği verildiğinde, tüm hatalar sığdır" [3] Linux'a en önemli başarısını kazandıran da işte bu kalabalıkların bilgeliği ilkesidir.


Bir kriptografik şemanın "güvenli" ya da "güvensiz" olduğu asla kesin olarak söylenemez Bunun yerine, kriptografik şemalar için çeşitli güvenlik kavramları vardır. Her **kriptografik güvenlik tanımı** (1) güvenlik hedeflerinin yanı sıra (2) bir saldırganın yeteneklerini de belirtmelidir. Kriptografik şemaların bir veya daha fazla özel güvenlik kavramına göre analiz edilmesi, bunların uygulamaları ve sınırlamaları hakkında bilgi sağlar.


Çeşitli kriptografik güvenlik kavramlarının tüm ayrıntılarına girmeyecek olsak da, simetrik ve asimetrik şemalara (ve bir şekilde diğer kriptografik ilkellere) ilişkin tüm modern kriptografik güvenlik kavramları için iki varsayımın her yerde bulunduğunu bilmelisiniz:



- Saldırganın şema hakkındaki bilgisi Kerckhoffs'un ilkesine uygundur.
- Saldırganın şema üzerinde kaba kuvvet saldırısı gerçekleştirmesi mümkün değildir. Özellikle, kriptografik güvenlik kavramlarının tehdit modelleri tipik olarak kaba kuvvet saldırılarına bile izin vermez, çünkü bunların ilgili bir husus olmadığını varsayarlar.



**Notlar:**


[1] Seutonius'a göre, sabit anahtar değeri 3 olan bir kaydırmalı şifre Julius Caesar tarafından askeri haberleşmelerinde kullanılmıştır. Böylece A her zaman D, B her zaman E, C her zaman F ve bu şekilde devam ederdi. Kaydırmalı şifrenin bu özel versiyonu bu nedenle **Sezar Şifresi** olarak bilinir hale gelmiştir (anahtar değeri sabit olduğu için kelimenin modern anlamında bir şifre değildir). Sezar şifresi, Roma'nın düşmanları şifrelemeye çok aşina değilse, MÖ birinci yüzyılda güvenli olabilirdi. Ancak modern zamanlarda çok güvenli bir şema olmayacağı açıktır.


[2] Jonathan Katz ve Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), s. 7f.


[3] Eric Raymond, "The Cathedral and the Bazaar", Linux Kongress, Würzburg, Almanya'da (27 Mayıs 1997) sunulmuştur. Bir kitabın yanı sıra bir dizi müteakip versiyonu da mevcuttur. Alıntılarım kitabın 30. sayfasından alınmıştır: Eric Raymond, _The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary_, revised edn. (2001), O'Reilly: Sebastopol, CA.



## Akış şifreleri

<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>


Simetrik şifreleme şemaları standart olarak iki türe ayrılır: **akış şifreleri** ve **blok şifreler**. Ancak insanlar bu terimleri tutarsız bir şekilde kullandıkları için bu ayrım biraz sorunludur. Önümüzdeki birkaç bölümde, ayrımı en iyi olduğunu düşündüğüm şekilde ortaya koyacağım. Bununla birlikte, birçok kişinin bu terimleri benim belirttiğimden biraz farklı kullanacağını bilmelisiniz.


İlk olarak akış şifrelerine dönelim. Bir **akış şifresi**, şifrelemenin iki adımdan oluştuğu simetrik bir şifreleme şemasıdır.


İlk olarak, özel bir anahtar aracılığıyla düz metin uzunluğunda bir dize üretilir. Bu dizeye **keystream** adı verilir.


Daha sonra, anahtar dizisi bir şifreli metin üretmek için düz metinle matematiksel olarak birleştirilir. Bu kombinasyon tipik olarak bir XOR işlemidir. Şifre çözme için işlemi tersine çevirebilirsiniz. ($A$ ve $B$ bit dizileri olduğu durumda $A \oplus B = B \oplus A$ olduğuna dikkat edin. Yani bir akış şifresindeki XOR işleminin sırası sonuç için önemli değildir. Bu özellik **komütativite** olarak bilinir)


Tipik bir XOR akış şifresi *Şekil 3*'te gösterilmiştir. İlk olarak $K$ özel anahtarı alınır ve generate anahtar dizisi için kullanılır. Anahtar dizisi daha sonra şifreli metni üretmek için bir XOR işlemi aracılığıyla düz metinle birleştirilir. Şifreli metni alan herhangi bir ajan, $K$ anahtarına sahipse şifresini kolayca çözebilir. Tek yapması gereken, şemanın belirtilen prosedürüne göre şifreli metin kadar uzun bir anahtar dizisi oluşturmak ve bunu şifreli metinle XORlamaktır.



*Şekil 3: Bir XOR akış şifresi*


![Figure 3: An XOR stream cipher](assets/Figure4-3.webp "Figure 3: An XOR stream cipher")


Bir şifreleme şemasının tam bir spesifikasyondan ziyade tipik olarak aynı çekirdek algoritma ile şifreleme için bir şablon olduğunu hatırlatmak isteriz. Buna bağlı olarak, bir akış şifresi tipik olarak farklı uzunluklarda anahtarlar kullanabileceğiniz bir şifreleme şablonudur. Anahtar uzunluğu, şemanın bazı küçük ayrıntılarını etkileyebilse de, temel biçimini etkilemeyecektir.


Shift şifresi çok basit ve güvensiz bir akış şifresi örneğidir. Tek bir harf (özel anahtar) kullanarak, mesajın uzunluğunda bir harf dizisi (anahtar dizisi) üretebilirsiniz. Bu anahtar dizisi daha sonra bir modulo işlemi aracılığıyla düz metinle birleştirilerek bir şifreli metin elde edilir. (Bu modulo işlemi, harfleri bit olarak temsil ederken bir XOR işlemine basitleştirilebilir).


Akış şifresinin bir başka ünlü örneği, 16. yüzyılın sonunda tamamen geliştiren Blaise de Vigenere'nin adını taşıyan **Vigenere şifresidir** (başkaları daha önce pek çok çalışma yapmış olsa da). Bu bir **polifabetik ikame şifresi** örneğidir: bir düz metin sembolü için şifreli metin alfabesinin metindeki konumuna bağlı olarak değiştiği bir şifreleme şeması. Monoalfabetik yer değiştirme şifresinin aksine, şifreli metin sembolleri birden fazla açık metin sembolü ile ilişkilendirilebilir.


Şifreleme Rönesans Avrupa'sında popülerlik kazandıkça, **kriptanaliz**, yani şifreli metinlerin kırılması da özellikle **frekans analizi** kullanılarak yaygınlaştı. İkincisi, şifreli metinleri kırmak için dilimizdeki istatistiksel düzenlilikleri kullanır ve dokuzuncu yüzyılda Arap bilim adamları tarafından keşfedilmiştir. Özellikle uzun metinlerde işe yarayan bir tekniktir. Ve en sofistike monoalfabetik yer değiştirme şifreleri bile 1700'lerde Avrupa'da, özellikle askeri ve güvenlik ortamlarında frekans analizine karşı artık yeterli değildi. Vigenere şifresi güvenlik alanında önemli bir ilerleme sağladığı için bu dönemde popüler hale gelmiş ve 1700'lerin sonlarına doğru yaygınlaşmıştır.


Gayri resmi olarak, şifreleme şeması aşağıdaki gibi çalışır:


1. Özel anahtar olarak çok harfli bir kelime seçin.

2. Herhangi bir mesaj için, anahtar kelimede karşılık gelen harfi kaydırma olarak kullanarak mesajın her harfine kaydırma şifresini uygulayın.

3. Eğer anahtar kelimenin üzerinden geçtiyseniz ancak hala düz metni tamamen şifreleyemediyseniz, anahtar kelimenin harflerini metnin geri kalanında karşılık gelen harflere kaydırmalı şifre olarak tekrar uygulayın.

4. Mesajın tamamı şifrelenene kadar bu işleme devam edin.


Örnek olarak, özel anahtarınızın "GOLD" olduğunu ve "CRYPTOGRAPHY" mesajını şifrelemek istediğinizi varsayalım. Bu durumda, Vigenère şifrelemesine göre aşağıdaki şekilde ilerlersiniz:



- $c_0 = [(2 + 6) \mod 26] = 8 = I$
- $c_1 = [(17 + 14) \mod 26] = 5 = F$
- $c_2 = [(24 + 11) \mod 26] = 9 = J$
- $c_3 = [(15 + 3) \mod 26] = 18 = S$
- $c_4 = [(19 + 6) \mod 26] = 25 = Z$
- $c_5 = [(14 + 14) \mod 26] = 2 = C$
- $c_6 = [(6 + 11) \mod 26] = 17 = R$
- $c_7 = [(17 + 3) \mod 26] = 20 = U$
- $c_8 = [(0 + 6) \mod 26] = 6 = G$
- $c_9 = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$


Böylece, $c$ = "IFJSZCRUGDSB" şifreli metni elde edilir.


Akış şifresinin bir diğer ünlü örneği **tek seferlik peddir**. One-time pad ile basitçe düz metin mesajı kadar uzun rastgele bitler dizisi oluşturur ve XOR işlemi ile şifreli metni üretirsiniz. Dolayısıyla, özel anahtar ve anahtar dizisi bir kerelik ped ile eşdeğerdir.


Shift şifresi ve Vigenere şifreleri modern çağda çok güvensiz olsa da, tek seferlik ped doğru kullanıldığında çok güvenlidir. Muhtemelen tek kullanımlık pedin en ünlü uygulaması, en azından 1980'lere kadar, **Washington-Moskova yardım hattı** içindi. [4]


Bu hat, Küba Füze Krizi sonrasında Washington ve Moskova arasında acil konular için kurulan doğrudan bir iletişim bağlantısıdır. Hattın teknolojisi yıllar içinde değişime uğramıştır. Şu anda doğrudan bir fiber optik kablonun yanı sıra e-posta ve metin mesajlaşmasını mümkün kılan iki uydu bağlantısı (yedeklilik için) içermektedir. Bağlantı ABD'nin çeşitli yerlerinde son bulmaktadır. Pentagon, Beyaz Saray ve Raven Rock Dağı bilinen uç noktalardır. Popüler görüşün aksine, yardım hattı hiçbir zaman telefonları içermemiştir.


Özünde, tek seferlik yastık şeması şu şekilde çalışıyordu. Hem Washington hem de Moskova iki rastgele sayı setine sahip olacaktı. Ruslar tarafından yaratılan bir rastgele sayı kümesi Rusça dilindeki mesajların şifrelenmesi ve deşifre edilmesiyle ilgiliydi. Amerikalılar tarafından yaratılan bir rastgele sayı kümesi ise İngilizce dilindeki mesajların şifrelenmesi ve deşifre edilmesiyle ilgiliydi. Zaman zaman daha fazla rastgele sayı güvenilir kuryeler tarafından karşı tarafa iletiliyordu.


Washington ve Moskova bu rastgele sayıları tek seferlik şifreler oluşturmak için kullanarak gizlice iletişim kurabiliyorlardı. Her iletişim kurmanız gerektiğinde, mesajınız için rastgele sayıların bir sonraki bölümünü kullanıyordunuz.


Oldukça güvenli olmasına rağmen, tek seferlik bloknot önemli pratik sınırlamalarla karşı karşıyadır: anahtarın mesaj kadar uzun olması gerekir ve tek seferlik bloknotun hiçbir parçası yeniden kullanılamaz. Bu da tek kullanımlık pedin neresinde olduğunuzu takip etmeniz, çok sayıda bit saklamanız ve zaman zaman karşı taraflarla rastgele bitler Exchange yapmanız gerektiği anlamına gelir. Sonuç olarak, tek seferlik yastık pratikte sık kullanılmaz.


Bunun yerine, uygulamada kullanılan baskın akış şifreleri **sözde rastgele akış şifreleridir**. Salsa20 ve ChaCha adlı yakından ilişkili bir varyant, yaygın olarak kullanılan sözde rastgele akış şifrelerine örnektir.


Bu sözde rastgele akış şifrelerinde, önce rastgele olarak düz metnin uzunluğundan daha kısa bir K anahtarı seçersiniz. Böyle rastgele bir K anahtarı genellikle bilgisayarımız tarafından ağ mesajları arasındaki süre, fare hareketleri gibi zaman içinde topladığı öngörülemeyen verilere dayanarak oluşturulur.


Bu rastgele anahtar $K$ daha sonra mesaj kadar uzun bir sözde rastgele anahtar akışı oluşturan bir genişletme algoritmasına eklenir. Anahtar akışının tam olarak ne kadar uzun olması gerektiğini belirtebilirsiniz (örneğin, 500 bit, 1000 bit, 1200 bit, 29.117 bit vb.).


Bir sözde rasgele anahtar dizisi, aynı uzunluktaki tüm diziler kümesinden tamamen rasgele seçilmiş gibi *görünür*. Dolayısıyla, sözde rastgele anahtar dizisi ile şifreleme, tek seferlik ped ile yapılmış gibi görünür. Ancak durum elbette böyle değildir.


Özel anahtarımız anahtar dizisinden daha kısa olduğundan ve şifreleme/şifre çözme işleminin çalışması için genişletme algoritmamızın deterministik olması gerektiğinden, belirli uzunluktaki her anahtar dizisi genişletme işlemimizden bir çıktı olarak ortaya çıkmayabilir.


Örneğin, özel anahtarımızın 128 bit uzunluğunda olduğunu ve bunu genişletici bir algoritmaya ekleyerek çok daha uzun, örneğin 2.500 bitlik bir anahtar dizisi oluşturabileceğimizi varsayalım. Genişletme algoritmamızın deterministik olması gerektiğinden, algoritmamız en fazla 2.500 bit uzunluğunda $1/2^{128}$ dizileri seçebilir. Dolayısıyla böyle bir anahtar dizisi hiçbir zaman aynı uzunluktaki tüm dizilerden tamamen rastgele seçilemez.


Akış şifresi tanımımızın iki yönü vardır: (1) düz metin kadar uzun bir anahtar dizisi özel bir anahtar yardımıyla oluşturulur; ve (2) bu anahtar dizisi, şifreli metni üretmek için tipik olarak bir XOR işlemi yoluyla düz metinle birleştirilir.


Bazen insanlar anahtar dizisinin özellikle sözde rastgele olması gerektiğini ileri sürerek (1) koşulunu daha katı bir şekilde tanımlarlar. Bu da ne shift cipher ne de one-time pad'in stream cipher olarak kabul edilmeyeceği anlamına gelir.


Benim görüşüme göre, koşul (1)'i daha geniş bir şekilde tanımlamak şifreleme şemalarını organize etmek için daha kolay bir yol sağlar. Buna ek olarak, aslında sözde rastgele anahtar akışlarına dayanmadığını öğrendiğimiz için belirli bir şifreleme şemasını akış şifresi olarak adlandırmayı bırakmak zorunda olmadığımız anlamına gelir.


**Notlar:**


[4] Crypto Museum, "Washington-Moscow hotline," 2013, [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm) adresinden erişilebilir.




## Blok şifreler

<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>


Bir **blok şifrenin** yaygın olarak anlaşıldığı ilk yol, bir akış şifresinden daha ilkel bir şeydir: Bir anahtar yardımıyla uygun uzunluktaki bir dize üzerinde uzunluğu koruyan bir dönüşüm gerçekleştiren temel bir algoritma. Bu algoritma şifreleme şemaları ve belki de diğer kriptografik şema türlerini oluşturmak için kullanılabilir.


Sıklıkla, bir blok şifre 64, 128 veya 256 bit gibi farklı uzunluklarda girdi dizileri ve 128, 192 veya 256 bit gibi farklı uzunluklarda anahtarlar alabilir. Algoritmanın bazı ayrıntıları bu değişkenlere bağlı olarak değişebilse de, temel algoritma değişmez. Eğer değişseydi, iki farklı blok şifreden bahsediyor olurduk. Burada çekirdek algoritma terminolojisinin kullanımının şifreleme şemaları ile aynı olduğunu unutmayın.


Bir blok şifrenin nasıl çalıştığına dair bir tasvir aşağıdaki *Şekil 4*'de görülebilir. L$ uzunluğunda bir $M$ mesajı ve bir $K$ anahtarı Blok şifrenin girdileri olarak hizmet eder. Çıktı olarak $L$ uzunluğunda bir $M'$ mesajı verir. Çoğu blok şifrede anahtarın $M$ ve $M'$ ile aynı uzunlukta olması gerekmez.


*Şekil 4: Bir blok şifre*


![Figure 4: A block cipher](assets/Figure4-4.webp "Figure 4: A block cipher")


Bir blok şifre tek başına bir şifreleme şeması değildir. Ancak bir blok şifre, farklı şifreleme şemaları üretmek için çeşitli **çalışma modları** ile kullanılabilir. Bir çalışma modu basitçe blok şifrenin dışına bazı ek işlemler ekler.


Bunun nasıl çalıştığını göstermek için 128 bitlik bir giriş dizesi ve 128 bitlik bir özel anahtar gerektiren bir blok şifre (BC) varsayalım. Aşağıdaki Şekil 5, bu blok şifrenin **elektronik kod kitabı modu** (**ECB modu**) ile bir şifreleme şeması oluşturmak için nasıl kullanılabileceğini göstermektedir. (Sağdaki elipsler, bu kalıbı gerektiği kadar tekrarlayabileceğinizi gösterir).


*Şekil 5: ECB moduna sahip bir blok şifre*


![Figure 5: A block cipher with ECB mode](assets/Figure4-5.webp "Figure 5: A block cipher with ECB mode")


Blok şifreleme ile elektronik kod kitabı şifreleme işlemi aşağıdaki gibidir. Düz metin mesajınızı 128 bitlik bloklara bölüp bölemeyeceğinize bakın. Eğer değilse, mesaja **dolgu** ekleyin, böylece sonuç 128 bitlik blok boyutuna eşit olarak bölünebilir. Bu, şifreleme işlemi için kullanılan verilerinizdir.


Şimdi verileri 128 bitlik dizelerden oluşan parçalara bölün ($M_1$, $M_2$, $M_3$, vb.). 128 bitlik şifreli metin parçaları ($C_1$, $C_2$, $C_3$, vb.) üretmek için her 128 bitlik dizeyi 128 bitlik anahtarınızla blok şifrelemeden geçirin. Bu parçalar yeniden birleştirildiğinde tam şifreli metni oluşturur.


Şifre çözme işlemi tam tersidir, ancak alıcının orijinal düz metin mesajını üretmek için şifresi çözülmüş verilerden herhangi bir dolguyu çıkarmak için tanınabilir bir yola ihtiyacı vardır.


Nispeten basit olmasına rağmen, elektronik kod kitabı moduna sahip bir blok şifre güvenlikten yoksundur. Bunun nedeni **deterministik şifrelemeye** yol açmasıdır. Herhangi iki aynı 128-bit veri dizisi tam olarak aynı şekilde şifrelenir. Bu bilgi istismar edilebilir.


Bunun yerine, bir blok şifreden oluşturulan herhangi bir şifreleme şeması **olasılıksal** olmalıdır: yani, herhangi bir $M$ mesajının veya $M$'nin belirli bir parçasının şifrelenmesi genellikle her seferinde farklı bir sonuç vermelidir. [5]


Şifreleme blok zincirleme modu (**CBC modu**) muhtemelen bir blok şifreleme ile kullanılan en yaygın moddur. Kombinasyon, doğru yapılırsa, olasılıksal bir şifreleme şeması üretir. Bu çalışma modunun bir tasvirini aşağıdaki *Şekil 6*'da görebilirsiniz.


*Şekil 6: CBC moduna sahip bir blok şifre*


![Figure 6: A block cipher with CBC mode](assets/Figure4-6.webp "Figure 6: A block cipher with CBC mode")


Blok boyutunun yine 128 bit olduğunu varsayalım. Başlangıç olarak, orijinal düz metin mesajınızın gerekli dolguyu aldığından emin olmanız gerekir.


Ardından, düz metninizin ilk 128 bitlik bölümünü 128 bitlik bir **başlangıç vektörü** ile XOR'larsınız. Sonuç, ilk blok için bir şifreli metin üretmek üzere blok şifrelemeye yerleştirilir. İkinci 128 bitlik blok için, blok şifreye yerleştirmeden önce ilk bloktaki şifreli metin ile düz metni XOR'larsınız. Tüm düz metin mesajınızı şifreleyene kadar bu işleme devam edersiniz.


İşiniz bittiğinde, şifrelenmiş mesajı şifrelenmemiş başlatma vektörü ile birlikte alıcıya gönderirsiniz. Alıcının başlatma vektörünü bilmesi gerekir, aksi takdirde şifreli metnin şifresini çözemez.


Bu yapı doğru kullanıldığında elektronik kod defteri modundan çok daha güvenlidir. Öncelikle, başlatma vektörünün rastgele veya sözde rastgele bir dize olduğundan emin olmalısınız. Ayrıca, bu şifreleme şemasını her kullandığınızda farklı bir başlatma vektörü kullanmalısınız.


Başka bir deyişle, başlatma vektörünüz rastgele veya sözde rastgele bir Nonce olmalıdır; burada **Nonce** "yalnızca bir kez kullanılan bir sayı" anlamına gelir Bu uygulamaya devam ederseniz, bir blok şifreleme ile CBC modu, herhangi iki aynı düz metin bloğunun genellikle her seferinde farklı şekilde şifrelenmesini sağlar.


Son olarak, dikkatimizi **çıkış geri besleme moduna** (**OFB modu**) çevirelim. Bu modun bir tasvirini *Şekil 7*'de görebilirsiniz.


*Şekil 7: OFB moduna sahip bir blok şifre*


![Figure 7: A block cipher with OFB mode](assets/Figure4-7.webp "Figure 7: A block cipher with OFB mode")


OFB modu ile ayrıca bir başlatma vektörü seçersiniz. Ancak burada, ilk blok için, başlatma vektörü doğrudan anahtarınızla birlikte blok şifrelemeye eklenir. Ortaya çıkan 128 bit, daha sonra bir anahtar dizisi olarak ele alınır. Bu anahtar dizisi, bloğun şifreli metnini üretmek için düz metin ile XORlanır. Sonraki bloklar için, bir önceki bloğun anahtar dizisini blok şifreye girdi olarak kullanır ve adımları tekrarlarsınız.


Dikkatli bakarsanız, burada OFB modlu blok şifreden oluşturulan şey aslında bir akış şifresidir. Düz metnin uzunluğuna sahip olana kadar 128 bitlik anahtar dizisi bölümlerini generate yaparsınız (son 128 bitlik anahtar dizisi bölümünden ihtiyacınız olmayan bitleri atarsınız). Daha sonra, şifreli metni elde etmek için anahtar dizisini düz metin mesajınızla XOR'larsınız.


Akış şifreleri ile ilgili bir önceki bölümde, bir özel anahtar yardımıyla bir anahtar dizisi ürettiğinizi belirtmiştim. Daha açık olmak gerekirse, sadece özel bir anahtarla oluşturulmak zorunda değildir. OFB modunda görebileceğiniz gibi, anahtar dizisi hem bir özel anahtar hem de bir başlatma vektörü desteği ile üretilir.


CBC modunda olduğu gibi, OFB modunda bir blok şifreleme kullandığınız her seferinde başlatma vektörü için bir sözde rastgele veya rastgele Nonce seçmenin önemli olduğunu unutmayın. Aksi takdirde, farklı iletişimlerde gönderilen aynı 128 bitlik mesaj dizisi aynı şekilde şifrelenecektir. Bu, bir akış şifresiyle olasılıksal şifreleme oluşturmanın bir yoludur.


Bazı akış şifreleri bir anahtar akışı oluşturmak için yalnızca özel bir anahtar kullanır. Bu akış şifrelerinde, her iletişim örneği için özel anahtarı seçmek üzere rastgele bir Nonce kullanmanız önemlidir. Aksi takdirde, bu akış şifreleriyle şifreleme sonuçları da deterministik olacak ve güvenlik sorunlarına yol açacaktır.


En popüler modern blok şifre **Rijndael şifresidir**. Ulusal Standartlar ve Teknoloji Enstitüsü (NIST) tarafından 1997-2000 yılları arasında eski bir şifreleme standardı olan **veri şifreleme standardı** (**DES**) yerine geçmek için düzenlenen bir yarışmaya on beş başvuru arasından kazanan giriş oldu.


Rijndael Ģifresi, anahtar uzunlukları ve blok boyutları için farklı özelliklerin yanı sıra farklı çalıĢma modlarında da kullanılabilir. NIST yarışması komitesi Rijndael şifresinin kısıtlı bir versiyonunu, yani 128 bit blok boyutları ve 128 bit, 192 bit ya da 256 bit anahtar uzunlukları gerektiren bir versiyonunu **gelişmiş şifreleme standardının** (**AES**) bir parçası olarak kabul etmiştir. Bu gerçekten simetrik şifreleme uygulamaları için ana standarttır. O kadar güvenlidir ki NSA bile çok gizli belgeler için 256 bit anahtarlarla kullanmaya isteklidir. [6]


AES blok şifresi *Bölüm 5*'de ayrıntılı olarak açıklanacaktır.



**Notlar:**


[5] Olasılıksal şifrelemenin önemi ilk olarak Shafi Goldwasser ve Silvio Micali tarafından vurgulanmıştır, "Probabilistic encryption," _Journal of Computer and System Sciences_, 28 (1984), 270-99.


[6] Bkz: NSA, "Ticari Ulusal Güvenlik Algoritma Paketi", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).




## Karışıklığı gidermek

<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>


Blok şifreler ve akış şifreleri arasındaki ayrımla ilgili kafa karışıklığı, bazen insanların blok şifre terimini özellikle blok şifreleme moduna sahip bir *blok şifreleme* anlamına gelecek şekilde anlamalarından kaynaklanmaktadır.


Önceki bölümdeki ECB ve CBC modlarını düşünün. Bunlar özellikle şifreleme için verilerin blok boyutuna bölünebilir olmasını gerektirir (yani orijinal mesaj için dolgu kullanmanız gerekebilir). Ayrıca, bu modlardaki veriler doğrudan blok şifre tarafından da işlenir (OFB modunda olduğu gibi sadece bir blok şifre işleminin sonucuyla birleştirilmez).


Bu nedenle, alternatif olarak, bir **blok şifrelemeyi** bir seferde mesajın sabit uzunluktaki blokları üzerinde çalışan herhangi bir şifreleme şeması olarak tanımlayabilirsiniz (herhangi bir bloğun bir bayttan daha uzun olması gerekir, aksi takdirde bir akış şifrelemesine dönüşür). Hem şifreleme için veri hem de şifreli metin bu blok boyutuna eşit olarak bölünmelidir. Tipik olarak blok boyutu 64, 128, 192 ya da 256 bit uzunluğundadır. Buna karşın, bir akış şifresi herhangi bir mesajı her seferinde bir bit ya da baytlık parçalar halinde şifreleyebilir.


Bu daha spesifik blok şifre anlayışıyla, modern şifreleme şemalarının ya akış ya da blok şifreler olduğunu iddia edebilirsiniz. Buradan itibaren, aksi belirtilmedikçe blok şifre terimini daha genel anlamda kullanacağım.


Önceki bölümde OFB modu üzerine yapılan tartışma bir başka ilginç noktayı da gündeme getirmektedir. OFB'li Rijndael gibi bazı akış şifreleri blok şifrelerden oluşturulmuştur. Salsa20 ve ChaCha gibi bazıları ise blok şifrelerden oluşturulmamıştır. İkincisine **ilkel akış şifreleri** diyebilirsiniz. (Bu tür akış şifrelerini ifade etmek için standartlaştırılmış bir terim yoktur)


İnsanlar akış şifreleri ve blok şifrelerin avantajları ve dezavantajları hakkında konuşurken, genellikle ilkel akış şifreleri ile blok şifrelere dayalı şifreleme şemalarını karşılaştırırlar.


Bir blok şifreden her zaman kolayca bir akış şifresi oluşturabilirken, ilkel bir akış şifresinden bir blok şifreleme moduyla (CBC modu gibi) bir tür yapı oluşturmak genellikle çok zordur.


Bu tartışmadan sonra artık *Şekil 8*'i anlamış olmalısınız. Simetrik şifreleme şemalarına genel bir bakış sağlar. Üç tür şifreleme şeması kullanırız: ilkel akış şifreleri, blok şifreli akış şifreleri ve blok modunda blok şifreler (diyagramda "blok şifreler" olarak da adlandırılır).


*Şekil 8: Simetrik şifreleme şemalarına genel bakış*


![Figure 8: Overview of symmetric encryption schemes](assets/Figure4-8.webp "Figure 8: Overview of symmetric encryption schemes")



## Mesaj kimlik doğrulama kodları

<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>


Şifreleme gizlilik ile ilgilidir. Ancak kriptografi aynı zamanda mesaj bütünlüğü, özgünlük ve inkar etmeme gibi daha geniş konularla da ilgilenir. **Mesaj kimlik doğrulama kodları** (MAC'ler), iletişimde özgünlüğü ve bütünlüğü destekleyen simetrik anahtar şifreleme şemalarıdır.


İletişimde gizlilik dışında herhangi bir şeye neden ihtiyaç duyulur? Bob'nin Alice'e pratikte kırılamaz bir şifreleme kullanarak bir mesaj gönderdiğini varsayalım. Bu mesajı ele geçiren herhangi bir saldırgan mesajın içeriğine ilişkin önemli bir bilgi elde edemeyecektir. Ancak, saldırganın elinde hala en az iki saldırı vektörü daha vardır:


1. Şifre metnini ele geçirebilir, içeriğini değiştirebilir ve değiştirilmiş şifre metnini Alice'e gönderebilir.

2. Bob'ün mesajını tamamen bloke edebilir ve kendi yarattığı şifre metnini gönderebilir.


Bu iki durumda da saldırgan (1) ve (2) numaralı şifreli metinlerin içeriği hakkında herhangi bir bilgiye sahip olmayabilir. Ancak yine de bu şekilde önemli hasara neden olabilir. İşte bu noktada mesaj doğrulama kodları önem kazanmaktadır.


Mesaj kimlik doğrulama kodları, üç algoritmaya sahip simetrik şifreleme şemaları olarak tanımlanır: bir anahtar oluşturma algoritması, bir etiket oluşturma algoritması ve bir doğrulama algoritması. Güvenli bir MAC, etiketlerin herhangi bir saldırgan için **varoluşsal olarak taklit edilemez** olmasını sağlar - yani, özel anahtara sahip olmadıkları sürece, doğrulayan mesaj üzerinde başarılı bir şekilde bir etiket oluşturamazlar.


Bob ve Alice bir MAC kullanarak belirli bir mesajın manipüle edilmesiyle mücadele edebilir. Bir an için gizliliğe önem vermediklerini varsayalım. Sadece Alice tarafından alınan mesajın gerçekten Bob'dan geldiğinden ve herhangi bir şekilde değiştirilmediğinden emin olmak istiyorlar.


Süreç *Şekil 9*'da gösterilmiştir. Bir **MAC** (Mesaj Kimlik Doğrulama Kodu) kullanmak için, önce generate ikisi arasında paylaşılan bir özel anahtar $K$ oluşturur. Bob $K$ özel anahtarını kullanarak mesaj için bir $T$ etiketi oluşturur. Daha sonra mesajı ve mesaj etiketini Alice'e gönderir. Alice daha sonra özel anahtarı, mesajı ve etiketi bir doğrulama algoritmasından geçirerek Bob'un gerçekten de etiketi oluşturduğunu doğrulayabilir.


*Şekil 9: Simetrik şifreleme şemalarına genel bakış*


![Figure 9: Overview of symmetric encryption schemes](assets/Figure4-9.webp "Figure 9: Overview of symmetric encryption schemes")


**Varoluşsal taklit edilemezlik** nedeniyle, bir saldırgan $M$ mesajını herhangi bir şekilde değiştiremez veya geçerli bir etikete sahip kendi mesajını oluşturamaz. Saldırgan, Bob ve Alice arasında aynı özel anahtarı kullanan birçok mesajın etiketlerini gözlemlese bile bu böyledir. Bir saldırgan en fazla Alice'in $M$ mesajını almasını engelleyebilir (kriptografinin **Address'ün** yapamayacağı bir sorun).


Bir MAC, bir mesajın gerçekten Bob tarafından oluşturulduğunu garanti eder. Bu özgünlük, otomatik olarak mesaj bütünlüğü anlamına gelir - yani, Bob bir mesaj yarattıysa, o zaman, ipso facto, bir saldırgan tarafından herhangi bir şekilde değiştirilmemiştir. Dolayısıyla, buradan itibaren, kimlik doğrulamaya yönelik herhangi bir kaygının otomatik olarak bütünlüğe yönelik bir kaygı anlamına geldiği anlaşılmalıdır.


Tartışmamda mesaj özgünlüğü ve bütünlüğü arasında bir ayrım yapmış olsam da, bu terimleri eşanlamlı olarak kullanmak da yaygındır. O halde, her ikisi de belirli bir gönderici tarafından oluşturulmuş ve herhangi bir şekilde değiştirilmemiş mesajlar fikrine atıfta bulunurlar. Bu bağlamda, mesaj kimlik doğrulama kodları sıklıkla **mesaj bütünlüğü kodları** olarak da adlandırılır.



## Kimlik doğrulamalı şifreleme

<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>


Tipik olarak, iletişimde hem gizliliği hem de gerçekliği garanti etmek istersiniz ve bu nedenle şifreleme şemaları ve MAC şemaları genellikle birlikte kullanılır.


Kimliği doğrulanmış bir **şifreleme şeması**, şifrelemeyi MAC ile yüksek güvenlikli bir şekilde birleştiren bir şemadır. Özellikle, varoluşsal taklit edilemezlik standartlarının yanı sıra çok güçlü bir gizlilik kavramını, yani **seçilmiş şifreli metin saldırılarına** karşı dirençli bir gizlilik kavramını karşılaması gerekir. [7]


Bir şifreleme şemasının seçilmiş şifreli metin saldırılarına karşı dirençli olması için **malleability** standartlarını karşılaması gerekir: yani, bir saldırgan tarafından bir şifreli metinde yapılan herhangi bir değişiklik ya geçersiz bir şifreli metin ya da orijinaliyle hiçbir ilişkisi olmayan bir düz metne deşifre olan bir şifreli metin vermelidir. [8]


Kimliği doğrulanmış bir şifreleme şeması, bir saldırgan tarafından oluşturulan bir şifreli metnin her zaman geçersiz olmasını sağladığından (etiket doğrulanmayacağından), seçilmiş şifreli metin saldırılarına karşı direnç standartlarını karşılar. İlginç bir şekilde, kimliği doğrulanmış bir şifreleme şemasının her zaman varoluşsal olarak taklit edilemez bir MAC ve **seçilmiş düz metin saldırısı güvenliği** olarak bilinen daha az güçlü bir güvenlik kavramını karşılayan bir şifreleme şemasının kombinasyonundan oluşturulabileceğini kanıtlayabilirsiniz.


Kimliği doğrulanmış şifreleme şemaları oluşturmanın tüm ayrıntılarına girmeyeceğiz. Ancak yapılarının iki detayını bilmek önemlidir.


İlk olarak, kimliği doğrulanmış bir şifreleme şeması önce şifrelemeyi gerçekleştirir ve ardından şifreli metin üzerinde bir mesaj etiketi oluşturur. Şifreli metni düz metin üzerindeki bir etiketle birleştirmek ya da önce bir etiket oluşturup ardından hem düz metni hem de etiketi şifrelemek gibi diğer yaklaşımların güvensiz olduğu ortaya çıkmıştır. Buna ek olarak, her iki işlemin de rastgele seçilmiş kendi özel anahtarı vardır, aksi takdirde güvenliğiniz ciddi şekilde tehlikeye girer.


Yukarıda bahsedilen ilke daha genel olarak geçerlidir: *temel kriptografik şemaları* birleştirirken her zaman farklı anahtarlar kullanmalısınız.


Kimliği doğrulanmış bir şifreleme şeması *Şekil 10*'da gösterilmiştir. Bob ilk olarak rastgele seçilmiş bir $K_C$ anahtarı kullanarak $M$ mesajından bir $C$ şifreli metni oluşturur. Daha sonra şifreli metni ve rastgele seçilen farklı bir $K_T$ anahtarını etiket oluşturma algoritmasından geçirerek bir $T$ mesaj etiketi oluşturur. Hem şifreli metin hem de mesaj etiketi Alice'e gönderilir.


Alice şimdi ilk olarak $C$ şifreli metni ve $K_T$ anahtarı göz önüne alındığında etiketin geçerli olup olmadığını kontrol eder. Eğer geçerliyse, $K_C$ anahtarını kullanarak mesajın şifresini çözebilir. İletişimlerinde çok güçlü bir gizlilik kavramından emin olmakla kalmaz, aynı zamanda mesajın Bob tarafından oluşturulduğunu da bilir.


*Şekil 10: Kimliği doğrulanmış bir şifreleme şeması*


![Figure 10: An authenticated encryption scheme](assets/Figure4-10.webp "Figure 10: An authenticated encryption scheme")


MAC'ler nasıl oluşturulur? MAC'ler birden fazla yöntemle oluşturulabilirken, bunları oluşturmanın yaygın ve etkili bir yolu **kriptografik Hash işlevleridir**.


Kriptografik Hash fonksiyonlarını *Bölüm 6*'da daha ayrıntılı olarak tanıtacağız. Şimdilik, bir **Hash fonksiyonunun** keyfi boyutta girdiler alan ve sabit uzunlukta çıktılar veren verimli bir şekilde hesaplanabilir bir fonksiyon olduğunu bilin. Örneğin, popüler Hash işlevi **SHA-256** (güvenli Hash algoritması 256), girdinin boyutundan bağımsız olarak her zaman 256 bitlik bir çıktı üretir. SHA-256 gibi bazı Hash fonksiyonlarının kriptografide faydalı uygulamaları vardır.


Kriptografik Hash işleviyle üretilen en yaygın etiket türü **Hash tabanlı mesaj kimlik doğrulama kodudur** (HMAC). Süreç *Şekil 11*'de gösterilmiştir. Bir taraf $K$ özel anahtarından iki farklı anahtar üretir, iç anahtar $K_1$ ve dış anahtar $K_2$. Daha sonra düz metin $M$ veya şifreli metin $C$ iç anahtarla birlikte hashlenir. Sonuç $T'$ daha sonra $T$ mesaj etiketini üretmek için dış anahtarla hash edilir.


Bir HMAC oluşturmak için kullanılabilecek bir Hash işlevleri paleti vardır. En yaygın kullanılan Hash işlevi SHA-256'dır.



*Şekil 11: HMAC*


![Figure 11: HMAC](assets/Figure4-11.webp "Figure 11: HMAC")


**Notlar:**


[7] Bu bölümde tartışılan spesifik sonuçlar Katz ve Lindell, s. 131-47'den alınmıştır.


[8] Teknik olarak, seçilmiş şifreli metin saldırılarının tanımı, karıştırılamazlık kavramından farklıdır. Ancak bu iki güvenlik kavramının eşdeğer olduğunu gösterebilirsiniz.




## Güvenli iletişim oturumları

<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>


İki tarafın bir iletişim oturumunda olduğunu ve ileri geri birden fazla mesaj gönderdiklerini varsayalım.


Kimliği doğrulanmış bir şifreleme şeması, bir mesajın alıcısının, iletişim oturumundaki ortağı tarafından oluşturulduğunu doğrulamasına olanak tanır (özel anahtar sızdırılmadığı sürece). Bu, tek bir mesaj için yeterince iyi çalışır. Ancak tipik olarak, iki taraf bir iletişim oturumunda ileri geri mesaj göndermektedir. Ve bu ortamda, önceki bölümde açıklandığı gibi düz bir kimlik doğrulamalı şifreleme şeması güvenlik sağlamada yetersiz kalır.


Bunun ana nedeni, kimliği doğrulanmış bir şifreleme şemasının, mesajın aslında bir iletişim oturumu içinde onu oluşturan aracı tarafından da gönderildiğine dair herhangi bir garanti sağlamamasıdır. Aşağıdaki üç saldırı vektörünü göz önünde bulundurun:


1. **Yeniden oynatma saldırısı**: Bir saldırgan, daha önceki bir noktada iki taraf arasında ele geçirdiği bir şifre metni ve bir etiketi yeniden gönderir.

2. **Yeniden sıralama saldırısı**: Bir saldırgan iki mesajı farklı zamanlarda ele geçirir ve bunları alıcıya ters sırada gönderir.

3. **Yansıma saldırısı**: Bir saldırgan A'dan B'ye gönderilen bir mesajı gözlemler ve bu mesajı A'ya da gönderir.


Saldırganın şifre metni hakkında hiçbir bilgisi olmamasına ve sahte şifre metinleri oluşturamamasına rağmen, yukarıdaki saldırılar yine de iletişimde önemli hasara neden olabilir.


Örneğin, iki taraf arasındaki belirli bir mesajın finansal fonların transferini içerdiğini varsayalım. Bir tekrarlama saldırısı fonları ikinci kez transfer edebilir. Kimliği doğrulanmış bir şifreleme şemasının bu tür saldırılara karşı hiçbir savunması yoktur.


Neyse ki, bu tür saldırılar bir iletişim oturumunda **tanımlayıcılar** ve **göreceli zaman göstergeleri** kullanılarak kolayca azaltılabilir.


Tanımlayıcılar şifrelemeden önce düz metin mesajına eklenebilir. Bu herhangi bir yansıma saldırısını engelleyecektir. Göreceli bir zaman göstergesi, örneğin, belirli bir iletişim oturumundaki bir sıra numarası olabilir. Her bir taraf şifrelemeden önce mesaja bir sıra numarası ekler, böylece alıcı mesajların hangi sırayla gönderildiğini bilir. Bu, yeniden sıralama saldırıları olasılığını ortadan kaldırır. Ayrıca tekrarlama saldırılarını da ortadan kaldırır. Bir saldırganın hat boyunca gönderdiği herhangi bir mesaj eski bir sıra numarasına sahip olacaktır ve alıcı mesajı tekrar işlemeyeceğini bilecektir.


Güvenli iletişim oturumlarının nasıl çalıştığını göstermek için yine Alice ve Bob'ü ele alalım. İleri geri toplam dört mesaj gönderiyorlar. Tanımlayıcılar ve sıra numaraları ile kimliği doğrulanmış bir şifreleme şemasının nasıl çalışacağını aşağıda *Şekil 11*'de görebilirsiniz.


İletişim oturumu Bob'in Alice'e $T_{0,B}$ mesaj etiketiyle $C_{0,B}$ şifreli metni göndermesiyle başlar. Şifreli metin mesajın yanı sıra bir tanımlayıcı (Bob) ve bir sıra numarası (0) içerir. T_{0,B}$ etiketi tüm şifreli metin üzerinden yapılır. Sonraki iletişimlerinde, Alice ve Bob bu protokolü sürdürür ve gerektiğinde alanları günceller.



*Şekil 12: Güvenli bir iletişim oturumu*


![Figure 12: A secure communication session](assets/Figure4-12.webp "Figure 12: A secure communication sessesion")







# RC4 ve AES

<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>





## RC4 akış şifresi

<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>


Bu bölümde, modern bir ilkel akış şifresi olan RC4 (veya "Rivest şifresi 4") ve modern bir blok şifresi olan AES ile bir şifreleme şemasının ayrıntılarını tartışacağız. RC4 şifresi bir şifreleme yöntemi olarak gözden düşmüş olsa da, AES modern simetrik şifreleme için standarttır. Bu iki örnek simetrik şifrelemenin nasıl çalıştığına dair daha iyi bir fikir verecektir.


___


Modern sözde rastgele akış şifrelerinin nasıl çalıştığına dair bir fikir sahibi olmak için RC4 akış şifresine odaklanacağım. Bu, WEP ve WAP kablosuz erişim noktası güvenlik protokollerinin yanı sıra TLS'de de kullanılan bir sözde rastgele akış şifresidir. RC4'ün kanıtlanmış birçok zayıflığı olduğu için gözden düşmüştür. Aslında, İnternet Mühendisliği Görev Gücü artık tüm TLS örneklerinde RC4 paketlerinin istemci ve sunucu uygulamaları tarafından kullanılmasını yasaklamıştır. Bununla birlikte, ilkel bir akış şifresinin nasıl çalıştığını göstermek için bir örnek olarak iyi çalışır.


Başlangıç olarak, önce bir düz metin mesajının bebek RC4 şifresiyle nasıl şifreleneceğini göstereceğim. Düz metin mesajımızın "SOUP" olduğunu varsayalım Bebek RC4 şifrelememiz ile şifreleme dört adımda gerçekleşir.


### Adım 1


İlk olarak, $S[0] = 0$ ile $S[7] = 7$ arasında bir **S** dizisi tanımlayın. Burada dizi basitçe, bazı programlama dillerinde (örneğin Python) liste olarak da adlandırılan, bir dizin tarafından düzenlenen değişken bir değer koleksiyonu anlamına gelir. Bu durumda, dizin 0'dan 7'ye kadar uzanır ve değerler de 0'dan 7'ye kadar uzanır. Yani **S** aşağıdaki gibidir:



- $S = [0, 1, 2, 3, 4, 5, 6, 7]$


Buradaki değerler ASCII sayıları değil, 1 baytlık dizelerin ondalık değer gösterimleridir. Yani 2 değeri $0000 \ 0011$ değerine eşittir. Dolayısıyla **S** dizisinin uzunluğu 8 bayttır.


### Adım 2


İkinci olarak, 1 ile 8 bayt arasında bir anahtar seçerek 8 bayt uzunluğunda bir anahtar dizisi **K** tanımlayın (baytların kesirlerine izin verilmez). Her bayt 8 bit olduğundan, anahtarınızın her baytı için 0 ile 255 arasında herhangi bir sayı seçebilirsiniz.


Diyelim ki **k** anahtarımızı $[14, 48, 9]$ olarak seçtik, böylece 3 bayt uzunluğa sahip olacak. Bu durumda, anahtar dizimizin her bir indeksi, sırayla, anahtarın o belirli elemanının ondalık değerine göre ayarlanır. Eğer tüm anahtarın üzerinden geçerseniz, anahtar dizisinin 8 yuvasını doldurana kadar en baştan tekrar başlayın. Dolayısıyla, anahtar dizimiz aşağıdaki gibidir:



- $K = [14, 48, 9, 14, 48, 9, 14, 48]$


### Adım 3


Üçüncü olarak, **anahtar çizelgeleme** olarak bilinen bir süreçte **K** anahtar dizisini kullanarak **S** dizisini dönüştüreceğiz. İşlem sözde kod olarak aşağıdaki gibidir:



- **J** ve **i** değişkenlerini oluşturun
- J = 0$ değişkenini ayarlayın
- 0'dan 7'ye kadar her $i$ için:
    - J = (j + S[i] + K[i]) \mod 8$ olarak ayarlayın
    - S[i]$ ve S[j]$'yi değiştirin


**S** dizisinin dönüşümü *Tablo 1* ile gösterilmiştir.


Başlangıç olarak **S**'nin başlangıç durumunu $[0, 1, 2, 3, 4, 5, 6, 7]$ olarak görebilirsiniz ve **j** için başlangıç değeri 0'dır. Bu, $[14, 48, 9, 14, 48, 9, 14, 48]$ anahtar dizisi kullanılarak dönüştürülecektir.


For döngüsü $i = 0$ ile başlar. Yukarıdaki sözde kodumuza göre, **j** 'nin yeni değeri 6 olur ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). S[0]$ ve S[6]$ değiştirildiğinde, **S**'nin 1 turdan sonraki durumu $[6, 1, 2, 3, 4, 5, 0, 7]$ olur.


Bir sonraki satırda, $i = 1$. Tekrar for döngüsüne girildiğinde, **j** 7 değerini alır ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). **S**'nin mevcut durumu olan $[6, 1, 2, 3, 4, 5, 0, 7]$ ile $S[1]$ ve $S[7]$'nin yer değiştirmesi, 2. turdan sonra $[6, 7, 2, 3, 4, 5, 0, 1]$ sonucunu verir.


Bu işleme **S** dizisi için alttaki son satırı üretene kadar devam ediyoruz, $[6, 4, 1, 0, 3, 7, 5, 2]$.



*Tablo 1: Anahtar programlama tablosu*


| Round   | i   | j   |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|         |     |     |     |      |      |      |      |      |      |      |      |
| Initial |     | 0   |     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 1       | 0   | 6   |     | 6    | 1    | 2    | 3    | 4    | 5    | 0    | 7    |
| 2       | 1   | 7   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 3       | 2   | 2   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 4       | 3   | 3   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 5       | 4   | 3   |     | 6    | 7    | 2    | 0    | 3    | 5    | 4    | 1    |
| 6       | 5   | 6   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 1    |
| 7       | 6   | 1   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 2    |
| 8       | 7   | 2   |     | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |

### Adım 4


Dördüncü adım olarak **keystream** üretiyoruz. Bu, göndermek istediğimiz mesaja eşit uzunlukta bir sözde rastgele dizedir. Bu, orijinal "SOUP" mesajını şifrelemek için kullanılacaktır Anahtar dizisinin mesaj kadar uzun olması gerektiğinden, 4 baytlık bir diziye ihtiyacımız var.


Anahtar akışı aşağıdaki sözde kod tarafından üretilir:



- **J**, **i** ve **t** değişkenlerini oluşturun.
- J = 0$ olarak ayarlayın.
- Düz metnin her $i$'si için, $i = 1$'den başlayıp $i = 4$'e kadar, anahtar dizisinin her baytı aşağıdaki gibi üretilir:
    - $j = (j + S[i]) \mod 8$
    - S[i]$ ve S[j]$ değerlerini değiştirin.
    - $t = (S[i] + S[j]) \mod 8$
    - Anahtar dizisinin $i^{th}$ baytı = $S[t]$


Hesaplamaları *Tablo 2*'den takip edebilirsiniz.


**S**'nin başlangıç durumu $S = [6, 4, 1, 0, 3, 7, 5, 2]$'dir. $I = 1$ olarak ayarlandığında, **j** değeri 4 olur ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Daha sonra $S[1]$ ve $S[4]$ değerlerini değiştirerek ikinci satırdaki **S** dönüşümünü elde ederiz, $[6, 3, 1, 0, 4, 7, 5, 2]$. Bu durumda **t** değeri 7'dir ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Son olarak, anahtar dizisi için bayt $S[7]$ veya 2'dir.


Daha sonra aşağıdaki dört baytı elde edene kadar diğer baytları üretmeye devam ederiz: 2, 6, 3 ve 7. Bu baytların her biri daha sonra "SOUP" düz metninin her bir harfini şifrelemek için kullanılabilir.


Başlangıç olarak, bir ASCII tablosu kullanarak, altta yatan bayt dizelerinin ondalık değerleriyle kodlanan "SOUP "un "83 79 85 80" olduğunu görebiliriz. "2 6 3 7" anahtar dizisi ile birleştirildiğinde "85 85 88 87" elde edilir ve bu değer modulo 256 işleminden sonra da aynı kalır. ASCII'de "85 85 88 87" şifreli metni "UUXW "ye eşittir.


Şifrelenecek kelime **S** dizisinden daha uzun olsaydı ne olurdu? Bu durumda, **S** dizisi, anahtar dizisindeki bayt sayısı düz metindeki harf sayısına eşit olana kadar, düz metnin her baytı **i** için yukarıda gösterilen şekilde dönüşmeye devam eder.



*Tablo 2: Ana akım üretimi*


| i   | j   | t   | Keystream | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     |     |     |           |      |      |      |      |      |      |      |      |
|     | 0   |     |           | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |
| 1   | 4   | 7   | 2         | 6    | 3    | 1    | 0    | 4    | 7    | 5    | 2    |
| 2   | 5   | 0   | 6         | 6    | 3    | 7    | 0    | 4    | 1    | 5    | 2    |
| 3   | 5   | 1   | 3         | 6    | 3    | 7    | 1    | 4    | 0    | 5    | 2    |
| 4   | 1   | 7   | 2         | 6    | 4    | 7    | 1    | 3    | 0    | 5    | 2    |

Az önce tartıştığımız örnek, **RC4 akış şifresinin** sadece sulandırılmış bir versiyonudur. Gerçek RC4 akış şifresi 8 bayt değil 256 bayt uzunluğunda bir **S** dizisine ve 1 ile 8 bayt arasında değil 1 ile 256 bayt arasında olabilen bir anahtara sahiptir. Anahtar dizisi ve anahtar akışlarının tümü **S** dizisinin 256 baytlık uzunluğu dikkate alınarak üretilir. Hesaplamalar son derece daha karmaşık hale gelir, ancak ilkeler aynı kalır. Aynı anahtar [14,48,9] kullanılarak, standart RC4 şifresiyle, düz metin mesajı "SOUP" onaltılık formatta 67 02 ed df olarak şifrelenir.


Anahtar dizisinin düz metin mesajından veya şifreli metinden bağımsız olarak güncellendiği bir akış şifresi **eşzamanlı bir akış şifresidir**. Anahtar dizisi yalnızca anahtara bağlıdır. Açıkçası, RC4 eşzamanlı bir akış şifresi örneğidir, çünkü anahtar akışının düz metin veya şifreli metin ile hiçbir ilişkisi yoktur. Bir önceki bölümde bahsedilen tüm ilkel akış şifrelerimiz, kaydırmalı şifre, Vigenère şifresi ve tek kullanımlık ped de dahil olmak üzere, eşzamanlı türdendir.


Buna karşılık, bir **asenkron akış şifresi** hem anahtar hem de şifreli metnin önceki Elements'sı tarafından üretilen bir anahtar akışına sahiptir. Bu tip şifrelere **kendini senkronize eden şifre** de denir.


Önemli olarak, RC4 ile üretilen anahtar dizisi tek seferlik bir ped olarak ele alınmalıdır ve anahtar dizisini bir sonraki seferde tam olarak aynı şekilde üretemezsiniz. Her seferinde anahtarı değiştirmek yerine, pratik çözüm, bytestream üretmek için anahtarı bir **Nonce** ile birleştirmektir.




## 128 bit anahtarlı AES

<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>


Önceki bölümde belirtildiği gibi, Ulusal Standartlar ve Teknoloji Enstitüsü (NIST) 1997 ve 2000 yılları arasında yeni bir simetrik şifreleme standardı belirlemek için bir yarışma düzenledi. Yarışmayı **Rijndael şifresi** kazanmıştır. Bu isim Belçikalı yaratıcıları Vincent Rijmen ve Joan Daemen'in isimleri üzerine bir kelime oyunudur.


Rijndael şifresi bir **blok şifresidir**, yani anahtar uzunlukları ve blok boyutları için farklı özelliklerle kullanılabilen bir çekirdek algoritması vardır. Daha sonra, şifreleme şemaları oluşturmak için farklı çalışma modlarıyla kullanabilirsiniz.


NIST yarışması komitesi, **Gelişmiş Şifreleme Standardı'nın (AES)** bir parçası olarak Rijndael şifresinin kısıtlı bir versiyonunu, yani 128 bit blok boyutları ve 128 bit, 192 bit veya 256 bit anahtar uzunlukları gerektiren bir versiyonunu kabul etmiştir. Rijndael şifrelemesinin bu kısıtlı versiyonu birden fazla çalışma modu altında da kullanılabilir. Standardın spesifikasyonu **Gelişmiş Şifreleme Standardı (AES)** olarak bilinir.


AES'in çekirdeği olan Rijndael şifrelemesinin nasıl çalıştığını göstermek için 128 bitlik bir anahtarla şifreleme sürecini göstereceğim. Anahtar boyutu, her bir şifreleme bloğu için gerçekleştirilen tur sayısı üzerinde etkilidir. 128 bit anahtarlar için 10 tur gereklidir. 192 bit ve 256 bit ile, sırasıyla 12 ve 14 tur olurdu.


Buna ek olarak, AES'in **ECB-modunda** kullanıldığını varsayacağım. Bu, açıklamayı biraz daha kolaylaştırır ve Rijndael algoritması için önemli değildir. Emin olmak için, ECB modu pratikte güvenli değildir çünkü deterministik şifrelemeye yol açar. AES ile en yaygın kullanılan güvenli mod **CBC** (Cipher Block Chaining)'dir.


Anahtara $K_0$ diyelim. Yukarıdaki parametrelerle yapı *Şekil 1*'deki gibi görünür, burada $M_i$ 128 bitlik düz metin mesajının bir bölümünü ve $C_i$ 128 bitlik şifreli metnin bir bölümünü temsil eder. Düz metin blok boyutuna eşit olarak bölünemiyorsa, son blok için düz metne dolgu eklenir.



*Şekil 1: 128 bit anahtarlı AES-ECB*


![Figure 1: AES-ECB with a 128-bit key](assets/Figure5-1.webp "Figure 1: AES-ECB with a 128-bit key")


Her 128 bitlik metin bloğu Rijndael şifreleme şemasında on turdan geçer. Bu, her tur için ayrı bir tur anahtarı gerektirir ($K_1$ ila $K_{10}$). Bunlar her tur için orijinal 128-bit $K_0$ anahtarından bir **anahtar genişletme algoritması** kullanılarak üretilir. Dolayısıyla, şifrelenecek her metin bloğu için orijinal $K_0$ anahtarının yanı sıra on ayrı tur anahtarı kullanacağız. Şifreleme gerektiren her 128 bitlik düz metin bloğu için aynı 11 anahtarın kullanıldığını unutmayın.


Anahtar genişletme algoritması uzun ve karmaşıktır. Üzerinde çalışmanın çok az didaktik faydası vardır. İsterseniz anahtar genişletme algoritmasını kendi başınıza inceleyebilirsiniz. Yuvarlak anahtarlar üretildikten sonra, Rijndael şifresi ilk 128 bitlik düz metin bloğunu, $M_1$, *Şekil 2*'de görüldüğü gibi manipüle edecektir. Şimdi bu adımların üzerinden geçeceğiz.


*Şekil 2: $M_1$'in Rijndael şifresi ile manipülasyonu:*


**Round 0:**


- S_0$ üretmek için $M_1$ ve $K_0$ XOR


---

**n = {1,...,9} için Round n:**


- XOR $S_{n-1}$ ve $K_n$
- Bayt Değiştirme
- Vardiya Satırları
- Karışık Sütunlar
- S_n$ üretmek için $S$ ve $K_n$ XOR


---

**10. Tur:**


- XOR $S_9$ ve $K_{10}$
- Bayt Değiştirme
- Vardiya Satırları
- S_{10}$ üretmek için $S$ ve $K_{10}$ XOR
- $S_{10}$ = $C_1$



### Tur 0


Rijndael şifrelemesinin 0. turu basittir. 128-bit düz metin ile özel anahtar arasında bir XOR işlemi yapılarak $S_0$ dizisi üretilir. Yani,



- $S_0 = M_1 \oplus K_0$


### 1. Tur


1. turda, $S_0$ dizisi ilk olarak bir XOR işlemi kullanılarak $K_1$ tur anahtarı ile birleştirilir. Bu yeni bir $S$ durumu üretir.


İkinci olarak, **byte substitution** işlemi $S$'ın mevcut durumu üzerinde gerçekleştirilir. Bu işlem, 16 baytlık $S$ dizisinin her baytını alıp **Rijndael'in S-kutusu** adı verilen bir diziden bir baytla değiştirerek çalışır. Her baytın benzersiz bir dönüşümü vardır ve sonuç olarak $S$'ın yeni bir durumu üretilir. Rijndael'in S-kutusu *Şekil 3*'te gösterilmiştir.


*Şekil 3: Rijndael'in S-Box*


|     | 00  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  | 0A  | 0B  | 0C  | 0D  | 0E  | 0F  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00  | 63  | 7C  | 77  | 7B  | F2  | 6B  | 6F  | C5  | 30  | 01  | 67  | 2B  | FE  | D7  | AB  | 76  |
| 10  | CA  | 82  | C9  | 7D  | FA  | 59  | 47  | F0  | AD  | D4  | A2  | AF  | 9C  | A4  | 72  | C0  |
| 20  | B7  | FD  | 93  | 26  | 36  | 3F  | F7  | CC  | 34  | A5  | E5  | F1  | 71  | D8  | 31  | 15  |
| 30  | 04  | C7  | 23  | C3  | 18  | 96  | 05  | 9A  | 07  | 12  | 80  | E2  | EB  | 27  | B2  | 75  |
| 40  | 09  | 83  | 2C  | 1A  | 1B  | 6E  | 5A  | A0  | 52  | 3B  | D6  | B3  | 29  | E3  | 2F  | 84  |
| 50  | 53  | D1  | 00  | ED  | 20  | FC  | B1  | 5B  | 6A  | CB  | BE  | 39  | 4A  | 4C  | 58  | CF  |
| 60  | D0  | EF  | AA  | FB  | 43  | 4D  | 33  | 85  | 45  | F9  | 02  | 7F  | 50  | 3C  | 9F  | A8  |
| 70  | 51  | A3  | 40  | 8F  | 92  | 9D  | 38  | F5  | BC  | B6  | DA  | 21  | 10  | FF  | F3  | D2  |
| 80  | CD  | 0C  | 13  | EC  | 5F  | 97  | 44  | 17  | C4  | A7  | 7E  | 3D  | 64  | 5D  | 19  | 73  |
| 90  | 60  | 81  | 4F  | DC  | 22  | 2A  | 90  | 88  | 46  | EE  | B8  | 14  | DE  | 5E  | 0B  | DB  |
| A0  | E0  | 32  | 3A  | 0A  | 49  | 06  | 24  | 5C  | C2  | D3  | AC  | 62  | 91  | 95  | E4  | 79  |
| B0  | E7  | C8  | 37  | 6D  | 8D  | D5  | 4E  | A9  | 6C  | 56  | F4  | EA  | 65  | 7A  | AE  | 08  |
| C0  | BA  | 78  | 25  | 2E  | 1C  | A6  | B4  | C6  | E8  | DD  | 74  | 1F  | 4B  | BD  | 8B  | 8A  |
| D0  | 70  | 3E  | B5  | 66  | 48  | 03  | F6  | 0E  | 61  | 35  | 57  | B9  | 86  | C1  | 1D  | 9E  |
| E0  | E1  | F8  | 98  | 11  | 69  | D9  | 8E  | 94  | 9B  | 1E  | 87  | E9  | CE  | 55  | 28  | DF  |
| F0  | 8C  | A1  | 89  | 0D  | BF  | E6  | 42  | 68  | 41  | 99  | 2D  | 0F  | B0  | 54  | BB  | 16  |


Bu S-Box, Rijndael şifresinde soyut cebirin, özellikle de **Galois alanlarının** devreye girdiği bir yerdir.


Başlangıç olarak, 00 ile FF arasındaki her olası bayt elemanını 8 bitlik bir vektör olarak tanımlarsınız. Bu tür her vektör, modulo işlemi için indirgenemez polinomun $x^8 + x^4 + x^3 + x + 1$ olduğu **Galois alanı GF(2^8)**'in bir elemanıdır. Bu özelliklere sahip Galois cismine **Rijndael'in Sonlu Cismi** de denir.


Daha sonra, alandaki her olası öğe için **Nyberg S-Box** adı verilen bir kutu oluştururuz. Bu kutuda, her bayt **çarpımsal tersi** ile eşleştirilir (yani, çarpımları 1'e eşit olacak şekilde). Daha sonra bu değerleri Nyberg S-kutusundan Rijndael'in S-kutusuna **affine dönüşümü** kullanarak eşleriz.


**S** dizisi üzerindeki üçüncü işlem **shift rows** işlemidir. Bu işlem **S**'nin durumunu alır ve on altı baytın tümünü bir matriste listeler. Matrisin doldurulması sol üstten başlar ve yukarıdan aşağıya doğru ilerleyerek ve ardından her sütun doldurulduğunda bir sütunu sağa ve üste kaydırarak yoluna devam eder.


S** matrisi oluşturulduktan sonra, dört satır kaydırılır. İlk satır aynı kalır. İkinci satır bir sola kaydırılır. Üçüncüsü iki sola kaydırılır. Dördüncü sıra üçü sola kaydırır. İşlemin bir örneği *Şekil 4*'da verilmiştir. S**'nin orijinal durumu üstte ve satır kaydırma işleminden sonra ortaya çıkan durum altta gösterilmiştir.


*Şekil 4: Satır kaydırma işlemi*


| F1   | A0   | B1   | 23   |
|------|------|------|------|
| 59   | EF   | 09   | 82   |
| 97   | 01   | B0   | CC   |
| D4   | 72   | 04   | 21   |
| F1   | A0   | B1   | 23   |
|------|------|------|------|
| EF   | 09   | 82   | 59   |
| B0   | CC   | 97   | 01   |
| 21   | D4   | 72   | 04   |


Dördüncü adımda, **Galois alanları** tekrar ortaya çıkar. Başlamak için, **S** matrisinin her bir sütunu *Şekil 5*'da görülen 4 x 4 matrisinin sütunuyla çarpılır. Ancak bu normal matris çarpımı yerine, $x^8 + x^4 + x^3 + x + 1$ gibi indirgenemez bir polinomun modulo vektör çarpımıdır. Elde edilen vektör katsayıları bir baytın tek tek bitlerini temsil eder.


*Şekil 5: Karışım sütunları matrisi*


| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
| 01   | 01   | 02   | 03   |
| 03   | 01   | 01   | 02   |

**S** matrisinin ilk sütununun yukarıdaki 4 x 4 matris ile çarpımı *Şekil 6*'daki sonucu verir.


*Şekil 6: İlk sütunun çarpımı:*


$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$


Bir sonraki adım olarak, matristeki tüm terimlerin polinomlara dönüştürülmesi gerekecektir. Örneğin, F1 1 baytı temsil eder ve $x^7 + x^6 + x^5 + x^4 + 1$ olur ve 03 1 baytı temsil eder ve $x + 1$ olur.


Tüm çarpımlar daha sonra **modulo** $x^8 + x^4 + x^3 + x + 1$ şeklinde gerçekleştirilir. Bu, sütunun dört hücresinin her birinde dört polinomun toplanmasıyla sonuçlanır. Bu toplamaları **modulo 2** yaptıktan sonra, dört polinom elde edersiniz. Bu polinomların her biri 8 bitlik bir dizeyi veya **S**'nin 1 baytını temsil eder. Kapsamlı oldukları için tüm bu hesaplamaları burada *Şekil 6*'daki matris üzerinde gerçekleştirmeyeceğiz.


İlk sütun işlendikten sonra, **S** matrisinin diğer üç sütunu da aynı şekilde işlenir. Sonunda, bu bir diziye dönüştürülebilen on altı baytlık bir matris verecektir.


Son adım olarak, **S** dizisi bir **XOR** işleminde yuvarlak anahtarla tekrar birleştirilir. Bu $S_1$ durumunu üretir. Yani,



- $S_1 = S \oplus K_0$


### 2'den 10'a kadar olan rauntlar


2'den 9'a kadar olan turlar 1. turun tekrarıdır, *mutatis mutandis*. Son tur, **sütunları karıştır** adımının ortadan kaldırılması dışında önceki turlara çok benzer. Yani, 10. tur aşağıdaki gibi yürütülür:



- $S_9 \oplus K_{10}$
- Bayt Değiştirme
- Vardiya Satırları
- $S_{10} = S \oplus K_{10}$


S_{10}$ durumu şimdi şifreli metnin ilk 128 biti olan $C_1$ olarak ayarlanmıştır. Kalan 128 bitlik düz metin blokları üzerinden ilerlendiğinde **C** şifreli metninin tamamı elde edilir.


### Rijndael şifrelemesinin işlemleri


Rijndael şifresinde görülen farklı işlemlerin arkasındaki mantık nedir?


Ayrıntılara girmeden, şifreleme şemaları karışıklık ve yayılma yaratma derecelerine göre değerlendirilir. Şifreleme şemasının yüksek derecede **karışıklık** yaratması, şifreli metnin düz metinden büyük ölçüde farklı göründüğü anlamına gelir. Şifreleme şeması yüksek derecede **difüzyon** içeriyorsa, düz metinde yapılan herhangi bir küçük değişikliğin büyük ölçüde farklı bir şifreli metin ürettiği anlamına gelir.


Rijndael şifrelemesinin arkasındaki işlemlerin mantığı, hem yüksek derecede karışıklık hem de yayılma üretmeleridir. Karışıklık Bayt değiştirme işlemi tarafından üretilirken, yayılma satır kaydırma ve sütunları karıştırma işlemleri tarafından üretilir.


# Asimetrik Kriptografi

<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>



## Anahtar dağıtımı ve yönetimi sorunu

<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>


Simetrik kriptografide olduğu gibi, asimetrik şemalar hem gizliliği hem de kimlik doğrulamayı sağlamak için kullanılabilir. Ancak bunun aksine, bu şemalar bir yerine iki anahtar kullanır: bir özel ve bir açık anahtar.


Araştırmamıza asimetrik kriptografinin keşfiyle, özellikle de onu teşvik eden sorunlarla başlıyoruz. Daha sonra, şifreleme ve kimlik doğrulama için asimetrik şemaların yüksek seviyede nasıl çalıştığını tartışıyoruz. Daha sonra, asimetrik kimlik doğrulama şemalarını anlamak için kilit öneme sahip olan ve Bölüm 4'te tartıştığımız Hash tabanlı mesaj kimlik doğrulama kodları gibi diğer kriptografik bağlamlarla da ilgili olan Hash işlevlerini tanıtıyoruz.


___



Bob'nin Kuzey Amerika'da milyonlarca müşterisi olan çevrimiçi bir spor malzemeleri perakendecisi olan Jim's Sporting Goods'tan yeni bir yağmurluk satın almak istediğini varsayalım. Bu, onlardan yapacağı ilk alışveriş olacak ve kredi kartını kullanmak istiyor. Bu nedenle, Bob'nin öncelikle Jim's Sporting Goods'ta bir hesap oluşturması gerekecek, bu da Address ve kredi kartı bilgileri gibi kişisel bilgilerin gönderilmesini gerektiriyor. Daha sonra yağmurluğu satın almak için gereken adımları uygulayabilir.


Bob ve Jim's Sporting Goods, internetin açık bir iletişim sistemi olduğunu göz önünde bulundurarak bu süreç boyunca iletişimlerinin güvenli olmasını sağlamak isteyecektir. Örneğin, hiçbir potansiyel saldırganın Bob'nin kredi kartı ve Address bilgilerini tespit edemeyeceğinden ve hiçbir potansiyel saldırganın onun alışverişlerini tekrarlayamayacağından veya onun adına sahte alışverişler yapamayacağından emin olmak isteyeceklerdir.


Önceki bölümde tartışıldığı gibi gelişmiş bir kimlik doğrulamalı şifreleme şeması Bob ile Jim's Sporting Goods arasındaki iletişimi kesinlikle güvenli hale getirebilir. Ancak böyle bir şemanın uygulanmasının önünde pratik engeller olduğu açıktır.


Bu pratik engelleri örneklemek için, sadece simetrik kriptografi araçlarının var olduğu bir dünyada yaşadığımızı varsayalım. Bu durumda Jim's Sporting Goods ve Bob güvenli iletişimi sağlamak için ne yapabilirdi?


Bu koşullar altında, güvenli bir şekilde iletişim kurmak için önemli maliyetlerle karşı karşıya kalacaklardır. İnternet açık bir iletişim sistemi olduğundan, bu sistem üzerinden bir anahtar seti Exchange oluşturamazlar. Bu nedenle, Bob ve Jim's Sporting Goods'un bir temsilcisinin Exchange anahtarını şahsen yapmaları gerekecektir.


Bir olasılık, Jim's Sporting Goods'un Bob ve diğer yeni müşterilerin güvenli iletişim için bir dizi anahtar alabilecekleri özel anahtar Exchange konumları oluşturmasıdır. Bunun önemli bir organizasyonel maliyet getireceği ve yeni müşterilerin alışveriş yapma verimliliğini büyük ölçüde azaltacağı açıktır.


Alternatif olarak, Jim's Sporting Goods çok güvenilir bir kurye ile Bob bir çift anahtar gönderebilir. Bu muhtemelen anahtar Exchange konumlarını organize etmekten daha etkilidir. Ancak bu yine de önemli maliyetler getirecektir, özellikle de birçok müşteri yalnızca bir veya birkaç alışveriş yapıyorsa.


Ayrıca, kimliği doğrulanmış şifreleme için simetrik bir şema Jim's Sporting Goods'u tüm müşterileri için ayrı anahtar setleri saklamaya zorlar. Bu, bırakın milyonları, binlerce müşteri için bile önemli bir pratik zorluk olacaktır.


Bu son noktayı anlamak için Jim's Sporting Goods'un her müşteriye aynı anahtar çiftini sağladığını varsayalım. Bu, her müşterinin - ya da bu anahtar çiftini elde edebilecek herhangi birinin - Jim's Sporting Goods ile müşterileri arasındaki tüm iletişimi okumasına ve hatta manipüle etmesine olanak tanıyacaktır. O halde, iletişimlerinizde kriptografiyi hiç kullanmayabilirsiniz.


Bir dizi anahtarın sadece bazı müşteriler için tekrarlanması bile korkunç bir güvenlik uygulamasıdır. Herhangi bir potansiyel saldırgan, şemanın bu özelliğinden faydalanmaya çalışabilir (Kerckhoffs'un ilkesi uyarınca saldırganların bir şema hakkında anahtarlar dışında her şeyi bildiklerinin varsayıldığını unutmayın)


Dolayısıyla Jim's Sporting Goods, bu anahtar çiftlerinin nasıl dağıtıldığından bağımsız olarak her müşteri için bir çift anahtar saklamak zorunda kalacaktır. Bu durum açıkça çeşitli pratik sorunlar ortaya çıkarmaktadır.



- Jim's Sporting Goods'un her müşteri için bir set olmak üzere milyonlarca anahtar çifti saklaması gerekecektir.
- Bu anahtarlar bilgisayar korsanları için kesin bir hedef olacağından uygun şekilde güvence altına alınmalıdır. Herhangi bir güvenlik ihlali, ya özel anahtar Exchange konumlarında ya da kurye ile maliyetli anahtar değişimlerinin tekrarlanmasını gerektirecektir.
- Jim's Sporting Goods'un her müşterisi bir çift anahtarı evinde güvenle saklamak zorundadır. Kayıplar ve hırsızlıklar meydana gelecek ve anahtar değişimlerinin tekrarlanmasını gerektirecektir. Müşteriler, internet üzerinden iletişim kurmak ve işlem yapmak istedikleri diğer çevrimiçi mağazalar veya diğer türden kuruluşlar için de bu süreçten geçmek zorunda kalacaklardır.


Az önce açıklanan bu iki ana sorun 1970'lerin sonlarına kadar çok temel meselelerdi. Bunlar sırasıyla **anahtar dağıtım sorunu** ve **anahtar yönetimi sorunu** olarak bilinmekteydi.


Bu sorunlar elbette her zaman vardı ve geçmişte sık sık baş ağrısı yaratıyordu. Örneğin askeri güçler, sahadaki personele güvenli iletişim için anahtarlı kitapları büyük risk ve maliyetlerle sürekli olarak dağıtmak zorunda kalıyordu. Ancak dünya, özellikle sivil toplum kuruluşları için giderek daha uzun mesafeli, dijital bir iletişim ortamına dönüşürken bu sorunlar daha da kötüleşiyordu.


Bu sorunlar 1970'lerde çözülmemiş olsaydı, Jim's Sporting Goods'da verimli ve güvenli alışveriş muhtemelen var olmayacaktı. Aslında, pratik ve güvenli e-posta, çevrimiçi bankacılık ve alışveriş ile modern dünyamızın çoğu muhtemelen sadece uzak bir hayal olurdu. Bitcoin'ye benzeyen herhangi bir şey bile var olamazdı.


Peki, 1970'lerde ne oldu? İnternet üzerinden anında alışveriş yapabilmemiz ve World Wide Web'de güvenli bir şekilde gezinebilmemiz nasıl mümkün olabiliyor? Akıllı telefonlarımızdan dünyanın dört bir yanına anında Bitcoin gönderebilmemiz nasıl mümkün olabiliyor?



## Kriptografide yeni yönler

<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>


1970'lere gelindiğinde, anahtar dağıtımı ve anahtar yönetimi sorunları bir grup Amerikalı akademik kriptografın dikkatini çekmişti: Whitfield Diffie, Martin Hellman ve Ralph Merkle. Meslektaşlarının çoğundan gelen ciddi şüphecilik karşısında, buna bir çözüm bulmaya giriştiler.


Girişimlerinin en azından birincil motivasyonu, açık bilgisayar iletişiminin dünyamızı derinden etkileyeceği öngörüsüydü. Diffie ve Helmann'ın 1976'da belirttiği gibi,


> Bilgisayar kontrollü iletiĢim ağlarının geliĢimi, dünyanın karĢı taraflarındaki insanlar ya da bilgisayarlar arasında zahmetsiz ve ucuz iletiĢim vaat etmekte, çoğu postanın ve birçok gezinin yerini telekomünikasyon almaktadır. Birçok uygulama için bu bağlantıların hem gizli dinlemeye hem de yasal olmayan mesajların enjekte edilmesine karĢı güvenli hale getirilmesi gerekmektedir. Ancak Ģu anda güvenlik sorunlarının çözümü iletiĢim teknolojisinin diğer alanlarının oldukça gerisinde kalmıĢtır. *Çağdaş kriptografi gereksinimleri karşılayamamaktadır, çünkü kullanımı sistem kullanıcılarına teleprocessing'in birçok faydasını ortadan kaldıracak kadar ciddi sakıncalar getirecektir.* [1]

Diffie, Hellman ve Merkle'nin azmi sonuç verdi. Sonuçlarının ilk yayını Diffie ve Helmann'ın 1976 yılında yayınladıkları "Kriptografide Yeni Yönelimler" başlıklı makaleydi Bu makalede, anahtar dağıtımı ve anahtar yönetimi sorunlarına Address için iki orijinal yol sundular.


Sundukları ilk çözüm uzaktan *key-Exchange protokolü*, yani güvensiz bir iletişim kanalı üzerinden bir veya daha fazla simetrik anahtarın Exchange'ü için bir dizi kuraldı. Bu protokol artık *Diffie-Helmann anahtarı Exchange* veya *Diffie-Helmann-Merkle anahtarı Exchange* olarak bilinmektedir. [2]


Diffie-Helmann anahtarı Exchange ile, iki taraf önce internet gibi güvensiz bir kanalda bazı bilgileri herkese açık olarak Exchange eder. Daha sonra bu bilgilere dayanarak, güvenli iletişim için bağımsız olarak bir simetrik anahtar (veya bir çift simetrik anahtar) oluştururlar. Her iki taraf da anahtarlarını bağımsız olarak oluştururken, herkese açık olarak paylaştıkları bilgiler bu anahtar oluşturma sürecinin her ikisi için de aynı sonucu vermesini sağlar.


Daha da önemlisi, güvensiz kanal üzerinden taraflar arasında aleni olarak değiş tokuş edilen bilgileri herkes gözlemleyebilirken, sadece Exchange bilgisini paylaşan iki taraf bu bilgilerden simetrik anahtarlar oluşturabilir.


Bu elbette kulağa tamamen mantığa aykırı geliyor. Nasıl olur da iki taraf, sadece kendilerinin simetrik anahtarlar oluşturmasına izin verecek bazı bilgileri herkese açık olarak Exchange yapabilir? Exchange bilgisini gözlemleyen bir başkası neden aynı anahtarları oluşturamasın?


Elbette güzel bir matematiğe dayanıyor. Diffie-Helmann anahtarı Exchange, bir tuzak kapısı olan tek yönlü bir fonksiyon aracılığıyla çalışır. Bu iki terimin anlamını sırayla tartışalım.


Size $f(x)$ fonksiyonu ve $f(a) = y$ sonucu verildiğini varsayalım; burada $a$, $x$ için belirli bir değerdir. Eğer $a$ ve $f(x)$ verildiğinde $y$ değerini hesaplamak kolaysa, ancak $y$ ve $f(x)$ verildiğinde $a$ değerini hesaplamak hesaplama açısından olanaksızsa, $f(x)$'in **tek yönlü bir fonksiyon** olduğunu söyleriz. Elbette **tek yönlü fonksiyon** adı, böyle bir fonksiyonun yalnızca tek bir yönde hesaplanmasının pratik olmasından kaynaklanmaktadır.


Bazı tek yönlü fonksiyonlar **tuzak kapısı** olarak bilinen bir özelliğe sahiptir. Yalnızca $y$ ve $f(x)$ verildiğinde $a$ değerini hesaplamak pratikte imkansız olsa da, $y$ değerinden $a$ değerini hesaplamayı mümkün kılan belirli bir $Z$ bilgisi vardır. Bu $Z$ bilgi parçası **trapdoor** olarak bilinir. Tuzak kapısı olan tek yönlü fonksiyonlar **tuzak kapısı fonksiyonları** olarak bilinir.


Burada Diffie-Helmann anahtarı Exchange'un detaylarına girmeyeceğiz. Ancak esasen her katılımcı, bir kısmı herkese açık olarak paylaşılan ve bir kısmı gizli kalan bazı bilgiler oluşturur. Daha sonra her bir taraf kendi gizli bilgisini ve diğer tarafın paylaştığı açık bilgiyi alarak bir özel anahtar oluşturur. Ve mucizevi bir şekilde, her iki taraf da aynı özel anahtara sahip olur.


Diffie Helmann anahtarı Exchange'ta iki taraf arasında sadece herkese açık olarak paylaşılan bilgileri gözlemleyen herhangi bir taraf bu hesaplamaları kopyalayamaz. Bunu yapabilmek için iki taraftan birinin özel bilgisine ihtiyaçları olacaktır.


Diffie-Helmann anahtarı Exchange'in 1976 tarihli makalede sunulan temel versiyonu çok güvenli olmasa da, temel protokolün sofistike versiyonları bugün hala kullanılmaktadır. En önemlisi, taşıma Layer güvenlik protokolünün en son sürümündeki (sürüm 1.3) her anahtar Exchange protokolü, esasen Diffie ve Hellman tarafından 1976'da sunulan protokolün zenginleştirilmiş bir sürümüdür. Aktarım Layer güvenlik protokolü, Web içeriği alışverişi standardı olan hiper metin aktarım protokolüne (http) göre biçimlendirilmiş bilgilerin güvenli bir şekilde alışverişi için kullanılan baskın protokoldür.


Daha da önemlisi, Diffie-Helmann anahtarı Exchange asimetrik bir şema değildir. Kesin konuşmak gerekirse, tartışmalı bir şekilde simetrik anahtar kriptografisi alanına aittir. Ancak hem Diffie-Helmann anahtarı Exchange hem de asimetrik kriptografi, tuzak kapıları olan tek yönlü sayı teorisi fonksiyonlarına dayandığından, genellikle birlikte tartışılırlar.


Diffie ve Helmann'ın 1976 tarihli makalelerinde anahtar dağıtımı ve yönetimi sorununa Address için önerdikleri ikinci yol elbette asimetrik kriptografiydi.


Diffie-Hellman anahtarı Exchange sunumlarının aksine, sadece asimetrik kriptografik şemaların makul bir şekilde nasıl inşa edilebileceğinin genel hatlarını sunmuşlardır. Bu tür şemalarda makul güvenlik için gereken koşulları özellikle yerine getirebilecek herhangi bir tek yönlü fonksiyon sunmamışlardır.


Ancak asimetrik bir şemanın pratik bir uygulaması bir yıl sonra üç farklı akademik kriptograf ve matematikçi tarafından bulundu: Ronald Rivest, Adi Shamir ve Leonard Adleman. [3] Ortaya koydukları kriptosistem **RSA kriptosistemi** (soyadlarından sonra) olarak tanındı.


Asimetrik kriptografide (ve Diffie Helmann anahtar Exchange) kullanılan trapdoor fonksiyonlarının hepsi iki ana **hesaplamalı Hard problemi** ile ilgilidir: asal çarpanlara ayırma ve ayrık logaritmaların hesaplanması.


**Asal çarpanlara ayırma**, adından da anlaşılacağı üzere, bir tamsayının asal çarpanlarına ayrılmasını gerektirir. RSA problemi, asal çarpanlara ayırma ile ilgili en bilinen kriptosistem örneğidir.


**Ayrık logaritma problemi** döngüsel gruplarda ortaya çıkan bir problemdir. Belirli bir devirli grupta bir üreteç verildiğinde, üreteçten grupta başka bir eleman üretmek için gereken benzersiz üssün hesaplanmasını gerektirir.


Ayrık logaritma tabanlı şemalar iki ana tür döngüsel gruba dayanır: tam sayıların çarpımsal grupları ve eliptik eğriler üzerindeki noktaları içeren gruplar. "Kriptografide Yeni Yönelimler "de sunulan orijinal Diffie Helmann anahtarı Exchange, tam sayıların döngüsel çarpımsal grubuyla çalışır. Bitcoin'un dijital imza algoritması ve yakın zamanda tanıtılan Schnorr imza şemasının (2021) her ikisi de belirli bir eliptik eğri döngüsel grubu için ayrık logaritma problemine dayanmaktadır.


Daha sonra, asimetrik ortamda gizlilik ve kimlik doğrulamaya ilişkin üst düzey bir genel bakışa döneceğiz. Ancak bunu yapmadan önce kısa bir tarihsel not düşmemiz gerekiyor.


Hükümet İletişim Merkezi (GCHQ) için çalışan bir grup İngiliz kriptograf ve matematikçinin birkaç yıl önce yukarıda bahsedilen keşifleri bağımsız olarak yapmış olması artık akla yatkın görünmektedir. Bu grup James Ellis, Clifford Cocks ve Malcolm Williamson'dan oluşuyordu.


Kendi açıklamalarına ve GCHQ'nun açıklamalarına göre, açık anahtar kriptografisi kavramını ilk kez 1969 yılında James Ellis geliştirmiştir. Daha sonra Clifford Cocks'un 1973 yılında RSA kriptografik sistemini ve Malcolm Williamson'ın da 1974 yılında Diffie Helmann anahtar Exchange kavramını keşfettiği söylenmektedir. [4] Bununla birlikte, GCHQ'da yapılan çalışmaların gizli niteliği göz önüne alındığında, keşiflerinin 1997 yılına kadar açıklanmadığı iddia edilmektedir.



**Notlar:**


[1] Whitfield Diffie ve Martin Hellman, "New directions in cryptography," _IEEE Transactions on Information Theory_ IT-22 (1976), pp. 644-654, at p. 644.


[2] Ralph Merkle ayrıca "Secure communications over insecure channels", _Communications of the Association for Computing Machinery_, 21 (1978), 294-99'da bir anahtar Exchange protokolünü tartışmaktadır. Merkle aslında bu makaleyi Diffie ve Hellman'ın makalesinden önce sunmuş olsa da daha sonra yayınlanmıştır. Merkle'nin çözümü Diffie-Hellman'ınkinin aksine üstel olarak güvenli değildir.


[3] Ron Rivest, Adi Shamir ve Leonard Adleman, "A method for obtaining digital signatures and public-key cryptosystems", _Communications of the Association for Computing Machinery_, 21 (1978), s. 120-26.


[4] Bu keşiflerin iyi bir tarihçesi Simon Singh, _The Code Book_, Fourth Estate (Londra, 1999), Bölüm 6'da verilmiştir.





## Asimetrik şifreleme ve kimlik doğrulama

<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>


Bob ve Alice yardımıyla **asimetrik şifrelemeye** genel bir bakış *Şekil 1*'de verilmiştir.


Alice ilk olarak bir açık anahtar ($K_P$) ve bir özel anahtardan ($K_S$) oluşan bir anahtar çifti yaratır; burada $K_P$'deki "P" "açık" ve $K_S$'deki "S" "gizli" anlamına gelir. Daha sonra bu açık anahtarı başkalarına serbestçe dağıtır. Bu dağıtım sürecinin ayrıntılarına biraz sonra döneceğiz. Ancak şimdilik, Bob dahil herkesin Alice'ün $K_P$ açık anahtarını güvenli bir şekilde elde edebileceğini varsayalım.


Daha sonraki bir noktada, Bob, Alice'ya bir $M$ mesajı yazmak ister. Hassas bilgiler içerdiğinden, içeriğin Alice dışında herkes için gizli kalmasını ister. Bu yüzden, Bob ilk olarak $M$ mesajını $K_P$ kullanarak şifreler. Daha sonra elde ettiği $C$ şifreli metnini Alice'ya gönderir ve Alice $C$ şifresini $K_S$ ile çözerek orijinal $M$ mesajını elde eder.


*Şekil 1: Asimetrik şifreleme*


![Figure 1: Asymmetric encryption](assets/Figure6-1.webp "Figure 1: Asymmetric encryption")



Bob ve Alice'in iletişimini dinleyen herhangi bir düşman $C$'yi gözlemleyebilir. Ayrıca $K_P$ ve $E(\cdot)$ şifreleme algoritmasını da bilir. Ancak daha da önemlisi, bu bilgi saldırganın $C$ şifreli metninin şifresini çözmesine izin vermez. Şifre çözme özellikle saldırganın sahip olmadığı $K_S$ gerektirir.


Simetrik şifreleme şemalarının genellikle düz metin mesajlarını geçerli bir şekilde şifreleyebilen bir saldırgana karşı güvenli olması gerekir (seçilmiş şifreli metin saldırısı güvenliği olarak bilinir). Bununla birlikte, bir saldırgan veya başka biri tarafından bu tür geçerli şifreli metinlerin oluşturulmasına izin vermek gibi açık bir amaçla tasarlanmamıştır.


Bu, tüm amacının saldırganlar da dahil olmak üzere herkesin geçerli şifre metinleri üretmesine izin vermek olduğu asimetrik bir şifreleme şemasının tam tersidir. Asimetrik şifreleme şemaları bu nedenle **çoklu erişim şifreleri** olarak etiketlenebilir.


Neler olduğunu daha iyi anlamak için, Bob'in elektronik olarak bir mesaj göndermek yerine, gizlilik içinde fiziksel bir mektup göndermek istediğini düşünün. Gizliliği sağlamanın bir yolu, Alice'ın Bob'e güvenli bir asma kilit göndermesi, ancak kilidi açacak anahtarı saklaması olacaktır. Mektubunu yazdıktan sonra Bob mektubu bir kutuya koyabilir ve Alice'ın asma kilidiyle kapatabilir. Daha sonra kilitli kutuyu mesajla birlikte, kilidi açacak anahtara sahip olan Alice'a gönderebilir.


Bob asma kilidi kilitleyebilse de, ne kendisi ne de kutuyu ele geçiren başka herhangi bir kişi, eğer gerçekten güvenliyse asma kilidi açamaz. Sadece Alice kilidi açabilir ve Bob'ün mektubunun içeriğini görebilir çünkü anahtar ondadır.


Asimetrik şifreleme şeması kabaca bu sürecin dijital bir versiyonudur. Asma kilit açık anahtara benzer ve asma kilit anahtarı da özel anahtara benzer. Ancak asma kilit dijital olduğu için Alice'ün bunu kendisine gizli mesajlar göndermek isteyebilecek herkese dağıtması çok daha kolay ve masrafsızdır.


Asimetrik ortamda kimlik doğrulama için **dijital imzalar** kullanırız. Dolayısıyla bunlar simetrik ortamdaki mesaj kimlik doğrulama kodlarıyla aynı işleve sahiptir. Dijital imzalara genel bir bakış *Şekil 2'de* verilmiştir.


Bob ilk olarak açık anahtar ($K_P$) ve özel anahtardan ($K_S$) oluşan bir anahtar çifti oluşturur ve açık anahtarını dağıtır. Alice'e kimliği doğrulanmış bir mesaj göndermek istediğinde, önce $M$ mesajını ve özel anahtarını alarak bir **dijital imza** $D$ oluşturur. Bob daha sonra Alice'e mesajını dijital imza ile birlikte gönderir.


Alice mesajı, açık anahtarı ve dijital imzayı bir **doğrulama algoritmasına** ekler. Bu algoritma geçerli bir imza için **doğru** veya geçersiz bir imza için **yanlış** üretir.


Dijital imza, adından da anlaşılacağı üzere, mektuplar, sözleşmeler vb. üzerindeki yazılı imzanın dijital eşdeğeridir. Aslında dijital imza genellikle çok daha güvenlidir. Biraz çabayla yazılı bir imzayı tahrif edebilirsiniz; yazılı imzaların genellikle yakından doğrulanmaması bu süreci kolaylaştırır. Ancak güvenli bir dijital imza, tıpkı güvenli bir mesaj kimlik doğrulama kodu gibi, **varoluşsal olarak taklit edilemez**: yani, güvenli bir dijital imza şemasıyla, özel anahtara sahip olmadıkça hiç kimse doğrulama prosedürünü geçen bir mesaj için uygulanabilir bir imza oluşturamaz.


*Şekil 2: Asimetrik kimlik doğrulama*


![Figure 2: Asymmetric authentication](assets/Figure6-2.webp "Figure 2: Asymmetric authentication")



Asimetrik şifrelemede olduğu gibi, dijital imzalar ve mesaj doğrulama kodları arasında ilginç bir zıtlık görüyoruz. İkincisi için, doğrulama algoritması yalnızca güvenli iletişimi bilen taraflardan biri tarafından kullanılabilir. Bunun nedeni özel bir anahtar gerektirmesidir. Ancak asimetrik ortamda, Bob tarafından atılan $S$ dijital imzayı herkes doğrulayabilir.


Tüm bunlar dijital imzaları son derece güçlü bir araç haline getirmektedir. Örneğin, yasal amaçlarla doğrulanabilen sözleşmeler üzerinde imzalar oluşturmanın temelini oluşturur. Eğer Bob yukarıdaki Exchange'de bir Contract'a imza atmışsa, Alice $M$ mesajını, Contract'u ve $S$ imzasını bir mahkemeye gösterebilir. Bu durumda mahkeme Bob'nin açık anahtarını kullanarak imzayı doğrulayabilir. [5]


Bir başka örnek olarak, dijital imzalar güvenli yazılım ve yazılım güncelleme dağıtımının önemli bir yönüdür. Bu tür bir genel doğrulanabilirlik sadece mesaj kimlik doğrulama kodları kullanılarak asla oluşturulamaz.


Dijital imzaların gücüne son bir örnek olarak Bitcoin'ü ele alalım. Özellikle medyada Bitcoin ile ilgili en yaygın yanlış anlamalardan biri, işlemlerin şifrelenmiş olduğudur: şifrelenmezler. Bunun yerine, Bitcoin işlemleri güvenliği sağlamak için dijital imzalarla çalışır.


Bitcoinler, harcanmamış işlem çıktıları (veya **UTXO'lar**) olarak adlandırılan gruplar halinde bulunur. Belirli bir Bitcoin Address'ten her biri 2 bitcoin karşılığında üç ödeme aldığınızı varsayalım. Teknik olarak artık o Address'te 6 bitcoininiz yoktur. Bunun yerine, söz konusu Address ile ilişkili bir kriptografik sorun tarafından kilitlenen 2 bitcoinlik üç grup paraya sahipsiniz. Yaptığınız herhangi bir ödeme için, işlem için ne kadar ihtiyacınız olduğuna bağlı olarak bu partilerden birini, ikisini veya üçünü birden kullanabilirsiniz.


Harcanmamış işlem çıktıları üzerinde Ownership'nin ispatı genellikle bir veya daha fazla dijital imza ile gösterilir. Bitcoin tam olarak çalışır çünkü harcanmamış işlem çıktıları üzerinde geçerli dijital imzalar, bunları yapmak için gereken gizli bilgilere sahip olmadığınız sürece, hesaplama açısından mümkün değildir.


Şu anda Bitcoin işlemleri, işlemde kullanılan harcanmamış işlem çıktılarının kökenleri gibi ağdaki katılımcılar tarafından doğrulanması gereken tüm bilgileri şeffaf bir şekilde içermektedir. Bu bilgilerin bazılarını gizlemek ve yine de doğrulamaya izin vermek mümkün olsa da (Monero gibi bazı alternatif kripto para birimlerinin yaptığı gibi), bu aynı zamanda belirli güvenlik riskleri de yaratır.


Bazen dijital imzalar ve dijital olarak yakalanan yazılı imzalar konusunda kafa karışıklığı ortaya çıkmaktadır. İkinci durumda, yazılı imzanızın bir görüntüsünü yakalar ve bunu Contract gibi bir elektronik belgeye yapıştırırsınız. Ancak bu kriptografik anlamda bir dijital imza değildir. Dijital imza sadece özel bir anahtara sahip olunduğunda üretilebilen uzun bir sayıdır.


Simetrik anahtar ayarında olduğu gibi, asimetrik şifreleme ve kimlik doğrulama şemalarını da birlikte kullanabilirsiniz. Benzer ilkeler geçerlidir. Öncelikle, şifreleme ve dijital imza oluşturma için farklı özel-genel anahtar çiftleri kullanmalısınız. Buna ek olarak, bir mesajı önce şifrelemeli ve ardından kimlik doğrulamasını yapmalısınız.


Daha da önemlisi, birçok uygulamada asimetrik kriptografi tüm iletişim süreci boyunca kullanılmaz. Bunun yerine, tipik olarak yalnızca taraflar arasında gerçekten iletişim kuracakları *Exchange simetrik anahtarlar* için kullanılacaktır.


Örneğin, çevrimiçi ürün satın aldığınızda durum böyledir. Satıcının açık anahtarını bilen satıcı size dijital olarak imzalanmış mesajlar gönderebilir ve siz de bu mesajların gerçekliğini doğrulayabilirsiniz. Bu temelde, güvenli bir şekilde iletişim kurmak için simetrik anahtar alışverişine yönelik birden fazla protokolden birini takip edebilirsiniz.


Yukarıda bahsedilen yaklaşımın sıklığının ana nedeni, asimetrik kriptografinin belirli bir güvenlik seviyesi üretmede simetrik kriptografiden çok daha az verimli olmasıdır. Açık kriptografinin yanında simetrik anahtar kriptografisine hala ihtiyaç duymamızın bir nedeni de budur. Buna ek olarak, simetrik anahtar kriptografisi, bir bilgisayar kullanıcısının kendi verilerini şifrelemesi gibi belirli uygulamalarda çok daha doğaldır.


Peki dijital imzalar ve açık anahtar şifrelemesi Address anahtar dağıtımı ve anahtar yönetimi sorunlarını tam olarak nasıl çözüyor?


Burada tek bir cevap yoktur. Asimetrik kriptografi bir araçtır ve bu aracı kullanmanın tek bir yolu yoktur. Ancak bu örnekte sorunların tipik olarak nasıl ele alınacağını göstermek için Jim's Sporting Goods'dan daha önceki örneğimizi ele alalım.


Jim's Sporting Goods başlamak için muhtemelen açık anahtar dağıtımını destekleyen bir kuruluş olan bir **sertifika yetkilisine** başvuracaktır. Sertifika yetkilisi Jim's Sporting Goods hakkında bazı bilgileri kaydedecek ve ona bir açık anahtar verecektir. Daha sonra Jim's Sporting Goods'a **TLS/SSL sertifikası** olarak bilinen ve Jim's Sporting Goods'un açık anahtarının sertifika yetkilisinin kendi açık anahtarı kullanılarak dijital olarak imzalandığı bir sertifika gönderir. Bu şekilde, sertifika yetkilisi belirli bir açık anahtarın gerçekten Jim's Sporting Goods'a ait olduğunu onaylar.


TLS/SSL sertifikaları ile bu süreci anlamanın anahtarı, Jim's Sporting Goods'un açık anahtarının bilgisayarınızda herhangi bir yerde saklanmamasına rağmen, tanınmış sertifika yetkililerinin açık anahtarlarının gerçekten de tarayıcınızda veya işletim sisteminizde saklanıyor olmasıdır. Bunlar **kök sertifikalar** olarak adlandırılan sertifikalarda saklanır.


Bu nedenle, Jim's Sporting Goods size TLS/SSL sertifikasını sağladığında, tarayıcınızdaki veya işletim sisteminizdeki bir kök sertifika aracılığıyla sertifika yetkilisinin dijital imzasını doğrulayabilirsiniz. İmza geçerliyse, sertifikadaki açık anahtarın gerçekten Jim's Sporting Goods'a ait olduğundan nispeten emin olabilirsiniz. Bu temelde, Jim's Sporting Goods ile güvenli iletişim için bir protokol oluşturmak kolaydır.


Jim's Sporting Goods için anahtar dağıtımı artık çok daha basit hale gelmiştir. Anahtar yönetiminin de büyük ölçüde basitleştiğini görmek Hard değildir. Jim's Sporting Goods'un binlerce anahtar saklamak yerine sadece SSL sertifikasındaki açık anahtar için imza oluşturmasını sağlayan bir özel anahtar saklaması yeterlidir. Bir müşteri Jim's Sporting Goods'un sitesine her geldiğinde, bu açık anahtardan güvenli bir iletişim oturumu kurabilir. Müşterilerin ayrıca (işletim sistemlerinde ve tarayıcılarında tanınmış sertifika yetkililerinin açık anahtarları dışında) herhangi bir bilgi depolamasına gerek yoktur.


**Notlar:**


[5] Bölüm 1'de ele aldığımız diğer bir konu olan inkar edilemezliği sağlamaya çalışan herhangi bir şemanın temelinde dijital imzaların yer alması gerekecektir.




## Hash fonksiyonları

<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>


Hash fonksiyonları kriptografide her yerde bulunur. Bunlar ne simetrik ne de asimetrik şemalardır, ancak kendi başlarına bir kriptografik kategoriye girerler.


Hash fonksiyonlarına Bölüm 4'te Hash tabanlı kimlik doğrulama mesajlarının oluşturulmasıyla zaten rastlamıştık. Biraz farklı bir nedenle de olsa, dijital imzalar bağlamında da önemlidirler: Dijital imzalar genellikle gerçek (şifrelenmiş) mesaj yerine bazı (şifrelenmiş) mesajların Hash değeri üzerinden yapılır. Bu bölümde, Hash fonksiyonlarına daha kapsamlı bir giriş sunacağım.


Bir Hash fonksiyonunu tanımlayarak başlayalım. Bir **Hash fonksiyonu**, keyfi boyutta girdiler alan ve sabit uzunlukta çıktılar veren verimli bir şekilde hesaplanabilir herhangi bir fonksiyondur.


Bir **kriptografik Hash işlevi** sadece kriptografi uygulamaları için yararlı olan bir Hash işlevidir. Bir kriptografik Hash işlevinin çıktısı genellikle **Hash**, **Hash-değeri** veya **mesaj özeti** olarak adlandırılır.


Kriptografi bağlamında, "Hash fonksiyonu" tipik olarak kriptografik bir Hash fonksiyonunu ifade eder. Bundan sonra bu uygulamayı benimseyeceğim.


Popüler bir Hash işlevine örnek olarak **SHA-256** (güvenli Hash algoritması 256) verilebilir. Girdinin boyutu ne olursa olsun (örneğin, 15 bit, 100 bit veya 10.000 bit), bu işlev 256 bitlik bir Hash değeri verecektir. Aşağıda SHA-256 fonksiyonunun birkaç örnek çıktısını görebilirsiniz.


"Merhaba": `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`


"52398": `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`


"Kriptografi eğlencelidir": `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`


Tüm çıktılar onaltılık formatta yazılmış tam 256 bittir (her bir onaltılık rakam dört ikili rakamla temsil edilebilir). Yani Tolkien'in *Yüzüklerin Efendisi* kitabını SHA-256 fonksiyonuna ekleseniz bile, çıktı yine 256 bit olacaktır.


SHA-256 gibi Hash fonksiyonları kriptografide çeşitli amaçlar için kullanılmaktadır. Bir Hash fonksiyonundan hangi özelliklerin isteneceği gerçekten de belirli bir uygulamanın bağlamına bağlıdır. Kriptografide Hash fonksiyonlarından genel olarak istenen iki temel özellik vardır: [6]


1.	Çarpışma direnci

2.	Saklanmak


Bir Hash fonksiyonu $H$, $x$ ve $y$ olmak üzere $x \neq y$, ancak $H(x) = H(y)$ olacak şekilde iki değer bulmak mümkün değilse **çarpışmaya dirençli** olarak adlandırılır.


Çarpışmaya dayanıklı Hash işlevleri, örneğin yazılımın doğrulanmasında önemlidir. Bitcoin core 0.21.0'ın (Bitcoin ağ trafiğini işlemek için bir sunucu uygulaması) Windows sürümünü indirmek istediğinizi varsayalım. Yazılımın meşruiyetini doğrulamak için atmanız gereken ana adımlar aşağıdaki gibidir:


1.	Öncelikle bir veya daha fazla Bitcoin core katılımcısının açık anahtarlarını indirmeniz ve dijital imzaları doğrulayabilen bir yazılıma (örneğin Kleopetra) aktarmanız gerekir. Bu açık anahtarları [burada] bulabilirsiniz (https://github.com/Bitcoin/Bitcoin/blob/master/contrib/builder-keys/keys.txt). Bitcoin core yazılımını birden fazla katılımcının açık anahtarları ile doğrulamanız önerilir.

2.	Ardından, içe aktardığınız açık anahtarları doğrulamanız gerekir. Atmanız gereken en az bir adım, bulduğunuz açık anahtarların diğer çeşitli yerlerde yayınlananlarla aynı olduğunu doğrulamaktır. Örneğin, açık anahtarlarını içe aktardığınız kişilerin kişisel web sayfalarına, Twitter sayfalarına veya Github sayfalarına başvurabilirsiniz. Genellikle açık anahtarların bu karşılaştırması, parmak izi olarak bilinen açık anahtarın kısa bir Hash'i karşılaştırılarak yapılır.

3.	Ardından, Bitcoin core için çalıştırılabilir dosyayı [web sitelerinden] (www.bitcoincore.org) indirmeniz gerekir. Linux, Windows ve MAC işletim sistemleri için paketler mevcut olacaktır.

4.	Ardından, iki sürüm dosyasını bulmanız gerekir. İlki, indirdiğiniz yürütülebilir dosya için resmi SHA-256 Hash ile birlikte yayınlanan diğer tüm paketlerin karmalarını içerir. Başka bir sürüm dosyası, paket karmaları ile birlikte sürüm dosyası üzerinde çeşitli katkıda bulunanların imzalarını içerecektir. Bu sürüm dosyalarının her ikisi de Bitcoin core web sitesinde bulunmalıdır.

5.	 Ardından, Bitcoin core web sitesinden indirdiğiniz yürütülebilir dosyanın SHA-256 Hash değerini kendi bilgisayarınızda hesaplamanız gerekir. Daha sonra, bu sonucu yürütülebilir dosyanın resmi Hash paketi ile karşılaştırın. Sonuçların aynı olması gerekir.

6.	Son olarak, resmi paket karmaları ile sürüm dosyası üzerindeki dijital imzalardan bir veya daha fazlasının gerçekten de içe aktardığınız bir veya daha fazla açık anahtara karşılık geldiğini doğrulamanız gerekir (Bitcoin core sürümleri her zaman herkes tarafından imzalanmaz). Bunu Kleopetra gibi bir uygulama ile yapabilirsiniz.


Bu yazılım doğrulama sürecinin iki ana faydası vardır. Birincisi, Bitcoin core'in web sitesinden indirme yaparken iletimde herhangi bir hata olmamasını sağlar. İkincisi, hiçbir saldırganın Bitcoin core web sitesini hackleyerek veya trafiği keserek değiştirilmiş, kötü amaçlı kod indirmenizi sağlayamayacağını garanti eder.


Yukarıdaki yazılım doğrulama süreci bu sorunlara karşı tam olarak nasıl koruma sağlıyor?


İçe aktardığınız açık anahtarları özenle doğruladıysanız, bu anahtarların gerçekten kendilerine ait olduğundan ve tehlikeye atılmadığından oldukça emin olabilirsiniz. Dijital imzaların varoluşsal olarak taklit edilemez olduğu göz önüne alındığında, yalnızca bu katkıda bulunanların sürüm dosyasındaki resmi paket karmaları üzerinde dijital bir imza oluşturabileceğini bilirsiniz.


İndirdiğiniz sürüm dosyasındaki imzaların kontrol edildiğini varsayalım. Şimdi indirdiğiniz Windows yürütülebilir dosyası için yerel olarak hesapladığınız Hash değerini düzgün imzalanmış sürüm dosyasında bulunan değerle karşılaştırabilirsiniz. Bildiğiniz gibi SHA-256 Hash işlevi çarpışmaya dayanıklıdır, eşleşme, yürütülebilir dosyanızın resmi yürütülebilir dosyayla tamamen aynı olduğu anlamına gelir.


Şimdi Hash fonksiyonlarının ikinci ortak özelliğine dönelim: **gizleme**. Herhangi bir Hash fonksiyonunun $H$, çok geniş bir aralıktan rastgele seçilen herhangi bir $x$ için, sadece $H(x)$ verildiğinde $x$ bulmak mümkün değilse, gizleme özelliğine sahip olduğu söylenir.


Aşağıda, yazdığım bir mesajın SHA-256 çıktısını görebilirsiniz. Yeterli rastgeleliği sağlamak için mesajın sonuna rastgele oluşturulmuş bir karakter dizisi eklenmiştir. SHA-256'nın gizleme özelliğine sahip olduğu göz önüne alındığında, hiç kimse bu mesajı deşifre edemeyecektir.



- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`


Ancak SHA-256 zayıflayana kadar sizi merakta bırakmayacağım. Yazdığım orijinal mesaj aşağıdaki gibiydi:



- "Bu çok rastgele bir mesaj, daha doğrusu rastgele sayılır. Bu başlangıç kısmı değil, ancak çok öngörülemez bir mesaj sağlamak için nispeten rastgele bazı karakterlerle bitireceğim. XLWz4dVG3BxUWm7zQ9qS".


Gizleme özelliğine sahip Hash işlevlerinin kullanıldığı yaygın bir yol parola yönetimidir (çarpışma direnci de bu uygulama için önemlidir). Facebook ya da Google gibi herhangi bir düzgün çevrimiçi hesap tabanlı hizmet, hesabınıza erişimi yönetmek için şifrelerinizi doğrudan saklamayacaktır. Bunun yerine, yalnızca bu şifrenin bir Hash'ini saklarlar. Bir tarayıcıda şifrenizi her girdiğinizde, önce bir Hash hesaplanır. Yalnızca bu Hash servis sağlayıcının sunucusuna gönderilir ve arka uç veritabanında saklanan Hash ile karşılaştırılır. Gizleme özelliği, saldırganların Hash değerinden kurtaramamasını sağlamaya yardımcı olabilir.


Hash'ler aracılığıyla parola yönetimi elbette yalnızca kullanıcılar gerçekten zor parolalar seçiyorsa işe yarar. Gizleme özelliği, x'in çok geniş bir aralıktan rastgele seçildiğini varsayar. "1234", "mypassword" ya da doğum tarihiniz gibi şifreler seçmek gerçek bir güvenlik sağlamayacaktır. Saldırganların parolanızın Hash'unu ele geçirmeleri halinde yararlanabilecekleri uzun yaygın parola listeleri ve bunların karmaları mevcuttur. Bu tür saldırılar **sözlük saldırıları** olarak bilinir. Saldırganlar kişisel bilgilerinizden bazılarını biliyorsa, bazı bilinçli tahminler de deneyebilirler. Bu nedenle, her zaman uzun, güvenli parolalara (tercihen bir parola yöneticisinden alınan uzun, rastgele dizelere) ihtiyacınız vardır.


Bazen bir uygulama hem çarpışma direncine hem de gizlemeye sahip bir Hash işlevine ihtiyaç duyabilir. Ama kesinlikle her zaman değil. Örneğin, tartıştığımız yazılım doğrulama süreci, yalnızca Hash işlevinin çarpışma direnci göstermesini gerektirir, gizleme önemli değildir.


Çarpışma direnci ve gizleme kriptografide Hash fonksiyonlarında aranan temel özellikler olmakla birlikte, bazı uygulamalarda başka tür özellikler de istenebilir.



**Notlar:**


[6] "Gizleme" terminolojisi yaygın bir dil değildir, ancak özellikle Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller ve Steven Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Bölüm 1'den alınmıştır.



# RSA kriptosistemi

<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>




## Çarpanlara ayırma problemi

<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>


Simetrik kriptografi çoğu insan için genellikle oldukça sezgisel olsa da, asimetrik kriptografi için durum genellikle böyle değildir. Her ne kadar önceki bölümlerde sunulan üst düzey açıklamalarla rahat olsanız da, muhtemelen tek yönlü fonksiyonların tam olarak ne olduğunu ve asimetrik şemalar oluşturmak için tam olarak nasıl kullanıldıklarını merak ediyorsunuzdur.


Bu bölümde, asimetrik kriptografiyi çevreleyen gizemin bir kısmını, belirli bir örneği, yani RSA kriptosistemini daha derinlemesine inceleyerek ortadan kaldıracağım. İlk bölümde, RSA probleminin dayandığı çarpanlara ayırma problemini tanıtacağım. Daha sonra, sayılar teorisinden bir dizi önemli sonucu ele alacağım. Son bölümde ise bu bilgileri bir araya getirerek RSA problemini ve bunun asimetrik kriptografik şemalar oluşturmak için nasıl kullanılabileceğini açıklayacağız.


Tartışmamıza bu derinliği katmak kolay bir iş değildir. Oldukça az sayıda sayı teoremi ve önerme sunmayı gerektiriyor. Ancak matematiğin sizi caydırmasına izin vermeyin. Bu tartışma üzerinde çalışmak, asimetrik kriptografinin temelinde yatan şeyi anlamanızı önemli ölçüde geliştirecek ve değerli bir yatırım olacaktır.


Şimdi ilk olarak çarpanlara ayırma problemine dönelim.


___



İki sayıyı, örneğin $a$ ve $b$ sayılarını çarptığınızda, $a$ ve $b$ sayılarına **faktörler**, sonuca ise **ürün** deriz. Bir $N$ sayısını iki ya da daha fazla faktörün çarpımına dönüştürmeye **faktörleştirme** ya da **faktörleme** denir. [1] Bunu gerektiren herhangi bir probleme **faktörleştirme problemi** diyebilirsiniz.


Yaklaşık 2.500 yıl önce, Yunan matematikçi İskenderiyeli Öklid, tam sayıların çarpanlara ayrılmasıyla ilgili önemli bir teorem keşfetti. Bu teorem genellikle **tekil çarpanlara ayırma teoremi** olarak adlandırılır ve aşağıdakileri ifade eder:


**Teorem 1**. 1'den büyük olan her $N$ tamsayısı ya bir asal sayıdır ya da asal çarpanların çarpımı olarak ifade edilebilir.


Bu ifadenin ikinci kısmı, 1'den büyük herhangi bir $N$ asal olmayan tamsayıyı alıp asal sayıların çarpımı olarak yazabileceğiniz anlamına gelir. Aşağıda asal çarpanların çarpımı olarak yazılan asal olmayan tamsayılara birkaç örnek verilmiştir.



- $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
- $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
- 144 $ = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$


Yukarıdaki tam sayıların üçü için de asal çarpanlarını hesaplamak, size sadece $N$ verilse bile nispeten kolaydır. En küçük asal sayı olan 2 ile başlarsınız ve $N$ tamsayısının bu sayıya kaç kez bölünebileceğini görürsünüz. Daha sonra $N$'nin 3, 5, 7 ve benzeri sayılarla bölünebilirliğini test etmeye devam edersiniz. Bu işleme $N$ tamsayınız sadece asal sayıların çarpımı olarak yazılana kadar devam edersiniz.


Örneğin 84 tamsayısını ele alalım. Aşağıda asal çarpanlarını belirleme sürecini görebilirsiniz. Her adımda, kalan en küçük asal faktörü (solda) çıkarıyoruz ve çarpanlara ayrılacak kalan terimi belirliyoruz. Kalan terim de bir asal sayı olana kadar devam ediyoruz. Her adımda, 84'ün mevcut çarpanlara ayrılması en sağda görüntülenir.



- Asal çarpan = 2: kalan terim = 42 ($84 = 2 \cdot 42$)
- Asal çarpan = 2: kalan terim = 21 ($84 = 2 \cdot 2 \cdot 21$)
- Asal çarpan = 3: kalan terim = 7 ($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
- 7 bir asal sayı olduğundan, sonuç $2 \cdot 2 \cdot 3 \cdot 7$ veya $2^2 \cdot 3 \cdot 7$ olur.


Şimdi $N$'nin çok büyük olduğunu varsayalım. N$'yi asal çarpanlarına ayırmak ne kadar zor olurdu?


Bu gerçekten $N$ değerine bağlıdır. Örneğin $N$'nin 50,450,400 olduğunu varsayalım. Bu sayı korkutucu görünse de, hesaplamalar o kadar karmaşık değildir ve elle kolayca yapılabilir. Yukarıda olduğu gibi, sadece 2 ile başlar ve ileriye doğru çalışırsınız. Aşağıda, bu işlemin sonucunu yukarıdakine benzer bir şekilde görebilirsiniz.



- 2: 25.225.200 $ (50.450.400 $ = 2 \cdot 25.225.200 $)
- 2: 12.612.600 $ (50.450.400 $ = 2^2 \cdot 12.612.600$)
- 2: 6.306.300 $ (50.450.400 $ = 2^3 \cdot 6.306.300$)
- 2: 3.153.150 $ (50.450.400 $ = 2^4 \cdot 3.153.150$)
- 2: 1.576.575 $ (50.450.400 $ = 2^5 \cdot 1.576.575$)
- 3: 525.525 (50.450.400 $ = 2^5 \cdot 3 \cdot 525.525$)
- 3: 175.175 (50.450.400 $ = 2^5 \cdot 3^2 \cdot 175.175$)
- 5: 35.035 (50.450.400 $ = 2^5 \cdot 3^2 \cdot 5 \cdot 35.035$)
- 5: 7.007 (50.450.400 $ = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7.007$)
- 7: 1.001 (50.450.400 $ = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1.001$)
- 7: 143 (50.450.400 $ = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
- 11: 13 (50.450.400 $ = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
- 13 bir asal sayı olduğundan, sonuç $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$ olur.


Bu problemi elle çözmek biraz zaman alır. Elbette bir bilgisayar tüm bunları saniyenin küçük bir bölümünde yapabilir. Aslında, bir bilgisayar çoğu zaman çok büyük tamsayıları bile saniyenin çok küçük bir bölümünde çarpanlarına ayırabilir.


Ancak bazı istisnalar da vardır. İlk olarak rastgele iki çok büyük asal sayı seçtiğimizi varsayalım. Bunları $p$ ve $q$ olarak etiketlemek tipiktir ve ben de burada bu geleneği benimseyeceğim.


Somutlaştırmak için, $p$ ve $q$ sayılarının her ikisinin de 1024 bitlik asal sayılar olduğunu ve temsil edilebilmeleri için gerçekten de en az 1024 bit gerektirdiklerini varsayalım (yani ilk bit 1 olmalıdır). Dolayısıyla, örneğin 37 asal sayılardan biri olamaz. 37'yi kesinlikle 1024 bit ile temsil edebilirsiniz. Ama açıkça görülüyor ki, onu temsil etmek için bu kadar bite ihtiyacınız yok. 37'yi 6 bit ya da daha fazla bit içeren herhangi bir dizge ile temsil edebilirsiniz. (6 bitte 37, $100101$ olarak temsil edilebilir).


Yukarıdaki koşullar altında seçildiğinde $p$ ve $q$ sayılarının ne kadar büyük olduğunu takdir etmek önemlidir. Örnek olarak, aşağıda gösterimi için en az 1024 bit gereken rastgele bir asal sayı seçtim.



- 14,752,173,874,503,595,484,930,006,383,670,759,559,764,562,721,397,166,747,289,220,945,457,932,666,751,048,198,854,920,097,085,690,793,755,254,946,188,163,753,506,778,089,706,699,671,722,089,715,624,760,049,594,106,189,662,669,156,149,028,900,805,928,183,585,427,782,974,951,355,515,394,807,209,836,870,484,558,332,897,443,152,653,214,483,870,992,618,171,825,921,582,253,023,974,514,209,142,520,026,807,636,589


Şimdi rastgele $p$ ve $q$ asal sayılarını seçtikten sonra bunları çarparak bir $N$ tamsayısı elde ettiğimizi varsayalım. Dolayısıyla bu son tamsayı, gösterimi için en az 2048 bit gerektiren 2048 bitlik bir sayıdır. Bu sayı $p$ ya da $q$ sayılarından çok çok daha büyüktür.


Bir bilgisayara sadece $N$ verdiğinizi ve ondan $N$'ın 1024 bitlik iki asal çarpanını bulmasını istediğinizi varsayalım. Bilgisayarın $p$ ve $q$ bulma olasılığı son derece düşüktür. Tüm pratik amaçlar için bunun imkansız olduğunu söyleyebilirsiniz. Bir süper bilgisayar ya da hatta süper bilgisayarlardan oluşan bir ağ kullansanız bile bu böyledir.


Başlangıç olarak, bilgisayarın problemi 1024 bitlik sayılar arasında dolaşarak, her durumda asal olup olmadıklarını ve $N$'nin çarpanları olup olmadıklarını test ederek çözmeye çalıştığını varsayalım. Bu durumda test edilecek asal sayılar kümesi yaklaşık olarak 1.265 \cdot 10^{305}$'dır. [2]


Gezegendeki tüm bilgisayarları alıp 1024 bitlik asal sayıları bu şekilde bulup test etmelerini isteseniz bile, $N$'nin asal bir çarpanını başarılı bir şekilde bulmak için milyarda 1 şans, Evrenin yaşından çok daha uzun bir hesaplama süresi gerektirecektir.


Şimdi pratikte bir bilgisayar az önce açıklanan kaba prosedürden daha iyisini yapabilir. Bilgisayarın daha hızlı bir çarpanlara ayırma işlemine ulaşmak için uygulayabileceği çeşitli algoritmalar mevcuttur. Ancak asıl mesele, bu daha verimli algoritmalar kullanıldığında bile bilgisayarın görevinin hesaplama açısından hala yetersiz olmasıdır. [3]


Daha da önemlisi, az önce açıklanan koşullar altında çarpanlara ayırmanın zorluğu, asal çarpanları hesaplamak için hesaplama açısından verimli algoritmalar olmadığı varsayımına dayanmaktadır. Aslında verimli bir algoritmanın var olmadığını kanıtlayamayız. Bununla birlikte, bu varsayım çok makuldür: yüzlerce yıl süren yoğun çabalara rağmen, hesaplama açısından verimli bir algoritma henüz bulamadık.


Dolayısıyla, çarpanlara ayırma probleminin, belirli koşullar altında, makul bir şekilde bir Hard problemi olduğu varsayılabilir. Özellikle, $p$ ve $q$ çok büyük asal sayılar olduğunda, çarpımları $N$'yi hesaplamak zor değildir; ancak yalnızca $N$ verildiğinde çarpanlara ayırma pratik olarak imkansızdır.



**Notlar:**


[1] Çarpanlara ayırma, sayılar dışındaki diğer matematiksel nesne türleriyle çalışmak için de önemli olabilir. Örneğin, $x^2 - 2x + 1$ gibi polinom ifadeleri çarpanlara ayırmak faydalı olabilir. Tartışmamızda sadece sayıların, özellikle de tam sayıların çarpanlara ayrılmasına odaklanacağız.


[2] **Asal sayı teoremine** göre, $N$'dan küçük veya eşit asal sayı yaklaşık olarak $N/\LN(N)$'dır. Bu, 1024 bit uzunluğundaki asal sayıların sayısını yaklaşık olarak şu şekilde hesaplayabileceğiniz anlamına gelir:


$$ \frac{2^{1024}}{\LN(2^{1024})} - \frac{2^{1023}}{\LN(2^{1023})} $$


...bu da yaklaşık olarak 1.265 $ \times 10^{305}$'a eşittir.


[3] Aynı durum ayrık logaritma problemleri için de geçerlidir. Asimetrik yapıların simetrik kriptografik yapılardan çok daha büyük anahtarlarla çalışmasının nedeni budur.




## Sayı teorisi sonuçları

<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>


Ne yazık ki çarpanlara ayırma problemi asimetrik kriptografik şemalar için doğrudan kullanılamaz. Ancak, bu amaçla daha karmaşık ama ilgili bir problemi kullanabiliriz: RSA problemi.


RSA problemini anlamak için sayılar teorisinden bir dizi teorem ve önermeyi anlamamız gerekecektir. Bunlar bu bölümde üç alt bölümde sunulmuştur: (1) N mertebesi, (2) N modülünde ters çevrilebilirlik ve (3) Euler teoremi.


Üç alt bölümdeki malzemenin bir kısmı *Bölüm 3'te* zaten tanıtılmıştır. Ancak burada kolaylık sağlamak için o materyali yeniden ifade edeceğim.



### N'nin sırası


Bir $a$ tamsayısı, aralarındaki en büyük ortak bölen 1 ise, bir $N$ tamsayısı ile **ortak** veya **göreceli asal**dır. 1 geleneksel olarak asal bir sayı olmasa da, her tamsayının ortak asal sayısıdır ($-1$ gibi).


Örneğin, $a = 18$ ve $N = 37$ olduğu durumu düşünün. Bunlar açıkça eş asal sayılardır. Hem 18 hem de 37'yi bölen en büyük tamsayı 1'dir. Buna karşılık, $a = 42$ ve $N = 16$ olduğu durumu düşünün. Bunlar açıkça eş asal değildir. Her iki sayı da 1'den büyük olan 2'ye bölünebilir.


Şimdi $N$ mertebesini aşağıdaki gibi tanımlayabiliriz. Diyelim ki $N$ 1'den büyük bir tamsayı olsun. O zaman **N** mertebesi, $N$ ile tüm eş asalların sayısıdır, öyle ki her eş asal $a$ için aşağıdaki koşul geçerlidir: $1 \leq a < N$.


Örneğin, $N = 12$ ise, 1, 5, 7 ve 11 yukarıdaki gereksinimi karşılayan tek eş asal sayılardır. Dolayısıyla, 12'nin mertebesi 4'e eşittir.


Diyelim ki $N$ bir asal sayı olsun. O zaman $N$'den küçük ancak 1'e eşit veya büyük herhangi bir tamsayı onunla eş asaldır. Bu, aşağıdaki kümedeki tüm Elements'ları içerir: $\{1,2,3,....,N - 1\}$. Dolayısıyla, $N$ asal olduğunda, $N$'nin mertebesi $N - 1$'dir. Bu önerme 1'de belirtilmiştir ve burada $\phi(N)$ $N$ mertebesini göstermektedir.


**Önerme 1**. $N$ asal olduğunda $\phi(N) = N - 1$


Diyelim ki $N$ asal değil. O zaman **Euler'in Phi fonksiyonunu** kullanarak sırasını hesaplayabilirsiniz. Küçük bir tamsayının mertebesini hesaplamak nispeten kolay olsa da, Euler'in Phi fonksiyonu özellikle daha büyük tamsayılar için önemli hale gelir. Euler'in Phi fonksiyonunun önermesi aşağıda belirtilmiştir.


**Teorem 2**. N$ eşit $p_1^{e_1} olsun \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, burada $\{p_i\}$ kümesi $N$'nin tüm farklı asal çarpanlarından oluşur ve her $e_i$, $p_i$ asal çarpanının $N$ için kaç kez oluştuğunu gösterir. O zaman,


$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$


**Teorem 2**, asal olmayan herhangi bir $N$'yi farklı asal çarpanlarına ayırdıktan sonra $N$'nin mertebesini hesaplamanın kolay olduğunu göstermektedir.


Örneğin, $N = 270$ olduğunu varsayalım. Bu açıkça asal bir sayı değildir. N$ asal çarpanlarına ayrıldığında şu ifade ortaya çıkar: $2 \cdot 3^3 \cdot 5$. Euler'in Phi fonksiyonuna göre, $N$'nin sırası aşağıdaki gibidir:


$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$


Şimdi $N$'nin $p$ ve $q$ olmak üzere iki asalın çarpımı olduğunu varsayalım. O zaman yukarıdaki **Teorem 2**, $N$'nin sırasının aşağıdaki gibi olduğunu belirtir:


$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$


Bu, özellikle RSA problemi için önemli bir sonuçtur ve aşağıdaki **Öneri 2**'de belirtilmiştir.


**Önerme 2**. Eğer $N$ iki asalın çarpımı ise, $p$ ve $q$, $N$'nin mertebesi $(p - 1) \cdot (q - 1)$ çarpımıdır.


Örnek olarak, $N = 119$ olduğunu varsayalım. Bu tamsayı 7 ve 17 olmak üzere iki asal sayıya bölünebilir. Dolayısıyla, Euler'in Phi fonksiyonu 119'un sırasının aşağıdaki gibi olduğunu göstermektedir:


$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$


Başka bir deyişle, 119 tamsayısının 1'den 119'a kadar olan aralıkta 96 eş aslı vardır. Aslında bu küme, 1'den 119'a kadar olan ve 7 ya da 17'nin katı olmayan tüm tamsayıları içerir.


Bundan sonra $N$'nin sırasını belirleyen eş asal sayılar kümesini $C_N$ olarak gösterelim. N = 119$ olan örneğimiz için $C_{119}$ kümesi tamamen listelenemeyecek kadar büyüktür. Ancak Elements'den bazıları aşağıdaki gibidir:


$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$


### Modulo N ters çevrilebilirlik


Eğer $a \cdot b \mod N = 1 \mod N$ olacak şekilde en az bir $b$ tamsayısı varsa, bir $a$ tamsayısının **terslenebilir modulo N** olduğunu söyleyebiliriz. Böyle herhangi bir $b$ tamsayısı, $a$'nın $N$ modülüne göre indirgenmiş bir **tersi** (veya **çarpımsal tersi**) olarak adlandırılır.


Örneğin, $a = 5$ ve $N = 11$ olduğunu varsayalım. 5\cdot b \mod 11 = 1 \mod 11$ olacak şekilde 5 ile çarpabileceğiniz birçok tamsayı vardır. Örneğin, 20 ve 31 tamsayılarını düşünün. Bu tamsayıların her ikisinin de modulo 11 indirgemesi için 5'in tersi olduğunu görmek kolaydır.



- $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
- $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$


5'in modulo 11'e indirgenmiş çok sayıda tersi varken, 5'in 11'den küçük olan tek bir pozitif tersinin var olduğunu gösterebilirsiniz. Aslında bu bizim örneğimize özgü değil, genel bir sonuçtur.


**Önerme 3**. Eğer $a$ tamsayısı $N$ modülünde ters çevrilebilir ise, $a$'nın tam bir pozitif tersi $N$'dan küçük olmalıdır. (Yani, $a$'nın bu tek tersi $\{1, \dots, N - 1\}$ kümesinden gelmelidir).


Önerme 3'ten $a$'nın tekil tersini $a^{-1}$ olarak gösterelim. $A = 5$ ve $N = 11$ olduğu durum için, $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$ olduğuna göre, $a^{-1} = 9$ olduğunu görebilirsiniz.


Örneğimizdeki $a^{-1}$ için 9 değerini, $a$'nın diğer herhangi bir tersini modulo 11'e indirgeyerek de elde edebileceğinize dikkat edin. Örneğin, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Dolayısıyla, bir $a > N$ tamsayısı $N$ modülünde ters çevrilebilir olduğunda, $a \mod N$ de $N$ modülünde ters çevrilebilir olmalıdır.


A$'nın tersinin $N$ modülünde bir indirgeme olması zorunlu değildir. Örneğin, $a = 2$ ve $N = 8$ olduğunu varsayalım. Hiçbir $b$ ya da özellikle herhangi bir $a^{-1}$ yoktur ki $2 \cdot b \mod 8 = 1 \mod 8$ olsun. Bunun nedeni $b$'nin herhangi bir değerinin her zaman 2'nin bir katını üretecek olmasıdır, bu nedenle 8 ile hiçbir bölme işlemi 1'e eşit bir kalan veremez.


Belirli bir $N$ için bir $a$ tamsayısının tersi olup olmadığını tam olarak nasıl bilebiliriz? Yukarıdaki örnekte fark etmiş olabileceğiniz gibi, 2 ile 8 arasındaki en büyük ortak bölen 1'den büyüktür, yani 2. Ve bu aslında aşağıdaki genel sonucun bir göstergesidir:


**Önerme 4**. Bir $a$ tamsayısının $N$ modülüne indirgenmiş bir tersi ve özellikle $N$'dan küçük tek bir pozitif tersi, ancak ve ancak $a$ ve $N$ arasındaki en büyük ortak bölen 1 ise (yani, eş asallarsa) vardır.


A = 5$ ve $N = 11$ olduğu durum için, 5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$ olduğuna göre, $a^{-1} = 9$ sonucuna vardık. Bunun tersinin de doğru olduğuna dikkat etmek önemlidir. Yani, $a = 9$ ve $N = 11$ olduğunda, $a^{-1} = 5$ olur.



### Euler teoremi


RSA problemine geçmeden önce, **Euler teoremi** olarak adlandırılan çok önemli bir teoremi daha anlamamız gerekir. Bu teorem aşağıdakileri ifade eder:


**Teorem 3**. İki $a$ ve $N$ tamsayısının eş asal olduğunu varsayalım. O zaman, $a^{\phi(N)} \mod N = 1 \mod N$.


Bu dikkate değer bir sonuçtur, ancak ilk başta biraz kafa karıştırıcıdır. Bunu anlamak için bir örneğe dönelim.


A = 5$ ve $N = 7$ olduğunu varsayalım. Bunlar gerçekten de Euler teoreminin gerektirdiği gibi eş asal sayılardır. 7'nin bir asal sayı olduğu göz önüne alındığında, 7'nin mertebesinin 6'ya eşit olduğunu biliyoruz (bkz. **Önermeler 1**).


Euler teoremine göre 5^6 \mod 7$, 1 \mod 7$'ye eşit olmalıdır. Aşağıda bunun gerçekten doğru olduğunu gösteren hesaplamalar yer almaktadır.



- 5^6 \mod 7 = 15,625 \mod 7 = 1 \mod N$


7 tamsayısı 15,624'e toplam 2,233 kez bölünür. Dolayısıyla, 16.625'in 7'ye bölünmesinden kalan 1'dir.


Daha sonra, Euler'in Phi fonksiyonunu kullanarak, **Teorem 2**, aşağıdaki **Önermeyi 5** türetebilirsiniz.


**Önerme 5**. herhangi bir pozitif $a$ ve $b$ tamsayısı için $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$.


Bunun neden böyle olduğunu göstermeyeceğiz. Ancak, **Önermeler 2**'de belirtildiği gibi, $p$ ve $q$ asal olduğunda $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ gerçeğiyle bu önermenin kanıtını zaten gördüğünüze dikkat edin.


Euler teoreminin **Önermesi 5** ile birlikte önemli çıkarımları vardır. Örneğin, $a$ ve $N$'nin eş asal olduğu aşağıdaki ifadelerde ne olduğuna bakın.



- $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
- $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$
- $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$


Dolayısıyla, Euler teoremi ve **Önermeler 5** kombinasyonu, bir dizi ifadeyi basitçe hesaplamamızı sağlar. Genel olarak, içgörüyü **Önermeler 6**'daki gibi özetleyebiliriz.


**Önerme 6**. $a^x \mod N = a^{x \mod \phi(N)}$


Şimdi zorlu bir son adımda her şeyi bir araya getirmemiz gerekiyor.


Tıpkı $N$'nin $C_N$ kümesinin Elements'ini içeren bir $\phi(N)$ mertebesine sahip olması gibi, $\phi(N)$ tamsayısının da bir mertebeye ve bir eş asal sayılar kümesine sahip olması gerektiğini biliyoruz. Şimdi $\phi(N) = R$ olsun. O zaman $\phi(R)$ için de bir değer ve $C_R$ eş asallar kümesi olduğunu biliyoruz.


Şimdi $C_R$ kümesinden bir $e$ tamsayısı seçtiğimizi varsayalım. Önerme 3'ten biliyoruz ki bu $e$ tamsayısının $R$'den küçük sadece bir tek pozitif tersi vardır. Yani, $e$'nin $C_R$ kümesinden tek bir tersi vardır. Bu tersi $d$ olarak adlandıralım. Bir tersin tanımı göz önüne alındığında, bu $e \cdot d = 1 \mod R$ anlamına gelir.


Bu sonucu orijinal $N$ tamsayımız hakkında bir açıklama yapmak için kullanabiliriz. Bu, **Önermeler 7**'de özetlenmiştir.


**Önerme 7**. Varsayalım ki $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$ olsun. O zaman $C_N$ kümesinin herhangi bir $a$ elemanı için $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$ olmalıdır.


Artık RSA problemini açık bir şekilde ifade etmek için gereken tüm sayı teorisi sonuçlarına sahibiz.



## RSA kriptosistemi

<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>


Şimdi RSA problemini ifade etmeye hazırız. Diyelim ki $p$, $q$, $N$, $\phi(N)$, $e$, $d$ ve $y$'den oluşan bir değişkenler kümesi oluşturdunuz. Bu kümeye $\Pi$ adını verin. Aşağıdaki gibi oluşturulur:


1. generate eşit büyüklükte iki rastgele asal $p$ ve $q$ ve bunların çarpımı $N$'yi hesaplayın.

2. N$'nin mertebesini, $\phi(N)$, aşağıdaki çarpımla hesaplayın: $(p - 1) \cdot (q - 1)$.

3. Öyle bir $e > 2$ seçin ki, $\phi(N)$'den küçük ve ona eş olsun.

4. E \cdot d \mod \phi(N) = 1$ olarak ayarlayarak $d$ değerini hesaplayın.

5. Daha küçük ve $N$ ile eş olan rastgele bir $y$ değeri seçin.


RSA problemi, sadece $\Pi$ ile ilgili bir alt bilgi kümesi, yani $N$, $e$ ve $y$ değişkenleri verilirken, $x^e = y$ olacak şekilde bir $x$ bulmaktan oluşur. P$ ve $q$ çok büyük olduğunda, tipik olarak 1024 bit boyutunda olmaları tavsiye edilir, RSA probleminin Hard olduğu düşünülür. Yukarıdaki tartışma göz önüne alındığında bunun neden böyle olduğunu şimdi görebilirsiniz.


X^e \mod N = y \mod N$ olduğunda $x$ değerini hesaplamanın kolay bir yolu $y^d \mod N$ değerini hesaplamaktır. Aşağıdaki hesaplamalarla $y^d \mod N = x \mod N$ olduğunu biliyoruz:


$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$


Sorun şu ki, problemde verilmediği için $d$ değerini bilmiyoruz. Dolayısıyla, $x \mod N$ üretmek için $y^d \mod N$ değerini doğrudan hesaplayamayız.


Bununla birlikte, $d$'yi $N$ mertebesinden, $\phi(N)$, dolaylı olarak hesaplayabiliriz, çünkü $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$ olduğunu biliyoruz. Ancak varsayım olarak problem $\phi(N)$ için de bir değer vermemektedir.


Son olarak, sıra $p$ ve $q$ asal çarpanlarıyla dolaylı olarak hesaplanabilir, böylece sonunda $d$ değerini hesaplayabiliriz. Ancak varsayım olarak, $p$ ve $q$ değerleri de bize sağlanmadı.


Açıkça söylemek gerekirse, bir RSA problemi içindeki çarpanlara ayırma problemi Hard olsa bile, RSA probleminin de Hard olduğunu kanıtlayamayız. RSA problemini çözmenin çarpanlara ayırma dışında başka yolları da olabilir. Bununla birlikte, RSA problemi içindeki çarpanlara ayırma problemi Hard ise, RSA probleminin kendisinin de Hard olduğu genel olarak kabul edilir ve varsayılır.


Eğer RSA problemi gerçekten Hard ise, o zaman bir tuzak kapısı olan tek yönlü bir fonksiyon üretir. Buradaki fonksiyon $f(g) = g^e \mod N$ şeklindedir. Herhangi biri $f(g)$ bilgisi ile belirli bir $g = x$ için $y$ değerini kolayca hesaplayabilir. Ancak, sadece $y$ değerini ve $f(g)$ fonksiyonunu bilerek belirli bir $x$ değerini hesaplamak pratikte imkansızdır. Bunun istisnası, size bir parça $d$ bilgisinin, yani tuzak kapısının verilmesidir. Bu durumda, $x$ değerini vermek için $y^d$ değerini hesaplayabilirsiniz.


RSA problemini açıklamak için belirli bir örnek üzerinden gidelim. Yukarıdaki koşullar altında Hard olarak kabul edilebilecek bir RSA problemi seçemiyorum, çünkü sayılar çok kabarık olacaktır. Bunun yerine, bu örnek sadece RSA probleminin genel olarak nasıl çalıştığını göstermek içindir.


Başlangıç olarak, rastgele 13 ve 31 olmak üzere iki asal sayı seçtiğinizi varsayalım. Yani $p = 13$ ve $q = 31$. Bu iki asal sayının $N$ çarpımı 403'e eşittir. 403'ün mertebesini kolayca hesaplayabiliriz. Bu $(13 - 1) \cdot (31 - 1) = 360$ değerine eşittir.


Ardından, RSA probleminin 3. adımında belirtildiği gibi, 360 için 2'den büyük ve 360'tan küçük bir eş asal sayı seçmemiz gerekir. Bu değeri rastgele seçmek zorunda değiliz. 103'ü seçtiğimizi varsayalım. Bu, 103 ile en büyük ortak böleni 1 olduğu için 360'ın bir eş aslıdır.


Adım 4 şimdi $103 \cdot d \mod 360 = 1$ olacak şekilde bir $d$ değeri hesaplamamızı gerektirmektedir. Bu, $N$ değeri büyük olduğunda elle yapılması kolay bir iş değildir. Bunun için **genişletilmiş Öklid algoritması** adı verilen bir prosedür kullanmamız gerekir.


Burada prosedürü göstermesem de, $e = 103$ olduğunda 7 değerini verir. Aşağıdaki hesaplamaları yaparak 103 ve 7 değer çiftinin gerçekten de $e \cdot d \mod \phi(n) = 1$ genel koşulunu karşıladığını doğrulayabilirsiniz.



- 103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$


Daha da önemlisi, *Önermesi 4* göz önüne alındığında, $d$ için 1 ile 360 arasında başka hiçbir tamsayının 103 \cdot d = 1 \mod 360$ sonucunu üretmeyeceğini biliyoruz. Ek olarak, önerme $e$ için farklı bir değer seçmenin $d$ için farklı bir benzersiz değer vereceğini ima eder.


RSA probleminin 5. adımında, 403'ün küçük bir eş katı olan $y$ pozitif tamsayısını seçmemiz gerekir. Diyelim ki $y = 2^{103}$ olarak belirledik. 2'nin 103 ile üssü aşağıdaki sonucu verir.



- $2^{103} \mod 403 = 10,141,204,801,825,835,211,973,625,643,008 \mod 403 = 349 \mod 403$


Bu örnekteki RSA problemi aşağıdaki gibidir: Size $N = 403$, $e = 103$ ve $y = 349 \mod 403$ veriliyor. Şimdi $x^{103} = 349 \mod 403$ olacak şekilde $x$ değerini hesaplamanız gerekiyor. Yani, 103 ile üs almadan önceki orijinal değerin 2 olduğunu bulmalısınız.


Eğer $d = 7$ olduğunu bilseydik $x$'i hesaplamak (en azından bir bilgisayar için) kolay olurdu. Bu durumda, $x$ değerini aşağıdaki gibi belirleyebilirsiniz.



- $x = y^7 \mod 403 = 349^7 \mod 403 = 630,634,881,591,804,949 \mod 403 = 2 \mod 403$


Sorun, size $d = 7$ bilgisinin verilmemiş olmasıdır. Elbette $d$'yi 103 \cdot d = 1 \mod 360$ gerçeğinden hesaplayabilirsiniz. Buradaki sorun, $N = 360$ olduğu bilgisinin de size verilmemiş olmasıdır. Son olarak, 403'ün sırasını şu çarpımı hesaplayarak da hesaplayabilirsiniz: $(p - 1) \cdot (q - 1)$. Ancak size $p = 13$ ve $q = 31$ olduğu da söylenmez.


Elbette, bir bilgisayar bu örnek için RSA problemini nispeten kolay bir şekilde çözebilir, çünkü ilgili asal sayılar büyük değildir. Ancak asal sayılar çok büyüdüğünde, neredeyse imkansız bir görevle karşı karşıya kalır.


Şimdi RSA problemini, bunun Hard olduğu bir dizi koşulu ve altında yatan matematiği sunduk. Bunların asimetrik kriptografiye nasıl bir faydası olabilir? Özellikle, belirli koşullar altında RSA probleminin zorluğunu nasıl bir şifreleme şemasına ya da dijital imza şemasına dönüştürebiliriz?


Yaklaşımlardan biri RSA problemini ele almak ve basit bir şekilde şemalar oluşturmaktır. Örneğin, RSA probleminde açıklandığı gibi bir $\Pi$ değişken kümesi oluşturduğunuzu ve $p$ ve $q$ değerlerinin yeterince büyük olduğundan emin olduğunuzu varsayalım. Açık anahtarınızı $(N, e)$ olarak belirlediniz ve bu bilgiyi tüm dünya ile paylaştınız. Yukarıda açıklandığı gibi, $p$, $q$, $\phi(n)$ ve $d$ değerlerini gizli tutarsınız. Aslında, $d$ sizin özel anahtarınızdır.


Size $C_N$'nin bir elemanı olan bir $m$ mesajı göndermek isteyen herhangi biri bu mesajı aşağıdaki gibi şifreleyebilir: (Buradaki $c$ şifreli metni RSA problemindeki $y$ değerine eşdeğerdir.) Bu mesajın şifresini $c^d \mod N$ hesaplayarak kolayca çözebilirsiniz.


Aynı şekilde bir dijital imza şeması oluşturmayı deneyebilirsiniz. Birisine $S$ dijital imzalı bir $m$ mesajı göndermek istediğinizi varsayalım. Sadece $S = m^d \mod N$ olarak ayarlayabilir ve $(m,S)$ çiftini alıcıya gönderebilirsiniz. Herkes sadece $S^e \mod N = m \mod N$ olup olmadığını kontrol ederek dijital imzayı doğrulayabilir. Ancak herhangi bir saldırgan $d$'ye sahip olmadığı için bir mesaj için geçerli bir $S$ oluşturmakta gerçekten zorlanacaktır.


Ne yazık ki, başlı başına bir Hard problemi olan RSA problemini kriptografik bir şemaya dönüştürmek bu kadar basit değildir. Basit şifreleme şeması için, mesajlarınız olarak yalnızca $N$'nin eş asallarını seçebilirsiniz. Bu bize çok fazla olası mesaj bırakmaz, kesinlikle standart iletişim için yeterli değildir. Ayrıca, bu mesajların rastgele seçilmesi gerekir. Bu biraz kullanışsız görünüyor. Son olarak, iki kez seçilen herhangi bir mesaj tam olarak aynı şifreli metni verecektir. Bu, herhangi bir şifreleme şemasında son derece istenmeyen bir durumdur ve şifrelemede hiçbir titiz modern standart güvenlik kavramını karşılamaz.


Basit dijital imza şemamız için sorunlar daha da kötüleşmektedir. Şu anki haliyle, herhangi bir saldırgan önce imza olarak $N$'nin bir eş aslını seçerek ve ardından ilgili orijinal mesajı hesaplayarak dijital imzaları kolayca taklit edebilir. Bu da varoluşsal taklit edilemezlik şartını açıkça ihlal eder.


Bununla birlikte, biraz zekice karmaşıklık ekleyerek, RSA problemi güvenli bir açık anahtar şifreleme şemasının yanı sıra güvenli bir dijital imza şeması oluşturmak için kullanılabilir. Burada bu tür yapıların ayrıntılarına girmeyeceğiz. [4] Ancak daha da önemlisi, bu ek karmaşıklık bu şemaların dayandığı temel RSA problemini değiştirmez.



**Notlar:**


[4] Bkz. örneğin, Jonathan Katz ve Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), RSA şifrelemesi için s. 410-32 ve RSA dijital imzaları için s. 444-41.




# Son Bölüm

<partId>e538fb79-bf28-40cd-a5c3-badf864d8567</partId>


## Yorumlar & Derecelendirmeler

<chapterId>366d6fd0-ceb2-4299-bf37-8c6dfcb681d5</chapterId>

<isCourseReview>true</isCourseReview>

## Final Sınavı

<chapterId>44882d2b-63cd-4fde-8485-f76f14d8b2fe</chapterId>

<isCourseExam>true</isCourseExam>

## Sonuç

<chapterId>f1905f78-8cf7-5031-949a-dfa8b76079b4</chapterId>

<isCourseConclusion>true</isCourseConclusion>