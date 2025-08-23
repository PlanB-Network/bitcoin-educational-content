---
term: Address'I ALMAK
---

Bitcoin almak için kullanılan bilgiler. Bir Address genellikle `SHA256` ve `RIMPEMD160` kullanılarak bir açık anahtarın hash edilmesi ve bu özete meta veri eklenmesiyle oluşturulur. Alıcı Address'i oluşturmak için kullanılan açık anahtarlar kullanıcının Wallet'ünün bir parçasıdır ve bu nedenle seed'ünden türetilir. Örneğin, SegWit adresleri aşağıdaki bilgilerden oluşur:


- "Bitcoin "i belirlemek için bir HRP: "bc";
- Bir ayırıcı: `1`;
- Kullanılan SegWit sürümü: q` veya `p`;
- Yük: açık anahtarın özeti (veya Taproot durumunda doğrudan açık anahtar);
- Sağlama toplamı: bir BCH kodu.


Ancak, alıcı bir Address kullanılan komut dosyası modeline bağlı olarak başka bir şeyi de temsil edebilir. Örneğin, P2SH adresleri betiğin Hash'u kullanılarak oluşturulur. Öte yandan Taproot adresleri, değiştirilmiş açık anahtarı hash etmeden doğrudan içerir.


Bir alıcı Address alfanümerik bir dize şeklinde veya bir QR kodu olarak temsil edilebilir. Her bir Address birden fazla kez kullanılabilir, ancak bu kesinlikle tavsiye edilmeyen bir uygulamadır. Aslında, belirli bir gizlilik seviyesini korumak için, her Bitcoin Address'nin yalnızca bir kez kullanılması tavsiye edilir. Kişinin Wallet'ine gelen her ödeme için yeni bir Address oluşturulmalıdır. Bir Address, SegWit V0 adresleri için `Bech32`, SegWit V1 adresleri için `Bech32m` ve Eski adresler için `Base58check` ile kodlanır. Teknik açıdan bakıldığında, Bitcoin almak, bir açık anahtarla (ve dolayısıyla bir Address ile) ilişkili özel anahtara sahip olmak anlamına gelir. Birisi bitcoin aldığında, gönderici harcamaları üzerindeki mevcut kısıtlamayı günceller, böylece artık yalnızca alıcı bu güce sahip olabilir.


![](../../dictionnaire/assets/23.webp)