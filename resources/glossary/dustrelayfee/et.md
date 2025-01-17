---
term: DUSTRELAYFEE

---
Standardimisreegel, mida võrgusõlmed kasutavad, et määrata kindlaks, mida nad peavad "tolmupiiriks" See parameeter määrab tasu määra satsides virtuaalse kilobaidi kohta (sats/kvB), mis on aluseks arvutamisel, kui UTXO väärtus on väiksem kui vajalikud tasud selle kaasamiseks tehingusse. Tõepoolest, UTXO loetakse Bitcoini "tolmuks", kui selle ülekandmiseks on vaja rohkem tasusid kui selle väärtus, mida ta ise esindab. Selle piirmäära arvutamine on järgmine:

```text
limit = (input size + output size) * fee rate
```

Kuna Bitcoini plokis sisalduvaks tehinguks nõutav tasu määr on pidevalt erinev, võimaldab parameeter "DustRelayFee" igale sõlmpunktile määrata selle arvutamisel kasutatava tasu määra. Bitcoin Core'i puhul on see väärtus vaikimisi määratud 3000 sats/kvB. Näiteks P2PKH sisendi ja väljundi tolmulimiidi arvutamiseks, mis on vastavalt 148 ja 34 baiti suurused, oleks arvutus järgmine:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

See tähendab, et kõnealune sõlmpunkt ei edasta tehinguid, sealhulgas P2PKH tagatud UTXO-d, mille väärtus on väiksem kui 546 sats.