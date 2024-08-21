---
term: PSBT
---

Akronüüm fraasile "Partially Signed Bitcoin Transaction" (osaliselt allkirjastatud Bitcoin tehing). See on spetsifikatsioon, mis tutvustati BIP174-ga, et standardiseerida viisi, kuidas pooleliolevaid tehinguid konstrueeritakse Bitcoiniga seotud tarkvaras, nagu näiteks rahakott-tarkvara. PSBT hõlmab tehingut, mille sisendid ei pruugi olla täielikult allkirjastatud. See sisaldab kõiki vajalikke andmeid osaleja jaoks tehingu allkirjastamiseks ilma lisainformatsiooni vajamata. Seega võib PSBT võtta kolm erinevat vormi:
* Täielikult koostatud tehing, kuid veel allkirjastamata;
* Osaliselt allkirjastatud tehing, kus mõned sisendid on allkirjastatud, samas kui teised veel mitte;
* Või täielikult allkirjastatud Bitcoin tehing, mida saab teisendada võrgus levitamiseks valmis olekuks.

PSBT formaat hõlbustab erineva rahakott-tarkvara ja allkirjastamisseadmete (riistvara rahakott) vahelist koostalitlusvõimet. Praegu kasutatakse PSBT versiooni 0, nagu on määratletud BIP174-s, kuid versiooni 2 pakutakse välja BIP370 kaudu.

> ► *PSBT versiooni 1 ei eksisteeri. Kuna versioon 0 oli esimene versioon, nimetati teine versioon mitteametlikult versiooniks 2. Ava Chow, kes on BIP370 autor, otsustas seega anda sellele uuele versioonile number 2, et vältida segadust.*