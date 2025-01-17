---
term: ADRESS REUSE

---
Aadressi korduvkasutamine tähendab, et sama vastuvõtuaadressi kasutatakse mitme UTXO blokeerimiseks, mõnikord mitme erineva tehingu raames. Bitcoine lukustatakse tavaliselt krüptograafilise võtmepaari abil, mis vastab unikaalsele aadressile. Kuna plokiahel on avalik, on lihtne näha, millised aadressid on seotud kui paljude bitcoinidega. Juhul, kui sama aadressi kasutatakse korduvalt mitme makse jaoks, on mõistlik ette kujutada, et kõik seotud UTXOd kuuluvad samale isikule. Seetõttu tekitab aadressi korduvkasutamine probleemi kasutaja privaatsusele. See võimaldab deterministlikke seoseid mitme tehingu ja UTXOde vahel, samuti jäädvustab see ahelas toimuvat fondide jälgimist. Satoshi Nakamoto mainis seda probleemi juba oma valges raamatus:

> "*Tuletõkkena võiks iga tehingu puhul kasutada uut võtmepaari, et vältida nende seostamist ühise omanikuga." - Nakamoto, S. (2008). "Bitcoin: Peer-to-Peer elektrooniline rahasüsteem". Konsulteeritud aadressil https://bitcoin.org/bitcoin.pdf.
Selleks, et säilitada privaatsust minimaalselt, on tungivalt soovitatav kasutada iga vastuvõtuaadressi ainult üks kord. Iga uue makse puhul on asjakohane luua uus aadress. Muudatuste väljastamise korral tuleks samuti kasutada uut aadressi. Õnneks on tänu deterministlikele ja hierarhilistele rahakottidele muutunud väga lihtsaks paljude aadresside kasutamine. Kõik rahakotiga seotud võtmepaarid saab hõlpsasti seemnest taastada. See on ka põhjus, miks rahakoti tarkvara genereerib alati uue, erineva aadressi, kui vajutate nupule "Receive".

> ► *Inglise keeles nimetatakse seda "Address Reuse"