---
term: Plånboksavtryck
definition: Utmärkande egenskaper som kan observeras i en plånboks transaktioner och som gör det möjligt att spåra dess aktiviteter.
---

En uppsättning särskiljande egenskaper som kan observeras i transaktioner som görs av samma Bitcoin Wallet. Dessa egenskaper kan omfatta likheter i användningen av skripttyper, återanvändning av adresser, ordningen på UTXO:er, placeringen av ändringsutgångar, signaleringen av RBF (*Replace-by-fee*), versionsnumret, fältet `nSequence` och fältet `nLockTime`.


Wallet-fotavtryck används av analytiker för att spåra en viss enhets aktiviteter på Blockchain genom att identifiera återkommande mönster i dess transaktioner. Till exempel skapar en användare som systematiskt skickar sina ändringar till P2TR-adresser (`bc1p...`) ett distinkt fotavtryck som kan användas för att spåra deras framtida transaktioner.


Som LaurentMT förklarar i Space Kek #19 (en fransktalande podcast) ökar användbarheten av Wallet-fotavtryck i kedjeanalys avsevärt med tiden. Det växande antalet skripttyper och den alltmer gradvisa implementeringen av dessa nya funktioner av Wallet-programvara accentuerar faktiskt skillnaderna. Det är till och med möjligt att exakt identifiera den programvara som används av den spårade enheten. Därför är det viktigt att förstå att det är särskilt relevant att studera en Wallet:s fotavtryck för nyligen genomförda transaktioner, mer än för dem som inleddes i början av 2010-talet.