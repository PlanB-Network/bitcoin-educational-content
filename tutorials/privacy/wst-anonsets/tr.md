---
name: Whirlpool İstatistik Araçları - Anonsets
description: Anonset kavramını ve WST ile nasıl hesaplanacağını anlamak
---
![cover](assets/cover.webp)


***UYARI:** Samourai Wallet'ün kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, Samourai'nin Gitlab'ında barındırıldığı için Whirlpool İstatistik Aracı artık indirilemiyor. Bu aracı daha önce yerel olarak makinenize indirmiş olsanız veya RoninDojo düğümünüze yüklemiş olsanız bile, WST şu anda çalışmayacaktır. Çalışması için OXT.me tarafından sağlanan verilere dayanıyordu ve bu siteye artık erişilemiyor. Şu anda, Whirlpool protokolü etkin olmadığından WST özellikle kullanışlı değildir. Bununla birlikte, bu yazılımların önümüzdeki haftalarda eski haline getirilmesi mümkündür. Ayrıca, bu makalenin teorik kısmı, genel olarak eş birleşmelerin ilkelerini ve hedeflerini (sadece Whirlpool değil) anlamanın yanı sıra Whirlpool modelinin etkinliğini anlamak için de geçerliliğini korumaktadır. Ayrıca CoinJoin döngüleri tarafından sağlanan gizliliğin nasıl ölçüleceğini de öğrenebilirsiniz.*


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

> *Paralarınızın geride bıraktığı bağı kırın*

Bu eğitimde, CoinJoin üzerindeki bir Whirlpool sürecinin kalitesini tahmin etmemizi sağlayan göstergeler olan anonset kavramını inceleyeceğiz. Bu göstergelerin hesaplama ve yorumlama yöntemlerini ele alacağız. Teorik bölümün ardından, Python aracı *Whirlpool Stats Tools* (WST) kullanarak belirli bir işlemin anonsetlerini hesaplamayı öğrenerek uygulamaya geçeceğiz.


## Bitcoin üzerindeki CoinJoin nedir?

**CoinJoin, Blockchain** üzerindeki bitcoinlerin izlenebilirliğini kıran bir tekniktir. Aynı adı taşıyan belirli bir yapıya sahip işbirlikçi bir işleme dayanır: CoinJoin işlemi.


CoinJoin işlemleri, harici gözlemciler için zincir analizini zorlaştırarak Bitcoin kullanıcılarının gizliliğini artırır. Yapıları, farklı kullanıcılardan gelen birden fazla madeni paranın tek bir işlemde birleştirilmesine olanak tanıyarak izleri belirsizleştirir ve giriş ve çıkış adresleri arasındaki bağlantıların belirlenmesini zorlaştırır.


CoinJoin prensibi işbirlikçi bir yaklaşıma dayanır: bitcoinlerini karıştırmak isteyen birkaç kullanıcı aynı işlemin girdileri olarak aynı miktarları yatırır. Bu tutarlar daha sonra eşdeğer değerde çıktılar halinde yeniden dağıtılır. İşlemin sonunda, belirli bir çıktıyı belirli bir kullanıcıyla ilişkilendirmek imkansız hale gelir. Girdiler ve çıktılar arasında doğrudan bir bağlantı bulunmaz ve böylece kullanıcılar ile UTXO'leri ve her bir Coin'ün geçmişi arasındaki ilişki kopar.


![coinjoin](assets/notext/1.webp)


Bir CoinJoin işlemi örneği:

