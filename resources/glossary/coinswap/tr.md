---
term: COINSWAP
---

Kullanıcılar arasında Ownership'in gizli transferi için protokol. Bu yöntem, Exchange'nin Blockchain üzerinde açıkça görünmeden, bitcoinlerin sahipliğini bir kişiden diğerine veya tam tersi şekilde aktarmayı amaçlamaktadır. Coinwap, taraflar arasında güvene ihtiyaç duymadan transferi gerçekleştirmek için akıllı sözleşmeler kullanır.


Alice ve Bob ile naif bir örnek (işe yaramayan) hayal edelim. Alice, $A$ özel anahtarı ile güvence altına alınmış 1 BTC'ye sahiptir ve Bob da $B$ özel anahtarı ile güvence altına alınmış 1 BTC'ye sahiptir. Teorik olarak, gizli bir transfer gerçekleştirmek için harici bir iletişim kanalı aracılığıyla özel anahtarlarını Exchange yapabilirler. Ancak bu naif yöntem güven açısından yüksek risk taşır. Alice'in Exchange'ten sonra $A$ özel anahtarının bir kopyasını saklamasını ve anahtar Bob'nın eline geçtikten sonra bunu bitcoinleri çalmak için kullanmasını engelleyen hiçbir şey yoktur. Dahası, Alice'in Bob'nın özel anahtarı $B$'yi almayacağının ve Exchange'te kendi özel anahtarı $A$'yı asla aktarmayacağının hiçbir garantisi yoktur. Dolayısıyla bu Exchange taraflar arasında aşırı güvene dayanır ve Ownership'ün güvenli, gizli bir şekilde aktarılmasını sağlamada etkisizdir.


Bu sorunları çözmek ve birbirlerine güvenmeyen taraflar arasında para takasını mümkün kılmak için, Exchange'i "atomik" yapan Smart contract sistemlerini kullanacağız. Bunlar HTLC (*Hash Time-Locked Contracts*) veya PTLC (*Point Time-Locked Contracts*) olabilir. Bu iki protokol, Exchange'in ya başarıyla tamamlanmasını ya da tamamen iptal edilmesini sağlayan ve böylece her iki tarafın fonlarının bütünlüğünü koruyan bir zaman kilitleme sistemi kullanarak benzer şekilde çalışır. HTLC ve PTLC arasındaki temel fark, HTLC'un işlemi güvence altına almak için hash ve preimages kullanırken PTLC'nin Adaptor Signatures kullanmasıdır.


Alice ve Bob arasında bir HTLC veya PTLC kullanan bir coin takası senaryosunda, Exchange güvenli bir şekilde gerçekleşir: ya başarılı olur ve her biri diğerinin BTC'sini alır ya da başarısız olur ve her biri kendi BTC'sini tutar. Bu, taraflardan birinin hile yapmasını veya diğerinin BTC'sini çalmasını imkansız hale getirir.


Adaptör İmzalarının kullanımı bu bağlamda özellikle ilginçtir, çünkü geleneksel komut dosyalarından vazgeçmeyi mümkün kılar (bazen "_scriptless scripts_" olarak adlandırılan bir mekanizma). Bu da Exchange ile ilişkili maliyetleri azaltır. Adaptör İmzaların bir diğer önemli avantajı da işlemin her iki tarafı için ortak bir Hash kullanımını gerektirmemesi ve böylece belirli Exchange türlerinde aralarında doğrudan bir bağlantı ortaya koyma ihtiyacını ortadan kaldırmasıdır.