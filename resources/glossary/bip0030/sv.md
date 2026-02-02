---
term: BIP0030
definition: Soft fork som förbjuder duplicerade transaktionsidentifierare (TXID), vilket löser en sårbarhet där två transaktioner kunde ha samma ID.
---

Förbättringsförslag som involverar en Soft Fork som implementerades den 15 mars 2012 för att lösa problemet med dubbla transaktionsidentifierare. Före BIP30 var det tekniskt möjligt att ha två olika transaktioner med samma transaktionsidentifierare (txid) i Blockchain. Detta hände särskilt två gånger för coinbase-transaktioner: den i block 91 880 har samma txid som coinbase i block 91 722, och den i block 91 842 har samma txid som coinbase i block 91 812. BIP30 löste detta fel genom att införa en ny enkel regel: ingen ny transaktion kan ha samma txid som en tidigare registrerad transaktion såvida inte den ursprungliga transaktionen hade använts helt och hållet (dvs. alla dess utgångar hade använts). Denna Soft Fork aktiverades med hjälp av flaggdagsmetoden. Det är således en av de första UASF:erna.