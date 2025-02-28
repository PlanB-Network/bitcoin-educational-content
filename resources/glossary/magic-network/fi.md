---
term: TAIKAVERKKO

---
Bitcoin-protokollassa käytetyt vakiot, joilla tunnistetaan solmujen välillä vaihdetun viestin tietty verkko (mainnet, testnet, regtest...). Nämä arvot merkitään jokaisen viestin alkuun, jotta niiden tunnistaminen tietovirrassa olisi helpompaa. Taikaverkot on suunniteltu siten, että ne esiintyvät harvoin tavallisessa viestintädatassa. Nämä neljä tavua ovat harvinaisia ASCII-koodissa, UTF-8-koodissa virheellisiä ja tuottavat hyvin suuren 32-bittisen kokonaisluvun riippumatta datan tallennusmuodosta. Magic Networks on (little-endian-muodossa):


- Mainnet:

```text
f9beb4d9
```


- Testnet:

```text
0b110907
```


- Regtest:

```text
fabfb5da
```

> ► * Näitä neljää tavua kutsutaan joskus myös nimellä "Magic Number", "Magic Bytes" tai "Start String". *