---
term: SHA512
definition: Türetmeler (derivations) için kullanılan, 512 bitlik bir özet üreten kriptografik hash fonksiyonu.
---

"*Secure Hash Algorithm 512 bits*" için kısaltma. 512 bitlik bir özet üreten bir kriptografik Hash işlevidir. 2000'li yılların başında *Ulusal Güvenlik Ajansı* (NSA) tarafından tasarlanmıştır. Bitcoin için, `SHA512` işlevi doğrudan protokol içinde kullanılmaz, ancak BIP32 ve BIP39'a göre uygulama düzeyinde alt anahtarların türetilmesi bağlamında kullanılır. Bu süreçlerde, `HMAC` algoritmasının yanı sıra `PBKDF2` anahtar türetme işlevinde birden çok kez kullanılır. SHA512` işlevi, `SHA256` gibi SHA 2 ailesinin bir parçasıdır. Çalışması ikincisine çok benzer.