---
term: OP_CHECKMULTISIGVERIFY (0XAF)

---
Kombineerib `OP_CHECKMULTISIG` ja `OP_VERIFY`. See võtab mitu allkirja ja avalikku võtit, et kontrollida, kas `M` allkirja `N`st on kehtiv, nagu `OP_CHECKMULTISIG`. Kui kontrollimine ebaõnnestub, peatub skript kohe veateatega, nagu ka `OP_VERIFY`. Kui kontrollimine on edukas, jätkab skript ilma ühtki väärtust virna lükkamata. See opkood eemaldati Tapscriptist.