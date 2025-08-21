---
term: BIP0072
---

Bitcoin URI (BIP21) uzantısını ek bir `r` parametresiyle tanımlayarak BIP70 ve BIP71'i tamamlar. Bu parametre, satıcının SSL sertifikası tarafından imzalanmış güvenli bir ödeme talebine bağlantı eklenmesini sağlar. Bir müşteri bu genişletilmiş URI'ye tıkladığında, Wallet ödeme ayrıntılarını istemek için satıcının sunucusuyla iletişime geçer. Bu ayrıntılar Wallet'nin işlem Interface'ında otomatik olarak doldurulur ve müşteri, imzalama sertifikasına karşılık gelen alan adı sahibine ödeme yaptığı konusunda bilgilendirilebilir (örneğin, "pandul.fr"). Bu geliştirme BIP70 ile birlikte sunulduğundan, hiçbir zaman yaygın olarak benimsenmemiştir.