---
term: Türetme
definition: Bir HD cüzdanda, bir ebeveyn anahtar çiftinden çocuk anahtarlar oluşturma süreci.
---

Deterministik ve hiyerarşik (HD) bir Wallet içinde bir ana anahtar çiftinden (özel anahtar ve açık anahtar) ve bir chain code'dan çocuk anahtar çiftleri üretme sürecini ifade eder. Bu süreç, dalların bölümlere ayrılmasına ve bir Wallet'ün çok sayıda alt anahtar çiftine sahip farklı seviyelerde düzenlenmesine olanak tanır; bunların tümü yalnızca temel kurtarma bilgileri (Mnemonic ifadesi ve herhangi bir potansiyel passphrase) bilinerek kurtarılabilir. Bir alt anahtar türetmek için, `HMAC-SHA512` işlevi üst chain code ve üst anahtar ile 32 bitlik bir dizinin birleştirilmesiyle kullanılır. İki tür türetme vardır:


- Normal türetme, `HMAC-SHA512` işlevinin temeli olarak ana ortak anahtarı kullanır;
- Ana özel anahtarı `HMAC-SHA512` işlevinin temeli olarak kullanan güçlendirilmiş türetme;


HMAC-SHA512'nin sonucu ikiye bölünür: ilk 256 bit alt anahtar (ECDSA ile işlendikten sonra özel veya genel) ve kalan 256 bit alt chain code olur.