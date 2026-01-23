---
term: Hesap
definition: Bir HD cüzdanda, anahtarların ve adreslerin hiyerarşik olarak organize edilmesine izin veren bir türev seviyesi (derinlik 3).
---

HD (Hiyerarşik Deterministik) cüzdanlarda, bir hesap BIP32'ye göre 3. derinlikte bir Layer türetimini temsil eder. Her hesap `/0'/` (sertleştirilmiş türetme, yani gerçekte `/2^31/` veya `/2 147 483 648/`)'den başlayarak sırayla numaralandırılır. Bu türetme derinliğinde iyi bilinen `xpub`lar bulunur. Günümüzde, bir HD Wallet içerisinde tipik olarak yalnızca bir hesap kullanılmaktadır. Ancak, başlangıçta, aynı Wallet içinde çeşitli kullanım kategorilerini ayırmak için tasarlanmışlardır. Örneğin, harici bir Taproot (P2TR) alımı Address için standart bir türetme yolu alırsak: `m/86'/0'/0'/0/0`, hesap dizini ikinci `/0'/`dir.


