---
name: GitHub Desktop
description: Kuidas seadistada oma kohalikku töökeskkonda?
---
![github](assets/cover.webp)

PlanB missiooniks on pakkuda tipptasemel haridusressursse Bitcoin'i kohta võimalikult paljudes keeltes. Kõik saidil avaldatud sisu on avatud lähtekoodiga ja majutatud GitHub'is, mis võimaldab kõigil platvormi rikastamises osaleda. Panused võivad võtta erinevaid vorme: olemasolevate tekstide parandamine ja toimetamine, tõlkimine teistesse keeltesse, teabe uuendamine või meie saidil veel mitteolevate uute õpetuste loomine.

Kui soovite panustada PlanB võrgustikku, peate muudatuste tegemiseks kasutama GitHub'i. Selleks on teil kaks võimalust:
- **Otse GitHub'i veebiliidese kaudu kaasa aidata**: See on lihtsaim meetod. Kui olete algaja või kavatsete teha vaid mõned väikesed panused, on see valik tõenäoliselt teie jaoks parim;
- **Kaasa aidata kohalikult, kasutades Giti**: See meetod sobib paremini, kui plaanite teha regulaarseid või olulisi panuseid PlanB võrgustikku. Kuigi oma kohaliku Giti keskkonna seadistamine arvutis võib alguses tunduda keeruline, on see lähenemine pikemas perspektiivis tõhusam. See võimaldab muudatuste paindlikumat haldamist. Kui olete selles uus, ärge muretsege, **selgitame kogu protsessi, kuidas oma keskkonda seadistada selles õpetuses** (lubame, et ei pea tippima ühtegi käsurida ^^).

Kui teil pole aimugi, mis on GitHub, või soovite rohkem teada saada Git'i ja GitHub'iga seotud tehnilistest terminitest, soovitan teil lugeda meie sissejuhatavat artiklit, et tutvuda nende kontseptsioonidega.

https://planb.network/tutorials/others/basics-of-github



- Alustuseks vajate ilmselgelt GitHub'i kontot. Kui teil juba on konto, saate sisse logida, vastasel juhul saate meie õpetuse abil luua uue konto.

https://planb.network/tutorials/others/create-github-account



## 1. samm: Installige GitHub Desktop

- Minge aadressile https://desktop.github.com/, et alla laadida GitHub Desktop tarkvara. See tarkvara võimaldab teil GitHub'iga hõlpsalt suhelda, ilma et peaksite kasutama terminali:
![github-desktop](assets/1.webp)
- Kui käivitate tarkvara esimest korda, palutakse teil ühendada oma GitHub'i konto. Selleks klõpsake nupul `Logi sisse GitHub.com`:
![github-desktop](assets/2.webp)
- Teie brauseris avaneb autentimisleht. Sisestage oma e-posti aadress ja konto loomisel valitud parool, seejärel klõpsake nupul `Logi sisse`:
![github-desktop](assets/3.webp)
- Klõpsake nupul `Autoriseeri desktop`, et kinnitada oma konto ja tarkvara vahelist ühendust:
![github-desktop](assets/4.webp)
- Teid suunatakse automaatselt tagasi GitHub Desktop tarkvarasse. Klõpsake nupul `Lõpeta`: ![github-desktop](assets/5.webp)
- Kui olete just loonud oma GitHub'i konto, suunatakse teid lehele, mis näitab, et te pole veel ühtegi hoidlat loonud. Sel hetkel jätke GitHub Desktop tarkvara kõrvale; pöördume selle juurde hiljem tagasi: ![github-desktop](assets/6.webp)

## 2. samm: Installige Obsidian

