---
name: Elektrum

description: Tam Elektrum Kılavuzu, 0'dan kahramana
---

![cover](assets/cover.webp)


Aşağıda Electrum için birkaç açıklama kaynağı bulun:



- [X](https://twitter.com/ElectrumWallet)
- [Electrum web sitesi](https://electrum.org/)
- [Electrum belgeleri](https://electrum.readthedocs.io/)


İşte Rogzy'nin bu eğitim hakkında düşündükleri:


> Bu rehbere rastladığımda şok olduğumu söylemeliyim. Bunun için Parman Arman'ı tebrik ederim. Burada barındırmamak ve mümkün olduğunca çok dile çevirmemek utanç verici olurdu. Dürüst olmak gerekirse, ipuçları dostum.

Orijinal gönderi aşağıdaki gibidir:


![Electrum Desktop Wallet (Mac / Linux) - download, verify, connect to your node.](https://youtu.be/wHmQNcRWdHM)


![Making a Bitcoin transaction with Electrum](https://youtu.be/-d_Zd7VcAfQ)


## Neden Electrum?


Bu, Electrum Bitcoin Wallet'in nasıl kullanılacağına dair, tüm tuzaklarına ve tuhaflıklarına çözümler içeren ayrıntılı bir kılavuzdur - birkaç yıl kullandıktan ve öğrencilere Bitcoin güvenliği / gizliliği hakkında eğitim verdikten sonra geliştirdiğim bir şey. Electrum, her şeyi olabildiğince basit tutmak isteyen ve başlangıç seviyesinde kalmayı tercih eden kişiler için en iyi Bitcoin Wallet değildir. Bunun yerine, "güçlü" bir kullanıcı olan veya olmak isteyen kişiler içindir.


Yeni Bitcoin'ciler için, yalnızca onlara yol gösterecek deneyimli bir kullanıcının gözetimi altında mükemmeldir. Tek başlarına kullanmayı öğreniyorlarsa, acele etmemeleri ve ilk başta sadece az sayıda Sats ile bir test ortamında kullanmaları güvenli olacaktır. Bu kılavuz bu çabayı desteklemektedir, ancak diğer herkes için de iyi bir referanstır.


**Uyarı:** bu kılavuz oldukça uzundur, bu nedenle açıklanan tüm adımları bir günde yapmaya çalışmayın. Kılavuzu el altında tutmanız ve zaman içinde istikrarlı bir şekilde ilerlemeniz tavsiye edilir.


**Not:** Aşağıdaki Electrum tam video kılavuzunu da izleyebilirsiniz (yazılı eğitimin yerini almadığına, ancak ona bir entegrasyon olduğuna dikkat edin):


![video](https://youtu.be/NNZdbYd8PUQ)


## Electrum İndiriliyor


İdeal olarak, Bitcoin işlemleriniz için özel bir Bitcoin bilgisayarı kullanın (Bunun için kılavuzum https://armantheparman.com/mint/) _(AYRICA gizlilik bölümünde mevcuttur)_. İlk öğrenirken "kirli" bir bilgisayarda küçük miktarlarla pratik yapmak iyidir (normal bilgisayarınızın yıllar içinde ne kadar gizli kötü amaçlı yazılım biriktirdiğini kim bilebilir - Bitcoin cüzdanlarınızı bunlara maruz bırakmak istemezsiniz).


Https://electrum.org/ adresinden Electrum alın.


En üstteki İndir sekmesine tıklayın.


Bilgisayarınıza karşılık gelen indirme bağlantısına tıklayın. Herhangi bir Linux veya Mac bilgisayar Python bağlantısını (kırmızı daire) kullanabilir. Intel veya AMD çipli bir Linux bilgisayar Appimage'ı kullanabilir (Green dairesi; bu bir Windows çalıştırılabilir dosyası gibidir). Raspberry Pi cihazı bir ARM mikroişlemciye sahiptir ve Pi'ler Linux çalıştırsa da Appimage'ı değil yalnızca Python sürümünü (kırmızı daire) kullanabilir. Mavi daire Windows için ve Siyah daire Mac içindir.


![image](assets/1.webp)


## Electrum'un Doğrulanması


İndirme işleminin "doğrulanmasının" amacı, tek bir veri parçasının bile değiştirilmediğinden emin olmaktır. Yazılımın "hacklenmiş" kötü amaçlı bir sürümünü kullanmanızı engeller. İndirilen kopyayı yalnızca pratik yapmak için kullanmanız, yani ciddi para tutan cüzdanları kullanmamanız koşuluyla bunu atlamanızda bir sakınca yoktur. Ardından, Electrum'u gerçek fonlarınız için kullanmaya hazır olduğunuzda, kopyanızı silmeli ve baştan başlamalısınız, bu sefer indirmenizi doğrulamalısınız.


Bunu yapmak için, burada hakkında bir rehber yazdığımız (https://armantheparman.com/gpg/) genel/özel anahtar kriptografi araçlarını - gpg'yi kullanıyoruz. Gpg aracı tüm Linux işletim sistemleriyle birlikte gelir. Mac ve Windows için, indirme talimatları için gpg bağlantısına bakın.


Electrum yazılımını indirmenin yanı sıra, güvenlik için yazılımın dijital İMZASINA da ihtiyacınız vardır. Bu, geliştiricinin ÖZEL gpg anahtarıyla ürettiği bir metin dizisidir (aslında metin kullanılarak kodlanmış bir sayıdır). Gpg programını kullanarak, İMZAYI, indirme DOSYASINA karşı herkesin erişebildiği KAMU anahtarına (geliştiricinin özel anahtarından oluşturulan) karşı "test edebiliriz".


Başka bir deyişle, üç girdiyle (imza, açık anahtar ve veri dosyası), dosyanın kurcalanmadığını doğrulamak için doğru veya yanlış bir çıktı elde ederiz.


İmzayı almak için, indirdiğiniz dosyaya karşılık gelen bağlantıya tıklayın (renkli oklara bakın):


![image](assets/2.webp)


Bağlantıya tıkladığınızda dosya otomatik olarak indirilenler klasörünüze indirilebilir veya tarayıcıda açılabilir. Tarayıcıda açılırsa, dosyayı kaydetmeniz gerekir. Sağ tıklayıp "farklı kaydet "i seçebilirsiniz. İşletim sistemine veya tarayıcıya bağlı olarak, metne değil beyaz boşluk alanına sağ tıklamanız gerekebilir.


İndirilen metin aşağıda görünmektedir. Birden fazla imza olduğunu görebilirsiniz - bunlar farklı kişiler tarafından atılan imzalar. Her birini veya herhangi birini doğrulayabilirsiniz. Ben size sadece geliştiricininkini nasıl doğrulayacağınızı göstereceğim.


![image](assets/3.webp)


Ardından, ThomasV'nin açık anahtarını almanız gerekir - kendisi ana geliştiricidir. Bunu doğrudan kendisinden, Keybase hesabından, Github'dan veya başka birinden, bir anahtar sunucusundan veya Electrum web sitesinden alabilirsiniz.


Electrum web sitesinden almak aslında en az güvenli yoldur, çünkü bu web sitesi kötü niyetliyse (kontrol ettiğimiz şey) neden ondan bir açık anahtar alıyoruz (açık anahtar sahte olabilir)?


Şimdilik basit tutmak için, yine de web sitesinden nasıl alacağınızı göstereceğim, ancak bunu aklınızda bulundurun. İşte GitHub'da karşılaştırabileceğiniz kopya (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc ).


ThomasV'nin açık anahtarının bağlantısını bulmak için sayfayı biraz aşağı kaydırın (aşağıdaki kırmızı daire). Tıklayın ve indirin ya da tarayıcıda bir metin açılırsa, kaydetmek için sağ tıklayın.


![image](assets/4.webp)


Artık 3 yeni dosyanız var, muhtemelen hepsi indirilenler klasöründe. Nerede oldukları önemli değil, ancak hepsini aynı klasöre koyarsanız işlemi kolaylaştırırsınız.


Üç dosya:


1. Elektrum indir

2. İmza dosyası (genellikle Electrum indirmesi ile aynı dosya adıdır ve ".asc" eklenir)

3. ThomasV'nin açık anahtarı.


Mac veya Linux'ta bir terminal veya Windows'ta komut istemi (CMD) açın.


İndirilenler dizinine (veya üç dosyayı nereye koyduysanız oraya) gidin. Bunun ne anlama geldiği hakkında hiçbir fikriniz yoksa, Linux/Mac için bu kısa videodan (https://www.youtube.com/watch?v=AO0jzD1hpXc) ve Windows için bu videodan (https://www.youtube.com/watch?v=9zMWXD-xoxc) öğrenin. Linux bilgisayarlarda dizin adlarının büyük/küçük harfe duyarlı olduğunu unutmayın.


Terminalde, ThomasV'nin açık anahtarını bilgisayarınızın "anahtarlığına" aktarmak için bunu yazın (anahtarlık soyut bir kavramdır - aslında sadece bilgisayarınızdaki bir dosyadır):


```bash
gpg --import ThomasV.asc
```


Dosya adının indirdiklerinizle eşleştiğinden emin olun. Ayrıca, tek tire değil çift tire olduğuna dikkat edin. Ayrıca, "-import "tan önce ve sonra bir boşluk olduğuna dikkat edin. Ardından <enter> tuşuna basın.


Dosya içe aktarılmalıdır. Bir hata alırsanız, dosyanın gerçekten bulunduğu dizinde olup olmadığınızı kontrol edin. Hangi dizinde olduğunuzu kontrol etmek için (Mac veya Linux'ta), pwd yazın. Bulunduğunuz dizinde hangi dosyaların olduğunu görmek için (Mac veya Linux'ta) ls yazın. Muhtemelen diğer dosyaların arasında "ThomasV.asc" metin dosyasının listelendiğini göreceksiniz.


Ardından imzayı doğrulamak için komutu çalıştırıyoruz.


```bash
gpg –verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```


Burada her biri bir boşlukla ayrılmış 4 "Elements" olduğuna dikkat edin. Görmenize yardımcı olmak için metni alternatif olarak kalınlaştırdım. Dört Elements şunlardır:


1. gpg programi

2. -verify seçeneği

3. imzanın dosya adı

4. programın dosya adı


İlginçtir ki, bazen 4. öğeyi atlayabilirsiniz ve bilgisayar ne demek istediğinizi tahmin eder. Emin değilim, ama sanırım sadece dosya adları sondaki "asc" ile farklıysa işe yarıyor.


Burada gösterdiğim dosya adlarını sadece kopyalamayın - sisteminizdeki dosya adıyla eşleştiğinden emin olun.


Komutu çalıştırmak için <enter> tuşuna basın. Başarılı olduğunu göstermek için "ThomasV'den iyi imza" yazısını görmelisiniz. İmza dosyasında bulunan diğer kişilerin imzalarının açık anahtarlarına sahip olmadığımız için bazı hatalar olacaktır (imzaları tek bir dosyada birleştiren bu sistem sonraki sürümlerde değişebilir). Ayrıca, en altta görmezden gelebileceğimiz bir uyarı var (bu, bilgisayara ThomasV açık anahtarına güvendiğimizi açıkça söylemediğimiz konusunda bizi uyarıyor).


Artık Electrum'un kullanımı güvenli olan doğrulanmış bir kopyasına sahibiz.


## Elektrum Çalıştırmak


### Python kullanıyorsanız Electrum'u çalıştırma


Python sürümünü indirdiyseniz, bu şekilde çalışmasını sağlayabilirsiniz. İndirme sayfasında şunu göreceksiniz:


![image](assets/5.webp)


Linux için, öncelikle sisteminizi güncellemek iyi bir fikirdir:


```bash
sudo apt-get update
sudo apt-get upgrade
```


Vurgulanan sarı metni kopyalayın, terminale yapıştırın ve <enter> tuşuna basın. Şifreniz sorulacak, muhtemelen devam etmek için bir onay istenecek ve ardından bu dosyaları ("bağımlılıklar") yükleyecektir.


Ayrıca sıkıştırılmış dosyayı seçtiğiniz bir dizine çıkarmanız gerekecektir. Bunu grafiksel kullanıcı Interface ile veya komut satırından (pembe vurgulu komut) yapabilirsiniz - dosya adlarınızın farklı olabileceğini unutmayın. (Önceki bölümde indirmeyi doğruladığımızda, doğruladığımızın zip dosyası olduğunu, çıkarılan dizin olmadığını unutmayın)


PIP programını kullanarak "yükleme" seçeneği vardır, ancak bu gereksizdir ve ekstra adımlar ve dosya yüklemeleri ekler. Tüm bunları atlamak için terminali kullanarak programı çalıştırın.


Adımlar (Linux) şunlardır:


1. dosyaların çıkarıldığı dizine gidin

2. tür: ./run_electrum


Mac'te adımlar aynıdır, ancak önce Python3'ü yüklemeniz ve çalıştırmak için bu komutu kullanmanız gerekebilir:


```bash
python3 ./run_electrum
```


Electrum çalıştığında, terminal penceresi açık kalacaktır. Eğer kapatırsanız, Electrum programını sonlandıracaktır. Electrum kullanırken sadece simge durumuna küçültün.


### Electrum'u Appimage ile Çalıştırma


Bu biraz daha kolaydır, ancak bir Windows çalıştırılabilir dosyası kadar kolay değildir. Çalıştırdığınız Linux sürümüne bağlı olarak, varsayılan olarak, Appimage dosyaları sistem tarafından yürütülmesine izin verilmeyecek şekilde ayarlanmış özniteliklere sahip olabilir. Bunu değiştirmeliyiz. Eğer Appimages dosyanız çalışıyorsa, bu adımı atlayabilirsiniz. Terminali kullanarak dosyanın bulunduğu yere gidin, ardından bu komutu çalıştırın:


```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```


"sudo" süper kullanıcı ayrıcalıkları verir; "chmod" modu değiştiren, kimin okuyabileceğini, yazabileceğini veya yürütebileceğini değiştiren bir komuttur; "ug+x" yürütmeye izin vermek için kullanıcı ve grubu değiştirdiğimiz anlamına gelir.


Dosya adını sürümünüzle eşleşecek şekilde ayarlayın.


Ardından, Electrum, Appimage simgesine çift tıklayarak çalışacaktır.


### Electrum'u Mac ile Çalıştırma


İndirilen dosyaya çift tıklayın (bu bir "sürücüdür"). Bir pencere açılacaktır. Penceredeki Electrum simgesini masaüstünüze veya programı tutmak istediğiniz yere sürükleyin. Daha sonra sürücüyü "çıkarabilir" ve sürücüyü (indirilen dosyayı) silebilirsiniz.


Programı çalıştırmak için çift tıklamanız yeterlidir. Atlanması gereken Mac'e özgü bazı "dadı" hataları alabilirsiniz.


### Electrum'u Windows ile Çalıştırma


Windows'tan en çok nefret etmeme rağmen, bu en basit yöntemdir. Çalıştırmak için yürütülebilir dosyaya çift tıklamanız yeterli.


## Sahte bir Wallet ile başlayın


Electrum'u ilk yüklediğinizde, aşağıdaki gibi bir pencere açılacaktır:


![image](assets/6.webp)


Sunucunuzu daha sonra manuel olarak seçeceğiz, ancak şimdilik varsayılanı ve otomatik bağlanmayı bırakın.


Ardından, sahte bir Wallet oluşturun - bu Wallet'e asla para koymayın. Bu sahte Wallet'in amacı, gerçek Wallet'inizi yüklemeden önce yazılımda ilerlemek ve her şeyin iyi çalıştığından emin olmaktır. Gerçek bir Wallet ile yanlışlıkla gizlilikten vazgeçmekten kaçınmaya çalışıyoruz. Sadece pratik yapıyorsanız, oluşturduğunuz Wallet zaten sahte bir Wallet olarak kabul edilebilir.


İsmi "default_wallet" olarak bırakabilir ya da istediğiniz şekilde değiştirebilir ve ileri butonuna tıklayabilirsiniz. Daha sonra, birden fazla cüzdanınız varsa, önce "Seç... "e tıklayarak onları bulabilir ve bu aşamada açabilirsiniz


![image](assets/7.webp)


"Standart Wallet" ve <Sonraki> öğesini seçin:


![image](assets/8.webp)


Ardından, "Zaten bir seed'um var" seçeneğini seçin. Electrum seed oluşturma alışkanlığı edinmenizi istemiyorum, çünkü diğer cüzdanlarla uyumlu olmayan kendi protokolünü kullanıyor - bu yüzden "yeni seed" seçeneğine tıklamıyoruz.


![image](assets/9.webp)


Https://iancoleman.io/bip39/ adresine gidin ve sahte bir seed oluşturun. Önce kelime numarasını 12 olarak değiştirin (bu yaygın bir uygulamadır), ardından "generate "e tıklayın ve kutudaki kelimeleri panonuza kopyalayın.


![image](assets/10.webp)


Ardından kelimeleri Electrum'a yapıştırın. İşte bir örnek:


![image](assets/11.webp)


Electrum kendi protokolüne uyan kelimeleri arayacaktır. Bunu atlamamız gerekiyor. Seçeneklere tıklayın ve BIP39 seed'ü seçin:


![image](assets/12.webp)


seed daha sonra geçerli hale gelir. (Bunu yapmadan önce, Electrum bir Electrum seed bekliyordu, bu nedenle bu seed geçersiz olarak görülüyordu). İleri'ye tıklamadan önce, "Checksum OK" yazan metne dikkat edin. Devam etmeden önce bunu görmeniz önemlidir (daha sonra kullanabileceğiniz gerçek Wallet için), çünkü bu, koyduğunuz seed'in geçerliliğini onaylar. En alttaki uyarı göz ardı edilebilir, Electrum geliştiricisinin BIP39 hakkındaki sızlanması ve kendi sürümlerinin (diğer cüzdanlarla uyumlu olmayan) daha üstün olduğuna dair "FUD'ey" iddialarıdır.


**Önemli bir uyarı için kısa bir sapma:** sağlama toplamının amacı, seed'inizi yazım hatası olmadan girdiğinizden emin olmaktır. Sağlama toplamı, matematiksel olarak seed'in ilk kısmı (11 kelime) tarafından belirlenen seed'in son kısmıdır (12. kelime sağlama toplamı kelimesi olur). Eğer başlangıçta yanlış bir şey yazarsanız, sağlama toplamı kelimesi matematiksel olarak eşleşmeyecek ve Wallet yazılımı sizi bir uyarı ile uyaracaktır. Bu, seed'in işlevsel bir Bitcoin Wallet oluşturmak için kullanılamayacağı anlamına gelmez. Yazım hatası olan bir Wallet oluşturduğunuzu, Wallet'yi Bitcoin ile yüklediğinizi, sonra bir gün Wallet'yi geri yüklemeniz gerekebileceğini, ancak bunu yaptığınızda yazım hatasını yeniden oluşturmadığınızı - yanlış Wallet'yi geri yükleyeceğinizi hayal edin! Sağlama toplamınız geçersizse Electrum'un Wallet yapmaya devam etmenize izin vermesi oldukça tehlikelidir, bu yüzden dikkatli olun, emin olmak sizin sorumluluğunuzdadır. Diğer cüzdanlar devam etmenize izin vermez, bu da çok daha güvenlidir. Electrum'u düzgün kullanmayı öğrendikten sonra kullanmanın iyi olduğunu söylerken kastettiğim şeylerden biri de budur (Electrum geliştiricileri bunu düzeltmelidir).


Bir passphrase eklemek isterseniz, bunu seçme şansının bu seçenekler penceresinde, hemen üstte olduğuna dikkat edin.


Tamam'a tıkladıktan sonra, seed ifadesini yazdığınız yere geri götürüleceksiniz. Bir passphrase seçeneği seçtiyseniz, bunu seed sözcükleriyle birlikte GİRMEYİN (bunun için istem daha sonra gelir).


Bir passphrase talep etmediyseniz, bu ekranı göreceksiniz - Wallet komut dosyası türünüz ve türetme yolunuz için buradan öğrenebileceğiniz daha fazla seçenek (https://armantheparman.com/public-and-private-keys/), ancak varsayılanları bırakın ve devam edin.


![image](assets/13.webp)


**Ekstra bilgi için** İlk seçenek, aşağıdakiler arasından seçim yapmanızı sağlar:



- eski ("1" ile başlayan adresler),
- Pay-to-Script-Hash ("3" ile başlayan adresler),
- bech32/native SegWit ("bc1q" ile başlayan adresler).


Bu yazının yazıldığı sırada Electrum henüz Taproot'yı ("bc1p" ile başlayan adresler) desteklememektedir. Bu penceredeki ikinci seçenek türetme yolunu değiştirmenize izin verir. Bunu asla değiştirmemenizi öneririm, özellikle de ne anlama geldiğini anlamadan önce. İnsanlar, gerektiğinde Wallet'nizi kurtarabilmeniz için türetme yolunu yazmanın önemini vurgulayacaklardır, ancak bunu varsayılan olarak bırakırsanız, muhtemelen iyi olacaksınız, bu yüzden panik yapmayın - ancak yine de türetme yolunu yazmak iyi bir uygulamadır.


Ardından, size bir ŞİFRE ekleme seçeneği sunulacaktır. Bu "passphrase" ile karıştırılmamalıdır. Parola, bilgisayarınızdaki dosyayı kilitler. passphrase özel anahtarın yapısının bir parçasıdır. Bu sahte bir Wallet olduğundan, şifreyi boş bırakabilir ve devam edebilirsiniz.


![image](assets/14.webp)


Yeni sürüm bildirimleri hakkında bir açılır pencere alacaksınız (hayır'ı seçmenizi öneririm). Wallet daha sonra kendini generate yapacak ve kullanıma hazır hale gelecektir (ancak unutmayın, bu Wallet silinmeye mahkumdur, sadece sahte bir Wallet'dir).


![image](assets/15.webp)


Yazılım ortamını kurmak için yapmanızı önerdiğim bazı şeyler var (yalnızca bir kez gerekli):


### Birimleri BTC olarak değiştirin


Üst menüye, araçlar -> electrum tercihlerine gidin ve orada genel sekmesinin altında "temel birimi" BTC olarak değiştirme seçeneğini bulacaksınız.

Adresler ve Madeni Paralar sekmesini etkinleştirin


Üst menüye gidin, görüntüleyin ve "adresleri göster "i seçin. Ardından görünüme geri dönün ve "paraları göster "i seçin.


### Oneserver'ı Etkinleştir


Electrum varsayılan olarak rastgele bir düğüme bağlanır. Ayrıca diğer birçok ikincil düğüme de bağlanır. Bu ikincil düğümlerle hangi verilerin değiş tokuş edildiğinden emin değilim, ancak gizlilik için bunun olmasını istemiyoruz. Örneğin kendi düğümünüz gibi bir düğüm belirleseniz bile, bu çok sayıda diğer düğüm de bağlanacaktır ve hangi bilgilerin paylaşıldığından emin değilim. Her şeye rağmen, bunu önlemek kolaydır. Size kendi düğümünüzü nasıl belirleyeceğinizi göstermeden önce, Electrum'u aynı anda yalnızca bir sunucuya bağlanmaya zorlayacağız.


**Not:** Bunu komut satırından "oneserver" belirterek yapmanın bir yolu var, ancak bu yolu önermiyorum. Uzun vadede daha kolay olduğunu düşündüğüm ve yanlışlıkla diğer düğümlere bağlanmanıza izin vermeme olasılığı daha yüksek olan bir alternatif göstereceğim.


Sahte bir Wallet kullanmamızın nedeni, gerçek Wallet'ümüzü gerçek Bitcoin'mizle yüklemiş olsaydık, şimdiye kadar yanlışlıkla rastgele bir düğüme bağlanmış olacaktık (başlangıçta "sunucuyu manuel olarak ayarla" yı seçmiş olsak bile, yine de bir nedenden dolayı bu diğer ikincil düğümlere bağlanıyor (hey Electrum geliştiricileri, bunu düzeltmelisiniz). Eğer Wallet'ümüz özel olsaydı, bu bir felaket olurdu.


Ayrıca aşağıda göstereceğim adımları bir tür Wallet yüklemeden yapamayız. (Yalnızca bir Wallet yüklendiğinde doldurulan ve düzenlemeye hazır hale gelen bir yapılandırma dosyasını düzenleyeceğiz).


Şimdi Electrum'u kapatın **(ÖNEMLİ: bunu yapmazsanız, yaptığınız aşağıdaki değişiklikler silinecektir)**.


### LINUX/MAC Yapılandırma Dosyası


Linux veya Mac'te terminali açın (Windows talimatları daha sonra):


Otomatik olarak ana klasörde olmalısınız. Oradan, gizli electrum ayarları klasörüne gidin (bu, uygulamanın bulunduğu yerden farklıdır).


```bash
cd .electrum
```


Gizli bir klasör olduğunu gösteren "electrum" kelimesinden önceki noktaya dikkat edin.


Oraya ulaşmanın bir başka yolu da yazmaktır:


```bash
cd ~/.electrum
```


burada "~" ev dizininizin yolunu temsil eder. Bulunduğunuz dizinin tam yolunu "pwd" komutu ile görebilirsiniz.


".electrum" dizinine girdikten sonra "nano config" yazın ve <enter> tuşuna basın.


Yapılandırma dosyası açıkken bir metin editörü açılacaktır (nano olarak adlandırılır). Fare burada pek işe yaramaz. Şöyle yazan satıra ulaşmak için ok tuşlarını kullanın:


```json
"oneserver": false,
```


"false" ifadesini "true" olarak değiştirin; ve sözdizimini bozmayın (virgül veya noktalı virgülü silmeyin).


Çıkmak için <ctrl> x tuşuna, kaydetmek için "y" tuşuna, ardından dosya adını düzenlemeden değiştirmeyi onaylayan <enter> tuşuna basın.


Şimdi Electrum'u tekrar çalıştırın. Ardından sağ alttaki daireye tıklayın, bu da ağ ayarlarını açar. Ardından, genel bakış sekmesinde en üste yakın bir yerde "1 düğüme bağlandı" ifadesini göreceksiniz - bu başarıyı gösterir.


Bunun hemen altında bir metin alanı göreceksiniz ve sunucunun Address'i orada. Şu anda o rastgele düğüme bağlısınız. Bir sonraki bölümde bir düğüme bağlanma hakkında daha fazla bilgi verilecektir.


### Windows Yapılandırma Dosyası


Windows yapılandırma dosyasını bulmak biraz daha zordur. Dizin: `C:/Users/Parman/AppData/Roaming/Electrum`


Açıkçası, "Parman "ı bilgisayar için kendi kullanıcı adınızla değiştirmeniz gerekir.


Bu klasörde yapılandırma dosyasını bulacaksınız. Bir metin düzenleyici ile açın ve satırı düzenleyin:


```json
"oneserver": false,
```


"false" ifadesini "true" olarak değiştirin; sözdizimini bozmayın (virgül veya noktalı virgülü silmeyin).


Ardından dosyayı kaydedin ve çıkın.


## Electrum'u bir düğüme bağlama


Ardından, sahte Wallet'mızı seçtiğimiz bir düğüme bağlamak istiyoruz. Bir düğüm çalıştırmaya hazır değilseniz, aşağıdakilerden birini yapabilirsiniz:


1. Bir arkadaşınızın kişisel düğümüne bağlanın (Tor gerektirir)

2. Güvenilir bir şirketin düğümüne bağlanın

3. Rastgele bir düğüme bağlanın (önerilmez).


Bu arada, işte kendi node'unuzu çalıştırmak için talimatlar ve bunu yapmanız için nedenler. (Node bölümündeki veya ücretsiz kurslarımızdaki eğitimlere göz atın)


### Tor aracılığıyla bir arkadaşınızın düğümüne bağlanın (Kılavuz çok yakında.)


### Güvenilir bir şirketin düğümüne bağlanın


Bunu yapmanın tek nedeni, Blockchain'ye erişmeniz gerekiyorsa ve kendi düğümünüz (veya bir arkadaşınızınki) yoksa olacaktır.


Bitaroo'nun düğümüne bağlanalım - Bize veri toplamadıkları söylendi. Onlar tutkulu bir Bitcoiner tarafından yönetilen bir Bitcoin Sadece Exchange. Onlara bağlanmak biraz güven gerektirir, ancak bir gözetim şirketi olabilecek rastgele bir düğüme bağlanmaktan daha iyidir.


Wallet'ın penceresinin sağ alt kısmındaki daireye tıklayarak Ağ Ayarlarına gidin (kırmızı bağlı olmadığını, Green bağlı olduğunu ve mavi Tor üzerinden bağlı olduğunu gösterir).


![image](assets/16.webp)


Daire simgesine tıkladığınızda, bir açılır pencere görünecektir: Daha önce zorladığımız için Wallet'niz "1 düğüme bağlı" olarak görünecektir.


"Sunucuyu otomatik olarak seç" kutusunun işaretini kaldırın ve ardından Sunucu Alanına Bitaroo'nun ayrıntılarını gösterildiği gibi yazın:


![image](assets/17.webp)


Pencereyi kapatın ve şimdi Bitaroo'nun düğümüne bağlı olmalıyız. Onaylamak için daire Green olmalıdır. Tekrar tıklayın ve sunucu ayrıntılarının rastgele bir düğüme geri dönmediğini kontrol edin.


### Kendi düğümünüze bağlanın


Eğer kendi düğümünüz varsa bu harika. Yalnızca Bitcoin core'ünüz varsa ve bir Electrum SERVER'ınız yoksa, düğümünüze henüz bir Electrum Wallet bağlayamazsınız.


**Electrum Server ve Electrum Wallet'in farklı şeyler olduğunu unutmayın:** sunucu, Electrum Wallet'in Bitcoin Blockchain ile iletişim kurabilmesi için gerekli bir yazılımdır - neden bu şekilde tasarlandığını bilmiyorum - muhtemelen hız için ama yanılıyor olabilirim.


MyNode (insanlara başlamalarını önerdiğim), Raspiblitz (daha ileri seviyeye geldiğinizde önerilir) veya Umbrel (çok fazla sorun yaşadığım için kişisel olarak henüz önermiyorum) gibi bir düğüm yazılım paketi kullanıyorsanız, Wallet'nizi sadece düğümü çalıştıran bilgisayarın (Raspberry Pi) IP Address'unu, artı iki nokta üst üste ve 50002'yi girerek bağlayabilirsiniz, önceki bölümdeki resimde gösterildiği gibi. (İleride size düğümünüzün IP Address'unu nasıl bulacağınızı göstereceğim).


Ağ ayarlarını açın (sağ alttaki Green veya kırmızı daireye tıklayın). "Sunucuyu otomatik olarak seç" kutusunun işaretini kaldırın, ardından benim yaptığım gibi Address IP'nizi girin, sizinki farklı olacaktır, ancak iki nokta üst üste ve "50002" aynı olmalıdır.


![image](assets/18.webp)


Pencereyi kapatın ve şimdi düğümünüze bağlı olmalıyız. Onaylamak için daireye tekrar tıklayın ve sunucu ayrıntılarının rastgele bir düğüme geri dönmediğini kontrol edin.


Bazen, her şeyi doğru yapmanıza rağmen, görünüşe göre, bağlanmayı reddediyor. İşte deneyebileceğiniz şeyler..



- Electrum'un ve düğüm yazılımınızın daha yeni bir sürümüne yükseltin;
- ".electrum" dizinindeki önbellek klasörünü silmeyi deneyin;
- Ağ ayarlarında bağlantı noktasını 50002'den 50001'e değiştirmeyi deneyin;
- Alternatif olarak Tor kullanarak bağlanmak için [bu kılavuzu] (https://armantheparman.com/tor/) kullanın;
- Electrum Server'ı düğüme yeniden yükleyin.


## Düğümünüzün IP'sini Bulma Address


IP Address, normal bir kullanıcının genellikle nasıl bakacağını ve kullanacağını bildiği bir şey değildir. Birçok kişinin bir node çalıştırmasına ve ardından cüzdanlarını node'a bağlamasına yardımcı oldum - tökezleyen bir engel genellikle IP Address'ü bulmak gibi görünüyor.


MyNode için bir tarayıcı penceresine yazabilirsiniz: `mynode.local`


Bazen "mynode.local" işe yaramaz (bunu bir Google arama çubuğuna yazmadığınızdan emin olun. Gezinti çubuğunun metninizi arama olarak değil Address olarak tanımasını sağlamak için metnin başına `http://` ekleyin: `http://mynode.local`. Bu işe yaramazsa, aşağıdaki gibi bir "s" ile deneyin: `https://mynode.local`.


Bu, cihaza erişecek ve IP Address'nın bulunduğu bu ekranı göstermek için ayarlar bağlantısına (aşağıdaki mavi "daireme" bakın) tıklayabilirsiniz:


![image](assets/19.webp)


Bu sayfa yüklenecek ve düğümün IP'sini göreceksiniz (mavi "daire")


![image](assets/20.webp)


Daha sonra, gelecekte tarayıcınıza 192.168.0.150 veya http://192.168.0.150 yazabilirsiniz.


Raspiblitz için (bir ekran bağlanmadığında), farklı bir yönteme ihtiyacınız vardır (MyNode için de çalışır):


Yönlendiricinizin web sayfasına giriş yapın - burada bağlı tüm cihazlarınızın IP Address'sini bulacağız. Yönlendiricinin web sayfası, bir web tarayıcısına girdiğiniz bir IP Address olacaktır. Benimki şöyle görünüyor:


http://192.168.0.1


Yönlendiricinin oturum açma kimlik bilgilerini almak için, kullanım kılavuzuna veya bazen yönlendiricinin üzerindeki bir etikete bakabilirsiniz. Kullanıcı adı ve parolayı arayın. Eğer bulamazsanız, Kullanıcı: "admin" Şifre: "password"


Oturum açabilirseniz, bağlı cihazlarınızı göreceksiniz ve adlarından düğümünüzün hangisi olduğu anlaşılabilir. IP Address orada olacaktır.


### İlk iki yöntem başarısız olursa, sonuncusu işe yarayacaktır ancak sıkıcıdır:


İlk olarak, ağınızdaki herhangi bir cihazın IP Address'unu bulun (mevcut bilgisayar yeterli olacaktır).


Mac'te bunu Ağ tercihlerinde bulabilirsiniz:


![image](assets/21.webp)


Biz ilk 4 Elements (192.168.0) ile ilgileniyoruz, resimde gördüğünüz 4. öğe olan "166" ile değil (sizinki farklı olacaktır).


Linux için komut satırını kullanın:


```bash
ifconfig | grep inet
```


Bu dikey çizgi "boru" sembolüdür ve <delete> tuşunun altında bulabilirsiniz. Bazı çıktılar ve bir IP Address göreceksiniz. (127.0.0.1'i dikkate almayın, o değil ve netmask'ı dikkate almayın)


Windows için, komut istemini (cmd) açın ve şunu yazın:


```bash
ipconfig/all
```


ve Enter tuşuna basın. IP Address çıktıda bulunabilir.


Bu işin kolay kısmıydı. Hard kısmı şimdi düğümünüzün IP Address'ünü bulmaktır - kaba kuvvetle tahmin etmemiz gerekir. Örneğin bilgisayarınızın IP Address'ünün 192.168.0.xxx ile başladığını varsayalım, o zaman düğümünüz için bir tarayıcıda şunu deneyin: `https://192.168.0.2`


Mümkün olan en küçük sayı 2'dir (0 herhangi bir cihaz anlamına gelir ve 1 yönlendiriciye aittir) ve sanırım en yüksek sayı 255'tir (bu, 1 bayt tarafından tutulan en büyük sayı olan ikili olarak 11111111 olur).


Teker teker 255'e doğru ilerleyin. Sonunda, MyNode sayfanızı (veya RaspiBlitz sayfanızı) yükleyen doğru numarada duracaksınız. O zaman düğümünüze bağlanmak için Electrum ağ ayarlarınıza hangi numarayı girmeniz gerektiğini bileceksiniz.


Şöyle bir şey görünecektir (iki nokta üst üste ve rakamları eklediğinizden emin olun):


![image](assets/22.webp)


**Not** Bu IP adreslerinin ev ağınız için DAHİLİ olduğunu bilmenizde fayda var. Dışarıdan kimse onları göremez ve hassas değildirler. Bunlar, büyük bir kuruluşta sizi farklı telefonlara yönlendiren telefon uzantıları gibidir.


## Sahte Wallet'i silin


Şimdi bir ve sadece bir düğüme başarıyla bağlandık. Electrum bundan sonra varsayılan olarak bu şekilde yüklenecektir. Şimdi sahte Wallet'yı silmelisiniz (Menü: dosya -> sil), yanlışlıkla bu güvensiz Wallet'ya para gönderme ihtimaline karşı (Güvensiz çünkü onu güvenli bir şekilde oluşturmadık).


## Bir alıştırma yapın Wallet


Sahte Wallet'i sildikten sonra, yeniden başlayın ve aynı şekilde yeni bir tane yapın, ancak bu sefer seed kelimelerini yazın ve oldukça güvenli bir yerde saklayın.


Bu pratik Wallet ile Electrum'un nasıl çalıştığını öğrenmek iyi bir fikirdir, hantal Hardware Wallet (yüksek güvenlik için gereklidir) olmadan. Bu Wallet'ye yalnızca küçük bir miktar Bitcoin koyun - Bu parayı kaybedeceğinizi varsayın. Yeterli olduktan sonra, Electrum'u bir Hardware Wallet ile kullanmayı öğrenin.


Oluşturduğunuz yeni Wallet'te bir adres listesi göreceksiniz. Green olanlara "alıcı adresler" denir. Bunlar 3 şeyin bir ürünüdür:



- seed ifadesi
- passphrase
- Türetme yolu


Yeni Wallet, seed, passphrase ve türetme yoluna sahip herhangi bir Software Wallet tarafından matematiksel ve tekrarlanabilir bir şekilde oluşturulabilen bir dizi alıcı adrese sahiptir. Bunlardan 4,3 milyar tane var! İhtiyacınız olandan daha fazla. Electrum size yalnızca ilk 20'sini gösterir ve siz ilklerini kullandıkça daha fazlasını gösterir.


Bitcoin özel anahtarları hakkında daha fazla bilgiyi bu kılavuzda bulabilirsiniz.


![image](assets/23.webp)


Bu, bir seferde yalnızca 1 Address sunan diğer bazı cüzdanlardan çok farklıdır.


Bu Wallet'ü oluştururken seed ifadesini girdiğiniz için, Electrum her bir adresin özel anahtarına sahiptir ve bu adreslerden harcama yapmak mümkündür.


Ayrıca "değişim adresleri" olarak adlandırılan sarı adresler olduğunu da unutmayın - Bunlar sadece farklı bir matematiksel daldan başka bir adres kümesidir (bunlardan 4,3 milyar tane daha vardır). Wallet tarafından fazla fonları otomatik olarak Wallet'ye değişim olarak geri göndermek için kullanılırlar. Örneğin, 1.5 Bitcoin alır ve 0.5'ini bir tüccara harcarsanız, kalan 1.0'ın bir yere gitmesi gerekir. Wallet'niz bunu bir sonraki boş sarı para üstü Address'e harcayacaktır - aksi takdirde Miner'e gider! Bu konuda daha fazla bilgi için (UTXO'lar) bkz. ![bu kılavuz] (https://armantheparman.com/UTXO/).


Ardından, Ian Colman özel anahtar web sitesine geri dönün ve seed'ı girin (bir tane oluşturmak yerine). Aşağıda özel ve açık anahtar bilgilerinin değiştiğini göreceksiniz; aşağıdaki her şey sayfanın yukarısındaki şeylere bağlıdır.


**Unutmayın:** gerçek Bitcoin Wallet veya bir bilgisayarınızın seed'ünü "asla" girmemelisiniz, kötü amaçlı bir yazılım bunu çalabilir. Biz sadece öğrenme amaçlı bir alıştırma Wallet kullanıyoruz, bu yüzden şimdilik sorun yok.


Aşağı kaydırın ve BIP84 sekmesine tıklayarak türetme yolunu Electrum Wallet ile eşleşecek şekilde BIP84 (SegWit) olarak değiştirin.


![image](assets/24.webp)


Bunun altında, hesabın genişletilmiş özel anahtarını ve hesabın genişletilmiş genel anahtarını göreceksiniz:


![image](assets/25.webp)


Electrum'a gidin ve eşleştiklerini karşılaştırın. Üstte bir menü var, Wallet ->bilgi:


![image](assets/26.webp)


Bu çıkıyor:


![image](assets/27.webp)


İki açık anahtarın eşleştiğine dikkat edin.


Sonra, adresleri karşılaştırın. Ian Coleman'ın sitesine geri dönün ve aşağıya doğru kaydırın:


![image](assets/28.webp)


Electrum'daki adreslerle eşleştiklerine dikkat edin.


Şimdi değişiklik adreslerini kontrol edeceğiz. Türetme yoluna doğru biraz yukarı kaydırın ve son 0'ı 1 olarak değiştirin:


![image](assets/29.webp)


Şimdi aşağı kaydırın ve adresleri Electrum'daki sarı adreslerle karşılaştırın


Tüm bunları neden yaptık?


seed kelimelerini aldık ve bize aynı bilgileri verdiklerinden emin olmak için iki farklı bağımsız yazılım programından geçirdik. Bu, hain kodun içeride gizlenmesi ve bize yanlış özel veya genel anahtarlar ya da adresler vermesi riskini önemli ölçüde azaltıyor.


Yapılacak bir sonraki şey, küçük bir test almak ve bunu bir Address'den diğerine Wallet içinde harcamaktır.


## Wallet'ün test edilmesi (Kullanmayı öğrenin)


Burada size bir UTXO'ü Wallet'nize nasıl alacağınızı ve ardından Wallet içindeki başka bir Address'e nasıl taşıyacağınızı (harcayacağınızı) göstereceğim. Bu, kaybetme riskini göze almayacağımız çok küçük bir miktardır.


Bunun birkaç amacı vardır.



- Yeni Wallet'te madeni para harcama gücüne sahip olduğunuzu kanıtlayacaktır.
- Güvenlik için ekstra karmaşıklık eklemeden önce (bir Hardware Wallet veya hava boşluklu bilgisayar kullanarak) bir harcama yapmak için Electrum yazılımının nasıl kullanılacağını (ve bazı özellikleri) gösterecektir
- Aynı Wallet içinde almak ve harcamak için seçebileceğiniz birçok adresiniz olduğu fikrini pekiştirecektir.


Test Electrum Wallet'inizi açın ve Adresler sekmesine tıklayın, ardından ilk Address'ye sağ tıklayın ve Kopyala -> Address'yi seçin:


![image](assets/30.webp)


Address artık bilgisayarınızın belleğindedir.


Şimdi biraz Bitcoin'nizin olduğu bir Exchange'a gidin ve bu Address'e küçük bir miktar çekelim, diyelim ki 50.000 Sats. Örnek olarak Coinbase'i kullanacağım çünkü Exchange düşmanı olmalarına rağmen en yaygın kullanılan Bitcoin bu ve bu amaçla terk edilmiş eski bir hesaba giriş yapmaktan iğreniyorum.


Oturum açın ve bugün itibariyle web sayfasının sağ üst köşesinde bulunan Gönder/Al düğmesine tıklayın.


![image](assets/31.webp)


Açıkçası Coinbase'de fonum yok, ancak burada fon olduğunu hayal edin ve takip edin: Electrum'dan Address'ü benim yaptığım gibi "Kime" alanına yapıştırın. Ayrıca bir miktar da seçmeniz gerekecek (ben 50.000 Sats gibi bir miktar öneriyorum). "İsteğe bağlı bir mesaj" koymayın - Coinbase verilerinizi yeterince topluyor (ve satıyor), onlara yardım etmeye gerek yok. Son olarak, "Devam Et" seçeneğine tıklayın. Bundan sonra başka hangi pop-up'ları alacağınızı bilmiyorum, kendi başınızasınız, ancak yöntem tüm borsalar için benzer.


![image](assets/32.webp)


Exchange'ya bağlı olarak, Sats'i Wallet'nizde hemen veya birkaç saat/gün içinde görebilirsiniz.


Electrum'un, Blockchain'da onaylanmamış olsalar bile size alınan coinleri göstereceğini unutmayın. Sahip olduğunuz coinler, bir Bitcoin Node'un bekleme listesinden veya "Mempool" den okunmaktadır. Bir bloğa ulaştığında, fonları onaylanmış olarak göreceksiniz.


Artık Wallet'ümüzde bir UTXO olduğuna göre, onu etiketlemeliyiz. Bu etiketi sadece biz görebiliriz, halka açık Ledger ile hiçbir ilgisi yoktur. Tüm Electrum Etiketlerimiz yalnızca kullandığımız bilgisayarda görülebilir. Aslında bir dosya kaydedebilir ve tüm etiketlerimizi aynı Wallet'ü çalıştıran farklı bir bilgisayara geri yüklemek için kullanabiliriz.


### UTXO için bir etiket yapın


Bu test Wallet'e bağış yapmam gerekiyordu, bana canlı bir UTXO (10.000 Sats) sağladığı için @Sathoarder'a teşekkür ederim ve başka bir kişi (anon) aynı Address'ya (5000 Sats) bağış yaptı. İlk Address bakiyesinde 15.000 Sats ve toplam 2 işlem olduğuna dikkat edin (en sağ sütun). Altta, Bakiye 10.000 Sats onaylanmış ve diğer 5.000 Sats onaylanmamış (hala Mempool'de).


![image](assets/33.webp)


Şimdi, Madeni Paralar sekmesine gidersek, iki "alınan madeni para" veya UTXO görebiliriz. İkisi de aynı Address'in içinde.


![image](assets/34.webp)


Address sekmesine geri dönecek olursak, Address'nin yanındaki "etiketler" alanına çift tıklarsanız, bazı metinler girebilir ve ardından kaydetmek için <enter> tuşuna basabilirsiniz:


![image](assets/35.webp)


Bu iyi bir uygulamadır, böylece madeni paralarınızın nereden geldiğini, KYC'siz olup olmadıklarını ve her bir UTXO'ün size ne kadara mal olduğunu takip edebilirsiniz (satmanız ve hükümetiniz tarafından sizden çalınacak vergiyi hesaplamanız gerektiğinde).


İdeal olarak, aynı Address'te birden fazla madeni para biriktirmekten kaçınmalısınız. Bunu yapmaya karar verirseniz (yapmayın), Address yöntemini kullanarak hepsini aynı etiketle etiketlemek yerine her bir Coin'yı etiketleyebilirsiniz. Aslında "madeni paralar" sekmesine gidip etiketleri orada düzenleyemezsiniz (hayır, bu çok sezgisel olurdu!). Geçmiş sekmesine gitmeniz, işlemi bulmanız, etiketlemeniz ve ardından etiketleri Coin bölümünde görmeniz gerekir. Madeni paralar bölümünde gördüğünüz tüm etiketler Address etiketlerinden VEYA geçmiş etiketlerindendir, ancak herhangi bir geçmiş etiketi herhangi bir Address etiketini geçersiz kılar. Etiketlerinizi bir dosyaya yedeklemek için, bunları üstteki menüden, Wallet->lables->export'tan dışa aktarabilirsiniz.


Ardından, ilk Address'deki madeni paraları ikinci Address'ye harcayalım. İlk Address'ye sağ tıklayın ve "şuradan harca" seçeneğini seçin (Bu senaryoda bu aslında gerekli değildir, ancak birçok adreste çok sayıda madeni paramız olduğunu düşünün; bu özelliği kullanarak Wallet'i yalnızca istediğimiz madeni paraları harcamaya zorlayabiliriz. Birden fazla adresteki birden fazla madeni parayı seçmek istiyorsak, komut tuşunu basılı tutarken farenin sol tuşuyla tıklayarak adresleri seçebilir, ardından sağ tıklayıp "şuradan harca" seçeneğini belirleyebiliriz:


![image](assets/36.webp)


Bunu yaptığınızda, Green penceresinin altında seçtiğiniz jeton sayısını ve harcayabileceğiniz toplam tutarı gösteren bir Wallet çubuğu olacaktır.


Ayrıca bir Address içinde tek tek coin harcayabilir ve aynı Address'deki diğer coinleri hariç tutabilirsiniz, ancak bu önerilmez çünkü coinlerden birinin harcanması nedeniyle kriptografik olarak zayıflatılmış bir Address'de coin bırakmış olursunuz (gizlilik nedenlerinin yanı sıra bir Address'e birden fazla coin koymamanın bir başka nedeni de, birini harcarsanız hepsini harcamanız gerektiği düşünüldüğünde, bunun gereksiz yere pahalıya mal olmasıdır). Paylaşılan bir Address'den tek bir Coin'yi nasıl seçeceğiniz aşağıda açıklanmıştır, ancak bunu yapmayın:


![image](assets/37.webp)


Şimdi, harcamak için seçtiğimiz iki madeni paramız var. Sonra, onları nereye harcayacağımıza karar verdik. Onları ikinci Address'e gönderelim. Address'ü şu şekilde kopyalamamız gerekecek:


![image](assets/38.webp)


Ardından "Gönder" sekmesine gidin ve ikinci Address'ü "ödeme yapılacak" alanına yapıştırın. Açıklama eklemenize gerek yok; ekleyebilirsiniz, ancak bunu daha sonra etiketleri düzenleyerek yapabilirsiniz. Miktar için, seçtiğimiz tüm madeni paraları harcamak için "Maks" seçeneğini seçin. Ardından "Öde "ye tıklayın ve ardından açılan pencerede "gelişmiş" düğmesine tıklayın.


![image](assets/39.webp)


Bu aşamada her zaman "gelişmiş" seçeneğine tıklayın, böylece ince kontrol yapabilir ve işlemde tam olarak ne olduğunu kontrol edebiliriz. İşte işlem:


![image](assets/40.webp)


İki dahili beyaz kutu/pencere görüyoruz. Üstteki pencere girdiler (hangi madeni paraların harcandığı), alttaki pencere ise çıktılar (madeni paraların nereye gittiği).


Durumun (sol üst) şimdilik "imzalanmamış" olduğuna dikkat edin. "Gönderilen miktar" 0'dır çünkü madeni paralar Wallet içinde transfer edilmektedir. Ücret 481 Sats'dır. Eğer 480 Sats olsaydı, son sıfırın düşeceğini unutmayın, bunun gibi, 0.0000048 ve yorgun bir göz için bu 48 Sats gibi görünebilir - dikkatli olun (Electrum geliştiricilerinin düzeltmesi gereken bir şey).


İşlemin boyutu, Bitcoin miktarını değil, bayt cinsinden veri boyutunu ifade eder. "Replace by fee" varsayılan olarak açıktır ve gerekirse işlemi daha yüksek bir ücretle yeniden göndermenize olanak tanır. LockTime, işlemin ne zaman geçerli olacağını ayarlamanıza olanak tanır - henüz bununla oynamadım, ancak ne yaptığınızı tam olarak anlamadığınız ve küçük miktarlarla biraz pratik yapmadığınız sürece kullanmamanızı tavsiye ederim.


En altta, bazı süslü Mining ücret ayarlama araçlarımız var. Dahili transferler için yapmanız gereken tek şey minimum ücret olan 1 sat/byte'a ayarlamaktır. Hedef ücret alanına sayıyı manuel olarak yazmanız yeterlidir. Harici bir ödeme için uygun bir ücreti kontrol etmek için, Mempool'un ne kadar meşgul olduğunu görmek için https://Mempool.space adresine başvurabilirsiniz ve bazı önerilen ücretler görüntülenir.


![image](assets/41.webp)


1 sat/byte seçtim.


Giriş penceresinde iki giriş görüyoruz. İlki 5000 satlık bağış. Sol tarafta Hash işlemini görüyoruz (Blockchain'e bakabiliriz). Yanında bir "21" var - bu, o işlemde 21 olarak etiketlenmiş çıktı olduğunu gösterir (aslında 22. çıktıdır çünkü ilki sıfır olarak etiketlenmiştir).


Burada dikkat edilmesi gereken bir şey var: UTXO'lar yalnızca bir işlemin içinde bulunur. Bir UTXO'ü harcamak için ona referans vermemiz ve bu referansı yeni bir işlemin girişine koymamız gerekir. Daha sonra çıkışlar yeni UTXO'lar haline gelir ve eski UTXO bir STXO (Harcanan işlem çıkışı) olur.


İkinci satır 10.000 satlık bağıştır. Hash işleminin yanında bir "0" vardır, çünkü bu işlem için ilk (ve muhtemelen tek) çıktıdır.


Alt pencerede Address'imizi görüyoruz. Bitcoin girişlerinin toplamının çıkışların toplamıyla tam olarak eşleşmediğine dikkat edin. Aradaki fark Miner'e gider. Miner, madenciliğini yapmaya çalıştığı bloktaki tüm işlemlerdeki tutarsızlığa bakar ve bu sayıyı ödülüne ekler. (Bu şekilde Mining ücretleri işlem zincirinden tamamen ayrılır ve yeni bir hayata başlar).


Mining ücretini ayarlarsak, çıkış değeri otomatik olarak değişecektir.


**Burada belirtmekte fayda var:** işlem penceresindeki adreslerin rengine dikkat edin. Green adreslerinin Address sekmenizde listelendiğini unutmayın. Bir Address işlem penceresinde Green (veya sarı) ile vurgulanmışsa, Electrum Address'ı kendisinden biri olarak tanımıştır. Address vurgulanmamışsa, harici bir Address'tır (o anda açık olan Wallet'in haricinde) ve bunu daha dikkatli kontrol etmelisiniz.


İşlemdeki her şeyi kontrol ettikten ve hangi jetonları harcadığınızdan ve jetonların nereye gittiğinden memnun olduğunuzdan emin olduktan sonra "sonlandır" düğmesine tıklayabilirsiniz


![image](assets/42.webp)


"Sonlandır" düğmesine tıkladıktan sonra artık düzenleme yapamazsınız - Gerekirse bunu kapatıp yeniden başlamanız gerekir. "Sonlandır" düğmesinin "dışa aktar" olarak değiştiğine ve yeni düğmelerin ortaya çıktığına dikkat edin: "kaydet", "birleştir", "imzala" ve "yayınla". "Yayınla" düğmesi gri renktedir çünkü işlem imzasızdır ve bu nedenle bu aşamada geçersizdir.


İmzala'ya tıkladığınızda, Wallet için bir şifreniz varsa bu şifre istenecek ve ardından durum (sağ üst) "İmzalanmadı "dan "İmzalandı "ya değişecektir. Ardından "Yayınla" düğmesi kullanılabilir olacaktır.


Yayın yaptıktan sonra işlem penceresini kapatabilirsiniz. Address sekmesine giderseniz, şimdi ilk Address'ün boş olduğunu ve ikinci Address'te 1 UTXO olduğunu göreceksiniz.


Not: Tüm bu değişiklikleri, işlem bir bloğa çıkarılmadan veya "onaylanmadan" önce bile göreceksiniz. Bunun nedeni, Electrum'un bakiyeleri/işlemleri yalnızca Blockchain verilerine göre değil, Mempool verilerine göre de güncellemesidir. Tüm cüzdanlar bunu yapmaz.


Dikkat edilmesi gereken bir nokta, yayınlamak yerine işlemi daha sonrası için kaydedebileceğimizdir. İmzasız ya da imzalı olarak kaydedilebilir.


"Dışa aktar" düğmesine tıklayın (paradoksal olarak, "kaydet" düğmesine TIKLAMAYIN) ve bir dizi seçenek göreceksiniz. İşlem metinle kodlanmıştır ve bu nedenle çeşitli şekillerde kaydedilebilir.


![image](assets/43.webp)


Bir QR koduna kaydetmek çok ilginçtir. Bunu seçerseniz, bir QR açılır:


![image](assets/44.webp)


Daha sonra QR kodunun bir fotoğrafını çekebilirsiniz. Bununla yapabileceğiniz birçok şey var, ancak şimdilik, daha sonra Wallet'e geri yükleyeceğinizi varsayalım. Electrum'u kapatabilir, Wallet'i tekrar yükleyebilir ve Araçlar menüsüne gidebilirsiniz:


![image](assets/45.webp)


Bu, bilgisayarınızın kamerasını yükleyecektir. Daha sonra kameraya telefonunuzdaki QR kodunun fotoğrafını gösterirsiniz ve bu da işlemi aynen bıraktığınız gibi geri yükler.


Kaydedilmiş bir işlemin nasıl yükleneceği sezgisel değildir, bu yüzden özel not alın. Bir işlemi yüklemek bir "araç" değildir, ancak seçenek araçlar menüsünde gizlidir (Electrum geliştiricilerinin düzeltmesi gereken başka bir şey).


Benzer bir işlem dosya olarak kaydedilmiş bir işlemle de mümkündür. Aynı Wallet içinde her iki yöntemle de pratik yapmayı deneyin. Burada anlatmayacağım ancak bu özelliği farklı bilgisayarlardaki aynı Wallet arasında, çoklu imza cüzdanları arasında ve donanım cüzdanlarına gidip gelmek için bir işlemi aktarmak için kullanabilirsiniz. İşte bazı talimatlar.


Şimdi, "kaydet" düğmesine geri dönersek - bu işlem metninin nasıl kaydedileceği değildir. Bunun aslında yaptığı şey Electrum Wallet'e bu işlemi yerel bilgisayarda bir ödeme olarak gönderilmiş olarak tanımasını söylemektir. Bunu yanlışlıkla yaparsanız, işlemi küçük bir bilgisayar simgesiyle görürsünüz. İşlemi sağ tıklayıp silebilirsiniz - endişelenmeyin, Bitcoin'i bu şekilde silemezsiniz. Electrum daha sonra bu işlemin gerçekleştiğini unutacak ve Sats'yi geri "iade edecek" ve Sats'yi gerçekte var oldukları doğru konumda görüntüleyecektir.


### Adresleri değiştirin


Değişim adresleri ilginçtir. Bu açıklamayı anlamak için UTXO'ları anlamanız gerekir. Bir Address'e UTXO'dan daha küçük bir miktar harcıyorsanız, bir değişiklik çıktısı belirtilmediği sürece kalan Bitcoin Miner'e gidecektir.


Elinizde 6,15 Bitcoin UTXO olabilir ve dünyanın herhangi bir yerindeki zalim "demokratik" hükümet tarafından ezilen bazı protestoculara bağış yapmak için 0,15 Bitcoin harcamak isteyebilirsiniz. Daha sonra 6,15 Bitcoin'yi alırsınız (Electrum'daki "spend from" işlevini kullanarak) ve bir işleme koyarsınız.


Protestocuların Address'unu "pay to" alanına yapıştırırsınız, belki "description" alanına "EndTheFed & WEF" yazarsınız ve miktar için 0,15 Bitcoin yazıp "pay" ve ardından "advanced" butonlarına tıklarsınız.


İşlem ekranında, girdi penceresi için 6,15 Bitcoin UTXO'ü göreceksiniz. Çıktı penceresi için, yanında 0,15 Bitcoin ile vurgulanmamış bir Address (bu protestocuların Address'idir) göreceksiniz. Ayrıca 6,0 Bitcoin'den biraz daha az olan sarı bir Address göreceksiniz. Bu, Wallet tarafından kendi sarı değişiklik adreslerinden birinden otomatik olarak seçilen Address değişikliğidir. Değişim Address'in amacı, Wallet'ün planladığınız veya fatura gönderdiğiniz alıcı adreslerin kullanılabilirliğini bozmadan bunlara değişim paraları koyabilmesidir. Örneğin, daha sonra müşteriler tarafından kullanılacaklarsa, Wallet'ünüzün bunları otomatik olarak kullanmasını ve doldurmasını istemezsiniz. Dağınıktır ve gizlilik için kötüdür.


Mining ücretini ayarladığınızda, ödeme tutarının değil, değişiklik çıktı tutarının otomatik olarak ayarlanacağını unutmayın.


### Manuel değişim veya birçok kişiye ödeme


Bu, Electrum'un gerçekten ilginç bir özelliğidir. Bu şekilde erişebilirsiniz.


![image](assets/46.webp)


Daha sonra harcadığınız UTXO bakiyesi için aşağıdaki gibi birden fazla hedef girebilirsiniz:


![image](assets/47.webp)


Address'yi yapıştırın, bir virgül, sonra bir boşluk, sonra tutarı yazın, sonra <enter>, sonra tekrar yapın. "TUTAR" PENCERELERİNE TUTARLARI GİRMEYİN - Electrum, siz "Öde" penceresine ayrı ayrı tutarları yazdıkça toplamı buraya dolduracaktır.


Bu, değişikliğin nereye gideceğini manuel olarak belirlemenize olanak tanır (örneğin, Address'inizdeki belirli bir Wallet veya başka bir Wallet) veya aynı anda birçok kişiye ödeme yapabilirsiniz. Toplamınız UTXO'ın boyutuyla eşleşecek kadar yüksek değilse, Electrum yine de sizin için ek bir değişiklik çıktısı oluşturacaktır.


Pay to Many özelliği aynı zamanda kendi "PayJoins" veya "CoinJoins "lerinizi oluşturma imkanı da sunuyor - bu makalenin kapsamı dışında, ancak burada bir rehberim var. (https://armantheparman.com/cj/)


## Cüzdanlar


Electrum kullanarak bir Watching Only Wallet göstermek istiyorum. Bunu yapmak için önce "Wallet "yi tanımlamam gerekiyor. Wallet'de "Bitcoin" iki şekilde kullanılır:



- A Tipi, "Wallet" - adreslerinizi ve bakiyelerinizi gösteren yazılımı ifade eder, örneğin Electrum, Blue Wallet, Sparrow wallet vb.



- B Tipi, "Wallet" - seed_phrase/passphrase/derivation_path kombinasyonumuzla ilişkili benzersiz adres koleksiyonunu ifade eder. Herhangi bir Wallet'da 8,6 milyar adres vardır (4,3 milyar alıcı adresi ve 4,3 milyar değişiklik adresi). seed cümlesinde, passphrase'te veya türetme yolunda herhangi bir şeyi değiştirirseniz, yeni ve tamamen benzersiz, 8,6 milyar boş adrese sahip kullanılmayan bir Wallet elde edersiniz.


"Wallet" kelimesini kullanırken hangi türden bahsedildiği bağlam içinde açıktır.


## Wallet'u izlemek - bir egzersiz


Wallet'in ne işe yaradığı tam olarak açık değil, ancak ne olduğunu, nasıl pratik yapılacağını açıklayarak başlayacağım ve daha sonra donanım cüzdanları hakkında daha fazla açıklama yaptığımda amacına geri döneceğiz. (Bir Hardware Wallet'ün ve çeşitli markaların nasıl kullanılacağına dair derinlemesine bir inceleme için buraya bakın)


Sahte bir normal Wallet (bu kez bir passphrase ile biraz daha karmaşıklık katarak) ve ardından ona karşılık gelen izleyici Wallet yapacağız. İsterseniz benim yaptığımı aynen kopyalayabilir ya da kendinizinkini oluşturabilirsiniz - bu Wallet atılacak; aslında onu kullanmayın. Ian Coleman web sitesini kullanarak 12 kelimelik bir seed oluşturarak başlayın.


Aşağıdaki ekran görüntüsünde 12 rastgele kelimeye ve passphrase alanına bir passphrase girdiğime dikkat edin:


passphrase: "Craig Wright bir yalancı ve dolandırıcıdır ve hapishaneye aittir. Ayrıca Ross Ulbricht de derhal hapisten çıkarılmalıdır."


passphrase en fazla 100 karakter uzunluğunda olabilir ve ideal olarak açık ve çok kısa olmamalıdır - Benim kullandığım sadece eğlence amaçlıdır - passphrase'nizi hatırlamakta sorun yaşarsanız, kombinasyonları denerken stresinizi azaltmak için genellikle büyük harflerden ve sembollerden kaçınmanızı öneririm.


![image](assets/48.webp)


Ardından, Electrum'da dosya->yeni/geri yükle menüsüne gidin. Yeni bir Wallet oluşturmak için benzersiz bir ad yazın ve "ileri" ye tıklayın.


![image](assets/49.webp)


Sonraki adımları şimdiye kadar biliyor olmalısınız, bu yüzden onları resimsiz olarak listeleyeceğim:



- Standart Wallet
- Zaten bir seed'um var
- 12 kelimeyi kopyalayıp kutuya yapıştırın veya elle yazın.
- Seçeneklere tıklayın ve BIP39'u seçin ve ayrıca passphrase onay işaretine tıklayın ("bu seed'yi özel kelimelerle genişletin")
- passphrase'ünüzü aynen Ian Coleman sayfasında yaptığınız gibi girin
- Varsayılan kod semantiğini ve türetme yolunu bırakın
- Şifre eklemeye gerek yoktur (Wallet'ü kilitler)


Şimdi Ian Coleman sitesine geri dönün, "türetme yolu" bölümüne gidin ve Electrum'daki (Yerel SegWit) varsayılanlarla aynı kod semantiğini seçmek için "BIP 84" sekmesine tıklayın.


![image](assets/50.webp)


Genişletilmiş özel ve açık anahtarlar hemen aşağıdadır ve türetme yolunda (veya sayfanın yukarısındaki herhangi bir şeyde) değişiklik yaptığınızda değişirler.


![image](assets/51.webp)


Ayrıca "BIP32 genişletilmiş özel/genel" anahtarları da göreceksiniz - bunlar şimdilik göz ardı edilmelidir.


Hesap genişletilmiş özel anahtarı, Wallet'nızı tamamen yeniden oluşturmak için kullanılabilir. Bununla birlikte, hesap genişletilmiş genel anahtarı, aynı Wallet'nın yalnızca sınırlı bir sürümünü üretebilir (Wallet'yı izleyerek) - Bu anahtarı Electrum'a koyarsanız, seed veya genişletilmiş özel anahtarın sahip olacağı 8,6 milyar adresin tamamını üretmeye devam edecektir, ancak Electrum için kullanılabilir özel anahtarlar olmayacaktır, bu nedenle harcama yapmak mümkün değildir. Konuyu göstermek için şimdi yapalım:


"Hesap genişletilmiş genel anahtarını" panoya kopyalayın.


Ardından Electrum'a gidin, yaptığımız mevcut Wallet'i açık bırakın ve file->new/restore'a gidin. Wallet'i yapma işlemi öncekinden biraz farklıdır:



- Standart Wallet
- Ana anahtar kullanın
- Genişletilmiş açık anahtarı kutuya yapıştırın ve devam edin
- passphrase girmenize gerek yok; bu zaten genişletilmiş genel anahtarın bir parçası
- Kod semantiğini ve türetme yolunu girmeye gerek yok
- Şifre eklemeye gerek yok (Wallet'i kilitler)


Wallet yüklendiğinde, daha önce seed girildiğinde yüklenen adreslerin tamamen aynı olduğunu fark etmelisiniz. Ayrıca başlık çubuğunun en üstünde "Wallet izleniyor" yazdığını da fark etmelisiniz. Bu Wallet size adreslerinizi ve bakiyelerinizi gösterebilir (bir düğüm aracılığıyla bakiyeleri kontrol ederek), ancak işlemleri İMZALAYAMAZSINIZ (çünkü izleyen Wallet'nin özel anahtarları yoktur).


O zaman ne anlamı var?


Bunun ana nedeni olmasa da bir nedeni, özel anahtarlarınızı bilgisayardaki herhangi bir kötü amaçlı yazılıma maruz bırakmadan Wallet'ünüzü ve bakiyesini potansiyel olarak bir bilgisayarda gözlemleyebilmenizdir.


Bir diğeri ise, özel anahtarlarınızı bilgisayar dışında tutmayı seçerseniz ödeme yapmak için GEREKLİ olmasıdır; açıklayacağım:


**Donanım cüzdanları (HWW)**, bir cihazın özel anahtarlarınızı güvenli bir şekilde tutabilmesi (PIN ile kilitli), anahtarları asla bir bilgisayara göstermemesi (bir bilgisayara kabloyla bağlı olsalar bile) ve kendilerinin internete bağlanamaması için oluşturulmuştur. Böyle bir cihaz kendi başına işlem yapamaz çünkü tüm Bitcoin işlemleri Blockchain (bir düğümde bulunan) üzerindeki bir UTXO(lar)a referans vererek başlar. Bir Wallet, UTXO'un hangi transaction ID'te olduğunu ve işlemin hangi çıktısının harcanacağını belirtmelidir. Yalnızca girdi belirtildikten sonra, imzalanmak bir yana, ilk etapta yeni bir işlem oluşturulabilir. Donanım cüzdanları işlem oluşturamaz çünkü herhangi bir UTXO'ya erişimleri yoktur - hiçbir şeye bağlı değildirler!


Genişletilmiş bir açık anahtar genellikle HWW'den çıkarılır ve adresler daha sonra bir bilgisayarda görüntülenir - birçok kişi bilgisayarlarında adresleri ve bakiyeleri gösteren Ledger yazılımına veya Trezor Suite'e aşina olacaktır - bu bir izleme Wallet'dir. Bu programlar işlem oluşturabilir, ancak imzalayamazlar. Yalnızca kendilerine bağlı olan HWW'ler tarafından imzalanmış işlemlere sahip olabilirler. HWW, yeni oluşturulan işlemi izleyen Wallet'den alır, imzalar ve ardından bir düğüme yayınlanması için bilgisayara geri gönderir. **HWW kendi başına yayın yapamaz**, bunu ilişkili izleyici Wallet yapar. Bu şekilde, iki cüzdan (bilgisayardaki açık anahtar Wallet ve HWW'deki özel anahtar Wallet) generate için işbirliği yapar, imzalar ve yayınlar, tüm bunları yaparken özel anahtarların izole ve internete bağlı bir cihazdan uzak kalmasını sağlar.


## Kısmen İmzalanmış Bitcoin İşlemleri (PSBT'ler)


Bir işlemin oluşturulması ve bir dosyaya kaydedilmesi, daha sonra yeniden yüklenmesi, imzalanması, kaydedilmesi, daha sonra yeniden yüklenmesi ve son olarak yayınlanması mümkündür - kimsenin bunu yapması gerektiğini söylemiyorum; bu sadece mümkün olan bir şey.


Şimdi 5 çoklu-imzalı Wallet'ün 3'ünü düşünün - 5 özel anahtar bir Wallet oluşturur ve bir işlemi tam olarak imzalamak için 3'ü gereklidir (Çoklu-imzalı Wallet anahtarları hakkında daha fazla bilgi edinmek için buraya bakın). Her biri beş özel anahtardan birine sahip 5 farklı bilgisayara sahip olmak mümkündür.


Birinci bilgisayar generate işlemini yapabilir ve imzalayabilir. Daha sonra bunu bir dosyaya kaydedebilir ve e-posta ile Bilgisayar 2'ye gönderebilir. Bilgisayar 2 daha sonra imzalayabilir ve dosyayı potansiyel olarak bir QR koduna kaydedebilir ve QR'yi bir Zoom çağrısı yoluyla dünyanın diğer tarafındaki Bilgisayar 3'e iletebilir. Bilgisayar 3 QR'yi yakalayabilir, işlemi electrum'a yükleyebilir ve işlemi imzalayabilir. İlk 2 imzadan sonra işlem bir PSBT (Partially Signed Bitcoin Transaction) olmuştur. 3. imzadan sonra işlem tamamen imzalanmış ve geçerli hale gelmiş, yayına hazır hale gelmiştir.


PSBTS hakkında daha fazla bilgi edinmek için bu kılavuza bakın. (https://armantheparman.com/PSBT/)


## Electrum ile Donanım Cüzdanlarını Kullanma


Genel olarak donanım cüzdanlarının kullanımına ilişkin, HWW'lere yeni başlayan kişilerin okumasının önemli olacağını düşündüğüm bir rehberim var. (https://armantheparman.com/using-hwws/)


Ayrıca burada Sparrow Bitcoin Wallet'e bağlanan çeşitli marka HWW'ler hakkında kılavuzlar bulunmaktadır. (https://armantheparman.com/hwws/)


Bu, Electrum ile bir Hardware Wallet'nin nasıl kullanılacağını gösteren ilk rehberim olacak - göstermek için ColdCard Hardware Wallet'yi kullanacağım. Bu, özellikle ColdCard hakkında ayrıntılı bir rehber olması anlamına gelmiyor, o rehber burada. Ben sadece Electrum'a özgü noktaları gösteriyorum. (https://armantheparman.com/cc/)


### Mikro SD kart üzerinden bağlanma (hava boşluklu)


Gerçek Wallet'ünüzü ColdCard üzerinden bağlamadan önce, umarım Electrum sahte Wallet'ü yükleme ve ağ parametrelerini ayarlama adımlarından geçmişsinizdir.


Ardından, ColdCard üzerinde SD kartı takın. seed'nızı zaten oluşturduğunuzu varsayıyorum. Wallet'e bir passphrase ile erişiyorsanız, şimdi uygulayın. Aşağı kaydırın ve Gelişmiş/Araçlar ->Wallet'i Dışa Aktar -> Electrum Wallet menüsünü seçin.


Aşağı kaydırıp mesajı okuyabilirsiniz. Sıfır olmayan bir hesap numarası (türetme yolunun bir parçası) girmek için her zaman "1 "i seçmenizi önerir, ancak tavsiyeme uyduysanız, varsayılan türetme yollarını karıştırmadınız, bu nedenle sıfır olmayan bir hesap numarası istemeyeceksiniz; devam etmek için onay işaretine basın.


Ardından komut dosyası semantiğini seçin. Çoğu kişi "Native SegWit" seçeneğini seçecektir.


"Electrum Wallet dosyası yazıldı" diyecek ve dosya adını görüntüleyecektir. Bunu zihninize not edin.


Ardından mikro SD kartı çıkarın ve Electrum ile bilgisayara takın.


Bazı işletim sistemleri, microSD'yi taktığınızda dosya gezginini otomatik olarak açacaktır. Birçok kişi yeni Wallet dosyasını görüp çift tıklayacak ve neden çalışmadığını merak edecektir. Bu harika bir tasarım değil. Aslında dosya gezginini görmezden gelmeli (kapatmalı) ve Electrum kullanarak Wallet dosyasını açmalısınız:


Electrum'u açın. Zaten başka bir Wallet ile açıksa, dosya -> yeni'yi seçin. Bu pencereyi arıyoruz:


![image](assets/52.webp)


İşte püf noktası, sezgisel değil. "Seç "e tıklayın. Ardından microSD karttaki dosya sisteminde gezinin ve Wallet dosyasını bulun ve açın.


Şimdi Hardware Wallet'nizin Wallet'ü izlemeye karşılık gelen kısmını açtınız. Güzel.


### USB kablosu ile bağlanma.


Bu yol daha kolay olmalı, ancak Linux bilgisayarlar için çok daha zor. "Udev kuralları" adı verilen bir şeyin güncellenmesi gerekiyor. İşte nasıl (ayrıntılı kılavuz https://armantheparman.com/gpg-articles/ ) ve kısaca:


Sistemin güncel olduğundan emin olmak iyi bir fikirdir. O halde:


```bash
sudo apt-get install libusb-1.0-0-dev libudev-dev
```


sonra.


```bash
python3 -m pip install ckcc-protocol
```


Eğer bir hata alırsanız pip'in kurulu olduğundan emin olun. (pip -version) ile kontrol edebilir ve (sudo apt install pythron3-pip) ile kurabilirsiniz


/etc/udev/rules.d/ dosyasını oluşturun veya mevcut dosyayı değiştirin


Bunun gibi:


```bash
sudo nano /etc/udev/rules.d
```


Bir metin düzenleyici açılacaktır. Metni buradan kopyalayın ve rules.d dosyasına yapıştırın, kaydedin ve çıkın.


![image](assets/53.webp)


Ardından bu komutları birbiri ardına çalıştırın:


```bash
sudo groupadd plugdev
sudo usermod -aG plugdev $(whoami)
sudo udevadm control –reload-rules && sudo udevadm trigger
```


Eğer "group plugdev" zaten var mesajı alırsanız, sorun değil, devam edin. İkinci komuttan sonra herhangi bir geri bildirim/cevap almayacaksınız, sadece üçüncü komuta geçin.


ColdCard'ın bilgisayarla bağlantısını kesmeniz ve ardından yeniden bağlamanız gerekebilir.


Tüm bunlardan sonra hala ColdCard'ı bağlayamıyorsanız, aygıt yazılımını güncellemeyi deneyin (yakında rehberlik edecek, ancak şimdilik üreticinin web sitesinde talimatları bulabilirsiniz).


Ardından, yeni bir Wallet oluşturun:



- Standart Wallet
- Bir donanım aygıtı kullanın
- ColdCard'ınızı tarayacak ve tespit edecektir. Devam edin.
- Kod semantiğini ve türetme yolunu seçin
- Wallet dosyasının şifrelenip şifrelenmeyeceğine karar verin (önerilir)


### ColdCard kullanılarak yapılan işlemler


Kablo bağlıyken işlemler kolaydır. İmzalama işlemleri sorunsuz olacaktır.


Cihazı hava bağlantılı bir şekilde kullanıyorsanız, kaydedilen işlemi microSD kartı kullanarak cihazlar arasında manuel olarak geçirmeniz gerekir. Bazı hileler var.


Bir işlem oluşturduktan ve sonlandırdıktan sonra, sol alt köşedeki dışa aktar düğmesine tıklamanız gerekir. Mantıksız bir şekilde istediğimiz şey olmayan "dosyaya kaydet" seçeneğini göreceksiniz. Aslında önce "donanım cüzdanları için" yazan en son menü seçeneğine gitmeniz ve ardından bu seçimden diğer "dosyaya kaydet" seçeneğini bulmanız ve bunu seçmeniz gerekir. Ardından dosyayı microSD'ye kaydedin, kartı çıkarın ve ColdCard'a yerleştirin. Doğru Wallet'i seçmek için bir passphrase uygulamanız gerekebileceğini unutmayın. Ekranda imzalamaya hazır yazacaktır. Onay işaretine tıklayın, işlemi inceleyin ve onay işaretiyle onaylayarak devam edin. İşiniz bittiğinde kartı çıkarın ve bilgisayara geri koyun.


Daha sonra işlemi electrum kullanarak açmamız gerekir. İşlev, araçlar -> işlem yükle menüsünde gizlidir. Dosya sisteminde gezinin ve dosyayı bulun. Her imzaladığınızda üç dosya olacaktır. Watching Wallet'un yaptığı orijinal kayıtlı dosya ve ColdCard tarafından yapılan iki dosya (bunu neden yaptığını bilmiyorum). Birinde "imzalandı" ve diğerinde "son" yazacak. Sezgisel değil ama "imzalı" olan kullanışlı değil, "son" işlemi açmamız gerekiyor.


Bunu yükledikten sonra, "yayınla" düğmesine tıklayabilirsiniz ve ödeme yapılacaktır.


## Electrum ve Gizli ".electrum" Dizininin Güncellenmesi


Electrum bilgisayarınızda iki yerde bulunur. Uygulamanın kendisi ve gizli bir yapılandırma klasörü vardır. Bu klasör işletim sisteminize bağlı olarak farklı yerlerde bulunur:


Pencereler:


```bash
C:/Users/your_user_name_goes_here/AppData/Roaming/Electrum
```


Mac:


```bash
/Users/your_user_name_goes_here/.electrum
```


Linux:


```bash
/home/your_user_name_goes_here/.electrum
```


Linux ve Mac'te `electrum'dan önce `.` olduğuna dikkat edin - bu, yönetmenin gizli olduğunu gösterir. Ayrıca, bu dizinin yalnızca Electrum'u ilk kez çalıştırdığınızda (otomatik olarak) oluşturulduğunu unutmayın. Dizin, electrum yapılandırma dosyasını ve ayrıca kaydettiğiniz tüm cüzdanları tutan dizini içerir.


Electrum programını bilgisayarınızdan silerseniz, onu da aktif olarak silmediğiniz sürece gizli dizin kalacaktır.


Electrum'u yükseltmek için, indirmek ve doğrulamak için başlangıçta anlattığım prosedürün aynısını uygulayacaksınız. Daha sonra bilgisayarınızda programın iki kopyası olacak ve ikisini de çalıştırabilirsiniz - her program kendi yapılandırması ve Wallet erişimi için aynı gizli electrum klasörüne erişecektir. Ana ünite, bağlanılacak varsayılan düğüm, diğer tercihler ve cüzdanlara erişim gibi kaydettiğimiz her şey kalacaktır çünkü bunların hepsi bu klasöre kaydedilmiştir.


### Electrum ve Cüzdanlarınızı başka bir bilgisayara taşıma


Bunu yapmak için, program dosyalarını bir USB sürücüye kopyalayabilir ve .electrum dizinini de kopyalayabilirsiniz. Ardından bunları yeni bilgisayara kopyalayın veya taşıyın. Programı tekrar doğrulamanıza gerek yoktur. .electrum dizinini varsayılan konuma kopyaladığınızdan emin olun (Electrum'u o bilgisayarda ilk kez çalıştırmadan ÖNCE kopyalamayı unutmayın, aksi takdirde boş bir varsayılan .electrum klasörü doldurulur ve kafanız karışabilir).


## Etiketler


Daha önce açıkladığım gibi, Address sekmesinde bir etiket sütunu vardır. Oraya çift tıklayabilir ve kendiniz için notlar girebilirsiniz (bu sadece sizin bilgisayarınızda olur, herkese açık değildir ve Blockchain'de de olmaz).


![image](assets/54.webp)


Electrum Wallet cihazınızı başka bir bilgisayara taşırken, tüm bu notları kaybetmek istemeyebilirsiniz. Wallet > etiketler > dışa aktar menüsünü kullanarak bunları bir dosyaya yedekleyebilir ve ardından yeni bilgisayarda Wallet > etiketler > içe aktar seçeneğini kullanabilirsiniz.


## İpuçları:


Bu kaynağı faydalı bulursanız ve Bitcoin için yaptıklarımı desteklemek isterseniz, buradan bir miktar Sats bağışlayabilirsiniz:


Statik Yıldırım Address: dandysack84@walletofsatoshi.com

https://armantheparman.com/electrum/