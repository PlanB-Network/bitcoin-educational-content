---
name: Arendamine Lightning SDK-ga
goal: Arendage oma Lightning arendusoskusi edasi kesktaseme Rust ja SDK koolitusega.
objectives:
  - Harjuge Rust keelega
  - Mõistke, miks kasutada Rusti Bitcoin'i arendamiseks
  - Omandage SDK alusteadmised
---

# Edasi oma LN arendusoskustes

Tere tulemast oma LN teekonnale SDK-ga.

Selles kursuses õpite Rust raamatu aluseid, seejärel jätkate mõningate LN programmeerimisega, kasutades SDK-sid, ja lõpetate mõningate praktiliste harjutustega. Meie erineva taustaga õpetajad juhendavad teid praktiliste oskuste poole ja selgitavad erinevaid väljakutseid, millega tänased LN insenerid sageli silmitsi seisavad.

See kursus filmiti LIVE seminaril, mille korraldas Fulgur'Ventures LN Tuscany üritusel oktoobris 2023.

Nautige kursust!

+++

# Sissejuhatus

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>

## Kursuse ülevaade

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>

**Sissejuhatus**

Tere tulemast sellele edasijõudnute programmeerimiskursusele SDK-de kohta. Sellel koolitusel õpite Rusti aluseid, seejärel keskendute BTC-le & Rustile ja lõpetate mõningate praktiliste harjutustega, kasutades SDK-sid.

See koolitus on praegu saadaval ainult inglise keeles ja oli osa Fulgure Venture'i poolt eelmisel oktoobril Toskaanas korraldatud live seminarist. LIVE ürituse programm on allpool ja see koolitus keskendub ainult esimesele nädalale. Teine pool oli suunatud RGB-le ja seda saab leida RGB kursuselt.

**Õpetajad**

Suur tänu meie õpetajatele, kes olid selle programmi osa:

- Alekos: "Hei, ma olen itaalia kooder ja häkker. Olen töötanud erinevate projektide kallal, nagu bitcoindevkit, magicalbitcoin ja h4ckbs"
- Andrei: "Lightning ekspert LIPA-s"
- Gabriel: "Kirjutan koodi ja teen asju."
- Jesse de Wit: "Lightning võrgu entusiast | arendaja | Breez"

**Seminarikava**

LN Tuscany ürituse 1. nädal
![image](assets/1.webp)

Kui olete selle kursuse lõpetanud ja olete huvitatud jätkukoolitusest, siis siin on teise osa ajakava:
![image](assets/2.webp)


See koolitus annab sulle võimaluse arendada oma programmeerimisoskusi Lightning Networki jaoks, kasutades Rusti ja erinevaid SDK-sid. Koolitus on mõeldud arendajatele, kellel on juba hea programmeerimispagas ja kes soovivad süveneda Lightning Networki spetsiifilisse arendusse. Õpid Rusti aluseid, miks see sobib Bitcoini arenduseks, ja liigud seejärel edasi praktilise töö juurde spetsiaalsete SDK-dega.

**Osa 2: Õpi programmeerima Rustiga**  
Selles osas avastad Rusti põhialused läbi järjestikuste peatükkide. Õpid kirjutama Rusti koodi, mõistma selle eripärasid ning valdama selle olulisi funktsioone seitsmes detailses osas. See moodul on võtmetähtsusega, et mõista, miks Rust on Bitcoini arenduses eelistatud keel.

**Osa 3: Rust ja Bitcoin**  
Siin uurime süvitsi, miks Rust on Bitcoini arendamiseks sobiv valik. Saad teada selle veakäsitlusmudelist, UniFFI tööriistast ning asünkroonsetest traits-idest – kõik need on olulised komponendid turvalise ja töökindla tarkvara loomiseks.

**Osa 4: LNP/BP arendus SDK-dega**  
Selles osas õpid arendama LN sõlmi kasutades erinevaid SDK-sid nagu Breez SDK ja Greenlight Lipa jaoks. Näed, kuidas rakendada Lightning Networki rakendusi, kasutades teeke, mis on loodud Bitcoini ja Lightningu arenduse lihtsustamiseks.

Valmis arendama oma Lightning Networki oskusi Rustiga? Alustame!
# Õppige koodi kirjutama Rust raamatuga

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>

## Sissejuhatus Rusti (1/7)

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>
<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>

:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

## Sissejuhatus Rusti (2/7)

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>

:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::

## Sissejuhatus Rusti (3/7)

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>

:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

## Sissejuhatus Rusti (4/7)

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>
:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

## Sissejuhatus Rusti (5/7)

<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>

:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

## Sissejuhatus Rusti (6/7)

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>

:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

## Sissejuhatus Rusti (7/7)

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>

:::video id=5e96914d-df02-4781-ae54-b06008952301:::

# Rust & BTC

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>

## Miks Rust Bitcoini jaoks

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>

:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::

## Veamudel

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>

:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

## Unniffit

<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>

:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

## Asünkroonsed trait'id

<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>

:::video id=8926dd48-3613-43b6-a509-60ba26ec337f:::

# LNP/BP arendamine SDK abil

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>

## LN sõlm SDK-s

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>

:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>

:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

## Greenlight lipa jaoks

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>

:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

## Breez sdk lipa jaoks

<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>

:::video id=f2770a37-a22f-43d7-9334-8de60eaacff8:::

# Lõpusektsioon

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>

## Hinnangud & Reitingud

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>
<isCourseReview>true</isCourseReview>

## Järeldus

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>
<isCourseConclusion>true</isCourseConclusion>
