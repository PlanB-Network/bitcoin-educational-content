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

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Wiskunde voor Bitcoin implementatie

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Elliptische kromme cryptografie

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Transactie Binnenwerk

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Transactie parsing en ECDSA-handtekeningen

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Script- en transactievalidatie

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Transactieconstructie en Pay-to-Script Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin netwerk binnenwerk

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Bitcoin Blokken en Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Netwerkcommunicatie en Merklebomen

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Geavanceerde knooppuntcommunicatie en gescheiden getuigenissen

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Laatste Sectie


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Beoordelingen


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Conclusie


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
