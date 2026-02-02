---
term: CISA
definition: Technisch voorstel om de handtekeningen van alle inputs van een transactie te combineren tot één enkele, waardoor de grootte en de kosten worden verminderd.
---

Acroniem voor "Cross-Input Signature Aggregation". Dit is een technisch voorstel om de grootte van Bitcoin transacties te optimaliseren door het aantal handtekeningen dat nodig is om ze te valideren te verminderen.


Momenteel moet op Bitcoin elke invoer in een transactie een individuele handtekening hebben voordat deze kan worden geconsumeerd. Dit bewijst dat de eigenaar van de UTXO in kwestie de transactie heeft geautoriseerd. Met CISA is het de bedoeling om de handtekeningen van alle ingangen van een enkele transactie te combineren tot een enkele handtekening die alle ingangen omvat. Dit zou het mogelijk maken om de omvang van transacties met veel ingangen te verkleinen en dus ook de kosten te verlagen. Dit zou vooral handig zijn voor degenen die coinjoins of consolidaties uitvoeren, terwijl er meer transacties op Bitcoin bevestigd kunnen worden zonder de blokgroottes of intervallen te veranderen. CISA is gebaseerd op het Schnorr-protocol, dat lineaire aggregatie van handtekeningen mogelijk maakt. Dit betekent dat een enkele handtekening het bezit van meerdere onafhankelijke sleutels kan bewijzen.


Het implementeren van CISA op Bitcoin is echter erg complex, omdat het ingrijpende veranderingen vereist in de manier waarop scripts werken. Momenteel wordt scriptverificatie op Bitcoin invoer voor invoer gedaan. Overgaan op een model waarbij een hele transactie in één keer wordt gecontroleerd, zoals CISA voorstelt, is verre van een triviale verandering.