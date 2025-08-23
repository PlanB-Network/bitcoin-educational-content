---
term: BIP0066
---

İşlemlerde imza formatının standartlaştırılması sağlandı. Bu BIP, OpenSSL'in farklı sistemler arasında imza kodlamasını ele alma biçimindeki farklılığa yanıt olarak önerilmiştir. Bu heterojenlik Blockchain'ı bölme riski oluşturuyordu. BIP66, katı DER kodlaması (*Ayırt Edici Kodlama Kuralları*) kullanarak tüm işlemler için imza formatını standartlaştırdı. Bu değişiklik bir Soft Fork gerektiriyordu. Etkinleştirilmesi için BIP66 daha sonra BIP34 ile aynı mekanizmayı kullandı, `nVersion` alanının sürüm 3'e yükseltilmesini gerektirdi ve %95 Miner eşiğine ulaşıldığında tüm sürüm 2 veya daha düşük blokları reddetti. Bu eşik 4 Temmuz 2015 tarihinde 363,725 numaralı blokta aşılmıştır.