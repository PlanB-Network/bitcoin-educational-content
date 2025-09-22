---
name: Mwongozo wa Kuendesha Jukwaa la Plan ₿ Network Ndani ya Nchi
description: Unawezaje kuendesha Plan ₿ Network katika mazingira ya karibu nawe ili kujaribu mchango wangu wa maudhui au kusahihisha/ukaguzi wa maudhui ya elimu kwenye Plan ₿ Network?
---
![github](assets/cover.webp)


## Kwa Muhtasari


Mafunzo haya yanatoa maagizo ya hatua kwa hatua ya kusanidi Mfumo wa Kusimamia Masomo wa Bitcoin kutoka Plan ₿ Network kwenye mashine ya karibu nawe kwa kutumia Docker, vitufe vya dummy, na usanidi maalum wa hazina.


Iwapo hukuelewa sehemu iliyo hapo juu, usijali—mafunzo haya ni kwa ajili yako!


---

## **Jinsi ya Kuendesha Mfumo wa Kusimamia Masomo wa Bitcoin Ndani ya Nchi**


Mafunzo haya yanatoa hatua za kina za kusanidi jukwaa, kushughulikia funguo za dummy, na kubinafsisha hazina. Fuata hatua zilizo hapa chini ili kuepuka masuala ya kawaida na usanidi vizuri mazingira yako ya ndani.



**1. Mahitaji**


- Mashine ya Linux iliyo na Docker na Docker Compose iliyosanikishwa (imeripotiwa kufanya kazi kwenye Windows pia).
- toleo la kutosha la `nodejs` (lililojaribiwa: 22.12.0)
- `pnpm` imesakinishwa kwenye mfumo wako.
- Git imesanidiwa kwa hazina za kuiga.



**2. Funga Hifadhi**

Funga hazina kwa mashine yako ya karibu:


git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-system


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. Sanidi Vigezo vya Mazingira**


1\. Nakili faili ya `.env.example`:


```bash
cp .env.example .env
```


1. Hariri faili ya `.env`, ukifuta sehemu ya .example ya jina, sasa lazima ujumuishe vitufe vya dummy kwa vigezo vinavyohitajika. Mfano:


⚠️ Hii ni hatua ya lazima, kuiruka itasababisha makosa kama vile kukataliwa kwa muunganisho kati ya baadhi ya vyombo.


Usisahau kuongeza Github PAT yako iliyojitolea pia kwenye faili



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4. Sakinisha Vitegemezi**


`Hakikisha` kuwa umesakinisha toleo linalofaa la nodejs. Kufikia 2024-12, v22.12.0 (LTS) imethibitishwa kufanya kazi.



⚠️ Toleo la nodi za hazina za Ubuntu 22.04 ni 12.22.9: ni nzee sana kukuruhusu kusakinisha pnpm



Ili kusakinisha nodi, pata maagizo [hapa](https://nodejs.org/en/download/package-manager); kwa mfano unaweza kuchagua kutumia `nvm` njia ya usakinishaji.


---

Kabla ya kuanza pnpm kusakinisha awamu ya vifurushi muhimu, hakikisha kuwa utegemezi wote umewekwa, unaweza kufanikisha hili kwa kutekeleza amri ifuatayo:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

Ndani ya folda yako ya `../Bitcoin-learning-management-system/`, endesha amri ifuatayo ili kusakinisha `pnpm`


```bash
pnpm install
```


__TIP:__Kumbuka kusasisha mara kwa mara utegemezi na pnpm yenyewe



**5. Endesha Vyombo**

Ndani ya folda yako ya `../Bitcoin-learning-management-system/`, anza mazingira ya ukuzaji na Docker:


```bash
docker compose up --build -V
```

Pia unaendesha amri hii ifuatayo kwa njia hii, hautaona magogo kwenye terminal yako.

```bash
docker compose up -d --build -V
```


Hii itaunda na kuanza vyombo vyote muhimu kutoka kwa dockers.


**6. Fikia Programu**

Mara tu vyombo vinapofanya kazi, fikia sehemu ya mbele kwa:

\[<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Network Local](assets/en/1.webp)


Kumbuka: kwamba programu itapakia upya kiotomatiki ikiwa utabadilisha faili zozote za chanzo.



**7.** Sanidi hifadhidata yako ya Schema


Mara ya kwanza, utahitaji kuendesha uhamishaji wa DB.


Ili kufanya hivyo, endesha hati ya uhamiaji: `pnpm run dev:db:migrate`


```markdown
pnpm run dev:db:migrate
```


**8. Ingiza Data kutoka kwa Hifadhi**

Ili kuingiza data kwenye hifadhidata, tuma ombi kwa API:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. Rekebisha Masuala ya Kufikia Kiasi cha Usawazishaji**

Ukikumbana na maswala ya ufikiaji na ujazo wa `cdn` na `kusawazisha`, endesha:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


basi tena:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Network Local](assets/en/2.webp)



**10. Binafsisha Hifadhi (Si lazima)**

Ikiwa unahitaji kutumia Fork au tawi maalum:

1. Hariri faili ya `.env` ili kusasisha vigeu vifuatavyo:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\. Anzisha tena Docker:


```markdown
docker compose down -v
docker compose up --build -V
```


3\. Sawazisha upya data ya hazina:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


Mafunzo haya yanahakikisha kuwa jukwaa limesanidiwa ipasavyo na vitufe vya dummy, vitegemezi vilivyosakinishwa, na hazina zilizobinafsishwa kama inavyohitajika. 🎉 Bahati nzuri na usanidi wako!


**Amri za usaidizi wa ziada**


kusimamisha vyombo vyote


```
docker compose down
```


kata vyombo vyote vilivyopo na ujazo


```
docker container prune -f
docker volume prune --all
```


tengeneza tena vyombo kwa amri ile ile iliyotumiwa katika mwongozo rasmi na hati ya kusawazisha ya chakula cha mchana:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
