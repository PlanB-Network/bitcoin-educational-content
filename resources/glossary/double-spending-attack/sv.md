---
term: Dubbelspendering
definition: Attack som försöker använda samma bitcoin flera gånger för att bedra motparter.
---

En attack där en illvillig användare försöker använda samma UTXO (*Unspent Transaction Output*) mer än en gång för att berika sig på bekostnad av de parter som är involverade i transaktionerna. När en transaktion bekräftas i ett block och läggs till i Blockchain registreras i princip användningen av dessa bitcoins permanent, vilket förhindrar ytterligare användning av samma bitcoins. Att förhindra dubbla utgifter är till och med Blockchain:s primära användningsområde.


Vid en double spending-attack gör angriparen först en legitim transaktion med en handlare och skapar sedan en andra konkurrerande transaktion där samma mynt används, antingen genom att skicka tillbaka dem till sig själv för att återfå beloppet eller genom att använda dem för att köpa en annan vara eller tjänst från en annan handlare.


Det finns två huvudsakliga scenarier som kan möjliggöra denna attack. Det första, och enklaste för angriparen, innebär att den bedrägliga transaktionen utförs innan den legitima transaktionen inkluderas i ett block. För att säkerställa att den bedrägliga transaktionen bekräftas först kopplar angriparen betydligt högre transaktionsavgifter till den än till den legitima transaktionen. Detta är en form av bedräglig RBF. Det här scenariot är bara möjligt om handlaren går med på att slutföra försäljningen i "zeroconf", vilket innebär utan några bekräftelser för betalningstransaktionen. Det är därför som det starkt rekommenderas att man väntar på flera bekräftelser innan man betraktar en transaktion som oföränderlig. Det andra scenariot, som är mycket mer komplext, är en 51%-attack. Om angriparen kontrollerar en betydande del av nätverkets datorkraft kan de bryta en konkurrerande kedja till den som innehåller den legitima transaktionen, men som inkluderar deras bedrägliga transaktion. När handlaren har accepterat försäljningen och angriparen har lyckats skapa en längre kedja (med mer ackumulerat arbete) än den legitima kedjan, kan de sedan sända ut sin bedrägliga kedja, som kommer att erkännas av nätverksnoderna som den giltiga.