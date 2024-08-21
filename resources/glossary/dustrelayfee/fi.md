---
termi: DUSTRELAYFEE
---

Standardisointisääntö, jota verkon solmut käyttävät määrittääkseen, mitä ne pitävät "pölyrajan" alarajana. Tämä parametri asettaa maksunopeuden satosheina virtuaalista kilotavua kohden (sats/kvB), joka toimii viitearvona laskettaessa, onko UTXO:n arvo pienempi kuin tarvittavat maksut sen sisällyttämiseksi siirtoon. Itse asiassa UTXO katsotaan Bitcoinissa "pölyksi", jos sen siirtämiseen tarvittavat maksut ovat suuremmat kuin sen itsensä edustama arvo. Tämän rajan laskenta on seuraava:

```text
raja = (syötteen koko + tulosteen koko) * maksunopeus
```

Koska vaadittu maksunopeus Bitcoin-lohkon sisältämään siirtoon vaihtelee jatkuvasti, `DustRelayFee`-parametri mahdollistaa kunkin solmun määrittää käytössä olevan maksunopeuden tässä laskennassa. Oletusarvoisesti Bitcoin Core:ssa tämä arvo on asetettu 3 000 satsiin/kvB. Esimerkiksi P2PKH-syötteen ja -tulosteen pölyrajan laskemiseksi, jotka ovat kooltaan 148 ja 34 tavua vastaavasti, laskenta olisi:

```text
raja (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Tämä tarkoittaa, että kyseinen solmu ei välitä siirtoja, jotka sisältävät P2PKH-suojatun UTXO:n, jonka arvo on alle 546 satsia.