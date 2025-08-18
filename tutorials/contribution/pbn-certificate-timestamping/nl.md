---
name: Timestamp of Plan ₿ Network diploma's
description: Begrijpen hoe Plan ₿ Network verifieerbare bewijzen afgeeft voor je certificaten en diploma's
---

![cover](assets/cover.webp)


Als je dit leest, is de kans groot dat je een ₿-CERT testcertificaat of een diploma van voltooiing hebt ontvangen voor een van de cursussen die je hebt gevolgd op planb.network, dus gefeliciteerd met deze prestatie!


In deze tutorial zullen we ontdekken hoe Plan ₿ Network verifieerbare bewijzen afgeeft voor uw ₿-CERT-testcertificaat of een Diploma voor het voltooien van een cursus. Vervolgens beschrijven we in een tweede deel hoe u de echtheid van deze bewijzen kunt verifiëren.


# Plan ₿ Network bewijsmechanisme


Op Plan ₿ Network ondertekenen we certificaten en diploma's cryptografisch en voorzien we ze van een tijdstempel met behulp van de Timechain (d.w.z. Bitcoin Blockchain), via een bewijsmechanisme dat berust op twee cryptografische operaties:


1. Een GPG-handtekening op een tekstbestand dat je prestaties samenvat

2. De tijdstempeling van hetzelfde ondertekende bestand via [opentimestamps](https://opentimestamps.org/).


Met de eerste bewerking kun je de uitgever van het certificaat (of diploma) bevestigen, terwijl je met de tweede bewerking de datum van uitgifte kunt controleren.

Wij geloven dat dit eenvoudige bewijsmechanisme ons in staat stelt om certificaten en diploma's uit te geven met onweerlegbaar bewijs dat iedereen onafhankelijk kan verifiëren.


![image](./assets/proof-mechanism.webp)


Dankzij dit bewijsmechanisme zal elke poging om zelfs maar het kleinste detail van je certificaat of diploma te veranderen, resulteren in een compleet andere SHA-256 Hash van het ondertekende bestand, wat onmiddellijk elke manipulatie onthult, aangezien zowel de handtekening als de Timestamp niet langer geldig zijn. Bovendien, als iemand probeert om certificaten of diploma's te vervalsen in naam van Plan ₿ Network, zal een eenvoudige verificatie van de handtekening de fraude aan het licht brengen.


## Hoe werkt de GPG-handtekening?


De GPG handtekening wordt gegenereerd met behulp van open-source software genaamd GNU Privacy Guard. Met deze software kunnen gebruikers eenvoudig privésleutels aanmaken, handtekeningen ondertekenen en verifiëren, en bestanden versleutelen en ontsleutelen. Voor deze tutorial is het belangrijk op te merken dat Plan ₿ Network GPG gebruikt om haar private/publieke sleutels te maken en om alle ₿-CERT Certificaten en Diploma's van Voltooiing van Cursussen te ondertekenen.


Aan de andere kant, als iemand de authenticiteit van een ondertekend bestand wil verifiëren, kan hij GPG gebruiken om de publieke sleutel van de uitgever te importeren en te verifiëren.


Wie nieuwsgierig is en meer wil weten over deze fantastische software, kan ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html) raadplegen


## Hoe werkt tijdstempelen?


Iedereen kan OpenTimestamps gebruiken om Timestamp een bestand te maken en verifieerbaar bewijs te verkrijgen van het bestaan ervan. Met andere woorden, het levert geen bewijs van wanneer het bestand is gemaakt, maar eerder bewijs dat het bestand niet later bestond dan een specifiek moment in de tijd.

OpenTimestamps levert deze service gratis door gebruik te maken van een zeer efficiënte methode om bewijs op te slaan in de Bitcoin Blockchain. Het gebruikt het SHA-256 Hash algoritme om een unieke identificatie voor uw bestand te creëren, en construeert een Merkle Tree met behulp van de hashes van de bestanden die door andere gebruikers zijn ingediend. Alleen de Hash van de Merkle Tree structuur is verankerd in een OP_RETURN transactie, wat zorgt voor een veilige en compacte manier om het bestaan van een bestand te verifiëren.

Als deze transactie eenmaal in een blok zit, kan iedereen met het initiële bestand en het bijbehorende `.ots`-bestand de echtheid van de tijdstempels verifiëren. In het tweede deel van de tutorial zullen we zien hoe je je Bitcoin Certificaat of een Diploma of Course Completion kunt verifiëren via een teminal en via een grafische Interface op de website van OpenTimestamps.


