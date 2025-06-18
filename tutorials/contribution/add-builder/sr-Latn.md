---
name: Dodavanje graditelja
description: Kako predložiti dodavanje novog graditelja na PlanB mreži?
---
![builder](assets/cover.webp)


Misija PlanB-a je da obezbedi vrhunske obrazovne resurse o Bitcoin, na što više jezika. Sav sadržaj objavljen na sajtu je otvorenog koda i hostovan na GitHub-u, što omogućava svakome da učestvuje u obogaćivanju platforme.


Želite li dodati novog Bitcoin "graditelja" na sajt PlanB Network i dati vidljivost svojoj kompaniji ili softveru, ali ne znate kako? Ovaj vodič je za vas!

![builder](assets/01.webp)


- Prvo, potrebno je da imate GitHub nalog. Ako ne znate kako da kreirate nalog, napravili smo detaljan vodič da vas uputimo.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Idite na [GitHub repozitorijum PlanB posvećen podacima](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/builders) u sekciji `resources/builder/`:

![builder](assets/02.webp)


- Kliknite u gornjem desnom uglu na dugme `Add file`, zatim na `Create new file`:

![builder](assets/03.webp)


- Ako nikada ranije niste doprineli sadržaju PlanB Network-a, biće potrebno da kreirate svoj Fork originalnog repozitorijuma. Forkovanje repozitorijuma znači kreiranje kopije tog repozitorijuma na vašem GitHub nalogu, što vam omogućava da radite na projektu bez uticaja na originalni repozitorijum. Kliknite na dugme `Fork this repository`:

![builder](assets/04.webp)


- Zatim ćete stići na GitHub stranicu za uređivanje:

![builder](assets/05.webp)


- Kreirajte fasciklu za vašu kompaniju. Da biste to uradili, u polje `Name your file...` upišite ime vaše kompanije malim slovima sa crticama umesto razmaka. Na primer, ako se vaša kompanija zove "Bitcoin Baguette", treba da napišete `Bitcoin-baguette`:

![builder](assets/06.webp)


- Da biste potvrdili kreiranje fascikle, jednostavno dodajte kosu crtu nakon vašeg imena u istom polju, na primer: `Bitcoin-baguette/`. Dodavanje kose crte automatski kreira fasciklu umesto fajla:

![builder](assets/07.webp)


- U ovom folderu, kreiraćete prvi YAML fajl pod nazivom `builder.yml`:

![builder](assets/08.webp)


- Popunite ovaj fajl informacijama o vašoj kompaniji koristeći ovaj šablon:


```yaml
name:

address_line_1:
address_line_2:
address_line_3:

language:
-

links:
website:
twitter:
Github:
youtube:
nostr:

tags:
-
-

category:
```


Evo šta treba uneti za svaki ključ:


- `name`: Ime vaše kompanije (obavezno);
- `Address` : Lokacija vašeg poslovanja (opcionalno);
- `language` : Zemlje u kojima vaše preduzeće posluje ili podržani jezici (opciono);
- `links` : Različiti zvanični linkovi vašeg poslovanja (opciono);
- `tags` : 2 termina koja kvalifikuju vaš posao (obavezno);
- `category` : Kategorija koja najbolje opisuje oblast u kojoj vaše preduzeće posluje među sledećim izborima:
 - `Wallet`,
 - `infrastruktura`,
 - `Exchange`,
 - `obrazovanje`,
 - `servis`,
 - `zajednice`,
 - `konferencija`,
 - `privatnost`,
 - `investicija`,
 - `node`,
 - `Mining`,
 - `vesti`,
 - `proizvođač`.


Na primer, vaša YAML datoteka može izgledati ovako:


```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3:

language:
- fr
- en

links:
website: https://bitcoin-baguette.com
twitter: https://twitter.com/bitcoinbaguette
Github:
youtube:
nostr:

tags:
- bitcoin
- education

category: education
```


![builder](assets/09.webp)


- Kada završite sa izmenama u ovoj datoteci, sačuvajte ih klikom na dugme `Commit changes...`:

![builder](assets/10.webp)


- Dodajte naslov za vaše izmene, zajedno sa kratkim opisom:

![builder](assets/11.webp)


- Kliknite na dugme Green `Propose changes`:

![builder](assets/12.webp)


- Zatim ćete doći na stranicu koja sumira sve vaše izmene:

![builder](assets/13.webp)


- Kliknite na svoju GitHub profilnu sliku u gornjem desnom uglu, zatim na `Your Repositories`:

![builder](assets/14.webp)


- Odaberite svoj Fork iz PlanB Network repozitorijuma:

![builder](assets/15.webp)


- Trebalo bi da vidite obaveštenje na vrhu prozora sa vašom novom granom. Verovatno se zove `patch-1`. Kliknite na njega:

![builder](assets/16.webp)


- Sada ste na svojoj radnoj grani (**proverite da li ste na istoj grani kao i vaše prethodne izmene, ovo je važno!**):

![builder](assets/17.webp)


