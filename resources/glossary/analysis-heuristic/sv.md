---
term: Analysheuristik
definition: En empirisk metod som används för att spåra Bitcoin-flöde på blockkedjan baserat på observerbara egenskaper i transaktioner.
---

En analysheuristik för Bitcoin-kedjan är en familj av empiriska metoder som används för att spåra flödet av bitcoins på Blockchain baserat på egenskaper som observerats i transaktioner. En heuristik är ett praktiskt tillvägagångssätt för problemlösning, ofta genom ungefärliga metoder, men som utgör en tillräckligt bra lösning för att uppnå ett visst mål. Dessa heuristiker ger ganska tillförlitliga resultat, men aldrig med absolut precision. Med andra ord innebär kedjeanalys alltid en viss grad av sannolikhet i de slutsatser som dras. Det kan till exempel vara mer eller mindre säkert att två adresser tillhör samma enhet, men total säkerhet är alltid utom räckhåll. Hela målet med kedjeanalys ligger just i att sammanställa olika heuristiker för att minimera risken för fel. Det är på sätt och vis en ackumulering av bevis som gör att vi kan komma närmare verkligheten. I detta sammanhang skiljer man på interna och externa heuristiker.



Intern heuristik fokuserar på egenskaper som är specifika för en enskild transaktion. De inkluderar Elements i sin analys, till exempel mängden UTXO, de skript som används, versioner eller låsningstider. Till exempel gör heuristiken för runda betalningar det möjligt att identifiera en transaktionsutmatning som sannolikt är en betalning om beloppet är ett runt tal. Dessa heuristiker gör det ofta möjligt att identifiera växelpengar (pengar som återlämnas till samma användare) och på så sätt fortsätta spårningen.



Extern heuristik, å andra sidan, analyserar likheter och egenskaper som ligger utanför själva transaktionen. De omfattar hela transaktionsmiljön. Återanvändningen av en Address i flera transaktioner är till exempel en extern heuristik. CIOH är också en sådan.