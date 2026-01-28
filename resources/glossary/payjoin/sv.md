---
term: Payjoin
definition: Samarbetstransaktion som förbättrar integriteten genom att inkludera mottagaren i ingångarna.
---

En specifik Bitcoin-transaktionsstruktur som förbättrar användarens integritet under en utgift genom att samarbeta med betalningsmottagaren. Det unika med PayJoin ligger i dess förmåga att generate en transaktion som ser vanlig ut vid första anblicken men som faktiskt är en mini CoinJoin mellan två parter. Transaktionsstrukturen innebär att betalningsmottagaren ingår i inmatningen vid sidan av den faktiska avsändaren. På så sätt inkluderar mottagaren en betalning till sig själv i mitten av transaktionen som gör att de kan få betalt. Om du till exempel köper en baguette för 6 000 Sats` med en UTXO på 10 000 Sats` och du väljer en PayJoin, kommer din bagare att lägga till en UTXO på 15 000 Sats` som tillhör dem som en input, som de kommer att återfå i sin helhet som en output, utöver dina 6 000 Sats`.


PayJoin-transaktionen uppfyller två mål. För det första syftar den till att vilseleda en extern observatör genom att skapa ett lockbete i kedjeanalysen på Common Input Ownership Heuristic (CIOH). När en transaktion på Blockchain har flera ingångar antas det vanligtvis att alla dessa ingångar sannolikt tillhör samma enhet. När en analytiker undersöker en PayJoin-transaktion förleds de således att tro att alla inmatningar kommer från samma person. Denna uppfattning är dock felaktig eftersom betalningsmottagaren också bidrar till inmatningarna vid sidan av den faktiska betalaren. För det andra vilseleder PayJoin också en extern observatör om det faktiska beloppet på den betalning som gjordes. Genom att granska transaktionens struktur kan analytikern tro att betalningen motsvarar beloppet för en av produktionerna. I själva verket motsvarar betalningsbeloppet ingen av prestationerna. Det är faktiskt skillnaden mellan mottagarens UTXO i utflödet och mottagarens UTXO i inflödet. I detta faller PayJoin-transaktionen inom steganografins område. Det gör det möjligt att dölja det faktiska beloppet för en transaktion i en falsk transaktion som fungerar som ett lockbete.





> ► *PayJoin kallas ibland också "P2EP (Pay-to-End-Point)", "Stowaway" eller "steganografisk transaktion".*