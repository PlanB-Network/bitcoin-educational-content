---
term: Ortalama tur süresi
definition: Bir madencilik havuzunun bir blok bulması için gereken ortalama zamanı, hesaplama gücü ve ağ zorluğu temelinde tahmin eden bir gösterge.
---

Ortalama tur süresi, ağın zorluğuna ve havuzun Hashrate'ine bağlı olarak bir Mining pool'ın bir blok bulması için gereken süreyi tahmin etmek için kullanılan bir göstergedir. Bir bloğu bulması beklenen hisse sayısı alınarak ve havuzun Hashrate'ine bölünerek hesaplanır. Örneğin, bir Mining pool'ın 200 madencisi varsa ve her biri saniyede ortalama 4 hisse üretiyorsa, havuzun toplam hesaplama gücü saniyede 800 hissedir:


```text
200 * 4 = 800
```


Geçerli bir blok bulmak için ortalama olarak 1 milyon paylaşım gerektiği varsayılırsa, havuzun *Avg. Tur Süresi* 1.250 saniye ya da yaklaşık 21 dakika olacaktır:


```text
1,000,000 / 800 = 1,250
```


Pratik açıdan bu, Mining pool'nin ortalama olarak her 21 dakikada bir blok bulması gerektiği anlamına gelir. Bu gösterge havuzun Hashrate'ündeki değişikliklerle dalgalanır: Hashrate'teki bir artış *Avg. Tur Süresini* azaltır, azalması ise uzatır. Ayrıca Bitcoin zorluk hedefinin her periyodik ayarlamasıyla (her 2016 blokta bir) dalgalanacaktır. Bu ölçüm, diğer havuzlar tarafından bulunan blokları dikkate almaz ve yalnızca incelenen havuzun iç performansına odaklanır.