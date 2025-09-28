---
term: CHECKSUM
---

Sağlama toplamı, bir dizi veriden hesaplanan ve iletim veya depolama sırasında bu verilerin bütünlüğünü ve geçerliliğini doğrulamak için kullanılan bir değerdir. Sağlama toplamı algoritmaları, iletim hataları veya dosya bozulması gibi kazara oluşan hataları veya verilerdeki kasıtsız değişiklikleri tespit etmek için tasarlanmıştır. Eşlik kontrolleri, modüler sağlama toplamları, kriptografik Hash işlevleri veya BCH (*Bose, Ray-Chaudhuri ve Hocquenghem*) kodları gibi farklı türlerde sağlama toplamı algoritmaları mevcuttur.


Bitcoin'de, alıcı adreslerin bütünlüğünü sağlamak için uygulama düzeyinde sağlama toplamları kullanılır. Bir kullanıcının Address'inin yükünden bir sağlama toplamı hesaplanır, ardından girdisindeki herhangi bir hatayı tespit etmek için bu Address'e eklenir. Kurtarma cümlelerinde (anımsatıcılar) de bir sağlama toplamı bulunur.


> ► *Genel olarak İngilizce "checksum" teriminin doğrudan Fransızca'da kullanılması kabul edilmektedir*