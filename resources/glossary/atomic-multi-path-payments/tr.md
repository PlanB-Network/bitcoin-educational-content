---
term: ATOMIK ÇOK YOLLU ÖDEMELER
---

MPP'nin (*Çok Yollu Ödemeler*) her ödeme parçasının farklı bir kısmi sırra sahip olduğu, işlemin atomik olarak, yani tam olarak veya hiç yapılmamasını sağlayan geliştirilmiş versiyonu.


MPP'ler, Lightning'de bir işlemin birkaç küçük parçaya bölünmesini ve farklı rotalar üzerinden yönlendirilmesini sağlayan ödeme teknikleridir. Başka bir deyişle, her ödeme parçası farklı bir düğüm yolunu izler. Bu, rotadaki tek bir kanal üzerindeki likidite sınırlamalarını ortadan kaldırır. Temel MPP'lerde her ödeme parçası aynı sırrı ve dolayısıyla HTLC'lerde aynı Hash'ı paylaşır. Bu durum, bir gözlemcinin birden fazla rotada bulunması halinde, tüm bu aynı sırları birbirine bağlayabileceğinden, işlemi izlenebilir hale getirebilir. Dahası, sır ödemenin tüm bölümleri için benzersiz olduğu için atomik değildir. Bu da ödemenin bazı kısımları başarıyla gerçekleştirilirken diğerlerinin başarısız olabileceği anlamına gelir.


AMP'de her bir fraksiyon için benzersiz kısmi sırlar kullanılır. Tüm parçalar alındığında, alıcının orijinal genel sırrı yeniden oluşturmasını ve ödemenin tamamını talep etmesini sağlarlar. Bu yöntem ödemenin kısmi olarak yapılmasını imkansız hale getirir, çünkü tam ödemenin kilidini açmak için tüm kısmi sırlara sahip olmak gerekir. Bu da ödemenin tamamen başarılı ya da tamamen başarısız (yani atomik) olmasını sağlar. AMP ayrıca farklı rotalar arasında artık görünür bağlantılar olmadığından gizliliği de artırır.


AMP'lerin bir avantajı, yalnızca alıcı ve gönderici bu yöntemi uygulamış olsa bile çalışmasıdır. Aracı düğümler, daha büyük bir ödemenin parçalarını işlediklerinin farkında olmadan, bu ödemeleri HTLC'leri kullanarak geleneksel işlemler olarak işler.