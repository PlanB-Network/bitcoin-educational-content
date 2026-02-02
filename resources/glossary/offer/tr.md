---
term: Offer
definition: Lightning (BOLT12) üzerinden birden fazla ödeme almak için yeniden kullanılabilir statik QR kodları.
---

BOLT12'de *teklifler*, Lightning Network'da birden fazla ödeme yapmak için statik QR kodlarıdır. Geleneksel faturaların aksine, *teklifler* yeniden kullanılabilir. generate birden fazla Invoice talebi için kullanılabilirler. Bir kullanıcı *teklif* içeren bir QR kodunu taradığında, ilişkili Lightning düğümüne yeni bir Invoice talep eden bir mesaj gönderir. Düğüm, ödeyenin kullanabileceği bir Invoice ile yanıt verir. Böylece *teklifler*, Lightning'de farklı kullanıcılardan birden fazla ödeme almak için benzersiz bir tanımlayıcı sağlar.