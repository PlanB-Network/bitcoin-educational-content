---
name: RGB
description: RGB'de giriş ve varlık oluşturma
---

![RGB vs Ethereum](assets/0.webp)


## gİRİŞ


3 Ocak 2009'da Satoshi Nakamoto ilk Bitcoin düğümünü başlattı, o andan itibaren yeni düğümler katıldı ve Bitcoin sanki yeni bir yaşam biçimiymiş gibi davranmaya başladı, gelişmeyi durdurmayan bir yaşam biçimi, yavaş yavaş Satoshi tarafından çok iyi düşünülmüş benzersiz tasarımının bir sonucu olarak dünyanın en güvenli ağı haline geldi, çünkü ekonomik teşvikler yoluyla, genellikle madenci olarak adlandırılan kullanıcıları ağ güvenliğine katkıda bulunan enerji ve bilgi işlem gücüne yatırım yapmaya çekiyor.


Bitcoin büyümeye ve benimsenmeye devam ettikçe ölçeklenebilirlik sorunlarıyla karşı karşıya kalmaktadır, Bitcoin ağı yaklaşık 10 dakikalık bir sürede işlemlerin bulunduğu yeni bir bloğun çıkarılmasına izin vermektedir, blok başına maksimum 2700 işlem değeriyle bir günde 144 bloğumuz olduğunu varsayarsak, Bitcoin saniyede yalnızca 4,5 işleme izin verirdi, Satoshi bu sınırlamanın farkındaydı, bunu Mart 2011'de Mike Hearn'e gönderilen ve bugün bir ödeme kanalı olarak bildiğimiz şeyin nasıl çalıştığını açıkladığı bir e-postada1 görebiliriz. onayları beklemeden hızlı ve güvenli bir şekilde mikro ödemeler. İşte bu noktada off-chain protokolleri devreye giriyor.


Christian Decker'a2 göre off-chain protokolleri genellikle kullanıcıların bir Blockchain'deki verileri kullandığı ve son dakikaya kadar Blockchain'in kendisine dokunmadan yönettiği sistemlerdir. Bu konsepte dayanarak, Lightning Network, off-chain ödemelerinin neredeyse anında yapılmasına izin vermek için Bitcoin protokollerini kullanan ve tüm bu işlemler blok zincirine yazılmadığı için saniyede binlerce işleme izin veren ve Bitcoin'u ölçeklendiren bir ağ olarak doğdu.


Bitcoin üzerinde off-chain protokolleri alanındaki araştırma ve geliştirme bir pandora kutusu açtı, bugün merkezi olmayan bir şekilde değer aktarımından çok daha fazlasını başarabileceğimizi biliyoruz, kar amacı gütmeyen LNP/BP Standartları Derneği, Bitcoin ve Lightning Network üzerinde Layer 2 ve 3 protokollerinin geliştirilmesine odaklanıyor, bu projeler arasında RGB öne çıkıyor.


## RGB nedir?


RGB, Peter Todd3 tarafından 2016-2019 yıllarında Giacomo Zucco ve topluluk tarafından Bitcoin ve Lightning Network için daha iyi bir varlık protokolüne dönüştürülen tek kullanımlık mühürler ve istemci tarafı doğrulama üzerine yapılan araştırmadan ortaya çıkmıştır. Bu fikirlerin daha da geliştirilmesi, RGB'nin 2019'dan bu yana topluluk katılımıyla uygulanmasına liderlik eden Maxim Orlovsky tarafından tam teşekküllü bir Smart contract sistemine dönüştürülmesine yol açtı.


