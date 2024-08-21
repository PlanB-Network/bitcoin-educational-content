---
term: DUSTRELAYFEE
---

Standardiseerimisreegel, mida võrgusõlmed kasutavad, et määratleda, mida nad peavad "tolmu piiriks". See parameeter seab tasumäära satsides virtuaalse kilobaidi kohta (sats/kvB), mis toimib viitena arvutamaks, kas UTXO väärtus on väiksem kui vajalikud tasud selle tehingusse kaasamiseks. Tõepoolest, UTXO-d peetakse Bitcoinis "tolmuks", kui selle ülekandmiseks vajalikud tasud on suuremad kui väärtus, mida see ise esindab. Selle piiri arvutamine on järgmine:

```text
piir = (sisendi suurus + väljundi suurus) * tasumäär
```

Kuna nõutav tasumäär tehingu Bitcoin'i blokki kaasamiseks pidevalt muutub, võimaldab `DustRelayFee` parameeter igal sõlmel määratleda selles arvutuses kasutatava tasumäära. Vaikimisi on Bitcoin Core'is see väärtus määratud 3,000 sats/kvB. Näiteks tolmu piiri arvutamiseks P2PKH sisendi ja väljundi jaoks, mis on vastavalt 148 ja 34 baiti, oleks arvutus:

```text
piir (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

See tähendab, et küsimuse all olev sõlm ei edasta tehinguid, mis sisaldavad P2PKH turvatud UTXO-d, mille väärtus on väiksem kui 546 satsi.