[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Her kullanıcının fonları üzerinde her zaman kontrol sahibi olmasını sağlarken bir CoinJoin gerçekleştirmek için süreç, işlemin bir koordinatör tarafından oluşturulması ve daha sonra her katılımcıya iletilmesiyle başlar. Her kullanıcı daha sonra işlemin kendisine uygun olduğunu doğruladıktan sonra imzalar. Toplanan tüm imzalar en sonunda işleme entegre edilir. Eğer bir kullanıcı ya da koordinatör tarafından CoinJoin işleminin çıktıları değiştirilerek fonların yönü değiştirilmeye çalışılırsa, imzalar geçersiz olacak ve işlemin düğümler tarafından reddedilmesine yol açacaktır.


CoinJoin'un Whirlpool, JoinMarket veya Wabisabi gibi, her biri katılımcılar arasındaki koordinasyonu yönetmeyi ve CoinJoin işlemlerinin verimliliğini artırmayı amaçlayan çeşitli uygulamaları vardır.

Bu eğitimde, benim favori uygulamama odaklanacağız: Samourai Wallet ve Sparrow wallet'de mevcut olan Whirlpool. Bana göre, Bitcoin'deki coinjoins için en verimli uygulama budur.


## CoinJoin'ün Bitcoin üzerindeki faydası nedir?


CoinJoin'nın faydası, Coin'nizi ayırt edilemeyen bir grup madeni para içinde boğarak makul inkar edilebilirlik üretme yeteneğinde yatmaktadır. Bu eylemin amacı, hem geçmişten günümüze hem de günümüzden geçmişe izlenebilirlik bağlantılarını kırmaktır.


Başka bir deyişle, CoinJoin döngülerinin girişindeki ilk işleminizi bilen bir analist, remiks döngülerinin çıkışındaki UTXO'unuzu kesin olarak belirleyememelidir (döngü girişinden döngü çıkışına kadar analiz).


![coinjoin](assets/en/2.webp)


Tersine, CoinJoin döngülerinin çıkışındaki UTXO'inizi bilen bir analist, döngülerin girişindeki orijinal işlemi belirleyememelidir (döngü çıkışından döngü girişine kadar analiz).


![coinjoin](assets/en/3.webp)


Bir analistin geçmişle günümüz arasında bağlantı kurmasının zorluğunu değerlendirmek için, Coin'nizin içinde gizlendiği grupların büyüklüğünü ölçmek gerekir. Bu ölçü bize aynı olasılığa sahip analizlerin sayısını söyler. Dolayısıyla, doğru analiz eşit olasılığa sahip diğer 3 analiz arasında boğulmuşsa, gizlenme düzeyiniz çok düşüktür. Öte yandan, doğru analiz, hepsi eşit olasılığa sahip 20.000 analizden oluşan bir kümenin içindeyse, Coin'niz çok iyi gizlenmiş demektir.


Ve tam olarak, bu grupların büyüklüğü "anonset" olarak adlandırılan göstergeleri temsil etmektedir.


## Anonsetleri anlama

Anonsetler, belirli bir UTXO'nın gizlilik derecesini değerlendirmek için gösterge görevi görür. Daha spesifik olarak, incelenen Coin'i içeren küme içindeki ayırt edilemeyen UTXO'ların sayısını ölçerler. Homojen bir UTXO kümesi gerekliliği, anonsetlerin genellikle CoinJoin döngüleri üzerinden hesaplandığı anlamına gelir. Bu göstergelerin kullanımı, homojenlikleri nedeniyle Whirlpool eş birleşimleri için özellikle önemlidir.


Anonsetler, uygun olduğu durumlarda, eş birleşimlerin kalitesinin değerlendirilmesine olanak tanır. Büyük bir anonset boyutu, set içindeki belirli bir UTXO'yi ayırt etmek zorlaştığından, daha yüksek bir anonimlik seviyesi anlamına gelir.


İki tür anons vardır:


- İleriye dönük anonimlik seti;**
- Geriye dönük anonimlik seti.**

İlk gösterge, incelenen UTXO'un döngünün sonunda gizlendiği grubun büyüklüğünü, girişteki UTXO'u bilerek, yani bu grupta bulunan ayırt edilemeyen madeni paraların sayısını gösterir. Bu gösterge, Coin'in gizliliğinin geçmişten günümüze (girişten çıkışa) bir analize karşı direncinin ölçülmesini sağlar. İngilizce'de bu göstergenin adı "*forward anonset*" ya da "*forward-looking metrics*"tir.

![coinjoin](assets/en/4.webp)


Bu metrik, UTXO'inizin CoinJoin sürecindeki giriş noktasından çıkış noktasına kadar olan geçmişini yeniden yapılandırma girişimlerine karşı ne ölçüde korunduğunu tahmin eder.


Örneğin, işleminiz ilk CoinJoin döngüsüne katıldıysa ve diğer iki alt döngü tamamlandıysa, Coin'ünüzün muhtemel anonseti `13` olacaktır:


![coinjoin](assets/en/5.webp)


İkinci gösterge, döngünün sonundaki UTXO'yı bilerek, belirli bir Coin için olası kaynakların sayısını gösterir. Bu gösterge Coin'in gizliliğinin günümüzden geçmişe (çıkıştan girişe) bir analize karşı direncini, yani bir analistin CoinJoin döngülerinden önce Coin'inizin kaynağına geri dönmesinin ne kadar zor olduğunu ölçer. İngilizce'de bu göstergenin adı "*backward anonset*" veya "*backward-looking metrics*"tir.


![coinjoin](assets/en/6.webp)


Döngülerin çıkışındaki UTXO'inizi bilen geriye dönük anonset, CoinJoin döngülerine girişinizi oluşturabilecek potansiyel Tx0 işlemlerinin sayısını belirler. Aşağıdaki diyagramda bu, tüm turuncu baloncukların toplamına karşılık gelmektedir.


![coinjoin](assets/en/7.webp)


## Whirlpool İstatistik Araçları (WST) ile anonsetlerin hesaplanması

Bu göstergeleri CoinJoin döngülerinden geçmiş kendi madeni paralarınız üzerinde hesaplamak için Samourai Wallet tarafından özel olarak geliştirilen bir aracı kullanabilirsiniz: *Whirlpool Stats Tools*.


Eğer bir RoninDojo'nuz varsa, WST düğümünüze önceden yüklenmiştir. Bu nedenle kurulum adımlarını atlayabilir ve doğrudan kullanım adımlarını takip edebilirsiniz. RoninDojo düğümüne sahip olmayanlar için, bu aracın bir bilgisayara kurulumuna nasıl devam edeceğimizi görelim.


İhtiyacınız olacak Tor Browser (veya Tor), Python 3.4.4 veya üstü, git ve pip. Bir terminal açın. Bu yazılımların sisteminizdeki varlığını ve sürümünü kontrol etmek için aşağıdaki komutları girin:

```plaintext
python --version
git --version
pip --version
```


Gerekirse, bunları ilgili web sitelerinden indirebilirsiniz:


- https://www.python.org/downloads/ (pip, 3.4 sürümünden beri doğrudan Python ile birlikte gelir);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.

Tüm bu yazılımlar kurulduktan sonra, bir terminalden WST deposunu klonlayın:

```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```


![WST](assets/notext/8.webp)


WST dizinine gidin:

```plaintext
cd whirlpool_stats
```


Bağımlılıkları yükleyin:

```plaintext
pip3 install -r ./requirements.txt
```


![WST](assets/notext/9.webp)


Bunları manuel olarak da yükleyebilirsiniz (isteğe bağlı):

```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```


`/whirlpool_stats` alt klasörüne gidin:

```plaintext
cd whirlpool_stats
```


WST'yi başlat:

```plaintext
python3 wst.py
```


![WST](assets/notext/10.webp)


Tor veya Tor Browser'ı arka planda başlatın.


**-> RoninDojo kullanıcıları için, eğitime doğrudan buradan devam edebilirsiniz.**


Proxy'yi Tor (RoninDojo) olarak ayarlayın,

```plaintext
socks5 127.0.0.1:9050
```


veya ne kullandığınıza bağlı olarak Tor Browser'a yönlendirebilirsiniz:

```plaintext
socks5 127.0.0.1:9150
```


Bu manipülasyon, işlemleriniz hakkında bilgi sızdırmamak için Tor aracılığıyla OXT'deki verileri indirmenize izin verecektir. Eğer acemiyseniz ve bu adım karmaşık görünüyorsa, bunun sadece internet trafiğinizi Tor üzerinden yönlendirmekten ibaret olduğunu bilin. En basit yöntem, bilgisayarınızda arka planda Tor Tarayıcısını başlatmak ve ardından bu tarayıcı üzerinden bağlanmak için yalnızca ikinci komutu çalıştırmaktan oluşur (`socks5 127.0.0.1:9150`).


![WST](assets/notext/11.webp)


Ardından, `workdir` komutunu kullanarak WST verilerini indirmeyi planladığınız çalışma dizinine gidin. Bu klasör, OXT'den alacağınız işlem verilerini `.csv` dosyaları şeklinde saklamaya yarayacaktır. Bu bilgiler, elde etmek istediğiniz göstergeleri hesaplamak için gereklidir. Bu dizinin konumunu seçmekte özgürsünüz. Özellikle WST verileri için bir klasör oluşturmak akıllıca olabilir. Örnek olarak, indirilenler klasörünü tercih edelim. RoninDojo kullanıyorsanız, bu adım gerekli değildir:

```plaintext
workdir path/to/your/directory
```


Komut istemi çalışma dizininizi gösterecek şekilde değişmiş olmalıdır.


![WST](assets/notext/12.webp)


Ardından işleminizi içeren havuzdan verileri indirin. Örneğin, eğer `100.000 Sats` havuzundaysam, komut şöyledir:

```plaintext
download 0001
```


![WST](assets/notext/13.webp)


WST üzerindeki mezhep kodları aşağıdaki gibidir:


- Havuz 0,5 bitcoin: `05`
- Havuz 0,05 bitcoin: `005`
- Havuz 0.01 bitcoins: `001`
- Havuz 0.001 bitcoins: `0001`

Veriler indirildikten sonra yükleyin. Örneğin, eğer `100.000 Sats` havuzundaysam, komut şöyledir:

```plaintext
load 0001
```


Bu adım bilgisayarınıza bağlı olarak birkaç dakika sürer. Şimdi kendinize bir kahve yapmak için iyi bir zaman! :)


