---
term: ÖZEL ANAHTAR
---

Özel anahtar, asimetrik kriptografinin temel bir unsurudur. Kriptografik bir sırrı temsil eden bir sayıdır (Bitcoin bağlamında 256 bit). Bu anahtar, işlemleri dijital olarak imzalamak ve bir `scriptPubKey`i karşılayarak bir Bitcoin genel anahtarının Ownership'ını (ve buna bağlı olarak bir alıcı Address'i) kanıtlamak için kullanılır. Bu nedenle, özel anahtarlar ilgili açık anahtarla ilişkili UTXO'ların kilidini açarak bitcoin harcamaya izin verir. Özel anahtarlar, ifşa edilmeleri kötü niyetli üçüncü tarafların ilgili fonların kontrolünü ele geçirmesine olanak tanıyabileceğinden kesinlikle gizli tutulmalıdır.


Bitcoin sisteminde özel anahtar, eliptik eğriler (ECDSA veya Schnorr) kullanan bir dijital imza algoritması aracılığıyla bir açık anahtara bağlanır. Açık anahtar özel anahtardan türetilir, ancak altta yatan matematiksel problemi (ayrık logaritma problemi) çözmenin doğasında bulunan hesaplama zorluğu nedeniyle bunun tersini başarmak pratikte imkansızdır. Açık anahtar genellikle bir komut dosyası kullanarak bitcoinleri kilitlemek için kullanılan bir generate Bitcoin Address için kullanılır. Kriptografide özel anahtarlar genellikle rastgele ya da sözde rastgele sayılardır. Bitcoin deterministik ve hiyerarşik cüzdanların özel bağlamında, özel anahtarlar deterministik olarak seed'den türetilir. Özel anahtarlar sıklıkla seed ya da kurtarma ifadesiyle (Mnemonic) karıştırılmaktadır. Ancak bu Elements birbirinden farklıdır.


> ► *İngilizcede özel anahtara "private key" denir Bu terim bazen "privkey" veya "PV" olarak kısaltılır