---
term: AADRESSI TAASKASUTUS
---

Aadressi taaskasutus viitab praktikale, kus sama vastuvõtu aadressi kasutatakse mitme UTXO blokeerimiseks, mõnikord mitme erineva tehingu raames. Bitcoine lukustatakse tavaliselt krüptograafilise võtmepaari abil, mis vastab unikaalsele aadressile. Kuna plokiahel on avalik, on lihtne näha, millised aadressid on seotud kui paljude bitcoinidega. Samal aadressil mitme makse jaoks taaskasutamise korral on mõistlik ette kujutada, et kõik seotud UTXOd kuuluvad samale entiteedile. Seega, aadressi taaskasutus kujutab endast probleemi kasutaja privaatsusele. See võimaldab deterministlikke seoseid mitme tehingu ja UTXO vahel, samuti plokiahelas rahaliste vahendite jälgimise jätkumist. Satoshi Nakamoto mainis seda probleemi juba oma Valges Raamatus:

> "*Lisakaitsemeetmena võiks iga tehingu jaoks kasutada uut võtmepaari, et hoida ära nende seostamist ühise omanikuga.*" - Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System". Konsulteeritud aadressil https://bitcoin.org/bitcoin.pdf.

Privaatsuse minimaalseks säilitamiseks on tungivalt soovitatav kasutada iga vastuvõtu aadressi ainult üks kord. Iga uue makse jaoks on asjakohane genereerida uus aadress. Ka vahetusväljundite jaoks tuleks kasutada värsket aadressi. Õnneks on tänu deterministlikele ja hierarhilistele rahakottidele muutunud väga lihtsaks kasutada paljusid aadresse. Kõiki rahakotiga seotud võtmepaare saab hõlpsasti taasluua seemnest. See on ka põhjus, miks rahakottide tarkvara alati genereerib uue, erineva aadressi, kui klõpsate nupul „Saada“.

> ► *Inglise keeles nimetatakse seda "Address Reuse".*