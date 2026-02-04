---
term: Diffie-hellman
definition: Kryptografisk metod som gör det möjligt för två parter att generera en delad hemlighet över en osäker kanal.
---

Kryptografisk metod som gör det möjligt för två parter att generate en delad hemlighet via en osäker kommunikationskanal. Denna hemlighet kan sedan användas för att kryptera kommunikationen mellan de två parterna. Diffie-Hellman använder modulär aritmetik så att även om en angripare kan observera utbytena kan de inte härleda den delade hemligheten utan att lösa ett svårt matematiskt problem: den diskreta logaritmen. I Bitcoin används ibland en variant av DH som kallas ECDH och som använder en elliptisk kurva, särskilt för statiska Address-protokoll som Silent Payments eller BIP47.