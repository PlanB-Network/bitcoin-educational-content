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

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Matematik för implementering av Bitcoin

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Kryptografi med elliptisk kurva

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Transaktion Innerworkings

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Transaktionsparsning och ECDSA-signaturer

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Skript- och transaktionsvalidering

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Transaktionskonstruktion och Pay-to-Script Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin-nätverket Innerworkings

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Bitcoin Block och Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Nätverkskommunikation och Merkle-träd

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Avancerad nodkommunikation och segregerat vittne

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Sista avsnittet


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Recensioner & betyg


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Slutsats


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
