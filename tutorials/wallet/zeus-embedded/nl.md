---
name: Zeus ingebed
description: Hoe de Lightning Zeus Embedded Wallet gebruiken
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS is in eerste instantie een mobiele applicatie voor beheer op afstand van lightning nodes, waarmee je je node kunt beheren die op een externe server is geïnstalleerd


Maar de applicatie bevat ook een "Embedded node".



**Het is dit facet van de applicatie dat we in deze tutorial zullen verkennen. Hierdoor kan iedereen zijn eigen bliksemknooppunt op mobiel hebben, zonder dat er een speciale server nodig is, op dezelfde manier als ACINQ zijn ongelooflijke Wallet bliksem Phoenix aanbiedt.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*Ter herinnering, Lightning is een netwerk dat parallel werkt met Bitcoin, waardoor bitcoins kunnen worden uitgewisseld zonder dat er systematisch On-Chain transacties moeten worden uitgevoerd. Het resultaat zijn bijna onmiddellijke transacties, zonder 10 minuten te hoeven wachten tot een blok is gevalideerd. Dit is vooral handig bij het betalen van een handelaar in de fysieke wereld. Bovendien biedt Lightning een opmerkelijk niveau van **vertrouwelijkheid** dat het Bitcoin netwerk van nature niet bezit*.



**Zeus "Integrated"** is gericht op Bitcoiners die hun privacy en autonomie willen maximaliseren.


Kortom, het is in potentie de Wallet mobiel uit de dromen van cypherpunks. Ook al staat het nog in de kinderschoenen (alpha-versie) en bevat het nog een paar bugs, de functies zijn legio en er bestaat geen twijfel over dat het de meest onverschrokkenen onder ons, die maximale controle en opties willen, zal plezieren.



Aan de andere kant denk ik niet dat het op dit moment geschikt is voor beginners die niet bekend zijn met Bitcoin en gewoon een eenvoudige manier willen om satoshis te verzenden/ontvangen. Hoewel dit in de toekomst kan veranderen, aangezien er een bewaarfunctie via het Cashu (chaumian Ecash) protocol wordt geïmplementeerd voor beginners...



## De toepassing installeren



