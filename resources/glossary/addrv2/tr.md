---
term: Addrv2
definition: Bitcoin düğüm adreslerinin yayınlanmasına izin veren yeni bir ağ iletisi biçimi (BIP155). Tor v3 veya I2P gibi daha uzun adresleri destekler.
---

Bitcoin ağındaki `addr` mesajının BIP155 ile önerilen evrimi. Addr` mesajı, gelen bağlantıları kabul eden düğüm adreslerini yayınlamak için kullanılıyordu, ancak 128 bit adreslerle sınırlıydı. Bu boyut IPv6, IPv4 ve Tor V2 adresleri için yeterliydi, ancak diğer protokoller için yetersizdi. Güncellenen `addrv2` sürümü, 256 bit Tor v3 gizli hizmetleri de dahil olmak üzere daha uzun adreslerin yanı sıra I2P gibi diğer ağ protokollerini veya gelecekteki protokolleri desteklemek üzere tasarlanmıştır.