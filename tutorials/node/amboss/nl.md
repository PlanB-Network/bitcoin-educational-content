---
name: Amboss
description: Lightning Network verkennen en analyseren
---

![cover](assets/cover.webp)



Lightning Network is een Layer van het Bitcoin protocol, dat in de eerste plaats werd ontwikkeld om de adoptie van Bitcoin betalingen op een dagelijkse basis te bevorderen door de verwerkingssnelheid van elke transactie te verhogen. Gebaseerd op het principe van decentralisatie, bestaat Lightning Network uit nodes (computers met een Lightning-implementatie) die peer-to-peer communiceren en gegevens (betalingen en betalingsverificatie) aan elkaar doorgeven.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Net als op de hoofdketen, is het essentieel geworden om gebruikers in staat te stellen de informatie en status van het netwerk te kennen, om verbindingen tussen knooppunten te vergemakkelijken en het liquiditeitsprobleem dat zich meestal voordoet op het netwerk te minimaliseren. Op Lightning Network raden we inderdaad microbetalingen aan van relatief kleinere bedragen dan die voor transacties op de hoofdketen van Bitcoin.



Het is belangrijk om te weten dat niet alle Lightning nodes beschikbaar zijn op het Amboss platform.



Net als [Mempool Space](https://Mempool.space), dat nuttige informatie geeft over de hoofdketen van het Bitcoin protocol, geeft [Amboss](https://amboss.space) sinds 2022 informatie over :





- Knooppunten op de Lightning Network
- Betalingskanalen en hun betalingscapaciteit
- Lightning Network evolutie in de tijd
- Statistieken over kosten voor betalingen aan relaisknooppunten.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

In deze tutorial nemen we je mee op een tour door dit platform, dat een essentiële bron is voor Lightning Network gebruikers, diegenen die hun node willen aansluiten om het netwerk uit te breiden, enz.




## Zoek paren



Een van de doelen van het Amboss platform is om de verschillende knooppunten in het netwerk met elkaar te verbinden en informatie met elkaar te laten communiceren. Op de startpagina van het platform kun je direct zoeken naar de naam van een knooppunt dat je al kent, of knooppunten vinden van de populairste Lightning-portefeuilles die je gebruikt.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Op de startpagina vind je ook knooppunten die zijn ingedeeld volgens :




- Capaciteitsontwikkeling: de hoeveelheid Bitcoin geassocieerd met de openbare sleutel van het knooppunt en het totaal beschikbare in al zijn kanalen.
- Kanalenevolutie: het aantal nieuwe verbindingen met andere knooppunten in het netwerk.
- Node populariteit: hoe vaak het knooppunt wordt gebruikt.



![nodes](assets/fr/03.webp)



Het kiezen van het juiste knooppunt om verbinding mee te maken komt dus neer op het controleren van de volgende criteria:





- Zorg ervoor dat het knooppunt voldoende bitcoins heeft; hoe groter de capaciteit van het knooppunt, hoe meer bitcoins je kunt betalen.





- Zorg ervoor dat het knooppunt een groot aantal verbindingen en open kanalen heeft met andere knooppunten in het netwerk.





- Controleer of het knooppunt actief is en nog steeds gewaardeerd wordt door zijn peers door het aantal nieuwe kanalen te controleren; hoe meer nieuwe kanalen dit knooppunt open heeft, hoe meer het gewaardeerd wordt door de andere knooppunten in het netwerk.



Als je het juiste knooppunt hebt gevonden, klik je op de naam om naar de informatiepagina van het knooppunt te gaan.



Op deze Interface, door de Timestamp van het nieuw aangemaakte kanaal te controleren, krijg je een aanwijzing over de activiteit van dit knooppunt. Je vindt hier ook informatie over de capaciteit van de kanalen van dit knooppunt: deze informatie is van vitaal belang als je dit knooppunt actief wilt gebruiken om je betalingen te doen.




![node_info](assets/fr/04.webp)



In het linkerdeel vind je meer details over de locatie van dit knooppunt. U kunt bijvoorbeeld :




- De openbare sleutel: de identifier net onder de knooppuntnaam.
- De geografische positie van dit knooppunt.




![channels](assets/fr/05.webp)



Deze Interface vertelt je de Address verbinding voor dit knooppunt: het heeft de vorm `pubkey@ip:port`. In ons voorbeeld willen we verbinden met het knooppunt waarvan de :




- de openbare sleutel `pubkey` is: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- De poort: `9735`



![geoinfo](assets/fr/06.webp)



In het **Kanalen** gedeelte zie je de lijst met open kanalen en de verbindingen van het knooppunt met andere knooppunten in het netwerk. Op deze Interface zijn verschillende stukjes informatie van vitaal belang om te bevestigen dat dit knooppunt aan onze behoeften voldoet of betrouwbaar is:





- Inkomend tarief**: Het bedrag dat het knooppunt je in rekening brengt voor elk miljoen Satoshi dat het ontvangt, afhankelijk van het gekozen kanaal.
- De verhouding (deeltjes per miljoen)** : die staat voor het aantal Satoshi per miljoen eenheden dat het knooppunt je in rekening brengt als je besluit een betaling te doen via een van zijn kanalen. Stel dat je besluit een betaling van `10_000 Sats` te doen via een kanaal waarvan de ppm-verhouding `500 Sats` is, dan moet je de knoop `10_000 * 500 / 1_000_000` satoshis betalen, wat overeenkomt met `5 Sats`.
- Het [HTLC](https://planb.academy/resources/glossary/htlc) maximum** : Het maximale bedrag dat dit knooppunt toestaat om door te sturen via een van deze kanalen.



Door de tabel in deze Interface te raadplegen, kun je al deze informatie ook vinden op het knooppunt waaraan het is gekoppeld.



![channels_info](assets/fr/07.webp)



In het gedeelte **Kanaalkaarten** zie je de verdeling en capaciteit van de verschillende kanalen op dit knooppunt. Je kunt de getoonde verdelingscriteria wijzigen door een van de opties in de vervolgkeuzelijst aan de rechterkant te selecteren.



![cha_maps](assets/fr/08.webp)



De sectie **Gesloten kanalen** groepeert alle voormalige kanalen van het knooppunt volgens het type sluiting:




- Wederzijds sluiten**: vertegenwoordigt de overeenkomst van beide partijen, die hun privésleutel gebruiken om de transactie te ondertekenen die het sluiten van het kanaal en de verdeling van saldi binnen het kanaal markeert
- Een **geforceerde sluiting**: staat voor de abrupte, eenzijdige sluiting van een deel van het kanaal. Dit type sluiting wordt niet aangeraden, omdat Lightning Network een straf-gebaseerd protocol is: wanneer je probeert het saldo van een kanaal te frauderen, riskeer je al je beschikbare saldo in dat kanaal te verliezen.



![closed](assets/fr/09.webp)



Informatie over doorvoerkosten voor het routeren van je betalingen via een kanaal op het knooppunt dat je gebruikt



![fees](assets/fr/10.webp)



## Netwerkinformatie



Amboss richt zich niet alleen op informatie over netwerkleden, maar ook op de toestand van het netwerk zelf.



In het gedeelte **Statistieken**, onder het menu "Simulaties" aan de linkerkant, vind je een grafiek die de waarschijnlijkheid van een succesvolle betaling weergeeft als functie van het betalingsbedrag.



In feite zul je zien dat de curve afneemt, want als het bedrag van je betaling toeneemt, heb je minder kans dat die betaling wordt uitgevoerd. Dit weerspiegelt het echte liquiditeitsprobleem op Lightning Network. Bijvoorbeeld, jouw betaling van `10_000` satoshis heeft een `79%` kans om gedaan te worden. Aan de andere kant, voor een betaling van `3_000_000` satoshis heb je minder dan `13%` kans van slagen.



![network](assets/fr/11.webp)



Met het menu **Netwerkstatistieken** kun je statistieken grafisch weergeven voor :




- Betalingskanalen
- Knooppunten
- Capaciteit
- Vergoedingen
- De evolutie van het kanaal.



![network_stat](assets/fr/12.webp)



In het menu **Marktstatistieken** kun je met de optie **Orderdetails** de vraag naar liquiditeit op de Lightning Network bekijken. Deze grafiek kan ook laten zien naar welke kanalen de meeste vraag is en/of welke een aanzienlijke capaciteit hebben.



![markets](assets/fr/13.webp)




## Gereedschap



Amboss biedt een aantal tools om je te helpen je zoekopdrachten en acties te optimaliseren.



### Lightning Network decoder



Dit hulpmiddel is voornamelijk verantwoordelijk voor het geven van details over de structuur van een Lightning Invoice, Lightning Address of Lightning URL.



Op de startpagina, in de sectie **Tools**, geef je bijvoorbeeld je Lightning Address op.



![decoder](assets/fr/14.webp)



Met deze decoder kun je informatie verkrijgen zoals :




- de publieke sleutel van het knooppunt die geassocieerd is met uw Lightning Address;
- De verlooptijd van een Invoice uit je Address;
- Het minimum en maximum dat je kunt verzenden;
- Het Nostr-knooppunt dat is gekoppeld aan uw Address, als Nostr is ingeschakeld op dit knooppunt.



![decode](assets/fr/15.webp)



### Magma IA



Ontdek de nieuwste tool van Amboss om uw verbindingen met Lightning Network nodes efficiënt te beheren. Magma AI gebruikt specifieke kunstmatige intelligentie om zich te richten op een belangrijk probleem: het maken van een goede selectie van nodes om mee te verbinden.



![magma](assets/fr/16.webp)



### Satoshi rekenmachine



Ontdek de huidige prijs van Bitcoin in jouw lokale valuta (EUR / USD). Gebruik op de startpagina de satoshis calculator om de huidige marktprijs te vinden.



![calculator](assets/fr/17.webp)




Je hebt nu een complete rondleiding gehad door de functies en analysehulpmiddelen van het platform. Hieronder vind je ons artikel over de Bitcoin **Mempool.space** verkenner.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f