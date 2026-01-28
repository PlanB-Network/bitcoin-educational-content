---
name: Sparrow Wallet - Stonewall
description: Inzicht in en gebruik van Stonewall-transacties op Sparrow
---

![cover](assets/cover.webp)




> *Doorbreek de aannames van blockchainanalyse met wiskundig bewijsbare twijfel tussen verzender en ontvanger van je transacties.*

## Wat is een Stonewall-transactie?



Stonewall is een specifieke vorm van Bitcoin transactie die ontworpen is om de vertrouwelijkheid van gebruikers te vergroten bij het uitgeven door een coinjoin tussen twee mensen na te bootsen, zonder er daadwerkelijk een te zijn. In feite werkt deze transactie niet samen. Een gebruiker kan hem zelf bouwen, met alleen de UTXO's die van hem zijn als invoer. Je kunt dus voor elke gelegenheid een Stonewall-transactie maken, zonder dat je hoeft te synchroniseren met een andere gebruiker.



De Stonewall-transactie werkt als volgt: als input voor de transactie gebruikt de emittent 2 UTXO die bij hem horen. Aan de outputzijde levert de transactie 4 outputs op, waarvan 2 van precies hetzelfde bedrag. De andere 2 zijn vreemde valuta. Van de 2 outputs van hetzelfde bedrag gaat er slechts één daadwerkelijk naar de begunstigde.



Er zijn dus maar 2 rollen in een Stonewall-transactie:




- De emittent, die de feitelijke betaling verricht ;
- De ontvanger, die zich mogelijk niet bewust is van de specifieke aard van de transactie en gewoon betaling verwacht van de verzender.



Laten we een voorbeeld nemen om deze transactiestructuur te begrijpen. Alice is bij de bakker om haar stokbrood te kopen, dat `4.000 sats` kost. Ze wil in bitcoins betalen, terwijl ze een vorm van vertrouwelijkheid over haar betaling behoudt. Dus besluit ze een Stonewall-transactie te bouwen voor de betaling.



![image](assets/fr/01.webp)



Door deze transactie te analyseren, kunnen we zien dat de bakker inderdaad `4.000 sats` heeft ontvangen als betaling voor het stokbrood. Alice gebruikte 2 UTXO's als input: één van `10.000 sats` en één van `15.000 sats`. Bij de output heeft het 3 UTXO teruggewonnen: een van `4.000 sats`, een van `6.000 sats` en een van `11.000 sats`. Alice heeft dus een nettosaldo van `- 4.000 sats` op deze transactie, wat goed overeenkomt met de prijs van het stokbrood.



In dit voorbeeld heb ik met opzet de mining vergoedingen weggelaten om het begrijpelijker te maken. In werkelijkheid worden transactiekosten volledig gedragen door de emittent.



## Wat is het verschil tussen Stonewall en Stonewall x2?



De Stonewall-transactie werkt identiek aan de StonewallX2-transactie, behalve dat deze laatste samenwerking vereist, in tegenstelling tot de klassieke Stonewall-transactie, vandaar de naam "x2". Dit komt omdat de Stonewall transactie wordt uitgevoerd zonder de noodzaak voor externe samenwerking: de verzender kan het uitvoeren zonder de hulp van een andere persoon. Bij een Stonewall x2 transactie daarentegen, voegt een extra deelnemer, bekend als de "medewerker", zich bij het proces. Hij of zij draagt zijn of haar eigen bitcoins bij aan de transactie, naast die van de verzender, en neemt aan het einde het hele bedrag over (minus de mining kosten).



Laten we teruggaan naar ons voorbeeld met Alice in de bakkerij. Als ze een Stonewall x2-transactie had willen doen, had Alice bij het opzetten van de transactie moeten samenwerken met Bob (een derde partij). Ze zouden elk een UTXO hebben ingebracht. Bob zou dan het volledige bedrag van zijn inbreng hebben ontvangen bij het verlaten van het bedrijf. De bakker zou op dezelfde manier als bij de Stonewall-transactie betaald zijn voor zijn stokbrood, terwijl Alice zijn oorspronkelijke saldo zou hebben teruggekregen, minus de kosten van het stokbrood.



![image](assets/fr/02.webp)



Vanuit het oogpunt van een buitenstaander zou de transactie precies hetzelfde zijn gebleven.



![image](assets/fr/03.webp)



Kortom, Stonewall- en Stonewall x2-transacties hebben een identieke structuur. Het onderscheid tussen de twee ligt in hun collaboratieve of niet-collaboratieve aard. De Stonewall-transactie wordt individueel ontwikkeld, zonder dat samenwerking nodig is. De Stonewall x2-transactie daarentegen is afhankelijk van samenwerking tussen twee individuen om het op te zetten.



