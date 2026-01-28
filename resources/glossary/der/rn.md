---
term: DER
---

Inyuguti y'inyongera y'ikirundi *Amategeko y'Ikode Atandukanye*. Ni igice gikomeye c’amategeko yo gushiramwo amakuru ASN.1 asobanuwe mu vyo gusobanura [ITU-T X.690, 2002.](https://www.itu.int. DER ikoreshwa cane cane mu bikorwa vyihariye, nk’ubuhinga bwo gukingira amakuru, aho amakuru ategerezwa gushirwa mu buryo busanzwe, bushobora gutegekanirwa.


Ku Bitcoin, imikono ya ECDSA ishirwa mu buryo bwa DER. Bigizwe n'imibare ibiri ifise amabayiti 32 (`r`,`s`). Uburyo bw'umukono bugizwe n'ibi bikurikira Elements (71 bytes):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Hamwe :




- 0x30` (1 byte): ikimenyetso c'imiterere y'ibintu vyinshi;
- uburebure` (1 byte): uburebure bw'amakuru akurikira ;
- 0x02` (1 byte): ubwoko bw'ikimenyetso c'amakuru `INTEGER` (umubare wose) ;
- `r-uburebure` (byte 1): uburebure bw'agaciro ka `r` gakurikira (bayite 32) ;
- r` (32 bytes): agaciro ka `r` nk'umubare wose w'iherezo rinini;
- 0x02` (1 byte): ubwoko bw'ikimenyetso c'amakuru `INTEGER` (umubare wose) ;
- `s-uburebure` (byte 1): uburebure bw'agaciro ka `s` gakurikira (bayite 32) ;
- `s` (32 bytes): `s` agaciro nk'umubare munini w'iherezo.


Mu gukoresha Bitcoin, byte yongerwa ku mpera y'umukono wa DER kugira ngo yerekane ubwoko bwa SigHash ikoreshwa.