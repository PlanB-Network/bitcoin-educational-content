---
term: SECP256K1
definition: Bitcoin'de ECDSA ve Schnorr dijital imzaları için kullanılan eliptik eğri.
---

ECDSA (*Elliptic Curve Digital Signature Algorithm*) ve Schnorr dijital imza algoritmalarının uygulanması için Bitcoin protokolünde kullanılan belirli bir eliptik eğriye verilen ad. Secp256k1` eğrisi Bitcoin'ın mucidi Satoshi Nakamoto tarafından seçilmiştir. Başta performans avantajları olmak üzere bazı ilginç özelliklere sahiptir.


Bitcoin'de `secp256k1` kullanımı, her bir özel anahtarın (rastgele 256 bitlik bir sayı), özel anahtarın noktasının `secp256k1` eğrisinin üreteç noktası ile toplanması ve iki katına çıkarılması yoluyla karşılık gelen bir açık anahtarla eşleştirildiği anlamına gelir. Bu işlemin tek yönde gerçekleştirilmesi kolaydır ancak tersine çevrilmesi neredeyse imkansızdır ve bu da Bitcoin'deki dijital imzaların güvenliğinin temelini oluşturur.


Secp256k1` eğrisi $y^2 = x^3 + 7$ eliptik eğri denklemiyle tanımlanır, yani $y^2 = x^3 + ax + b$ eliptik eğri denkleminin genel formunda $a$ katsayıları $0$'a ve $b$ katsayıları $7$'a eşittir. secp256k1`, mertebesi çok büyük bir asal sayı olan sonlu bir alan üzerinde tanımlanır, özellikle $p = 2^{256} - 2^{32} - 977$. Eğrinin ayrıca eğri üzerindeki farklı noktaların sayısı olan bir grup sırası, kriptografik işlemlerde generate anahtar çiftleri için kullanılan önceden tanımlanmış bir üreteç noktası (veya $G$ noktası) ve $1$'a eşit bir kofaktörü vardır.


> ► *"SEC", "Verimli Kriptografi Standartları" anlamına gelir. "P256" eğrinin $\mathbb{Z}_p$ alanı üzerinde tanımlandığını gösterir, burada $p$ 256 bitlik bir asal sayıdır. "K", mucidi Neal Koblitz'in adını ifade eder. Son olarak, "1" bunun bu eğrinin ilk versiyonu olduğunu gösterir.*