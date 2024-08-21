---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

Ühendab `OP_CHECKMULTISIG` ja `OP_VERIFY`. See võtab mitu allkirja ja avalikku võtit, et kontrollida, kas `M` `N`-st allkirjast on kehtivad, just nagu `OP_CHECKMULTISIG` teeb. Seejärel, nagu `OP_VERIFY` puhul, kui kontroll ebaõnnestub, peatub skript kohe veaga. Kui kontroll on edukas, jätkub skript ilma väärtust stäkki lükkamata. See operatsioonikood eemaldati Tapscriptis.