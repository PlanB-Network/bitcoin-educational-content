---
name: Zeus Embedded
description: Så här använder du Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS är ursprungligen en mobilapplikation för fjärrhantering av blixtnoder, så att du kan styra din nod installerad på en fjärrserver


Men applikationen innehåller också en "Embedded node".



**Det är denna aspekt av applikationen som vi kommer att utforska i denna handledning. Detta gör att vem som helst kan ha sin egen blixtnod på mobilen, utan behov av en dedikerad server, på samma sätt som ACINQ erbjuder sin otroliga Wallet blixt Phoenix.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*Som en påminnelse är Lightning ett nätverk som fungerar parallellt med Bitcoin, vilket gör det möjligt att växla bitcoins utan att systematiskt behöva genomföra On-Chain-transaktioner. Resultatet är nästan omedelbara transaktioner, utan att behöva vänta 10 minuter på att ett block ska valideras. Detta är särskilt användbart när man betalar en handlare i den fysiska världen. Dessutom ger Lightning en anmärkningsvärd nivå av **konfidentialitet** som Bitcoin-nätverket inte har inbyggt*.



**Zeus "Integrated"** riktar sig till Bitcoiners som vill maximera sin integritet och autonomi.


Kort sagt, det är **potentiellt** Wallet-mobilen i cypherpunks drömmar. Även om den fortfarande är i sin linda (alfaversion) och är föremål för några buggar, är dess funktioner legio, och det råder ingen tvekan om att den kommer att glädja de mest orädda bland oss, som vill ha maximal kontroll och valmöjlighet.



Å andra sidan tror jag inte att det för närvarande är lämpligt för nybörjare som inte känner till Bitcoin och helt enkelt vill ha ett enkelt sätt att skicka / ta emot satoshis. Även om detta kan förändras i framtiden, eftersom en vårdnadsfunktion via Cashu (chaumian Ecash) -protokollet implementeras för nybörjare ...



## Installera programmet



