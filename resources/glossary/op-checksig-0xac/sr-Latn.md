---
term: OP_CHECKSIG (0XAC)
---

Proverava validnost potpisa u odnosu na dati javni ključ. Uzima gornja dva Elements sa steka: potpis i javni ključ, i procenjuje da li je potpis ispravan za transakciju Hash i navedeni javni ključ. Ako je verifikacija uspešna, stavlja vrednost `1` (tačno) na stek, u suprotnom `0` (netačno). Ovaj opcode je modifikovan u Tapscript-u da verifikuje Schnorr potpise.