---
term: Derinlik
definition: Bir HD cüzdanın türetme yapısında, ana anahtardan (master key) itibaren bir anahtarın seviyesi.
---

HD (Hiyerarşik Deterministik) cüzdanlar bağlamında derinlik, Wallet'nin ana anahtardan türetme yapısındaki bir anahtarın (açık veya özel), bir chain code'ın, bir genişletilmiş anahtarın veya bir Address'in belirli bir seviyesini ifade eder. Bu yapının her bir seviyesi, ana anahtarın kökte (derinlik 0) olduğu ve sonraki seviyelerin aşağıdaki gibi çeşitli nitelikleri tanımladığı bir anahtar ağacındaki bir kat olarak görülebilir:

amaç (derinlik 1), para birimi türü (derinlik 2), hesap (derinlik 3), zincir türü (derinlik 4) ve belirli Address endeksi (derinlik 5).





Bir derinlikten diğerine geçmek için, bir çift ana anahtardan bir çift alt anahtara bir türetme işlemi kullanılır.


> ► *Bazen derinlik yerine "türetme tabanı" terimi de kullanılmaktadır*