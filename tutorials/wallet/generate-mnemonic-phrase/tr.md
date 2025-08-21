---
name: Mnemonic İfade - Zar Atma
description: Zarlarla kendi kurtarma cümlenizi nasıl generate yapabilirsiniz?
---

![cover](assets/cover.webp)


Bu eğitimde, zar atarak Bitcoin Wallet için bir kurtarma cümlesini manuel olarak nasıl oluşturacağınızı öğreneceksiniz.


**UYARI:** Bir Mnemonic ifadesinin güvenli bir şekilde oluşturulması, oluşturulması sırasında hiçbir dijital iz bırakılmamasını gerektirir ki bu neredeyse imkansızdır. Aksi takdirde, Wallet çok geniş bir saldırı yüzeyi oluşturacak ve bitcoinlerinizin çalınma riskini önemli ölçüde artıracaktır. **Bu nedenle, kendi oluşturduğunuz bir kurtarma cümlesine bağlı olan bir Wallet'ya para aktarmamanız şiddetle tavsiye edilir.** Bu öğreticiyi harfiyen takip etseniz bile, kurtarma cümlesinin ele geçirilme riski vardır. **Bu nedenle, bu eğitim gerçek bir Wallet oluşturmak için uygulanmamalıdır.** Bu görev için bir Hardware Wallet kullanmak çok daha az risklidir, çünkü ifadeyi çevrimdışı olarak üretir ve gerçek kriptograflar kalitatif entropi kaynaklarının kullanımını düşünmüşlerdir.


Bu eğitim, gerçek bitcoinlerle kullanma niyeti olmaksızın, yalnızca hayali bir Wallet oluşturmak için deneysel amaçlarla takip edilebilir. Ancak, bu deneyim iki fayda sağlamaktadır:



- İlk olarak, Bitcoin Wallet'unuzun temelindeki mekanizmaları daha iyi anlamanızı sağlar;
- İkinci olarak, bunu nasıl yapacağınızı bilmenizi sağlar. Bir gün işe yarayacağını söylemiyorum, ama yarayabilir!


## Mnemonic ifadesi nedir?


Bazen "Mnemonic", "seed cümlesi" veya "gizli cümle" olarak da adlandırılan bir kurtarma cümlesi, genellikle 12 veya 24 kelimeden oluşan ve bir entropi kaynağından sözde rastgele bir şekilde üretilen bir dizidir. Sözde rastgele dizi her zaman bir sağlama toplamı ile tamamlanır.


Mnemonic ifadesi, isteğe bağlı bir passphrase ile birlikte, bir HD (Hiyerarşik Deterministik) Wallet ile ilişkili tüm anahtarları deterministik olarak türetmek için kullanılır. Bu, bu ifadeden, Bitcoin Wallet'nin tüm özel ve açık anahtarlarını deterministik olarak generate ve yeniden oluşturmanın ve sonuç olarak onunla ilişkili fonlara erişmenin mümkün olduğu anlamına gelir.

![mnemonic](assets/notext/1.webp)

Bu cümlenin amacı, bitcoinlerin yedeklenmesi ve kurtarılması için kullanımı kolay bir araç sağlamaktır. Mnemonic cümlesini güvenli ve emniyetli bir yerde saklamak zorunludur çünkü bu cümleye sahip olan herkes ilgili Wallet'nin fonlarına erişebilir. Geleneksel bir Wallet bağlamında ve isteğe bağlı bir passphrase olmadan kullanılırsa, genellikle bir SPOF (Tek Arıza Noktası) oluşturur.

Genellikle bu ifade, Wallet'ünüzü oluştururken, kullanılan yazılım veya Hardware Wallet tarafından size doğrudan verilir. Bununla birlikte, bu ifadeyi kendiniz generate yapmanız ve ardından Wallet tuşlarını türetmek için seçilen desteğe girmeniz de mümkündür. Bu eğitimde bunu yapmayı öğreneceğiz.


## Gerekli malzemelerin hazırlanması


Kurtarma cümlenizi elle oluşturmak için ihtiyacınız olacak:



