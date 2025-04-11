---
term: PSBT

---
Akronüüm "Osaliselt allkirjastatud Bitcoin-tehing". See on spetsifikatsioon, mis võeti kasutusele koos BIP174-ga, et standardiseerida viis, kuidas lõpetamata tehinguid Bitcoiniga seotud tarkvaras, näiteks rahakoti tarkvaras, konstrueeritakse. PSBT kapseldab tehingu, mille sisendid ei pruugi olla täielikult allkirjastatud. See sisaldab kogu vajalikku teavet, et osaleja saaks tehingu allkirjastada ilma lisaandmeid nõudmata. Seega võib PSBT võtta 3 erinevat vormi:


- Täielikult konstrueeritud tehing, kuid veel allkirjastamata;
- Osaliselt allkirjastatud tehing, kus mõned sisendid on allkirjastatud, kuid teised veel mitte;
- Või täielikult allkirjastatud Bitcoini tehing, mida saab konverteerida, et olla valmis võrgus edastamiseks.

PSBT-vorming hõlbustab koostalitlusvõimet erinevate rahakoti tarkvarade ja allkirja andmise seadmete (riistvaraline rahakott) vahel. Praegu kasutatakse PSBT versiooni 0, mis on määratletud dokumendis BIP174, kuid versioon 2 on välja pakutud dokumendis BIP370.

> ► * PSBT 1. versiooni ei ole olemas. Kuna versioon 0 oli esimene versioon, nimetati teine versioon mitteametlikult versiooniks 2. Ava Chow, kes on BIP370 autor, otsustas seega anda sellele uuele versioonile numbri 2, et vältida segadust *