---
name: Veiledning for lokal kjøring av Plan ₿ Network-plattformen
description: Hvordan kan du kjøre Plan ₿ Network i et lokalt miljø for å teste innholdsbidraget mitt eller korrekturlesing/gjennomgang av pedagogisk innhold på Plan ₿ Network?
---
![github](assets/cover.webp)

## Oppsummering

Denne veiledningen gir trinnvise instruksjoner for hvordan du konfigurerer Bitcoin Learning Management System fra Plan ₿ Network på din lokale maskin ved hjelp av Docker, dummy-nøkler og egendefinerte repository-konfigurasjoner.

Hvis du ikke forsto delen ovenfor, ikke bekymre deg - denne veiledningen er for deg!

---
## **Slik kjører du Bitcoin Learning Management System lokalt**

Denne veiledningen inneholder detaljerte trinn for å sette opp plattformen, håndtere dummy-nøkler og tilpasse repositorier. Følg trinnene nedenfor for å unngå vanlige problemer og konfigurere det lokale miljøet på riktig måte.

**1. Forkunnskaper**


- Linux-maskin med Docker og Docker Compose installert (det har blitt rapportert at det også fungerer på Windows).
- tilstrekkelig `nodejs`-versjon (testet: 22.12.0)
- `pnpm` installert på systemet ditt.
- Git konfigurert for kloning av repositorier.

**2. Klone depotet**

Klon depotet til din lokale maskin:

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-læringsstyringssystem

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3. Sette opp miljøvariabler**

1\. Dupliser filen `.env.example`:

```bash
cp .env.example .env
```

1. Rediger filen `.env`, og slett .example-delen av navnet. Nå må du inkludere dummy-nøkler for nødvendige variabler. Eksempel:

⚠️ Dette er et obligatorisk trinn, og hvis du hopper over det, vil det føre til feil, for eksempel at forbindelsen mellom noen av containerne nektes.

Ikke glem å legge til ditt dedikerte Github PAT i filen

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4. Installer avhengigheter**

sørg for å ha installert en passende nodejs-versjon. Per 2024-12 har v22.12.0 (LTS) vist seg å fungere.

⚠️ Ubuntu 22.04 repository nodejs versjon er 12.22.9: for gammel til å tillate deg å installere pnpm

For å installere nodejs, finn instruksjoner [her] (https://nodejs.org/en/download/package-manager); for eksempel kan du velge å bruke `nvm` installasjonsmetode.

---
Før du starter pnpm-installasjonsfasen av nødvendige pakker, må du sørge for å ha alle avhengigheter installert, du kan oppnå dette ved å kjøre følgende kommando:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
I mappen `../Bitcoin-learning-management-system/` kjører du følgende kommando for å installere `pnpm`

```bash
pnpm install
```

__TIP:__ Husk å oppdatere både avhengigheter og selve pnpm fra tid til annen

**5. Kjør beholderne**

Start utviklingsmiljøet med Docker i mappen `../Bitcoin-learning-management-system/`:

```bash
docker compose up --build -V
```

Hvis du også kjører den neste kommandoen på denne måten, vil du ikke se loggene i terminalen.

```bash
docker compose up -d --build -V
```

Dette vil bygge og starte alle nødvendige containere fra dockers.

**6. Få tilgang til applikasjonen**

Når containerne er i gang, får du tilgang til frontend på :

\[<http://localhost:8181](http://localhost:8181)>

![Plan ₿ Network Local](assets/en/1.webp)

Merk: Appen lastes automatisk inn på nytt hvis du endrer kildefiler.

**7. Sett opp databasen din Schema

Ved første kjøring må du kjøre DB-migreringene.

For å gjøre dette kjører du migreringsskriptet: `pnpm run dev:db:migrate`

```markdown
pnpm run dev:db:migrate
```

**8. Importer data fra Repository**

For å importere data til databasen må du sende en forespørsel til API-et:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Løs problemer med tilgang til synkroniseringsvolum**

Hvis du støter på tilgangsproblemer med volumene `cdn` og `sync`, kjører du :

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

men så igjen..:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10. Tilpasse depotet (valgfritt)**

Hvis du trenger å bruke en Fork eller en bestemt gren:

1. Rediger filen `.env` for å oppdatere følgende variabler:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Start Docker på nytt:

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Synkroniser depotdataene på nytt:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

Denne veiledningen sikrer at plattformen er riktig konfigurert med dummy-nøkler, avhengigheter installert og repositorier tilpasset etter behov. 🎉 Lykke til med oppsettet!

**Kommandoer for ekstra hjelp**

stoppe alle containere

```
docker compose down
```

beskjære alle eksisterende beholdere og volumer

```
docker container prune -f
docker volume prune --all
```

gjenskap containerne med den samme kommandoen som brukes i den offisielle guiden og lunsjsynkroniseringsskriptet:

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
