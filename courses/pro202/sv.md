---
name: Programmering Bitcoin
goal: Bygga ett komplett Bitcoin-bibliotek från grunden och förstå Bitcoin:s kryptografiska grundprinciper
objectives: 

 - Implementera aritmetik för finita fält och elliptiska kurvor i Python
 - Konstruera och analysera Bitcoin-transaktioner programmatiskt
 - Skapa Testnet-adresser och sända transaktioner över nätverket
 - Behärska de matematiska grunderna som ligger till grund för Bitcoin:s säkerhetsmodell

---
# En resa till Bitcoin:s skript och program


Denna intensiva tvådagarskurs, som leds av Jimmy Song, tar dig djupt in i Bitcoin:s tekniska grunder genom att bygga ett komplett Bitcoin-bibliotek från grunden. Du börjar med den grundläggande matematiken för finita fält och elliptiska kurvor och går sedan vidare med transaktionsanalys, skriptexekvering och nätverkskommunikation. Genom praktiska kodningsövningar i Jupyter-anteckningsböcker skapar du din egen Testnet Address, konstruerar transaktioner manuellt och sänder dem direkt till nätverket - allt medan du får en djup förståelse för de kryptografiska principer som gör Bitcoin säker och Trustless.


Njut av din upptäckt!


+++

# Introduktion

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Kursöversikt

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Välkommen till kursen PRO 202 _**Programming Bitcoin**_, en intensiv resa som tar dig från aritmetik med ändliga fält till att bygga och sända verkliga transaktioner på Bitcoins testnät.

I denna kurs kommer du stegvis att bygga ett Bitcoin-bibliotek i Python samtidigt som du förvärvar de kryptografiska, protokollmässiga och mjukvarumässiga grunder som krävs för att exakt förstå Bitcoins säkerhet och inre funktioner. PRO 202-ansatsen är helt praktisk: varje koncept implementeras omedelbart i Jupyter-anteckningsböcker, vilket säkerställer att teori och kod stärker varandra.

### Grundläggande matematiska begrepp för Bitcoin

Denna första sektion etablerar den oumbärliga matematiska grunden. Du kommer att implementera aritmetik i ändliga kroppar och operationer för elliptiska kurvor (grupplagen, addition, dubblering, skalärmultiplikation...) — förutsättningarna för ECDSA. Målet är tvåfaldigt: att förstå den algebraiska struktur som gör kryptografiska signaturer möjliga och att bygga tillförlitliga Python-verktyg för att manipulera dem.

Därefter kommer du att formalisera komponenterna i ECDSA: nyckelgenerering, punktformatering, hashing, skapande och verifiering av signaturer. Detta avsnitt kopplar direkt samman teori med praktik och betonar implementeringsdetaljer samt robustheten i den underliggande säkerhetsmodellen.

### Den inre funktionen hos en Bitcoin-transaktion

I det andra avsnittet kommer du att analysera strukturen av en Bitcoin-transaktion: UTXO:er, in-/utgångar, sekvenser, skript, kodningar och mer. Du kommer att skriva kod för att konstruera, signera och verifiera transaktioner, och få en exakt förståelse av vad som förbinds av hash och varför.

Därefter kommer du att implementera en minimal _Script_-tolk, granska viktiga opkoder och validera utgiftsvägar. Målet är att göra dig kapabel att granska transaktionsbeteenden, diagnostisera valideringsfel och resonera kring säkerheten i utgiftspolicys.

### Den inre funktionen hos Bitcoin-nätverket

I det tredje avsnittet kommer du att placera transaktionen inom det bredare systemet: blockstruktur, rubriker, svårighetsgrad och Proof-of-Work-mekanismen. Du kommer att hantera protokollmeddelanden, blockrubriker och Merkle-träd.

Slutligen kommer du att studera peer-to-peer-nodkommunikation, meddelandeoptimering och introduktionen av SegWit.

Som med varje kurs på Plan ₿ Academy innehåller det sista avsnittet en utvärdering som är utformad för att befästa din förståelse. Redo att avslöja Bitcoins inre funktioner och skriva koden som driver det? Låt oss börja!

# Grundläggande matematiska begrepp för Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematik för implementering av Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Kryptografi med elliptisk kurva

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Transaktion Innerworkings

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Transaktionsparsning och ECDSA-signaturer

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Skript- och transaktionsvalidering

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Transaktionskonstruktion och Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin-nätverket Innerworkings

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin Block och Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Nätverkskommunikation och Merkle-träd

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Avancerad nodkommunikation och segregerat vittne

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Sista avsnittet


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Recensioner & betyg


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Slutsats


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
