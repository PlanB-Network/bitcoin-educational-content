---
term: BIP0093
---

Informativni BIP koji predlaže standard za čuvanje i obnavljanje seed hijerarhijskog determinističkog portfolija (prema BIP32) koristeći Šamirovo deljenje tajnog ključa. Ovaj protokol definiše format "codex32", koji je inspirisan formatom bech32, uvodeći strukturirani niz koji se sastoji od prefiksa, parametra praga, identifikatora, indeksa deljenja, korisnog tereta i kontrolnog zbira (BCH). Metoda omogućava da se seed podeli na do 31 deo, od kojih je definisani prag (između 1 i 9) potreban za potpuno obnavljanje seed.