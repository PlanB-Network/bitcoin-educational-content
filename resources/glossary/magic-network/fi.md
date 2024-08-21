---
termi: MAGIC NETWORK
---

Vakiot, joita käytetään Bitcoin-protokollassa tunnistamaan viestien vaihdossa solmujen välillä käytetyn tietyn verkon (pääverkko, testiverkko, regtest...) tyypin. Nämä arvot on kirjoitettu kunkin viestin alkuun helpottamaan niiden tunnistamista datavirrassa. Magic Networkit on suunniteltu esiintymään harvoin tavallisessa kommunikaatiodatassa. Itse asiassa nämä 4 tavua ovat harvinaisia ASCII:ssa, ne ovat virheellisiä UTF-8:ssa, ja ne tuottavat hyvin suuren 32-bittisen kokonaisluvun riippumatta datan tallennusmuodosta. Magic Networkit ovat (little-endian -muodossa):
* Pääverkko:

```text
f9beb4d9
```

* Testiverkko:

```text
0b110907
```

* Regtest:

```text
fabfb5da
```

> ► *Näitä 4 tavua kutsutaan joskus myös "Magic Number", "Magic Bytes" tai "Start String".*