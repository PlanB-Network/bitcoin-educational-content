---
term: BIP0022
definition: Madencilik yazılımının bloklar oluşturmak için tam düğümlerle iletişim kurmasını sağlayan JSON-RPC getblocktemplate standardı.
---

Luke Dashjr tarafından 2012 yılında önerilen ve harici Mining arayüzleri için "getblocktemplate" adı verilen standartlaştırılmış bir JSON-RPC yöntemi sunan BIP. Mining zorluğundaki artışla birlikte, Proof of Work üretmek için özel harici yazılım kullanımı gelişmiştir. Bu BIP, tam düğümler ve Mining'de uzmanlaşmış yazılımlar arasında blok şablonu için ortak bir iletişim standardı önermektedir. Bu yöntem, Miner'nin özelleştirmesine izin vermek için sadece başlık yerine bloğun tüm yapısının gönderilmesini içerir.