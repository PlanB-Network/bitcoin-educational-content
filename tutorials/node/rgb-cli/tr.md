---
name: RGB CLI
description: RGB üzerinde nasıl Exchange akıllı sözleşmeleri oluşturabilirim?
---
![cover](assets/cover.webp)


Bu eğitimde, LNP/BP birliği tarafından oluşturulan `RGB` komut satırı aracını kullanarak bir Contract yazma sürecini adım adım takip edeceğiz. Amaç, CLI'in nasıl kurulacağını ve manipüle edileceğini, bir Schema'nin nasıl derleneceğini, Interface ve Interface Implementation'ün nasıl içe aktarılacağını ve ardından bir RGB varlığının nasıl yayınlanacağını göstermektir. Ayrıca derleme ve durum doğrulama dahil olmak üzere temel mantığa da bakacağız. Bu eğitimin sonunda, süreci yeniden üretebilmeli ve kendi RGB sözleşmelerinizi oluşturabilmelisiniz.


## RGB protokol hatırlatması


RGB, Bitcoin'nın üzerinde çalışan ve dayandığı Blockchain'e aşırı yük bindirmeden Smart contract işlevselliğini ve dijital varlık yönetimini taklit eden bir protokoldür. Geleneksel On-Chain akıllı sözleşmelerinin aksine (örneğin Ethereum'da olduğu gibi), RGB bir "*Client-side Validation*" sistemine dayanır: verilerin ve durum geçmişlerinin çoğu yalnızca ilgili katılımcılar tarafından değiş tokuş edilir ve saklanırken, Bitcoin Blockchain yalnızca küçük kriptografik taahhütleri barındırır (*Tapret* veya *Opret* gibi mekanizmalar aracılığıyla). RGB protokolünde, Bitcoin Blockchain bu nedenle yalnızca zaman damgası sunucusu ve Double-spending koruma sistemi olarak hizmet vermektedir.


Bir RGB Contract evrimsel bir durum makinesi gibi yapılandırılmıştır. Başlangıç durumunu (örneğin Supply, ticker veya diğer meta verileri tanımlayan) katı bir şekilde yazılmış ve derlenmiş bir Schema'ye göre tanımlayan bir Genesis ile başlar. Daha sonra bu durumu değiştirmek veya genişletmek için Durum Geçişleri ve gerekirse Durum Uzantıları uygulanır. İster değiştirilebilir varlıkların aktarılması (RGB20) ister benzersiz varlıkların oluşturulması (RGB21) olsun, her işlem *Tek kullanımlık Mühürler* içerir. Bunlar Bitcoin UTXO'ları off-chain durumlarına bağlar ve gizlilik ve ölçeklenebilirlik sağlarken çifte harcamayı önler.


RGB protokolünün nasıl çalıştığı hakkında daha fazla bilgi edinmek için bu kapsamlı eğitim kursuna katılmanızı tavsiye ederim:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

RGB'un iç mantığı, geliştiriciler olarak *Client-side Validation* kısmını yönetmek için projelerinize aktarabileceğiniz Rust kütüphanelerine dayanmaktadır. Buna ek olarak, LNP/BP ekibi diğer diller için bağlayıcılar üzerinde çalışmaktadır, ancak bu henüz sonuçlandırılmamıştır. Buna ek olarak, Bitfinex gibi diğer kuruluşlar da kendi entegrasyon yığınlarını geliştirmektedir, ancak bunlardan başka bir eğitimde bahsedeceğiz. Şimdilik, `RGB` CLI, nispeten cilasız kalsa bile resmi referanstır.


## RGB CLI aracının kurulumu ve sunumu


Ana komut basitçe `RGB` olarak adlandırılır. Sözleşmeleri manipüle etmek, onları çağırmak, varlık vermek vb. için bir dizi alt komutla `git`i anımsatacak şekilde tasarlanmıştır. Bitcoin Wallet şu anda entegre edilmemiştir, ancak yakın bir sürümde (0.11) olacaktır. Bu sonraki sürüm, kullanıcıların PSBT oluşturma, imzalama için harici donanımla (örneğin bir Hardware Wallet) uyumluluk ve Sparrow gibi yazılımlarla birlikte çalışabilirlik dahil olmak üzere cüzdanlarını (tanımlayıcılar aracılığıyla) doğrudan `RGB`den oluşturmalarını ve yönetmelerini sağlayacaktır. Bu, tüm varlık ihracı ve transfer senaryosunu basitleştirecektir.


### Kargo aracılığıyla kurulum


Aracı Rust ile yüklüyoruz:


```bash
cargo install rgb-contracts --all-features
```


(Not: sandık `RGB-contracts` olarak adlandırılır ve yüklenen komut `RGB` olarak adlandırılır. Eğer `RGB` adında bir sandık zaten mevcutsa, bir çakışma olmuş olabilir, bu nedenle bu isim verilmiştir)


Kurulum çok sayıda bağımlılığı derler (örneğin komut ayrıştırma, Electrum entegrasyonu, sıfır bilgi kanıtları yönetimi, vb.)


Kurulum tamamlandığında, :


```bash
rgb
```


RGB` (argümanlar olmadan) çalıştırıldığında `arayüzler`, `Schema`, `ithalat`, `ihracat`, `sorun`, `Invoice`, `aktarım` gibi mevcut alt komutların bir listesi görüntülenir. Yerel depolama dizinini (tüm günlükleri, şemaları ve uygulamaları tutan bir Stash) değiştirebilir, ağı (Testnet, Mainnet) seçebilir veya Electrum sunucunuzu yapılandırabilirsiniz.


![RGB-CLI](assets/fr/01.webp)


### Kontrollere ilk genel bakış


Aşağıdaki komutu çalıştırdığınızda, varsayılan olarak bir `RGB20` Interface'nın zaten entegre edilmiş olduğunu göreceksiniz:


```bash
rgb interfaces
```


Bu Interface entegre edilmemişse, :


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


Derle:


```bash
cargo run
```


Ardından seçtiğiniz Interface'i içe aktarın:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-CLI](assets/fr/02.webp)


Ancak, bize henüz hiçbir Schema'nin yazılıma aktarılmadığı söylendi. Stash'de bir Contract da yoktur. Bunu görmek için şu komutu çalıştırın :


```bash
rgb schemata
```


Daha sonra belirli şemaları almak için depoyu klonlayabilirsiniz:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-CLI](assets/fr/03.webp)


Bu depo, `src/` dizininde, şemaları tanımlayan birkaç Rust dosyası (örneğin `nia.rs`) içerir ("*Şişirilebilir Olmayan Varlık*" için NIA, "*Benzersiz Dijital Varlık*" için UDA, vb.) Derlemek için daha sonra :


```bash
cd rgb-schemata
cargo run
```


Bu, derlenen şemalara karşılık gelen birkaç `.RGB` ve `.rgba` dosyası oluşturur. Örneğin, `NonInflatableAsset.RGB` dosyasını bulacaksınız.


### Schema ve Interface Implementation'ün içe aktarılması


Artık şemayı `RGB` içine aktarabilirsiniz:


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-CLI](assets/fr/04.webp)


Bu, onu yerel Stash'e ekler. Aşağıdaki komutu çalıştırırsak, Schema'nin artık göründüğünü görürüz:


```bash
rgb schemata
```


## Contract oluşturma (yayınlama)


Yeni bir varlık oluşturmak için iki yaklaşım vardır:




- Ya Rust'te Schema alanlarını (Global State, Sahip Olunan Eyaletler, vb.) doldurarak bir Contract oluşturan ve bir `.RGB' veya `.rgba' dosyası üreten bir komut dosyası veya kod kullanırız;
- Veya token'in özelliklerini açıklayan bir YAML (veya TOML) dosyası ile doğrudan `issue` alt komutunu kullanın.


Rust'de `examples' klasöründe, bir `ContractBuilder'ı nasıl oluşturduğunuzu, `Global State'yı (varlık adı, ticker, Supply, tarih, vb.) nasıl doldurduğunuzu, Owned State'i (hangi UTXO'e atandığını) tanımladığınızı ve ardından tüm bunları bir Stash'e aktarabileceğiniz, doğrulayabileceğiniz ve içe aktarabileceğiniz bir *Contract Consignment* olarak derlediğinizi gösteren örnekler bulabilirsiniz.


Diğer yol ise `ticker`, `name`, `Supply` ve benzerlerini özelleştirmek için bir YAML dosyasını elle düzenlemektir. Dosyanın adının `RGB20-demo.yaml` olduğunu varsayalım. Belirtebilirsiniz :




- `spec`: ticker, name, precision ;
- `terms`: yasal bildirimler için bir alan;
- `issuedSupply` : ihraç edilen token miktarı;
- `assignments`: Single-Use Seal'yi (*Seal Definition*) ve kilidi açılmış miktarı gösterir.


İşte oluşturulacak bir YAML dosyası örneği:


```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```


![RGB-CLI](assets/fr/05.webp)


Ardından komutu çalıştırmanız yeterlidir:


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-CLI](assets/fr/06.webp)


Benim durumumda, benzersiz Schema tanımlayıcısı (tek tırnak içine alınacak) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` ve herhangi bir ihraççı koymadım. Yani benim siparişim :


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Schema ID'sini bilmiyorsanız, komutu çalıştırın:


```bash
rgb schemata
```


CLI yeni bir Contract'in yayınlandığını ve Stash'e eklendiğini yanıtlar. Aşağıdaki komutu yazarsak, artık yeni verilene karşılık gelen ek bir Contract olduğunu görürüz:


```bash
rgb contracts
```


![RGB-CLI](assets/fr/07.webp)


Ardından, bir sonraki komut global durumları (isim, ticker, Supply...) ve Sahip Olunan Durumların listesini, yani tahsisatları (örneğin, UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`de tanımlanan 1 milyon `PBN` jetonu) görüntüler.


