---
name: Utveckling av Lightning med SDK
goal: Förbättra dina färdigheter inom blixtutveckling med mellanliggande Rust- och SDK-utbildning.
objectives: 

  - Vänj dig vid Rust-språket
  - Förstå varför man använder Rust för att utveckla Bitcoin
  - Skaffa grunden för SDK

---

# Förbättra dina LN-utvecklingsfärdigheter


Välkommen till din LN-resa med SDK.


I den här kursen kommer du att lära dig grunderna i Rust-boken, sedan följa upp med lite LN-programmering med hjälp av SDK och avsluta med några praktiska övningar. Våra lärare med olika bakgrunder kommer att vägleda dig mot praktiska färdigheter och förklara de olika utmaningar som dagens LN-ingenjörer ofta står inför.


Den här kursen filmades under ett LIVE-seminarium som anordnades av Fulgur'Ventures under LN Tuscany-evenemanget i oktober 2023.


Njut av kursen!


+++

# Inledning

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Kursöversikt

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Introduktion**


Välkommen till denna avancerade programmeringskurs om SDK:er. I den här utbildningen lär du dig grunderna i Rust, fokuserar sedan på BTC & Rust och avslutar med några praktiska övningar med SDK.


Denna utbildning kommer endast att vara tillgänglig på engelska för tillfället och var en del av ett live-seminarium som organiserades i oktober förra året i Toscana av Fulgure Venture. Programmet för LIVE-evenemanget finns nedan, och den här utbildningen kommer endast att fokusera på den första veckan. Den andra halvan var inriktad på RGB och finns i RGB-kursen.


**Lärare**


Stort tack till våra lärare som har varit en del av detta program:



- Alekos : "Hej, jag är en italiensk kodare och hacker. jag har arbetat med olika projekt som bitcoindevkit, magicalbitcoin och h4ckbs"
- Andrei : "Blixtexpert på LIPA"
- Gabriel : "Jag skriver kod och gör saker."
- Jesse de wit : "Lightning Network-entusiast | utvecklare | Breez"


**Seminaire schema**


Vecka 1 av LN:s evenemang i Toscana

![image](assets/1.webp)


När du har avslutat den här kursen och är intresserad av uppföljningsutbildningen kommer här den andra delen av schemat:

![image](assets/2.webp)



Den här utbildningen ger dig möjlighet att utveckla dina programmeringskunskaper på Lightning Network med hjälp av Rust och olika SDK:er. Den är utformad för utvecklare med en gedigen programmeringsbakgrund som vill dyka in i Lightning Network-specifik utveckling. Du kommer att lära dig grunderna i Rust, varför det är lämpligt för Bitcoin-utveckling och sedan gå vidare till praktisk implementering med hjälp av specialiserade SDK:er.


**Avsnitt 2: Lär dig att koda med Rust**

I det här avsnittet kommer du att upptäcka grunderna i Rust genom en serie progressiva kapitel. Du får lära dig att skriva Rust-kod, förstå dess särdrag och behärska dess väsentliga funktioner i sju detaljerade delar. Denna modul är viktig för att förstå varför Rust är ett föredraget språk för Bitcoin-utveckling.


**Avsnitt 3: Rust & Bitcoin**

Här kommer vi att utforska på djupet varför Rust är ett relevant val för Bitcoin-utveckling. Du kommer att lära dig om dess felmodell, UniFFI-verktyget och asynkrona egenskaper - alla viktiga Elements för att bygga robust och säker programvara.


**Avsnitt 4: LNP/BP-utveckling med SDK:er**

Du får lära dig hur du utvecklar LN-noder med hjälp av olika SDK:er som Breez SDK och Greenlight for Lipa. Du får se hur du implementerar Lightning Network-applikationer med hjälp av bibliotek som är utformade för att förenkla Bitcoin- och Lightning-utveckling.


Redo att utöka dina Lightning Network-kunskaper med Rust? Nu kör vi!

# Lär dig att koda med Rust-boken

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Introduktion till Rust (1/7)

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::


## Introduktion till Rust (2/7)

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


## Introduktion till Rust (3/7)

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::


## Introduktion till Rust (4/7)

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::


## Introduktion till Rust (5/7)

<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::


## Introduktion till Rust (6/7)

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::


## Introduktion till Rust (7/7)

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::


# Rust & BTC

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Varför Rust jämfört med Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


## Felmodell

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::


## Otillräcklig

<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::


## Asynkrona egenskaper

<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>


:::video id=8926dd48-3613-43b6-a509-60ba26ec337f:::


# Utveckling av LNP/BP med SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## LN nod på SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::


## Grönt ljus för Lipa

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::


## Breez sdk för lipa

<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>


:::video id=f2770a37-a22f-43d7-9334-8de60eaacff8:::


# Sista avsnittet

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>




## Recensioner & betyg

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Slutsats

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>