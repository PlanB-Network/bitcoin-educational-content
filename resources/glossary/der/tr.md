---
term: DER
---

Ayırt Edici Kodlama Kuralları* için kısaltma. ITU-T X.690, 2002.] (https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) spesifikasyonunda tanımlanan ASN.1 kodlama kurallarının katı bir alt kümesidir ve her tür veriyi ikili bir dizide kodlamak için kullanılır. DER temel olarak verilerin standart, öngörülebilir bir şekilde kodlanması gereken kriptografi gibi belirli alanlarda kullanılır.


Bitcoin'de ECDSA imzaları DER biçiminde kodlanır. İki adet 32 baytlık kodlanmış sayıdan (`r`,`s`) oluşurlar. İmza biçimi aşağıdaki Elements'dan (71 bayt) oluşur:


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Ile :




- 0x30` (1 bayt): bir bileşik yapının tanımlayıcısı;
- length` (1 bayt): aşağıdaki verinin uzunluğu ;
- 0x02` (1 bayt): veri tanımlayıcı tipi `INTEGER` (tamsayı) ;
- r-length` (1 bayt): bir sonraki `r` değerinin uzunluğu (32 bayt) ;
- r` (32 bayt): big-endian tamsayı olarak `r` değeri;
- 0x02` (1 bayt): veri tanımlayıcı tipi `INTEGER` (tamsayı) ;
- s-length` (1 bayt): bir sonraki `s` değerinin uzunluğu (32 bayt) ;
- s` (32 bayt): big-endian tamsayı olarak `s` değeri.


Bir Bitcoin işleminde, kullanılan SigHash türünü belirtmek için DER imzasının sonuna bir bayt eklenir.