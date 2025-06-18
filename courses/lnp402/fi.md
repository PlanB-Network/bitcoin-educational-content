---
name: Kehittäminen Lightningilla SDK:n avulla
goal: Kehitä Lightning-kehitystaitojasi edistyneellä Rust- ja SDK-koulutuksella.
objectives:
  - Tutustu Rust-ohjelmointikieleen
  - Ymmärrä, miksi Rustia käytetään Bitcoinin kehittämiseen
  - Opi SDK:n perusteet
---

# LN-kehitystaitojesi edistäminen

Tervetuloa LN-matkalle SDK:n kanssa.

Tässä kurssissa opit Rust-kirjan perusteet, seuraat sitten LN-ohjelmointia SDK:iden avulla ja lopetat käytännön harjoituksilla. Eri taustoista tulevat opettajamme ohjaavat sinut käytännön taitoihin ja selittävät erilaisia haasteita, joita tämän päivän LN-insinöörit usein kohtaavat.

Tämä kurssi kuvattiin LIVE-seminaarissa, jonka järjesti Fulgur'Ventures LN Tuscany -tapahtumassa lokakuussa 2023.

Nauti kurssista!

+++

# Johdanto
<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>

## Kurssin yleiskatsaus
<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>

**Johdanto**

Tervetuloa tähän edistyneeseen ohjelmointikurssiin SDK:iden parissa. Tässä koulutuksessa opit Rustin perusteet, keskityt sitten BTC & Rustiin ja lopetat käytännön harjoituksilla SDK:iden avulla.

Tämä koulutus on toistaiseksi saatavilla vain englanniksi ja oli osa viime lokakuussa Toscanassa Fulgure Venturen järjestämää live-seminaaria. LIVE-tapahtuman ohjelma löytyy alta, ja tämä koulutus keskittyy vain ensimmäiseen viikkoon. Toinen puolisko oli suunnattu RGB:lle ja löytyy RGB-kurssilta.

**Opettajat**

Suurkiitokset opettajillemme, jotka ovat olleet osa tätä ohjelmaa:

- Alekos: "Hei, olen italialainen koodari ja hakkeri. Olen työskennellyt erilaisissa projekteissa, kuten bitcoindevkit, magicalbitcoin ja h4ckbs"
- Andrei: "Lightning-asiantuntija LIPA:ssa"
- Gabriel: "Kirjoitan koodia ja teen juttuja."
- Jesse de Wit: "Lightning-verkon intoilija | kehittäjä | Breez"

**Seminaarin aikataulu**

LN Tuscany -tapahtuman 1. viikko
![kuva](assets/1.webp)

Kun olet saanut tämän kurssin päätökseen, jos olet kiinnostunut jatkokoulutuksesta, tässä on toisen osan aikataulu:
![kuva](assets/2.webp)


Tämä koulutus tarjoaa sinulle mahdollisuuden kehittää ohjelmointitaitojasi Lightning Networkin parissa käyttämällä Rustia ja erilaisia SDK-työkaluja. Se on suunniteltu kehittäjille, joilla on jo hyvä ohjelmointiosaaminen ja jotka haluavat syventyä Lightning Network -kehitykseen. Opit Rust-kielen perusteet, miksi se sopii Bitcoin-kehitykseen, ja siirryt käytännön sovelluksiin erikoistuneiden SDK:iden avulla.

**Osa 2: Opettele ohjelmoimaan Rustilla**  
Tässä osassa tutustut Rustin perusasioihin vaiheittain etenevien lukujen kautta. Opit kirjoittamaan Rust-koodia, ymmärtämään sen erityispiirteet ja hallitsemaan sen keskeiset ominaisuudet seitsemässä yksityiskohtaisessa osassa. Tämä moduuli on oleellinen, jotta ymmärrät, miksi Rust on suosittu kieli Bitcoin-kehityksessä.

**Osa 3: Rust & Bitcoin**  
Tässä osassa perehdytään siihen, miksi Rust on merkityksellinen valinta Bitcoin-kehitykseen. Tutustut sen virhemalliin, UniFFI-työkaluun sekä asynkronisiin traitteihin, jotka ovat tärkeitä turvallisten ja vakaiden ohjelmistojen rakentamisessa.

**Osa 4: LNP/BP-kehitys SDK:iden avulla**  
Tässä osassa opit kehittämään LN-solmuja hyödyntäen erilaisia SDK:ita kuten Breez SDK ja Greenlight Lipalle. Näet, kuinka Lightning Network -sovelluksia voidaan toteuttaa kirjastoilla, jotka on suunniteltu helpottamaan Bitcoinin ja Lightningin kehitystä.

Valmis kehittämään Lightning Network -osaamistasi Rustilla? Mennään!
# Opi koodaamaan Rust-kirjan avulla
<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>

## Johdanto Rustiin (1/7)
<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>
<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>

:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

## Johdanto Rustiin (2/7)
<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>

:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::

## Johdanto Rustiin (3/7)
<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>

:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

## Johdanto Rustiin (4/7)
<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>
:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

## Johdanto Rustiin (5/7)
<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>

:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

## Johdanto Rustiin (6/7)
<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>

:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

## Johdanto Rustiin (7/7)
<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>

:::video id=5e96914d-df02-4781-ae54-b06008952301:::

# Rust & BTC 
<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>

## Miksi Rust Bitcoinille
<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>

:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::

## Virhemalli
<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>

:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

## Unniffit
<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>

:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

## Asynkroniset traitit
<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>

:::video id=8926dd48-3613-43b6-a509-60ba26ec337f:::

# LNP/BP:n kehittäminen SDK:n avulla
<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>

## LN-solmu SDK:lla
<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>

:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

## Breez sdk
<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>

:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

## Greenlight lipalle
<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>

:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

## Breez sdk lipalle
<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>

:::video id=f2770a37-a22f-43d7-9334-8de60eaacff8:::

# Lopullinen osio
<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Arviot & Arvosanat
<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>
<isCourseReview>true</isCourseReview>

## Yhteenveto
<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>
<isCourseConclusion>true</isCourseConclusion>