[**-> Meer informatie over Stonewall transacties x2**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Wat is het nut van een Stonewall-transactie?



De Stonewall structuur voegt een enorme hoeveelheid entropie toe aan de transactie, waardoor de lijnen van ketenanalyse vervagen. Van buitenaf gezien kan zo'n transactie worden geïnterpreteerd als een kleine coinjoin tussen twee mensen. Maar in werkelijkheid is het, net als de Stonewall x2 transactie, een betaling. Deze methode zorgt dus voor onzekerheden in de ketenanalyse, of leidt zelfs tot valse aanwijzingen.



Laten we het voorbeeld nemen van Alice bij de bakker. De transactie op de blockchain zou er als volgt uitzien:



![image](assets/fr/04.webp)



Een buitenstaander die vertrouwt op de heuristiek van gewone ketenanalyse zou ten onrechte kunnen concluderen dat "*twee mensen een kleine coinjoin hebben gemaakt, met elk een UTXO als invoer en elk twee UTXO's als uitvoer*".



![image](assets/fr/05.webp)



Deze interpretatie is onnauwkeurig, want zoals je weet werd er één UTXO naar de bakker gestuurd, kwamen de 2 inkomende UTXO's van Alices en herstelde ze 3 ruiluitgangen.



![image](assets/fr/01.webp)



Zelfs als de externe waarnemer erin slaagt om de paterne van de Stonewall-transactie te identificeren, zal hij niet alle informatie hebben. Hij zal niet kunnen bepalen welke van de twee UTXO's met dezelfde bedragen overeenkomt met de betaling. Bovendien zal hij niet kunnen bepalen of de twee UTXO boekingen van twee verschillende mensen komen, of dat ze toebehoren aan één persoon die ze heeft samengevoegd. Dit laatste komt doordat de hierboven genoemde Stonewall x2 transacties precies hetzelfde patroon volgen als de Stonewall transacties. Van buitenaf gezien en zonder extra contextuele informatie is het onmogelijk om het verschil te zien tussen een Stonewall transactie en een Stonewall x2 transactie. De eerste zijn geen collaboratieve transacties, terwijl de laatste dat wel zijn. Dit voegt nog meer twijfel toe aan de kosten.



![image](assets/fr/03.webp)



## Hoe maak ik een Stonewall-transactie op Sparrow?



Oorspronkelijk ontwikkeld door het Samurai Wallet team, werden de Stonewall transacties overgenomen door de Ashigaru toepassing, een fork uit de originele portfolio die werd gecreëerd na de arrestatie van de Samurai ontwikkelaars, en ook op Sparrow Wallet.



Je moet Sparrow installeren en een :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

In tegenstelling tot Stowaway of Stonewall x2 (*cahoots*) transacties, vereisen Stonewall transacties geen gebruik van Paynyms. Ze kunnen direct worden uitgevoerd, zonder speciale voorbereiding of samenwerking met een andere gebruiker.



Om een Stonewall-transactie op Sparrow uit te voeren, is de procedure heel eenvoudig: begin met het aanmaken van een transactie zoals gebruikelijk, ofwel via het `Verstuur` menu, of via het `UTXO` menu als je *Coin Controle* wilt doen.



![Image](assets/fr/06.webp)



Voer vervolgens de transactiegegevens in: het adres van de ontvanger, een label, het te verzenden bedrag en het bedrag of tarief van de kosten, afhankelijk van de marktomstandigheden.



![Image](assets/fr/07.webp)



Voordat je bevestigt, kun je hier de Stonewall-structuur selecteren. Onderaan de interface vervang je `Efficiëntie` door `Privacy`. Als deze optie niet verschijnt, betekent dit dat je portefeuille niet voldoende UTXO's heeft om dit type transactie op te bouwen.



![Image](assets/fr/08.webp)



Nadat je de `Privacy` optie hebt geselecteerd, zul je zien dat de structuur van de transactie volledig is gewijzigd: het wordt een Stonewall transactie, die verschillende van je UTXO's als inputs verbruikt en twee outputs van identieke bedragen produceert, waarvan er één overeenkomt met de daadwerkelijke betaling van `100.000 sats`, naast de ruiloutputs.



![Image](assets/fr/09.webp)



Als alles correct is, klik je op `Transactie aanmaken`.



Je kunt dan je transactiegegevens nog een laatste keer controleren en op `Transactie voltooien voor ondertekening` klikken.



![Image](assets/fr/10.webp)



Onderteken vervolgens de transactie volgens de methode die specifiek is voor jouw portefeuille en klik op `Transactie uitzenden` om deze uit te zenden op het Bitcoin netwerk, in afwachting van bevestiging.



![Image](assets/fr/11.webp)



Je weet nu hoe een Stonewall transactie werkt op Sparrow Wallet en hoe je er een kunt maken. Om je te verdiepen in deze tools die ontworpen zijn om je onchain vertrouwelijkheid te versterken, nodig ik je uit om mijn BTC 204 training op Plan ₿ Academy te volgen:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c