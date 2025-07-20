---
name: Dodavanje podkasta na PlanB mrežu
description: Kako dodati novi podcast na PlanB Network?
---
![podcast](assets/cover.webp)


Misija PlanB-a je da obezbedi vrhunske obrazovne resurse o Bitcoin na što više jezika. Sav sadržaj objavljen na sajtu je otvorenog koda i hostovan na GitHub-u, omogućavajući svakome da učestvuje u obogaćivanju platforme.


Da li želite da dodate Bitcoin podcast na PlanB Network sajt i povećate vidljivost vaše emisije, ali ne znate kako? Ovaj vodič je za vas!

![podcast](assets/01.webp)


- Prvo, potrebno je da imate GitHub nalog. Ako ne znate kako da ga kreirate, napravili smo detaljan vodič da vas uputimo.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Idite na [GitHub repozitorijum PlanB posvećen podacima](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/podcasts) u sekciji `resources/podcasts/`:

![podcast](assets/02.webp)


- Kliknite u gornjem desnom uglu na dugme `Add file`, zatim na `Create new file`:

![podcast](assets/03.webp)


- Ako nikada ranije niste doprineli sadržaju PlanB Network-a, biće potrebno da kreirate svoj Fork originalnog repozitorijuma. Forkovanje repozitorijuma znači kreiranje kopije tog repozitorijuma na vašem GitHub nalogu, što vam omogućava da radite na projektu bez uticaja na originalni repozitorijum. Kliknite na dugme `Fork this repository`:

![podcast](assets/04.webp)


- Zatim ćete stići na GitHub stranicu za uređivanje:

![podcast](assets/05.webp)


- Kreirajte fasciklu za vaš podcast. Da biste to uradili, u polje `Name your file...` upišite naziv vašeg podcasta malim slovima sa crticama umesto razmaka. Na primer, ako se vaša emisija zove "Super Podcast Bitcoin", treba da napišete `super-podcast-Bitcoin`:

![podcast](assets/06.webp)


- Da biste potvrdili kreiranje fascikle, jednostavno dodajte kosu crtu nakon imena vašeg podkasta u istom polju, na primer: `super-podcast-Bitcoin/`. Dodavanje kose crte automatski kreira fasciklu umesto fajla:

![podcast](assets/07.webp)


- U ovom folderu, kreiraćete prvi YAML fajl pod nazivom `podcast.yml`:

![podcast](assets/08.webp)


- Popunite ovu datoteku informacijama o svom podcastu koristeći ovaj predložak:


```yaml
name:
host:
language:
links:
podcast:
twitter:
website:
description: |

tags:
-
-
contributors:
-
```


Evo detalja koje treba uneti za svako polje:



- `name`**: Naznačite ime vašeg podkasta.
- `host`**: Navedite imena ili pseudonime govornika ili voditelja podkasta. Svako ime treba biti odvojeno zarezom.
- `language`**: Označite kod jezika koji se govori u vašem podcastu. Na primer, za engleski, navedite `en`, za italijanski `it`...



- `linkovi`**: Pružite linkove ka vašem sadržaju. Imate dve opcije:
 - `podcast`: link ka vašem podcastu,
 - `twitter`: link ka Twitter profilu podkasta ili organizacije koja ga proizvodi,
 - `website`: link ka vebsajtu podkasta ili organizacije koja ga proizvodi.



- `description`**: Dodajte kratak pasus koji opisuje vaš podkast. Opis mora biti na istom jeziku kao što je navedeno u polju `language:`.



- `oznake`**: Dodajte dve oznake povezane sa vašim podkastom. Primeri:
    - `Bitcoin`
    - `tehnologija`
    - `ekonomija`
    - `obrazovanje`...



- `contributors`**: Navedite svoj ID saradnika ako ga imate.


Na primer, vaš YAML fajl može izgledati ovako:


```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
twitter: https://twitter.com/decouvrebitcoin
website: https://decouvrebitcoin.fr
description: |
Super Podcast Bitcoin is a technical LIVE session held once a week on Twitter to delve deep into the Bitcoin protocol, layer two solutions, and all things that blow minds. Our hosts Lounes, Pantamis, Loïc, and Sosthene will answer your questions and offer the most technical show on Bitcoin in the world.

tags:
- bitcoin
- technology
contributors:
- rabbit-hole
```


![podcast](assets/09.webp)



