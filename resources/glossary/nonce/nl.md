---
term: Nonce
---

In de context van computers verwijst de term "Nonce" naar een getal dat slechts één keer gebruikt wordt en daarna vervangen wordt. Het is vaak willekeurig of pseudo-willekeurig. Nonces worden gebruikt in verschillende cryptografische protocollen om de veiligheid van het proces te garanderen. Bijvoorbeeld, de ECDSA handtekeningen die gebruikt worden in het Bitcoin protocol bevatten het gebruik van een Nonce. Dit betekent dat dit nummer nieuw moet zijn. Dit betekent dat dit nummer voor elke handtekening nieuw moet zijn. Als dit niet het geval is, is het mogelijk om de gebruikte private sleutel te berekenen door twee handtekeningen te vergelijken die dezelfde Nonce gebruiken.


Nonces worden ook gebruikt in het Bitcoin Mining proces. Miners verhogen deze aanpasbare waarden binnen hun kandidaat-blokken. Ze wijzigen de Nonce waarde om een cryptografische Hash te vinden die lager is dan of gelijk aan de moeilijkheidsdoelstelling. Dit proces vereist aanzienlijke rekenkracht, omdat het een uitputtende zoektocht tussen een groot aantal mogelijke nonces inhoudt. Wanneer een Miner een Nonce vindt die, wanneer opgenomen in hun blok, een digest produceert die voldoet aan de moeilijkheidscriteria, wordt het blok uitgezonden naar het netwerk en wint de Miner de beloning.


> in 2010 ontdekten onderzoekers dat Sony's PlayStation 3 dezelfde Nonce gebruikte bij het ondertekenen van verschillende codepakketten. Dit hergebruik van de Nonce stelde aanvallers in staat om de privésleutel te berekenen die werd gebruikt om de software te ondertekenen. Met de privésleutel in de hand konden aanvallers geldige handtekeningen maken voor elke code, waardoor ze ongeautoriseerde software, waaronder illegale games of aangepaste besturingssystemen, rechtstreeks op de PS3 konden uitvoeren.*

> *Er bestaat een wijdverbreid misverstand over de oorsprong van de term "Nonce" Sommigen beweren dat het de afkorting is van "nummer dat maar één keer wordt gebruikt" In werkelijkheid gaat de oorsprong van het woord terug tot de 18e eeuw en komt het van de semantische evolutie van de Oud-Engelse uitdrukking "then anes", wat "voor de gelegenheid" betekende