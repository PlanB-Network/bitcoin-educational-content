---
term: VASTUVÕTU AADRESS
---

Informatsioon, mida kasutatakse bitcoinide vastuvõtmiseks. Aadress luuakse tavaliselt avaliku võtme räsides, kasutades `SHA256` ja `RIMPEMD160`, ning lisades sellele kokkuvõttele metaandmeid. Vastuvõtu aadressi loomiseks kasutatavad avalikud võtmed on osa kasutaja rahakotist ja seega tuletatud nende seemnest. Näiteks SegWiti aadressid koosnevad järgnevast informatsioonist:
* HRP, et tähistada "bitcoin": `bc`;
* Eraldaja: `1`;
* Kasutatava SegWiti versioon: `q` või `p`;
* Koormus: avaliku võtme kokkuvõte (või otse avalik võti Taprooti puhul);
* Kontrollsumma: BCH kood.

Siiski võib vastuvõtu aadress sõltuvalt kasutatavast skripti mudelist esindada ka midagi muud. Näiteks P2SH aadressid luuakse skripti räsi kasutades. Taprooti aadressid seevastu sisaldavad kohandatud avalikku võtit otse ilma seda räsides.

Vastuvõtu aadressi saab esitada tähtnumbrilise jada või QR-koodi kujul. Iga aadressi saab kasutada mitu korda, kuid see on väga ebasoovitatav praktika. Tõepoolest, teatud privaatsuse taseme säilitamiseks soovitatakse iga Bitcoin aadressi kasutada ainult üks kord. Iga sissetuleva makse jaoks oma rahakotti tuleks genereerida uus aadress. Aadress kodeeritakse `Bech32` jaoks SegWit V0 aadressidel, `Bech32m` jaoks SegWit V1 aadressidel ja `Base58check` jaoks Legacy aadressidel. Tehnilisest vaatepunktist tähendab bitcoinide vastuvõtmine privaatvõtme omamist, mis on seotud avaliku võtmega (ja seega aadressiga). Kui keegi saab bitcoine, uuendab saatja olemasolevat piirangut nende kulutamisele nii, et nüüdsest võib seda jõudu omada ainult saaja.

![](../../dictionnaire/assets/23.png)