```bash
rgb state '<ContractId>'
```


![RGB-CLI](assets/fr/08.webp)


## Dışa aktarma, içe aktarma ve doğrulama


Bu Contract'i diğer kullanıcılarla paylaşmak için, Stash'dan bir :


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-CLI](assets/fr/09.webp)


MyContractPBN.RGB` dosyası başka bir kullanıcıya verilebilir, o da komutla Stash'sine ekleyebilir:


```bash
rgb import myContractPBN.rgb
```


İçe aktarma sırasında, eğer basit bir *Contract Consignment* ise, "`Importing Consignment RGB`" mesajı alırız. Eğer daha büyük bir *State Transition Consignment* ise, komut farklı olacaktır (`RGB accept`).


Geçerliliği sağlamak için yerel doğrulama işlevini de kullanabilirsiniz. Örneğin, :


```bash
rgb validate myContract.rgb
```


### Stash kullanımı, doğrulama ve görüntüleme


Bir hatırlatma olarak, Stash şemaların, arayüzlerin, uygulamaların ve sözleşmelerin (Genesis + geçişler) yerel bir envanteridir. "Import" komutunu her çalıştırdığınızda, Stash'e bir öğe eklersiniz. Bu Stash şu komutla ayrıntılı olarak görüntülenebilir :


```bash
rgb dump
```


![RGB-CLI](assets/fr/10.webp)


Bu, generate'yı tüm Stash'nin ayrıntılarını içeren bir klasör haline getirecektir.


## Transfer ve PSBT


Bir transfer gerçekleştirmek için, `Tapret` veya `Opret` taahhütlerini yönetmek üzere yerel bir Bitcoin Wallet'ü manipüle etmeniz gerekecektir.


### generate an Invoice


Çoğu durumda, bir Contract'teki katılımcılar (örneğin Alice ve Bob) arasındaki etkileşim bir Invoice'ün oluşturulması yoluyla gerçekleşir. Alice, Bob'nin bir şey yürütmesini isterse (bir token aktarımı, bir yeniden düzenleme, bir DAO'da bir eylem, vb.), Alice, Bob'ye talimatlarını detaylandıran bir Invoice oluşturur. Yani elimizde :




- Alice** (Invoice'in ihraççısı) ;
- Bob** (Invoice'u alan ve uygulayan kişi).


Diğer ekosistemlerin aksine, bir RGB Invoice ödeme kavramıyla sınırlı değildir. Contract ile bağlantılı herhangi bir talebi içerebilir: bir anahtarı iptal etme, oylama, bir NFT üzerinde gravür (*gravür*) oluşturma vb. İlgili işlem Contract Interface'de tanımlanabilir. İlgili işlem Contract Interface'de açıklanabilir.


Aşağıdaki komut bir RGB Invoice oluşturur:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Ile :




- `$Contract`: Contract tanımlayıcısı (*ContractId*) ;
- `$Interface`: kullanılacak Interface (örneğin `RGB20`) ;
- `$ACTION`: Interface'de belirtilen işlemin adı (basit bir değiştirilebilir token transferi için bu "Transfer" olabilir). Interface zaten varsayılan bir eylem sağlıyorsa, bunu buraya tekrar girmenize gerek yoktur;
- `$STATE`: aktarılacak durum verisi (örneğin, değiştirilebilir bir token aktarılıyorsa bir miktar jeton);
- `$Seal`: faydalanıcının (Alice'nın) Single-Use Seal'ü, yani bir UTXO'e açık bir referans. Bob bu bilgiyi Witness Transaction'ü oluşturmak için kullanacaktır ve ilgili çıktı daha sonra Alice'ya ait olacaktır (*blinded UTXO* veya şifrelenmemiş biçimde).


Örneğin, aşağıdaki komutlarla


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI, generate ve Invoice gibi olacaktır:


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Herhangi bir kanal (metin, QR kodu vb.) aracılığıyla Bob'e iletilebilir.


### Transfer yapma


Bu Invoice'ten aktarmak için:




- Bob (tokenları Stash'inde tutan) bir Bitcoin Wallet'ye sahiptir. Gerekli RGB tokenlarının bulunduğu UTXO'ları ve para birimi (Exchange) için bir UTXO harcayan bir Bitcoin işlemi (PSBT şeklinde, örneğin `tx.PSBT`) hazırlaması gerekir;
- Bob aşağıdaki komutu yürütür:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Bu, . içeren bir `Consignment.RGB` dosyası oluşturur:
 - Alice'ya jetonların gerçek olduğunu kanıtlayan geçiş geçmişi;
 - Jetonları Alice'in Single-Use Seal'sine aktaran yeni geçiş;
 - Bir Witness Transaction (imzasız).
- Bob bu `Consignment.RGB` dosyasını Alice'e gönderir (e-posta, bir paylaşım sunucusu veya bir RGB-RPC protokolü, Storm, vb. ile);
- Alice, `Consignment.RGB`i alır ve kendi Stash'sinde kabul eder:


```bash
alice$ rgb accept consignment.rgb
```




- CLI geçişin geçerliliğini kontrol eder ve Alice'ın Stash'sine ekler. Geçersizse, komut ayrıntılı hata mesajlarıyla birlikte başarısız olur. Aksi takdirde başarılı olur ve örnek işlemin henüz Bitcoin ağında yayınlanmadığını bildirir (Bob, Alice'ın Green ışığını bekliyor);
- Onaylama yoluyla, `accept` komutu Alice'nın *Consignment*'i doğruladığını göstermek için Bob'ye gönderebileceği bir imza (*payslip*) döndürür;
- Bob daha sonra Bitcoin işlemini imzalayabilir ve yayınlayabilir (`--publish`):


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Bu işlem onaylanır onaylanmaz On-Chain, varlığın Ownership'inin Alice'e aktarıldığı kabul edilir. İşlemin Mining'ünü izleyen Alice'in Wallet'ü, yeni Owned State'in Stash'sında göründüğünü görür.


Artık bir RGB Contract'yi nasıl düzenleyeceğinizi ve aktaracağınızı biliyorsunuz. Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı koyarsanız çok minnettar olurum. Lütfen bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Ayrıca, RGB uyumlu bir Lightning düğümünün Exchange jetonlarına neredeyse anında nasıl başlatılacağını açıkladığım bu diğer öğreticiyi de tavsiye ederim:


https://planb.network/tutorials/node/others/rln-ffc02528-329b-4e16-bd83-873d0299feea