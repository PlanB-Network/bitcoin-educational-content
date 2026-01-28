---
term: Silent payments
definition: Adres yeniden kullanımı olmadan statik bir adres üzerinden ödeme alma yöntemi.
---

Address yeniden kullanılmadan, etkileşim olmadan ve farklı ödemeler ile statik Address arasında görünür bir On-Chain bağlantısı olmadan ödeme almak için statik Bitcoin adreslerini kullanma yöntemi. Bu teknik, her işlem için yeni, kullanılmayan alıcı adresleri generate ihtiyacını ortadan kaldırır, böylece alıcının ödeme yapana yeni bir Address sağlaması gereken Bitcoin'teki olağan etkileşimlerden kaçınır.


Sessiz Ödemelerde, ödeyici alıcının açık anahtarlarını (harcama açık anahtarı ve tarama açık anahtarı) ve kendi özel anahtarlarının toplamını generate'ya girdi olarak kullanır ve her ödeme için yeni bir Address oluşturur. Yalnızca alıcı, kendi özel anahtarları ile bu ödeme Address'ye karşılık gelen özel anahtarı hesaplayabilir. Bir kriptografik anahtar Exchange algoritması olan ECDH (*Elliptic-Curve Diffie-Hellman*), daha sonra alıcı Address'yi ve özel anahtarı (yalnızca alıcı tarafında) türetmek için kullanılan ortak bir sır oluşturmak için kullanılır. Alıcılar, kendilerine yönelik Sessiz Ödemeleri belirlemek için Blockchain'ü taramalı ve protokol kriterlerine uyan her işlemi incelemelidir. Ödeme kanalını kurmak için bir bildirim işlemi kullanan BIP47'nin aksine, Sessiz Ödemeler bu adımı ortadan kaldırarak bir işlem tasarrufu sağlar. Bununla birlikte, alıcının ECDH uygulayarak kendisine yönelik olup olmadığını belirlemek için tüm potansiyel işlemleri taraması gerekir.


Örneğin, Bob'un statik Address $B$'si tarama açık anahtarı ile harcama açık anahtarının birleşimini temsil eder:


$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{harcama}} $$


Bu anahtarlar basitçe aşağıdaki yoldan türetilir:


```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```


Bu statik Address, Bob tarafından yayınlanır. Alice, Bob'ye Sessiz Ödeme yapmak için bunu alır. Bob'nin Address $P_0$ ödemesini bu şekilde hesaplar:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$


Nerede?


$$ \text{inputHash} = \text{Hash}(\text{outpoint}_L \text{ ‖ } A) $$


Ile:


- $B_{\text{scan}}$: Bob'nın tarama açık anahtarı (statik Address);
- $B_{\text{spend}}$: Bob'in harcama açık anahtarı (statik Address);
- $A$: Girdideki açık anahtarların toplamı (tweak);
- $a$: İnce ayarın özel anahtarı, yani Alice'un işleminde girdi olarak tüketilen UTXO'ların `scriptPubKey'inde kullanılan tüm anahtar çiftlerinin toplamı;
- $\text{outpoint}_L$: Alice'nin işleminde girdi olarak kullanılan en küçük UTXO (lexicographically);
- $\text{ ‖ }$: Birleştirme (işlenenleri uç uca ekleme işlemi);
- $G$: Secp256k1 eliptik eğrisinin jeneratör noktası;
- $\text{Hash}$: SHA256 Hash işlevi `BIP0352/SharedSecret` ile etiketlenmiştir;
- $P_0$: Bob'e ödeme için ilk açık anahtar / benzersiz Address;
- $0$: generate çoklu benzersiz ödeme adresleri için kullanılan bir tamsayı.


Bob, Sessiz Ödemesini bu şekilde bulmak için Blockchain'yı tarar:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$


Ile:


- $b_{\text{scan}}$: Bob'un özel tarama anahtarı.


Eğer $P_0$'ı kendisine gönderilmiş bir Sessiz Ödeme içeren bir Address olarak bulursa, Alice tarafından $P_0$'a gönderilen fonları harcamasını sağlayan özel anahtar olan $p_0$'ı hesaplar:


$$ p_0 = (b_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$


Ile:


- $b_{\text{spend}}$: Bob'ün özel harcama anahtarı;
- n$: `secp256k1` eliptik eğrisinin mertebesi.


Bu temel versiyona ek olarak, etiketler aynı temel statik Address'ten generate birkaç farklı statik adres için de kullanılabilir; bunun amacı, tarama sırasında gereken işi makul olmayan bir şekilde çoğaltmadan birden fazla kullanımı ayırmaktır.