- Bir sayfa kağıt;
- Düzenlemeyi kolaylaştırmak için ideal olarak farklı renklerde bir kalem veya kurşun kalem;
- Dengesiz bir zarla ilgili önyargı risklerini en aza indirmek için birkaç zar;
- [2048 BIP39 kelimelik liste] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf) çıktısı alındı.


Daha sonra, sağlama toplamının hesaplanması için terminali olan bir bilgisayarın kullanılması gerekli hale gelecektir. İşte tam da bu nedenle Mnemonic cümlesinin elle oluşturulmasını tavsiye etmiyorum. Bana göre, bir bilgisayarın müdahalesi, bu eğitimde belirtilen önlemler altında bile, bir Wallet'nın güvenlik açığını önemli ölçüde artırır.


"Hayali bir Wallet" ile ilgili deneysel bir yaklaşım için, normal bilgisayarınızı ve terminalini kullanmak mümkündür. Ancak, ifadenizi tehlikeye atma risklerini sınırlamayı amaçlayan daha titiz bir yaklaşım için ideal olan, internet bağlantısı kesilmiş (tercihen wifi bileşeni veya RJ45 kablolu bağlantısı olmayan), minimum çevre birimleriyle donatılmış (Bluetooth'tan kaçınmak için hepsi kabloyla bağlanmalıdır) ve hepsinden önemlisi [Tails] (https://tails.boum.org/index.fr.html) gibi amnezik bir Linux dağıtımıyla çalışan, çıkarılabilir bir ortamdan başlatılan bir bilgisayar kullanmaktır.


![mnemonic](assets/notext/2.webp)


Gerçek bir bağlamda, meraklı gözlerden uzak, insan trafiğinin olmadığı ve kameraların (web kameraları, telefonlar...) bulunmadığı bir yer seçerek çalışma alanınızın gizliliğini sağlamak çok önemli olacaktır.

Potansiyel olarak dengesiz bir zarın entropi üzerindeki etkisini azaltmak için yüksek sayıda zar kullanılması tavsiye edilir. Kullanmadan önce zarların kontrol edilmesi önerilir: bu, zarların tuza doymuş su dolu bir kapta test edilmesi ve zarların yüzmesine izin verilmesiyle gerçekleştirilebilir. Ardından her bir zarı tuzlu suda yaklaşık yirmi kez yuvarlayın ve sonuçları gözlemleyin. Eğer bir ya da iki yüz diğerlerine kıyasla orantısız görünüyorsa, testi daha fazla zar atarak genişletin. Düzgün dağılmış sonuçlar kalıbın güvenilir olduğunu gösterir. Ancak, bir veya iki yüz düzenli olarak baskın çıkıyorsa, bu zarlar bir kenara bırakılmalıdır, çünkü Mnemonic ifadenizin entropisini ve dolayısıyla Wallet'unuzun güvenliğini tehlikeye atabilirler.

Gerçek koşullarda, bu kontrolleri yaptıktan sonra, gerekli entropiyi generate'a hazır hale getirmiş olursunuz. Bu eğitimin bir parçası olarak oluşturulan deneysel bir kurgusal Wallet için doğal olarak bu hazırlıkları atlayabilirsiniz.


## Kurtarma İfadesi Hakkında Birkaç Hatırlatma


Başlangıç olarak, BIP39'a göre bir Mnemonic ifadesi oluşturmanın temellerini gözden geçireceğiz. Daha önce açıklandığı gibi, ifade, bütünlüğünü sağlamak için bir sağlama toplamının eklendiği belirli bir boyuttaki sözde rasgele bilgiden türetilir.


Genellikle "entropi" olarak adlandırılan bu başlangıç bilgisinin boyutu, kurtarma cümlesinde elde etmek istediğiniz kelime sayısına göre belirlenir. En yaygın formatlar, sırasıyla 128 bit ve 256 bit entropiden türetilen 12 ve 24 kelimelik ifadelerdir. İşte BIP39'a göre farklı entropi boyutlarını gösteren bir tablo:


| Phrase (words) | Entropy (bits) | Checksum (bits) | Entropy + Checksum (bits) |
| -------------- | -------------- | --------------- | ------------------------- |
| 12             | 128            | 4               | 132                       |
| 15             | 160            | 5               | 165                       |
| 18             | 192            | 6               | 198                       |
| 21             | 224            | 7               | 231                       |
| 24             | 256            | 8               | 264                       |

Entropi 128 ile 256 bit arasında rastgele bir sayıdır. Bu eğitimde, entropinin 128 bit olduğu 12 kelimelik bir cümle örneğini ele alacağız, yani 128 `0` veya `1`den oluşan rastgele bir diziyi generate yapacağız. Bu, 2 tabanında (ikili) 128 basamaktan oluşan bir sayıyı temsil eder.

Bu entropiye dayalı olarak bir sağlama toplamı oluşturulur. Sağlama toplamı, bir dizi veriden hesaplanan ve iletim veya depolama sırasında bu verilerin bütünlüğünü ve geçerliliğini doğrulamak için kullanılan bir değerdir. Sağlama toplamı algoritmaları, verilerdeki kazara oluşan hataları veya değişiklikleri tespit etmek için tasarlanmıştır.

Mnemonic ifademiz söz konusu olduğunda, sağlama toplamının işlevi, ifadeyi bir Wallet yazılımına girerken herhangi bir giriş hatasını tespit etmektir. Geçersiz bir sağlama toplamı, ifadede bir hata olduğuna işaret eder. Tersine, geçerli bir sağlama toplamı ifadenin büyük olasılıkla doğru olduğunu gösterir.


Bu sağlama toplamını elde etmek için entropi SHA256 Hash fonksiyonundan geçirilir. Bu işlem çıktı olarak 256 bitlik bir dizi üretir, bu dizinin sadece ilk `N` biti saklanır, `N` kurtarma ifadesinin istenen uzunluğuna bağlıdır (yukarıdaki tabloya bakın). Böylece, 12 kelimelik bir ifade için, Hash'nın ilk 4 biti saklanacaktır.

![mnemonic](assets/en/3.webp)

Sağlama toplamını oluşturan bu ilk 4 bit daha sonra orijinal entropiye eklenecektir. Bu aşamada, kurtarma cümlesi pratik olarak oluşturulmuştur, ancak hala ikili formdadır. Bu ikili diziyi BIP39 standardına uygun olarak kelimelere dönüştürmek için önce diziyi 11 bitlik segmentlere böleceğiz.

![mnemonic](assets/notext/4.webp)

Bu paketlerin her biri, daha sonra ondalık sayıya (10 tabanı) dönüştürülecek olan ikili bir sayıyı temsil eder. Her sayıya `1` ekleyeceğiz, çünkü hesaplamada sayma `0`dan başlar, ancak BIP39 listesi `1`den başlayarak numaralandırılır.


![mnemonic](assets/notext/5.webp)


Son olarak, ondalık sayı bize ilgili kelimenin [2048 BIP39 kelime listesi] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf) içindeki konumunu gösterir. Geriye kalan tek şey, Wallet'imiz için kurtarma ifadesini oluşturmak üzere bu kelimeleri seçmektir.


