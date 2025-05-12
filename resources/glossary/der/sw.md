---
term: DER
---

Kifupi cha *Kanuni Zilizojulikana za Usimbaji*. Ni sehemu ndogo ya sheria za usimbaji za ASN.1 zilizobainishwa katika vipimo [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) na hutumika kusimba aina yoyote ya data ya mfuatano wa mfumo wa jozi. DER hutumiwa hasa katika nyanja mahususi, kama vile kriptografia, ambapo data lazima isimbishwe kwa njia ya kawaida, inayotabirika.


Kwenye Bitcoin, sahihi za ECDSA husimbwa katika umbizo la DER. Zinajumuisha nambari mbili zilizosimbwa za baiti 32 (`r`,`s`). Umbizo la sahihi lina Elements ifuatayo (baiti 71):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Na:




- 0x30` (1 byte): kitambulisho cha muundo wa kiwanja;
- urefu` (baiti 1): urefu wa data ifuatayo ;
- 0x02` (baiti 1): aina ya kitambulisho cha data `INTEGER` (idadi kamili);
- `r-length` (baiti 1): urefu wa thamani `r` inayofuata (baiti 32);
- r` (baiti 32): thamani ya `r` kama nambari kamili ya mwisho;
- 0x02` (baiti 1): aina ya kitambulisho cha data `INTEGER` (idadi kamili);
- `s-urefu` (baiti 1): urefu wa thamani `s` inayofuata (baiti 32);
- `s` (baiti 32): `s` thamani kama nambari kamili ya mwisho.


Katika shughuli ya Bitcoin, byte huongezwa mwishoni mwa saini ya DER ili kuonyesha aina ya SigHash iliyotumiwa.