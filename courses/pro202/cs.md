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

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematika pro implementaci Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Kryptografie eliptických křivek

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Transakce Bitcoin Vnitřní součásti

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Rozbor transakcí a podpisy ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Ověřování skriptů a transakcí Bitcoin

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Konstrukce transakcí a Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Vnitřní struktury sítě Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bloky Bitcoin a Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Síťová komunikace a Merklovy stromy

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Pokročilá komunikace uzlů a oddělený svědek

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Závěrečná část


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Recenze a hodnocení


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>


## Závěr


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
