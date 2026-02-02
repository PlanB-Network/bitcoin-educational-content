---
term: Självisk brytning
definition: Miningstrategi där block hålls hemliga för att få ett försprång gentemot andra miners.
---

Strategi (eller attack) i Mining, där en Miner eller grupp av miners avsiktligt håller block med en giltig Proof of Work utan att omedelbart släppa dem till nätverket. Syftet är att ligga före andra miners när det gäller Proof of Work, vilket potentiellt gör det möjligt för dem att Miner flera block i rad och publicera dem alla på en gång och därmed maximera sina vinster. Med andra ord bryter den angripande gruppen av gruvarbetare inte på det sista blocket som validerats av hela nätverket, utan snarare på ett block som de själva har skapat och som skiljer sig från det som validerats av nätverket.


Denna process genererar en slags hemlig gren av Blockchain, som förblir okänd för hela nätverket tills denna alternativa kedja potentiellt överstiger den ärliga Blockchain. När de angripande gruvarbetarnas hemliga kedja blir längre (d.v.s. innehåller mer ackumulerat arbete) än den ärliga, offentliga kedjan, sänds den ut till hela nätverket. Vid denna tidpunkt kommer de noder i nätverket som följer den längsta kedjan (med mest ackumulerat arbete) att synkronisera till denna nya kedja. Så det är en omorganisation.


Mining:s själviskhet är irriterande för användarna, eftersom den minskar systemsäkerheten genom att slösa bort en del av nätverkets datorkraft. Om det lyckas leder det också till Blockchain-omorganisationer, vilket påverkar tillförlitligheten hos transaktionsbekräftelser för användare. Denna metod är dock fortfarande riskabel för den angripande gruppen av miners, eftersom det ofta är mer lönsamt att Miner normalt ligger över det sista offentligt kända blocket än att allokera datorkraft till en hemlig gren som förmodligen aldrig kommer att överstiga den ärliga Blockchain. Ju större antalet block i omorganisationen är, desto lägre är sannolikheten för en lyckad attack.