- Kada završite sa izmenama u ovoj datoteci, sačuvajte ih klikom na dugme `Commit changes...`:

![podcast](assets/10.webp)


- Dodajte naslov za vaše izmene, kao i kratak opis:

![podcast](assets/11.webp)


- Kliknite na dugme Green `Predloži izmene`:

![podcast](assets/12.webp)


- Zatim ćete stići na stranicu koja rezimira sve vaše promene:

![podcast](assets/13.webp)


- Kliknite na svoju GitHub profilnu sliku u gornjem desnom uglu, zatim na `Your Repositories`:

![podcast](assets/14.webp)


- Odaberite svoj Fork iz PlanB Network repozitorijuma:

![podcast](assets/15.webp)


- Trebalo bi da vidite obaveštenje na vrhu prozora sa vašom novom granom. Verovatno se zove `patch-1`. Kliknite na nju:

![podcast](assets/16.webp)


- Sada ste na svojoj radnoj grani:

![podcast](assets/17.webp)


- Vratite se u folder `resources/podcast/` i izaberite folder podcasta koji ste upravo kreirali u prethodnom commitu: ![podcast](assets/18.webp)
- U vašem folderu za podkaste, kliknite na dugme `Add file`, zatim na `Create new file`:

![podcast](assets/19.webp)


- Nazovi ovaj novi folder `assets` i potvrdi njegovo kreiranje dodavanjem kosa crta `/` na kraju:

![podcast](assets/20.webp)


- U ovom folderu `assets`, kreiraj fajl nazvan `.gitkeep`:

![podcast](assets/21.webp)


- Kliknite na dugme `Commit changes...`:

![podcast](assets/22.webp)


- Ostavite naslov commita kao podrazumevani, i proverite da je opcija `Commit directly to the patch-1 branch` označena, zatim kliknite na `Commit changes`:

![podcast](assets/23.webp)


- Vratite se u fasciklu `assets`:

![podcast](assets/24.webp)


- Kliknite na dugme `Add file`, zatim na `Upload files`:

![podcast](assets/25.webp)


- Otvoriće se nova stranica. Prevucite i otpustite logo svog podkasta u taj prostor. Ova slika će biti prikazana na sajtu PlanB Network:

![podcast](assets/26.webp)


- Budite pažljivi, slika mora biti kvadratna, kako bi se najbolje uklopila na našu veb stranicu:

![podcast](assets/27.webp)


- Kada se slika otpremi, proverite da je polje `Commit directly to the patch-1 branch` označeno, zatim kliknite na `Commit changes`:

![podcast](assets/28.webp)


- Budite pažljivi, vaša slika mora biti nazvana `logo` i mora biti u `.webp` formatu. Puno ime fajla treba da bude: `logo.webp`:

![podcast](assets/29.webp)


- Vratite se u svoj folder `assets` i kliknite na međufajl `.gitkeep`:

![podcast](assets/30.webp)


- Kada ste na datoteci, kliknite na tri male tačke u gornjem desnom uglu, a zatim na `Obriši datoteku`:

![podcast](assets/31.webp)


- Potvrdite da ste i dalje na istoj radnoj grani, zatim kliknite na dugme `Commit changes`:

![podcast](assets/32.webp)


- Dodajte naslov i opis svom commitu, zatim kliknite na `Commit changes`:

![podcast](assets/33.webp)


- Vratite se na koren svog repozitorijuma:

![podcast](assets/34.webp)


- Trebalo bi da vidite poruku koja ukazuje da je vaša grana pretrpela promene. Kliknite na dugme `Compare & pull request`:

![podcast](assets/35.webp)


- Dodajte jasan naslov i opis svom PR-u:

![podcast](assets/36.webp)


- Kliknite na dugme `Create pull request`:

![podcast](assets/37.webp)

Čestitamo! Vaš PR je uspešno kreiran. Administrator će ga sada pregledati i, ako je sve u redu, spojiti ga u glavni repozitorijum PlanB Network-a. Trebalo bi da vidite vaš podcast na vebsajtu nekoliko dana kasnije.


Molimo vas da pratite napredak vašeg PR-a. Administrator može ostaviti komentar tražeći dodatne informacije. Sve dok vaš PR nije validiran, možete ga pregledati u kartici `Pull requests` na PlanB Network GitHub repozitorijumu:

![podcast](assets/38.webp)

Hvala vam puno na vašem dragocenom doprinosu! :)