RGB'u, karmaşık akıllı sözleşmeleri ölçeklenebilir ve gizli bir şekilde yürütmemizi sağlayan bir dizi açık kaynak protokolü olarak tanımlayabiliriz. Belirli bir ağ değildir (Bitcoin veya Lightning gibi); her bir Smart contract, farklı iletişim kanalları (varsayılan olarak Lightning Network) kullanarak etkileşime girebilen bir dizi Contract katılımcısıdır. RGB, Bitcoin Blockchain'ü bir Layer durum Commitment'ü olarak kullanır ve Smart contract'nin kodunu ve off-chain verilerini korur, bu da onu ölçeklenebilir hale getirir, akıllı sözleşmeler için bir Ownership kontrol sistemi olarak Bitcoin işlemlerinden (ve Komut Dosyasından) yararlanır; Smart contract'nin gelişimi bir off-chain şeması tarafından tanımlanırken, son olarak her şeyin istemci tarafında doğrulandığını belirtmek önemlidir.


Basit bir ifadeyle, RGB, kullanıcının bir Smart contract'i denetlemesine, yürütmesine ve istediği zaman ek bir maliyet olmadan bireysel olarak doğrulamasına olanak tanıyan bir sistemdir, çünkü bunun için "geleneksel" sistemlerin yaptığı gibi bir Blockchain kullanmaz, karmaşık akıllı sözleşme sistemleri Ethereum tarafından öncülük edildi, ancak kullanıcının her işlem için önemli miktarda gaz harcamasını gerektirdiğinden, vaat ettikleri ölçeklenebilirliği asla elde edemediler, sonuç olarak mevcut finansal sistemden dışlanan kullanıcıları bankalamak için hiçbir zaman bir seçenek olmadı.


Şu anda Blockchain endüstrisi, hem akıllı sözleşmelerin kodunun hem de verilerin Blockchain'te depolanması ve boyuttaki aşırı artışa veya hesaplama kaynaklarının kötüye kullanılmasına bakılmaksızın ağın her bir düğümü tarafından yürütülmesi gerektiğini teşvik etmektedir. RGB tarafından önerilen şema, akıllı sözleşmeleri ve verileri Blockchain'ten ayırarak Blockchain paradigmasını kestiği ve böylece diğer platformlarda görülen ağın doygunluğunu önlediği için çok daha akıllı ve verimlidir, buna karşılık her düğümü her Contract'i yürütmeye zorlamaz, bunun yerine daha önce hiç görülmemiş bir seviyeye gizlilik katan ilgili taraflar.


![RGB vs Ethereum](assets/1.webp)


## RGB'de akıllı sözleşmeler


RGB'de Smart contract geliştiricisi, Contract'un zaman içinde nasıl geliştiğine dair kuralları belirten bir şema tanımlar. Şema, RGB'de akıllı sözleşmelerin oluşturulması için standarttır ve hem ihraç için bir Contract tanımlayan bir ihraççı hem de bir Wallet veya Exchange, Contract'u doğrulamaları gereken belirli bir şemaya uymalıdır. Yalnızca doğrulama doğruysa her iki taraf da talepleri kabul edebilir ve varlıkla çalışabilir.


RGB'deki bir Smart contract, grafiğin yalnızca bir kısmının her zaman bilindiği ve geri kalanına erişimin olmadığı durum değişikliklerinin bir Directed Acyclic Graph'üdür (DAG). RGB şeması, Smart contract'in başladığı bu grafiğin evrimi için temel bir kurallar kümesidir. Her bir Contract Participant bu kurallara ekleme yapabilir (Schema tarafından izin veriliyorsa) ve ortaya çıkan çizge bu kuralların yinelemeli olarak uygulanmasıyla oluşturulur.


## Değiştirilebilir varlıklar


RGB'deki değiştirilebilir varlıklar LNPBP RGB-20 spesifikasyonunu4 takip eder, bir RGB-20 tanımlandığında, "Genesis verileri'' olarak bilinen varlık verileri, varlığı kullanmak için gerekenleri içeren Lightning Network aracılığıyla dağıtılır. Varlıkların en temel şekli ikincil ihraca, token yakmaya, yeniden adlandırmaya veya değiştirmeye izin vermez.


