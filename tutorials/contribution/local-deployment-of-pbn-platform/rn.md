---
name: Inyobora yo gukoresha urubuga rwa Plan ₿ Network mu karere
description: Woshobora gute gukoresha Plan ₿ Network mu bidukikije vyo mu karere kugira ngo ugerageze intererano yanje y’ibirimwo canke gukosora/gusubiramwo ibirimwo inyigisho kuri Plan ₿ Network?
---
![github](assets/cover.webp)


## Mu ncamake


Iyi nyigisho itanga amabwirizwa y’intambwe ku yindi yo gushinga Bitcoin Learning Management System kuva kuri Plan ₿ Network ku mashini yawe yo mu karere ukoresheje Docker, imfunguruzo z’ibinyoma, n’imiterere y’ububiko bw’ibintu.


Nimba utatahuye igice kiri hejuru, ntuhagarike umutima—iyi nyigisho ni iyawe!


---

## **Uko wokoresha ubuhinga bwo gucunga inyigisho za Bitcoin mu karere**


Iyi nyigisho itanga intambwe zitomoye zo gushinga urubuga, gukoresha imfunguruzo z'ibinyoma, no guhindura ububiko. Kurikiza intambwe zikurikira kugira wirinde ibibazo bisanzwe kandi utunganye neza ibidukikije vyo mu karere kawe.



**1. Ibisabwa**


- Igikoresho ca Linux gifise Docker na Docker Compose (vyavuzwe ko gikora no kuri Windows).
- verisiyo y'ibihimba bihagije (yageragejwe: 22.12.0)
- `pnpm` yashizwe kuri sisitemu yawe.
- Git yatunganijwe ku bubiko bwo gukora cloning.



**2. Kora ububiko**

Clone ububiko kuri mashini yawe yo mu karere:


git clone [Umugambi-B-Uburongozi-bw'Inyigisho-Bitcoin]

[cd](https://github.com/Irezo-ya-PlanB/Bitcoin-uburyo- bwo-gucunga-inyigisho￼cd) Bitcoin-uburyo- bwo-gucunga-inyigisho


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. Gutegura ibidukikije bihinduka**


1\. Gusubiramwo `.env.akarorero` dosiye:


```bash
cp .env.example .env
```


1. Guhindura dosiye `.env`, gukuraho igice .akarorero c'izina, ubu ubwirizwa gushiramwo imfunguruzo z'ibinyoma ku bihinduka bisabwa. Akarorero:


⚠️ Iyi ni intambwe y’ingenzi, kuyisimbuka bizovamwo amakosa nk’ukwanga guhuza hagati ya bimwe mu bikoresho.


Ntukibagire kwongerako Github PAT yawe yihariye nayo muri dosiye



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4. Shiraho ibivako**


`Urabe neza` ko washizeho verisiyo ya nodejs ibereye. Kuva mu mwaka w’2024-12, v22.12.0 (LTS) yaragaragaye ko ikora.



⚠️ Ubuntu 22.04 ububiko nodejs verisiyo ni 12.22.9: irashaje cane kugira ngo ushobore gushiramwo pnpm



Kugira ngo ushiremwo nodejs, rondera amabwirizwa [hano](https://nodejs.org/ru/gukuraho/umucungerezi-w'amapaki); nk'akarorero ushobora guhitamwo gukoresha uburyo bwo gushiramwo `nvm`.


---

Imbere yo gutangura pnpm installing phase y'amapaki akenewe, urabe ko ufise ama dependencies yose ashizwemwo, ushobora kubishikako ukoresheje iri tegeko rikurikira:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

Imbere muri dosiye yawe `../Bitcoin-uburyo bwo kwiga/`, koresha itegeko rikurikira kugira ngo ushiremwo `pnpm`


```bash
pnpm install
```


__ICIYUMVIRO:__Ibuka guhindura rimwe na rimwe ivyo vyose bishingiyeko na pnpm ubwayo



**5. Gukoresha ibikoresho**

Imbere muri dosiye yawe `../Bitcoin-ukwiga-uburongozi-uburyo/`, tangura ibidukikije vy'iterambere na Docker:


```bash
docker compose up --build -V
```

Ushobora kandi gukoresha iri tegeko rikurikira muri ubu buryo, ntuzobona ibitabo biri muri terminal yawe.

```bash
docker compose up -d --build -V
```


Ivyo bizokwubaka kandi bitangure ibikoresho vyose bikenewe bivuye ku ba dockers.


**6. Kugera kuri Porogaramu**

Igihe ibikoresho biriko birakora, genda ku frontend kuri:

\[<umushitsi wo mu karere:8181](umushitsi wo mu karere:8181)>


![Plan ₿ Network Local](assets/en/1.webp)


Iciyumviro: ko app izosubira kwifungura iyo uhinduye amadosiye yose y’inkomoko.



**7.** Gushinga urutonde rwawe rw'amakuru Schema.


Ku rugendo rwa mbere, uzokenera gukoresha ivyiyumviro vya DB.


Kugira ngo ubikore, koresha inyandiko y'ukwimuka: `pnpm koresha dev:db:kwimuka`


```markdown
pnpm run dev:db:migrate
```


**8. Injira amakuru mu bubiko**

Kugira ngo winjize amakuru mu rutonde rw'amakuru, usabe API:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. Gukosora ibibazo vyo gushika ku rwego rwo gukorana**

Niwahura n'ingorane zo gushika ku bitabo `cdn` na `sync`, genda:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


hanyuma kandi:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Network Local](assets/en/2.webp)



**10. Guhindura ububiko (Ntibikenewe)**

Niba ukeneye gukoresha Fork canke ishami rimwe na rimwe:

1. Guhindura dosiye `.env` kugira ngo uhindure ibi bihinduka:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\. Gusubiramwo Docker:


```markdown
docker compose down -v
docker compose up --build -V
```


3\. Subira guhuza amakuru y'ububiko:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


Iyi nyigisho iratuma urubuga rwashizweho neza n’imfunguruzo z’ibinyoma, ibishingiyeko vyashizweho, n’ububiko buhinduwe uko bikenewe. 🎉 Mugire amahirwe mu setup yanyu!


**Amabwirizwa y'imfashanyo y'inyongera**


guhagarika ibikoresho vyose


```
docker compose down
```


gukata ibikoresho vyose biriho n'ibipimo


```
docker container prune -f
docker volume prune --all
```


gusubira kurema ibikoresho n'itegeko rimwe rikoreshwa mu burongozi buzwi maze utangure inyandiko yo gukorana:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```