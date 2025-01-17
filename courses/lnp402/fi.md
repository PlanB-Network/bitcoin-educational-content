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

## Kurssin opetussuunnitelma & johdanto
<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>

### Johdanto

Tervetuloa tähän edistyneeseen ohjelmointikurssiin SDK:iden parissa. Tässä koulutuksessa opit Rustin perusteet, keskityt sitten BTC & Rustiin ja lopetat käytännön harjoituksilla SDK:iden avulla.

Tämä koulutus on toistaiseksi saatavilla vain englanniksi ja oli osa viime lokakuussa Toscanassa Fulgure Venturen järjestämää live-seminaaria. LIVE-tapahtuman ohjelma löytyy alta, ja tämä koulutus keskittyy vain ensimmäiseen viikkoon. Toinen puolisko oli suunnattu RGB:lle ja löytyy RGB-kurssilta.

### Opettajat

Suurkiitokset opettajillemme, jotka ovat olleet osa tätä ohjelmaa:

- Alekos: "Hei, olen italialainen koodari ja hakkeri. Olen työskennellyt erilaisissa projekteissa, kuten bitcoindevkit, magicalbitcoin ja h4ckbs"
- Andrei: "Lightning-asiantuntija LIPA:ssa"
- Gabriel: "Kirjoitan koodia ja teen juttuja."
- Jesse de Wit: "Lightning-verkon intoilija | kehittäjä | Breez"

### Seminaarin aikataulu

LN Tuscany -tapahtuman 1. viikko
![kuva](assets/1.webp)

Kun olet saanut tämän kurssin päätökseen, jos olet kiinnostunut jatkokoulutuksesta, tässä on toisen osan aikataulu:
![kuva](assets/2.webp)

Onnea opintoihisi.

# Opi koodaamaan Rust-kirjan avulla
<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>

## Johdanto Rustiin (1/7)
<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>
<professor>radio-talent</professor>

![video](https://www.youtube.com/watch?v=aZYhDXE_Gas)

## Johdanto Rustiin (2/7)
<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>

![video](https://youtu.be/Xm8eCv4LQPc)

## Johdanto Rustiin (3/7)
<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>

![video](https://youtu.be/R8NeHvHT0uc)

## Johdanto Rustiin (4/7)
<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>
![video](https://youtu.be/et8pKvYiO4c)

## Johdanto Rustiin (5/7)
<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>

![video](https://youtu.be/PxQkVmxOc40)

## Johdanto Rustiin (6/7)
<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>

![video](https://youtu.be/3C6hl9BW-Ho)

## Johdanto Rustiin (7/7)
<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>

![video](https://youtu.be/SBDcb_AauHM)

# Rust & BTC 
<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>

## Miksi Rust Bitcoinille
<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>

![video](https://youtu.be/veLj2w6ulpc)

## Virhemalli
<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>

![video](https://youtu.be/X3VKhLtKTRU)

## Unniffit
<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>

![video](https://youtu.be/zro9GQpJrH0)

## Asynkroniset traitit
<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>

![video](https://youtu.be/cz66eTfk0lw)

# LNP/BP:n kehittäminen SDK:n avulla
<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>

## LN-solmu SDK:lla
<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>

![video](https://youtu.be/aEzpxuhLdeo)

## Breez sdk
<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>

![video](https://youtu.be/M3ad9BE6ovo)

## Greenlight lipalle
<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>

![video](https://youtu.be/gKiIPF4apeE)

## Breez sdk lipalle
<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>

![video](https://youtu.be/6VaIVvBKjLY)

# Yhteenveto
<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Arviot & Arvosanat
<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>
<isCourseReview>true</isCourseReview>

## Loppusanat
<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>
<isCourseConclusion>true</isCourseConclusion>