# Hoe een Plan ₿ Network ₿-CERT-certificaat of -diploma verifiëren


## Stap 1. Download je certificaat of diploma


Log in op je persoonlijke/studenten dashboard op planb.network.


![image](./assets/login.webp)


Ga naar "Credentials" door op het menu aan de linkerkant te klikken en selecteer je examensessie of je Diploma.


![image](./assets/credential.webp)


Het zip-bestand downloaden.


![image](./assets/download.webp)


Pak de inhoud uit door met de rechtermuisknop op het `.zip` bestand te klikken en "Uitpakken" te selecteren. Je zult drie verschillende bestanden vinden:



- Een ondertekend tekstbestand (bijv. certificate.txt)
- Een Open Timestamp (OTS) bestand (bijv. certificate.txt.ots)
- Een PDF-certificaat (bijv. certificate.pdf)


## Stap 2: Hoe kun je de handtekening van het tekstbestand verifiëren?


Ga eerst naar de map waar je de bestanden hebt uitgepakt en open een terminal (klik met de rechtermuisknop op het mapvenster en klik op "Open in Teminal"). Volg dan de onderstaande instructies.


1. Importeer de Plan ₿ Network publieke PGP-sleutel met het volgende commando:


```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```


U zou een bericht als het volgende moeten zien als u de PGP-sleutel met succes hebt geïmporteerd


```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```


OPMERKING: als je ziet dat er 1 sleutel is verwerkt en 0 sleutels zijn geïmporteerd, betekent dit waarschijnlijk dat je dezelfde sleutel al eerder hebt geïmporteerd, wat helemaal prima is.


2. Controleer de handtekening van het certificaat of diploma met het volgende commando:


```bash
gpg --verify certificate.txt
```


Dit commando zou je details over de handtekening moeten laten zien, inclusief:



- Wie ondertekende het (Plan ₿ Network)
- Toen het werd ondertekend
- Of de handtekening geldig is of niet


Dit is een voorbeeld van het resultaat:


```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```


Als je een bericht als "BAD signature" ziet, betekent dit dat er met het bestand geknoeid is.


## Stap 3: Controleer de Open Timestamp


### Verifiëren via een grafische Interface


1. Bezoek de website van OpenTimestamps: https://opentimestamps.org/

2. Klik op het tabblad "Stempelen & verifiëren".

3. Sleep het OTS-bestand (bijvoorbeeld `certificate.txt.ots`) naar het aangewezen gebied.

4. Sleep het bestand met tijdstempel (bijvoorbeeld `certificate.txt`) naar het aangewezen gebied.

5. De website controleert automatisch de open Timestamp en geeft het resultaat weer.


Als je een bericht als het volgende ziet, is de Timestamp geldig:


![cover](assets/opentimestamp_wegui_verified.webp)


### De CLI-Methode


OPMERKING: deze procedure **vereist een draaiend lokaal Bitcoin knooppunt**


1. Installeer de OpenTimestamps-client vanuit de officiële [repository] (https://github.com/opentimestamps/opentimestamps-client) door het volgende commando uit te voeren:


```
pip install opentimestamps-client
```


2. Navigeer naar de map met de uitgepakte certificaatbestanden.


3. Voer het volgende commando uit om de open Timestamp te verifiëren:


```
ots verify certificate.txt.ots
```


Deze opdracht zal:



- Vergelijk de Timestamp met de Blockchain van de Bitcoin
- Laat precies zien wanneer het bestand een tijdstempel kreeg
- De echtheid van de Timestamp bevestigen


### Eindresultaten


De verificatie is geslaagd als **beide** van de volgende berichten worden weergegeven:


1. De GPG-handtekening wordt gerapporteerd als **"Goede handtekening van Plan ₿ Network"**

2. De OpenTimestamps verificatie toont een specifiek Bitcoin blok Timestamp en rapporteert **"Succes! Bitcoin blok [blokhoogte] bevestigt dat gegevens bestonden vanaf [Timestamp]"**


Nu je weet hoe Plan ₿ Network verifieerbare bewijzen afgeeft voor elk ₿-CERT Certificaat en Diploma, kun je de integriteit ervan eenvoudig verifiëren.