![mnemonic](assets/notext/6.webp)


Şimdi uygulamaya geçelim! 12 kelimelik bir kurtarma cümlesini generate yapacağız. Ancak bu işlem, bu bölümün başında yer alan eşdeğerlik tablosunda belirtildiği gibi 256 bit entropi ve 8 bitlik bir sağlama toplamı gerektirmesi dışında 24 kelimelik bir ifade durumunda da aynı kalır.


## Adım 1: Entropinin Oluşturulması


Kağıdınızı, kaleminizi ve zarınızı hazırlayın. Başlamak için, 128 biti rastgele generate yapmamız gerekecek, yani arka arkaya 128 `0` ve `1`den oluşan bir dizi. Bunu yapmak için zar kullanacağız.

![mnemonic](assets/notext/7.webp)


Zarların 6 yüzü vardır ve hepsinin atılma olasılığı aynıdır. Ancak bizim amacımız iki olası sonuç anlamına gelen ikili bir sonuç üretmektir. Bu nedenle, çift sayıya denk gelen her zar için `0` değerini ve her tek sayı için `1` değerini atayacağız. Sonuç olarak, 128 bitlik entropimizi oluşturmak için 128 zar atacağız. Eğer zar `2`, `4` veya `6` gösterirse, `0` değerini yazacağız; `1`, `3` veya `5` için ise `1` olacak. Her sonuç soldan sağa ve yukarıdan aşağıya doğru sırayla not edilecektir.


