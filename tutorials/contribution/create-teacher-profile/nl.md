---
name: Professor Plan ₿ Network
description: Hoe kan ik mijn docentenprofiel op Plan ₿ Network toevoegen of wijzigen?
---
![cover](assets/cover.webp)


Als je van plan bent bij te dragen aan Plan ₿ Network door een nieuwe tutorial of cursus te schrijven, heb je een docentprofiel nodig. Met dit profiel ontvang je de juiste credits voor de inhoud die je bijdraagt aan het platform.


Voor degenen die al betrokken zijn geweest bij het maken van educatieve inhoud op Plan ₿ Network, heb je waarschijnlijk al een docentenprofiel. Je kunt het vinden in de `/professors` map [op onze GitHub repository] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). Als je profiel al bestaat, vind dan je login in het `professor.yml` bestand.


Om je profiel te wijzigen, ga je naar het gedeelte "Je lerarenprofiel bewerken" aan het einde van deze handleiding.


## Voeg een nieuwe leraar toe met onze software


De makkelijkste manier om je leraarsprofiel op Plan ₿ Network aan te maken is door onze geïntegreerde Python-tool te gebruiken. Dit is hoe het werkt.


### 1 - Uw lokale omgeving configureren


Je moet je eigen Fork hebben van [Plan ₿ Network repository op GitHub] (https://github.com/PlanB-Network/Bitcoin-educational-content).


Synchroniseer de hoofdbranch (`dev`) van je Fork met het bronrepository.


Werk je lokale kloon bij.


```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```


### 2 - Maak een nieuwe tak


Zorg ervoor dat je op de `dev` branch zit. Maak een nieuwe branch aan met een beschrijvende naam (bijv. `add-professor-loic-morel`).


Publiceer deze tak op je Fork online.


```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```


### 3 - Maak je docentenprofiel aan


Ga naar de `scripts/tutorial-related/data-creator/` map op je lokale kloon. Zorg ervoor dat je alle afhankelijkheden hebt geïnstalleerd die nodig zijn voor de software, nadat je eerst Python hebt geïnstalleerd:


```bash
pip install -r requirements.txt
```


Start vervolgens de software met het commando:


```bash
python3 main.py
```


Eenmaal op de startpagina, voer je het lokale pad naar je repositorykloon in, de taal waarin je schrijft en je GitHub ID. Als je dit profiel voor iemand anders aanmaakt en al een Professor's profiel hebt, voer dan je ID in het "*PBN Professor's ID*" veld in. Als je je eigen profiel aanmaakt, zul je nog geen Professor's ID hebben, omdat je bezig bent er een aan te maken, dus laat dit veld leeg.


Klik dan op de knop "*New Professor*".


![Image](assets/fr/01.webp)


Vul de vereiste informatie in (merk op dat al deze informatie openbaar zal zijn op zowel ons platform als op GitHub):




- Naam van je lerarendossier (gebruik je voor- en achternaam of een pseudoniem, in kleine letters) ;
- Je naam of bijnaam ;
- Je website en profiel X (optioneel) ;
- Een Lightning Address om donaties van lezers te ontvangen (optioneel) ;
- Selecteer 2 of 3 tags uit de lijst;
- Klik op "*Select Image*" om een profielafbeelding te kiezen uit je lokale mappen (je kunt elke naam en formaat voor de afbeelding gebruiken en de software past deze automatisch aan. Zorg ervoor dat de afbeelding vierkant is);
- Schrijf een korte beschrijving van je profiel.


Rond het aanmaken af door op "*Create Professor*" te klikken. Dit zal automatisch alle benodigde bestanden voor je profiel generate maken.


![Image](assets/fr/02.webp)


Sla je wijzigingen lokaal op door een commit aan te maken met een verklarende boodschap. Push de wijzigingen naar je Fork GitHub.


```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```


Als je klaar bent, maak dan een Pull Request (PR) aan op GitHub om de integratie van je wijzigingen voor te stellen. Voeg een titel en een korte beschrijving toe aan de PR.


### 4 - Proeflezen en samenvoegen


Wacht op validatie of feedback van een beheerder. Breng indien nodig correcties aan en push nieuwe commits.


```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```


Als de PR samengevoegd is, kun je je werktak verwijderen.


## Je docentenprofiel aanpassen


Als je het gebruik van Git onder de knie hebt, pas dan je leraarsprofiel aan door een nieuwe branch aan te maken en het relevante bestand direct in je bestaande map te bewerken. Wijzigingen kunnen worden gemaakt in het `professor.yml` bestand of in het markdown bestand, afhankelijk van de informatie die gecorrigeerd moet worden. Als je je wijzigingen lokaal hebt gemaakt, push ze dan naar je Fork en dien een PR in.


Voor beginners raad ik aan om de wijziging direct via GitHub's Interface web te doen. Zorg ervoor dat je een GitHub account hebt. Als je niet weet hoe je er een moet aanmaken, volg dan deze tutorial:


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Ga naar [de Plan ₿ Network GitHub repository gewijd aan gegevens] (https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors).


![Image](assets/fr/03.webp)


Klik op de map "*professors*" en ga dan naar je persoonlijke map.


![Image](assets/fr/04.webp)


Om de metadata van je profiel te wijzigen, zoals Bliksem Address, naam of links, selecteer je het bestand "*professor.yml*". Om je beschrijving te wijzigen, klik je op het YAML-bestand voor jouw taal (bv. "*en.yml*" of "*fr.yml*").


Als je je beschrijving aanpast, vergeet dan niet om alle verouderde vertalingen te verwijderen. Dan kun je ofwel zelf zorgen voor het vertalen van je beschrijving in de andere talen met de hulp van een LLM, of alleen de beschrijving in je moedertaal laten staan en in je Pull Request vermelden dat je beschrijving door ons team vertaald moet worden.


![Image](assets/fr/05.webp)


Klik op het potloodpictogram in het bestand dat u wilt wijzigen.


![Image](assets/fr/06.webp)


Als je nog geen Fork van het Plan ₿ Network repository hebt, zal GitHub voorstellen dat je er een aanmaakt. Klik op "*Fork this repository*".


![Image](assets/fr/07.webp)


Breng de gewenste wijzigingen aan in het bestand. Klik op "*Wijzigingen vastleggen*" als je klaar bent.


![Image](assets/fr/08.webp)


Voer een bericht in waarin je je wijziging beschrijft en selecteer vervolgens "*Wijzigingen voorstellen*".


![Image](assets/fr/09.webp)


Een samenvatting van je wijzigingen wordt weergegeven. Als je nog meer wijzigingen in je profiel wilt aanbrengen, kun je teruggaan naar de mappen en nog meer commits doen. Als je klaar bent, klik je op "*Create pull request*".


Een Pull Request is een verzoek om wijzigingen van jouw branch te integreren in de hoofdbranch van het Plan ₿ Network repository, zodat wijzigingen bekeken en besproken kunnen worden voordat ze samengevoegd worden.


![Image](assets/fr/10.webp)


Zorg ervoor, bovenaan Interface, dat je werktak samengevoegd is met de `dev` tak van het Plan ₿ Network repository (dat is de hoofd tak).


Voer een titel in die kort de wijzigingen samenvat die je wilt samenvoegen met het bron repository. Voeg een korte opmerking toe die deze wijzigingen beschrijft en klik dan op de Green "*Create pull request*" knop om het pull request te bevestigen:


![Image](assets/fr/11.webp)


Je PR zal dan zichtbaar zijn op het tabblad "*Pull Request*" van het Plan ₿ Network repository. Je hoeft nu alleen nog maar te wachten tot een beheerder je wijziging samenvoegt.


![Image](assets/fr/12.webp)


Als je technische problemen ondervindt bij het indienen van je wijziging, aarzel dan niet om hulp te vragen op [onze Telegram-groep gewijd aan bijdragen](https://t.me/PlanBNetwork_ContentBuilder). Hartelijk dank!