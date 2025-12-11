---
name: Programování Bitcoin
goal: Vytvoření kompletní knihovny Bitcoin od nuly a pochopení kryptografických základů Bitcoin
objectives: 

 - Implementace aritmetiky konečného pole a operací s eliptickými křivkami v jazyce Python
 - Programová konstrukce a analýza transakcí Bitcoin
 - Vytváření adres Testnet a vysílání transakcí v síti
 - Zvládnutí matematických základů bezpečnostního modelu Bitcoin

---
# Cesta ke skriptům a programům Bitcoin


Tento intenzivní dvoudenní kurz, který vede Jimmy Song, vás zavede hluboko do technických základů Bitcoin a umožní vám vytvořit kompletní knihovnu Bitcoin od základů. Začínáte základní matematikou konečných polí a eliptických křivek a postupujete přes zpracování transakcí, provádění skriptů a síťovou komunikaci. Prostřednictvím praktických kódovacích cvičení v zápisnících Jupyter si vytvoříte vlastní Testnet Address, ručně zkonstruujete transakce a odvysíláte je přímo do sítě - to vše při hlubokém pochopení kryptografických principů, díky nimž je Bitcoin bezpečný a Trustless bezpečný.


Užijte si svůj objev!


+++

# Úvod

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Přehled kurzu

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Vítejte v kurzu PRO 202 _**Programování Bitcoinu**_, intenzivní cestě, která vás provede od aritmetiky konečných polí až po vytváření a vysílání skutečných transakcí v testovací síti Bitcoinu.

V tomto kurzu budete postupně vytvářet bitcoinovou knihovnu v Pythonu a zároveň získáte kryptografické, protokolární a softwarové základy potřebné k přesnému pochopení bezpečnosti a vnitřního fungování Bitcoinu. Přístup PRO 202 je zcela praktický: každý koncept je okamžitě implementován v Jupyter noteboocích, což zajišťuje, že teorie a kód se navzájem posilují.

### Základní matematické koncepty pro Bitcoin

Tato první část vytváří nezbytné matematické základy. Implementujete aritmetiku konečných polí a operace na eliptických křivkách (grupový zákon, sčítání, zdvojení, násobení skalárem...) — předpoklady pro ECDSA. Cíl je dvojnásobný: pochopit algebraickou strukturu, která umožňuje kryptografické podpisy, a vytvořit spolehlivé nástroje v Pythonu pro jejich manipulaci.

Poté formalizujete komponenty ECDSA: generování klíčů, formátování bodů, hašování, vytváření a ověřování podpisů. Tato část přímo propojuje teorii s praxí, zdůrazňuje detaily implementace a robustnost základního bezpečnostního modelu.

### Vnitřní fungování bitcoinové transakce

V druhé části rozeberete strukturu bitcoinové transakce: UTXO, vstupy/výstupy, sekvence, skripty, kódování a další. Napíšete kód pro vytvoření, podepsání a ověření transakcí, čímž získáte přesné pochopení toho, co je hashováním závazně potvrzeno a proč.

Dále implementujete minimalistický vykonavatel _Scriptu_, přezkoumáte klíčové opkódy a ověříte cesty utrácení. Cílem je, abyste byli schopni auditovat chování transakcí, diagnostikovat chyby ověřování a uvažovat o bezpečnosti zásad utrácení.

### Vnitřní fungování bitcoinové sítě

Ve třetí části umístíte transakci do širšího systému: struktura bloku, hlavičky, obtížnost a mechanismus Proof-of-Work. Budete pracovat s protokolovými zprávami, hlavičkami bloků a Merkleho stromy.

Nakonec se budete zabývat komunikací uzlů peer-to-peer, optimalizací zpráv a zavedením SegWitu.

Stejně jako u každého kurzu na Plan ₿ Academy obsahuje závěrečná část hodnocení navržené tak, aby upevnilo vaše porozumění. Jste připraveni odhalit vnitřní fungování Bitcoinu a napsat kód, který jej pohání? Začněme!

# Základní matematické pojmy pro Bitcoin

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Matematika pro implementaci Bitcoin

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Kryptografie eliptických křivek

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Transakce Bitcoin Vnitřní součásti

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Rozbor transakcí a podpisy ECDSA

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Ověřování skriptů a transakcí Bitcoin

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Konstrukce transakcí a Pay-to-Script Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Vnitřní struktury sítě Bitcoin

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Bloky Bitcoin a Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Síťová komunikace a Merklovy stromy

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Pokročilá komunikace uzlů a oddělený svědek

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Závěrečná část


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Recenze a hodnocení


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Závěr


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
