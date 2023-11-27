---
name: Inleiding tot Kriptografie
goal: Verstaan die skep van 'n Bitcoin-bewaarplek vanuit 'n kriptografiese perspektief
objectives:
  - Ontmasker die terminologie van kriptografie wat verband hou met Bitcoin.
  - Meester die skepping van 'n Bitcoin-bewaarplek.
  - Verstaan die struktuur van 'n Bitcoin-bewaarplek.
  - Verstaan ​​adres en afleidingspaaie.
---

# 'n Reis in kriptografie

Is jy gefassineer deur Bitcoin? Wonder jy hoe 'n Bitcoin-bewaarplek werk? Maak gereed om op 'n boeiende reis in kriptografie te gaan! Loïc, ons kenner, sal jou deur die ingewikkeldhede van die skepping van 'n Bitcoin-bewaarplek lei en die geheime agter intimiderende tegniese terme soos hasing, sleutelafleiding, en elliptiese kurwes onthul.

Hierdie opleiding sal jou nie net toerus met die kennis om die struktuur van 'n Bitcoin-bewaarplek te verstaan ​​nie, maar jou ook voorberei om diep in die opwindende wêreld van kriptografie in te duik. Is jy gereed om op hierdie reis te gaan? Sluit by ons aan en omskep jou nuuskierigheid in kundigheid!

+++

# Inleiding

## Inleiding tot Kriptografie

### Is hierdie opleiding vir jou? JA!

