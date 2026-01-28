---
term: PBKDF2
definition: Yinelemeler yoluyla bir paroladan kriptografik anahtarlar türetme işlevi.
---

pBKDF2`, *Şifre Tabanlı Anahtar Türetme Fonksiyonu 2* anlamına gelir. Bir türetme işlevi kullanarak bir paroladan kriptografik anahtarlar oluşturmak için kullanılan bir yöntemdir. Girdi olarak bir parola, bir kriptografik tuz alır ve bu verilere önceden belirlenmiş bir işlevi (genellikle `SHA256` veya `HMAC` gibi bir Hash işlevi) yinelemeli olarak uygular. Bu işlem bir kriptografik anahtarı generate yapmak için birçok kez tekrarlanır.


Bitcoin bağlamında, `PBKDF2`, 12 veya 24 kelimelik bir kurtarma cümlesinden deterministik ve hiyerarşik bir Wallet'ün (seed) seed'ini oluşturmak için `HMAC-SHA512` işleviyle birlikte kullanılır. Bu durumda kullanılan kriptografik tuz BIP39 passphrase'dir ve yineleme sayısı `2048`dir.