Ga naar [de projectwebsite](https://zeusln.com/) om de applicatie voor het OS van je smartphone te downloaden:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Portfolio maken



Zodra de toepassing is opgestart, klik je op de knop "Snel starten" om te beginnen met het aanmaken van de Wallet.



![image](assets/fr/03.webp)





Er verschijnt dan een reeks initialisatieschermen. Wacht enkele ogenblikken, wacht dan enkele minuten tot het knooppunt 100% gesynchroniseerd is via Neutrino.



Dit kan een paar minuten duren. Ter informatie: neutrino is een manier voor mobiele portemonnees om toegang te krijgen tot Blockchain Bitcoin informatie, zonder een Full node te hoeven draaien.



![image](assets/fr/04.webp)





Na enkele ogenblikken ben je klaar om te gaan.



![image](assets/fr/05.webp)




## Toepassing instellen



Klaar, nou ja niet helemaal, want het spreekt voor zich dat een Zeus-gebruiker die naam waardig zijn Wallet met klasse en stijl navigeert. Dus moeten we zijn avatar veranderen.



Klik op je avatar in de rechterbovenhoek van het scherm:



![image](assets/fr/06.webp)





Klik op het tandwiel en vervolgens op de plus "+" :



![image](assets/fr/07.webp)





Kies de mooiste foto van Zeus om deze Wallet voor te stellen en klik op "CHOOSE PICTURE" onderaan het scherm, ga dan terug door op de pijl rechtsboven te klikken.



![image](assets/fr/08.webp)





Geef je Wallet tot slot een bijnaam en klik op 'SAVE Wallet CONFIG' om de verandering te laten ingaan. Klik ten slotte op de pijl terug in de linkerbovenhoek om terug te keren naar het beginscherm.



![image](assets/fr/09.webp)





Nu kunnen we echt beginnen.



![image](assets/fr/10.webp)



### Biometrie



Om de toegang tot je Wallet te beveiligen, kun je een PIN/wachtwoord toevoegen en biometrie activeren.



Ga hiervoor naar het Wallet hoofdmenu door op de horizontale streepjes linksboven te klikken.



![image](assets/fr/11.webp)





Selecteer "Instellingen", dan "Beveiliging" en tot slot "PIN instellen/wijzigen".



![image](assets/fr/12.webp)





Maak uw pincode aan, bevestig deze en activeer biometrie door op de bijbehorende knop "Biometrie" te drukken.  Ga terug naar het hoofdmenu met de pijl linksboven.



![image](assets/fr/13.webp)




### Mnemonic zin opslaan



Als je terug bent in het hoofdmenu, klik dan op "Back-up Wallet", lees dan de waarschuwingstekst die je informeert dat het verliezen van de 24 woorden die je gaat ontvangen gelijk staat aan het verliezen van toegang tot je fondsen, en dat iedereen die deze woorden naast jou heeft toegang heeft tot je fondsen. Geef ze nooit aan iemand.



Selecteer "I UNDERSTAND" onderaan het scherm. Klik dan op elk van de 24 woorden om ze te laten verschijnen en noteer ze zorgvuldig.



Je kunt het op papier schrijven of, voor extra veiligheid, op roestvrij staal graveren om het te beschermen tegen brand, overstroming of instorting. De keuze van het medium voor je Mnemonic hangt af van je beveiligingsstrategie, maar als je Zeus gebruikt als een onkosten Wallet met gematigde hoeveelheden, zou papier voldoende moeten zijn.



Voor meer informatie over de juiste manier om je Mnemonic zinsdeel op te slaan en te beheren, raad ik je aan deze andere tutorial te volgen, vooral als je een beginner bent:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Als je klaar bent, klik je op "I'VE BACKUP MY 24 WORDS" onderaan het scherm en zijn we terug op het beginscherm, klaar om onze eerste bitcoins te ontvangen.




## Optie 1 - On-Chain bitcoins ontvangen & een Lightning-kanaal openen



**Zeus Embedded** is in de eerste plaats ontworpen als embedded bliksemknooppunt, maar kan ook worden gebruikt als Wallet On-Chain.



Om On-Chain bitcoins te ontvangen, klik je op de knop "On-Chain" en vervolgens op "Ontvangen".


Scan tot slot de QR-code of kopieer de Bitcoin Address om geld te storten.



![image](assets/fr/15.webp)





Zodra het geld is bevestigd en bijgeschreven op je Wallet, kun je het gebruiken om een **Lightning-kanaal** te openen. Je Lightning-kanaal is je toegangspoort tot de Lightning Network, waardoor je Exchange bitcoins op een veel vertrouwelijkere en snellere manier kunt gebruiken.





- Klik hiervoor op "MOVE On-Chain FUNDS TO LIGHTNING"



Op het volgende scherm wordt u gevraagd om een kanaal te openen in samenwerking met **"Olympus by Zeus"**, de LSP (Lightning Service Provider) die Wallet verkiest.


In deze tutorial kiezen we deze optie omwille van de eenvoud, maar het is perfect mogelijk om kanalen te openen met elk knooppunt op het netwerk.


Het is zelfs mogelijk om meerdere kanalen in een enkele transactie te openen door "OPEN ADDITIONAL CHANNEL" te selecteren. *Maar hier gaan we dieper op in in een "geavanceerde" versie van de **Zeus Embedded**** tutorial.





- Selecteer dan het bedrag dat je aan dit kanaal wilt besteden. In ons geval worden al onze On-Chain fondsen gebruikt, dus activeren we de "Gebruik alle mogelijke fondsen" knop.





- Selecteer ten slotte de knop "OPEN CHANNEL" onderaan het scherm.



![image](assets/fr/16.webp)





Binnen enkele seconden is het kanaal tot stand gebracht en zijn we klaar om onze eerste Lightning-transacties uit te voeren. Op het beginscherm zien we een klein klokje naast ons Wallet saldo. Dit komt omdat we nog moeten wachten op 3 On-Chain bevestigingen voordat het kanaal echt functioneel is.



![image](assets/fr/17.webp)





Na de 3 bevestigingen zien we dat ons saldo nu is bijgeschreven op de Lightning-invoegtoepassing.



![image](assets/fr/18.webp)



Een klein detail: als we op het menu onderaan het scherm klikken om de status van onze bliksemkanalen te bekijken, zien we dat een klein deel van ons saldo niet beschikbaar is om uit te geven: we kunnen slechts 208253 satoshis uitgeven in plaats van de 210370 die we daadwerkelijk hebben. Dit is normaal, omdat het specifiek is voor het bliksemprotocol.



Tot slot moet worden opgemerkt dat onze partner Olympus zich het recht voorbehoudt om het kanaal naar eigen goeddunken te sluiten als het bijvoorbeeld niet wordt gebruikt. Om ervoor te zorgen dat ons kanaal behouden blijft, moeten we de LSP (Lightning Service Provider) betalen, zoals we in de volgende paragraaf zullen zien, via de 2e manier om een kanaal te openen.





## Bitcoins versturen via Lightning



Nu we ons kanaal aan de praat hebben, laten we eens kijken hoe we het kunnen gebruiken om een Invoice (Invoice) bliksem te betalen.



Klik hiervoor op de knop "Lightning" en vervolgens op "Verzenden".



![image](assets/fr/19.webp)





Kopieer op het volgende scherm uw Invoice in het daarvoor bestemde veld of scan het door op het pictogram rechtsboven te klikken. Schuif ten slotte de knop "Slide to Pay" naar rechts om te betalen.



![image](assets/fr/20.webp)






Wacht een paar seconden en de Invoice is afbetaald en je satoshi's hebben met de snelheid van het licht gereisd.



![image](assets/fr/21.webp)





Met Zeus kun je dan een biljet toevoegen om je betaling uit te drukken, of de route bekijken die je satoshi's aflegden voordat ze hun bestemming bereikten (en de kosten die alle tussenliggende knooppunten in rekening brachten). Dit is het soort functionaliteit dat we zo leuk vinden aan Wallet.



![image](assets/fr/22.webp)



Merk op dat in tegenstelling tot een Wallet zoals [Phoenix]([Plan ₿ Network - Phoenix](https://planb.network/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), met Zeus de route lokaal wordt berekend en niet wordt gedelegeerd naar een derde partij (ACINQ in het geval van Phoenix). Dus jij bent de enige die de ontvanger van de betaling kent. We verliezen een beetje efficiëntie (betalingen duren iets langer om te voltooien, maar we winnen veel op het gebied van privacy).





Door op het kleine pijltje onderaan het beginscherm te klikken, kun je ook onze betalingsgeschiedenis bekijken. Hier zien we in Green de 212.121 Sats ontvangen voor On-Chain, dan in rood respectievelijk de 211.756 Sats gebruikt om ons kanaal te openen, dan de 121.212 satoshis gebruikt om onze Invoice bliksem te betalen.



![image](assets/fr/23.webp)





## Optie 2 - Bitcoins direct ontvangen op Lightning



In plaats van handmatig een kanaal te openen, zoals we zojuist hebben gezien, is het mogelijk om direct geld te ontvangen via Lightning, zelfs zonder een bestaand kanaal, door gebruik te maken van Olympus, het Zeus LSP.




- Klik hiervoor op de knop "Lightning" op het beginscherm en vervolgens op "Ontvangen".
- Kies vervolgens het bedrag dat je wilt ontvangen in het vak "Bedrag" en selecteer de knop "Invoice CREËREN" onderaan het scherm.



![image](assets/fr/24.webp)





Het volgende scherm toont de Invoice die betaald moet worden om de satoshis te ontvangen. Er wordt ons verteld dat de LSP 10.000 Sats zal inhouden als de betaling wordt gedaan door Lightning. We zullen later zien hoe deze kosten voor het openen van kanalen worden gerechtvaardigd.



Betaal de Invoice of laat iemand anders het betalen en het kanaal wordt automatisch geopend, maar met aftrek van de afgesproken 10.000 Sats.



![image](assets/fr/25.webp)





We staan nu aan het hoofd van 2 bliksemkanalen, waarvan je de status kunt controleren door op de knop met de witte pijl onderaan het beginscherm te klikken.



We kunnen zien dat, in tegenstelling tot het kanaal dat geopend werd vanuit onze On-Chain schaal, het kanaal dat rechtstreeks door de bliksem werd geopend geen waarschuwing weergeeft.


Omdat je hebt betaald om dit kanaal op te zetten, verplicht de Lightning Service Provider (LSP) zich om het kanaal 3 maanden te onderhouden en biedt hij je "inkomende liquiditeit". Op het onderste kanaal kun je zien dat de ontvangstcapaciteit 96383 satoshis is. De LSP heeft dus kapitaal gebonden zodat je direct na het openen van het kanaal betalingen kunt ontvangen.



Dus de 10.000 Satoshi aan betaalde vergoedingen dekken: de kosten voor het openen van het kanaal (Bitcoin On-Chain transactie, de garantie om het kanaal 3 maanden te onderhouden en de kapitaalopslag).



![image](assets/fr/26.webp)





Gefeliciteerd, je bent nu klaar om Zeus Embedded te gebruiken, het Wallet mobiele verlichtingssysteem met de meest geavanceerde functies op de markt.





Om meer te weten te komen over de technische werking van Lightning Network, kun je de uitstekende gratis Plan ₿ Network training van Fanis Michalakis vinden:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb