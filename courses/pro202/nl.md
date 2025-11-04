---
name: Programmering Bitcoin
goal: Een complete Bitcoin bibliotheek vanaf nul opbouwen en de cryptografische fundamenten van Bitcoin begrijpen
objectives: 

 - Eindige veldrekenkundige en elliptische krommebewerkingen implementeren in Python
 - Bitcoin transacties programmatisch opbouwen en parsen
 - Testnet adressen aanmaken en transacties uitzenden over het netwerk
 - De wiskundige fundamenten beheersen die ten grondslag liggen aan het Bitcoin beveiligingsmodel

---
# Een reis naar de scripts en programma's van Bitcoin


Deze intensieve tweedaagse cursus, gegeven door Jimmy Song, neemt je mee in de technische fundamenten van Bitcoin door een complete Bitcoin bibliotheek vanaf de grond op te bouwen. Beginnend met de essentiële wiskunde van eindige velden en elliptische krommen, ga je verder met transactie parsing, script uitvoering en netwerk communicatie. Door middel van hands-on coderingsoefeningen in Jupyter notebooks maak je je eigen Testnet Address, construeer je handmatig transacties en zend je ze direct uit naar het netwerk - dit alles terwijl je een diepgaand begrip krijgt van de cryptografische principes die Bitcoin en Trustless veilig maken.


Geniet van je ontdekking!


+++

# Inleiding

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Cursusoverzicht

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Welkom bij de cursus PRO 202 _**Programming Bitcoin**_, een intensieve reis die je meeneemt van eindige-veldaritmetiek tot het bouwen en uitzenden van echte transacties op het testnet van Bitcoin.

In deze cursus bouw je stap voor stap een Bitcoin-bibliotheek in Python, terwijl je de cryptografische, protocol- en softwarebasis verwerft die nodig is om nauwkeurig te redeneren over de veiligheid en interne werking van Bitcoin. De PRO 202-aanpak is volledig praktisch: elk concept wordt direct geïmplementeerd in Jupyter-notebooks, zodat theorie en code elkaar versterken.

### Essentiële wiskundige concepten voor Bitcoin

Deze eerste sectie legt de onmisbare wiskundige basis. Je zult de rekenkunde van eindige velden en elliptische krommebewerkingen implementeren (groepwet, optelling, verdubbeling, scalair vermenigvuldigen...) — de vereisten voor ECDSA. Het doel is tweeledig: de algebraïsche structuur begrijpen die cryptografische handtekeningen mogelijk maakt en betrouwbare Python-hulpmiddelen bouwen om deze te manipuleren.

Vervolgens formaliseer je de componenten van ECDSA: sleutelaanmaak, puntopmaak, hashing, handtekeningcreatie en verificatie. Deze sectie verbindt theorie direct met praktijk en benadrukt implementatiedetails en de robuustheid van het onderliggende beveiligingsmodel.

### De interne werking van een Bitcoin-transactie

In het tweede deel zal je de structuur van een Bitcoin-transactie ontleden: UTXO’s, inputs/outputs, sequenties, scripts, coderingen en meer. Je zult code schrijven om transacties te bouwen, te ondertekenen en te verifiëren, en zo een nauwkeurig begrip krijgen van wat de hash vastlegt en waarom.

Vervolgens implementeer je een minimale _Script_-uitvoerder, bekijk je belangrijke opcodes en valideer je de uitgavenpaden. Het doel is dat je in staat bent het transactiegedrag te auditen, validatiefouten te diagnosticeren en te redeneren over de veiligheid van bestedingsbeleid.

### De interne werking van het Bitcoin-netwerk

In het derde deel plaats je de transactie binnen het bredere systeem: blokstructuur, headers, moeilijkheidsgraad en het Proof-of-Work-mechanisme. Je zult protocolberichten, blokheaders en Merkle-bomen behandelen.

Tot slot bestudeer je peer-to-peer-knooppuntcommunicatie, berichtoptimalisatie en de introductie van SegWit.

Zoals bij elke cursus op Plan ₿ Academy bevat het laatste gedeelte een evaluatie die is ontworpen om je begrip te versterken. Klaar om de interne werking van Bitcoin te ontdekken en de code te schrijven die het aandrijft? Laten we beginnen!

# Essentiële wiskundige concepten voor Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Wiskunde voor Bitcoin implementatie

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Elliptische kromme cryptografie

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Transactie Binnenwerk

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Transactie parsing en ECDSA-handtekeningen

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Script- en transactievalidatie

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Transactieconstructie en Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin netwerk binnenwerk

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin Blokken en Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Netwerkcommunicatie en Merklebomen

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Geavanceerde knooppuntcommunicatie en gescheiden getuigenissen

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Laatste Sectie


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Beoordelingen


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>


## Conclusie


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
