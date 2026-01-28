---
term: Speedy trial
definition: Metod för snabb aktivering av soft fork med förkortad tidsfrist, använd för Taproot.
---

Metod för att aktivera en Soft Fork som ursprungligen konceptualiserades för Taproot i början av 2021 av David A. Harding baserat på en idé av Russell O'Connor. Principen är att använda BIP8-metoden med en `LOT`-parameter inställd på `false`, samtidigt som aktiveringsperioden minskas till endast 3 månader. Denna förkortade röstningsperiod möjliggör en snabb verifiering av Miner-godkännandet. Om den nödvändiga tröskeln för godkännande uppnås under en av perioderna låses Soft Fork in. Den kommer att aktiveras flera månader senare, vilket ger miners den tid som behövs för att uppdatera sin programvara.


Framgången med denna metod för Taproot, som hade bred konsensus inom Bitcoin-communityn, garanterar dock inte att den är effektiv för alla uppdateringar. Även om Speedy Trial-metoden möjliggör snabbare aktivering uttrycker vissa utvecklare oro över dess framtida användning. De befarar att det kan leda till en alltför snabb följd av Soft-forks, vilket potentiellt skulle kunna hota stabiliteten och säkerheten i Bitcoin-protokollet. Jämfört med BIP8 med parametern `LOT=true` är Speedy Trial-metoden mycket mindre hotfull för gruvarbetare. Ingen UASF planeras automatiskt. Denna aktiveringsmetod har ännu inte formaliserats inom en BIP.