![WST](assets/notext/14.webp)


Verileri yükledikten sonra, anonsetlerini almak için `score` komutunu ve ardından txid (işlem tanımlayıcınızı) yazın:

```plaintext
score TXID
```


**Dikkat:** Kullanılacak txid seçimi, hesaplamak istediğiniz anonsete bağlı olarak değişir. Bir Coin'nin ileriye dönük anonsetini değerlendirmek için, `score' komutu aracılığıyla, bu UTXO ile gerçekleştirilen ilk karışım olan ilk CoinJoin'ya karşılık gelen txid'u girmek gerekir. Öte yandan, geriye dönük anonseti belirlemek için, gerçekleştirilen son CoinJoin'nın txid'unu girmeniz gerekir. Özetlemek gerekirse, prospektif anonset ilk karışımın txid'undan hesaplanırken, retrospektif anonset son karışımın txid'undan hesaplanır.


WST daha sonra geriye dönük skoru (*Geriye dönük metrikler*) ve ileriye dönük skoru (*İleriye dönük metrikler*) görüntüler. Örneğin, bana ait olmayan Whirlpool üzerinde rastgele bir Coin'in txid'sini aldım.


![WST](assets/notext/15.webp)


Söz konusu işlem: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://Mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)


Bu işlemi ilgili Coin için gerçekleştirilen ilk CoinJoin olarak kabul edersek, o zaman `86,871`lik olası bir anonsetten yararlanır. Bu, `86,871` ayırt edilemeyen madeni para arasında gizlendiği anlamına gelir. CoinJoin döngülerinin başlangıcında bu Coin'i bilen ve çıktısını izlemeye çalışan harici bir gözlemci için, her biri aranan Coin olma olasılığı aynı olan `86.871` olası UTXO ile karşı karşıya kalacaktır.


