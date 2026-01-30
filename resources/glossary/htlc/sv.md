---
term: HTLC
definition: Smart kontrakt som villkorar en överföring vid avslöjandet av en hemlighet inom en tidsgräns.
---

Står för "*Hashed Timelock Contract*". Detta är en Smart contract-mekanism som främst används på Lightning. Den finns också ibland i atombyten. I grund och botten gör HTLC en penningöverföring beroende av att en hemlighet avslöjas och inkluderar även ett tidsvillkor för att skydda avsändarens pengar i händelse av en misslyckad transaktion.


På Lightning låter HTLC dig skicka bitcoins till en nod som du inte har en direkt kanal med, genom att passera genom flera kanaler, utan behov av förtroende längs vägen. Betalningen mellan varje nod är villkorad av att en förbild tillhandahålls (den hemlighet som, när den hashas, motsvarar ett överenskommet värde). Om den slutliga mottagaren tillhandahåller denna förbild kan den göra anspråk på medlen, vilket med nödvändighet gör det möjligt för varje mellanliggande nod att göra anspråk på medlen i kaskad.


Om Alice till exempel vill skicka 1 BTC till David, men inte har en direktkanal med honom, måste hon gå via Bob och Carol, som har betalningskanaler med varandra. Så här fungerar transaktionen:




- David presenterar Alice med en Invoice Lightning. Denna innehåller Hash $h$ av en hemlig $s$ (förbilden) som endast David känner till. Så vi har: $h = \text{Hash}(s)$ ;
- Alice skapar en HTLC med Bob, som erbjuder sig att skicka 1 BTC till henne under förutsättning att Bob förser henne med en hemlighet $s$ (förbilden) som motsvarar Hash $h$ ;
- Bob skapar en HTLC med Carol, som erbjuder sig att skicka 1 BTC till honom under förutsättning att hon tillhandahåller samma hemlighet $s$ ;
- Carol skapar en HTLC med David, som erbjuder ytterligare 1 BTC om han avslöjar $ s$-förbilden;
- David avslöjar $s$ (som bara han visste) för Carol för att få 1 BTC. Carol kan nu använda $s$ för att få BTC från Bob. Och Bob, som nu känner till $s$, gör samma sak med Alice.


Slutligen skickade Alice 1 BTC till David via Bob och Carol (en neutral åtgärd för den senare), utan att någon behövde lita på varandra, eftersom allt är säkrat i kaskad genom HTLC:ernas villkor.


HTLC möjliggör så kallade "atomiska" utbyten: antingen är överföringen helt framgångsrik eller så misslyckas den och pengarna återlämnas. Detta garanterar transaktionernas säkerhet, även mellan flera deltagare utan behov av förtroende.