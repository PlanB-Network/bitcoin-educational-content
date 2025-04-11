---
term: TRANSAKTIOTODISTAJA

---
Viittaa Bitcoin-tapahtumien komponenttiin, joka siirrettiin SegWit-softhaarukan myötä transaktioiden muokattavuuden ongelman ratkaisemiseksi. Todistaja sisältää allekirjoitukset ja julkiset avaimet, joita tarvitaan transaktiossa käytettyjen bitcoinien avaamiseen. Legacy-tapahtumissa todistaja edusti kaikkien syötteiden `scriptSig`-summaa. SegWit-tapahtumissa todistaja edustaa `scriptWitness`-summaa kunkin syötteen osalta, ja tämä osa tapahtumasta on nyt siirretty erilliseen Merkle-puuhun lohkon sisällä.

Ennen SegWitiä allekirjoituksia voitiin muuttaa hieman ilman, että ne mitätöitiin, ennen kuin transaktio vahvistettiin, mikä muutti transaktion tunnusta. Tämä vaikeutti erilaisten protokollien rakentamista, sillä vahvistamattoman transaktion tunniste saattoi muuttua. SegWit erottelee todistajat toisistaan ja tekee transaktioista mahdottomia jäljitellä, sillä kaikki allekirjoitusten muutokset eivät enää vaikuta transaktion tunnisteeseen (TXID) vaan ainoastaan todistajan tunnisteeseen (WTXID). Sen lisäksi, että tämä erottelu ratkaisee muokattavuusongelman, se mahdollistaa kunkin lohkon kapasiteetin kasvattamisen.

> ► *Englanniksi "témoin" on käännetty "witness".*