Bu işlemi Coin'nin son CoinJoin'sı olarak kabul edersek, geriye dönük `42,185` anonsu vardır. Bu da bu UTXO için `42,185` potansiyel kaynak olduğu anlamına gelir. Dışarıdan bir gözlemci bu Coin'yi döngülerin sonunda tanımlar ve kaynağını izlemeye çalışırsa, hepsi de aranan kaynak olma olasılığı eşit olan `42.185` olası kaynakla karşı karşıya kalacaktır.

Anons puanlarına ek olarak, WST size anonsa dayalı olarak çıktınızın havuz içindeki yayılma oranını da sağlar. Bu diğer gösterge, eserinizin gelişme potansiyelini değerlendirmenize olanak tanır. Bu oran özellikle muhtemel anonset için kullanışlıdır. Gerçekten de, eğer eseriniz %15'lik bir yayılma oranına sahipse, bu havuzdaki eserlerin %15'i ile karıştırılabileceği anlamına gelir. Bu iyi bir şey, ancak remiks yapmaya devam ederek kendinizi geliştirmek için hala çok büyük bir marjınız var. Öte yandan, eğer parçanızın yayılma oranı %95 ise, o zaman havuzun sınırlarına yaklaşıyorsunuz demektir. Yeniden karıştırmaya devam edebilirsiniz, ancak anonsetiniz fazla artmayacaktır.


