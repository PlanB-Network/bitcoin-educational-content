---
term: BIP0061
definition: Düğümler arasında bir işlemin veya bloğun neden geçersiz olduğunu bildiren reddetme mesajı. Bitcoin Core 0.20.0'da kullanımdan kaldırıldı.
---

Düğümler arasındaki iletişim protokolüne bir ret mesajı eklenmiştir. BIP61'in amacı, bir düğüm başka bir düğümden geçersiz olduğunu düşündüğü bir işlem veya blok aldığında bir geri bildirim mekanizması eklemektir. Bu ret mesajı, bir düğümün göndericiye neden reddedildiğini bildirmesine olanak tanıyacaktır. Bu tür bir iletişimin, farklı istemciler arasında birlikte çalışabilirliği ve tam düğümler ile SPV istemcileri arasındaki iletişimi geliştirmesi amaçlanmıştır. BIP61 tarafından getirilen işlevler, artan bant genişliği ihtiyaçlarını içerdikleri halde gereksiz görüldükleri için sonunda Bitcoin core'ın 0.20.0 sürümünden itibaren terk edilmiştir.