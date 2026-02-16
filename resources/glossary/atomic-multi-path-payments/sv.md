---
term: Atomic multi-path payments
definition: En förbättrad version av flerstigiga betalningar på Lightning där varje fragment har en egen hemlighet, vilket garanterar att betalningen regleras helt eller inte alls.
---

Förbättrad version av MPP (*Multi-Path Payments*) där varje betalningsfragment har en distinkt partiell hemlighet, vilket säkerställer att transaktionen avvecklas atomiskt, dvs. i sin helhet eller inte alls.


MPP:er är betalningstekniker på Lightning som gör det möjligt att bryta ner en transaktion i flera mindre delar och dirigera den via olika vägar. Med andra ord tar varje betalningsfraktion en annan nodväg. På så sätt kringgår man likviditetsbegränsningar på en enda kanal i rutten. I grundläggande MPP:er delar varje betalningsfraktion samma hemlighet, och därför samma Hash i HTLC:er. Detta kan göra transaktionen spårbar om en observatör är närvarande på flera rutter, eftersom han kan länka samman alla dessa identiska hemligheter. Eftersom hemligheten är unik för alla delar av betalningen är den dessutom inte atomär. Detta innebär att vissa delar av betalningen kan utföras framgångsrikt, medan andra kan misslyckas.


I AMP används unika partiella hemligheter för varje fraktion. När alla fragment har mottagits gör de det möjligt för mottagaren att rekonstruera den ursprungliga allmänna hemligheten och göra anspråk på hela betalningen. Denna metod omöjliggör partiell avveckling av betalningen, eftersom det krävs innehav av alla delhemligheter för att låsa upp hela betalningen. På så sätt säkerställs att betalningen är helt framgångsrik eller helt misslyckad (dvs. atomär). AMP förbättrar också sekretessen, eftersom det inte längre finns några synliga länkar mellan olika rutter.


En fördel med AMPs är att de fungerar även om bara mottagaren och avsändaren har implementerat denna metod. Förmedlingsnoderna behandlar dessa betalningar som konventionella transaktioner med HTLC, omedvetna om att de behandlar delar av en större betalning.