![inleiding deur Rogzy](https://youtu.be/ul8zU5QWIXg)

Ons is verheug om jou te verwelkom by die nuwe opleidingskursus getiteld "Crypto 301: Inleiding tot Kriptografie en HD-bewaarplek", georkestreer deur die kenner self, Loïc Morel. Hierdie kursus sal jou onderdompel in die boeiende wêreld van kriptografie, die fundamentele dissipline van wiskunde wat verseker dat jou data geënkripteer en veilig is.

In ons daaglikse lewe, en veral in die wêreld van Bitcoin, speel kriptografie 'n belangrike rol. Konsepte wat verband hou met kriptografie, soos privaat sleutels, openbare sleutels, adresse, afleidingspaaie, saad, en entropie, is die kern van die gebruik en skepping van 'n Bitcoin-bewaarplek. Gedurende hierdie kursus sal Loïc in detail verduidelik hoe privaat sleutels gegenereer word en hoe hulle gekoppel is aan adresse. Loïc sal ook 'n uur wy aan die verduideliking van die wiskundige besonderhede van elliptiese kurwes, hierdie komplekse wiskundige kurwe. Daarbenewens sal jy verstaan ​​waarom die gebruik van HMAC SHA512 belangrik is vir die beveiliging van jou bewaarplek en wat die verskil is tussen saad en mnemoniese frase.

Die uiteindelike doel van hierdie opleiding is om jou in staat te stel om die tegniese prosesse van die skepping van 'n HD-bewaarplek en die gebruikte kriptografiese metodes te verstaan. Deur die jare het Bitcoin-bewaarplekke ontwikkel om makliker om te gebruik, veiliger, en gestandaardiseer te word danksy spesifieke BIP's. Loïc sal jou help om hierdie BIP's te verstaan ​​om die keuses wat deur Bitcoin-ontwikkelaars en kriptografen gemaak is, te begryp. Soos al die opleidings wat deur ons universiteit aangebied word, is hierdie een heeltemal gratis en oopbron. Dit beteken dat jy dit vrylik kan neem en gebruik soos jy wil. Ons sien uit daarna om jou terugvoer aan die einde van hierdie opwindende kursus te ontvang.

### Die woord is aan jou, professor!

![inleiding deur Loïc](https://youtu.be/mwuxXLk4Kws)

Hallo almal, ek is Loïc Morel, jou gids deur hierdie tegniese verkenning van die kriptografie wat in Bitcoin-bewaarplekke gebruik word.

Ons reis begin met 'n duik in die dieptes van kriptografiese hasfunksies. Saam sal ons die innerlike werking van die noodsaaklike SHA256 ontled en verskeie algoritmes wat aan afleiding gewy is, verken.

Ons sal ons avontuur voortsit deur die geheimsinnige wêreld van digitale handtekeninge te ontsyfer. Jy sal ontdek hoe die toorkrag van elliptiese kurwes op hierdie handtekeninge van toepassing is, en ons sal lig werp op hoe om die openbare sleutel uit die privaat sleutel te bereken. En natuurlik, ons sal die handeling van ondertekening met die privaat sleutel aanspreek.
Volgende gaan ons terug in die tyd om die evolusie van Bitcoin beursies te sien, en ons sal die konsepte van entropie en lukrake getalle verken. Ons sal die bekende mnemoniese frase hersien, terwyl ons ook die onderwerp van wagwoorde ondersoek. Jy sal selfs die geleentheid hê om iets unieks te ervaar deur 'n saad van 128 dobbelsteenrolle te skep!

Met hierdie soliede grondslae sal ons gereed wees vir die belangrike deel: die skep van 'n Bitcoin beursie. Van die geboorte van die saad en die meestersleutel, tot die studie van uitgebreide sleutels en die afleiding van kindersleutelpare, sal elke stap ontleed word. Ons sal ook die struktuur van die beursie en afleidingspaaie bespreek.

Om dit alles af te rond, sal ons ons reis afsluit deur Bitcoin-adresse te ondersoek. Ons sal verduidelik hoe hulle geskep word en hoe hulle 'n essensiële rol speel in die werking van Bitcoin beursies.

Sluit by my aan op hierdie boeiende reis en maak gereed om die wêreld van kriptografie soos nooit tevore te verken. Los jou vooroordele by die deur en maak jou verstand oop vir 'n nuwe manier om Bitcoin en sy fundamentele struktuur te verstaan.

# Hashfunksies

## Inleiding tot kriptografiese hashfunksies wat verband hou met Bitcoin

![2.1 - Kriptografiese Hashfunksies](https://youtu.be/dvnGArYvVr8)

Welkom by vandag se sessie wat gewy is aan 'n diepgaande onderdompeling in die kriptografiese wêreld van hashfunksies, 'n essensiële hoeksteen van die Bitcoin-protokol se veiligheid. Stel jou 'n hashfunksie voor as 'n ultradoeltreffende kriptografiese ontsyferingsrobot wat inligting van alle groottes omskep in 'n unieke en vaste-grootte digitale vingerafdruk genaamd 'n "hash". Gedurende ons verkenning sal ons die profiel van kriptografiese hashfunksies skets, hul gebruik in die Bitcoin-protokol beklemtoon, en die spesifieke doelwitte wat hierdie kriptografiese funksies moet bereik, definieer.

![beeld](assets/image/section1/0.JPG)

Om die profiel van kriptografiese hashfunksies uit te beeld, vereis begrip van twee essensiële eienskappe: hul onomkeerbaarheid en hul weerstand teen vervalsing. Elke kriptografiese hashfunksie is soos 'n unieke kunstenaar wat 'n onderskeie "hash" vir elke inset produseer. Selfs 'n effense afwykende kwassie verander die finale skildery, m.a.w. die hash, aansienlik. Hierdie funksies tree op as digitale wagte, wat die integriteit van afgelaai sagteware verifieer. 'n Ander belangrike eienskap wat hulle besit, is hul weerstand teen botsings. In die wêreld van hashing is botsings beslis onvermydelik, maar 'n uitstekende kriptografiese hashfunksie verminder dit aansienlik. Dit is asof elke hash 'n huis in 'n groot stad is; ten spyte van die enorme aantal huise, verseker 'n goeie hashfunksie dat elke huis 'n unieke adres het.

![beeld](assets/image/section1/1.JPG)

Laat ons nou die onstuimige waters van verouderde hashfunksies navigeer. SHA0, SHA1 en MD5 word nou beskou as roesagtige relikwieë in die oseaan van kriptografiese hashing. Hulle word dikwels afgeraai omdat hulle hul weerstand teen botsings verloor het. Die beginsel van laaie verklaar waarom, ten spyte van ons beste pogings, botsingvermyding onmoontlik is as gevolg van die beperking van die uitsetgrootte. Dit is ook belangrik om daarop te let dat weerstand teen tweede voorbeeld afhanklik is van weerstand teen botsings. Om werklik as veilig beskou te word, moet 'n hashfunksie weerstand bied teen botsings, tweede voorbeeld en voorbeeld.

'n Sleutel-element in die Bitcoin-protokol is die SHA-256 hashfunksie, wat die kaptein van die skip is. Ander funksies, soos SHA-512, word gebruik vir afleiding met HMAC en PBKDF. Daarbenewens word RIPMD160 gebruik om 'n vingerafdruk tot 160 bits te verminder. Wanneer ons praat van HASH256 en HASH160, verwys ons na die gebruik van dubbele hashing met SHA-256 en RIPMD. Die gebruik van HASH160 is besonder voordelig omdat dit die veiligheid van SHA-256 toelaat terwyl die grootte van die vingerafdruk verminder word.
Om saam te vat, die uiteindelike doel van 'n kriptografiese hasfunksie is om arbitrêre-grootte inligting te transformeer na 'n vasgestelde grootte vingerafdruk. Om as veilig beskou te word, moet dit verskeie sterk punte hê: onomkeerbaarheid, weerstand teen vervalsing, weerstand teen botsings, en weerstand teen tweede prent.

Aan die einde van hierdie verkenning het ons kriptografiese hasfunksies ontrafel, hul gebruik in die Bitcoin-protokol beklemtoon, en hul spesifieke doelwitte ontleed. Ons het geleer dat hasfunksies weerstand moet bied teen prent, tweede prent, botsings, en vervalsing om as veilig beskou te word. Ons het ook die verskeidenheid hasfunksies wat in die Bitcoin-protokol gebruik word, bespreek. In ons volgende sessie sal ons die kern van die SHA256 hasfunksie ondersoek en die fassinerende wiskunde ontdek wat dit sy unieke eienskappe gee.

## Die Innerlike Werking van SHA256

![Die Innerlike Werking van SHA256](https://youtu.be/74SWg_ZbUj4)

Welkom by die voortsetting van ons fassinerende reis deur die kriptografiese doolhowe van die hasfunksie. Vandag onthul ons die geheime van SHA256, 'n komplekse maar vernuftige proses wat ons in ons vorige bespreking oor hasfunksies bekend gestel het. Kom ons neem nog 'n tree in hierdie doolhof, beginnende met die voorverwerking van SHA256. Stel jou voor dat voorverwerking die voorbereiding van 'n heerlike gereg is, waar ons "vulbits" byvoeg om die grootte van ons hoofbestanddeel, die inset, te maak tot 'n perfekte veelvoud van 512 bits. Dit alles met die uiteindelike doel om 'n smaaklike 256-bit has van 'n veranderlike-grootte bestanddeel te genereer.

![image](assets/image/section1/2.JPG)

In hierdie kriptografiese resep speel ons met bits, met 'n aanvanklike boodskapgrootte wat ons M sal noem. Een bit word gereserveer vir die skeier, terwyl P-bits gebruik word vir vulsel. Daarbenewens stel ons 64 bits apart vir die tweede voorverwerkingsfase. Die totaal moet 'n veelvoud van 512 bits wees. Dit is soos om seker te maak dat al die bestanddele perfek in ons gereg meng.

![image](assets/image/section1/3.JPG)
![image](assets/image/section1/4.JPG)

Ons gaan nou voort na die tweede fase van voorverwerking, wat die byvoeging van die binêre voorstelling van die aanvanklike boodskapgrootte, in bits, behels. Hiervoor gebruik ons ons 64 gereserveerde bits van die vorige stap. Ons voeg nulle by om ons 64 bits na 'n gebalanseerde inset af te rond. Dan meng ons die aanvanklike boodskap, die vulbits, en die grootte-vulsel, soos bestanddele in 'n blender, om ons gebalanseerde inset te verkry.

![image](assets/image/section1/5.JPG)

Nou maak ons gereed vir die eerste stappe van die SHA-256 funksie-verwerking. Soos in enige goeie resep, het ons basiese bestanddele nodig, wat ons konstantes en inisialisasievektore noem. Die inisialisasievektore, van A tot H, is die eerste 32 bits van die desimale dele van die vierkantswortels van die eerste 8 priemgetalle. Die konstantes K, van 0 tot 63, verteenwoordig die eerste 32 bits van die desimale dele van die kubieke wortels van die eerste 64 priemgetalle.

![image](assets/image/section1/6.JPG)

Binne die kompressiefunksie gebruik ons spesifieke operatore soos XOR, AND, en NOT. Ons verwerk die bits een vir een volgens hul rang, deur die XOR-operator en 'n waarheidstabel te gebruik. Die AND-operator word gebruik om slegs 1 terug te gee as beide operandi gelyk is aan 1, en die NOT-operator om die teenoorgestelde waarde van 'n operand terug te gee. Ons gebruik ook die SHR-operasie om die bits regs te skuif met 'n gekose getal.

![image](assets/image/section1/7.JPG)


![image](assets/image/section1/9.JPG)
Uiteindelik, nadat die gebalanseerde inset in verskillende blokke van 512-bit boodskappe verdeel is, voer ons 64 rondtes van berekening uit in die saampersfunksie. Soos in 'n fietswedren, verbeter elke rondte ons posisie. Ons voeg modulo 2^32 die tussenstaat by die aanvanklike staat van die saampersfunksie. Die optellings in die saampersfunksie is modulo 2^32 optellings om die grootte van die somme tot 32 bits te beperk.

![image](assets/image/section1/10.JPG)
![image](assets/image/section1/11.JPG)
![image](assets/image/section1/12.JPG)
![image](assets/image/section1/13.JPG)

Om af te sluit, wil ons die belangrike rol van die berekeninge wat in die CH, MAJ, σ0 en σ1 blokkies uitgevoer word, beklemtoon. Hierdie operasies, onder andere, is die beskermers wat die robuustheid van die SHA256 hasfunksie teen aanvalle verseker, wat dit 'n verkose keuse maak vir die beveiliging van talle digitale stelsels, veral binne die Bitcoin-protokol. Dit is duidelik dat, alhoewel dit kompleks is, die skoonheid van SHA256 lê in sy robuustheid om die inset vanaf die has te vind, terwyl die has vir 'n gegewe inset geverifieer word deur 'n meganies eenvoudige aksie.

## Die algoritmes wat gebruik word vir afleiding

![Die algoritmes wat gebruik word vir afleiding](https://youtu.be/ZF1_BMsOJXc)

Die HMAC- en PBKDF2-afleidingsalgoritmes is sleutelkomponente in die sekuriteitsmeganisme van die Bitcoin-protokol. Dit voorkom 'n verskeidenheid potensiële aanvalle en verseker die integriteit van Bitcoin-bewaarplekke.

HMAC en PBKDF2 is kriptografiese gereedskap wat vir verskillende take in Bitcoin gebruik word. HMAC word hoofsaaklik gebruik om lengte-uitbreidingsaanvalle te teenwerk wanneer hiërargies-deterministiese (HD) bewaarplekke afgelei word, terwyl PBKDF2 gebruik word om 'n mnemoniese frase in 'n saad te omskep.

![image](assets/image/section1/14.JPG)

HMAC, wat 'n boodskap en 'n sleutel as insette neem, genereer 'n vaste-grootte uitset. Om uniformiteit te verseker, word die sleutel aangepas op grond van die blokgrootte wat in die hasfunksie gebruik word. In die konteks van HD-bewaarplekafleiding word HMAC-SHA-512 gebruik. Die laasgenoemde werk met 1024-bit (128-byte) blokke en pas die sleutel dienooreenkomstig aan. Dit gebruik die konstantes OPAD (0x5c) en IPAD (0x36), herhaal indien nodig vir verbeterde sekuriteit.

Die HMAC-SHA-512-proses behels die saamvoeging van die resultaat van SHA-512 wat op die sleutel XOR OPAD en die sleutel XOR IPAD toegepas word, met die boodskap. Wanneer dit met 1024-bit (128-byte) blokke gebruik word, word die insetsleutel met nulle gepad indien nodig, dan XORed met IPAD en OPAD. Die gewysigde sleutel word dan saamgevoeg met die boodskap.

![image](assets/image/section1/15.JPG)

Die gebruik van 'n sout, deur 'n addisionele bron van entropie in te sluit, verhoog die sekuriteit van afgeleide sleutels. Sonder dit kan 'n aanval die hele bewaarplek in gevaar stel en al die bitcoins steel.
PBKDF2 word gebruik om 'n mnemoniese frase in 'n saad om te skakel. Hierdie algoritme voer 2048 rondtes uit met behulp van HMAC SHA512. Danksy hierdie afleidingsalgoritmes kan twee verskillende insette 'n unieke en vaste uitset produseer, wat die probleem van moontlike lengte-uitbreidingsaanvalle op SHA-2-funksies verminder. 'n Lengte-uitbreidingsaanval maak gebruik van 'n spesifieke eienskap van sekere kriptografiese hasfunksies. In so 'n aanval kan 'n aanvaller wat reeds die has van 'n onbekende boodskap het, dit gebruik om die has van 'n langer boodskap te bereken, wat 'n uitbreiding van die oorspronklike boodskap is. Dit is dikwels moontlik sonder om die inhoud van die oorspronklike boodskap te ken, wat tot aansienlike sekuriteitskwesbaarhede kan lei as hierdie tipe hasfunksie gebruik word vir take soos integriteitsverifikasie.
![beeld](assets/image/section1/16.JPG)

Ter afsluiting speel die HMAC- en PBKDF2-algoritmes 'n essensiële rol in die veiligheid van HD-beursie-afleiding in die Bitcoin-protokol. HMAC-SHA-512 word gebruik om teen lengte-uitbreidingsaanvalle te beskerm, terwyl PBKDF2 die omskakeling van die mnemoniese frase na 'n saad moontlik maak. Die kettingkode voeg 'n addisionele bron van entropie in sleutelafleiding in, wat die robuustheid van die stelsel verseker.

# Digitale Handtekeninge

## Digitale Handtekeninge en Elliptiese Kurwes

![Digitale Handtekeninge en Elliptiese Kurwes](https://youtu.be/gOjYiPkx4z8)

In die wêreld van kriptogelde is transaksieveiligheid van uiterste belang. In die kern van die Bitcoin-protokol word digitale handtekeninge gebruik as wiskundige bewyse wat die besit van 'n privaat sleutel wat verband hou met 'n spesifieke openbare sleutel demonstreer. Hierdie data-beskermingstegniek is essensieel gebaseer op 'n boeiende veld van kriptografie genaamd elliptiese kurwe-kriptografie (ECC).

![beeld](assets/image/section2/0.JPG)

Elliptiese kurwe-kriptografie is die ruggraat van Bitcoin-transaksieveiligheid. Hierdie elliptiese kurwes, wat herinner aan die wiskundige kurwes wat ons op skool bestudeer het, is nuttig in 'n verskeidenheid kriptografiese toepassings, wat wissel van sleuteluitruilings tot asimmetriese versleuteling tot die skep van digitale handtekeninge. 'n Interessante detail wat elliptiese kurwes onderskei, is hul simmetrie: enige nie-vertikale lyn wat twee punte op die kurwe sny, sal 'n derde punt sny.

Laten ons nou 'n bietjie dieper ingaan: die Bitcoin-protokol gebruik 'n spesifieke elliptiese kurwe genaamd SecP256K1 om sy kriptografiese bewerkings uit te voer. Hierdie kurwe, wat gedefinieer is op 'n eindige stel positiewe heelgetalle modulo 'n eerstegetal van 256 bits, kan voorgestel word as 'n wolk van punte eerder as 'n tradisionele kurwe. Dit is hierdie unieke ontwerp wat Bitcoin in staat stel om sy transaksies effektief te beveilig.

![beeld](assets/image/section2/1.JPG)

Wat die keuse van die secp256k1-kurwe vir Bitcoin betref, is dit interessant om op te merk dat dit verkies is bo die secp256r1-kurwe. Hierdie kurwe word gedefinieer deur die parameters a=0 en b=7, en sy vergelyking is y² = x³ + 7 modulo n, waar n die eerstegetal is wat die orde van die kurwe bepaal.

Wanneer ons praat oor die konstantes wat in die Bitcoin-stelsel gebruik word, verwys ons gewoonlik na die spesifieke parameters van die Elliptiese Kurwe Digitale Handtekening Algoritme (ECDSA) en die elliptiese kurwe-stelsel wat deur Bitcoin gebruik word, naamlik die secp256k1-kurwe. Hier is hierdie parameters:
- Primêre veld (p): Bitcoin gebruik 'n kromme oor 'n primêre veld, so p is die eerste getal wat gebruik word om hierdie veld te definieer. Vir die secp256k1-kromme is p gelyk aan `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` in heksadesimaal of p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 in desimaal.
- Krommeorde (n): Dit is die aantal punte op die kromme, insluitend die punt by oneindigheid. Vir secp256k1 is n gelyk aan `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` in heksadesimaal of n = 2^256 - 432420386565659656852420866394968145599 in desimaal.
- Generatorpunt (G): Die basispunt, of generator, is die punt op die kromme waaruit alle ander openbare sleutels gegenereer word. Dit het spesifieke x- en y-koördinate, gewoonlik voorgestel in heksadesimaal. Vir secp256k1 is die koördinate G, in heksadesimaal:
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

![image](assets/image/section2/2.JPG)

Let daarop dat alle heksadesimale waardes oor die algemeen in basis 16 voorgestel word, terwyl desimale waardes in basis 10 is. Verder word alle operasies op hierdie konstantes uitgevoer modulo p vir puntkoördinate op die kromme en modulo n vir sleutel- en handtekeningoperasies.

Dus, waar word hierdie beroemde bitcoins gestoor? Nie in 'n Bitcoin-balgeld nie, soos mens sou dink. In werklikheid stoor 'n Bitcoin-balgeld die privaat sleutels wat nodig is om eienaarskap van die bitcoins te bewys. Die bitcoins self word aangeteken op die blokketting, 'n gedesentraliseerde databasis wat alle transaksies argiveer.

In die Bitcoin-stelsel is die eenheid van rekening die bitcoin (let op die kleinletter "b"). Dit is verdeelbaar tot agt desimale plekke, met die kleinste eenheid wat die satoshi is. UTXO's, of "Ongebruikte Transaksie-uitsette," verteenwoordig die ongebruikte transaksie-uitsette wat aan 'n gebruiker behoort. Om hierdie bitcoins te spandeer, moet mens eienaarskap van die privaat sleutel demonstreer wat ooreenstem met die openbare sleutel wat aan elke UTXO gekoppel is.

Om transaksie-sekuriteit te verseker, steun Bitcoin op twee digitale handtekeningprotokolle: ECDSA (Elliptic Curve Digital Signature Algorithm) en Schnorr. ECDSA is 'n handtekeningprotokol wat sedert die bekendstelling van Bitcoin in 2009 geïntegreer is, terwyl Schnorr-handtekeninge onlangs in November 2021 bygevoeg is. Alhoewel beide protokolle gebaseer is op ellipsoïdekrommekriptografie en soortgelyke wiskundige meganismes gebruik, verskil hulle hoofsaaklik in terme van handtekeningstruktuur.

Voordat ons dieper in hierdie handtekeningmeganismes indink, is dit belangrik om te verstaan wat 'n ellipsoïdekromme is. 'n Ellipsoïdekromme word gedefinieer deur die vergelyking y² = x³ + ax + b. Elke punt op hierdie kromme het 'n kenmerkende simmetrie wat sleutel is tot sy bruikbaarheid in kriptografie.
Uiteindelik word verskeie elliptiese kurwes erken as veilig vir kriptografiese gebruik. Miskien is die bekendste die secp256r1-kurwe. Vir Bitcoin het Satoshi Nakamoto egter gekies vir 'n ander kurwe: secp256k1.

In die volgende gedeelte van hierdie kursus, sal ons 'n nader kyk neem na die openbare sleutel en privaat sleutel vir 'n deeglike begrip van kriptografie op elliptiese kurwes en die digitale handtekening algoritme. Dit sal die tyd wees om jou kennis te konsolideer en te verstaan hoe al hierdie inligting saamkom om die veiligheid van die Bitcoin-protokol te verseker.

## Die berekening van die openbare sleutel vanaf die privaat sleutel

![Die berekening van die openbare sleutel vanaf die privaat sleutel](https://youtu.be/NJENwFU889Y)

In die volgende gedeelte van hierdie kursus, sal ons die werking van openbare en privaat sleutels, twee kritieke elemente van die Bitcoin-protokol, ondersoek. Hierdie sleutels is intrinsiek gekoppel deur die Elliptiese Kurwe Digitale Handtekening Algoritme (ECDSA). Om hulle te verstaan, sal ons 'n diep insig kry in hoe Bitcoin transaksies op sy platform beveilig.

![beeld](assets/image/section2/3.JPG)
![beeld](assets/image/section2/4.JPG)

Om te begin, laat ons ons in die wêreld van die ECDSA-algoritme duik. Bitcoin maak gebruik van hierdie digitale handtekening algoritme om privaat en openbare sleutels te koppel. In hierdie stelsel is die privaat sleutel 'n lukrake of pseudo-lukrake 256-bit getal. Die totale aantal moontlikhede vir 'n privaat sleutel is teoreties 2^256, maar in werklikheid is dit effens minder as dit. Om presies te wees, is sommige 256-bit privaat sleutels nie geldig vir Bitcoin nie.

![beeld](assets/image/section2/5.JPG)

Om verenigbaar te wees met Bitcoin, moet 'n privaat sleutel tussen 1 en n-1 wees, waar n die orde van die elliptiese kurwe verteenwoordig. Dit beteken dat die totale aantal moontlikhede vir 'n Bitcoin privaat sleutel amper gelyk is aan 1.158 x 10^77. Om dit in perspektief te plaas, is dit ongeveer dieselfde aantal atome wat teenwoordig is in die waarneembare heelal. Die unieke privaat sleutel word dan gebruik om 'n 512-bit openbare sleutel af te lei.

![beeld](assets/image/section2/6.JPG)

Die openbare sleutel, aangedui as K, is 'n punt op die elliptiese kurwe wat afgelei word van die privaat sleutel deur puntoperasies op die kurwe. Dit is belangrik om daarop te let dat die ECDSA-funksie onomkeerbaar is, wat beteken dat dit onmoontlik is om die privaat sleutel van die openbare sleutel te herwin. Hierdie onomkeerbaarheid is die hoeksteen van Bitcoin-beursie-sekuriteit.

Die openbare sleutel bestaan uit twee 256-bit punte, wat 'n totaal van 512 bits is. Dit kan egter saamgedruk word tot 'n 264-bit getal. Die punt G is die beginpunt vir die berekening van al die openbare sleutels van gebruikers in die stelsel.

![beeld](assets/image/section2/7.JPG)

Een merkwaardige eienskap van elliptiese kurwes is dat 'n lyn wat die kurwe by twee punte sny, ook 'n derde punt, genaamd punt O, sal sny. Hierdie eienskap word gebruik om punt U te bepaal, wat die teenoorgestelde van punt O is. Die byvoeging van 'n punt by homself word gedoen deur 'n raaklyn aan die kurwe by daardie punt te trek, wat 'n nuwe unieke punt genaamd j tot gevolg het. Die skalaarvermenigvuldiging van 'n punt met n is gelykstaande aan die byvoeging van daardie punt by homself n keer.

![beeld](assets/image/section2/8.JPG)
Hierdie operasies op punte van 'n ellipiese kromme is die basis vir die berekening van openbare sleutels. Deur die privaatsleutel te ken, is dit maklik om die openbare sleutel te bereken. Omgekeerd, deur die openbare sleutel te ken, is dit nie moontlik om die privaatsleutel te bereken nie, wat die veiligheid van die Bitcoin-stelsel verseker. In werklikheid berus die veiligheid van openbare en privaatsleutels op die diskrete logaritme-probleem, 'n komplekse wiskundige vraagstuk.
![beeld](assets/image/section2/9.JPG)

In ons volgende les sal ons ondersoek hoe 'n digitale handtekening bereik word deur die gebruik van die ECDSA-algoritme met 'n privaatsleutel om bitcoins te ontsluit. Bly op die uitkyk vir hierdie opwindende verkenning van die wêreld van kriptogeld en kriptografie.

## Ondertekening met die privaatsleutel

![Ondertekening met die privaatsleutel](https://youtu.be/h2hIyGgPqkM)

Die proses van 'n digitale handtekening is 'n sleutelmetode om te bewys dat jy die houer van 'n privaatsleutel is sonder om dit bekend te maak. Dit word bereik deur die gebruik van die ECDSA-algoritme, wat die bepaling van 'n unieke nonce, die berekening van 'n spesifieke getal V, en die skep van 'n digitale handtekening wat uit twee dele, S1 en S2, bestaan. Dit is van kritieke belang om altyd 'n unieke nonce te gebruik om sekuriteitsaanvalle te voorkom. 'n Berugte voorbeeld van wat kan gebeur wanneer hierdie reël nie nagekom word nie, is die geval van die PlayStation 3-hack, wat gekompromitteer is as gevolg van nonce-hergebruik.

Spesifiek, om 'n digitale handtekening te valideer deur die gebruik van die ECDSA (Elliptic Curve Digital Signature Algorithm) algoritme, word tipies die volgende stappe gevolg:

1. Verifieer dat die handtekeningwaardes, S1 en S2, binne die reeks [1, n-1] val. Indien nie, is die handtekening ongeldig.
2. Bereken die inverse van S2 modulo n. Ons sal dit u noem. Dit word dikwels as volg bereken: u = (S2)^-1 modulo n.
3. Bereken H, wat die haswaarde van die ondertekende boodskap is.
4. Bereken u1 = H * u modulo n en u2 = S1 * u modulo n.
5. Bereken die punt P op die ellipiese kromme deur gebruik te maak van u1, u2, en die openbare sleutel K: P = u1*G + u2*K, waar G die kromme se generatorpunt is.
6. As P die punt by oneindigheid is, is die handtekening ongeldig.
7. Bereken I = x-koördinaat van P modulo n.
8. Die handtekening is geldig as I gelyk is aan S1.

![beeld](assets/image/section2/10.JPG)
![beeld](assets/image/section2/11.JPG)

Dit is belangrik om daarop te let dat elke sagteware moontlik verskillende notasies kan gebruik en sommige stappe gekombineer of herskik kan word, maar die basiese logika bly dieselfde. Let ook daarop dat alle rekenkundige bewerkings in die eindige veld uitgevoer word wat gedefinieer word deur die ellipiese kromme (modulo n, waar n die orde van die kromme is). As 'n herinnering, die secp256k1-kromme (wat in Bitcoin gebruik word) het n = 2^256 - 432420386565659656852420866394968145599.
Wanneer dit kom by die genereer van openbare en privaatsleutels, is dit noodsaaklik om vertroud te raak met die ellipiese kromme en die generatorpunt. Om 'n openbare sleutel te verkry, moet 'n lukrake getal as die privaatsleutel gekies word, dikwels 'n "nonce" genoem, en gebruik word in die vergelyking van die ellipiese kromme.
Die ellipiese kromme is 'n kragtige instrument vir die skep van veilige openbare en private sleutels. Byvoorbeeld, om die openbare sleutel 3G te verkry, trek jy 'n raaklyn aan punt G, bereken die teenoorgestelde van -G om 2G te verkry, en voeg dan G en 2G bymekaar. Om 'n transaksie uit te voer, moet jy bewys dat jy die nommer 3 ken deur die bitcoins wat verband hou met die openbare sleutel 3G te ontsluit.
Om 'n digitale handtekening te skep en te bewys dat jy die private sleutel ken wat verband hou met die openbare sleutel 3G, bereken jy eers 'n willekeurige getal, dan die punt V wat verband hou met hierdie willekeurige getal (in die gegewe voorbeeld is dit 4G). Dan bereken jy die punt T deur die openbare sleutel 3G en die punt V bymekaar te voeg, wat 7G gee.

![beeld](assets/image/section2/12.JPG)

Die verifikasie van 'n digitale handtekening is 'n kritieke stap in die gebruik van die ECDSA-algoritme, wat die egtheid van 'n ondertekende boodskap kan bevestig sonder om die sender se private sleutel nodig te hê. Hier is hoe dit in detail werk:

In ons voorbeeld het ons twee belangrike waardes: T en V. T is 'n numeriese waarde (7 in hierdie voorbeeld) en V is 'n punt op die ellipiese kromme (hier voorgestel deur 4G). Hierdie waardes word geproduseer tydens die skep van die digitale handtekening en word dan saam met die boodskap gestuur om verifikasie moontlik te maak.

Wanneer die verifieerder die boodskap ontvang, sal hulle ook hierdie twee waardes, T en V, ontvang.

Hier is die stappe wat die verifieerder sal volg om die handtekening te valideer:

1. Hulle sal eers die has van die boodskap bereken, wat ons H sal noem.
2. Dan sal hulle u1 en u2 bereken. Hiervoor sal hulle die volgende formules gebruik:
   - u1 = H * (S2)^-1 mod n
   - u2 = T * (S2)^-1 mod n'

# Die mnemoniese frase

## Evolusie van Bitcoin-bewaarplekke

![Evolusie van Bitcoin-bewaarplekke](https://youtu.be/6tmu1R9cXyk)

Die Hiërargiese Bepalende Bewaarplek, of meer algemeen bekend as die HD-bewaarplek, speel 'n prominente rol in die kriptogeldekosisteem. Die term "bewaarplek" mag misleidend wees vir diegene wat nuut is in die veld, aangesien dit nie die hou van geld of geldeenheid impliseer nie. Dit verwys eerder na 'n versameling private kriptografiese sleutels wat afgelei word van 'n enkele meestersleutel, danksy 'n vernuftige proses van algoritmiese wiskunde. Hierdie private sleutels, wat 'n vaste lengte van 256 bits het, is die essensie van kriptogeldeienaarskap en word soms verwys na as "Just a Bunch Of Keys" (JBOC).

![beeld](assets/image/section3/0.JPG)

Die kompleksiteit van die bestuur van hierdie sleutels word egter gelykgestel deur 'n stel protokolle, bekend as Bitcoin-verbeteringsvoorstelle (BIP's). Hierdie opgraderingsvoorstelle is die kern van die funksionaliteit en veiligheid van HD-bewaarplekke. Byvoorbeeld, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), bekendgestel in 2012, het die manier waarop hierdie sleutels gegenereer en gestoor word, gerevolusioneer deur die konsep van deterministies en hiërargies afgeleide sleutels in te voer. Dit vereenvoudig die proses om hierdie sleutels te bewaar, terwyl hul veiligheidsvlak behou word.

![beeld](assets/image/section3/1.JPG)
Daarna het [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) 'n baanbreker-innovasie bekendgestel: die 24-woord mnemoniese frase. Hierdie stelsel het dit moontlik gemaak om 'n komplekse, moeilik-om-te-onthou reeks syfers te omskep na 'n reeks gewone woorde, wat baie makliker is om te onthou en te stoor. Daarbenewens het [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) voorgestel om 'n addisionele wagwoord by te voeg om die veiligheid van individuele sleutels te versterk. Hierdie opeenvolgende verbeterings het gelei tot BIP43 en BIP44, wat die struktuur en hiërargie van HD-bewaarplekke gestandaardiseer het, wat dit meer toeganklik en makliker gemaak het vir die algemene publiek.

In die volgende afdelings sal ons 'n dieper insig kry in hoe HD-portefeuljes werk. Ons sal die beginsels van sleutelafleiding dek en die fundamentele konsepte van entropie en lukrake getalgenerering ondersoek, wat essensieel is vir die versekering van die veiligheid van jou HD-portefeulje.

Die Hiërargiese Bepalende Bewaarplek, of meer algemeen bekend as die HD-bewaarplek, speel 'n prominente rol in die kriptogeldekosisteem. Die term "bewaarplek" mag misleidend lyk vir diegene wat nuut is in die veld, aangesien dit nie die hou van geld of geldeenheid impliseer nie. Dit verwys eerder na 'n versameling private kriptografiese sleutels wat afgelei word van 'n enkele meestersleutel, danksy 'n vernuftige proses van algoritmiese wiskunde. Hierdie private sleutels, wat 'n vaste lengte van 256 bits het, is die essensie van kriptogeldeienaarskap en word soms verwys na die ietwat grof naam van "Just a Bunch Of Keys" (JBOC).

![beeld](assets/image/section3/0.JPG)

Die kompleksiteit van die bestuur van hierdie sleutels word egter opgeweeg deur 'n stel protokolle, bekend as Bitcoin-verbeteringsvoorstelle (BIP's). Hierdie opgraderingsvoorstelle is die kern van die funksionaliteit en veiligheid van HD-bewaarplekke. Byvoorbeeld, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), bekendgestel in 2012, het die manier waarop hierdie sleutels gegenereer en gestoor word, gerevolusioneer deur die konsep van deterministies en hiërargies afgeleide sleutels in te voer. Dit vereenvoudig die proses om hierdie sleutels te stoor, terwyl hul veiligheidsvlak behou word.![beeld](assets/image/section3/1.JPG)

Kortom, dit is noodsaaklik om die sentrale rol van BIP32 en BIP39 in die ontwerp en veiligheid van HD-bewaarplekke te beklemtoon. Hierdie protokolle maak die generering van veelvuldige sleutels vanuit 'n enkele saad moontlik, wat veronderstel word om 'n lukrake of pseudolukrake getal te wees. Vandag word hierdie standaarde deur die meerderheid kriptogeldebewaarplekke aanvaar, hetsy hulle toegewy is aan 'n enkele kriptogeldeenheid of ondersteuning bied vir verskillende tipes geldeenhede.

Ek hoop hierdie inleiding het jou gehelp om die grondslag van HD-bewaarplekke en hul verskeie eienskappe beter te verstaan. Ons doel is om jou te help om hierdie essensiële konsepte meester te word en meer doeltreffend te navigeer in die komplekse wêreld van kriptogelde. Bly dus by ons terwyl ons voortgaan om die ingewikkeldhede en fynhede van hierdie boeiende wêreld in die komende lesse te verken.

## Entropie en Lukrake Getal

![Entropie en Lukrake Getal](https://youtu.be/k18yH18w2TE)
Die belangrikheid van privaat sleutel sekuriteit in die Bitcoin ekosisteem is onbetwisbaar. Dit is inderdaad die hoeksteen wat die sekuriteit van Bitcoin transaksies verseker. Om enige kwesbaarheid wat verband hou met voorspelbaarheid te vermy, moet hierdie sleutels in 'n werklik willekeurige wyse gegenereer word, wat vinnig 'n arbeidsintensiewe oefening vir die gebruiker kan word. Een oplossing vir hierdie raaisel is die Hierargiese Bepalende Beursie, of HD beursie. Hierdie metode maak dit moontlik om die bepalende en hierargiese generasie van kind sleutelpare vanuit 'n enkele stuk inligting aan die basis van die beursie te doen. Dit is waar willekeurigheid noodsaaklik word om die sekuriteit van afgeleide sleutels te waarborg.
![beeld](assets/image/section3/2.JPG)

Die generasie van willekeurige getalle is inderdaad 'n kritieke element in kriptografie, om die integriteit van privaat sleutels te verseker. Om enige kwesbaarheid wat verband hou met voorspelbaarheid te voorkom, moet 'n privaat sleutel willekeurig geproduseer word. Die gebruik van 'n nuwe sleutelpaar vir elke transaksie verhoog verder die sekuriteit, alhoewel dit die rugsteun daarvan bemoeilik en slegs gedeeltelik vertroulikheid behou. Kortom, die sekuriteit van privaat sleutels is 'n absolute prioriteit wat streng en willekeurige generasie vereis. HD beursies bied 'n oplossing om die generasie en bestuur van sleutels te fasiliteer terwyl 'n hoë vlak van sekuriteit behou word.

Die generasie van willekeurige getalle op rekenaars stel egter 'n groot uitdaging, aangesien die verkrygde resultate nie werklik willekeurig is nie. Dit is waarom dit noodsaaklik is om 'n Willekeurige Getal Generator (RNG) te gebruik. Die tipes RNG wissel, van Pseudo-Willekeurige Getal Generators (PRNG) tot Werklike Willekeurige Getal Generators (TRNG), sowel as PRNG's wat 'n entropiebron inkorporeer.

![beeld](assets/image/section3/3.JPG)

In die geval van Bitcoin word privaat sleutels gegenereer vanuit 'n enkele stuk inligting aan die basis van die beursie. Hierdie inligting maak dit moontlik om die bepalende en hierargiese afleiding van kind sleutelpare te doen. Entropie is die grondslag van enige HD beursie, alhoewel daar geen standaard is vir die generasie van hierdie willekeurige getal nie. Daarom is die generasie van willekeurige getalle 'n groot bekommernis vir die beveiliging van Bitcoin transaksies.

Die verifikasiefase van sleutelgenerasie is krities om die sekuriteit en egtheid van willekeurige getal generasie te verseker, 'n fundamentele stap om enige kwesbaarheid wat verband hou met voorspelbaarheid te voorkom. Dit word sterk aanbeveel om oopbron beursies te gebruik om hierdie verifikasie moontlik te maak.

Dit is egter belangrik om daarop te let dat sommige hardeware beursies "geslote bron" kan wees, wat dit onmoontlik maak om die generasie van die willekeurige getal te verifieer. 'n Moontlike omweg sou wees om jou eie mnemoniese frase te genereer deur dobbelstene te gebruik, alhoewel hierdie benadering sekere risiko's kan inhou.

![beeld](assets/image/section3/4.JPG)

Die gebruik van 'n willekeurig gegenereerde wagwoord kan help om hierdie risiko's te verminder.

'n Voorbeeld van die toepassing van hierdie metode is die "dobbelsteenrol" opsie wat deur CoinKit aangebied word om mnemoniese frases te genereer. 'n Ander moontlikheid sou wees om 'n baie groot aanvanklike stuk inligting te gebruik en hierdie inligting tot 256 bits te verminder met behulp van die SHA-256 hasfunksie, wat in staat is om 'n goeie willekeurige getal te genereer. Dit is belangrik om te vermeld dat die SHA-256 hasfunksie weerstand bied teen botsings, vervalsing, en pre-beeld en tweede pre-beeld aanvalle.

Uiteindelik speel willekeurigheid 'n sentrale rol in kriptografie en rekenaarwetenskap, en die vermoë om willekeurigheid veilig te genereer is noodsaaklik om die sekuriteit van privaat sleutels en Bitcoin transaksies te verseker. Entropie, wat die kern van die Bitcoin HD beursie is, is essensieel vir sy sekuriteit. In ons volgende les sal ons voortgaan om hierdie onderwerp te verken en die rol van entropie in die sekuriteit van HD beursies te ondersoek.

## Die mnemoniese frase

![Die mnemoniese frase](https://youtu.be/uJERqH9Xp7I)

Die sekuriteit van 'n Bitcoin beursie is 'n groot bekommernis vir al sy gebruikers. 'n Essensiële manier om die rugsteun van die beursie te verseker, is om 'n mnemoniese frase te genereer gebaseer op entropie en 'n kontrolesom.
Entropie is die hoeksteen van HD-beursie-sekuriteit. Verskeie metodes bestaan om hierdie entropie te genereer, insluitend deur middel van pseudorandomgetalopwekkers (PRNG's), ware randomgetalopwekkers (TRNG's) of deur handmatig. Dit is noodsaaklik dat hierdie entropie willekeurig of pseudorandom is om die veiligheid van die beursie te waarborg.

Aan die ander kant verseker die kontrolesom die verifikasie van die akkuraatheid van die herstel frase. Sonder hierdie kontrolesom kan 'n fout in die frase lei tot die skepping van 'n ander beursie en dus die verlies van fondse. Die kontrolesom word verkry deur die entropie deur die SHA256-funksie te stuur en die eerste 8 bits van die has te herwin.

Verskillende standaarde bestaan vir die mnemoniese frase, afhangende van die grootte van die entropie. Die mees algemeen gebruikte standaard vir 'n 24-woord herstel frase is 'n entropie van 256 bits. Die grootte van die kontrolesom word bepaal deur die grootte van die entropie te deel deur 32.

Byvoorbeeld, 'n 256-bit entropie genereer 'n 8-bit kontrolesom. Die saamvoeging van die entropie en die kontrolesom lei dan tot onderskeidelik groottes van 128 bits, 160 bits, ens. Afhangende van die grootte van die entropie, sal die herstel frase bestaan uit 12 woorde vir 128 bits, 15 woorde vir 160 bits, en 24 woorde vir 256 bits.

Om die bits in frases te omskep, word elke segment geassosieer met 'n woord uit 'n lys van 2048 woorde. Dit is belangrik om daarop te let dat geen woord dieselfde volgorde van die eerste vier letters het nie.

Dit is noodsaaklik om die 24-woord herstel frase te rugsteun om die integriteit van die Bitcoin-beursie te behou. Die twee mees algemeen gebruikte standaarde is gebaseer op 'n entropie van 128 of 256 bits en 'n saamvoeging van 12 of 24 woorde. Die byvoeging van 'n wagwoord is 'n bykomende opsie om die veiligheid van die beursie te verbeter.

Ten slotte is die generering van 'n mnemoniese frase om 'n Bitcoin-beursie te beveilig 'n noodsaaklike proses. Dit is belangrik om by die standaarde van die mnemoniese frase te hou, afhangende van die grootte van die entropie. Die rugsteun van die 24-woord herstel frase is noodsaaklik om enige verlies van fondse te voorkom. Dankie vir u aandag en ons sien uit na ons volgende kriptogeldkursus.

## Die wagwoord

Die wagwoord is 'n bykomende wagwoord wat in 'n Bitcoin-beursie geïntegreer kan word om die veiligheid daarvan te verhoog. Die gebruik daarvan is opsioneel en is na die diskresie van die gebruiker. Deur arbitrêre inligting by te voeg wat, saam met die mnemoniese frase, die berekening van die beursie se saad moontlik maak, verhoog die wagwoord die veiligheid daarvan.

Om die sleutels van 'n HD-beursie af te lei, is sowel die mnemoniese frase as die wagwoord nodig. Die wagwoord is gratis en kan 'n bykans oneindige grootte bereik. Dit is nie ingesluit in die mnemoniese frase nie, wat gestandaardiseer is en sekere beperkings van grootte, kontrolesom en enkodering moet volg. 'n Aanvaller kan nie toegang tot 'n gebruiker se bitcoins verkry sonder om die wagwoord te ken nie. Die wagwoord speel 'n rol in die konstruksie en berekening van al die beursie se sleutels.

Die pbkdf2-funksie word gebruik om die saad van die wagwoord te genereer. Hierdie saad maak die afleiding van al die kindersleutelpare van die beursie moontlik. As die wagwoord verander word, word die Bitcoin-beursie heeltemal anders.
Die wagwoordfrase is 'n essensiële instrument om die veiligheid van Bitcoin-bewaarplekke te verbeter. Dit kan die toepassing van verskeie veiligheidsstrategieë moontlik maak. Byvoorbeeld, dit kan gebruik word om duplikate te skep en die rugsteun van die mnemoniese frase te vergemaklik. Dit kan ook die veiligheid van die bewaarplek verbeter deur die risiko's wat verband hou met die lukrake generering van die mnemoniese frase te verminder.
'n Effektiewe wagwoordfrase moet lank wees (20 tot 40 karakters) en uiteenlopend wees (deur gebruik te maak van hoofletters, kleinletters, syfers en simbole). Dit moet nie direk verband hou met die gebruiker of hul omgewing nie. Dit is veiliger om 'n lukrake reeks karakters te gebruik eerder as 'n eenvoudige woord as 'n wagwoordfrase.

'n Wagwoordfrase is veiliger as 'n eenvoudige wagwoord. Die ideale wagwoordfrase is lank, uiteenlopend en lukraak. Dit kan die veiligheid van 'n bewaarplek of warm sagteware verbeter. Dit kan ook gebruik word om oorbodige en veilige rugsteun te skep.

Dit is noodsaaklik om sorg te dra vir wagwoordfrase-rugsteun om te voorkom dat toegang tot die bewaarplek verloor gaan. 'n Wagwoordfrase is 'n opsie vir 'n HD-bewaarplek. Dit kan lukraak gegenereer word met dobbelstene of 'n ander pseudolukrake getalgenerator. Dit word nie aanbeveel om 'n wagwoordfrase of mnemoniese frase te onthou nie.

In ons volgende les sal ons in detail die werking van die saad en die eerste paar sleutels wat daaruit gegenereer word, ondersoek. Volg gerus hierdie kursus om jou leerproses voort te sit. Ons sien uit daarna om jou binnekort te sien.

# Skepping van Bitcoin Bewaarplekke

## Skepping van die saad en meestersleutel

![Skepping van die saad en meestersleutel](https://youtu.be/56yAt_JDWhY)

In hierdie deel van die kursus sal ons die stappe ondersoek om 'n Hierargiese Bepalende Bewaarplek (HD Bewaarplek) af te lei, wat die skepping en bestuur van private en openbare sleutels op 'n hiërargiese wyse moontlik maak.

![image](assets/image/section4/0.JPG)

Die grondslag van die HD Bewaarplek berus op twee essensiële elemente: die mnemoniese frase en die wagwoordfrase (opsionele bykomende wagwoord). Saam vorm hulle die saad, 'n 512-bit alfanumeriese reeks wat as die basis dien vir die afleiding van die bewaarplek se sleutels. Vanuit hierdie saad is dit moontlik om al die kindersleutelpare van die Bitcoin bewaarplek af te lei. Die saad is die sleutel wat toegang verleen tot al die bitcoins wat met die bewaarplek geassosieer word, of jy nou 'n wagwoordfrase gebruik of nie.

Om die saad te verkry, word die pbkdf2-funksie (Wagwoordgebaseerde Sleutelafleidingsfunksie 2) gebruik met die mnemoniese frase en die wagwoordfrase. Die uitset van pbkdf2 is 'n 512-bit saad. Die meestersleutel en die meesterkettingkode word bepaal deur die HMAC SHA-512 (Hash-gebaseerde Boodskapverifikasiekode Sekuriteitsalgoritme 512) algoritme. Hierdie algoritme vereis 'n boodskap en 'n sleutel om 'n resultaat te genereer. Die meestersleutel word bereken vanuit die saad en die frase "Bitcoin SEED". Hierdie frase is identies vir alle HD bewaarplek afleidings, wat verseker dat daar konsekwentheid is tussen bewaarplekke.

![image](assets/image/section4/1.JPG)

Aanvanklik was die SHA-512 funksie nie geïmplementeer in die Bitcoin-protokol nie, daarom word HMAC SHA-512 gebruik. Die gebruik van HMAC SHA-512 met die frase "Bitcoin SEED" beperk die gebruiker om 'n bewaarplek spesifiek vir Bitcoin te genereer. Die resultaat van HMAC SHA-512 is 'n 512-bit getal, verdeel in twee dele: die linkerkantse 256-bits verteenwoordig die meestersleutel, terwyl die regterkantse 256-bits die meesterkettingkode verteenwoordig.
Die meester privaat sleutel is die ouersleutel van alle toekomstige sleutels in die beursie, terwyl die meester kettingkode betrokke is by die afleiding van kindersleutels. Dit is belangrik om daarop te let dat dit onmoontlik is om 'n kindersleutelpaar af te lei sonder om die ooreenstemmende kettingkode van die ouersleutelpaar te ken. Die kettingkode voeg 'n bron van entropie by die afleidingsproses.

'n Sleutelpaar in die beursie bestaan uit 'n privaat sleutel, 'n openbare sleutel en 'n kettingkode. Die kettingkode maak dit moontlik om willekeurigheid in die afleiding van kindersleutels in te voer en isoleer elke sleutelpaar om enige informasie-uitlek te voorkom.

Dit is belangrik om te beklemtoon dat die meester privaat sleutel die eerste privaat sleutel is wat afgelei word uit die saad en geen verband het met die uitgebreide sleutels van die beursie nie. Daarom is die saad die fundamentele element vir die afleiding van al die sleutels van die beursie. Dit verskil van die mnemoniese frase en wagwoord, wat gebruik word vir saad-skepping.

In die volgende les sal ons in detail die uitgebreide sleutels soos xPub, xPRV, zPub verken en verstaan waarom hulle gebruik word en hoe hulle saamgestel word.

## Uitgebreide Sleutels

![Uitgebreide Sleutels](https://youtu.be/TRz760E_zUY)

In hierdie deel van die les sal ons die uitgebreide sleutels (xPub, zPub, yPub) en hul voorvoegsels bestudeer wat 'n belangrike rol speel in die afleiding van kindersleutels in 'n HD (Hierargiese Bepalende Beursie) beursie.

Uitgebreide sleutels onderskei hulself van meestersleutels. 'n HD-beursie genereer 'n mnemoniese frase en 'n saad om die meestersleutel en meester kettingkode te verkry. Uitgebreide sleutels word gebruik om kindersleutels af te lei en vereis beide die ouersleutel en die ooreenstemmende kettingkode. 'n Uitgebreide sleutel kombineer hierdie twee stukke inligting om die afleidingsproses te vereenvoudig.

Uitgebreide sleutels word geïdentifiseer deur spesifieke voorvoegsels (XPRV, XPUB, YPUB, ZPUB) wat aandui of dit 'n uitgebreide privaat of openbare sleutel is, sowel as sy spesifieke doel. Die metadata wat met 'n uitgebreide sleutel geassosieer word, sluit die weergawe (voorvoegsel), diepte, openbare sleutel vingerafdruk, indeks en nutslading (kettingkode en ouersleutel) in.

Die nutslading bestaan uit die kettingkode (32 byte) en die ouersleutel (33 byte). Hierdie elemente is noodsaaklik vir die afleiding van kindersleutels. 'n Privaat sleutel word gegenereer uit 'n willekeurige of pseudowillekeurige getal, terwyl 'n openbare sleutel gegenereer word met behulp van die ECDSA (Elliptiese Kromme Digitale Handtekening Algoritme) algoritme.

Elke paar uitgebreide sleutels is geassosieer met 'n unieke kettingkode, wat spesifieke afleidings moontlik maak. Deur die ouersleutel met die kettingkode te kombineer, word 'n uitgebreide privaat of openbare sleutel verkry.

Uitgebreide openbare sleutels kan slegs afgelei word uit normale kinder openbare sleutels, terwyl uitgebreide privaat sleutels afgelei kan word uit beide openbare en private kindersleutels, hetsy deur normale of geharde afleiding. Deur uitgebreide sleutels met die XPUB voorvoegsel te gebruik, kan nuwe adresse afgelei word sonder om terug te gaan na die ooreenstemmende private sleutels, wat beter sekuriteit bied. Die metadata wat met uitgebreide sleutels geassosieer word, verskaf belangrike inligting oor hul rol en posisie in die sleutelhiërargie.

Gekomprimeerde openbare sleutels het 'n grootte van 33 byte, terwyl ongekomprimeerde openbare sleutels 512 bits is. Gekomprimeerde openbare sleutels behou dieselfde inligting as ongekomprimeerde sleutels, maar met 'n kleiner grootte. Uitgebreide sleutels het 'n grootte van 82 byte en hul voorvoegsel word voorgestel in basis 58 deur middel van heksadesimale omskakeling. Die kontrolesom word bereken met behulp van die HASH256 hashfunksie.
Geharde afleidings begin by indekse wat magte van 2 is (2^31). Uitgebreide openbare sleutels maak slegs afleiding van normale kind openbare sleutels moontlik, terwyl uitgebreide private sleutels afleiding van enige kind sleutel moontlik maak. Dit is die moeite werd om daarop te let dat die mees algemeen gebruikte voorvoegsels xpub en zpub is, wat onderskeidelik ooreenstem met die erfenis en segwit v1 en segwit v0 standaarde.

In ons volgende les sal ons die afleiding van kind sleutelpare verken deur gebruik te maak van die kennis wat ons opgedoen het oor uitgebreide sleutels en die beursie se meestersleutel.

Ten slotte speel uitgebreide sleutels 'n essensiële rol in die kriptografie en die werking van HD-beursies. Om hul gebruik en berekening te verstaan, is noodsaaklik om transaksie-sekuriteit en die beskerming van digitale bates te verseker. Die voorvoegsels en metadata wat met uitgebreide sleutels geassosieer word, maak doeltreffende gebruik en akkurate afleiding van nodige kind sleutels moontlik.

## Afleiding van Kind Sleutelpare

![Afleiding van Kind Sleutelpare](https://youtu.be/FXhI-GmE9Aw)

Hierna sal ons die berekening van die saad en die meestersleutel bespreek, wat die eerste essensiële elemente is vir die hiërargiese organisasie en afleiding van die HD-beursie (Hiërargiese Bepalende Beursie). Die saad, met 'n lengte van 128 tot 256 bits, word lukraak gegenereer of van 'n geheime frase afgelei. Dit speel 'n bepalende rol in die afleiding van alle ander sleutels. Die meestersleutel is die eerste sleutel wat van die saad afgelei word, en dit maak die afleiding van alle ander kind sleutelpare moontlik.

Die meesterskettingkode speel 'n belangrike rol in die herstel van die portefeulje vanuit die saad. Dit moet opgemerk word dat alle sleutels wat van dieselfde saad afgelei word, dieselfde meesterskettingkode sal hê.

![image](assets/image/section4/7.JPG)

Die hiërargiese en bepalende beursie (HD-beursie) bied meer doeltreffende bestuur van sleutels en beursiestrukture. Uitgebreide sleutels maak die afleiding van 'n kind sleutelpaar moontlik van 'n ouersleutelpaar deur gebruik te maak van wiskundige berekeninge en spesifieke algoritmes.

Daar is verskillende tipes kind sleutelpare, insluitend geharde sleutels en normale sleutels. Die uitgebreide openbare sleutel maak slegs die afleiding van normale kind openbare sleutels moontlik, terwyl die uitgebreide private sleutel die afleiding van alle kind sleutels, beide openbaar en privaat, in normale of geharde modus moontlik maak. Elke sleutelpaar het 'n indeks wat hulle van mekaar onderskei.

![image](assets/image/section4/8.JPG)

Die afleiding van kind sleutels maak gebruik van die HMAC-SHA512 funksie deur die ouersleutel saam te voeg met die indeks en die kettingkode wat met die sleutelpaar geassosieer word. Normale kind sleutels het 'n indeks wat wissel van 0 tot 2 tot die mag van 31 minus 1, terwyl geharde kind sleutels 'n indeks het wat wissel van 2 tot die mag van 31 tot 2 tot die mag van 32 minus 1.

![image](assets/image/section4/9.JPG)
![image](assets/image/section4/10.JPG)

Daar is twee tipes kind sleutelpare: geharde pare en normale pare. Die proses van die afleiding van kind sleutels maak gebruik van die openbare sleutels om spandeer voorwaardes te genereer, terwyl die private sleutels gebruik word vir ondertekening. Die uitgebreide openbare sleutel maak slegs die afleiding van normale kind openbare sleutels moontlik, terwyl die uitgebreide private sleutel die afleiding van alle kind sleutels, beide openbaar en privaat, in normale of geharde modus moontlik maak.

![image](assets/image/section4/11.JPG)
![image](assets/image/section4/12.JPG)

Geharde afleiding maak gebruik van die ouer private sleutel, terwyl normale afleiding die ouer openbare sleutel gebruik. Die HMAC-SHA512 funksie word gebruik vir geharde afleiding, terwyl normale afleiding 'n 512-bit hashtoewysing gebruik. Die kind openbare sleutel word verkry deur die kind private sleutel met die generator van die elliptiese kromme te vermenigvuldig.

![image](assets/image/section4/13.JPG)
## Beursie Struktuur en Afleidingspaaie

![Beursie Struktuur en Afleidingspaaie](https://youtu.be/etO9UxwyE2I)

In hierdie hoofstuk sal ons die struktuur van die afleidingsboom in 'n Hierargiese Bepalende Beursie (HD Beursie) bestudeer. Ons het reeds die berekening van die saad, die meester sleutel, en die afleiding van kind sleutelpare ondersoek. Nou sal ons fokus op die organisasie van sleutels binne die beursie.

Die HD Beursie gebruik diepte lae om die sleutels te organiseer. Elke afleiding van 'n ouerpaar na 'n kindpaar stem ooreen met 'n dieptelaag. Diepte 0 stem ooreen met die meester sleutel en die meester kettingkode.

![image](assets/image/section4/15.JPG)

- Diepte 1 word gebruik om kind sleutels af te lei vir 'n spesifieke doel, wat bepaal word deur die indeks. Die doeleindes is in ooreenstemming met BIP 84 en Segwit v0/v1 standaarde.

- Diepte 2 maak differensiasie van rekeninge vir verskillende kriptogeldeenhede of netwerke moontlik. Dit maak dit moontlik om die beursie te organiseer op grond van verskillende bronne van fondse.

- Diepte 3 word gebruik om die beursie in verskillende rekeninge te organiseer, wat 'n duideliker en meer georganiseerde struktuur bied.

- Diepte 4 stem ooreen met die eksterne en interne kettings, wat gebruik word vir adresse wat bedoel is om openlik gekommunikeer te word. Indeks 0 word geassosieer met die eksterne ketting, terwyl indeks 1 geassosieer word met die interne ketting. Elke rekening het twee kettings: die eksterne ketting (0) en die interne ketting (1). Diepte 4 word ook gebruik om skripsotipes te bestuur in die geval van multi-handtekening beursies.

- Diepte 5 word gebruik vir ontvangsadresse in 'n standaard beursie. In die volgende afdeling sal ons die afleiding van kind sleutelpare in meer detail ondersoek.

![image](assets/image/section4/16.JPG)

Vir elke dieptelaag gebruik ons indekse om die kind sleutelpare te differensieer. Geharde indekse word gebruik met 'n apostroof vir sekere afleidings. Die openbare sleutel per jaar word as inset vir die HMAC-funksie gebruik. Die indeks in 'n afleidingspad dui die waarde aan wat in die HMAC-funksie gebruik word.
Die indeks sonder 'n apostroof stem ooreen met die werklike indeks wat gebruik word, terwyl die indeks met 'n apostroof ooreenstem met die werklike indeks + 2^31. Versterkte afleidings gebruik indekse vanaf 2^31 tot 2^32-1. Byvoorbeeld, indeks 44' stem ooreen met die werklike indeks 2^31 + 44.
Om 'n spesifieke ontvangsadresse te genereer, leid ons 'n paar kind sleutels af van die meester sleutel en die meester kettingkode. Dan gebruik ons die indeks om te differensieer tussen verskillende pare kind sleutels op dieselfde diepte.

Uitgebreide sleutels, soos XPUB, maak dit moontlik om jou beursie met verskeie mense te deel. Die afleidingspad word gebruik om te differensieer tussen die eksterne ketting (adresse bedoel om gekommunikeer te word) en die interne ketting (veranderingsadresse).

Dit is belangrik om daarop te let dat verskillende dieptes gebruik word in 'n HD beursie, afhangende van verskillende standaarde. Die afleiding van ouersleutels na kind sleutels maak oorgang van die een diepte na die ander moontlik. Die gebruik van verskillende takke in die HD beursie dui op die verskillende standaarde wat gevolg word.

In die volgende hoofstuk sal ons ontvangsadresse bestudeer, hul voordele van gebruik, en die stappe wat betrokke is by hul konstruksie. 

# Wat is 'n Bitcoin-adres?

## Bitcoin-adresse

![Bitcoin-adresse](https://youtu.be/nqGBMjPtFNI)
In hierdie hoofstuk sal ons ontvangsadresse verken, wat 'n kritieke rol speel in die Bitcoin-stelsel. Dit maak dit moontlik om fondse op 'n munt te ontvang en word gegenereer uit pare van private en openbare sleutels. Alhoewel daar 'n tipe skrip genaamd Pay2PublicKey is wat dit moontlik maak om bitcoins aan 'n openbare sleutel te vergrendel, verkies gebruikers gewoonlik om ontvangsadresse te gebruik in plaas van hierdie skrip.
![beeld](assets/image/section5/0.JPG)

Wanneer 'n ontvanger bitcoins wil ontvang, verskaf hulle 'n ontvangsadresse aan die sender in plaas van hul openbare sleutel. 'n Adres is eintlik 'n has van 'n openbare sleutel, met 'n spesifieke formaat. Die openbare sleutel word afgelei van die kind private sleutel deur gebruik te maak van wiskundige bewerkings soos puntbyvoeging en verdubbeling op elliptiese krommes.

![beeld](assets/image/section5/1.JPG)

Dit is belangrik om daarop te let dat dit nie moontlik is om van 'n adres na die openbare sleutel terug te keer nie, of van die openbare sleutel na die private sleutel nie. Die gebruik van 'n adres help om die grootte van die openbare sleutelinligting te verminder, wat aanvanklik 512 bits is. Dit is moontlik om 'n openbare sleutel te komprimeer deur slegs die x-waarde te behou en 'n voorvoegsel by te voeg, maar hierdie tegniek was nie bekend ten tyde van die skepping van Bitcoin nie. Daarom spaar die gebruik van 'n adres nie spasie in die blokke.

## Hoe om 'n Bitcoin-adres te skep?

![Hoe om 'n Bitcoin-adres te skep?](https://youtu.be/ewMGTN8dKjI)

In hierdie hoofstuk sal ons die konstruksie van 'n ontvangsadresse vir Bitcoin-transaksies bespreek. 'n Ontvangsadresse is 'n alfanumeriese voorstelling van 'n gekomprimeerde openbare sleutel. Die omskakeling van 'n openbare sleutel na 'n ontvangsadresse gaan deur verskeie stappe.

![beeld](assets/image/section5/3.JPG)

Een voordele van ontvangsadresse is die teenwoordigheid van 'n kontrolesom, wat foute opspoor. Hiervoor gebruik ons BCH (Bose-Chaudhuri-Hocquenghem) kontrolesomtegnologie, wat akkurate foutopsporing verseker. Hierdie tegnologie dra ook by tot die vermindering van die aantal karakters wat nodig is om 'n adres voor te stel, wat dit makliker maak om te gebruik.

Om 'n adres te begin bou, moet ons die ooreenstemmende openbare sleutel komprimeer. 'n Rou openbare sleutel beslaan 520 bits, maar danksy die simmetrie van die gebruikte elliptiese kromme, kan 'n elliptiese kromme 'n x-koördinaat hê wat geassosieer word met twee moontlike waardes vir y: positief of negatief. Op die Bitcoin-netwerk werk ons met 'n eindige stel positiewe heelgetalle eerder as die stel reële getalle. Om 'n openbare sleutel vanaf x voor te stel, voeg ons 'n voorvoegsel by wat die waarde van y (eweredig of onewe) aandui. Die kompressie van 'n openbare sleutel verminder sy grootte van 520 tot 264 bits. Die eweredigheid van y in 'n eindige stel positiewe heelgetalle stem ooreen met die eweredigheid van y in die stel reële getalle.

![beeld](assets/image/section5/4.JPG)
![beeld](assets/image/section5/5.JPG)

Laten ons die voorbeeld van die openbare sleutel wat aan Satoshi Nakamoto behoort, met 'n voorvoegsel 0,3 wat 'n onewe waarde van y aandui, neem. Ons kan dan na die tweede stap van die konstruksie van 'n adres vanaf gekomprimeerde openbare sleutels oorgaan. Dit is moontlik om twee adresse vir elke openbare sleutel te bereken. Hiervoor gebruik ons die SHA256-funksie om die has van die openbare sleutel te verkry. Dan pas ons die ripemd160-funksie toe op die resultaat van SHA256 om 'n string van karakters te verkry. Hierdie string word dan in binêre formaat in groepe van 5 bits gekodeer, waaraan metadata vir kontrolesomberekening met behulp van die BCH-program bygevoeg word.

![beeld](assets/image/section5/6.JPG)
In die geval van erfenisadressering gebruik ons dubbele SHA256 hashing om die adreskontrolesom te genereer. Vir Segwit V0 en V1 adresse steun ons egter op BCH-kontrolesomtegnologie om foutopsporing te verseker. Die BCH-program is in staat om foute voor te stel en te regstel met 'n uiters lae foutwaarskynlikheid. Tans word die BCH-program gebruik om wysigings voor te stel, maar dit maak nie outomaties die wysigings namens die gebruiker nie. Die berekening van die kontrolesom met die BCH-kode is gebaseer op polinomiale Chien-Chauffage-aritmetika.
![beeld](assets/image/section5/7.JPG)

Die BCH-program vereis verskeie insetinligting, insluitend die HRP (Human Readable Part) wat uitgebrei moet word. Die uitbreiding van die HRP behels die enkodering van elke letter in basis 2, deur die eerste drie bits van elke karakter in te voeg deur 'n skeier 0 in te voeg, en dan die laaste vyf bits van elke karakter aan mekaar te heg. Die blou karakters wat na basis 10 omgeskakel is, stem ooreen met 3 en 3 in desimaal, terwyl die ander vyf oranje karakters ooreenstem met 2 en 3 in basis 10. Die uitbreiding van die HRP in basis 10 maak dit moontlik om die laaste vyf bits van elke karakter te isoleer, en sodoende die kontrolesom te versterk.

![beeld](assets/image/section5/8.JPG)

Die Segwit V0-weergawe word voorgestel deur die kode 00 en die "payload" is in swart, in basis 10. Dit word gevolg deur ses karakters wat vir die kontrolesom gereserveer is. Die inset wat die metadata bevat, word dan aan die BCH-program voorgelê om die kontrolesom in basis 10 te verkry. Die aanhegting van die weergawe, payload en kontrolesom maak dit moontlik om die adres te bou. Die basis 10 karakters word dan omgeskakel na bech32 karakters deur gebruik te maak van 'n karteringstabel. Die bech32 alfabet sluit alle alfanumeriese karakters in, behalwe 1, b, i en o, om verwarring te voorkom.

![beeld](assets/image/section5/9.JPG)
![beeld](assets/image/section5/10.JPG)

Om 'n adres te bou wat met bc1q begin, moet ons 'n hasfunksie (H160) toepas op 'n saamgedrukte openbare sleutel, dan die kontrolesom, die weergawe (q), die HRP (bc) en die skeier (1) byvoeg. Taproot adresse daarenteen begin met bc1p omdat hul weergawe (Segwit V1) ooreenstem met 0+1=1, vandaar die gebruik van die karakter p. Al hierdie elemente word dan omgeskakel na BCH32, 'n Bitcoin-spesifieke variant van basis 32.

Dus het ons deur die stappe gegaan om 'n ontvangsadresse te konstrueer, die gebruik van BCH-kontrolesomtegnologie, sowel as die konstruksie van 'n adres wat met bc1q of bc1p begin deur gebruik te maak van die BCH32-variant van Bitcoin-spesifieke basis 32.

## Opsomming van Kriptografie vir Bitcoin Beursies

![opleidingsopsomming](https://youtu.be/NkAYoVUMvOs)

Gedurende hierdie opleiding het ons die Hierargiese Bepalende (HD) beursie met BIP32 in diepte bestudeer. Entropie speel 'n sentrale rol in hierdie tipe beursie, aangesien dit gebruik word om 'n mnemoniese frase van 'n lukrake getal te genereer. Met die lys van 2048 woorde wat in BIP39 verskaf word, kan hierdie mnemoniese frase in 'n reeks maklik onthou woorde gekodeer word. Die mnemoniese frase, tesame met 'n opsionele wagwoord, is nodig om die beursie se saad te genereer. Die wagwoord tree op as 'n kriptografiese sout wat 'n ekstra laag van beskerming aan die beursie toevoeg.

![beeld](assets/image/section5/11.JPG)
Die pbkdf2-funksie word gebruik om die saad te genereer uit die mnemoniese frase en wagwoord, deur gebruik te maak van hmacha512 en 2048 iterasies. Die meester sleutel en meester kettingkode word dan afgelei uit hierdie saad deur weer die hmacha512-funksie te gebruik met die frase "bitcoin seed". Die meester privaat sleutel en meester kettingkode is die hoogste elemente in die HD-beursie-hierargie.
![beeld](assets/image/section5/12.JPG)

Die afleiding van 'n kindersleutel hang af van verskeie faktore, insluitend die ouersleutel en die ooreenstemmende kettingkode. 'n Uitgebreide sleutel word verkry deur 'n ouersleutel met sy kettingkode te kombineer, terwyl 'n meestersleutel 'n afsonderlike sleutel is. Om 'n adres af te lei, word die saamgedrukte openbare sleutel eerste gehash met behulp van SHA256 en RIPMD160, en dan word 'n kontrolesom bereken. Dubbele SHA256 hashing word gebruik om die kontrolesom te bereken in die geval van 'n erfenisstandaard, terwyl die BCH (Bose-Chaudhuri-Hocquenghem) program gebruik word om die kontrolesom te bereken in die geval van 'n segwit-standaard. Dan word 'n basis 58-formaatvoorstelling gebruik vir 'n erfenisstandaard, terwyl die bech32-formaat gebruik word vir 'n segwit-standaard, om die HD-beursie-adres te verkry.

![beeld](assets/image/section5/13.JPG)

Opsommend het ons in detail die hasfunksies en hul eienskappe ondersoek, sowel as digitale handtekeninge en ellipsoïde kurwes. Ons het toe ingedring in die wêreld van Hierargiese Bepalende (HD) beursies met BIP32, deur entropie en wagwoord te gebruik om die beursie-saad te genereer. Ons het ook geleer hoe om kindersleutels af te lei en die HD-beursie-adres te verkry. Ek hoop hierdie inligting was vir jou nuttig, en ek moedig jou nou aan om voort te gaan na die assessering om jou kennis wat jy tydens die Crypto 301-kursus opgedoen het, te toets. Baie dankie vir jou aandag.

# Gaan verder

## Die skep van 'n saad deur middel van 128 dobbelsteenrolle!

![Die skep van 'n saad deur middel van 128 dobbelsteenrolle!](https://youtu.be/lUw-1kk75Ok)

Die skep van 'n mnemoniese frase is 'n belangrike stap in die beveiliging van jou kriptogeldportefeulje. Daar is verskeie metodes om 'n mnemoniese frase te genereer, maar ons sal fokus op die handmatige generasie-metode met behulp van dobbelstene. Dit is belangrik om daarop te let dat hierdie metode nie geskik is vir 'n hoëwaarde-beursie nie. Dit word aanbeveel om oopbron sagteware of 'n hardeware-beursie te gebruik om die mnemoniese frase te genereer. Om 'n mnemoniese frase te skep, sal ons dobbelstene gebruik om binêre inligting te genereer. Die doel is om die proses van die skep van die mnemoniese frase te verstaan.

**Stap 1 - Voorbereiding:**
Maak seker dat jy 'n amnesiese Linux-verspreiding, soos Tails OS, op 'n USB-aandrywing geïnstalleer het vir bygevoegde veiligheid. Let daarop dat hierdie handleiding nie gebruik moet word om 'n primêre beursie te skep nie.

**Stap 2 - Die skep van 'n willekeurige binêre nommer:**
Ons sal dobbelstene gebruik om binêre inligting te genereer. Rol 'n dobbelsteen 128 keer en neem elke resultaat op (1 vir oneweredig, 0 vir eweredig).

**Stap 3 - Die organiseer van die binêre getalle:**
Organiseer die verkrygde binêre getalle in rye van 11 syfers om verdere berekeninge te vergemaklik. Die twaalfde ry moet slegs 7 syfers hê.

**Stap 4 - Die berekening van die kontrolesom:**
Die laaste 4 syfers vir die twaalfde ry stem ooreen met die kontrolesom. Om hierdie kontrolesom te bereken, moet ons 'n terminaal van 'n Linux-distribusie gebruik. Dit word aanbeveel om [TailOs](https://tails.boum.org/index.fr.html) te gebruik, wat 'n geheuevrye distribusie is wat van 'n USB-aandrywer kan opstart. Sodra jy op jou terminaal is, tik die opdrag `echo <binêre nommer> | shasum -a 254 -0` in. Vervang `<binêre nommer>` met jou lys van 128 nullen en enes. Die uitset is 'n heksadesimale has. Maak aantekening van die eerste karakter van hierdie has en omskep dit na binêre vorm. Jy kan hierdie [tabel](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) gebruik vir hulp. Voeg die binêre kontrolesom (4 syfers) by die twaalfde ry van jou blad.

**Stap 5 - Omskakeling na desimaal:**
Om die woorde wat met elkeen van jou lyne geassosieer word, te vind, moet jy elke reeks van 11 bits na desimaal omskakel. Hier kan jy nie 'n aanlyn-omskakelaar gebruik nie, omdat hierdie bits jou mnemoniese frase verteenwoordig. Jy sal dus moet omskakel met behulp van 'n sakrekenaar en 'n truuk soos volg: elke bit is geassosieer met 'n mag van 2, so van links na regs het ons 11 grade wat ooreenstem met 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Om jou reeks van 11 bits na desimaal om te skakel, hoef jy net die grade wat 'n 1 bevat, bymekaar te tel. Byvoorbeeld, vir die reeks 00110111011, stem dit ooreen met die volgende optelling: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Jy kan nou elke lyn na desimaal omskakel. En voordat jy na die kodering na woorde oorgaan, moet jy +1 by al die lyne voeg omdat die indeks van die BIP39-woordelys vanaf 1 begin en nie 0 nie.

**Stap 8 - Opgestel van die mnemoniese frase:**
Begin deur die [lys van 2048 woorde](https://seedxor.com/files/wordlist.pdf) af te druk om tussen jou desimale getalle en die BIP39-woorde te omskakel. Die besonderheid van hierdie lys is dat geen woord dieselfde eerste 4 letters gemeen het met al die ander woorde in hierdie woordeboek nie. Soek dan vir elkeen van jou lyne die woord wat met die desimale nommer geassosieer word.

**Stap 9 - Toetsing van die mnemoniese frase:**
Toets onmiddellik jou mnemoniese frase op Sparrow Wallet deur 'n beursie daaruit te skep. As jy 'n ongeldige kontrolesomfout kry, is dit waarskynlik dat jy 'n berekeningsfout gemaak het. Regstel hierdie fout deur terug te gaan na stap 4 en toets weer op Sparrow Wallet. Daar gaan jy! Jy het so pas 'n nuwe Bitcoin-beursie geskep deur 128 dobbelsteenrolle.

Die opstel van 'n mnemoniese frase is 'n belangrike proses vir die beveiliging van jou kriptogeldbeursie. Dit word aanbeveel om meer veilige metodes te gebruik, soos die gebruik van oopbron sagteware of hardeware-beursies, om die mnemoniese frase te genereer. Deur hierdie werkswinkel te voltooi, help dit om beter te verstaan hoe ons 'n Bitcoin-beursie kan skep uit 'n lukrake nommer.

## Gevolgtrekking en einde

### Erkenning en blyf die konynegat grawe

Ons wil jou opreg bedank vir die bywoning van die Crypto 301-opleiding. Ons hoop dat hierdie ervaring verrykend en opvoedkundig vir jou was. Ons het baie opwindende onderwerpe gedek, van wiskunde tot kriptografie tot die werking van die Bitcoin-protokol.
As jy verder in die onderwerp wil indring, het ons 'n addisionele bron om met jou te deel. Ons het 'n eksklusiewe onderhoud gevoer met Théo Pantamis en Loïc Morel, twee bekende deskundiges op die gebied van kriptografie. Hierdie onderhoud gaan diep in op verskeie aspekte van die onderwerp en bied interessante perspektiewe.

Voel vry om hierdie onderhoud te kyk om voort te gaan met die verkenning van die boeiende veld van kriptografie. Ons hoop dat dit nuttig en inspirerend sal wees in jou reis. Nogmaals baie dankie vir jou deelname en toewyding gedurende hierdie opleiding.

### Ondersteun Ons

Hierdie kursus, tesame met al die inhoud wat beskikbaar is op hierdie universiteit, is gratis aan jou verskaf deur ons gemeenskap. Om ons te ondersteun, kan jy dit deel met ander, 'n lid van die universiteit word, en selfs bydra tot die ontwikkeling daarvan via GitHub. Namens die hele span, baie dankie!

### Beoordeel die Opleiding

'n Beoordelingstelsel vir die opleiding sal binnekort geïntegreer word in hierdie nuwe E-leerplatform! Intussen baie dankie vir die voltooiing van die kursus, en as jy dit geniet het, oorweeg asseblief om dit met ander te deel.