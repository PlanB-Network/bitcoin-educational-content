---
name: Public Pool
description: Inleiding tot openbaar zwembad
---

![signup](assets/cover.webp)


**Public Pool** is niet zomaar een pool; het is wat ook wel een **Solo Pool** wordt genoemd. Als jouw Miner erin slaagt een blok Mining te maken, dan ontvang je de volledige Block reward, die niet gedeeld wordt met andere deelnemers van de pool of met de pool zelf.


**Public Pool** biedt alleen een **bloksjabloon** voor je Miner, zodat het zijn taak kan uitvoeren zonder dat je een **Bitcoin node** en de software die met je Miner communiceert, nodig hebt. Omdat je je rekenkracht niet samenvoegt met die van andere deelnemers, zijn je kansen om met succes een Mining blok te maken natuurlijk erg laag. Het lijkt een beetje op een loterijsysteem, waarbij soms een gelukkige de jackpot wint.


![signup](assets/1.webp)


Op het **Dashboard** van **Public Pool** staan nog enkele statistieken zoals het **Totaal Hashrate** van de pool en een verdeling van de verschillende soorten miners die aangesloten zijn op de pool.


![signup](assets/2.webp)


In de eerste paar regels zien we **Bitaxe** met 1323 **Bitaxe** aangesloten voor een totaal van 649TH/s. **Bitaxe** is een **Open source** project dat het mogelijk maakt om eenvoudig een chip van een **ASIC** zoals de **Antminer S19** te hergebruiken op een **opensource** elektronisch bord om een kleine Miner van 0,5TH/s voor 15W te maken. Dit is de Miner die we zullen gebruiken als voorbeeld voor deze tutorial.


## Een **Werker** toevoegen 👷‍♂️


![signup](assets/cover.webp)


Bovenaan de pagina kun je de pool Address **stratum+tcp://public-pool.io:21496** kopiëren.


Voer vervolgens in het veld **gebruiker** een **Bitcoin** Address in waarvan u de eigenaar bent.


Als je meerdere mijnwerkers hebt, kun je voor allemaal dezelfde Address invoeren zodat hun **hashrates** worden gecombineerd en verschijnen als één enkele Miner. Je kunt ze ook van elkaar onderscheiden door ze allemaal een eigen naam te geven. Voeg hiervoor **.workername** toe na de **Bitcoin** Address.


Gebruik ten slotte **'x'** voor het veld **wachtwoord**.


Voorbeeld: Als uw **Bitcoin** Address **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv'** is en u wilt uw Miner **" Brrrr"** noemen, dan zou u de volgende informatie invoeren in de Interface van uw Miner:



- **URL**: stratum+tcp://public-pool.io:21496
- **USER**: **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr'**
- **Wachtwoord**: **'x'**

Als je Miner een **Bitaxe** is, zijn de velden een beetje anders, maar de informatie blijft hetzelfde:


- **URL**: public-pool.io (hier moet je het deel aan het begin **'stratum+tcp://'** en het deel aan het eind **':21496'** dat in het poortveld wordt vermeld, verwijderen)
- **Poort**: 21496
- **Gebruiker**: **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr'**
- **Wachtwoord**: **'x'**


![signup](assets/3.webp)


Enkele minuten nadat u Mining hebt opgestart, kunt u uw gegevens zien op de **Public Pool** website door te zoeken naar uw Address.


## Dashboard


![signup](assets/4.webp)


Zodra je verbonden bent met **Public Pool**, kun je toegang krijgen tot je **Dashboard** door te zoeken met je **Bitcoin** Address die je hebt ingevoerd in het **User** veld. In ons geval is dat **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv'**.


Op het **Dashboard** wordt verschillende informatie weergegeven over je gegevens en over het netwerk.


![signup](assets/5.webp)


Je hebt **Network Hash Rate** dat overeenkomt met het totale werkvermogen van het **Bitcoin** netwerk.


De **Network Difficulty** geeft de moeilijkheidsgraad aan die bereikt moet worden om een blok te valideren.


En **Uw beste moeilijkheidsgraad** is de hoogste moeilijkheidsgraad die je hebt bereikt. Als je toevallig 🍀 de netwerk moeilijkheid bereikt, dan win je de hele Block reward... na 100 blokjes. Je moet dan 100 blokjes wachten voordat je ze kunt uitgeven.


Je hebt ook de **Block Height**, dat is het nummer van het laatste blok dat werd gedolven en het gewicht uitgedrukt in WU, met een maximum van 4.000.000.


Hieronder kun je alle statistieken van elk van je apparaten afzonderlijk zien als je ze een aparte naam hebt gegeven door **.name** toe te voegen achter je **Bitcoin** Address in het **User** veld.