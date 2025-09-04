---
name: Guide till lokal drift av Plan ₿ Network-plattformen
description: Hur kan du köra Plan ₿ Network i en lokal miljö för att testa mitt innehållsbidrag eller korrekturläsning/granskning av utbildningsinnehåll på Plan ₿ Network?
---
![github](assets/cover.webp)


## Sammanfattning


Denna handledning innehåller steg-för-steg-instruktioner för att konfigurera Bitcoin Learning Management System från Plan ₿ Network på din lokala maskin med hjälp av Docker, dummy-nycklar och anpassade arkivkonfigurationer.


Om du inte förstod delen ovan, oroa dig inte - den här handledningen är för dig!


---

## **Hur man kör Bitcoin Learning Management System lokalt**


Denna handledning innehåller detaljerade steg för att konfigurera plattformen, hantera dummy keys och anpassa repositories. Följ stegen nedan för att undvika vanliga problem och konfigurera din lokala miljö på rätt sätt.



**1. Förkunskapskrav**


- Linux-maskin med Docker och Docker Compose installerat (det har rapporterats att det fungerar på Windows också).
- tillräcklig `nodejs`-version (testad: 22.12.0)
- `pnpm` installerat på ditt system.
- Git konfigurerat för kloning av repositories.



**2. Klona förvaret**

Klona arkivet till din lokala maskin:


git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-system för hantering av inlärning


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. Konfigurera miljövariabler**


1\. Duplicera filen `.env.example`:


```bash
cp .env.example .env
```


1. Redigera filen `.env` och ta bort .example-delen av namnet, nu måste du inkludera dummy-nycklar för nödvändiga variabler. Exempel:


⚠️ Detta är ett obligatoriskt steg, om du hoppar över det kommer det att leda till fel, t.ex. att vissa containrar inte kan kopplas ihop.


Glöm inte att lägga till din dedikerade Github PAT också i filen



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4. Installera beroenden**


`Se till` att ha installerat en lämplig nodejs version. Från och med 2024-12 har v22.12.0 (LTS) visat sig fungera.



⚠️ Ubuntu 22.04 repository nodejs version är 12.22.9: för gammal för att du ska kunna installera pnpm



För att installera nodejs, hitta instruktioner [här] (https://nodejs.org/en/download/package-manager); till exempel kan du välja att använda `nvm` installationsmetod.


---

Innan du börjar pnpm-installationsfasen av nödvändiga paket, se till att alla beroenden är installerade, du kan uppnå detta genom att köra följande kommando:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

I mappen `../Bitcoin-learning-management-system/` kör du följande kommando för att installera `pnpm`


```bash
pnpm install
```


__TIP:__Kom ihåg att då och då uppdatera både beroenden och pnpm själv



**5. Kör containrarna**

I mappen `../Bitcoin-learning-management-system/` startar du utvecklingsmiljön med Docker:


```bash
docker compose up --build -V
```

Om du också kör nästa kommando på det här sättet kommer du inte att se loggarna i din terminal.

```bash
docker compose up -d --build -V
```


Detta kommer att bygga och starta alla nödvändiga containrar från dockers.


**6. Få tillgång till applikationen**

När containrarna körs kan du komma åt frontend via:

\[<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Network Local](assets/en/1.webp)


Observera: att appen automatiskt laddas om om du ändrar några källfiler.



**7.** Konfigurera din databas Schema


Vid den första körningen måste du köra DB-migreringarna.


För att göra det, kör migreringsskriptet: `pnpm run dev:db:migrate`


```markdown
pnpm run dev:db:migrate
```


**8. Importera data från Repository**

För att importera data till databasen gör du en förfrågan till API:et:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. Fixa problem med åtkomst till synkroniseringsvolym **

Om du stöter på problem med åtkomst till volymerna `cdn` och `sync`, kör:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


och sen igen:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Network Local](assets/en/2.webp)



**10. Anpassa förvaret (valfritt)**

Om du behöver använda en Fork eller en specifik gren:

1. Redigera filen `.env` för att uppdatera följande variabler:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\. Starta om Docker:


```markdown
docker compose down -v
docker compose up --build -V
```


3\. Synkronisera data från förvaret igen:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


Denna handledning säkerställer att plattformen är korrekt konfigurerad med dummy-nycklar, beroenden installerade och arkiv anpassade efter behov. 🎉 Lycka till med din installation!


**Kommandon för extra hjälp**


stoppa alla containrar


```
docker compose down
```


beskära alla befintliga behållare och volymer


```
docker container prune -f
docker volume prune --all
```


återskapa behållarna med samma kommando som används i den officiella guiden och lunchsynkroniseringsskriptet:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```