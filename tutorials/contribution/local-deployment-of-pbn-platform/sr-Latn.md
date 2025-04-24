---
name: Vodič za lokalno pokretanje platforme Plan ₿ Network
description: Kako možete pokrenuti Plan ₿ Network u lokalnom okruženju za testiranje mog doprinosa sadržaju ili lekture/pregleda obrazovnog sadržaja na Plan ₿ Network?
---
![github](assets/cover.webp)


## Ukratko


Ovaj vodič pruža detaljna uputstva za postavljanje Bitcoin Sistema za upravljanje učenjem sa Plan ₿ Network na vašem lokalnom računaru koristeći Docker, lažne ključeve i prilagođene konfiguracije repozitorijuma.


Ako niste razumeli deo iznad, ne brinite—ovaj vodič je za vas!


---

## **Kako pokrenuti Bitcoin sistem za upravljanje učenjem lokalno**


Ovaj vodič pruža detaljne korake za postavljanje platforme, rukovanje lažnim ključevima i prilagođavanje repozitorijuma. Pratite korake ispod kako biste izbegli uobičajene probleme i pravilno konfigurisali vaše lokalno okruženje.



**1. Preduslovi**


- Linux mašina sa instaliranim Docker-om i Docker Compose-om (prijavljeno je da radi i na Windows-u).
- dovoljna `nodejs` verzija (testirano: 22.12.0)
- `pnpm` instaliran na vašem sistemu.
- Git konfigurisan za kloniranje repozitorijuma.



**2. Kloniraj Repozitorijum**

Klonirajte repozitorijum na vašu lokalnu mašinu:


git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-system


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. Postavite Varijable Okruženja**


1\. Duplirajte datoteku `.env.example`:


```bash
cp .env.example .env
```


1. Izmenite datoteku `.env`, brišući deo .example iz imena, sada morate uključiti lažne ključeve za potrebne promenljive. Primer:


⚠️ Ovo je obavezni korak, preskakanje će rezultirati greškama kao što je odbijanje veze između nekih kontejnera.


Ne zaboravi da dodaš svoj posvećeni Github PAT takođe u datoteku.



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4. Instaliraj Zavisnosti**


`Be sure` da imate instaliranu odgovarajuću verziju nodejs-a. Od 2024-12, v22.12.0 (LTS) se pokazala kao funkcionalna.



⚠️ Verzija nodejs-a u Ubuntu 22.04 repozitorijumu je 12.22.9: previše stara da biste mogli instalirati pnpm



Da instalirate nodejs, pronađite uputstva [ovde](https://nodejs.org/en/download/package-manager); na primer, možete odabrati da koristite `nvm` metod instalacije.


---

Pre nego što započnete fazu instalacije potrebnih paketa sa pnpm, budite sigurni da su sve zavisnosti instalirane, to možete postići pokretanjem sledeće komande:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

Unutar vaše `../Bitcoin-learning-management-system/` fascikle, pokrenite sledeću komandu da instalirate `pnpm`


```bash
pnpm install
```


__SAVET:__Ne zaboravite da povremeno ažurirate i zavisnosti i sam pnpm



**5. Pokreni kontejnere**

Unutar vaše `../Bitcoin-learning-management-system/` fascikle, pokrenite razvojno okruženje sa Docker-om:


```bash
docker compose up --build -V
```

Takođe pokrenete ovu naredbu na sledeći način, nećete videti logove u vašem terminalu.

```bash
docker compose up -d --build -V
```


Ovo će izgraditi i pokrenuti sve potrebne kontejnere iz dockera.


**6. Pristup aplikaciji**

Kada kontejneri budu pokrenuti, pristupite frontend-u na:

\[<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Network Local](assets/en/1.webp)


Napomena: aplikacija će se automatski ponovo učitati ako promenite bilo koje izvorne datoteke.



**7.** Postavite svoju bazu podataka Schema


Na prvom pokretanju, potrebno je pokrenuti DB migracije.


Da biste to uradili, pokrenite skriptu za migraciju: `pnpm run dev:db:migrate`


```markdown
pnpm run dev:db:migrate
```


**8. Uvoz podataka iz repozitorijuma**

Da biste uvezli podatke u bazu podataka, pošaljite zahtev API-ju:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. Popravite probleme sa pristupom sinhronizovanom volumenu**

Ako naiđete na probleme sa pristupom `cdn` i `sync` volumenima, pokrenite:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


onda opet:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Network Local](assets/en/2.webp)



**10. Prilagodite Repozitorijum (Opcionalno)**

Ako treba da koristite Fork ili određenu filijalu:

1. Uredite `.env` datoteku da ažurirate sledeće promenljive:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\. Restartujte Docker:


```markdown
docker compose down -v
docker compose up --build -V
```


3\. Ponovo sinhronizujte podatke repozitorijuma:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


Ovaj vodič osigurava da je platforma ispravno postavljena sa lažnim ključevima, instaliranim zavisnostima i prilagođenim repozitorijumima po potrebi. 🎉 Srećno sa postavljanjem!


**Komande za dodatnu pomoć**


zaustavi sve kontejnere


```
docker compose down
```


obriši sve postojeće kontejnere i volumene


```
docker container prune -f
docker volume prune --all
```


ponovo kreirajte kontejnere koristeći istu komandu iz zvaničnog vodiča i pokrenite skriptu za sinhronizaciju:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```