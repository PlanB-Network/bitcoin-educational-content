---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Bu özelliklerden herhangi birinin gözlemlenmesi durumunda işlemi geçersiz kılar:


- Yığın boş;
- Yığının en üstündeki değer `0`dan küçüktür;
- Yığının en üstündeki değer için devre dışı bırakma bayrağı tanımsızdır ve; İşlem sürümü `2`den küçüktür veya; Girişin `nSequence` alanı için devre dışı bırakma bayrağı ayarlanmıştır veya; Zaman kilidi türü `nSequence` alanı ile yığının en üstündeki değer arasında aynı değildir (gerçek zaman veya blok sayısı) veya; Yığının en üstündeki değer girişin `nSequence` alanının değerinden büyüktür.


Bu özelliklerden biri veya daha fazlası gözlemlenirse, `OP_CHECKSEQUENCEVERIFY` içeren kod tatmin edilemez. Tüm koşullar geçerliyse, `OP_CHECKSEQUENCEVERIFY` bir `OP_NOP` gibi davranır, yani kod üzerinde herhangi bir eylem gerçekleştirmez. Sanki ortadan kaybolmuş gibidir. böylece `OP_CHECKSEQUENCEVERIFY`, kendisini içeren kod ile güvence altına alınan UTXO'ın harcanmasına göreceli bir zaman kısıtlaması getirir. Bunu gerçek zaman şeklinde ya da blok sayısı olarak yapabilir. Bunu yapmak için, onu harcayan girdinin `nSequence` alanı için olası değerleri kısıtlar ve bu `nSequence` alanının kendisi, bu girdiyi içeren işlemin bir bloğa ne zaman dahil edilebileceğini kısıtlar.


> ► *Bu işlem kodu `OP_NOP` yerine kullanılır. OP_NOP3` üzerine yerleştirilmiştir. Genellikle "CSV" kısaltması ile anılır. Not: `OP_CSV` bir işlemin `nSequence` alanı ile karıştırılmamalıdır. Birincisi ikincisini kullanır, ancak doğaları ve eylemleri farklıdır.*