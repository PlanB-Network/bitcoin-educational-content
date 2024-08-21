---
term: OP_CHECKSIGVERIFY (0XAD)
---

Teostab sama operatsiooni nagu `OP_CHECKSIG`, kuid kui allkirja kontroll ebaõnnestub, peatub skript kohe veaga ja tehing on seetõttu kehtetu. Kui kontroll õnnestub, jätkub skript ilma, et lükkaks virna `1` (tõene) väärtuse. Kokkuvõttes teostab `OP_CHECKSIGVERIFY` operatsiooni `OP_CHECKSIG` järgneb `OP_VERIFY`. See operaatorikood muudeti Tapscriptis, et kontrollida Schnorri allkirju.