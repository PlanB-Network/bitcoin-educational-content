---
term: Sweep-transaktion
definition: Transaktionsmönster med en enda UTXO-input och en enda output, karakteristiskt för en självöverföring.
---

Mönster- eller transaktionsmodell som används i kedjeanalys för att fastställa transaktionens art. Denna modell kännetecknas av konsumtion av en enda UTXO som input och produktion av en enda UTXO som output. Tolkningen av denna modell är att vi befinner oss i en självöverföring. Användaren har överfört sina bitcoins till sig själv, till en annan Address som de äger. Eftersom det inte sker någon förändring i transaktionen är det mycket osannolikt att vi har att göra med en betalning. När en betalning görs är det faktiskt nästan omöjligt för betalaren att ha en UTXO som exakt matchar det belopp som krävs av säljaren, utöver transaktionsavgifterna. I allmänhet tvingas betalaren därför att producera en förändringsutgång. Vi vet då att den observerade användaren sannolikt fortfarande innehar denna UTXO. I samband med en kedjeanalys kan vi, om vi vet att den UTXO som användes som input i transaktionen tillhör Alice, anta att UTXO i output också tillhör henne.





