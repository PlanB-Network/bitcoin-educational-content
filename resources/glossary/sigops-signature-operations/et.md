---
term: SIGOPS (ALLKIRJAOPERATSIOONID)

---
Viitab tehingute valideerimiseks vajalikele digitaalallkirjaoperatsioonidele. Iga Bitcoini tehing võib sisaldada mitu sisendit, millest igaühe kehtivaks tunnistamiseks võib olla vaja ühte või mitut allkirja. Nende allkirjade kontrollimine toimub spetsiaalsete opkoodide abil, mida nimetatakse "sigops". Konkreetselt hõlmab see `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY`. Need operatsioonid põhjustavad teatava töökoormuse võrgusõlmedele, mis peavad neid kontrollima. Et vältida DoS-rünnakuid sigopide arvu kunstliku suurendamise kaudu, seab protokoll seetõttu piirangu lubatud sigopide arvule ploki kohta, et tagada, et valideerimiskoormus jääb sõlmede jaoks hallatavaks. See piirang on praegu kehtestatud maksimaalselt 80 000 sigopsi ploki kohta. Arvutamiseks järgivad sõlmed järgmisi reegleid:

`scriptPubKey`s loetakse `OP_CHECKSIG` ja `OP_CHECKSIGVERIFY` 4 sigopsiks. Opkoodid `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY` moodustavad 80 sigopi. Tõepoolest, loendamisel korrutatakse need operatsioonid 4ga, kui nad ei ole osa SegWit sisendist (P2WPKH puhul on sigopide arv seega 1);

`redeemScriptis` loetakse opkoodid `OP_CHECKSIG` ja `OP_CHECKSIGVERIFY` samuti 4 sigops, `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY` loetakse `4n`, kui need eelnevad `OP_n`-le, või 80 sigops, kui need eelnevad `OP_n`-le;

Tunnistusskripti puhul on `OP_CHECKSIG` ja `OP_CHECKSIGVERIFY` väärt 1 sigop, `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY` loetakse `n`, kui need on esitatud `OP_n`-ga, või 20 sigopi, kui need on esitatud `OP_n`-ga, muidu 20 sigopi;

Taproot-skriptides käsitletakse sigoppe erinevalt võrreldes traditsiooniliste skriptidega. Selle asemel, et otseselt lugeda iga allkirjaoperatsiooni, võtab Taproot iga tehingu sisendi jaoks kasutusele sigopsi eelarve, mis on proportsionaalne selle sisendi suurusega. See eelarve on 50 sigops pluss sisendi tunnistaja baitide suurus. Iga allkirjaoperatsioon vähendab seda eelarvet 50 võrra. Kui allkirjaoperatsiooni täitmine vähendab eelarvet alla nulli, on skript kehtetu. See meetod võimaldab Taproot'i skriptides suuremat paindlikkust, säilitades samal ajal kaitse sigopsiga seotud võimalike kuritarvituste eest, sidudes need otseselt sisendi kaaluga. Seega ei hõlma Taproot-skriptid 80 000 sigopsi piirangut ploki kohta.