Liikugem edasi kirjutustarkvara installimise juurde. Siin on teil mitu võimalust. Teil on vaja tarkvara, mis toetab Markdown-failide redigeerimist, kuna PlanB võrgustik kasutab seda formaati oma hoidla tekstifailides.
On olemas palju tarkvara, mis on spetsialiseerunud Markdown-failide redigeerimisele, nagu näiteks Typora, mis on loodud spetsiaalselt kirjutamiseks. Kuigi see ei ole ideaalne, on võimalik valida ka koodiredaktor, nagu Visual Studio Code (VSC) või Sublime Text. Siiski, kirjanikuna eelistan ma kasutada Obsidian tarkvara. Vaatame koos, kuidas seda installida ja alustada.
- Mine aadressile https://obsidian.md/download ja laadi alla tarkvara: ![github-desktop](assets/7.webp)
- Installi Obsidian, käivita tarkvara, vali oma keel ja seejärel klõpsa `Quick Start`: ![github-desktop](assets/8.webp)
- Jõuad Obsidian tarkvarasse. Praegu sul pole avatud ühtegi faili: ![github-desktop](assets/9.webp)

## 3. samm: Tee PlanB Network repositoriost fork

- Mine PlanB Network andmerepositori aadressile: [https://github.com/PlanB-Network/bitcoin-educational-content](https://github.com/PlanB-Network/bitcoin-educational-content): ![github-desktop](assets/10.webp)
- Sellelt lehelt klõpsa akna paremas ülanurgas asuval `Fork` nupul: ![github-desktop](assets/11.webp)
- Loomismenüüs võid jätta vaikeseaded. Veendu, et `Copy the dev branch only` kast on märgitud, seejärel klõpsa `Create fork` nupul: ![github-desktop](assets/12.webp)
- Seejärel jõuad oma PlanB Network repositori forki: ![github-desktop](assets/13.webp)
See fork on eraldi repositorium originaalist, kuigi praegu sisaldab see sama andmeid. Nüüd hakkad töötama selle uue repositoriumiga.

Oleme omamoodi teinud koopia PlanB Network allikarepositoriumist. Sinu fork (koopia) ja originaalrepositorium hakkavad nüüd arenema sõltumatult üksteisest. Originaalrepositoriumis võivad teised kaastöötajad lisada uusi andmeid, samal ajal kui sina oma forkis tegeled oma muudatustega.
Nende kahe repositoriumi järjepidevuse säilitamiseks on vajalik neid perioodiliselt sünkroniseerida, et nad saaksid sama informatsiooni. Oma muudatuste saatmiseks allikarepositoriumisse kasutad nn **Pull Request**. Ja allikarepositoriumist muudatuste integreerimiseks oma forki kasutad GitHubi veebiliidesel saadaolevat **Sync fork** käsku.
![github-desktop](assets/14.webp)

## 4. samm: Kloonige fork

- Naase GitHub Desktop tarkvarasse. Praeguseks peaks sinu fork ilmuma `Your repositories` sektsiooni. Kui sa seda kohe ei näe, kasuta nimekirja värskendamiseks topelt noole nuppu. Kui sinu fork ilmub, klõpsa sellel, et see valida:
![github-desktop](assets/15.webp)
- Seejärel klõpsa sinisel nupul: `Clone [username]/bitcoin-educational-content`:
![github-desktop](assets/16.webp)
- Jäta vaikimisi tee. Kinnitamiseks klõpsa sinisel `Clone` nupul:
![github-desktop](assets/17.webp)
- Oota, kuni GitHub Desktop kloonib sinu forki kohalikult:
![github-desktop](assets/18.webp)
- Pärast repositoriumi kloonimist pakub tarkvara sulle kahte võimalust. Sa pead valima esimese: `To contribute to the parent project`. See valik võimaldab sul esitada oma tulevase töö panusena vanemprojekti (`PlanB-Network/bitcoin-educational-content`), mitte ainult kui muudatusi sinu isiklikus forkis (`[username]/bitcoin-educational-content`). Kui valik on tehtud, klõpsa `Continue`:
![github-desktop](assets/19.webp)- Teie GitHub Desktop on nüüd õigesti seadistatud. Nüüd võite tarkvara taustal avatuna hoida, et jälgida meie poolt tehtavaid muudatusi.
![github-desktop](assets/20.webp)
Sellel etapil oleme saavutanud teie repositooriumi kohaliku koopia loomise, mis on majutatud GitHubis. Meeldetuletuseks, see repositoorium on PlanB Networki allika repositooriumi fork. Teil on võimalik teha muudatusi selles kohalikus koopias, nagu lisada õpetusi, tõlkeid või parandusi. Kui need muudatused on tehtud, kasutate **Push origin** käsku, et saata oma kohalikud muudatused teie GitHubis majutatud forki.

Samuti on võimalik hankida muudatusi forkist, näiteks sünkroniseerimise ajal PlanB Networki repositooriumiga. Selleks kasutate **Fetch origin** käsku, et laadida muudatused alla oma kohalikku koopiasse (teie kloon), ja seejärel **Pull origin** käsku, et ühendada need oma tööga. See võimaldab teil püsida kursis projekti viimaste arengutega, samal ajal efektiivselt kaasa aidates.

![github-desktop](assets/21.webp)
## 5. samm: Loo uus Obsidiani seif

- Ava Obsidiani tarkvara ja klõpsa akna vasakus alanurgas väikesele seifi ikoonile:
![github-desktop](assets/22.webp)
- Klõpsa `Open` nupule, et avada olemasolev kaust seifina: ![github-desktop](assets/23.webp)
- Sinu failihaldur avaneb. Peate leidma ja valima kausta pealkirjaga `GitHub`, mis peaks asuma teie `Documents` kataloogis teie failide seas. See tee vastab sellele, mille määrasite 4. sammus. Pärast kausta valimist kinnitage selle valik. Teie seifi loomine Obsidianis käivitub seejärel tarkvara uuel lehel:

![github-desktop](assets/24.webp)
-> **Tähelepanu**, on oluline mitte valida `bitcoin-educational-content` kausta, kui loote Obsidianis uut seifi. Selle asemel valige emakaust, `GitHub`. Kui valite `bitcoin-educational-content` kausta, siis konfiguratsioonikaust `.obsidian`, mis sisaldab teie kohalikke Obsidiani seadeid, integreeritakse automaatselt repositooriumisse. Tahame seda vältida, kuna pole vajalik edastada teie Obsidiani seadistusi PlanB Networki repositooriumisse. Alternatiivina võib `.obsidian` kausta lisada `.gitignore` faili, kuid see meetod muudaks ka allika repositooriumi `.gitignore` faili, mis ei ole soovitav.

- Akna vasakul küljel näete failipuud oma erinevate GitHubi repositooriumitega, mis on kohalikult kloonitud.
- Klõpsates kaustade nimede kõrval olevatele nooltele, saate neid laiendada, et pääseda juurde repositooriumite alamkaustadele ja nende dokumentidele:
![github-desktop](assets/25.webp)
- Ärge unustage seadistada Obsidiani tumedasse režiimi: "Valgus meelitab ligi putukaid" ;)

