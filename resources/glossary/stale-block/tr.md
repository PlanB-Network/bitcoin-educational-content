---
term: Eski (blok)
definition: İki madencinin aynı anda aynı yükseklikte bir blok bulması durumunda ana zincirin dışında kalan geçerli blok.
---

Çocukları olmayan bir bloğu ifade eder: geçerli bir bloktur, ancak ana Bitcoin zincirinden çıkarılmıştır. İki madenci kısa bir süre içinde aynı zincir yüksekliğinde geçerli bir blok bulduğunda ve bunu ağ üzerinden yayınladığında ortaya çıkar. Düğümler en sonunda, en çok birikmiş işe sahip zincir ilkesine göre zincire dahil etmek için yalnızca bir blok seçer ve diğerini "kullanılmaz" hale getirir. Eski bir bloğun üretilmesine yol açan süreç aşağıdaki gibidir:


- İki madenci kısa bir zaman aralığında aynı zincir yüksekliğinde geçerli bir blok bulur. Bunlara `Blok A` ve `Blok B` diyelim;
- Her biri kendi bloğunu Bitcoin düğüm ağına yayınlar. Artık her düğümün aynı yükseklikte 2 bloğu vardır. Bu nedenle, iki geçerli zincir vardır;
- Madenciler sonraki bloklar için çalışma kanıtlarını aramaya devam eder, ancak bunu yapmak için, üzerinde madencilik yapacakları `Blok A` ve `Blok B` arasında yalnızca bir blok seçmeleri gerekir;
- Bir Miner sonunda `Block B`nin üzerinde geçerli bir blok bulur. Buna `Blok B+1` diyelim;
- Ağ düğümlerine `Block B+1` yayınlarlar;
- Düğümler en uzun zinciri (en fazla birikmiş işle) takip ettiklerinden, `Zincir B`nin takip edilmesi gereken zincir olduğunu tahmin edeceklerdir;
- Artık ana zincirin bir parçası olmayan `Blok A`yı terk edeceklerdir. Böylece eski bir blok haline gelmiştir.





