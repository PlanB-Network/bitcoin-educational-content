---
termi: TRANSAKTION TODISTAJA
---

Viittaa Bitcoin-siirtojen komponenttiin, joka SegWit-pehmeän haarukan myötä siirrettiin ratkaisemaan siirtojen muunneltavuuden ongelma. Todistaja sisältää allekirjoitukset ja julkiset avaimet, jotka ovat tarpeen siirrossa käytettyjen bitcoinien vapauttamiseen. Perinteisissä siirroissa todistaja edusti kaikkien syötteiden `scriptSig`-summaa. SegWit-siirroissa todistaja edustaa kunkin syötteen `scriptWitness`-summaa, ja tämä osa siirrosta on nyt siirretty erilliseen Merkle-puuhun lohkon sisällä.

Ennen SegWitiä allekirjoituksia voitiin muuttaa lievästi ilman, että ne mitätöityivät ennen siirron vahvistamista, mikä muutti siirron tunnistetta. Tämä teki erilaisten protokollien rakentamisen vaikeaksi, sillä vahvistamaton siirto saattoi nähdä tunnisteensa muuttuvan. Todistajien erottamalla SegWit tekee siirroista muuntumattomia, sillä allekirjoitusten muutokset eivät enää vaikuta siirron tunnisteeseen (TXID), vaan ainoastaan todistajan tunnisteeseen (WTXID). Muunneltavuusongelman ratkaisemisen lisäksi tämä erottelu mahdollistaa kunkin lohkon kapasiteetin kasvattamisen.

> ► *Englanniksi "témoin" käännetään "witness"ksi.*