## 6. samm: Paigalda koodiredaktor

Enamik teie muudatustest toimub Markdown formaadis failides (`.md`). Nende dokumentide redigeerimiseks võite kasutada Obsidiani, tarkvara, millest me varem rääkisime. Siiski, PlanB Network kasutab teisi failiformaate ja mõningaid neist peate muutma.

Näiteks uue õpetuse loomisel peate looma YAML (`.yml`) faili, et sisestada oma õpetuse märksõnad, pealkiri ja õpetaja ID. Obsidian ei paku võimalust seda tüüpi failide muutmiseks, seega on teil vaja koodiredaktorit.
Selleks on teil mitmeid võimalusi. Kuigi arvuti tavalist märkmikku saab nende muudatuste tegemiseks kasutada, ei ole see lahendus korraliku töö jaoks ideaalne. Soovitan valida spetsiaalselt selleks otstarbeks loodud tarkvara, nagu [VS Code](https://code.visualstudio.com/download) või [Sublime Text](https://www.sublimetext.com/download). Sublime Text, olles eriti kergekaaluline, on meie vajadusteks enam kui piisav. - Installige üks neist tarkvaradest ja hoidke see oma tulevaste muudatuste jaoks kõrvale. ![github-desktop](assets/26.webp)
Palju õnne! Teie töökeskkond on nüüd seadistatud, et panustada PlanB Networki. Nüüd saate uurida meie teisi spetsiifilisi õpetusi iga panuse tüübi kohta (tõlkimine, toimetamine, kirjutamine.

https://planb.network/tutorials/others

..).
