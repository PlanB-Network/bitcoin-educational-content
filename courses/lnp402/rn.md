---
name: Guteza imbere ku Muravyo na SDK
goal: Teza imbere ubuhinga bwawe bwo gutegura imiravyo n’amahugurwa yo hagati ya Rust na SDK.
objectives: 

  - Menya ururimi rwa Rust
  - Gutahura igituma ukoresha Rust mu gutegura Bitcoin.
  - Kuronka ishingiro rya SDK

---

# Gutera imbere mu buhinga bwawe bwo gutegura LN


Ikaze mu rugendo rwawe rwa LN na SDK.


Muri iki cigwa, uzokwiga ivy’ishimikiro vyo mu gitabu ca Rust, hanyuma ukurikizeho porogarama zimwe zimwe za LN ukoresheje SDKs, hanyuma uheze n’imyimenyerezo imwe imwe y’ingirakamaro. Abigisha bacu bava mu mice itandukanye bazokuyobora mu bijanye n’ubuhinga ngirakamaro bongere bagusigurire ingorane zitandukanye abahinga bo muri iki gihe ba LN bakunda guhura na zo.


Iryo shure ryafashwe amasanamu mu gihe c'amahugurwa yateguwe na Fulgur'Ventures mu gihe c'umusi mukuru wa LN muri Toscane mu kwezi kwa Gitugutu 2023.


Nimwinovore inyigisho!


+++

# Imenyekanisha

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Incamake y'amashure

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Imenyekanisha**


Ikaze muri iri shure ry'ivy'ubuhinga bwa none ku bijanye na SDKs. Muri iri huriro, uzokwiga ivy’ishimikiro vya Rust, hanyuma wibande kuri BTC & Rust, hanyuma uheze n’imyimenyerezo imwe imwe ukoresheje SDKs.


Iryo huriro rizoba mu congereza gusa ubu kandi ryari mu nama y’ubuzima yateguwe mu kwezi kwa Gitugutu guheze i Toscane na Fulgure Venture. Porogarama y’ikiganiro ca LIVE ushobora kuyibona aha hepfo, kandi iyi nyigisho izoba ishingiye ku ndwi ya mbere gusa. Igice ca kabiri cari kigenewe RGB kandi gishobora gusangwa mu nyigisho ya RGB.


**Abigisha**


Turashimira cane abigisha bacu babaye muri iyo porogarama:



- Alekos : "Hey, ndi umuhinga mu vy'amakode n'umunyagihugu w'umutaliyano. Nakoze ku migambi itandukanye nka bitcoindevkit, magicalbitcoin na h4ckbs".
- Andrei : "Umuhinga mu vy'imiravyo muri LIPA".
- Gabriel : "Ndandika code kandi nkora ibintu."
- Jesse de wit : "Umukunzi wa Lightning Network | umuhinguzi | Umuyaga"


**Ingingo y'amaseminari**


Indwi ya mbere y'ikiganiro ca LN co muri Toscane

![image](assets/1.webp)


Uhejeje iri shure, nimba ushaka gukurikirana amahugurwa, ng’iki igice ca kabiri c’urutonde:

![image](assets/2.webp)



Iryo huriro riguha akaryo ko guteza imbere ubuhinga bwawe bwo gukora porogarama kuri Lightning Network ukoresheje Rust na SDK zitandukanye. Igenewe abahinguzi bafise ubumenyi bukomeye bwo gukora porogarama bashaka kwisuka mu gutegura ivy’ubuhinga bwa Lightning Network. Uzokwiga ivy’ishimikiro vya Rust, igituma ibereye gutegura Bitcoin, hanyuma ugende ku gushirwa mu ngiro ukoresheje SDKs zidasanzwe.


**Igice ca 2: Iga gukora code na Rust**

Muri iki gice, uzobona ivy’ishimikiro vya Rust biciye mu bice bigenda biratera imbere. Uzokwiga kwandika kode ya Rust, utahure ivyihariye vyayo, kandi umenye neza ibintu vyayo vy’ingenzi mu bice indwi vy’ido n’ido. Iyi module ni ngombwa kugira ngo umuntu atahure igituma Rust ari ururimi rwo gukunda cane mu guteza imbere Bitcoin.


**Igice ca 3: Rust na Bitcoin**

Aha, tuzokwihweza mu buryo bwimbitse igituma Rust ari ihitamwo ribereye mu guteza imbere Bitcoin. Uzomenya ivyerekeye urugero rwayo rw’ikosa, igikoresho ca UniFFI, n’ibiranga asynchronous – vyose ni urufunguruzo rwa Elements mu kwubaka porogarama zikomeye kandi zitekanye.


**Igice ca 4: Iterambere rya LNP/BP n'ama SDK**

Uzomenya ingene wokora ama node ya LN ukoresheje SDK zitandukanye nka Breez SDK na Greenlight ya Lipa. Uzobona ingene woshira mu ngiro ibikorwa vya Lightning Network ukoresheje amasomero yagenewe kworohereza Bitcoin n’iterambere rya Lightning.


Ni mwiteguye gukura mu buhinga bwanyu bwa Lightning Network na Rust? Reka tugende!

# Iga ingene wokora kode ukoresheje igitabu Rust .

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Intangamarara ya Rust (1/7)

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<Id y'umwigisha>e7e63d59-ea19-4960-9446-61bd4dcc98f0</Id y'umwigisha>


:::id ya videwo=12a518cf-64be-43f1-b6d4-f6592a1324ea:::


## Intangamarara ya Rust (2/7)

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::id ya videwo=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


## Intangamarara ya Rust (3/7)

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::id ya videwo=c78a543f-1462-43a1-9845-889d310d31a4::


## Intangamarara ya Rust (4/7)

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::id ya videwo=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::


## Intangamarara ya Rust (5/7)

<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::id ya videwo=5514da77-5b71-4763-96b8-49eb21291c2b:::


## Intangamarara ya Rust (6/7)

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::id ya videwo = 44c681d1-d154-4240-b3e8-15590cbfcbd2::


## Intangamarara ya Rust (7/7)

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::id ya videwo=5e96914d-df02-4781-ae54-b06008952301::


# Rust na BTC

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Kubera iki Rust kuri Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::id ya videwo=f59c4951-e109-4c70-b7da-41721e50ab04:::


## Ikosa ry'akarorero

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::id ya videwo=9fac0184-8443-4c36-8afd-8acb21fb43c3:::


## Udafise

<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::id ya videwo=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::


## Ibiranga Async

<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>


:::id ya videwo=8926dd48-3613-43b6-a509-60ba26ec337f:::


# Gutegura LNP/BP na SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## LN urudodo kuri SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::id ya videwo=94b9inzuki6-154e-4b9c-a8ce-5e2d9e9656a2:::


## Umuyaga sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::id ya videwo = 68d1f253-6210-4eab-8329-b676e5772eac:::


## Umuco w'icatsi kibisi kuri lipa

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::id ya videwo=c3dec3df-1416-4761-b7c8-e1d66d27e390:::


## Umuyaga sdk kuri lipa

<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>


:::id ya videwo=f2770a37-a22f-43d7-9334-8de60eaacff8:::


# Igice ca nyuma

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>




## Amasuzuma n'Ibipimo

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Iciyumviro

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>