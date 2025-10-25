---
name: Weblate - statische elementen vertalen
description: Hoe kun je deelnemen aan de vertaling van de statische elementen op planb.network?
---
![cover](assets/cover.webp)


De missie van Plan ₿ Network is om eersteklas educatieve bronnen over Bitcoin aan te bieden en deze in zoveel mogelijk talen te vertalen. Veel van de inhoud die op de site wordt gepubliceerd is open-source en wordt gehost op GitHub, zodat iedereen kan deelnemen aan het verrijken van het platform. Bijdragen kunnen verschillende vormen aannemen: het corrigeren en proeflezen van bestaande inhoud, het bijwerken van informatie of het creëren van nieuwe tutorials om toe te voegen aan het platform.


In deze tutorial laten we je zien hoe je eenvoudig kunt bijdragen aan de vertaling van de statische elementen op onze website. De gegevens op het platform zijn verdeeld in twee hoofdcategorieën:


- de frontend gegevens/statische elementen (pagina's, knoppen, enz.);
- de educatieve inhoud (tutorials, cursussen, bronnen...).


Om de educatieve inhoud te vertalen, gebruiken we [kunstmatige intelligentie] (https://github.com/Asi0Flammeus/LLM-Translator). Om eventuele fouten in deze bestanden te corrigeren, nodigen we proeflezers uit om bij te dragen. Als je inhoud wilt proeflezen, raadpleeg dan de volgende handleiding:


https://planb.network/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017

Aan de andere kant, als je geïnteresseerd bent in het vertalen van de statische elementen van de website (met uitzondering van educatieve inhoud), ben je op de juiste plaats! Om de frontend effectief te vertalen, gebruiken we de tool Weblate, die heel eenvoudig te gebruiken is en de aanpak van de vertaling vergemakkelijkt.


Als je een compleet nieuwe taal aan Plan ₿ Network wilt toevoegen, neem dan contact op met het Plan ₿ Network team via onze [Telegram groep] (https://t.me/PlanBNetwork_ContentBuilder). Als je geen telegram hebt, kun je een e-mail sturen naar mari@planb.network. Zorg ervoor dat je een kleine presentatie schrijft over wie je bent en welke talen je spreekt.

Onze teamleden zullen je specifieke instructies geven en de gerelateerde "issues" openen op Github om je werk te coördineren.


Volg eerst deze specifieke tutorial om een nieuwe taal toe te voegen aan de Weblate.


https://planb.network/tutorials/contribution/content/weblate-add-new-language-eef2f5c0-1aba-48a3-b8f0-a57feb761d86

Als je klaar bent om te beginnen met vertalen, kom dan terug naar deze tutorial en neem de volgende punten door.


## Registreren op de Weblate



- Ga naar [de zelf gehoste Weblate van Plan ₿ Network](https://weblate.planb.network/):

![weblate](assets/01.webp)


- Als je al een Weblate-account hebt, klik je op `Sign in` (Aanmelden):

![weblate](assets/02.webp)


- Als je nog geen account hebt, klik je op `Register` (Registreren):

![weblate](assets/03.webp)


- Voer je e-mailadres adres in, evenals een gebruikersnaam en volledige naam (je kunt een pseudoniem gebruiken), klik dan op `Register` (Registreren):

![weblate](assets/04.webp)


- In de inbox van je e-mail zou je een bevestigingsbericht van Weblate moeten hebben ontvangen. Klik op de link om je registratie te bevestigen:

![weblate](assets/05.webp)


- Kies een sterk wachtwoord en klik vervolgens op `Change my password` (Verander mijn wachtwoord):

![weblate](assets/06.webp)


- Je kunt nu teruggaan naar het Plan ₿ Network dashboard:

![weblate](assets/07.webp)


## Beginnen met vertalen



- Klik op het project `Website element` (niet de woordenlijst):

![weblate](assets/08.webp)


- Je komt bij een overzicht, waar je de talen in uitvoering kunt zien:

![weblate](assets/09.webp)


- Kies je taal. Laten we bijvoorbeeld Frans nemen:

![weblate](assets/10.webp)


- Klik op de knop `Translate` (Vertaal) om te beginnen met vertalen:

![weblate](assets/11.webp)


- Je wordt doorgestuurd naar de werk omgeving:

![weblate](assets/12.webp)


- De Weblate zal dan automatisch zinnen, paragrafen of zelfs woorden voorstellen om te vertalen in het `taal` vak `. In jouw geval zie je waarschijnlijk de Engelse hoofdstring en een ander tekstvak voor jouw taal:

![weblate](assets/13.webp)


- Jouw taak bestaat uit het vertalen van de aangegeven strings. Je moet je tekst invoegen in het vak dat overeenkomt met de taal die je hebt gekozen. Als je bijvoorbeeld aan de Franse versie werkt, schrijf je je vertaling in het vak `Frans`:

![weblate](assets/14.webp)


- Klik op het tabblad `Automatic suggestion` (Automatische suggestie):

![weblate](assets/15.webp)


- Hier laat de Weblate je een vertaling zien die door kunstmatige intelligentie is gemaakt:

![weblate](assets/16.webp)


- Als de voorgestelde vertaling relevant voor je lijkt, kun je op de knop `Clone to translation` (Clonen naar vertaling) klikken:

![weblate](assets/17.webp)


- De suggestie wordt nu in je werkvak geplaatst:

![weblate](assets/18.webp)


- Je kunt de suggestie dan handmatig aanpassen:

![weblate](assets/19.webp)


- Als de vertaling je bevredigend lijkt, klik je op de knop `Save and Continue` (Opslaan en doorgaan). Zorg ervoor dat je het vinkje weghaalt bij "Needs editing" (Moet bewerkt worden) als je zeker bent van je vertaling:

![weblate](assets/20.webp)


- Ziezo! Je vertaling is succesvol opgeslagen. De Weblate zal je automatisch doorverwijzen naar het volgende te vertalen item. Als je teruggaat naar het dashboard dat overeenkomt met jouw taal, zie je dat elk type string een andere vertaalstatus heeft. Als je je bijvoorbeeld alleen wilt concentreren op "untranslated strings" (onvertaalde strings), kun je op de specifieke tab klikken:

![weblate](assets/21.webp)


- Als je naar een specifiek woord moet zoeken, in jouw taal of in de oorspronkelijke taal, klik dan op "search" (zoeken) en voeg het daar in:

![weblate](assets/22.webp)


## Richtlijnen voor vertalingen



- Als je woorden vindt die tussen accolades "{" staan, hoef je ze niet te vertalen. Bijvoorbeeld, in "Uw account is aangemaakt, {{userName}}!", vertaal je de hele zin, maar behoud je "gebruikersnaam" in het Engels.
- Als je "Plan ₿ Network" in een string tegenkomt, zorg er dan voor dat je het woord "netwerk" NIET vertaalt (beschouw Plan ₿ Network als een handelsmerk). Gebruik trouwens altijd de ₿ van Bitcoin!
- Als je het woord "netwerk" alleen tegenkomt, kun je het in plaats daarvan vertalen.
- Vertaal "B-CERT" niet, want dat is een ander vast woord.
- Als je strings tegenkomt die eindigen met een spatie, kun je die laten staan.
- Sommige strings kunnen een spatie bevatten tussen het laatste woord en een leesteken: laat deze niet staan in je doeltaal, tenzij de grammatica dit impliceert. Bijvoorbeeld, "Contactinformatie :" moet worden gecorrigeerd in "Contactinformatie:". Vertaal het in dit geval op de juiste manier. Je kunt ook een opmerking toevoegen om de beheerders op de hoogte te stellen van dit probleem in de originele Engelse versie.


## Nieuwe functies


- We werken aan het toevoegen van een "explanation"-sectie (uitleg) voor elke string, samen met een screenshot, om je te helpen vinden waar een specifieke zin/woord op de website staat. Op dit moment kun je, als je twijfels hebt over bepaalde woorden en hun specifieke locatie op de website wilt vinden, een vraag stellen in de "comments"-sectie (opmerkingen) of aan de vertaalcoördinator vragen in de Telegram-groep die aan het begin van deze tutorial wordt genoemd.

![weblate](assets/23.webp)


Alvast bedankt voor je bijdrage aan de vertaling van Plan ₿ Network! Als je specifieke vragen of opmerkingen voor ons hebt, neem dan gerust contact met ons op via de [Telegram groep](https://t.me/PlanBNetwork_ContentBuilder).