Aşağıdaki adımları kolaylaştırmak için, bitleri aşağıdaki resimde gösterildiği gibi dörtlü ve üçlü paketler halinde gruplayacağız. Her satırda 11 bit olmalıdır: 4 bitlik 2 paket ve 3 bitlik bir paket.


![mnemonic](assets/notext/8.webp)


Örneğimde de görebileceğiniz gibi, on ikinci kelime şu anda sadece 7 bitten oluşmaktadır. Bunlar, 11 biti oluşturmak için bir sonraki adımda sağlama toplamının 4 biti ile tamamlanacaktır.


![mnemonic](assets/notext/9.webp)


## Adım 2: Sağlama toplamının hesaplanması


Bu adım, bir bilgisayar kullanımı gerektirdiğinden, Mnemonic ifadesinin manuel olarak oluşturulmasında en kritik adımdır. Daha önce de belirtildiği gibi, sağlama toplamı entropiden üretilen SHA256 Hash'nin başlangıcına karşılık gelir. Teorik olarak 128 veya 256 bitlik bir girdi için bir SHA256'yı elle hesaplamak mümkün olsa da, bu görev bütün bir hafta sürebilir. Dahası, manuel hesaplamalardaki herhangi bir hata ancak işlemin sonunda tespit edilebilir ve sizi en baştan başlamaya zorlar. Bu nedenle, bu adımı sadece bir kağıt ve bir kalemle yapmak düşünülemez. Bir bilgisayar neredeyse zorunludur. Yine de elle nasıl SHA256 yapılacağını öğrenmek istiyorsanız, [CRYPTO301 kursunda] (https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f) nasıl yapılacağını açıklıyoruz.


Bu nedenle, gerçek bir Wallet için manuel bir ifade oluşturulmamasını şiddetle tavsiye ediyorum. Kanımca, bu aşamada bir bilgisayar kullanmak, gerekli tüm önlemler alınsa bile, Wallet'ün saldırı yüzeyini makul olmayan bir şekilde artırır.

Sağlama toplamını mümkün olduğunca az iz bırakarak hesaplamak için, **Tails** adlı çıkarılabilir bir sürücüden amnesik bir Linux dağıtımı kullanacağız. Bu işletim sistemi bir USB bellekten önyükleme yapar ve Hard sürücüsüyle etkileşime girmeden tamamen bilgisayarın RAM'inde çalışır. Böylece, teorik olarak, kapatıldıktan sonra bilgisayarda hiçbir iz bırakmaz. Lütfen Tails'in yalnızca x86_64 tipi işlemcilerle uyumlu olduğunu ve ARM tipi işlemcilerle uyumlu olmadığını unutmayın.

