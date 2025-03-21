---
name: Opas Plan ₿ Network-alustan käyttämiseen paikallisesti
description: Miten Plan ₿ Network:tä voidaan käyttää paikallisessa ympäristössä, jotta voidaan testata sisältöön osallistumista tai opetussisällön oikolukemista/arviointia Plan ₿ Network:llä?
---
![github](assets/cover.webp)

## Yhteenveto

Tämä opetusohjelma sisältää vaiheittaiset ohjeet Bitcoin-oppimisen hallintajärjestelmän asentamiseen Plan ₿ Network:sta paikalliselle koneellesi käyttäen Dockeria, valeavaimia ja mukautettuja arkistokokoonpanoja.

Jos et ymmärtänyt yllä olevaa kohtaa, älä huoli - tämä ohje on sinua varten!

---
## **Kuinka Bitcoin-oppimisenhallintajärjestelmää käytetään paikallisesti**

Tämä opetusohjelma sisältää yksityiskohtaiset vaiheet alustan määrittämiseksi, valeavaimien käsittelemiseksi ja arkistojen mukauttamiseksi. Seuraa alla olevia ohjeita välttääksesi yleiset ongelmat ja määrittääksesi paikallisen ympäristösi oikein.

**1. Edellytykset**


- Linux-kone, johon on asennettu Docker ja Docker Compose (sen on raportoitu toimivan myös Windowsissa).
- riittävä `nodejs`-versio (testattu: 22.12.0)
- `pnpm` asennettuna järjestelmääsi.
- Git konfiguroitu arkistojen kloonausta varten.

**2. Kloonaa arkisto**

Kloonaa arkisto paikalliselle koneellesi:

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-järjestelmä

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3. Ympäristömuuttujien määrittäminen**

1\. Kopioi tiedosto `.env.example`:

```bash
cp .env.example .env
```

1. Muokkaa `.env`-tiedostoa poistamalla .example-osa nimestä, nyt sinun on lisättävä tarvittavat muuttujien valeavaimet. Esimerkki:

⚠️ Tämä on pakollinen vaihe, sen ohittaminen johtaa virheisiin, kuten joidenkin säiliöiden välisen yhteyden epäämiseen.

Älä unohda lisätä myös oma Github PAT tiedostoasi tiedostoon

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4. Asenna riippuvuudet**

varmista, että olet asentanut sopivan nodejs-version. Vuodesta 2024-12 lähtien v22.12.0 (LTS) on osoittautunut toimivaksi.

⚠️ Ubuntu 22.04 repository nodejs versio on 12.22.9: liian vanha, jotta voit asentaa pnpm:n

Nodejs:n asentamiseen löydät ohjeet [täältä](https://nodejs.org/en/download/package-manager); voit esimerkiksi käyttää `nvm`-asennusmenetelmää.

---
Ennen kuin aloitat pnpm-asennusvaiheen, varmista, että kaikki riippuvuudet on asennettu, voit tehdä sen suorittamalla seuraavan komennon:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
Asenna `../Bitcoin-learning-management-system/` -kansioon seuraava komento asentaaksesi `pnpm`

```bash
pnpm install
```

__TIP:__ Muista päivittää aika ajoin sekä riippuvuudet että itse pnpm:n tiedot

**5. Suorita säiliöt**

Käynnistä kehitysympäristö Dockerilla kansiossa `../Bitcoin-learning-management-system/`:

```bash
docker compose up --build -V
```

Jos suoritat myös tämän seuraavan komennon tällä tavalla, et näe lokitietoja terminaalissasi.

```bash
docker compose up -d --build -V
```

Tämä rakentaa ja käynnistää kaikki tarvittavat kontit dokkareista.

**6. Pääsy sovellukseen**

Kun säiliöt ovat käynnissä, pääset etusivulle osoitteessa:

\[<http://localhost:8181](http://localhost:8181)>

![Plan ₿ Network Local](assets/en/1.webp)

Huomaa: sovellus latautuu automaattisesti uudelleen, jos muutat lähdetiedostoja.

**7.** Tietokannan perustaminen Schema

Ensimmäisellä ajokerralla sinun on suoritettava tietokantojen siirrot.

Suorita migraatioskripti : `pnpm run dev:db:migrate`

```markdown
pnpm run dev:db:migrate
```

**8. Tietojen tuonti arkistosta**

Jos haluat tuoda tietoja tietokantaan, tee pyyntö API:lle:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Korjaa synkronoinnin äänenvoimakkuuden käyttöongelmat**

Jos törmäät käyttöongelmiin `cdn`- ja `sync`-tietueiden kanssa, suorita:

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

sitten taas:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10. Varaston mukauttaminen (valinnainen)**

Jos haluat käyttää Fork:tä tai tiettyä haaraa:

1. Muokkaa `.env`-tiedostoa päivittääksesi seuraavat muuttujat:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Käynnistä Docker uudelleen:

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Synkronoi arkiston tiedot uudelleen:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

Tämä opetusohjelma varmistaa, että alusta on asetettu oikein, ja siinä on valeavaimet, riippuvuudet asennettu ja arkistot mukautettu tarpeen mukaan. 🎉 Onnea asetusten kanssa!

**Komennot lisäapua varten**

pysäytä kaikki säiliöt

```
docker compose down
```

karsia kaikki olemassa olevat säiliöt ja tilavuudet

```
docker container prune -f
docker volume prune --all
```

luo kontit uudelleen samalla komennolla, jota käytetään virallisessa oppaassa ja lounaan synkronointiskriptissä:

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
