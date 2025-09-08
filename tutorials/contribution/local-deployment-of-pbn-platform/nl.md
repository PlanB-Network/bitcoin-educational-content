---
name: Handleiding voor het lokaal draaien van het Plan ₿ Network platform
description: Hoe kunt u de Plan ₿ Network in een lokale omgeving laten draaien om mijn bijdrage aan inhoud of het proeflezen/beoordelen van educatieve inhoud op de Plan ₿ Network te testen?
---
![github](assets/cover.webp)


## Samengevat


Deze tutorial geeft stapsgewijze instructies voor het opzetten van het Bitcoin Leerbeheersysteem vanuit Plan ₿ Network op je lokale machine met behulp van Docker, dummy keys en aangepaste repository configuraties.


Als je het gedeelte hierboven niet begreep, maak je dan geen zorgen - deze tutorial is voor jou!


---

## **Hoe Bitcoin Leerbeheersysteem Lokaal draaien**


Deze tutorial geeft gedetailleerde stappen om het platform in te stellen, dummy keys te verwerken en repositories aan te passen. Volg de onderstaande stappen om veelvoorkomende problemen te voorkomen en je lokale omgeving goed te configureren.



**1. Vereisten**


- Linux machine met Docker en Docker Compose geïnstalleerd (er is gemeld dat het ook op Windows werkt).
- voldoende `nodejs` versie (getest: 22.12.0)
- `pnpm` geïnstalleerd op je systeem.
- Git geconfigureerd voor het klonen van repositories.



**2. Kloon het archief**

Kloon het archief naar je lokale machine:


git kloon [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-systeem


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. Omgevingsvariabelen instellen**


1\. Dupliceer het bestand `.env.example`:


```bash
cp .env.example .env
```


1. Bewerk het `.env` bestand en verwijder het .example gedeelte van de naam, nu moet je dummy sleutels toevoegen voor de benodigde variabelen. Voorbeeld:


⚠️ Dit is een verplichte stap, het overslaan ervan zal resulteren in fouten zoals verbindingsweigering tussen sommige containers.


Vergeet niet om uw speciale Github PAT ook toe te voegen in het bestand



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4. Afhankelijkheden installeren**


zorg ervoor dat je een geschikte nodejs versie hebt geïnstalleerd. Vanaf 2024-12 is bewezen dat v22.12.0 (LTS) werkt.



⚠️ Ubuntu 22.04 repository nodejs versie is 12.22.9: te oud om pnpm te installeren



Om nodejs te installeren, vind je instructies [hier](https://nodejs.org/en/download/package-manager); je kunt er bijvoorbeeld voor kiezen om `nvm` installatiemethode te gebruiken.


---

Voordat je begint met pnpm installeren van de benodigde pakketten, moet je ervoor zorgen dat alle afhankelijkheden geïnstalleerd zijn. Dit kun je bereiken door het volgende commando uit te voeren:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

Voer in de map `../Bitcoin-learning-management-system/` het volgende commando uit om `pnpm` te installeren


```bash
pnpm install
```


__TIP:__Neem in gedachten dat je van tijd tot tijd zowel de afhankelijkheden als pnpm zelf moet bijwerken



**5. Voer de containers** uit

Start in je `../Bitcoin-learning-management-system/` map de ontwikkelomgeving met Docker:


```bash
docker compose up --build -V
```

Als je het volgende commando ook op deze manier uitvoert, zie je de logs niet in je terminal.

```bash
docker compose up -d --build -V
```


Dit zal alle nodige containers van dockers bouwen en starten.


**6. Toegang tot de toepassing**

Zodra de containers draaien, opent u de frontend op:

\[<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Network Local](assets/en/1.webp)


Opmerking: de app wordt automatisch opnieuw geladen als je bronbestanden wijzigt.



**7.** Stel je database in Schema


Bij de eerste run moet je de DB-migraties uitvoeren.


Voer hiervoor het migratiescript uit: `pnpm run dev:db:migrate`


```markdown
pnpm run dev:db:migrate
```


**8. Gegevens importeren uit de database**

Om gegevens in de database te importeren, dien je een verzoek in bij de API:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. Problemen met toegang tot synchronisatievolume oplossen**

Als u toegangsproblemen ondervindt met de volumes `cdn` en `sync`, voer dan het volgende uit:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


dan weer wel:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Network Local](assets/en/2.webp)



**10. De database aanpassen (optioneel)**

Als je een Fork of een specifieke tak moet gebruiken:

1. Bewerk het `.env` bestand om de volgende variabelen bij te werken:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\. Docker herstarten:


```markdown
docker compose down -v
docker compose up --build -V
```


3\. Synchroniseer de archiefgegevens opnieuw:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


Deze tutorial zorgt ervoor dat het platform correct is ingesteld met dummy keys, geïnstalleerde afhankelijkheden en aangepaste repositories. veel succes met je installatie!


**Commando's voor extra hulp**


alle containers stoppen


```
docker compose down
```


alle bestaande containers en volumes snoeien


```
docker container prune -f
docker volume prune --all
```


maak de containers opnieuw aan met hetzelfde commando als in de officiële handleiding en start het synchronisatiescript:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```