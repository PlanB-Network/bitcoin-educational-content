---
name: Juhend Plan ₿ Network platvormi kohalikuks kasutamiseks
description: Kuidas saab Plan ₿ Network kohalikus keskkonnas käivitada, et testida minu sisulist panust või haridusliku sisu korrektuuri/ülevaatust Plan ₿ Network-l?
---
![github](assets/cover.webp)

## Kokkuvõttes

See õpetus annab samm-sammult juhiseid Bitcoin õpihaldussüsteemi seadistamiseks Plan ₿ Network-st oma kohalikul masinal, kasutades Dockerit, dummy võtmeid ja kohandatud repositooriumi konfiguratsioone.

Kui sa ei saanud ülaltoodud osast aru, siis ära muretse - see õpetus on mõeldud just sulle!

---
## **Kuidas käivitada Bitcoin õpihaldussüsteemi kohapeal**

Selles õpetuses on esitatud üksikasjalikud sammud platvormi seadistamiseks, võltsvõtmete käitlemiseks ja hoidlate kohandamiseks. Järgige alljärgnevaid samme, et vältida tavalisi probleeme ja konfigureerida oma kohalik keskkond õigesti.

**1. Eeltingimused**


- Linuxi masin, millele on paigaldatud Docker ja Docker Compose (on teatatud, et see töötab ka Windowsis).
- piisav `nodejs` versioon (testitud: 22.12.0)
- `pnpm` on teie süsteemi paigaldatud.
- Git konfigureeritud repositooriumide kloonimiseks.

**2. Kloonige hoidla**

Kloonige repositoorium oma kohalikku masinasse:

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-õppejuhtimissüsteem

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3. Keskkonnamuutujate seadistamine**

1\. Dubleeri faili `.env.example`:

```bash
cp .env.example .env
```

1. Redigeeri faili `.env`, kustutades nimest .example osa, nüüd pead lisama vajalike muutujate jaoks fiktiivsed võtmed. Näide:

⚠️ See on kohustuslik samm, selle vahelejätmine toob kaasa vead, näiteks ühenduse keeldumise mõne konteineri vahel.

Ärge unustage lisada ka oma spetsiaalne Github PAT faili

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4. Paigaldage sõltuvused**

"Veenduge", et olete paigaldanud sobiva nodejs versiooni. Alates 2024-12 on tõestatud, et v22.12.0 (LTS) töötab.

⚠️ Ubuntu 22.04 repositooriumi nodejs versioon on 12.22.9: liiga vana, et võimaldada pnpm installimist

Nodejs'i paigaldamiseks leiate juhised [siit](https://nodejs.org/en/download/package-manager); näiteks võite kasutada `nvm` paigaldusmeetodit.

---
Enne pnpm installimise faasi vajalike pakettide, veenduge, et kõik sõltuvused on paigaldatud, saate seda saavutada, käivitades järgmise käsu:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
Käivitage oma kaustas `../Bitcoin-learning-management-system/` järgmine käsk, et paigaldada `pnpm`

```bash
pnpm install
```

__TIP:__ Ärge unustage aeg-ajalt uuendada nii sõltuvusi kui ka pnpm ise
**5. Käivitage konteinerid**

Käivitage arenduskeskkond Dockeriga oma kaustas `../Bitcoin-learning-management-system/`:

```bash
docker compose up --build -V
```

Kui käivitate ka selle järgmise käsu niimoodi, ei näe te oma terminalis logisid.

```bash
docker compose up -d --build -V
```

See ehitab ja käivitab kõik vajalikud konteinerid dokkidest.

**6. Juurdepääs rakendusele**

Kui konteinerid on käivitatud, pääsete frontendile aadressil:

\[<http://localhost:8181](http://localhost:8181)>

![Plan ₿ Network Local](assets/en/1.webp)

Märkus: rakendus laadib automaatselt uuesti, kui muudate mis tahes lähtefaile.

**7.** Seadistage oma andmebaas Schema

Esimesel käivitamisel peate käivitama andmebaasi migratsiooni.

Selleks käivitage migratsiooniskript : `pnpm run dev:db:migrate`

```markdown
pnpm run dev:db:migrate
```

**8. Andmete importimine repositooriumist**

Andmete importimiseks andmebaasi tehke taotlus API-le:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Sünkroonimismahu juurdepääsu probleemide lahendamine**

Kui teil tekib juurdepääsuprobleemide korral mahtude `cdn` ja `sync` puhul, käivitage:

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

siis jälle:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10. Kohandage hoidlat (valikuline)**

Kui teil on vaja kasutada Fork või konkreetset haru:

1. Muuda faili `.env`, et uuendada järgmisi muutujaid:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Käivitage Docker uuesti:

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Uuesti sünkroniseerida hoidla andmed:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

See õpetus tagab, et platvorm on õigesti seadistatud koos dummy-võtmete, paigaldatud sõltuvuste ja vajaduse korral kohandatud repositooriumidega. 🎉 Palju õnne oma seadistusega!

**Käsklused lisaabi saamiseks**

peatada kõik konteinerid

```
docker compose down
```

kärpida kõik olemasolevad konteinerid ja mahud

```
docker container prune -f
docker volume prune --all
```

looge konteinerid uuesti sama käsuga, mida kasutatakse ametlikus juhendis ja lõunasöögi sünkroonimisskriptis:

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
