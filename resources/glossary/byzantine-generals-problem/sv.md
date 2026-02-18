---
term: Byzantinska generalsproblemet
definition: Problem som illustrerar utmaningarna med samordning i ett distribuerat system där aktörerna inte kan lita på varandra.
---

Problemet formulerades först av Leslie Lamport, Robert Shostak och Marshall Pease i facktidskriften *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) i juli 1982. Det används idag för att illustrera utmaningarna när det gäller beslutsfattande när ett distribuerat system inte kan lita på någon aktör.


I den här metaforen har en grupp bysantinska generaler och deras respektive arméer slagit läger runt en stad som de vill anfalla eller belägra. Generalerna är geografiskt åtskilda från varandra och måste kommunicera via budbärare för att samordna sin strategi. Om de anfaller eller retirerar spelar ingen roll, så länge alla generaler når konsensus.


Därför kan vi ta hänsyn till följande krav:


- Varje general måste fatta ett beslut: anfalla eller retirera (ja eller nej);
- När beslutet väl är fattat går det inte att ändra;
- Alla generaler måste vara överens om samma beslut och verkställa det synkront.


Dessutom kan en general bara kommunicera med en annan genom meddelanden som sänds av en kurir, vilka kan försenas, förstöras, ändras eller förloras. Och även om ett meddelande levereras framgångsrikt kan en eller flera generaler välja (av vilken anledning som helst) att svika det etablerade förtroendet och skicka ett falskt meddelande, vilket skapar kaos.


Genom att tillämpa dilemmat på Bitcoin Blockchain representerar varje general en nod i nätverket som måste nå konsensus om systemets tillstånd. Med andra ord måste majoriteten av deltagarna i ett distribuerat nätverk komma överens och utföra samma åtgärd för att undvika ett totalt misslyckande. Det enda sättet att nå konsensus i den här typen av distribuerade system är att minst 2/3 av nätverksnoderna är pålitliga och ärliga. Om majoriteten av nätverket beslutar sig för att agera illvilligt är systemet därför sårbart.


> detta dilemma kallas ibland också "problemet med tillförlitlig sändning"