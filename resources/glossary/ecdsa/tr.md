---
term: ECDSA
definition: Bitcoin'de işlemleri imzalamak için kullanılan Eliptik Eğri Dijital İmza Algoritması.
---

"Eliptik Eğri Dijital İmza Algoritması" için kısaltma Eliptik eğri kriptografisine (ECC) dayalı bir dijital imza algoritmasıdır. DSA'nın (Dijital İmza Algoritması) bir çeşididir. ECDSA, önemli ölçüde daha küçük anahtar boyutları kullanırken RSA gibi geleneksel açık anahtar algoritmalarıyla karşılaştırılabilir güvenlik seviyeleri sağlamak için eliptik eğrilerin özelliklerini kullanır. ECDSA, anahtar çiftlerinin (açık ve özel anahtarlar) oluşturulmasının yanı sıra dijital imzaların oluşturulmasına ve doğrulanmasına olanak tanır.


Bitcoin bağlamında ECDSA, özel anahtarlardan açık anahtarlar türetmek için kullanılır. Ayrıca, bitcoinlerin kilidini açmak ve onları harcamak için bir komut dosyasını karşılamak amacıyla işlemleri imzalamak için de kullanılır. Bitcoin'ın ECDSA'sında kullanılan eliptik eğri, $y^2 = x^3 + 7$ denklemiyle tanımlanan `secp256k1`dir. Bu algoritma Bitcoin'ın 2009'daki başlangıcından beri kullanılmaktadır. Günümüzde, 2021 yılında Taproot ile tanıtılan bir başka dijital imza algoritması olan Schnorr protokolü ile yerini paylaşmaktadır.