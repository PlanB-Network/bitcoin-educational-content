---
term: DUSTRELAYFEE

---
Standardisointisääntö, jota verkon solmut käyttävät määritellessään, mitä ne pitävät "pölyrajana" Tämä parametri asettaa maksun määrän sateina virtuaalista kilotavua kohti (sats/kvB), joka toimii viitteenä laskettaessa, jos UTXO:n arvo on pienempi kuin sen sisällyttämiseen transaktioon tarvittavat maksut. UTXO:ta pidetäänkin "pölynä" Bitcoinissa, jos sen siirtäminen vaatii enemmän maksuja kuin sen itse edustama arvo. Tämän rajan laskenta on seuraava:

```text
limit = (input size + output size) * fee rate
```

Koska Bitcoin-lohkoon sisällytettävän transaktion maksun määrä vaihtelee jatkuvasti, `DustRelayFee`-parametrin avulla kukin solmu voi määritellä tässä laskennassa käytettävän maksun määrän. Oletusarvo Bitcoin Core -ohjelmassa on 3 000 satsia/kvB. Esimerkiksi laskettaessa pölyraja P2PKH-sisääntulolle ja -ulostulolle, joiden mitat ovat 148 ja 34 tavua, laskelma olisi seuraava:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Tämä tarkoittaa, että kyseinen solmu ei välitä tapahtumia, jotka sisältävät P2PKH-suojatun UTXO:n, jonka arvo on alle 546 satsia.