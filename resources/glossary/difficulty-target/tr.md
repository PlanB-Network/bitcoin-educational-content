---
term: Zorluk hedefi
definition: Blok başlıklarının hashlenmesi için kabul edilebilirlik sınırını belirleyen 256 bitlik sayısal değer.
---

Zorluk hedefi olarak da bilinen zorluk faktörü, Bitcoin üzerinde Proof of Work (Proof of Work, PoW) tarafından mutabakat mekanizmasında kullanılan bir parametredir. Hedef, madencilerin Blockchain üzerinde yeni bir blok oluştururken Proof of Work adı verilen belirli bir kriptografik problemi çözme zorluğunu belirleyen sayısal bir değeri temsil eder.


Zorluk hedefi, blok başlıklarının hashlenmesi için kabul edilebilirlik sınırını belirleyen ayarlanabilir 256 bitlik (64 bayt) bir sayıdır. Başka bir deyişle, bir bloğun geçerli olması için, `SHA256d` (çift `SHA256`) ile başlığının Hash'sı sayısal olarak zorluk hedefinden düşük veya eşit olmalıdır. Proof of Work, blok başlığının `Nonce` alanının veya Coinbase Transaction`ün, sonuçta elde edilen Hash hedef değerden düşük olana kadar değiştirilmesinden oluşur.


Bu hedef her 2016 blokta bir (yaklaşık iki haftada bir), "ayarlama" adı verilen bir etkinlik sırasında ayarlanır Zorluk faktörü, önceki 2016 bloklarının madenciliğinin ne kadar sürdüğüne bağlı olarak yeniden hesaplanır. Eğer toplam süre iki haftadan az ise, hedef aşağı doğru ayarlanarak zorluk derecesi artırılır. Toplam süre iki haftadan fazlaysa, hedef yukarı doğru ayarlanarak zorluk derecesi azaltılır. Amaç, blok başına ortalama 10 dakikalık bir Mining süresini korumaktır. Her blok arasındaki bu süre, Bitcoin ağının bölünmesini önlemeye yardımcı olur ve bu da hesaplama gücünün boşa harcanmasına neden olur. Zorluk hedefi her blok başlığında `nBits` alanı içinde bulunur. Bu alan 32 bite indirildiğinden ve hedef aslında 256 bit olduğundan, hedef daha az kesin bir bilimsel formata sıkıştırılmıştır.





> ► *Zorluk hedefi bazen "zorluk faktörü" olarak da adlandırılır.* Uzantı olarak, blok başlıklarındaki kodlamasıyla "nBits" terimiyle ifade edilebilir