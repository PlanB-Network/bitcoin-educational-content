---
term: RBF (replace-by-fee)
definition: Mechanisme waarmee een onbevestigde transactie kan worden vervangen door een andere met hogere kosten.
---

Een transactiemechanisme waarmee de verzender een transactie kan vervangen door een andere door hogere vergoedingen te betalen om de bevestiging te versnellen. Als een transactie met te lage vergoedingen vastloopt, kan de verzender *Replace-by-fee* gebruiken om de vergoedingen te verhogen en prioriteit te geven aan hun vervangende transactie in de mempools.


RBF is van toepassing zolang de transactie in de mempools zit; eenmaal in een blok kan het niet meer vervangen worden. Bij het initiële verzenden moet de transactie aangeven dat ze beschikbaar is om vervangen te worden door de `nSequence` waarde aan te passen naar een getal kleiner dan `0xfffffe`. Dit staat bekend als een RBF "vlag". Deze instelling geeft de mogelijkheid aan om de transactie bij te werken nadat deze is uitgezonden, wat vervolgens een RBF mogelijk maakt. Soms is het echter mogelijk om een transactie te vervangen die geen RBF signaal heeft gegeven. Knooppunten die de configuratieparameter `mempoolfullrbf=1` gebruiken, accepteren deze vervanging zelfs als RBF in eerste instantie niet was gesignaleerd.


In tegenstelling tot CPFP (*Kind betaalt voor ouder*), waar de ontvanger kan handelen om de transactie te versnellen, staat RBF (*Replace-by-fee*) de verzender toe het initiatief te nemen om zijn eigen transactie te versnellen door de kosten te verhogen.