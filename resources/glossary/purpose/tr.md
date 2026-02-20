---
term: Amaç
definition: HD cüzdanlarda kullanılan adres standardını belirleyen türetme seviyesi.
---

Deterministik ve hiyerarşik (HD) portföylerde, BIP43 tarafından tanımlanan amaç, belirli bir türetme seviyesini temsil eder. Türetme ağacının ilk derinliğinde (`m/amaç' /`) bulunan bu indeks, farklı portföy yönetim yazılımları arasında uyumluluğu kolaylaştırmak için portföy tarafından benimsenen türetme standardını tanımlar. Örneğin, SegWit adresleri (BIP84) söz konusu olduğunda, amaç `/84'/` olarak belirtilir. Bu yöntem, anahtarların tek bir HD portföyü içindeki farklı Address türleri arasında verimli bir şekilde organize edilmesini sağlar. Kullanılan standart indeksler şunlardır :




- P2PKH için: `44'` ;
- P2SH içinde yuvalanmış P2WPKH için: `49'` ;
- P2WPKH için: `84'` ;
- P2TR için: `86'`.