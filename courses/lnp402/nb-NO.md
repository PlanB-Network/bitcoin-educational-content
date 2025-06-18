---
name: Developping on Lightning with SDK
goal: Avanser dine lynutviklingsferdigheter med mellomnivå Rust og SDK-opplæring.
objectives:
  - Bli vant til Rust-språket
  - Forstå hvorfor Rust brukes for å utvikle Bitcoin
  - Få grunnlaget av SDK
---

# Videreutvikling av dine LN-utviklingsferdigheter

Velkommen til din LN-reise med SDK.

I dette kurset vil du lære grunnleggende om Rust-boken, deretter fortsette med noe LN-programmering ved bruk av SDK-er, og avslutte med noen praktiske øvelser. Våre lærere fra ulike bakgrunner vil veilede deg mot praktiske ferdigheter og forklare de ulike utfordringene dagens LN-ingeniører ofte står overfor.

Dette kurset ble filmet under et LIVE-seminar organisert av Fulgur'Ventures under LN Tuscany-arrangementet i oktober 2023.

Nyt kurset!

+++

# Introduksjon

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>

## Kursoversikt

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>

**Introduksjon**

Velkommen til dette avanserte programmeringskurset om SDK-er. I denne opplæringen vil du lære grunnleggende om Rust, deretter fokusere på BTC & Rust, og avslutte med noen praktiske øvelser ved bruk av SDK-er.

Denne opplæringen vil for øyeblikket kun være tilgjengelig på engelsk og var en del av et live-seminar organisert sist oktober i Toscana av Fulgure Venture. Programmet for LIVE-arrangementet kan finnes nedenfor, og denne opplæringen vil fokusere på den første uken bare. Den andre halvdelen var rettet mot RGB og kan finnes i RGB-kurset.

**Lærere**

Mange takk til våre lærere som har vært en del av dette programmet:

- Alekos: "Hei, jeg er en italiensk koder og hacker. Jeg har jobbet med ulike prosjekter som bitcoindevkit, magicalbitcoin og h4ckbs"
- Andrei: "Lightning-ekspert hos LIPA"
- Gabriel: "Jeg skriver kode og gjør ting."
- Jesse de Wit: "Lightning network-entusiast | utvikler | Breez"

**Seminarplan**

Uke 1 av LN Tuscany-arrangementet
![bilde](assets/1.webp)

Når du har fullført dette kurset, hvis du er interessert i oppfølgingstreningen, her er den andre delen av planen:
![bilde](assets/2.webp)


Denne opplæringen gir deg muligheten til å utvikle dine programmeringsferdigheter på Lightning Network ved å bruke Rust og ulike SDK-er. Den er laget for utviklere som allerede har god kjennskap til programmering og som ønsker å fordype seg i spesifikk utvikling for Lightning Network. Du vil lære det grunnleggende om Rust, hvorfor det egner seg til Bitcoin-utvikling, og deretter gå over til praktisk implementering med spesialiserte SDK-er.

**Del 2: Lær å kode med Rust**  
I denne delen vil du lære det grunnleggende om Rust gjennom en serie med progressive kapitler. Du vil lære å skrive Rust-kode, forstå dets særegenheter og mestre dets essensielle funksjoner gjennom syv detaljerte deler. Denne modulen er viktig for å forstå hvorfor Rust er et foretrukket språk for Bitcoin-utvikling.

**Del 3: Rust & Bitcoin**  
Her vil vi utforske i dybden hvorfor Rust er et relevant valg for Bitcoin-utvikling. Du vil lære om dets feilhåndteringsmodell, verktøyet UniFFI, samt asynkrone traits – viktige elementer for å bygge robust og sikker programvare.

**Del 4: LNP/BP-utvikling med SDK-er**  
Her lærer du å utvikle LN-noder ved hjelp av ulike SDK-er som Breez SDK og Greenlight for Lipa. Du vil se hvordan man implementerer Lightning Network-applikasjoner ved å bruke biblioteker som er laget for å forenkle utviklingen av Bitcoin- og Lightning-applikasjoner.

Klar til å utvikle ferdighetene dine på Lightning Network med Rust? La oss sette i gang!
# Lær hvordan du koder med Rust-boken

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>

## Introduksjon til Rust (1/7)

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>
<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>

:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

## Introduksjon til Rust (2/7)

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>

:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::

## Introduksjon til Rust (3/7)

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>

:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

## Introduksjon til Rust (4/7)

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>
:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

## Introduksjon til Rust (5/7)

<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>

:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

## Introduksjon til Rust (6/7)

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>

:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

## Introduksjon til Rust (7/7)

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>

:::video id=5e96914d-df02-4781-ae54-b06008952301:::

# Rust & BTC

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>

## Hvorfor Rust for Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>

:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::

## Feilmodell

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>

:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

## Unniffit

<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>

:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

## Asynkrone trekk

<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>

:::video id=8926dd48-3613-43b6-a509-60ba26ec337f:::

# Utvikling av LNP/BP med SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>

## LN node på SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>

:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>

:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

## Greenlight for lipa

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>

:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

## Breez sdk for lipa

<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>

:::video id=f2770a37-a22f-43d7-9334-8de60eaacff8:::

# Siste seksjon

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>

## Vurderinger & Karakterer

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>
<isCourseReview>true</isCourseReview>

## Konklusjon

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>
<isCourseConclusion>true</isCourseConclusion>
