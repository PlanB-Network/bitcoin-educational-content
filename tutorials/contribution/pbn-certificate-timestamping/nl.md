---
name: Tijdstempel van Plan ₿ Academy diploma's
description: Begrijpen hoe Plan ₿ Academy verifieerbare bewijzen afgeeft voor je certificaten en diploma's
---

![cover](assets/cover.webp)


Als je dit leest, is de kans groot dat je een ₿-CERT testcertificaat of een diploma van voltooiing hebt ontvangen voor een van de cursussen die je hebt gevolgd op planb.network, dus gefeliciteerd met deze prestatie!


In deze tutorial zullen we ontdekken hoe Plan ₿ Academy verifieerbare bewijzen afgeeft voor je ₿-CERT-testcertificaat of elk diploma voor het voltooien van een cursus. Vervolgens beschrijven we in een tweede deel hoe je de echtheid van deze bewijzen kunt verifiëren.


## Plan ₿ Academy bewijsmechanisme


Op Plan ₿ Academy ondertekenen we certificaten en diploma's cryptografisch en voorzien we ze van een tijdstempel met behulp van de Timechain (d.w.z. Bitcoin blockchain), via een bewijsmechanisme dat berust op twee cryptografische operaties:


1. Een GPG-handtekening op een tekstbestand dat je prestaties samenvat

2. De tijdstempeling van hetzelfde ondertekende bestand via [opentimestamps](https://opentimestamps.org/).


Met de eerste bewerking kun je de uitgever van het certificaat (of diploma) bevestigen, terwijl je met de tweede bewerking de datum van uitgifte kunt controleren.

Wij geloven dat dit eenvoudige bewijsmechanisme ons in staat stelt om certificaten en diploma's uit te geven met onweerlegbaar bewijs dat iedereen onafhankelijk kan verifiëren.


![image](./assets/proof-mechanism.webp)


Dankzij dit bewijsmechanisme zal elke poging om zelfs maar het kleinste detail van je certificaat of diploma te veranderen, resulteren in een compleet andere SHA-256 hash van het ondertekende bestand, wat onmiddellijk elke manipulatie onthult, aangezien zowel de handtekening als de tijdstempel niet langer geldig zijn. Bovendien, als iemand probeert om certificaten of diploma's te vervalsen in naam van Plan ₿ Academy, zal een eenvoudige verificatie van de handtekening de fraude aan het licht brengen.


### Hoe werkt de GPG-handtekening?


De GPG handtekening wordt gegenereerd met behulp van open-source software genaamd GNU Privacy Guard. Met deze software kunnen gebruikers eenvoudig privésleutels aanmaken, ondertekenen en handtekeningen verifiëren, en bestanden versleutelen en ontsleutelen. Voor deze tutorial is het belangrijk op te merken dat Plan ₿ Academy GPG gebruikt om haar private/publieke sleutels te maken en om alle ₿-CERT Certificaten en Diploma's van cursus voltooiing te ondertekenen.


Aan de andere kant, als iemand de authenticiteit van een ondertekend bestand wil verifiëren, kan hij GPG gebruiken om de publieke sleutel van de uitgever te importeren en te verifiëren.


Wie nieuwsgierig is en meer wil weten over deze fantastische software, kan ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html) raadplegen.


### Hoe werkt tijdstempelen?


Iedereen kan OpenTimestamps gebruiken om een bestand te timestempelen en verifieerbaar bewijs te verkrijgen van het bestaan ervan. Met andere woorden, het levert geen bewijs van wanneer het bestand is gemaakt, maar eerder bewijs dat het bestand niet later bestond dan een specifiek moment in de tijd.

OpenTimestamps levert deze service gratis door gebruik te maken van een zeer efficiënte methode om bewijs op te slaan in de Bitcoin blockchain. Het gebruikt het SHA-256 hash algoritme om een unieke identificatie voor je bestand te creëren, en construeert een Merkle Tree met behulp van de hashes van de bestanden die door andere gebruikers zijn ingediend. Alleen de hash van de Merkle Tree structuur is verankerd in een OP_RETURN transactie, wat zorgt voor een veilige en compacte manier om het bestaan van een bestand te verifiëren.

Als deze transactie eenmaal in een blok zit, kan iedereen met het initiële bestand en het bijbehorende `.ots`-bestand de echtheid van de tijdstempels verifiëren. In het tweede deel van de tutorial zullen we zien hoe je je Bitcoin Certificaat of een Diploma van cursus voltooiing kunt verifiëren via een teminal en via een grafische interface op de website van OpenTimestamps.


