---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
definition: Bir UTXO'nun harcanması üzerinde mutlak bir zaman kısıtlaması getiren işlem kodu.
---

Tüm bu koşullar karşılanmadığı sürece işlemi geçersiz kılar:


- Yığın boş değil;
- Yığının en üstündeki değer `0`dan büyük veya eşittir;
- Zaman kilidinin türü, `nLockTime` alanı ile yığının en üstündeki değer (gerçek zaman veya blok numarası) arasında aynıdır;
- Girdinin `nSequence` alanı `0xffffff` değerine eşit değil;
- Yığının en üstündeki değer, işlemin `nLockTime` alanının değerine eşit veya daha büyüktür.


Bu koşullardan herhangi biri karşılanmazsa, `OP_CHECKLOCKTIMEVERIFY` içeren kod tatmin edilemez. Tüm bu koşullar geçerliyse, `OP_CHECKLOCKTIMEVERIFY` bir `OP_NOP` gibi davranır, yani kod üzerinde herhangi bir işlem gerçekleştirmez. Sanki ortadan kaybolmuş gibidir. böylece `OP_CHECKLOCKTIMEVERIFY`, kendisini içeren kod ile güvence altına alınan UTXO'ın harcanmasına bir zaman kısıtlaması getirir. Bunu bir Unix zaman tarihi şeklinde ya da bir blok numarası olarak yapabilir. Bunu yapmak için, onu harcayan işlemin `nLockTime` alanı için olası değerleri kısıtlar ve bu `nLockTime` alanının kendisi işlemin bir bloğa ne zaman dahil edilebileceğini kısıtlar.


> ► *Bu işlem kodu `OP_NOP` yerine kullanılır. OP_NOP2` üzerine yerleştirilmiştir. Genellikle "CLTV" kısaltması ile anılır. Not: `OP_CLTV` bir işlemin `nLockTime` alanı ile karıştırılmamalıdır. Birincisi ikincisini kullanır, ancak doğaları ve eylemleri farklıdır.*