---
term: VOUT
---

Kipengele mahususi cha muamala wa Bitcoin ambacho huamua mahali pa kutuma pesa. Muamala unaweza kujumuisha matokeo mengi, kila moja ikitambuliwa kipekee na mseto wa kitambulishi cha muamala (`txid`) na faharasa inayoitwa `vout`. Faharasa hii, inayoanzia `0`, inaashiria nafasi ya matokeo katika mfuatano wa matokeo ya muamala. Kwa hivyo, matokeo ya kwanza yatateuliwa na `"vout": 0`, ya pili kwa `"vout": 1`, na kadhalika.


Kila `vout` kimsingi inajumuisha vipande viwili vya habari:


- thamani, iliyoonyeshwa kwa bitcoins, ambayo inawakilisha kiasi kilichotumwa;
- hati ya kufunga (`scriptPubKey`) inayobainisha masharti yanayohitajika ili pesa zitumike tena katika shughuli ya siku zijazo.


Mchanganyiko wa `txid` na `vout` ya kipande maalum huunda kile kinachoitwa UTXO, kwa mfano:


```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```