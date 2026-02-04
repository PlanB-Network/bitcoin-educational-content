---
term: LIBSECP256K1
definition: Kryptografiskt C-bibliotek för signaturer och operationer på den elliptiska kurvan secp256k1 som används av Bitcoin.
---

Högpresterande C-bibliotek med hög säkerhet för digitala signaturer och andra kryptografiska primitiver på den elliptiska kurvan `secp256k1`. Eftersom den här kurvan aldrig har använts i stor utsträckning utanför Bitcoin (till skillnad från den ofta föredragna `secp256r1`-kurvan), syftar det här biblioteket till att vara den mest omfattande referensen för dess användning. Utvecklingen av libsecp256k1 var främst inriktad på Bitcoin:s behov, och funktioner avsedda för andra tillämpningar kan vara mindre testade eller verifierade. Lämplig användning av detta bibliotek kräver noggrann uppmärksamhet för att säkerställa att det är lämpligt för de specifika syftena med andra applikationer än Bitcoin.


Biblioteket libsecp256k1 erbjuder en mängd olika funktioner, bland annat:




- ECDSA-secp256k1 signatur och verifiering samt generering av kryptonycklar ;
- Additiva och multiplikativa operationer på hemliga och publika nycklar ;
- Serialisering och analys av hemliga nycklar, publika nycklar och signaturer ;
- Signering och generering av offentliga nycklar i konstant tid med konstant minnesåtkomst;
- Och en mängd andra kryptografiska primitiver.