WST tarafından hesaplanan anonsetlerin tam olarak doğru olmadığına dikkat etmek önemlidir. İşlenmesi gereken büyük hacimli veriler göz önüne alındığında, WST yerel veri işleme ve gerekli bellekle ilgili yükü önemli ölçüde azaltmak için *HyperLogLogPlusPlus* algoritmasını kullanır. Bu, sonuçta yüksek doğruluğu korurken çok büyük veri kümelerindeki farklı değerlerin sayısını tahmin etmeyi sağlayan bir algoritmadır. Bu nedenle, sağlanan skorlar gerçeğe çok yakın tahminler olduğundan analizlerinizde kullanılmak için yeterince iyidir, ancak birimin kesin değerleri olarak yorumlanmamalıdır.


Sonuç olarak, eş birleşimlerde her bir parçanız için anonsetlerin sistematik olarak hesaplanmasının zorunlu olmadığını unutmayın. Whirlpool'un tasarımı zaten garanti sağlamaktadır. Gerçekten de, geriye dönük anonset nadiren bir endişe kaynağıdır. İlk karışımınızdan, Genesis CoinJoin'ten bu yana önceki karışımların mirası sayesinde özellikle yüksek bir retrospektif puan elde edersiniz. İleriye dönük anonsete gelince, parçanızı yeterince uzun bir süre boyunca post-mix hesabında tutmanız yeterlidir.


Bu nedenle Whirlpool kullanımının özellikle *HODL -> Karıştır -> Harca -> Değiştir* stratejisiyle ilgili olduğunu düşünüyorum. Bence en mantıklı yaklaşım, kişinin Bitcoin birikimlerinin büyük kısmını bir Cold Wallet'te tutarken, günlük harcamaları karşılamak için Samourai'deki coinjoin'lerde sürekli olarak belirli sayıda parça bulundurmaktır. Coinjoinlerdeki bitcoinler harcandığında, tanımlanan karışık parça eşiğine geri dönmek için yenileriyle değiştirilirler. Bu yöntem, kişinin UTXO anons setlerimizin endişesinden kurtulmasını sağlarken, coinjoins'in etkinliği için gerekli zamanı çok daha az kısıtlayıcı hale getirir.


**Harici Kaynaklar:**



- [Fransızca Podcast on chain analizi](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [HyperLogLog hakkındaki Wikipedia makalesi](https://en.wikipedia.org/wiki/HyperLogLog)
- Samourai'nin Whirlpool İstatistikleri için deposu
- Samourai tarafından hazırlanan Whirlpool web sitesi
- [Samourai'nin mahremiyet ve Bitcoin üzerine İngilizce Medium makalesi](https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Samourai tarafından belirlenen anonimlik kavramı üzerine İngilizce Medium makalesi](https://medium.com/samourai-Wallet/diving-head-first-into-Whirlpool-anonymity-sets-4156a54b0bc7)