## Hoe een Plan ₿ Academy ₿-CERT-certificaat of -diploma verifiëren


### Stap 1. Download je certificaat of diploma


Log in op je persoonlijke/studenten dashboard op planb.network.


![image](./assets/login.webp)


Ga naar "Credentials" door op het menu aan de linkerkant te klikken en selecteer je examensessie of je diploma.


![image](./assets/credential.webp)


Download het zip-bestand.


![image](./assets/download.webp)


Pak de inhoud uit door met de rechtermuisknop op het `.zip` bestand te klikken en "Extract" (Uitpakken) te selecteren. Je zult drie verschillende bestanden vinden:



- Een ondertekend tekstbestand (bijv. certificate.txt)
- Een Open Timestamp (OTS) bestand (bijv. certificate.txt.ots)
- Een PDF-certificaat (bijv. certificate.pdf)


### Stap 2: Hoe kun je de handtekening van het tekstbestand verifiëren?


Ga eerst naar de map waar je de bestanden hebt uitgepakt en open een terminal (klik met de rechtermuisknop op het mapvenster en klik op "Open in Teminal"). Volg dan de onderstaande instructies.


1. Importeer de Plan ₿ Academy publieke PGP-sleutel met het volgende commando:


```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/Plan ₿ Academy-pk.asc | gpg --import
```


Je zou een bericht als het volgende moeten zien als je de PGP-sleutel met succes hebt geïmporteerd.


```
gpg: key 8F12D0C63B1A606E: public key "Plan ₿ Academy (used for Plan ₿ Academy platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```


OPMERKING: als je ziet dat er 1 sleutel is verwerkt en 0 sleutels zijn geïmporteerd, betekent dit waarschijnlijk dat je dezelfde sleutel al eerder hebt geïmporteerd, wat helemaal prima is.


2. Controleer de handtekening van het certificaat of diploma met het volgende commando:


```bash
gpg --verify certificate.txt
```


Dit commando zou je details over de handtekening moeten laten zien, inclusief:



- Wie ondertekende het (Plan ₿ Academy)
- Wanneer het werd ondertekend
- Of de handtekening geldig is of niet


Dit is een voorbeeld van het resultaat:


```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "Plan ₿ Academy (used for Plan ₿ Academy platform) <admin@planb.network>" [unknown]
```


Als je een bericht als "BAD signature" ziet, betekent dit dat er met het bestand geknoeid is.


### Stap 3: Controleer de Open Timestamp


#### Verifiëren via een grafische interface


1. Bezoek de website van OpenTimestamps: https://opentimestamps.org/

2. Klik op het tabblad "Stamp & Verify".

3. Sleep het OTS-bestand (bijvoorbeeld `certificate.txt.ots`) naar het aangewezen gebied.

4. Sleep het bestand met de tijdstempel (bijvoorbeeld `certificate.txt`) naar het aangewezen gebied.

5. De website controleert automatisch de open timestamp en geeft het resultaat weer.


Als je een bericht als het volgende ziet, is de tijdstempel geldig:


![cover](assets/opentimestamp_wegui_verified.webp)


#### De CLI-Methode


OPMERKING: deze procedure **vereist een draaiende lokale Bitcoin node**


1. Installeer de OpenTimestamps-client vanuit de officiële [repository](https://github.com/opentimestamps/opentimestamps-client) door het volgende commando uit te voeren:


```
pip install opentimestamps-client
```


2. Navigeer naar de map met de uitgepakte certificaatbestanden.


3. Voer het volgende commando uit om de open timestamp te verifiëren:


```
ots verify certificate.txt.ots
```


Deze opdracht zal:



- de Timestamp met de Bitcoin blockchain vergelijken
- precies laten zien wanneer het bestand een tijdstempel kreeg
- de echtheid van de Timestamp bevestigen


#### Eindresultaten


De verificatie is geslaagd als **beide** van de volgende berichten worden weergegeven:


1. De GPG-handtekening wordt gerapporteerd als **"Good signature from Plan ₿ Academy"**

2. De OpenTimestamps verificatie toont een specifiek Bitcoin Timestamp blok  en rapporteert **"Success! Bitcoin block [blockheight] attests data existed as of [timestamp]"**


Nu je weet hoe Plan ₿ Academy verifieerbare bewijzen afgeeft voor elk ₿-CERT Certificaat en Diploma, en kan je de integriteit ervan eenvoudig verifiëren.