Bazen ihraççının gelecekte daha fazla token, yani her bir token'in değerini USD gibi enflasyonist bir para biriminin değerine bağlı tutan USDT gibi sabit coinler ihraç etmesi gerekecektir. Bunu başarmak için daha karmaşık RGB-20 şemaları mevcuttur ve Genesis verilerine ek olarak, ihraççının Lightning Network'de de dolaşımda olacak sevkiyatlar üretmesini gerektirirler; bu bilgi ile varlığın toplam dolaşımdaki Supply'ünü bilebiliriz. Aynı durum varlıkların yakılması veya adının değiştirilmesi için de geçerlidir.


Varlıkla ilgili bilgiler kamuya açık veya özel olabilir: ihraççı gizlilik istiyorsa, token ile ilgili bilgileri paylaşmamayı ve işlemleri mutlak gizlilik içinde gerçekleştirmeyi seçebilir, ancak ihraççının ve sahiplerin tüm sürecin şeffaf olmasını istediği tersi bir durum da vardır. Bu, token verilerinin paylaşılmasıyla elde edilir.


## RGB-20 prosedürleri


Yakma prosedürü belirteçleri devre dışı bırakır, yakılan belirteçler artık kullanılamaz.


Değiştirme prosedürü, jetonlar yakıldığında ve aynı token'dan yeni bir miktar oluşturulduğunda gerçekleşir. Bu, varlığın hızını korumak için önemli olan varlığın geçmiş verilerinin boyutunu azaltmaya yardımcı olur.


Varlıkları değiştirmek zorunda kalmadan yakmanın mümkün olduğu kullanım durumunu desteklemek için, yalnızca varlıkların yakılmasına izin veren bir RGB-20 alt şeması kullanılır.


## Değiştirilebilir olmayan varlıklar


RGB'teki değiştirilemez varlıklar LNPBP RGB-21 spesifikasyonunu5 takip eder, NFT'lerle çalıştığımızda ayrıca bir ana şemamız ve bir alt şemamız vardır. Bu şemalar, token sahibinin bir parçası olarak özel veriler eklememize olanak tanıyan bir gravür prosedürüne sahiptir, bugün NFT'lerde gördüğümüz en yaygın örnek token ile bağlantılı dijital sanattır. token düzenleyicisi, RGB-21 alt şemasını kullanarak bu verilerin kazınmasını yasaklayabilir. Diğer NFT Blockchain sistemlerinden farklı olarak RGB, RGB'e özgü Smart contract işlevlerinin diğer birçok biçimini oluşturmak için de kullanılan Bifrost adlı Lightning P2P ağının uzantısını kullanarak büyük boyutlu medya token verilerini tamamen merkezi olmayan ve sansüre dirençli bir şekilde dağıtmaya olanak tanır.


Değiştirilebilir varlıklar ve NFT'lere ek olarak, RGB ve Bifrost, gelecek makalelerde ele alacağımız DEX'ler, likidite havuzları, algoritmik sabit coinler vb. dahil olmak üzere diğer akıllı sözleşme biçimlerini üretmek için kullanılabilir.


## RGB'den NFT ve diğer platformlardan NFT



