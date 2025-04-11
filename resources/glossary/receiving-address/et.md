---
term: VASTUVÕTVA AADRESS

---
Bitcoinide saamiseks kasutatav teave. Aadress konstrueeritakse tavaliselt avaliku võtme hashimise teel, kasutades `SHA256` ja `RIMPEMD160` ning lisades sellele digesti metaandmed. Avalikud võtmed, mida kasutatakse vastuvõtva aadressi konstrueerimiseks, on osa kasutaja rahakotist ja on seega tuletatud tema seemnest. Näiteks SegWit-aadressid koosnevad järgmisest teabest:


- HRP "bitcoini" määramiseks: "bc";
- Eraldaja: "1";
- Kasutatud SegWit'i versioon: `q` või `p`;
- Kaskoormus: avaliku võtme digesti (või Taproot'i puhul otse avaliku võtme);
- Kontrollsumma: BCH-kood.

Vastuvõtuaadress võib aga sõltuvalt kasutatavast skripti mudelist esindada ka midagi muud. Näiteks P2SH-aadressid konstrueeritakse skripti hashi abil. Taproot-aadressid seevastu sisaldavad tiritud avalikku võtit otse, ilma seda hashimata.

Vastuvõtuaadressi võib esitada tähtnumbrilise stringina või QR-koodina. Iga aadressi võib kasutada mitu korda, kuid see on väga ebasoodne praktika. Teatud privaatsuse säilitamiseks soovitatakse iga Bitcoini aadressi kasutada ainult üks kord. Iga rahakotti saabuva makse jaoks tuleks luua uus aadress. SegWit V0 aadresside puhul on aadress kodeeritud kujul `Bech32`, SegWit V1 aadresside puhul `Bech32m` ja Legacy aadresside puhul `Base58check`. Tehnilisest vaatenurgast tähendab bitcoini saamine avaliku võtmega (ja seega aadressiga) seotud eravõti omamist. Kui keegi saab bitcoin'e, uuendab saatja olemasolevat piirangut oma kulutuste kohta, nii et ainult vastuvõtja saab nüüd seda võimu omada.

![](../../dictionnaire/assets/23.webp)