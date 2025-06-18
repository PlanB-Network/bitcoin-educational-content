---
term: VIN
---

Kipengele mahususi cha muamala wa Bitcoin ambacho hubainisha chanzo cha fedha kinachotumika kukidhi matokeo. Kila `vin` inarejelea pato ambalo halijatumika (UTXO) kutoka kwa shughuli ya awali. Muamala unaweza kuwa na pembejeo nyingi, kila moja ikitambuliwa kwa mchanganyiko wa `txid` (kitambulisho cha muamala asilia) na `vout` (kielezo cha matokeo katika muamala huo).


Kila `vin` inajumuisha habari ifuatayo:


- `txid`: kitambulisho cha shughuli ya awali iliyo na matokeo yaliyotumika hapa kama ingizo;
- `vout`: faharasa ya pato katika shughuli ya awali;
- `scriptSig` au `scriptWitness`: hati ya kufungua ambayo hutoa data muhimu ili kukidhi masharti yaliyotolewa na `scriptPubKey` ya shughuli ya awali ambayo fedha zake zinatumika, kwa kawaida kwa kutoa saini ya siri;
- `nMfuatano`: sehemu mahususi inayotumiwa kuonyesha jinsi ingizo hili limefungwa kwa wakati, pamoja na chaguo zingine kama vile RBF.