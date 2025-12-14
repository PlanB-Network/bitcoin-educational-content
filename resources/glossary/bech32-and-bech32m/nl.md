---
term: BECH32 EN BECH32M
---

`Bech32` en `Bech32m` zijn twee Address coderingsformaten voor het ontvangen van bitcoins. Ze zijn gebaseerd op een licht gewijzigde basis 32. Ze bevatten een controlesom gebaseerd op een foutcorrigerend algoritme genaamd BCH (*Bose-Chaudhuri-Hocquenghem*). Vergeleken met Legacy adressen, gecodeerd in `Base58check`, hebben de `Bech32` en `Bech32m` adressen een efficiëntere controlesom, waardoor typefouten kunnen worden opgespoord en mogelijk automatisch gecorrigeerd. Hun formaat is ook beter leesbaar, met alleen kleine letters. Hier is de optelmatrix voor dit formaat van basis 10:


| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

Bech32 en Bech32m zijn coderingsformaten die gebruikt worden om SegWit adressen weer te geven. Bech32 is een Address coderingsformaat dat in 2017 werd geïntroduceerd door BIP173. Het gebruikt een specifieke set tekens, bestaande uit cijfers en kleine letters, om typefouten te minimaliseren en het lezen te vergemakkelijken. Bech32-adressen beginnen over het algemeen met `bc1` om aan te geven dat ze oorspronkelijk SegWit zijn. Dit formaat wordt alleen gebruikt op SegWit V0 adressen, met de scripts P2WPKH (Pay to Witness Public Key Hash) en P2WSH (Pay to Witness Script Hash). Er is echter een kleine, onverwachte fout die specifiek is voor het Bech32 formaat. Wanneer het laatste karakter van de Address een `p` is, maakt het toevoegen of verwijderen van een willekeurig aantal `q` karakters direct ervoor de checksum niet ongeldig. Dit heeft geen invloed op bestaand gebruik van SegWit V0 adressen (BIP173) vanwege hun beperking tot twee gedefinieerde lengtes. Dit kan echter wel van invloed zijn op toekomstig gebruik van de Bech32 codering. De Bech32m-indeling is gewoon een Bech32-indeling waarbij deze fout is gecorrigeerd. Het werd geïntroduceerd met BIP350 in 2020. Bech32m adressen beginnen ook met `bc1`, maar ze zijn speciaal ontworpen om compatibel te zijn met SegWit V1 (Taproot) en latere versies, met het script P2TR (Pay to Taproot).