---
term: VÄLJUNDSKRIPTI KIRJELDAJAD

---
Väljundskriptide kirjeldajad ehk lihtsalt kirjeldajad on struktureeritud väljendid, mis kirjeldavad täielikult väljundskripti (`scriptPubKey`) ja annavad kogu vajaliku teabe, et jälgida tehinguid konkreetsesse skriptini või konkreetsest skriptist. Need kirjeldajad hõlbustavad võtmete haldamist HD rahakottides struktuuri ja kasutatavate aadresside tüüpide standardse kirjelduse kaudu.

Deskriptorite peamine huvi seisneb selles, et nad suudavad kapseldada kogu rahakoti taastamiseks vajaliku teabe ühte stringi (lisaks taastamislausele). Salvestades deskriptori koos vastavate mnemofraasidega, on võimalik taastada mitte ainult privaatvõtmed, vaid ka rahakoti täpne struktuur ja sellega seotud skriptiparameetrid. Rahakoti taastamine nõuab tõepoolest mitte ainult algseemne teadmist, vaid ka konkreetseid indekseid lapsvõtmepaaride tuletamiseks, samuti iga teguri `xpub` multisig rahakoti puhul. Varem eeldati, et see teave on kõigile kaudselt teada. Kuid skriptide mitmekesistumise ja keerukamate konfiguratsioonide tekkimise tõttu võib seda teavet olla raske ekstrapoleerida, muutes need andmed seega privaatseks ja raskesti brutaalseks teabeks. Deskriptorite kasutamine lihtsustab protsessi oluliselt: piisab taastamislause(te) ja vastava(te) deskriptori(de) teadmisest, et kõik usaldusväärselt ja turvaliselt taastada.

Deskriptor koosneb mitmest elemendist:


- Skriptifunktsioonid nagu `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature) ja `sortedmulti` (Multisignature koos sorteeritud võtmetega);
- Tuletatud teed, näiteks `[d34db33f/44h/0h/0h]`, mis näitab tuletatud teed ja konkreetset peavõti sõrmejälge;
- Võtmed erinevates vormingutes, nagu näiteks heksadekmelised avalikud võtmed või laiendatud avalikud võtmed (`xpub`);
- Kontrollsumma, millele eelneb hash, kirjelduse terviklikkuse kontrollimiseks.

Näiteks P2WPKH rahakoti kirjeldus võiks olla järgmine:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

Selles kirjelduses tähistab tuletamisfunktsioon "wpkh" Pay-to-Witness-Public-Key-Hash skripti tüüpi. Sellele järgneb tuletamise tee, mis sisaldab:


- `cdeab12f`: peavõti sõrmejälg;
- `84h`: see tähendab, et kasutatakse BIP84 eesmärki, mis on mõeldud SegWit v0 aadresside jaoks;
- `0h`: mis näitab, et tegemist on BTC-valuutaga Mainnetis;
- `0h`: viitab konkreetsele kontonumbrile, mida rahakotis kasutatakse.

Kirjeldus sisaldab ka selles rahakotis kasutatavat laiendatud avalikku võtit:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Järgnevalt määrab märkus `/<0;1>/*`, et kirjeldaja võib genereerida aadressid välisest (`0`) ja sisemisest (`1`) ahelast, kusjuures jokker (`*`) võimaldab mitme aadressi järjestikust tuletamist konfigureeritaval viisil, sarnaselt "vahepiirangu" haldamisega traditsioonilises rahakoti tarkvaras.

Lõpuks kujutab `#jy0l7nr4` kontrollsummat, millega kontrollitakse kirjelduse terviklikkust.