- Vratite se u folder `resources/builders/` i izaberite folder vašeg poslovanja koji ste upravo kreirali u prethodnom commitu:

![builder](assets/18.webp)


- U fascikli vašeg poslovanja, kliknite na dugme `Add file`, zatim na `Create new file`:

![builder](assets/19.webp)


- Nazovi ovaj novi folder `assets` i potvrdi njegovo kreiranje stavljanjem kosa crta `/` na kraj:

![builder](assets/20.webp)


- U ovom folderu `assets`, kreiraj fajl pod nazivom `.gitkeep`:

![builder](assets/21.webp)


- Kliknite na dugme `Commit changes...`:

![builder](assets/22.webp)


- Ostavite naslov commita kao podrazumevani, i proverite da je opcija `Commit directly to the patch-1 branch` označena, zatim kliknite na `Commit changes`: ![builder](assets/23.webp)
- Vratite se u fasciklu `assets`:

![builder](assets/24.webp)


- Kliknite na dugme `Add file`, zatim na `Upload files`:

![builder](assets/25.webp)


- Otvorit će se nova stranica. Prevucite i ispustite sliku vaše kompanije ili vašeg softvera u područje. Ova slika će biti prikazana na PlanB Network sajtu:

![builder](assets/26.webp)


- Može biti logo ili ikonica:

![builder](assets/27.webp)


- Kada se slika otpremi, proverite da je polje `Commit directly to the patch-1 branch` označeno, zatim kliknite na `Commit changes`:

![builder](assets/28.webp)


- Budite pažljivi, vaša slika mora biti kvadratna, mora biti nazvana `logo`, i mora biti u `.webp` formatu. Puno ime datoteke treba da bude: `logo.webp`:

![builder](assets/29.webp)


- Vratite se u svoj folder `assets` i kliknite na međufajl `.gitkeep`:

![builder](assets/30.webp)


- Kada ste na datoteci, kliknite na tri male tačke u gornjem desnom uglu, a zatim na `Obriši datoteku`:

![builder](assets/31.webp)


- Potvrdite da ste i dalje na istoj radnoj grani, zatim kliknite na dugme `Commit changes`:

![builder](assets/32.webp)


- Dodajte naslov i opis vašoj izmeni, zatim kliknite na `Commit changes`:

![builder](assets/33.webp)


- Vrati se u fasciklu svoje kompanije:

![builder](assets/34.webp)


- Kliknite na dugme `Add file`, zatim na `Create new file`:

![builder](assets/35.webp)


- Kreirajte novu YAML datoteku tako što ćete je imenovati indikatorom vašeg maternjeg jezika. Ova datoteka će se koristiti za opis graditelja. Na primer, ako želim da napišem svoj opis na engleskom, imenovaću ovu datoteku `en.yml`:

![builder](assets/36.webp)


- Nažalost, ne mogu da popunim YAML datoteku bez dodatnih informacija. Molim vas da mi pružite više detalja ili sadržaj koji treba da bude uključen u YAML datoteku.

```yaml
description: |

contributors:
-
```



- Za ključ `contributors`, možete dodati svoj identifikator saradnika na PlanB Network ako ga imate. Ako nemate, ostavite ovo polje prazno.
- Za ključ `description`, jednostavno treba da dodate kratak pasus koji opisuje vašu kompaniju ili vaš softver. Opis mora biti na istom jeziku kao i naziv datoteke. Ne morate prevoditi ovaj opis na sve jezike koje sajt podržava, jer će PlanB timovi to učiniti koristeći njihov model. Na primer, ovako bi vaša datoteka mogla izgledati:

```yaml
description: |
Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.

contributors:
-
```

![builder](assets/37.webp)


- Kliknite na dugme `Commit changes`:

![builder](assets/38.webp)


- Osigurajte da je polje `Commit directly to the patch-1 branch` označeno, dodajte naslov, a zatim kliknite na `Commit changes`:

![builder](assets/39.webp)


- Vaš folder kompanije sada bi trebalo da izgleda ovako:

![builder](assets/40.webp)


- Ako vam sve odgovara, vratite se na koren vašeg Fork:

![builder](assets/41.webp)


- Trebalo bi da vidite poruku koja ukazuje da je vaša grana pretrpela promene. Kliknite na dugme `Compare & pull request`:

![builder](assets/42.webp)


- Dodajte jasan naslov i opis svom PR-u:

![builder](assets/43.webp)


- Kliknite na dugme `Create pull request`:

![builder](assets/44.webp)

Čestitamo! Vaš PR je uspešno kreiran. Administrator će ga sada pregledati i, ako je sve u redu, integrisati u glavni repozitorijum PlanB Network-a. Vaš profil graditelja bi trebalo da se pojavi na vebsajtu nekoliko dana kasnije.


Obavezno pratite napredak vašeg PR-a. Administrator može ostaviti komentar tražeći dodatne informacije. Dok vaš PR nije validiran, možete ga pregledati u kartici `Pull requests` na PlanB Network GitHub repozitorijumu:

![builder](assets/45.webp)

Hvala vam puno na vašem dragocenom doprinosu! :)