Gå till [projektets webbplats] (https://zeusln.com/) för att ladda ner applikationen för din smartphones operativsystem:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Skapande av portfölj



När programmet har startat klickar du på knappen "Quick Start" för att börja skapa Wallet.



![image](assets/fr/03.webp)





En serie initialiseringsskärmar visas sedan. Vänta några ögonblick, vänta sedan några minuter tills noden är 100% synkroniserad via Neutrino.



Detta kan ta några minuter. För information är neutrino ett sätt för mobila plånböcker att få tillgång till Blockchain Bitcoin information, utan att behöva köra en Full node.



![image](assets/fr/04.webp)





Efter några ögonblick är du redo att köra.



![image](assets/fr/05.webp)




## Inställning av applikation



Redo, ja inte riktigt, för det säger sig självt att en Zeus-användare värd namnet navigerar sin Wallet med klass och stil. Så vi kommer att behöva ändra hans avatar.



Klicka på din avatar i det övre högra hörnet på skärmen:



![image](assets/fr/06.webp)





Klicka på kugghjulet och sedan på plustecknet "+" :



![image](assets/fr/07.webp)





Välj det vackraste fotot av Zeus som ska representera denna Wallet och klicka på "CHOOSE PICTURE" längst ner på skärmen och gå sedan tillbaka genom att klicka på pilen längst upp till höger.



![image](assets/fr/08.webp)





Slutligen ger du din Wallet ett smeknamn och klickar på "SAVE Wallet CONFIG" för att ändringen ska träda i kraft. Klicka slutligen på bakåtpilen i det övre vänstra hörnet för att återgå till startskärmen.



![image](assets/fr/09.webp)





Den här gången kan vi verkligen komma igång.



![image](assets/fr/10.webp)



### Biometri



För att skydda åtkomsten till din Wallet kan du lägga till en PIN-kod/ett lösenord och aktivera biometri.



För att göra detta, gå till Wallet huvudmeny genom att klicka på de horisontella strecken längst upp till vänster.



![image](assets/fr/11.webp)





Välj "Inställningar", sedan "Säkerhet" och slutligen "Ange/ändra PIN-kod".



![image](assets/fr/12.webp)





Skapa din PIN-kod, bekräfta den och aktivera biometri genom att trycka på motsvarande "Biometrics"-knapp.  Gå tillbaka till huvudmenyn med hjälp av pilen uppe till vänster.



![image](assets/fr/13.webp)




### Spara Mnemonic fras



När du är tillbaka i huvudmenyn klickar du på "Säkerhetskopiera Wallet" och läser sedan varningstexten som informerar dig om att förlora de 24 ord du ska få är detsamma som att förlora tillgången till dina pengar, och att alla som har dessa ord utöver dig kan komma åt dina pengar. Ge dem aldrig till någon.



Välj "I UNDERSTAND" längst ner på skärmen. Klicka sedan på vart och ett av de 24 orden för att få upp dem och anteckna dem noggrant.



Du kan skriva den på papper eller kanske, för ökad säkerhet, gravera den på rostfritt stål för att skydda den mot brand, översvämning eller kollaps. Valet av medium för din Mnemonic beror på din säkerhetsstrategi, men om du använder Zeus som en kostnads-Wallet som innehåller måttliga mängder bör papper vara tillräckligt.



För mer information om det rätta sättet att spara och hantera din Mnemonic-fras rekommenderar jag starkt att du följer den här andra handledningen, särskilt om du är nybörjare:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



När du är klar klickar du på "I'VE BACKUP MY 24 WORDS" längst ner på skärmen, och vi är tillbaka på startskärmen, redo att ta emot våra första bitcoins.




## Alternativ 1 - Ta emot On-Chain bitcoins och öppna en Lightning-kanal



**Zeus Embedded** är främst utformad som en inbäddad blixtnod, men den kan också användas som en Wallet On-Chain.



För att ta emot On-Chain bitcoins, klicka på knappen "On-Chain" och sedan på "Receive".


Slutligen skannar du QR-koden eller kopierar Bitcoin Address för att sätta in pengar.



![image](assets/fr/15.webp)





När pengarna har bekräftats och krediterats till din Wallet kan du använda dem för att öppna en **Lightning-kanal**. Din Lightning-kanal är din gateway till Lightning Network, vilket gör det möjligt för dig att Exchange bitcoins på ett mycket mer konfidentiellt och snabbt sätt.





- För att göra det, klicka på "Flytta On-Chain FUNDS till LIGHTNING"



På nästa skärm ombeds du att öppna en kanal i samarbete med **"Olympus by Zeus"**, den LSP (Lightning Service Provider) som Wallet föredrar.


I den här handledningen väljer vi det här alternativet för enkelhetens skull, men det är fullt möjligt att öppna kanaler med vilken nod som helst i nätverket.


Det är till och med möjligt att öppna flera kanaler i en enda transaktion genom att välja "OPEN ADDITIONAL CHANNEL". *Men vi kommer att titta på detta i en "avancerad" version av **Zeus Embedded**** handledning.





- Välj sedan det belopp som du vill avsätta till denna kanal. I vårt fall kommer alla våra On-Chain-medel att användas, så vi aktiverar knappen "Använd alla möjliga medel".





- Välj slutligen knappen "OPEN CHANNEL" längst ned på skärmen.



![image](assets/fr/16.webp)





Inom några sekunder är kanalen etablerad och vi är redo att göra våra första Lightning-transaktioner. På startskärmen kan vi se en liten klocka bredvid vårt Wallet-saldo. Detta beror på att vi fortfarande måste vänta på 3 On-Chain-bekräftelser innan kanalen verkligen är funktionell.



![image](assets/fr/17.webp)





Efter de tre bekräftelserna märker vi att vårt saldo nu krediteras Lightning-insatsen.



![image](assets/fr/18.webp)



En liten detalj: när vi klickar på menyn längst ner på skärmen för att se statusen för våra blixtkanaler ser vi att en liten del av vårt saldo inte är tillgängligt för utgifter: vi kan bara spendera 208253 satoshis istället för de 210370 vi faktiskt har. Detta är normalt, eftersom det är specifikt för blixtprotokollet.



Slutligen bör det noteras att vår partner Olympus förbehåller sig rätten att stänga kanalen efter eget gottfinnande, om den till exempel inte används. För att säkerställa att vår kanal upprätthålls måste vi betala LSP (Lightning Service Provider), som vi kommer att se i nästa stycke, genom det andra sättet att öppna en kanal.





## Skicka bitcoins via Lightning



Nu när vi har fått vår kanal igång, låt oss se hur vi kan använda den för att betala en Invoice (Invoice) blixt.



För att göra detta klickar du på knappen "Lightning" och sedan på "Send".



![image](assets/fr/19.webp)





På nästa skärm kopierar du din Invoice till det avsedda fältet eller skannar den genom att klicka på ikonen längst upp till höger. Skjut slutligen knappen "Slide to Pay" åt höger för att betala.



![image](assets/fr/20.webp)






Vänta några sekunder så är Invoice betald och dina satoshis har färdats med ljusets hastighet.



![image](assets/fr/21.webp)





Med Zeus kan du sedan lägga till en nota för att denominera din betalning, eller se vilken väg dina satoshis tog innan de nådde sin destination (och de avgifter som tas ut av alla mellanliggande noder). Det här är den typ av funktionalitet som vi älskar med Wallet.



![image](assets/fr/22.webp)



Observera att till skillnad från en Wallet som [Phoenix]([Plan ₿ Network - Phoenix](https://planb.network/fr/tutorials/Wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), beräknas rutten med Zeus lokalt och delegeras inte till en tredje part (ACINQ i fallet med Phoenix). Så du är den enda som vet vem som är mottagare av betalningen. Vi förlorar lite effektivitet (betalningar tar lite längre tid att slutföra, men vi vinner mycket när det gäller integritet).





Genom att klicka på den lilla pilen längst ner på startskärmen kan du också se vår betalningshistorik. Här ser vi i Green de 212 121 Sats som vi fick för On-Chain, sedan i rött de 211 756 Sats som användes för att öppna vår kanal, sedan de 121 212 satoshis som användes för att betala för vår Invoice-blixt.



![image](assets/fr/23.webp)





## Alternativ 2 - Ta emot bitcoins direkt på Lightning



I stället för att öppna en kanal manuellt, som vi just har sett, är det möjligt att ta emot medel direkt via Lightning, även utan en redan befintlig kanal, med Olympus, Zeus LSP.




- För att göra detta, klicka på knappen "Lightning" på startskärmen och sedan på "Receive".
- Välj sedan det belopp du vill ha i rutan "Amount" och klicka på knappen "CREATE Invoice" längst ned på skärmen.



![image](assets/fr/24.webp)





På nästa skärm visas de Invoice som ska betalas för att få satoshis. Vi får veta att LSP kommer att hålla inne 10 000 Sats om betalningen sker via Lightning. Vi kommer senare att se hur dessa kanalöppningsavgifter motiveras.



Betala Invoice eller låt någon annan betala det, så öppnas kanalen automatiskt, men med avdrag för 10 000 Sats enligt överenskommelse.



![image](assets/fr/25.webp)





Vi befinner oss nu i spetsen för 2 blixtkanaler, vars status kan kontrolleras genom att klicka på knappen som indikeras av den vita pilen längst ner på startskärmen.



Vi kan se att till skillnad från den kanal som öppnas från vår On-Chain-skala, visar den som öppnas direkt via blixten ingen varning.


Eftersom du har betalat för att sätta upp den här kanalen åtar sig Lightning Service Provider (LSP) att underhålla kanalen i 3 månader och erbjuder dig "inkommande likviditet". På den nedre kanalen kan du se att mottagningskapaciteten är 96383 satoshis. LSP:n har alltså bundit kapital för att du ska kunna ta emot betalningar direkt efter att du öppnat kanalen.



De 10 000 Satoshi som betalats i avgifter täcker alltså: kostnaden för att öppna kanalen (Bitcoin On-Chain transaktion, garantin för att underhålla kanalen i 3 månader och kapitalbindningen).



![image](assets/fr/26.webp)





Grattis, du är nu redo att använda Zeus Embedded, det mobila belysningssystemet Wallet med de mest avancerade funktionerna på marknaden.





För att ta reda på mer om den tekniska driften av Lightning Network kan du hitta Fanis Michalakis utmärkta gratis Plan ₿ Network-utbildning:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb