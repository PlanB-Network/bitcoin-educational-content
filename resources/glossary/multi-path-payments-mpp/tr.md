---
term: Çok yollu ödemeler (MPP)
definition: Bir ödemeyi farklı yollarla yönlendirilen birkaç parçaya bölen Lightning tekniği.
---

Lightning'de bir işlemin birkaç küçük parçaya bölünmesini ve farklı rotalar üzerinden yönlendirilmesini sağlayan tüm ödeme teknikleri için genel bir terim. Başka bir deyişle, her ödeme parçası farklı bir düğüm yolu izler. Bu, rotadaki tek bir kanaldaki likidite sınırlamalarını atlamayı mümkün kılar.


Çok yollu ödemeler gizlilik açısından da küçük avantajlar sunar, çünkü bir gözlemcinin her bir ödeme parçasını tüm işlemle ilişkilendirmesi daha zor hale gelir. Bununla birlikte, temel versiyonunda, tüm parçalar HTLC'ler için aynı sırrı paylaşır, bu da bir gözlemcinin birkaç rotada bulunması durumunda işlemi izlenebilir hale getirebilir. Dahası, sır ödemenin tüm parçaları için benzersiz olduğundan, atomik değildir. Bu da ödemenin bazı kısımları başarıyla gerçekleştirilirken diğer kısımlarının başarısız olabileceği anlamına gelir. Bu dezavantajlar "Atomic Multi-Path Payment" ile düzeltilmiştir.