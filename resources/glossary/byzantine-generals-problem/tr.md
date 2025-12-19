---
term: BİZANS GENERALLERİ SORUNU
---

Bu problem ilk olarak Leslie Lamport, Robert Shostak ve Marshall Pease tarafından Temmuz 1982'de *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) adlı özel dergide formüle edilmiştir. Günümüzde, dağıtık bir sistem herhangi bir aktöre güvenemediğinde karar verme açısından karşılaşılan zorlukları göstermek için kullanılmaktadır.


Bu metaforda, bir grup Bizanslı general ve orduları, saldırmak veya kuşatmak istedikleri bir şehrin etrafında kamp kurmuşlardır. Generaller coğrafi olarak birbirlerinden ayrıdır ve stratejilerini koordine etmek için haberci aracılığıyla iletişim kurmaları gerekir. Tüm generaller fikir birliğine vardığı sürece saldırmaları ya da geri çekilmeleri önemli değildir.


Bu nedenle, aşağıdaki gereklilikleri göz önünde bulundurabiliriz:


- Her general bir karar vermelidir: saldırmak ya da geri çekilmek (evet ya da hayır);
- Karar bir kez verildikten sonra değiştirilemez;
- Tüm generaller aynı karar üzerinde hemfikir olmalı ve bunu eşzamanlı olarak uygulamalıdır.


Dahası, bir general bir başkasıyla ancak bir kurye tarafından iletilen mesajlar aracılığıyla iletişim kurabilir ve bu mesajlar gecikebilir, yok edilebilir, değiştirilebilir ya da kaybolabilir. Ve bir mesaj başarıyla iletilse bile, bir veya daha fazla general (herhangi bir nedenle) kurulan güvene ihanet etmeyi ve sahte bir mesaj göndermeyi seçebilir ve kaos tohumları ekebilir.


İkilemi Bitcoin Blockchain bağlamına uygularsak, her bir genel ağdaki bir düğümü temsil eder ve sistemin durumu hakkında bir uzlaşmaya varması gerekir. Başka bir deyişle, dağıtılmış bir ağdaki katılımcıların çoğunluğu, toplam başarısızlığı önlemek için aynı eylemi kabul etmeli ve yürütmelidir. Bu tür bir dağıtık sistemde fikir birliğine varmanın tek yolu, ağ düğümlerinin en az 2/3'ünün güvenilir ve dürüst olmasıdır. Bu nedenle, ağın çoğunluğu kötü niyetli davranmaya karar verirse, sistem savunmasız kalır.


> ► *Bu ikilem bazen "Güvenilir Yayın Sorunu" olarak da adlandırılmaktadır*