Başlamak için, normal bilgisayarınızdan [Tails görüntüsünü resmi web sitesinden indirin] (https://tails.net/install/index.fr.html). Geliştiricinin imzasını veya site tarafından sunulan doğrulama aracını kullanarak indirme işleminizin gerçekliğinden emin olun.

![mnemonic](assets/notext/10.webp)

Öncelikle USB belleğinizi biçimlendirin, ardından [Balena Etcher] (https://etcher.balena.io/) gibi bir araç kullanarak Tails'i yükleyin.

![mnemonic](assets/notext/11.webp)

Yanıp sönme işleminin başarılı olduğunu onayladıktan sonra bilgisayarınızı kapatın. Ardından Supply'in güç bağlantısını kesmeye ve Hard sürücüsünü bilgisayarınızın anakartından çıkarmaya devam edin. Bir WiFi kartının mevcut olması durumunda, bu kartın bağlantısı kesilmelidir. Benzer şekilde, RJ45 Ethernet kablosunu da çıkarın. Veri sızıntısı riskini en aza indirmek için internet kutunuzun fişini çekmeniz ve cep telefonunuzu kapatmanız önerilir. Ayrıca, mikrofon, web kamerası, hoparlör veya kulaklık gibi gereksiz çevre birimlerinin bilgisayarınızla bağlantısını kestiğinizden emin olun ve diğer çevre birimlerinin yalnızca kabloyla bağlı olup olmadığını kontrol edin. Tüm bu bilgisayar hazırlığı adımları zorunlu değildir, ancak gerçek bir bağlamda saldırı yüzeyini mümkün olduğunca azaltmaya yardımcı olurlar.


BIOS'unuzun harici bir cihazdan önyüklemeye izin verecek şekilde yapılandırılıp yapılandırılmadığını kontrol edin. Değilse, bu ayarı değiştirin ve ardından makinenizi yeniden başlatın. Bilgisayar ortamını güvence altına aldıktan sonra, bilgisayarı Tails OS içeren USB bellekten yeniden başlatın.


Tails karşılama ekranında istediğiniz dili seçin ve ardından `Start Tails` seçeneğine tıklayarak sistemi başlatın.


![mnemonic](assets/notext/12.webp)


Masaüstünden `Uygulamalar` sekmesine tıklayın.


![mnemonic](assets/notext/13.webp)


Yardımcı Programlar menüsüne gidin.


![mnemonic](assets/notext/14.webp)


Ve son olarak, `Terminal` uygulamasına tıklayın.


![mnemonic](assets/notext/15.webp)


Yeni bir boş komut terminaline ulaşacaksınız.


![mnemonic](assets/notext/16.webp)

Echo` komutunu ve ardından önceden oluşturduğunuz entropiyi yazın, `echo` ile ikili rakam diziniz arasında bir boşluk bıraktığınızdan emin olun.

![mnemonic](assets/notext/17.webp)


Ek bir boşluk ekleyin, ardından _pipe_ (`|`) kullanarak aşağıdaki komutu girin:


```plaintext
| shasum -a 256 -0


![mnemonic](assets/notext/18.webp)


Benim entropim ile ilgili örnekte, toplam komut aşağıdaki gibidir:


```plaintext
echo 11010111000110111011000011000010011000100111000001000000001001011011001010111111001010011111110001010100000101110010010011011010 | shasum -a 256 -0
```


Bu komutta:



- bit dizisini göndermek için `echo` kullanılır;
- `|`, _pipe_, `echo` komutunun çıktısını bir sonraki komutun girdisine yönlendirmek için kullanılır;
- shasum` SHA (_Secure Hash Algorithm_) ailesine ait bir hashing fonksiyonu başlatır;
- a` belirli bir hashing algoritmasının seçimini belirtir;
- 256` SHA256 algoritmasının kullanıldığını gösterir;
- 0` girdinin ikili sayı olarak yorumlanmasını sağlar.


İkili dizinizin herhangi bir yazım hatası içermediğini dikkatlice kontrol ettikten sonra, komutu çalıştırmak için `Enter` tuşuna basın. Terminal daha sonra entropinizin SHA256 Hash değerini görüntüleyecektir.


![mnemonic](assets/notext/19.webp)


Şimdilik, Hash onaltılık formatta (16 tabanı) ifade edilmektedir. Örneğin benimki şöyle:


```plaintext
a27abf1aff70311917a59a43ce86fa45a62723a00dd2f9d3d059aeac9b4b13d8
```


Mnemonic cümlemizi sonlandırmak için Hash'in yalnızca sağlama toplamını oluşturan ilk 4 bitine ihtiyacımız var. Onaltılık formatta her karakter 4 biti temsil eder. Bu nedenle, Hash'in yalnızca ilk karakterini saklayacağız. 24 kelimelik bir ifade için ilk iki karakteri dikkate almak gerekecektir. Benim örneğimde bu, harfe karşılık gelmektedir: `a`. Bu karakteri dikkatlice sayfanızda bir yere not edin ve ardından bilgisayarınızı kapatın.


Bir sonraki adım, bu onaltılık karakteri (taban 16) ikili değere (taban 2) dönüştürmektir, çünkü ifademiz bu formatta oluşturulmuştur. Bunu yapmak için aşağıdaki dönüşüm tablosunu kullanabilirsiniz:


| Decimal (base 10) | Hexadecimal (base 16) | Binary (base 2) |
| ----------------- | --------------------- | --------------- |
| 0                 | 0                     | 0000            |
| 1                 | 1                     | 0001            |
| 2                 | 2                     | 0010            |
| 3                 | 3                     | 0011            |
| 4                 | 4                     | 0100            |
| 5                 | 5                     | 0101            |
| 6                 | 6                     | 0110            |
| 7                 | 7                     | 0111            |
| 8                 | 8                     | 1000            |
| 9                 | 9                     | 1001            |
| 10                | a                     | 1010            |
| 11                | b                     | 1011            |
| 12                | c                     | 1100            |
| 13                | d                     | 1101            |
| 14                | e                     | 1110            |
| 15                | f                     | 1111            |

Benim örneğimde, `a` harfi `1010` ikili sayısına karşılık gelmektedir. Bu 4 bit kurtarma cümlemizin sağlama toplamını oluşturur. Şimdi bunları kağıdınıza önceden not ettiğiniz entropiye ekleyebilir ve son kelimenin sonuna yerleştirebilirsiniz.


![mnemonic](assets/notext/20.webp)


Mnemonic cümleniz artık tamamlanmıştır, ancak ikili formattadır. Bir sonraki adım bunu ondalık sisteme dönüştürmek olacaktır, böylece her sayıyı BIP39 listesinde karşılık gelen bir sözcükle ilişkilendirebilirsiniz.


## Adım 3: Kelimeleri Ondalık Sayıya Dönüştürme


Her bir ikili satırı ondalık sayıya dönüştürmek için, manuel hesaplamayı kolaylaştıran bir yöntem kullanacağız. Şu anda, kağıdınızda her biri `0` veya `1` olmak üzere 11 ikili rakamdan oluşan on iki satır var. Ondalık sayıya dönüştürme işlemine devam etmek için, her bir ilk basamağa `1` ise `1024`, aksi takdirde `0` değerini atayın. İkinci basamak için, `1` ise `512` değeri atanır, aksi takdirde `0` ve bu on birinci basamağa kadar devam eder. Karşılıklar aşağıdaki gibidir:



- 1. bit: `1024`;
- 2. bit: `512`;
- 3. bit: `256`;
- 4. bit: `128`;
- 5. bit: `64`;
- 6. bit: `32`;
- 7. bit: `16`;
- 8. bit: `8`;
- 9. bit: `4`;
- 10. bit: `2`;
- 11. bit: `1`.


Her satır için, ikili sayının ondalık sayı karşılığını elde etmek için `1` rakamlarına karşılık gelen değerleri toplayacağız. Şuna eşit bir ikili satır örneğini ele alalım:


```plaintext
1010 1101 101
```


Dönüşüm aşağıdaki gibi olacaktır:

![mnemonic](assets/notext/21.webp)

O zaman sonuç şöyle olur:


```plaintext
1389
```


1`e eşit olan her bit için aşağıdaki ilgili sayıyı raporlayın. 0`a eşit her bit için hiçbir şey bildirmeyin.


![mnemonic](assets/notext/22.webp)

Ardından, her bir ikili satırı temsil eden ondalık sayıyı elde etmek için `1`lerle doğrulanan tüm sayıları toplamanız yeterlidir. Örneğin, işte benim sayfam için nasıl göründüğü:

![mnemonic](assets/notext/23.webp)


## Adım 4: Mnemonic İfadesinin Sözcüklerini Arama


Elde edilen ondalık sayılarla, artık Mnemonic ifadesini oluşturmak için listedeki ilgili kelimeleri bulabiliriz. Ancak, BIP39 listesindeki 2048 kelimenin numaralandırılması `1` ile `2048` arasında değişmektedir. Ancak, hesapladığımız ikili sonuçlar `0` ile `2047` arasında değişmektedir. Bu nedenle, düzeltilmesi gereken bir birimlik bir kayma vardır. Bu kaymayı düzeltmek için, daha önce hesaplanan on iki ondalık sayıya `1` eklemeniz yeterlidir.


![mnemonic](assets/notext/24.webp)


Bu ayarlamadan sonra, listedeki her bir kelimenin sıralamasına sahip olursunuz. Geriye kalan tek şey her kelimeyi numarasına göre tanımlamaktır. Açıkçası, diğer tüm adımlarda olduğu gibi, bu dönüşümü gerçekleştirmek için bilgisayarınızı kullanmamalısınız. Bu nedenle, listeyi önceden yazdırdığınızdan emin olun.


[**-> BIP39 listesini A4 formatında yazdırın.**](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf)


Örneğin, ilk satırdan elde edilen sayı 1721 ise, karşılık gelen kelime listedeki 1721. kelime olacaktır:


```plaintext
1721. strike
```


![mnemonic](assets/notext/25.webp)

Bu şekilde, Mnemonic cümlemizi oluşturmak için 12 kelime ile art arda ilerliyoruz.


![mnemonic](assets/notext/26.webp)


## Adım 5: Bitcoin Wallet'in Oluşturulması


Bu noktada geriye kalan tek şey Mnemonic cümlemizi bir Bitcoin Wallet yazılımına aktarmaktır. Tercihlerimize bağlı olarak, bu işlem bir Hot Wallet elde etmek için bir masaüstü yazılımında veya bir Hardware Wallet Cold Wallet için bir GW-69 üzerinde yapılabilir.


![mnemonic](assets/notext/27.webp)


Yalnızca içe aktarma sırasında sağlama toplamınızın geçerliliğini doğrulayabilirsiniz. Yazılım `Geçersiz Sağlama Toplamı` gibi bir mesaj görüntülerse, oluşturma sürecinize bir hata girmiş demektir. Genellikle bu hata ya manuel dönüşümler ve eklemeler sırasında yapılan bir yanlış hesaplamadan ya da entropinizi Tails terminaline girerken yapılan bir yazım hatasından kaynaklanır. Bu hataları düzeltmek için süreci baştan başlatmanız gerekecektir.


![mnemonic](assets/notext/28.webp)

Wallet'inizi oluşturduktan sonra, kurtarma ifadenizi kağıt veya metal gibi fiziksel bir ortamda yedeklemeyi ve herhangi bir bilgi sızıntısını önlemek için oluşturma sırasında kullanılan elektronik tabloyu imha etmeyi unutmayın.


## Coldcard'larda Zar Atma Seçeneğinin Özel Durumu


Coldcard ailesinin donanım cüzdanları, Wallet'nizin kurtarma ifadesini zarlarla generate yapmak için _Dice Roll_] (https://youtu.be/Rc29d9m92xg?si=OeFW2iCGRvxexhK7) adlı bir özellik sunar. Bu yöntem mükemmeldir çünkü eğitimimizde olduğu gibi sağlama toplamını hesaplamak için harici bir cihaz kullanmanıza gerek kalmadan entropi oluşturma üzerinde doğrudan kontrol sahibi olmanızı sağlar.


Ancak son zamanlarda bu özelliğin uygunsuz kullanımı nedeniyle Bitcoin hırsızlığı vakaları rapor edilmiştir. Gerçekten de, çok sınırlı sayıda zar atımı yetersiz entropiye yol açarak teorik olarak Mnemonic ifadesini kaba kuvvetle zorlamayı ve ilgili bitcoinleri çalmayı mümkün kılabilir. Bu riskten kaçınmak için Soğuk Kart üzerinde en az 99 zar atılması tavsiye edilir, bu da yeterli entropi sağlar.


Coldcard tarafından önerilen sonuçları yorumlama yöntemi bu eğitimde sunulandan farklıdır. Biz eğitimde 128 bit güvenlik elde etmek için 128 zar atılmasını önerirken, Coldcard 256 bit güvenlik elde etmek için 99 zar atılmasını önermektedir. Aslında, bizim yaklaşımımızda, her zar atışı için sadece iki sonuç mümkündür: çift (`0`) veya tek (`1`). Bu nedenle, her zar atımının yarattığı entropi `log2(2)`ye eşittir. Zarın altı olası yüzünü (`1`den `6`ya kadar) dikkate alan Coldcard durumunda, zar başına entropi `log2(6)`ya eşittir. Bu nedenle dersimizde, aynı entropi seviyesine ulaşmak için daha fazla zar atmamız gerekir.


```plaintext
Entropy = number of rolls * log2(number of possible outcomes on the dice)

Coldcard :

Entropy = 99 * log2(6)
Entropy = 255.91

Our tutorial :

Entropy = 128 * log2(2)
Entropy = 128
```