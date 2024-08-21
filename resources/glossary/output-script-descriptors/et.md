---
term: VÄLJUNDISTSRIPTORITE KIRJELDUSED
---

Väljundistsriptorid ehk lihtsalt deskriptorid on struktureeritud avaldised, mis kirjeldavad täielikult väljundistsripti (`scriptPubKey`) ja annavad kõik vajaliku teabe tehingute jälgimiseks konkreetse skripti suhtes või sellest eemale. Need deskriptorid hõlbustavad võtmete haldamist HD rahakottides, pakkudes standardkirjeldust kasutatavate aadresside struktuuri ja tüüpide kohta.

Deskriptorite peamine eelis seisneb nende võimes kapseldada kõik oluline teave rahakoti taastamiseks ühte stringi (lisaks taastefraasile). Deskriptori ja vastavate mnemooniliste fraaside salvestamisega on võimalik taastada mitte ainult privaatvõtmed, vaid ka rahakoti täpne struktuur ja seotud skriptiparameetrid. Tõepoolest, rahakoti taastamine nõuab mitte ainult algse seemne teadmist, vaid ka spetsiifilisi indekseid lastevõtmepaaride tuletamiseks, samuti iga faktori `xpub` multisig rahakoti puhul. Varem eeldati, et see teave oli kõigile implitsiitselt teada. Siiski, skriptide mitmekesistumise ja keerukamate konfiguratsioonide tekkimisega võib see teave muutuda raskesti ekstrapoleeritavaks, muutes need andmed privaatseks ja raskesti murdmiseks. Deskriptorite kasutamine lihtsustab protsessi märkimisväärselt: piisab taastefraasi(de) ja vastava deskriptori teadmisest, et kõik usaldusväärselt ja turvaliselt taastada.

Deskriptor koosneb mitmest elemendist:
* Skriptifunktsioonid nagu `pk` (Maksa-PubKey'le), `pkh` (Maksa-PubKey-Hash'ile), `wpkh` (Maksa-Witness-PubKey-Hash'ile), `sh` (Maksa-Script-Hash'ile), `wsh` (Maksa-Witness-Script-Hash'ile), `tr` (Maksa-Taproot'ile), `multi` (Mitmeallkirjaga), ja `sortedmulti` (Sorteeritud võtmetega mitmeallkirjaga);
* Tuletamisteed, näiteks `[d34db33f/44h/0h/0h]`, mis näitab tuletatud teed ja konkreetse peamise võtme sõrmejälge;
* Võtmed erinevates formaatides, nagu kuueteistkümnendsüsteemi avalikud võtmed või laiendatud avalikud võtmed (`xpub`);
* Kontrollsumma, mida eelneb räsi, deskriptori terviklikkuse kontrollimiseks.

Näiteks P2WPKH rahakoti deskriptor võib välja näha:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```
Selles deskriptoris näitab tuletamisfunktsioon `wpkh` Maksa-Witness-Public-Key-Hash skripti tüüpi. Sellele järgneb tuletamistee, mis sisaldab:
* `cdeab12f`: peamise võtme sõrmejälg;
* `84h`: mis tähistab BIP84 eesmärgi kasutamist, mõeldud SegWit v0 aadresside jaoks;
* `0h`: mis näitab, et tegemist on BTC valuutaga peavõrgus;
* `0h`: mis viitab rahakotis kasutatavale konkreetsele kontonumbrile.

Deskriptor sisaldab ka selles rahakotis kasutatud laiendatud avalikku võtit:
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U

Järgnevalt tähistab märge `/<0;1>/*`, et kirjeldaja suudab genereerida aadresse väliselt (`0`) ja sisemiselt (`1`) ahelalt, kasutades metamärki (`*`), mis võimaldab mitme aadressi järjestikust tuletamist konfigureeritaval viisil, sarnaselt traditsioonilise rahakotitarkvara "gap limit" haldamisega.

Lõpuks tähistab `#jy0l7nr4` kontrollsummat, et kinnitada kirjeldaja terviklikkust.