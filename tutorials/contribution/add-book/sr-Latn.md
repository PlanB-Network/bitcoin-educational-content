---
name: Dodavanje knjige u PlanB mrežu
description: Kako dodati novu knjigu na PlanB Network?
---
![book](assets/cover.webp)


Misija PlanB-a je da obezbedi vrhunske obrazovne resurse o Bitcoin na što više jezika. Sav sadržaj objavljen na sajtu je otvorenog koda i hostovan na GitHub-u, omogućavajući svakome da doprinese obogaćivanju platforme.


**Želite li dodati knjigu vezanu za Bitcoin na sajt PlanB Network i povećati vidljivost svog rada, ali ne znate kako? Ovaj vodič je za vas!**

![book](assets/01.webp)


- Prvo, potrebno je da imate GitHub nalog. Ako ne znate kako da kreirate nalog, napravili smo detaljan vodič da vas uputimo.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Idite na [GitHub repozitorijum PlanB posvećen podacima](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/books) u sekciji `resources/books/`:

![book](assets/02.webp)


- Kliknite u gornjem desnom uglu na dugme `Add file`, zatim na `Create new file`:

![book](assets/03.webp)


- Ako nikada ranije niste doprineli sadržaju PlanB Network-a, biće potrebno da kreirate svoj Fork originalnog repozitorijuma. Forkovanje repozitorijuma znači kreiranje kopije tog repozitorijuma na vašem GitHub nalogu, što vam omogućava da radite na projektu bez uticaja na originalni repozitorijum. Kliknite na dugme `Fork this repository`:

![book](assets/04.webp)


- Zatim ćete stići na GitHub stranicu za uređivanje:

![book](assets/05.webp)


- Kreirajte fasciklu za svoju knjigu. Da biste to uradili, u polje `Name your file...` upišite naziv vaše knjige malim slovima sa crticama umesto razmaka. Na primer, ako se vaša knjiga zove "*My Bitcoin Book*", trebali biste napisati `my-Bitcoin-book`:

![book](assets/06.webp)


- Da biste potvrdili kreiranje fascikle, jednostavno dodajte kosu crtu nakon naziva vaše knjige u istom polju, na primer: `my-Bitcoin-book/`. Dodavanje kose crte automatski kreira fasciklu umesto fajla:

![book](assets/07.webp)


- U ovom folderu, kreiraćete prvi YAML fajl pod nazivom `book.yml`:

![book](assets/08.webp)


- Popunite ovu datoteku informacijama o vašoj knjizi koristeći ovaj šablon:


```yaml
author:
level:
tags:
-
-
```


Evo detalja za popunjavanje svakog polja:


- `autor`**: Indikujte ime autora knjige.
- `nivo`**: Naznačite potreban nivo da biste mogli dobro čitati i razumeti knjigu. Izaberite nivo među sledećim:
 - `početnik`
 - `srednji`
- `napredni` - `ekspert`
- `tags`**: Dodajte dve ili tri oznake povezane sa vašom knjigom. Na primer:
    - `Bitcoin`
    - `istorija`
    - `tehnologija`
    - `privreda`
    - `obrazovanje`...


Na primer, vaša YAML datoteka može izgledati ovako:


```yaml
author: Loïc Morel
level: beginner
tags:
- bitcoin
- technology
```


![book](assets/09.webp)


- Kada završite sa izmenama u ovoj datoteci, sačuvajte ih klikom na dugme `Commit changes...`:

![book](assets/10.webp)


- Dodajte naslov za vaše izmene, kao i kratak opis:

![book](assets/11.webp)


- Kliknite na dugme Green `Predloži izmene`:

![book](assets/12.webp)


- Zatim ćete doći na stranicu koja sumira sve vaše promene:

![book](assets/13.webp)


- Kliknite na svoju GitHub profilnu sliku u gornjem desnom uglu, zatim na `Your Repositories`:

![book](assets/14.webp)


- Odaberite svoj Fork iz PlanB Network repozitorijuma:

![book](assets/15.webp)


- Trebalo bi da vidite obaveštenje na vrhu prozora sa vašom novom granom. Verovatno se zove `patch-1`. Kliknite na nju:

![book](assets/16.webp)


- Sada ste na svojoj radnoj grani:

![book](assets/17.webp)


- Vratite se u folder `resources/books/` i izaberite folder vaše knjige koji ste upravo kreirali u prethodnom commitu:

![book](assets/18.webp)


- U fascikli vaše knjige, kliknite na dugme `Add file`, zatim na `Create new file`:

![book](assets/19.webp)


- Nazovi ovu novu fasciklu `assets` i potvrdi njeno kreiranje stavljanjem kosa crta `/` na kraj:

![book](assets/20.webp)


- U ovom folderu `assets`, kreiraj fajl pod nazivom `.gitkeep`:

![book](assets/21.webp)


- Kliknite na dugme `Commit changes...`:

![book](assets/22.webp)


- Ostavite naslov commita kao podrazumevani, i proverite da je opcija `Commit directly to the patch-1 branch` označena, zatim kliknite na `Commit changes`:

![book](assets/23.webp)


- Vratite se u fasciklu `assets`:

![book](assets/24.webp)


- Kliknite na dugme `Add file`, zatim na `Upload files`:

![book](assets/25.webp)


- Otvorit će se nova stranica. Prevucite i otpustite naslovnu sliku vaše knjige u područje. Ova slika će biti prikazana na PlanB Network sajtu:

![book](assets/26.webp)


- Budite pažljivi, slika mora biti u formatu knjige, kako bi se najbolje prilagodila našem vebsajtu, na primer:

![book](assets/27.webp)


- Kada se slika otpremi, proverite da je polje `Commit directly to the patch-1 branch` označeno, zatim kliknite na `Commit changes`:

![book](assets/28.webp)- Please note, your image must be named `cover_en` if the cover is in English and must be in `.webp` format. Therefore, the complete file name should be `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, etc. If you wish to use a different cover image for each language, for example in the case of a book translation, you can place them in the same location in the `assets` folder:

![book](assets/29.webp)


- Vratite se u svoj folder `assets` i kliknite na međudatoteku `.gitkeep`:

![book](assets/30.webp)


- Kada otvorite datoteku, kliknite na 3 male tačke u gornjem desnom uglu, a zatim na `Delete file`:

![book](assets/31.webp)


- Uverite se da ste i dalje na istoj radnoj grani, zatim kliknite na dugme `Commit changes...`:

![book](assets/32.webp)


- Dodajte naslov i opis svom commitu, zatim kliknite na `Commit changes`:

![book](assets/33.webp)


- Vratite se u fasciklu vaše knjige:

![book](assets/34.webp)


- Kliknite na dugme `Add file`, zatim na `Create new file`:

![book](assets/35.webp)


- Kreirajte novu YAML datoteku tako što ćete je imenovati sa jezičkim indikatorom knjige. Ova datoteka će se koristiti za opis knjige. Na primer, ako želim da napišem svoj opis na engleskom, imenovaću ovu datoteku `en.yml`:

![book](assets/36.webp)


- Popunite ovu YAML datoteku koristeći ovaj predložak:

```yaml
title: ""
publication_year:
cover: cover_en.webp
original: true
description: |

contributors:
-
```


Evo detalja za popunjavanje svakog polja:


- `title`**: Naznačite naziv knjige u navodnicima.
- `publication_year`**: Naznačite godinu kada je knjiga objavljena.
- `cover`**: Naznačite naziv datoteke koja odgovara naslovnoj slici, u skladu sa jezikom YAML datoteke koju trenutno uređujete. Na primer, ako uređujete `en.yml` datoteku i prethodno ste dodali naslovnu sliku na engleskom jeziku pod nazivom `cover_en.webp`, jednostavno navedite `cover_en.webp` u ovom polju.
- `description`**: Dodajte kratak pasus koji opisuje knjigu. Opis mora biti na istom jeziku kao što je navedeno u naslovu YAML datoteke.
- `contributors`**: Dodajte svoj ID saradnika ako ga imate.


Na primer, vaš YAML fajl može izgledati ovako:


```yaml