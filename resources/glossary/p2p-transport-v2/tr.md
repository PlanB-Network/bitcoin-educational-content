---
term: P2P TRANSPORT V2
definition: Gizliliği artırmak için şifreleme içeren yeni Bitcoin P2P protokolü sürümü.
---

Düğümler arasındaki iletişimin gizliliğini ve güvenliğini artırmak için fırsatçı şifrelemeyi içeren Bitcoin P2P taşıma protokolünün yeni sürümü. Bu iyileştirme, Address protokolünün temel sürümüyle ilgili çeşitli sorunları, özellikle de değiş tokuş edilen verileri pasif bir gözlemci (internet servis sağlayıcısı gibi) için ayırt edilemez hale getirerek, böylece veri paketlerindeki belirli modellerin algılanması yoluyla sansür ve saldırı risklerini azaltmayı amaçlamaktadır.


Uygulanan şifreleme, gereksiz karmaşıklık eklemekten kaçınmak ve ağ bağlantısının izinsiz doğasından ödün vermemek için kimlik doğrulamayı içermez. Bu yeni P2P aktarım protokolü yine de pasif saldırılara karşı daha iyi güvenlik sunmakta ve aktif saldırıları önemli ölçüde daha maliyetli ve tespit edilebilir hale getirmektedir (özellikle MITM saldırıları). Sözde rastgele veri akışının eklenmesi, iletişimi sansürlemek veya manipüle etmek isteyen saldırganların işini zorlaştırmaktadır.


P2P Transport V2, Aralık 2023'te dağıtılan Bitcoin core'in 26.0 sürümüne bir seçenek olarak (varsayılan olarak devre dışı) dahil edilmiştir. Yapılandırma dosyasındaki `v2transport=1` seçeneği ile etkinleştirilebilir.