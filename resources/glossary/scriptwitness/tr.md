---
term: SCRIPTWITNESS
---

SegWit işlem girdilerinde, işlemde gönderilen bitcoinlerin kilidini açmak için gerekli imzaları ve genel anahtarları içeren bir öğe. Legacy işlemlerindeki `scriptSig`e benzer şekilde, `scriptWitness` aynı konumda yer almaz. Aslında, "tanık" (İngilizce'de `*witness*`) olarak adlandırılan bu kısım, işlemin değiştirilebilirlik sorununu çözmek için ayrı bir veritabanına taşınmıştır. Her SegWit girdisinin kendi `scriptWitness`ı vardır ve tüm `scriptWitness` Elements birlikte işlemin `Witness` alanını oluşturur.


> ► *`scriptWitness` ile `witnessScript`i karıştırmamaya dikkat edin. ScriptWitness` herhangi bir SegWit girdisi için tanık verilerini içerirken, `witnessScript` bir P2WSH veya P2SH-P2WSH UTXO'in harcama koşullarını tanımlar ve bir P2SH çıktısı için `redeemscript`ye benzer şekilde kendi başına bir komut dosyası oluşturur.*