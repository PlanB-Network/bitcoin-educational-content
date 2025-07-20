---
name: Dodajte događaj na PlanB Network
description: Kako da predložim dodavanje novog događaja na PlanB Network?
---
![event](assets/cover.webp)


Misija PlanB-a je da obezbedi vrhunske obrazovne resurse o Bitcoin na što više jezika. Sav sadržaj objavljen na sajtu je otvorenog koda i hostovan na GitHub-u, pružajući svakome priliku da doprinese obogaćivanju platforme.


Ako želite da dodate Bitcoin konferenciju na sajt PlanB Network i povećate vidljivost vašeg događaja, ali ne znate kako? Ovaj vodič je za vas!

![event](assets/01.webp)


- Prvo, potrebno je da imate nalog na GitHub-u. Ako ne znate kako da kreirate nalog, napravili smo detaljan vodič da vas uputimo.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Idite na [GitHub repozitorijum PlanB posvećen podacima](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) u sekciji `resources/conference/`:

![event](assets/02.webp)


- Kliknite u gornjem desnom uglu na dugme `Add file`, zatim na `Create new file`:

![event](assets/03.webp)


- Ako nikada ranije niste doprineli sadržaju PlanB Network-a, biće potrebno da kreirate svoj Fork originalnog repozitorijuma. Forkovanje repozitorijuma znači kreiranje kopije tog repozitorijuma na vašem GitHub nalogu, što vam omogućava da radite na projektu bez uticaja na originalni repozitorijum. Kliknite na dugme `Fork this repository`:

![event](assets/04.webp)


- Zatim ćete stići na GitHub stranicu za uređivanje:

![event](assets/05.webp)


- Kreirajte fasciklu za vašu konferenciju. Da biste to uradili, u polje `Name your file...` napišite ime vaše konferencije malim slovima sa crticama umesto razmaka. Na primer, ako se vaša konferencija zove "Paris Bitcoin Conference", treba da zabeležite `paris-Bitcoin-conference`. Takođe dodajte godinu vaše konferencije, na primer: `paris-Bitcoin-conference-2024`:

![event](assets/06.webp)


- Da biste potvrdili kreiranje fascikle, jednostavno zabeležite kosu crtu nakon vašeg imena u istom polju, na primer: `paris-Bitcoin-conference-2024/`. Dodavanje kose crte automatski kreira fasciklu umesto fajla:

![event](assets/07.webp)


- U ovom folderu, kreiraćete prvi YAML fajl pod nazivom `events.yml`:

![event](assets/08.webp)


- Ispunite ovu datoteku informacijama o vašoj konferenciji koristeći ovaj šablon:


```yaml
start_date:
end_date:
address_line_1:
address_line_2:
address_line_3:
name:
builder:
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description:
language:
-
links:
website:
replay_url:
live_url :
tags:
-
```


Na primer, vaš YAML fajl može izgledati ovako:


```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2:
address_line_3:
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants each year!
language:
- fr
- en
- es
- it
links:
website: https://paris.bitcoin.fr/conference
replay_url:
live_url :
tags:
- Bitcoiner
- General
- International
```

![event](assets/09.webp)

Ako još uvek nemate "*builder*" identifikator za vašu organizaciju, možete ga dodati prateći ovaj drugi vodič.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- Kada završite sa izmenama u ovoj datoteci, sačuvajte ih klikom na dugme `Commit changes...`:

![event](assets/10.webp)


- Dodajte naslov za svoje izmene, kao i kratak opis:

![event](assets/11.webp)


- Kliknite na dugme Green `Predloži izmene`:

![event](assets/12.webp)


- Zatim ćete stići na stranicu koja sumira sve vaše promene:

![event](assets/13.webp)


- Kliknite na svoju GitHub profilnu sliku u gornjem desnom uglu, zatim na `Your Repositories`:

![event](assets/14.webp)


- Odaberite svoj Fork iz PlanB Network repozitorijuma:

![event](assets/15.webp)


- Trebalo bi da vidite obaveštenje na vrhu prozora sa vašom novom granom. Verovatno se zove `patch-1`. Kliknite na njega:

![event](assets/16.webp)


- Sada ste na svojoj radnoj grani:

![event](assets/17.webp)


- Vratite se u fasciklu `resources/conference/` i izaberite fasciklu vaše konferencije koju ste upravo kreirali u prethodnom commitu:

![event](assets/18.webp)


- U fascikli vaše konferencije, kliknite na dugme `Add file`, zatim na `Create new file`:

![event](assets/19.webp)


- Nazovite ovu novu fasciklu `assets` i potvrdite njeno kreiranje stavljanjem kosa crta `/` na kraj:

![event](assets/20.webp)


- U ovom folderu `assets`, kreiraj fajl pod nazivom `.gitkeep`:

![event](assets/21.webp)


- Kliknite na dugme `Commit changes...`:

![event](assets/22.webp)


- Ostavite naslov commita kao podrazumevani, i proverite da je opcija `Commit directly to the patch-1 branch` označena, zatim kliknite na `Commit changes`:

![event](assets/23.webp)


- Vratite se u fasciklu `assets`:

![event](assets/24.webp)


- Kliknite na dugme `Add file`, zatim na `Upload files`: ![event](assets/25.webp)
- Otvorit će se nova stranica. Prevucite i otpustite sliku koja predstavlja vašu konferenciju i koja će biti prikazana na PlanB Network sajtu:

![event](assets/26.webp)


- To može biti logo, sličica ili čak poster:

![event](assets/27.webp)


- Kada se slika otpremi, proverite da li je polje `Commit directly to the patch-1 branch` označeno, zatim kliknite na `Commit changes`:

![event](assets/28.webp)


- Budite pažljivi, vaša slika mora biti nazvana `thumbnail` i mora biti u `.webp` formatu. Puno ime fajla treba da bude: `thumbnail.webp`:

![event](assets/29.webp)


- Vratite se u svoj folder `assets` i kliknite na posrednički fajl `.gitkeep`:

![event](assets/30.webp)


- Kada ste na datoteci, kliknite na 3 male tačke u gornjem desnom uglu, a zatim na `Obriši datoteku`:

![event](assets/31.webp)


- Potvrdite da ste i dalje na istoj radnoj grani, zatim kliknite na dugme `Commit changes`:

![event](assets/32.webp)


- Dodajte naslov i opis vašoj izmeni, zatim kliknite na `Commit changes`:

![event](assets/33.webp)


- Vratite se na koren vašeg repozitorijuma:

![event](assets/34.webp)


- Trebalo bi da vidite poruku koja ukazuje da je vaša grana pretrpela promene. Kliknite na dugme `Compare & pull request`:

![event](assets/35.webp)


- Dodajte jasan naslov i opis svom PR-u:

![event](assets/36.webp)


- Kliknite na dugme `Create pull request`:

![event](assets/37.webp)

Čestitamo! Vaš PR je uspešno kreiran. Administrator će ga sada proveriti i, ako je sve u redu, spojiti ga u glavni repozitorijum PlanB Network-a. Trebalo bi da vidite vaš događaj na sajtu nekoliko dana kasnije.


Obavezno pratite napredak vašeg PR-a. Administrator može ostaviti komentar tražeći dodatne informacije. Sve dok vaš PR nije validiran, možete ga pregledati u kartici `Pull requests` na PlanB Network GitHub repozitorijumu:

![event](assets/38.webp)

Hvala vam puno na vašem dragocenom doprinosu! :)