---
term: SIGOPS (ALLKIRJAOPERATSIOONID)
---

Viitab digitaalsetele allkirjaoperatsioonidele, mis on vajalikud tehingute valideerimiseks. Iga Bitcoin'i tehing võib sisaldada mitut sisendit, millest igaüks võib nõuda ühte või mitut allkirja, et neid peetaks kehtivaks. Nende allkirjade kontrollimine toimub spetsiifiliste opkoodide, mida nimetatakse "sigops", kasutamise kaudu. Konkreetselt hõlmab see `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY`. Need operatsioonid panevad võrgusõlmedele teatud töökoormuse, mis peab neid kontrollima. Et vältida DoS-rünnakuid läbi sigops'ide arvu kunstliku suurendamise, kehtestab protokoll seetõttu piirangu lubatud sigops'ide arvule bloki kohta, tagamaks, et valideerimiskoormus jääks sõlmede jaoks hallatavaks. See piirang on hetkel seatud maksimaalselt 80 000 sigops'ile bloki kohta. Loendamiseks järgivad sõlmed neid reegleid:

`scriptPubKey`s loetakse `OP_CHECKSIG` ja `OP_CHECKSIGVERIFY` 4 sigops'iks. Opkoodid `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY` loetakse 80 sigops'iks. Tõepoolest, loendamise käigus korrutatakse neid operatsioone 4-ga, kui need ei ole osa SegWit sisendist (P2WPKH puhul on sigops'ide arv seega 1);

`redeemScript`is loetakse opkoodid `OP_CHECKSIG` ja `OP_CHECKSIGVERIFY` samuti 4 sigops'iks, `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY` arvestatakse kui `4n`, kui need eelnevad `OP_n`-le, või muidu 80 sigops'iks;

`witnessScript`is on `OP_CHECKSIG` ja `OP_CHECKSIGVERIFY` väärt 1 sigop, `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY` loetakse `n`-ks, kui neid tutvustab `OP_n`, või muidu 20 sigops'iks;

Taproot skriptides käsitletakse sigops'e erinevalt võrreldes traditsiooniliste skriptidega. Erinevalt iga allkirjaoperatsiooni otsesest loendamisest tutvustab Taproot iga tehingu sisendi jaoks sigops'e eelarvet, mis on proportsionaalne selle sisendi suurusega. See eelarve on 50 sigops'i pluss sisendi tunnistaja baitide suurus. Iga allkirjaoperatsioon vähendab seda eelarvet 50 võrra. Kui allkirjaoperatsiooni täitmine langetab eelarve alla nulli, on skript kehtetu. See meetod võimaldab Taproot skriptidel olla paindlikumad, säilitades samal ajal kaitse potentsiaalsete kuritarvituste eest, mis on seotud sigops'idega, sidudes need otseselt sisendi kaaluga. Seega ei ole Taproot skriptid kaasatud 80 000 sigops'i piirangusse bloki kohta.