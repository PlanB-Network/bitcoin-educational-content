---
term: pruned NODE
---

Bir pruned düğümü, İngilizce "pruned Node", Blockchain'in budamasını gerçekleştiren bir Full node'dir. Bu, en eski blokları usulüne uygun olarak doğruladıktan sonra, yalnızca en yeni blokları tutmak için aşamalı olarak kaldırmayı içerir. Saklama limiti `Bitcoin.conf` dosyasında `prune=n` parametresi aracılığıyla belirtilir, burada `n` megabayt (MB) cinsinden bloklar tarafından alınan maksimum boyuttur. Bu parametreden sonra `0` belirtilirse, budama devre dışı bırakılır ve düğüm Blockchain'i bütünüyle saklar.


pruned düğümleri bazen tam düğümlerden farklı düğüm türleri olarak kabul edilir. Bir pruned düğümünün kullanımı, depolama kapasitesi kısıtlamalarıyla karşı karşıya olan kullanıcılar için özellikle ilginç olabilir. Şu anda, bir Full node sadece Blockchain'i depolamak için neredeyse 600 GB'a sahip olmalıdır. Bir pruned düğümü gerekli depolama alanını 550 MB'a kadar sınırlayabilir. Daha az disk alanı kullanmasına rağmen, bir pruned düğümü Full node'nınkine benzer bir doğrulama ve onaylama seviyesini korur. Bu nedenle pruned düğümleri, hafif düğümlere (SPV) kıyasla kullanıcılarına daha fazla güven sunar.