- Pahalı Blockchain depolamaya gerek yok
- IPFS'ye gerek yoktur, bunun yerine bir Lightning Network uzantısı (Bifrost olarak adlandırılır) kullanılır (ve tamamen uçtan uca şifrelenir)
- Özel bir veri yönetimi çözümüne gerek yok - yine Bifrost bu rolü üstleniyor
- NFT tokenleri veya ihraç varlıkları / Contract ABI'leri hakkında veri tutmak için web sitelerine güvenmeye gerek yok
- Dahili DRM şifreleme ve Ownership yönetimi
- Lightning Network (Bifrost) kullanarak yedeklemeler için altyapı
- İçerikten para kazanma yolları (sadece NFT'nin kendisini satmak değil, içeriğe birkaç kez erişim)


## Sonuçlar


Yaklaşık 13 yıl önce Bitcoin'ün piyasaya sürülmesinden bu yana bu alanda çok sayıda araştırma ve deney yapıldı, hem başarılar hem de hatalar, merkezi olmayan sistemlerin pratikte nasıl davrandığını, onları gerçekten merkezi olmayan yapan şeyleri ve hangi eylemlerin onları merkezileşmeye götürme eğiliminde olduğunu biraz daha anlamamızı sağladı, tüm bunlar bizi gerçek ademi merkeziyetçiliğin nadir ve ulaşılması zor bir olgu olduğu sonucuna götürdü, gerçek ademi merkeziyetçilik yalnızca Bitcoin tarafından başarıldı ve bu nedenle çabalarımızı bunun üzerine inşa etmeye odaklıyoruz.


RGB, Bitcoin tavşan deliğinin içinde kendi tavşan deliğine sahiptir, ben onların içinden düşerken öğrendiklerimi yayınlayacağım, bir sonraki makalede LNP ve RGB düğümlerine ve bunların nasıl kullanılacağına bir giriş yapacağız.



- 1 https://plan99.net/~mike/Satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md


# RGB-node Eğitimi


## Giriş


Bu eğitimde, değiştirilebilir bir token oluşturmak için RGB-node'un nasıl kullanılacağını ve nasıl aktarılacağını açıklıyoruz, bu belge RGB-node demosuna dayanmaktadır ve bu eğitimin gerçek Testnet verilerini kullanması bakımından farklılık göstermektedir ve bunun için bundan sonra kendi Partially Signed Bitcoin Transaction, PSBT'mizi oluşturmalıyız.


## Gereksinimler


Bir Linux dağıtımının kullanılması tavsiye edilir, bu eğitim Ubuntu tabanlı Pop!OS kullanılarak yazılmıştır ve ihtiyacınız olacaktır:



- kargo
- Bitcoin core
- git


Not: Bu eğitimde komutların Linux terminalinde çalıştırılması gösterilmektedir, kullanıcının terminalde yazdıkları ile aldığı yanıtı birbirinden ayırmak için bash komut istemini simgeleyen $ işaretini ekliyoruz.


Bazı bağımlılıkları yüklemeniz gerekecektir:


```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```


İnşa Et ve Çalıştır


RGB-node devam eden bir çalışmadır (WIP), bu yüzden onu doğru bir şekilde derleyebilmek ve kullanabilmek için kendimizi belirli bir commit'te (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) konumlandırmalıyız, bunun için aşağıdaki komutları uyguluyoruz.


```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```


Şimdi derliyoruz, --locked bayrağını kullanmayı unutmayın çünkü clap'in bir sürümünde kırılma değişikliği var.


```
$ cargo install --path . --all-features --locked

....
....
Finished release [optimized] target(s) in 2m 14s
Installing /home/user/.cargo/bin/fungibled
Installing /home/user/.cargo/bin/rgb-cli
Installing /home/user/.cargo/bin/rgbd
Installing /home/user/.cargo/bin/stashd
Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```


Rust derleyicisinin bize söylediği gibi, ikili dosyalar $HOME/.cargo/bin dizinine kopyalanmıştır, eğer derleyiciniz onları farklı bir yere kopyaladıysa, bu dizinin $PATH'e dahil edildiğinden emin olmalısınız.


Yüklü ikili dosyalar arasında üç daemon veya servis (d ile biten dosyalar) ve bir CLI (komut satırı Interface) görebiliriz, CLI ana rgbd daemon ile etkileşime girmemizi sağlar. Bu derste iki düğüm çalıştıracağımız için, her biri kendi düğümüne bağlanması gereken iki istemciye de ihtiyacımız olacak, bunun için iki takma ad oluşturuyoruz.


```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```


Takma adları çalıştırabilir veya $HOME/.bashrc dosyasının sonuna ekleyebilir ve kaynak $HOME/.bashrc dosyasını çalıştırabiliriz.

Öncül


RGB-node, Wallet ile ilgili herhangi bir işlevi yerine getirmez, sadece Bitcoin core gibi harici bir Wallet tarafından sağlanacak veriler üzerinde RGB'ye özgü görevleri yerine getirir. Özellikle, ihraç ve transfer ile temel bir iş akışını göstermek için ihtiyacımız olacak:



- RGB-node-0'ın yeni ihraç edilen varlığı bağlayacağı bir issuance_utxo
- RGB-node-1'in varlığı aldığı bir receive_utxo
- RGB-node-0'ın varlık değişikliğini aldığı bir change_utxo
- Bir Partially Signed Bitcoin Transaction (tx.PSBT), çıktı açık anahtarı aktarıma bir Commitment eklemek için değiştirilecektir.


Bitcoin core CLI'ü kullanacağız, bitcoind daemon'nin Testnet üzerinde çalışmasını sağlamamız gerekiyor, bu bize birlikte çalışabilirlik sağlayacak ve sonunda kendi varlıklarımızı bu öğreticiyi izleyen diğer RGB kullanıcısına gönderebileceğiz.


Basitlik adına bu takma adı ~/.bashrc dosyamızın sonuna ekleyeceğiz.


```
alias bcli="bitcoin-cli -testnet"
```


Harcanmamış çıktı işlemlerimizi listeleyelim ve iki tane seçelim, biri issuance_utxo ve diğeri change_utxo olacak, hangisinin hangisi olduğu önemli değil, önemli olan ihraççının bu iki UTXO'in kontrolüne sahip olmasıdır.


```
$ bcli listunspent
[
{
"txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
"vout": 1,
"address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
"label": "",
"scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
"amount": 0.01703963,
"confirmations": 62432,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
"safe": true
},
{
"txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
"vout": 1,
"address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
"scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
"amount": 0.02877504,
"confirmations": 189184,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
"safe": true
}
]
```


Daha ileri gitmeden önce çıkış noktaları hakkında konuşmamız gerekir, tek bir işlem birden fazla çıkış içerebilir, çıkış noktası hem 32 baytlık bir txid hem de iki nokta üst üste : ile ayrılmış belirli bir çıkışa atıfta bulunmak için 4 baytlık bir çıkış indeks numarası (vout) içerir. Listunspent çıktımızda iki UTXO bulabiliriz, her birinde txid ve vout görebiliriz, bunlar issuance_utxo ve change_utxo çıkış noktalarıdır.


receive_utxo alıcı tarafından kontrol edilen bir UTXO'dir, bu durumda başka bir Wallet'den bir çıkış noktası olan e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0'ı kullanacağız.



- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0


Şimdi kısmen imzalanmış bir işlem (tx.PSBT) oluşturacağız, bu işlemin çıktısı transfer için bir taahhüt içerecek şekilde değiştirilecek, txid ve vout'u kendinizinkiyle değiştirmeyi unutmayın, hedef Address gerçekten önemli değil, sizin olabilir veya başka bir kişiden olabilir, bu Sats'in nereye gittiği önemli değil, önemli olan issuance_utxo kullanmamızdır.


```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
"psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
"fee": 0.00000280,
"changepos": 0
}
```


Çıktı bize tx.PSBT oluşturmak için kullanacağımız base64 kodlamasında bir PSBT verdi.


```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```


Her düğümün veri dizininin depolandığı rgbdata adında yeni bir dizin oluşturalım.


```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```


Zaten $HOME/rgbdata'da bulunan her düğümü farklı terminallerde başlatıyoruz, burada ~/.cargo/bin, kargonun RGB düğümü kurulumundan sonra tüm ikili dosyaları kopyaladığı dizindir.


```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```


## İhraç


Bir varlık ihraç etmek için rgb0-CLI'i fungible issue alt komutlarıyla çalıştırıyoruz, ardından argümanları, USDT ticker'ını, "USD Tether" adını ve tahsisatta ihraç miktarını ve aşağıda gördüğümüz gibi issuance_utxo'yu kullanacağız:


```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```


Varlık başarıyla verildi. Bu bilgiyi paylaşım için kullanın:

Varlık bilgisi:


```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"


genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```


Varlık kimliğini alıyoruz, varlığı aktarmak için buna ihtiyacımız var.


```
$ rgb0-cli fungible list

- name: USD Tether
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
```


## generate blinded UTXO


Yeni USDT'yi almak için, RGB-node-1'in varlığı tutmak için receive_utxo'ya karşılık gelen bir generate blinded UTXO'e ihtiyacı vardır.


```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```


Bu UTXO ile ilgili transferleri kabul edebilmek için orijinal receive_utxo ve blinding_factor'a ihtiyacımız olacak.


## Transfer


Varlığın bir miktarını RGB-node-1'e aktarmak için bunu blinded UTXO'e göndermemiz gerekir, RGB-node-0'ın bir Consignment ve bir açıklama oluşturması ve bunu bir Bitcoin işlemine işlemesi gerekir. Daha sonra, commit'i içerecek şekilde değiştireceğimiz bir PSBT'ye ihtiyacımız olacak. Ek olarak, -i ve -a seçenekleri, varlığın kaynağı olacak bir giriş çıkış noktası ve değişikliği alacağımız bir tahsisat sağlamamıza izin verir, bunu aşağıdaki şekilde belirtmeliyiz @<change_utxo>.


```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1

Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```


Bu üç yeni dosya yazacaktır, Consignment, açıklama ve ince ayar içeren PSBT, bu PSBT Witness Transaction olarak adlandırılır, Consignment RGB-node-1'e gönderilir.


## Tanık


Witness Transaction imzalanmalı ve yayınlanmalıdır, bunun için onu base64 kodlamamız gerekir.


```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```


Walletprocesspsbt alt komutu ile imzalayın.


```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
{
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
"complete": true
}
```


Şimdi son halini verin ve altıgeni alın.


```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="
{
"hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
"complete": true
}
```


## Yayın


Blockchain'e onaylatmak için sendrawtransaction alt komutunu kullanarak yayınlayın.


```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```


## Kabul et


Gelen bir aktarımı kabul etmek için RGB-düğüm-1, RGB-düğüm-0'dan Consignment dosyasını almış olmalı, receive_utxo ve ilgili blinding_factor, UTXO'nin körleştirilmesi sırasında üretilmiş olmalıdır.


```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Asset transfer successfully accepted.
```


Şimdi çalıştırarak <receive_utxo> içindeki 100 varlık biriminin yeni tahsisini (knownAllocations alanında) görebiliriz:


```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 1
outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
revealedAmount:
value: 100
blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```


Transfer yapıldığında receive_utxo blinded olduğundan, ödeyici RGB-node-0 100 USDT'nin nereye gönderildiği hakkında bilgi sahibi değildir, bu nedenle konum knownAllocations içinde gösterilmez.


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```


Ancak gördüğünüz gibi RGB-node-0, transfer komutuna -a bağımsız değişkeniyle sağladığımız 900 varlık değişikliğini göremiyor. Değişikliği kaydetmek için RGB-node-0'ın açıklamayı kabul etmesi gerekiyor.


```
$ rgb0-cli fungible enclose disclosure.rgb

Disclosure data successfully enclosed.
```


RGB-node-0 başarılı olduysa, varlığı listeleyerek değişikliği görebilirsiniz.


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 0
outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
revealedAmount:
value: 900
blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```


## Sonuçlar


Değiştirilebilir bir varlık yaratabildik ve bir işlemden diğerine özel bir şekilde taşıyabildik, bir Block explorer'te onaylanmış işlemi kontrol edersek, normal işlemden farklı bir şey bulamayız, bu, RGB'ün işlemleri değiştirmek için tek kullanımlık mühürler kullanması sayesinde, Bu yazıda, RGB'ün nasıl çalıştığına bir giriş yapıyorum.


Bu gönderide hatalar olabilir, bir şey bulursanız lütfen bu kılavuzu geliştirmek için bana bildirin, öneriler ve eleştirilere de açığız, mutlu hacklemeler! 🖖