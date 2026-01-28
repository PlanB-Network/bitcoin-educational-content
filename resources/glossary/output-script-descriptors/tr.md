---
term: Çıktı betiği tanımlayıcıları
definition: Bir çıktı betiğini ve bir cüzdanı geri yüklemek için gereken bilgileri tanımlayan yapılandırılmış ifadeler.
---

Çıktı komut dosyası tanımlayıcıları veya kısaca tanımlayıcılar, bir çıktı komut dosyasını (`scriptPubKey`) tam olarak tanımlayan ve belirli bir komut dosyasına veya komut dosyasından yapılan işlemleri izlemek için gerekli tüm bilgileri sağlayan yapılandırılmış ifadelerdir. Bu tanımlayıcılar, kullanılan adreslerin yapısı ve türlerinin standart bir açıklaması aracılığıyla HD cüzdanlarındaki anahtarların yönetimini kolaylaştırır.


Tanımlayıcıların ana ilgi alanı, bir Wallet'ü geri yüklemek için gerekli tüm bilgileri tek bir dizede (kurtarma ifadesine ek olarak) kapsülleme yeteneklerinde yatmaktadır. Bir Descriptor'ı karşılık gelen Mnemonic cümleleriyle birlikte kaydederek, yalnızca özel anahtarları değil, aynı zamanda Wallet'ün kesin yapısını ve ilgili komut dosyası parametrelerini de geri yüklemek mümkündür. Aslında, bir Wallet'ün kurtarılması yalnızca ilk seed'in bilinmesini değil, aynı zamanda alt anahtar çiftlerinin türetilmesi için özel indekslerin yanı sıra bir Multisig Wallet durumunda her bir faktörün `xpub'ını da gerektirir. Önceden, bu bilgilerin herkes tarafından dolaylı olarak bilindiği varsayılıyordu. Ancak senaryoların çeşitlenmesi ve daha karmaşık konfigürasyonların ortaya çıkmasıyla birlikte bu bilgilerin tahmin edilmesi zorlaşabilir, dolayısıyla bu veriler özel ve Hard'ten Hard'e bilgi haline gelebilir. Tanımlayıcıların kullanımı süreci büyük ölçüde basitleştirir: her şeyi güvenilir ve emniyetli bir şekilde geri yüklemek için kurtarma ifadesini/ifadelerini ve ilgili Descriptor'ı bilmek yeterlidir.


Bir Descriptor birkaç Elements'den oluşur:


- Pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature) ve `sortedmulti` (Multisignature with sorted keys) gibi komut dosyası işlevleri;
- Türetme yolları, örneğin `[d34db33f/44h/0h/0h]` türetilmiş bir yolu ve belirli bir ana anahtar parmak izini gösterir;
- Onaltılık genel anahtarlar veya genişletilmiş genel anahtarlar (`xpub`) gibi çeşitli biçimlerdeki anahtarlar;
- Descriptor'in bütünlüğünü doğrulamak için Hash'den önce gelen bir sağlama toplamı.


Örneğin, bir P2WPKH Wallet için bir Descriptor şöyle görünebilir:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/#jy0l7n
r4
```

Bu Descriptor'de, `wpkh` türetme işlevi bir Pay-to-Witness-Public-Key-Hash kod türünü belirtir. Bunu, aşağıdakileri içeren türetme yolu takip eder:


- `cdeab12f`: ana anahtarın parmak izi;
- `84h`: SegWit v0 adresleri için tasarlanmış bir BIP84 amacının kullanıldığını gösterir;
- `0h`: bu da Mainnet'da bir BTC para birimi olduğunu gösterir;
- `0h`: Wallet'de kullanılan belirli hesap numarasını ifade eder.


Descriptor ayrıca bu Wallet'de kullanılan genişletilmiş açık anahtarı da içerir:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


Daha sonra, `/<0;1>/*` notasyonu Descriptor'ün generate adreslerini harici (`0`) ve dahili (`1`) zincirden, geleneksel Wallet yazılımında bir "boşluk sınırını" yönetmeye benzer şekilde yapılandırılabilir bir şekilde birden fazla adresin sıralı olarak türetilmesine izin veren bir joker karakter (`*`) ile türetebileceğini belirtir.


Son olarak, `#jy0l7nr4` Descriptor'nın bütünlüğünü doğrulamak için sağlama toplamını temsil eder.