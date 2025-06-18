---
name: Razvijanje na Lightning-u sa SDK
goal: Unapredite svoje veštine razvoja munje sa srednjim Rust i SDK obukama.
objectives: 

  - Navikni se na Rust jezik
  - Razumeti zašto koristiti Rust za razvijanje Bitcoin
  - Nabavite osnovu SDK

---

# Napredovanje u vašim LN dev veštinama


Dobrodošli na vaše LN putovanje sa SDK.


Na ovom kursu ćete naučiti osnove Rust knjige, zatim nastaviti sa LN programiranjem koristeći SDK-ove, i završiti sa praktičnim vežbama. Naši nastavnici iz različitih oblasti će vas voditi ka praktičnim veštinama i objasniti razne izazove sa kojima se današnji LN inženjeri često suočavaju.


Ovaj kurs je snimljen tokom LIVE seminara koji je organizovao Fulgur'Ventures tokom LN Tuscany događaja u oktobru 2023.


Uživaj u kursu!


+++

# Uvod

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Pregled kursa

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Uvod**


Dobrodošli na ovaj napredni kurs programiranja o SDK-ovima. U ovoj obuci ćete naučiti osnove Rust, zatim se fokusirati na BTC & Rust, i završiti sa praktičnim vežbama koristeći SDK-ove.


Ova obuka će biti dostupna samo na engleskom jeziku za sada i bila je deo seminara uživo organizovanog prošlog oktobra u Toskani od strane Fulgure Venture. Program događaja UŽIVO možete pronaći ispod, a ova obuka će se fokusirati samo na prvu nedelju. Druga polovina je bila usmerena na RGB i može se pronaći u kursu RGB.


**Nastavnici**


Mnogo hvala našim nastavnicima koji su bili deo ovog programa:



- Alekos : "Hej, ja sam italijanski koder i haker. Radio sam na raznim projektima kao što su bitcoindevkit, magicalbitcoin i h4ckbs"
- Andrei : "Stručnjak za munje u LIPA-i"
- Gabriel : "Pišem kod i radim stvari."
- Jesse de wit : "Lightning Network entuzijasta | developer | Breez"


**Seminaire schedual**


Nedelja 1 LN Toskana događaja

![image](assets/1.webp)


Kada završite ovaj kurs, ako ste zainteresovani za nastavak obuke, ovde je drugi deo rasporeda:

![image](assets/2.webp)



Ova obuka vam pruža priliku da razvijete svoje programerske veštine na Lightning Network koristeći Rust i razne SDK-ove. Dizajnirana je za programere sa solidnim programerskim iskustvom koji žele da se upuste u razvoj specifičan za Lightning Network. Naučićete osnove Rust, zašto je pogodan za razvoj na Bitcoin, a zatim preći na praktičnu implementaciju koristeći specijalizovane SDK-ove.


**Sekcija 2: Naučite programirati sa Rust**

U ovom odeljku ćete otkriti osnove Rust kroz seriju progresivnih poglavlja. Naučićete da pišete Rust kod, razumete njegove specifičnosti i savladate njegove osnovne karakteristike kroz sedam detaljnih delova. Ovaj modul je ključan za razumevanje zašto je Rust omiljeni jezik za razvoj Bitcoin.


**Sekcija 3: Rust & Bitcoin**

Ovde ćemo detaljno istražiti zašto je Rust relevantan izbor za razvoj Bitcoin. Saznaćete o njegovom modelu grešaka, alatu UniFFI i asinhronim osobinama – sve ključne Elements u izgradnji robusnog i sigurnog softvera.


**Sekcija 4: LNP/BP razvoj sa SDK-ovima**

Naučićete kako da razvijate LN čvorove koristeći razne SDK-ove kao što su Breez SDK i Greenlight za Lipa. Videćete kako da implementirate Lightning Network aplikacije koristeći biblioteke dizajnirane da pojednostave razvoj Bitcoin i Lightning.


Spremni da unapredite svoje Lightning Network veštine sa Rust? Hajde da krenemo!

# Naučite kako da kodirate uz knjigu Rust

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Uvod u Rust (1/7)

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::


## Uvod u Rust (2/7)

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


## Uvod u Rust (3/7)

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::


## Uvod u Rust (4/7)

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::


## Uvod u Rust (5/7)

<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::


## Uvod u Rust (6/7)

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::


## Uvod u Rust (7/7)

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::


# Rust & BTC

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Zašto Rust po Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


## Model greške

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::


## Unniffit

<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::


## Asinhroni trejti

<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>


:::video id=8926dd48-3613-43b6-a509-60ba26ec337f:::


# Razvijanje LNP/BP sa SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## LN čvor na SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::


## Zeleno svetlo za lipu

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::


## Breez sdk za lipa

<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>


:::video id=f2770a37-a22f-43d7-9334-8de60eaacff8:::


# Završni Deo

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>




## Recenzije i ocene

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Zaključak

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>