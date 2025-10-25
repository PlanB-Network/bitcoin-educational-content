---
term: HİSSELER
---

Mining havuzları bağlamında pay, bireysel bir Miner'nin havuz içindeki katkısını ölçmek için kullanılan bir göstergedir. Bu ölçü, havuzun her bir Miner'ye yeniden dağıttığı ödülün hesaplanmasında temel teşkil eder. Her bir pay, Bitcoin ağınınkinden daha düşük bir zorluk hedefini karşılayan bir Hash'e karşılık gelir.


Bir benzetme ile açıklamak gerekirse, 20 yüzlü bir zar düşünün. Bitcoin'da, Proof of Work'ün bir bloğu doğrulamak için 3'ten daha düşük bir sayı atmayı gerektirdiğini (yani 1 veya 2 sonucuna ulaşmayı) varsayalım. Şimdi, bir Mining pool içinde, bir paylaşım için zorluk hedefinin 10 olarak belirlendiğini düşünün. Böylece, havuzdaki tek bir Miner için, 10'dan düşük bir sayı ile sonuçlanan her zar atışı geçerli bir paylaşım olarak sayılır. Bu paylaşımlar daha sonra Bitcoin'daki bir blok için geçerli bir sonuca karşılık gelmese bile, ödüllerini talep etmek için Miner tarafından havuza iletilir.


Hesaplanan her bir Hash için, bir havuzdaki bireysel bir Miner üç farklı senaryo ile karşılaşabilir:


- Hash değeri havuzun bir paylaşım için belirlediği zorluk hedefine eşit veya daha büyükse, bu Hash işe yaramaz. Miner daha sonra yeni bir Hash denemek için Nonce'lerini değiştirir: `Hash > share > block`.
- Hash, paylaşımın zorluk hedefinden düşük ancak Bitcoin'ün zorluk hedefinden büyük veya eşitse, bu Hash geçerli bir paylaşım oluşturur, ancak bir bloğu doğrulamak için yeterli değildir. Miner bu Hash'i kendi havuzuna göndererek paylaşımla ilişkili ödülü talep edebilir: `share > Hash > block`.
- Hash, Bitcoin ağının zorluk hedefinden düşükse, hem geçerli bir paylaşım hem de geçerli bir blok olarak kabul edilir. Miner bu Hash'i kendi havuzuna iletir, havuz da bunu Bitcoin ağında yayınlamak için acele eder. Bu Hash aynı zamanda Miner için geçerli bir paylaşım olarak sayılır: `share > bloc > Hash`.


![](../../dictionnaire/assets/32.webp)


Bu paylaşım sistemi, bir Miner tarafından üretilen tüm karmaları ayrı ayrı yeniden hesaplamak zorunda kalmadan, bir havuzdaki her bir Miner tarafından yapılan işi tahmin etmek için kullanılır, bu da havuz için tamamen verimsiz olacaktır.


Mining havuzları doğrulama yükünü dengelemek için paylaşımların zorluğunu ayarlar ve küçük ya da büyük her Miner'nin yaklaşık birkaç saniyede bir paylaşım göndermesini sağlar. Bu, her bir Miner'nin Hashrate'sinin doğru bir şekilde hesaplanmasına ve seçilen tazminat hesaplama yöntemine (PPS, PPLNS, TIDES...) göre ödüllerin dağıtılmasına olanak tanır.


> ► *Fransızca'da "shares" kelimesi "part" olarak çevrilebilir*